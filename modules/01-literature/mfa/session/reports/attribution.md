# RQ2 (attribution): one strong factor or the combination? Evidence report

Session name and slug: `mfa-attribution`. Date of all searches: 2026-11-12. Protocol: `modules/01-literature/mfa/contents.tex` (read before searching; unchanged).
Output directory: `/tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/mfa-attribution/`

## 0. Answer in brief

Against remote threats the evidence supports the prediction: protection comes from the properties of one authenticator, not from the number of factors. A random unique password already resists guessing and credential stuffing (P+); adding a code or push (A1, A2) adds protection only against credentials harvested for later use, nothing against real-time phishing, and a push adds an attack of its own. An origin-bound key resists phishing and harvesting with or without a password beside it. This rests on expert assessment (E5, NCSC, CISA, NIST), a few attack demonstrations (E3), and formal analysis (E4); no study measures one factor's contribution on real accounts, and nothing isolates P+ against A1 in the field.
Against local threats the prediction is only half right. A locally verified second factor does matter (NIST, WebAuthn and NCSC classify key-with-user-verification as multi-factor; Büttner et al. say user verification is what makes a stolen device-bound passkey hard to use), but the NCSC's own table shows that a commodity-device passkey with a weak PIN still falls to device theft, that a remembered password not stored on the device (P) survives device theft where password-manager passwords, authenticator apps and synced passkeys do not, and that a hardware key with a PIN/password is rated resistant to all eight listed attacks. Malware and malicious browser extensions defeat the key in every analysis found, and one demonstration (Yadav and Seamons) shows passwordless exposing accounts that a separate strong password would not have exposed. Strength: moderate for the remote half (consistent across independent authorities, mostly assessment and analysis), weak-to-moderate for the local half (demonstrations without frequency data; the one threat-by-threat comparison is an agency assessment without disclosed method).

## 1. Providers check (run first)

Command `scholar providers check`, exit status 1 (as expected: S2 and DBLP fail). Output at the start of the session (tail of the table, as captured):

```
  openalex         Yes          ok             API key configured; $0.995 of $1.00 daily budget left
  dblp             Yes          http error     non-JSON response (HTTP 202, text/html)
  wos              Yes          ok
  ieee             Yes          ok
  arxiv            Yes          ok
  scopus           Yes          ok             standard view (no abstracts, first author only)
s2: key rejected HTTP 403 -- check or replace S2_API_KEY
dblp: http error non-JSON response (HTTP 202, text/html)
```

Rerun after the searches (saved in `providers-check.txt`): s2 key rejected (HTTP 403), dblp http error, **ieee: quota exhausted** (daily quota used up by the enrichment step, which ran after the IEEE searches had completed; IEEE searches themselves all answered), openalex ok ($0.965 of $1.00 left), wos ok, arxiv ok. Semantic Scholar and DBLP were **not searched**. OpenAlex requests used by this strand: about 20 searches plus about 10 DOI lookups, far below the 200 allowed; no HTTP 429 on any search cell. The enrichment step (`scholar enrich`) hit WoS 429 and the IEEE daily quota; abstracts that could not be filled stay empty (see Limitations).

## 2. Search protocol

Session `mfa-attribution`, one `scholar search -n mfa-attribution -p <provider> -l 40 -f csv` call per query and provider (script `run.sh`, exact strings in `queries.log`). M and K as in the protocol. The same keywords on every provider; WoS got `TS=(...)`, Scopus `TITLE-ABS-KEY(...)`, the others the bare boolean string. No cell failed (no 429, no error); no cell is zero.

Exact strings (K = `(passwordless OR passkey OR FIDO2 OR WebAuthn OR "security key" OR "single-factor")`):

- S1 (openalex, ieee, arxiv): `K AND password AND (replace OR comparison OR "security analysis" OR evaluation)`; wos: `TS=(` same `)`; scopus: `TITLE-ABS-KEY(` same `)`.
- S2: `K AND ("user verification" OR PIN OR biometric) AND (stolen OR theft OR "local attack")` with the same wrappers.
- C1: `("multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification") AND ("defence in depth" OR "defense in depth" OR "independent factors" OR "factor independence" OR "combination of factors")` with the same wrappers.
- C2: `K AND password AND ("still needed" OR fallback OR weakness OR vulnerability)` with the same wrappers.

Query x provider x hits (limit 40 per cell; hits as recorded in the `# Results:` line of each export and in `scholar sessions show`):

| Query | OpenAlex | WoS | Scopus | IEEE Xplore | arXiv | Sum |
|---|---|---|---|---|---|---|
| S1 | 40 | 40 | 40 | 40 | 15 | 175 |
| S2 | 40 | 6 | 23 | 26 | 1 | 96 |
| C1 | 40 | 12 | 21 | 8 | 1 | 82 |
| C2 | 40 | 39 | 40 | 40 | 10 | 169 |
| Sum | 160 | 97 | 124 | 114 | 27 | 522 |

Semantic Scholar: not searched (key rejected, HTTP 403). DBLP: not searched (anti-bot page, HTTP 202 text/html). Cells at 40 are capped by the limit.

### Complements (not `scholar`), all 2026-11-12

| Tool | Verbatim query / URL | Outcome |
|---|---|---|
| WebSearch | `NIST SP 800-63B authenticator assurance level multi-factor cryptographic authenticator user verification single-factor` | vendor summaries only; led to retrieving the NIST text from nvlpubs.nist.gov (retained: `nist2025sp80063b4`) |
| WebSearch | `FIDO Alliance passkeys multi-factor user verification single-factor authentication device-bound synced passkey NIST AAL2` | FIDO Alliance and vendor coverage of the 2024 NIST supplement; supplement (SP 800-63Bsup1) retrieved, found withdrawn and superseded by 800-63B-4; not cited |
| WebSearch | `W3C WebAuthn Level 3 user verification user presence multi-factor authenticator security considerations` | led to w3.org/TR/webauthn-3 (retained: `w3c2026webauthn3`) |
| WebSearch | `ISO/IEC 29115 entity authentication assurance framework multi-factor definition authentication factors` | only store pages; **ISO/IEC 29115 not obtained** (paid text); dropped |
| WebSearch | `CISA implementing phishing-resistant MFA fact sheet FIDO WebAuthn PKI-based not vulnerable to phishing` | retained: `cisa2022phishres` |
| WebSearch | `NCSC guidance passkeys passwordless authentication single factor versus multi-factor device unlock stolen phone` | led to ncsc.gov.uk/passkeys and its technical paper (retained: `ncsc2026fido2`) |
| WebFetch | `https://pages.nist.gov/800-63-4/sp800-63b/authenticators/` | used only to locate the section numbers; quotes taken from the PDF instead |
| WebFetch | `https://pages.nist.gov/800-63-4/sp800-63b/definitions/` | HTTP 404; glossary quoted from the PDF |
| alphaXiv discover_papers | keywords passkey, WebAuthn, FIDO2, password, security analysis, user verification; question "security analysis of passkeys and FIDO2 compared with passwords plus second factor ..." | 15 hits; all relevant ones (2308.02973, 2501.07380, 2604.20826, 2609.03789, 2211.07161) were already in the session |

Known-item retrievals (not discovery): NIST SP 800-63B-4 PDF, NIST SP 800-63Bsup1 PDF, W3C WebAuthn L3 HTML, NCSC paper HTML, CISA PDF, HAL copy of Jacomme and Kremer, Springer chapters by curl through the KTH tunnel, arXiv PDFs through `fetch_pdf.py --text`; metadata checked through Crossref and DataCite.

## 3. Flow counts

- Records identified: 522 (sum of cells); after de-duplication by the tool: **298** records in the session (289 unique papers when preprint and published versions are merged, as the table caption counts them).
- Classified (model `anthropic/claude-sonnet-5-5`, `scholar llm classify --no-examples`, zero-shot): 298. Before my review: supports-claim 15, qualifies-claim 31, adjacent-subtopic 203, off-topic-false-hit 49. After my 14 overrides: **supports-claim 10, qualifies-claim 25, adjacent-subtopic 214, off-topic-false-hit 49.** Pending after classification: 0.
- Read in full text (obtained and the relevant sections read): 11: NIST SP 800-63B-4, WebAuthn L3 (§6.2.3 and surrounding), NCSC paper, CISA fact sheet, Yadav and Seamons (arXiv v1), Büttner and Gruschka (device-bound vs synced, arXiv v1), Berladskyy and Aßmuth, Mitra et al. (abstract, related work, attack sections; not every section), Jacomme and Kremer (HAL copy; the threat model, Table 5 discussion and conclusion, not every proof), Guan et al. (8 pages, abstract and introduction closely), Büttner et al. (inconsistencies; section 4.3 closely).
- Read as abstract only: 9 cited (`gautam2025secret`, `barbosa2023rogue`, `lee2025windowshello`, `mahdad2024fidola`, `mahdad2023sok`, `alqubaisi2020rush`, `wasser2026resilience`, `wang2025illusion`, `jubur2021hiena`), flagged `ABSTRACT ONLY` in `VERIFIED`.
- Cited: **20** bib entries (4 grey-literature, 16 from the session).
- Dropped: ISO/IEC 29115 (not obtainable, never cited). No cited source was dropped for failing existence checks; `scholar verify` found 0 retracted, 0 corrected, 0 superseded (65 of 298 records have no DOI and could not be checked).

## 4. Deviations from the planned queries

1. The planned queries were run verbatim and none was reworded: no query returned mostly another topic in a way that called for a rewording, although C1 (M AND defence-in-depth terms) returned mostly generic MFA-scheme papers (see 7).
2. The session was classified with `-m anthropic/claude-sonnet-5-5` and the four tags passed with `-t`, because the machine's default `llm` model (`openai-codex/gpt-5.6-sol`) is not installed and the first attempt failed with `UnknownModelError` (nothing was classified or changed by it).
3. `scholar enrich` was first run with the default provider order, stalled for over 20 minutes (Semantic Scholar rejects the key), and was stopped; it was rerun with `--enrich-providers openalex,wos,ieee,arxiv`. 262 of 298 records have an abstract afterwards (188 before); the 36 without abstract are mostly Scopus-only records, which carry no abstract.
4. After `scholar sessions decide`, which appends tags, I removed the superseded category tag from the 14 overridden papers by editing the session JSON (a backup of the session before the override is `session-backup-before-overrides.json`, and `session-after-decide-before-tagpatch.json` before the tag fix). No decision was changed by that edit.

## 5. How the standards define factor and multi-factor, and classify cases B and C

Standards' reasons are given in their own words. The case labels are the protocol's.

**Factor.** NIST SP 800-63B-4 (`nist2025sp80063b4`), glossary: "multi-factor authentication (MFA) An authentication system that requires more than one distinct type of authentication factor for successful authentication." (glossary; MFA "can be performed using a multi-factor authenticator or by combining single-factor authenticators that provide different types of factors"). §2.2.1 (AAL2): "At AAL2, authentication SHALL use either a multi-factor authenticator or a combination of two separate authentication factors." WebAuthn L3 (`w3c2026webauthn3`) §6.2.3: three classes of factor, "All WebAuthn Authenticators belong to the something you have class, but an authenticator that supports user verification can also act as one or two additional kinds of authentication factor." NCSC (`ncsc2026fido2`, section on factors): "\"factors\" do not refer to different devices, but to whether the credentials have two or more of:" something you have, something you are, something you know. This agrees with the protocol's definition; none of the standards counts two steps of the same kind as multi-factor.

**Case B (key with user verification): multi-factor, in all three.**
- NIST §3.1.7 (p. 27-28): "A multi-factor cryptographic authenticator is \"something you have\" and is activated by an activation factor that represents either \"something you know\" or \"something you are.\"" §3.1.7.1: keys "SHALL only be accessible through the presentation and verification of an activation factor".
- WebAuthn §6.2.3: "Therefore, an authenticator that supports user verification is multi-factor capable." The reason given: the PIN is something you know and a biometric is something you are; "Although user verification is performed locally on the authenticator and not by the Relying Party, the authenticator indicates if user verification was performed by setting the UV flag in the signed response returned to the Relying Party."
- NCSC: "FIDO2 credentials including passkeys are multifactor authentication where user verification is performed as part of the authentication." Reason: it rejects the objection that key and verification sit on one device ("factors" are about kinds, not devices) and notes that traditional MFA often has all its factors on the same phone too.

**Case C (key without user verification): single-factor, in all three.**
- NIST §3.1.6 (p. 26): "A single-factor cryptographic authenticator is \"something you have.\"" §3.1.7.2 (p. 28-29): "If such a flag is present and indicates that an activation factor was not used, the authentication [...] SHALL be treated as single-factor." And Appendix B.5: "Without user verification, the verifier prompts for an additional authentication factor as part of the transaction."
- WebAuthn §6.2.3: "Conversely, an authenticator that is not multi-factor capable is single-factor capable."
- NCSC: only the credential that "verifies the user prior to authenticating" is equivalent to two-factor.

**What a single-factor key is still allowed to do.** NIST §2.1: "AAL1 requires only single-factor authentication using a wide range of available authentication technologies."; §3.2.5: "Phishing resistance requires single- or multi-factor cryptographic authentication." So phishing resistance is a property of the cryptographic protocol, not of the number of factors. For AAL2 a single-factor cryptographic authenticator must be combined with "either a password or a biometric comparison" (§2.2.1) and AAL3 needs two factors plus a non-exportable key. The NIST glossary and sections 3.1.6-3.1.7 give as reason for the multi-factor class that the key "requires activation through a second authentication factor"; the reasoning for treating a missing UV flag as single-factor is that the relying party cannot know the second factor was used. CISA (`cisa2022phishres`, p. 2-3) ranks FIDO/WebAuthn and PKI as the strongest forms "based on their susceptibility to the above cyber threats" (phishing and relays), and notes "FIDO authentication can incorporate various other types of factors, such as biometrics or PIN codes": the ranking is by phishing resistance, not by factor count.

**Not obtained:** ISO/IEC 29115 (paid), so how it defines multi-factor is unknown here. NIST's supplement SP 800-63Bsup1 (April 2024) was withdrawn on 2025-08-01 and superseded by 800-63B-4; only the withdrawal notice was read.

## 6. Case x threat table (what the evidence says; empty = no evidence found)

Legend: resists / fails / partly, then the bib key and grade. "NCSC T19a/b/c" = Tables 19a, 19b, 19c of `ncsc2026fido2` (an assessment by the agency, E5; it does not disclose how each cell was derived). NCSC "credential harvest" is mapped to R3, "credential stuffing" and "password brute-force" to R1, "adversary-in-the-middle phishing" to R4, "fatigue attacks" to R6, "device malware / infostealer" to L3, "device theft with weak PIN" to L1. NCSC rows do not split B and C: its "FIDO2 credential" rows assume a user-verified credential, so they are entered under B only. Case mapping: NCSC "password only (user generated / remembered)" = P; "password only, created and managed by a credential manager" = P+; "password and software TOTP / app approval", "email OTP", "SMS OTP", "hardware OTP" = A1/A2; "FIDO2 credential / synced passkey / single device passkey" = B; "FIDO2 key + PIN/Password" = B or A3 (the table does not say which; shown separately).

| | R1 stuff/guess | R2 stored creds | R3 harvest | R4 real-time phish | R5 channel takeover | R6 approval | R7 session theft | R8 recovery/fallback | L1 theft | L2 shared/observed | L3 malware |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **P** | fails (stuffing); partly (brute force) `ncsc2026fido2` E5 | | fails `ncsc2026fido2` E5 | fails `ncsc2026fido2` E5 | | | | | resists (a remembered password is not revealed by device theft) `ncsc2026fido2` E5 | | fails `ncsc2026fido2` E5 |
| **P+** | resists `ncsc2026fido2` E5 | | fails `ncsc2026fido2` E5 | fails `ncsc2026fido2` E5 | | | fails (session cookies exfiltrated by infostealers, any case) `ncsc2026fido2` E5 | | fails `ncsc2026fido2` E5 | | fails `ncsc2026fido2` E5; partly (a password unique to the account is not exposed to an extension on other logins) `yadav2024local` E3 |
| **A1** (code) | resists `ncsc2026fido2` E5 | | resists `ncsc2026fido2` E5 | fails `ncsc2026fido2` E5; fails (ASR 100% in 200 lab trials, password+TOTP) `wasser2026resilience` E3, abstract only | | | fails (session extracted by the proxy) `wasser2026resilience` E3, abstract only | partly (3 of 9 services allow a password reset without the second factor, but login still needs it) `buttner2025inconsistencies` E2; weaknesses in deployed 1FA/2FA/reset combinations `wang2025illusion` E2, abstract only | fails for app, email and SMS codes, resists for hardware OTP (see note 1) `ncsc2026fido2` E5 | | fails (app codes), resists (email codes, hardware OTP), partly (SMS) `ncsc2026fido2` E5; second factors are not secure under concurrent session injection `mahdad2023sok` E4, abstract only |
| **A2** (push) | resists `ncsc2026fido2` E5 | | resists `ncsc2026fido2` E5 | fails `ncsc2026fido2` E5 | | fails (68% attacker success without spoofing, password assumed known) `jubur2021hiena` E1, abstract only; fails `ncsc2026fido2` E5 | | | fails `ncsc2026fido2` E5 | | fails `ncsc2026fido2` E5 |
| **A3** (password + key) | resists (password assumed compromised, key still secure in many scenarios) `jacomme2021formal` E4 | | resists `jacomme2021formal` E4 | resists (U2F resists phishing scenarios) `jacomme2021formal` E4 | | | | | | | fails (malware controlling the USB interface) `jacomme2021formal` E4; fails (overlay attack on hardware keys used in 2FA) `mahdad2024fidola` E3, abstract only |
| **B** (key + UV) | resists `ncsc2026fido2` E5 | resists by requirement (public-key cryptography protects secrets from verifier compromise) `nist2025sp80063b4` E5 | resists `ncsc2026fido2` E5 | resists `ncsc2026fido2` E5; resists (0% in 200 lab trials) `wasser2026resilience` E3, abstract only; resists, "largely holds true" `berladskyy2026attack` E3 | | resists `ncsc2026fido2` E5 | fails (all cases) `ncsc2026fido2` E5 | partly (downgrade to a weaker registered method is expected, a forecast not a measurement) `ncsc2026fido2` E5; flaws in the Client PIN mechanism `guan2022formal` E4 | fails: synced passkey and single-device passkey on a commodity device with a weak PIN `ncsc2026fido2` T19c E5; partly: generic row; hard "provided it is protected by user verification" `buttner2025devicebound` E4; platform passkey extractable unless ESS `lee2025windowshello` E3, abstract only; cloned key defeats clone detection `yadav2024local` E3 | fails (PIN extraction, rogue key) `barbosa2023rogue` E3, abstract only | partly: "situation dependent" `ncsc2026fido2` E5; fails (malicious extension, browser, OS) `yadav2024local` E3, `mitra2026trust` E3, `berladskyy2026attack` E3, `gautam2025secret` E3 (abstract only), `lee2025windowshello` E3 (abstract only) |
| **B on a hardware key with PIN/password** (NCSC row "FIDO2 key + PIN/Password") | resists `ncsc2026fido2` T19c E5 | | resists | resists | | resists | | | resists (including weak PIN) `ncsc2026fido2` T19c E5 | | resists `ncsc2026fido2` T19c E5 |
| **C** (key alone) | | resists by requirement (AAL3) `nist2025sp80063b4` E5 | | | | | | | partly: protection against a stolen device rests on user verification, so without it analysis, no source | | |

Note 1 (A1, L1): NCSC T19b: device theft with weak PIN is "Vulnerable" for app/TOTP, email OTP and SMS OTP codes and "Not vulnerable" for hardware OTP; the generic traditional-MFA row says "Commonly vulnerable". The remembered-password exception (P) is in footnote 3 of the paper.

Cells left empty have no evidence in this strand: R5 (SIM swap, email takeover) was not covered by any retrieved source; R7 only appears as the infostealer sentence; C against R1, R3, R4, R6, L2, L3 has no source separating C from B (the NCSC rows do not); L2 only for B.

## 7. The three isolating comparisons

**P+ vs A1-A3 (what a second factor adds beside a strong unique password).** The only source that has both rows is the NCSC paper (E5, assessment). Against R1 (stuffing, guessing) the second factor adds nothing: P+ is "Not vulnerable" to both (T19a), as is every traditional-MFA row (T19b). Against R3 (harvested credentials used later) it adds protection: P+ "Vulnerable", every A1 row "Not vulnerable". Against R4 (real-time phishing) it adds nothing: P+, A1 and A2 are all vulnerable; the lab trials in `wasser2026resilience` agree in direction (E3, abstract only, unrefereed) and `jacomme2021formal` gives a formal reason for the push/code variants it analyses. Against R6 a push adds an attack surface (A2: `jubur2021hiena` E1, abstract only, 68% attacker success, password assumed known). Against L1 and L3 the second factor helps only when it is not on the same phone as the password manager: app, email and SMS codes are vulnerable like P+, hardware OTP is not. Against A3: `jacomme2021formal` (E4) shows that with the password assumed lost, the key still resists phishing and spoofed fingerprints, and is beaten only by malware at the USB interface. The NCSC states that it compares against the strongest password ("passkeys are always as secure or more secure than 2SV using the strongest password", `ncsc2026fido2` and the ncsc.gov.uk/passkeys page) but this is a statement of its conclusion, not a measurement. No measurement of P+ against A1 on real accounts was found.

**A3 vs C and B (what a password adds beside a key).** Remote: nothing found that the password adds; `jacomme2021formal` (E4) and the NCSC rows suggest it adds nothing against R1, R3, R4. Local: mixed. The NCSC row "FIDO2 key + PIN/Password" is "Not vulnerable" to all eight attacks, whereas the commodity-device passkey is "Vulnerable" to device theft with a weak PIN and "Situation dependent" to malware (T19c): this is the strongest sign that a second thing the thief does not have helps, but the row does not say whether the added element is the hardware token, the PIN, or a separate password, so it cannot be attributed to A3. `yadav2024local` (E3) shows C or B at higher risk than P+ in one scenario: "passwordless authentication presents more risk than passwords alone in the presence of a compromised extension", because the attacker can log in to an account the victim never logs in to from the compromised browser.

**B vs C (what user verification adds).** Standards classify the difference but give no measured effect. Analysis: "Even for an attacker with physical access to the device, it will be difficult to steal a user's device-bound passkey, provided it is protected by user verification mechanisms" (`buttner2025devicebound`, E4). Against that: PIN extraction and rogue key registration were demonstrated on commercial authenticators (`barbosa2023rogue` E3, abstract only), flaws were found in the Client PIN protocol (`guan2022formal` E4), biometrics weakened protection on Windows (`lee2025windowshello` E3, abstract only), and the NCSC rates the commodity-device passkey vulnerable to device theft with a weak PIN. So user verification adds protection in principle, and how much depends on PIN strength, platform hardening and the verification flow.

## 8. Findings, sorted

### 8a. Supports: one strong factor does the work (remote threats)

| Key | Grade | Finding | Verbatim quote and locator |
|---|---|---|---|
| `ncsc2026fido2` | E5 | FIDO2 credentials resist every commonly observed remote attack; traditional MFA is "inherently phishable". | Abstract: "shows that at all stages of a credential's lifecycle, and against all commonly observed attacks, FIDO2 credentials including passkeys are as secure or more secure than all forms of traditional MFA for individuals." Summary: "All traditional / classical multifactor authentication including passwords, SMS codes, email codes, TOTP codes, TOTP tokens and notification approval systems are inherently phishable and attackers are increasingly abusing this property to access accounts." |
| `nist2025sp80063b4` | E5 | Phishing resistance is a property of cryptographic authentication, single- or multi-factor. | §3.2.5: "Phishing resistance requires single- or multi-factor cryptographic authentication." §2.1 (AAL1): "AAL1 requires only single-factor authentication using a wide range of available authentication technologies." |
| `cisa2022phishres` | E5 | Strongest MFA forms are ranked by phishing resistance. | p. 3: "The only widely available phishing-resistant authentication is FIDO/WebAuthn authentication." |
| `jacomme2021formal` | E4 | With the password assumed compromised, a hardware key is secure in many scenarios incl. phishing. | Sect. 1: "Compromised passwords: our basic assumption is that the user's password has been compromised." Sect. 5 (HAL p. 21): "U2F is secure under many threat scenarios, including some that combine phishing and fingerprint spoofing." |
| `berladskyy2026attack` | E3 | Attacks on passkeys exist but need substantial effort; phishing resistance largely holds. | Abstract: "The claim that passkeys are phishing-resistant largely holds true, significantly raising the bar compared to traditional password-based authentication." |
| `wasser2026resilience` | E3 (abstract only, unrefereed) | 200 lab trials: password+TOTP 100% attack success, hardware key 0%. | Abstract: "the password + TOTP scheme exhibited an Attack Success Rate of $\text{ASR} = 100.0\%$,whereas hardware-bound FIDO2 demonstrated absolute resilience ($\text{ASR} = 0.0\%$)" |
| `alqubaisi2020rush` | E4 (abstract only) | Single-factor FIDO (C) judged more secure than password (P). | Abstract: "Our analysis shows that although password-based authentication is less secure than FIDO SF authentication" |
| `jubur2021hiena` | E1 (abstract only) | With the password known, a push (A2) gives little protection: users accepted the attacker's notification. | Abstract: "Even for the non-spoofed sessions (our primary attack), the attack success rates are about 68%" |
| `mahdad2023sok` | E4 (abstract only) | States the community view that the independent second factor is what protects against terminal malware, then tests it (see 8b). | Abstract: "As password-only authentication cannot adequately protect against malware on terminals" |

### 8b. Contradicts or narrows

| Key | Grade | Finding | Verbatim quote and locator |
|---|---|---|---|
| `yadav2024local` | E3 | Local attacker with a malicious extension: passwordless exposes accounts a separate strong password would not; also key cloning defeats clone detection. | §I: "We were surprised to discover two attacks (3 and 4) where passwordless authentication presents more risk than passwords alone in the presence of a compromised extension." and "This risk did not exist in the world of passwords when a user had a different strong password on their high-value account." |
| `ncsc2026fido2` | E5 | Device theft: a commodity-device passkey is vulnerable, a remembered password is not; a hardware key with PIN/password resists all. Downgrade attacks expected. | Section Physical access: "An attacker who has stolen a device and has the passcode to the device (and that of the credential manager, if it is different) will be able to view and export passwords and other credentials depending on the credential manager." Table 19 footnote: "If a user uses a password that they remember and it is not stored in any credential managers on the device, then theft of a device even with the PIN won't reveal that password." Future state: "Users are therefore unlikely to see the full benefits of FIDO2 protected authentication until tMFA is removed as an option (either by themselves or the relying party)." Also: "Even with FIDO2 authentication, the security of the user's device and browser used to authenticate via remains important" |
| `ncsc2026fido2` (self-limit) | E5 | The NCSC warns that comparisons assume an idealised traditional MFA. | "Such arguments tend to be comparing FIDO2 and passkeys to tMFA, but an idealised version of tMFA is used as the comparison, ie, a complex, unique, remembered password and a robust second factor that the user would only ever use correctly, on a device only the user can access and would never lose or break." (this narrows what P+ plus a second factor would show, and applies to the strongest-password comparison). |
| `mitra2026trust` | E3 | Compromise of browser, OS or hardware affects FIDO2; the crypto layer is rarely the weak link. | Abstract: "These findings support the thesis that the weak link in a FIDO2 deployment is rarely the crypto layer." |
| `jacomme2021formal` | E4 | Hardware key defeated by malware at the USB interface (L3). | Sect. 5 (HAL p. 21): "However, an attack is found when the computer runs malware that [...]" (malware controlling the USB interface of the trusted computer). |
| `buttner2025devicebound` | E4 | User verification is what makes physical theft of a device-bound passkey hard; synced passkeys concentrate security in the provider. | §3.1: "Even for an attacker with physical access to the device, it will be difficult to steal a user's device-bound passkey, provided it is protected by user verification mechanisms, e.g., a PIN or fingerprint." |
| `guan2022formal` | E4 | Client PIN protocol has flaws. | Abstract: "The results also reveal that the newly introduced Client PIN mechanism has flaws" |
| `buttner2025inconsistencies` | E2 | Password reset did not bypass 2FA login in ten services; 3 of 9 allowed reset without the second factor. | Sect. 4.3 (p. 175): "Even when the password could be reset without the second factor, it would not allow bypassing 2FA during the subsequent login." |
| `barbosa2023rogue` | E3 (abstract only) | PIN extraction, impersonation, rogue key registration on commercial authenticators. | Abstract: "two of these attacks, which appear to be folklore in the community, are actually straightforward to launch in practice (user PIN extraction, impersonation and rogue key registration)" |
| `lee2025windowshello` | E3 (abstract only) | Windows platform passkeys with biometrics extractable unless ESS. | Abstract: "Among all tested cases, only systems with Enhanced Sign-in Security (ESS) prevented our attacks." |
| `mahdad2024fidola` | E3 (abstract only) | Hardware security keys in 2FA and passwordless can be tricked by overlays. | Abstract: "Two-factor authentication (2FA) systems aim to secure user accounts, provided that either the password or the second factor device remains uncompromised. However, in this research, we challenge this perception" |
| `gautam2025secret` | E3 (abstract only) | Passwords and FIDO2 are both exposed to malicious scripts and extensions. | Abstract: "malicious client-side scripts and browser extensions can steal passwords after the manager has autofilled them into the web page" |
| `mahdad2023sok` | E4 (abstract only) | The community belief that 2FA is secure against terminal malware does not hold for concurrent session injection. | Abstract: "According to the community view in the literature, 2FA-oriented methods appear to be secure in the presence of malware on the authentication terminal." |
| `wang2025illusion` | E2 (abstract only) | 50 sites: weak links in the combination of 1FA, 2FA and password reset. | Abstract: "highlighting both the overestimated strengths and overlooked weaknesses of current deployments" |

Standards definitions (`nist2025sp80063b4`, `w3c2026webauthn3`) are quoted in section 5.

Corroborating records classified supports-claim or qualifies-claim but not cited (not verified beyond title and abstract in the classification; listed in the CSV and the table): about 17, mostly reviews and surveys of passwordless methods and attacks (e.g. HiPass, Defeating FIDO2 using browser-in-the-middle, Mobile Login Bridge, SoK reviews). They repeat the attack-on-the-environment finding.

## 9. Which conclusions rest on what

- Measurement (E2): `buttner2025inconsistencies` (ten services, small), `wang2025illusion` (abstract only). No measurement isolates one factor's contribution to compromise rates on real accounts.
- Controlled experiment (E1): `jubur2021hiena` (abstract only), lab only.
- Attack demonstrations (E3): `yadav2024local`, `berladskyy2026attack`, `mitra2026trust`, `wasser2026resilience` (unrefereed), and the abstract-only items.
- Formal analysis (E4): `jacomme2021formal`, `guan2022formal`, `buttner2025devicebound` (analytical framework).
- Expert/standard consensus (E5): NIST, WebAuthn, NCSC, CISA. The NCSC threat-by-threat table is the only structure that compares all the cases, and it is an agency's assessment; its cells are not derived from stated data. The NCSC recommends passkeys in the same paper, which is a reason to read its tables as assessment, not as independent evidence.

## 10. Empty or thin piles

- C1 ("defence in depth" and similar terms with M): 82 raw hits, of which almost all concerned multi-factor scheme proposals (biometrics, IoT, cloud); only `mahdad2023sok` was retained. No paper was found that measures factor independence or defence in depth in deployed authentication. This is a thin pile, not an empty one, and the vocabulary "factor independence" never appeared in any title of a bearing record.
- Direct measurement of what a password contributes beside a key (A3 vs B/C): nothing found. All evidence is analytical or from agency assessment.
- R5 (SIM swap, email takeover of the second factor): not covered in this strand; the protocol's RQ3 queries cover it.
- C vs B per threat: no source separates them beyond the definitions.

## 11. Limitations (facts about the data and tools)

- Capped at 40 records per query and provider; OpenAlex, IEEE and Scopus hit the cap on three of four queries, so the search samples the most relevant records and does not exhaust the literature.
- Semantic Scholar and DBLP were not searched; IEEE ran out of quota after the searches (during enrichment), so 36 records lack abstracts, mostly Scopus-only (Scopus returns no abstracts, first author only: the Scopus author field in the session is the first author only, so authors in the bib come from Crossref).
- One screener (a language model, zero-shot, confidence often 0.35-0.55 on borderline items) with my checks: 52 rows had confidence below 0.7; I read every qualifies-claim row and every supports-claim row and the title of every adjacent row, and read abstracts of about 70 rows. I did not read the abstract of every low-confidence adjacent row. Papers without an abstract (e.g. a 2026 simulation of social media account compromise across user-chosen schemes, a 2026 Trojan-based passkey compromise paper, a 2025 Evilginx study) are classified from the title only and none is cited.
- Closed-access texts that could not be read in full text: see section 12. A bot check (Cloudflare "Just a moment") stopped retrieval from dl.acm.org; I did not work around it.
- The two version records of the same paper (preprint and venue) are separate rows in the CSV; the table merges them.
- `yadav2024local` was read from the arXiv v1 preprint; the NDSS version differs (the abstract adds cross-site scripting).
- The grades say what a source can show, not its quality. The NCSC paper is dated 2026-04-23 and the NIST text July 2025; both postdate many of the attack papers, so fixes may have landed.

## 12. What could not be obtained

| Title | DOI | Why |
|---|---|---|
| Evaluating the Security Posture of Real-World FIDO2 Deployments (Kuchhal, Saad, Oest, Li; CCS 2023) | 10.1145/3576915.3623063 | ACM bot check (Cloudflare, HTTP 403); abstract in the session is truncated; not cited |
| Rogue key and impersonation attacks on FIDO2 | 10.1145/3600160.3600174 | same; cited abstract-only |
| SoK: A Comprehensive Evaluation of 2FA-based Schemes ... | 10.1145/3558482.3590183 | same; cited abstract-only |
| Bypassing Push-based Second Factor and Passwordless Authentication ... | 10.1145/3433210.3453084 | no open-access copy; ACM bot check; cited abstract-only |
| Breaching Security Keys without Root (FIDOLA) | 10.1145/3658644.3690286 | same |
| False Promises of Passwordless: Defeating Windows Hello through TPM Misuses | 10.1109/ACSAC67867.2025.00037 | no open-access copy found; IEEE not tried through the tunnel |
| The 2FA Illusion: Uncovering Weak Links of Web Account Access in the Wild | 10.1109/ACSAC67867.2025.00060 | same |
| Should We Rush to Implement Password-less Single Factor FIDO2 based Authentication? | 10.1109/URC49805.2020.9099190 | same |
| Privacy and Security of FIDO2 Revisited; Passkey in the Wooden Horse; Session Replication Attack Through QR Code Sniffing in Passkey CTAP Registration | 10.56553/popets-2025-0100; 10.1007/s11235-026-01496-y; 10.1007/978-3-031-65175-5_21 | not attempted (peripheral, or no abstract); not cited |
| Resilience of the FIDO2/WebAuthn Protocol ... (Zenodo) | 10.5281/zenodo.23955576 | PDF not retrieved by `fetch_pdf.py` (no open-access PDF found); abstract only |
| ISO/IEC 29115:2013 | none | paid standard; not obtained |

## 13. Table, classification and overrides

- Table command: `scholar sessions export mfa-attribution -f table --bearing-only --lang en --label hits-attribution --track "What each factor contributes" --theme local-malware="Local attacks and malware" --theme key-resists-remote="A key resists remote attacks" --theme fallback-recovery="Fallback and recovery" --theme synced-passkeys="Synced passkeys" --theme second-factor-weakness="Weak second factors" --theme formal-analysis="Formal analysis" -o <OUT>/mfa-attribution-full` -> `mfa-attribution-full.tex` (caption: 16 cited, 7 supporting, 10 qualifying out of 289 unique hits; 208 adjacent and 48 false hits not listed). CSV: `scholar sessions export mfa-attribution -f csv -o <OUT>/mfa-attribution` -> `mfa-attribution.csv`.
- Classification: `scholar llm context mfa-attribution "<question; criteria; four tags>"`, then `scholar llm classify mfa-attribution -m anthropic/claude-sonnet-5-5 --no-examples -n 300 -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit --no-enrich` (2 min 38 s). Model: `anthropic/claude-sonnet-5-5`.
- **Human overrides: 14.** Twelve moved from supports/qualifies to adjacent-subtopic (Privacy and Security of FIDO2 Revisited; Comparative Analysis of User Authentication Technologies for On-Premises Cloud Systems, two records; Choosing the right MFA method for online systems; two general papers on 2FA effectiveness (an Instagram survey study and a paper on the human factor); Hack for Hire; From Passwords to Passkeys (design and implementation); Revisiting Authentication Security; Can "Something You Know" be saved?; Unveiling the Covert Vulnerabilities in MFA Protocols; Beyond Passwords: The Essence and Impact of MFA). Two moved to kept as qualifies-claim (Passwords and FIDO2 Are Meant To Be Secret, from adjacent; The 2FA Illusion, from supports). In addition I re-confirmed the 18 records carrying theme tags (cited papers) with `sessions decide --keep`, which the tool shows as "human"/"confirmed" and is not a change of category.
- Papers left pending by the classifier: none.
- Theme tags on cited records: local-malware, key-resists-remote, fallback-recovery, synced-passkeys, second-factor-weakness, formal-analysis.

## 14. Files

- `mfa-attribution.bib` (20 entries; `check_provenance.py`: all entries carry complete provenance; `check_metadata.py`: 17 DOI entries, 4 flagged, all benign: arXiv and Zenodo DOIs are not in Crossref (confirmed against DataCite: titles and authors match) and the diacritic in Aßmuth; 3 entries have no DOI and are grey literature)
- `mfa-attribution.csv`, `mfa-attribution-full.tex`, `mfa-attribution-report.md` (this file)
- Working files: `queries.log`, `run.sh`, `out-*.csv` (per-cell search exports), `providers-check.txt`, `classify.log`, `enrich.log`, session backups.
