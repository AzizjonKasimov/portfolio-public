---
type: profile
platform: linkedin
profile_url: https://www.linkedin.com/in/azizjon-kasimov/
verified: 2026-09-25
---

# LinkedIn Profile

The live LinkedIn profile, the decisions behind it, and notes for editing it. Everything below was
verified on 2026-09-25, when the stand-out rewrite went live, except the changes made and checked
on 2026-10-05: the Open to Work preferences, the Recs intern title, the About's closing line, the
meetup count (13) in the About and Volunteering, the two new Volunteering entries, and the
education field of study. The Android-apps project text and the Recs Innovation media were changed
and checked on 2026-10-09. The two earlier audits (2026-06-23 and 2026-09-25) were folded into
this file on 2026-10-05 and are in git history under `profile/audits/`.

## Decisions (do not reopen)

- **Korean label:** stays `Professional working proficiency`. The connected Duolingo app sets it,
  and Azizjon keeps Duolingo for the badge. Do not raise it again.
- **LINC 3.0 honor:** the wording stays as it is on LinkedIn.
- **Recs Innovation:** "newly formed AI team" is confirmed true (2026-09-25).
- **Daejeon Global Tech Coffee:** listed under Volunteering, not Experience.

## Live profile

- **Name:** Azizjon Kasimov, additional name `Aziz` (the top card reads "Azizjon (Aziz) Kasimov").
- **Headline (option A):**
  `AI/ML Engineer · Shipped LLM/vector search over 2M+ auto parts as a one-person AI team · MLOps & AWS data pipelines · Organizer, Daejeon Global Tech Coffee`
- **Banner:** `assets/linkedin/generated/linkedin-banner-a.png` ("Use AI for judgment calls. / Use
  code for anything that must be exact.").
- **Open to Work** (checked 2026-10-05): visible to everyone on LinkedIn. On-site locations are the
  European Union, Switzerland, Germany, and Denmark, set on 2026-10-05 for the Germany-first plan
  (South Korea and Canada were removed). Remote locations were left as they were: Europe, North
  America, Asia, South Korea. Location types on-site, hybrid, and remote; employment types
  full-time and internship. Titles (LinkedIn's maximum of five): Artificial Intelligence Engineer,
  Software Engineer, Machine Learning Engineer, Data Engineer, Back End Developer.
- **Top skills** (set 2026-06-23): Machine Learning, Python (Programming Language), MLOps,
  Retrieval-Augmented Generation (RAG), Vector Databases.
- **Featured, in order:** the expense-app post ("I built an app that saves me 40 to 100 hours a
  year"); the portfolio link `https://azizjonkasimov.github.io/` titled "Portfolio: production AI/ML
  work and case studies"; the 12th-meetup post; the semantic-search case-study link.
- **Education:** Woosong University, Bachelor's degree, Future Technology (Data Science), with
  `Grade: 4.39/4.5 · Highest honors` and the Korean diploma scan whose birth date is covered. The
  field of study and the program name in the description said Future Technologies until
  2026-10-05.
- **Honors:** the SW중심대학 entry reads 자립상 (the 자림상 typo was fixed on 2026-09-25).
- **Experience titles:** G-Man Auto Parts, AI Engineer, Mar 2025 - Jul 2026, Hwaseong, Gyeonggi
  (Remote). Recs Innovation appears as 렉스이노베이션 with three roles: AI Team Lead (Jul 2024 - Nov
  2024), AI Engineer (Jun 2024 - Jul 2024), Data Science Intern (Mar 2024 - Jun 2024; renamed
  from Data Scientist Intern on 2026-10-05). The resumes use the same titles. The older roles
  (PROMOM KINDER, Woosong dormitory, GS25, Citifuel) were left unchanged.
- **Projects (9):** the four entries below on top, then the older academic projects.

### About

LinkedIn's editor collapses pasted blank lines, so each blank line carries a single space
(2,570 of 2,600 characters). On 2026-10-05 the closing line changed from "remote or
on-site/hybrid in Korea" to the Germany plan, and the Neo4j certification sentence was cut to make
room; the certificates are still listed under Licenses & certifications.

```text
At my last job I was the entire AI team: one engineer, 2M+ auto parts, and a search box that had to reach 95% accuracy on a 3,000-part test before R&D would sign off. It passed and shipped.

Owning the whole path, from raw catalog data to a monitored production system, taught me four things I now build by:

1. Use AI for judgment calls, and code for anything that must be exact. In the search system, entity recognition and structured filters do the precise matching; the LLM cleans up the query and re-ranks. My own expense app once counted my bank balance as income, so now code reads the numbers and the AI only picks the category.

2. Better input beats a better prompt. A part-name alias layer that turns "headlight" into "Head Lamp Assembly" raised recall measurably. In my expense app, no prompt could label "쿠팡(쿠페이)_KICC"; feeding the model real product names from receipt emails could.

3. Measure before you claim. I built the automated accuracy suite (accuracy@1/@3, precision, recall, F1, confusion matrix) before quoting a number. At Recs Innovation, anomaly-detection precision went up about 35% and recall about 37%, one measured change at a time.

4. Ship small, then improve. Docker and GitHub Actions took deploys from 3 hours to 15 minutes. My expense tracker started as a two-day Telegram bot and is now an Android app I use every day.

Before G-Man Auto Parts, I joined Recs Innovation as an intern on its newly formed AI team and was leading that team four months later. We shipped solar power forecasting (error down from 9% to 7%, meeting the bar for KPX power trading) and solar-plant anomaly detection, with inference services integrated into a VPP platform, plus the MLOps around them: Docker Compose, GitHub Actions, PostgreSQL, Prometheus, Grafana; about 80% less manual ops work.

Outside work I run Daejeon Global Tech Coffee, an English-friendly meetup for people in tech: no talks, no slides, 13 meetups so far. The useful part always starts when someone says out loud what they are stuck on. I also build small tools I actually use, like a weather alert bot that messages my family in Tashkent in Russian.

Stack: Python, Django/DRF, FastAPI, PyTorch, PostgreSQL, Weaviate, LangGraph, AWS (Lambda, SQS, EventBridge, RDS, CloudWatch), Docker, GitHub Actions. I work in English, speak Russian natively, and my Korean is conversational.

I plan to move to Germany and am looking for an AI/ML engineer role there or elsewhere in Europe, or remote, where one person can own the path from data to production. azizkhasimov@gmail.com
```

### G-Man Auto Parts description

```text
Sole AI/ML engineer for a used auto-parts e-commerce platform: owned NLP, MLOps, data engineering, and the AWS infrastructure under them, from research through production and day-to-day operation.

- Built the AI semantic search for 2M+ automotive parts (Weaviate vector search, spaCy entity recognition, structured filters, LLM query preprocessing and re-ranking); passed the ~95% accuracy bar on the mandated 3,000-part R&D evaluation.
- Built the automated accuracy test suite behind that number (accuracy@1/@3, precision, recall, F1, confusion matrix, cross-validation), with reports persisted to S3 so the data team could read results without me.
- Designed and operated a serverless marketplace data pipeline on AWS (Lambda containers, SQS, EventBridge, RDS PostgreSQL, DLQ, CloudWatch alarms), load-tested to ~5M listings/day, with anti-blocking resilience: circuit breaker, adaptive rate limiting, multi-NAT routing.
- Prototyped a LangGraph agent that fetches, normalizes, and maps third-party catalog data into the company catalog, automating repetitive data-team ingestion work.
- Redesigned the catalog data model and ran the migration: ~40K legacy records moved and ~2M third-party catalog records ingested with deduplication and atomic transactions.
- Added multilingual query normalization and a part-name alias layer ("headlight" to "Head Lamp Assembly") that measurably raised recall.
- Took over AWS infrastructure ownership from a departing senior engineer, mentored a junior teammate, and translated evaluation results and tradeoffs for a non-technical CEO and COO.
```

### Recs Innovation descriptions

AI Team Lead:

```text
Recs Innovation (렉스이노베이션), a Korean energy company building ESS and Virtual Power Plant (VPP) services in Naju. I joined its newly formed AI team as an intern in March 2024 and was leading the team by July.

- Productionized solar power forecasting and solar-plant anomaly detection, with inference services integrated into the company's VPP platform.
- Cut forecast error from 9% to 7% through data analysis and hyperparameter tuning, meeting the <8% requirement for Korean Power Exchange (KPX) power brokerage and the revenue that came with it.
- Built the MLOps stack (Docker Compose, GitHub Actions, PostgreSQL, Prometheus, Grafana): roughly 80% less manual operations work, an estimated $48K/year saved.
- Raised anomaly-detection precision by ~35% and recall by ~37% over several measured changes: 24 hourly thresholds instead of one global threshold, anomaly-filtered training data, and production-aligned cross-validation with nightly retraining.
- Coordinated ML, backend, and frontend teams: agreed interfaces, deployment plans, and integration fixes.
```

AI Engineer:

```text
- Containerized the anomaly-detection system (Docker Compose) and automated deployment with GitHub Actions: 2 to 3 hours of manual work down to about 15 minutes.
- Built the PyTorch solar generation forecasting model (<10% average error) that met the technical requirement for KPX power brokerage, opening a new revenue line.
```

Data Science Intern:

```text
- Built the FastAPI service that integrated solar-plant anomaly detection into the VPP platform.
- Trained a graph neural network (GNNAD) for multivariate sensor anomaly detection: ~70% precision, ~50% recall, experiments tracked in MLflow.
- Added 24 hourly thresholds instead of one global threshold (+10% recall) and anomaly-filtered training data (+30% precision, +20% recall).
- Built the PyTorch/pandas pipeline and the prediction-vs-actual visualizations the team used to iterate.
```

### Recs Innovation media

Until 2026-10-09 the five Recs screenshots on LinkedIn were the uncovered originals, which name
the customer plant. A privacy audit found them that day, and they were replaced with the
`-covered` copies from `experience/media/recs-innovation/` (what each one shows is in
`experience/recs-innovation.md`). The Data Science Intern role has no media.

- AI Team Lead, in order: `forecast-bars-covered.jpg`, `forecast-week-covered.jpg`, and
  `forecast-page-covered.jpg`, each titled "Power generation prediction system", then the Solar
  Today article link.
- AI Engineer, in order: `anomaly-detected-covered.png` ("Detected anomalous points") and
  `anomaly-none-covered.png` ("Continuous monitoring. No anomalies detected.").
- The titles and descriptions were kept, with two typos fixed ("the amount of power", "is the
  average error rate"). The article card's description now spells Recs Innovation; it said "Rex
  Innovation" before.

### Volunteering

Three entries since 2026-10-05, shown in this order. The two new ones keep the centers' Korean
names in the Organization field and explain them in English in the description: neither center
has an English name on record, and a literal "Good Neighbor Center" could be confused with the
NGO Good Neighbors (굿네이버스). Never name or describe the people there.

Founder and Organizer, Daejeon Global Tech Coffee, Jan 2026 - present, cause Science and Technology.

```text
Started an English-friendly tech meetup in Daejeon because meeting people in tech here as a foreigner was hard. No talks, no slides, one rule in the intro round: say what you are stuck on right now.

13 meetups so far. Recent ones drew 12 to 13 people, including two founders who took the train from Seoul to see whether Daejeon has a tech community. Now hosted in a free room provided by the city, two minutes from the subway. Regulars help newcomers with their projects; my job is mostly to keep the format simple and get out of the way.
```

Volunteer English Teacher, 좋은이웃센터, Sep 2026 - present, cause Education (added 2026-10-05,
form `179215867`; `community/english-classes-mental-health-rehabilitation-center.md`):

```text
Every week I teach a one-hour elementary English class to people in the center's mental health rehabilitation program in Daejeon.
```

Volunteer, 후생학원, Sep 2026 (one visit), cause Children (added 2026-10-05, form `179273987`;
`community/child-care-center-visit.md`):

```text
Went with a volunteer group to this children's home in Daejeon to play and spend time with children who can't live with their families.
```

### Projects

Portfolio website with production case studies (Jun 2025 - present; skills Front-End Development,
Back-End Web Development). The text still says "four case studies"; the site has six since
2026-09-29.

```text
Static site with four case studies from production work: LLM semantic search, a serverless AWS data pipeline, solar forecasting and anomaly-detection MLOps, and a LangGraph catalog-data agent, plus diploma and award scans.

Rebuilt in September 2026. The first version was an LLM chatbot that answered questions about me; it took 42 seconds to wake up on a free tier and recruiters skim rather than chat, so I replaced it with pages that load instantly.

https://azizjonkasimov.github.io
```

Expense tracker with AI bank-statement import (Apr 2026 - present; no skills attached yet):

```text
Reads my Toss Bank statement (a password-protected Excel export), lets AI pick each transaction's category, and keeps every amount and date in plain code because the AI once misread my balance as income. I review every row before it is saved; my girlfriend then gets an itemized Telegram list of what she owes.

Started as a two-day Telegram bot, became a Telegram Mini App, and is now an Android app I use every day: about 1,000 transactions across two years of history, roughly 40 to 100 hours a year saved. The Android version was built by directing Claude Code and Codex; Claude does the labeling through a small gateway on my VPS.
```

Weather and air-quality alerts for family in two countries (2026; no skills attached yet):

```text
A dependency-free Python script on a cron job that warns before rain or bad air: Daejeon by email in English, Tashkent by Telegram in Russian, and silent when there is nothing to say. My family in Uzbekistan uses it daily. Open-Meteo data, no API keys, one config dict per city.
```

Five Android apps built entirely with coding agents, plus a private AI gateway (Apr 2026 - present;
no skills attached yet; form `1478639419`). Since then the Network App saves AI changes right away
with one Undo per reply instead of asking first; see `projects/network-app.md`. Until 2026-10-09
the gateway sentence said "A small TypeScript gateway".

```text
Expenses, Notes, OneShot Reminder, Network App, and Life Simulator: Kotlin and Jetpack Compose apps whose code was written by Claude Code and Codex under a guardrail system I maintain (shared rules, per-project context files, mandatory end-to-end checks, no destructive commands without approval).

Every AI-generated write is schema-validated and confirmed by the user before it is saved; if the model's answer is invalid, nothing is saved. A small gateway on my VPS gives the apps one Claude-backed endpoint with JSON-Schema-constrained output. Each app updates itself from a GitHub Releases channel.

Public source: github.com/AzizjonKasimov (network-app, oneshot-reminder, note-taking-app, life_simulator_app).
```

## Open items

- The meetup count (13 since 2026-10-05) goes stale with each new meetup.
- Attach skills to the three new projects. Do not tag Kotlin: the AI tools wrote the Android code.
- Move the three IBM basics (Sep 2023) below the Neo4j LLM certificates (2025), or delete "What is
  Data Science?".
- Update the portfolio project text to six case studies, and the Android-apps text to the Network
  App's Undo design.
- The June skills snapshot (`profile/skills.md`) listed Java and Chatbot Development. Check
  whether they are still on the profile and remove them: Java was one course, and the chatbot was
  retired on 2026-09-23.


## Audit checklist

Capture these each time LinkedIn is audited, then update "Live profile" above:

- Audit date, public headline, and the first 300 characters of About.
- Top five skills.
- Open-to-Work titles, start date, employment types, location types, and visibility.
- Featured items and order.
- The current role's first visible bullets.
- Languages and proficiency labels.
- Projects and certifications shown near the top.
- Profile analytics if available: profile views, search appearances, post impressions.
- Changes made after the audit, and application or recruiter outcomes after the changes.
