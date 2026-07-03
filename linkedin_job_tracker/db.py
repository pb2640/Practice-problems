"""SQLite storage for scraped job postings."""
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone

import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    job_id          TEXT PRIMARY KEY,
    title           TEXT NOT NULL,
    company         TEXT,
    location        TEXT,
    posted_date     TEXT,
    url             TEXT,
    search_keywords TEXT,
    search_location TEXT,
    first_seen      TEXT NOT NULL,
    last_seen       TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_jobs_first_seen ON jobs (first_seen);
CREATE INDEX IF NOT EXISTS idx_jobs_company    ON jobs (company);

CREATE TABLE IF NOT EXISTS scrape_runs (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at  TEXT NOT NULL,
    finished_at TEXT,
    jobs_found  INTEGER DEFAULT 0,
    jobs_new    INTEGER DEFAULT 0,
    status      TEXT DEFAULT 'running'
);
"""


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@contextmanager
def connect():
    config.DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def upsert_job(conn, job: dict) -> bool:
    """Insert a job if unseen; refresh last_seen otherwise. Returns True if new."""
    now = utcnow()
    cur = conn.execute("SELECT 1 FROM jobs WHERE job_id = ?", (job["job_id"],))
    if cur.fetchone():
        conn.execute("UPDATE jobs SET last_seen = ? WHERE job_id = ?", (now, job["job_id"]))
        return False
    conn.execute(
        """INSERT INTO jobs (job_id, title, company, location, posted_date, url,
                             search_keywords, search_location, first_seen, last_seen)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            job["job_id"], job["title"], job.get("company"), job.get("location"),
            job.get("posted_date"), job.get("url"),
            job.get("search_keywords"), job.get("search_location"),
            now, now,
        ),
    )
    return True


def start_run(conn) -> int:
    cur = conn.execute("INSERT INTO scrape_runs (started_at) VALUES (?)", (utcnow(),))
    return cur.lastrowid


def finish_run(conn, run_id: int, found: int, new: int, status: str = "ok"):
    conn.execute(
        "UPDATE scrape_runs SET finished_at = ?, jobs_found = ?, jobs_new = ?, status = ? WHERE id = ?",
        (utcnow(), found, new, status, run_id),
    )
