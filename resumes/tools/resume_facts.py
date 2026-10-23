"""Fact rules shared by the resume checkers.

check_resume_pdf.py applies them to the text blocks of a PDF, and check_resume_text.py to the
lines of an online platform resume. The facts come from the item files and the portfolio
PROJECT_CONTEXT: Recs Innovation is never "Rex"; G-Man Auto Parts ended in July 2026; Java was one
university course, and the AI coding tools wrote the Kotlin and Rust; the Recs anomaly detection
monitored solar power-plant data, and only its inference service was integrated into a Virtual
Power Plant (VPP) platform; and the degree's highest honors appear.
"""

import re
from pathlib import Path

SKILLS_MD = Path(__file__).resolve().parents[2] / "profile" / "skills.md"

# Latin-letter boundaries instead of \b, so "Java로" (a Korean particle attached) still counts.
NOT_LATIN_BEFORE = r"(?<![A-Za-z0-9_+#])"
NOT_LATIN_AFTER = r"(?![A-Za-z0-9_+#])"

AI_TOOLS = re.compile(r"Claude Code|Codex|coding agents?|AI-written|agent-built|built entirely", re.I)
COURSE = re.compile(r"course|수업|과목|이수|수강|강의", re.I)
VPP = re.compile(
    r"anomal\w*\s+detection\s+(?:for|on|in)\s+(?:a\s+|the\s+)?(?:commercial\s+)?(?:VPP|virtual\s+power\s+plant)"
    r"|Virtual Power Plant\s*용|VPP\s*용\s*AI"
    # "Virtual Power Plant AI Model", "VPP 이상탐지": the models served solar plants, not the VPP.
    r"|(?:(?<![A-Za-z])VPP|Virtual\s+Power\s+Plants?|가상\s*발전소)(?:\s*\((?:VPP|가상\s*발전소)\))?\s*(?:용\s*)?"
    r"(?:(?:AI|ML)(?![A-Za-z])|anomal|이상\s*(?:탐지|감지)|모델|models?(?![A-Za-z]))",
    re.I)

# (id, label, pattern, allowed): a match is a problem unless `allowed` matches the same text.
FACT_RULES = [
    ("rex", "company is Recs Innovation, never Rex", re.compile(r"\bRex\s*Innovation", re.I), None),
    ("java", "Java listed as a skill (it was one university course)",
     re.compile(NOT_LATIN_BEFORE + r"(?:Java|자바(?!\s*스크립트))" + NOT_LATIN_AFTER), COURSE),
    ("kotlin-rust", "Kotlin or Rust listed without saying AI tools wrote it",
     re.compile(NOT_LATIN_BEFORE + r"(?:Kotlin|Rust|코틀린|러스트)" + NOT_LATIN_AFTER), AI_TOOLS),
    ("vpp", "Recs AI described as for or in a VPP (it monitored solar plant data)", VPP, None),
]

GMAN = re.compile(r"G-?Man|지맨")
CURRENT_JOB = re.compile(r"\bPresent\b|현재|재직\s*중|근무\s*중", re.I)
HONORS = re.compile(r"highest honors|최우수", re.I)

# Spellings of the never-claim names besides the name itself; any other name is matched as written.
NAME_SPELLINGS = {
    "Java": [r"Java", r"자바(?!\s*스크립트)"],
    # Kept out of the public copy, like the never-claim list itself.
    "Kotlin": [r"Kotlin", r"코틀린"],
    "Rust": [r"Rust", r"러스트"],
    "C++": [r"C\+\+", r"CPP"],
}


def never_claim_terms(skills_md=SKILLS_MD):
    """Return the names in the "Never claim" list of profile/skills.md, such as Kotlin and C++.

    Each item there starts with its names in bold (`- **Rust or C++:** ...`), which keeps that list
    the one home of the rule. The public copy of the repo hides the list, so there it is empty.
    """
    text = Path(skills_md).read_text(encoding="utf-8")
    section = re.search(r"^## Never claim[ \t]*$(.*?)(?=^## |<!-- private:end -->|\Z)", text, re.M | re.S)
    if not section:
        return []
    terms = []
    for label in re.findall(r"^- \*\*(.+?):\*\*", section.group(1), re.M):
        terms += [name.strip() for name in re.split(r",|\bor\b", label) if name.strip()]
    return terms


def term_pattern(term):
    """Match a never-claim name, in any letter case and its common spellings, as a whole word."""
    spellings = NAME_SPELLINGS.get(term, [re.escape(term)])
    return re.compile(NOT_LATIN_BEFORE + "(?:" + "|".join(spellings) + ")" + NOT_LATIN_AFTER, re.I)
