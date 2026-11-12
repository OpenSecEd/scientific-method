# RQ4 (necessity): Is multi-factor authentication necessary?

Session and slug: `mfa-necessary`. Date of searches: 2026-11-12. Protocol: `/home/dbosk/devel/edu/scientific-method/modules/01-literature/mfa/contents.tex` (unchanged by me; I edited nothing in the repository).
Research question: "Is multi-factor authentication necessary: can comparable security be reached with a single factor, or by other means?" Protocol prediction H_necessary: not necessary against the remote threats, because a single cryptographic key (case C) resists them as well as the multi-factor cases.

## 0. Answer in brief

* The prediction is **partly supported, with a definitional catch and with narrowing evidence**. Against the remote phishing-type threats (R3, R4) and credential stuffing/guessing (R1) and a leaked server database (R2), the evidence says that what does the work is a **phishing-resistant cryptographic key**, not the number of factors: NIST treats phishing resistance as a property of single- or multi-factor cryptographic authentication, and the NCSC's tabulated assessment finds FIDO2 credentials at least as secure as password-plus-second-factor against all common attacks. Password plus an ordinary second factor (code, push) does **not** resist R4/R3-relay (NCSC paper, CISA, OMB), so the number of factors alone is not what buys security.
* But **no source in the hit list evaluates case C (a key with no user verification) head to head against a multi-factor case**. The NCSC, the strongest source for the comparison, analyses FIDO2 credentials *with* user verification and itself classifies them as **multi-factor**. So the strongest "alternative" is, in the protocol's terms, case B, and does not show that a single factor suffices. Evidence on case C against the local threats (L1 lost/stolen device) is absent from what I could read; the standards require two factors at AAL2 and AAL3 (NIST), which is expert consensus (E5), not proof.
* **Risk-based authentication (RBA)** is the one alternative studied with measurement (E2): it blocks most naive and targeted attackers who only hold the stolen password (Wiefling2022), but is bypassed by phishing kits and a criminal market that replay victim profiles (Campobasso2020, Lin2022), is rarely triggered at big providers (Makowski2023), and NIST does not count risk signals as a factor. It is also not a replacement: its step-up is a second factor (Wiefling2019).
* **Random unique passwords from a manager (case P+)** resist guessing and stuffing (R1) but fail against phishing, relay, and malware (NCSC paper Table 19a). The NCSC's own advice is to use them *together with* 2SV where passkeys are unavailable. No measured head-to-head comparison of P+ against MFA was found (two WebSearch queries returned only vendor blogs).
* Strength: moderate for "what protects against remote phishing is a bound cryptographic key", weak for "a single factor is enough". Mostly E3, E4 and E5 evidence; only one E2 source per alternative; no E1. Details and the full tables follow.

## 1. Providers and health

`scholar providers check` at start (2026-11-12 ~10:20), relevant lines:

```
openalex  ok   API key configured; $0.995 of $1.00 daily budget left
wos       ok
scopus    ok   standard view (no abstracts, first author only)
ieee      ok   (later in the session: quota exhausted, 200/200 per day, shared with the other agents)
arxiv     ok
dblp      http error  non-JSON response (HTTP 202, text/html)   [not searched]
s2        key rejected HTTP 403 -- check or replace S2_API_KEY  [not searched]
```
Semantic Scholar and DBLP were not searched (instructed). At the end of the session `scholar providers check` shows `ieee: quota exhausted` (resets 01:00); this is why the two supplementary queries S1b and C3 have no IEEE result (below). OpenAlex: no HTTP 429 seen; `scholar providers limits` shows 1914 requests used today (all agents together; my own count is not separable, my searches were 30 cells of at most 40 records plus scholar's enrichment lookups, well under the 200 allowed).

## 2. Queries and the query x provider x hits matrix

Blocks (as in the protocol):
* M = `"multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification"`
* K = `passwordless OR passkey OR FIDO2 OR WebAuthn OR "security key" OR "single-factor"`

Exact strings sent. OpenAlex, IEEE Xplore and arXiv received the string as is; Web of Science received `TS=(<string>)`; Scopus received `TITLE-ABS-KEY(<string>)`. The same keywords everywhere.

* **S1** `(passwordless OR passkey OR FIDO2 OR WebAuthn OR "security key" OR "single-factor" OR "risk-based authentication" OR "password manager") AND (alternative OR "instead of" OR without) AND ("multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification")`
* **S2** `"risk-based authentication" AND (evaluation OR effectiveness OR security)`
* **C1** `("multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification") AND (necessary OR mandatory OR mandate OR required) AND (security OR compromise)`
* **C2** `("password-only" OR "single-factor authentication") AND (insufficient OR inadequate OR compromise)`
* **S1b** (supplementary, see Deviations) `(passwordless OR passkey OR FIDO2 OR WebAuthn OR "security key" OR "single-factor") AND (phishing OR "account takeover" OR "credential stuffing") AND (evaluation OR measurement OR "security analysis" OR "formal analysis")`
* **C3** (supplementary, see Deviations) `("multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification") AND ("assurance level" OR "phishing-resistant" OR "NIST SP 800-63B" OR "strong customer authentication")`

All with `--limit 40` (`scholar search "<string>" -n mfa-necessary -p <provider> -l 40`). The scripts are `q.sh` and `q2.sh` in the output directory.

Records returned per cell (copied from `scholar sessions show mfa-necessary` and the CSV `# Results:` lines; FAILED = no answer, not zero):

| Query | openalex | wos | scopus | ieee | arxiv |
|---|---|---|---|---|---|
| S1 | 40 | 30 | 28 | 27 | 2 |
| S2 | 40 | 40 | 40 | 40 | 12 |
| C1 | 40 | 40 | 40 | 40 | 40 |
| C2 | 40 | 27 | 36 | 14 | 1 |
| S1b | 40 | 12 | 20 | FAILED | 8 |
| C3 | 40 | 13 | 21 | FAILED | 1 |

Notes on the matrix: (a) the S2 x WoS cell failed on the first run (`wos ... Read timed out`, session recorded `failed (rate limited or HTTP/parse error)`); I re-ran the identical query after 20 s and it returned 40; the table shows the successful re-run. (b) S1b x IEEE and C3 x IEEE: `WARNING: ieee: daily quota exhausted (IEEE); resets 01:00. Skipping.` They are **failed, not searched**; no negative may rest on them. (c) arXiv returns very few records for long boolean strings (C2: 1, C3: 1, S1: 2), so its recall for these queries is low. (d) Cells at 40 hit the cap; the results are a sample of the most relevant records, not an exhaustive set.

## 3. Complements outside `scholar` (WebSearch / WebFetch / curl), all 2026-11-12

alphaXiv was not used.

| # | Tool | Verbatim query or URL | Outcome |
|---|---|---|---|
| 1 | WebSearch (standard) | `phishing-resistant multi-factor authentication government guidance requirement fact sheet` | CISA fact sheet and references to OMB; retained CISA2022 (retrieved from cisa.gov) and led to OMB M-22-09; vendor blogs dropped |
| 2 | WebSearch (standard) | `strong customer authentication regulatory technical standard two or more elements knowledge possession inherence PSD2` | Law-firm and FIDO Alliance commentary on Delegated Regulation 2018/389; primary text not obtained (see 8); nothing cited |
| 3 | WebSearch (standard) | `zero trust federal strategy phishing-resistant multi-factor authentication agencies memorandum` | Found whitehouse.gov M-22-09 PDF; retained OMB2022 |
| 4 | WebFetch | `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R0389` | empty page; then `curl` of the HTML URL returned HTTP 202 with an empty body (bot challenge); **stopped, not worked around** |
| 5 | WebSearch (standard) | `NCSC guidance multi-factor authentication for online services recommendation passkeys single factor` | NCSC blog, paper, passkeys page, authentication-methods guidance; retained NCSC2026paper, NCSC2026blog, NCSC2026page, NCSC2026methods; trade-press summaries dropped |
| 6 | WebFetch | `https://www.ncsc.gov.uk/information/passkeys-what-you-need-to-know` | summary by the fetch model only; I re-read the page text with `curl` and verified every quoted sentence verbatim |
| 7 | curl | `https://www.ncsc.gov.uk/blogs/passkeys-are-more-secure-than-traditional-ways-to-log-in` and `https://www.ncsc.gov.uk/paper/traditional-user-and-fido2-credentials-personal-use` (HTML to text) | read; quoted verbatim |
| 8 | WebSearch (standard) | `account takeover rate security key passkey versus password with SMS or app second factor measured phishing study` | only vendor blogs with unsourced numbers; **no measured head-to-head study found**; nothing cited |
| 9 | WebSearch (standard) | `random unique password from password manager versus two-factor authentication account compromise risk comparison` | only SEO/blog guides saying the two are complementary; nothing cited |
| 10 | fetch_pdf.py (scholar cache) | CISA fact sheet PDF; whitehouse.gov M-22-09 PDF; NCSC `Authentication-methods-choosing-the-right-type.pdf`; NIST SP 800-63B-4 via DOI | read in full |

## 4. Flow counts

* Records identified: 772 (sum of the records returned by the 28 answered cells of the 6 queries x 5 providers = 30 cells; 2 cells failed).
* In the session after de-duplication by `scholar`: 523 papers. (The audit-table export counts 497 unique hits because it merges more variants of the same work.)
* Classified (anthropic/claude-sonnet-5-5, `--no-examples`, zero pending afterwards): model output supports-claim 14, qualifies-claim 43, adjacent-subtopic 420, off-topic-false-hit 46. After 9 human overrides: supports-claim 12, qualifies-claim 36, adjacent-subtopic 429, off-topic-false-hit 46.
* Read in full text: 16 (NIST SP 800-63B-4, Wiefling2022, Wiefling2019, Makowski2023, Campobasso2020, Buettner2024, Berladskyy2026, Buettner2025, Kunke2021, Jacomme2021 via scholar's PDF cache from OA copies; CISA2022, OMB2022, NCSC2026methods as PDFs; NCSC2026paper, NCSC2026blog, NCSC2026page as HTML pages). Full text for Wiefling2022, Makowski2023, Campobasso2020, Wiefling2019, Buettner2024, Buettner2025 and Jacomme2021 is the open-access author copy (arXiv or HAL) of the published version.
* Read as abstract only: 9 (Lin2022, Spooren2015, Catalano2025, Mahdad2024, Lee2025, Kamar2026, Holthouse2025, NISTcswp4, Cocheo2006).
* Cited (verified bib entries): 25.
* Retraction check: `scholar verify mfa-necessary`: 1 retracted, 1 superseded, 0 corrected, 396 ok, 125 unknown (no DOI or no Crossref status). Neither the retracted nor the superseded paper is among the cited sources.

## 5. Deviations from the planned queries

1. **WoS S2 failed once** (timeout) and was re-run unchanged (see matrix note a).
2. **Supplementary query S1b added** (kept alongside the planned ones). Reason: S1 requires M in every record, so it only finds work on keys and passkeys that also uses "two-factor/multi-factor" wording; it returned few records that bear on a key-based scheme on its own (27 to 40 per provider but mostly scheme proposals, arXiv: 2). S1b drops M and adds the threat vocabulary (phishing, account takeover, credential stuffing) and the evidence vocabulary (evaluation, measurement, security analysis, formal analysis), keeping K. It recovered Kunke2021 (single-factor FIDO2 recovery), Berladskyy2026, Buettner2025, Jacomme2021 and Lee2025.
3. **Supplementary query C3 added.** Reason: C1 and C2 returned mostly usability and scheme papers; C3 uses the field's own words for requirements (assurance level, phishing-resistant, NIST SP 800-63B, strong customer authentication) with M. It surfaced NIST SP 800-63B-4 itself and the NIST PIV white paper (via C2). S1b and C3 could not be run on IEEE (quota).
4. **Classification model**: the default model configured for `llm` (`openai-codex/gpt-5.6-sol`) is unknown inside scholar's own Python environment (`UnknownModelError`), so I passed `-m anthropic/claude-sonnet-5-5`.
5. **Full texts**: ACM and Springer answered 403/HTML for Pump Up (ACM TOPS), Makowski2023, Campobasso2020; I used the arXiv/HAL author copies listed by Unpaywall, i.e. the same works; no bot check was circumvented.
6. The two-column PDFs were read with `pdftotext` (raw order) for quoting; every quote in the bib was checked by script against the extracted text (normalising hyphenation and whitespace): 0 failures.

## 6. Alternatives table

Single-factor means one of the three factor kinds in the protocol's sense. "Key + UV" means the key unlocked by PIN or biometric, which the NCSC and NIST count as multi-factor (case B).

| Source | Year | Alternative | Single-factor in the protocol's sense? | Threats evaluated | Result vs which multi-factor case | Grade |
|---|---|---|---|---|---|---|
| Temoshok2025 (NIST SP 800-63B-4) | 2025 | key alone (case C), "single-factor cryptographic authentication" | yes (something you have) | R2 (public-key crypto protects against verifier compromise, AAL3 text), R3/R4 (phishing resistance requires single- or multi-factor cryptographic authentication) | defined as permitted at AAL1; not accepted alone at AAL2/AAL3; no comparison measured | E5 |
| Temoshok2025 | 2025 | risk indicators | not a factor ("do not substitute for an authentication factor") | R1 | cannot replace a factor at any AAL | E5 |
| NCSC2026paper / NCSC2026blog | 2026 | FIDO2 credential, passkey (synced or single device); "FIDO2 key + PIN/Password" | no: NCSC counts FIDO2 with user verification as multi-factor (case B); key without UV is not separately analysed | credential harvest (R3), brute force and stuffing (R1), infostealer (L3), AitM (R4), fatigue (R6), phishing the sync fabric (R8-like), device theft with weak PIN (L1) | as secure or more secure than traditional MFA (cases A1, A2) against all common attacks, E5 expert assessment, not a measurement | E5 |
| NCSC2026paper | 2026 | random unique password from a credential manager (case P+) | yes | same list | resists brute force and stuffing; vulnerable to credential harvest, infostealer, AitM, sync fabric, device theft (Table 19a); no direct comparison with a multi-factor row, but the password+code rows resist stuffing as well and are likewise phishable | E5 |
| NCSC2026page | 2026 | password manager | yes | not evaluated | advises manager-generated password plus 2SV where no passkey | E5 |
| Berladskyy2026 | 2026 | passkey (FIDO2), with the UV of passkeys | case B/C ambiguous | R3, R4 (attacker-controlled site, CA-store spoofing), L3 (infected authenticator) | phishing resistance "largely holds", attacks need substantial effort; compared with password-based, not with MFA | E3 |
| Buettner2025 | 2025 | device-bound vs synced passkeys vs passwords (Bonneau framework) | not stated | R1, R3, provider compromise | synced passkeys: security concentrated in the provider | E4 |
| Kunke2021 | 2021 | single-factor passwordless FIDO2 (case C), recovery | yes (stated) | R8 | recovery methods have many drawbacks, some use passwords; no MFA comparison | E4 |
| Jacomme2021 | 2021 | U2F key as second factor (case A3) | no (two factors) | R3, R4, L1-ish (fingerprint spoof), L3 (malware on USB/TLS interface) | resists phishing; malware on the computer still lets an attacker abuse the token; better than Google 2-step variants | E4 |
| Catalano2025 | 2025 | FIDO2 hardware key (+ password flows) | not stated | R4 (browser-in-the-middle) plus XSS | defeated in the demonstrated setting | E3 |
| Mahdad2024 | 2024 | FIDO2 security keys with limited display | key used in 2FA and passwordless | R6-like (user deceived into approving) | 95.55% of users approved cross-service attacks in a user study | E3 |
| Lee2025 | 2025 | Windows Hello / platform passkeys | UV-based, multi-factor in NIST terms | L1, L3 | attacks work unless Enhanced Sign-in Security | E3 |
| Wiefling2022 | 2022 | risk-based authentication (password + context signals, step-up) | one factor plus context (NIST: context is not a factor) | R1 (stuffing/guessing), naive, VPN, targeted and very targeted attackers replayed on 31.3 M real logins | blocks most such attackers with few re-authentications; compared with 2FA only via cited user perception, not security | E2 |
| Wiefling2019 | 2019 | RBA at 8 services | as above | R1 | step-up is a verification code | E2/E3 |
| Makowski2023 | 2023 | RBA at Google, Amazon, Facebook | as above | R1 | step-up rarely triggered in test cases | E3 |
| Campobasso2020 | 2020 | RBA | as above | R3/R4 with profile replay, L3 (profiles from botnets) | bypassed (and thus MFA bypassed) by a criminal service | E3 |
| Lin2022 | 2022 | RBA with browser fingerprint (abstract only) | as above | R3/R4 | phishing kits replicate fingerprints, bypassing 2FA | E3 |
| Spooren2015 | 2015 | RBA, mobile fingerprint (abstract only) | as above | signal quality | fingerprints similar across devices, less reliable | E4 |
| Buettner2024 | 2024 | RBA in recovery flows | as above | R8 | recovery is an entry point; implementations differ widely | E3 |
| Holthouse2025 | 2025 | password only (case P), 23andMe incident (abstract only) | yes | R1 | about 14,000 accounts compromised by credential stuffing; MFA absent | E3 |

## 7. Requirements table (E5: expert consensus, not proof of necessity)

| Standard or regulation | Level or scope | What is required | Reason given | Quote and locator |
|---|---|---|---|---|
| NIST SP 800-63B-4 (Temoshok2025) | AAL1, all RPs | single- or multi-factor; verifiers SHOULD offer MFA | basic confidence | "AAL1 requires either single-factor or multi-factor authentication using a wide range of available authentication technologies." (Sec. 2.1, p. 4) |
| same | AAL2; federal agencies SHALL select at least AAL2 when personal information is online | two distinct factors; replay-resistant authenticator; a phishing-resistant option offered | higher AAL "requires malicious actors to have better capabilities and to expend greater resources" | "Proof of possession and control of two distinct authentication factors through the use of secure authentication protocols is required." (Sec. 2.2, p. 6); "Stronger authentication (i.e., a higher AAL) requires malicious actors to have better capabilities and to expend greater resources to successfully subvert the authentication process." (Sec. 1, p. 1) |
| same | AAL3 | non-exportable key, phishing-resistant; single-factor key plus password or biometric, or multi-factor key; syncable passkeys not allowed | very high confidence | "Single-factor cryptographic authentication (Sec. 3.1.6) used in conjunction with either a password (Sec. 3.1.1) or a biometric comparison" (Sec. 2.3.1, p. 8) |
| same | all levels | fraud indicators (risk signals) may be used but do not replace a factor | | "The use of potential fraud indicators ... does not impact or change the AAL of a transaction or substitute for an authentication factor." (Sec. 2, p. 4; ellipsis mine; full sentence in the bib) |
| OMB M-22-09 (OMB2022) | US federal agencies | phishing-resistant MFA for staff, contractors, partners; offered as an option to public users; stop SMS/voice/OTP/push for them | enterprise users are valuable phishing targets | "For agency staff, contractors, and partners, phishing-resistant MFA is required." (p. 5); "This requirement for phishing-resistant methods is necessitated by the reality that enterprise users are among the most valuable targets for phishing." (p. 7) |
| CISA fact sheet (CISA2022) | recommendation to all organisations | MFA for all users and services; migrate to phishing-resistant MFA | other MFA forms are phishable, push-bombable, SIM-swappable | "While any form of MFA is better than no MFA ... phishing-resistant MFA is the gold standard" (p. 1; full sentence in the bib) |
| NCSC (NCSC2026blog, NCSC2026paper, NCSC2026page, NCSC2026methods) | UK, individuals and online services | recommend passkeys where supported, 2SV where not; do not demand a second factor at every login, only for high-impact actions and suspicious activity | traditional MFA "inherently phishable"; FIDO2 with UV is itself multi-factor | "At CYBERUK 2026 in Glasgow, the NCSC announced that we will begin recommending passkeys wherever a service supports them, and two-step verification (2SV) where it does not." (blog); "You should not mandate use of a second factor every time an MFA-protected service is used" (methods guidance, MFA section) |
| NIST CSWP 4 (NISTcswp4), abstract only | US federal privileged users | multifactor PIV-based authentication instead of password-based single-factor | OMB CSIP 2015 requirement | "...the need for multifactor PIV-based user authentication to take the place of password-based single-factor authentication for privileged users." (abstract) |
| FFIEC 2005 guidance, via Cocheo2006 (abstract only; guidance itself not read) | US banks, high-risk online transactions | single-factor "inadequate"; MFA or other approaches; title: MFA "an option not a requirement" | | "Single-factor authentication requires only asking that customers provide one form of identification to access services, which the agencies consider inadequate for high-risk transactions conducted under modern conditions." (abstract) |
| PSD2 RTS (EU 2018/389), strong customer authentication | EU payments | two or more of knowledge, possession, inherence | | **not retrieved** (see section 11); WebSearch snippets are not citable |

Note the two-sided reading: the requirement texts show that the authorities require more than one factor at their upper levels (NIST AAL2/3, OMB, PIV, FFIEC for high-risk), which is evidence of consensus on a need; but the same authorities (NIST AAL1, NCSC, FFIEC "other approaches") accept single-factor or risk-based approaches at lower assurance, and the strongest recent statements (OMB, CISA, NCSC) put the weight on phishing resistance, not on the number of factors.

## 8. Case x threat summary (P, P+, C, and RBA as an extra row)

Entries are resists / fails / partly with the bib key; empty cells have no evidence in what I read. R5 (second-factor channel) and R7 (session theft) do not apply to single-factor cases and no source evaluated them for these rows.

| Case | R1 guess/stuff | R2 stored credentials | R3 phish (store) | R4 relay (AitM) | R6 approval | R8 recovery/fallback | L1 stolen device | L3 malware |
|---|---|---|---|---|---|---|---|---|
| P password chosen by user | fails (NCSC2026paper Table 19a "always vulnerable" to stuffing; Holthouse2025) | | fails (NCSC2026paper) | fails (NCSC2026paper) | | | | fails (NCSC2026paper) |
| P+ random unique password (manager) | resists (NCSC2026paper: brute force and stuffing "not vulnerable") | | fails (NCSC2026paper) | fails (NCSC2026paper) | | | fails (NCSC2026paper, weak-PIN theft) | fails (NCSC2026paper) |
| C key alone (case C; evidence is mostly for FIDO2 with UV = case B) | resists (NCSC2026paper; Buettner2025) | resists (Temoshok2025, public-key requirement at AAL3) | resists (Temoshok2025 Sec. 3.2.5; NCSC2026paper; Berladskyy2026) | resists, partly: Berladskyy2026, NCSC2026paper "never vulnerable"; fails in demonstrated edge cases (Catalano2025 BitM+XSS) | partly (Mahdad2024: 95.55% approved a deceptive overlay) | partly/fails (Kunke2021: recovery drawbacks, some use passwords; NCSC2026paper: sync fabric situation dependent) | no evidence for a key without UV; for key + UV: "potentially vulnerable" or "vulnerable" for weak PINs (NCSC2026paper); Lee2025 | partly (Jacomme2021: malware on the computer abuses the token; NCSC2026paper "situation dependent"; Lee2025) |
| RBA (password plus context, step-up) | resists mostly (Wiefling2022: blocks most naive and targeted attackers; but Makowski2023: rarely triggered) | | fails (Lin2022, abstract) | fails (Campobasso2020; Lin2022) | | partly (Buettner2024) | | fails (Campobasso2020: profiles from infected hosts) |

## 9. Findings

### 9a. Supports "not necessary" (comparable security without several factors)

1. **A phishing-resistant cryptographic key is what resists remote phishing, whether or not it is combined with a second factor.** Temoshok2025, E5: "Phishing resistance requires single- or multi-factor cryptographic authentication." (Sec. 3.2.5, p. 35). Corroborated by NCSC2026blog, E5: "FIDO2 credentials, including passkeys, are as secure or more secure than traditional MFA against all common credential attacks observed in the wild." and by NCSC2026paper: "All traditional / classical multifactor authentication including passwords, SMS codes, email codes, TOTP codes, TOTP tokens and notification approval systems are inherently phishable" (Summary and recommendations). Berladskyy2026, E3: "The claim that passkeys are phishing-resistant largely holds true, significantly raising the bar compared to traditional password-based authentication." (Abstract).
2. **Standards allow a single-factor key at the lowest level and regulators have accepted non-MFA approaches.** Temoshok2025, E5: "AAL1 requires either single-factor or multi-factor authentication using a wide range of available authentication technologies." (Sec. 2.1, p. 4). Cocheo2006, E5 (abstract only), title: "Regulators Say Multi-Factor Authentication Is an Option Not a Requirement".
3. **RBA reaches high security against password-only attackers without asking everyone for a second factor.** Wiefling2022, E2: "Therefore, we consider RBA an effective measure to protect users from the majority of attacks involving stolen passwords." (Sec. 15, p. 6:28); same source: "scalable interim solution to strengthen password-based authentication, until more secure authentication methods are in place." Corroboration, Wiefling2019 (E2/E3): RBA deployed at large services; the NCSC itself recommends rationing the second factor ("You should not mandate use of a second factor every time an MFA-protected service is used", NCSC2026methods).
4. **A random unique password (P+) removes credential stuffing and guessing**, NCSC2026paper Table 19a ("Password only - created and managed by a credential manager": brute-force and stuffing "Not vulnerable"). This is the NCSC's assessment (E5), not a measurement.

### 9b. Contradicts or narrows

1. **The best alternative is itself multi-factor in the standards' sense.** NCSC2026blog: "When user verification is required as part of the login, FIDO2 authentication constitutes multi-factor authentication"; NCSC2026paper: "FIDO2 credentials including passkeys are multifactor authentication where user verification is performed as part of the authentication." and, against the objection that the factors share a device: "Occasionally arguments are made that as the passkey private key and the user verification (via biometrics or PIN) are on the same device, it cannot be two factor". So the NCSC evidence is for case B, not case C. Kunke2021 is the only source stating it studies case C ("passwordless FIDO2 single-factor authentication systems only", Limitations) and it reports recovery weaknesses, not a head-to-head comparison.
2. **Standards require two factors at higher assurance, for local-attack reasons not tested in the literature found.** Temoshok2025, E5: "Proof of possession and control of two distinct authentication factors through the use of secure authentication protocols is required." (Sec. 2.2, p. 6); AAL3 requires a key plus a password or biometric or a multi-factor key (Sec. 2.3.1, p. 8). OMB2022: "For agency staff, contractors, and partners, phishing-resistant MFA is required." (p. 5). These are requirements (E5), not evidence that fewer factors fail, and the reason they give is phishing/attacker cost, not factor count.
3. **Key-based schemes fall to attacks outside the cryptographic binding.** Catalano2025 (E3, abstract): "the novel BitM + attack that proves to be capable of defeating any available MFA method"; Mahdad2024 (E3, abstract): "users approved approximately 95.55% of cross-service attacks when presented with a screen overlay"; Lee2025 (E3, abstract): "Among all tested cases, only systems with Enhanced Sign-in Security (ESS) prevented our attacks."; Jacomme2021 (E4): "While the claim indeed holds for the first threats, malware attacks are still possible." (Sec. 5.5); Buettner2025 (E4): "The security of synced passkeys is mainly concentrated in the passkey providers as a trusted third-party service." (Sec. 5.1). These attacks also apply to the multi-factor key cases, so they narrow "resists as well as" to "resists the cryptographic phishing threats, not every remote threat".
4. **Recovery and fallback remain a weak path for key-only schemes.** Kunke2021 (E4): "Some even rely on passwords, taking passwordless authentication ad absurdum." (Abstract); Buettner2024 (E3): "Account recovery mechanisms remain a relevant entry point for account takeover attacks" (Conclusion).
5. **RBA is not a general substitute.** Campobasso2020 (E3): "to circumvent risk-based authentication system and effectively bypass multifactor authentication mechanisms" (Abstract); Lin2022 (E3, abstract only): phishing kits replicate fingerprints to bypass 2FA; Makowski2023 (E3): "We confirm the observation of Wiefling et al. [41] that RBA is rarely triggered at several services." (Sec. 1); Temoshok2025: risk signals do not "substitute for an authentication factor" (Sec. 2, p. 4); Wiefling2019 (E2/E3): "verification codes are currently the unwritten standard for additional RBA authentication factors." (Conclusion) i.e. RBA relies on a second factor when it fires.
6. **P and P+ fail against phishing and malware.** NCSC2026paper Table 19a (E5): manager-generated passwords "Vulnerable" to credential harvest, AitM, infostealer and sync-fabric attacks; NCSC2026page: "Where passkeys are not an available option, you should continue to use strong passwords, for example generated by a password manager and enable 2SV ." Single-factor passwords in practice: Holthouse2025 (E3, abstract) credential stuffing against the 23andMe accounts "exacerbated by ... the absence of robust security measures such as multi-factor authentication (MFA)".
7. **Optional MFA does not help: mandated MFA does.** Kamar2026 (E2, abstract only): "mandatory 2FA significantly reduced the number of compromised bank accounts, whereas optional 2FA did not." This bears on the effect question; it does not compare against any single-factor alternative.

### 9c. Verdict on H_necessary

Against R1 to R4 (and R2) a bound cryptographic key resists at least as well as password plus a code or push (NIST definition, NCSC assessment, Berladskyy2026), so the number of factors is not what delivers security against those threats; **in that sense MFA is not necessary**, and the NCSC and OMB/CISA now recommend phishing-resistant authentication over adding factors to weak ones. But: (i) no source tests case C against local threats or against a case B comparison in a controlled or measured way (so the "comparable security with a **single** factor" part is untested), (ii) the NCSC's positive evidence is for a key with user verification, which it calls multi-factor, (iii) recovery, session theft (R7), provider compromise, malware and approval deception are open for key schemes, and (iv) the standards require two factors at the higher levels.

## 10. Limitations

* A capped sample (40 per query x provider cell); 13 of the 28 answered cells hit the cap, so more relevant records probably exist.
* IEEE Xplore: the two supplementary queries failed (quota); arXiv gives low recall on long boolean strings.
* One automated screener (a language model) over titles and abstracts; many records have no or only a short abstract (Scopus returns none), so the classification is weaker there. Many classifications had confidence below 0.7; I read every qualifies-claim, supports-claim row of confidence below 0.7 and the adjacent rows whose titles mention passkeys, FIDO2, RBA or MFA effect.
* ACM, Springer, and IEEE full texts were mostly closed; nine cited sources are abstract-only (see section 4).
* The session hit list contains many 2026 records from Zenodo, TechRxiv and low-tier journals whose findings I could not check; I treated them as uncited.
* The evidence for case C and for P+ is expert assessment (E5) and analysis (E3/E4); I found no E1 and no E2 comparison with a multi-factor case. Source heterogeneity prevents any combined estimate.
* The classification categories for the 9 papers I overrode are recorded as a second tag in the session ("qualifies-claim; adjacent-subtopic"), because scholar's `sessions decide` appends tags and cannot remove them; the table export treats them as discarded and omits them.
* The NCSC paper's tables are one authority's assessment; they are the only place that treats P+ and FIDO2 in one scheme, and they concern individual users (not enterprise).

## 11. What could not be obtained, and what was dropped

Could not obtain (needs the user):
* Regulation (EU) 2018/389 (PSD2 strong customer authentication), `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32018R0389` (HTTP 202 bot challenge; stopped). Load-bearing for the "requirements" table.
* The FFIEC 2005 guidance on authentication in internet banking, referred to by Cocheo2006 (not in a provider index; the abstract is garbled).
* Full texts: Catalano2025 (10.1007/s11416-025-00556-2, Springer 403), Mahdad2024 (10.1145/3658644.3690286, ACM 403), Lee2025 (10.1109/ACSAC67867.2025.00037, no OA copy), Kamar2026 (10.1177/00111287261441235, no OA copy), Lin2022 (USENIX Security 2022, I tried one URL, 404), Spooren2015 (10.1145/2751323.2751329), Holthouse2025 is on arXiv but I did not read the full text, NISTcswp4 (10.6028/nist.cswp.4, only the abstract read).
* The NCSC technical paper is HTML only; I read its text but no printable PDF was cached.

Dropped (never cited): the Zenodo monograph on FIDO2 resilience against AiTM (10.5281/zenodo.23955576; unreviewed, one author, the lab results could not be independently checked); "An In-Depth Analysis of Password Managers and Two-Factor Authentication Tools" (10.1145/3711117; the abstract states no finding, full text closed); "Traditional Multi Factor Authentication Under AiTM Phishing: A Controlled Campaign in Ecuador" (10.1007/978-3-032-41327-7_14; no abstract or full text available, only the title); the 2026 Zenodo/TechRxiv/IJ-journal reviews on passkeys (not verifiable); all vendor and trade-press web pages returned by WebSearch (rows 8 and 9 above); the PSD2 commentary pages (row 2).

## 12. Reproduction details

* Table command: `scholar sessions export mfa-necessary -f table --bearing-only --lang en --label hits-necessary --track "Is multi-factor authentication necessary" --theme RBA="Risk-based authentication" --theme FIDO="Cryptographic keys and passkeys" --theme REC="Account recovery and fallback" --theme STD="Standards and requirements" --theme ATT="Attacks on and measurements of MFA" -o <OUT>/mfa-necessary-full` (`-f table` worked; the fallback script was not needed). Caption of the generated table: 18 cited, 9 supporting and 18 qualifying out of 497 unique hits.
* Classification model: `anthropic/claude-sonnet-5-5`, `scholar llm classify mfa-necessary --no-examples -n 450 -m anthropic/claude-sonnet-5-5 -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit` (two runs: 435 papers, then 87 more after the supplementary queries; zero left pending). The research context text is stored in the session (`scholar llm context mfa-necessary`).
* Human overrides: **9 recorded** with `scholar sessions decide --discard -t adjacent-subtopic` (voice-assistant insecurity paper, disposable phone numbers and SMS verification, Security Friction Quotient, Mercer Advisors breach case, Rwanda online banking, ATO detection in SSO with a new ML scheme, HF-SCA scheme, lexical vulnerability of password management systems, 2FA in Nigerian banking, i.e. new schemes, off-subject incidents or effect-only studies, from qualifies/supports to adjacent). **1 not recorded in the session**: Berladskyy2026 was classified qualifies-claim, but I read it as supporting "keys resist phishing" (its demonstrated attacks needed substantial effort); I did not change it because the tool can only append tags. Theme tags (RBA, FIDO, REC, STD, ATT) were attached to 18 cited sources with `scholar sessions decide --keep -t`.
* Date: 2026-11-12. KTH SOCKS tunnel opened for full-text fetches and closed at the end.

## 13. Bib keys (25) and files

`Temoshok2025, Wiefling2022, Wiefling2019, Makowski2023, Campobasso2020, Lin2022, Spooren2015, Buettner2024, Berladskyy2026, Buettner2025, Kunke2021, Catalano2025, Mahdad2024, Lee2025, Jacomme2021, Kamar2026, Holthouse2025, NISTcswp4, Cocheo2006, CISA2022, OMB2022, NCSC2026paper, NCSC2026blog, NCSC2026page, NCSC2026methods`.
`check_provenance.py`: OK (all entries complete). `check_metadata.py`: 17 DOI entries checked, one benign author-format mismatch (NISTcswp4: corporate author), three arXiv-only entries carry `eprint` instead of `doi` (Crossref has no record for arXiv DOIs); the non-DOI entries (Lin2022, Cocheo2006, CISA2022, OMB2022, four NCSC entries) were verified by hand against the retrieved documents.

Output directory: `/tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/mfa-necessary`: `mfa-necessary.bib`, `mfa-necessary.csv`, `mfa-necessary-full.tex`, `mfa-necessary-report.md`.
