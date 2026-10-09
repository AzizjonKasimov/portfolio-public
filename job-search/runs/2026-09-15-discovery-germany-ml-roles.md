# Germany ML Job Discovery — 2026-09-15

> **Made-up example.** The companies, postings, and people in this note are fictional. The real
> notes in this folder stay private; this one shows what a discovery note looks like.

## Scope

- Request: find machine learning and MLOps roles in Germany at employers that hire from abroad.
- Sources searched: LinkedIn, company careers pages, and Ashby and Greenhouse boards found through
  web search. Queries included `machine learning engineer Germany visa sponsorship`,
  `MLOps engineer Munich English`, and `junior ML engineer Berlin`.
- This pass is discovery only. No form was filled and nothing was submitted.
- Every lead was checked on the employer's own careers page on 2026-09-15, not taken from an
  aggregator's summary.
- Every lead was checked against the existing rows of `applications.csv` before shortlisting.

## Shortlist

| # | Company | Role | City | Fit | Visa signal | Seniority match |
|---|---|---|---|---|---|---|
| 1 | Northwind Analytics GmbH | Machine Learning Engineer, Search | Berlin | strong | **Sponsors the EU Blue Card and relocation** | 2+ years |
| 2 | Contoso Robotics | MLOps Engineer | Munich | good | Not stated | 3+ years, flexible |
| 3 | Proseware | Senior ML Platform Engineer | Frankfurt | stretch | Not stated | 8+ years: a large gap |

### 1. Northwind Analytics GmbH — Machine Learning Engineer, Search (top pick)

- The team builds product search with embeddings and LLM re-ranking, the closest match to the
  semantic-search case study.
- English is the working language, and German is a plus.
- The posting states Blue Card sponsorship and relocation support.

### 2. Contoso Robotics — MLOps Engineer

- Model deployment, monitoring, and AWS pipelines match the MLOps work.
- The posting says nothing about sponsorship, but the company page mentions international hires.
  The row records `visa_risk=medium`, and the application should ask.

### 3. Proseware — Senior ML Platform Engineer (stretch)

- The technical match is strong, but the role asks for 8+ years and team leadership.
- It was not added to the tracker: the gap is too large for a tailored application now.

## Verified exclusions

| Company | Role | City | Reason |
|---|---|---|---|
| Tailspin Data | ML Engineer | Hamburg | Fluent German is required for client work. Recorded as `skipped`. |
| Litware | AI Engineer | Berlin | The posting says the company cannot sponsor visas. |

## Outcome of this pass

- Leads 1 and 2 went to an application run the next day; see
  `job-search/runs/2026-09-16-run-germany-applications.md`.
- Lead 3 was left out on purpose.

## Notes for the next step

- Lead 1 fits the AI/RAG + Backend resume with a search-focused headline. Lead 2 fits the
  MLOps/Data Pipeline resume.
- Only Northwind states sponsorship. For Contoso, work authorization is an open question to
  raise, not an established fact.
