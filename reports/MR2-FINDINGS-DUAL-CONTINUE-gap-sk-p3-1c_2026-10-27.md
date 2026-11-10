# MR2 FINDINGS — DUAL-CONTINUE GAP-SK-p3-1c (Soft SF) — 2026-10-27
STATUS: CLOSED (Soft SF, elementary, Brauer-free) | tip_touched: NO | Kerr: BLOCKED | NOT OPERATIVE | REPORT ONLY, no RECS | no new invent values
Parents: gap-sk-p3-1a (bf07abbf…: Sym^s⊗det^a irreducible, 0≤s≤p−1), gap-sk-p3-1b (a3455f1d…).
Lit search: lit/bm grep for Brauer-free/socle-of-Ind found no written Brauer-free completeness proof (hits are context only). Proof below uses no BL94/BL95 and no Brauer count.

## Claim
Every irreducible F̄p-rep V of G=GL2(Fp) is ≅ Sym^s⊗det^a, 0≤s≤p−1, a mod p−1. (Reps of GL2(Zp) with K(1) acting trivially, i.e. smooth irreducibles, factor through G since K(1) pro-p fixes a nonzero subspace, which is G-stable as K(1) is normal.)

## Proof
B=TU upper Borel, U≅Fp, T diagonal (order prime to p), w = antidiagonal.
1. (Nonzero U-coinvariants.) (V^∨)^U≠0 since U is a p-group in char p; so V_U≠0. T normalizes U, acts semisimply on V_U; pick a T-character ψ quotient. Get nonzero B-map V→ψ (U acts trivially on ψ). Frobenius reciprocity: nonzero G-map V→Ind_B^G ψ, injective as V irreducible.
2. (Every ψ is hit by some W=Sym^s⊗det^a.) W_U is 1-dim (spanned by the extreme monomial), with T-character λ^{a}μ^{a+s} (or the w-swap, by convention). As s ranges 0..p−2 and a mod p−1, all (p−1)^2 characters of T arise. So W↪Ind ψ for a suitable W of the list (W irreducible by 1a).
3. (Ind^U.) B\G/U = {B, BwU}; dim (Ind ψ)^U = 2, basis f_B (supp B) and f_w (supp BwU), T-weights ψ and ψ^w. Translates of f_B are the coset deltas, so f_B generates Ind ψ.
4a. (ψ≠ψ^w.) Any irreducible sub X has X^U≠0 a T-stable subspace of ⟨f_B⟩⊕⟨f_w⟩ (distinct weights), so X^U ∋ f_B or f_w. If f_B∈X then X=Ind. Hence either Ind is irreducible (then V=Ind=W), or every irreducible sub contains f_w, so two distinct irreducible subs would meet nontrivially — impossible; socle simple, V≅W.
4b. (ψ=ψ^w, i.e. ψ=det^a∘.) Ind ψ = det^a⊗F̄p[P^1(Fp)]. Constants C; St = sum-zero functions; C∩St=0 (p+1≡1≠0), Ind=C⊕St. Irreducible X≠C: X^U⊂⟨δ_∞,1⟩ contains aδ_∞+b·1, a≠0; G-translates aδ_x+b1, differences span St, so X⊇St. Hence St irreducible (its irreducible sub ≠C must contain St) and the irreducible subs are exactly C≅Sym^0 and St. Sym^{p−1} (irreducible, dim p, ≠C) embeds via W_U for ψ (step 2, s=p−1), so St≅Sym^{p−1}. V∈{C,St} ⊂ list (twisted by det^a).
∎ Completeness without Brauer. (Consistency: list size p(p−1) matches 1b class count; not used.)

Soft SF caveats: weight convention in step 2 (λ^aμ^{a+s} vs swap) is convention-dependent but surjectivity onto T^ holds either way; not machine-checked.
