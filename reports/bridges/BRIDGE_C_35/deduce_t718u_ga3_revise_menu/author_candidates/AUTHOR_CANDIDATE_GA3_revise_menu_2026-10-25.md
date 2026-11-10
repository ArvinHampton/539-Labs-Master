# AUTHOR-CANDIDATE G-A3 revise menu (NOT Cat A) — t718u
PREREG c3ea78b6f09531762a8cd44ccd52c121bbbd0f6276cae4503d62a89a4bb7ebfa. Baseline = t713s4497 P1–P7 + t713s4484. No numbers below are new; all cited from REJECTED fill RESULTS c4755206….

## Diagnostic basis (from REJECTED fill, cited)
- |δ| N=106: 62.97 / 7.08 / 5.56 / 35.14; N=150: 64.80 / 7.52 / 14.34 / 31.88; V-P(43/58/67): 57.25 / 7.32 / 7.40 / 32.44.
- |ψ| ≤ 4e-2 ⇒ ψ-knobs cannot move |δ| by more than ~O(10⁻¹·slash) — far below the O(10) gap.
- tol ~1e-3–1e-2 driven by 4-decimal slash rounding; |δ|/tol ~10³–10⁴ ⇒ precision is NOT the F1 driver.
- Ξ_N on ℝ: |e(νx)|=1, c_ν/√ν growing ⇒ termwise I(x) non-convergent; N-shift (5.56→14.34 at x=5/7) shows h is truncation-artefact-dominated. ⇒ dominant F1 lever = Ξ form / evaluation (convergence), not ψ / precision.

## Single-knob options
| id | change vs t713s4497 | grounding | invent status | expected F1 / F2 / F3 |
|---|---|---|---|---|
| R-A1 | Path 0→i∞ (Eichler-standard) instead of i∞→x | b329c67c L21; 552541cf L46; 22959c01 L57 (Written, conflicts 1bab65c4 L32) | Written (path choice needs AUTHOR pick between conflicting Written) | Changes h by a period-type constant/x-dependent term; ray from x=real still hits non-convergent Ξ on ℝ at endpoint 0 ⇒ F1 likely still FAIL; F2 not forced; F3 defect changes form |
| R-A2 | Keep path, alt branch Arg∈[0,2π) / (w−x)^{−1/2}=e^{+iπ/4}t^{−1/2} | none Written (branch unspecified everywhere, t712u B-path) | invent-risk / AUTHOR-ACCEPT-needed | Global phase flip on I ⇒ conjugate-type change; |δ| magnitudes O(10) persist; F1 FAIL expected |
| R-B0 | Keep ψ≡psi-Cocycle (t713s4484) | 1be7f7d1… ACCEPT | ACCEPT-sourced | baseline |
| R-B1 | ψ≡0 restricted trial (Ξ-integral-only diagnostic) | none (t712u: "ψ≡0 would be invented") | AUTHOR-ACCEPT-needed (diagnostic only, never fill) | |Δδ| ≲ few×4e-2·slash ⇒ F1 unchanged FAIL; useful only to isolate Ξ contribution |
| R-B2 | ψ as W₇-cocycle obtained by conjugating S-cocycle (W₇ = S∘diag(√7) scaling) | 1be7f7d1 §A4 + 7368b855 L44 — conjugation itself NOT Written | invent-risk | Same small magnitude ⇒ F1 unchanged; removes S-vs-W₇ soft flag only if ACCEPT |
| R-C0 | Ξ product-only, N=106 (status quo) | 1bab65c4 L18; 736cfd72 L16; 552541cf L20–24 | Written+ACCEPT | baseline (FAIL) |
| R-C1 | Lift ledger HOLD: use ledger Ξ 7dbd63af… (χ/ϑ catalogued, order77 Cat A) | 7dbd63af…; HOLD per t604u FINDINGS L10 / P4 | AUTHOR-ACCEPT-needed (HOLD lift for G-A3) | Only option that reproduces Written 43/58/67 and 78:6 by construction; if ledger has closed χ/ϑ form, permits modular evaluation (convergent off-ℝ) ⇒ best chance of moving F1; pass NOT claimed |
| R-C2 | Hybrid: product + Written partial 43/58/67 + 78:6 entries as listed (c=table col2) | be1faa52 §1; 736cfd72; 1bab65c4 §2 (col2 semantics unstated) | AUTHOR-ACCEPT-needed (col2 = coefficient vs index re-decision, reverses P6) | V-P already shows ≈ same |δ| (57/7/7/32) ⇒ F1 FAIL expected; resolves "not from product" soft flag only |
| R-D1 | N_trunc=106 retained | 736cfd72/1bab65c4 last listed degree | Written | FAIL; no error bound |
| R-D2 | N_trunc ↑ (150/250/…) | none | AUTHOR convention | Evidence (N=150) shows drift, not convergence ⇒ F1 not fixed; diagnostic only |
| R-D3 | Complex-contour / Im-shifted evaluation: integrate on w = x+iε+it (or i∞→x+iε then Γ-type tail), giving geometric convergence |q|=e^{−2πε} and explicit tail bound; take ε→0 by Abel/limit with stated bound | Rationale from fill PREREG "no convergent bound"; contour not Written | AUTHOR-ACCEPT-needed (evaluation convention, not new object) | Gives controlled error ⇒ F3 could become "controlled"; F1 outcome unknown (honest: may still FAIL if defect real) |
| R-D4 | Modular-completion evaluation: use transformation of Θ_{3/2} to evaluate I near ℝ via W₇ image in upper half-plane | 552541cf L24 Θ form; transform law not Written for partial theta | invent-risk (partial theta not modular) | Unclear; partial theta lacks clean law ⇒ not recommended |
| R-E1 | Slash coeffs 8-digit (10.69231032, 0.21604451, 2.7617779, −7.53161419) + target magnitudes 19.80101008/1.82482876/9.24175308/20.902153 | grok_export …/fe3969ab-…/prod-grok-backend.json ("Candidate 2" fit) — export, NOT Written corpus | AUTHOR-ACCEPT-needed (RM-4) | Shrinks tol ~10²–10³×; |δ| unchanged O(10) ⇒ F1 FAIL unchanged (stricter) |
| R-E2 | Regenerate slash from selectors (Cat A 437d4571… / S-B1′ 3d502756…) at full precision | 437d4571…, 3d502756…, 7368b855 §2 | Written/ACCEPT (refit = compute, needs auth) | Same as R-E1; no F1 rescue |

## Bundled packages
- **R-PKG1 (recommended, minimal-invent, Written-first):** R-C1 (ledger Ξ HOLD lift) + R-D3 (contour/tail bound) + R-E2 (full-precision slash) + R-B0 + path per Arvin pick between R-A1/P2. Changes: Ξ source, evaluation convention, precision. Status: AUTHOR-ACCEPT-needed ×2 (HOLD lift; contour). Expect: F3 controlled; F1 undetermined (only bundle with plausible movement); F2 not forced.
- **R-PKG2 (diagnostic decomposition):** R-C0 + R-D3 + R-B1 + R-E1. Isolates Ξ-integral defect with bound. AUTHOR-ACCEPT-needed (ψ≡0 diagnostic; export coeffs). Expect F1 FAIL; output = clean obstruction measurement, not fill.
- **R-PKG3 (path audit):** R-PKG1 run twice: P2 (i∞→x) vs R-A1 (0→i∞). Resolves Written path conflict empirically. Expect F1 FAIL under at least one; F2 not forced.
- Not recommended: R-A2, R-B2, R-D2, R-D4 (invent-risk or evidence-negative).

## Invariants
Samples never force δ≡0 (F2). Menu NOT Cat A. No re-run until Arvin picks. Bridge PARTIAL | READY NO | residual-C OPEN. No order78.
