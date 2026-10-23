---
type: project
title: AI-Native Engineering Workflow (Agent Guardrails, AI Gateway, Android Apps)
start: 2026-04
end: present
repos:
  - https://github.com/AzizjonKasimov/my-agent-configs # private
  - https://github.com/AzizjonKasimov/ai-gateway # private
  - https://github.com/AzizjonKasimov/network-app # public
  - https://github.com/AzizjonKasimov/oneshot-reminder # public
  - https://github.com/AzizjonKasimov/note-taking-app # public
  - https://github.com/AzizjonKasimov/life_simulator_app # public
  - https://github.com/AzizjonKasimov/expense-tracking-app # private
stack: [Claude Code, Codex CLI, JSON Schema, GitHub Releases]
ai_written_code: [Kotlin, Jetpack Compose, Room, TypeScript] # apps and AI gateway; never list these as skills
tags: [ai-native-engineering, ai-assisted-sdlc, coding-agents, guardrails, llm-evaluation, structured-output, personal-project]
sources: ["my_agent_configs README, PROJECT_CONTEXT_REGISTRY.md, GENERAL_AGENTS_RULES.md and project contexts (2026-09-21)", "ai-gateway README via gh (2026-09-21)", "gh repo list AzizjonKasimov (2026-09-21)"]
---

# AI-Native Engineering Workflow

Since April 2026, Azizjon has built software mainly by directing coding agents (Claude Code and
Codex) inside a guardrail system he designed and maintains. This file holds the source facts that
resumes use for AI-native, AI-assisted-SDLC, and agentic-engineering roles.

## Agent instruction and context system (`my-agent-configs`, private)

- Canonical repo for agent instruction files and project context, first commit 2026-04-06; 154
  commits as of 2026-09-21.
- 19 registered projects as of 2026-09-21: 9 company (six G-Man Auto Parts repos,
  `ai-agent-data-processing`, `part-price-prediction`, and a researcher-notes workspace) and 10
  personal.
- Layers: shared rules (`GENERAL_AGENTS_RULES.md`), company and personal general context, and one
  `PROJECT_CONTEXT.md` per project, which carries durable state between agent sessions.
- Dual loader: each project exposes `AGENTS.md` (Codex) and/or `CLAUDE.md` (Claude Code), both
  pointing at one canonical source through symlinks or tiny pointer files. A symlink-safe header
  and a stop rule make agents halt when they cannot load the required files.
- Guardrails in the shared rules: never read credentials or dump environment variables, no
  destructive commands without approval, never apply production database changes, focused
  reviewable diffs, documentation upkeep, at least one real end-to-end check before a task counts
  as done, and a maintained stress or diagnostic harness for load and concurrency bugs.
- `vps/VPS_SETUP.md` bootstraps headless Claude Code on a VPS so every session loads the same
  rules.

## Private AI gateway (`ai-gateway`, private, TypeScript)

- Created 2026-09-04. A small HTTP service on one VPS that gives Azizjon's apps a single AI
  endpoint backed by Claude.
- Bearer-token auth per caller; listens on localhost.
- `POST /v1/generate`: prompt plus optional JSON Schema; returns output that matches the schema.
- `POST /v1/chat/completions`: OpenAI-compatible, so existing OpenAI clients work unchanged.
- `POST /v1/agent/turns`: Claude plans and calls tools that the calling app executes and posts
  back, so app data never lives on the gateway. Built-in Claude Code tools stay off. Tool results
  do pass through the gateway to Claude; the gateway does not store them and logs tool names
  only. Never write that app data "never reaches" the gateway (a 2026-09-27 site rewrite did, and
  it was corrected on 2026-09-29).
- Used by the expense tracker, Network App, and OneShot Reminder.

## Android apps (Kotlin, Jetpack Compose, Room)

Five apps, each with an in-app updater fed by a GitHub Releases channel: Sorted (the expense
tracker, called Expenses until 2026-10-22; private source), Network App, OneShot Reminder, Notes,
and Life Simulator (public source).

- Three of the five apps use AI (Sorted, Network App, OneShot Reminder); Notes and Life
  Simulator do not. Each AI app validates the answer before using it.
- Sorted and OneShot Reminder ask the user before saving AI output. OneShot Reminder never
  falls back to local parsing; a failed or invalid AI response leaves the draft unsaved. Sorted
  falls back to local rules with a blocking alert.
- Since 2026-09-14 Network App's assistant is an agent that saves adds and edits immediately,
  with one Undo per reply; only deletes and merges wait for a tap. See `network-app.md`.
- Model evaluation in Network App (2026-08-26 to 2026-09-05): `gemini-3.7-flash` structured-output
  calls repeatedly timed out, so the app moved to `gemini-3.6-flash` (valid JSON in 11.65 s in a
  direct probe). A 256-token output limit truncated high-thinking responses and was raised to
  1,024. On 2026-09-05 the app moved to the Claude-backed gateway; the full proposal schema
  returned in 18.7 s on `claude-sonnet-5`.
- Network App release assets are verified after publishing against the updater's size and hash
  and a pinned signing certificate.

