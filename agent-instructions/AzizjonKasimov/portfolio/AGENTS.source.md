IMPORTANT: This file may be a symlink.
If this file is a symlink, resolve the real path of this file first.
Interpret all relative paths in this file relative to the real file location, not the current working directory.

Shared rules: [GENERAL_AGENTS_RULES.md](../../GENERAL_AGENTS_RULES.md)
General context: [PERSONAL_GENERAL_CONTEXT.md](../../PERSONAL_GENERAL_CONTEXT.md)
Local context: [PROJECT_CONTEXT.md](./PROJECT_CONTEXT.md)

Canonical absolute file paths for this project (try Windows first, then WSL):
- `GENERAL_AGENTS_RULES.md`
  - Windows: `E:\PersonalProjects\my_agent_configs\GENERAL_AGENTS_RULES.md`
  - WSL: `/mnt/e/PersonalProjects/my_agent_configs/GENERAL_AGENTS_RULES.md`
- `PERSONAL_GENERAL_CONTEXT.md`
  - Windows: `E:\PersonalProjects\my_agent_configs\PERSONAL_GENERAL_CONTEXT.md`
  - WSL: `/mnt/e/PersonalProjects/my_agent_configs/PERSONAL_GENERAL_CONTEXT.md`
- `PROJECT_CONTEXT.md`
  - Windows: `E:\PersonalProjects\my_agent_configs\AzizjonKasimov\portfolio\PROJECT_CONTEXT.md`
  - WSL: `/mnt/e/PersonalProjects/my_agent_configs/AzizjonKasimov/portfolio/PROJECT_CONTEXT.md`
- Optional private local context
  - Windows: `E:\PersonalProjects\my_agent_configs\AzizjonKasimov\portfolio\PRIVATE_CONTEXT.local.md`
  - WSL: `/mnt/e/PersonalProjects/my_agent_configs/AzizjonKasimov/portfolio/PRIVATE_CONTEXT.local.md`

Always read the three files above before doing work.
These files are required instructions and required working context.
Do not treat them as optional reference material.
Keep their instructions active while working.
Do not rewrite their contents into this file. They remain the source of truth.
If a relative path cannot be resolved, use the canonical absolute paths above.
If you still cannot find or read the necessary instruction or context files, stop immediately and tell the user before doing any other work.
If `PRIVATE_CONTEXT.local.md` exists, read it after the required context files for user-authorized sensitive job-application facts. Keep that file local: never commit it, expose it in public portfolio material, or transmit its contents except to a specific application destination already authorized by the user.

This file contains project-specific agent instructions for the portfolio repo.

## Knowledge Base

- Treat this as a personal portfolio and resume knowledge base.
- Keep the root `README.md` useful as the main entry point as the repository grows, and list every item file in its Index.
- Store career facts in the repo's item files, one item per file (`profile/`, `experience/`, `case-studies/`, `projects/`, `community/`, `education/`, `certifications/`, `awards/`), and give each fact one home rather than copying it into several notes. Keep `PROJECT_CONTEXT.md` for cross-cutting context, guardrails, and pointers, not item details.
- Do not invent resume claims, metrics, employers, dates, titles, certifications, or project outcomes. If a detail is unknown, leave it marked as unknown or ask the user.
- When drafting resumes, cover letters, bios, or portfolio copy, tailor the writing to the requested role or audience while staying grounded in the facts recorded in this repo and the linked context files.
- Prose that the public reads (the portfolio website, the case studies written for it, bios, and the LinkedIn About and Featured text) follows the copy rules in `E:\PersonalProjects\my_agent_configs\AzizjonKasimov\AzizjonKasimov.github.io\AGENTS.source.md`: explain each piece of shorthand once, where it first appears; give every sentence a subject and a verb; put one number in a sentence, followed by what it meant; tell each story in time order. Resume bullets may stay compressed; web prose may not, because the user found their own site hard to read when it was written like a resume (2026-09-27).
- Prefer clear source-of-truth organization over polished prose when capturing new raw portfolio information. Polish later when producing a specific resume or portfolio artifact.
- Turn private work into public proof only through anonymized case studies, sanitized architecture diagrams, and small synthetic demos (`job-search/reference/portfolio-proof-plan.md`). Do not expose employer code, private data, credentials, internal URLs, or proprietary implementation details.
- LinkedIn is the main platform profile. Its live text, standing decisions, and editing notes are in `profile/linkedin.md`; follow that file's audit checklist when auditing it, and update the file after every LinkedIn change.

## Public Copy

- This repo stays private and holds everything; keep working in it as usual. A public copy,
  https://github.com/AzizjonKasimov/portfolio-public, is built from its committed files by
  public-mirror (`E:\PersonalProjects\public-mirror`), and
  `.public-mirror.toml` decides what the copy holds: which files are public, and which private
  names are rewritten (G-Man data sources and partners, colleagues, the Recs customer plant).
- Text item files in the existing folders (`experience/`, `case-studies/`, `projects/`,
  `community/`, `education/`, `certifications/`, `awards/`) are public by default. Scans, photos,
  screenshots, new folders, and anything under `job-search/` or `resumes/current/` stay private
  unless the settings name them.
- When a public file needs a private detail (a person's name or contact, an application, a
  client, a data source, a credential ID, health or money matters), wrap those lines in
  `<!-- private:start -->` and `<!-- private:end -->` (`# private:start` / `# private:end` inside
  YAML front matter). For a name that recurs across files, add a rule to `[transform.replace]`
  in the settings instead.
- `public-versions/` holds made-up stand-ins that the public copy shows in place of private files:
  example rows for every CSV tracker, and one example each of a discovery note, an application-run
  note, and an outcome audit. When a tracker's columns change, change its example too; `check`
  warns when they differ. Keep everything in that folder fictional.
- The public copy also shows this file and the other instruction and context files, copied from
  `my_agent_configs` into `agent-instructions/`. Private lines there use the same markers.
- After changing public files or the settings, run
  `uv run E:\PersonalProjects\public-mirror\public-mirror.py check -v` and fix every reported
  problem. Publish (`... publish`) only when the user asks. Never commit to or push to the public
  repo directly: every change goes through this repo and `publish`.

## Resumes

- Maintain the resume library structure under `resumes/`: active reusable variants belong in `resumes/current/korea/` or `resumes/current/global/` (one folder per resume, named by role, never by company), historical one-off packets belong in `resumes/archive/applications/YYYYMMDD-company-role/`, reusable starting points belong in `resumes/templates/`, and shared build/render/validation helpers belong in `resumes/tools/`. Do not create new top-level folders directly under `resumes/`. Update `resumes/resume-index.csv` and `resumes/README.md` whenever current resumes are created, moved, regenerated, archived, or superseded.
- Edit a resume's Markdown source and rebuild it with `resumes/tools/build_resume.py`, which writes the DOCX and PDF and runs `resumes/tools/check_resume_pdf.py`. Do not hand-edit generated DOCX or PDF files, and do not create version-suffixed copies.
- Maintain a small set of reusable master variants instead of generating unrelated one-off resumes from scratch. The preferred masters are `AI/RAG + Backend`, `MLOps/Data Pipeline`, and `Korean E-7 Backend/AI Systems` (mapped to folders in `resumes/README.md`). For each posting, adjust the headline and top strengths while keeping the core structure consistent.
- Optimize the top 10 seconds of every resume before applying. The top section should immediately answer "why this role" with the target role title, 3-4 role-matched strengths, and proof metrics. Avoid starting with broad generic summaries or long skill inventories.
- For English resumes, use the A1/Ashby-style structure: clear role headline, targeted strengths near the top, concise skill groups, then experience bullets. Keep dense metric blocks and broad infrastructure lists secondary unless the role specifically asks for them.
- For Korean resumes and Korean cover letters, write the user-facing copy naturally in Korean. Translate school names, degree/major names, locations, and generic role/process terms when a normal Korean expression exists; keep English only for proper nouns, official product/framework names, common technical abbreviations, exact company/job-title wording when necessary, and credential names that are normally shown in English.
- For Korean resumes, write in Korean-market resume logic rather than translating English paragraphs. Prefer short sections such as `지원 직무`, `핵심 역량`, `주요 성과`, `기술 스택`, and `비자/언어`. Keep normal technical terms in English when Korean engineering resumes commonly do so, such as `LLM`, `RAG`, `AWS`, `PostgreSQL`, and `Docker`. Make sentences short, concrete, and result-based, and avoid awkward mixed-language wording such as `English fluent`; prefer `영어 업무 가능, 한국어 회화 가능, 러시아어 원어민`.
- For adjacent-fit roles, do not lead with limitations in the top section. Keep the top 30% focused on transferable strengths and credible matching evidence. Be honest about gaps, but place caveats later in the cover letter, notes, or interview preparation.
- Unless the user explicitly asks otherwise, resume PDFs stay at one page, but never by making the text feel squeezed: embedded fonts, body text of 8.5 pt or larger, leading around 1.3x-1.4x, real `https://` and `mailto:` link annotations, and the available page used before typography shrinks. The builder and checker enforce these; before a high-value application, also look at the rendered PDF for clipped text or broken Korean glyphs.
- When auditing rejections, distinguish resume-format problems from positioning problems. A polished-looking PDF can still underperform if the first screen does not match the posting's center of gravity quickly enough.

## Job Search

- Read `job-search/STRATEGY.md` (current direction and constraints) and `job-search/LESSONS.md` (employer re-apply rules and platform quirks) before searching or applying.
- Before applying to any job, check `job-search/applications.csv` for the same platform posting ID, posting URL, or company/role combination. Do not apply again if an `applied` row already exists unless the user explicitly confirms a duplicate submission is intended.
- When preparing job application materials or submitting applications, update `job-search/applications.csv` immediately. Use `materials_prepared` for generated packets that are not yet submitted, and use `applied` only after the submission or email send is confirmed. Append every step (found, materials prepared, applied, outcome, audit) to the append-only `job-search/application-events.csv` instead of relying only on the latest status.
- Fill the audit fields in `applications.csv` (fit level, selection rationale, screening risks, tailoring level, outcome stage, reported reason, audit summary, audit confidence) for every platform; they feed rejection and response-rate analysis. Use the fit-level vocabulary in `job-search/README.md`, and keep batches and rejection audits separated by fit level: do not mix `strong` and `good` applications with `adjacent`, `stretch`, `unknown`, or `materials_prepared` rows when judging resume or application quality.
- Close out stale rows by the rule in `job-search/README.md` (approved 2026-10-05): a lead not pursued within 45 days of being found becomes `skipped`, and an application with no reply 60 days after applying becomes `no_response`. Log each change as an event, and reopen a row if anything arrives later.
- Store platform-specific form answers, unusual submission details, and extra application notes in `job-search/applications/<application_id>.md` when they do not fit cleanly in the CSV tracker. Discovery passes, batches, and application runs go in `job-search/runs/`, multi-row outcome audits in `job-search/audits/`, and HR outreach plans and drafts in `job-search/outreach/`; see `job-search/README.md` for the layout. Add any new employer rule or platform quirk to `job-search/LESSONS.md`.
- Before submitting high-value applications, preserve an application snapshot from `job-search/templates/application-snapshot.md`: posting evidence, selected resume or profile state, submitted form answers, visa/language wording, confirmation evidence, and dashboard/status URLs where available. Do not store session tokens, cookies, passwords, OTPs, or private credentials.
- When registering with, contacting, or auditing employment agencies, recruiters, staffing firms, public job centers, or broad talent platforms, maintain `job-search/agencies.csv`, append every meaningful step to `job-search/agency-events.csv`, and store extra notes in `job-search/agencies/`. Use the agency tracker for relationship/profile setup and the normal application tracker for specific role applications that come from an agency. Do not store passwords, OTPs, cookies, session tokens, or private credentials.
- When searching for more jobs to apply to, do the sourcing directly: use the browser extension to search multiple live job boards, company career pages, LinkedIn/company pages, Google/Bing search results, and relevant Korean/global hiring platforms (LinkedIn, Wanted, Jumpit/Saramin, JobKorea, Dev Korea, Kowork/KoMate, Ashby, Lever, Greenhouse, Workable) yourself. Inspect real search results and postings, open the source platform page, and verify current status there before treating a role as a candidate. Perplexity AI must not be the primary discovery tool for job-search sourcing; use it only as an optional secondary aid for query expansion, cross-checking, or finding additional source pages after direct searching has already started.
- Treat job boards as discovery sources, not the only application route. When a platform listing is closed, stale, missing an apply button, blocked by login, or otherwise not submittable, search for the same company and role on the company's careers page and common ATS hosts (Ashby, Greenhouse, Lever, Workday, SmartRecruiters, Workable) and company email/contact pages before marking it closed or giving up.
- When sourcing job listings on any platform, deliberately include junior and lower-experience searches to increase interview chances. Search for and prioritize terms such as `신입`, `경력무관`, `주니어`, `1년 이상`, `2년 이상`, `0-3 years`, `entry-level`, `junior`, and `associate`, and do not filter out credible technical stepping-stone roles just because they are not perfect AI/RAG matches. Aim for a practical batch mix: mostly realistic junior/lower-mid technical roles, some solid direct-fit mid roles, and only a small number of reach roles.
- Europe, starting with Germany, is the first priority since 2026-10-05 (`job-search/STRATEGY.md`). For roles there, filter early for English-language roles at employers that hire from abroad and support the work permit (usually the EU Blue Card) and relocation, and record the sponsorship risk explicitly when a posting is silent about it.
- The user prefers tailored resumes and cover letters when tailoring would improve fit. Do not batch-submit the same default resume across materially different roles if there is time to create or choose better-targeted variants. Group roles by application narrative when useful (LLM/RAG/agent, AI backend/data pipeline, search/NLP, MLOps/platform, computer vision) and use the most relevant variant for each group. If only a generic resume is available and several roles would benefit from tailoring, pause before final submission and ask whether to create tailored versions first, unless the user prioritizes speed.
- When a platform allows selecting or uploading a resume, use the most tailored available resume for that listing. Treat a platform default resume as a fallback only when upload or selection is unavailable, broken, or blocked, or when the default is already the best option; record the reason if a default resume is used.
- During submission, provide as much truthful and useful information as the platform allows when it helps the application: visa status, nationality, work authorization context, language proficiency, portfolio/resume attachments, cover-letter fields, and short answers. Start visa and language answers from `job-search/reference/visa-language-answer-templates.md` and verify the current date and visa status before using time-sensitive wording. Do not invent details; ask if a custom answer needs information that is not already known.
- After applying, always tell the user which resume and cover letter, if any, were used for each listing, and record those exact material paths in `job-search/applications.csv` before finishing the run.
- During job applications, if Chrome/browser automation has trouble with a UI, file upload, modal, or external career site, switch to the computer-use plugin and interact with the live browser visually. If the computer-use plugin or browser control plugin is installed but not working, debug/fix that tool path before giving up. When a site still blocks progress (login, CAPTCHA, OTP, hidden details), stop, leave the page at the exact blocker, and tell the user what is blocking it so they can help from their browser session.
- For job-search and application work, use the user's existing Chrome/Gmail session to read relevant application emails, confirmations, and verification messages when needed. Prefer browser access for this workflow; do not install or use a Gmail connector unless the user explicitly asks for one. The user gives standing permission to launch Chrome when it is not running so this workflow can continue.

## Git

- The user gives standing permission for AI coding agents working in this portfolio repo to commit and push completed, self-contained changes without asking for separate confirmation each time. Use an appropriate concise commit message and include only files that belong to the completed work.
- Before committing or pushing, inspect `git status`, avoid staging unrelated local changes, and never commit secrets, private credentials, or editor/system clutter.
- Generated resume, cover-letter, and application packet artifacts are okay to commit when they are referenced by the tracker, README, or application notes as part of completed work. If `.idea/`, temporary files, unreferenced generated drafts, debug screenshots, or private personal material appear in the worktree, confirm they are intended before committing them.
