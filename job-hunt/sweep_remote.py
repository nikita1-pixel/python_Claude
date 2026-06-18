"""
sweep_remote.py — the REMOTE-jobs leg of the job-hunt sweep.

Why this exists (real-world): Pune local roles live on Naukri/LinkedIn (no free
API), so Claude web-searches those during a /job-sweep. THIS file covers the
other half — remote roles — by reusing the Remotive API client Nikita already
built for her Remote Job Market Analyzer. We don't rebuild the fetcher; we
import it and add a filter + ranking on top.

Run it on its own:  python job-hunt/sweep_remote.py
Or import it:       from sweep_remote import sweep_remote
"""

import os
import re
import sys

# fetch_jobs() lives in the sibling project folder, not here. Add that folder to
# Python's import path so we can reuse it instead of copy-pasting the code.
_HERE = os.path.dirname(os.path.abspath(__file__))
_FETCHER_DIR = os.path.join(_HERE, "..", "job-market-analyzer")
sys.path.insert(0, os.path.abspath(_FETCHER_DIR))

from fetch_jobs import fetch_jobs  # noqa: E402  (import after sys.path tweak)


# --- What counts as "a job for Nikita" -------------------------------------

# Title relevance tiers (Data Analyst first, then the analyst family, then any
# role her skills clearly match). Lowercased substrings.
EXACT_TITLES = ["data analyst"]
ANALYST_FAMILY = [
    "analyst", "analytics", "business intelligence", "bi developer",
    "data engineer", "data scientist", "reporting", "mis",
]

# Her skill set, pulled straight from the resume's TECHNICAL SKILLS section.
# Used to (a) catch skill-matched roles and (b) show WHICH skills hit.
SKILLS = [
    "python", "sql", "pandas", "sqlite", "excel", "power bi", "tableau",
    "matplotlib", "plotly", "streamlit", "jupyter", "cognos", "etl",
    "data cleaning", "eda", "statistics", "visualization", "dashboard",
    "rest api", "git",
]

# CORE data skills — a role only counts as a "skill match" if it needs one of
# these. Stops generic mentions of git/excel from flagging copywriter/sales
# jobs as relevant.
CORE_SKILLS = [
    "python", "sql", "pandas", "sqlite", "power bi", "tableau",
    "matplotlib", "plotly", "streamlit", "cognos", "etl", "eda",
]

# Location priority — India-remote beats global-remote.
INDIA_HINTS = ["india", "pune", "anywhere", "asia"]


def _text(job):
    """All the searchable text of one job, lowercased."""
    parts = [
        job.get("title", ""),
        job.get("category", ""),
        " ".join(job.get("tags", []) or []),
        job.get("description", ""),
    ]
    return " ".join(parts).lower()


def _has(skill, blob):
    """Whole-word match so 'git' doesn't match 'digital', 'sql' not 'mysql-ish'."""
    return re.search(r"\b" + re.escape(skill) + r"\b", blob) is not None


def matched_skills(job):
    """Which of Nikita's skills appear in this job (as whole words)."""
    blob = _text(job)
    return [s for s in SKILLS if _has(s, blob)]


def title_tier(job):
    """0 = exact Data Analyst, 1 = analyst family, 2 = skill-matched, 3 = no.

    Tier 2 needs a CORE data skill (Python/SQL/BI tool), not just a stray
    git/excel mention — that keeps copywriter/sales roles out.
    """
    title = job.get("title", "").lower()
    if any(t in title for t in EXACT_TITLES):
        return 0
    if any(t in title for t in ANALYST_FAMILY):
        return 1
    blob = _text(job)
    if any(_has(s, blob) for s in CORE_SKILLS):
        return 2
    return 3


def location_rank(job):
    """0 = India/anywhere, 1 = other remote. Lower is better (closer to Pune)."""
    loc = (job.get("candidate_required_location") or "").lower()
    return 0 if any(h in loc for h in INDIA_HINTS) else 1


def sweep_remote(min_tier=2):
    """
    Fetch remote jobs, keep the ones relevant to Nikita, and rank them.
    min_tier=2 keeps Data Analyst + analyst family + skill-matched roles.
    Returns a list of dicts sorted best-first.
    """
    jobs = fetch_jobs()
    results = []
    for job in jobs:
        tier = title_tier(job)
        if tier > min_tier:
            continue
        results.append({
            "title": job.get("title", ""),
            "company": job.get("company_name", ""),
            "location": job.get("candidate_required_location", "") or "Anywhere",
            "type": job.get("job_type", ""),
            "url": job.get("url", ""),
            "posted": job.get("publication_date", "")[:10],
            "tier": tier,
            "skills": matched_skills(job),
            "loc_rank": location_rank(job),
        })

    # Sort: best title tier first, then India-first, then most skill matches.
    results.sort(key=lambda j: (j["tier"], j["loc_rank"], -len(j["skills"])))
    return results


if __name__ == "__main__":
    tier_label = {0: "Data Analyst", 1: "Analyst family", 2: "Skill match"}
    found = sweep_remote()
    print(f"Remote leg: {len(found)} relevant remote jobs (Remotive API)\n")
    for j in found[:15]:
        loc = "India/Remote" if j["loc_rank"] == 0 else "Global Remote"
        print(f"[{tier_label[j['tier']]}] {j['title']} - {j['company']} ({loc})")
        print(f"    skills: {', '.join(j['skills']) or '-'}")
        print(f"    {j['url']}\n")
