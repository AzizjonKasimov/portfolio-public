# Job Search

The tracker and notes for every job lead, application, agency, and HR contact. The main rule is
simple: before applying anywhere, check `applications.csv` so the same posting, company role, or
platform listing is never applied to twice.

## Start here

- `STRATEGY.md`: the current direction, the constraints, and the default resumes.
- `LESSONS.md`: employer re-apply rules, platform quirks, and screening patterns from past runs.
- `.\job-search\audit-applications.ps1`: where things stand, including applications waiting on a
  reply and leads never acted on.

## Layout

| Path | Purpose |
|------|---------|
| `applications.csv` | One row per posting or company-role application, with fit, risk, outcome, and audit fields. |
| `application-events.csv` | Append-only timeline of every application: found, materials prepared, applied, outcomes, audits, follow-ups. |
| `hr-contacts.csv` | Direct outreach to an employer's recruiters, HR team, or published recruiting inbox; one row per person or inbox. |
| `agencies.csv`, `agency-events.csv` | Agencies, recruiters, public job centers, and talent platforms, with an append-only timeline. |
| `applications/` | Notes for a single application, named `<application_id>.md`: custom form answers, pre-submission snapshots, unusual submission flows. |
| `runs/` | Dated logs of discovery passes, candidate batches, and application runs, named `YYYY-MM-DD-<discovery\|batch\|run>-<topic>.md`. |
| `audits/` | Dated outcome, rejection, and submission audits that update many rows at once. |
| `outreach/` | HR outreach plans and message drafts, and follow-up drafts. |
| `agencies/` | One note per agency, named like its `agency_id`. |
| `templates/` | Starting points for an application note, a pre-submission snapshot, and an agency note. |
| `reference/` | Visa and language answers, the international target countries, and the portfolio proof plan. |
| `check-application.ps1`, `audit-applications.ps1`, `validate-applications.ps1` | Read-only helpers (see below). |
| `wanted-posting.py`, `wanted_api.py` | Read-only Wanted helper: a posting ID in, a lead-note snapshot out (see Wanted Helpers). |
| `wanted-discover.py` | Read-only Wanted search: finds open roles, ranks them, and marks the ones already tracked (see Wanted Helpers). |
| `wanted-dashboard.js`, `wanted-dashboard-compare.py` | Read-only Wanted outcome check: the first reads every application's status in Chrome, the second compares them with `applications.csv` (see Wanted Helpers). |

## Required Workflow

1. Before preparing or submitting an application, search `applications.csv` by posting ID, posting
   URL, company, and role, and check `LESSONS.md` for that employer.
2. If a matching row exists with `status=applied`, do not apply again unless Azizjon explicitly
   confirms that a duplicate submission is intended.
3. If materials are generated but submission is not complete, add or update the row with
   `status=materials_prepared`.
4. Only set `status=applied` after the application was actually submitted, emailed, or confirmed by
   the platform.
5. When the platform allows resume selection or upload, attach the most tailored available resume
   for that listing. Use a platform default resume only when upload or selection is unavailable,
   broken, or blocked, or when the default is already the best fit; record the reason.
6. Record the exact resume, cover letter, packet notes, and detail file paths used.
7. After applying, tell Azizjon which resume and cover letter were used for each listing, including
   when no cover letter was submitted.
8. Before submitting high-value applications, copy `templates/application-snapshot.md` to
   `applications/<application_id>.md` and capture the posting evidence, selected resume or profile
   state, form answers, visa and language wording, and confirmation evidence.
9. If a platform has fields that do not fit the CSV, keep the row in `applications.csv` and put the
   extra data in `applications/<application_id>.md`, starting from `templates/application-detail.md`.
   Log a discovery pass, candidate batch, or application run in `runs/`, and a multi-row outcome
   audit in `audits/`; point each affected row's `details_path` at that file.
10. When an outcome arrives, update `status`, `outcome_date`, `outcome_stage`, and
    `outcome_reason_reported`, then append an `outcome_received` row to `application-events.csv`.
11. After reviewing an outcome, fill `last_audited`, `audit_summary`, and `audit_confidence`, then
    append an `audit` row to `application-events.csv`. Add any new employer rule or platform quirk
    to `LESSONS.md`.
12. Close out stale rows (rule approved by Azizjon on 2026-10-05): a lead (`found`,
    `materials_prepared`, `on_hold`, or `follow_up_needed` without a submission) not pursued within
    45 days of `date_found` becomes `skipped`, and an application with no reply 60 days after
    `date_applied` becomes `no_response`. Append the change to `application-events.csv` and note
    it in `notes`; reopen the row if anything arrives later.

## Agency Outreach Tracking

Use `agencies.csv` and `agency-events.csv` for employment agencies, recruiters, staffing firms,
public job centers, and broad talent platforms where the target is a relationship or a profile
rather than one specific job posting.

1. Before registering with or contacting an agency, check `agencies.csv` by agency name and URL.
2. Add one agency row before starting onboarding, with a note in `agencies/` copied from
   `templates/agency-detail.md`.
3. Append an event to `agency-events.csv` for every meaningful step: found, registration started,
   account or profile created, resume uploaded or sent, recruiter contacted, follow-up scheduled,
   outcome received, or audit completed.
4. Use `status=profile_submitted` or `status=contacted` only after a real profile or CV submission
   or recruiter message is confirmed. Use `needs_user_login`, `needs_user_registration`, or
   `on_hold` when the next step needs Azizjon's password, OTP, identity verification, or account
   creation.
5. If the agency later produces a specific role to apply for, create a normal `applications.csv`
   row for that role and reference the agency record in its notes or detail file.
6. Set `status=closed` when Azizjon decides to stop tracking an agency, and append a `closed`
   event.

## HR Outreach Tracking

Use `hr-contacts.csv` for direct messages or emails to an employer's recruiters, HR team, or
published recruiting inbox (agencies stay in `agencies.csv`). Plans and drafts live in `outreach/`.

1. Before messaging, check `hr-contacts.csv` by company and contact so the same person is not
   messaged twice, and check `applications.csv` so the message can reference the real application.
2. Only record emails the company publishes (careers page, FAQ, posting) or that a recruiter used
   to contact Azizjon. Do not guess email formats or store personal phone numbers.
3. Set `status` to `connection_sent`, `messaged`, or `emailed` only after the send is confirmed,
   and fill `date_contacted` and `next_follow_up`. Other values: `not_contacted`, `replied`,
   `no_response`, `do_not_contact`.
4. When outreach turns into an application, interview, or outcome, record it in `applications.csv`
   and `application-events.csv` as usual.

## Fit And Risk Fields

Use these fields before applying and again during audits. They are deliberately practical rather
than perfect: the goal is to compare patterns across submissions.

| Field | Meaning |
|-------|---------|
| `fit_level` | How directly the role matches Azizjon's strongest profile. Values: `strong`, `good`, `adjacent`, `stretch`, `unknown`. |
| `fit_confidence` | Confidence in the fit assessment: `low`, `medium`, `high`, `unknown`. |
| `selection_rationale` | Why this application was worth sending. |
| `screening_risks` | Semicolon-separated concerns such as `visa_unclear`, `korean_required`, `domain_gap`, `seniority_gap`, `platform_profile_weak`, or `unknown_company_fit`. |
| `visa_risk` | Risk that work authorization blocks the application: `low`, `medium`, `high`, `unknown`. |
| `language_risk` | Risk that Korean or another language requirement blocks the application: `low`, `medium`, `high`, `unknown`. |
| `tailoring_level` | Material quality: `generic`, `profile_only`, `role_family`, `role_specific`, `company_specific`, `unknown`. |

Fit levels:

| Fit level | Use when |
|-----------|----------|
| `strong` | The role directly asks for the user's clearest strengths: AI/ML engineering, LLM/RAG, MLOps, AI systems, backend AI, data/cloud infrastructure, or model evaluation. |
| `good` | The role uses a clear subset of the user's strengths but does not hit the whole profile. |
| `adjacent` | The role is plausible but the employer may primarily want a different center of gravity, such as pure frontend, compiler internals, security research, generic SI/backend, or domain expertise the user has only partly shown. |
| `stretch` | The role has major gaps or likely screen-out requirements, but there is a strategic reason to try. |
| `unknown` | The posting or application evidence is not enough to judge yet. |

Adjacent fit is not "bad." It means "possible, but not the easiest yes." A high-chance batch
should mostly contain `strong` and `good` applications, with `adjacent` applications explicitly
marked so their rejection rate does not distort the main signal.

When reviewing outcomes, separate results by `fit_level`. Do not let `materials_prepared` rows,
`unknown` rows, or adjacent-fit experiments distort the signal from submitted strong/good-fit
applications.

## Outcome Audit Fields

Use these fields after a rejection, withdrawal, closure, interview, or offer:

| Field | Meaning |
|-------|---------|
| `outcome_stage` | Where the application ended: `pre_screen`, `recruiter_screen`, `hiring_manager`, `assessment`, `interview`, `offer`, `post_offer`, `unknown`. |
| `outcome_reason_reported` | The exact reason given by the employer or platform, if any. Do not invent one. |
| `last_audited` | Date the outcome was reviewed. |
| `audit_summary` | Short judgment about the likely cause and what to change next. |
| `audit_confidence` | Confidence in the audit: `low`, `medium`, `high`, `unknown`. |

When the reason is not stated, keep `outcome_reason_reported` empty and write the inference in
`audit_summary` with an appropriate confidence level.

## Status Values

Use one of these values in the `status` column:

| Status | Meaning |
|--------|---------|
| `found` | Posting discovered, but no tailored materials created yet. |
| `materials_prepared` | Resume, cover letter, or answer packet created; submission not confirmed. |
| `applied` | Application submitted or email sent. |
| `follow_up_needed` | Application submitted and needs a specific follow-up action. |
| `interview` | Interview or assessment process started. |
| `offer` | Offer received. |
| `rejected` | Rejection received. |
| `no_response` | Applied, but no reply arrived within 60 days. Reopen the row if the employer answers later. |
| `withdrawn` | Azizjon chose not to continue. |
| `expired` | Posting expired before applying. |
| `closed` | Role closed or no longer available. |
| `duplicate` | Duplicate lead; canonical application is recorded elsewhere in the tracker. |
| `on_hold` | Paused pending more information or user decision. |
| `skipped` | Reviewed but intentionally not submitted because the expected return was too low, requirements were blockers, or user chose not to continue; also a lead not pursued within 45 days. |

## Duplicate Checks

Prefer this matching order:

1. `platform` + `platform_posting_id`
2. exact `posting_url`
3. same company + very similar role title
4. same company + same hiring platform, even if the title changed slightly

The `duplicate_check_key` column should be stable and easy to compare:

- Platform posting: `saramin:12345678`, `jobkorea:23456789`, `kowork:1234`
- No posting ID: `company-role:examplecorp:ai-software-engineer`

## PowerShell Helpers

Search before applying:

```powershell
.\job-search\check-application.ps1 -Company "ExampleCorp"
.\job-search\check-application.ps1 -Platform "JobKorea" -PostingId "23456789"
.\job-search\check-application.ps1 -Url "https://kowork.kr/en/post/1234"
```

Validate the tracker (also checks that every recorded path exists):

```powershell
.\job-search\validate-applications.ps1
```

Show the audit dashboard:

```powershell
.\job-search\audit-applications.ps1
.\job-search\audit-applications.ps1 -Status rejected -Detailed
.\job-search\audit-applications.ps1 -Platform Wanted -Detailed
.\job-search\audit-applications.ps1 -Detailed -StaleDays 45   # list replies and leads older than 45 days
```

Show submitted applications:

```powershell
Import-Csv .\job-search\applications.csv |
  Where-Object { $_.status -eq "applied" } |
  Sort-Object date_applied |
  Format-Table date_applied, platform, company, role_title, platform_posting_id
```

## Wanted Helpers

Before writing a lead note for a Wanted posting or proposal, print its snapshot instead of
reading the posting, its API, and the company page by hand:

```powershell
uv run job-search/wanted-posting.py 393698
uv run job-search/wanted-posting.py https://www.wanted.co.kr/wd/382306 393698
```

It prints Markdown for `applications/<application_id>.md`, to summarize there in English:

- **Company:** founding year, address, website, people (국민연금 가입 사원수), employment
  insurance (고용보험 가입 사원수), average salary, this year's hires' average salary (올해
  입사자 평균연봉), and revenue (매출액), each with its source and date, then every open role
  on Wanted.
- **Posting Snapshot:** title, status, deadline, date posted, the experience range in Wanted's
  field beside the one in the title (they can differ: wd/393698's title says 5~8년, its field
  8-12년), location, employment type, job category, skill tags, Wanted's visa and language
  fields, the lines that mention visas or languages, and the posting's sections word for word
  (Intro, 주요업무, 자격요건, 우대사항, 혜택 및 복지, 채용 전형).

It reads `/api/v4/jobs/<id>`, the posting page `/wd/<id>` (the API lacks 채용 전형),
`/api/v4/companies/<id>`, and the calls behind the company page:
`/api/krs/v1/company/<id>/info-for-wanted`, then `summary-for-wanted` and
`hired-average-salaries` by the company's registration hash, and
`/api/chaos/companies/v1/<id>/jobs`. It is read-only: GET requests only, a 0.4-second pause
before each (`--delay`), no login or cookies, and nothing written to disk. `wanted_api.py`
holds these requests so other Wanted scripts can share them.

### Finding open roles

Before a Wanted application run, list the open roles instead of searching the site by hand:

```powershell
uv run job-search/wanted-discover.py
uv run job-search/wanted-discover.py --query LLM --query "AI 에이전트" --top 60
```

It runs about 30 built-in searches (LLM, RAG, MLOps, AI 에이전트, 데이터 엔지니어, 신입 AI, 주니어
AI, 영어 가능, 외국인, and others) through `/api/chaos/search/v1/position`, keeps postings in
Wanted's 개발 category, drops titles from other job families (frontend, mobile, embedded, QA,
sales), and reads each posting through `/api/v4/jobs/<id>`. Each row gets:

- **rank:** profile terms in the title and the work sections (LLM, RAG, MLOps, agents, vector
  search, AWS, pipelines, forecasting, and more), plus points for language signals, minus points
  for a fluent-Korean requirement or 4+ years asked, and minus 100 for a tracker match;
- **flags:** `foreign-lang-pref` (the posting's 기타사항: 외국어 능통자 우대; foreign-language
  speakers preferred, not visa support), `visa-listed`, `english-pref`, `english-text`,
  `foreigner-text`, `KOREAN-RISK`, and `military` (전문연구요원 or 산업기능요원 postings);
- **tracker:** the status of any `applications.csv` row with the same Wanted posting ID or the
  same company on any platform. Company names match when equal, or when one contains the
  other and both have at least four characters, so 드랩 never matches 원티드랩.

It prints the top of the ranking and writes every row to `%TEMP%\wanted-discover.csv`
(`--out`), and caches each posting's JSON in `%TEMP%\wanted-discover-cache` (`--cache`), so a
second run reads only the searches again. A full run reads about 330 postings and takes several
minutes at the default 0.4-second pause (`--delay`). It is read-only: GET requests through
`wanted_api.py`, no login or cookies, and nothing written to the repo. Read every shortlisted
posting before applying; the rank only orders the reading.

### Reading a proposal

A 면접 제안 or 지원 제안 shows only to the logged-in account. Read it in Chrome with the
JavaScript tool, in a wanted.co.kr tab of your own, and never click 수락 or 거절 on the
proposal page: accepting happens at once (`LESSONS.md`).

```js
// Both kinds: company.name, position.position, offer_type (INTERVIEW = 면접 제안,
// APPLY = 지원 제안), expired_time (answer by), histories (newest first: OFFER,
// USER_ACCEPT, USER_APPLY, ...).
const list = await (await fetch('/api/chaos/proposal/v1/history?type=OFFER&limit=20')).json();
// One proposal, by its newest history id: proposal.job_id (the posting ID), message, rank,
// min_salary and max_salary (만원), salary_negotiable, stock_option, location,
// created_time, expired_time; and reward.
const one = (await (await fetch('/api/chaos/proposal/v1/history/' + list.data[0].histories[0].id)).json()).data;
```

Send only GET requests to these paths: the page's own PUT to `history/<id>` is the accept or
decline. The JavaScript tool cuts its output at about 1,000 characters, so print the message
in slices. Then run `wanted-posting.py` on `proposal.job_id`.

### Checking outcomes against the tracker

Wanted's 지원 현황 (`wanted.co.kr/status/applications/applied`) shows outcomes that never arrive
by email: some employers reject only on Wanted, and Wanted closes applications that get no
feedback within 30 days. On every outcome audit, compare it with `applications.csv` in two steps:

1. In Chrome, in a wanted.co.kr tab of your own where the account is logged in, paste all of
   `wanted-dashboard.js` into the extension's JavaScript tool. It reads the dashboard's list,
   then each application's record, 0.6 seconds apart, in the background. Call
   `wantedDashboard.progress()` until it says done, then print `wantedDashboard.part(1)`,
   `part(2)`, and so on, and save every part, exactly as printed and in order, to
   `%TEMP%\wanted-dashboard.txt`.
2. Compare:

```powershell
uv run job-search/wanted-dashboard-compare.py
uv run job-search/wanted-dashboard-compare.py $env:TEMP\wanted-dashboard.txt --table
```

It prints status mismatches, dashboard applications with no tracker row, Wanted rows with a
`date_applied` that the dashboard lacks, Wanted rows missing `platform_posting_id` or
`date_applied`, and applied dates that differ. Statuses are judged by each record's status code,
which tells an employer rejection from Wanted's closure (both show as 불합격); the codes are in
`LESSONS.md` (Wanted dashboard), and a code the script does not know yet is listed on its own.
`--table` adds every application beside its tracker row, as a Markdown table for the audit note,
and `--tracker` compares another copy of the tracker, such as one saved from git history. The
script exits with 1 while anything is listed.

Each line the snippet prints is one application: Wanted's application ID, the posting ID, the
applied, opened, and decision times (KST), the dashboard's status, the record's status code, the
company, and the role. The JavaScript tool cuts its output at 1,000 characters and blocks text
that looks like `key=value`, so the parts stay under 900 characters, with `|` between fields, and
each part carries a checksum: the compare script names any part that was cut or mistyped, so
print that part again. Both steps are read-only. The snippet clicks nothing and sends GET
requests only; it takes the account's `user_id` from the page without printing it, and never
prints the name, email, or phone fields in Wanted's responses. The compare script writes
nothing: fix the tracker by hand and run it again.

## Notes

- This repo is private, so the real tracker is stored here directly.
- Do not put passwords, account recovery data, raw session tokens, or private platform credentials
  in this folder.
- Keep paths relative to the repository root so future agents and scripts can resolve them.
- `resume_path` points at the living resume file, which is rebuilt in place. To see the exact
  version that was sent, check git history:
  `git log --follow --until=<date_applied> -1 -- <resume_path>`.
- If submission status is uncertain, use `materials_prepared` or `found`, not `applied`.
- Do not overwrite prior events. Append new facts to `application-events.csv` and update the latest
  summary fields in `applications.csv`.
