# MR2 FINDINGS — DUAL CONTINUE — skconv — 2026-10-27
Discipline: Soft SF. REPORTS ONLY. No recommendations, no tip fold, no P5a. Kerr BLOCKED. Filtration 10∥40 both named in parallel, no pick. Residual-C lattice not picked. No agents messaged.
Parent: MR2-FINDINGS-DUAL-CONTINUE-sockval_2026-10-27.md sha256 2b8528f303d36fb71f7d0d91ea396ae3de402205f59e81e6c7517e8b1e64924d.
Tip: residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after. tip_touched NO.

## 1. Mod-p Ind_P^G convention in 1209.5205 (Soft SF)
- l.1278–1282 (§3 Preliminaries): "Let P be the subgroup of upper triangular matrices in G ... If χ1 and χ2 are characters of Q_p^×, then we write χ1 ⊗ χ2 for a character of P, which maps (a b; 0 d) to χ1(a)χ2(d)."
- No k-coefficient (mod-p) definition of Ind_P^G appears anywhere in the text. The search covered every "IndG" hit: l.1392, 1564, 1593, 1615, 2628, 2717, 2814, 3424, 3721. None of them gives a function-space definition, and the word "normalized" never occurs in an induction context. The only function-space definition is l.3545–3547, I^sm(χ): "locally constant functions f : G → L such that f(bg) = χ(b)f(g) for all b ∈ P ... with G-action by the right translations". That definition is unnormalised and left-equivariant, but its coefficients are L (char 0), and it sits in the appendix.
- Classification: the mod-p convention is NOT STATED. Nothing in the text points to a δ^{1/2}-normalised version, and any half-twist would involve √p, which cannot be defined on k-valued smooth characters of the torus.
- Internal anchors (Soft SF):
  - l.1390–1393: "If π ≅ Ind_P^G χ1⊗χ2ω^{-1} then V̌(π^∨) ≅ χ1", attributed to Breuil [6].
  - l.2628: "π := Ind_P^G χ1⊗χ2ω^{-1}, so that V̌(π^∨) = χ1".
  - l.2814 (§6.2): "πα := Ind^G_B ω⊗ω^{-1}". This is literally the same name and character as Hu–Tan l.1670. The subgroup is written B, and B is not defined separately in the extracted text.
  - Rem 6.2 cites "[6], [7]" (Breuil I/II) at l.2700. That points to Breuil's convention, which is not verified here.

## 2. (r, m) match for πα under the convention
- Rem 6.2 (l.2711–2720): ρ ≅ (χ1 *; 0 χ2ω^{r+1}) ⊗ ω^m and π ≅ (Ind_P^G χ1⊗χ2ω^r) ⊗ ω^m∘det. "Hence, soc_K π = Sym^r k² ⊗ det^m if 0 < r < p−1".
- Restricted to the torus, the character is χ1ω^m ⊗ χ2ω^{r+m}. Matching it to ω ⊗ ω^{-1} with χ1 = χ2 = 1 gives m = 1 and r ≡ −2 ≡ p−3 (mod p−1). For p ≥ 5 (l.1275), 0 < p−3 < p−1, so soc_K πα = Sym^{p−3} k² ⊗ det. The match HOLDS under the stated χ1⊗χ2 convention (l.1282), read as the same left-equivariant induction as l.3545.
- Sensitivity, stated explicitly:
  - A χ1↔χ2 swap (or equivalently f(gb) / opposite-Borel conventions) WOULD change the socle. Ind(ω^{-1}⊗ω) gives m ≡ p−2 and r = 2, so the socle becomes Sym² ⊗ det^{p−2}.
  - A δ^{1/2} normalisation is not definable over k. The unnormalised modulus character a/d ↦ |a/d| sends p ↦ p^{∓1} ≡ 0 or undefined in k, so the only usable smooth mod-p version is unnormalised. This does not move (r, m).
  - The convention risk is only the swap or side, and the l.2814 notational identity with Hu–Tan reduces it.

## 3. OPEN-SK-conv: NARROWED (Soft SF-named)
- The character convention is verbatim (l.1282).
- The same πα name and character appear in §6.2 (l.2814).
- The match (χ1 = χ2 = 1, m = 1, r ≡ p−3) holds.
- Exact remaining gap: 1209.5205 never states the k-coefficient Ind_P^G function-space convention (f(bg) = χ(b)f(g) and right translation). It also does not define the B in l.2814 as P. Closing the gap needs a verbatim mod-p definition, from Breuil [6]/[7] or from Hu–Tan's own notation section.

## 4. Carried forward unchanged
SF-IC-c′ unchanged; soc_K=soc_Γ verbatim OPEN (value-level only); OPEN-SK-p3; SF-R3′; BL94/BL95 MISS (SF-BL1 MISS, SF-BL-ord MISS); residual-C pick OPEN.
