# MR2 FINDINGS — DUAL CONTINUE gl2qp — 2026-10-27 (Soft SF) — REPORTS ONLY, no RECS
Dual label: Soft SF / Filtration 10∥40 BOTH NAMED PARALLEL — no pick. Kerr BLOCKED. Residual-C pick OPEN dual, no pick.
Tip before: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91  (LOCK 7cddb188…dfc91)
Parent bm02 FINDINGS 561c4740650122d94ffad3c55b27b82d2037e24bbf8caa2006f9ef97689783db; PRESS bef4b14e0e22b2b587793a9cbd17531b223a5d63583a3b3bdae833d9ebee6728

## Sources (sha256 of .txt)
- breuil_GL2Qp_I.txt 3b5f0a8e7a58de7a3c37c4391bf6d855704ddbc947b0b9deaa17c1edf3154518
- breuil_GL2Qp_II.txt 245f62ee00f8c392bfc1dbe0ce5a14d40a634e137c161ec2d07414cd0362b273
- 1209.5205.txt (Paškūnas, BM) 4ac1a4c57fe6a38e1f05210e0c6e57df06eb8e875cb01852aaa57c5031fe8592
- 1005.2008.txt b1ea4b455eb89ea68e5606f08aa228411e49343c45130fdf33d1b6a82d8a19c1

## Soft SF facts
SF-GL2-1 (Breuil I, l.1514–1522, Rem 4.2.5): "Ces représentations ont génériquement une interprétation en termes d'induites paraboliques (cf. [2]) : ind_KZ^G σ_r/(T−λ) ≃ ind_B^G(μ_{λ^{-1}} ⊗ ω^r μ_λ) … où B désigne le sous-groupe de Borel de G." — mod-p smooth parabolic induction named; NO word-for-word f(bg)=χ(b)f(g) definition in Breuil I (grep "f(bg)" MISS). Defers to [2].
SF-GL2-2 (Breuil II, l.672): "l'induite parabolique est l'induite lisse classique." — characteristic 0 (Q̄p), no formula given. grep socle MISS in Breuil I/II.
SF-GL2-3 (1209.5205, l.3545–3547): "I^sm(χ) denotes the space of locally constant functions f : G → L such that f(bg) = χ(b)f(g) for all b ∈ P and g ∈ G, with G-action by the right translations." — word-for-word unnormalised convention, but coefficients L (char 0), not mod p.
SF-GL2-4 (1005.2008, l.5529–5530): "(Ind_P^G Π)cont … continuous functions f : G → Π such that f(bg) = bf(g) for all b ∈ P" — same unnormalised shape, Banach/continuous.
SF-GL2-5 (1209.5205 Rem 6.2, l.2711–2720): "If ρ ≅ (χ1 ∗; 0 χ2ω^{r+1}) ⊗ ω^m … then π ≅ (Ind_P^G χ1 ⊗ χ2ω^r) ⊗ ω∘det. Hence, socK π = Sym^r k² ⊗ det^m if 0 < r < p−1 and det^m ⊕ Sym^{p−1} k² ⊗ det^m, otherwise. In particular, socK π is multiplicity free." — Soft SF quote of soc_K of a mod-p principal series (k coefficients). Soft SF-NARROWS soc_K equality: gives soc_K(Ind_P^G) = irreducible Sym^r⊗det^m for 0<r<p−1, consistent with Γ-socle form; does NOT state soc_K = soc_Γ(Ind_B^Γ χ̄) verbatim.

## Status
- SF-IC-c′: Soft SF-NARROWED, OPEN. Exact gap: word-for-word definition of mod-p (k-coefficient) smooth Ind_P^G with f(bg)=χ(b)f(g). On disk only char-0 (SF-GL2-3) / Banach (SF-GL2-4); Breuil I uses ind_B^G mod p without formula, citing its [2].
- soc_K equality: Soft SF-NARROWED, OPEN. SF-GL2-5 gives soc_K π for mod-p principal series; remaining gap = explicit identification soc_K(Ind_P^G χ) = soc_Γ(Ind_B^Γ χ̄) (restriction to K / inflation step) — SF-SK2e remains inference-only for that step. Rem 6.2 cites [6],[7] (Breuil) for ρ irreducible case.
- BL94 SF-BL1: MISS; no new free full-text lead found. Not hunted.
- Carry unchanged: SF-R3′ OPEN-named; Rem 6.2 L₂ stands; indconv MATCH; χ/χ^s CLOSED conditional.

Tip after: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched NO.
