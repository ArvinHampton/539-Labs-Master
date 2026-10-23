# A61 REPORT: proof status of every asserted step of the local-CLT layer and the tail step (g_k, odd k = 17..33, N1 = 1500)

Category A (computer-assisted mathematics). Scope: the steps listed in `prereg.md` (28 items, fixed 2026-10-22 22:05:05 CDT, sha256 e2adfff0...df13, `prereg.sha256`, `mtime_prereg.txt`) for the local-CLT layer (A56 `clt56.py`/REPORT, A59 `DERIVATION.md`) and the tail step (A56 `tails56.py`, A57 section 3.2). No statement beyond that. Times America/Chicago (CDT), filesystem mtimes (self-attested). Proofs are in `PROOFS.md`; finite checks in `code/`, outputs in `out/`.

## 0. Outcome

* All 28 items now have a written proof. **No item is false as stated, and no constant has to change** (so δ, R_k, D_0 and T are exactly those of A56/A57/A59; no block rerun was needed, none was done).
* The two known items: (1) the shift bound is **proved with the stated constant 1**, via a one-line argument (|1-p+pe^{iy}|² = 1-4v sin²(y/2) >= cos²(y/2), |1-p-pe^{iy}| <= (1-2p)+p|y|); (2) the cos-sum bound is **true as stated** (Abel summation with nonnegative, monotone partial sums C(J) >= (J+1-X)/2; a naive Abel bound would not give it).
* One partial item: the upper bound log A_n(e^{-u/n}) <= nΦ1(u)+log 2+g(u) is claimed in the A56 docstring for all n; I prove it for **even n** (even with log 2 only, no g), the only case used (e_n are even-n terms). For odd n the stated form is not proved here and not needed.
* Remaining dependencies (said exactly in section 5): the numbers are produced by A56/A59 code that I checked against the proved lemmas by reading and by containment tests, not by a from-scratch A61 reimplementation of the A56 layer (the tail inequality WAS re-implemented from scratch, `code/tail61.py`, and closes for all odd k = 17..33).

## 1. Status table (items numbered as in prereg.md; all hypotheses in PROOFS.md)

| # | item (statement) | status | where used |
|---|---|---|---|
| 1 | Shift bound: |h(1-h)(1-2h)| <= v((1-2p)+p|y|)/cos(y/2)³ <= (v(1-2p)+t v p)/cos(t/2)³, 0<p<=1/2, |y|<=t<π, h = pe^{iy}/(1-p+pe^{iy}); geometric analogue w(1+w)/(1-w)³; assembly sup|f'''| <= n⁴κ(τ0) | **Proved** (constant 1, equality at y=0) | A56 `kappa` -> D1, every A56 cell (A57 layer) |
| 2 | Abel bound: Σ_{odd j<=n}v_j(1-cos jθ) >= Σ_{odd j>=1/|sinθ|+1}v_j for v nonincreasing; integral form with Y0 | **Proved** | A56 region B (DB), every cell |
| 3 | Region C: Σ >= (n/2)∫_{1/n0}^{1/2}v(ub y)dy for θ = π-φ, φ<=1.5/n | **Proved** | A56 DC |
| 4 | Region A: |φ| <= exp(-n(b_o+b_g)) from 1-cos x >= x²/2-x⁴/24, sin²x >= x²-x⁴/3, chord bound ell | **Proved** | A56 DA |
| 5 | D1 = K3/(6√(2π)σ³(1/2-c/6)²), c = τ0κ/S_lo < 3, uniform in n >= 1467 | **Proved** (all cells c <= 1.187) | A56 D1 |
| 6 | D2: erfc(σθ0/√2) <= e^{-z²}/(z√π) | **Proved** | A56 D2 |
| 7 | δ = D1+D2+D3 decomposition, sup over all integers m | **Proved** | A56, A59 |
| 8 | `sumenc` odd/geometric lattice lemmas (TV and midpoint), derivative formulas, sum identities | **Proved**; 7 derivative identities exact (sympy); 2079 exact-sum containment checks, 0 violations | A56 all S, M, K3, K4, W enclosures |
| 9 | n^a e^{-nβ} nonincreasing for nβ >= a; all "mono" flags | **Proved**; flags true in 312/312 cells (sharp, c15, A57) | A56 D3 uniformity |
| 10 | Cell lists contiguous and covering [UA(1-k/N1), UB(1+k/N1)], k=17..33 | **Proved** (exact rational check) | A56 `blocks56.cover`, A59 blocks |
| 11 | Product form, E-O identity, tilted model | **Proved**; exact checks (6416 (k,d) pairs; GF identity n<=6) | everywhere |
| 12 | Lemma 5: |φ| <= exp(-B_tot), geometric ν = 4w/(1+w)² | **Proved** | A59 Q |
| 13 | Lemma 6: (1-cos y)/y² decreasing on (0,2π] | **Proved** | A59 regimes I-III |
| 14 | Lemma 7: block bound m-1/|sinθ|, (4.2) with 1/4 and tanh form | **Proved** | A59 regime IV |
| 15 | Regimes I, II, III, V (incl. Lemma 8) | **Proved** | A59 Q |
| 16 | Regime IV | **Proved** | A59 Q |
| 17 | Lemma 4: K4 <= Σ j⁴Φ_B + Σ(2l)⁴Φ_G (derivative polynomials, |h| <= H, Φ_G identity) | **Proved**; symbolic identities exact; float sanity ratio 0.9975 | A59 main arc |
| 18 | Main arc (3.1)-(3.2), a3*, a4*, ε = k4τ0²/(12 S_lo), uniform in n | **Proved** | A59 M |
| 19 | Section 5 midpoint enclosures (cell geometry odd/even/geometric, (h²/24)b sup|F''|, count correction) | **Proved** | A59 all sums |
| 20 | Block inequality: algebra of R, existence of saddle u, m_± >= 0 automatic, weights <= O_d | **Proved** | A56 `blocks56`, A59 `block59`, A57 |
| 21 | Φ1 closed form with dilogarithms | **Proved** (derivative argument; was only checked to 1e-25; now also 1e-57 in arb) | A56/A57 tail |
| 22 | log A_n bounds: upper (even n) nΦ1+log 2; lower (all n) nΦ1-(1/2)log 2-g | **Proved** (upper for odd n as stated: not proved, not used) | tail (Chernoff, C*) |
| 23 | Chernoff; F convex in α; tangent and endpoint evaluation | **Proved**; tail re-implemented without tangent: closes | tail |
| 24 | Tiny-α part: F_tiny, log(2D/k)+1, 1-e^{-x} >= xe^{-x/2}, u_c = kα²/2 | **Proved** (A56 constants valid); 3200 arb checks | tail |
| 25 | Monotone in D: gap <= -2.5/√D, tiny gap <= -4.5/√D, nested windows | **Proved** | tail (T(D0) <= 0 implies all d >= D0) |
| 26 | Central odd term: existence of odd n*, u*-bracket, C* formula | **Proved**; 1512 exact checks of constants | tail |
| 27 | Window: α ∈ [α1,α2] implies n >= N1 and u ∈ [UA,UB]; D0 | **Proved** | block range, D0 |
| 28 | Assembly: E_d <= (R+η_t)O_d | **Proved** | A56/A57 conclusion |

Counts: Proved 28 (item 22 with the parity qualification above); Proved with corrected constant 0; Not provable as stated 0.

## 2. The two known items in detail

Item 1. Variables: Bernoulli odd j <= n, p = p_j = 1/(1+e^{ju/n}) ∈ (0,1/2), v = p(1-p), y = jθ, |θ| <= θ0 = τ0/n so |y| <= t_j = jτ0/n <= τ0; τ0 ∈ {0.1,...,1.2} (A56 sharp grid 0.05·i, i = 2..24, i.e. <= 1.2), <= 1 (c15), <= 1.5 (A59). n >= n0 = 1467, u ∈ [0.19,3.31] (A56) or [0.40,2.90] (A59). Statement and proof: PROOFS item 1. Since t·K4a·n⁴ = Σ j³ t_j v_j p_j, the formula κ(τ0) = (K3a + τ0K4a)/cos(τ0/2)³ + 8 KGr of `clt56.py` is the exact sum of the per-term bounds with the denominator relaxed from cos(t_j/2) to cos(τ0/2). The "worst ratio 0.99958" of A59 is the approach to equality at y -> 0; my float sweep over p ∈ (0,1/2], 0 <= |y| <= t, t = 0.05..1.5 gives 0.99990 and the intermediate bound v((1-2p)+p|y|)/cos(y/2)³ gives ratio exactly <= 1 (`out/out_chk03a.txt`).
Item 2. Variables: v_j = v(ju/n) nonincreasing, θ ∈ [1.5/n, π-1.5/n], X = 1/|sin θ| <= n/(1.5(1-1.5²/(6n²))), Y0 = 3/n0 + 1/(1.5(1-1.5²/(6n0²))) < 1, n >= 1467. Statement and proof: PROOFS item 2; A59's Lemma 7 (block form, 1/|sinθ|) is item 14. Both forms are now proved.

## 3. δ and R for k = 27..33: unchanged

Since no constant changed, the existing numbers stand; they are quoted from the existing files (not recomputed by A61):
| k | max block δ (A56 sharp, window incl. tilts) | R_k (A56/A57 SHARP) | A59 R_k | tail T(D0) A56/A57 (tangent) | T(D0) A61 `tail61` (no tangent) |
|---|---|---|---|---|---|
| 27 | 0.05526 | 0.83798 | 0.7905 | -27.62 | -25.48 |
| 29 | 0.05641 | 0.85970 | 0.8068 | -26.95 | -24.71 |
| 31 | 0.05761 | 0.88196 | 0.8229 | -26.10 | -23.85 |
| 33 | 0.05905 | 0.90522 | 0.8391 | -25.05 | -22.78 |
(A59 max cell δ over its 500 cells: 0.02282..0.04546.) D0: 49 312 289 / 51 557 554 / 53 684 094 / 55 698 896 (equal to A56/A57 and to `tail61`). A byte-identical copy of the A59 block code with a changed δ input was therefore not required and was not run.

## 4. Finite checks performed (new code in `code/`, all rerunnable with `code/run_all.sh`, log `out/run_all.log`)

| file | what | result |
|---|---|---|
| chk01_symbolic.py | sympy exact: derivatives of f_v, f_p, f_3, f_4, f_lam, f_g3, f_gm; B', ..., B'''' and G', ..., G'''' polynomials; Φ_G identity; third-cumulant forms; modulus identities; ν = 4w/(1+w)²; Dirichlet sums M<=12 | 28/28 identities |
| chk02_phi1_logA.py | arb 200 bit: Φ1 closed form vs quadrature (13 u); log A_n bounds, n = 1..160 × 15 values of u; product-form identity | |diff| < 8.6e-58; 0 violations; min slack upper (even n) 0.695, lower 0.258 |
| chk03_shift_abel_sanity.py | float64 SANITY of items 1, 2 | ratio 0.99990 <= 1; 3200 Abel tests, 0 violations |
| chk04_enclosures_cells.py | exact rational contiguity/coverage; flags (mono, c < 2.9, δ >= D1+D2+D3) | all true; max c = 1.187 |
| chk05_containment.py | exact (arb) finite-n sums inside A56 `sumenc` enclosures: 7 cells × 11 n × 3 u × 9 quantities | 2079 checks, 0 violations |
| chk06_consts.py | exact μ/n², σ²/n³ inside the point constants (UA, UB, ULO, UHI, S_hi), k = 17..33 | 1512 checks, 0 violations |
| chk07_minor_arcs_sanity.py | float64 SANITY: A56 exponent bounds of regions A, B, C vs exact -log|φ| | 8640 points, 0 violations; min slack A 0.0025, B 55, C 414 |
| chk08_identities_k4.py | exact integers: E-O identity, a_n >= 0, product form; exact GF identity; float K4 sanity | 6416 (k,d) pairs; ratio 0.9975 |
| chk09_tiny.py | arb: items 24 (i)-(iv) for all odd k 3..33, 200 α each | 3200 checks, 0 violations |
| tail61.py | NEW independent implementation of T(D0) for k = 17..33 (no convexity for Ψ_low) | closes for all 9 k; T from -22.78 (k=33) to -35.07 (k=19) |
Labelled float64 SANITY (not part of any proof): chk03, chk07, and the float part of chk08. Everything else is exact, symbolic, or arb with rigorous enclosures.

## 5. Limits: exactly where a proof depends on more than mathematics

1. Items 8, 9, 15, 18, 19, 21-27 produce numbers by code (A56 `clt56.py`/`tails56.py`, A59 `clt59.py`/`riem59.py`). The mathematics behind each formula is proved in PROOFS.md and compared with the code term by term (written into the proofs), and the enclosure/constant containment tests above pass; but I did not re-implement the A56 layer (`cell()`) from scratch in A61, so a software bug in A56's cell computation that preserved all those tests would not be excluded by A61. The independent A59 implementation gives δ <= A56's in all 500 cells and A59's FFT/DP sanity is below its δ (A59 REPORT), which supports but is not a proof of A56's numerical constants. For the A57 use (k = 31, 33) the layer is A56's `cells57_sharp.json` (equal to A56's).
2. Floating-point JSON: cell edges and constants are stored as float64 and compared exactly as floats; the outward rounding by one ulp (`fl_up`, `fl_dn`) is part of the code; I verified contiguity exactly (item 10), not every rounding step.
3. Item 22 (odd n upper bound): not proved for odd n, not needed (see above).
4. Out of scope and not examined: the translation of PD into the project definitions (A57 §6 item 6), the finite modular certificate, zero sets. The A57 tail input "δ_C = max δ over the central window" is covered by item 26.
5. I did not formally verify anything in a proof assistant.

## 6. Disclosures

* First run of `chk01_symbolic.py`: 4 identities reported FAIL because `sympy.simplify` does not reduce mixed hyperbolic/exponential forms; the script was changed to `simplify(expand(expr.rewrite(exp)))` (a symbolic fix, no tolerance) and rerun: all 28 pass. A first version of three scripts wrote outputs one directory up (relative path bug); the files were moved into `out/` and the scripts fixed to use script-relative paths. A first float sweep in `chk03` had a NaN in the second ratio (division by 0 at p = 1/2, y = 0); fixed by masking.
* `code/clt56.py` and `code/arb_compat.py` are byte-identical copies of A56 `proof/clt56.py` (sha256 58010703...88ee) and `proof/arb_compat.py` (sha256 54960056...3326), verified with cmp, used only by chk05 and chk07 as the object under test. All other code is new. `tail61.py` reads A56 data files (params, point constants, cells) and uses no A56 module.
* Resource limits: nice, OMP_NUM_THREADS=1, ulimit -v 3 GB. Python-flint 0.9.0.
* Category A only; no TPC/RH statement.

## 7. Files

`prereg.md`, `prereg.sha256`, `mtime_prereg.txt`, `PROOFS.md`, `REPORT.md`, `REPORT.pdf`, `SHA256SUMS`, `code/` (chk01..chk09, tail61.py, run_all.sh, copies clt56.py, arb_compat.py), `out/` (JSON/text outputs and run_all.log).
