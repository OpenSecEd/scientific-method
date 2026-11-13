# Round 2, strand `mfa-effect` (RQ1): screening of the uncapped searches

Date 2026-11-13. Session `mfa-effect`. Question: "Does multi-factor authentication reduce account compromise, by how much, and for which kinds of second factor?"
The git repository was not edited. Files are in
`/tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/round2/mfa-effect/` (called `$OUT`).

## Summary

757 pending records were screened: 3 supports-claim, 17 qualifies-claim, 617 adjacent-subtopic, 120 off-topic-false-hit (after my 8 corrections). Nothing in them is a new measurement of compromise on real accounts, no key-based factor (cases B, C) was tested on real accounts, and no new population-level null or negative result was found. The Results of the report are not overturned. Two changes are proposed: (1) the closing paragraph on the counter-search ("returned none ... outcome of a capped search") must be reworded, because the search is now uncapped and one 2019 systematic review (abstract only) states that its authors found no strong evidence that two-factor authentication outperforms password-only login; (2) the sentence "All seven point the same way" can stay, but the table should note that no uncapped search changed the set of seven.

## 1. Query x database matrix (`scholar sessions show mfa-effect`, as it stands)

Cells are hits. "Yesterday" is the capped run (limit 40); "today" is the unlimited run. OpenAlex "today" counts only records matching in title or abstract (query prefixed `title_and_abstract.search:`); OpenAlex full-text matches are in the cache and are not screened (the author's decision). The session shows no failed or incomplete cell.

| Query | OpenAlex yesterday (limit 40) | OpenAlex today (title+abstract, limit 0) | WoS | Scopus | IEEE Xplore | arXiv |
|---|---|---|---|---|---|---|
| S1 | 40 (cap) | 31 | 9 (limit 40, not reached) | 13 (40, not reached) | 5 (40, not reached) | 2 (40, not reached) |
| S2 | 40 (cap) | 94 | 9 (40) | 16 (40) | 8 (40) | 1 (40) |
| C1 | 40 (cap) | 475 | 40 -> 119 (limit 0) | 40 -> 242 (limit 0) | 40 -> 93 (limit 0) | 40 -> 62 (limit 0) |
| R1 | 40 (cap) | 100 | 25 (40) | 29 (40) | 18 (40) | 3 (40) |
| R2 | 40 (cap) | 338 | 39 (40, not reached) | 40 -> 61 (limit 0) | 40 -> 78 (limit 0) | 10 (40) |

Cells with limit 40 and fewer than 40 hits were complete yesterday and were not rerun; cells at 40 were rerun with limit 0 (C1 on WoS, Scopus, IEEE, arXiv; R2 on Scopus, IEEE). Only OpenAlex has the limit-40 run and the title/abstract run as separate entries. The strings are those of yesterday (`session/reports/effect.md`, `sent-*.txt`). Semantic Scholar and DBLP: not searched (as yesterday).

## 2. Counts

- Records in the session before today: 405 (53 human + 347 LLM unreviewed + 5 LLM reviewed). Now: 1162. Pending at the start of this round: 757 (and 0 now).
- Abstracts: `scholar enrich --enrich-providers openalex,arxiv` ran to the end (153 papers enriched; arXiv answered HTTP 429 repeatedly, the run went on). Afterwards 147 of 1162 records have no abstract, 97 of them among the 757 new ones (mostly Scopus records without DOI); these were classified on title and metadata. The enrichment also flagged two currency issues: one retracted (a 2024 conference paper, `10.1109/icocwc60930.2024.11149541`, classified adjacent, not cited) and one superseded (`10.12688/openreseurope.22957.1`, adjacent).
- Classified today (757, model `anthropic/claude-sonnet-5-5`, one run, `-n 757`): before my corrections 5 supports-claim, 21 qualifies-claim, 611 adjacent-subtopic, 120 off-topic-false-hit; after: 3, 17, 617, 120.
- Session as it now stands (1162): supports-claim 9, qualifies-claim 41, adjacent-subtopic 920, off-topic-false-hit 192. Kept 48, discarded 1114 (the 1112 discards of adjacent and off-topic records plus 2 bearing records discarded by yesterday's human decision, which carry no x label because they are not adjacent).
- Exclusion labels over ALL 920 discarded adjacent records of the session: x1-new-scheme 475, x4-no-evidence 254, x5-other-question 88, x3-usability-only 65, x2-machine 35, x6-not-english 3. `relabel.py` labelled 303 records that had none (x1 159, x4 51, x3 39, x5 29, x2 22, x6 3), and a second run found 0 left. The labels are the model's (Sonnet 5.5) and were not read one by one; I looked at all the x3 and x5 titles of the new records and found no record that bears on the question.
- Low-confidence new records (<0.7): 32. All read (title and abstract, 23 of them not already among the bearing ones listed above); none changed class.
- My changes to the model's classes, 8 in all, by kind:
  - supports -> adjacent: 2 (an access-control framework built on the 2024 Snowflake breach, x1; a root-cause analysis of Kazakh breaches that lists missing MFA among many causes, x5).
  - qualifies -> adjacent: 4 (the two records of "Multi-factor biometrics for authentication: a false sense of security", about leaked transformation keys in biometric templates, x5; a narrative review on WhatsApp verification-code hijacking with no original data, x4; a book chapter "SMS attacks" that describes attacks without data, x4).
  - qualifies -> supports: 1 (a randomised phishing simulation that shows MFA groups compromised less; see 3).
  - supports -> qualifies: 1 (Wang and Baskerville 2019, systematic review; see 3).
- Systematic errors of the model: (a) it again filed measurement-like studies under the wrong side: a study that finds MFA users compromised far less was tagged qualifies (0.75), and a systematic review that finds no strong evidence for 2FA was tagged supports (0.5); both were records whose abstract has "effectiveness" and "limitations" in the same breath, and confidence was low. (b) Overview chapters and narrative reviews on attacks (SMS, WhatsApp) were tagged qualifies/bypass instead of x4. (c) The classifier invents free tags: `no-effect-size-stated` on 731 of the 757 new records, and the theme tags `measured-effect` (4 records) and `bypass-attack` (18) on records that nobody had cited. I removed those three tags from all new records except the one I propose to cite (`striptags.py` in `$OUT`), so that only cited records carry themes. Of the 17 new qualifies-claim records, 13 are attack demonstrations or incident analyses (correct), 2 are low-quality surveys, 1 is the systematic review, 1 is the Evilginx thesis. The model's x1/x4 labelling of the 614 new discards looks sound in the sample read (titles of all x3/x5, abstracts of the 23 low-confidence ones).

## 3. Records read, and what each changes

### 3.1 Wang and Baskerville 2019, `Wang2019CaseTwoFactor` (ABSTRACT ONLY)
- Grade: E5-like (a systematic review, not a measurement); case: two-factor in general (P versus A1-A3); claim: "a second factor reduces compromise".
- Finding: the review of 38 studies from two business databases (ABS/Inform and EBSCOhost) found no strong evidence that two-factor authentication performs better, and strong evidence of unexpected risks.
- Quote (abstract, publisher landing page https://aisel.aisnet.org/pacis2019/179): "We found no strong evidence to support the assumption that two-factor authentication has superior performance."
- Could not be read in full: the PDF answered 403 to scholar's downloader (https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1178&context=pacis2019); I did not work around it. Which 38 studies, and what "superior performance" means, is therefore unchecked. It predates Meyer et al. 2023 and covers only business and information-systems databases, so it probably did not reach the security-venue measurements; I think it narrows how the evidence should be described (the academic literature of that time had little), not the finding itself.
- What it changes: the report's paragraph (section Effect)
  > "The search worded to find the opposite, a study in which multi-factor authentication made no difference or made things worse, returned none apart from the optional case above. That is the outcome of a capped search and not proof that no such study exists."

  Proposed replacement in plain English: "The search worded to find the opposite, run without a limit on every database, returned no measurement of real accounts in which multi-factor authentication made no difference or made things worse, apart from the optional case above. It returned one systematic review, from 2019, whose abstract says that its authors found no strong evidence that two-factor authentication performs better than password-only login (read as an abstract only); that review drew on academic studies from two business databases and predates the measurements above, and we do not treat it as a measurement of compromise. That a search finds none is not proof that none exists." Add `Wang2019CaseTwoFactor` (bib entry in `mfa-effect-round2.bib`, themes: `effect-review`).

### 3.2 Dukup and Yola 2026, "Assessment of multi factor authentication techniques for mitigating phishing attacks" (DOI 10.65752/hstxa249), full text read, NOT proposed for citation
- Grade: nominally E1 (controlled experiment, 100 participants, random allocation to MFA or password only, simulated phishing); cases A1 (SMS-OTP, TOTP) and a biometric "MFA"; threats R3, R4, R5, R6.
- Finding as stated: without MFA, compromise 60% or more across attack types (Table 1: 50-75%); biometric 0-5%, TOTP 0-40%, SMS-OTP 5-60%.
- Quote (Sec. 4.1): "Password-only users showed the highest compromise rate, while MFA users had significantly fewer successful attacks. Among the MFA methods, SMS-OTP was the least secure, TOTP offered moderate protection, and biometric authentication achieved the strongest resistance to phishing."
- Why not cited: (a) 50 MFA users split over three methods (about 17 each) cannot give the table's percentages (5%, 2%); the paper gives no counts per cell, no test results, and its own text contradicts its table (it writes "success rates are less than 50 percent" for biometrics, where the table gives 2-5%; "SMS-OTP ... compromise rate of 37 percent" where the table has no such overall figure); (b) the method is written partly in future tense ("will be requested", "allocation ... will be random") and ethics approval is "Not applicable" although human participants were phished; (c) the journal (Nature Journal of Emerging Sciences, Technologies, and Innovations, ISSN 3115-4611) is new and unknown to me; I did not check predatory-publisher lists. I treat the numbers as not reliable. The direction agrees with the report and its ordering (SMS < app < biometric) agrees with Meyer et al. and Doerfler et al., so it counts as corroboration with a warning, not as evidence.
- What it changes: nothing.

### 3.3 Sharma et al. 2026, "Navigating Human Factors in Cybersecurity" (Zenodo, DOI 10.5281/zenodo.20353467), full text read, NOT proposed for citation
- Grade: E2 only nominally (self-reported survey, 149 STEM students and professionals, purposive and snowball sampling, cross-sectional); case: MFA in general.
- Finding as stated: 83.2% use MFA, 26.2% reported unauthorised account access; "no significant association between technology adoption and reduced incidents".
- Quote (Sec. 4.1): "Chi-square analysis revealed no significant association between technology adoption and reduced incidents (χ2 (2) = 2.13, p = 0.345), confirming that technical safeguards alone do not protect against human-factor vulnerabilities."
- Why not cited: the test is one chi-square across three technologies (df 2), not MFA against no MFA; with 83% adopters only about 25 respondents had no MFA; Table 2 gives MFA users an incident rate of 23.4% against 26.2% overall, which, by my arithmetic, implies about 40% (10 of 25) among non-users, i.e. the direction of the report, not a null; the paper's own text says the tests "fell short of significance (p>0.05 due to N=149)" and later reports a different statistic for the same comparison (χ2(2) = 5.77, p = 0.056). The authors' conclusion ("confirming") does not follow from an underpowered test. It is the only new record that states a null for MFA against incidents, and it is a preprint of low reliability.
- What it changes: nothing, but it is the closest to "a null result" among the new records and should be listed in the appendix as read and dropped, with these reasons.

### 3.4 Harvard breach analysis, 2026 (Zenodo, DOI 10.5281/zenodo.19344101), full text read, NOT proposed for citation
- Grade: E3 (incident analysis from public reports and open-source information, by one author); cases A1/A2, threats R4, R6, R7.
- Finding: an incident in 2026 in which attackers combined voice phishing and real-time relay to defeat push MFA at scale. The paper states its figures "are approximate, derived from open-source" material.
- What it changes: nothing; it adds one more secondary case of a bypassed second factor in real use, already covered by the cells (A2 against R4/R6 are marked fail). It cannot be checked against the university's own report; not cited.

## 4. Corroboration at abstract level (new records that bear on the question)

20 new records bear on it (3 supports, 17 qualifies). By what they corroborate:

- Second factor bypassed in use or in the laboratory (qualifies, 13 records, all E3 or E4; per case and threat):
  - Push or notification approval (A2, R6, L3): "Breaking mobile notification-based authentication" (ACM 2023, DOI 10.1145/3570361.3613273; 82.2% cross-service success in a user study; not obtainable, ACM); the Harvard breach analysis; "Attacks using Evilginx and defense" (a master's thesis, Theseus, 2026, a laboratory study in which app-based MFA was relayed and FIDO2 keys resisted; closed access, abstract only).
  - Codes (A1, L3, R5, R7): "Analyzing the security of OTP 2FA in the face of malicious terminals" (Springer 2021, DOI 10.1007/978-3-030-86890-1_6, no abstract); "Security analysis of mobile authenticator applications" (2020); "Investigasi autentikasi dua faktor menggunakan TOTP" (2026, exported TOTP QR codes reveal the seed); "Two step verification system of highly secure social media" (2017, Facebook breach demonstration); DOMtegrity (2019, attack on bank 2FA by browser extension, also proposes a defence).
  - Keys (A3, R4, L3): "BitM+ attack" (SSRN 2024, relay defeating FIDO/CTAP2 through a browser-in-the-middle); "Please remember me" (2020, U2F "remember me" flaws in practice, R8).
  - Real-world campaigns: UAT-11985 detection analysis (2026, real-time Google AiTM phishing; a threat-intelligence write-up), Scattered Spider in aviation (2025, scoping review of incidents, help-desk social engineering, R8).
  - Together these corroborate cells that the report already marks as failing or partly; none fills an empty cell (R2, R6 for A1, R8 for B, L2) and none contradicts one. The group is not large enough to change how strongly any claim is worded, and these show that bypass is possible, not how often, as the report already says.
- Real-account or incident evidence that a second factor helps (supports, 3 records, all low-grade): the NICS grid centre (IEEE GRID 2011, DOI 10.1109/grid.2011.41; "no known user account compromises caused by stolen NICS user credentials", an operator's statement, not a comparison); a reconstruction of one password-spraying incident in which the attack "was driven by incomplete Multi-Factor Authentication (MFA) deployment" (DOI 10.55606/jutiti.v5i3.6290, one incident, abstract only); the randomised phishing simulation in 3.2. All three agree in direction with the report; together with the existing seven they do not change the size or the wording.
- A null or weak result (1 record, not cited): the survey in 3.3.
- Evidence on kinds of second factor: only 3.2 (not cited), whose ordering agrees with the report. None separates a cryptographic key from codes on real accounts.
- Authoritative figure beyond the seven in Table "Reported effects": none.

## 5. New records that contradict or narrow a claim but could not be read in full

| Record | DOI or URL | Why |
|---|---|---|
| Wang and Baskerville 2019 (the review in 3.1) | https://aisel.aisnet.org/pacis2019/179 | Narrows the claim; abstract only, PDF 403 |
| Breaking mobile notification-based authentication | 10.1145/3570361.3613273 | A2 against R6/L3, user study 82.2%; ACM bot check |
| Improved grid security posture through MFA | 10.1109/grid.2011.41 | Supports; IEEE, no open PDF |
| Analyzing the security of OTP 2FA in the face of malicious terminals | 10.1007/978-3-030-86890-1_6 | Springer; not fetched (no abstract in the records either; I did not use the tunnel for it) |
| Exploring phone-based authentication vulnerabilities in SSO systems | 10.1007/978-3-031-15777-6_11 | Springer; no abstract; not fetched |
| BitM+ attack | 10.2139/ssrn.4711140 | SSRN; no abstract in the record; not fetched |
| Attacks using Evilginx and defense | https://openalex.org/W7126130047 (Theseus) | Closed access; lab study of app-based MFA against FIDO2 keys |

None of them contradicts a sentence of the Results; they bear on cells that are already marked "fails" or "depends".

## 6. Anything in the Results now thought wrong, overstated or understated

1. Understated: the report says no measurement of "no effect" exists apart from the optional-2FA arm. After the uncapped search the statement is still true for measurements of accounts, but the review by Wang and Baskerville (3.1) shows the question "is there evidence that 2FA outperforms passwords?" had been answered in the negative by an academic review in 2019. The report should say so, and should say that the academic literature indexed in business databases was thin (the measurements of 2019-2023 are from providers and security venues).
2. The report says (Effect, sum): "within one provider the kinds differ by a few percentage points of the attempts". For Doerfler et al. the gap is 96 against 99 for phishing but 76 against 90 for targeted attacks, i.e. 14 points, and the security key's 100% rests on a small n; "a few percentage points" fits Meyer et al. (1.66 against 0.99) better than Google. I have not re-read Doerfler et al. this round; this is from the report's own quotation (sec. 1 of that paper, "preventing only 96% of attacks rooted in phishing and 76% of targeted attacks"). Suggest: "a few points for phishing, more for targeted attacks".
3. "All seven point the same way": correct, with the optional-2FA arm as the one exception, and the new records do not alter it.
4. The sentence "That is the outcome of a capped search" is now untrue (the searches are uncapped; the OpenAlex full-text matches, tens of thousands, are cached but unscreened by the author's decision). This should name the actual limit: full-text matches on OpenAlex were not screened, Semantic Scholar and DBLP were not searched.
5. Egenti and Ojo 2026 (cited, abstract only) appears in the session as one record only under DOI 10.70882/noun-ijcea.2026.1119, consistent with the bib. No duplicate found.

## 7. Limitations and what was left undone

- Abstracts missing for 147 of 1162 records (97 of the 757 new); these were classified on titles. arXiv rate-limited the enrichment (HTTP 429, retries).
- OpenAlex full-text matches (tens of thousands) are cached and not screened (decision of the author), so a measurement that names MFA only in its body text, and not in title or abstract, would be missed by the search; the counter-search vocabulary also depends on the word "limitations", which makes C1 noisy (475 title/abstract hits on OpenAlex, mostly scheme proposals and overviews).
- Reading: 4 full texts this round (3.2, 3.3, 3.4 and the 2019 review's landing page); 7 records in section 5 could not be obtained. I did not use the KTH tunnel for Springer, SSRN or Theseus papers because those records are corroboration of already filled cells and could not change a result; if wanted, they can be fetched.
- The labels x1 to x6 for the 303 relabelled and the 614 new discards are the model's; I checked titles of x3 and x5, the 32 low-confidence records, and all kept records, not every x1/x4 abstract. An x1 or x4 record that in fact reports a measurement would not be noticed by this review. I scanned titles and abstracts of all new adjacent records with keyword patterns (account takeover, compromised accounts, randomised, natural experiment, %, field study, telemetry, passkey, FIDO, security key, U2F, hardware token) and found 142 pattern matches among the non-off-topic records, none that measures compromise with and without a second factor. That scan is a coarse filter, not a reading.
- `scholar sessions export -f table` counts "10 cited, 3 supporting and 32 qualifying" in its caption; the 10 cited there are the records carrying a theme tag; yesterday's report cited 11 sources, so check the table against the bib when merging.

## 8. Exact commands

```
scholar enrich mfa-effect --enrich-providers openalex,arxiv        # inside timeout 1500
scholar llm context mfa-effect "<question and criteria as in the brief>"
scholar llm classify mfa-effect --no-examples -m anthropic/claude-sonnet-5-5 -n 757 -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit -t x1-new-scheme -t x2-machine -t x3-usability-only -t x4-no-evidence -t x5-other-question -t x6-not-english --no-enrich
$PY -I $R2/relabel.py mfa-effect "<question>"                      # 303 labelled; rerun: 0 left
$PY -I $R2/retag.py mfa-effect <category> [<tag>] -- <paper_ids>   # 8 changes, see section 2
$PY -I $OUT/striptags.py mfa-effect $OUT/newids.json hash:9663f8216d05c502   # removed stray classifier tags
scholar sessions decide mfa-effect --keep --paper-id hash:9663f8216d05c502 -t effect-review
scholar sessions export mfa-effect -f csv -o $OUT/mfa-effect
scholar sessions export mfa-effect -f table --bearing-only --lang en --label hits-effect --track "Effect of multi-factor authentication" --theme measured-effect="Measurement of effect" --theme bypass-attack="Bypass or attack on MFA" --theme effect-review="Systematic review of effect" -o $OUT/mfa-effect-full
```

`$PY` = `/home/dbosk/.local/pipx/venvs/scholarcli/bin/python`, `$R2` = the shared round2 directory. The theme `effect-review` is new (needed for the one cited record).

Files: `mfa-effect.csv`, `mfa-effect-full.tex`, `mfa-effect-round2.bib` (1 entry, `check_provenance.py` OK, `check_metadata.py` 0 problems), `mfa-effect-round2-report.md`, plus working files (`before.csv`, `cur.csv`, `newids.json`, `show-before.txt`, `show-after.txt`, `enrich.log`, `classify1.log`, `striptags.py`).
