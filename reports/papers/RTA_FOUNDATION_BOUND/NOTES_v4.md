# NOTES v4
Build: cd src && pdflatex -interaction=nonstopmode -jobname=v4 -output-directory=../build main_v4.tex (x3); copied to RTA_FOUNDATION_BOUND_v4.pdf (128 pp, sha256 fd51c846…). v3 untouched.
New sources: main_v4.tex, front_v4.tex, glossary_v4.tex, partIII_shadow_v4.tex, found_v4.tex, appD_v4.tex.
Changes from v3: new Section "Shadow structure of the companion series" (Lemma Pinv, Prop. M²=35P & (MT)³=35√35P, Lemmas O/W, Cor. even, parity split, Prop. ξ for cone completions with three unary thetas, Prop. B(ĉ′)≡0, unary-theta vanishing Lemma, Thm. B(ĉ1) iff, Thm. Laplacian defect, Prop. line terms, summary Thm. hybrid, Category B remark, descriptive remark); abstract sentence; 7 glossary rows; found §"Where Ξ enters" and Problem 1 updated; App. D items sh1–sh4.
## Problems (not in paper)
- Prop. B(ĉ′) and Lemma Pinv rely on finite exact checks done in scripts (order14 cprime_all.py, order9 cyclo.py); the paper cites the scripts rather than tabulating.
- Thm. Bc1 uses B(ν,β)=7(b0+b1)m−5b0u in (u,m) coordinates; the sign ε is fixed only at the endpoint used in Thm. lap.
- The law of Ĥ, Ĝ_O with exactly (35^{-1/2}M,T) is Category B (Zwegers gives a Weil-type law; the matching is numeric).
- 𝓗(Φ_orth)=S^E is Category B.
- Open: S-covariance of A1 after completion; identification of RTA's Ξ; Maps E1–E3.
