---
type: case-study
company: G-Man Auto Parts
title: AI Data-Processing Agent (LangGraph)
status: prototype
start: 2026-02
end: 2026-06
stack: [Python, LangGraph, OpenAI API, APScheduler, PostgreSQL]
tags: [ai-agents, langgraph, llm, automation, data-ingestion, etl]
related: [gman-auto-parts, gman-marketplace-data-pipeline]
website: https://azizjonkasimov.github.io/work/catalog-agent/
---

# AI Data-Processing Agent (LangGraph)

**Company:** G-Man Auto Parts · **Status:** working prototype, not in production at the end of employment (July 2026) · **Role:** sole developer

## Problem
Ingesting third-party vehicle/parts data into the company catalog was
repetitive, manual data-team work: pick many parameters, download, normalize, and map records
into the right catalog tables. The goal was to **automate the repetitive ingestion** so the
data team could stop doing it by hand.

## Approach & what I built
- Prototyped a **LangGraph** agent that receives a request (drop-down selection of brand /
  model / year / region, for the **7 vehicle brands** the company handles), resolves the
  matching vehicle variants, fetches the relevant data through the **third-party catalog API** with
  caching and retries, normalizes it, and **maps and writes it into the catalog DB** itself.
- Started from an MVP (natural-language query + a clarification node + debug tracing of the
  agent's internal steps), then simplified to deterministic drop-down inputs once the workflow
  stabilized.
- Added a **scheduling layer** (APScheduler) with a UI to run the agent on a schedule (KST),
  including manual run-times and fixes for duplicate task registration.
- Kept job scope, job status, and billable API use **visible** instead of hiding them behind
  autonomous behavior.
- Added **automatic reporting** of how the agent normalized and mapped each batch, so the
  impact is auditable and understandable to non-engineers.
- Generated reference documentation of the catalog schema (which tables to read vs. write) and
  a temporary caching schema for catalog data down to the group level, with
  resumable, chunked persistence to handle very large models (100k+ variations): batches are
  saved to PostgreSQL with checkpoints, so a job can resume or be cancelled safely.

## Engineering judgment
- Evaluated **build-vs-buy** for agent tooling and orchestration — surveyed existing AI-agent
  data-collection tools and workflow engines (Airflow / Prefect / Celery) — and chose a
  lightweight approach appropriate to the current phase, with a path to scale later.
- Reasoned about *why* LangGraph adds value even when the LLM is used for only one small step
  of the workflow (structured, inspectable, resumable orchestration).

## Tech
Python · LangGraph · OpenAI API · APScheduler · PostgreSQL · third-party catalog API.

## Outcome
- Working prototype that fetches, processes, and maps catalog data, with scheduling and a
  demo UI for the data team. It was being folded into the consolidated internal admin tool.
- **Not in production at the end of employment (July 2026).** The goal was to automate the data
  team's manual ingestion.

## My role
Sole developer — research, architecture, agent implementation, scheduling, and the demo UI.
