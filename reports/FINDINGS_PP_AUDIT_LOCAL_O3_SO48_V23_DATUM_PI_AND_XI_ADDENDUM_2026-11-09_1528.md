# FINDINGS — PP audit of Local O3 (SO₄₈ / v=23 datum match, Codex π adopted) + rollup erratum + Ξ-carrier citation addendum — 2026-11-09 15:28 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Authority: GO (2) under OW reports/OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md (sha 5a6e7177…, verified earlier). Additive new file; the audited files are unchanged. Tip 7cddb188… untouched. No CERT. Nothing sent outside. No Gemini. Lock 96f8d42e §4 not used.
Scripts/logs: /workspace/audit-scratch/pp_local_o3o5o7_1521/ (o3_checks.py/.log, o5_addendum_checks.py/.log; manifest SCRATCH_MANIFEST.sha256). Literature theorems are used from standard texts; per PP rules each **citation** is tagged CONDITIONAL until pinned (listed in §4). The mathematical arguments below are checked line by line.

## 0. Hashes (sha256 recomputed vs sidecar)
- FINDINGS_LOCAL_SO48_V23_DATUM_MATCH_CODEX_PI_ADOPTED_2026-11-09.md: d2d2d2266c147a171f235b617f8375dd79d183b05786beba7f73fe80e6abc5c8 — **MATCH** (sidecar OK).
- ERRATUM_LOCAL_SO48_V23_DATUM_MATCH_CODEX_PI_ADOPTED_ROLLUP_2026-11-09.md: cf86d913fcbc8200b6c182b60e2f2df19afb2a6b34826ce1e5c31e0b59570825 — **MATCH**.
- ADDENDUM_LOCAL_XI_WEIL_CARRIER_CITE_MR1_AMEND_2026-11-09.md: ed63348d5f65408239311436c5e76109be1d5d278de75ccb4e630ed5b6bd8ad7 — **MATCH** (sidecar holds the bare hash without filename; content matches).
- Cited MR1-AM FINDINGS_MR1_B_SEC3_APPELL_RC_S2_S4_AMEND_PP_AUDIT_2026-11-09.md: 0ea030aee260983add0c3e9f14b79a4a814f8e1b8a7c75ae2b43e2f76d4ed0fa — **MATCH**.
- **Hash-custody question (16813caf vs 6813caf): Local is right.** FINDINGS_PP_SOFTSF_AUDIT_LOCAL_INVARIANT_SPLIT_FORM_QU140_SO48_2026-11-09_1305.md has sha256 16813cafa6daea78323cf28f0e58ef1af383c409e0cbc83d56e81a2d50fce759 (recomputed = sidecar; Auditor manifests AUDITOR_ADVANCEMENTS_SINCE_RTA_V17 :54 and CORPUS_CRAWL_BATCH14b :56 agree). No .sha256 sidecar in reports/ begins with 6813caf; every "6813caf" occurrence in reports/ is a substring of 16813caf. "6813caf…" was a dropped leading digit. **PROVED (by grep + recompute).**

## 1. Item-by-item audit of d2d2d226
1. **π₂₃ trivial — PROVED, CONFIRM.** ρ(D₂₄) = (23,…,1,0); trivial rep is K-spherical with Satake parameter q^{±ρ}, and q^{ρ} ~ q^{−ρ} under W(D₂₄) because the 0 entry lets any sign change be made even. Codex y_i = 23^{24−i} is q^{ρ}.
   - Sign note — **PROVED, CONFIRM**, and provable directly: on the split torus t = diag(t₁..t₂₄, t₂₄⁻¹..t₁⁻¹), θ(t) = ∏t_i mod squares (each hyperbolic-plane factor diag(t,t⁻¹) is a product of two reflections with spinor norm t). So the unramified χ∘θ with χ(23) = −1 multiplies every Satake coordinate by −1; −q^{ρ} is not in W·q^{ρ} (W does not change signs of coordinates). No extra citation needed.
2. **23 unramified — PROVED, CONFIRM.** (35/23) = +1, (−7/23) = +1 (computed); 49·140·48 ≡ 12 (mod 23). K₂₃ hyperspecial rests on LD-1 (adopted, PP-confirmed 16813caf).
3. **π one-dimensional, π = χ∘θ — PROVED, CONFIRM** (argument correct; citation tag: strong approximation). Hypotheses checked against the correct statement: Spin(V) is simply connected and absolutely almost simple (D₂₄, dim 48 ≥ 3); S = {23} with Spin(ℚ₂₃) non-compact (V⊗ℚ₂₃ split, hence isotropic) ⇒ Spin(ℚ)Spin(ℚ₂₃) dense in Spin(𝔸). The step "f left Spin(ℚ)-, right Spin(ℚ₂₃)-invariant, continuous ⇒ constant" is correct, and π₂₃ = 1 does mean G(ℚ₂₃) acts trivially on the space of π. Two steps Local leaves implicit, both true:
   - (a) H := image of Spin(𝔸) is normal in G(𝔸) and G(𝔸)/H embeds in ∏′ℚ_v^×/(ℚ_v^×)² via θ, because Spin(F)→SO(F)→F^×/F^{×2} is exact at SO(F) for every field F (from 1→μ₂→Spin→SO→1); so ker θ_v = image of Spin(ℚ_v), including v = ∞.
   - (b) θ(G(ℚ)) = ℚ^×/ℚ^{×2} because V ⊃ H represents every c ∈ ℚ^×, so θ(τ_{v}τ_{w}) = Q(v)Q(w) ranges over all classes. Hence χ is trivial on ℚ^×: a quadratic (order ≤ 2) Hecke character; θ surjective at 23 forces χ₂₃ = 1.
   - Irreducible π of the abelian quotient is a character (Schur for admissible reps; at ∞ the Lie algebra acts by 0 since H contains the image of Spin(ℝ)). 
   - **Minor precision (no label change):** the parenthetical "item 3 also applies to SO(Γ₄₈⊗ℚ)" is right for one-dimensionality, but there θ(G(ℚ)) = ℚ_{>0}^×/squares (definite form), so χ is only forced trivial on positive rationals.
4. **Trivial character automorphic, residual — PROVED, CONFIRM** (citation tag: Borel–Harish-Chandra finite volume).
5. **π away from 23 — OPEN, CONFIRM.** LD-O3a is a Local-derived proposal; Owner's call.
6. **Λ(s,π) — CONDITIONAL on LD-O3a/LD-O3b, CONFIRM.** Std eigenvalues of the principal parameter p^{±23..±1},1,1 ⇒ L = ζ(s)²∏ζ(s∓i) and Λ = ξ(s)²∏ξ(s−i)ξ(s+i). Functional equation PROVED. Pole bookkeeping recomputed: poles exactly at the 48 integers −23..24, orders 1 at −23, 24; 3 at 0, 1; 2 elsewhere; total **96** (o3_checks.log). No cancellation: ξ has no zeros on ℝ∩ℤ. **Remark:** the "standard identification of spinor-norm twists with central twists" that Local marks CONDITIONAL is provable at unramified places by the torus computation in item 1; the χ ≠ 1 global formula still needs ramified/archimedean local factors, so CONDITIONAL stays correct there.
7. **ω₂₃.**
   - **Identity — PROVED, CONFIRM.** #maximal totally singular subspaces of the split 2n-dim quadratic space over 𝔽_q = ∏_{i=0}^{n−1}(q^i+1) = 2∏_{i=1}^{n−1}(q^i+1): two families of ∏_{i=1}^{n−1}(q^i+1) each. Brute force (n,q) = (2,3),(3,3),(2,5),(2,7),(3,5),(3,2),(4,2): 8, 80, 12, 16, 312, 30, 270, all equal to the formula. For n = 24, q = 23: 2∏_{i=1}^{23}(23^i+1) has **377 digits, 1.436…×10^376**, and equals 2·23^{276}∏_{i=1}^{23}ζ₂₃(i)/ζ₂₃(2i) exactly (Fraction arithmetic; 276 = dim OG(24,48)).
     - **Correction to the task brief (not to Local):** "two components each ∏_{i=0}^{n−1}(q^i+1)" is wrong; each component has ∏_{i=1}^{n−1}(q^i+1) and the total is ∏_{i=0}^{n−1}. Local's statement is the correct one.
   - **LD-O3c normalization — CONDITIONAL, CONFIRM** (Local-derived proposal; Owner adoption pending).
   - **Siegel-density reading — REFUTED, CONFIRM by recomputation.** α₂₃(L,L) = 2(1−23^{−24})∏_{i=1}^{23}(1−23^{−2i}) = **1.99621213…**, α⁻¹ = **0.50094876…** ≠ 2∏(23^i+1). This equals |O⁺₄₈(𝔽₂₃)|/23^{dim O}, and the refutation holds in every standard normalization (all are within a factor 2 of 1 against a target ~10^376). **Is #OG a local-density inverse?** No. #OG = [O(𝔽₂₃) : P_S(𝔽₂₃)], a flag-variety point count = q^{dim OG}·(ratio of reduced densities of O and P_S). It is not the inverse of α₂₃(L,L) in any convention.
8. **Consistency with LD-1 — PROVED, CONFIRM.** (b) can be strengthened and made unconditional: A ⊂ G(ℚ), and for any χ∘θ, π(a) = χ(θ(a)) = 1 because θ(a) ∈ ℚ^× and χ is trivial on ℚ^×. So π|_A = 1 does not need LD-O3a.
9. **REFUTED (stays), CONFIRM.** Isometric over every ℚ_p (even unimodular, rank 48, disc 1; at p = 2 even unimodular ℤ₂-lattices are classified by rank and discriminant), not over ℝ. Shorter argument: SO(24,24)(ℝ) is non-compact and SO(48)(ℝ) is compact, so the ℚ-groups are not isomorphic.
10. **HOLD (α undefined) — CONFIRM.** Carried items 11 (θ₁ REFUTED; others OPEN) are not re-audited here.

**Erratum cf86d913:** the corrected tally (PROVED 7 / CONDITIONAL 2 / OPEN 1 new / REFUTED 2 / HOLD 1) matches the item labels. CONFIRM. No math change.

## 2. Addendum ed63348d (Ξ-carrier citations to MR1-AM) — ACCURATE
- Line references into MR1-AM all check: R1 at :9, :25; R2 at :10, :26; S2a at :11, :27; S3b at :12–14, :31; Weil(140) tie at :19, :37. The S3b quote is verbatim from :31. The original MR1 :26 is the Weil(140) sentence.
- The MR1 line numbers cited inside ae951f3e (MR1:22 R1, MR1:24–25 R2, MR1:42 S4c) are correct. ae951f3e cites MR1:25 at its lines 26 and 84, both covered by ":24–25". MR1:42 (√(7/8)/√10 normalization OPEN) agrees with MR1-AM S4c OPEN.
- Numerics recomputed (mpmath, 50 digits): the finite formula gives L(1,χ₁₄₀) = 0.8376792812588585…; h = L√140/(2Reg) = 2.0 (exact finite formula, so h = 2 is forced); √(7/8)·L = Reg/√10 = 0.78357721761742351124 = Λ₀. No norm −1 unit (x² ≢ −1 mod 7). **PROVED, CONFIRM.**
- **Wording nit (no label effect):** "MR1-AM's R1/R2 supersede the basis of :22" is too strong for R1. MR1-AM marks R1 "PROVED (unchanged)"; only the PARI certificate was added. R2's basis did change.
- Rollup "no change: 12/1/3/1" for ae951f3e — consistent, since no ae951f3e item relied on S2a, S3b or the REMARK. (ae951f3e itself is audited separately.)

## 3. PP rollup (this file)
- d2d2d226 items 1, 1-sign, 2, 3, 4, 7-identity, 8: **PROVED** (7, all CONFIRM). Item 6: **CONDITIONAL** (CONFIRM; FE and pole orders PROVED given the formula). Item 7 normalization: **CONDITIONAL** (CONFIRM). Item 5: **OPEN** (CONFIRM). Item 9 and the Siegel-density reading: **REFUTED** (CONFIRM). Item 10: HOLD.
- Errors found: none of substance. Three precision notes: item 3's definite-form parenthetical; item 8(b) is unconditional; the brief's #OG per-component formula, not Local's.
- Addendum ed63348d: citations ACCURATE; one wording nit.
- Hash custody: 16813caf is correct.

## 4. Citation tags (CONDITIONAL until pinned; arguments otherwise verified)
Strong approximation (Kneser; Platonov–Rapinchuk, Thm 7.12); Borel–Harish-Chandra; Satake isomorphism; classification of even unimodular ℤ₂-lattices; local mass/density formula for split unimodular forms (Conway–Sloane "standard mass").
No CERT. Tip untouched.
