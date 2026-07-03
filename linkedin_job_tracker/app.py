"""Flask dashboard for the LinkedIn job tracker.

Run:  python app.py   then open http://127.0.0.1:5050
"""
from datetime import datetime, timedelta, timezone

from flask import Flask, abort, jsonify, render_template, request

import config
import db

app = Flask(__name__)

STATUSES = ["applied", "referred", "interviewing", "offer", "rejected"]


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
        clauses.append("(title LIKE ? OR company LIKE ? OR location LIKE ? OR description LIKE ?)")
        params.extend([f"%{q}%"] * 4)
    skill = request.args.get("skill", "").strip()
    if skill:
        clauses.append("skills LIKE ?")
        params.append(f"%,{skill},%")
    status = request.args.get("status", "").strip()
    if status == "tracked":
        clauses.append("status IS NOT NULL AND status != ''")
    elif status:
        clauses.append("status = ?")
        params.append(status)
    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    return where, params


def skills_list(padded: str | None) -> list[str]:
    return [s for s in (padded or "").strip(",").split(",") if s]


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/jobs")
def api_jobs():
    where, params = job_filters()
    limit = min(request.args.get("limit", 200, type=int), 1000)
    order = ("match_score IS NULL, match_score DESC, first_seen DESC"
             if request.args.get("sort") == "match" else "first_seen DESC")
    with db.connect() as conn:
        rows = conn.execute(
            f"""SELECT job_id, title, company, location, posted_date, url, first_seen,
                       skills, salary_text, seniority, match_score, status, notes
                FROM jobs {where}
                ORDER BY {order} LIMIT ?""",
            (*params, limit),
        ).fetchall()
    jobs = []
    for r in rows:
        job = dict(r)
        job["skills"] = skills_list(job.pop("skills"))
        jobs.append(job)
    return jsonify(jobs)


@app.route("/api/top-skills")
def api_top_skills():
    from collections import Counter
    where, params = job_filters()
    with db.connect() as conn:
        rows = conn.execute(f"SELECT skills FROM jobs {where}", params).fetchall()
    counts = Counter(s for r in rows for s in skills_list(r["skills"]))
    return jsonify([{"skill": s, "n": n} for s, n in counts.most_common(10)])


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
        # Pipeline is deliberately unfiltered: your applications are your
        # applications regardless of the current dashboard view.
        pipeline = {s: 0 for s in STATUSES}
        for row in conn.execute(
            "SELECT status, COUNT(*) AS n FROM jobs "
            "WHERE status IS NOT NULL AND status != '' GROUP BY status"
        ):
            if row["status"] in pipeline:
                pipeline[row["status"]] = row["n"]
    return jsonify({
        "total": total,
        "companies": companies,
        "new_24h": new_24h,
        "new_7d": new_7d,
        "pipeline": pipeline,
        "last_run": dict(last_run) if last_run else None,
    })


@app.route("/api/jobs/<job_id>/status", methods=["POST"])
def api_set_status(job_id):
    body = request.get_json(silent=True) or {}
    status = (body.get("status") or "").strip().lower()
    if status and status not in STATUSES:
        abort(400, f"status must be empty or one of {STATUSES}")
    with db.connect() as conn:
        cur = conn.execute(
            "UPDATE jobs SET status = ?, status_updated = ?, "
            "notes = COALESCE(?, notes) WHERE job_id = ?",
            (status, db.utcnow(), body.get("notes"), job_id),
        )
        if cur.rowcount == 0:
            abort(404)
    return jsonify({"ok": True, "job_id": job_id, "status": status})


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
