# RQ3 (sufficiency): is multi-factor authentication sufficient against threats R1-R8, L1-L3?

Session name and slug: `mfa-sufficient`. Date of the search: 2026-11-12. Output directory:
`/tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/mfa-sufficient/`

Files: `mfa-sufficient.bib` (26 entries, provenance blocks; `check_provenance.py`: OK; `check_metadata.py`: only benign
mismatches, see Limitations), `mfa-sufficient.csv` (515 records, classified), `mfa-sufficient-full.tex` (hit table, 20 cited rows),
`providers-check.txt`, `overrides.log`, per-query CSVs `s1-*.csv s2-*.csv c1-*.csv s3-*.csv c2-*.csv`.

## 1. Answer in one paragraph

The evidence supports the protocol's prediction in a narrower form than stated. For A1 (code by text message or app) and A2 (push)
there are documented attacks that succeed: real incidents for SMS (SIM swap, R5, authority review), laboratory and survey evidence
for real-time relays (R4) and for trusted-device cookies (R7). For A3 and B the evidence is thinner and of lower grade: no source
shows a successful remote attack on the key itself (R3/R4 resist in every source that tests it), but there are demonstrated
successful attacks under other conditions, all in the laboratory or as vendor proof of concept: downgrade to a weaker method
plus session theft (R8, R4, R7; Proofpoint, not seen in the wild), malware on the user's device (L3; Yadav, Mitra), local
attacks on a platform authenticator through implementation flaws (L1/L3; Lee), and weak recovery (R8; Kunke). No source
isolates case A3 (password plus key) from case B; what is said about "FIDO2" is inherited by both. No incident report of an
account takeover that defeated a FIDO2 key in real use was found. Strength: strong for "not sufficient" on A1/A2 (E2/E3),
moderate-to-weak for A3/B (E3, mostly lab, several preprints, three key papers abstract only). Main narrowing evidence:
Barbosa et al. (provable security confirms WebAuthn authentication, CTAP2 only weakly), Berladskyy and Asmuth (attacks on
passkeys "require substantial effort and resources"; phishing resistance "largely holds true"), Cloudflare and Google
provider reports (E6) of zero compromise by phishing with security keys, and Doerfler et al. (device-based challenges block 94%
of phishing hijacks and 100% of bots, i.e. strong but not complete). The hypothesis H-sufficient ("for each of A1-A3 and B at least one
threat succeeds") is not refuted for any case; for A3 and B it rests on conditional, lab-demonstrated attacks.

## 2. Providers check (verbatim, `scholar providers check`, 2026-11-12 10:17)

```
Route: direct
  s2               Yes   key rejected   HTTP 403 -- check or replace S2_API_KEY
  openalex         Yes   ok             API key configured; $0.993 of $1.00 daily budget left
  dblp             Yes   http error     non-JSON response (HTTP 202, text/html)
  wos / ieee / arxiv / scopus (standard view: no abstracts, first author only) ok
```
Semantic Scholar and DBLP: **not searched** (as instructed). Later in the day `scholar providers limits` showed
IEEE Xplore **quota exhausted** (200/200 per day, shared with other agents): the two extra queries S3 and C2 were **not run on
IEEE** (failed cells below). OpenAlex use shown by `providers limits` at the end: 2178 requests today for all agents together; my own count
cannot be isolated (about 25 search calls plus abstract enrichment lookups through the shared cache); no HTTP 429 was seen from OpenAlex.
Web of Science timed out once on a first attempt (30 s read timeout); that attempt was discarded with the session it
belonged to and the query was rerun, same string, in the final session.

## 3. Query x provider x hits matrix (from `scholar sessions show mfa-sufficient`, limit 40 per cell)

M = "multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification"

| Query | OpenAlex | IEEE | arXiv | WoS | Scopus |
|---|---|---|---|---|---|
| S1: M AND (bypass OR phishing OR "man-in-the-middle" OR "adversary-in-the-middle") | 40 | 40 | 18 | 40 | 40 |
| S2: M AND ("SIM swap" OR "push fatigue" OR "prompt bombing" OR "session hijacking" OR "account recovery") | 40 | 19 | 3 | 21 | 37 |
| C1: M AND ("formal verification" OR "provable security" OR "security proof" OR "phishing-resistant") | 40 | 40 | 2 | 40 | 40 |
| S3 (added): K' AND (attack OR bypass OR downgrade OR vulnerability OR phishing OR "man-in-the-middle" OR "adversary-in-the-middle" OR "account recovery" OR "session hijacking" OR malware) | 40 | **failed (IEEE daily quota exhausted)** | 40 | 40 | 40 |
| C2 (added): K' AND ("formal verification" OR "formal analysis" OR "provable security" OR "security proof" OR "phishing-resistant" OR "security analysis") | 40 | **failed (IEEE daily quota exhausted)** | 40 | 40 | 40 |

K' = passwordless OR passkey OR passkeys OR FIDO2 OR WebAuthn OR "security key" (the protocol's K block without "single-factor", which concerns RQ4).

Exact strings sent (concept clause C replaced per query as in the table):
- OpenAlex, IEEE, arXiv: `(M) AND (C)` with M and C as written above, e.g. S1: `("multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification") AND (bypass OR phishing OR "man-in-the-middle" OR "adversary-in-the-middle")`
- WoS: `TS=((M) AND (C))`, e.g. `TS=(("multi-factor authentication" OR ... OR "two-step verification") AND (bypass OR phishing OR "man-in-the-middle" OR "adversary-in-the-middle"))`
- Scopus: `TITLE-ABS-KEY((M) AND (C))`, same keywords.
- For S3 and C2 the same three wrappers with `(passwordless OR passkey OR passkeys OR FIDO2 OR WebAuthn OR "security key")` in place of M.
The scripts that sent them are `run.sh` and `runk.sh` in the output directory. arXiv returns few hits for M-based queries
(2 to 18): its phrase search is narrow; this is recorded as the count, not as a gap in the literature.

## 4. Complements (non-scholar searches), all 2026-11-12

| Tool | Verbatim query / URL | Outcome |
|---|---|---|
| WebSearch | `adversary-in-the-middle phishing bypasses multi-factor authentication advisory CISA` | vendor blogs only; one MS-ISAC (CIS) 2023 item; no CISA AiTM advisory found; nothing retained |
| WebSearch | `phishing-resistant multi-factor authentication FIDO WebAuthn fact sheet government guidance` | led to the CISA fact sheet; retrieved from cisa.gov (CISA2022PhishingResistant) |
| WebSearch | `MFA fatigue push bombing incident review board report Lapsus$ authentication` | led to the CSRB Lapsus$ review; press about Uber 2022 dropped (news is not evidence) |
| WebSearch (allowed_domains cisa.gov, dhs.gov) | `Cyber Safety Review Board Review of the Attacks Associated with Lapsus$ and Related Threat Groups report pdf` | PDF URL; fetched with `fetch_pdf.py` (CSRB2023Lapsus) |
| WebSearch | `Cloudflare 0ktapus phishing attack hardware security keys prevented account takeover postmortem` | Cloudflare blog 2022-08-09; fetched with curl (Cloudflare2022Phishing); other results are press |
| WebSearch | `passkey downgrade attack authentication method fallback bypass WebAuthn session cookie theft infostealer` | vendor blogs (SpyCloud, Netcraft, Hacker News, Recorded Future); only Proofpoint retained after retrieval from the issuer; SquareX / Recorded Future / Google DBSC claims were not retrieved and are **not cited** |
| WebSearch (allowed_domains proofpoint.com) | `Proofpoint researchers phishing proxy downgrade FIDO authentication Microsoft Entra unsupported browser spoof` | Proofpoint blog 2025-08-12; fetched with curl (Miron2025Downgrade) |
| WebSearch | `Google security blog new research how effective is basic account hygiene at preventing hijacking security key phishing bots targeted attacks` | Google Security Blog 2019-05-17; fetched with curl (Thomas2019Hygiene) |
| WebSearch (allowed_domains nist.gov, pages.nist.gov, csrc.nist.gov) | `NIST SP 800-63B-4 Digital Identity Guidelines Authentication and Authenticator Management phishing resistance requirement AAL2` | final SP 800-63B-4 PDF fetched with `fetch_pdf.py` (NIST2025SP80063B) |
| WebSearch (allowed_domains usenix.org) | `Adventures in Recovery Land: Testing the Account Recovery of Popular Websites When the Second Factor is Lost SOUPS 2023 usenix` | **known-item retrieval** of an open-access PDF for a paper already found by scholar (WoS, Scopus; abstract-only records); not discovery |
| WebFetch | `https://blog.cloudflare.com/2022-07-sms-phishing-attacks/` (quote check) | confirmed; the quote was then located in the curl-fetched text |
| Zenodo REST | `https://zenodo.org/api/records/23955576` | returned HTML, not JSON; English full text not obtained |
| alphaXiv | not used | |

KTH SOCKS tunnel (127.0.0.1:1081) was used for two Springer chapters (Kikuchi, Cuellar), the ESORICS and CRYPTO chapters and the Springer
journal article, with plain `curl` (Python `requests` via `fetch_pdf.py` got an HTML page from Springer). No bot check or login form was served;
nothing was worked around. ACM (Doerfler, Wee published version, Campobasso published version) answered 403 to `fetch_pdf.py`: stopped; arXiv copies used where they exist.

## 5. Flow counts

- Records returned by the 23 answered query x provider cells: 780 (S1 178, S2 120, C1 162, S3 160, C2 160). IEEE cells of S3 and C2 not run.
- After scholar's de-duplication: **515 records** in the session (the table generator counts **508** unique hits, merging records of the same work found in two providers).
- Classified (model, whole session): **supports-claim 33, qualifies-claim 12, adjacent-subtopic 347, off-topic-false-hit 123** (sum 515). Left pending: 0.
- Abstract missing for 30 records after `scholar enrich` (mostly Scopus standard view); these were classified from title only.
- Read in full text: 20 sources (14 papers, 6 grey: CSRB, CISA, NIST, Cloudflare page, Proofpoint page, Google page). NIST read for the quoted passages only.
- Read as abstract only: 6 cited papers (Pazmino2025Cookie, Wang2023Proofs, Bindel2023FIDO2, Doerfler2019Challenges, Lee2025WindowsHello, Wasser2026Resilience).
- Cited: **26** (all in `mfa-sufficient.bib`). Four further records classified supports-claim were considered and not cited (SoK on web authentication and recovery; Mobile Paradox push-fatigue study; SIM-swapping student thesis; AI-driven identity attacks SOC dataset): their abstracts do not state a finding on a case; not cited.
- `scholar verify mfa-sufficient`: 0 retracted, 2 corrected (both off-topic hits), 0 superseded, 394 ok, 119 unknown.

## 6. Deviations from the planned queries

1. **Added S3 and C2** (not in the protocol). Reason: C1 as planned returned mostly new-scheme proposals (smart-card/WSN/IoT two-factor schemes with their own proofs, which the protocol counts as adjacent) and almost nothing on FIDO2/WebAuthn, i.e. nothing on cases A3 and B, which the task singles out. S3 and C2 reuse every concept term of S1/S2/C1 (attack/bypass/phishing/MITM/AiTM/recovery/session hijacking/malware; formal verification/provable security/security proof/phishing-resistant) and add the field's own terms for the key-based schemes (passkey, FIDO2, WebAuthn, "security key", "formal analysis", "security analysis", downgrade). The originals S1, S2, C1 stay in the session and the matrix. C2 adds "formal analysis" and "security analysis" to the C1 terms; S3 adds downgrade, vulnerability and malware to S1/S2.
2. S3 and C2 **failed on IEEE** (daily quota exhausted); those two cells are failed, not zero. The relevant IEEE papers (Bindel, Lee) arrived through WoS/Scopus/OpenAlex.
3. The default `llm` model of this machine (`openai-codex/gpt-5.6-sol`) is rejected by `llm` ("Unknown model"); classification used `anthropic/claude-sonnet-5-5` instead (`-m`). First classification pass ran without the four category tags in the vocabulary and lost the qualifies-claim and off-topic categories (no category assigned to many papers); I reset all decisions to pending in the session file (backup copy `session-before-reclass.json` here) and reran with the four tags passed by `-t`. All numbers above are from the rerun.
4. K' omits "single-factor" from the protocol's K block, since that term concerns RQ4.
5. Grey literature was searched with concept queries only (table in section 4); the Adventures in Recovery Land search used the title because it retrieved an already identified item.

## 7. Attacks documented (cases A1 code, A2 push, A3 password+key, B key with user verification)

| Source key | Year | Case | Threat | Lab or real use | Conditions | Grade |
|---|---|---|---|---|---|---|
| CSRB2023Lapsus | 2023 | A1 by **text message** | R5 (SIM swap) | real use (2021-22 intrusions) | attacker gets the phone number moved, via telecom provider staff tools; reviewed by a public board | E2 |
| Kikuchi2025Evilginx | 2025 | A1 (SMS, call, e-mail, **app TOTP**) and A2 (push) | R4 | lab relay + survey of 102 sites; FIDO resistance only assumed | victim visits the proxy; session token captured; 80% of surveyed services judged vulnerable | E3 |
| Cuellar2026AiTM | 2026 | A1/A2 unspecified | R4 | controlled campaign, n=30 | AiTM flow, simulated credentials; exploratory | E1 |
| Wang2024Simple | 2024 | A1 (2FA with "remember device" cookie) | R7 (forge or reuse the 2FA cookie) | lab on real services, test accounts | 3 zero-days in 93 sites relying on cookies; services anonymised | E3 |
| Campobasso2020IMPaaS | 2020 | MFA unspecified | R7, L3 (stolen profiles incl. cookies) | observed: live criminal platform, 260,000 profiles | infostealer-style profile theft; bypasses risk-based auth and MFA | E3 |
| Pazmino2025Cookie | 2025 | MFA unspecified | R7, L3 | review (abstract only) | malware-as-a-service cookie theft | E5 |
| Gerlitz2023Recovery | 2023 | A1/A2 (SMS, app) | R8 | audit of recovery on popular sites; attacker view not tested | second factor disabled by a request without proof; code by e-mail in six cases | E2 |
| Kunke2021Recovery | 2021 | A3/B | R8 | heuristic evaluation, no attack run | recovery methods for lost tokens, some rely on passwords | E5 |
| Miron2025Downgrade | 2025 | A3/B (Entra ID) | R8, then R4/R7 (session cookie import) | vendor lab PoC (Evilginx phishlet); "no evidence ... in the wild" | spoof an unsupported user agent so FIDO is not offered; needs an alternative method enrolled | E3 (E6 provider) |
| Yadav2023Local | 2023 | A3/B | L3 (malicious browser extension), L1 (physical access to key) | lab on 10 popular FIDO2 sites; no evidence in the wild among extensions | seven attacks from four flaws (message confidentiality to extensions, clone detection, social engineering via messages, cookie life cycle) | E3 |
| Mitra2026Wooden | 2026 | A3/B | L3 (Trojan), R7 | lab PoC, 100% success against the tested setup | local malware; evaded Defender and 60+ engines | E3 |
| Lee2025WindowsHello | 2025 | B (Windows Hello platform authenticator) | L1/L3, implementation flaw (TPM misuse; template injection; passkey migration) | lab, abstract only | only systems with Enhanced Sign-in Security resisted | E3 |
| Casagrande2025CTRAPS | 2025 | A3/B | proximity or remote CTAP client attacks (no R/L fits exactly) | lab on 6 authenticators, 10 relying parties | deletes passkeys without interaction; **not shown to authenticate as the user** | E3 |
| Mitra2026Trust | 2026 | B | L1-L3 (eight vectors) | analysis, preprint | environment assumptions of FIDO2 do not hold when browser, OS or hardware is compromised | E4 |
| Ang2025Excavating | 2025 | academic MFA protocols (smart-card/WSN) | scheme-level | analysis | vulnerabilities in ten of the investigated protocols; not deployed web MFA | E4 |
| Wang2023Proofs | 2023 | MFA schemes with proofs (abstract only) | scheme-level | analysis | most "formally proven" schemes later found insecure | E4 |
| CISA2022PhishingResistant | 2022 | A1, A2 | R3, R4, R6 (push bombing named as an attack class) | guidance, no incident data | states vulnerability, not incidence | E5 |

Not found: a peer-reviewed or authority-reported **incident** of push bombing (R6) succeeding. CISA names it; press on Uber 2022 was dropped.

## 8. Results claiming security

| Source key | Case | Threat model assumed | What is proved or measured | What it leaves out |
|---|---|---|---|---|
| Barbosa2021FIDO2 (E4) | A3/B | as modelled by the authors (WebAuthn and CTAP2 analysed separately); the model was not audited, only abstract and introduction read | WebAuthn authentication security proved; CTAP2 only in a weak sense; flaws found | malware (L3), recovery (R8), session (R7), downgrade, user behaviour |
| Bindel2023FIDO2 (E4, abstract only) | B | formal model of CTAP 2.1/WebAuthn 2 including user verification | first formal analysis of this version; downgrade resilience improvable for some threat models | same as above; not read in full |
| Guan2022FormalFIDO2 (E4) | A3/B | symbolic model of FIDO2 as a whole | finds that FIDO2 **fails** some strong authentication properties; Client PIN flaws | listed in 7 only as analytical weakness; properties not audited |
| Wasser2026Resilience (E3, unreviewed preprint) | B, A3 | worst-case attacker, 100% user compliance, lab, 200 trials | FIDO2 hardware key ASR 0.0% vs password+TOTP 100% against AiTM proxies | one author, lab only, no malware, no recovery, not peer reviewed |
| Berladskyy2026Vectors (E3, preprint) | B | attacks implemented: infected authenticator, certificate-store manipulation | "phishing-resistant largely holds"; attacks need substantial effort | only two attacks implemented |
| Doerfler2019Challenges (E2, abstract only) | A1/A2-type "device-based challenge" | 350,000 real hijack attempts at Google (bots, phishers, targeted) | blocks over 94% of phishing hijacks, 100% of bots | not 100% for phishing; account recovery attempts included; not FIDO-specific |
| Thomas2019Hygiene (E6) | A3/B (security keys) | Google users, bulk and targeted phishing | zero security-key-only users lost to targeted phishing in the study | provider report, no method on the page; says nothing on malware or recovery |
| Cloudflare2022Phishing (E6) | A3 | real-time phishing campaign July 2022 | attackers had password and could not pass the key step | provider report, one incident, no independent check |
| NIST2025SP80063B, CISA2022PhishingResistant (E5) | A1 vs B/A3 | standard and guidance | classify out-of-band and OTP as not phishing-resistant; require a phishing-resistant option; call FIDO/WebAuthn the only widely available one | a requirement, not an attack result; says nothing on malware, recovery |

Formal verification of a whole account scheme including R7, R8, L3 was **not found**: formal results cover the protocol layer.

## 9. Case x threat summary (blank = no evidence found)

| Case | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | L1 | L2 | L3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 code (text message) | resists (Doerfler2019Challenges; device challenge, abstract) | | | fails (Kikuchi2025Evilginx) | fails (CSRB2023Lapsus) | | fails (Wang2024Simple; Campobasso2020IMPaaS) | partly (Gerlitz2023Recovery) | | | fails (Campobasso2020IMPaaS; Pazmino2025Cookie, abstract) |
| A1 code (app, TOTP) | | | | fails (Kikuchi2025Evilginx; Wasser2026Resilience lab) | | | fails (Wang2024Simple) | partly (Gerlitz2023Recovery) | | | |
| A2 push | | | | fails (Kikuchi2025Evilginx table 2) | | fails by authority classification only (CISA2022PhishingResistant; E5) | | | | | |
| A3 password + key | | | resists (Cloudflare2022Phishing E6) | resists (Cloudflare2022Phishing E6; Wasser2026Resilience lab; Berladskyy2026Vectors) | | | fails after downgrade (Miron2025Downgrade, lab) | fails (Miron2025Downgrade lab; Kunke2021Recovery) | partly (Yadav2023Local) | | fails (Yadav2023Local; Mitra2026Wooden) |
| B key with user verification | | | resists (Barbosa2021FIDO2 model; Thomas2019Hygiene E6) | resists (Barbosa2021FIDO2 model; Wasser2026Resilience lab; Thomas2019Hygiene E6) | | | fails after downgrade (Miron2025Downgrade, lab) | fails (Miron2025Downgrade lab; Kunke2021Recovery) | partly (Yadav2023Local; Lee2025WindowsHello, resists only with ESS) | | fails (Yadav2023Local; Mitra2026Wooden; Berladskyy2026Vectors, with effort) |

Notes. (a) No source isolates A3 (password plus key) from B: the FIDO2 attack papers address the key factor and apply to both
when the attacker also holds the password; the A3 row inherits them by that inference, which no source tests. The password is not tested as a
contributor in any attack. (b) R2 (stolen server credentials) and L2 (shared device, shoulder surfing) have no evidence for any case.
(c) Cells with "lab" are demonstrations (E3) and say the attack can succeed under the stated conditions, not that it has been seen in use.

## 10. Findings

### Supports (MFA not sufficient)

1. **CSRB2023Lapsus, E2.** SIM swap defeated text-message MFA in real intrusions (A1 text, R5).
   QUOTE (Executive Summary, PDF p.5): "The Board found that the multi-factor authentication (MFA) implementations used broadly in the digital ecosystem today are not sufficient for most organizations or consumers." and "attackers gained initial access to targeted organizations through Subscriber Identity Module (SIM) swapping attacks, which allowed them to intercept one-time passcodes and push notifications sent via SMS, effectively defeating this widely used MFA control".
2. **Kikuchi2025Evilginx, E3.** A relay captures the session through SMS, call, e-mail, TOTP and push 2FA; about 80% of 102 surveyed sites judged vulnerable.
   QUOTE (abstract): "revealing that 80% of major web services are vulnerable to Evilginx attacks". Caveat (section 4.1, p.154): "Therefore, we assume that these MFA methods are resilient against Evilginx." (about FIDO2/passkeys): an assumption, not a test.
3. **Wang2024Simple, E3.** QUOTE (abstract): "three zero-day vulnerabilities on three service providers that could allow an attacker to access a victim's account without possessing the victim's second authentication factor, thereby bypassing 2FA protections entirely".
4. **Campobasso2020IMPaaS, E3 (observed in use).** QUOTE (abstract): "to circumvent risk-based authentication system and effectively bypass multifactor authentication mechanisms".
5. **Cuellar2026AiTM, E1 (n=30, exploratory).** QUOTE (abstract): "In the controlled AiTM flow, these submissions also led to MFA completion and session-artifact exposure events."
6. **Gerlitz2023Recovery, E2 (R8).** QUOTE (p.235, Discussion): "Interestingly, after disclaiming that we did not have access to this, the second factor was disabled anyway." Authors did not test the attacker view.
7. **Miron2025Downgrade, E3 (A3/B).** QUOTE: "The attack sequence relies on the existence of an alternative authentication method (usually MFA), besides FIDO, for the targeted user account." and "Although technically feasible, there is currently no evidence for the usage of this technique by threat actors in the wild."
8. **Yadav2023Local, E3 (A3/B, L1/L3).** QUOTE (abstract): "we demonstrate the feasibility of seven attacks that exploit those flaws". Also: "A static and dynamic analysis of current browser extensions finds no evidence of the attacks in the wild."
9. **Mitra2026Wooden, E3 (L3).** QUOTE (abstract): "Our experiments achieved a 100% attack success rate while evading detection by Windows Defender and over 60 antivirus engines on VirusTotal."
10. **Lee2025WindowsHello, E3 (B, abstract only).** QUOTE (abstract): "Among all tested cases, only systems with Enhanced Sign-in Security (ESS) prevented our attacks."
11. **Casagrande2025CTRAPS, E3.** QUOTE (abstract): "They include zero-click attacks capable of deleting FIDO2 credentials, including passkeys, without user interaction." Narrower than authentication as the user.
12. **Kunke2021Recovery, E5.** QUOTE (abstract): "Some even rely on passwords, taking passwordless authentication ad absurdum."
13. **Mitra2026Trust, E4 (preprint).** QUOTE (abstract): "compromising the environment at any layer — the browser, the OS, or the hardware — can affect the security of FIDO2".
14. **Guan2022FormalFIDO2, E4.** QUOTE (abstract): "The verification results show FIDO2 fails to achieve some strong authentication properties."
15. **Ang2025Excavating, E4 and Wang2023Proofs, E4.** QUOTES (abstracts): "we manage to identify critical vulnerabilities in ten of the MFA protocols investigated"; "Hundreds of new schemes have been successfully proposed, and many are even equipped with a formal security proof. However, most of them have been shortly found to be insecure and cannot achieve the claimed security goals."
16. **Pazmino2025Cookie, E5, abstract only.** QUOTE (abstract): "enabling attackers to bypass multi-factor authentication and perpetrate large-scale account takeovers".
17. **CISA2022PhishingResistant, E5.** QUOTE (p.1): "not all forms of MFA are equally secure. Some forms are vulnerable to phishing, “push bombing” attacks,".

### Contradicts or narrows

1. **Barbosa2021FIDO2, E4.** QUOTE (abstract): "First, our proof confirms the authentication security of WebAuthn. Then, we show CTAP2 can only be proved secure in a weak sense".
2. **Berladskyy2026Vectors, E3 (preprint).** QUOTE (abstract): "The claim that passkeys are phishing-resistant largely holds true, significantly raising the bar compared to traditional password-based authentication." and "Our results demonstrate that successful attacks on passkeys require substantial effort and resources."
3. **Wasser2026Resilience, E3 (unreviewed, lab).** QUOTE (abstract of the English Zenodo record): "the password + TOTP scheme exhibited an Attack Success Rate of $\text{ASR} = 100.0\%$, whereas hardware-bound FIDO2 demonstrated absolute resilience ($\text{ASR} = 0.0\%$)". Single author, no peer review; read the Polish version (same numbers) in the cache; weak.
4. **Cloudflare2022Phishing, E6.** QUOTE: "While the attacker attempted to log in to our systems with the compromised username and password credentials, they could not get past the hard key requirement."
5. **Thomas2019Hygiene, E6.** QUOTE: "zero users that exclusively use security keys fell victim to targeted phishing during our investigation".
6. **Doerfler2019Challenges, E2, abstract only.** QUOTE (abstract): "Device-based challenges provide the best protection, blocking over 94% of hijacking attempts rooted in phishing and 100% of automated hijacking attempts."
7. **Bindel2023FIDO2, E4, abstract only.** QUOTE (abstract): "we show that for some threat models, the downgrade resilience of FIDO2 can be improved, and show how to achieve this with a simple modification".
8. **NIST2025SP80063B, E5.** QUOTE (PDF p.29): "Out-of-band authentication is not phishing-resistant." and (PDF p.18): "Verifiers SHALL offer at least one phishing-resistant authentication option at AAL2". **CISA2022PhishingResistant** (p.3): "The only widely available phishing-resistant authentication is FIDO/WebAuthn authentication."
9. Absent counter-evidence worth stating: **Yadav2023Local** found "no evidence of the attacks in the wild"; **Miron2025Downgrade** found "no evidence ... in the wild".

## 11. Limitations (facts about data and tools)

- Capped search: 40 records per query and provider; the number of relevant records beyond the cap is unknown. arXiv answered only 2 to 18 hits for the M-based queries.
- IEEE Xplore daily quota exhausted for S3 and C2; Semantic Scholar and DBLP not searched; WoS timed out once (rerun).
- Scopus returns the standard view without abstracts: 30 of 515 records have no abstract and were classified from the title.
- One screener (a model, `anthropic/claude-sonnet-5-5`, temperature not set by me); the default model of the machine failed. It over-assigned "adjacent" to papers whose abstracts do not state results; I read all 12 qualifies rows and all rows below 0.7 confidence by title and abstract and changed 15 (section 12), but I did not read the other 347 adjacent rows beyond titles.
- Classification was run before the dedicated K queries added 205 records; all 515 were classified in the final run.
- Seven of the 20 cited papers are preprints or unreviewed (Wang2024Simple arXiv, Yadav2023Local arXiv, Berladskyy2026Vectors, Mitra2026Trust, Wasser2026Resilience Zenodo, Kunke2021Recovery arXiv version, Ang2025Excavating arXiv version read). Several 2026 items are recent and not yet cited by others.
- Six cited papers are abstract only (section 5). The ACM and IEEE publishers refused automated fetches (bot check), which was respected.
- E6 provider reports (Cloudflare, Google, Proofpoint) disclose no method; Google blog figures are quoted from the page, the underlying study was not retrieved.
- `check_metadata.py` mismatches left in the bib are benign: compound surnames split by Crossref (Lara Cuellar, Lo Iacono, Assmuth) and arXiv or Zenodo DOIs that Crossref does not hold (checked by reading the PDFs). Cuellar2026AiTM: Scopus lists the volume as 2027, Crossref/Springer year 2026 used.
- The key is "not documented attack" (cases A3, B in real use): the query set is built around attack words in titles and abstracts; incident reports that never name MFA or FIDO would not be found, and breach analyses by companies are mostly unpublished.

### Could not be obtained
- Doerfler et al. 2019, 10.1145/3308558.3313481 (ACM 403; abstract only).
- Lee et al. 2025, 10.1109/ACSAC67867.2025.00037 (IEEE closed; abstract only). Bindel et al. 2023, 10.1109/SP46215.2023.10179454 (IEEE/figshare, not a PDF; abstract only).
- Wang and Wang 2023, 10.1109/TIFS.2022.3227753 (IEEE closed). Huang et al. 2015 (anonymous 2FA impossibility), 10.1109/TDSC.2014.2355850 (closed; classified adjacent, not cited).
- Pazmino et al. 2025, open access but not fetched (abstract only).
- English full text of Wasser 2026 (Zenodo 23955576; REST call returned HTML); Polish version 23956050 read.
- Not retrieved and therefore not cited: SquareX and Recorded Future/Google DBSC claims about cookie theft and extension hijack found only in vendor blogs; Uber 2022 press.
- Held for the user (closed access, load-bearing first): Lee2025WindowsHello, Bindel2023FIDO2, Doerfler2019Challenges.

## 12. Command, model, overrides

Table:
```
scholar sessions export mfa-sufficient -f table --bearing-only --lang en --label hits-sufficient --track "Is multi-factor authentication sufficient" --theme aitm="Phishing proxies and session theft" --theme recovery="Recovery and fallback" --theme fidoatk="Attacks on FIDO2 and passkeys" --theme analysis="Formal and analytical security analyses" -o <OUT>/mfa-sufficient-full
```
(the output shows "20 cited, 16 supporting and 7 qualifying or contradicting it, out of 508 unique hits; 342 adjacent and 123 false hits not listed").
Classification: `scholar llm classify mfa-sufficient --no-examples -n 310 -m anthropic/claude-sonnet-5-5 -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit`, then the same with `-n 400` for the 205 records added by S3 and C2. Context set with `scholar llm context mfa-sufficient "<RQ, criteria, four tag definitions>"`.
Human overrides: **15** (log in `overrides.log`): 7 qualifies-claim to adjacent (absent-2FA ransomware case, Gmail with/without MFA, authentication threat-model overview, account recovery with RBA proposal, anonymous smart-card 2FA impossibility, two qualitative comparisons without stated method); 6 supports-claim to adjacent (eIDAS ProVerif methodology, account access graphs, SMS-OTP interception detector, and three expert-opinion articles or book chapters without stated method: "The many ways to hack 2FA", "SMS Attacks", "Access Control Token Tricks"); 2 adjacent to supports-claim (the two records of Adventures in Recovery Land). Because `sessions decide` appends tags, I rewrote the tag lists of these 15 records in the session file so each has exactly one category (backup: `session-before-reclass.json` is the pre-rerun file).
Theme tags (`aitm`, `recovery`, `fidoatk`, `analysis`) were put on the cited records with `sessions decide --keep -t`.
