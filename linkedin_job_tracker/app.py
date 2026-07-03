"""Flask dashboard for the LinkedIn job tracker.

Run:  python app.py   then open http://127.0.0.1:5050
"""
from datetime import datetime, timedelta, timezone

from flask import Flask, jsonify, render_template, request

import config
import db

app = Flask(__name__)


def since(days: int) -> str:
    return (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")


def job_filters():
    """Build the WHERE clause shared by /api/jobs and /api/stats from query args."""
    clauses, params = [], []
    days = request.args.get("days", type=int)
    if days:
        clauses.append("first_seen >= ?")
        params.append(since(days))
    q = request.args.get("q", "").strip()
    if q:
        clauses.append("(title LIKE ? OR company LIKE ? OR location LIKE ?)")
        params.extend([f"%{q}%"] * 3)
    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    return where, params


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/jobs")
def api_jobs():
    where, params = job_filters()
    limit = min(request.args.get("limit", 200, type=int), 1000)
    with db.connect() as conn:
        rows = conn.execute(
            f"""SELECT job_id, title, company, location, posted_date, url, first_seen
                FROM jobs {where}
                ORDER BY first_seen DESC LIMIT ?""",
            (*params, limit),
        ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/stats")
def api_stats():
    where, params = job_filters()
    with db.connect() as conn:
        total = conn.execute(f"SELECT COUNT(*) FROM jobs {where}", params).fetchone()[0]
        companies = conn.execute(
            f"SELECT COUNT(DISTINCT company) FROM jobs {where}", params
        ).fetchone()[0]
        new_24h = conn.execute(
            "SELECT COUNT(*) FROM jobs WHERE first_seen >= ?", (since(1),)
        ).fetchone()[0]
        new_7d = conn.execute(
            "SELECT COUNT(*) FROM jobs WHERE first_seen >= ?", (since(7),)
        ).fetchone()[0]
        last_run = conn.execute(
            "SELECT started_at, finished_at, jobs_found, jobs_new, status "
            "FROM scrape_runs ORDER BY id DESC LIMIT 1"
        ).fetchone()
    return jsonify({
        "total": total,
        "companies": companies,
        "new_24h": new_24h,
        "new_7d": new_7d,
        "last_run": dict(last_run) if last_run else None,
    })


@app.route("/api/timeseries")
def api_timeseries():
    days = request.args.get("days", 14, type=int)
    with db.connect() as conn:
        rows = conn.execute(
            """SELECT substr(first_seen, 1, 10) AS day, COUNT(*) AS n
               FROM jobs WHERE first_seen >= ?
               GROUP BY day ORDER BY day""",
            (since(days),),
        ).fetchall()
    counts = {r["day"]: r["n"] for r in rows}
    today = datetime.now(timezone.utc).date()
    series = []
    for i in range(days - 1, -1, -1):
        d = (today - timedelta(days=i)).isoformat()
        series.append({"day": d, "n": counts.get(d, 0)})
    return jsonify(series)


@app.route("/api/top-companies")
def api_top_companies():
    where, params = job_filters()
    with db.connect() as conn:
        rows = conn.execute(
            f"""SELECT company, COUNT(*) AS n FROM jobs
                {where + (' AND ' if where else 'WHERE ')} company IS NOT NULL
                GROUP BY company ORDER BY n DESC, company LIMIT 8""",
            params,
        ).fetchall()
    return jsonify([dict(r) for r in rows])


if __name__ == "__main__":
    app.run(host=config.DASHBOARD_HOST, port=config.DASHBOARD_PORT, debug=False)
