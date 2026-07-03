"""Run the scraper once a day at config.DAILY_RUN_AT (local time).

This is a zero-dependency alternative to cron for machines that stay on:

    python scheduler.py            # waits until the next run time, forever
    python scheduler.py --now      # also scrape immediately on startup

On servers, prefer a real cron entry (see README.md).
"""
import argparse
import time
from datetime import datetime, timedelta

import config
import scraper


def seconds_until_next_run() -> float:
    hh, mm = (int(x) for x in config.DAILY_RUN_AT.split(":"))
    now = datetime.now()
    nxt = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
    if nxt <= now:
        nxt += timedelta(days=1)
    return (nxt - now).total_seconds()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--now", action="store_true", help="scrape once immediately, then schedule")
    args = parser.parse_args()

    if args.now:
        safe_run()
    while True:
        wait = seconds_until_next_run()
        print(f"Next scrape at {config.DAILY_RUN_AT} (in {wait / 3600:.1f}h)")
        time.sleep(wait)
        safe_run()


def safe_run():
    try:
        scraper.run()
    except Exception as exc:
        print(f"Scrape failed: {exc}")


if __name__ == "__main__":
    main()
