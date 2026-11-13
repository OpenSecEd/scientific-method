# Round 2, RQ4 (necessity): screening of the uncapped searches

Session and slug: `mfa-necessary`. Date: 2026-11-13. Question: "Is multi-factor authentication necessary: can comparable security be reached with a single factor, or by other means?" Nothing in the git repository was edited.

## 1. Query x database matrix (from `scholar sessions show mfa-necessary`)

Hits per cell and limit as the session records them (OpenAlex rows prefixed `title_and_abstract.search:` are today's uncapped title/abstract matches; rows with `--limit 40` are yesterday's capped runs, kept in the session). No cell failed or is marked incomplete. The session lists 36 query rows; the cells that today were run with `--limit 0` are:

```
 openalex: title_and_abstract.search:(passwordless OR passke ... --limit 0 — hits: 96 
 openalex: title_and_abstract.search:("multi-factor authenti ... --limit 0 — hits: 1495 
 openalex: title_and_abstract.search:("password-only" OR "si ... --limit 0 — hits: 81 
 openalex: title_and_abstract.search:"risk-based authenticat ... --limit 0 — hits: 147 
 openalex: title_and_abstract.search:(passwordless OR passke ... --limit 0 — hits: 78 
 openalex: title_and_abstract.search:("multi-factor authenti ... --limit 0 — hits: 56 
 arxiv: ("multi-factor authentication" OR "multifactor authe ... --limit 0 — hits: 43 
 ieee: ("multi-factor authentication" OR "multifactor authen ... --limit 0 — hits: 316 
 scopus: TITLE-ABS-KEY(("multi-factor authentication" OR "mu ... --limit 0 — hits: 338 
 wos: TS=(("multi-factor authentication" OR "multifactor aut ... --limit 0 — hits: 395 
 ieee: "risk-based authentication" AND (evaluation OR effect ... --limit 0 — hits: 46 
 scopus: TITLE-ABS-KEY("risk-based authentication" AND (eval ... --limit 0 — hits: 85 
 wos: TS=("risk-based authentication" AND (evaluation OR eff ... --limit 0 — hits: 47 
 ieee: (passwordless OR passkey OR FIDO2 OR WebAuthn OR "sec ... --limit 0 — hits: 30 
 ieee: ("multi-factor authentication" OR "multifactor authen ... --limit 0 — hits: 9 
```
Full text of the rows (query strings abbreviated above) is in `scholar sessions show mfa-necessary`; the per-cell files are in the round2 scratchpad (`mfa-necessary-q<k>-<db>.csv`, `log.tsv`). Yesterday's cells (limit 40) are the remaining 21 rows. OpenAlex full-text matches (tens of thousands) are in scholar's cache and were not screened, by the author's decision. IEEE's daily quota was shared with the other strands; its rows above completed. DBLP and Semantic Scholar were not used.

## 2. Counts

* Records in the session: 523 before today, 2282 now (1759 new; 1758 were classified today, 1 was already decided).
* Abstracts: enrichment (openalex, arxiv; 286 papers enriched) left **284 of 2282 records without an abstract** (197 of the new ones); these were classified on title.
* Classified today (new records), model result: supports 9, qualifies 70, adjacent 1266, off-topic 414. After my reading: **supports 3, qualifies 13, adjacent 1329, off-topic 414**.
* Session totals now: supports 17, qualifies 56, adjacent 1749, off-topic 460; kept = the supports and qualifies records (73).
* Exclusion labels over ALL discarded adjacent records of the session (the relabel script labelled 429 that had none; 364 discards are off-topic hits and carry no x-label by definition): x1-new-scheme 997, x2-machine 95, x3-usability-only 118, x4-no-evidence 442, x5-other-question 184, x6-not-english 18. The x1 count is high (the labeller put most unlabelled adjacent records there); I did not re-read labels beyond those I retagged.
* My changes to the model's classes (63 records, all of them supports/qualifies -> adjacent): 29 to x4-no-evidence (reviews, opinion, white papers, narrative reviews, repository/zenodo/SSRN items), 20 to x1-new-scheme, 14 to x5-other-question. No record was moved the other way. I read title and abstract of all 79 new supports/qualifies and the 181 new low-confidence (<0.7) discards that were not already in that set; among the 181 I found none to move into the bearing classes (nearest: Wiefling's extended abstract on RBA, a German dissertation outline; a survey that quotes Gavazzi et al.).
* **Systematic error found:** the model files every attack or security analysis of an MFA scheme as "qualifies" (SMS-OTP attacks, social authentication, SS7, MitB, FIDO/CTAP attacks, push-notification attacks). For RQ4 these answer RQ2 (sufficiency), not necessity; 49 of the 63 changes were of this kind. Second error: low-quality secondary items (Zenodo, SSRN, regional journals) filed as qualifies because they say "MFA is necessary/effective" without method, i.e. x4 by the report's own rule for "bare statement". One duplicate: "Phish in Sheep's Clothing" appears under a second id (already cited as Lin2022PhishSheep); kept as qualifies.

## 3. Records read in full

**Gavazzi et al. 2023, bib key `Gavazzi2023Availability`** (Scopus record without abstract; full text from USENIX). Grade: E2 for the services' behaviour (208 real sites of the Tranco top 5K), E3 for the hijack attempt. Case: risk-based authentication (RBA) beside MFA; threat R1 with a stolen password. Finding: only 42.31% of sites offer any MFA and only 22.12% block a highly suspicious login (38 of the 88 MFA-supporting sites do); 15 sites use RBA without offering MFA.
Quote (abstract, p. 2043): "We find that only 42.31% of sites support any form of MFA, and only 22.12% of sites block an obvious account hijacking attempt."
Changes in the report: paragraph "Risk-based authentication" in Necessity, after the Makowski2023RBA sentence ("At large services several test cases rarely trigger the RBA system"). Proposed addition: "A measurement of 208 popular services found that only 22.12 per cent blocked a login from another country and machine made with the correct password, and that 15 services use risk-based checks without offering a second factor \autocite{Gavazzi2023Availability}." Also a cell: Table remote has no RBA row, so no table change. It strengthens, not changes, "not a substitute".

**NIST IR 8523 (Fisher et al.), `Fisher2025CJISMFA`**, grade E5 (initial public draft of an authority's guidance for a regulation, the FBI CJIS Security Policy). Case: password alone vs MFA, threat R1/R3. Quote (sec. 2.1): "if an attacker obtains a user's password, they still need access to the additional factor to successfully authenticate." and (sec. 2.5): "All MFA has security benefits compared to using a single factor, but not all forms of MFA are created equal, even if they are at the same AAL." Also: AAL1 is "typically a single-factor username and password" and AAL2 or AAL3 "may be required" for systems whose compromise causes detrimental impact.
Changes: paragraph "What is required" (currently: "The authorities require more than one factor at their upper levels."). Proposed addition after the OMB sentence: "The criminal-justice regulation likewise requires MFA, with the reason that a stolen password is then not enough; its guidance counts phishing resistance as optional at the second level \autocite{Fisher2025CJISMFA}." It is a further E5 source with the same reason (credential theft, phishing) and, like the others, does not consider a key alone; it does not alter the verdict.

**CTRAPS (DOI 10.1109/EuroSP63326.2025.00063)**, read in part (13,336 words; protocol and attack sections): E4/E3. It evaluates the CTAP authenticator API of authenticators "for single-factor and second-factor authentication" and shows attacks that skip user verification by targeting relying parties that do not require it (factory reset, credential deletion, lockout, tracking). It does not test a key alone against an account-takeover threat or compare it with a multi-factor case, so it does **not** contradict "no source tests a key alone". It bears on case C/B availability and denial rather than takeover. Not proposed for a bib entry (no result changes); listed as corroboration for the attacks theme.

**Assessment of MFA techniques for mitigating phishing attacks (Dukup and Yola 2026, 10.65752/hstxa249)**, full text read. Claims a randomised experiment, 100 participants, MFA vs password-only groups, over six simulated attacks; no-MFA compromise "exceeding 60%". Not proposed: new journal, tiny simulated sample, simulated MFA, biometrics tested "alone" without a key; no case C. Corroboration only (single factor falls short; effect), flagged weak.

## 4. Corroboration at abstract level (new bearing records, not cited)

* Single factor falls short / MFA effective, weak methods (qualifies): CERN second-factor deployment (2000 users gave up passwords in a simulated phishing campaign; 10.1051/epjconf/202429504025), VPN 2FA experiment at one company (10.34288/jri.v7i3.367), survey of 100 e-commerce users (10.32505/jii.v11i2.14855), education-system MFA evaluation (10.37366/jpcs.v4i1.4451), acoustic eavesdropping on typed passphrases (password-only falls to a nearby attacker; arXiv 2503.16719). 5 records; none changes the strength of the wording on necessity.
* Requirements, regulation, law: PSD2 e-banking study (10.1109/ACCESS.2022.3149475), law-review debate on whether the Gramm-Leach-Bliley rule should mandate two factors (OpenAlex W2266061148; argues a mandate goes beyond minimum standards and that 2FA is not adequate against phishing and trojans), EU-law analysis of MFA requirements (10.1016/j.clsr.2015.12.004). 3 records; the first and third are potential E5 sources, not read.
* Alternatives ranked: FIDO2 hardware token ranked with face+PIN above password+TOTP in a weighted-sum comparison (Zenodo 10.5281/zenodo.24022071, SSRN twin), US Navy thesis ranking CAC PKI > FIDO2 PKI > 2FA > password (no DOI). 3 records, weak.
* RBA: Wiefling's dissertation outline (10.18420/sicherheit2020_12), "As soon as it's a risk, I want to require MFA" (admins configuring RBA), a survey quoting Gavazzi on RBA acting on only 22% of suspicious logins. 3 records, usability or survey level.
* No new record tests case C (a key alone, no PIN/biometric) against any threat, measures a random unique password against MFA, or reports an account protected by a key taken over in real use. The abstract scan of all 1759 new records for single-factor with FIDO/passkey/security key/U2F found only CTRAPS. No group is large enough to change how a claim is worded.

## 5. Records that contradict or narrow a claim but were not read in full

* **Evidence-based cybersecurity policy? A meta-review of security control effectiveness**, DOI 10.1080/23738871.2024.2335461, ABSTRACT ONLY (Taylor & Francis refused the fetch; also through the KTH tunnel; stopped, no workaround). Abstract: "Multi-factor authentication was effective in protecting individual accounts, although inconsistent MFA-implementation undermines efficacy when rolled out across an organisation. ... policy measures that mandate specific controls are unlikely to result in risk reduction." This narrows the sentence "A requirement shows what experts agree on (E5), not that fewer factors would fail": it is the one new source that argues, from a review of empirical studies, that mandates as such are not shown to reduce risk. Worth reading by the author (todo).
* The Gramm-Leach-Bliley debate paper (OpenAlex W2266061148, 2006; no DOI): argues two-factor mandate exceeds a minimum standard; not obtainable by DOI.
* CERN paper (DOI above): EPJ/CDS full text behind a bot check; stopped.
* EU-law analysis (10.1016/j.clsr.2015.12.004): Elsevier; not tried (bot check named in the brief).

## 6. Anything in the Results now thought wrong, over- or understated

* Nothing is wrong. The sentence "Two web searches for a measured comparison of such passwords with multi-factor authentication returned no study" stands: no new record measures a random unique password against MFA (one Ukrainian article on password managers and entropy is x5).
* "The search found no source that tests a key alone against a multi-factor case, for any threat" stands after 1759 more records; I would add that this is now true of title/abstract matches of all five databases without a cap, which is a stronger statement of the absence than yesterday's capped one. It is still a negative about abstracts only: many records lacked abstracts (284).
* The risk-based paragraph may be slightly overstated in the direction of RBA's effectiveness ("effective measure to protect users from the majority of attacks involving stolen passwords"): Gavazzi's 22.12 per cent shows that most services do not act on such an attempt; the two are about different things (a study of one service's RBA vs what services deploy), and the text should say which.

## 7. Limitations and what was left undone

* 284 records have no abstract (classified on title); classification by a model, checked by reading only the 79 bearing and 181 low-confidence records; the 1.6 thousand high-confidence discards were not re-read. The relabeller put most unlabelled discards under x1 (248 of 429); labels are model output.
* The first classification run with `-n 1758` returned invalid JSON and was lost (about half an hour); the second run used batches of 50. Classification of 1758 records took about 25 minutes.
* Not read in full: the meta-review, CERN, EU-law, Gramm-Leach-Bliley; the Zenodo/SSRN items. Only two sources are proposed for the bibliography. I did not search again with new queries; counter-searching was done by the title/abstract scan above and by the report's own queries.
* The KTH SOCKS tunnel was opened and closed by me; T&F and EPJ answered with 403 / "enable JS" and I stopped.

## 8. Commands

```
scholar enrich mfa-necessary --enrich-providers openalex,arxiv        # timeout 1500; 286 enriched
scholar llm context mfa-necessary "<question + criteria + tags as in the brief>"
scholar llm classify mfa-necessary --no-examples -m anthropic/claude-sonnet-5-5 -n 50 -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit -t x1-new-scheme -t x2-machine -t x3-usability-only -t x4-no-evidence -t x5-other-question -t x6-not-english --no-enrich     # repeated 36 times via classify.sh until Pending 0
$PY -I $R2/relabel.py mfa-necessary "<question>"       # labelled 429 of 429
$PY -I $R2/retag.py mfa-necessary adjacent-subtopic <x-tag> -- <ids>   # 29 x4, 20 x1, 14 x5
scholar sessions decide mfa-necessary --keep --paper-id hash:9cf70d1410121d1d -t RBA
scholar sessions decide mfa-necessary --keep --paper-id doi:10.6028/nist.ir.8523 -t STD
scholar sessions export mfa-necessary -f csv -o <OUT>/mfa-necessary
scholar sessions export mfa-necessary -f table --bearing-only --lang en --label hits-necessary --track "Is multi-factor authentication necessary" --theme RBA="Risk-based authentication" --theme FIDO="Cryptographic keys and passkeys" --theme REC="Account recovery and fallback" --theme STD="Standards and requirements" --theme ATT="Attacks on and measurements of MFA" -o <OUT>/mfa-necessary-full
```
