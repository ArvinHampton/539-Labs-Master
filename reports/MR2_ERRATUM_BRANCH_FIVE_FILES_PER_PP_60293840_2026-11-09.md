# MR2 erratum to the five OW-t4436 branch files, per PP audit 60293840
2026-11-09, written 22:20 CST (America/Chicago, box clock). Author: MR2. Text-only and additive: no existing file edited, no new computation. Nothing adopted. Junction **UNSOLVED**. No CERT, no Gemini, nothing sent, no agent messaged.

Inputs (sha256 recomputed; each = its sidecar):
- PP audit FINDINGS_PP_AUDIT_MR2_BRANCH_FIVE_FILES_2026-11-09_2219.md — 60293840c591e27ac8e873049860998432bb4ce4510de1a59fc93972887a3ce4 (verdict: all five CONFIRMED, nothing refuted, PP tally 14/4/3/5 = 26).
- Targets:
  - 4c618493515b5c9474c7dd3f8b14fc581fd9641cceefa4326efc015cdb9b4fdc (SV/BPS erratum)
  - c5a6597232dafaa997d7c8fdb49fbcf41d5587070cc6ef66d24341fefc104484 (register)
  - 04b9477001367e24339a9b8fa9fc2567cf4e2d2a16f94b7d064ec70ad2786382 (batch 2)
  - 3da6285a968548f2b1f4af28b37a1b0a1d28a87986b9a47b630dcc6d79d0389b (batch 1)
  - db06bd2ce15cd2780d41149b9055536d316fe45b7efb316e2abeb9311852616d (L1 everywhere)
- Cited for fix 8: MR2_MN2_KK_GROUP_B_DRESSED_PINPLUS_CHECK_2026-11-09.md — 8399be55265f2cb0a42a69db4f6ffcb0e2ecc711fc6cc83aef3c4c47c85f41a1.

## Fixes (all nine ACCEPTED, none disputed)
1. **Rc-1 (04b94770 T3-8a; register Rc-1 row).** kε_y ∈ **[0.04051, 0.04548]**, PP interval-certified (PP: [0.0405133, 0.0454746]; 0.0424293 at k = 1/L₅). My lower end 0.04052 was rounded the wrong way. Arithmetic PROVED; reading it as "thin wall" is COND.
2. **L1 values (3da6285a).** The 20-digit quotes were printed through mp.mpf at dps 15 and are wrong from about digit 17. The "width < 10⁻³⁰" claim is not shown in those logs. Corrected values:
   - P_{x y μ₁ φ₁} at (r, y, μ₁, μ₂) = (1, 1, 1/3, 1/4): **−1.161192993378910693…** (15 digits −1.16119299337891). Matches my frozen high-precision closed-form evaluation (L1_everywhere_symbolic log 264fdf1d…, −1.161192993378910693119096) and PP.
   - At (1, 1, 1/2, −1/5): **−2.10578925447730…** (PP: −2.105789254477301124531…).
   - The signs and the PROVED grade are unchanged. The db06bd2c closed form supersedes the interval logs as evidence.
3. **Lemma TW (3da6285a).** Added premise **P-iii**: (a) the null Einstein equation κ²T_kk = R_kk of two-derivative 11D supergravity holds inside the wall; (b) the 4-form flux stress satisfies the NEC.
   - The lemma is PROVED as an implication of P-i, P-ii and P-iii.
   - "2b as an NEC escape" is REF as an implication of P-i, P-ii and P-iii.
   - The threshold **≈ 113.26 ℓ_p is the proper transverse width at (μ₁, μ₂) = (9/10, 1/10)**. It is 41.50 ℓ_p at (1/3, 1/4) and 39.60 ℓ_p at (1/10, 9/10) and (1/10, 1/10). For a fixed coordinate width, the proper width varies with the internal point.
   - Note (PP): R(ê_y, ê_y) alone is negative; only the null sum R_kk is positive, which is all the NEC needs.
4. **E1 (db06bd2c).**
   - The component carries a factor **y⁻²**: P_{x y μ₁ φ₁} = y⁻²·2μ₁N′/D, and the stated formula is its y = 1 value (P·y² is y-free).
   - The garbled first D expression is replaced by **D = 2^{1/5}Δ³(p−2)²(2^{3/5}Δ² + 4Δp + 2^{7/5}p²)** = 2^{1/5}d⁹(p−2)²(2^{3/5}d⁶ + 4d³p + 2^{7/5}p²), with d³ = Δ.
5. **E2 coverage (db06bd2c).** The chart (μ₁, μ₂) covers μ₀ > 0 only. The result also covers the rest of F₁₀:
   - **μ₀ < 0:** follows from the isometry μ₀ → −μ₀ (the metric depends on μ₀² and dμ₀²).
   - **μ₀ = 0 with 0 < μ₁ < 1:** switch to the chart (μ₁, μ₀). Since P_{x y μ₂ φ₁} ≡ 0, the coefficient of dx∧dy∧dμ₁∧dφ₁ is unchanged and nonzero.
   - **μ₁ = 0:** the Cartesian argument stands.
   - So "tr R∧R ≠ 0 on F₁₀ \ {μ₁ = 1}" is PROVED for every μ₀. E3 ({μ₁ = 1}) stays COND.
6. **Premises (04b94770).**
   - T3-6 (W-3 diverges) uses **K1 on shell**, ‖G‖² = G·G/4! = 6R > 0. It is REF as finite-without-cutoff, given K1.
   - T3-7 uses the standard fact **G₂ ⊂ Spin(7) is the stabilizer of a spinor**: a torsion-free G₂-structure gives a parallel spinor, hence Ric = 0. This is a stated premise, so (t-i) and (t-ii) are REF as an implication.
7. **Batch-2 tally (04b94770).** The garbled sentence is replaced by **PROVED 8 · COND 3 · OPEN 1 · REF 4 = 16**.
8. **Register B1-c2, W × (P∘r) with r ∈ Isom(Bolza) \ Aut⁺. Status: parked pending an Owner ruling** on whether t4436 lifts the standing "no c2 work". That is the Owner's call, not MR2's. The parking is not a drop. No c2 work was done or started.
   - Keep (PROVED): cases (i′)/(ii′) of 8399be55 re-derived on the doubled MN2. Specifically: the Pin/Spin lift of W × (P∘r) exists, commutes with W̃, and is compatible with the chiral HW projection.
   - Drop (REFUTED): a proof of inconsistency, either no consistent lift, or incompatibility with the HW chirality or with the MN2 twist.
   - Next computation (only if the Owner allows): the explicit spinor lift of P∘r on Σ × S⁴ with the twist, as an orientation and commutator check (~1–2 h).
   - Conflict: Group A (OW 8b26c786). This is a scope conflict, not a REF.
9. **Register status table, post-audit (PP 60293840 grades):**

| branch / row | register (c5a65972) | post-audit grade |
|---|---|---|
| 4b-ii Φ range (as 144R/ℓ²) | COND | **PROVED** [0.308665516, 0.700009526] ℓ_p⁻² |
| reading 144R as G·G | COND | **COND** (K1 on shell; MN2 a solution) |
| 4c R_max = 12 | COND | **PROVED** |
| Φ-2 EH lock | OPEN | **REF** (any positive weight; k in the AdS₅ warped-radius family); averages R̄, Φ̄ **COND** |
| Φ-3 EH lock | REF, COND on R_max | **REF** (PROVED) |
| W-2 | finite COND; value OPEN | finite **PROVED** (implication of K1 + compact M₆); value **COND** |
| W-3 (finite, no cutoff) | OPEN | **REF** given K1; W-3 with cutoff OPEN (NL lane) |
| G2-2 (t-i), (t-ii) torsion-free | OPEN | **REF** (implication; G₂ spinor premise) |
| G2-2 (t-iii) | OPEN | **OPEN** |
| Rc-1 | PROVED/COND | kε ∈ [0.04051, 0.04548] arithmetic **PROVED**; thin-wall interpretation **COND** |
| Rc-2 | PROVED/COND | cutoff (L₅/R_c)² ∈ [555.4788, 555.4790] and all computed modes below it: arithmetic **PROVED**; as KK masses **COND** |
| B1-1b-ii L1 tr R∧R ≢ 0 | COND | **PROVED** |
| B1-1b-ii F ≠ 0 required | COND | **PROVED** (given HW) |
| B1-1b-ii L1 everywhere | OPEN | nonzero off {μ₁ = 1} **PROVED** (all μ₀); vanishing on {μ₁ = 1} **COND** |
| B1-2b as NEC escape (fixed internal metric) | OPEN | **REF** (implication of P-i, P-ii, P-iii) |
| B1-2b identification ε_y = R_S4 | OPEN | **OPEN** |
| B1-c2 | COND, parked | **COND; parked pending Owner ruling** (fix 8) |

All other register rows are unchanged.

## Tallies
- PP's tally of the new claims in files 3–5 is adopted: **14 / 4 / 3 / 5 = 26** (04b94770 8/3/1/4; 3da6285a 4/0/2/1; db06bd2c 2/1/0/0).
- Carried unchanged: ff7fb67f 10/3/2/0 = 15; BPS 14/2/1/1 = 18.
- This erratum adds no new mathematical claim. Fixes 1 and 2 correct two numeric quotes; no label changes.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (checked 22:20 CST), untouched.
