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
