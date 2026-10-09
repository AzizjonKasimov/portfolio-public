---
type: case-study
company: G-Man Auto Parts
title: AI Semantic Search for Auto Parts
status: production
start: 2025-08
end: 2026-02
stack: [Python, Django, Django REST Framework, Weaviate, spaCy, OpenAI API, Hugging Face, Celery, PostgreSQL, AWS S3, TypeScript, React]
tags: [semantic-search, vector-database, nlp, ner, llm, rag-adjacent, evaluation, mlops]
related: [gman-auto-parts]
website: https://azizjonkasimov.github.io/work/semantic-search/
---

# AI Semantic Search for Auto Parts

**Company:** G-Man Auto Parts · **Status:** in production at the end of employment (July 2026) · **Role:** sole AI/ML engineer

## Problem
Used auto-parts buyers and suppliers struggle to find the right part through rigid keyword
filters — the same part is described many ways across languages, and the "right" answer is a
specific part number tied to an exact vehicle (brand, model, year, fuel, transmission,
generation, left/right/front/rear). The goal was natural-language search that returns the
correct part/part-number with high precision.

## Approach & what I built
- **Vector search core.** Embedded the catalog into a **Weaviate** vector DB and built the
  search service in **Django / Django REST Framework**. Engineered the embedding sentences
  (field labels, part side, car year, and curated synonyms) to maximize recall.
- **Entity recognition.** Used **spaCy NER** to pull structured entities out of free-text
  queries (brand, model, year, fuel, transmission, part name, part side, generation) and
  convert them into hard filters layered on top of the vector search. Moved entity ingestion
  to the relational DB and scheduled re-ingestion on instance restart.
- **Two search modes.** A buyer-facing **product search** and a supplier-facing
  **auto-matching** search that maps an uploaded part to catalog records and their part-number
  variants (with a fan-out so each distinct part number is its own result).
- **Multilingual querying.** Added an LLM translation/normalization step for non-English
  queries (GPT-3.5-Turbo → **GPT-4o-mini** for quality + cost), gated behind a lightweight
  **language-detection** package so the LLM is only called when needed.
- **Relevance tuning.** Added an **LLM post-filter/re-ranker** to drop clearly irrelevant
  results and re-order by relevance, and a **part-name alias/synonym** system (e.g.
  "headlight" → "Head Lamp Assembly") that improved accuracy on colloquial queries.
- **Frontend integration.** Wired the e-commerce/admin frontends (TypeScript/React) to the
  search APIs — filters feed the query, results autofill forms, sorting by relevance/distance,
  certainty thresholds.

## Accuracy-testing framework
To make accuracy measurable rather than anecdotal, I built an internal **Testing page**:
- Automated **and** manual evaluation over a deterministic, curated test set, sharing the exact
  same pipeline as production search.
- Metrics: **accuracy@1 / accuracy@3, precision, recall, F1**, plus a **confusion matrix** and
  **cross-validation**.
- Reproducible test-set generation, environment-scoped Vector DB collections (guarded so non-
  prod can't touch prod data), reports persisted to **S3** to survive redeploys, and per-run
  metadata (who ran it, with/without LLM preprocessing).
- Used it for systematic **error analysis** — e.g. tracing "no results" cases to stale objects
  in the test collection, SKU↔`PartMaster` mismatches, multi-pattern entity clashes, and
  body-color handling — and fixed each.

## Tech
Python · Django / DRF · Weaviate · spaCy · OpenAI API (GPT-4o-mini) · Hugging Face (local LLM
option) · Celery · PostgreSQL · AWS S3 · TypeScript / React.

## Outcome
- Shipped to **production** for both buyer and supplier search; ran automated accuracy tests in
  prod and resolved the issues they surfaced.
- **Met the accuracy bar required for the R&D submission (≈95% target)** on the mandated
  **3,000-part** evaluation set, and the project was **approved**. The submission went to a
  government R&D program, which approved it; the company did not approve it itself (user,
  2026-09-27).
- **Capacity:** comfortably supports **300K+ searchable listings** from a catalog of **2M+ part
  records** (accuracy was formally
  measured on the 3,000-part submission set).
- Dataset scope: Kia, Hyundai, SsangYong, Chevrolet.

## My role
Sole owner end-to-end: architecture, embeddings, NER, LLM integration, the evaluation
framework, frontend wiring, and production operation.
