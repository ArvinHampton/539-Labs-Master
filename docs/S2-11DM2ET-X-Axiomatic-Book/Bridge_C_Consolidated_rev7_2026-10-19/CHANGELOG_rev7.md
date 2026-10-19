# Bridge C consolidated — CHANGELOG rev6 → rev7 (2026-10-19)

The PDF is bridge_c_consolidated_rev7.pdf.b64. Decode it with `base64 -d`. It has 65 pages and 843060 bytes; sha256 e794053a6c35e1cbcac19663b6a2ec2e161713afc5529d21b4d84b6545be1c37.

Build: pdflatex ×3, no errors, no undefined or multiply-defined references, no overfull boxes (build_rev7.log). The main file is a copy of rev6's bridge_c_consolidated_rev6.tex with these edits only (see rev6_to_rev7.diff): date/revision line; one new theorem environment (Proposition K1); one abstract sentence; \input{rev7_sec} and \input{rev7_app}; sources [S36], [S37].

Unchanged \input files are not re-pushed. They are on Master already, with identical sha256: dims_table.tex and rev4_*.tex in Bridge_C_Consolidated_rev4_2026-10-18/; rev5_sec.tex and rev5_app.tex in Bridge_C_Consolidated_rev5_2026-10-18/; rev6_sec.tex and rev6_app.tex in Bridge_C_Consolidated_rev6_2026-10-18/.

Page renders: render/rev7_master_p-01.png.b64 (title page) and render/rev7_master_p-41.png.b64 (first page of the new §15). Decode with `base64 -d`.

## Added
- §15, Revision 7 (PDF p. 41 on):
  - 15.1 Proposition K1 (extra h-relations = k(k−1) for every k ≥ 2; proof outline), Corollary 15.1 (spectrum of τ), dimension consequences (proved upper bounds; sharpness open). Cat A.
  - 15.2 Proposition 15.2: lattice origin of Δ; 7s − 32 = −2Q(c₂). Cat A.
  - 15.3 Propositions 15.3–15.5 and Remark 15.6: the involution M and edge-class invariance; c₁ forced by the wall n = 0; the axes cone (Cmixed ≡ 0); status of c₂ = (−4,1) (a definition; unique only among b = 1). Only (s − 2) is intrinsic; 7s − 32 and the √Δ terms are tied to the locked c₂. Cat A; the selection-rule reading is Cat B.
  - 15.4 Definition 15.7 and Theorem 15.8: the parallel object H_s^axes; exact closed forms through t^{13/2}. Cat A; PSLQ/direct-sum support is Cat B.
  - 15.5 Proposition 15.9: universal piece R_r = S^ax_r for r = −1/2, …, 13/2 (wall-independent). Cat A; general order open.
  - 15.6 Propositions 15.10–15.14: general-formula checks completed (N = 32, 35, 45, 49); even N from the 2-adic reduction; N = 8 classes pairwise distinct (no scan over s); ea tables at x = a/8; t^{11/2}, t^{13/2} at x = 1/4, 1/6 with two vanishing results; t^{15/2}, t^{17/2} at x = 0; S_e structure (Cat A per e; general pattern incl. Bernoulli numerators = Cat B observation).
  - 15.7 Proposition 15.15: Weil representations of Z/47, Z/59, Z/71, Z/17², Z/19², Z/23² (exact mod ℓ with lift). Cat A. s = 121, 3481 remain factor-dimension predictions (Cat B).
  - 15.8 Remark 15.16: correction — only (s − 2) of Δ is intrinsic.
  - 15.9 Open problems after rev7.
- Appendix F (R7.1–R7.8).
- Sources [S36], [S37].

## Labels
CRT factorisation = CRT Factorization Proposition (CFP) = Proposition 14.8(ii) in the PDF. The k(k−1) result = Proposition K1. No lettered theorem and no letter-L theorem label is introduced; no collision with L1–L7; Lemma L and Lemma R (rev. 4) keep their meaning.

## Hygiene
New files only; no existing Master file edited, renamed or deleted; no locks touched. CORE_FREEZE: locked H_s (c₂ = (−4,1)) unchanged; H_s^axes is a parallel object. No TPC/RH claim; distinct from HQCC termination claims. No lepton, Orch-OR or neuroscience material.
