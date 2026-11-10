# order34 PREREG (written and hashed before numerics)
Pieces (order33, pieces.py): for cone(u1,u2), T_BB = Σf·B̄1(a)B̄1(b), T_2a = Σf·(B/(4Q(u2)))·B2(a), T_2b = Σf·(B/(4Q(u1)))·B2(b).
For e1-edge cones T_e1 = T_2b and T_other = T_2a. For cones without e1 the two B2 terms have no e1 label, so the B2 part is T_B2 := T_2a + T_2b (the same object as T_e1+T_other on e1-cones).
Criterion (order31–33): w* = −1, |κ̂−1| ≤ 0.01, r(−1) ≤ 0.10. Non-vacuity: d′ from span{CO, Γ_γCO, vtx} > 1e−3.
Test set: the 9 order33 e1-cones (pieces read from order33/data/o33_pieces.npz) plus the 28 order32 control cones (26 Stern–Brocot depth 1–4 non-e1 cones, ((1,5),(0,1)) and ((1,6),(0,1))), recomputed with pieces.py. 37 cones in total.
Control: reconstruction T_BB+T_2a+T_2b = stored Cor (order30/32) ≤ 1e−12.
## RG31.1 B2 part on all cones
PASS iff T_B2 meets the criterion and r(−1) ≤ 0.01 on all 37 cones. FAIL iff more than 10% of the cones have r > 0.01 or fail the criterion. Else inconclusive.
Prediction (blind for the 28 controls): PASS.
## RG31.2 B̄1B̄1 term on all cones
PASS iff T_BB fails the criterion on all 37 cones. FAIL iff it meets it on more than 10%. Prediction: PASS.
## RG31.3 Relation to order20 Bernoulli objects (definitions recovered from order20/scripts/o20.py and PREREG: Prop. L_B; arrays order19/data/rg5_arrays.npz, C = [C11, C2a, C2b] at x, SC at −1/x)
Order20 defines C2b = Σ_r f_r B2(ρ2/N), C2a = Σ_r f_r B2(ρ1/N), C11 = Σ_r f_r B̄1(ρ1/N)B̄1(ρ2/N). Identities to test, exactly as written (no fitted scale):
 I-b: T_e1(K) = (7/4)·C2b;  I-a: T_other(K) = (1/2)·C2a;  I-11: T_BB(K) = C11;  I-n: T_e1((1,0),(n,1)) = ((2n+7)/4)·C2b for n = 1..8.
PASS each if max abs error ≤ 1e−10 (x and −1/x); FAIL if ≥ 1e−6.
If an identity fails only by a constant normalisation, the ratio is reported post hoc as a normalisation diagnostic; it does not change the verdict.
Correction statement: if I-b and I-n PASS, then T_e1 is exactly a multiple of C2b, and Prop. L_B (order20, Category A) says the S-image of C2b lies in Gauss means with characteristics outside the 105 companions. The miss r(T_e1) ≈ 0.003 is then the known L_B effect.
Consistency check: r(C2b) under the same metric equals r(T_e1) to 1e−12 (scale invariance). No new Bernoulli objects are introduced.
Naming: RG* only, no labels L1–L7. Geometric only; MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
