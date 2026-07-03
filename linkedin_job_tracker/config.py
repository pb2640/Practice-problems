"""Configuration for the LinkedIn job tracker.

Edit SEARCHES to control what gets scraped each day. Each entry is one
search that the scraper runs against LinkedIn's public (logged-out) job
search endpoint.
"""
from pathlib import Path

# --- What to search for -----------------------------------------------------
# keywords: the search box text. location: any location string LinkedIn accepts.
# geo_id: LinkedIn's internal location id — anchors the search far better than
#   the free-text location (which is fuzzy-matched and can leak other
#   countries). Find one by searching jobs on linkedin.com and copying the
#   geoId= value from the URL. remote_only: use LinkedIn's remote filter
#   (f_WT=2) instead of putting "Remote" in the location, which searches
#   worldwide.
US_GEO_ID = "103644278"

SEARCHES = [
    {"keywords": "Data Engineer", "location": "United States", "geo_id": US_GEO_ID},
    {"keywords": "Senior Data Engineer", "location": "United States", "geo_id": US_GEO_ID},
    {"keywords": "Data Engineer", "location": "United States", "geo_id": US_GEO_ID,
     "remote_only": True},
]

# Safety net: drop any scraped job whose location doesn't look like the US,
# even if LinkedIn returns it. Set to False if you add non-US searches.
US_ONLY = True
# Locations that don't end in a state code but should still count as US.
US_LOCATION_EXTRAS = ["United States", "Bay Area", "Greater Boston",
                      "New York City Metropolitan Area", "Washington DC"]

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
