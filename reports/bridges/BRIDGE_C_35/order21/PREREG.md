# PREREG order21 — the near-law of X = C2b − (N²/6)G; Maps RG8a (low-|k|), RG8b (smooth defect)
Written 2026-10-24 (America/Chicago) BEFORE any order21 numerics. CORE_FREEZE. Does not touch MAPS_CANDIDATES/BATCH5_*. Inputs read-only: order19/data/rg5_arrays.npz (C2b at XS and −1/x), order4b/data/A2.npz (A0).
Notation (order20): N = period used for C2b at the point (x or −1/x separately), f_r phases on classes r mod N, ρ2 = α2+j, T_k := Σ_r f_r e(kρ2/N) = N² G_{α,β+λ_k}, c_k = DFT weights of B2 (order20 Prop. L_B), k taken in the symmetric range −N/2 < k ≤ N/2. X := Σ_k c̃_k T_k with c̃_k = c_k − δ_{k0}/6·N^{−2}·N²… i.e. X = C2b − (1/6)T_0 (T_0 = N²G). Law ℒ: Y(−1/x) = κ·x·35^{−1/2}M Y(x), κ ∈ C fitted once over all 216 points; rel(Y) = ‖residual‖_F/‖Y(−1/x)‖_F; abs(Y) = ‖residual‖_F.

## Fact used (Category A, from the multiplication theorem B2(u) = N Σ_{j<N} B2((u+j)/N)): c_0 = B2(α2)/N², so the k=0 term of C2b is B2(α2)·G_{α,β}(x), and the k=0 term of X is (B2(α2) − 1/6)·G_{α,β}(x). Characteristics β+λ_k reduce to the 105 companions iff N | k (rule (ii)), i.e. only k = 0 is inside the 105; "closeness" of β+λ_k to the companion family is measured by d_k = |k|/N (the distance of Aλ_k = (0,k/N) to Z²).

## Controls
- K0: Σ_k c_k T_k = C2b at x and −1/x, all 216×105: max abs ≤ 1e−9 (else void). Full Bernoulli S-law (order20 L_B (ii)) cited as passed (2.7e−15).
- K1: rel(X) reproduces order20 (9.5e−4) to 1e−8.

## Map RG8a (the order20 guess, as a predefined map)
X_K := Σ_{|k|≤K} c̃_k T_k (same K at x and −1/x), K ∈ {0,1,2}. **Statement:** the near-law is carried by the low-|k| part: rel(X_K) ≤ 1e−4 for some K ≤ 2 AND rel(X − X_K) ≥ 1e−2 for that K. PASS if both; FAIL if rel(X_K) ≥ 1e−3 for all K ≤ 2; else inconclusive. Also reported: joint rank [G | x·X_K(−1/x)] vs 36. Prior: FAIL (the k=0 term is a Gauss mean, which obeys the x^{−1} law, not the x^{+1} law).

## Map RG8b (residual-internal, NEW prediction: smooth defect)
Defect D(x) := X(−1/x) − κ·x·35^{−1/2}M X(x) (κ from ℒ). **Statement:** D extends smoothly in x: on the points x ∈ XS with x ≥ 1/2, a least-squares polynomial of degree 8 in x (per component, Chebyshev basis on [1/2,3]) leaves s(D) = ‖D − fit‖_F/‖D‖_F ≤ 1e−2, while the same fit on X(x) itself (control, erratic Gauss-type data) leaves s(X) ≥ 0.3. PASS if both; FAIL if s(D) ≥ 0.3; else inconclusive. Same test reported for the defect of the full A2c = A2_corner law (order19 L0) as secondary. (If PASS, this is the shape of a quantum-modular-type defect; that wording stays framing, not theorem.)

## Thresholds summary
Absolute norms reported alongside every relative number. FAIL recorded by these rules before any post-hoc work.
No Resonant-side object; E1–E3 OPEN; no bridge claim. nice, OMP_NUM_THREADS=1, <3 GB; no push/sends; new files only.
