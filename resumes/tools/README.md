# Resume Tools

Shared helpers for building and checking resumes. Install their packages into the repo `.venv`
with `.venv\Scripts\python.exe -m pip install -r resumes\tools\requirements.txt`. The builder needs
Microsoft Word on Windows.

## `build_resume.py`

Builds a resume's `.docx` and `.pdf` from its Markdown source, which sits next to them with the same
stem. The source format is documented in `resumes/templates/resume-template.md`.

```powershell
.venv\Scripts\python.exe resumes\tools\build_resume.py resumes\current\global\ai-rag-agent-engineer\Azizjon_Kasimov_Resume_AI_RAG_Agent_Engineer.md
.venv\Scripts\python.exe resumes\tools\build_resume.py --all   # every source under resumes/current/
```

What it does:

- Writes the DOCX with python-docx in one house style (A4; Arial for English, Malgun Gothic for
  Korean) and exports the PDF through Word, so the two files always match.
- Picks the largest body size between 8.5 and 10 pt that keeps the resume within its page budget
  (front matter `pages`, default 1). Only if the text still overflows at 8.5 pt does it tighten the
  line spacing, never below 1.2 times the font size.
- Turns visible email, LinkedIn, GitHub, and github.io addresses into real links.
- Runs `check_resume_pdf.py` on the result and exits non-zero if a rule fails. It writes only the
  resume's own `.docx` and `.pdf`; temporary attempts go to the system temp folder.

## `check_resume_pdf.py`

Read-only check of one or more PDFs against the resume standards and fact rules.

```powershell
.venv\Scripts\python.exe resumes\tools\check_resume_pdf.py resumes\current\korea\backend-e7-ko\Azizjon_Kasimov_Resume_Backend_E7_KO.pdf
.venv\Scripts\python.exe resumes\tools\check_resume_pdf.py <pdf> --pages 2 --no-honors
```

It fails a PDF that is longer than its page budget, lacks a text layer, has an unembedded font,
uses body text under 8.5 pt or any text under 8.0 pt, or shows an email or profile address without
a link. It also fails these fact errors: "Rex Innovation"; G-Man Auto Parts shown as "Present";
Java, Kotlin, or Rust listed as a skill (Java was one course and the AI tools wrote the Kotlin and
Rust); the Recs anomaly detection described as for or in a VPP; and a missing highest-honors line.
Use `--no-honors` for archived packets made before 2026-09-25.

## `export_docx_to_pdf.ps1`

Exports a `.docx` to PDF through Microsoft Word (COM automation), so the PDF matches the Word layout
and embeds the fonts. It reads the DOCX, writes only the requested PDF, and closes Word when done.
`build_resume.py` calls it; run it by hand for DOCX files built elsewhere, such as the
green-economy resume and archived packets.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File resumes\tools\export_docx_to_pdf.ps1 `
  -InputDocx path\to\Resume.docx -OutputPdf path\to\Resume.pdf
```

If a build stops with "Word did not finish exporting", close any stuck Word window or `WINWORD.EXE`
process and run it again.
