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

## Dashboard

- Stat tiles: jobs in view, new in 24h / this week, distinct companies
- New jobs per day (last 14 days) and top-companies charts
- Search box + time-window filter over the full table of postings, each
  linking to the LinkedIn listing

## Notes & limits

- Uses the same endpoint LinkedIn serves to signed-out visitors — **no login,
  no credentials**. Automated access may still be restricted by LinkedIn's
  Terms of Service; keep this personal and low-volume. The scraper adds
  random 2–5 s delays and backs off on HTTP 429.
- LinkedIn caps guest search results (~40 per search per run with the default
  `MAX_PAGES_PER_SEARCH = 4`). For a daily 24-hour window that's usually
  plenty; add more specific searches rather than more pages.
- Data lives in `data/jobs.db` (gitignored). Delete it to start fresh.
