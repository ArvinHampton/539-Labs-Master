# ADDENDUM D — Owner 17:56 three theorems (same review; bounded reasoning only; No CERT)
## I Character table
- PROVED: X[ψ,a]=ψ(a) over the 48 characters and 48 units of U140; XX*=48I; X^{-1}=X*/48 (unitary up to scale, nonsingular).
- FALSE/UNSUPPORTED: U140 (order 48, C2×C4×C6) does not "represent cyclic components" of Gal(ℚ(ζ49)/ℚ)≅U49 (cyclic order 42). The two groups are not isomorphic (48≠42).
- Partial bridge: reduction mod 7 gives surjections U140→U7 (kernel order 8) and U49→U7 (kernel order 7). PROVED. U7 (cyclic order 6) is a common quotient only; it gives no field descent, says nothing about the 503-dim kernel, and does not resolve reconstruction. The 48-dim function space on U140 is ≠ cyclotomic descent. Reconstruction stays OPEN.
## II Bianchi IX metric −dt²+Σa_i²σ_i²
- Valid: in 4D vacuum, R_abcd=C_abcd. So C≠0 ⇔ spacetime non-flat.
- Proposed C1212 formula: NOT verified. It depends on the coframe and structure constants (dσ_i=±½ε_ijk σ_j∧σ_k vs ±ε…), which are not stated. Missing derivation: coframe e^i=a_iσ^i, connection 1-forms, full Riemann components.
- FALSE as an inference: "a_i unequal ⇒ bracket nonzero". The bracket is X²−Y²; it vanishes whenever |ȧ1/a1−ȧ2/a2| = |a1²−a2²|/(a1a2), which unequal a_i do not exclude. Also the a_i are not arbitrary: they must solve the vacuum ODEs plus the Hamiltonian constraint with admissible initial data.
- Existence (literature, cited not reproved here): Taub (a1=a2≠a3) is an explicit non-flat vacuum Bianchi IX solution; generic all-unequal Mixmaster vacuum solutions exist (Cauchy problem), with curvature unbounded toward the singularity (Ringström 2001). So non-flat, unequal vacuum Bianchi IX solutions exist → C≠0 somewhere. That does NOT give C≠0 pointwise for all t, any "stable microstates" (stability is separate and unproved; Mixmaster is chaotic and recollapses per Lin–Wald), or a 5D embedding or junction. Geometric block NOT closed.
## III Graph energy
- PROVED: finite connected graph, w_xy=w_yx>0, L=weighted Laplacian. LΦ=q solvable ⇔ Σ_x q_x=0; the solution is unique up to adding a constant. If q≠0 then Φ is nonconstant. Energy identity Φᵀq=ΦᵀLΦ=Σ_edges w(Φx−Φy)² holds at each time (it is gauge-invariant when Σq=0). For q(t) continuous, Φ(t) can be chosen continuous (pseudoinverse).
- Example: 2 vertices, w=1, q=(1,−1), Φ=(½,−½); energy=1=Φᵀq. ✓
- Defining N:=Φᵀq and |W|:=energy makes N=|W| a TAUTOLOGY (energy balance) at every t, with no time integral needed. This does NOT prove anything about the original path count N or the complex path sum |W|; a link identity is still missing.
- q=βS_eff T3·Ad_(ζ^t−1)∧… : untyped (what vector space? how Ad acts? what is the ∧?). Σq=0 is not automatic and must be shown.
Distinctions: proved ≠ could exist ≠ stable ≠ certified. No CERT.
