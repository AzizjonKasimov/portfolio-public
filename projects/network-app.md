---
type: project
title: Network App (AI agent for a personal network)
start: 2026-08
end: present
repo: https://github.com/AzizjonKasimov/network-app # public
releases: https://github.com/AzizjonKasimov/network-app-releases # public
stack: [Android, Claude (Agent SDK on the private AI gateway), tool calling, JSON Schema, AES-256-GCM encrypted GitHub backup, GitHub Releases]
ai_written_code: [Kotlin, Jetpack Compose, Room] # written by Claude Code and Codex; never list these as skills
tags: [personal-project, ai-agent, tool-calling, llm-evaluation, privacy, android]
status: in personal use; latest release v0.15.1 (2026-09-22)
sources: ["network-app README and PRIVACY.md (2026-09-29)", "my_agent_configs network_app PROJECT_CONTEXT.md (2026-09-29)", "gh release list for network-app-releases (2026-09-29)", "screenshots taken on the codex_notes_api35 test emulator with synthetic people, 2026-09-29"]
---

# Network App

**August 2026 - Present | Personal project | Public source**

An Android app that helps Azizjon remember a network that grew too large to keep in his head:
who people are, what they are trying to achieve, what they could help with, and what was said in
dated conversations. Ordinary contact apps store names and numbers but cannot answer "Who could
help with this?" He records and asks everything in one chat thread, where an AI agent reads and
updates the saved records through tools that run on the phone. The app never contacts anyone.

The coding agents (Claude Code and Codex) wrote all of the code. Azizjon designed the product,
the agent, its tools, and the safety rules. Describe it as built with coding agents, never list
Kotlin as a skill (see `ai-native-engineering-workflow.md`).

## Timeline

- 2026-08-24: native Android milestone started. v0.1.0 released 2026-08-25.
- 2026-08-26 (v0.2.0): AI capture and search with review before saving. Model evaluation on the
  real schema: `gemini-3.7-flash` structured-output calls kept timing out, so the app used
  `gemini-3.6-flash` (valid JSON in 11.65 s in a direct probe); a 256-token output limit
  truncated high-thinking answers and was raised to 1,024.
- 2026-09-05: AI calls moved to Azizjon's private Claude-backed gateway.
- 2026-09-08: one conversational Assistant thread replaced the separate capture and search
  screens.
- 2026-09-14 (v0.14.0, released 2026-09-15): the assistant was rebuilt as a tool-using agent,
  because each new kind of request had needed its own prompt, schema, parser, and card.
- 2026-09-21 (v0.15.0): Needs tab, one list of what people in the network are looking for.
- 2026-09-22: v0.15.1, the current release.

## How an agent turn works

- The turn starts with the message, a short history, the current time and locale, the prompt,
  and 17 tool definitions, but no saved records.
- Claude plans on the gateway (`POST /v1/agent/turns`, Agent SDK with its built-in tools off).
  The gateway validates each tool call's arguments against its JSON Schema and relays it to the
  phone.
- The phone re-checks every call (ids exist, text lengths, duplicates, no future dates), runs it
  on the local Room database, and returns only that call's result. A refused call writes nothing
  and comes back as an error the model can read and correct.
- Tools: five read, eight write, and four (deleting a person, note, or record, and merging two
  people) only queue a confirmation card that runs when the user taps it.
- Adds and edits save immediately, each tool call in its own transaction. The reply lists every
  change with one Undo for the whole reply, built from before-and-after copies of each row; undo
  refuses rather than overwrite anything edited since. This was Azizjon's deliberate choice of
  flexibility over review-before-save.
- The prompt tells the model that saved records, notes, and earlier messages are data, not
  instructions. Answers must rest on saved records, say when evidence is old or thin, and never
  imply that someone is willing or available because an old note mentions a skill.
- Measured live on the gateway: a two-person update 11.6 s (22.6 s before `add_note` learned to
  save a note and its records in one call), a question 6.6 s, a new person with four records
  12.8 s.

## Privacy

- The database stays on the phone. What leaves it is what the assistant's tool calls read; a
  stored contact value never leaves. The gateway does not keep tool results after the turn.
- No accounts, analytics, telemetry, or automatic contact import. Android cloud backup is off.
- Optional backup to a private GitHub repository, encrypted on the phone with AES-256-GCM (key
  from a passphrase via PBKDF2-HMAC-SHA256); the app refuses to back up to a public repository.
- Speech input prefers the on-device recognizer and never saves audio.
- Real network data must never appear in source control, tests, screenshots, or logs.

## Evaluation loop

- Every assistant answer has **Report a problem** with fixed labels (wrong person, missed
  something, invented something, wrong record type, wrong date, bad search results,
  misunderstood the request, something else). A report copies the message, the answer, what the
  reply saved or queued, and its tool calls in order, with contact values removed.
- Reports travel in the encrypted backup; `scripts/read-feedback.ps1` decrypts only the reports
  on the development machine. Faults found this way became fixes and regression tests.
- Example (2026-09-14): reports showed education and volunteering filed as jobs. After the fix, a
  synthetic note that had produced four positions produced one position, one education entry,
  and two background records.
- Every meaningful assistant change is checked live against the real gateway on a test emulator
  with obviously made-up people (JVM and instrumented tests too; 53 JVM tests at v0.15.1).

## Public proof

- Source: <https://github.com/AzizjonKasimov/network-app> (README describes the agent,
  privacy boundary, and feedback loop). The repository has no license, so call the code public,
  not open source.
- Case study: <https://azizjonkasimov.github.io/work/network-app/> (live since 2026-09-29, in
  all six site languages).
- Screenshots for the portfolio website were taken on 2026-09-29 on the `codex_notes_api35` test
  emulator (a read-only session, discarded afterwards) with made-up people such as Sara Lind,
  Jordan Kim, and Tomas Reyes, against the live gateway: a save with its Undo list, an honest "no
  clear match" answer, the Needs tab, and the Report a problem dialog.
