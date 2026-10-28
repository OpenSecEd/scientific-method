#!/usr/bin/env python3
"""Generate the "About you" slides from the course's "About you" survey.

Run with the interpreter of the canvaslms installation (see the Makefile):

    $PY -I about-you.py COURSE_REGEX > about-you.tex

One beamer frame per multiple-choice question, from Canvas' quiz statistics
(counts only), except the consent question for pedagogical research.  One
frame summarizing the free-text answers about research interests: the answers
go straight from the quiz report to `llm` (its default model) and only the
summary is written.  No answer, name or other personal data is printed.
"""
import re
import subprocess
import sys

from canvasapi import Canvas
from canvaslms.cli.courses import filter_courses
from canvaslms.cli.login import load_credentials
from canvaslms.cli.quizzes import download_csv_report, poll_progress

QUIZ_TITLE = "About you"
EXCLUDE = re.compile(r"pedagogical research", re.I)
INTERESTS = re.compile(r"interest you the most", re.I)
SHORT_TITLES = [
    (re.compile(r"Have you taken AK2030", re.I),
     "Have you taken AK2030 TaMoS?"),
    (re.compile(r"courses that you have taken", re.I),
     "Courses you have taken"),
    (re.compile(r"courses that you are currently taking", re.I),
     "Courses you are currently taking"),
]
COLUMNS_FROM = 6  # items; longer lists are set in two columns
TINY_FROM = 12  # items; even longer lists also in a smaller font
SUMMARY_PROMPT = """\
The input is a list of students' answers to the question "What research
questions or areas in cybersecurity interest you the most?", separated by
lines with three dashes. Group them into at most 14 areas and count how many
students mention each area (a student may count in several areas). Output
only lines of the form

\\item Area name: N

sorted by N, highest first, with plain-text area names. Output nothing else.
"""


def latex(text):
    """Escape the LaTeX special characters in plain text."""
    text = re.sub(r"<[^>]+>", "", text).strip()
    for char, repl in (("\\", r"\textbackslash{}"), ("&", r"\&"),
                       ("%", r"\%"), ("$", r"\$"), ("#", r"\#"),
                       ("_", r"\_"), ("{", r"\{"), ("}", r"\}"),
                       ("~", r"\textasciitilde{}"), ("^", r"\^{}")):
        text = text.replace(char, repl)
    return text


def title_for(question_text):
    for pattern, title in SHORT_TITLES:
        if pattern.search(question_text):
            return title
    return latex(question_text)


def choice_frame(stat):
    """A frame with the counts of one multiple-choice question."""
    responses = stat["responses"]
    answers = sorted((a for a in stat["answers"]
                      if a.get("responses") and a.get("text") != "No Answer"),
                     key=lambda a: -a["responses"])
    selections = sum(a["responses"] for a in answers)
    items = [f"    \\item {latex(a['text'])}: {a['responses']} "
             f"({100 * a['responses'] / responses:.1f}\\%)"
             for a in answers]
    head = f"  \\emph{{Total responses:}} {responses}"
    if stat["question_type"] == "multiple_answers_question":
        head += f"\\qquad\n  \\emph{{Total selections:}} {selections}"
    body = "\n".join(items)
    if len(items) >= COLUMNS_FROM:
        size = "\\tiny" if len(items) >= TINY_FROM else "\\scriptsize"
        body = (f"  \\begin{{multicols}}{{2}}{size}\n"
                f"  \\begin{{itemize}}\n{body}\n  \\end{{itemize}}\n"
                "  \\end{multicols}")
    else:
        body = f"  \\begin{{itemize}}\n{body}\n  \\end{{itemize}}"
    return (f"\\begin{{frame}}\n  \\begin{{block}}{{"
            f"{title_for(stat['question_text'])}}}\n{head}\n{body}\n"
            "  \\end{block}\n\\end{frame}\n")


def interest_answers(quiz):
    """The free-text answers about interests, from the student analysis."""
    report = quiz.create_report(report_type="student_analysis",
                                includes_all_versions=True)
    report = poll_progress(
        report, refresh=lambda current: quiz.get_quiz_report(current.id)
    ) or report
    url = report.file["url"] if isinstance(report.file, dict) \
        else report.file.url
    rows = download_csv_report(url)
    column = next((c for c in rows.fieldnames if INTERESTS.search(c)), None)
    if column is None:
        sys.exit("about-you.py: no interests question in the report")
    return [row[column].strip() for row in rows if row[column].strip()]


def interests_frame(answers):
    """A frame with the llm summary of the interests; the answers stay here."""
    summary = subprocess.run(["llm", "prompt", "--no-stream", SUMMARY_PROMPT],
                             input="\n---\n".join(answers), text=True,
                             capture_output=True, check=True).stdout
    items = []
    for line in summary.strip().splitlines():
        match = re.fullmatch(r"\\item\s+(.+?):\s*(\d+)\s*", line.strip())
        if not match or int(match.group(2)) > len(answers):
            sys.exit("about-you.py: unexpected summary line from llm; "
                     "not writing the interests frame")
        items.append(f"    \\item {latex(match.group(1))}: {match.group(2)}")
    return ("\\begin{frame}\n  \\begin{block}{Qualitative summary: "
            "Interests in cybersecurity}\n    \\scriptsize\n"
            f"  \\emph{{Individual responses:}} {len(answers)}\n"
            "  \\begin{itemize}\n" + "\n".join(items) +
            "\n  \\end{itemize}\n  \\end{block}\n\\end{frame}\n")


def main():
    host, token = load_credentials({})
    if not host.startswith("http"):
        host = "https://" + host
    canvas = Canvas(host, token)
    courses = list(filter_courses(canvas, sys.argv[1]))
    if len(courses) != 1:
        sys.exit(f"about-you.py: {len(courses)} courses match {sys.argv[1]}")
    quiz = next(q for q in courses[0].get_quizzes() if q.title == QUIZ_TITLE)
    stats = next(iter(quiz.get_statistics()))
    frames = [choice_frame(s) for s in stats.question_statistics
              if s["question_type"] in ("multiple_choice_question",
                                        "multiple_answers_question")
              and not EXCLUDE.search(s["question_text"])
              and s.get("responses")]
    answers = interest_answers(quiz)
    if answers:
        frames.append(interests_frame(answers))
    print("\\subsection{Some stats}\n")
    print("\n".join(frames))


if __name__ == "__main__":
    main()
