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

GUEST_SEARCH_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}
JOB_ID_RE = re.compile(r"(\d+)")


def fetch_page(session: requests.Session, keywords: str, location: str,
               start: int, time_range: str) -> str | None:
    params = {
        "keywords": keywords,
        "location": location,
        "f_TPR": time_range,
        "start": start,
    }
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


def scrape_search(session: requests.Session, conn, keywords: str, location: str,
                  time_range: str) -> tuple[int, int]:
    found = new = 0
    print(f"Searching: '{keywords}' in '{location}' ({time_range})")
    for page in range(config.MAX_PAGES_PER_SEARCH):
        start = page * 10
        html = fetch_page(session, keywords, location, start, time_range)
        if html is None:
            break
        cards = parse_cards(html)
        if not cards:
            break
        for job in cards:
            job["search_keywords"] = keywords
            job["search_location"] = location
            found += 1
            if db.upsert_job(conn, job):
                new += 1
        print(f"  page {page + 1}: {len(cards)} jobs")
        time.sleep(random.uniform(*config.REQUEST_DELAY_SECONDS))
    return found, new


def run(time_range: str | None = None) -> int:
    time_range = time_range or config.TIME_RANGE
    total_found = total_new = 0
    with db.connect() as conn:
        run_id = db.start_run(conn)
        conn.commit()
        status = "ok"
        try:
            with requests.Session() as session:
                for search in config.SEARCHES:
                    found, new = scrape_search(
                        session, conn, search["keywords"], search["location"], time_range
                    )
                    total_found += found
                    total_new += new
                    conn.commit()
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
                conn.execute("UPDATE jobs SET first_seen = ?, last_seen = ? WHERE job_id = ?",
                             (stamp, stamp, job["job_id"]))
                n += 1
        db.finish_run(conn, run_id, 140, n, "demo")
    print(f"Loaded {n} demo jobs into {config.DB_PATH}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--backfill", action="store_true",
                        help="look back 7 days instead of the configured window")
    parser.add_argument("--demo", action="store_true",
                        help="insert sample data instead of scraping")
    args = parser.parse_args()
    if args.demo:
        load_demo_data()
        return 0
    return run("r604800" if args.backfill else None)


if __name__ == "__main__":
    sys.exit(main())
