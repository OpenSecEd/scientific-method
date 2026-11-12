# Plan: Is MFA necessary or sufficient for secure user authentication? (LaTeX report draft, exemplar)

## Context

You asked for research on whether multi-factor authentication (MFA) is
*necessary* or *sufficient* for secure authentication of users, delivered as
a LaTeX report draft with the PDF on your reMarkable. It is meant as a
**good example** for the course: it answers, by doing it, the reflection
prompt "does MFA actually improve security — how would you explore the
literature, which review type?"
(`canvas/04-case-study-passwords-literature/assignments/reflection-on-literature-reviews.md`)
and the MFA claim in `modules/05-scientificity/seminar.tex`.

Your steer: passwordless authentication suggests the password can be
*replaced* by a cryptographic key. If so, the benefit credited to "multi"
may really come from the strength of the added factor, with the password
contributing nothing once the key is there. The report must be able to
tell these two explanations apart.

Nothing exists yet: `modules/01-literature/` is empty, and the old scholar
session "MFA literature seminar" holds only material-flow-analysis false
hits.

## What the report will answer

The question is ill-posed until its terms are fixed, so the report first
defines: *factor* versus *authenticator*; MFA; *passwordless*; and "secure"
as resistance under an explicit threat model, split into **remote** threats
(guessing and credential stuffing, phishing including real-time relay,
server-side leaks, session theft, recovery fallback) and **local** threats
(lost or stolen device, shared device, malware on the device).

- **RQ1 (effect)** — Does MFA reduce account compromise, by how much, and
  for which factor types?
- **RQ2 (attribution)** — Is that effect due to *combining* factors or to
  the *strength of one factor*? What does the password contribute once a
  cryptographic key is present, and what does a second factor contribute
  beside a strong unique password? Evidence sought: comparisons across
  factor types, single-factor key and passwordless deployments, analyses of
  how factors compose.
- **RQ3 (sufficiency)** — Are MFA-protected accounts secure under the
  threat model? Counter-evidence sought: documented bypasses, fallback and
  recovery weaknesses, usability-driven failures.
- **RQ4 (necessity)** — Can comparable security be reached without several
  factors? Counter-evidence sought: single-factor cryptographic
  authenticators, risk-based authentication, password managers; what the
  standards require at which assurance level, and their stated reasons.

Hypotheses, written down before any search and held as predictions only:
(H1) MFA reduces compromise, with large differences between factor types;
(H2) against remote threats the effect comes from the strongest factor, so
the password adds nothing beside a phishing-resistant key, while against
local threats a second, locally verified factor does add something;
(H3) not sufficient; (H4) not necessary against remote threats.
Each can fail: the searches are symmetric, and the subagent prompts state
the claims to test, not these expected answers.

A definitional point the report must settle rather than assume: a passkey
unlocked by PIN or biometric counts as multi-factor in the standards, so
"passwordless" and "single-factor" are different things. RQ2 and RQ4
therefore compare three cases — password plus second factor, key with
local user verification, key alone — per threat.

Review type: a **rapid, scoping-style review with a systematic, documented
search** — not a full systematic review. The method section says so and
motivates the choice against the alternatives, which is the reflection
prompt's own question.

## What makes it an exemplar

- **Protocol before results.** Questions, hypotheses, queries, databases,
  inclusion and exclusion criteria and the evidence grading are written
  into the report's method section and committed *before* the searches
  run, so the git history shows the protocol predates the findings.
- **Evidence graded by study design** (controlled or randomised study,
  large-scale observational measurement, attack demonstration, formal
  analysis, standard or expert consensus, vendor report), so that "many
  sources say so" is not mistaken for strong evidence.
- **Flow counts** per question: identified → screened → read in full →
  included, with the classified hit lists in the appendix.
- **Two-sided throughout**: each question has support and counter queries
  with the same vocabulary; refuting and qualifying work is cited, not
  buried.

## Approach

1. **Write and commit the protocol** (`mfa.tex` skeleton with introduction,
   definitions, RQs, hypotheses, method; `Makefile`). Commit 1.
2. **Search (backing-claims protocol), four parallel strands.** One named
   `scholar` session per RQ: `mfa-effect`, `mfa-attribution`,
   `mfa-sufficient`, `mfa-necessary`. Shared concept vocabulary
   ("multi-factor authentication", "two-factor authentication", 2FA, MFA,
   "two-step verification"; for RQ2/RQ4 also passwordless, passkey, FIDO2,
   WebAuthn, "security key", "single-factor", "risk-based authentication",
   "password manager"), every query on every live provider — OpenAlex, Web
   of Science, Scopus, IEEE Xplore, arXiv, field syntax translated per
   provider. Semantic Scholar (key rejected, HTTP 403) and DBLP (anti-bot
   page) are down today and are reported as *not searched*. Standards and
   industry measurement reports are found through documented WebSearch
   complements and retrieved as known items.
   - Delegated to 4 subagents, `subagent_type: long-job`, `model: sonnet`
     (classifying a few hundred hits can exceed 4 minutes), each given the
     skill's delegation preamble and the committed protocol; each writes a
     provenance `.bib`, session export and full report to the scratchpad.
   - Full texts via `~/.claude/skills/backing-claims/scripts/fetch_pdf.py`
     (scholar's PDF cache; KTH tunnel for closed access, stopping at any
     bot check or login form).
   - Sessions classified (`scholar llm context` / `classify --no-examples`;
     supports / qualifies / adjacent / off-topic), low-confidence and every
     qualifying row read by hand.
3. **My own verification pass.** I read the `.bib` files, not the agents'
   summaries: every load-bearing quote checked against the cached full
   text, duplicates across strands merged, unverifiable sources dropped and
   listed as dropped. `check_provenance.py` and `check_metadata.py` over
   the merged bib.
4. **Write results and conclusions** (English; skills: scientific-writing,
   latex-writing): results per RQ with verbatim quotes for load-bearing
   sources, evidence grade per source, corroborations cited with a finding
   each; a threat-by-case table (three cases × remote/local threats) as the
   synthesis for RQ2 and RQ4; discussion and limitations; a conclusion
   whose first sentences answer "necessary?" and "sufficient?" and say what
   happened to each hypothesis; future work; appendices with query tables
   and classified hit lists. Open points as `% XXX`/`% TODO`.
5. **Build, upload, commit.**
   - `make mfa.pdf LATEXFLAGS="-interaction=nonstopmode"`.
   - Upload (remarkable skill) to `/Courses/OpenSecEd/vetcyb` as
     `MFA necessary or sufficient (draft 2026-11-12, v1)`, verified by
     browsing the folder afterwards.
   - Commit 2 on `vetcyb26h` at upload time (results + search exports).
     **No push, no PR, no GitHub issues** unless you say so; papers that
     could not be obtained are listed in the final summary.

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
- The method section in commit 2 differs from commit 1 only by reported
  deviations, each stated as a deviation.
- Each RQ is stated once, restated in the method overview and answered in
  the conclusion; every cited source has a verified quote or is flagged
  abstract-only.
- The PDF is visible in the reMarkable folder under the versioned name.

## Limits to expect in a first draft

- Rapid review: 40 hits per database and query, two databases unavailable
  today, some sources possibly read at abstract level only (flagged).
- The largest effect-size figures come from vendors' own observational
  data; the report will say how far they can be trusted.
- RQ2 may find little direct evidence: studies rarely isolate what the
  password adds beside a key. If so the answer rests on analysis of threat
  models plus indirect comparisons, and the report will say that plainly.
- OpenAlex has a shared daily request budget (about 1000 requests left); if
  it runs out mid-search, the affected cells are reported as failed and
  listed under future work.
- Expect roughly 60–100 minutes of wall-clock time.
