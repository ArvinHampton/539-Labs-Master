# NOTES v6
Build: cd src && pdflatex -interaction=nonstopmode -jobname=v6 -output-directory=../build main_v6.tex (x3) → RTA_FOUNDATION_BOUND_v6.pdf (131 pp, sha256 0fe599bf0d76d850…). v5 untouched.
New sources: main_v6, front_v6, glossary_v6, partIII_order0_v6, found_v6, appD_v6 (.tex).
Changes from v5: new Section "The order t^0 coefficient" (Lemma EMline, Thm A2odd, Thm A2even, Thm A2exact, Prop noaffine, remark deriving c=0, Category B remark); abstract sentence; glossary row; found §Ξ; App. D item o19.
## Problems (not in paper)
- Lemma EMline remainder: uniformity in the iterated 2D application is asserted from Gaussian bounds on the closed quadrant; a written constant would strengthen it.
- The A2_lines formula's half-line convention (b ≥ 0 / b < 0 split and f(0) term) is written compactly; it matches the order4b A2 to 7.8e−15.
- Prop noaffine needs the law on all of Q^×; the numerics cover x ∈ (0,3] only.
- Open: identify a law (if any) for A2^corner, e.g. involving Fourier-transformed Bernoulli weights; RTA's Ξ; Maps E1–E3.
