# order51 PREREG: R1 tail bound and R2 H7 completion data (written and hashed before numerics)
## R1: explicit bound on ‖R‖ from L_B (ii) (Category A as an inequality)
Sources: v12 Prop. bern (L_B): C2(x) = N²Σ_k c_k G_{α,β+λ_k}(x), with c_k = Σ_{n≡k (N), n≠0} e((n−k)α2/N)/(2π²n²). order43: G is a normalised mean, so |G| ≤ 1; D0 = B2(α2)·G (the k = 0 term).
Derivation:
- |Rem_j(x)| = |N²Σ_{k≠0}c_kG_k| ≤ N²Σ_{k≠0}|c_k| ≤ N²·Σ_{n≢0 (N)}1/(2π²n²) = (N²−1)/6.
- With κ = 1 and kM unitary (order47): R = (a) + (b), (a) = [(x√35)^{−1}M_b − x·kM]D0(x) (exact, from G), (b) = Rem(−1/x) − x·kM·Rem(x).
- So ‖R‖ ≤ B1 := ‖(a)‖ + ‖((N′_j²−1)/6)_j‖ + x‖((N_j²−1)/6)_j‖ (crude tail), and ‖R‖ ≤ B2 := same with Σ_{k≠0}|c_k| computed directly (sharper, still rigorous).
Test points: order43's 12 points, κ = 1.
Checks:
- R1a (validity, must hold): ‖R‖ ≤ B2 ≤ B1 at every point.
- R1b (non-vacuity, the question): B2 < ‖S‖ (= ‖C2b(−1/x)‖) at every point. PASS iff it holds at all 12 points; FAIL otherwise.
Prediction (written now): FAIL. Triangle bounds cannot see the (a) ≈ −(b) cancellation. Already ‖(a)‖ ≥ ‖R‖/0.13 (order43), and the tail term is ~N²/6 per entry.
## R2: H7 erf-completion data (exact)
Walls of H7 (v12 Open problem 1; sign forms in order18 lines()): rays (0,1) and (21,−1), with forms ν1 and ν1+21ν2. The dual vectors c with B(c,ν) = form are c1 = A^{−1}(1,0)ᵀ and c2 = A^{−1}(1,21)ᵀ.
Exact claims (Fractions):
- Q(c1) = −1/10, Q(c2) = −17/2 (both negative);
- B(c1,c2) = c1ᵀAc2 = 1/5 − 21/5 = −4 < 0 (same component of the negative cone).
These are Zwegers' hypotheses, so the completion sign(B(c_i,ν)) → E(s_{c_i}(ν)√y), with s_c = B(c,ν)/√(−Q(c)), has constants 1/√(−Q(c1)) = √10 and 1/√(−Q(c2)) = √(2/17). With v12 Prop. 37.7 (the ξ1-images X^c) this is written.
What is NOT derivable from written sources here: the order-t^{−1/2} coefficient of the completion term at rational x (needed to form A1 − Ξ_compl and test an S-law). No test of A1 − Ξ_compl is run. Ξ is identified only if such a test passes non-vacuously.
v13 only if R1b PASS (unexpected) or R2 yields a new passing law. Naming: RG* only, no labels L1–L7. MAPS_CANDIDATES untouched; no Π/α1/fibre invented; no bridge claim.
