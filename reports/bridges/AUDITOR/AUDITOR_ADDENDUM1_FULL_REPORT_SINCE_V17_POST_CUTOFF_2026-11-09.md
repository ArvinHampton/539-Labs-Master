# AUDITOR — ADDENDUM 1 to the full since-v17 report: files after the cutoff — 2026-11-09

Role: Auditor, the audit-only keeper. Written Mon 2026-11-09 ~18:27 CST (America/Chicago). Additive and created exclusively (noclobber), with a .sha256 sidecar.
Parent report (not touched): AUDITOR_FULL_REPORT_ALL_ADVANCEMENTS_SINCE_V17_2026-11-09_1816
- .md: b3933d665226d703c5b46519da65698b3cc142ca6cbcb9724080e158604a5350
- .pdf: 49c573d5d71d35ca5d5fb4d7b032de3f76948ed6afb882b6eea7b5230003b078
- Both sidecars unchanged.
Window: files in /workspace/quantum-comp/ and /workspace/539-labs/ with mtime after 18:16 CST, up to the scan at ~18:26 CST. The parent's own outputs are excluded.
Labels: PROVED / CONDITIONAL / OPEN / REFUTED. Reported labels are the **authors' own**; no PP audit of these files was on disk at the scan. Hashes only. No CERT, no Gemini, nothing sent outside.

## 1. Files Physicist named (each verified here)
| # | time (mtime, CST) | file (reports/) | sha256 | sidecar |
|---|---|---|---|---|
| A | 18:19:55 | ERRATUM_LOCAL_RELABEL_ce4d9e80_ROOTNUMBER_VS_FRICKE_SYMBOLS_AND_STS_CONTROL_2026-11-09_1819.md | c2e9b6fe2cb6b08ec24a7f6dfddc967eb7918adb244050d2d67c703b033d42ec | MATCH |
| B | 18:21:07 | FINDINGS_LOCAL_BRIDGE_C_OPEN_ITEMS_RESOLUTION_PASS_2026-11-09_1822.md | 9e34f2dc7fab9b3c42b6f73fc815b3ff2cfc62e496c6af04ce311ed94b6f39dd | MATCH |
| C | 18:18:08 | NL_ERRATUM13_CITATION_MATH_CHECKS_OW_36683379_2026-11-09_1818.md | b5190ea8c908200f8dab6455bcd4462143cad8b4e01993c88425c925be003412 | MATCH |
| D | 18:17:32 | MR2_SOURCE_LIMIT_NARROWING_FLAGS_ALL_SOURCES_PER_OW_36683379_2026-11-09.md | a40843225c36e0010ba82375ab440f6ef23eac685aa49aa419caeac7515fce8b | MATCH |

**A. Local erratum: the ce4d9e80 symbol fix.**
- What it says: it fixes two lines in RELABEL ce4d9e80 and records three matching lines in XW ae951f3e. Neither file is edited.
  - L36: "ε = −w = +1" becomes "w₁₉₆₀₀ = −ε = +1 (root number ε = −1)".
  - L25: the control element is named STS⁻¹.
  - Convention: ε = −w_N at weight 2.
- New PARI checks: Ξ and the −20 twist are **7-isogenous** and not isomorphic. Their a_n agree for all n ≤ 7000, above the Sturm bound 6721.
- Status impact:
  - The fix is **notational only**; no label or value changes. ce4d9e80's rollup 13/2/4/1 stands.
  - Ξ ~ −20 twist by a 7-isogeny, with the same newform: **PROVED** (Local-derived, awaiting PP).
  - This resolves the parent's NOT FOUND item "ce4d9e80 fix".

**B. Local FINDINGS: Bridge C open-items resolution pass.**
- What it says:
  - **Item 2 (Ξ ↔ level-49 Weil carrier): OPEN → PROVED.**
    - f is the CM theta series on L₁ (Hecke, cited).
    - cusp(θ_{L₄₉}) = f exactly.
    - f_Ξ = R_{χ₁₄₀}f = R_{χ₋₂₀}f (Shimura 3.64 cited; Sturm check).
    - w₁₉₆₀₀ = +1 via Atkin–Li, flipped only by χ₋₂₀(−1) = −1.
    - f_Ξ ∉ S₂(Γ₀(980)).
  - Two REFUTED: 2e (span of F₂ twists) and 2f (twist of cusp(θ²); the weights differ).
  - **Item 4a: χ₁₄₀ on all of Γ₀(140), CONDITIONAL → PROVED** (computer-assisted). It uses 259 Schreier generators and 48 Galois twists, with residual 5.21e-13 and a norm argument (margin ~35×). The floating-point error is measured, not interval-bounded, and Local flags this for PP.
  - **Item 4b:** the induced-carrier math is PROVED. Adopting V₈₄ is the Owner's call (CONDITIONAL).
  - **Item 3 (weight 3/2): OPEN → PARTIAL.** 3a–3c are PROVED (exact). 3d is CONDITIONAL on Waldspurger (75/75 squarefree n ≤ 120). O-a, O-b and O-c are OPEN.
  - H₊U stays OPEN/undefined. The joint carrier stays UNDEFINED (Owner neutral).
  - **Bridge C overall: still PARTIAL.**
- **Tally check: CLAIMED 11/2/6/2 = FILE ROLLUP 11/2/6/2. VERIFIED** by counting the named items:
  - PROVED 11: 2a, 2b, 2c, 2d, 2g, the f²-rank fact, 3a, 3b, 3c, 4a, 4b-math.
  - CONDITIONAL 2: 3d, 4b-adoption.
  - OPEN 6: O-a, O-b, O-c, H₊U, Λ₀ dynamics, "2/5-parts".
  - REFUTED 2: 2e, 2f.
- Status impact: as above. All labels are Local's own and need a PP audit. Owner definitions and the neutral items are unchanged. This resolves the parent's NOT FOUND item "Local FINDINGS after 15:20".
- **Custody note (B-1): two files are missing.**
  - Files: evidence_local_bridgeC_resolution_2026-11-09/part3_halfint.py (sha 857e14f370e035bfa9b7be7e2c54d954b0c582ef18ec8c673faddf6361609602) and part3_halfint.log (sha c4b8cf4d87887f98ce185a820d78035da6ca62d0bd0d12a4f3e64ba6d345b006).
  - Both were on disk and hashed by me at ~17:37 CST. My parent report §4.8 quoted the log ("Kohnen plus space S⁺_{3/2}(196) has dimension 0").
  - At ~18:26 CST both are **no longer on disk anywhere under /workspace**.
  - B's evidence list does not name them. B's 3a states the same dim-0 fact, citing part3_search/preimage.
  - The Auditor did not remove them; who did is not on record. **Flag for the Owner/Local.** No value in B depends only on them. The other 10 evidence files (part1, part3_search/preimage/check2, part4 .py/.log) all have sidecars, and all MATCH.

**C. NL erratum 13: citation math checks under OW 36683379.**
- What it says: each cited result is re-graded as "math checked" or "math not yet checked".
  - Checked (PROVED): SSU conformal reduction (M1); Sadun–Segert cohomogeneity and C₂ table to |C₂| ≤ 60 (M3, M4); Taubes hypotheses on S⁴ (M6); BLS frame-bundle example (M8); SU(2)⊂E₈ embedding (M10); Bolza length 2 arccosh(1+√2) (M12); |Aut⁺ Bolza| ≥ 48 (M15); BBBW z ∈ ℤ for g = 2 (M18).
  - Not yet checked (CONDITIONAL): M2, M5, M7, M9, M11, M13 (systole minimality, Jenni global max), M14, M16, M19 (HW/GH/SW/E-string).
  - REFUTED: M17, NL's own "order 21 → 42" script slip. The log is kept and superseded by autcheck_1821.log.
- **Tally check:** file 10/9/0/1 = 20, and the item list agrees. 1800 after the erratum: 15/11/3/2 = 31, stated (not re-derived here). Erratum 12 tally unchanged at 7/5/0/2.
- Status impact:
  - **No upgrade to PROVED from a citation alone** (rule respected).
  - Y12 and Y13 stay CONDITIONAL. Y14 and Y15 stay **OPEN**, now with a concrete route: weighted YM–Higgs via the SSU U(1) reduction.
  - Bolza systole *length* PROVED; *minimality / global max* CONDITIONAL.
  - This partly resolves the parent's NOT FOUND item "citation re-check under 36683379" (NL side).
- **Label discrepancy (C-1, wording only).** The four scripts in /workspace/nl-junction-1817/ all exist and their sidecars MATCH, but C swaps the names on its hashes:
  - fce1f08f… is autcheck.py (C says mathcheck.py);
  - be56e69c… is mathcheck.py (C says autcheck.py);
  - 9401128d… is autcheck_1821.log (C says mathcheck_1820.log);
  - 67186319… is mathcheck_1820.log (C says autcheck_1821.log).
  NL should fix this in an additive erratum.

**D. MR2: source-limit narrowing flags under OW 36683379.**
- What it says: it lists 11 MR2/NL findings (F1–F11) whose ABSENT/unverified status was narrowed by the old arXiv-only diet, plus 4 explicitly not narrowed. It ran 4 widened public web-search clusters (~18:15–18:16 CST; reading only).
  - F1–F3 (γ = 7/20, β(κ)): still **NOT FOUND IN SEARCHED SOURCES**.
  - F4 (erratum-12 citations): candidate journal/DOI sources found for SSU, Sadun–Segert, Taubes and BLS; math "partial/pending"; **none upgraded**.
  - F5 (ultrametric SU(3) map): ABSENT stands.
  - F11 (Bolza numbers): verified numerically (3.057141838961996; 4.896904895356152). Global max pending (Jenni).
- Tally: no PROVED/OPEN rollup. Counts: 11 flagged, 4 not narrowed, 4 clusters. Consistent with the tables.
- Status impact: **no status changes.** It is a queue (P0: PP math audit of the Y12/Y13 lemmas). Together with C, it resolves the parent's NOT FOUND item "citation re-check". The re-check is **filed, but the math is only partly checked and PP has not audited it**.
- Note: header time "~18:16" vs mtime 18:17:32. This is the usual header/mtime lag.

## 2. Other files after 18:16 in the two trees
| time | file | sha256 | sidecar | summary / impact |
|---|---|---|---|---|
| 18:16:27 | reports/OWNER_WRITE_VOICE_11fd320e_AUDITOR_FULL_REPORT_…_1816.md | c7795d6e88d5da7662d3a562f2564313ad472e0cb5560ce684cb067c61acd2b7 | MATCH | the OW governing the parent report (already cited there) |
| 18:17:07 | reports/MR2_TWISTED_VACUA_EINSTEIN_SYMBOLIC_AND_GLOBAL_CURVATURE_2026-11-09_FRAME_EINSTEIN_AND_DG4_CONTROL.log | 604aa979f656cf38ca238fdf2a83ab5280b2674b57156a9e806d425a35e5f024 | MATCH | dG₄ test **with controls that can fail** (PP 384096a8 fix 5): max\|dG₄\| ~1e-37 at λ = 1/16, vs 2.5e-3–0.21 at λ = 0 and ~1e-8 at λ(1+1e-6), for all four candidates at 2 points. Evidence only; no .md, no status change |
| 18:17:29 | reports/MR2_…_MN2_SYMBOLIC_REDUCED.py | 3cfbe7da8726048f330f6eaec72e6aa11b11ce42fad8552f0c2c821a3f5e7a59 | MATCH | script for the MN2 exact symbolic Einstein check (PP fix 7). **No result log or .md yet**; all-points Einstein stays CONDITIONAL |
| 18:17:53 / 18:17:56 | reports/evidence_local_bridgeC_resolution_2026-11-09/part4_gamma0_140_weil_e0.py / .log | 99eb4f78c42c57f3dd8b3f27e15880931bd9ab0a9c44036bf2512064a9d7e2b6 / 651f115a970aa2049959ea5b9b92807cf299be1bc32d9c2c6501c3057cf6a271 | MATCH / MATCH | evidence for B item 4a |
| 18:21:07 | sidecars for part1/part3_*/part4 evidence | — | all MATCH | sidecars added at 18:21 (none existed at the parent cutoff) |
- /workspace/539-labs/: **no files** after 18:16.
- **No new Owner write** after c7795d6e (18:16).
- **No new PP .md audit** after fe0c3d92 / 384096a8.
- Outside the two trees (scratch only, mtime 18:16–18:20; not records, not graded):
  - /workspace/audit-scratch/pp_1813_audit/ (y16.py, y16_rerun.log) and pp_1818_audit/ (autcheck rerun): a PP audit of Y16 and of erratum 13 appears to be **in progress**.
  - /workspace/pp_wall_1820/ (PP wall/N_req scripts).
  - /workspace/scratch/mr2_1750/ (sym_mn2.py, symred_MN2.log).
  - /workspace/nl-junction-1817/: C's scripts, sidecars MATCH.

## 3. Parent NOT FOUND items: what changed
| parent NOT FOUND item | now |
|---|---|
| ce4d9e80 fix | **FOUND**: A (c2e9b6fe…) |
| Local FINDINGS after 15:20 | **FOUND**: B (9e34f2dc…) |
| citation re-check under 36683379 | **FOUND (partial)**: C (b5190ea8…) + D (a4084322…); math partly checked; not PP-audited |
| PP audit of NL Y16 (7270a6b3) | **still NOT FOUND** (scratch suggests in progress) |
| MR2 symbolic/global-curvature .md | **still NOT FOUND**; new .log (604aa979…) and .py (3cfbe7da…) only |
| separate MR2 "ERRATUM2" to 9ab8f0a6 | still NOT FOUND |
| t4371 text | still NOT FOUND (relayed only) |
| RTA v18 draft | still NOT FOUND (only the safe outline e18d8fea) |

## 4. Net effect on the parent report
- Bridge C stays PARTIAL. Two Local items move up on Local's own labels: Item 2 → PROVED, and χ₁₄₀ on Γ₀(140) → PROVED (computer-assisted). Weight 3/2 → PARTIAL. All of these await a PP audit.
- Junction: unchanged (UNSOLVED). Y14 and Y15 OPEN. Y16 not yet audited by PP.
- Vacuum: MN N=2 CONDITIONAL, unchanged. The dG₄ control now discriminates, but this is evidence only.
- Citations: no upgrades by citation (rule respected).
- v18 blockers (parent §7): unchanged except item 7, which is now "filed, pending PP".
- New custody flags: **B-1** (two evidence files missing from disk) and **C-1** (swapped script names).
- MISMATCH: none in this window.
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, verified before and after writing. Parent report, PDF, sidecars, v16 and v17 untouched.
