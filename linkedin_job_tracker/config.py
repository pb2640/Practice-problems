"""Configuration for the LinkedIn job tracker.

Edit SEARCHES to control what gets scraped each day. Each entry is one
search that the scraper runs against LinkedIn's public (logged-out) job
search endpoint.
"""
from pathlib import Path

# --- What to search for -----------------------------------------------------
# keywords: the search box text. location: any location string LinkedIn accepts.
# time_range: how far back to look, in seconds ("r86400" = last 24 hours).
#   Use "r604800" (7 days) for the very first run so the dashboard starts with
#   a useful backlog, then leave it at r86400 for the daily cron.
SEARCHES = [
    {"keywords": "Data Engineer", "location": "United States"},
    {"keywords": "Senior Data Engineer", "location": "United States"},
    {"keywords": "Data Engineer", "location": "Remote"},
]

TIME_RANGE = "r86400"          # posted within the last 24h
MAX_PAGES_PER_SEARCH = 4       # LinkedIn returns ~10 cards per page
REQUEST_DELAY_SECONDS = (2, 5) # random polite delay between requests (min, max)

# --- Storage -----------------------------------------------------------------
DB_PATH = Path(__file__).resolve().parent / "data" / "jobs.db"

# --- Scheduler ---------------------------------------------------------------
DAILY_RUN_AT = "08:00"  # local time, HH:MM, used by scheduler.py

# --- Dashboard ---------------------------------------------------------------
DASHBOARD_HOST = "127.0.0.1"
DASHBOARD_PORT = 5050
