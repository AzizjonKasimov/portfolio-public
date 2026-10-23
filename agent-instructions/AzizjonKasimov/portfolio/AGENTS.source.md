This file lives in `my_agent_configs` and is reached through pointer files in the project's folder (on the VPS, through a symlink; resolve it to the real file first).
Links to the shared files, `PROJECT_CONTEXT.md`, and `notes/` are relative to this file's folder in `my_agent_configs`; every other relative path refers to the project's own checkout.

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

Read the three files above before doing work, unless they are already in your context. They are required instructions and working context, and they remain the source of truth: do not copy their contents into this file.
If a relative path cannot be resolved, use the canonical absolute paths above.
If you still cannot find or read the necessary instruction or context files, stop immediately and tell the user before doing any other work.
If `PRIVATE_CONTEXT.local.md` exists, read it after the required context files for user-authorized sensitive job-application facts. Keep that file local: never commit it, expose it in public portfolio material, or transmit its contents except to a specific application destination already authorized by the user.

This file contains project-specific agent instructions for the portfolio repo. Note files (`notes/`) sit beside this file, not in the repo; read each one only when a line below or in `PROJECT_CONTEXT.md` says to.

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
- Public profiles and bios (LinkedIn, the website's homepage, "about me" answers) lead with one of the user's own stories or principles from `profile/narrative.md`, in the first person, and add the search keywords after. On 2026-09-25 the user called a correct, metric-rich profile "too generic": resume-speak reads like thousands of other profiles. Resumes keep their tight structure; this is about profiles and bios.

## Public Copy

- This repo stays private and holds everything; keep working in it as usual. A public copy,
  https://github.com/AzizjonKasimov/portfolio-public, is built from its committed files by
  public-mirror (https://github.com/AzizjonKasimov/public-mirror, cloned at
  `E:\PersonalProjects\public-mirror`), and
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
- Never write the Recs Innovation customer plant's name or town in chat replies, commit messages, or new public text; say "the plant name" (asked 2026-10-09). The settings rewrite the name in the public copy, but chat has no such filter. Anywhere public, use only the `-covered` screenshots.
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
- Before changing what the public copy hides or shows, or answering when it was set up, read
  `notes/public-copy.md`.

## Resumes

- Before writing, editing, rebuilding, or archiving a resume, or writing a Korean cover letter, read `notes/resumes.md` (library layout, builder, master variants, English and Korean writing, one-page rules).
- For adjacent-fit roles, do not lead with limitations in the top section. Keep the top 30% focused on transferable strengths and credible matching evidence. Be honest about gaps, but place caveats later in the cover letter, notes, or interview preparation.

## Job Search

- Read `job-search/STRATEGY.md` (current direction and constraints) and `job-search/LESSONS.md` (employer re-apply rules and platform quirks) before searching or applying.
- Before searching for jobs, preparing application materials, applying, updating the job-search trackers, or working with agencies, also read `notes/job-search-workflow.md` (tracker rules and audit fields, sourcing, submission steps, agency tracking).
- Before a job outcome or rejection audit (`job-search/audits/`), read `notes/outcome-audits.md` (finding every reply while leaving the mailbox as it was, and judging a rejection).
- Before finding recruiters or open roles through LinkedIn, Wanted, or other job sites in Chrome, read `notes/linkedin-sourcing.md` (page addresses, in-page fetches, and rate limits).
- Before writing a lead note for a Wanted posting or proposal, run `uv run job-search/wanted-posting.py <posting ID>`: it prints the posting's and the company page's facts as Markdown, read-only (GET requests, no login). Read the proposal itself with the in-page GET calls in `job-search/README.md` (Wanted Helpers), never by clicking around the proposal page, where one click accepts.
- Before applying to any job, check `job-search/applications.csv` for the same platform posting ID, posting URL, or company/role combination. Do not apply again if an `applied` row already exists unless the user explicitly confirms a duplicate submission is intended.
- Do not store session tokens, cookies, passwords, OTPs, or private credentials in application snapshots or in the agency tracker and its notes.
- When sourcing job listings on any platform, deliberately include junior and lower-experience searches to increase interview chances. Search for and prioritize terms such as `신입`, `경력무관`, `주니어`, `1년 이상`, `2년 이상`, `0-3 years`, `entry-level`, `junior`, and `associate`, and do not filter out credible technical stepping-stone roles just because they are not perfect AI/RAG matches. Aim for a practical batch mix: mostly realistic junior/lower-mid technical roles, some solid direct-fit mid roles, and only a small number of reach roles.
- The user prefers tailored resumes and cover letters when tailoring would improve fit. Do not batch-submit the same default resume across materially different roles if there is time to create or choose better-targeted variants. Group roles by application narrative when useful (LLM/RAG/agent, AI backend/data pipeline, search/NLP, MLOps/platform, computer vision) and use the most relevant variant for each group. If only a generic resume is available and several roles would benefit from tailoring, pause before final submission and ask whether to create tailored versions first, unless the user prioritizes speed.
- During submission, provide as much truthful and useful information as the platform allows when it helps the application: visa status, nationality, work authorization context, language proficiency, portfolio/resume attachments, cover-letter fields, and short answers. Start visa and language answers from `job-search/reference/visa-language-answer-templates.md` and verify the current date and visa status before using time-sensitive wording. Do not invent details; ask if a custom answer needs information that is not already known.
- When an application asks the user to try the company's product and review it, write two or three plain sentences: one easy positive and one easy improvement, each something the user can see for themselves in about a minute. Give them that one-minute path (the demo URL and what to click). Never write test reports or detailed error lists in their voice; the user rejected one (2026-09-15) because it read as tests they never ran, and they must be able to explain the answer in an interview.
- During job applications, if the Chrome extension has trouble with a UI, file upload, modal, or external career site, debug and fix that tool path before giving up; computer use can see browser windows but cannot click or type in them, so it is no fallback there. When a site still blocks progress (login, CAPTCHA, OTP, hidden details), stop, leave the page at the exact blocker, and tell the user what is blocking it so they can help from their browser session.
- For job-search and application work, use the user's existing Chrome/Gmail session to read relevant application emails, confirmations, and verification messages when needed. Prefer browser access for this workflow; do not install or use a Gmail connector unless the user explicitly asks for one (the user did for outcome audits; see `notes/outcome-audits.md`). The user gives standing permission to launch Chrome when it is not running so this workflow can continue.

## Git

- The user gives standing permission for AI coding agents working in this portfolio repo to commit and push completed, self-contained changes without asking for separate confirmation each time. Use an appropriate concise commit message and include only files that belong to the completed work.
- Before committing or pushing, inspect `git status`, avoid staging unrelated local changes, and never commit secrets, private credentials, or editor/system clutter.
- Generated resume, cover-letter, and application packet artifacts are okay to commit when they are referenced by the tracker, README, or application notes as part of completed work. If `.idea/`, temporary files, unreferenced generated drafts, debug screenshots, or private personal material appear in the worktree, confirm they are intended before committing them.
