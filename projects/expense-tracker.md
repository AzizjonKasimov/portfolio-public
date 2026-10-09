---
type: project
title: Expense Tracking App
start: 2026-04
end: present
repo: https://github.com/AzizjonKasimov/expense-tracker-bot # private
stack: [Python, python-telegram-bot, FastAPI, SQLite, JavaScript, Telegram Mini App, Claude (Haiku 4.5), Hetzner VPS] # the Telegram era, April to June 2026
ai_written_code: [Kotlin, Jetpack Compose, Room] # the Android app, written by Claude Code and Codex
tags: [personal-project, in-production, finance, telegram, ai, llm]
status: in daily use (Android app since mid-2026; the Telegram Mini App was the previous form)
demo_video: https://www.youtube.com/watch?v=8pA2G70gYdI
---

# Expense Tracking App

**Personal project, in daily use since April 2026 | Android app since 2026-06-24; earlier a Telegram bot and Telegram Mini App on a Hetzner VPS**

Started as a plain Telegram bot, evolved over ~50 commits into a Telegram Mini App with an
AI-powered import pipeline. Sole user is Azizjon; his girlfriend interacts through split-expense
notifications.

## Application positioning

- This is Azizjon's current default answer when an application asks for the project he is most
  proud of.
- He has worked on and continuously polished the app for several months and uses it extensively
  for his own finances.
- Its AI-assisted automatic transaction labeling saves him substantial manual tracking time.
- The visibility and habits created by the app have helped him save money personally; do not
  invent or attach a monetary amount unless Azizjon supplies one.
- The source repository is private. For application fields that require a public URL, ask for a
  shareable demo or case-study link rather than implying that recruiters can access the repo.
- Public demo: the YouTube video "I Built an AI Expense Tracker That Splits Costs With My
  Girlfriend" (<https://www.youtube.com/watch?v=8pA2G70gYdI>, 12 minutes, published
  2026-09-17 on the channel `@azizjon_kasimov`). It walks through the Android app in demo mode,
  so every transaction shown is sample data. The portfolio website links it from the Expenses
  case study (<https://azizjonkasimov.github.io/work/expense-tracker/>, live since 2026-09-29).

## AI bank-statement import (human-in-the-loop)

- Accepts raw bank-statement text and **password-protected Excel exports** from Korean banks
  (decrypted with `msoffcrypto-tool` + `openpyxl`).
- Statements are chunked (~15 transactions per chunk, header re-attached to each for context) and
  parsed by **Claude Haiku 4.5**, up to 6 chunks in parallel, into
  structured JSON: account, signed amount, currency, note, date, category, subcategory.
- The prompt enforces a fixed taxonomy (12 categories with subcategories) plus **user-defined
  merchant → category mappings and ignore patterns**, both editable from inside the bot
  (`/mappings` conversation flow).
- Azizjon verifies/edits every import in the mini app before it lands — AI does the labeling,
  human keeps the ledger trustworthy.

## Other features

- **Split-expense settlement**: each transaction has a split mode (`i_pay_full`, `half`,
  `she_pays_full`, `custom`); the app computes the girlfriend's share and sends her grouped
  Telegram notifications of what she owes, so reimbursement is built into the tracker.
- **Rolling budget**: a fixed monthly allocation for a chosen subcategory where unspent budget
  rolls forward and overspending goes negative until absorbed; months can be marked "skipped".
- **Mini App web UI** for browsing and editing transaction history (vanilla HTML/JS served by
  FastAPI), with toast feedback and a demo/presentation mode.
- Tested on both sides: Python tests for the backend, headless DOM tests for the mini app
  (Node test runner + jsdom).

## Architecture & data

- Python backend: `python-telegram-bot` for the bot flow, **FastAPI + Uvicorn** for the mini-app
  API, **SQLite** for storage.
- ~2 years of expense history (migrated from previous expense apps), **~1,000 transactions**.
- Deployed on a rented Hetzner VPS.

## Update 2026-09-25: the app is now an Android app

Source: Azizjon's LinkedIn post of about 2026-09-18 ("I built an app that saves me 40 to 100
hours a year", video attached), read during the 2026-09-25 LinkedIn audit. The sections above
describe the earlier Telegram Mini App; this is the current state.

- Timeline in his words: a Telegram bot built in two days, then the Mini App, then the Android
  app "two and a half months later". The Android app is the "Expenses" app listed in
  `ai-native-engineering-workflow.md` (private source; Kotlin, Jetpack Compose, Room, written by
  the coding agents).
- Import: a Toss Bank statement as a password-protected Excel file goes into the Android app; AI
  (Claude, through the private gateway) assigns the category; he confirms each row with "Half",
  "I Pay Full", or "She Pays"; history is saved for later analysis; his girlfriend gets an
  itemized Telegram list with the total she owes.
- Self-reported saving: 40 to 100 hours a year (previously 30 to 60 minutes every 3 to 4 days,
  now 5 to 10 minutes per import).
- Lessons he published with the post, reusable as his engineering principles: "Don't let AI touch
  the numbers" (the AI once read the account balance as income, so code now reads amounts and
  dates and the AI only picks the category); "Better input beats a better prompt" (bank rows such
  as `쿠팡(쿠페이)_KICC` were labelled by reading the Coupang receipt emails and giving the model
  real product names); "Always start small" (the two-day Telegram bot came first).

## Android app design (verified 2026-09-29)

Sources: the private `expense-tracking-app` README and source, the `expense-tracker-bot`
PROJECT_CONTEXT in my_agent_configs, and the releases repository.

- Timeline: first commit (the Telegram bot) 2026-04-10; Android v1.0 released 2026-06-24;
  v1.27 (2026-09-26) is the current release.
- Import: the Toss Bank Excel file is decrypted and read on the phone. When the date and amount
  columns are found unambiguously, code parses the date, amount, and note, and the AI (or local
  rules) only assigns the category and subcategory; the AI never sets an amount. The
  income/expense type follows the code-owned amount sign, so the AI cannot flip a transaction's
  direction.
- Labeling: Claude through the private gateway picks from a fixed taxonomy that is in the prompt.
  The request is a plain prompt (no JSON Schema). User merchant mappings always win over the AI,
  and merchant defaults fill in only when labeling produced no answer.
- Failures are never silent: a missing token, a network or HTTP failure, an empty response, or
  incomplete or invalid labels make the app use local rules and show a blocking alert with the
  reason; uncertain rows stay `Unknown` for review.
- Receipt lookup: Coupang charges all read like `쿠팡(쿠페이)_KICC`, so the app reads Coupang
  order mails over IMAP (read-only) and attaches a receipt only when its charged total equals the
  statement amount and the mail was sent within two hours; ambiguous matches are skipped.
- Review: every row is marked I Pay Full, Half, She Pays Full, Custom, or Skip (income: Confirm
  or Skip), and amount, note, date, and category stay editable. Finish sends the split rows to a
  shared Telegram group chat from the phone, with the total she owes.
- Refunds: in his real statements (2026-04 to 2026-09), 10 of 17 Coupang refunds equalled exactly
  one earlier charge, so the app deducts those automatically and leaves partial refunds for him
  to match by hand.
- Also: Ask AI (up to three category suggestions with reasons, filtered to the taxonomy and the
  row's direction), charts, a rolling Dates budget, GitHub SQL backup to a private repository,
  and signed in-app updates from GitHub Releases.
- Demo mode runs every feature on fake data with a banner on every screen; AI calls in demo mode
  use the saved gateway token on the fake rows. Without a token, the demo import falls back to
  local rules with the usual alert.
- Screenshots for the portfolio website were taken on 2026-09-29 from the published v1.27 in demo
  mode on a read-only test emulator (discarded afterwards). That emulator had no gateway token, so
  its review list and Telegram preview showed local-rule labels (`Unknown`). The same day the
  review list and Telegram preview were retaken with real AI labels on the `ExpensesQaApi35`
  emulator, which has the token saved. The page shows the review list (a Coupang order renamed
  from its receipt and labeled Groceries by the AI), the Telegram preview, and Charts.
