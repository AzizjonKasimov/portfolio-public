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
a link. It also fails these fact errors, whose rules live in `resume_facts.py` and are shared with
`check_resume_text.py`: "Rex Innovation"; G-Man Auto Parts shown as "Present" or 재직 중; Java,
Kotlin, or Rust listed as a skill (Java was one course and the AI tools wrote the Kotlin and Rust);
the Recs anomaly detection or its models described as for or in a VPP; and a missing
highest-honors line. Use `--no-honors` for archived packets made before 2026-09-25.

## `check_resume_text.py` and `capture_resume_text.js`

Read-only check of an online platform resume (Wanted, Saramin, JobKorea) against the same fact
rules. Those resumes are edited by hand in the browser, outside the builder, and they drifted twice
with the same wrong facts, so check the platform's own copy before applying through it or
accepting a Wanted interview proposal (which sends no file, only the online resume). Check it also after
uploading a PDF to a platform, because the platform turns the PDF into its own resume: Wanted's
conversion once turned "B.S., 2020-2024" into 대학원 / 석사 with 2020.01-2024.01. Read the
editor's fields, not the platform's PDF export, which may leave fields out (Wanted's prints no
degree level).

```powershell
.venv\Scripts\python.exe resumes\tools\check_resume_text.py $env:TEMP\wanted-resume.txt
```

It prints each problem with its line and the text that matched, and exits with 1 when it finds
any; `-` in place of a file reads standard input. Besides the PDF fact rules, it fails:

- G-Man shown as current: 재직 중, 현재, or Present beside its name, or a period that starts in
  2025.03 or 2025.04 and has no end (it ended in 2026.07);
- a name from the never-claim list in `profile/skills.md`, read from that file, in a skills list:
  a skills section, or a `관련기술:` or `Tech stack:` line. Descriptions may still name features
  built with them;
- education other than one 공학사 (B.S.) from Woosong, 2020.09 - 2024.08: 대학원, 석사, or another
  degree, other dates, a status other than 졸업, or the major written "Future Technologies" or
  "AI and Big Data";
- the old Recs title AI Developer;
- an email address or phone number in the file.

`--no-honors` skips the highest-honors check, as in the PDF checker.

### Capturing a platform resume

`capture_resume_text.js` copies the open resume as text. It changes nothing on the page, and it
replaces email addresses and phone numbers with `[email]` and `[phone]`; never save a copy that
still holds them.

1. Open the resume in Chrome with the Claude in Chrome extension.
   - Wanted: open `wanted.co.kr/cv/list` and click the resume's title, which opens its editor at
     `wanted.co.kr/cv/<id>`. Do not type or click in the form.
   - Saramin and JobKorea: open the resume's own view page. Not tested yet (see below).
2. Run the whole of `capture_resume_text.js` with the extension's JavaScript tool. It answers with
   a line such as `86 lines, 4245 characters, fingerprint 95da9bce, 5 chunks`.
3. The tool cuts its output near 1,000 characters, so read `window.__resumeChunks[0]`, `[1]`, and
   so on (one `browser_batch` call can read them all), and join the pieces with newlines.
4. Save the text outside the repo, for example in `%TEMP%`, and run the check. It prints the
   fingerprint of the file it read; if that differs from the capture's, the copy has a slip (a
   wrong fact "corrected" while copying hides the very error the check looks for), so save the
   chunks again. Delete the file when done.

Why a script and not the page text: the Wanted editor keeps company names, titles, the school,
the major, and descriptions in input fields, which page text leaves out. Its education level and
degree are custom dropdowns: a chosen value is drawn in dark text, and an empty one shows a grey
placeholder marked `data-placeholder="true"`. The script reads the fields, keeps only chosen
values, drops faint placeholder text (an empty `YYYY.MM`) and unticked checkboxes with their
labels, marks section titles with `## `, and joins items shown side by side into one line, such
as `2025.04 - 재직 중 (1년 7개월)`. On Wanted it reads only the resume
(`[class*="ResumeDetail_ResumeDetail__wrapper"]`), not the job suggestions beside it; elsewhere it
reads `main` or the whole page. To read another part of a page, set
`window.__resumeRoot = '<CSS selector>'` before running it.

The script has been tried only on Wanted so far (2026-10-21). On the first capture from Saramin or
JobKorea, check that the text holds the career, education, and skills entries and no menus or job
suggestions, then note the page address, and a root selector if one was needed, in this section.


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
