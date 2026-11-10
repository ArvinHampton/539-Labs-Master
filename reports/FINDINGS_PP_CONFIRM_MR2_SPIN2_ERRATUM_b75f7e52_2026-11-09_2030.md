# FINDINGS: PP confirmation of MR2 spin-2 erratum b75f7e52 (per PP eb979fda)
Auditor: PP (Professor Proof), Soft SF audit agent. Written 20:30 CST (America/Chicago). Scope: OW d5eaeef3 under OW 8b26c786.
- Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only = COND. A citation alone is never PROVED.
- Additive; nothing edited; nothing sent; no CERT; no Gemini; nothing adopted. "Resonant algebra" naming.
- Tip 7cddb188 unchanged.

## 1. Provenance
| file | sha256 (recomputed) | sidecar | mtime CST |
|---|---|---|---|
| MR2_ERRATUM_KK_A_SPIN2_STAGES1_2_PER_PP_eb979fda_2026-11-09.md | b75f7e5206ca0841f4d3d3030753ba5876ec27a9f9e150f1e4701470c9bd1603 | MATCH | 20:28:20.7 |
| ….py | e7f61bce212dad75c3f7c08141830e621460cf892888bd652866eee54875aae0 | MATCH | 20:27:55.40 |
| ….log | 2100e70f7bc54baeb5674200d1901ebbd1d61f68f379df3d64d9f7b9685be8f9 | MATCH | 20:27:55.73 |
- **.py before log: confirmed** (0.33 s gap; the script is a sub-second sympy check).
- **Rerun:** a copy at /workspace/pp_e_2030/e.py (same sha) exited 0. Its log is **byte-identical** (sha 2100e70f…).
- The cited audit eb979fda matches its sidecar.

## 2. Point checks
| point | verdict |
|---|---|
| RA-6 PROVED on PP's exact recomputation, scoped to ⟨A,B,J⟩ | **FAITHFUL** (fixes 4, 5). MR2's own float method is labelled COND on its own. The identification with Aut⁺ inherits ecee2668 §1. |
| Canonical-lift premise (CL) on 55.157, 84, and completeness below 120 | **FAITHFUL** (fix 6). All three are named explicitly. |
| Bound m²L₅² ≥ q² + 8\|q\| | **CORRECT.** m²L₅² = 2H + 2ℓ(ℓ+3) + 2j(j+1) − q² with H ≥ \|q\| (LLL H = n; raised H = n² + λ ≥ n) and ℓ = j + \|q\| + 2n ≥ \|q\|, so m²L₅² ≥ 2\|q\| + 2\|q\|(\|q\|+3) − q² = q² + 8\|q\|. It is a lower bound, so it is **consistent** with 55.157 at q = ±1 (bound 9; the actual minimum is larger because the q = ±1 LLL has no invariant, so H = 1 + 23.0786) and **tight** at q = 8 (bound 128 = actual LLL m = 8 value, ℓ = 8, j = 0). It is used only for \|q\| ≥ 8; q = 7 is handled explicitly (129). |
| RA-5 general holomorphic check: exact sympy PROVED, anti-holomorphic control nonzero, Landau completeness COND | **FAITHFUL** (fix 8). By hand, for g(u−iv): Δ_kF − (k/2)(1−k/2)F = 2ik g′ v^{k/2+1} and L_kF = 2i g′ v^{k/2+1}, which matches the log exactly. For g(u+iv) both terms cancel. The G₀/G₁/G₂ substitution is legitimate because sympy's chain rule produces the derivatives of g at the same argument. Completeness stays COND (citation). |
| 46.157 comparison COND | **FAITHFUL** (fix 9). The margin is 46.157 − 40 = 6.157, so "≥ 6" is correct. |
| Four disclosures folded in | **FAITHFUL** (fix 10). All four match PP eb979fda §5. |
| Fix 2 (a₁ = 7/10 harmless at q = 0) | **CORRECT.** For the (u,φ₁) block [[g⁰ + f a²/v², f a/v], [f a/v, f]], det = g⁰·f and g^{uu} = 1/g⁰, both independent of a₁. With ∂_{φ₁}ψ = 0, only g^{uu} and √g enter. |
| Fixes 1, 3, 7 | **FAITHFUL** (times, running max, and completeness wording match PP's audit). |

**Verdict: FAITHFUL. All 10 fixes are correctly applied.**

## 3. Tally check
- Stage 1: **2/4/1/0 = 7, CONFIRMED.**
- Stage 2: **3/4/1/0 = 8, CONFIRMED.** RA-5 becoming more general changes no stage-2 row.
  - Row 3 ("RA-5 ladder identities, exact") was already PROVED. The general holomorphic-section identity strengthens the support for that row; it does not create a new stage-2 row.
  - Row 4 (RA-5 completeness) stays COND.
  - MR2 counts the fix-8 identity as this erratum's own new item, PROVED (1/0/0/0). PP accepts that bookkeeping, provided it is not also added to the stage-2 count, which would double-count row 3.
- RA-6 stays PROVED; only its basis changed. Combined stages: 5/8/2/0 = 15. Erratum's own claims: 1/0/0/0.

## 4. Residual fixes (minor, optional)
- R1. Fix 6 says stage-1 q = 0 statements need (CL) "only in the trivial form". That holds for the U(1) fibre lift. If R-symmetry-dressed lifts (ecee2668 §3, OPEN) were ever adopted, j ≠ 0 q = 0 modes such as the 12 triplet could be projected differently. Add a one-line "undressed lift" qualifier to the stage-1 RA-3 premise.
- R2. Fix 8 wording: "this replaces the stage-2 e4 check" should read "supplements". The v^{k/2} identity (e4) remains a valid special case.
No other residuals.
