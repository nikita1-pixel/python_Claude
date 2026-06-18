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

## Sources covered (every sweep lists which ones had results)

The sweep works through **all** of these each run and reports ✅/➖/⚠️ per source. Advanced queries (boolean, ATS X-ray, recency, Pune micro-markets) are used — not just plain title searches.

**A. Indian general boards** — [Naukri](https://www.naukri.com/data-analyst-jobs-in-pune) · [LinkedIn](https://in.linkedin.com/jobs/data-analyst-jobs-pune) · [Indeed](https://in.indeed.com/q-data-analyst-l-pune,-maharashtra-jobs.html) · [Foundit](https://www.foundit.in/srp/results?query=data%20analyst&locations=Pune) · [Glassdoor](https://www.glassdoor.co.in/Job/pune-data-analyst-jobs-SRCH_IL.0,4_IC2856202_KO5,17.htm) · [Shine](https://www.shine.com/job-search/data-analyst-jobs-in-pune) · [SimplyHired](https://www.simplyhired.co.in/search?q=data+analyst&l=pune) · TimesJobs

**B. Tech / startup** — [Wellfound](https://wellfound.com/role/l/data-analyst/india) · [Cutshort](https://cutshort.io/jobs/data-analyst-jobs-in-pune) · [Instahyre](https://www.instahyre.com/data-analyst-jobs-in-pune/) · [Hirist](https://www.hirist.tech/c/data-analytics-bi-jobs) · [YC Work at a Startup](https://www.workatastartup.com/)

**C. Fresher / internship** — [Internshala](https://internshala.com/jobs/data-analyst-jobs-in-pune/) · [Indeed fresher](https://in.indeed.com/q-fresher-data-analyst-l-pune,-maharashtra-jobs.html) · [Built In Pune](https://builtinpune.in/jobs/data-analytics/search/data-analyst)

**D. Remote** — Remotive (via `sweep_remote.py`) · [RemoteOK](https://remoteok.com/remote-data-analyst-jobs) · [We Work Remotely](https://weworkremotely.com/remote-jobs/search?term=data+analyst) · [Working Nomads](https://www.workingnomads.com/jobs?category=data) · [Remote Rocketship](https://www.remoterocketship.com/country/india/jobs/data-analyst)

**E. Company ATS X-ray** — Greenhouse, Lever, Workday, Ashby, SmartRecruiters (e.g. `site:boards.greenhouse.io data analyst India`)

**F. Direct Pune-employer careers** — Barclays, Citi, ZS Associates, Wipro, Infosys, TCS, Persistent, Mastercard, Vanguard, UBS, Deutsche Bank, John Deere, Cummins, Eaton, FIS, Synechron, PubMatic, Druva

**G. Aggregators / community** — Google for Jobs (`data analyst Pune`) · X/Twitter hiring posts

## How ranking works
1. **Title tier** — exact *Data Analyst* first, then analyst family (Business/BI/MIS/Reporting Analyst, Data/Analytics), then any role matching my skills.
2. **Skill overlap** — which of my resume skills the posting needs (Python, SQL, pandas, Excel, Power BI, Plotly, Streamlit, Cognos, etc.).
3. **Location** — Pune → Remote-India → Global-remote.

## Weekly
A scheduled cloud agent runs `/job-sweep` weekly and commits the new sweep log + updated `jobHunt.md` to the GitHub repo. The cloud can't write to my local Desktop directly, so I run `git pull` to sync. The on-demand trigger word is always the reliable path.
