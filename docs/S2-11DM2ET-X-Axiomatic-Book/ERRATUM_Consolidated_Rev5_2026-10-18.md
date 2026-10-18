# ERRATUM / changelog — Bridge C Consolidated, revision 5 (2026-10-18)

New file. Pure copy-and-create; earlier repository files are not edited. Consolidated statement: `Bridge_C_Consolidated_rev5_2026-10-18/` (§13 and Appendix D). Convention: Cat A means proved or exact; floating-only results are Cat B. No TPC/RH claim; distinct from HQCC termination claims. CORE_FREEZE holds. No lock files altered.

- **R5.1** s = 98: "2406 ≤ dim V ≤ 2408 (not certified)" (rev. 4 Theorem 11.6(iv) and open problem 2; `U1_LEDGER_Cusp_Onset_2026-10-18.md` A3) is replaced by **dim V(98) = 2406 (Cat A)**.
  - The kernel is 42 g-relations plus 2 h-relations, h = (g+I)/4, proved via the h-invariant overlattice M = ⟨(4,0),(1,1/7)⟩ and the cone argument. Source: `Open_Algebraic_2026-10-18/`.
  - The half-cone bound 2408 is not sharp.
- **R5.2** The rev. 4 Cat B statement "gap m(m−1) for all m" is withdrawn: the gap is 44 at m = 7. Extra relations are predicted at m = 2k²−1 (Cat B; no count claimed for m = 17).
- **R5.3** The original orbit lemma is false for some odd s (first at s = 27; 16 cases with s ≤ 30001). The corrected lemma is Cat A for all odd s. No tabulated dimension changes (s = 27: dim V = 702).
- **R5.4** "Modulo F1" is removed: the 2-D Euler–Maclaurin expansion is proved (`Open_Analytic_2026-10-18/` §2). Any separate Hecke input is unaffected.
- **R5.5** The x = 1/2 and x = 1/3 instability (rev. 4 open item) came from fitting outside the asymptotic window. The old fits remain unquoted; exact closed forms replace them.
- **R5.6** Upgraded from B to A:
  - ∫_{Γ_F} Ξ₁ = 0 and the Θ_a identification;
  - the E-part cocycle (C = −π/2, both signs of cx+d, the 140-label vector law);
  - the ambiguous-class count, the squarefree criterion (Eis ⇔ h = 2^{ω(s)}) and the coset property for all s (rev. 4 Cat B items in `U1_LEDGER_Cusp_Onset_2026-10-18.md`);
  - the ε_all = −1 sectors vanish for all odd s;
  - d₂(k = 6) = 36.
- **R5.7** u_L at s = 32, 34, 36, 40: CUSP (Cat A); these were listed as open in rev. 4.
