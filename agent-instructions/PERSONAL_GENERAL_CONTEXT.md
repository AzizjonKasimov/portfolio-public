# Personal General Context

## Overview

This file captures durable background for the user's personal projects in this config repo. It is intended for chatbot context, not for agent behavior rules.

## Ownership And Usage Context

- These projects are owned directly by the user and are separate from company production/R&D work.
- Personal projects may include productivity tools, experiments, bots, or small automation systems built for everyday use.
- The user works on Windows, and coding agents (Claude Code and Codex) run natively on Windows too. WSL2 is installed but agents no longer run there. Some services, such as the AI gateway and the expense tracker's legacy bot, run on a headless Linux VPS.

## Common Priorities

- Personal projects tend to favor simple, maintainable solutions with low operational overhead.
- Fast iteration, usable outputs, and clear documentation are more important than heavyweight architecture.
- When the project is user-facing, practical UX clarity still matters even if the implementation stays small.

## Common Technical Context

- Most current personal projects are native Android apps (Kotlin, Jetpack Compose) built with AI coding agents; others are Python tools, a static Vite website, and a Rust simulation sandbox. The exact stack varies by project.
- Deployment may happen either on the user's local Windows machine or on a simple Linux/VPS environment depending on the tool.
- Local project context files should carry the project-specific background, while local instruction files should focus on behavioral rules and workflow preferences.
