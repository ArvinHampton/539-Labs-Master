# ADDENDUM K — Owner t4103 complete 26KB master (same review; relay-based; No CERT; no .tex)
## Source
The cited attachment path does NOT exist on PP's box (ls fails), so I could not do a full-source read. These findings are based on Physicist's relay of lines 181–195. If a readable copy is placed under /workspace/quantum-comp/intake/, I will do a line-by-line confirmation (as for F.1).
## Lines 181–195: [h_i]_{rs} = Σ_{k=1}^{11} α_{ik} δ(ψ(r,s), p_k)
- This is a mask family: [h_i] = Σ_k α_{ik} M_{i,k}, where M_{i,k} = 1[ψ(r,s)=p_k] is an indicator matrix.
- It is NOT a representation until the following are specified: dims n_i, bases, ψ, α, and how the matrices relate to the G-action. No identity or compatibility with the group action is established.
- Counterexamples (inert labels decide nothing):
  - ψ ≡ 0 (never an inert prime) ⇒ T_i = 0.
  - ψ ≡ 3 and α_{i1} = 1 ⇒ T_i = all-ones matrix, which has rank 1 for every dimension ≥ 2.
  - So rank and the endpoint map T_M⋯T_1 need not be full rank.
- "Inert support preserves field extensions": UNSUPPORTED. The values p_k are only labels in ℤ; no field action is defined.
- Composed entries: (T_2T_1)_{rt} = Σ_s (T_2)_{rs}(T_1)_{st} is the standard matrix product. This is correct, but it is not an inert-indexed form.
- Line 195 (ker D, coker D depend on the parameters) is CORRECT by Addenda H/I, and it CONTRADICTS the master's unconditional "n0 / 0" claim elsewhere.
- Negative α would rule out a conductance (Laplacian) reading. The directed T_i in D need no positivity.
## Carried regressions (J), plus the shifted symmetry
- Untwisted symmetry a_c = a_{c⁻¹} is INSUFFICIENT for the shifted C_xy = a_{(yx⁻¹)w⁻¹}. The correct condition is a_c = a_{c⁻¹w⁻²}.
- Counterexample VERIFIED: w = 3 (3⁻¹ = 47, 3⁻² = 109 mod 140), a_1 = 2 and every other a = 1. Then a_c = a_{c⁻¹} holds, yet C_{1,3} = a_1 = 2 and C_{3,1} = a_{109} = 1. So C is not symmetric.
- The real degree must carry σ: δ = Σ_{g≠e} σ(a_g) in the unshifted form.
- The other J items stand:
  - the +√35 embedding does not give positivity;
  - the torus claim is false (b1(K48) = 1081);
  - backtracks are not homology;
  - the boundary criterion needs column rank;
  - |W| is a redefinition.
## Document state
- The appendix and \end{document} are reported present (no longer truncated).
- Row breaks and syntax are still broken, so the document does not compile as given. Not assembled or compiled.
- The embedded follow-up offers are document content, not Owner authorization.
## Constructive correct statement
Fix n_i, bases, ψ: [n_i]×[n_{i−1}] → ℤ and α ∈ F (F ⊂ ℝ if a conductance reading is wanted). Then:
- T_i := Σ_k α_{ik} M_{i,k};
- D is as in Addendum I;
- ker D ≅ L0, and the boundary solutions ≅ ker(C0 + C_M T_M⋯T_1).
Rank is decided by the actual T's, not by the inert labels.
Remaining OPEN: the original N/W/capacity, and any link between inert primes and rank.

## K.1 — full-source confirmation + CORRECTION (intake owner-20261105-1854/OWNER_MASTER_COORDINATE_TRANSFER_1854.txt, 248 lines, sha dbfa0f94…)
- I read the source directly. Lines 178–200 match the relay: the mask formula, the matrix-product formula, and the "preserves algebraic field extensions" claim (still UNSUPPORTED). The appendix is present, and the TeX is broken (`{i-1}`, `{r,s}`, `, ,` row breaks).
- CORRECTION to my K line 13: I wrote that the source's claim "ker D/coker D must be determined by parameters" (L195 in the relay numbering, the final sentence of §"Decoupling") is CORRECT. That is WRONG.
  - For the unrestricted D(x)_i = x_i − T_i x_{i−1}, Addendum I proves that D is surjective (coker D = 0) and that ker D ≅ L0 (dim n0), for EVERY choice of T_i. So the source sentence is FALSE.
  - Only the boundary-constrained kernel ker(C0 + C_M T_M⋯T_1), and the rank of the terminal product T_M⋯T_1, depend on the parameters.
- Everything else in K stands: the counterexamples, the shifted symmetry (w = 3), the regressions, the constructive statement, and the items listed as OPEN.
