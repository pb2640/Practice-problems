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

# --- Job descriptions & profile matching -------------------------------------
# After the search pass, fetch each new job's full description (same public
# guest endpoint, one request per job) to extract skills, salary, seniority,
# and a match score against MY_SKILLS.
FETCH_DESCRIPTIONS = True
ENRICH_MAX_PER_RUN = 80  # cap detail requests per run to stay low-volume

# Your skills — the match score is the share of a job's detected skills that
# appear here. Edit to mirror your resume; names must match SKILL_PATTERNS keys.
MY_SKILLS = ["Python", "SQL", "Spark", "Airflow", "Kafka", "Snowflake",
             "dbt", "AWS", "Docker", "Terraform"]

# Canonical skill -> case-insensitive regex used on the title + description.
SKILL_PATTERNS = {
    "Python": r"\bpython\b",
    "SQL": r"\bsql\b",
    "Spark": r"\b(?:py)?spark\b",
    "Airflow": r"\bairflow\b",
    "Kafka": r"\bkafka\b",
    "Snowflake": r"\bsnowflake\b",
    "dbt": r"\bdbt\b",
    "Databricks": r"\bdatabricks\b",
    "AWS": r"\baws\b|\bamazon web services\b",
    "Azure": r"\bazure\b",
    "GCP": r"\bgcp\b|\bgoogle cloud\b",
    "Redshift": r"\bredshift\b",
    "BigQuery": r"\bbigquery\b",
    "Kubernetes": r"\bkubernetes\b|\bk8s\b",
    "Docker": r"\bdocker\b",
    "Terraform": r"\bterraform\b",
    "Flink": r"\bflink\b",
    "Hadoop": r"\bhadoop\b",
    "Hive": r"\bhive\b",
    "Scala": r"\bscala\b",
    "Java": r"\bjava\b",
    "Kinesis": r"\bkinesis\b",
}

# --- Storage -----------------------------------------------------------------
DB_PATH = Path(__file__).resolve().parent / "data" / "jobs.db"

# --- Scheduler ---------------------------------------------------------------
DAILY_RUN_AT = "08:00"  # local time, HH:MM, used by scheduler.py

# --- Dashboard ---------------------------------------------------------------
DASHBOARD_HOST = "127.0.0.1"
DASHBOARD_PORT = 5050
