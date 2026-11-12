# Plan: Is MFA necessary or sufficient for secure user authentication? (LaTeX report draft)

## Context

You asked for research on whether multi-factor authentication (MFA) is
*necessary* or *sufficient* for secure authentication of users, delivered as
a LaTeX report draft with the PDF on your reMarkable. The question mirrors
the course's own reflection prompt ("does MFA actually improve security —
how would you explore the literature, which review type?",
`canvas/04-case-study-passwords-literature/assignments/reflection-on-literature-reviews.md`)
and the MFA claim in `modules/05-scientificity/seminar.tex`, so the report
can also serve as a worked example of a documented literature search.

Nothing exists yet: `modules/01-literature/` is empty, and the old scholar
session "MFA literature seminar" only holds material-flow-analysis false
hits (nothing to reuse).

## What the report will answer

The question is ill-posed until "secure authentication" is defined, so the
report fixes definitions first (MFA and assurance levels from the standards
literature; an explicit threat model: remote guessing/stuffing, phishing
incl. real-time relay, device/SIM takeover, session theft, recovery
fallback) and then answers three questions, each two-sidedly:

- **RQ1 (effect)** — Does MFA reduce account compromise, by how much, and
  for which factor types? (prerequisite for both others)
- **RQ2 (sufficiency)** — Does deploying MFA suffice, i.e. are MFA-protected
  accounts secure under the stated threat model? Counter-evidence sought:
  documented bypasses, fallback/recovery weaknesses, usability-driven
  failures.
- **RQ3 (necessity)** — Is there no non-MFA way to reach comparable
  security? Counter-evidence sought: single-factor cryptographic
  authenticators, risk-based authentication, password managers; what
  standards actually require at which level.

My expectation (neither strictly necessary nor sufficient, but a large risk
reduction, strongly dependent on factor type) is recorded as a hypothesis
only. Searches are symmetric so it can fail, and the subagent prompts state
the claims to test, not the expected answer. One known trap to handle
explicitly: passkeys with user verification count as MFA under the standard
definitions, so "passwordless" is not evidence against necessity by itself.

Review type: a **rapid, scoping-style review with a systematic, documented
search** — not a full SLR. The method section says so and why.

## Approach

1. **Search (backing-claims protocol), three parallel strands.** One named
   `scholar` session per RQ: `mfa-effect`, `mfa-sufficient`,
   `mfa-necessary`. Each strand: topic-driven support *and* counter queries
   with mirrored vocabulary ("multi-factor authentication", "two-factor
   authentication", 2FA, MFA, "two-step verification", plus strand terms),
   every query on every live provider — OpenAlex, Web of Science, Scopus,
   IEEE Xplore, arXiv (field syntax translated per provider). Semantic
   Scholar (key rejected, HTTP 403) and DBLP (anti-bot page) are down today
   and are reported as *not searched*. Standards and industry measurement
   reports (grey literature) are found via documented WebSearch complements
   and retrieved as known items.
   - Delegated to 3 subagents, `subagent_type: long-job`, `model: sonnet`
     (LLM classification of a few hundred hits can exceed 4 minutes), each
     with the skill's delegation preamble; each writes a provenance `.bib`,
     session export and full report to the scratchpad.
   - Full texts via `~/.claude/skills/backing-claims/scripts/fetch_pdf.py`
     (scholar's PDF cache; KTH tunnel for closed access, stopping at any
     bot check or login form).
   - Sessions classified (`scholar llm context` / `classify --no-examples`,
     tags supports / qualifies / adjacent / off-topic), low-confidence and
     every qualifying row read by hand.
2. **My own verification pass.** I read the `.bib` files, not the agents'
   summaries: every load-bearing quote is checked against the cached full
   text, duplicates merged, unverifiable sources dropped and listed as
   dropped. `check_provenance.py` and `check_metadata.py` over the merged bib.
3. **Write the report** (English; skills: scientific-writing, latex-writing):
   introduction with definitions, threat model, restatable RQs and
   hypotheses → method (review type, date, databases and their health,
   query × database × hits tables, screening) → results per RQ with
   verbatim quotes for load-bearing sources and corroborations cited with a
   finding each → discussion and limitations (observational vendor data,
   40-hit caps, dead providers) → conclusion whose first sentences answer
   "necessary?" and "sufficient?" → future work → appendices with the
   classified hit lists. Open points as `% XXX`/`% TODO` in the source.
4. **Build, upload, commit.**
   - `make mfa.pdf LATEXFLAGS="-interaction=nonstopmode"`.
   - Upload (remarkable skill) to `/Courses/OpenSecEd/vetcyb` as
     `MFA necessary or sufficient (draft 2026-11-12, v1)`, verified by
     browsing the folder afterwards.
   - One local commit on `vetcyb26h` at upload time (source + search
     exports). **No push, no PR, no GitHub issues** unless you say so;
     papers that could not be obtained are listed in the final summary.

## Files (all new)

`modules/01-literature/mfa/` — a subdirectory, so the module directory stays
free for other material:

- `mfa.tex` — memoir article class (`sidecaption` for the query tables),
  biblatex/csquotes/cleveref as in `modules/01-methods-overview/preamble.tex`
- `preamble.tex`, `contents.tex`, `abstract.tex`
- `mfa.bib` — every entry under a provenance block
- `search/` — per-session exports (`.csv`, `.bib`) and generated hit-list
  tables (`scholar sessions export -f table --bearing-only --lang en`)
- `Makefile` — `INCLUDE_MAKEFILES=../../../makefiles`, `include .../tex.mk`
  (pattern of `modules/01-methods-overview/Makefile`); `ltxobj/` is already
  git-ignored

## Verification

- Build exits 0; no undefined references or citations in `ltxobj/mfa.log`.
- `check_provenance.py mfa.bib` passes; `check_metadata.py` differences
  investigated (diacritics/subtitles aside).
- Every query-table cell matches `scholar sessions show`; failed cells are
  marked failed, never 0.
- Each RQ is stated once, restated in the method overview and answered in
  the conclusion; every cited source has a verified quote or is flagged
  abstract-only.
- The PDF is visible in the reMarkable folder under the versioned name.

## Limits to expect in a first draft

- Rapid review: 40 hits per database and query, two databases unavailable
  today, some sources possibly read at abstract level only (flagged).
- The largest effect-size figures come from vendors' own observational
  data; the report will say how far they can be trusted.
- OpenAlex has a shared daily request budget (about 1000 requests left); if
  it runs out mid-search, the affected cells are reported as failed and
  listed under future work.
- Expect roughly 45–90 minutes of wall-clock time.
