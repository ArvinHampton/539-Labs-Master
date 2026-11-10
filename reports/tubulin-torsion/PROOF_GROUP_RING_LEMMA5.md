# PROOF — Lemma 5 (group-ring reading, Owner t58u). Definitions: DEFINITIONS_GROUP_RING.md.

## A. Positive coefficients ⇒ no cancellation. Status: PROVED
If all a_{i,c} ≥ 0 then σ ≥ 0 for every path, so W = N and Γ = 0. Proof: sum of nonnegative terms. ∎ (No determinant used.)

## B. Signed bound. Status: PROVED
For any a_{i,c} ∈ ℤ: |W| ≤ N ≤ ∏_i ‖h_i‖_1 = spr(ρ(|T|)).
Proof: |Σσ| ≤ Σ|σ| = N (triangle). N is an entry of ρ(|T|) whose column sums equal ‖|T|‖_1 = ∏‖h_i‖_1 (augmentation ε: ℤ[G]→ℤ is a ring hom), so each entry ≤ that. For a nonnegative circulant, the all-ones vector is a Perron eigenvector with eigenvalue = row sum, hence spr(ρ(|T|)) = ∏‖h_i‖_1. ∎
Also |W| ≤ ‖ρ(T)‖_2 = spr(ρ(T)) = ∏ spr(ρ(h_i)) (circulants normal and simultaneously diagonalized). ∎

## C. What det ρ(H) ≠ 0 buys. Status: PROVED (negative)
C1. det ρ(h) ≠ 0 ⇔ ĥ(k) ≠ 0 ∀k ⇔ h is a non-zero-divisor (indeed a unit) in ℚ[G] ≅ ∏ ℚ(ζ_d). It is invertibility only.
C2. det ≠ 0 does NOT eliminate signed cancellation. Counterexample (verified numerically): M=3, h_1=[0]+[1], h_2=−[0]+[1]+3[2]. det ρ(h_1)=2, det ρ(h_2)=36. Paths 0→1: (c: 1 then 0) σ=1·(−1); (0 then 1) σ=1·1; W = 0, N = 2, Γ = 2. ∎
C3. With ℤ⁺ coefficients, Γ = 0 by A regardless of det. det is irrelevant to cancellation; residue collisions are controlled by M > Σ (PROOF_NP_HARDNESS Lemma 2b), not by det.

## D. "Cancellation bounded by the regular spectral radius". Status: PARTIAL
Precise proved inequality: 0 ≤ Γ ≤ N ≤ spr(ρ(|T|)) = ∏‖h_i‖_1 (from B), for all signed coefficients, with no det hypothesis. Under ℤ⁺ coefficients Γ = 0 (stronger, trivial). The claim's causal link "det ≠ 0 ⇒ bound" is FALSE as implication content (det plays no role; C2). The phrase "total cancellation" is ABSENT-as-written; GR5 reading invented pending mathematical proof. Under reading (b), vacuous (GR2').

## E. Weak NP-completeness on the slice det ρ(H) ≠ 0, coefficients ℤ⁺. Status: PROVED (reading (a), C={0,1}, a_{i,c}=1)
E1. Standard reduction has det = 0 often: M = 2^k, h_i = [0]+[w_i], ĥ_i(k') = 1+ω^{k'w_i}; at k' = M/2, = 1+(−1)^{w_i} = 0 for w_i odd. ∎
E2. Lemma (odd M). If M odd, 1+ω^j ≠ 0 ∀j. Proof: 1+ω^j=0 ⇒ ω^j=−1 ⇒ (−1)^M = ω^{jM} = 1, contradiction for M odd. ∎ (If w_i ≡ 0, h_i = 2[0], det = 2^M ≠ 0.) Hence det ρ(h_i) ≠ 0 ∀i and det ρ(T) = ∏ det ρ(h_i) ≠ 0.
E3. Modified reduction: Lemma 1 with M := 2^k + 1 (odd, > Σ); NO-instance M := 5. Lemma 2b/3 used only M > Σ (resp. reachable residues {0,1} ∌ 2 for NO case), so SS ≤_p RPP-slice. NP membership: Thm A certificate; slice membership is poly-checkable for C={0,1}, unit coefficients: det = 0 ⇔ M even and v_2(gcd(w_i,M)) < v_2(M) for some i (1+ω^{kw}=0 ⇔ kw ≡ M/2 mod M solvable ⇔ gcd(w,M) | M/2). ∎
Weak only: O(nM) DP still applies. General ℤ⁺ multiplicities / larger C: hardness holds (contains the slice above as a promise subclass); poly-time checkability of det ≠ 0 there not addressed → NF-WHY.

## Lemma 5 overall: PARTIAL. A, B, C, E PROVED; D proved as the inequality above, its det-causation FALSE; "total cancellation" phrase invented pending mathematical proof; G := ℤ/Mℤ reading invented pending mathematical proof.
