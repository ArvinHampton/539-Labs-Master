# PP-AUDIT — PR1 LIT: BQP/NP/PH · C_HQH chain · 128-qutrit · mod-27
Mode: soft SF audit only (not first-prove). No CERT issued. No messages sent. Date 2026-11-03 ~11:15 CST.

## §0 Packet identity (verified live)
| Item | Path | sha256 | Expected prefix | Result |
|---|---|---|---|---|
| PR1 findings | reports/PR1-FINDINGS-LIT_BQP_NP_PH_CHQH_QUTRIT128_MOD27_2026-11-03.md | bc58e2e5883bc40dbed1f46e84c92792b409e9e20b55469b1f8b8436fb3abfc3 | bc58e2e5 | CONFIRM |
| PR1 PRESS | reports/SOFTSF_PRESS_PR1_LIT_BQP_NP_PH_CHQH_QUTRIT128_MOD27_2026-11-03.md | c24d068f16b60c1720b2007177a69d84d63a2b3559b9f1a8d720418c537b3fdc (= sidecar) | c24d068f | CONFIRM |
| Tip (read-only, not modified) | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | 7cddb188…dfc91 | CONFIRM |

## §1 Literature (WebFetch this run)
| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | BBBV quant-ph/9701001: random-oracle NP ⊄ BQTime(o(2^{n/2})); Thm 3.5; caveat "do not rule out the possibility that NP⊆BQP"; BPP⊆BQP⊆PSPACE (BV); BQP^BQP=BQP (Cor 4.15) | CONFIRM | arXiv page opened; quotes match verbatim. |
| 2 | Aaronson 0910.4698: abstract "open problem since the earliest days"; Thm 1 relation separation FBQP^A ⊄ FBPP^{PH^A} (unconditional); Thm 3 decision BQP^A ⊄ PH^A conditional on GLN; unconditional BPP_path/SZK; §1 RFS gives BQP^A ⊄ NP^A, MA^A; ADH BQP⊆PP footnote | CONFIRM | arXiv page opened; all quotes match. |
| 3 | Raz–Tal ECCC TR18-107 (31 May 2018): oracle O with BQP^O ⊈ PH^O | CONFIRM | ECCC page opened; abstract matches. (STOC/JACM DOIs not re-checked; PR1 already marks them SEARCH-ONLY.) |
| 4 | Blok et al. arXiv 2003.03307: five-qutrit superconducting processor (8-transmon ring, 5 used); F_avg=0.568 | CONFIRM | arXiv opened; "we have demonstrated a five-qutrit quantum processor built from superconducting transmon circuits". |
| 4b | Journal ref Phys. Rev. X 11, 021010 (2021) | CONFIRM (upgrade SEARCH-ONLY→VERIFIED) | journals.aps.org/prx/abstract/10.1103/PhysRevX.11.021010 opened: "Phys. Rev. X 11, 021010 – Published 9 April, 2021", same title/authors/abstract. |
| 5 | Bocharov–Cui–Roetteler–Svore arXiv 1512.03824: §4.1 "To add two n-qutrit numbers modulo 3^n, we simply do not compute the the high carry trit c_n" (theory/circuits only) | CONFIRM | arXiv page opened; quote matches (including the doubled "the the"). |

## §2 On-disk checks
| # | Item | Verdict | Evidence |
|---|---|---|---|
| 6 | Codex L64–65 verbatim "…strictly between BQP … and NP-Complete:" / "\(\text{BQP}\subset \mathcal{C}_{\text{HQH}}\subset \text{NP-Complete}\)", no condition stated | CONFIRM | sed -n 63,66p reports/539labs/539_Labs_Technical_Corpus_Codex_2026-11-03.txt. |
| 7 | PR1 §2 / PRESS L9: "A conditional form 'BQP ⊆ C_HQH ⊆ NP' (with ⊆ NP): ABSENT on disk" | **FLAG** | rg across quantum-comp finds it present in prior PP audit files: bridges/PROFESSOR_PROOF/PP-FINDINGS-CATA_FOOLPROOF_RERUN_OW9aec847a_2026-11-03.md L20 (copies in bridges/AUDITOR/ and reports/AUDITOR/): "BQP⊆C_HQH⊆NP ⇒ BQP⊆NP, open … Well-posed conditional: 'If C_HQH ⊆ NP (certificate = Thm A) and BQP ⊆ C_HQH, then BQP ⊆ NP'". Also the PP rerun PRESS: "Chain BQP⊆NP OPEN/conditional". The claim holds only if it is narrowed to the 539 corpus/Codex/live-site sources. Those contain no ⊆NP conditional; only the Codex strict "⊂…⊂NP-Complete" exists there. Suggested correction: "ABSENT in the 539 Labs sources; present only as an audit-side repair in PP-FINDINGS-CATA_FOOLPROOF_RERUN L20." |
| 8 | Logical note: BQP ⊆ X ⊆ NP ⇒ BQP ⊆ NP, which is open and fails relative to oracles (RFS; Raz–Tal ⊇ NP^O) | CONFIRM | Follows from items 2–3. |

## §3 Hardware / mod-27
| # | Item | Verdict | Evidence |
|---|---|---|---|
| 9 | 128-qutrit processor/ALU has no external (experimental-literature) source; on disk only 539-internal (Codex L102 RTL, NSF pitch, zenodo, live site) | CONFIRM | rg hits only 539-internal/grok-chat files. Verified external max is the 5-qutrit device (Blok) and up to d=7 qudits on ions (Ringbauer, per PR1). No external source for 128 found. |
| 10 | Mod-27 test on qutrit hardware: no external source; theory only (Bocharov §4.1, n=3) | CONFIRM | rg: Codex plus grok-chats extracts/rollups only ("mod-27 merge automaton" analyses); no experiment. |

## §4 Summary
CONFIRM 10 + 4b; FLAG 1 (item 7: the "no conditional ⊆NP form anywhere on disk" claim is overstated). The PR1 literature content is accurate. No CERT. Tip untouched (7cddb188…dfc91).
