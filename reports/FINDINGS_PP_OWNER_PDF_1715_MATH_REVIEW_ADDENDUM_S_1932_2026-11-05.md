# ADDENDUM S — Owner t4121: M = [S0; S_M R_t H] (relay-based; exact bounded 24-character evaluation + numeric cross-check; No CERT; no .tex)

## Setup
- Basis split by j: S0 = [I24 0] and S_M = [0 I24].
- R_t is translation by t = (1,2,3). It flips j, so R_t = [0 Θ_A; Θ_B 0], where Θ_A and Θ_B are permutations.
- H is the shifted conductance from R.1 (same A/B/C/D table).

## Block reduction (PROVED)
- S_M R_t = [Θ_B 0], so S_M R_t H = [Θ_B H00, Θ_B H01].
- Therefore M = [I 0; Θ_B H00 Θ_B H01].
- Row-reducing gives rank M = 24 + rank(Θ_B H01) = 24 + rank H01, because Θ_B is invertible.

## H01: exact spectrum
- H01 is the j = 1 cross block. It is a group circulant on C4 × C6: H01 = Σ_{c : j_c = 1} a_c R′_{(cy)|C4×C6}.
- Its eigenvalue for each character (q, r) is μ(q, r) = Σ_{c : j_c = 1} a_c i^{q(k_c + 1)} ω^{r l_c}.
- Exact values (value: multiplicity):
  - 0: 12. These are exactly the characters with q odd (q = 1, 3, all r). The cause is that the j = 1 weights have period 2 in k.
  - 76 + 16√35: 1
  - 4: 1
  - −4: 1
  - 2: 2
  - −2: 2
  - 10 − 8√35: 2
  - 14 − 8√35: 2
  - 20 − 8√35: 1
- The multiplicities sum to 24. The 12 nonzero values are nonzero exactly, since each is either a nonzero integer or u + v√35 with v ≠ 0.

## Verdict (exact)
- rank H01 = 12. Hence rank M = 36 and nullity M = 12. A numeric rank computation agrees (36 and 12).
- Kernel: x has zero j = 0 part, and its j = 1 part lies in the 12-dimensional span of the C4 × C6 Fourier modes with q odd.
- So M is NOT full rank. The Owner's claim that rank M = rank B = 24 is FALSE, and so is any claim of 48.

## Errors in the premises
- "row(AD) = row(A) for an invertible Fourier-diagonal D" is FALSE. Only the dimension is invariant, and only under right multiplication by an invertible matrix.
- Here H multiplies only the terminal block, not the whole matrix from the right. So even the dimension argument does not apply, which is why the rank is 36 and not 24.

## Path Theorem 3 (W = a single coefficient)
- The bounds are VALID for finite abelian G with weights in a field embedded in ℝ or ℂ, not in Z[G]: the √35 weights are not in ℤ.
- Clarify the two norms:
  - N = Π_l ||h_l||_1 is the uncollected path mass.
  - The norm of the collected product is only submultiplicative: ||h_M⋯h_1||_1 ≤ N. The ℓ1 norm does not distribute over products.
- With that, |W| ≤ ||h_M⋯h_1||_1 ≤ N, and |W| ≤ Π_l spr(ρ(h_l)) (R.1).

## OPEN
- The physical choice of selectors.
- The N/W/capacity link.
