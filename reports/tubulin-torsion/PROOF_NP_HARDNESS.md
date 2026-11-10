# PROOF — NP-hardness of RPP({0,1}) (Lemmas 1–3, formalized)
Definitions: DEFINITIONS.md. Known: Subset Sum is NP-complete (Garey–Johnson 1979 [SP13]; Karp 1972).

## Lemma 1 (Injection). Status: PROVED
Map SS instance (a_1..a_n, T) to RPP instance f(a,T):
- Σ := Σ a_i. If T > Σ, output a fixed NO instance (n=1, w_1=1, M=4, s=(0,0), t=(1,2), L=1; reachable residues are 0,1 only).
- Else: w_i := a_i, C = {0,1}, M := 2^{k}, k := ⌈log2(Σ+1)⌉+1 (so M > Σ), s := (0,0), t := (n, T), L := n.
Time: computing Σ, comparing, writing M in binary: O(total bits) arithmetic → polynomial. Output size O(input size + log Σ). ∎

## Lemma 2 (Structural barrier = layering + no wraparound). Status: PROVED
(a) Layering: every edge goes from layer i−1 to layer i, so every s→t path has length exactly n and visits exactly one vertex per layer; thus L = n imposes nothing beyond reachability and "leakage" to intermediate states is impossible by construction.
(b) No wraparound: for any x ∈ {0,1}^n, 0 ≤ Σ x_i a_i ≤ Σ < M, so the map x ↦ (Σ x_i a_i mod M) agrees with the integer sum.
The PDF's Lemma 2 (det(H) ≠ 0 "isolates binary choice") is NOT needed and is not proved; the binary choice is enforced by C = {0,1} in the edge definition. Hankel moved to PROOF_HANKEL_POSITIVITY.md.
Proof of (a): by D3 edges change layer by exactly +1; a path from layer 0 to layer n therefore has n edges. ∎

## Lemma 3 (Soundness and completeness). Status: PROVED
Claim: (a,T) ∈ SS ⇔ f(a,T) ∈ RPP.
Case T > Σ: no subset sums to T; fixed instance is NO (from (0,0) one reaches (1,0),(1,1) only). ⇔ holds.
Case T ≤ Σ.
(⇒) Let x solve SS. Define r_0 = 0, r_i = r_{i−1} + x_i a_i mod M. Each step (i−1,r_{i−1})→(i,r_i) is admissible with c = x_i. r_n ≡ Σ x_i a_i = T (mod M), and since 0 ≤ T < M, vertex (n,T) = t. Path length n ≤ L.
(⇐) Let P be an admissible s→t path of length ≤ n. By Lemma 2(a) it is (0,r_0)…(n,r_n) with r_0=0, r_n=T, and for each i some c_i ∈ {0,1} with r_i ≡ r_{i−1} + c_i a_i. Summing: T ≡ Σ c_i a_i (mod M). Both sides lie in [0, M−1] (Lemma 2(b) and T ≤ Σ < M), so T = Σ c_i a_i: x := c solves SS. ∎

## Theorem A. RPP({0,1}) (succinct encoding) is NP-complete. Status: PROVED
NP-hard: Lemmas 1, 3 give a poly-time many-one reduction SS ≤_p RPP.
In NP: certificate = sequence (c_1..c_k) ∈ C^k with k ≤ min(L, n) (paths of length > n do not exist by layering). Verifier recomputes residues mod M (poly-size integers), checks the endpoint layer/residue equal t and k ≤ L. A path corresponds to such a sequence and conversely. Certificate size O(n). ∎
Remark (PROVED): weakly NP-hard only; O(n·M) DP decides it, so with M in unary / explicit G it is in P. Nothing here concerns biology, 22D lattices, or quantum resonances.
