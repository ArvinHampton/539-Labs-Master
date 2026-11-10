# AUDITOR — Corpus crawl batch 07 — dependency closure for open conditionals — 2026-11-09

Role: Auditor. Reports only. Written 2026-11-09 ~13:00 CST (America/Chicago).
Authority: Owner "All haults lifted" (chat 12:34 CST 2026-11-09, id pt1864u). Limits kept: new file with exclusive create only; no frozen or hashed record edited; no sidecars created; no CERT; no Gemini; no external sends; no verdict changed; no physics invented. Probes ran only in /tmp/aud06 scratch.
Tip residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91: MATCH before writing.
Labels: PROVED / CONDITIONAL / OPEN / REFUTED-by-proof. Pure-math standard applies.
D := oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/ (identical copies are in self-audit/repo and in _git_v8_unpushed_clone).

## 1. Custody
| Tag | File | sha256 | Sidecar | mtime (CST) | Stated date |
|---|---|---|---|---|---|
| RPC | D/Residual_Product_Complex.md | f155466edf9858cf58dcbd28aae658bf7b621e29c1871ce6a1593cfb9605cb98 | NONE | 11-06 14:37 | — |
| Q | D/Residual_Product_Cohomology.md | 900ffa219417d0b67253f137ba46c4b733c1a5c57e96c3e1debf7f6e6bf9848b | NONE | 11-06 14:37 | — |
| TCF | D/Thin_Complex_Formality.md | 325002c4cc5f08c43771c92fb44b7c38d377a242c3a0d45f98c32c56bde939ad | NONE | 11-06 14:37 | — |
| FSS | D/Residual_Form_Spectral_Sequences.md (cited by TCF) | acf0281c15538a30e95fdd147a57c9f57103b447b4089b93432a4178eb00b15f | NONE | 11-06 14:37 | — |
| MPS | D/Mechanics_Principle_S_Residual_Flux_Provenance_Vertex_Edge_2026-08-12.md | 14bd7b97c8cd8f4146297a8f59dd124ee906e47b79a99b58efc99d1628ae0db2 | NONE | 11-06 14:37 | 2026-08-12 |
| LB | D/L_body_Structural_Derivation.md | c7933f6601394b156ec2c4a9b015fb3e1a36efd8507b5641acb5ffc1519ff4ae | NONE | 11-06 14:37 | — |
| RPP | reports/crypto/RPP_formal_statement/RPP_formal_statement.md | 173c2c6661792613298011d7be1442b1db9fe88c7401914b8e3a277d65177dac | NONE | 11-06 14:38 | — |
| NL-I | reports/FINDINGS_NL_BH_PROOF_GAP_INVENTORY_2026-11-05.md | b2581c1a21464f7e1e23bb617f63f017db5f28d63722bd60b539554adea39ea8 | MATCH | 11-06 14:40 | 11-05 13:21 |
| NL-P | reports/FINDINGS_NL_BH_EXISTING_PADIC_GRAVITY_DEFINITIONS_2026-11-05.md | a520db709bdb5a39ef0cb2b9c246bbe73425d91f90cb1722aae69f4847a64f68 | MATCH | 11-06 14:40 | 11-05 13:30 |
All mtimes come from the Nov 6 bulk copy and carry no provenance weight. The six Axiomatic-Book and RPP files have no sidecar (extends B6-1).

## 2. Arithmetic chain (f_max, B′, L_body)
- LB :19–22, :51–57: N_flux = ⌊e³·3⁵⌋ = 4880. N_tow = 243. The democratic multiset {21×20, 20×223} is unique for range ≤ 1. f_max = ⌈4880/243⌉ = 21 → **PROVED** (re-computed).
- LB :65–76: B_Q = 4880//9 = 542, remainder 2 → PROVED.
- LB :102–140 and MPS :42–54: Principle (S), "clear one max-tower seed", selects B_Q − f_max = 521. Both files call (S) an extra combination rule that is not forced by Axiom 0 or by democracy → **definition/adopted principle**. The Auditor makes no verdict on its physics.
- LB :168–189: uniqueness of (S) within {f_min, f_max} → PROVED, given that it is relative to the declared class.
- LB :223–272 and MPS :88–96: B′ = ⌊4859/9⌋ = 539 → PROVED. The equivalence L_pref + B_Q − f_max = B′ ⇔ L_pref = f_max + ⌊(r − f_max)/9⌋ → PROVED. It holds at (4880, 21, 2) because 18 = 21 − 3. The heading word "identity" means equality at these values only; the body states this correctly.
- MPS :155–183: W = ⌊e³/ln 3⌋ = 18 vertices, 17 window edges, tower edges {17..537} = 521, and 17 + 521 = 538 = B′ − 1 → PROVED.
- MPS :51: "ACE depth N⋆ = 14", from the No-Go doc (not crawled) → OPEN. This is a third candidate source for DT's "~14 layers" (B6-4).

## 3. The G17 / H² / D₁ dependency, settled
Definitions (Q :135–153, RPC :59–80): G = span{1, f | h_α, v_δ, h_αf | t_ω, s, t_ωf | ω₂⊗δf}, with t_μ = −B′t_ω on ordered triples. The true product differential gives Df = v_δ, Dh_α = t_ω, Dh_αf = t_ωf − s, **Ds = Dt_ωf = ω₂⊗δf** (RPC :130–146; Q :156; FSS :163–167 diagram).
Exact computation on the probe's core-0 data in /tmp: f is nonconstant, with 241 of 538 δf values nonzero. ω₂⊗δf ≠ 0 on 20244 of 45192 prisms. Dη = 0 on all prisms. rank{t_ω, s, t_ωf} = 3.

Results:
1. Q's F is G with D|F² := 0, i.e. F = G/G³, a legitimate quotient complex. TCF :97–101 says this outright: D(α⊗δf) = ω₂⊗δf "then set to boundary/0 under thin residual closure". H⁰(F) = ℚ, H¹(F) = 0, H²(F) = ℚ·[s] → **PROVED**. The **exact condition** is that f is nonconstant on P_B′. That is verified from the locked loads and f_max = 21; if f were constant, H²(F) = 0. B6-5 is CLOSED.
2. The honest closed complex G has H⁰ = ℚ and H¹ = H² = H³ = 0. H²(F) ≅ ℚ is exactly the connecting-map image of the deleted class ω₂⊗δf (LES of 0 → G³ → G → F → 0). Any reading of [s_αδ] as a cohomology class of C•(X×), or of G → **REFUTED-by-proof**: s is not a D-cocycle.
3. Q :151–153, "all listed 2-generators are cocycles", true for D only in the quotient. It is false for s and t_ωf under the product D, so it is inconsistent with Q :156 → REFUTED-by-proof as worded (B7-1).
4. RPC :107, "Nontrivial mixed class η" → REFUTED-by-proof. η = −D(h_αf) is exact, and Q :70 and TCF itself concede this. RPC's "Theorem Dη = 0" and the prism check :150–158 → PROVED.
5. TCF §1.1 :51–60 lists degree-0 = {1} only, with 1⊗δf closed. As written, that presentation gives H¹ = ℚ[1⊗δf] ≠ 0, which contradicts TCF :103–113. FSS §4 (no 1⊗f, with (2,1) present) gives H¹ = ℚ and H² = 0. Both are repaired by Q's presentation, which includes f in degree 0 and truncates. Presentation errors → REFUTED-by-proof as written (B7-2); the Lock is unaffected.
6. Formality F ≃ ℚ[0] ⊕ ℚ[−2] → PROVED (Lemma A, field splitting). TCF Cor. 3, Massey products vanishing for degree reasons → PROVED. thin_formality_probe.py :156 hard-codes chain_map=True and never computes D on degree 2 (B7-3).

## 4. NL A4 and the NL inventories
- RPP §1.4 items 1–4 → **PROVED**. Re-checked: the preimage rule for y < 3000; itinerary bijection plus the affine form T3^L(3^L q + r) = A_e q + C_e, exhaustive for L ≤ 8; the induction proof is valid. Item 5's −0.585 bits = log₂(2/3) is arithmetic; the orbit statement is labelled heuristic, consistent with B6-4. Item 6 is reproduced (300/300 256-bit seeds reach {1,2} in 539 steps; 0/300 510-bit seeds do).
- NL-I: Haar ∫_{ℤ₃⁴}|x|^{ν−1} = (1−3⁻⁴)/(1−3^{−(ν+3)}) and genus X₀(31) = 2 → PROVED (re-checked). Gaps 1–6 → OPEN (definitions absent). The scope disclaimer is correct.
- NL-P: the S1–S4 summaries were not re-fetched → citation accuracy OPEN. Gap 1 REMAINING is consistent.

## 5. Updated conditionals
| Item | Status | On exactly what |
|---|---|---|
| G17 / RTA P10 / D₁ rank-1, Lock :8 | **PROVED** | F := Q's truncation (D|F² = 0) and f nonconstant, which is verified. The "class of X×" reading is REFUTED. |
| B6-5 | CLOSED | Above |
| G18 / RTA P11 (S_eff) | PROVED (definitional) | B′ = 539 arithmetic under adopted (S) |
| f_max = 21 | PROVED | Forced |
| NL A4 | PROVED | — |
| NL B1 | CONDITIONAL | Unchanged (normalization hypothesis) |
| B6-4 Lyapunov / "~14" | CONDITIONAL / OPEN | Heuristic; three candidate sources |
| Layer S acyclic | CONDITIONAL | Not re-checked |

## 6. New blockers
- B7-1: Q :151–153 vs :156 (Owner erratum wording).
- B7-2: TCF §1.1 and FSS §4 presentation errors.
- B7-3: Probes assert D|F² = 0 without computing it.
- B7-4: 6 batch-07 files have no sidecar.

Next: batch 08 (owner-20261105 intake folders). Tip re-hash after writing: see the digest.
