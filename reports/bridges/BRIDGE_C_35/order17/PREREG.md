# PREREG order17 — A1 minus the explicit completion; Zwegers law as Category A
Written 2026-10-24 (America/Chicago) BEFORE any order17 numerics. CORE_FREEZE. Data read-only: order3/data/parts.npz (A1 literal at x∈XS, and at −1/x; 216 points × 105 companions, column order = symbols FAM×35).

Conventions. q = e(x)e^{−t}, τ = x + i t/(2π), y = t/(2π). A_j(x) = coefficient of t^{(j−2)/2} of S(e(x)e^{−t}). P-odd/even projections Π± = ½(I ± P) act on the companion index (Lemma Pinv: A_j(PS) = P·A_j(S)). Weights: literal W, ν-sign p, odd part o = −¼s1 + ¼s2 − ½s3, even part ¼(1+s1s2).

## Part 2 (Category A, written here; no numerics needed)
**Proposition Z.** Ĥ = ½(Ŝ^{c1}+Ŝ^{c2}) and Ĝ_O = ½(Ŝ^{c1}+Ŝ^{c'}) satisfy, for every companion, F̂(−1/τ) = τ·35^{−1/2}·M F̂(τ) and F̂(τ+1) = T F̂(τ), with χ = 1, M, T the formal matrices of the paper.
Proof. In Zwegers' notation (thesis, Cor. 2.9; Q(x)=½xᵀAx, A=[[2,7],[7,7]], r=2, det A=−35, A* = (2,7)), ϑ̂_{a,b} = Σ_{ν∈a+Z²} ρ̂(ν) e(Q(ν)τ + B(ν,b)) with ρ̂ = E(B(c1,ν)√y/√−Q(c1)) − E(B(c2,ν)√y/√−Q(c2)), c1,c2 ∈ C_Q (Q<0, same component). Cor. 2.9: ϑ̂_{a,b}(τ+1) = e(−Q(a) − ½B(A^{−1}A*, a)) ϑ̂_{a, a+b+½A^{−1}A*}; ϑ̂_{a,b}(−1/τ) = (i/√35)(−iτ) e(B(a,b)) Σ_{p∈A^{−1}Z²/Z²} ϑ̂_{b+p,−a}. Here ½A^{−1}A* = (½,0) = hA and (i)(−iτ) = τ. These are verbatim the S and T rules from which S_rows/T_rows (hence M, T) are built; the reduction rules (shift of a by Z², shift of b by A^{−1}Z²) hold termwise for every ν-dependent weight, and closure of the 105 companions under the rules is the exact (Q-arithmetic) computation in S_rows/T_rows (it raises if a pair is not found). Pairs: Ĥ uses (c1, −c2) = ((−1,1),(−4,1)): Q = −5/2, −17/2, B(c1,−c2) = −20 < 0. Ĝ_O uses (c1, −c′) = ((−1,1),(−7,2)): Q = −5/2, −35, B = −35 < 0. E is odd, so ½(E(s_{c1})+E(s_{c})) = ½ρ̂ for the pair (c1,−c). ∎
So sh2 is upgraded to Category A (citation + exact identity). What remains Category B: nothing for this statement; the numeric agreement (orders 5,6,11) is corroboration only.

**Theorem R (radial triviality).** For every companion and rational x, F̂_odd := ½Ĝ_O − Ĥ satisfies F̂_odd(x + i t/2π) = O(t^K) for all K. Hence every A_j of the completed P-odd series is 0.
Proof. Phases e(xQ(ν)+B(ν,β)) are N-periodic on α+Z² (N = 2·den(x) times a fixed factor; checked exactly per case). On each coset ν_r + NZ² the sum is Σ g(√y ν), g(w) = (½ρ̂_O − ρ̂_H)(w) e^{−2πQ(w)}, which is Schwartz (derivatives of E are Gaussians in s; Zwegers' cone estimate gives decay of ρ̂e^{−2πQ}), so Poisson gives (N²y)^{−1}∫g + O(y^∞), and ∫g = 0 since g is odd. ∎
**Corollary R1.** A1(S^o) = −A1(corr), corr = Σ_c κ_c (E(s_c√y) − sgn s_c)-series, κ_{c1} = −¼, κ_{c′} = ¼, κ_{c2} = −½. For a wall with primitive direction d, unimodular basis (e,d), a = transverse coordinate (a ∈ a_α+Z), φ(ρ) = mean over one period of the phase on the line a = ρ:
  A1(S^o) = −Σ_c 2κ_c √(π/Q(d_c)) Σ_{ρ ∈ a_α + {0..N−1}} φ_c(ρ) B̄1(ρ/N),  B̄1(u) = {u} − ½ (0 at integers).
(Derivation: Gaussian sum along d is exact to O(y^∞); the transverse sum has a jump −2κ at a=0; Euler–Maclaurin with jump gives the constant 2κB̄1; ∫ = 0 by oddness.) Walls: c1: d=(0,1), e=(1,0), Q(d)=7/2; c′: d=(1,0), e=(0,1), Q(d)=1; c2: d=(21,−1), e=(1,0), Q(d)=595/2.
**Line terms A1 (from order16 identity).** Along a line with direction u, Q(u)>0, and asymptotic weights w± at b→±∞: A1 = (√π/2)Q(u)^{−1/2}·mean(phase)·(w+ + w−). From W − p: h2-lines (ν2 fixed): w+ = h2, w− = 0, u=(1,0); h1-lines (ν1 fixed): w+ = h1 − ½g1, w− = −½g1, u=(0,1); g3-lines (n+21k=m): w± = −½g3, u=(21,−1). Points contribute O(1) only.

## Part 1 test (Category B)
**Exact subtracted terms.** A1c := A1_lit − A1_lines − A1_pred(S^o), with A1_pred(S^o) the Corollary R1 formula. By Theorem R this equals A1(S^p) + A1(corr) = A1(F̂_odd) + ½A1(S^E) = ½A1(S^E). The P-even Laplacian defect is NOT an additive term of any series (it is (Δ₀−¼)Φ_orth), so nothing is subtracted for it; no P-even completion in the (M,T) class exists (Lemma W).
**K1 (consistency gate, tests Corollary R1 + line formula + P):** e_K1 = max over points (x and −1/x sets) of ‖Π−(A1_lit − A1_lines) − A1_pred‖ / max(‖Π−A1_lit‖, 1e−3). PASS ≤ 1e−9; FAIL > 1e−6; else inconclusive.
**C0 (control gate):** fixed-M law on A0: r0 = ‖A0(−1/x) − x^{−1}35^{−1/2} M A0(x)‖_F / ‖A0(−1/x)‖_F ≤ 1e−10 else verdicts void.
**T1 (primary, as requested):** weight-½ fixed-M law for A1c: r(w) = min_{κ∈C} ‖S − κ x^{−w} 35^{−1/2} M A1c‖_F / ‖S‖_F, S = A1c(−1/x), w = ½. PASS r ≤ 1e−8; FAIL r ≥ 1e−3; else inconclusive.
**T2 (secondary):** same for w = 0 (the order-t^{−1/2} law induced by a weight-1 law) and w = 1; and T1/T2 applied to Π+A1c and Π−A1c separately (Π−A1c ≈ 0 by K1 is reported as vacuous, not as a pass).
**Predictions (written now):** K1 PASS; T1 FAIL; T2 FAIL for Π+ (no P-even completion).
FAIL is recorded by these rules before any post-hoc work.

## Maps
No new Residual–Resonant map arises from this stage; none is proposed. Maps E1–E3 remain OPEN. Framing ("local mock / non-local quantum modular", "residual geometric bridge") stays opinion.
## Runs
nice, OMP_NUM_THREADS=1, <3 GB. No push, no sends. New files only.
