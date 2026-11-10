# MR2 FINDINGS — DUAL CONTINUE — soc_K (2026-10-27)
STATUS: PARTIAL. REPORTS ONLY — no RECS; no P5a; Bridge PARTIAL READY NO; G1 BLOCKED (no OMS / L7); Kerr BLOCKED; no tip fold.
Prior: sfr3p FINDINGS 7f9b7d22… / PRESS 96612a2b… — SF-R3′ OPEN stands (OPEN (C)+B′), not re-litigated. Filtration labels 10 ∥ 40 BOTH NAMED PARALLEL, NO PICK.

## Lit ingested (lit/bm/, MANIFEST.sha256 updated)
- [6] Breuil, Compositio 138 (2003) 165–188, part I — author page (imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/GL2(Qp)I.pdf) → breuil_GL2Qp_I.pdf ceac657c69a8439e50bf28a4f385766714579669781cace1fa77f698cb4b3f33 (+ .txt 3b5f0a8e…)
- [7] Breuil, JIMJ 2 (2003) 23–58, part II — same page, GL2(Qp)II.pdf → breuil_GL2Qp_II.pdf 53b1a2e4838861aa6101c4ac4e4f91959e06c832a9a4d942b598dc92dd6691a8 (+ .txt 245f62ee…)
- Missed/not attempted: BM02 Duke 115 — no free PDF searched-found this pass (not ingested; not invented). numdam CM_2003 URL 404.

## Facts
- SF-SK1 (quote [6] Thm 2.7.1(ii), summarising [1],[2]=Barthel–Livné): ind_KZ^G σ_r/(T−λ) ⊗ (χ∘dét) irreducible iff (r,λ) ∉ {(0,±1),(p−1,±1)}.
- SF-SK2 (quote [6] Rem 4.2.5, "cf. [2]"): "Ces représentations ont génériquement une interprétation en termes d'induites paraboliques: ind_KZ^G σ_r/(T−λ) ≃ ind_B^G(µ_{λ⁻¹} ⊗ ω^r µ_λ)".
- SF-SK3 (derived, not quoted): Ind(ω⊗ω⁻¹) = Ind(1⊗ω⁻²)⊗ω, ω⁻² = ω^{p−3} ⇒ πα ≅ (ind_KZ^G σ_{p−3}/(T−1)) ⊗ (ω∘dét), irreducible for p>3 (r=p−3∉{0,p−1}). Hence σ_{p−3}⊗det (the K-generator image) ⊂ πα|_K, i.e. σ_{p−3}⊗det ⊂ soc_K(πα). Caveats: "génériquement" in the quote; character-order/normalisation convention of Ind (µ_λ sends arithmetic Frobenius to λ⁻¹) must be matched to our πα convention — not checked here.
- SF-SK4 (miss): neither [6] nor [7] contains the word "socle" (grep count 0 both); no explicit statement of full soc_K(πα), nor of soc_K of (k⊗̂P̃)^∨ (Rem 6.3 form). Equality soc_K = σ_{p−3}⊗det NOT quoted.
## Effect on L₂ σ-label / rem62 SF-R4
- Not settled. SF-SK3 gives one constituent (containment) only; full socle and convention match open ⇒ L₂ σ-label / SF-R4 remain OPEN, gap named: "soc_K(πα) equality + Ind-convention match".
## Residual-C lattice pick (from residual-mult-bm)
- Still OPEN; dual parallel named, NO PICK.
## Tip
- /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 BEFORE and AFTER; tip_touched NO.
## Remaining gaps
1. Full soc_K(πα) (explicit quote; candidates: BL94 / Breuil–Paškūnas / Paškūnas Image of Colmez's functor). 2. Ind convention match. 3. BM02 free PDF. 4. Residual-C lattice pick OPEN. 5. Kerr, G1, Bridge unchanged.
