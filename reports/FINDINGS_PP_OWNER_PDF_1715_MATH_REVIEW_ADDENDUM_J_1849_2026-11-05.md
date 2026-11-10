# ADDENDUM J — Owner t4100 18:49 assembled master (truncated; same review; exact Legendre enumeration p<90 only; relay-based; No CERT; no .tex)

## Inert list K90
- VERIFIED COMPLETE: the primes p<90 with p∤140 and (140/p)=−1 are exactly {3,11,37,41,47,53,61,71,79,83,89}. That is 11 entries, and the list matches.
- The master's definition is DEFECTIVE. "All odd primes with (5/p)≠(7/p)" also admits 5 and 7, where (5/5)=0≠(7/5)=−1 and (7/7)=0≠(5/7)=−1.
  Correct definition: K_B = {p<B prime : p∤140, (140/p)=−1}.
- The factorization (35/p)=(5/p)(7/p) is valid, but the wording is wrong.
  - (5/p) is about splitting in ℚ(√5); by reciprocity it equals (p/5).
  - (7/p) is about splitting in ℚ(√7); it equals (p/7)·(−1)^((p−1)/2).
  - Neither symbol says "p splits mod 5" or "p is inert in a prime field mod 7".
- O=ℤ[√35] with discriminant 140: correct. (ℤ[√35] is the maximal order since 35≡3 mod 4.)
- Quotient rings (true):
  - Inert p: O/p ≅ F_{p²}.
  - Split p: O/p ≅ F_p×F_p.
  - Ramified p (2,5,7): O/p ≅ F_p[ε]/(ε²), which has nilpotents.
  - NO graph, kernel, capacity, 3-adic or stability implication follows. The ramified "collapse", split "zero divisors undermine kernel" and inert "stability" claims are UNSUPPORTED.
- Products: a product of inert primes is coprime to 140, but χ is multiplicative, so an even number of inert factors gives χ=+1. Example: 3·11=33, χ(33)=+1, which is a split class. Such products are not inert.

## Regressions in the master
- The embedding √35↦+√35 does NOT guarantee positivity, because coefficients like 1−√35 are negative.
- C_xy=σ(a_{x⁻¹y}) is the UNSHIFTED form, but the master still claims δ=Σa−a_{w⁻¹}.
  - Correct unshifted form: δ=Σ_{g≠e}σ(a_g).
  - Shifted form: φ(g)=a_{g·w⁻¹}, with twisted symmetry a_c=a_{c⁻¹w⁻²}.
  - The graph is connected iff the positive support generates G.
- Topology:
  - "Any unit action forces a high-dimensional torus" is FALSE.
  - All 48 positive gives K48 with b1=1081.
  - Involution backtracks are not homology.
  - Cycles are not a capacity obstruction.
- Self-inverse elements: 8 = identity + 7 involutions (Addendum G).
- Boundary lemma: the master proves only sufficiency.
  - Corrected statement: the solution set ≅ ker(C0+C_M P), and it is trivial ⇔ C0+C_M P is injective ⇔ C0+C_M P has full COLUMN rank (not "full row injectivity"). Both directions are proved in Addendum I.
  - It gives no dynamics and no stability.
- The conjecture redefines the original |W| as a cardinality, with no equivalence to the original.
- LaTeX: broken subscripts/braces, "$|W| |…", a missing conjecture label, and a truncated appendix with no \end{document}. It cannot compile as given. (No .tex was created and nothing was compiled.)

Original N/W/capacity: OPEN.
