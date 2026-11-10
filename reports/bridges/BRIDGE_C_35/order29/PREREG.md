# order29 PREREG (written and hashed before numerics)
## Recovered order17 definition (scripts/k1t1.py, PREREG order17)
"Completed law for A1" = A1 is decomposed exactly as lines + P-odd completion (A1_lit = A1_lines + A1(S^o); Thm R/E). The law tested was the fixed-M law with free scalar and weight:
r(w) = min_{κ∈C} ‖S − κ·x^{−w}·35^{−1/2}·M·Y‖_F/‖S‖_F, S = Y(−1/x), w ∈ {½, 0, 1}, applied to the full vector and to Π± = ½(I ± P), P = Γ_{−I}. PASS r ≤ 1e−8, FAIL r ≥ 1e−3.
For A2 the completion piece is A2(S^o) = 0 (order18), so "A2 lines + completion" = LN (order18 A2_lines).
## RG21 (primary)
Objects: LN (full), Π+LN, Π−LN; comparison object CO (and Π+CO = CO).
Weights w ∈ {−1, −½, 0, ½, 1} (w = −1 is the order18 weight-1 normalisation R(Y) = Y(−1/x) − x·35^{−1/2}MY). κ free (as in order17). Absolute residual a = ‖S − κ̂·x^{−w}35^{−1/2}MY‖ is also reported.
Non-vacuity: d(Y) from span{CO, Γ_γCO} > 1e−3, and ‖Y‖ ≥ 1e−6‖LN‖.
"Obey": r_min = min over w ≤ 1e−8 for LN (PASS). FAIL if r_min ≥ 1e−3; else inconclusive. Each Π± sector gets the same rule.
Corner-only isolation statement: true iff RG21(LN) PASS and CO FAIL under the same metric.
Prediction: blind with respect to this metric. Order28 found the fixed κ = 1, w = −1 law off by rel 1.78, so I predict FAIL (r_min ≥ 1e−3) for LN; the near-law is then NOT isolated as corner-only.
## RG22 (secondary) — Stern–Brocot chain of K, rule fixed now
Depth-n subdivision: rays of K = (1,0),(0,1); at each depth insert the mediants between neighbours. Cones C_{n,1..2^n} are ordered from (1,0) to (0,1) and are all unimodular.
Rule (fixed): Alt_n = Σ_{i=1}^{2^n} (−1)^{i+1} Cor_{C_{n,i}} (alternating signs by position, i.e. by the parity of Stern–Brocot position; Möbius-type alternating rule). Depths n = 1, 2, 3. (Alt_1 = A_K of order28.)
Target identity (fixed, coefficient 1, no fit): T_n: R(CO) + R(Alt_n) = 0, i.e. ‖R(CO + Alt_n)‖ ≤ 1e−8 (PASS); FAIL if ‖R(CO+Alt_n)‖ ≥ 1e−3·‖R(CO)‖.
Scale-free check (also fixed): |cos(R(Alt_n), −R(CO))| ≥ 1 − 1e−6 PASS; ≤ 0.99 FAIL.
Controls: Σ_i Cor_{C_{n,i}} = CO + ¼(2^n − 1)·vtx (iterated v8 subdivision); non-vacuity d(Alt_n) > 1e−3.
Prediction (blind): T_n FAIL for all n; |cos| < 0.99.
## Controls
C1 corner(K) = CO; C2 ‖R(CO)‖ = 54.406 (order28 value, ≤1e−9 relative).
Rules: geometric only; MAPS_CANDIDATES/DISCOVER_GRADING_PATH/MARKOV_FIBRE_FREQ untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
