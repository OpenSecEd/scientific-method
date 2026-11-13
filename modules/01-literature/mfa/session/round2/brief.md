# Second round of the MFA review (2026-11-13): screening the uncapped searches

You run one strand of a literature review, for ONE research question. The
review exists as a draft (v5); this round extends its search. Do NOT edit
anything in the git repository, do not run LaTeX builds, do not touch
`nytid` or the reMarkable. Write only under your output directory (given in
your prompt). Shared helper scripts are in
`/tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/round2/`
(called `$R2` below); run the Python ones with scholar's own interpreter:
`PY=/home/dbosk/.local/pipx/venvs/scholarcli/bin/python`.

## What happened before you

- Yesterday each question was searched on OpenAlex, Web of Science, Scopus,
  IEEE Xplore and arXiv, with at most 40 records per query and database.
  The records were classified and the report written:
  `/home/dbosk/devel/edu/scientific-method/modules/01-literature/mfa/contents.tex`
  (sources in `mfa.bib`, yesterday's run reports in `session/reports/`).
- The author has since decided: **searches are never capped.** Today every
  query that had hit the cap, and the four that had failed on IEEE Xplore,
  were run again without a limit. Your `scholar` session now also holds,
  as *pending* records: everything those queries return from Web of
  Science, Scopus, IEEE Xplore and arXiv, and every OpenAlex record that
  matches the query in **title or abstract** (recorded in the session under
  the query prefixed `title_and_abstract.search:`). OpenAlex's full-text
  matches (tens of thousands) are kept in the cache and are not screened:
  the author's decision.
- The author also decided what is read: **screen every pending record;
  read in full only what could change a result**; everything else that
  bears on the question is counted and listed as corroboration at abstract
  level.
- The exclusion criteria now carry labels (report, section "Inclusion and
  exclusion"), and the label is the reason recorded with every discard:
  `x1-new-scheme`, `x2-machine`, `x3-usability-only`, `x4-no-evidence`,
  `x5-other-question`, `x6-not-english`.

## Read first

1. Load the `backing-claims` skill (Skill tool) and follow it; it was
   amended today (no caps, labelled exclusion criteria).
2. The report: sections Terms (cases P, P+, A1, A2, A3, B, C), Threat model
   (R1-R8, L1-L3), Inclusion and exclusion (X1-X6), Grading the evidence
   (E1-E6), and the Results for your question, including the tables of
   cases against threats. You need to know what the report now says in
   order to recognise a record that would change it.
3. Yesterday's report for your strand in `session/reports/`.

## Steps

1. **Abstracts.** Many new records come from Scopus, which gives no
   abstracts. Add them, without IEEE (its daily quota is small) and without
   Semantic Scholar (key rejected):
   `timeout 1500 scholar enrich <session> --enrich-providers openalex,arxiv`
   (check `scholar enrich --help` for the exact option names). If it stalls
   or the time runs out, go on: records without abstract are classified on
   their titles, and you report how many.
2. **Context.** Set the research context with the criteria and tags:
   `scholar llm context <session> "<your question>. Keep a record only if it
   bears on that question for the authentication of human users to online
   services and reports evidence (experiment, measurement of real accounts
   or incidents, attack shown or observed, formal or analytical security
   analysis, standard or authority guidance, provider report). Category
   tags, exactly one per record: supports-claim = <as given in your prompt>;
   qualifies-claim = <as given in your prompt>; adjacent-subtopic = about
   authentication but excluded by one of the criteria below;
   off-topic-false-hit = another subject, returned for a shared word.
   Every adjacent-subtopic record also gets exactly one exclusion tag:
   x1-new-scheme = proposes a new scheme, protocol or system with only its
   own security argument or evaluation; x2-machine = authentication between
   machines or devices, no human user; x3-usability-only = only usability,
   adoption or perception, nothing on security outcomes; x4-no-evidence =
   opinion, overview, tutorial or recommendation without evidence of its
   own or a stated method; x5-other-question = authentication of users,
   with evidence, but not on this question; x6-not-english = not in
   English."`
3. **Classify every pending record**, in the background with a generous
   timeout, in batches until `scholar llm status <session>` shows none
   pending:
   `scholar llm classify <session> --no-examples -m anthropic/claude-sonnet-5-5 -n <number pending> -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit -t x1-new-scheme -t x2-machine -t x3-usability-only -t x4-no-evidence -t x5-other-question -t x6-not-english --no-enrich`
   (`anthropic/claude-sonnet-5-5` because the tool's default model is not
   installed). Records the run leaves pending get a decision from you.
4. **Label every discard.** Records discarded yesterday carry no exclusion
   label, and today's classifier may have left some adjacent records
   without one. Label them all:
   `$PY $R2/relabel.py <session> "<your question>"`
   It adds one `x…` tag to each discarded adjacent record that has none,
   and changes nothing else. Run it again if it reports fewer labelled than
   there were to label.
5. **Check the classification by reading.** Read title and abstract of
   every NEW record classified supports-claim or qualifies-claim, and of
   every new record with confidence below 0.7 whatever its class. Where
   the model is wrong, change the class with
   `$PY $R2/retag.py <session> <category> [<x-tag>] -- <paper_id> [<paper_id> ...]`
   (it replaces the category, which `scholar sessions decide` cannot do,
   and sets kept or discarded accordingly). Count your changes by kind.
   Yesterday one model filed every measurement study as "qualifies"; look
   for systematic errors of that kind and say what you find.
6. **Pick what could change a result, and read it in full.** A record
   could change a result if it
   - measures compromise on real accounts or incidents, or reports a null
     or negative result;
   - shows or refutes an attack for a cell of the tables of cases against
     threats that is empty, or contradicts what the cell says;
   - tests a cryptographic key used alone (case C), or isolates what one
     factor adds beside another;
   - gives stronger evidence (a higher grade for the purpose) than what the
     report now cites for a claim;
   - reports an account protected by a cryptographic key being taken over
     in real use;
   - contradicts a sentence of the Results for your question.
   Fetch those with
   `~/.claude/skills/backing-claims/scripts/fetch_pdf.py --text <doi-or-url>`
   (KTH tunnel as in the skill's `references/closed-access.md`; ACM, SAGE,
   IEEE, Elsevier, Wiley and MDPI serve a bot check also from KTH: stop
   there, do not work around it; Springer answers `curl` through the
   tunnel). Read each through, not only the abstract. A record you could
   not obtain is listed with its DOI and marked ABSTRACT ONLY.
   Everything else that bears on the question stays at abstract level: do
   not write bib entries for it, but give it a theme tag
   (`scholar sessions decide <session> --keep --paper-id <id> -t <theme>`
   is NOT needed for these; only cited records get theme tags) and count
   it in your report by what it corroborates.
7. **Outputs** in your output directory:
   - `<slug>-round2.bib`: entries ONLY for sources you propose to cite
     that are not yet in `mfa.bib`, each under a provenance block
     (CLAIM / FOUND-VIA / PICKED / QUOTE / VERIFIED / COUNTER / DATE);
     run the skill's `check_provenance.py` and `check_metadata.py` on it.
     Quotes verbatim with locator; check each against the text you read.
   - Tag every record you propose to cite with a theme tag in the session
     (`scholar sessions decide <session> --keep --paper-id <id> -t <theme>`;
     the themes used yesterday are in your prompt, add one if needed).
   - `<slug>.csv`: `scholar sessions export <session> -f csv -o <OUT>/<slug>`.
   - `<slug>-full.tex`: the table command in your prompt.
   - `<slug>-round2-report.md`, the COMPLETE report (your reply to me is cut
     at about 4 KB):
     1. the query x database matrix from `scholar sessions show <session>`
        as it now stands (hits per cell, the limit of each, failures);
     2. counts: records in the session before today and now; classified
        today into each category; per exclusion label for ALL discards of
        the session; abstracts missing; your changes to the model's
        classes, by kind, and any systematic error;
     3. the records read in full: for each, bib key, grade (E1-E6), case
        and threat it concerns, one-sentence finding, verbatim quote with
        locator, and **what it changes in the report**: the sentence or
        table cell, quoted as it stands, and your proposed replacement
        text in plain English;
     4. corroboration at abstract level: counts of new bearing records by
        what they corroborate (per case and threat, or per claim), with
        the three or four most notable titles each, and whether any group
        is large enough to change how strongly a claim should be worded;
     5. new records that contradict or narrow a claim of the report but
        that you could not read in full (title, DOI, why);
     6. anything in the report's Results for your question that you now
        think is wrong, overstated or understated, with the evidence;
     7. limitations (facts about data and tools) and what you left undone;
     8. the exact commands for classification and table export.

Work within about 90 minutes. If time runs short, finish steps 1 to 5 for
all records and read fewer papers in full, most consequential first; say
what was left.

Reply with one paragraph: how many records were screened and how they
fell, what (if anything) changes in the report, the main open point, and
the paths of your files.
