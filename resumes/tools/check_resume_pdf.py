"""Check resume PDFs against the repo's resume standards and fact rules.

Usage (repo root, project venv):
    .venv\\Scripts\\python.exe resumes\\tools\\check_resume_pdf.py <pdf> [<pdf> ...] [--pages N] [--no-honors]

Read-only. For each PDF it reports pages, body font size, smallest font size, fonts, and link
targets, and fails (exit code 1) when any rule below is broken:

- Layout: at most N pages (default 1), an extractable text layer, every font embedded, body text
  of at least 8.5 pt, and no text smaller than 8.0 pt.
- Links: every visible email, LinkedIn, GitHub, or github.io address has a real /URI annotation.
- Facts (see the portfolio PROJECT_CONTEXT and profile/skills.md): "Recs Innovation" is never
  "Rex"; G-Man Auto Parts ended in July 2026, so it is never "Present"; Java (one course), Kotlin
  and Rust (written by AI tools) are never listed as skills; the Recs anomaly detection monitored
  solar power-plant data and is never described as detecting anomalies for or in a VPP; and the
  degree's highest honors appear (skip with --no-honors for archived packets).
"""

import argparse
import collections
import json
import re
import sys
from pathlib import Path

import fitz

MIN_BODY_PT = 8.5
MIN_ANY_PT = 8.0

# Visible address patterns and the link target each one must carry.
LINK_PATTERNS = [
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]*\w"), lambda m: "mailto:" + m),
    (re.compile(r"(?:www\.)?linkedin\.com/in/[\w-]+/?"),
     lambda m: "https://www.linkedin.com/in/" + m.split("/in/")[1].strip("/") + "/"),
    (re.compile(r"(?<![\w.])github\.com/[\w-]+(?:/[\w.-]*\w)?"), lambda m: "https://" + m),
    (re.compile(r"[\w-]+\.github\.io(?:/[\w./-]*)?"), lambda m: "https://" + m),
]

FACT_RULES = [
    ("company is Recs Innovation, never Rex", re.compile(r"\bRex Innovation\b"), None),
    ("Java listed as a skill (it was one university course)",
     re.compile(r"\bJava\b"), re.compile(r"course|수업|과목", re.I)),
    ("Kotlin or Rust listed without saying AI tools wrote it",
     re.compile(r"\bKotlin\b|\bRust\b"),
     re.compile(r"Claude Code|Codex|coding agents?|AI-written|agent-built|built entirely", re.I)),
    ("Recs anomaly detection described as for or in a VPP",
     re.compile(r"anomal\w*\s+detection\s+(?:for|on|in)\s+(?:a\s+|the\s+)?(?:commercial\s+)?"
                r"(?:VPP|virtual\s+power\s+plant)|Virtual Power Plant\s*용|VPP\s*용\s*AI", re.I),
     None),
]


def expected_uri(match_text):
    for pattern, to_uri in LINK_PATTERNS:
        if pattern.fullmatch(match_text):
            return to_uri(match_text)
    return None


def normalize_uri(uri):
    """Compare links without scheme, www., letter case, or a trailing slash."""
    uri = re.sub(r"^(?:https?://)?(?:www\.)?", "", uri.strip().lower())
    return uri.rstrip("/")


def check(pdf_path, max_pages=1, require_honors=True):
    pdf = fitz.open(pdf_path)
    text = "".join(page.get_text() for page in pdf)
    blocks = [b[4] for page in pdf for b in page.get_text("blocks") if b[4].strip()]
    uris = {link["uri"] for page in pdf for link in page.get_links() if link.get("uri")}

    sizes = collections.Counter()
    smallest = 99.0
    for page in pdf:
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    chars = len(span["text"].strip())
                    if chars:
                        size = round(span["size"], 1)
                        sizes[size] += chars
                        if chars >= 3:
                            smallest = min(smallest, size)
    body = sizes.most_common(1)[0][0] if sizes else 0.0
    fonts = sorted({f[3].split("+")[-1] for page in pdf for f in page.get_fonts()})
    unembedded = sorted({f[3] for page in pdf for f in page.get_fonts() if f[1] == "n/a"})

    problems = []
    if pdf.page_count > max_pages:
        problems.append(f"{pdf.page_count} pages; at most {max_pages} allowed")
    if len(text) < 1500:
        problems.append("text layer looks incomplete")
    if unembedded:
        problems.append(f"unembedded fonts: {unembedded}")
    if body < MIN_BODY_PT:
        problems.append(f"body text is {body} pt; minimum {MIN_BODY_PT} pt")
    if smallest < MIN_ANY_PT:
        problems.append(f"smallest text is {smallest} pt; minimum {MIN_ANY_PT} pt")

    flat = re.sub(r"\s+", " ", text)
    linked = {normalize_uri(u) for u in uris}
    for pattern, _ in LINK_PATTERNS:
        for match in pattern.finditer(flat):
            uri = expected_uri(match.group(0).rstrip("./"))
            if uri and normalize_uri(uri) not in linked:
                problems.append(f"no link annotation for visible '{match.group(0)}' (expected {uri})")

    for label, pattern, allowed in FACT_RULES:
        for block in blocks:
            if pattern.search(block) and not (allowed and allowed.search(block)):
                problems.append(f"{label}: '{' '.join(block.split())[:90]}'")
    for block in blocks:
        if "G-Man" in block and re.search(r"\bPresent\b|현재", block, re.I):
            problems.append(f"G-Man shown as current: '{' '.join(block.split())[:90]}'")
    if require_honors and not re.search(r"highest honors|최우수", text, re.I):
        problems.append("highest honors (최우수) missing")

    report = {
        "pdf": str(pdf_path),
        "pages": pdf.page_count,
        "body_pt": body,
        "smallest_pt": smallest,
        "fonts": fonts,
        "uris": sorted(uris),
        "problems": problems,
    }
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pdfs", nargs="+", type=Path)
    parser.add_argument("--pages", type=int, default=1, help="maximum pages allowed (default 1)")
    parser.add_argument("--no-honors", action="store_true", help="do not require the highest-honors line")
    args = parser.parse_args()

    failed = 0
    for pdf in args.pdfs:
        report = check(pdf, args.pages, not args.no_honors)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        failed += bool(report["problems"])
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
