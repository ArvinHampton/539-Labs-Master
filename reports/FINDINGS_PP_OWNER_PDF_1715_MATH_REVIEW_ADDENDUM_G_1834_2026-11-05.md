# ADDENDUM G — Owner 18:34 draft (same review; exact sympy on stated 4x4/3x6 matrices only; PDF/plot code NOT run; no .tex; No CERT)
Source: Physicist's relay. I did not read the full t4088u text.
## Klein-group graph (K4, edges e-a,e-b,e-ab,a-b,a-ab,b-ab; weights 2,3,1,1,3,2)
- VERIFIED: L = B_full·diag(w)·B_fullᵀ; spectrum {0,6,8,10}; rank 3; spectral gap 6; b1(K4) = 6−4+1 = 3.
- VERIFIED: grounded cofactor det = 120 = (6·8·10)/4 (matrix-tree theorem).
- Relayed reduced B (rows a,b,ab of −B_full): rank 3; B·W·Bᵀ = [[6,−1,−3],[−1,6,−2],[−3,−2,6]], which is positive definite with det 120.
- "Cycle basis" correction: e-a-e and e-b-e are backtracks with zero H1 class; e-a-ab-b-e is a single cycle. That set is NOT a basis.
- Correct basis: the fundamental triangles of the star tree {e-a, e-b, e-ab}, each in ker B (verified):
  - z1 = (1,−1,0,1,0,0): e→a→b→e
  - z2 = (1,0,−1,0,1,0): e→a→ab→e
  - z3 = (0,1,−1,0,0,1): e→b→ab→e
- Algebraic facts, PROVED:
  - ker B (cycle flows) ∩ im(W Bᵀ) (potential-driven currents) = {0}, by positive energy.
  - ℝ⁶ = ker B ⊕ im(W Bᵀ); E/ker B ≅ ℝ³; the grounded L has rank 3 even with cycles.
  - So there is no automatic capacity loss. Positive conductance changes do not change cycle homology.
- P matrix:
  - P has an identity block, so rank 3: there is NO rank drop.
  - Its columns are unsigned (not oriented incidence).
  - ker P ≠ H1. Counterexample: z1 satisfies Bz1 = 0 but Pz1 = (2,0,0).
  - "Defect 3 = b1" rests on N, |W| redefined as 6 edges and 3. This is a definition; the original capacity is NOT refuted.
  - "Number of independent paths = edges" is undefined without a stated space.
  - An arbitrary key-space size cannot be bounded by b1.
- Topology:
  - A closed torsion word is not a nonzero homology class.
  - "Boundaries avoided" is undefined.
  - A K48 with all coefficients positive is a 1-complex with b1 = 1128−48+1 = 1081 (complete graph, loops excluded), not a torus.
## U140 involutions
- VERIFIED order counts: 1:1, 2:7, 3:2, 4:8, 6:14, 12:16. So 8 elements have w² = 1 (correct). The other 40 have orders 3/4/6/12 (the Owner omits 12).
- Exponent is 12, not 6; e.g. 3⁶ ≡ 29 (mod 140).
- w = w⁻¹ does NOT imply a_{w⁻¹} = a_e (needs w = e or equal coefficients).
- The graph is degree-regular at every vertex. i is a layer index, not 8 axial nodes. The degree form does not force two capacity classes.
## Prime filter (K=ℚ(√35), D=140)
- For odd p ∤ 140: χ(p) = (140/p) = (35/p) = (5/p)(7/p). p is inert iff (5/p) and (7/p) have opposite signs. CORRECT.
- But this is not simply "(p/7)": (7/p) = ±(p/7) by reciprocity, and (7/p) is the ℚ(√7) symbol.
- Algebra (true):
  - O_K is always a domain.
  - O_K/p ≅ F_p×F_p for split p (zero divisors).
  - Ramified p (2, 5, 7): O_K/p has nilpotents.
  - Inert p: O_K/p ≅ F_{p²}, a field.
- UNPROVED: "ramified ⇒ capacity collapse", "split ⇒ undermines constant kernel", "inert ⇒ stability/cyclic protection/safe 3-adic boundary". No link from residue-ring structure to rank or capacity is given.
## Status
Original capacity / N / W: OPEN. The claimed plot run has no evidence; no execution was claimed or performed. The draft text is truncated at the final LaTeX definition; I did not review that definition.
