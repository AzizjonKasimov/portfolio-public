# Resume Library

Reusable resumes in `current/`, one-off application packets in `archive/`, and the shared tools
that build and check them.

## Start here: which resume to send

| Posting | Resume (folder under `current/`) |
|---------|----------------------------------|
| **Default English:** AI/ML, LLM/RAG, AI agent, and AI backend roles | `global/ai-rag-agent-engineer/` |
| Cloud AI, MLOps, AWS data infrastructure | `global/ai-cloud-engineer/` |
| Data engineering, ingestion pipelines, PostgreSQL | `global/data-ai-engineer/` |
| Technical lead or senior AI backend | `global/tech-lead-ai-backend/` |
| Energy, solar forecasting, or VPP-domain AI | `global/energy-ai-fullstack/` |
| AI-native engineering, AI-assisted SDLC, roles that value Claude Code and Codex work | `global/ai-native-engineer/` |
| **Default Korean:** AI service, LLM/RAG, and backend roles in Korean postings | `korea/ai-service-developer-ko/` |
| Korean backend and AI systems postings, including E-7 sponsorship | `korea/backend-e7-ko/` |

These cover the three master variants the job-search context names: `AI/RAG + Backend`
(`ai-rag-agent-engineer`, `tech-lead-ai-backend`), `MLOps/Data Pipeline` (`ai-cloud-engineer`,
`data-ai-engineer`), and `Korean E-7 Backend/AI Systems` (`backend-e7-ko`,
`ai-service-developer-ko`). `resume-index.csv` lists every resume and archived packet.

## Layout

| Path | Use |
|------|-----|
| `current/global/`, `current/korea/` | One folder per reusable resume: the Markdown source (`<stem>.md`, the file to edit) and the generated `<stem>.docx` and `<stem>.pdf`. File names carry the role, never a company. |
| `archive/applications/YYYYMMDD-company-role/` | One-off packets and notes as they were sent. Do not reuse them as defaults; several still say "Rex Innovation" or use older wording. |
| `templates/` | `resume-template.md`, a documented starting point for a new source. |
| `tools/` | The shared builder and PDF checker; see `tools/README.md`. |
| `resume-index.csv` | Every current resume and archived packet, with its family, default flag, source, PDF, and DOCX. |

## Editing and building

1. Edit the resume's `.md` source, taking every claim from the source folders (`experience/`,
   `projects/`, `profile/`).
2. Build it; the builder rewrites the `.docx` and `.pdf` beside the source and checks the PDF:

   ```powershell
   .venv\Scripts\python.exe resumes\tools\build_resume.py resumes\current\korea\backend-e7-ko\Azizjon_Kasimov_Resume_Backend_E7_KO.md
   .venv\Scripts\python.exe resumes\tools\build_resume.py --all
   ```

3. Open the PDF and look at it before sending it.

For a one-off tailored version, copy the closest source into a new
`archive/applications/YYYYMMDD-company-role/` folder, edit it there, and build it there; the
builder works in any folder.

## Rules

- Choose from `current/` first when applying to a new role.
- Keep exactly one canonical `.docx` and one canonical `.pdf` per resume. Rebuild those stable file
  names in place; never create `_Updated`, `_Final`, `_New`, `v2`, or similar copies.
- Resumes are rebuilt in place, so the file at a tracker's `resume_path` may be newer than what was
  sent. Git history keeps every sent version:
  `git log --follow --until=<date_applied> -1 -- <resume_path>`.
- Update `resume-index.csv` whenever a resume is created, renamed, regenerated, archived, or
  superseded.
- Do not create new top-level folders directly under `resumes/`.
- The builder and checker enforce the format rules (one page, body text of at least 8.5 pt,
  embedded fonts, real links) and the fact rules (no "Rex", no G-Man "Present", no Java, Kotlin,
  or Rust skills, no "anomaly detection for a VPP", highest honors present).
- The online resumes on Wanted, Saramin, and JobKorea are edited by hand, outside the builder.
  Before applying through one, capture it and run `tools/check_resume_text.py` on it (steps in
  `tools/README.md`).
