# Addendum X: bounded check of the t4136 follow-up (relay-based; no reconstruction, simulation or drafting)

1. **Naming.** The tuned matrix must be written H′ = H + R_x, because the +1 on xy³ becomes x after the y-shift.
   - The original rank is 36, and the tuned rank is 48 (Addenda R and V).
   - Calling the tuned matrix "H", unprimed, conflates the two cases.
   - Capacity is NOT closed and remains OPEN.

2. **"rank 36 ⇒ PBP* invertible for an orthogonal projection P of rank 36": FALSE.**
   - Counterexample: N = [[0,1],[0,0]] has rank 1, but its compression to span(e1) is 0.
   - Embedding it as I₃₅ ⊕ N ⊕ 0₁₁ gives rank 36 with a singular 36×36 compression.
   - **Constructive fix.** Take U, an orthonormal basis of im B, and V, an orthonormal basis of (ker B)^⊥. Then U*BV is 36×36 and invertible.
   - Proof: B restricted to (ker B)^⊥ is injective, and its image is im B. Both spaces have dimension 36, but they are different spaces.

3. **Field equality K = Q(√35, i, √−3) = Q(i, √−3, √5, √7): FALSE.**
   - The left side has square classes {−1, −3, 35}, which are independent, so its degree is 8.
   - The right side has square classes {−1, −3, 5, 7}, so its degree is 16.
   - The left side is a proper subfield of the right side.

4. **Branch cuts.** Avoiding a branch cut has nothing to do with invertibility. The argument is a non sequitur.

5. **v3 det B_red = 0 ⇒ isometry: unsupported and FALSE in general.**
   - The value of v3 det B_red was assumed, not computed.
   - Counterexample: diag(1/3, 3) has det 1, but it sends (1,0) to (1/3,0), which has sup-norm 3.
   - Valid condition: if A ∈ GLₙ(O_{F3}), then A and A⁻¹ are both integral, so A is a sup-norm isometry.
   - A complex P does not by itself define an F3-matrix or lattice. ND.

6. **K_B.** The fix p ∤ 140 is good. The cutoff p < X must be restored if the set is claimed to be finite.

7. **VALID, unchanged:** 3 is inert in Q(√35), and 4 generates 1 + 3Z₃.

The verified tuning in Addenda R–V stands. No CERT, and the tip is untouched.
