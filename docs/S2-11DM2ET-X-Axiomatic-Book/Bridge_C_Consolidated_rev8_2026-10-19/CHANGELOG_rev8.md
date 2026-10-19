# Bridge C consolidated — CHANGELOG rev7 → rev8 (2026-10-19)

The PDF is bridge_c_consolidated_rev8.pdf.b64. Decode it with `base64 -d`. It has 77 pages and 943254 bytes; sha256 04c3b7d2856ed63df15a7fc8a2b4f39ea716a814ba852a4bd6c7cc2a6d9bbf41.

Build: pdflatex ×3, no errors, 0 undefined references or citations, 0 LaTeX warnings, 0 overfull boxes (40 underfull, 172 hyperref "Token not allowed in a PDF string" warnings; rev7 had 32 and 164). Log: build_rev8.log.

The main file is a copy of rev7's bridge_c_consolidated_rev7.tex with these edits only (see rev7_to_rev8.diff): date/revision line (revision 8); one abstract sentence; \input{rev8_sec} and \input{rev8_app}; sources [S38], [S39]; bibliography items Nikulin, Morrison, Huybrechts, Gromov–Yomdin.

The \input files needed to build (rev5_sec, rev5_app, rev6_sec, rev6_app, rev7_sec, rev7_app) and dims_table.tex are included as unchanged copies. The rev4_*.tex files are not \input by the master (their content is inlined) and are not included here; they are in rev8_latex_source.zip.b64 and on Master in Bridge_C_Consolidated_rev4_2026-10-18/.

Page renders: render/rev8_master_p-01.png.b64 (title page) and render/rev8_master_p-49.png.b64 (first page of the new §16). Decode with `base64 -d`. Full text: bridge_c_consolidated_rev8_fulltext.txt (pdftotext -layout). All .tex: rev8_latex_source.zip.b64.

## Added
- §16 K3 lattice realisation of the 140-label representation (PDF p. 49):
  - Prop 16.1 discriminant form of N₂ = {x ∈ Z²: x₂ even} (Gram [[2,14],[14,28]], det −140, ≅ ⟨2⟩⊕⟨−70⟩), local table. Cat A.
  - Thm 16.2 ρ_rev = (S ↦ S_lab⁻¹, T ↦ T_lab) ≅ ρ_{N₂}; explicit intertwiner X e_z = u_{([z],0)} + e(B(z,β₁)) u_{([z],β₁)}, exact in Z[ζ₂₈₀]; not ≅ ρ_{N₂}*, ρ_{N₁}, ρ_{N₁}*. Cat A.
  - Prop 16.3 relations and Hom dimensions mod ℓ = 840841. Cat A (mod-ℓ); the "8 sectors" reading Cat B.
  - Remark 16.4 dual/twist/metaplectic.
  - Prop 16.5 explicit primitive embedding; T = ⟨−2⟩⊕⟨70⟩⊕U⊕E8(−1)², q_T = −q_{N₂}. Cat A.
  - Cor 16.6 ρ_rev ≅ ρ_T*. Cat A.
  - Thm 16.7 N₂-polarised K3 exists, embedding/T unique, no (−2)-curves, no elliptic fibrations. Cat A (cited: Nikulin 1.14.4, Morrison Cor 2.9(i)).
  - Prop 16.8 γ on A_{N₂} (2: non-trivial involution, 5: +1, 7: −1), O(N₂). Cat A.
  - Thm 16.9 γ² lifts, entropy 2 log(6+√35) ≈ 4.9558; involution ι; Aut(X) ≅ D_∞ (very general); γ does not lift. Cat A (cited).
  - Remark 16.10 Cat B / open items (K-9, special members, interpretations, citation hygiene, N₂-only scope).
- §17 Implications (RTA; fifth-order unification (N1)–(N3); even multi-k; K3, N₂ only): Props 17.1 (no scalar residual law; Baker-conditional; W₇ exact at 178/270), 17.2 (weight-1 vector law; χ_nat), 17.4 (IC-1, IC-2), 17.6 (role of s = 7 from frozen c₂); Remarks 17.3 (samples, Cat B numbers), 17.5 (RTA §11). Corrections: IC-1, IC-2, H³(K3) = 0, 2cos(2π/539.9) algebraic of degree 2699.
- Appendix G: reproducibility (scripts, outputs, reproduce command; re-run byte-identical), corrections R8.1–R8.8.
- Sources [S38] (K3-140 check), [S39] (Implications report).

## Labels
All new statements numbered within §16/§17. No lettered theorem, no "Theorem L", no collision with L1–L7. CFP and Proposition K1 keep their names.

## Hygiene
New files only; built locally then pushed as copies. CORE_FREEZE: locked H_s (c₁ = (−1,1), c₂ = (−4,1)) unchanged; H_s^axes is a parallel object. No TPC/RH claim; distinct from HQCC termination claims. No lepton, Orch-OR or neuroscience material.
