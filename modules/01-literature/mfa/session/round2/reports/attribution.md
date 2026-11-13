# Round 2, RQ2 (attribution): one strong factor or the combination?

Session `mfa-attribution`. Date of the work: 2026-11-13. Output directory:
`/tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/round2/mfa-attribution/`
Files: `mfa-attribution.csv`, `mfa-attribution-full.tex`, `mfa-attribution-round2.bib`, this report.

## 0. Result in brief

290 new records were screened (298 before, 588 now). The model first classified 11 of them as bearing on the question (5 supports, 6 qualifies) and 279 as adjacent or off-topic. After reading I moved 4 of the 11 out (see 2), leaving 7 (3 supports, 4 qualifies); 3 of these 7 are duplicates of records the session already held under another identifier (the Wasser monograph, Jacomme and Kremer, Kunke et al.), so **4 are new bearing records**: a Nigerian experiment (read in full, low credibility), a master's thesis and a MobiCom paper (abstract only, not obtainable), and a practitioner study (abstract only). None is a measurement of real accounts, none isolates what one factor adds, none tests a key used alone (case C), none concerns R2 or L2. **No sentence or table cell of the Results for RQ2 needs to change.** "No study found isolates the contribution of one factor in measured compromise" still stands after the uncapped search. The round adds corroboration: laboratory demonstrations against a relayed login (R4) and one more E3 demonstration against the push approval (R6/L3). One optional bib entry is proposed (Wasser 2026, read in full).

## 1. Query x database matrix (as `scholar sessions show mfa-attribution` stands)

S1 = K AND password AND (replace OR comparison OR "security analysis" OR evaluation). S2 = K AND ("user verification" OR PIN OR biometric) AND (stolen OR theft OR "local attack"). C1 = (MFA terms) AND (defence in depth, independent factors, ...). C2 = K AND password AND ("still needed" OR fallback OR weakness OR vulnerability). K = (passwordless OR passkey OR FIDO2 OR WebAuthn OR "security key" OR "single-factor"). Exact strings are in the session and in yesterday's report. No cell failed, was incomplete or needed a retry (`grep -ci "failed\|incomplete\|retries"` on `scholar sessions show` = 0).

Hits per cell, with the limit of the run that is in the session. `OA-plain` is yesterday's OpenAlex run with `--limit 40` (full-text match, capped); `OA-t/a` is today's uncapped OpenAlex run that matches in title or abstract (recorded as `title_and_abstract.search:...`).

| Query | OA-plain | OA-t/a | WoS | Scopus | IEEE Xplore | arXiv |
|---|---|---|---|---|---|---|
| S1 | 40 (limit 40, capped) | 226 (no limit) | 53 (no limit) | 86 (no limit) | 66 (no limit) | 15 (limit 40) |
| S2 | 40 (limit 40, capped) | 74 (no limit) | 6 (limit 40) | 23 (limit 40) | 26 (limit 40) | 1 (limit 40) |
| C1 | 40 (limit 40, capped) | 51 (no limit) | 12 (limit 40) | 21 (limit 40) | 8 (limit 40) | 1 (limit 40) |
| C2 | 40 (limit 40, capped) | 227 (no limit) | 39 (limit 40) | 78 (no limit) | 53 (no limit) | 10 (limit 40) |

A cell with limit 40 and fewer than 40 hits is complete. The only capped cells left are the four OpenAlex full-text runs (OA-plain), whose full-text matches (tens of thousands) are in the cache and, by the author's decision, not screened; their title-and-abstract counterparts are uncapped. Semantic Scholar and DBLP were not searched (key rejected; anti-bot page), as yesterday.

## 2. Counts

- Records in the session: 298 before today, 588 now (290 added). Of the 290, 13 have a title that equals that of an older record (same work under a different identifier, e.g. the published and the preprint version, or the Zenodo concept and version DOI); the session counts them as separate records.
- Abstracts: `scholar enrich mfa-attribution --enrich-providers openalex,arxiv` ran to completion (about 3 minutes) and filled 39 records. After it, 86 of 588 records have no abstract (40 of the 290 new ones); mostly Scopus-only records. These were classified on title (and venue). arXiv answered HTTP 429 for some lookups.
- Classified today with `anthropic/claude-sonnet-5-5`, zero-shot, 289 papers (the 290th had a human decision): supports-claim 5, qualifies-claim 6, adjacent-subtopic 246, off-topic-false-hit 33 (the model's numbers for the 290 new records, before my changes).
- After my changes the 290 new records are: supports-claim 3, qualifies-claim 4, adjacent-subtopic 250, off-topic-false-hit 33. The whole session: supports 13, qualifies 29, adjacent 464, off-topic 82 (the 13 + 29 = 42 kept records include 3 of the 7 that are duplicates of older cited records; one old record is discarded but carries the supports tag, which is a leftover of yesterday's human decision).
- Exclusion labels on ALL 464 + 1 discards of the session that carry one (after `relabel.py`: 214 records had none and were labelled, a second run labelled 0 of 0): x1-new-scheme 273, x2-machine 7, x3-usability-only 38, x4-no-evidence 104, x5-other-question 35, x6-not-english 7. The 83 discards without an x label are the 82 off-topic-false-hit records (they take no label by design) and the one discarded record that carries the supports tag.
- Changes to the model's classes (all after reading title and abstract, and the full text where noted), 4 in total:
  - 3 x "qualifies/supports" moved to adjacent-subtopic **x4-no-evidence**: a social-media simulation whose attack-success matrix is assumed, not measured (so its results restate its inputs; full text read); a literature review of recovery channels; a systematic review of FIDO2 for which I found neither abstract nor a PDF (title only, so it cannot be counted as evidence; listed in 5).
  - 1 x "qualifies" moved to adjacent-subtopic **x1-new-scheme**: a design-science framework for migrating to passwordless that derives a threat catalogue by method and offers an analytic evaluation only.
  - 0 changes from adjacent to bearing: I read the titles of all 250 adjacent and 33 off-topic new records and the abstracts of the 17 with confidence below 0.7, and found none that bears on the question for the cases, threats or comparisons above.
- Systematic errors of the model: (a) it files anything about weakness or recovery as "qualifies" (three of the four I moved are of that kind: reviews and frameworks, not evidence); (b) it files secondary or simulated studies as "supports" when they agree with the expected answer (the simulation); (c) opposite to yesterday's error there is no sign that it filed measurement studies as "qualifies": the laboratory demonstrations were filed "supports" with confidence 0.8-0.9, which I judge right. (d) the x-labelling by the model matches my reading of the titles; the one doubtful label is x6 on a Greek-language thesis about MFA bypass (its abstract is Greek, so x6 is correct).

## 3. Records read in full

Only three records could be obtained and read in full (one a duplicate of an older record, one moved out afterwards); none changes a result. The abstract-only ones are in 4 and 5.

### 3.1 `Wasser2026Resilience` (proposed for the bib; Zenodo, Polish text, English abstract)

- Grade: E3 (attack demonstrated in a laboratory), non-refereed, single author. Case: A1 (password + TOTP) against B (key with user verification). Threat: R4.
- Finding: in 100 trials per arm (10 domain mutations x 10), Evilginx3 captured the session in every password+TOTP trial and in none of the YubiKey 5 trials (user presence and PIN enforced). The victim is assumed fully compliant, so the test is of the machine-side checks only.
- Quote, abstract (English): "the password + TOTP scheme exhibited an Attack Success Rate of ASR = 100.0%, whereas hardware-bound FIDO2 demonstrated absolute resilience (ASR = 0.0%)". Quote, sec. 7.2 (Polish): "W przypadku FIDO2 z tokenem YubiKey 5 NFC (USB-A i USB-C) wskaźnik sukcesu ataku wyniósł 0,0% (0/100 prób)." Sec. 6.1: "firmware 5.4.3 z wymuszeniem UP i UV (kod PIN)".
- What it changes: nothing in the tables (R4 is already `\fail` for A1 and `\res` for B). It could be added as one more source to the sentence "A laboratory relay captured the session through codes by text message, call, email and app and through push approvals ..." (Kikuchi, Cuellar), with the caveats: not refereed, the key arm has no password, so it does not test A3 or C. Proposed text, if added: "A third laboratory bench, not refereed, captured the session in all 100 trials with a password and an app code and in none of 100 with a key unlocked by a PIN \autocite{Wasser2026Resilience}." This says nothing new about attribution, and I would not add it if economy matters. Note that the Polish PDF was read; the English abstract is that of the record (DataCite title and author checked; Crossref does not hold Zenodo DOIs, so `check_metadata.py` reports "TITLE mismatch" with an empty Crossref title, which is an artefact).

### 3.2 `Dukup2026Assessment` (not proposed for the bib)

- doi 10.65752/hstxa249, Nature Journal of Emerging Sciences, Technologies and Innovations 6(3), March 2026. Grade nominally E1 (randomised groups of 50 and 50, simulated phishing), but I judge the evidence unreliable: ethics approval "Not applicable" for a study with 100 human participants; the number of participants per MFA method is not given; the text says that biometric success rates "are less than 50 percent" where the table has 0-5 per cent; "biometric" is not defined as a key, a device or a template; the data are "on request"; the methods section mixes future and past tense. Case: password-only (P) against A1 (SMS, app code) and an unspecified biometric second factor. Threats R1, R3, R4, R5, R6.
- Finding: success rates of simulated phishing (Table 1): No MFA 50-75 per cent, SMS 5-60, app code 0-40, biometric 0-5. "Which second factor" matters, and the weakest ones add little against a relayed login (SMS 60 per cent, app 40 per cent, no MFA 75 per cent).
- Quote (sec. 4.1): "Among the MFA methods, SMS-OTP was the least secure, TOTP offered moderate protection, and biometric authentication achieved the strongest resistance to phishing."
- What it changes: nothing. It does not isolate a factor (all arms have the password), and the first group is not a strong unique password (the password-only group "was asked to generate a password in accordance with the general password requirements"). It points the same way as the Results ("what a second factor adds depends on which factor it is"). I would not cite it.

### 3.3 `Gundu2026Simulation` (dropped, moved to adjacent x4)

- doi 10.34190/ecsm.13.1.4685. An agent-based simulation of 10,000 users whose attack-success probabilities are set by the author (Table 1: password with reuse 0.8, SMS 0.1, app 0.01, passkey 0 for credential stuffing; phishing 0.7/0.6/0.4/0.05). "Password elimination" reduces compromises by 89 per cent because the matrix says so. It is not evidence of any effect; it models only attacks and cohorts of user choices. DROPPED (not cited, not counted as evidence).

## 4. Corroboration at abstract level (new, bearing, not read in full)

New bearing records after my changes: 7 (3 supports, 4 qualifies). Three are duplicates of records already in the session (the Wasser Zenodo item; the Jacomme and Kremer formal analysis; the Kunke et al. recovery evaluation), one is the Nigerian experiment read in full (3.2), so **3 records** are new and abstract-only (the first three rows below):

| What it corroborates | New records | Notable |
|---|---|---|
| A key resists the relayed login, a code or push does not (R4; supports one strong factor) | 1 (+ Wasser above, as read) | Amer 2026, "Attacks Using Evilginx and Defense" (Theseus master's thesis, repository 403 for download, ABSTRACT ONLY): a local lab and a proof of concept against a real mail service; app-based MFA with number matching was bypassed, a FIDO2 hardware key prevented the session hijack, and a server-side session revocation worked as a reactive defence. Same direction as Kikuchi and Wasser. |
| A second factor on a push approval fails against a malicious program on the user's computer or a deceived user (R6, L3; qualifies) | 1 | Mahdad, Jubur, Saxena, "Breaking Mobile Notification-based Authentication with Concurrent Attacks Outside of Mobile Devices", MobiCom 2023 (doi 10.1145/3570361.3613273; ACM bot check, ABSTRACT ONLY): proof-of-concept attack and a user study with an 82.2 per cent cross-service success rate, with the attacker "compromis[ing] user account without compromising possession-factor device". An E3 source for A2 against R6 and L3 beside the NCSC rows (E5) and `Jubur2021PushBypass`. Authors are the same group as `Mahdad2023SoK2FA`. |
| Residual risk sits in recovery, weaker second factors and continuity, not in the key's cryptography (R8) | 1 | Preprints.org 2026, "Towards Passwordless Authentication: A Practitioner-Grounded, Risk-Tiered Framework ..." (doi 10.20944/preprints202610.1811.v1; no open PDF, ABSTRACT ONLY): a panel of 28 IT managers, E5 at best; "None of the 16 statements supported immediate password elimination, while 13 endorsed a phased transition ... retaining passwords as time-limited fallbacks for legacy systems, recovery, and exceptions." Bears on "password beside a key" as practice, not as effect. |
| Which second factor matters (A1 with SMS/app/biometric against P) | 1 | the Nigerian experiment of 3.2 (read in full, low credibility) |

No group is large enough to change how strongly a claim is worded; each is one record, and the groups for R4 and R8 are already well covered by the cited sources. Nothing new for case C, R2 or L2.

## 5. New records that contradict or narrow a claim but could not be read in full

- Mahdad, Jubur, Saxena 2023, doi 10.1145/3570361.3613273 (ACM bot check, stopped). It narrows nothing in the tables but would be the strongest source for the cell A2 x L3 (currently `\fail` on the NCSC assessment alone) and R6; E3. The authors' earlier paper is cited as `Jubur2021PushBypass`.
- Amer 2026, Theseus handle 10024/910221 (HTTP 403), E3 thesis; confirms the R4 cells.
- AlQahtani et al. 2026, "A Systematic Review of FIDO2 Security, Usability, and Deployment Evidence", SSRN doi 10.2139/ssrn.6759998: no abstract, no open PDF. Secondary study; I moved it to adjacent x4, and a reader with SSRN access may want to look at whether it summarises measurements of keys alone or with a password. Not blocking.
- "Ranljivosti pri implementaciji standarda WebAuthn" (doi 10.31449/upinf.293; Slovenian title, English abstract): four 2025-2026 CVEs and a demonstration of server-side flaws in credential binding by which an attacker takes over another user's account with the attacker's own valid credential. It is an attack on keys in use (E3), but on the relying party's code, not on the factors, so it falls under x5 for this question. It would belong under R8 or a new "server-side flaws" remark if the report ever discusses implementation errors; it does not contradict anything in RQ2.

## 6. Anything in the Results for RQ2 that I now think is wrong, overstated or understated

Nothing found to be wrong. Two remarks:

1. "A password beside a key" rests, for the remote threats, on one formal analysis (assumed lost password), the NCSC table and two providers' reports. After the uncapped search it still rests on those: no new source tests a key with and without a password. The statement "no source shows the password adding anything" remains true; its strength remains "absence of evidence from a search, supported by analysis". I would keep the wording "no source shows", not "the password adds nothing".
2. The cell for R2 (stored credentials) and the whole L2 column, and case C against every threat, stay empty. The uncapped search for these (S2, C2 on all databases) turned up no evidence for them: the only R2-related new records are schemes (x1, e.g. a "passwordless web SSO mitigating server breaches"). That is a result of the search, not a gap in it; the report's limitation sentence can say that the search was repeated without cap and still found nothing for R2, L2 and case C.

## 7. Limitations and what I left undone

- Abstracts: 86 of 588 records (40 of the new 290) have none, because Scopus gives none and OpenAlex and arXiv did not hold them; they were classified on titles. IEEE was not used for enrichment (quota), Semantic Scholar's key is rejected.
- Most new records are low-grade (conference papers of schemes, Zenodo uploads, podcasts, student theses). That is what an uncapped title-and-abstract search returns; it is why only 4 records turned out to bear on the question.
- Read in full: 3 (Wasser, the Nigerian experiment, the simulation). Others that could have changed a result were not obtainable (3 listed in 5); I did not work around the ACM bot check or the 403.
- The "new" set is defined by the paper identifier against yesterday's backup of the session (`round2/backup/mfa-attribution.json`); records whose identifier changed (13) count as new although they are the same work.
- The classification used `--no-examples` and the model named; the Copilot-models warning in the output (HTTP 403) is harmless.
- Not done: I did not read the full text of the 17 low-confidence adjacent records, only title and abstract (or title only for 8 without abstract); none looked as if it could change a result. I did not re-screen the 298 old records, whose abstracts the enrichment partly filled in.

## 8. Commands

```
scholar enrich mfa-attribution --enrich-providers openalex,arxiv     # timeout 1500
scholar llm context mfa-attribution "<RQ2 text, criteria and tags as in the brief>"
scholar llm classify mfa-attribution --no-examples -m anthropic/claude-sonnet-5-5 -n 289 \
  -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit \
  -t x1-new-scheme -t x2-machine -t x3-usability-only -t x4-no-evidence -t x5-other-question -t x6-not-english --no-enrich
$PY $R2/relabel.py mfa-attribution "<RQ2 text>"                       # 214 labelled; second run 0 of 0
$PY $R2/retag.py mfa-attribution adjacent-subtopic x4-no-evidence -- doi:10.34190/ecsm.13.1.4685 doi:10.47772/ijriss.2025.908000647 doi:10.2139/ssrn.6759998
$PY $R2/retag.py mfa-attribution adjacent-subtopic x1-new-scheme -- hash:a92f0d604bea9aee
scholar sessions decide mfa-attribution --keep --paper-id doi:10.5281/zenodo.23956049 -t key-resists-remote
scholar sessions export mfa-attribution -f csv -o <OUT>/mfa-attribution
scholar sessions export mfa-attribution -f table --bearing-only --lang en --label hits-attribution \
  --track "What each factor contributes" --theme local-malware="Local attacks and malware" \
  --theme key-resists-remote="A key resists remote attacks" --theme fallback-recovery="Fallback and recovery" \
  --theme synced-passkeys="Synced passkeys" --theme second-factor-weakness="Weak second factors" \
  --theme formal-analysis="Formal analysis" -o <OUT>/mfa-attribution-full
python3 ~/.claude/skills/backing-claims/scripts/check_provenance.py <OUT>/mfa-attribution-round2.bib   # OK
python3 ~/.claude/skills/backing-claims/scripts/check_metadata.py <OUT>/mfa-attribution-round2.bib     # DataCite-only DOI: checked by hand
```
