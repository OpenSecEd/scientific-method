# Record of the session behind the review

The review in this directory was made in one session on 2026-11-12 by a
language model (Claude Fable 5.2 in Claude Code) directed by the author.
It started five further runs of a model (Claude Sonnet 5.5) for parts of
the work. This directory keeps what those runs were told and what they
reported, so that the work can be checked. The report's last appendix
("How the review was made") describes the session.

| File | What it is |
|---|---|
| `plan.md` | The plan the author approved before any file was written |
| `instructions/effect.txt`, `attribution.txt`, `sufficient.txt`, `necessary.txt` | The written instructions given to the four search runs, verbatim (started 10:16-10:17) |
| `instructions/read-through.txt` | The instructions for the run that read four papers in full (started 14:57) |
| `reports/*.md` | The full report each run wrote, unedited |
| `plan-first-version.md` | The plan as first written (09:54), before the author's comment on it |
| `asta-sources.md` | The 41 sources of Asta's report with our classification, our own 57 by the same kinds, and the checks made on Asta's citations (for the comparison appendix) |
| `scripts/verify_quotes.py` | Compares every quoted passage in a bibliography's provenance blocks with a directory of extracted full texts |
| `scripts/merge_bib.py` | Merged the four runs' bibliographies under common keys |

Things to know when reading them:

- The instructions and reports are as written at the time. They name a
  scratch directory under `/tmp` that no longer exists, and the runs'
  own bibliography keys, which `scripts/merge_bib.py` mapped to the keys
  in `../mfa.bib`.
- A report is a run's account of its own work, not a checked result.
  The second check corrected several of them: two sources were
  dropped, one grade changed, and four sentences written from abstracts
  were narrowed after the papers were read. The report's sections
  "Deviations from the protocol" and "How the review was made" say
  which.
- The search tool's records are in `../search/` (one export per session:
  every record with its status, tags, who decided and the model's
  confidence). The queries, dates and databases are in the report's
  appendix.
- The full texts are not here: they belong to their publishers. To rerun
  `verify_quotes.py`, extract your own copies to text
  (`pdftotext paper.pdf`) into one directory and run
  `python3 scripts/verify_quotes.py ../mfa.bib <that directory>`.
