# MR2 · MN2 · KK Group A — scalar/vector towers: status, plus errata to stages 1/2 and b75f7e52
Written 20:33 CST (box clock). Additive; no existing file edited. Authority: OW d5eaeef3 under OW 8b26c786 (Group A = Aut⁺(48) × wall ℤ₂, a scope choice, not a result). Full spectrum OPEN; junction UNSOLVED; count gap unchanged. Tip 7cddb188 MATCH, untouched. Usage at last check: 75.3%.

PP confirmation read: FINDINGS_PP_CONFIRM_MR2_SPIN2_ERRATUM_b75f7e52_2026-11-09_2030.md, sha256 7441335e84b47bea6b60e6059675070765c987232f6914c7c438c8727f9226ec, **MATCHES** its sidecar.

## 1. Scalar and vector towers: status. OPEN (not computed)
- **No scalar or vector KK masses have been computed** beyond the Σ-constant scalars already filed (ecee2668 §7: −4, 0 (5-plet), 12, within the U(1)² truncation).
- **Why.** Unlike spin-2, which obeys the universal Bachas–Estes scalar-Laplacian equation (stages 1/2), the scalar and vector fluctuations of the MN2 uplift mix metric and C₃/G₄ modes. Their masses need the full coupled linearised 11D equations, or an exceptional-field-theory KK spectroscopy, on the V2 background.
- That is the "skip any part that blows the budget and mark it OPEN" case of OW d5eaeef3 stage 2. No partial or estimated values are given. In particular, I did not infer scalar masses from spin-2 masses via a supermultiplet assignment: which N=2 multiplet each spin-2 mode sits in is not established here.
- **The Group A selection carries over unchanged once masses exist:**
  - a scalar or vector mode survives iff its Σ factor is Aut⁺-invariant under the lift used (see errata (1)), for every SO(3)_R spin j and every U(1) charge q;
  - wall parity follows ecee2668 §6 (metric-derived even; C₃-derived with 4D-tangent legs odd).
  - Under the canonical, undressed lift, the Σ-side invariant content is the same as for spin-2: raised scalar levels with Aut⁺-invariant λ, and Landau levels only where dim H⁰(K^m)^{⟨A,B,J⟩} ≠ 0 (m = 6, 8 among m ≤ 8).
  - This is a selection statement only: **COND** (canonical undressed lift, HW, and ⟨A,B,J⟩ = Aut⁺ per ecee2668 §1). It carries no masses.

## 2. Errata (per PP 7441335e)
**(1) Undressed-lift qualifier. ACCEPT.**
- Stage-1 RA-3 (8ca7b93a; b75f7e52 fix 6) holds for the **undressed** lift: the canonical derivative lift with no R-symmetry dressing.
- If an R-symmetry-dressed lift (ecee2668 §3, OPEN) were adopted, Aut⁺ could act on SO(3)_R multiplets. Then j ≠ 0 modes at q = 0 could be projected differently. An example is the **12 (Δ = 6) SO(3)_R triplet**, and likewise the 32 (j = 2) and 40 (j = 1) levels.
- Only the j = 0 rows of stage 1 are unaffected by dressing by an SO(3)_R element, since j = 0 carries no SO(3)_R action: the 20 singlet (Δ = 2+2√6) and the 56 level.
- The same qualifier applies to all stage-2 charged rows (premise (CL) becomes canonical **undressed** lift) and to the selection statement in §1 above.

**(2) b75f7e52 fix 8 wording and tally. ACCEPT.**
- In b75f7e52 fix 8, "This replaces the stage-2 e4 check" should read "**This supplements** the stage-2 e4 check". The v^{k/2} check stays valid; the general v^{k/2}g(u+iv) check is added to it.
- Tally bookkeeping: the RA-5 general holomorphic identity is counted **only** in b75f7e52's own tally, as PROVED 1 · COND 0 · OPEN 0 · REF 0. It is not counted again in stage 2.
- The stage-2 tally stays PROVED 3 · COND 4 · OPEN 1 · REF 0. Its row 3 is the original ladder identities, already counted there.

## Tally (this file)
| # | item | label |
|---|---|---|
| 1 | scalar/vector KK masses (beyond the Σ-constant scalars) | OPEN |
| 2 | Group A selection rule for scalar/vector modes (canonical undressed lift; HW; ⟨A,B,J⟩ = Aut⁺) | COND |
| 3 | errata (1): undressed-lift qualifier on stage-1 RA-3, stage-2 (CL) and §1 | bookkeeping (not graded) |
| 4 | errata (2): "supplements"; RA-5 identity counted once (b75f7e52: 1/0/0/0) | bookkeeping (not graded) |

**PROVED 0 · COND 1 · OPEN 1 · REF 0 = 2.** Unchanged: stage 1 2/4/1/0, stage 2 3/4/1/0, b75f7e52 1/0/0/0.

Rules: new dated file only; no existing file edited; tip untouched; no CERT, no Gemini, nothing external; no messages sent. Naming: resonant algebra (RA-n) as in stages 1/2.
