# MR2 FINDINGS — DUAL-CONTINUE GAP-SK-p3-1c-MC (Soft SF) — 2026-10-27
STATUS: ALL_OK (p=3,5,7) | tip_touched: NO | Kerr: BLOCKED | NOT OPERATIVE | REPORT ONLY, no RECS | no invented values
Parent: MR2-FINDINGS-DUAL-CONTINUE-gap-sk-p3-1c_2026-10-27.md (sha bb7b15354298fa94efdc65a83f617ef94f7bed0aaaac36b176143d27868ecdd9)
Script: MR2_gap_sk_p3_1c_mc_2026-10-27.py (sha 8c507171b23ecae41a749dae53086beaeddb2a1a1bc652e07f22c8411949907b); output .out (sha ede2d3e073b9179564069b2060225dca9bf3ed32a5e721b5c3b34aaa177fd2c5), last line ALL_OK. Pure python over F_p; F_{p^2} not needed.

## Setup
G=GL2(Fp) enumerated; Ind_B^G ψ realized on B\G ≅ P^1(Fp) (p+1 coset reps), (g·f)(x)=f(xg), f(bx)=ψ(b)f(x). ψ(diag(t1,t2))=t1^i t2^j, i,j mod p−1 (Fp-valued via a primitive root g0). Sym^s⊗det^a built on monomials, (X,Y)↦(aX+cY,bX+dY). Identification key: (dim, T-weight of the 1-dim U-fixed line); checked distinct over all p(p−1) pairs (s,a) for each p.

## Results (all p=3,5,7; all (p−1)^2 ψ each)
1. dim (Ind ψ)^U = 2 for every ψ; f_B (supp B) and f_w (supp BwU) U-fixed; f_B generates Ind (dim p+1).
2. ψ≠ψ^w: f_B ∉ ⟨G f_w⟩ and weights of f_B, f_w distinct ⇒ ⟨G f_w⟩ is the unique irreducible sub (= socle); its (dim, U-weight) matches a Sym^s⊗det^a in the list in every case.
   ψ=ψ^w (=det^i): Ind = C ⊕ St, dims 1 and p, St G-stable, St^U 1-dim and every nonzero vector in it generates St (St irreducible); C ≅ Sym^0⊗det^i, St ≅ Sym^{p−1}⊗det^i by key.
3. Every (s,a), 0≤s≤p−1, a mod p−1, occurs as a socle constituent: 6/6 (p=3), 20/20 (p=5), 42/42 (p=7).
Runtime < 1 s.

## Caveats (Soft SF)
- Irreducibility over F̄p is derived from the criterion "X^U is T-stable with T-weights in Fp^×" (U-fixed lines), not a full MeatAxe; isomorphism is by (dim, U-weight) key, not an explicit intertwiner.
- First run FAILED in step 2 (ψ=det^i, i≠0) due to a script bug: the "constant" line was taken as literal 1s instead of det(rep x)^i. Fixed (C := det^i-twisted line, St := kernel of the twisted sum functional, G-stability checked). Final run ALL_OK.
