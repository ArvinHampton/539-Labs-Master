# MR2 branch attempt: B1-c2′ / 1a wall — pointwise wall Bianchi identity and the sign of the M5 density J_M5 for the f-lifted E₈ candidates E-0, E-T, E-Λ±, E-S± (cc21b272 rows 22–23; 0069b9ae row 12; 51cd8bc8 row 13)
2026-11-10, written 10:30:58 CST (America/Chicago; this is the write time, matching the file's mtime). Author: MR2. Additive; nothing edited; **nothing adopted** (not 1a, not B1-c2′, not any candidate); no CERT, no Gemini, nothing sent. Junction **UNSOLVED**. Group A stays the KK scope; c2′ conflicts with it on scope only. Wording: resonant algebra.

## Inputs (sha = sidecar, all checked 10:17 CST)
- cc21b2728dd74fe6aae8d7da186a5bb40f9b5b4e8d8390226f2fa0e904f08f11 (the E₈ bundle file: candidates, D1–D5, M-s / M-loc).
- Erratum 55941d820946de7fd5aec8603cfb711c569a71a42b27fe32b77bd575a192f4fa.
- PP 51198d6fd2056673a01d22aff38147ffe626dab29d26de471a4c90ca73978deb, addendum 107dc13de4a9a8ea097908d639f5c6e951539c1972c7f64f5f0425bb9f18501d, confirm f2e2e0a68230f578f9eabd04a1e240eced7e6ae7cb761c99125152c9eaf91f95.
- E-S± 51cd8bc836926a68b55d8ce80933008baf5f94d3994321773dc11f31d0f2a882 and E-T 0069b9ae53a1d9f2f4a863ff8e97f5aaad6de02497a62ed704e8c21a55506781. Both restorations are pending PP; this file does not depend on the lifts beyond listing the candidates.
- bd47ff5e8f62a6226680a93107cacae8c8be573399e1f101a2dc57635f03fbfb: G₄ index sets; wall charge 2N; the flux route. Its .py ce94face… was read only for the flux route.
- 5511845e7c4b6e212bf3aa0b11a8e3b531925dd277a7029c8624c74c78bb15b9: Fix 1, flux = π² exact, so 2N = 9760.
- f825dfffb8cd17a7f3f57a2b0a70bd0d9c9d73f215febffdbd2ca95b494d7cd1: wall Bianchi relation N_M5 + n_inst = 2N; E₈ sector COND.
- 425b4e67e5cc58ac8607d9f0c668f2e5d48f3d2bc3363e011ebd194800ecd85a: sha checked only; not otherwise used.
- V2 routines …_V2.py ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85 (sha = sidecar), exec'd verbatim before its MAIN marker, as in bd47ff5e.
- No external source was fetched. HW (hep-th/9603142) and the E₈ embedding-index facts below are cited only, so they are COND.

## Script and log (frozen: chmod a-w and sidecar written before the run)
| file | sha256 | mtime |
|---|---|---|
| /workspace/mr2-c2e8-1010/c2p_wall_bianchi_jm5_2026-11-10_1030.py (+ identical copy in reports/ with its own sidecar, cmp ✓) | 2a4339e26c97f3c4ca83db71291418e7e3dd4beaaf9b5c4649bcc1791d0c7336 | 10:24:37 (sidecar 10:24:42; run started 10:24:42) |
| /workspace/mr2-c2e8-1010/c2p_wall_bianchi_jm5_2026-11-10_1030.log (+ identical copy in reports/, cmp ✓) | ef281a27920832a323e0e61bee572b44b73e38284f40be7b2ec5b37c00837a21 | 10:27:09; exit 0 |

**Self-disclosed nits:**
- **Name vs mtime.** "1030" in the names is ~6 min ahead of the run. The mtimes are authoritative.
- **Exit file.** An extra 7-byte file c2p_wall_bianchi_jm5_2026-11-10_1030.exit ("exit 0") was written next to the log by the shell wrapper. It is not copied into reports/.
- **Log line 1** ("== MR2 adoption blockers … ==") is printed by the verbatim V2 prefix, not by this job.
- **[F] prints False.** That check is a symbolic artefact: the V2 metric keeps a₂ symbolic, so g_{φ₂u} ∝ a₂ is formally nonzero. At MN2, a₂ = 0 (log line 3). The (α, β, φ₁, φ₂) block used for the fibre has no u, v entries in any case.
- **Mislabelled check.** "max |star²+1| = 2.0" means ⋆² = +1 on Λ² (correct for 4D Riemannian). The check should have been printed as |⋆² − 1| = 0.
- **Unused name.** U_s, returned by Omega_sym, is never used. There is no other dead code.
- **Elapsed counters.** The counters restart after the geometry build, so the 57 s + 4 s build time is not included in them.
- No empty or superseded logs.

## 0. What is being tested, and the premises
The wall Bianchi identity, as in cc21b272, is J := 2G₄|_wall = c·(tr F∧F − ½ tr R∧R) + J_M5 on Y₆.
- **Charge units:** Q := (1/16π²)(tr F² − ½ tr R²), with tr = Tr₂₄₈/30 = tr₁₆ and p₁ = −(1/8π²) tr R∧R. So ∫_{S⁴} J = 2N = 9760 and n = ∫ Q_gauge.
- **σ = ±1** is the relative sign of instanton and M5 charge in the HW identity. It is not fixed by any filed source, so every result is given for both signs.

**Premises:**
- **HW.** The normalisation c (f825dfff; HW cited, COND).
- **Unbackreacted wall.** J = 2G₄^{MN2}|_wall, exact MN2 on both sides (bd47ff5e premise; localized backreaction OPEN).
- **Or.** M5 worldvolumes are ℝ^{1,3} × C, and every tangent 2-plane P of C satisfies π*vol_Σ(P) ≥ 0. This is the MN wrapping orientation over Σ. Vertical or mixed planes with π*vol_Σ(P) = 0 are allowed in either orientation.
- **Emb-T** (for E-T) and the fixed SO(3) ⊂ E₈ premise of index j (for E-Λ±; PP addendum fix 8).
- **M-s / M-loc.** As in cc21b272.

## 1. Results
- **[U] J's fibre component has a definite sign (exact).**
  - At MN2, X₀ = X₂ = p := 2^{2/5} and X₁ = p/2 (exact, log [U]). With s = μ₁², the CLP/V2 flux function is **U = −p²(4 − s)** (sympy factor), so U ∈ [−4p², −3p²] < 0 on all of S⁴.
  - **Fibre component.** The 11D metric is block-diagonal in the coframe (AdS₅, Σ, dα, dβ, Dφ₁, dφ₂), and ε₇ is the unwarped 7-volume. So the pure-fibre coordinate component is G₄|_{αβφ₁φ₂} = ±κ·U·D^{−7/6}·√det g_fib.
  - **Checks.** This formula matches the V2 Hodge dual (the bd47ff5e route) to 25 digits at two points (log [J]: 0.004801292192432389780811121 and 0.08861410043251590019223917, up to overall sign).
  - **Normalisation.** GL 24×16 gives |∫ G₄_fib| = 9.869604400823735415 against π² = 9.8696044010893586188, and 5511845e shows it is exactly π². So ρ_J := J_fib (∫ = 9760) is nowhere zero.
  - Per unit fibre volume, min 4983.71725859555 and max 8391.05022271765 (log [R]).
- **[Lemma, positivity under Or.]** The pointwise cone generated by the Poincaré-dual 4-forms of allowed 2-planes is the closed half-space {J : J ∧ π*vol_Σ ≥ 0}.
  - Proof: the dual cone K* is the set of 2-forms ω with ω(P) ≥ 0 on every allowed plane. Such an ω must vanish on all vertical and mixed planes (both orientations are allowed), so it kills Λ²F and H⊗F, leaving ω = λ·vol_Σ with λ ≥ 0. Then K = K**.
  - So **J_M5 ≥ 0 ⇔ (J_M5)_{αβφ₁φ₂} ≥ 0** in the orientation where ∫J_fib = +9760. Mixed components with Σ legs are unconstrained.
- **[Closure.]** dJ = 0 (dG₄ = 0 in the bulk), and Chern–Weil forms are closed. So J_M5 is closed and M-s satisfies the pointwise Bianchi equation by construction. The content of the test is the sign condition.
- **[P-lemma] Natural 4-forms have no pure-fibre component (exact).**
  - P (φ₂ ↦ −φ₂) is an isometry of the 11D metric, of the 10D wall metric and of Y₆ ([M] in cc21b272, exact). It fixes the Σ point and (α, β).
  - Any natural 4-form ν (p₁ of Y₆, of the fibre, of the 10D wall, or tr R∧R restricted from 11D) satisfies P*ν = ν. But P*(h dα dβ dφ₁ dφ₂) = −h dα dβ dφ₁ dφ₂ for φ-independent h. **Hence h ≡ 0.**
  - The log agrees: p₁(TY₆) and p₁(fibre) components are exactly 0.0 at all 408 points, and at v = 1 and v = 3.
  - The Euler form is not natural under orientation reversal (P*e = −e), so it survives.
  - This also covers both readings of the HW gravitational term, and agrees with the one-point [Q] in cc21b272.
- **[Gauss.]** The pure-fibre component of the curvature of V_vert (the vertical projection of Levi-Civita) is the intrinsic Levi-Civita curvature of the fibre metric g_fib (Gauss formula). E-Λ± and E-S± therefore need only the squashed S⁴.
- **[Λ²±.]** p₁(Λ²±) = p₁ ± 2e at form level (so(4) = so(3)₊ ⊕ so(3)₋).
  - Verified directly from the induced action on Λ²± (log [I]): pointwise defect ≤ 8.6096e-42.
  - Integrals: ∫e = 1.9999999784732826887, ∫p₁(Λ²±) = ±3.9999999569465653773 (GL 24×16 accuracy), ∫p₁ = 0.0.
  - With [P-lemma], (p₁(Λ²±))_fib = ±2e_fib.

## 2. Verdict per candidate (keep/drop only on "solves the pointwise Bianchi equation with J_M5 ≥ 0, or a precise obstruction")
- **E-0** (F = 0, n = 0, N_M5 = 9760). Q_fib = (p₁(Y₆)/4)_fib ≡ 0, so (J_M5)_fib = ρ_J > 0 everywhere, for either σ.
  - **M-s with J_M5 ≥ 0: PROVED as an implication** (premises HW, unbackreacted wall, Or). Log: min J_M5/ρ_J = 1.0 for σ = ±1. **Keep.**
- **E-T** (F = R_{Y₆} via SO(6) ⊂ SO(16), so tr₁₆F² = tr₆R²; Q = −p₁(Y₆)/4; n = 0, N_M5 = 9760). Q_fib ≡ 0 by [P-lemma] for the gauge part and the gravity part, so (J_M5)_fib = ρ_J > 0.
  - **M-s with J_M5 ≥ 0: PROVED as an implication** (HW, unbackreacted wall, Or, Emb-T). Log: 1.0 for σ = ±1. **Keep.**
  - Its connection-preserving lift is still pending PP (0069b9ae).
- **E-Λ±** (index j). Q_fib = ∓(j/2)·e_fib.
  - **Scan** (408 points: GL 24×16 plus 24 edge points at dps 60 down to 1e-5):
    - e_fib > 0 at every point. The per-unit-j ratio (e/2)/ρ_J ranges over [1.42304189431507e-5, 0.000402497029203276]. The maximum is at (α, β) = (π/2, 1e-5), i.e. μ₁ → 1.
    - In the adverse pairing (Λ⁺ with σ = −1, Λ⁻ with σ = +1), J_M5 ≥ 0 at all scanned points **iff j ≤ j\* = 2484.4903873687**.
    - In the favourable pairing there is no bound.
  - **Index.** The sources do not fix j, so it stays labelled.
    - j ≠ 1: a homomorphism SO(3) → E₈ needs −1 ∈ SU(2) to act trivially, but the index-1 (root) SU(2) has 248 = (3,1) + (2,56) + (1,133), which contains doublets.
    - j ≤ 1240: the principal SU(2).
    - Both facts are cited, so COND.
  - So **J_M5 ≥ 0 for every admissible j and both σ: COND** (float scan plus citations), with a margin of j\*/1240 ≈ 2.
  - N_M5 = 9760 ± j > 0. **Keep (COND).**
- **E-S±** (j = 1, n = ±1). Log: min J_M5/ρ_J = 0.999597502970797 (adverse sign) and 1.00001423041894 (favourable sign). **J_M5 ≥ 0: COND** (float scan). **Keep (COND).**
- **M-loc, all candidates (precise obstruction).**
  - J − Q is a smooth form. If it equals a δ-current supported on finitely many surfaces, it vanishes off them, hence everywhere by continuity. So N_M5 = 0.
  - But N_M5 = 9760 − n ≠ 0 for every candidate (|n| ≤ 1240). Alternatively, J_fib > 0 while Q_fib ∝ e_fib integrates to |n| ≤ 1240 ≠ 9760.
  - **M-loc is obstructed: PROVED as an implication of the unbackreacted-wall premise.** Localized backreaction is OPEN.
  - This is not a drop of any candidate, because M-s survives.
- **Not shown for any candidate:**
  - that the positive smeared J_M5 is realised by an actual smeared family of oriented M5 curves (global realisation);
  - BPS/calibrated positivity, which is stronger than Or;
  - wall SUSY;
  - which candidate is the physical 1a datum.

## Labels (PP convention)
| # | item | grade |
|---|---|---|
| 1 | [U] U = −p²(4 − s) < 0 on S⁴; G₄_fib = ±κU D^{−7/6}√det g_fib (checked against the V2 Hodge dual); J_fib nowhere zero | PROVED |
| 2 | normalisation ∫J_fib = 9760 (5511845e exact; reproduced to 2.7e-11) | PROVED (in-repo) |
| 3 | lemma: under Or, J_M5 ≥ 0 ⇔ (J_M5)_{αβφ₁φ₂} ≥ 0 | PROVED as implication of Or |
| 4 | closure: J_M5 closed; M-s solves the pointwise Bianchi equation by construction | PROVED |
| 5 | P-lemma: natural 4-forms (p₁ of Y₆, fibre, 10D wall; restricted 11D tr R²) have zero pure-fibre component | PROVED as implication of [M] (P an isometry) |
| 6 | Gauss: the fibre component of the V_vert curvature equals the fibre's intrinsic curvature | PROVED |
| 7 | p₁(Λ²±) = p₁ ± 2e at form level (defect ≤ 8.6e-42; integrals ±4, 2, 0) | PROVED |
| 8 | E-0: M-s with J_M5 ≥ 0, N_M5 = 9760 | PROVED as implication (HW, unbackreacted wall, Or) |
| 9 | E-T: M-s with J_M5 ≥ 0, N_M5 = 9760 | PROVED as implication (HW, unbackreacted wall, Or, Emb-T) |
| 10 | E-Λ±: Q_fib = ∓(j/2)e_fib; J_M5 ≥ 0 iff j ≤ j\* = 2484.4903873687 (adverse sign), no bound otherwise | COND (float scan) |
| 11 | E-Λ± index: unfixed; j ≥ 2 and j ≤ 1240 | COND (cited E₈ facts; j labelled) |
| 12 | E-Λ±: J_M5 ≥ 0 for every admissible j and both σ | COND (rows 10–11) |
| 13 | E-S±: J_M5 ≥ 0 (min ratio 0.999597502970797) | COND (float scan) |
| 14 | M-loc obstructed for every candidate (N_M5 ≠ 0) | PROVED as implication of the unbackreacted wall |
| 15 | global realisation of the positive smeared J_M5 by actual M5 curves | OPEN |
| 16 | BPS/calibrated positivity and wall SUSY | OPEN |
| 17 | which candidate is the physical 1a datum | OPEN (nothing adopted) |
| — | σ (relative instanton/M5 sign) unfixed; both signs reported | bookkeeping |

**Tally (graded rows 1–17):**
- PROVED 10: rows 1–9 and 14.
- COND 4: rows 10–13.
- OPEN 3: rows 15–17.
- REF 0.
- Total 10 + 4 + 3 + 0 = 17, plus 1 bookkeeping row and the junction UNSOLVED.

## Branch status (pending PP)
- **cc21b272 row 22** ("some candidate solves the pointwise wall Bianchi with J_M5 ≥ 0 / is SUSY"). Proposed split:
  - the Bianchi/J_M5 part becomes **PROVED as an implication for E-0 and E-T** (M-s, premises HW, unbackreacted wall, Or), and COND for E-Λ± and E-S±;
  - the SUSY and realisation parts stay **OPEN**.
- **cc21b272 row 23, 0069b9ae row 12, 51cd8bc8 row 13** (the physical datum): stay **OPEN**.
- **Unchanged:**
  - B1-c2′ COND, not adopted;
  - 1a not adopted, pure form REF (fe0c3d92), rescues OPEN;
  - E-T and E-S± lift restorations pending PP.
- MR2 edits none of these files.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, MATCH at 10:17 CST and at write.
