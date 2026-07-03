# LinkedIn Job Tracker

Scrapes LinkedIn's **public (logged-out) job search** once a day, stores every
posting in SQLite, and serves a local dashboard to browse and filter them.
Built for a data-engineer job hunt — the default searches in `config.py` are
Data Engineer roles in the US and remote.

```
scraper.py    → fetches jobs from LinkedIn's guest search endpoint
db.py         → SQLite schema + upsert (dedupes by LinkedIn job id)
scheduler.py  → runs the scraper daily (or use cron, below)
app.py        → Flask dashboard at http://127.0.0.1:5050
config.py     → searches, schedule time, DB path
```

## Setup

```bash
cd linkedin_job_tracker
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## First run

```bash
python scraper.py --backfill   # look back 7 days to seed the DB
python app.py                  # open http://127.0.0.1:5050
```

No network / just want to see the dashboard? `python scraper.py --demo`
loads sample data.

## Daily scraping

**Option A — cron** (recommended on a machine/server that's always on):

```cron
0 8 * * * cd /path/to/linkedin_job_tracker && /path/to/.venv/bin/python scraper.py >> data/scrape.log 2>&1
```

**Option B — built-in scheduler** (no cron needed, keep the process running):

```bash
python scheduler.py --now   # scrapes immediately, then daily at config.DAILY_RUN_AT
```

## Customizing searches

Edit `SEARCHES` in `config.py`:

```python
SEARCHES = [
    {"keywords": "Data Engineer", "location": "United States"},
    {"keywords": "Analytics Engineer", "location": "New York, NY"},
]
```

`TIME_RANGE = "r86400"` limits results to jobs posted in the last 24 hours —
right for a daily cadence. Every run dedupes against the DB, so overlap
between runs is harmless.

Location targeting: each search pins LinkedIn's `geoId` for the US (free-text
locations are fuzzy-matched and can leak other countries), remote searches use
LinkedIn's remote filter (`f_WT=2`) rather than "Remote" as a location, and
`US_ONLY = True` drops any returned posting whose location string doesn't look
like the US. Searching another country? Set its `geo_id` and `US_ONLY = False`.

## Profile matching

After the search pass, the scraper fetches each new job's full description
(same public guest endpoint) and derives:

- **Skills** — matched against `SKILL_PATTERNS` in `config.py` (Spark,
  Airflow, dbt, Kafka, …)
- **Match score** — the share of a job's detected skills that appear in
  `MY_SKILLS`. **Edit `MY_SKILLS` in `config.py` to mirror your resume** —
  that's what powers the "Best match" sort.
- **Salary** — extracted from the description when the posting includes a range
- **Seniority** — Entry / Mid / Senior / Staff+ / Manager, from the title

Backfill descriptions for jobs already in the DB with `python scraper.py
--enrich` (it processes up to `ENRICH_MAX_PER_RUN` per call; rerun until done).

## Dashboard

- Stat tiles: jobs in view, new in 24h / this week, distinct companies
- Charts: new jobs per day, top companies, most in-demand skills
- Filters: text search (includes descriptions), time window, skill,
  newest-first or best-match ordering
- Table shows skills, salary, and match % per posting, each linking to the
  LinkedIn listing

## Notes & limits

- Uses the same endpoint LinkedIn serves to signed-out visitors — **no login,
  no credentials**. Automated access may still be restricted by LinkedIn's
  Terms of Service; keep this personal and low-volume. The scraper adds
  random 2–5 s delays and backs off on HTTP 429.
- LinkedIn caps guest search results (~40 per search per run with the default
  `MAX_PAGES_PER_SEARCH = 4`). For a daily 24-hour window that's usually
  plenty; add more specific searches rather than more pages.
- Data lives in `data/jobs.db` (gitignored). Delete it to start fresh.
