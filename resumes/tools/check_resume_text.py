"""Check the text of an online platform resume (Wanted, Saramin, JobKorea) against the fact rules.

Usage (repo root, project venv):
    .venv\\Scripts\\python.exe resumes\\tools\\check_resume_text.py <capture.txt> [<capture.txt> ...] [--no-honors]

Read-only. Platform resumes are edited by hand in the browser, and they drifted twice with the same
wrong facts (Saramin on 2026-10-13, Wanted on 2026-10-21), so check the platform's own copy before
applying through it. capture_resume_text.js copies one as text (resumes/tools/README.md); "-"
reads the text from standard input. Every problem prints with its line and the text that matched,
and the exit code is 1 when anything is found. The fingerprint printed for each file must match
the one the capture script printed, or the text was changed while it was copied.

Each line gets the PDF checker's fact rules (resume_facts.py), and then the ones platform forms
need:
- G-Man Auto Parts shown as current: 재직 중, 현재, or Present beside its name or alone in its
  entry, or a period that starts in 2025.03 or 2025.04 and stays open (it ended in 2026.07);
- a name from the never-claim list in profile/skills.md in a skills list: a skills section, or a
  "관련기술:" or "Tech stack:" line (descriptions may still name features built with them);
- education: a degree other than 학사, 공학사, or B.S. (석사, 대학원, ...), a status other than
  graduated, Woosong dates other than 2020.09 - 2024.08, or the major written "Future
  Technologies" or "AI and Big Data" (it is 미래기술학부 데이터사이언스전공, Future Technology);
- the old Recs title "AI Developer" (the middle title is AI Engineer since 2026-10-05);
- an email address or phone number, because a saved capture must never hold contact details.
"""

import argparse
import re
import sys
from pathlib import Path

from resume_facts import (CURRENT_JOB, FACT_RULES, GMAN, HONORS, NOT_LATIN_AFTER, NOT_LATIN_BEFORE,
                          SKILLS_MD, never_claim_terms, term_pattern)

# Section titles, compared in lower case without spaces, "#", "*", or a colon.
SECTION_TITLES = {
    "experience": {"경력", "경력사항", "경력기술서", "경력및경험", "experience", "workexperience",
                   "professionalexperience", "employment", "career"},
    "education": {"학력", "학력사항", "학력및자격", "학력/자격", "education"},
    "skills": {"스킬", "기술", "기술스택", "핵심기술", "보유기술", "보유스킬", "업무스킬", "기술/스킬",
               "스킬/기술", "기술및역량", "핵심역량", "skills", "skill", "technicalskills", "techstack",
               "coreskills"},
    "other": {"간단소개", "소개", "자기소개", "요약", "summary", "about", "profile", "프로젝트",
              "주요프로젝트", "projects", "certifications", "awards", "언어", "외국어", "languages",
              "링크", "links", "portfolio", "ai활용경험", "활동", "activities", "교육", "연수", "기타"},
}
# A short plain line with one of these words also opens another section (Saramin's 자격증/어학/수상내역).
OTHER_TITLE_WORDS = re.compile(r"자격|수상|어학|자기소개|포트폴리오|희망|우대|병역|인적사항|기본정보|대외|교육이수|해외")

MONTHS = {name: number for number, name in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
DATE = (r"(?:(?:19|20)\d\d\s*(?:[./-]|년)\s*(?:1[0-2]|0?[1-9])(?!\d)\.?(?:\s*월)?"
        r"|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(?:19|20)\d\d)")
YEAR = r"(?:19|20)\d\d"
OPEN_END = r"현재|재직\s*중|근무\s*중|재학\s*중|진행\s*중|Present|Current|Now"
PERIOD = re.compile(
    rf"(?P<start>{DATE}|{YEAR})\s*(?:-|–|—|~|to|until)\s*"
    rf"(?:(?P<end>{DATE}|{YEAR})|(?P<open>{OPEN_END})|(?=\(|$))", re.I)
DATED = re.compile(rf"{DATE}\s*(?P<kind>입학|졸업)", re.I)
HAS_DATE = re.compile(rf"{DATE}|{YEAR}", re.I)
ALONE_CURRENT = re.compile(rf"[-~\s]*(?:{OPEN_END})(?:\s*\(.*\))?", re.I)

GMAN_LABEL = "G-Man shown as current (it ended in July 2026)"
RECS = re.compile(r"\bRe(?:cs|x)\s*Innovation|렉스\s*이노베이션", re.I)
OLD_TITLE = re.compile(r"\bAI\s+Developer\b", re.I)
OLD_TITLE_KO = re.compile(r"AI\s*개발자")
TITLE_CHAIN = re.compile(r"Team\s*Lead|\bIntern\b|팀장|인턴", re.I)
SKILL_LABEL = re.compile(
    r"[\s\-*•·]*(?:\*\*)?\s*(?:관련\s*기술|사용\s*기술|기술\s*스택|보유\s*기술|핵심\s*기술|개발\s*언어|스킬|기술"
    r"|Tech(?:nolog(?:y|ies))?(?:\s*Stack)?|Stack|Skills?|Tools|Languages?)\s*(?:\*\*)?\s*[:：]", re.I)

SCHOOL = re.compile(r"우송|Woosong|University|College|High\s*School|고등학교|대학교(?!\s*\()|어학당|Academy|"
                    r"아카데미|Institute", re.I)
WOOSONG = re.compile(r"우송|Woosong", re.I)
WOOSONG_START, WOOSONG_END = (2020, 9), (2024, 8)
WRONG_DEGREE = re.compile(
    r"석사|박사|대학원|전문학사|이학사|문학사|전문대|대학교?\s*\(\s*2\s*,?\s*3\s*년\s*\)"
    rf"|{NOT_LATIN_BEFORE}(?:Master(?:'s)?|M\.\s?S\.|M\.?Sc|MBA|Ph\.?\s?D|Doctor\w*|B\.\s?A\.){NOT_LATIN_AFTER}"
    r"|Bachelor of Arts|Associate(?:'s)?\s+(?:degree|of)", re.I)
WRONG_STATUS = re.compile(r"재학|휴학|중퇴|자퇴|수료|졸업\s*예정|Enrolled|Expected", re.I)
PLURAL_MAJOR = re.compile(r"Future\s+Technologies", re.I)
RENAMED_MAJOR = re.compile(
    r"(?:AI|Artificial\s+Intelligence)\s*(?:and|&)\s*Big\s*Data|인공지능\s*(?:및|과|·|/)?\s*빅\s*데이터", re.I)

EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
PHONE = re.compile(r"(?:\+?82[\s.()-]*0?|(?<!\d)0)1[016789][\s.()-]*\d{3,4}[\s.()-]*\d{4}(?!\d)"
                   r"|\+\d{1,3}(?:[\s.()-]*\d{2,4}){3,4}")


def section_of(line):
    """Return the section a title line opens ("experience", "education", ...), or None."""
    markdown = re.match(r"\s*#{1,2}(?!#)\s*(.*)", line)
    key = re.sub(r"[\s#*:：]", "", markdown.group(1) if markdown else line).lower()
    key = re.sub(r"(?:총)?\d+년(?:\d+개월)?$|\d+개월$|\(\d+\)$", "", key)
    for section, titles in SECTION_TITLES.items():
        if key in titles:
            return section
    if markdown or (key and len(key) <= 15 and not re.search(r"\d", key) and OTHER_TITLE_WORDS.search(key)):
        return "other"
    return None


def parse_date(text):
    """Return (year, month or None) for a date such as 2024.08, 2024년 8월, Aug 2024, or 2024."""
    year = int(re.search(YEAR, text).group(0))
    numeric = re.search(rf"{YEAR}\s*(?:[./-]|년)\s*(\d{{1,2}})", text)
    if numeric:
        return year, int(numeric.group(1))
    name = re.match(r"[A-Za-z]{3}", text)
    return year, MONTHS[name.group(0).lower()] if name else None


def same_month(found, expected):
    """A year without a month matches any month of the expected year."""
    return found[0] == expected[0] and found[1] in (None, expected[1])


def open_gman_period(line):
    """Return a period that starts when G-Man did (2025.03 or 2025.04) and has no end, or None."""
    for period in PERIOD.finditer(line):
        year, month = parse_date(period.group("start"))
        if period.group("end") is None and year == 2025 and month in (None, 3, 4):
            return period.group(0).strip()
    return None


def wrong_woosong_dates(line):
    """Return the first study period or 입학/졸업 date that differs from 2020.09 - 2024.08, or None."""
    for period in PERIOD.finditer(line):
        end = period.group("end")
        if not (same_month(parse_date(period.group("start")), WOOSONG_START)
                and end and same_month(parse_date(end), WOOSONG_END)):
            return period.group(0).strip()
    for dated in DATED.finditer(line):
        expected = WOOSONG_START if dated.group("kind") == "입학" else WOOSONG_END
        if not same_month(parse_date(dated.group(0)), expected):
            return dated.group(0)
    return None


def education_entries(lines):
    """Map each line number inside an education section to its school: "woosong", "other", or None.

    An entry starts at a line naming a school; lines above the first such line in a section (a
    period shown before the school name) belong to the entry below them.
    """
    entries, pending, section, school = {}, [], None, None
    for number, line in enumerate(lines, 1):
        opened = section_of(line)
        if opened:
            entries.update(dict.fromkeys(pending))
            section, school, pending = opened, None, []
            continue
        if section != "education":
            continue
        if SCHOOL.search(line):
            school = "woosong" if WOOSONG.search(line) else "other"
            entries.update(dict.fromkeys(pending, school))
            pending = []
        if school is None:
            pending.append(number)
        else:
            entries[number] = school
    entries.update(dict.fromkeys(pending))
    return entries


def check(text, terms, require_honors=True):
    """Return the problems in a platform resume's text, in line order.

    Each problem is (line number or None, rule id, label, matched text, line). `terms` is the
    never-claim list (never_claim_terms()).
    """
    lines = text.splitlines()
    # Java, Kotlin, and Rust already break a fact rule anywhere, so only the other names need this.
    skill_terms = [(term, term_pattern(term)) for term in terms
                   if not any(pattern.search(term) for _, _, pattern, _ in FACT_RULES)]
    education = education_entries(lines)
    has_education_section = any(section_of(line) == "education" for line in lines)
    problems = {}

    def report(number, rule, label, match, line=""):
        problems.setdefault((number, label), (number, rule, label, match, line))

    section = company = None
    company_line = 0
    for number, line in enumerate(lines, 1):
        opened = section_of(line)
        if opened:
            section, company = opened, None
        elif section == "experience":
            if RECS.search(line):
                company, company_line = "recs", number
            elif GMAN.search(line):
                company, company_line = "gman", number
            elif line.lstrip().startswith("###"):
                company = None

        for rule, label, pattern, allowed in FACT_RULES:
            match = pattern.search(line)
            if match and not (allowed and allowed.search(line)):
                report(number, rule, label, match.group(0), line)

        current = CURRENT_JOB.search(line) if GMAN.search(line) else None
        current = current and current.group(0) or open_gman_period(line)
        # A status line of its own ("재직중") counts only close under the G-Man name.
        near_gman = company == "gman" and number - company_line <= 3
        if not current and near_gman and ALONE_CURRENT.fullmatch(line.strip()):
            current = line.strip()
        if current:
            report(number, "gman-current", GMAN_LABEL, current, line)

        if section == "skills" or SKILL_LABEL.match(line):
            for term, pattern in skill_terms:
                match = pattern.search(line)
                if match:
                    report(number, "never-claim-skill",
                           f"{term} listed as a skill (never-claim list in profile/skills.md)", match.group(0), line)

        title = OLD_TITLE.search(line)
        if not (title and (company == "recs" or RECS.search(line) or TITLE_CHAIN.search(line))):
            title = OLD_TITLE_KO.search(line) if TITLE_CHAIN.search(line) else None
        if title:
            report(number, "ai-developer", "old Recs title AI Developer (it is AI Engineer)", title.group(0), line)

        woosong_line = not has_education_section and WOOSONG.search(line)
        if number in education or woosong_line:
            for rule, label, pattern in (
                    ("degree", "degree other than 학사/공학사 (B.S.)", WRONG_DEGREE),
                    ("major", "major is 미래기술학부 데이터사이언스전공 (Future Technology)", RENAMED_MAJOR)):
                match = pattern.search(line)
                if match:
                    report(number, rule, label, match.group(0), line)
        if (education.get(number) == "woosong" or woosong_line) and (SCHOOL.search(line) or HAS_DATE.search(line)):
            status = WRONG_STATUS.search(line)
            if status:
                report(number, "edu-status", "education status other than 졸업 (graduated 2024.08)",
                       status.group(0), line)
            dates = wrong_woosong_dates(line)
            if dates:
                report(number, "edu-dates", "Woosong dates other than 2020.09 - 2024.08", dates, line)
        plural = PLURAL_MAJOR.search(line)
        if plural:
            report(number, "major", "major is 미래기술학부 데이터사이언스전공 (Future Technology)", plural.group(0), line)

        for pattern, kind in ((EMAIL, "[email]"), (PHONE, "[phone]")):
            if pattern.search(line):
                report(number, "contact", "contact details in a saved capture (recapture without them)", kind)

    if require_honors and not HONORS.search(text):
        report(None, "honors", "highest honors (최우수) missing", "")
    return sorted(problems.values(), key=lambda problem: problem[0] or len(lines) + 1)


def fingerprint(text):
    """FNV-1a of the text's UTF-8 bytes, which capture_resume_text.js prints for its capture."""
    value = 0x811C9DC5
    for byte in text.strip().encode("utf-8"):
        value = ((value ^ byte) * 0x01000193) & 0xFFFFFFFF
    return f"{value:08x}"


def describe(problem):
    number, _, label, match, line = problem
    where = f"line {number}" if number else "resume"
    shown = " ".join(line.split())
    if len(shown) > 100:
        shown = shown[:97] + "..."
    if not match:
        return f"  {where}: {label}"
    if not line or match == shown:
        return f"  {where}: {label}: '{match}'"
    return f"  {where}: {label}: '{match}' in '{shown}'"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="+", help="captured resume text; - reads standard input")
    parser.add_argument("--no-honors", action="store_true", help="do not require the highest-honors line")
    args = parser.parse_args()
    # Piped output on Windows otherwise uses the ANSI code page and fails on Korean text.
    sys.stdout.reconfigure(encoding="utf-8")

    terms = never_claim_terms()
    if not terms:
        parser.error(f"no '## Never claim' list with '- **Name:**' items in {SKILLS_MD}")
    for name in args.files:
        if name != "-" and not Path(name).is_file():
            parser.error(f"no such file: {name}")

    failed = 0
    for name in args.files:
        data = sys.stdin.buffer.read() if name == "-" else Path(name).read_bytes()
        text = data.decode("utf-8-sig").replace("\r\n", "\n")
        problems = check(text, terms, not args.no_honors)
        result = f"{len(problems)} problem(s)" if problems else "no problems"
        print(f"{name}: {result} (fingerprint {fingerprint(text)})")
        for problem in problems:
            print(describe(problem))
        failed += bool(problems)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
