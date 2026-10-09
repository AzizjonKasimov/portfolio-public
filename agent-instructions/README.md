# Agent instructions

These are the instructions that the AI coding agents (Claude Code and Codex) follow in this repo.
They live in a separate private repo of agent settings, and each publish of this public copy
copies them here, without their private lines.

The private repo holds two small pointer files, `CLAUDE.md` and `AGENTS.md`, that git ignores.
Each pointer tells the agent to read these four files before it does any work:

| File | What it holds |
|---|---|
| [AzizjonKasimov/portfolio/AGENTS.source.md](AzizjonKasimov/portfolio/AGENTS.source.md) | The rules for this repo: the knowledge base, resumes, the job search, the public copy, and git. |
| [AzizjonKasimov/portfolio/PROJECT_CONTEXT.md](AzizjonKasimov/portfolio/PROJECT_CONTEXT.md) | The background the agents need: where things live, the key facts, and the job-search direction. |
| [GENERAL_AGENTS_RULES.md](GENERAL_AGENTS_RULES.md) | The rules that every one of Azizjon's projects shares: communication, safety, documentation, and testing. |
| [PERSONAL_GENERAL_CONTEXT.md](PERSONAL_GENERAL_CONTEXT.md) | The background that every project shares. |

The paths inside the files point at folders on Azizjon's own computer (`E:\PersonalProjects\...`).
To reuse the setup, copy the files into your own project, then replace those paths and the
personal facts with your own.

The CSV trackers in this public copy (`job-search/*.csv` and `resumes/resume-index.csv`) hold
made-up example rows with the real columns, and the notes in `job-search/runs/` and
`job-search/audits/` are made-up examples too. The real rows and notes stay private.
