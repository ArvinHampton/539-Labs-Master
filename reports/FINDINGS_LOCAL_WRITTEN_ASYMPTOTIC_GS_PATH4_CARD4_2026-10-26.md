# FINDINGS — Local Written asymptotic for ĝ_s (s∈{7,8,11}) / Path4 Card4 gate (2026-10-26)

**STATUS**
- Written asymptotic: **LANDED** (cite-only, Soft SF Write-only).
- C1 tolerance: **NAMED = 0.10** relative of leading A/4 (OW `586dbac0d703a10f547277a7e9a61792da0da89c72dac4af1624af7ca117baff` + amend `0b37e98dba7a3a33d0d16fb9bf59abfa01396f7e40c7d7d18540a163f8eeb0af`). **FLAG:** the value was chosen under the Owner's voice delegation (precedent: Bridge C order33 r≤0.10), not spoken as a number by the Owner.
- Package numerics: **NOT AUTHORIZED in this Write.** They become eligible only after this FINDINGS lands; none are run here.
- tip Soft SF LOCK `7cddb188…` tip_touched NO; invent HOLD; Soft SF F3 CLOSED; Bridge PARTIAL READY NO; Card11 tip folds HELD.
- Aligns with Owner pick PR2 openQ **Q1**.

## 1) Authority chain (live sha256sum, all MATCH)

| Doc | sha256 |
|---|---|
| OWNER_WRITE_CARD4_WRITTEN_ASYMPTOTIC_PATH_OPEN_2026-10-26.md | 2469ca26ee07bbf96be8df30ad2d4005b504457e058319f91b1406cf8b0890ae |
| ASSIGN_LOCAL_WRITTEN_ASYMPTOTIC_CARD4_BEGIN_2026-10-26.md | 3129cd3f9985d161fa68b34c8c31085f6f7023ee182e273a01f4236e6f8a6a75 |
| OWNER_WRITE_PR2_OPENQ_Q1_PICK_2026-10-26.md | 97591bcc548fd32c5e66ff69a9dafb593583d0c4e104cfbe7acf969b7dba3ef6 |
| OWNER_WRITE_PURSUE_SIX_LOCAL_NL_2026-10-26.md | 802d923b7147c48171a6b523f17da6000711c8a266f8384277fda1582fd9e53d |
| OWNER_WRITE_LOCAL_ASYMPTOTIC_C1_GATE_CARD4_2026-10-26.md (prior HOLD) | 6298ad2696f19560be92087e4bccae4770ee3dca79a337d261a00e48c75696c2 |
| OWNER_WRITE_ZWEGERS_BH_CONSISTENCY_CHECK_SHEET_LOCKED_2026-10-26.md | 28bf58fb406fb2f3e3ebe8c9727f20d0eb6b5c4d4f046c891de44cfba366c9b3 |
| OWNER_WRITE_D1_D2_DEFS_LOCKED_2026-10-26.md | 6fba77178694a42e1556134323f1c67b1f79c83ca0b9ed4b071dedf200e5a4a2 |
| OWNER_WRITE_CANDIDATE_TRIAL_ZWEGERS_BH_ENTROPY_COUNT_2026-10-26.md | 85beaffa0aefc3d1435a5b3c7912dedc390b8af24baaeea4626e74b3cd538c56 |
| OWNER_WRITE_CANDIDATE_LOCAL_ZWEGERS_BH_TRIAL_OBS_MATCH_RECS_2026-10-26.md | 2d79521ba67b5960e3a697405d6288f93bed2108de89c27f95db1a261f833182 |
| OWNER_WRITE_CANDIDATE_LOCAL_PATH4_SHEET_TBD_REFINE_RECS_2026-10-26.md | 8bed9d12c79bf4c7c2a64c7b7cb38ab1265e3595abfad4ea71f997bec617b52b |
| OWNER_WRITE_LOCAL_ZWEGERS_BH_OBS_MATCH_RECS_LOCKED_2026-10-26.md | e30eb2cbb7cf4c2444df351362d0df0a4a49fc3ffcb163581a2714f319c9f321 |
| FINDINGS_LOCAL_RAMANUJAN_HAMPTON_LANE_MAP_2026-10-26.md | 9910ade24d1c4cdb0f010b728c7b138fc904beb79c423f689889b5b3fc4f1290 |
| FINDINGS_PR2_RH_PHYSICAL_LOAD_OPENQ_2026-10-26.md | 26ec0bac09184eb55733584d62cc016170ca707835fec4ba1fb1b8aa834e8ca1 |
| OWNER_WRITE_CARD4_C1_TOLERANCE_NAMED_DELEGATED_2026-10-26.md | 586dbac0d703a10f547277a7e9a61792da0da89c72dac4af1624af7ca117baff |
| OWNER_WRITE_CARD4_C1_FILLED_AMENDS_ASYMPTOTIC_PATH_2026-10-26.md | 0b37e98dba7a3a33d0d16fb9bf59abfa01396f7e40c7d7d18540a163f8eeb0af |
| tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` (before Write) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |

## 2) Written asymptotic statement

**Corpus grounding.** Trial Step A proposes that the leading asymptotic of the completed count reproduces S = A/4 + ⋯, and labels this "to be tested," not Category A. D2 fixes the residual series g_s and its Zwegers completion ĝ_s = g_s + (nonholomorphic correction), for s∈{7,8,11}. Path4 C1 compares the "leading asymptotic of ĝ_s coefficient growth vs A/4." RECS H1 notes that the coefficients of weight-½ mock theta functions grow like exp(c√n). All of this is residual-packaging language only.

**Literature class (cited, not derived here).**
- Rademacher-type exact formulas and circle-method asymptotics for mock theta coefficients: G. E. Andrews, "On the theorems of Watson and Dragonette for Ramanujan's mock theta functions," *Amer. J. Math.* 88 (1966); L. A. Dragonette, "Some asymptotic formulae for the mock theta series of Ramanujan," *Trans. AMS* 72 (1952).
- Exact formulas via harmonic Maass forms: K. Bringmann and K. Ono, "The f(q) mock theta function conjecture and partition ranks," *Invent. Math.* 165 (2006); K. Bringmann and J. Manschot, "Asymptotic formulas for coefficients of inverse theta functions," *Commun. Number Theory Phys.* 10 (2016).
- Completion framework: S. Zwegers, *Mock Theta Functions*, PhD thesis, Utrecht (2002); D. Zagier, "Ramanujan's mock theta functions and their applications [after Zwegers and Bringmann–Ono]," Sém. Bourbaki 986 (2007).
- Black-hole and mock-modular link (context only): A. Dabholkar, S. Murthy and D. Zagier, "Quantum black holes, wall crossing and mock modular forms," arXiv:1208.4074 (2012).

**Statement (growth class).** Suppose the holomorphic part g_s has a weight-½ mock modular completion ĝ_s with nonzero principal part. Then the cited Rademacher and circle-method results give coefficients with leading behavior
a_s(n) ∼ A_s · n^{α} · exp(β_s √n),  n → ∞.
Here β_s > 0 is set by the principal-part (polar) order and the level, and α and A_s come from the weight and the Kloosterman-type leading constant. The leading log-growth is therefore log a_s(n) ∼ β_s √n. This FINDINGS states the class only. It does **not** assign numerical values to β_s, α, or A_s for s∈{7,8,11}, and it does not write any Fourier coefficients.

**C1 map.** C1 identifies the leading term L_ĝs = β_s√n (in the Path4/D1 normalization) with the D1 Bekenstein–Hawking target A/4. The test passes if |L_ĝs − A/4| / (A/4) ≤ 0.10 when A/4 ≠ 0. No claim of Category A, READY YES, or Bridge YES is made.

## 3) LANDED vs ABSENT

| Item | State |
|---|---|
| Written asymptotic class for ĝ_s coefficients, with literature and corpus bind to C1 | LANDED (this file) |
| C1 tolerance | NAMED = 0.10 (delegated; see FLAG) |
| Numerical β_s / A_s / α for s∈{7,8,11} | ABSENT (not invented) |
| Package numerics, physical-load match, tip fold | NOT RUN |

## 4) Q1 answer
The asymptotic half lands in this FINDINGS (path and sha in the sidecar). The C1 half is 0.10 under OW 586dbac0… and amend 0b37e98d…. Both halves are now filled.

## 5) Constraints / non-claims
- invent HOLD stands for tip Soft SF, Card4, and Local tip.
- Local stays OFF the QM wt-½ track (`42835129cda899f587759f84f1db8f3b32ee08c76cfb605a38e1a87236583ebc` stands).
- Residual-packaging language only. Path 8 exclusion STANDS.
- No microstate claim and no confirmation of the 1/4 factor (C3 lock).
- SUSY-extremal black-hole counts ≠ astrophysical Kerr; any match is consistency only.
- Soft SF CONFIRM Write-only is owed to the Auditor.
- tip_touched NO: tip sha before = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, after = (same; verified after writing).

## 6) Next
NL may run the C1–C3 physical-load checks under Path4, using C1 = 0.10, once the Owner or Auditor accepts this landing. Local stays cite-only. Eigen, CRT, and W1 are untouched.
