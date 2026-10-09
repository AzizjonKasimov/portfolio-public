# Portfolio Project Context

This file is the durable working context for `E:\PersonalProjects\portfolio`. Agent rules live in
`AGENTS.source.md` beside this file, and the career facts live in the repo's item files; this file
keeps the cross-cutting context, the guardrails, and pointers to where things are.

## Purpose

The repository is the cumulative source of truth for Azizjon's portfolio information and
resume-writing material: career history, projects, accomplishments, skills, supporting evidence,
reusable resumes, and the job-search trackers.

## Repository

- Local path: `E:\PersonalProjects\portfolio`
- Git remote: `https://github.com/AzizjonKasimov/portfolio.git` (private)
- Scope: personal
- Canonical instruction file: `E:\PersonalProjects\my_agent_configs\AzizjonKasimov\portfolio\AGENTS.source.md`
- Local loaders: the repo root has gitignored plain-text `AGENTS.md` and `CLAUDE.md` pointer files
  (Windows tools cannot read WSL symlinks). The repo root's tracked `PROJECT_CONTEXT.md` is only a
  pointer to this file, so keep context here.
- AI coding agents have standing permission to commit and push completed changes in this repo
  (see `AGENTS.source.md`).

## Where things live

- **Career facts:** `profile/` (summary, skills with a "never claim" list, narrative and
  principles, and `linkedin.md`), `experience/`, `case-studies/`, `projects/`, `community/`,
  `education/`, `awards/`, `certifications/`. The repo's root `README.md` indexes every file.
- **LinkedIn:** `profile/linkedin.md` holds the live profile text, the standing decisions, the
  editing notes for agents, and the audit checklist.
- **Job search:** `job-search/STRATEGY.md` (direction and constraints), `job-search/LESSONS.md`
  (employer rules and platform quirks), and `job-search/README.md` (trackers, folders, workflow,
  schema, and scripts).
- **Resumes:** `resumes/README.md` (which resume to send for which posting, and how to build one),
  `resumes/resume-index.csv`, and the shared builder and checker in `resumes/tools/`.
- **Portfolio website:** https://azizjonkasimov.github.io (Korean version at `/ko/`), built from
  `E:\PersonalProjects\resume_website\resume_website_frontend`.

## Key facts and guardrails

- **G-Man Auto Parts:** AI/ML Engineer (resumes; LinkedIn says AI Engineer), Daejeon, South Korea
  (remote), April 2025-July 2026 officially. Practical work started in March 2025, so drafts may
  use March 2025 for the actual work history. Azizjon resigned in July 2026; the exact final day
  is not recorded, so use July 2026 as the end month unless the user gives a date.
- **Recs Innovation:** always spelled this way, never `Rex Innovation`. The anomaly detection
  monitored solar power-plant data, and its inference service was integrated into a Virtual Power
  Plant (VPP) platform; never describe the anomaly detection as operating on or detecting anomalies
  in the VPP itself. Some archived materials use the older shorthand "anomaly detection for a VPP
  platform"; treat it as historical.
- **AI-built work is not a language skill:** see the "Never claim" list in `profile/skills.md`.
- **Education:** one degree from Woosong University: B.S., Department of Future Technology (English
  diploma), 미래기술학부 데이터사이언스전공 공학사 (Korean diploma). Resumes write "B.S. Future
  Technology (Data Science)" and "미래기술학부 데이터사이언스전공 (공학사)". GPA 4.39/4.5; graduated
  2024-08 with highest honors (최우수), which only the Korean diploma prints. Every current resume shows it ("Highest honors" or
  "최우수 졸업"); archived packets were left as sent. The Korean diploma also shows the date of
  birth, so public material uses `education/certificates/woosong-diploma-ko-birthdate-covered.jpg`.
- **Awards:** one note per award in `awards/`, each beside its certificate scan. The SW중심대학
  award's Korean name is 자립상 (the 자림상 on LinkedIn was a typo and is fixed). The LINC 3.0
  wording stays as it is (decided 2026-09-25).
- **Languages:** English fluent, Russian native, Uzbek conversational, Korean
  conversational/limited working and improving. LinkedIn's Korean label stays `Professional
  working proficiency` because the connected Duolingo app sets it; never raise it again. Russian
  text written in Azizjon's voice uses masculine forms (я руководил, открыт к предложениям), as
  chosen on 2026-09-25 for the Russian website.
- **Portfolio website:** rebuilt on 2026-09-23 as a static site, and every current resume links
  it. Its six case studies are the public technical proof; link the one that matches what a
  posting values: semantic search, AWS data pipeline, solar MLOps, LangGraph agent, the expense
  tracker (`/work/expense-tracker/`: AI inside a product used daily, where code owns the numbers,
  AI labels, and a human checks every row; good for "project you are most proud of" fields), and
  Network App (`/work/network-app/`: an AI agent with tool calling, safety rules, and a
  report-and-fix evaluation loop; good for AI-agent roles).
- A LinkedIn-to-repo import on 2026-06-23 brought the LinkedIn facts into the item files; LinkedIn
  analytics, recommendations, ads, and "people you may know" suggestions were deliberately not kept.

## Job-search context

- **Core profile:** AI/ML engineer focused on production AI systems, LLM/vector search, MLOps,
  AWS/cloud data infrastructure, data engineering, backend systems, web scraping pipelines, and AI
  agents.
- **Strong target-role signals:** AI Software Engineer, AI/ML Engineer, Applied ML Engineer, MLOps
  Engineer, LLM/RAG Engineer, AI Agent Engineer, Data Engineer for AI/data platforms, backend
  engineer with an AI-systems focus, and model evaluation or computer vision roles when aligned.

Job posting fit rules:

- Highest priority: technical AI/ML, AI software, MLOps, backend AI, cloud/data infrastructure,
  LLM/RAG/agent, data engineering, model evaluation, and computer vision roles that are
  foreigner-friendly or English-friendly.
- Azizjon is open to junior roles when they are still technical, visa/language-compatible, and
  credible stepping stones; do not filter out junior or 0-3 year roles just because of seniority.
  Junior roles at reputable companies, strong AI teams, foreigner-friendly employers, or companies
  with visible technical credibility can be good targets, because some past employers carry little
  external credibility and some of the strongest work is private.
- Medium priority: global/overseas business roles only when they are still technical or
  technical-adjacent, use the technical background or language strengths, and do not require
  business-fluent Korean.
- "Foreigner possible" alone is not enough: check the role type, visa type, Korean requirement,
  English/global work fit, and whether the company can provide visa documents.

JobKorea profile tags: the user is comfortable keeping GAN, OCR, and CNN. Remove or avoid weak or
unwanted tags such as CUDA, Spark, NoSQL, and Azure unless the user confirms stronger experience.
