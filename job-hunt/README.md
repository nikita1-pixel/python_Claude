# 🎯 Job Hunt Sweep

An automated job-hunt tool for **Data Analyst** roles in **Pune** (and matching remote roles), built by Nirmala Choudhary. It finds the latest postings, ranks them against my actual resume skills, and logs every run so I can track the market over time.

## How to run a sweep

**On demand — just say the word:**
```
/job-sweep
```
(or type "job sweep" in Claude). Claude then web-searches the Pune + India job boards, runs the remote-jobs feed, ranks everything, writes a dated log, and updates `jobHunt.md`.

**Remote feed on its own (pure Python):**
```
python job-hunt/sweep_remote.py
```
Reuses my own `fetch_jobs.py` (Remotive API) and prints ranked remote roles.

**Weekly automatic:** a scheduled cloud run does the sweep every Monday and commits results to GitHub — I just `git pull` to sync. (See "Weekly" below.)

## What's in here

| File / folder | What it is |
|---|---|
| `jobHunt.md` | **Master tracker** — updated every sweep: top live leads, my apply-status table, source links, sweep changelog |
| `sweep-logs/` | **One file per run** (`sweep-YYYY-MM-DD.md`) — the full results of that sweep |
| `sweep_remote.py` | The remote-jobs leg — reuses my Remotive API client and ranks results against my skills |

## Curated sources (clickable any time)

Pune Data Analyst searches, pre-filtered:
- **Naukri:** https://www.naukri.com/data-analyst-jobs-in-pune
- **LinkedIn:** https://www.linkedin.com/jobs/search/?keywords=Data%20Analyst&location=Pune
- **Indeed:** https://in.indeed.com/jobs?q=Data+Analyst&l=Pune
- **Foundit:** https://www.foundit.in/srp/results?query=data%20analyst&locations=Pune
- **Instahyre:** https://www.instahyre.com/data-analyst-jobs-in-pune/
- **Cutshort:** https://cutshort.io/jobs/data-analyst-jobs-in-pune
- **Hirist:** https://www.hirist.tech/
- **Wellfound (startups):** https://wellfound.com/role/r/data-analyst
- **Internshala (fresher):** https://internshala.com/jobs/data-analyst-jobs-in-pune/
- **Remote feed:** Remotive API via `sweep_remote.py`

## How ranking works
1. **Title tier** — exact *Data Analyst* first, then analyst family (Business/BI/MIS/Reporting Analyst, Data/Analytics), then any role matching my skills.
2. **Skill overlap** — which of my resume skills the posting needs (Python, SQL, pandas, Excel, Power BI, Plotly, Streamlit, Cognos, etc.).
3. **Location** — Pune → Remote-India → Global-remote.

## Weekly
A scheduled cloud agent runs `/job-sweep` weekly and commits the new sweep log + updated `jobHunt.md` to the GitHub repo. The cloud can't write to my local Desktop directly, so I run `git pull` to sync. The on-demand trigger word is always the reliable path.
