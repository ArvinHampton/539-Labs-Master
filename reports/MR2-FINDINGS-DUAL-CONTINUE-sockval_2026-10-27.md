# MR2 FINDINGS — DUAL CONTINUE sockval (2026-10-27) — REPORTS ONLY, NO RECS
Labels: [Soft SF] / [Project Quantum Comp]
Parent: MR2-FINDINGS-DUAL-CONTINUE-gl2qp_2026-10-27.md 99902c1671ec19212ecf007b0708ad84d24564b7b937a4d293c80cb7f7440f19
Parent PRESS: SOFTSF_PRESS_MR2-DUAL-CONTINUE-gl2qp_2026-10-27.md 6da470dc75800de1a7c378781c54d02e1da2b56843915bc8fa90065643228ea5
Tip before: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | tip_touched NO

## 1. Rem 6.2 applied to πα = Ind(ω⊗ω⁻¹)
Source quote (lit/bm/1209.5205.txt, Rem 6.2): "π ≅ (Ind_P^G χ1 ⊗ χ2ω^r) ⊗ ω^m∘det. Hence, socK π = Sym^r k² ⊗ det^m if 0 < r < p−1 and det^m ⊕ Sym^{p−1} k² ⊗ det^m, otherwise. In particular, socK π is multiplicity free."
Match: χ1=χ2=1 (unramified, trivial); χ1ω^m = ω ⇒ m=1; χ2ω^{r+m} = ω⁻¹ ⇒ r ≡ −2 ≡ p−3 (mod p−1), r ∈ [0,p−2].
- p ≥ 5: 0 < p−3 < p−1 ⇒ soc_K(πα) = Sym^{p−3}k² ⊗ det. [Soft SF CLOSED-conditional]
- p = 3: r = 0 ⇒ "otherwise" branch: soc_K = det ⊕ Sym^2k²⊗det (Rem 6.2 literal). [Soft SF flagged edge case]
Reconcile with indconv σ^[s] = Sym^{p−3}⊗det: MATCH for p ≥ 5.
Conditions: (a) Rem 6.2 Ind convention assumed equal to indconv convention (indconv MATCH was Soft SF; 1209.5205 convention not re-verified verbatim this pass); (b) Rem 6.2 is stated in context of ρ with χ1 ≠ χ2ω^{r+1}; for χ1=χ2=1, r=p−3: ω^{p−2} = ω⁻¹ ≠ 1 for p ≥ 3 ⇒ hypothesis holds (generic, non-split-trivial).
OPEN-SK-p3: p=3 branch value differs from σ^[s] form (reducible socle). OPEN-SK-conv: verbatim Ind convention in 1209.5205 unverified.
Gap soc_K = soc_Γ verbatim: still not stated in Rem 6.2; value-level agreement only (Soft SF-NARROWED).

## 2. BL hunt
- [1] BL95 J. Number Theory 55(1) 1995 1–27, doi 10.1006/jnth.1995.1124: sciencedirect fetch returned HTML (no PDF); academia.edu listing abstract only; no arXiv/HAL. SF-BL-ord MISS.
- [2] BL94 Duke 75(2) 1994 261–292, doi 10.1215/S0012-7094-94-07508-X: Project Euclid first-page preview only (p.261 text: "We set V_σ = ind_{KZ}^G σ … Hecke algebra … E[T]"). No free full text. SF-BL1 MISS.
- Secondary (not ingested): Berger "Central characters…" (perso.ens-lyon.fr/laurent.berger/articles/article21.pdf) Thm 1.3 cites BL94/BL95: π(r,λ,χ) ≅ ind_B^G(μ_{λ⁻¹}χ ⊗ χω^r μ_λ) for λ ∉ {0,±1}.
Nothing ingested; lit/bm/MANIFEST unchanged. Items 3 (f(bg)=χ(b)f(g) read) N/A.

## OPEN
OPEN-SK-p3; OPEN-SK-conv; SF-BL1 MISS; SF-BL-ord MISS; SF-IC-c′ unchanged; soc_K=soc_Γ verbatim OPEN. Kerr BLOCKED. Filtration 10∥40 both named parallel, no pick. Residual-C not picked.
Tip after: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | tip_touched NO
