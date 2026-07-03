"""Alert on new high-match jobs after a scrape.

Two channels, both optional:
- Windows desktop toast (on by default, zero setup, Windows only)
- Email via SMTP (set NOTIFY_EMAIL in config.py and put the app password in
  the env var named by SMTP_PASSWORD_ENV)
"""
import os
import platform
import smtplib
import subprocess
from email.mime.text import MIMEText

import config


def notify_new_matches(jobs: list[dict]) -> None:
    """jobs: dicts with title, company, location, match_score, salary_text, url."""
    if not jobs:
        return
    jobs = sorted(jobs, key=lambda j: -(j.get("match_score") or 0))
    print(f"{len(jobs)} new jobs at or above {config.NOTIFY_MIN_MATCH}% match")
    if config.NOTIFY_WINDOWS_TOAST and platform.system() == "Windows":
        _toast(jobs)
    if config.NOTIFY_EMAIL:
        _email(jobs)


def _toast(jobs: list[dict]) -> None:
    top = jobs[0]
    title = f"{len(jobs)} new job match{'es' if len(jobs) > 1 else ''}"
    body = f"{top['match_score']}% {top['title']} @ {top['company']}"
    if len(jobs) > 1:
        body += f" (+{len(jobs) - 1} more)"
    # msg.exe isn't on Home editions; a WinRT toast via PowerShell works everywhere.
    script = (
        "[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, "
        "ContentType = WindowsRuntime] | Out-Null;"
        "$t = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent("
        "[Windows.UI.Notifications.ToastTemplateType]::ToastText02);"
        "$n = $t.GetElementsByTagName('text');"
        f"$n.Item(0).AppendChild($t.CreateTextNode({_ps_quote(title)})) | Out-Null;"
        f"$n.Item(1).AppendChild($t.CreateTextNode({_ps_quote(body)})) | Out-Null;"
        "[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("
        "'LinkedIn Job Tracker').Show([Windows.UI.Notifications.ToastNotification]::new($t))"
    )
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", script],
                       capture_output=True, timeout=20)
    except Exception as exc:
        print(f"  toast failed: {exc}")


def _ps_quote(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def _email(jobs: list[dict]) -> None:
    password = os.environ.get(config.SMTP_PASSWORD_ENV, "")
    if not password:
        print(f"  email skipped: set the {config.SMTP_PASSWORD_ENV} environment variable")
        return
    lines = []
    for j in jobs:
        salary = f" · {j['salary_text']}" if j.get("salary_text") else ""
        lines.append(f"{j.get('match_score')}%  {j['title']} — {j['company']}"
                     f" ({j.get('location', '?')}){salary}\n{j['url']}\n")
    msg = MIMEText("\n".join(lines))
    msg["Subject"] = f"{len(jobs)} new job match{'es' if len(jobs) > 1 else ''} " \
                     f"≥ {config.NOTIFY_MIN_MATCH}%"
    sender = config.SMTP_USER or config.NOTIFY_EMAIL
    msg["From"] = sender
    msg["To"] = config.NOTIFY_EMAIL
    try:
        with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT, timeout=30) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(msg)
        print(f"  emailed {config.NOTIFY_EMAIL}")
    except Exception as exc:
        print(f"  email failed: {exc}")
