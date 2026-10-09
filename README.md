# Portfolio

Cumulative source of truth for Azizjon Kasimov's portfolio, resume, and career material. Raw,
factual source content lives here so AI agents (and I) can assemble targeted resumes, cover
letters, bios, and portfolio copy without re-deriving the facts each time.

The repo exists in two versions: the private original, and a
[public copy](https://github.com/AzizjonKasimov/portfolio-public) that leaves out the job-search
data, contact details, and other private files and lines. In the public copy, the CSV
trackers and the notes in `job-search/runs/` and `job-search/audits/` are made-up examples, and
[agent-instructions/](agent-instructions/README.md) holds the instructions the AI agents follow.

## Structure

| Path | Contents |
|------|----------|
| `profile/` | Summary & contact, technical skills (with a "never claim" list), personal narrative and principles, and the live LinkedIn profile (`linkedin.md`) |
| `experience/` | One file per employer (roles, accomplishments, metrics); work screenshots in `experience/media/` |
| `case-studies/` | Fact sheets for the major G-Man projects; three have a public website page, linked in their `website` field |
| `projects/` | One file per personal / academic project |
| `community/` | Community initiatives and non-employer leadership |
| `education/` | Degrees and academic record; diploma scans in `education/certificates/` |
| `certifications/` | One file per certification / course; certificate scans in `certifications/certificates/` |
| `awards/` | One file per award / honor; award certificate scans in `awards/certificates/` |
| `assets/` | Generated public images and their renderers: the LinkedIn banner |
| `resumes/` | Reusable resumes (Markdown source, DOCX, PDF), archived application packets, and the shared builder and checker |
| `job-search/` | Strategy, lessons, the application, agency, and HR-contact trackers, and dated run, audit, and outreach notes |

> Keep durable raw facts in the source folders above. Put polished, role-specific application
> outputs under `resumes/` so generated drafts stay separate from reusable source facts.
> Track every found, prepared, or submitted job application under `job-search/` before applying
> so duplicate submissions are avoided.

## Conventions

- **One item per file.** Each experience, project, or certification is its own Markdown file so
  agents can load only what's relevant for a given resume.
- **YAML front-matter** at the top of every content file carries structured metadata for
  filtering and assembly. Common fields:
  - `type`: `experience` | `project` | `case-study` | `community` | `education` |
    `certification` | `award` | `profile`
  - `tags`: themes/skills for filtering (e.g. `mlops`, `nlp`, `time-series`)
  - dates: `start` / `end` as `YYYY-MM` (or `YYYY` when the month is unknown), or a single `date`;
    `end: present` for ongoing work
  - `stack` or `skills`: technologies; `ai_written_code`: languages the AI coding tools wrote,
    which must never be listed as Azizjon's skills
  - links: `repo` (one) or `repos` (several), `website` for a public page
  - item-specific: `company`/`role`, `provider`/`status`, `institution`/`degree`, `associated_with`
  - no `updated` field: git history records when a file changed
- **Facts only.** Don't invent dates, metrics, titles, or outcomes. Mark unknowns explicitly.
- **Scans next to their notes.** Original certificate and diploma scans go in a `certificates/`
  folder beside the note that describes them, and the note records what the scan says. Some scans
  hold private details (the Korean diploma shows the date of birth), so check before using one in
  public material, and use a covered copy such as
  `education/certificates/woosong-diploma-ko-birthdate-covered.jpg`. Work screenshots follow the
  same rule in a `media/` folder beside the employer note: `experience/media/recs-innovation/` holds
  the original screenshots of the Recs systems and the covered copies that the website uses.
- **Source vs. output.** Keep durable facts in the source folders; keep polished, role-specific
  resumes and packets under `resumes/current/` or `resumes/archive/applications/`.

## Index

### Profile
- [Technical skills & languages](profile/skills.md) — including what never to claim
- [Values, principles & story](profile/narrative.md)
- [LinkedIn profile](profile/linkedin.md) — live headline, About, and experience text, decisions, editing notes

### Experience
- [AI/ML Engineer (MLOps & Cloud) — G-Man Auto Parts](experience/gman-auto-parts.md) — 2025 – 2026
- [ML Engineer & Data Scientist — Self-Employed / Upwork](experience/self-employed-upwork.md) — 2024 – 2025
- [Recs Innovation — Intern → Developer → AI Team Lead](experience/recs-innovation.md) — 2024
- [English Teacher — PROMOM KINDER](experience/promom-kinder.md) — 2023 – 2024
- [Dormitory Assistant — Woosong University](experience/woosong-dormitory-assistant.md) — 2023
- [Cashier — Life at GS25](experience/life-at-gs25.md) — 2021 – 2022
- [Sales Assistant — Citifuel LLC](experience/citifuel-llc.md) — 2021

### Case studies (G-Man Auto Parts)
- [AI Semantic Search for Auto Parts](case-studies/gman-ai-semantic-search.md)
- [Large-Scale Marketplace Data Pipeline on AWS](case-studies/gman-marketplace-data-pipeline.md)
- [AI Data-Processing Agent (LangGraph)](case-studies/gman-data-processing-agent.md)
- [Used-Parts Price-Prediction Algorithm](case-studies/gman-price-prediction.md)

### Projects (personal / academic)
- [AI-Native Engineering Workflow](projects/ai-native-engineering-workflow.md) — agent guardrails across 19 projects, private AI gateway, five Android apps
- [Portfolio Website](projects/portfolio-website.md) — static site with six case studies at azizjonkasimov.github.io (the former LLM chatbot was retired on 2026-09-23)
- [Expense Tracking App](projects/expense-tracker.md) — Android app in daily use (started as a Telegram bot), AI categorization
- [Network App](projects/network-app.md) — AI agent with tool calling for a personal network, public source
- [Game Engine with Realistic Body Destruction Physics](projects/game-engine-body-destruction.md) — agent-built prototype (C++, ported to Rust), public repo, browser version, and YouTube videos (June and October 2026)
- [Weather & Air Quality Alert App](projects/weather-alert.md) — multi-city, bilingual, in use by Azizjon + family
- [Diabetic Retinopathy Detection on Human Retina Images](projects/diabetic-retinopathy-detection.md) — Upwork-associated medical CV project
- [Time-Series Prediction Using Reinforcement Learning](projects/rl-time-series.md)
- [Early Road Sign Detection Using YOLOv7](projects/yolov7-road-signs.md) — 2022 university practice project
- [Automatic Music Generator](projects/automatic-music-generator.md)
- [Finger-print voting system](projects/fingerprint-voting-system.md)
- [AI in Medicine Research Paper](projects/ai-in-medicine-paper.md)

### Community
- [Daejeon Global Tech Coffee](community/daejeon-global-tech-coffee.md) — founder and organizer of an English-friendly tech meetup
- [English classes at 좋은이웃센터](community/english-classes-mental-health-rehabilitation-center.md) — weekly volunteer English class at a mental health rehabilitation center in Daejeon, since 2026-09
- [Visit to 후생학원](community/child-care-center-visit.md) — one-time volunteering at a children's home in Daejeon, 2026-09

### Education
- [Woosong University — B.S., Department of Future Technology](education/woosong-university.md) — Data Science major, GPA 4.39 / 4.5, highest honors (최우수)

### Awards
- [Woosong graduation awards — Academic Excellence Award and Commendation Award](awards/woosong-graduation-awards.md) — Aug 2024
- [LINC 3.0 Program Award](awards/linc-3-smart-city-challenge.md) — Dec 2023
- [SW중심대학 Software Application Competition — Excellence Award (자립상)](awards/sw-centered-university-software-competition.md) — Dec 2023
- [Silicon Valley Business Plan Competition — Finalist](awards/silicon-valley-business-plan-finalist.md) — May 2023
- [SolBridge Debate Competition](awards/solbridge-debate-competition.md) — Apr 2022

### Certifications
- [Math for ML & Data Science (DeepLearning.AI)](certifications/math-for-ml-and-data-science.md)
- [Deep Learning Specialization (Coursera)](certifications/deep-learning-specialization.md)
- [Machine Learning in Production (DeepLearning.AI)](certifications/machine-learning-in-production.md)
- [Neo4j Graph Database Courses](certifications/neo4j-graph-database.md)
- [IBM Data Science Courses (IBM / Coursera)](certifications/data-science-courses.md)
- [English Proficiency Tests](certifications/english-proficiency.md) — both expired
- [Learning How to Learn (Coursera)](certifications/learning-how-to-learn.md)

### Job search and resumes
- **Job-search workflow:** [job-search/README.md](job-search/README.md) explains the trackers, folders, and workflow.
- **Resumes:** [resumes/README.md](resumes/README.md) says which resume to send for which posting and how to build one.
- **Resume list:** [resume-index.csv](resumes/resume-index.csv) lists every resume and archived packet.

## Agent instructions

AI coding agents should read `AGENTS.md` (Codex) or `CLAUDE.md` (Claude) before working in this
repo. Both are local, gitignored pointer files that list the canonical instruction and context files
in `E:\PersonalProjects\my_agent_configs\AzizjonKasimov\portfolio`. `PROJECT_CONTEXT.md` in this repo
is only a pointer: keep durable context in the `PROJECT_CONTEXT.md` in that folder.

When adding new portfolio information, create or update the relevant item file (with front-matter)
and add it to the **Index** above — don't dump everything into a single file.

Before submitting any job application, check `job-search/applications.csv` and update it after
materials are prepared or an application is submitted.
