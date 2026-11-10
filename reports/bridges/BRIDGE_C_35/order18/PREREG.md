# PREREG order18 — A2 minus the explicit completion and line terms; new residual-internal maps
Written 2026-10-24 (America/Chicago) BEFORE any order18 numerics. CORE_FREEZE. Data read-only: order4b/data/A2.npz (A0,A1,A2 at XS and at −1/x; 216×105). Conventions as order17 (q=e(x)e^{−t}; Π± = ½(I±P); B̄1(u) = {u}−½ (0 at integers); B2(u) = {u}²−{u}+1/6).

## Category A arguments (written now)
(a) A2(F̂_odd) = 0 (order17 Thm R). (b) A2(R_c) = 0 for each wall correction: the sum along the wall direction is exact to O(t^∞); the transverse sum Σ_{a∈ρ+NZ} h(√t a), h odd with a jump only in even derivatives, equals 2B̄1(ρ/N) + O(t) (the B2·h′ terms of the two half-lines cancel since B2(1−y) = B2(y) and h′ is even). Hence A2(S^o) = 0.
(c) A2(S^E), E = χ++ + χ−− (half weight on half-axes, ¼ at 0): on a coset class r (phase f_r constant, coordinates ρ1, ρ2 = values of ν1, ν2 on the class, period N), iterated Euler–Maclaurin (paper Lemma EM1, third line) with h = e^{−Q(w)} gives for χ++ the t^0 coefficient B̄1(ρ1/N)B̄1(ρ2/N) − ½B2(ρ1/N)∫_0^∞∂1h(0,w)dw − ½B2(ρ2/N)∫_0^∞∂2h(v,0)dv = B̄1B̄1 + ½B2(ρ1/N) + (7/4)B2(ρ2/N); χ−− gives the same (B̄1B̄1 and B2 are even). So ½A2(S^E) = Σ_r f_r [B̄1(ρ1/N)B̄1(ρ2/N) + ½B2(ρ1/N) + (7/4)B2(ρ2/N)] =: A2_corner.
(d) Lines (order16 identity): for a line ν0 + b u (Q(u)>0, l = B(ν0,u)), weight w(b) = w+ (b≥0 large), w− (b<0 large), finite remainder δ(b): t^0 coefficient = w+[−m·l/(2Q(u)) − Σ_{ρ<N} f(ρ)B1(ρ/N)] + w−[m·l/(2Q(u)) − Σ_{ρ<N} f(−ρ)B1(ρ/N) − f(0)] + Σ δ(b)f(b), B1(y) = y−½, m = mean f; points h1h2 add weight×phase. Sum = A2_lines.

## Maps (hashed here, before testing)
- **Map RG3 (residual-internal, NEW):** Π−(A2_lit − A2_lines) = 0 (the odd sector has no t^0 term after line removal). Gate: e3 = ‖Π−(A2_lit−A2_lines)‖_F / ‖Π−A2_lit‖_F. PASS ≤ 1e−9; FAIL > 1e−6; else inconclusive.
- **Map RG4 (residual-internal, NEW):** A2_lit = A2_lines + A2_corner exactly. e4 = ‖A2_lit − A2_lines − A2_corner‖_F/‖A2_lit‖_F, same thresholds, on both the x and the −1/x sets.
No Resonant-side (T3 / O_res / Π) object is used or invented; E1–E3 remain OPEN.

## Test T (A2c law, Category B)
A2c := A2_lit − A2_lines − Σκ_c A2(R_c) = A2_lit − A2_lines (by (b)). Law: r(w) = min_κ ‖S − κ x^{−w}35^{−1/2}M A2c‖/‖S‖, S = A2c(−1/x). Primary w = −½ (weight-½ law at t^0); secondary w = −1 (law induced by weight 1), w = 0. PASS r ≤ 1e−8; FAIL r ≥ 1e−3. Zero-target guard: if ‖S‖_F/‖A2_lit‖_F < 1e−10 the verdict is "vacuous". Control C0 as order17 (A0 fixed-M law ≤ 1e−10) gates everything.
**Predictions:** RG3 PASS; RG4 PASS; T FAIL at all w (P-even, Lemma W; A2c = A2_corner ≠ 0).
FAIL recorded by these rules before any post-hoc. nice, OMP_NUM_THREADS=1, <3 GB; no push/sends; new files only.
