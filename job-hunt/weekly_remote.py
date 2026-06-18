"""
weekly_remote.py — the automatic weekly piece (runs LOCALLY, nothing published).

A Windows Task Scheduler job runs this every Monday. It pulls the remote-jobs
feed (reusing sweep_remote.py), saves a dated file in sweep-logs/, and leaves a
reminder to run the full /job-sweep in Claude for the Pune web search.

Manual run:  python job-hunt/weekly_remote.py
"""

import datetime
import os

from sweep_remote import sweep_remote

HERE = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(HERE, "sweep-logs")
TIER_LABEL = {0: "Data Analyst", 1: "Analyst family", 2: "Skill match"}


def run():
    os.makedirs(LOGS, exist_ok=True)
    today = datetime.date.today().isoformat()
    jobs = sweep_remote()
    out_path = os.path.join(LOGS, f"remote-feed-{today}.md")

    lines = [
        f"# Weekly remote feed - {today}",
        "",
        f"Auto-run (Windows Task Scheduler). {len(jobs)} relevant remote jobs from the Remotive API.",
        "",
        "> For the full Pune + India web sweep, open Claude and run `/job-sweep`.",
        "",
    ]
    for j in jobs:
        loc = "India/Remote" if j["loc_rank"] == 0 else "Global Remote"
        skills = ", ".join(j["skills"]) or "-"
        lines.append(f"- **[{TIER_LABEL[j['tier']]}] {j['title']}** - {j['company']} ({loc})")
        lines.append(f"  - skills: {skills}")
        lines.append(f"  - {j['url']}")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote {out_path} ({len(jobs)} jobs). Run /job-sweep in Claude for the Pune web sweep.")


if __name__ == "__main__":
    run()
