---
type: experience
company: G-Man Auto Parts
role: AI/ML Engineer
linkedin_role: AI Engineer
headline: AI/ML Engineer — Production AI Systems, Search & MLOps
location: Daejeon, South Korea (Remote)
linkedin_location: Hwaseong, Gyeonggi, South Korea (Remote)
start: 2025-04
linkedin_start: 2025-03
end: 2026-07
skills: [Python, Django, Django REST Framework, Weaviate, spaCy, OpenAI API, LangGraph, Celery, PostgreSQL, AWS Lambda, AWS SQS, AWS EventBridge, AWS RDS, CloudWatch, Docker, Playwright, curl_cffi, TypeScript, React] # TypeScript and React: features delivered, not skills (see profile/skills.md)
tags: [mlops, nlp, semantic-search, vector-database, ai-agents, llm, web-scraping, aws, serverless, data-engineering, price-prediction, ecommerce, remote]
sources: ["업무일지 work log (Aug 2025 – Jun 2026)", "Azizjon Cumulative Info.docx"]
---

# AI/ML Engineer — G-Man Auto Parts

**April 2025 – July 2026 officially; practical work started March 2025 | Daejeon, South Korea (Remote)**
**Production AI Systems · Search · MLOps**

Resumes list this role as **AI/ML Engineer**. LinkedIn lists it as **AI Engineer**, full-time,
**March 2025 - July 2026**, **Hwaseong, Gyeonggi, South Korea (Remote)**. The repo keeps the
official-employment note above because official employment began in April 2025 while practical
work started in March 2025. Azizjon officially resigned in July 2026; the exact final day has not
yet been recorded.

## Overview

The live LinkedIn description of this role is in `profile/linkedin.md`.

Served as the sole AI/ML engineer building the AI and data infrastructure for a used auto-parts
e-commerce business. Work spanned applied NLP/LLM systems, MLOps, large-scale data
engineering, and AWS cloud architecture — taking features from research through to
production and operating them. Worked with technical PMs on requirements, priorities, and
delivery; translated system behavior, evaluation results, and operational tradeoffs for the
non-technical CEO, COO, and data-labeling team. Informally mentored a junior teammate
and took over AWS infrastructure ownership from a departing senior engineer.

> Scope note: official employment began April 2025, while practical work started in March
> 2025; the granular daily work log covers Aug 2025 – Jun 2026 (daily logging started
> partway into the role).

## Selected highlights
- Built and shipped to production an **AI semantic search** for auto parts (Weaviate vector
  DB + spaCy entity recognition + LLM query understanding), with a full automated
  **accuracy-testing framework** (accuracy@1/@3, precision/recall/F1, confusion matrix,
  cross-validation).
- Designed and operated a **serverless data pipeline on AWS** (Lambda, SQS, EventBridge,
  RDS Postgres) to collect used-parts market data at scale — targeting ~5M listings/day
  across 7 vehicle brands — with full observability and anti-blocking resilience.
- Prototyped a **LangGraph AI agent** that autonomously fetches, normalizes, and maps
  third-party catalog data into the company's catalog, automating the data team's
  repetitive ingestion work.
- Researched and prototyped a **used-parts price-prediction algorithm** combining
  depreciation, demand, and live marketplace supply/demand signals.

---

## 1. AI semantic search for auto parts (production)
→ Full case study: [AI semantic search](../case-studies/gman-ai-semantic-search.md)

- Built a semantic search that lets users find parts from natural-language queries, backed
  by a **Weaviate** vector database and **spaCy NER** extracting entities (brand, model,
  year, fuel, transmission, part name, part side, car generation) to build precise filters.
- Shipped two search modes: a buyer-facing **product search** and a supplier-facing
  **auto-matching search** (matching uploaded parts to catalog records / part numbers).
- Added **multilingual support** via an LLM translation step, switching GPT-3.5-Turbo →
  GPT-4o-mini for better quality at lower cost, and gating it behind language detection to
  avoid unnecessary LLM calls.
- Improved relevance with an **LLM post-filter / re-ranker** and a **part-name synonym/alias**
  system (e.g. "headlight" → "Head Lamp Assembly") that measurably raised recall.
- Engineered the embedding sentences (field labels, synonyms, part side, car year) and wired
  frontend filters through to the vector search; integrated entity ingestion via RDB.
- Dataset scope: Kia, Hyundai, SsangYong, and Chevrolet parts.
- **Outcome:** met the accuracy bar required for the R&D submission (≈95% target) on the
  mandated **3,000-part** evaluation set, and the project was **approved**; the system
  comfortably supports **300K+ searchable listings** (accuracy was formally measured on the
  3,000-part set).

## 2. AI accuracy-testing framework (production)
→ Covered in the [AI semantic search case study](../case-studies/gman-ai-semantic-search.md)

- Built an internal testing page running **automated and manual** search evaluations on a
  deterministic, curated test set, computing **accuracy@1 / accuracy@3, precision, recall,
  F1**, plus a **confusion matrix and cross-validation**.
- Generated reproducible test datasets, persisted reports to **S3** (to survive redeploys),
  and added per-run metadata so the data team could interpret results independently.
- Drove iterative accuracy improvements through error analysis (stale vector objects, SKU↔
  PartMaster mismatches, entity-recognition clashes, body-color handling, etc.).

## 3. Large-scale marketplace data pipeline on AWS (production)
→ Full case study: [Marketplace data pipeline](../case-studies/gman-marketplace-data-pipeline.md)

- Designed and deployed a **serverless scraping pipeline** to collect used-parts listings
  from **a European used-parts marketplace**: AWS **Lambda** (packaged as Docker containers) as workers, **SQS** as the
  task queue, **EventBridge** for scheduling, **RDS PostgreSQL** for storage, **DLQ** for
  failures, **SNS + CloudWatch** for alerting.
- Target throughput ~**5M listings/day** across the 7 brands the company handles; made
  worker target-claiming concurrency-safe with retry and stuck-job recovery, and wrote
  incrementally to the DB.
- Engineered **anti-blocking resilience**: replaced headed Playwright with **curl_cffi**,
  added a circuit breaker, global cooldown, request jitter, adaptive rate-limiting, multiple
  browser profiles, and multi-NAT-gateway / multi-region "two-lane" routing to spread IPs.
- Built full **observability**: CloudWatch custom metrics and alarms (worker failures, DB
  health, SQS backlog/age, blocked pages, capacity/throttling), health-check scripts (AWS
  CLI, OS-agnostic), and a read-only monitoring Lambda.
- Hardened for production per senior review: Postgres statement timeouts, URL allow-list,
  response-size limits, atomic writes, structured failure capture; added ECR/CloudWatch
  retention policies for cost control.
- Built a **Manifest V3 Chrome extension scraper** as a fallback when the headless path is
  blocked — watchdog recovery, resume/checkpoint JSON/CSV exports, unattended scheduled VM
  runs, and an idempotent Python importer into the catalog DB.
- **Outcome:** reached the ~**5M listings/day** target in testing; as the marketplace's anti-bot /
  rate-limiting escalated, sustainable throughput was progressively throttled down to
  ~**5,000 listings/day**, which became the practical operating rate. The testing run reached
  the 5M/day target on the smallest RDS instance (user, 2026-09-27).

## 4. AI data-processing agent — LangGraph (prototype → internal tool)
→ Full case study: [AI data-processing agent](../case-studies/gman-data-processing-agent.md)

- Prototyped a **LangGraph** agent that takes a request, fetches third-party catalog
  data, processes it, and maps/writes it into the company catalog — automating repetitive
  data-team ingestion.
- Added a scheduling layer (APScheduler) with a UI, a Chrome-extension bridge for fetching
  blocked/rate-limited sources, and automatic reporting of how data was normalized and mapped.
- Evaluated build-vs-buy for agent tooling and orchestration (Airflow/Prefect/Celery) before
  committing to a lightweight approach.
- **Status at the end of employment:** working prototype, not in production.

## 5. Used-parts price-prediction algorithm (R&D / PoC)
→ Full case study: [Price-prediction algorithm](../case-studies/gman-price-prediction.md)

- Researched and prototyped a market-value / lifecycle-aware price-prediction algorithm for
  used parts, iterating through several model designs (depreciation + Gaussian-demand,
  demand-driven, scarcity price-floor), at 3-month prediction granularity.
- Collected ground-truth price histories (the company's own sales records, a European used-parts marketplace) and evaluated with
  **MAE / MAPE** and prediction-vs-actual visualizations across multiple part types
  (e.g. headlights, Kia Sportage tail light, ECU).
- Built a **v2** adding external/market signals: ACEA vehicle registrations, model
  discontinuation dates, **Google Trends (pytrends)**, and live marketplace signals (active/
  new/disappeared listings) derived from the marketplace data.
- **Status at the end of employment:** ~**70–80% accuracy** on a limited real-world
  ground-truth set; not productionized.

## 6. Data engineering, migration & catalog modeling
- Designed the core catalog **Django models** (incl. `PartMaster`) prioritizing query speed
  and future-proofing; refactored a 6,000-line `views.py` into maintainable modules.
- Built **legacy-data migration** (old DB → new DB via export/import) and a multi-stage
  importer for third-party catalog data, with deduplication, atomic transactions,
  and unique constraints to guarantee integrity — migrating **~40K company records** and
  ingesting **~2M catalog records**.
- Implemented a **PC-group → category matching** system (search-as-you-type UI, bulk Excel
  upload, parent/child propagation) and VIN-search pipelines (supplier and consumer sides).
- Optimized heavy jobs with **chunked processing and adaptive batch sizing** (RAM-aware) to
  avoid overloading instances, and offloaded long tasks to **Celery** background workers.

## 7. LLM part-summary generation (PoC / demo)
- Built an LLM pipeline generating **bilingual (English + Korean)** car-part summaries from
  structured row data, with prompt engineering, QA/normalization rules, and tests.
- Incorporated domain-expert feedback into the output (replacement cycle + mileage,
  installation/certification guidance, pre-/post-purchase checks, liability-safe compatibility
  wording).
- Generated summaries for **all ~40K of the company's products**; not shipped to production by
  the end of employment.

## 8. E-commerce platform features
- Integrated a **PayPal** payment flow (backend + test page).
- Built an **email service via MS 365 / Entra** for verification, forgot-password, and
  reset-password, plus the corresponding Sign Up / Log In / Forgot Password pages.
- Improved the supplier product-upload form and product pages (filters, autofill from AI
  matches, UX/performance fixes).

## 9. AWS infrastructure ownership & cloud upskilling
- Took over **AWS infrastructure ownership** from a departing senior engineer, ramping
  through IAM/MFA, VPC, public/private subnets and NAT gateways, EC2/key pairs, RDS, SSM
  tunneling, CloudFormation, ECR, and App Runner/Lightsail/Elastic Beanstalk trade-offs.
- Established operational habits for cost monitoring and safely stopping/throttling runaway
  cloud workloads.
- Began consolidating the separate tools (price-prediction dashboard, marketplace data UI, part-
  summary generation, data-processing agent) into a single internal **admin tool**.

## Remote work & ways of working
- Operated fully remotely with strong self-discipline, structured daily scheduling, and
  proactive break management to sustain productivity and health.
- Worked day to day with technical PMs, including across a Korean/English language gap;
  estimated effort and translated technical work for the non-technical CEO, COO, and
  data-labeling team, including preparing presentation scripts for an external client
  presentation in Seoul.
- Used AI coding tools (Cursor, Codex CLI) deliberately, adding guardrail rules after
  catching cases where the AI missed easy-to-detect errors.
