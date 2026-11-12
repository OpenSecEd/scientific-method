# RQ1 (effect): does multi-factor authentication reduce account compromise?

Session `mfa-effect`, run 2026-11-12 (searches 10:19-10:25 CET; classification 11:00-11:20).
Question: "Does multi-factor authentication reduce account compromise, by how much, and for which kinds of second factor?"
Protocol: `/home/dbosk/devel/edu/scientific-method/modules/01-literature/mfa/contents.tex` (queries S1, S2, C1 for RQ1). The repository was not edited.

## Answer in brief

Yes, but the size depends on who measured, on what, and on the kind of factor.

- Best-grade evidence (E2, real accounts) all points the same way: compromise is lower with a second factor. The figures range from 43% fewer takeovers (one marketplace, `kawase2019`, abstract only) via 99.22% lower risk (Microsoft enterprise accounts, `meyer2023`) to 94-100% of hijacking attempts blocked (Google, `doerfler2019`).
- The size of the reduction differs widely, and the large figures are the least trustworthy: they come from the providers themselves, from samples of suspicious activity, without randomisation.
- Factor kinds: in the two E2 studies that split by factor, an authenticator app or on-device prompt did better than SMS code (Microsoft failure rates 0.97-0.99% versus 1.66%; Google 99%/90% versus 96%/76% for phishing/targeted), and a security key blocked 100% of the (few) attempts in Google's data (95% interval +-25 to 28 points). No study here separates case A2 (push) from A1 with a key-based control, and none measures case B or C against A3.
- Narrowing evidence: optional 2FA at two Canadian banks showed no measurable reduction while mandatory 2FA did (`kamar2026`, abstract only); documented bypasses exist for SMS (`mirian2019`), for risk-based and cookie-based flows (`campobasso2020`, `wang2024`) and, in a proof of concept, for hardware keys (`catalano2025`). These show that bypass is possible, not how often.
- Contradicting pile: no study found reporting zero or negative effect of MFA on compromise in a population comparison. The counter-queries returned bypass demonstrations (E3), implementation flaws, adoption studies and many scheme proposals, but no measurement of "no effect". This is a result of a capped search (40 per query and provider), not proof of absence.
- Hypothesis H-effect (reduces compromise; size differs widely between kinds): supported in direction; "differs widely between kinds" is supported by the SMS-versus-app/prompt gap and the optional-versus-mandatory gap, but the gaps measured within one provider are modest (a few percentage points of attempts), while the across-study spread (43% to 99%) mixes factor kind with setting, method and who measured.

## 1. Provider health (`scholar providers check`, 2026-11-12 10:18, route: direct)

Full output: `providers-check.txt`.

| Provider | Status |
|---|---|
| s2 (Semantic Scholar) | key rejected, HTTP 403: not searched |
| openalex | ok (daily budget $0.992 of $1.00 left at start) |
| dblp | rate limited, HTTP 429 (the lead said DBLP serves an anti-bot page): not searched |
| wos | ok |
| ieee | ok |
| arxiv | ok |
| scopus | ok, "standard view (no abstracts, first author only)" |

Searched: openalex, wos, scopus, ieee, arxiv. Not searched: Semantic Scholar, DBLP. No query cell failed (all 25 cells answered; no HTTP 429 from OpenAlex; fewer than 200 OpenAlex requests were made, since 10 search calls plus enrichment).

## 2. Queries, strings sent, and hits (query x provider)

M = ("multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification").
Strings sent are in `sent-<Q>-<provider>.txt` in this directory; the same keywords everywhere, wrapped as `TS=(...)` for WoS and `TITLE-ABS-KEY(...)` for Scopus. Limit 40 per cell.

Planned queries:

- S1 = M AND (("account compromise" OR "account takeover" OR hijacking) AND (effectiveness OR empirical OR measurement))
- S2 = M AND ((adoption OR deployment) AND ("risk reduction" OR "compromise rate" OR incident))
- C1 = M AND ((ineffective OR "no effect" OR "does not prevent" OR "false sense of security" OR limitations))

Added (see Deviations):

- R1 = M AND (("compromised accounts" OR "account compromise" OR "account takeover" OR hijacking OR hijacked) AND (reduces OR reduction OR "real-world" OR "large-scale" OR prevented OR blocks))
- R2 = M AND ((adoption OR deployment OR enabled) AND (compromised OR breach OR hijacked OR "account takeover") AND (users OR accounts OR customers))

| Query | OpenAlex | WoS | Scopus | IEEE Xplore | arXiv | Sum |
|---|---|---|---|---|---|---|
| S1 | 40 | 9 | 13 | 5 | 2 | 69 |
| S2 | 40 | 9 | 16 | 8 | 1 | 74 |
| C1 | 40 | 40 | 40 | 40 | 40 | 200 |
| R1 (reword) | 40 | 25 | 29 | 18 | 3 | 115 |
| R2 (reword) | 40 | 39 | 40 | 40 | 10 | 169 |
| Sum | 200 | 122 | 138 | 111 | 56 | 627 |

Semantic Scholar and DBLP: not searched (key rejected / unavailable). No cell is failed or incomplete (`error: None`, `retries: 0` in all 25 search records).

Example of the exact strings (S1): OpenAlex/IEEE/arXiv `("multi-factor authentication" OR "multifactor authentication" OR "two-factor authentication" OR "2FA" OR "two-step verification") AND (("account compromise" OR "account takeover" OR hijacking) AND (effectiveness OR empirical OR measurement))`; WoS `TS=(` + same + `)`; Scopus `TITLE-ABS-KEY(` + same + `)`. All 25 are in the `sent-*.txt` files.

## 3. Non-scholar searches (WebSearch, WebFetch, curl), all 2026-11-12

| # | Tool | Verbatim query or URL | Outcome |
|---|---|---|---|
| 1 | WebSearch | how effective is two-factor authentication at preventing account takeover measured on real accounts | Led to the Google/NYU/UCSD hijacking study (known item, DOI 10.1145/3308558.3313481, then found in the scholar hit list as well) and to Google's 50% claim and a Canadian-bank natural experiment (both then found/verified below). Snippets not cited. |
| 2 | WebSearch | multi-factor authentication blocks percent of automated account compromise attacks study of enabled accounts | Led to Microsoft's 99.9% claim and the Microsoft measurement (arXiv 2305.00945, also in scholar hits). |
| 3 | WebSearch | two-factor authentication limitations overstated effectiveness self-selection careful users compromised accounts evidence | Counter-query. Returned no study of self-selection bias; returned Google's auto-enrolment figure (which avoids opt-in selection), a 2FA bypass study (`wang2024`) and trade-press opinion (dropped). |
| 4 | WebSearch | auto-enrolling accounts in two-step verification 50% decrease in compromised accounts | Press coverage only (secondary). |
| 5 | WebSearch | natural experiment two-factor authentication account takeover fraud banks mandatory versus optional | Returned abstract of `kamar2026` only. |
| 6 | WebSearch (domains blog.google, security.googleblog.com, cloud.google.com) | Google 2-step verification auto-enrolled 150 million accounts 50% decrease in accounts being compromised | Issuing-organisation page found. |
| 7 | WebSearch (domains microsoft.com, techcommunity.microsoft.com) | MFA blocks 99.9 percent of account compromise attacks identity security Microsoft | Issuing-organisation page found. |
| 8 | WebFetch | https://par.nsf.gov/servlets/purl/10094542 | Returned a PDF that WebFetch could not decode; the PDF was then fetched with `fetch_pdf.py` (scholar cache) and read. |
| 9 | curl (no proxy) | https://blog.google/technology/safety-security/safer-internet-day-2022 | 200; sentence read (see `google2022`). |
| 10 | curl (no proxy) | https://www.microsoft.com/en-us/security/blog/2019/08/20/one-simple-action-you-can-take-to-prevent-99-9-percent-of-account-attacks/ | 200; sentence read (see `maynes2019`). |
| 11 | curl (no proxy) | https://blog.google/technology/safety-security/making-sign-safer-and-more-convenient | 200; read, general statement only ("a second form of authentication dramatically decreases an attacker's chance of gaining access"), no figure; not cited. |

alphaXiv was not used. Nothing was retrieved by searching author or title to discover it; the three known-item retrievals (rows 1, 2, 5) were of items first identified by concept queries. The KTH SOCKS tunnel on port 1081 was already open (another agent's); the closed-access ACM, SAGE, IEEE and Springer papers still could not be fetched (see section 9).

## 4. Flow counts

| Step | Count |
|---|---|
| Records identified (sum of hits over 25 query x provider cells) | 627 |
| After de-duplication (distinct papers in the session) | 404 (the generated table's caption counts 387 "unique hits", since it merges a few more near-duplicates) |
| Classified: supports-claim | 6 |
| Classified: qualifies-claim | 24 |
| Classified: adjacent-subtopic | 302 |
| Classified: off-topic-false-hit | 72 |
| Read in full text | 4 papers (`meyer2023`, `doerfler2019`, `wang2024`, `campobasso2020`) and 2 provider web pages (Google, Microsoft) |
| Read as abstract only (cited) | 5: `kamar2026`, `kawase2019`, `egenti2026`, `mirian2019`, `catalano2025` |
| Abstract-only, classified supporting but not cited | 2: Ededet 2026 (10.56201/ijcsmt.vol.12.no1.2026.pg144.154) and Ghana banking study (10.37602/ijssmr.2025.8106): self-described mixed-method studies without effect sizes in the abstract; not cited as evidence of size |
| Cited (bib entries) | 11 |
| Retracted / superseded (`scholar verify`) | 1 retracted (a 2024 conference paper, classified adjacent, not cited), 1 superseded (not cited); 312 ok, 90 unknown (no DOI in Crossref) |

Counting note: the model's first pass gave 76 qualifies, 257 adjacent, 71 off-topic and **0 supports**; it tagged even the Microsoft and Google measurements as qualifies-claim (confidence 0.95), apparently because they also narrow the claim by factor kind. I moved those to supports-claim (see section 10).

## 5. Deviations from the planned queries

1. S1 and S2 returned few records on WoS, Scopus, IEEE and arXiv (1-16 each) and mostly records on other topics in the OpenAlex top 40 (fraud detection, scheme proposals). I added two reworded queries R1 and R2 (strings above) on all five providers, using the same concept terms plus the field's own wording ("compromised accounts", "hijacked", "real-world", "large-scale", "enabled", "breach"). The originals S1, S2 stay in the session and in the matrix. Whether R1/R2 recover every relevant S1/S2 result was not checked paper by paper; the cited Meyer and Doerfler papers were also returned by the original S1, Kawase and Mirian only by R1.
2. C1 returned 40 on every provider and was not reworded, but it is noisy ("limitations" matches generic scheme papers).
3. Semantic Scholar and DBLP not searched, as instructed.
4. The `scholar llm` default model (`openai-codex/gpt-5.6-sol`) is not available in scholar's own Python environment (plugin too old, token expired); classification used `anthropic/claude-opus-4-8` instead (section 10).
5. `scholar enrich` of the whole session ran for over 30 minutes without finishing (rate limits) and was stopped; it was redone with `--enrich-providers wos,ieee` (89 papers enriched). 118 Scopus records (standard view) had no abstract, of which some stayed without one (classified on title and metadata). A search of abstracts for the rest was not done.

## 6. Effect sizes

Grades are those of the protocol (E1 experiment, E2 real accounts, E3 attack, E5 consensus, E6 provider report without method). "Case" maps to the protocol's cases (A1 code by text message or app, A2 push, A3 key, B key with user verification, C key alone, P password only).

| Key | Year | Population, setting | Kind of second factor (case) | Comparison | Reported effect | Grade | How far to trust it |
|---|---|---|---|---|---|---|---|
| `meyer2023` | 2023 | Microsoft Azure AD commercial accounts reviewed for suspicious activity, 22 Apr-22 Sep 2022; 128,000 accounts with leaked passwords in a second sample | Mixed; split for leaked-credential sample: authenticator OTP (A1), notification (A2), SMS (A1) | MFA enabled versus not, by benchmark-multiplier estimate | Compromise rate 0.0079% versus 1.0071%: risk reduction 99.22%; leaked credentials: 98.56%; failure rate with MFA: OTP 0.99%, notification 0.97%, SMS 1.66% | E2 | Authors are the provider's staff; arXiv preprint; sample is accounts flagged as suspicious; sample sizes behind the 0.0079% figure are estimates with a stated CI; MFA is set by tenant admins, not randomised, so careful organisations may self-select; no key-based factor separated. |
| `doerfler2019` | 2019 | Google consumer accounts; 350,000 hijacking attempts by bots, phishers, targeted attackers | Risk-triggered challenges: on-device prompt (A2), app OTP, SMS code (A1), security key (A3-like, no password interplay measured), knowledge-based | Challenge versus attempt blocked; no group without challenges | Device-based: over 94% of phishing-rooted and 100% of automated attempts blocked; prompts 99% phishing, 90% targeted; SMS 96% phishing, 76% targeted; security key 100% (n small, interval +-25 to 28); knowledge-based as low as 10% (phishing) | E2 | Peer reviewed; authors at Google; counts only attempts that reached a challenge; not static always-on 2FA; no unprotected baseline; small n for keys and for targeted attacks. |
| `kamar2026` | 2026 | Three Canadian banks, Mar 2021-Feb 2022, illicit-market threat-intelligence data | 2FA (kind not given in abstract); two banks optional, one mandatory | Bayesian time series before/after, by policy | Mandatory: significant reduction of compromised accounts; optional: no significant reduction (sizes not in the abstract) | E2 (quasi-experimental) | Peer reviewed; outcome is a proxy (accounts seen on illicit markets); abstract only. |
| `kawase2019` | 2019 | One online vehicle marketplace (mobile.de) | "mutual two-factor authentication" (kind not stated) | Before/after | 43% fewer account takeovers | E2 | Single operator, before/after, abstract only. |
| `egenti2026` | 2026 | Nigerian online banking, 2019-2024 statistics plus expert opinion plus prototype | 2FA generally; app-based versus SMS-OTP (A1) | Before/after proliferation; prototype comparison | Fraud cases down about 10-15%; compromise 0% (app) versus 4% (SMS) in the prototype | E2 (weak) | Mixed method, abstract only; the 0% versus 4% comes from a prototype, not from accounts; confounded by a five-year trend. Low trust. |
| `google2022` | 2022 | Google accounts auto-enrolled in 2SV in 2021 (over 150 million) | 2-step verification (mixed) | Not stated | "50% decrease in accounts being compromised" | E6 | Provider's own post; no method, no counts, no comparison group; per press only accounts with recovery options were enrolled (secondary, not verified). |
| `maynes2019` | 2019 | Microsoft cloud services | MFA (unspecified) | Not stated | "can block over 99.9 percent of account compromise attacks" | E6 | Marketing blog by a product marketing manager; no method; Microsoft's later measurement (`meyer2023`) gives 99.22%. |

Pattern: the three measurements on enterprise/consumer platforms with a vendor author give 99% or more; the independent operator and bank studies give 10-43% and a null for optional 2FA. Whether that is the setting (platform with strong risk engine and many bots versus a single site), who measured, or the outcome definition cannot be told from these sources.

## 7. Findings that support

**S-1 (E2) `meyer2023`.** MFA-enabled enterprise accounts were compromised far less often. Quote (Abstract): "MFA reduces the risk of compromise by 99.22% across the entire population and by 98.56% in cases of leaked credentials. We further demonstrate that dedicated MFA applications, such as Microsoft Authenticator, outperform SMS-based authentication, though both methods provide significantly enhanced security compared to not using MFA." Also (Sec. 5): "we find that SMS was 40.8% less effective than Microsoft Authenticator". Read in full text.

**S-2 (E2) `doerfler2019`.** Device-based challenges block nearly all bots and most phishing. Quote (Abstract): "Device-based challenges provide the best protection, blocking over 94% of hijacking attempts rooted in phishing and 100% of automated hijacking attempts." Quote (Sec. 4.1): "security keys provide the best protection, blocking 100% of attacks in our dataset." Read in full text.

**S-3 (E2) `kamar2026`.** Mandatory 2FA reduced compromise at banks. Quote (Abstract): "Bayesian time series analysis revealed that mandatory 2FA significantly reduced the number of compromised bank accounts, whereas optional 2FA did not." Abstract only.

**S-4 (E2) `kawase2019`.** A second factor cut takeovers by 43% at one marketplace. Quote (Abstract): "implemented a mutual two-factor authentication that achieved a reduction of 43% of account takeovers." Abstract only.

**S-5 (E2, weak) `egenti2026`.** Fraud down about 10-15% after 2FA; app-based better than SMS. Quote (Abstract): "fraud cases decreased by about 10-15% after the proliferation of 2FA while there was a reduction in the compromise rate to 0% for app-based authentication compared to 4% for SMS-OTP." Abstract only.

**S-6 (E6) `google2022`.** Quote: "In 2021, we auto-enrolled over 150 million people in two-step verification (2SV). As a result of this effort, we have seen a 50% decrease in accounts being compromised." Provider's claim; read on the issuer's page.

**S-7 (E6) `maynes2019`.** Quote: "MFA can block over 99.9 percent of account compromise attacks". Provider's claim without method.

Convergence: every measurement of real accounts or incidents found (S-1 to S-5) shows lower compromise with a second factor; none shows higher or equal compromise except the optional-2FA arm of S-3.

## 8. Findings that contradict or narrow

**N-1 (E2) `kamar2026`, optional 2FA.** Quote as S-3, second clause: "whereas optional 2FA did not." Narrows: the effect needs coverage; self-selected adoption showed no population effect at those banks. Abstract only.

**N-2 (E2) `meyer2023` and `doerfler2019`, SMS weaker.** Meyer Table 2: failure rate SMS 1.66% versus authenticator 0.99%; Doerfler Sec. 1: SMS "preventing only 96% of attacks rooted in phishing and 76% of targeted attacks", against 99% and 90% for on-device prompts. Narrows: the benefit depends on the kind of factor. Both read in full text.

**N-3 (E3) `mirian2019`.** Quote (Abstract): "Attackers primarily relied on tailored phishing messages, with enough sophistication to bypass SMS two-factor authentication." 5 of 27 services succeeded; the market was small. Narrows SMS (A1) against targeted attackers. Abstract only.

**N-4 (E3) `campobasso2020`.** Quote (Abstract): "Impersonation-as-a-Service (IMPaaS) allows attackers to systematically collect and enforce user profiles (consisting of user credentials, cookies, device and behavioural fingerprints, and other metadata) to circumvent risk-based authentication system and effectively bypass multi-factor authentication mechanisms." Narrows: stolen sessions and profiles go around the second factor (threat R7). Read in full text (abstract and Sections 1-2).

**N-5 (E3) `wang2024`.** Quote (Abstract): "Our analysis and evaluation found three zero-day vulnerabilities on three service providers that could allow an attacker to access a victim's account without possessing the victim's second authentication factor, thereby bypassing 2FA protections entirely." Narrows: a deployed 2FA is only as good as its implementation (3 of 407 systems). Read in full text for abstract and introduction.

**N-6 (E3) `catalano2025`.** Quote (Abstract): "we show how the effectiveness of BitM-used along a Reflected XSS vulnerability exploitation-can be improved resulting in the novel BitM + attack that proves to be capable of defeating any available MFA method including FIDO2/WebAuthn solutions that rely on hardware dongles". Narrows the 100% security-key figure in `doerfler2019` to "in the attacks observed"; a proof of concept needing an XSS flaw. Abstract only.

**N-7 (E6 against E6) `maynes2019` versus `meyer2023`.** Microsoft's 2019 blog says over 99.9%; its own 2023 measurement says 99.22%. The headline number is a rounded older claim.

Self-selection and vendor-method concern: `meyer2023` (Sec. 3) states that "Some accounts had MFA configured, and some did not", with the choice made by tenant administrators; it does not adjust for organisation. `doerfler2019` has no unprotected baseline. `google2022` discloses no method. The WebSearch for self-selection (query 3) found no study quantifying it. The "counter-queries that came back empty" are: C1 on all five providers returned no measurement showing that MFA does not reduce compromise; WebSearch query 3 returned no study of self-selection. The only null result found is optional 2FA in `kamar2026`.

## 9. Limitations and what could not be obtained

Limitations (facts about the data and tools):

- Capped search (40 per cell) and keyword relevance ranking: older or grey literature is under-represented. S1/S2 returned few records outside OpenAlex.
- Semantic Scholar and DBLP not searched.
- One screener (a language model, one pass, no examples); all 24 qualifies rows and all 30 rows with confidence below 0.7 were looked at by me; I did not read the 302 adjacent rows individually, only their titles (and some abstracts), so a relevant paper with an off title may be misclassed.
- Scopus "standard view" returned no abstracts and only first authors; 118 Scopus rows were classified on title and metadata, and the author of a record (e.g. "A. Mirian") is incomplete there; bib entries were completed from Crossref.
- Most of the E2 evidence is from three providers (Google, Microsoft, two banks plus one marketplace); the closed-access papers were read as abstracts only.
- Effect sizes cannot be pooled: different outcomes (compromise rate, share of attempts blocked, takeovers, fraud cases), populations and factor kinds.
- No source found separates cases A3, B and C from A1 in a measurement of compromise; that belongs to RQ2.
- Crossref lists C. Jordan Howell as family name "Jordan Howell"; the bib uses Howell, C. Jordan; `check_metadata.py` flags this and the arXiv DOIs (no Crossref title) as benign.

Could not be obtained in full text (all read as abstract only):

| Title | DOI | Why |
|---|---|---|
| Evaluating the Effectiveness of Two-Factor Authentication (2FA) in Mitigating Account Takeover Fraud (Kamar et al.) | 10.1177/00111287261441235 | SAGE, no open-access copy found; behind a bot check; not circumvented |
| Internet Fraud: The Case of Account Takeover in Online Marketplace (Kawase et al.) | 10.1145/3342220.3343651 | ACM, no open-access copy found |
| Hack for Hire (Mirian et al.) | 10.1145/3308558.3313489 | ACM, HTTP 403 |
| Defeating FIDO2/CTAP2/WebAuthn using browser in the middle (Catalano et al.) | 10.1007/s11416-025-00556-2 | Springer returned HTML, not a PDF, also through the tunnel |
| The Effectiveness of Two-Factor Authentication in Preventing Online Banking Fraud in Nigeria | 10.70882/noun-ijcea.2026.1119 | not fetched (low-trust source, abstract used) |
| Evaluating the Effectiveness of MFA in Preventing Unauthorized Access to University Information Systems; Evaluating the Effectiveness of MFA in Mitigating Cyber Threats in Digital Banking in Ghana | 10.56201/ijcsmt.vol.12.no1.2026.pg144.154; 10.37602/ijssmr.2025.8106 | not fetched; not cited |
| The 2FA Illusion (ACSAC 2025) | 10.1109/acsac67867.2025.00060 | IEEE, no open-access PDF found; classified qualifies (reset flows), not cited here |

DROPPED (existence or content not checked, not cited): press coverage of Google's and Microsoft's figures; trade-press and vendor blogs returned by WebSearch (Bitdefender, TechTarget, Ravelin, mojoauth, drivestrike, securityscientist.net and others); the Fraud Practice PDF. Also dropped: Microsoft's Entra documentation statement of "99.2%", which was only seen in a search summary, and the Google 2019 "100%/96%/76%" blog figures, which were seen only as quoted in `meyer2023` and press.

## 10. Classification

- Model: `anthropic/claude-opus-4-8` (zero-shot, `--no-examples`, batches of 10-30), because scholar's default model `openai-codex/gpt-5.6-sol` was not usable (see Deviations).
- Context: the RQ with the protocol's inclusion/exclusion criteria and the four tags, set with `scholar llm context mfa-effect "..."` (shown by `scholar llm context mfa-effect`).
- Commands: `scholar llm context mfa-effect "<RQ, criteria, tags>"`; `scholar llm classify mfa-effect --no-examples -t supports-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit -m anthropic/claude-opus-4-8 -n 30` repeated until none were pending. The run twice reported one paper as "Left pending, not exactly one category tag"; the final export shows a category on all 404 rows (how those two were resolved was not recorded).
- Human overrides: **52** rows (decision_source `human` in the CSV). 6 qualifies-to-supports (Meyer, Doerfler, Kawase, Egenti, Ededet, Ghana study); 35 qualifies-to-adjacent (scheme proposals, retracted paper, reviews, opinion pieces, adoption or availability studies); 10 further qualifies-to-adjacent after a second pass (availability studies, adoption, NIST compliance, review) and 1 qualifies-to-off-topic (jailbreak detection in banking apps). First-pass model tags were not kept per paper except in `pre-override-session-backup.json` (copy of the session file before the overrides).
- Mechanics: `scholar sessions decide` adds tags and cannot remove the model's tag, so the overrides were written by editing the `tags` and `status` of the session JSON `~/.local/share/scholar/review_sessions/mfa-effect.json` directly (not through scholar); the file loads and exports fine.
- The model assigned zero papers to supports-claim in the first pass; I read this as a weakness of the tag definition for papers that both support and narrow, and decided by the main finding.
- Theme tags on cited papers: `measured-effect` (7), `bypass-attack` (6).

Table command (the exact command used):

```
scholar sessions export mfa-effect -f table --bearing-only --lang en --label hits-effect --track "Effect of multi-factor authentication" --theme measured-effect="Measurement of effect" --theme bypass-attack="Bypass or attack on MFA" -o /tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/mfa-effect/mfa-effect-full
```

The generated table's caption says "6 cited, 0 supporting and 22 qualifying or contradicting it, out of 387 unique hits". It counts papers with a theme tag as "cited" and so does not match the 6 supporting and 24 qualifying above; check the caption before using the table.

## 11. Output files (all in `/tmp/claude-1000/-home-dbosk-devel-edu-scientific-method-modules-01-literature/d4416f34-4f69-4915-99d4-89e8a316f9e1/scratchpad/mfa-effect/`)

- `mfa-effect.bib` (11 entries with provenance; `check_provenance.py`: OK; `check_metadata.py`: only benign author/arXiv-title notes)
- `mfa-effect.csv` (classified session export, 404 rows)
- `mfa-effect-full.tex` (audit table, LaTeX longtable fragment; the label `tab:hits-effect`)
- `mfa-effect-report.md` (this file), `providers-check.txt`, `sent-*.txt` (strings sent), `run.sh`, `run2.sh` (the search scripts), `table-command.txt`, `pre-override-session-backup.json`.

## 12. What was left undone

- No second screener; adjacent rows not individually read.
- Full texts of the five closed-access cited papers not read.
- The reworded queries R1/R2 were not checked paper by paper against S1/S2 for recovery of relevant results (the cited Meyer and Doerfler papers appear in S1 as well).
- No search for the policy and standards literature (E5) on RQ1; the lead's protocol asks for it under another question.
