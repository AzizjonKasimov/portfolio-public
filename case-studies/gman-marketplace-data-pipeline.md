---
type: case-study
company: G-Man Auto Parts
title: Large-Scale Marketplace Data Pipeline on AWS
status: production
start: 2026-03
end: 2026-06
stack: [Python, AWS Lambda, AWS SQS, AWS EventBridge, AWS RDS, AWS RDS Proxy, AWS DLQ, AWS SNS, CloudWatch, AWS ECR, Docker, PostgreSQL, Playwright, curl_cffi, JavaScript]
tags: [aws, serverless, web-scraping, data-engineering, observability, distributed-systems, anti-bot, cost-optimization]
related: [gman-auto-parts, gman-price-prediction]
website: https://azizjonkasimov.github.io/work/aws-data-pipeline/
---

# Large-Scale Marketplace Data Pipeline on AWS

**Company:** G-Man Auto Parts · **Status:** in production at the end of employment (July 2026) · **Role:** designed, built & operated solo

## Problem
The price-prediction work and pricing strategy needed a continuous, broad feed of used-parts
market data. The target source was a large European used-parts marketplace. The
challenge: collect listing data at very large scale — on the order of **5 million listings per
day across 7 vehicle brands** — reliably, within cost limits, and against active anti-bot
defenses.

## Architecture
A fully **serverless** pipeline on AWS:
- **Lambda workers** packaged as **Docker containers** do the fetching/parsing.
- **SQS** as the work queue (migrated from an earlier DB-as-queue design), with a **DLQ** +
  redrive policy for failures.
- **EventBridge** schedules crawl cycles; a dedicated Lambda resets crawl targets daily.
- **RDS PostgreSQL** stores listings/observations; writes are incremental, atomic, and
  concurrency-safe (safe target-claiming, retry, stuck-job recovery).
- **SNS + CloudWatch** for alerting and metrics.

## Anti-blocking & reliability
- Replaced headed **Playwright** with **curl_cffi** after the site began issuing anti-bot
  challenges to the browser automation.
- Added a **blocked-page circuit breaker**, global cooldown state in Postgres, request
  **jitter**, and **adaptive rate-limiting** that backs off automatically under blocking.
- Spread egress across **multiple NAT gateways / Elastic IPs and regions** ("two-lane" Lambda
  routing), multiple browser profiles, and a gradual worker spin-up after cooldowns.
- Built a **Manifest V3 Chrome extension** as a fallback scraper for when the headless path is
  blocked: watchdog recovery for stale states, resume from JSON/checkpoint exports, unattended
  Seoul-scheduled VM runs, idempotent re-imports, and a guarded Python importer into the
  catalog DB.

## Observability & operations
- **CloudWatch custom metrics + alarms**: orchestrator down, worker failures, capacity/
  concurrency throttling, SQS backlog/age, blocked-page rate, DB-write failures,
  listings-per-day throughput.
- Health-check tooling via AWS CLI (made **OS-agnostic**) and a small **read-only monitoring
  Lambda** posting DB health to CloudWatch.
- Learned and documented safe operational procedures (throttle/stop Lambdas, purge SQS) to
  prevent runaway cost, plus how to query historical CloudWatch logs.

## Production hardening (from senior review)
Postgres statement timeouts; URL **allow-list**; response-size limits; fail-fast on suspicious
empty/wrong discovery pages; atomic write paths; structured failure capture; removed expensive
`COUNT(*)` operations from the hot path; index maintenance/audit tooling; **ECR + CloudWatch
retention policies** for cost control.

## Tech
Python · AWS Lambda (Docker) · SQS · EventBridge · RDS PostgreSQL · RDS Proxy · DLQ · SNS ·
CloudWatch · ECR · Playwright · curl_cffi · Chrome extension (Manifest V3, JS).

## Outcome
- Deployed to **production** on AWS with daily scraping and DB persistence operating and
  monitored.
- **Reached the ~5M listings/day target in testing, on the smallest RDS instance**
  (user, 2026-09-27). As the marketplace's anti-bot / rate-limiting
  escalated, sustainable throughput was progressively throttled down to **~5,000 listings/day**,
  which became the practical operating rate — a real lesson in adversarial, rate-limited data
  collection.

## My role
Sole designer, builder, and operator — from architecture and IaC-style deploy scripts through
anti-bot engineering, observability, and day-to-day production operation. Part of taking over
AWS ownership from a departing senior engineer.
