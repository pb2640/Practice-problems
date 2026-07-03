"""Scrape LinkedIn's public (logged-out) job search results into SQLite.

Uses the guest endpoint that powers linkedin.com/jobs for signed-out
visitors, so no credentials are involved. Be polite: keep the built-in
delays, run it once a day, and expect LinkedIn to rate-limit (HTTP 429)
if you hammer it. Scraping may be restricted by LinkedIn's Terms of
Service — this tool is for personal, low-volume job hunting.

Usage:
    python scraper.py              # run all searches from config.py
    python scraper.py --backfill   # first run: look back 7 days instead of 24h
    python scraper.py --demo       # load sample data to try the dashboard
"""
import argparse
import random
import re
import sys
import time

import requests
from bs4 import BeautifulSoup

import config
import db
import notify

GUEST_SEARCH_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
JOB_DETAIL_URL = "https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}
JOB_ID_RE = re.compile(r"(\d+)")


US_STATES = {
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID",
    "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
    "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV",
    "WI", "WY", "DC", "PR",
}


def location_is_us(loc: str | None) -> bool:
    """True if a scraped location string looks like the United States."""
    if not loc:
        return False
    low = loc.lower()
    if any(extra.lower() in low for extra in config.US_LOCATION_EXTRAS):
        return True
    # "City, ST" / "City, ST (Remote)" — check the piece after the last comma
    tail = loc.rsplit(",", 1)[-1].strip()
    tail = re.sub(r"\(.*\)", "", tail).strip()
    return tail.upper() in US_STATES


def fetch_page(session: requests.Session, search: dict,
               start: int, time_range: str) -> str | None:
    params = {
        "keywords": search["keywords"],
        "location": search["location"],
        "f_TPR": time_range,
        "start": start,
    }
    if search.get("geo_id"):
        params["geoId"] = search["geo_id"]
    if search.get("remote_only"):
        params["f_WT"] = "2"
    for attempt in range(3):
        resp = session.get(GUEST_SEARCH_URL, params=params, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.text
        if resp.status_code == 429:
            wait = 15 * (attempt + 1)
            print(f"  rate limited (429), waiting {wait}s...")
            time.sleep(wait)
            continue
        print(f"  unexpected status {resp.status_code} for start={start}, skipping page")
        return None
    return None


def parse_cards(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    jobs = []
    for card in soup.select("div.base-card, div.job-search-card"):
        urn = card.get("data-entity-urn", "")
        m = JOB_ID_RE.search(urn)
        if not m:
            continue
        title = card.select_one("h3.base-search-card__title")
        company = card.select_one("h4.base-search-card__subtitle")
        location = card.select_one("span.job-search-card__location")
        posted = card.select_one("time[datetime]")
        link = card.select_one("a.base-card__full-link")
        if not title:
            continue
        job_id = m.group(1)
        jobs.append({
            "job_id": job_id,
            "title": title.get_text(strip=True),
            "company": company.get_text(strip=True) if company else None,
            "location": location.get_text(strip=True) if location else None,
            "posted_date": posted["datetime"] if posted else None,
            "url": (link["href"].split("?")[0] if link and link.get("href")
                    else f"https://www.linkedin.com/jobs/view/{job_id}"),
        })
    return jobs


# --- Enrichment: description, skills, salary, seniority, match score --------

SKILL_RES = {name: re.compile(rx, re.I) for name, rx in config.SKILL_PATTERNS.items()}
SALARY_RE = re.compile(
    r"\$\s?(\d{2,3}(?:,\d{3})?(?:\.\d+)?)\s*([kK])?\s*(?:-|–|—|to)\s*"
    r"\$?\s?(\d{2,3}(?:,\d{3})?(?:\.\d+)?)\s*([kK])?"
)
SENIORITY_RULES = [
    (re.compile(r"\b(intern|junior|entry[- ]level)\b", re.I), "Entry"),
    (re.compile(r"\b(staff|principal|lead)\b", re.I), "Staff+"),
    (re.compile(r"\b(manager|director|head of)\b", re.I), "Manager"),
    (re.compile(r"\b(senior|sr\.?)\b", re.I), "Senior"),
]


def extract_skills(text: str) -> list[str]:
    return [name for name, rx in SKILL_RES.items() if rx.search(text)]


def match_score(job_skills: list[str]) -> int | None:
    """Share of the job's detected skills that are in MY_SKILLS, as 0-100."""
    if not job_skills:
        return None
    mine = {s.lower() for s in config.MY_SKILLS}
    hit = sum(1 for s in job_skills if s.lower() in mine)
    return round(100 * hit / len(job_skills))


def extract_salary(text: str) -> tuple[str | None, int | None, int | None]:
    m = SALARY_RE.search(text)
    if not m:
        return None, None, None

    def to_number(value: str, k: str | None) -> float:
        n = float(value.replace(",", ""))
        return n * 1000 if k else n

    lo, hi = to_number(m.group(1), m.group(2)), to_number(m.group(3), m.group(4))
    if lo >= 10_000 and hi >= lo:  # annual figures; hourly rates keep text only
        return m.group(0), int(lo), int(hi)
    return m.group(0), None, None


def detect_seniority(title: str) -> str:
    for rx, label in SENIORITY_RULES:
        if rx.search(title):
            return label
    return "Mid"


def fetch_detail(session: requests.Session, job_id: str) -> str | None:
    url = JOB_DETAIL_URL.format(job_id)
    for attempt in range(3):
        resp = session.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.text
        if resp.status_code == 429:
            time.sleep(15 * (attempt + 1))
            continue
        return None
    return None


def parse_description(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    node = soup.select_one("div.show-more-less-html__markup")
    return node.get_text("\n", strip=True) if node else ""


def enrich_jobs(session: requests.Session, conn, limit: int | None = None) -> int:
    """Fetch descriptions for jobs that don't have one yet and derive
    skills, salary, seniority, and the profile match score."""
    limit = limit or config.ENRICH_MAX_PER_RUN
    rows = conn.execute(
        """SELECT job_id, title FROM jobs
           WHERE description IS NULL AND job_id GLOB '[0-9]*'
           ORDER BY first_seen DESC LIMIT ?""",
        (limit,),
    ).fetchall()
    if not rows:
        return 0
    print(f"Fetching descriptions for {len(rows)} jobs...")
    done = 0
    for row in rows:
        html = fetch_detail(session, row["job_id"])
        if html is None:
            continue
        desc = parse_description(html)
        skills = extract_skills(f"{row['title']}\n{desc}")
        sal_text, sal_min, sal_max = extract_salary(desc)
        conn.execute(
            """UPDATE jobs SET description = ?, skills = ?, salary_text = ?,
               salary_min = ?, salary_max = ?, seniority = ?, match_score = ?
               WHERE job_id = ?""",
            (desc, "," + ",".join(skills) + "," if skills else "",
             sal_text, sal_min, sal_max,
             detect_seniority(row["title"]), match_score(skills), row["job_id"]),
        )
        done += 1
        if done % 10 == 0:
            conn.commit()
            print(f"  {done}/{len(rows)}")
        time.sleep(random.uniform(*config.REQUEST_DELAY_SECONDS))
    conn.commit()
    print(f"  enriched {done} jobs")
    return done


def scrape_search(session: requests.Session, conn, search: dict,
                  time_range: str) -> tuple[int, int]:
    found = new = skipped = 0
    tag = " (remote only)" if search.get("remote_only") else ""
    print(f"Searching: '{search['keywords']}' in '{search['location']}'{tag} ({time_range})")
    for page in range(config.MAX_PAGES_PER_SEARCH):
        start = page * 10
        html = fetch_page(session, search, start, time_range)
        if html is None:
            break
        cards = parse_cards(html)
        if not cards:
            break
        for job in cards:
            if config.US_ONLY and not location_is_us(job.get("location")):
                skipped += 1
                continue
            job["search_keywords"] = search["keywords"]
            job["search_location"] = search["location"]
            found += 1
            if db.upsert_job(conn, job):
                new += 1
        print(f"  page {page + 1}: {len(cards)} jobs")
        time.sleep(random.uniform(*config.REQUEST_DELAY_SECONDS))
    if skipped:
        print(f"  filtered out {skipped} non-US postings")
    return found, new


def run(time_range: str | None = None) -> int:
    time_range = time_range or config.TIME_RANGE
    total_found = total_new = 0
    run_started = db.utcnow()
    with db.connect() as conn:
        run_id = db.start_run(conn)
        conn.commit()
        status = "ok"
        try:
            with requests.Session() as session:
                for search in config.SEARCHES:
                    found, new = scrape_search(session, conn, search, time_range)
                    total_found += found
                    total_new += new
                    conn.commit()
                if config.FETCH_DESCRIPTIONS:
                    enrich_jobs(session, conn)
                matches = conn.execute(
                    """SELECT title, company, location, match_score, salary_text, url
                       FROM jobs WHERE first_seen >= ? AND match_score >= ?""",
                    (run_started, config.NOTIFY_MIN_MATCH),
                ).fetchall()
                notify.notify_new_matches([dict(m) for m in matches])
        except Exception as exc:  # record the failure, then re-raise
            status = f"error: {exc}"
            raise
        finally:
            db.finish_run(conn, run_id, total_found, total_new, status)
    print(f"Done: {total_found} jobs seen, {total_new} new.")
    return 0 if status == "ok" else 1


# --- Demo data so the dashboard can be tried without a live scrape ----------

def load_demo_data():
    from datetime import datetime, timedelta, timezone

    companies = ["Netflix", "Stripe", "Databricks", "Airbnb", "Snowflake", "Datadog",
                 "Robinhood", "Chime", "Plaid", "Instacart", "Reddit", "Figma"]
    titles = ["Data Engineer", "Senior Data Engineer", "Data Engineer II",
              "Staff Data Engineer", "Analytics Engineer", "Data Platform Engineer"]
    locations = ["New York, NY", "San Francisco, CA", "Seattle, WA", "Austin, TX",
                 "United States (Remote)", "Chicago, IL", "Boston, MA"]
    rng = random.Random(42)
    now = datetime.now(timezone.utc)
    n = 0
    with db.connect() as conn:
        run_id = db.start_run(conn)
        for i in range(140):
            days_ago = rng.betavariate(1.2, 2.5) * 14
            seen = now - timedelta(days=days_ago, minutes=rng.randint(0, 720))
            stamp = seen.strftime("%Y-%m-%dT%H:%M:%SZ")
            job = {
                "job_id": f"demo-{i}",
                "title": rng.choice(titles),
                "company": rng.choice(companies),
                "location": rng.choice(locations),
                "posted_date": seen.strftime("%Y-%m-%d"),
                "url": "https://www.linkedin.com/jobs/",
                "search_keywords": "Data Engineer",
                "search_location": "United States",
            }
            if db.upsert_job(conn, job):
                skills = rng.sample(sorted(config.SKILL_PATTERNS), k=rng.randint(3, 7))
                has_salary = rng.random() < 0.4
                lo = rng.randrange(120, 165, 5) * 1000 if has_salary else None
                hi = lo + rng.randrange(20, 50, 5) * 1000 if has_salary else None
                conn.execute(
                    """UPDATE jobs SET first_seen = ?, last_seen = ?, description = ?,
                       skills = ?, salary_text = ?, salary_min = ?, salary_max = ?,
                       seniority = ?, match_score = ? WHERE job_id = ?""",
                    (stamp, stamp,
                     "Sample posting looking for experience with " + ", ".join(skills) + ".",
                     "," + ",".join(skills) + ",",
                     f"${lo:,} - ${hi:,}" if has_salary else None, lo, hi,
                     detect_seniority(job["title"]), match_score(skills), job["job_id"]),
                )
                n += 1
        db.finish_run(conn, run_id, 140, n, "demo")
    print(f"Loaded {n} demo jobs into {config.DB_PATH}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--backfill", action="store_true",
                        help="look back 7 days instead of the configured window")
    parser.add_argument("--demo", action="store_true",
                        help="insert sample data instead of scraping")
    parser.add_argument("--enrich", action="store_true",
                        help="only fetch descriptions for jobs already in the DB")
    args = parser.parse_args()
    if args.demo:
        load_demo_data()
        return 0
    if args.enrich:
        with db.connect() as conn, requests.Session() as session:
            enrich_jobs(session, conn)
        return 0
    return run("r604800" if args.backfill else None)


if __name__ == "__main__":
    sys.exit(main())
