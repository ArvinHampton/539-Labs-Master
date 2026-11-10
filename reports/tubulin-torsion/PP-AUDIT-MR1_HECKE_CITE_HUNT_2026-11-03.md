# PP-AUDIT — MR1 Cat A cite hunt: Hecke over Q(√35) / residual C (2026-11-03)
Status: AUDIT only (not a first proof). No CERT. No RECS. tip_touched NO. Messaged nobody.
Target: reports/FINDINGS_MR1_CAT_A_HECKE_Q35_RESIDUAL_C_CITE_HUNT_2026-11-03.md
- FINDINGS sha256 6eb9713e03e01a2feef3c0797f1dc97ddd8a4d2097dd7af245eef048ce506b13 — MATCH (claimed)
- PRESS located: reports/PRESS_MR1_CAT_A_HECKE_Q35_RESIDUAL_C_CITE_HUNT_2026-11-03.md (also sidecar in reports/bridges/AUDITOR/) sha256 95d610e81134a45989dab0ca83bbd9a75a9e0201eb3d671b9094b4c73ad6b48d — MATCH
- Tip residual-c-field-WRITTEN_PREMISES_DRAFT.md 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH pre and post (not modified)

## arXiv checks (live, 2026-11-03)
- arXiv:0712.0574 = Meerschaert, Nane, Xiao, "Large deviations for local time fractional Brownian motion and applications" (probability). Not BOR. MR1 decoy exclusion CONFIRMED.
- arXiv:0802.0963 = Bruinier, Ono, Rhoades, "Differential operators for harmonic weak Maass forms and the vanishing of Hecke eigenvalues" (ξ_{2-k}, D^{k-1}, Hecke action on harmonic Maass forms; algebraicity for CM duals). Correct BOR ID CONFIRMED. (Journal venue Ramanujan J. 2010 not live-checked in this run.)

## Other references (live: crossref API / arXiv meta)
L1 Dembélé–Voight arXiv:1010.5727 title/authors MATCH. L2 Shimura Duke Math J 1978 MATCH. L3 1-2-3 of Modular Forms, Springer 2008, 4 authors MATCH. L4 Atkin–Lehner Math. Ann. 1970 MATCH. L5 Zwegers arXiv:0807.4834 MATCH (thesis Utrecht 2002; arXiv posting 2008 — cite year should say 2002 thesis). L6 Bruinier–Funke arXiv math/0212286 + Duke 2004 MATCH. L8 Bringmann–Ono Invent. Math. 2006 MATCH. No fabricated refs found.

## LMFDB (Item 1 test)
- MR1's URL https://www.lmfdb.org/ModularForm/GL2/TotallyReal/2.2.140.1/ returns 404 (reproduced) — MR1's "Page Not Found" is accurate for that URL, but it is the wrong URL form.
- https://www.lmfdb.org/ModularForm/GL2/TotallyReal/?field_label=2.2.140.1 returns 137 Hilbert modular forms over Q(√35), parallel weight [2,2], levels norm 1,4,5,7,8,… (e.g. 2.2.140.1-1.1-a, page 200 at https://www.lmfdb.org/ModularForm/GL2/TotallyReal/2.2.140.1/holomorphic/2.2.140.1-1.1-a).
- https://www.lmfdb.org/NumberField/2.2.140.1 : Q(√35), disc 140, ramified 2,5,7, class number 2 (MR1 arithmetic note confirmed; class number 2 not mentioned by MR1 and is relevant to Hecke setup — narrow/wide class group matters for T_𝔭 at non-principal 𝔭).

## Deformation-of-Hecke literature (Item 3 test)
Standard p-adic/Hida-type deformation literature exists and MR1 should have named it as "different object, excluded", not silently omitted:
- H. Hida, "On p-adic Hecke algebras for GL2 over totally real fields", Ann. of Math. 128 (1988) [from knowledge, not live-checked]; Hida, "Hecke fields of Hilbert modular analytic families" https://www.math.ucla.edu/~hida/PSoffprint.pdf ; Hida, "Growth of Hecke fields along a p-adic analytic family" https://www.math.ucla.edu/~hida/Growth.pdf
- A. Wiles, "On ordinary λ-adic representations associated to modular forms", Invent. Math. 94 (1988) [not live-checked]
- Aribam, nearly ordinary Hilbert Hecke algebra deformations, https://arxiv.org/abs/1608.00392
- Bergdall–Hansen, p-adic L-functions for Hilbert modular forms in p-adic families / eigenvarieties, https://arxiv.org/abs/1710.05324
- Coleman–Mazur eigencurve (1998) [not live-checked]
These deform eigensystems p-adically in weight; none defines T_p·exp(Θ) or T_p+εΘ. So "ABSENT as Owner-defined" stands, but "no Hecke deformation in the literature" is overstated.

## Verdicts
- Item1 PARTIAL (field-specific ABSENT): FLAG. LMFDB has 137 HMFs over 2.2.140.1; field-specific computational data is PRESENT (data, not a paper). Recommend: PARTIAL with field-specific data PRESENT (LMFDB), published field-specific paper not found.
- Item2 PRESENT: CONFIRM (L1, L3 define T_𝔭 on HMFs of level 𝔫). Minor note: class number 2 of Q(√35) should be flagged for T_𝔭 at non-principal primes.
- Item3 ABSENT: CONFIRM for the Owner construction; FLAG wording — must cite Hida/Wiles/eigenvariety theory as standard, distinct "Hecke deformation" and state why excluded.
- Item4 PARTIAL/ABSENT: CONFIRM (L5, L7, L8 give computable coefficient formulas for standard objects only; no published C).
- Decoy 0712.0574 exclusion and 0802.0963 correction: CONFIRM.
Overall: 3 CONFIRM, 1 FLAG (Item1) + 1 wording FLAG (Item3). No CERT.
