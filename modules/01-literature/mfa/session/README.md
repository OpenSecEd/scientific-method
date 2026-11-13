# Record of the session behind the review

The review in this directory was made in a session on 2026-11-12, extended
on 2026-11-13, by a language model (Claude Fable 5.2 in Claude Code)
directed by the author. It started five further runs of a model (Claude
Sonnet 5.5) for parts of the work on the first day and four on the
second. A third round, on the afternoon of the second day, was made
by the lead alone. This directory keeps what those runs were told and what they
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

## Second round (2026-11-13): `round2/`

The author read draft 5 and ruled that a search is never limited. Every
search that had returned the 40 records allowed, and the four that IEEE
Xplore had not answered, were run again without a limit, and the new
records were screened.

| File | What it is |
|---|---|
| `round2/brief.md` | The instructions common to the four screening runs |
| `round2/instructions/*.txt` | What each run was told in addition, verbatim (started 07:37), and the message that restarted the sufficiency run at 09:02 |
| `round2/reports/*.md` | The full report each run wrote, unedited |
| `round2/worklist.json`, `round2/counts.json` | The searches that were repeated, and the number of records each returned without a limit |
| `round2/scripts/run.py`, `add.py` | Ran the repeated searches and added their records to the sessions |
| `round2/scripts/oa_ta.py` | Added the OpenAlex records that match a query in title or abstract (the tool itself matches full text): the provider's own code with one function replaced |
| `round2/scripts/relabel.py` | Gave every record discarded as adjacent the label of an exclusion criterion (by a model, from title and abstract) |
| `round2/scripts/retag.py` | Changes a record's category, which the tool's own command cannot |
| `round2/scripts/cited_only.py`, `strip_themes.py` | Keep the tags that mark cited sources only on records that are in the bibliography |
| `round2/scripts/export.sh`, `strip_abstracts.py` | Regenerate the hit lists and the exports in `../search/` |
| `round2/scripts/count.py` | Counted the new records per question before the author decided what to screen |

- The decisions on what to screen and what to read were the author's,
  taken when the counts were known; the report's section "Deviations from
  the protocol" states them.
- The lead checked the runs' quoted passages against the texts, corrected
  tags in the sessions (a cited record that a run had left discarded, a
  wrong theme), and added one source itself (`Woods2023MetaReview`).
  It did not follow one proposal: the sufficiency run wanted a cell of the
  table of local threats changed on the strength of `Roche2021Titan`; the
  note above that entry in `../mfa.bib` says why not. It also corrected two
  statements in the runs' reports (a NIST report called a draft; a paper
  listed as not cited that the report already cites).
- The scripts were written for this session and are kept as a record of
  what was done, not as tools: they contain paths of the scratch
  directory.


## Third round (2026-11-13, afternoon): `round3/`

The comparison with Asta's report had shown a study of account recovery
(Klivan et al. 2023, `Klivan2023Recovery`) that two rounds of search had
not returned. The author asked why, then asked for queries that find it
and for the story to be told. The report's appendix "A study that the
search missed" is that story; this is its record.

| File | What it is |
|---|---|
| `round3/queries.json`, `round3/worklist.json` | The three added queries, and each as sent to each database |
| `round3/scripts/go.sh` | Ran them: `add.py` (Web of Science, Scopus, IEEE Xplore, arXiv, into the session `mfa-sufficient`), `oa_ta.py` (OpenAlex, title or abstract, into the session), `run.py openalex` (OpenAlex full text, to a file only) |
| `round3/logs/` | What those runs logged: one line per search, with counts |
| `round3/scripts/fill_abstracts.py` | Added abstracts from OpenAlex to the new records that had none (the tool's own command goes through the whole session) |
| `round3/scripts/classify.sh`, `pending.py` | Classified the 409 new records, a hundred at a time |
| `round3/scripts/oa_abstracts.py`, `round3/oa-abstracts.json` | Compared, for 48 records, the length of the abstract in Web of Science with that in OpenAlex |
| `round3/scripts/oa_semantic.py`, `round3/semantic/` | Asked OpenAlex's search by meaning two questions; the 50 works returned for each, in order, with how our screening had classified them (`*.txt` as after the third round; the report's table gives the state before it) |
| `round3/scripts/s2probe.py`, `round3/s2/` | The same two questions to Semantic Scholar's public search without a key: every attempt was answered "too many requests" |

- Where the study was, before the round: in no session; in the files of
  OpenAlex full-text matches of the second round for 13 of 20 queries
  (scratch files, not kept: the lists belong to the database). The check
  against Web of Science was `scholar search '"Multi-Factor
  Authentication Recovery Deployments"' -p wos -f json`.
- The lead read the records the model filed as bearing or was unsure of,
  and changed eight decisions and two labels with `round2/scripts/retag.py`;
  the report's section "Deviations from the protocol" gives the counts.
  `round2/scripts/export.sh` gained the theme `device-loss`.
- A search with alphaXiv's `discover_papers` (question: "an attacker uses
  account recovery or a weaker fallback login to get around multi-factor
  authentication") was tried three times and did not answer. It counts as
  failed.
- The 39 works that the search by meaning returned and our records lack
  (`semantic/*.txt`, "not in our records") were not screened.
- Four papers were read for this round: Klivan et al. 2023 (arXiv
  version), Gilsenan et al. 2023, Bhardwaj et al. 2025, and the paper on
  Scholar QA (Singh et al. 2025); the provenance blocks in `../mfa.bib`
  say which sections. Frymann et al. 2020 could be read only as an
  abstract.
