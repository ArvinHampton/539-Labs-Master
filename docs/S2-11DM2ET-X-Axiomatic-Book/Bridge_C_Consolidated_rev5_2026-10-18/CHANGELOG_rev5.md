# Bridge C Consolidated — revision 5 changelog (2026-10-18)

PDF: `bridge_c_consolidated_rev5.pdf.base64`. It has 51 pages; the PDF is 711198 bytes with sha256 `6f09f36bee8a9852df22bfddbcaaec501c432c4a65cfb6cb35660d0628e109a3`. Decode with `base64 -d bridge_c_consolidated_rev5.pdf.base64 > bridge_c_consolidated_rev5.pdf`.
Build: `pdflatex` ×3 on `bridge_c_consolidated_rev5.tex`, which `\input`s `rev5_sec.tex` and `rev5_app.tex`. The build is clean: no errors, no undefined references and no overfull boxes (`build_rev5.log`).
Source: the rev. 4 tex (`Bridge_C_Consolidated_rev4_2026-10-18/`, unchanged in the repo) with the edits in `rev4_to_rev5.diff`.
Convention: Cat A means proved or exact (including exact finite computation); floating-only results are Cat B. No TPC/RH claim. This is distinct from HQCC termination claims. CORE_FREEZE holds.

## New §13 "Revision 5" (sources [S28]–[S31])
- 13.1 **F1 removed.** The 2-D cone Euler–Maclaurin expansion is proved and is sector-uniform (Cat A). "Modulo F1" is dropped.
- 13.2 **H_s.**
  - x = 1/2: for odd s, every order vanishes. For even s, the closed forms through t^{9/2} are given, including the 16 | s √Δ terms.
  - x = 1/3: closed form. γ₀ and eb depend on s mod 3, and ea depends on s mod 144 (Cat A). The mod-72 four-shape table is Cat B.
  - t^{7/2} and t^{9/2} at x = 0 (Cat A).
- 13.3 **C_third.** The unit-cone weight-1 piece vanishes, including its Zwegers completion. The weight-0 integral equals Zwegers' Θ_a (Cat A; both were B in rev. 4).
- 13.4 **E-part cocycle, Cat A.**
  - The constant C = −π/2 is derived by hand.
  - The boundary step holds for both signs of cx+d, with branch sign ε = sgn(cx+d).
  - The vector law u∘γ′ = ρ(γ′)u is proved label by label for all 140 labels, including b_λ = log ε·δ.
  - Numerics at STS, ST²S and ST³S agree to ≤ 3.3e−12 (Cat B support).
- 13.5 **u_L criterion.**
  - The coset property holds for all s and every c-part (Cat A).
  - For squarefree s(s−2): Eisenstein iff h = 2^{ω(s)} (Chevalley plus genus theory, Cat A).
  - Verdict table for s ≤ 44. Eisenstein at 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 20, 24, 28; CUSP at the rest. s = 32, 34, 36, 40 are CUSP.
- 13.6 **Sectors.**
  - Odd-parity sectors are cusp (Cat A).
  - Parity fact: x₂ is even, so the ε_all = −1 sectors vanish for all odd s (Cat A).
  - Corrected orbit lemma (Cat A). The original lemma is false; the first counterexample is s = 27, where dim V = 702.
  - Prime-square old/new pieces are exact at s = 9, 11, 25 (s = 25: old 36, new 432, (−,−) 132).
- 13.7 **2-adic gap and s = 98.**
  - For all odd m: tr g = 2m, and the g = −1 eigenspace has dimension m(m−1) (Cat A).
  - Half-cone relations = δ_iso ⊗ X. This is proved for prime m given g-consistency, which is checked exactly at m = 3, 5, 7. Composite m is open.
  - **dim V(98) = 2406 (Cat A).** The kernel is 44 = 42 g-relations + 2 h-relations R1 (q = 11/12) and R2 (q = 1/4), with h = (g+I)/4.
  - The overlattice M = ⟨(4,0),(1,1/7)⟩ has Gram [[32,64],[64,32]] and satisfies h·M = M; the theta identities follow from the cone argument. The half-cone bound 2408 is not sharp.
  - Prediction (Cat B, no count): extra relations at m = 2k²−1 (7, 17, 31, …). No number is given for m = 17.
- 13.8 **s = 64 and Atkin–Lehner.**
  - s = 64: W_P = 1986 and d₂(k = 6) = 36 (Cat A).
  - Atkin–Lehner, partial: the 24 characters have conductor norm 140 and level 19600; the global root numbers are non-real (Cat B). The local split at 5 and 7 is open (blocked).

## Appendix D
Errata R5.1–R5.7 and the changelog; see also `ERRATUM_Consolidated_Rev5_2026-10-18.md`.

## Other edits in the rev. 4 text
- Title date: revision 5. One sentence is added to the abstract.
- Theorem 11.6(iv): the s = 98 sentence is updated. The Cat B box no longer contains "gap m(m−1) for all m".
- Open problems: items 2–7 are updated.
- Sources [S28]–[S31] are added.

## Naming
- New labels are numbered within §13 (Propositions 13.1–13.17 and Theorems 13.7, 13.8, 13.9, 13.16). There is no lettered theorem and no "Theorem L"; Theorem L is the framework's Parity Dominance Theorem, and Lemma L keeps its name. No label collides with L1–L7.
- Rev. 4 names are kept: W_P vs d_Eis, Theorem G = Lewis–Zagier, Prod1/Prod2, d₂(k,v).
