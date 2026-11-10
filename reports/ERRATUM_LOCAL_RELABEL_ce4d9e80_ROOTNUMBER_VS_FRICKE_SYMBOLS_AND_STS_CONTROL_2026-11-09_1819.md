# ERRATUM (Local-derived): symbol fixes for RELABEL ce4d9e80 (root number ε vs Fricke eigenvalue w), and the §2 control-element name, 2026-11-09 ~18:19 CST (America/Chicago)

- **Authority:** Owner voice 17:30 CST, OWNER_WRITE_VOICE_9c8fa1db_t4358_PURSUE_ALL_OPEN_ITEMS_TO_RESOLUTION_ALL_BOTS_2026-11-09_1730.md (sha ff8a1670…), item 4 ("including the ce4d9e80 symbol fix").
- **Target (not edited):** RELABEL_LOCAL_XI_WEIL_CARRIER_PP_AUDIT_1525_2026-11-09.md, sha ce4d9e800f4d3b75…. Cross-referenced parent (not edited): FINDINGS_LOCAL_DERIVE_XI_WEIL_VECTOR_CARRIER_FRICKE_PLUS1_DICTIONARY_2026-11-09.md, sha ae951f3e7aa5be4b… ("XW").
- **Flag source:** PP 5cbd050a (FINDINGS_PP_AUDIT_NL_JUNCTION_AND_XI_FRICKE_2026-11-09_1702.md), L70: "Local's RELABEL file ce4d9e80 (L33–36) repeats it citing PP. Its wording "ε = −w = +1" swaps the symbols; the value is right (w_N = −ε = +1)." and X2 (L76): project convention ε = (−1)^{k/2} w_N.
- **Ξ (Owner, OW 7b5a725b, 17:03):** Ξ := the curve 49a1 ⊗ χ₁₄₀.
- Additive file. Tip 7cddb188… untouched (sha checked before and after). No CERT. Nothing sent outside. No Gemini. Pure math only.
- **Evidence:** evidence_local_bridgeC_resolution_2026-11-09/part1_twist_newform.py and .log (PARI 2.17.2 via cypari2, local), each with a .sha256 sidecar.

## 1. Convention (stated once, used everywhere below)
- **ε(E)** := the global root number of E/ℚ (PARI `ellrootno`): Λ(E, 2−s) = ε·Λ(E, s).
- **w_N(f)** := the Fricke (Atkin–Lehner, full level) eigenvalue of the weight-2 newform f of level N: f|₂W_N = w_N·f, with W_N = (0, −1; N, 0).
- **Identity (weight 2):** ε = (−1)^{k/2}·w_N = **−w_N**. Equivalently **w_N = −ε**.
- So "Fricke +1" ⇔ "root number −1", and "Fricke −1" ⇔ "root number +1".

## 2. Corrected lines in ce4d9e80
| Line | As written | Corrected | Value change |
|---|---|---|---|
| L36 | "Hence the Fricke eigenvalue of the twisted newform is ε = −w = **+1**." | "Hence the Fricke eigenvalue of the twisted newform is **w₁₉₆₀₀ = −ε = +1** (root number ε = −1)." | none |
| L25 | "Control: (1,0;−1,1) = S⁻¹T⁻¹S-type conjugate in SL₂(ℤ) gives \|tr\| = √140" | "Control: (1,0;−1,1) = **STS⁻¹**, a conjugate of T in SL₂(ℤ), gives \|tr\| = √140" | none |

- **L25 check (PARI, part1 log):** with S = (0,−1;1,0), T = (1,1;0,1): S·T·S⁻¹ = [1,0;−1,1] ✓, while S⁻¹·T⁻¹·S = [1,0;1,1] ✗. The trace modulus √140 is unchanged because STS⁻¹ is conjugate to T.

## 3. Same symbol swap in the parent XW (ae951f3e), recorded here, not edited
In XW, "ε" was used for the Fricke/Atkin–Lehner eigenvalue. Values are right; only the symbol is wrong under §1.
| XW line | As written | Corrected reading |
|---|---|---|
| L68 | "ε(f⊗χ) = ε(f)·χ(−N)" (Atkin–Li) | **w(f⊗χ) = w(f)·χ(−N)** (χ quadratic, conductor prime to N; Atkin–Li, Invent. Math. 48 (1978)) |
| L69 | "ε(f⊗χ₋₂₀) = (−1)·χ₋₂₀(−49) = (−1)(−1) = +1, equivalently root number −1" | **w₁₉₆₀₀(f⊗χ₋₂₀) = w₄₉(f)·χ₋₂₀(−49) = (−1)(−1) = +1**, equivalently root number ε = −1 |
| L97 | "49a1 with ε = −1" | "49a1 with **w₄₉ = −1** (root number ε = +1)" |
- The carry-forward 60778d10 (L9, "root number −1, so the Fricke sign is +1") already uses the convention correctly. No change.

## 4. Local re-verification (PARI, exact; part1 log)
| Curve | a-invariants | Conductor | ε (ellrootno) | w_N = −ε | j |
|---|---|---|---|---|---|
| 49a1 | [1,−1,0,−2,−1] | 49 | +1 | −1 | −3375 |
| Ξ = 49a1⊗χ₁₄₀ (`elltwist(E,140)`) | [0,−105,0,−39200,−2744000] | 19600 | −1 | **+1** | −3375 |
| 49a1⊗χ₋₂₀ (`elltwist(E,−20)`) | [0,15,0,−800,8000] | 19600 | −1 | +1 | −3375 |
| 49a1⊗χ₋₇ | [−1,5,0,−98,343] | 49 | +1 | −1 | −3375 |

- **Isogeny (PROVED, Local-verified):** `ellisomat(Ξ)` gives an isogeny class of size 4 with degree matrix [1,2,7,14; 2,1,14,7; 7,14,1,2; 14,7,2,1]. `ellisisom` identifies Ξ with class member 1 and the −20 twist with class member 3. So **Ξ and the −20 twist are 7-isogenous**. They are not isomorphic (`ellisisom` = 0), matching PP X3.
- **Same newform (PROVED, Sturm):** a_n(Ξ) = a_n(−20 twist) for **all n ≤ 7000**. The Sturm bound for weight 2 on Γ₀(19600) is ⌊(2/12)·40320⌋+1 = 6721.
  - a_n(Ξ) = χ₁₄₀(n)·a_n(49a1) = χ₋₂₀(n)·a_n(49a1) for all n ≤ 7000.
  - χ₁₄₀ = χ₋₂₀·χ₋₇ (checked n ≤ 1000).
  - a_n = χ₋₇(n)a_n holds for 49a1 and for Ξ (CM by ℚ(√−7)).
- **L-function:** `lfuncheckfeq`(Ξ) = −135 bits (functional equation holds). `lfunrootres` root number = −1. Analytic rank 1, with L′(Ξ,1) = 4.4326227316864…. For 49a1: analytic rank 0, L(1) = 0.9666558528….
- **Not available:** `ellidentify` (no local elldata package). Cremona/LMFDB labels were not looked up; nothing was computed through web services.

## 5. Effect on counts
- No label changes. ce4d9e80's rollup (PROVED 13 · CONDITIONAL 2 · OPEN 4 · REFUTED 1) and XW's values stand. The fixes are notational, 2 lines in ce4d9e80 plus 3 cross-reference lines in XW.
- New Local-verified facts: Ξ ~ (−20 twist) by a **7-isogeny**, same newform up to n ≤ 7000 > Sturm. PROVED.

Local-derived. For PP audit. Tip untouched. No CERT.
