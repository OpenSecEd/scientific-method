# Round 2, RQ3 (sufficiency): screening of the uncapped searches, session `mfa-sufficient`

Date: 2026-11-13. Output directory: `/tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/round2/mfa-sufficient/`.
Sections 2 to 7 of the brief. Section 1 (query matrix), the CSV and the table export, and the cleaning of theme tags and invented tags
(`unreviewed-not-verified` is on 151 records) are left to the lead, as agreed. The matrix as it stood before classification is in `matrix-before.txt`.

## 2. Counts

- Records in the session: 515 before today, 4005 now (3490 new; the lead's figure of 3489 pending was one short of the number of new records, the
  difference is one record that was already classified).
- Classified today (new records, 3490), after my changes: supports-claim 67, qualifies-claim 12, adjacent-subtopic 1497, off-topic-false-hit 1914.
  Before my changes: supports 118, qualifies 12, kept in total 130; I moved 54 records out of "bearing" and 3 from qualifies to supports (see below).
  Of the 515 old records, 45 are kept (33 supports, 12 qualifies); not touched.
- Exclusion labels on ALL discarded adjacent records of the session (after `relabel.py`, 348 labelled, 0 left without label):
  x1-new-scheme 1085, x5-other-question 887, x4-no-evidence 615, x2-machine 265, x3-usability-only 122, x6-not-english 35 (sum 3009).
  The sum exceeds the 1844 adjacent records because the classifier also put x-tags on many off-topic-false-hit records (2037 in all, 3817+ discards in total); I did not remove them. `relabel.py` found no adjacent discard without a label afterwards.
- Abstracts missing: 744 of 4005 (604 of the new). Enrichment through OpenAlex and arXiv timed out after 25 minutes (07:59); those records were classified on their title.
- Records without a confidence value: the session gives no confidence for these runs (`conf` empty in the export), so the brief's "confidence below 0.7" check could not be done.
  I did NOT read the low-confidence discards; instead I read every new kept record (130) and not the 3360 discards. Discarded records that should be bearing are therefore unchecked.
- My changes to the model's classes (new records only), by kind:
  - new scheme, cryptanalysis of a scheme, or detection method filed as supports: 16 -> x1-new-scheme
  - book chapters, narrative reviews, theses, framework papers, an extended abstract with no results (43): 15 -> x4-no-evidence
  - bearing on another question or not authentication (forensics of 2FA apps, Android Keystore, browser fingerprint spoofing, trojan web-injects, Signal phishing, TEE): 9 -> x5-other-question
  - not in English (Russian, Slovene, Swedish, Finnish, Indonesian x4): 8 -> x6-not-english
  - IoT protocol: 1 -> x2-machine; unrelated (Dropbox reverse engineering, deepfakes): 2 -> off-topic-false-hit
  - qualifies -> supports (a PIN-choice study with 40 per cent guessable PINs, two lab/data studies of AiTM): 3
  Total 54 moves out of "bearing" + 3 class changes of kept records = 57 changes.
- Systematic errors found: (a) the model files every attack on a scheme, including cryptanalyses of authentication schemes that nobody uses, as "supports"
  (x1); (b) it files popular-security books, case studies posted on Zenodo and narrative reviews as bearing; (c) it filed measurement studies and lab
  demonstrations of AiTM as "qualifies" (3 corrected); (d) the same paper appears under several records (preprint, journal and chapter versions: Titan x3, Barbosa, Jacomme x3, PRMitM x4,
  "Analysis of attacks on SMS OTP" x2, "Phish in Sheep's Clothing" x2, "Security analysis of SMS" x2, FIDO downgrade x2): these are counted once in section 4.
  (e) A prototype of the kind "agrees with the expected answer" was not a large problem in this strand; the lead's warning was about the other direction and I applied it by moving 16 schemes.

## 3. Records read in full

Only two records could change a result and were obtainable; both are proposed for citation. `mfa-sufficient-round2.bib` (provenance checked, `check_provenance.py` OK, `check_metadata.py`: 0 problems, both entries have no DOI, authors checked against the PDF title pages).

### 3.1 Roche2021Titan (USENIX Security 2021), record hash:3c382570ddeda346 (duplicates hash:9e7492edf66e7c32, chapter 10.1002/9781394351930.ch12)
- Grade: E3 (laboratory demonstration on a deployed product, peer reviewed).
- Case and threat: A3 and B (hardware key, FIDO U2F), L1 (device in the attacker's hands), with R3 as the way to get the password.
- Finding: the private key of an account on a Google Titan Security Key can be extracted with about 10 hours of physical access and electromagnetic side-channel measurements; the attacker then signs in without the key and the victim does not notice (the paper notes a counter can later reveal the clone).
- Quote (sec. 1, abstract): "This allows, given physical access to a Google Titan Security Key during about 10 hours, to retrieve a user-specific secret key (there is one key for each remote account) and therefore to clone the security key."
- What it changes. The report's cells (table `tab:local`) say L1 for A3 and B is `\partly`, resting on NCSC's rating that a separate hardware token is "not exposed" and on PIN-extraction attacks on platform authenticators. This is the first source found where the key itself is extracted and the account taken without the key, for a deployed security key, with the password assumed stolen (the paper's attack scenario, sec. 2.3).
  - Now: "A lost or stolen device (L1) ... a separate hardware token as not exposed, whether the token produces codes or holds a key unlocked by a PIN or password" (NCSC) followed by the PIN-extraction demonstrations.
  - Proposed: add one sentence after the NCSC rating: "That rating is contradicted for one product: given the password and about ten hours of physical access, the secret key on a Google Titan Security Key was recovered by a side-channel attack and the key cloned, so that the account could be entered without the key \autocite{Roche2021Titan}; the flaw was in the chip's implementation of the signature algorithm and was disclosed to the manufacturer." Cell: L1 for A3 from `\partly` to `\fail` (a demonstration on one product; the key was without user verification, so case B with user verification is not tested by this paper and stays `\partly`).
  - In Sufficiency, the paragraph "No source reports an attack that defeats the key itself from a distance" stays true ("from a distance" carries the weight), but the next sentence "The attacks that succeed go around the key" is now not true for L1: add "The one exception is an attack on the key itself that needs the key in the attacker's hands for hours \autocite{Roche2021Titan}".

### 3.2 ScottRailton2015London (Citizen Lab report 61, 2015), record hash:0bdfd6bcbaab731c
- Grade: E5-E4 (investigation of real incidents by an independent group; small number of selected targets, not a measurement).
- Case and threat: A1 (password and code by text message), R4 (relay as it happens), with R3.
- Finding: a campaign against Iranian diaspora targets relayed the Gmail password and the code to the real site while the victim was on the phone or on a fake page.
- Quote (Summary): "The ongoing attacks attempt to circumvent the extra protections conferred by two-factor authentication in Gmail, and rely heavily on phone-call based phishing and “real time” login attempts by the attackers."
- What it changes. The paragraph "Phishing (R3, R4)" supports the failure of A1 against R4 with a laboratory relay (Kikuchi2025Evilginx) and a controlled campaign (Cuellar2026AiTM); Sufficiency says A1 and A2 failures "are documented in use" but the cited in-use evidence is the SIM swap review (R5) only.
  - Proposed: in "Phishing" after the Cuellar sentence: "The same relay was used against real targets already in 2015: an investigation of a campaign against Iranian activists found attackers who phished the password and the code by text message and entered both at once \autocite{ScottRailton2015London}." This gives R4 for A1 an observation in use (a few targets, a decade old); in Sufficiency this makes the sentence "the attacks are documented in use" hold for R4 as well as R5.

### 3.3 Read in full but not proposed
- Krumm, Dekinder and Donnet 2026 (10.1145/3843179.3858058): a one-page proposal for measuring the challenge quality of FIDO2 deployments; no results. x4-no-evidence. It would matter (a measurement of real deployments) if the full study appears.
- Panchenko 2025 (10.21681/2311-3456-2025-6-48-57): in Russian; a Trojan-based man-in-the-middle against WebAuthn in a laboratory. Moved to x6-not-english; it repeats the L3 attack already covered by Mitra2026WoodenHorse and Yadav2024LocalAttacks.

## 4. Corroboration at abstract level (new kept records, 79 after my changes; grouping is mine and counts are approximate to plus or minus 2)

Duplicates of sources already in the report are listed separately (15 records: Kunke, Lin2022PhishSheep x2, Jacomme x3, Wang2025TwoFAIllusion, Barbosa2021, Catalano, Barbosa2023RogueKey, Yadav, Mahdad2024, Egenti, Jubur, Mirian) and are not counted below.

| Group | Records | What they corroborate | Notable titles |
|---|---|---|---|
| Codes by text message or app against R4, R5, R8 (A1) | 21 | SIM swap, SS7, password-reset man in the middle (PRMitM, 4 versions), malware relays, flaws in authenticator apps | "Security analysis of SMS as a second factor of authentication" (CACM/ACM 2020); "Understanding the implications of SIM card swap fraud in India"; "OTP bots and crypto: a tactic to disrupt"; "Security Analysis of Google Authenticator, Microsoft Authenticator, and Authy" |
| Real-time relay and AiTM kits, observed or measured (R4, R7, A1 and A2) | 18 | kits in use, phishing-as-a-service, campaigns, hack-for-hire, case reports of breaches | "Catching Transparent Phish" (CCS 2021, measurement of kits in the wild, ACM bot check, abstract only); "Proxy in a Haystack: Uncovering and Classifying MFA Bypass Phishing Attacks in Large-Scale Authentication Data" (2023, not obtained); "Hack for Hire" companion (2019 market study); "Deconstructing Tycoon 2FA"; Citizen Lab "Spying on a Budget" (Tibet, 2018) |
| Push approvals (R6, A2) | 2 | notification bypass and number-matching; the notification paper (MobiCom 2023) is on the lead's list | "Breaking Mobile Notification-based Authentication with Concurrent Attacks Outside of Mobile Devices"; "The Verification Illusion: Hardening Push-Based MFA with Context-Rich Number Matching" (2026, controlled experiment) |
| Keys, A3 and B: attacks on the key or the device (L1, L3, R4, R8) | 15 | extraction of keys, PIN brute force, social-engineering downgrade (2 versions), CTAP interception, session replication through QR codes, malware on the phone, BitM in both browser and protocol | "A Side Journey to Titan" (3 records, section 3.1); "Hello Again: Exploiting Replay Protected Monotonic Counters to Brute-Force Windows Hello PINs" (CCS 2026, artifact record, paper not obtained); "Is Real-time Phishing Eliminated with FIDO? Social Engineering Downgrade Attacks against FIDO Protocols" (2021, ETH, not obtained); "HiPass: Hijacking CTAP in Passkey Authentication"; "Mobile Login Bridge: Subverting 2FA and Passwordless Authentication via Android Debug Bridge"; "BitM+ attack ... defeating the FIDO/CTAP2 protocol and the W3C WebAuthn API" (SSRN preprint) |
| Recovery of MFA accounts (R8) | 1 plus the 4 PRMitM versions above | weak recovery channels | "Quantifying Internet Privacy and Security Risks in Authentication Recovery Channels" (2025) |
| Qualifies: formal analyses and measurements that resist | 6 plus Barbosa, Jacomme, Egenti duplicates | formal analysis of FIDO 1.x, of FIDO2 as a whole (PoPETs 2025), of a national SMS-OTP scheme, of MitID; CERN deployment (2000 phished passwords in a drill, 2FA introduced afterwards); effectiveness surveys in Ghana | "Privacy and Security of FIDO2 Revisited"; "Formal analysis of the FIDO 1.x protocol"; "Security keys: Practical cryptographic second factors for the modern web"; "The Second-Factor Authentication System at CERN" |

Does any group change the wording? The AiTM group (18, many of them measurements or reports of kits in use) strengthens "real-time relay is observed, not only demonstrated" for A1 and A2 and I recommend that wording (Sufficiency, section 3.2). No group is large enough to change the grade for A3 and B: the 15 key records are laboratory demonstrations and preprints (E3-E4) of attacks by an attacker with physical access, a local foothold or a deceived user, as the report already says. No new record reports a key-protected account taken over in real use, and none the key itself defeated from a distance. Three records are CTAP or BitM demonstrations (HiPass, BitM+, session replication): they need local malware, a hostile page or a nearby attacker, which are the conditions already stated in the report.

Counts per threat among the new bearing records (a record can count under several): R4 about 24, R5 about 8, R6 2, R7 about 6, R8 about 7, L1 5, L3 5, R3 3. Cells of the tables that were empty: R6 for cases A3, B (key) still has no attack and no new test; R2, L2, and the whole row C: no new record (none tests a key alone). The only new record for an empty cell is the Titan paper for L1 under A3.

## 5. New records that contradict or narrow a claim but were not read in full

- "Evaluating the Security Posture of Real-World FIDO2 Deployments", ACM CCS 2023, 10.1145/3576915.3623063: tests FIDO2 relying parties in deployment; the ACM site refused the download (bot check). Abstract only: it says FIDO2 gives strong guarantees "assuming the benign behavior of the client-side protocol components", which narrows the claim for A3 and B to the client assumption. Could change the cell for R8 or L3 if it measures real sites. On the author's list.
- "Proxy in a Haystack: Uncovering and Classifying MFA Bypass Phishing Attacks in Large-Scale Authentication Data" (2023, session id hash:de4b6c92d9054696, no DOI, no abstract): the title announces a measurement of real AiTM attacks in authentication logs, the kind of source the brief asks for (frequency of the documented attacks). Not found on arXiv, OpenAlex or Crossref in a title search; needs a manual search.
- "Is Real-time Phishing Eliminated with FIDO? Social Engineering Downgrade Attacks against FIDO Protocols" (2021, hash:3e5df107697e1ed1; ETH research collection 10.3929/ethz-b-000521513, no open PDF served): abstract says "social engineering attacks allow an adversary to downgrade" the key to a weaker method. This is the same threat as Miron2025Downgrade (R8 for keys) and is older; the report's phrase "a vendor demonstrated this" could cite it as an academic precedent.
- "Catching Transparent Phish" (CCS 2021, 10.1145/3460120.3484765): ACM; measurement of MITM kits and their servers in the wild; frequency evidence for R4.
- "Hello Again" (CCS 2026, https://doi.org/10.1145/3830454.3846631; only the Zenodo artifact 10.5281/zenodo.22704918 was in the search): PINs of four digits on Windows Hello brute-forced via replay of monotonic counters; would add to L1 beside Lee2025WindowsHello.
- "Mobile Login Bridge" (IEEE PST 2024, 10.1109/pst62714.2024.10788081) and "Breaking Mobile Notification-based Authentication" (MobiCom 2023, 10.1145/3570361.3613273): abstracts only.

## 6. What in the Results for RQ3 I now think is wrong, overstated or understated

1. Table `tab:local`, case A3, L1: `\partly` understates; with Roche et al. it is `\fail` for a key without user verification, on one product, with the password stolen. The sentence quoted in section 3.1 contradicts the NCSC rating, and the report should say so as it does for L3 ("which the demonstrations above contradict").
2. Sufficiency, "none reports an account protected by a key being taken over in use" and "No source reports an attack that defeats the key itself from a distance": both remain true in this round's 79 new records; the phrase "The attacks that succeed go around the key" does not hold for L1 (section 3.1).
3. Sufficiency, "the attacks are documented in use" for A1 and A2: the in-use evidence cited is the SIM-swap review (R5); R4 relays in use are now documented by the Citizen Lab report (2015) and by several kit analyses at abstract level (not read). Understated; not wrong.
4. The R6 paragraph says "We found no report of the frequency of this attack in use". No new record changes that; the number-matching experiment (2026) and the MobiCom paper are demonstrations.
5. I found nothing that contradicts the conclusion that H-sufficient is supported, or its difference of strength between codes/push and keys.

## 7. Limitations and what was left undone

- 744 records have no abstract; 604 of the new ones were classified from their title alone. The brief's check of confidence below 0.7 was impossible (the export gives no confidence for these runs), and the 3360 new discards were not read; a missed bearing record among them is possible. The kept records were read in 420-character excerpts of the abstract for the 130 new kept, plus titles; for the 54 I moved, the excerpt was enough to see the type, for the rest I did not read the full abstract.
- The classifier left 3490 records in one session; the grouping in section 4 is mine and approximate.
- Fetches: ACM, IEEE and SSRN pages served no PDF (bot check; stopped there as instructed); the ETH research collection and ninjalab copies were not available. Only three PDFs were read through (Roche, Scott-Railton and Kleemola, and, in part, two others in section 3.3).
- Left undone: reading in full the five records in section 5; querying provider reports on frequency of attacks in use; checking whether the 2023 USENIX/CCS follow-ups on FIDO2 deployments have a measurement of real websites.
- Session facts: 4 human decisions in the session (2 kept, 2 discarded) were not changed. Session write contention: classification and relabelling ran one after the other in the background; nothing else touched the session.
- Theme tags: I set `fidoatk` on hash:3c382570ddeda346 (Roche2021Titan) and `aitm` on hash:0bdfd6bcbaab731c (ScottRailton2015London), the only two records proposed for citation. No `strip_themes.py` was run (the lead does it). Note for the lead: both records have duplicates (Titan: hash:9e7492edf66e7c32 and 10.1002/9781394351930.ch12) that should keep no theme tag.

## 8. Commands

Classification (in a loop of batches of 100, `loop.sh`, 35 batches, about 1 minute each, 09:03 to 09:40):

    scholar llm classify mfa-sufficient --no-examples -m anthropic/claude-sonnet-5-5 -n 100 -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit -t x1-new-scheme -t x2-machine -t x3-usability-only -t x4-no-evidence -t x5-other-question -t x6-not-english --no-enrich

Enrichment (timed out at 25 minutes, 744 abstracts missing): `timeout 1500 scholar enrich mfa-sufficient --enrich-providers openalex,arxiv`.
Labelling: `$PY -I $R2/relabel.py mfa-sufficient "<question>"` (348 of 348 labelled).
Retagging: `$PY -I $R2/retag.py mfa-sufficient <category> [<x-tag>] -- <ids>`, commands in `retag.sh`; the full list of moved ids is in `retag.sh`, the 130 kept new records with abstract excerpts in `newkept.txt`.
Table export (for the lead, not run by me): the command in the prompt with `-o <OUT>/mfa-sufficient-full`.
Files: `mfa-sufficient-round2.bib`, `mfa-sufficient-round2-report.md`, `newkept.txt`, `newkept.json`, `retag.sh`, `classify.log`, `relabel.log`, `matrix-before.txt`, `dump.json`.
