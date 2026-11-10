# FINDINGS: PP confirmation of NL Erratum 22 (NL_ERRATUM22_ACCEPT_PP_e2f5f582_aad209d2_2026-11-09_2211.md, 72a7f5b7…)
2026-11-09, 22:18 CST (America/Chicago). Auditor: Professor Proof (PP). Pure math only. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL; a citation alone never proves; a stated premise is graded as an implication. **Nothing adopted. Junction: UNSOLVED.** Branches [χS], [χU] and [w] are all kept (OW t4436). No CERT, nothing sent. New file only. Scratch work in /workspace/audit-scratch/e22-confirm/; nothing was written into NL directories.
Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start and at write time (unchanged).

## 0. Integrity and reruns
- Target: sha256 72a7f5b77e642c2a54c5635631b9d8b0ea2ff1ac8974ad199ff6afb6909ca7b4 = sidecar (both 22:13:06) ✓.
- Cited sources match: PP e2f5f582… (heavy 6/7/8) ✓, PP aad209d2… (E21 confirm) ✓, PP v2 pushforward 87deaed2… / log 3d26fbed… ✓, PP pp_heavy678 bf61cc56… / 158aeaf9… ✓.
- /workspace/nl-e22-2203/: all four sidecars OK. Each .py sidecar was written before its log (checks: .py 22:05:33, sidecar 22:06:07, log 22:07:53; v0: .py and sidecar 22:06:07, log 22:10:35). The log sidecars were written after the runs (22:11:03), as E22 discloses ✓.
- PP reruns (PYTHONDONTWRITEBYTECODE, cwd in audit-scratch):
  - e22_checks_2026-11-09_2203.py: exit 0, **byte-identical** (b4c2325b…).
  - e22_st2_Tseq_phase_v0_2026-11-09_2203.py: exit 0, **byte-identical** (02f7bfe9…). The fixed v0 makes the log reproducible, so H7-1 is discharged. Against 2129, the only differing line is n=1 Neumann λ₃/λ₄ in the 7th digit, as E22 states ✓.
- Independence: e22_checks shares 5 of 169 non-trivial lines with PP's pp_heavy678 script. It is independent code, as claimed.
- PP scripts (new, with sidecars): pp_e22_h65_2026-11-09.py = 45051cd7…, log 28c52aac…; pp_e22_exact_2026-11-09.py = 8758aace…, log 051d1963….

## 1. H6-5 ruling (key check): **NL is right, and so was PP's e2f5f582. There is no reversal, and no PP self-correction is needed.**
Setup (singlet toy, wall curve): A′ = (√6/3)e^{−4δ} with δ = C − C₀, and d²(δ) = (A′+1)² + 5A′² + (B−B₀)² + δ².
- **Correct sign**, B = C − ½ln6 (from e^{−2B} = 6e^{−2C}): B − B₀ = δ − ln2 exactly.
  - Minimum **|Y−FP| = 1.24430569163132024017677286455** at **δ* = 0.581915470405483457306922238149** (50 digits).
- **Old wrong sign**, B = C + ½ln6: B − B₀ = δ + ln3.
  - Minimum **1.96643776254626511861884143226** at **δ* = 0.348448455672046177156940967787**.
- **Rigour.** d² is strictly convex on ℝ: A′ > 0 is convex; x ↦ (x+1)² + 5x² is convex and increasing on x ≥ 0; the quadratic terms add 4. So each minimum is the unique global minimum (not box-limited). Each root of d²′ is certified by an interval sign change on [δ* ± 10⁻⁴⁰] (mpmath iv, 60 digits). d²″(δ*) = 8.98 and 26.24, both > 0.
- **Bound.** The analytic bound |Y−FP| ≥ 1 uses only (A′+1)² ≥ 1 with A′ > 0, so it is **unaffected** by the sign of B (margins 0.2443 and 0.9664).
- **Which way round.** PP's e2f5f582 says (H6-5 and §1 R6): "The numeric minimum is **1.2443 at C−C₀ ≈ 0.582, not 1.966 at 0.348**", i.e. the correct sign gives 1.2443. That is exactly NL's ordering. PP's relayed summary ("gives 1.244 instead of 1.966") also means the corrected value is 1.244. **PP was not wrong.**
- **New exact sub-fact (unlabelled, no grade change).** On the wall curve, |Y−FP| ≥ 1.244305691631… globally. R6 (J4, "no toy solution") stays **CONDITIONAL**.

## 2. Fix-by-fix faithfulness
| fix | E22 | verdict |
|---|---|---|
| H6-1 EOM-level only; Palais not applicable (non-compact H, PSL(2,ℝ) local); no reduced-action licence | §2 | **faithful** |
| H6-2 8th 4-form vol(S²)∧dr∧dχ, closed; Λ⁴ = 8, Sym² = 9; R1 split, R1b REFUTED | E22-1; rerun reproduces the 8-term kernel | **faithful** |
| H6-3 full g_χχ; cone ratios 1; scope = metric | §2 | **faithful** |
| H6-4 R5 withdrawn; a(C_w) = (√6/3)e^{−4δ}; counterexample C₀−1 → 44.58; proper frame 1/L₅,E = (256/9)^{1/3} | E22-2 | **faithful**. PP exact: minpoly(4·2^{2/3}3^{1/3}/3) = 9X³−256; ratio to (256/9)^{1/3} has minpoly X−1 |
| J7b-PP: δ ≥ 7ln2/36 − ln3/12 ≈ 0.0432276; C_w = C₀ fails (3.9565 > 3.0526); y-frame −ln(3/2)/8 | E22-3 | **faithful**. PP exact: the linear log-equation has coefficient −6, and root − target = (5/36)(ln6 − ln2 − ln3), with exp(36·residual) = 6⁵/(2⁵3⁵) = 1, so the residual is 0 |
| J7a PP self-correction (y-derivative; magnitude needs e^{−s}) | E22-3 | **faithful** |
| H6-5 sign fix; 1.2443 @ 0.582 correct vs 1.966 @ 0.348 wrong; bound unaffected | §2 | **faithful** (see §1) |
| H7-1 fixed v0 | e22 v0 script | **faithful**; rerun byte-identical |
| H7-2 drop "remaining positive" for n=2,3 Neumann; grade rests on identity; A > 0 exact | §3 | **faithful** |
| H7-3 "enters only via α′ − a_t" | §3 | **faithful** |
| H7-4 "agree to 6 digits" (T=16 λ₁; n=3 λ₃) | §3 | **faithful** |
| H8-1 Weyl argument; W_{χφχφ}(π/4) = 2^{3/5}/18 at the MN2 IR, 0 when X_a = X_b | E22-4 | **faithful**. PP exact: minpoly(W(π/4) − 2^{3/5}/18) = X, i.e. the difference is exactly 0 |
| H8-2 converse, real zeros {0}; also recorded for R3 | §4 | **faithful** |
| E21-α attribute flux derivation to PP (3fa2e067 §4) | §1 | **faithful** (NL writes v for PP's u; notation only) |
| E21-β E21 distinct new 0/0/0/0 | §1 | **faithful** |
| v2 citation: minpoly(R) = X−1; value −2 + 2√2·log(1+√2) | §1 | **faithful**; matches the PP v2 log |

## 3. Grade drift: **none**
Revised tallies equal PP e2f5f582 exactly:
- 2103: 4/2/2/2 = 10, plus J7b-PP (PROVED, implication of N4).
- 2133: 3/1/2/0.
- 2137: 3/1/3/0.
- Heavy-queue roll-up: 10/4/7/2 = 23 + J7b-PP.
- E21: 0/0/0/0 distinct.

R2, R3 and R7–R9, and every 2133/2137 row, are unchanged. Z2 stays OPEN and the [w] branch is untouched.

E22's own header 2/0/0/2 = 4 is arithmetically correct as a row count (E22-1 REFUTED, E22-2 REFUTED, E22-3 PROVED, E22-4 PROVED) ✓. **Distinct new claims, for roll-ups: 0/0/0/0.**
- E22-1 restates R1b.
- E22-2 restates R5.
- E22-4 is the basis of Q8-conf; NL itself says it is not a new 2137 row.
- E22-3 is J7b-PP, already carried as "+J7b-PP" in the heavy roll-up.

Do not add E22's 2/0/0/2 to any roll-up (fix E22-β).

## 4. Verdict
**FAITHFUL.** Every listed fix (H6-1–H6-5, H7-1–H7-4, H8-1, H8-2, E21-α/β, J7b-PP, the J7a self-correction) is applied correctly, both NL scripts rerun byte-identical, and no grade drifted.

## 5. Remaining fixes (bookkeeping only; no grade change)
- **E22-α (attribution).** E22-1 to E22-4 are PP-originated results (e2f5f582: the R1b counterexample, the R5 counterexample, J7b-PP, the Weyl closure), independently re-derived by NL. Say so in the row text, as E21-α did for the flux.
- **E22-β (double counting).** Record E22's 2/0/0/2 as a row count only. Its distinct new claims for roll-ups are 0/0/0/0.
- **E22-γ (exact tests).** e22_checks uses `simplify(x − y) == 0` for three equalities (lines 185, 203 and 210: the Weyl value, (256/9)^{1/3}, and the J7b bound). All three are true, as PP's exact tests above confirm (minimal_polynomial = X; minpoly ratio = X−1; rational exp-identity). Replace them with minimal_polynomial or rational-arithmetic tests, since a `simplify` result of False is not a disproof and a True is not an audit-grade proof.
- **E22-δ (optional).** R6's minimum 1.2443… is a global minimum (strict convexity plus interval-certified root), not only box-limited. NL may record this as an unlabelled exact sub-fact. R6 stays CONDITIONAL.
