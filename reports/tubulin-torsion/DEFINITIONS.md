# DEFINITIONS — Formalized Resonant Path Problem (RPP)
Source: Tubulin-to-Torsion-Pipeline.pdf (§1.2, §2, Addendum). Every definition below that is not in the PDF is a modeling choice, labelled **invented pending mathematical proof** (as a faithful reading of the PDF's intent; the definitions are mathematically precise, but that they capture the paper's "resonances" is unproved).

## D0. Input instance (binary)
Subset Sum (SS): input positive integers a_1..a_n and target T ≥ 0, in binary. Question: ∃ x ∈ {0,1}^n with Σ x_i a_i = T. NP-complete (Karp 1972; Garey–Johnson 1979, [SP13]).

## D1. Ring R — invented pending mathematical proof
R = ℤ/Mℤ, M ≥ 2 an integer given in binary as part of the instance. (Replaces the undefined "discrete ring R" / "discrete valuation ring".)

## D2. Modulus — invented pending mathematical proof
The PDF's "mod 10p²" is kept only as a *choice*: p := least prime with 10p² > Σ a_i (resp. > 2Σ b_i in the ternary case), M := 10p². (Optional; finding p is not needed.) NOTE: to avoid relying on prime search cost, the hardness proof only needs **any M > Σ a_i**; M := 2^{⌈log2(Σa_i+1)⌉+1} works and is trivially poly-time. "Ray class congruences" have no definition in the PDF and are NOT used.

## D3. State graph G = (V, E) (implicit / succinct) — invented pending mathematical proof
Given step set C ⊆ ℤ (binary case C = {0,1}; ternary C = {−1,0,1}), weights w_1..w_n ∈ ℤ, modulus M:
- V = {0,…,n} × ℤ/Mℤ (layer i, residue r).
- Edge (i−1, r) → (i, r′) is **admissible** iff ∃ c ∈ C with r′ ≡ r + c·w_i (mod M).
- No other edges. G is given implicitly by (n, w, M, C); |V| = (n+1)M may be exponential in input size, but adjacency is decidable in poly time.

## D4. Decision problem RPP — invented pending mathematical proof (as reading of PDF)
RPP(C): input (n, w_1..w_n, M, s, t, L) with s = (0, r_s), t = (n, r_t). Question: does G contain an admissible directed path from s to t of length ≤ L?
"Fast-projection operator" := the map (i,r) ↦ i (layer index) — the only structure the proof uses. Any other meaning is undefined in the PDF → ABSENT.

Caveat (proved, trivial): if G is given **explicitly** (as an adjacency list), RPP is in P by BFS; hardness holds only for the succinct encoding (M in binary), i.e. RPP is weakly NP-hard, exactly like Subset Sum (pseudo-polynomial DP exists).

## D5. Explicitly NOT used in any proof (modeling only)
- 22-dimensional "Temporal Torsion Cohomology lattice", superpotential W(φ): undefined → ABSENT.
- 22 → 13 projection / 13-protofilament mapping: invented pending mathematical proof (modeling; one could set residues mod 13 to "protofilaments", but nothing follows).
- Hankel matrix / det(H) ≠ 0: not needed for hardness; moved to PROOF_HANKEL_POSITIVITY.md.
- All biophysics (§§4–6, nuclear envelope, relativistic): not mathematical consequences of anything here.
