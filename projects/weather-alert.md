---
type: project
title: Weather & Air Quality Alert App
date: 2026 # built a few months before June 2026; repo pushed to GitHub 2026-06-10
repo: https://github.com/AzizjonKasimov/weather-alert # private
stack: [Python (stdlib only), Open-Meteo API, cron, Gmail SMTP, Telegram Bot API, Hetzner VPS]
tags: [personal-project, in-production, automation, alerts, telegram, i18n]
status: in active use (Azizjon + girlfriend by email, 3 family members via Telegram)
---

# Weather & Air Quality Alert App

**Personal project, in active use | dependency-free Python, cron-driven on a Hetzner VPS**

A zero-dependency Python script (standard library only — no `pip install`) that runs from cron
on a headless VPS and alerts before rain or bad air quality. **Silent by design**: when
conditions are fine it sends nothing, so every notification is actionable.

## Alert logic

- **Day run** (07:00 local): checks hourly forecast 08:00–21:00 for rain, plus current air
  quality.
- **Night run** (21:00 local): checks overnight rain, 21:00–08:00.
- **Rain alert** when any hour in the window has precipitation probability **≥ 40%** — the alert
  lists the exact rainy hours, max probability, an umbrella reminder, and current/feels-like/
  low/high temperatures, with a full hourly breakdown.
- **AQI alert** (day runs only) when **US AQI > 100**, tiered by severity (sensitive / unhealthy /
  very unhealthy) with PM2.5 and PM10 readings.

## Multi-city, multi-language, multi-channel

- **Daejeon, South Korea** — alerts in English, delivered by **email** (Gmail SMTP) to Azizjon
  and his girlfriend.
- **Tashkent, Uzbekistan** — alerts in **Russian**, broadcast via a **Telegram bot** to 3 family
  members.
- i18n string table covers both languages, including translated WMO weather-code descriptions.
- Family onboarding is self-serve: relatives `/start` the bot and a helper script harvests their
  chat IDs via `getUpdates`.

## Architecture

- Data from the free **Open-Meteo** forecast and air-quality APIs (no API key needed).
- Four daily cron entries (day/night × two cities) on the same Hetzner VPS as the expense
  tracker; per-city config (coordinates, timezone, language, channels) in a single dict.
