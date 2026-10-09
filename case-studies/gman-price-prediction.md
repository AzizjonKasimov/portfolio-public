---
type: case-study
company: G-Man Auto Parts
title: Used-Parts Price-Prediction Algorithm
status: research-poc
start: 2026-02
end: 2026-06
stack: [Python, pandas, NumPy, Matplotlib, OpenAI API, pytrends, PostgreSQL]
tags: [forecasting, pricing, time-series, demand-modeling, evaluation, research]
related: [gman-auto-parts, gman-marketplace-data-pipeline]
---

# Used-Parts Price-Prediction Algorithm

**Company:** G-Man Auto Parts · **Status:** R&D / PoC · **Role:** sole researcher & developer

## Problem
Pricing used auto parts well requires understanding how a part's market value evolves over its
lifecycle — depreciation, demand swings (wear vs. collision parts), and scarcity as a model is
discontinued. The company needed a **proprietary** algorithm to forecast a part's price over
time, with the AI as a *supplementary* signal rather than the core.

## Approach & what I built
- Iterated through several algorithm designs at **3-month prediction granularity**:
  - depreciation + **Gaussian-demand** model,
  - a **demand-driven** model,
  - a **scarcity price-floor** modification for discontinued/rare parts,
  with the repository structured to run and compare multiple algorithms side by side.
- Derived a market-value formula and reasoned carefully about the right starting price (OEM
  price vs. original release price vs. second-hand price) and how each variable is obtained.
- **Ground-truth & evaluation:** assembled historical price series from **the company's own sales records** and
  **a European used-parts marketplace** (and explored Wayback Machine / Google date-range tooling), then measured accuracy
  with **MAE / MAPE** and prediction-vs-actual visualizations across multiple part types
  (headlights, Kia Sportage tail light, ECU), handling outlier-dominated low-volume quarters.
- **v2 with external signals:** integrated ACEA vehicle-registration data, model
  discontinuation dates, **Google Trends (via pytrends)**, and live marketplace signals
  (active / new / disappeared listings) sourced from the
  [AWS data pipeline](gman-marketplace-data-pipeline.md).
- Built a demo **dashboard UI** for the data team (predictions, key attributes, historical
  prices) and converted the algorithm documentation to maintainable Markdown.

## Tech
Python · pandas · NumPy · Matplotlib · OpenAI API (price estimation step) · pytrends ·
PostgreSQL.

## Outcome
- Multiple working prototypes with an accuracy-comparison harness against real ground-truth
  data.
- Reached ~**70–80% accuracy** on a limited real-world ground-truth set by the end of
  employment (July 2026); not productionized.

## My role
Sole researcher and developer — algorithm design, ground-truth collection, evaluation
methodology, external-signal integration, and the demo dashboard.
