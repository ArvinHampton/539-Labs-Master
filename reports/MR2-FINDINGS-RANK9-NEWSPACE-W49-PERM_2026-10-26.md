# MR2 FINDINGS — Rank 9: Newspace / W₄₉-on-Perm cut (R4/R5), κ=4, k=−2
- **Status:** FAIL diagnostic / PARTIAL (bounds only). Bridge PARTIAL READY NO. Not a rescue of P5a.
- tip Soft SF LOCK sha (start=end): `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`; tip_touched Soft SF NO
- Rank 9 ONLY (Q5 → MR2). Soft SF invent HOLD. Soft SF F3 CLOSED. Opt 1 Weil NOT selected. Perm-side only. No Cat A invented. No tip-fold.
- Inputs: Connection FINDINGS `2b49ca25…` §R4/R5; Corpus map AMENDED `b271f42a…` V-R4/V-R5; MR1 P5a FAIL 592 (`b829661e…`); Rank 11 `570cc005…` (scalar analogy only).

## 1. R4 — newspace definition and dims
Ambient: S₄(Γ₀(49), ρ̄) ≅ S₄(SL₂ℤ, Ind_{Γ₀(49)}^{SL₂ℤ}(ρ̄)) ≅ S₄(SL₂ℤ, ρ̄⊗Perm(P¹(ℤ/49))), d=42, μ=[SL₂ℤ:Γ₀(49)]=56, dim 592 (MR1). Leading term 42·3·56/12 = 588, +4 corrections.
"Old" (model): images under degeneracy maps of levels M | 49, M<49, i.e. via Perm(P¹(ℤ/49)) → Perm(P¹(ℤ/7)) → trivial (coset projections). Atkin–Lehner multiplicity σ₀(49/M): old = 3·new₁ + 2·new₇.
- new₁ = dim S₄(SL₂ℤ, ρ̄) = 11 (corpus).
- dim S₄(Γ₀(7), ρ̄): ABSENT as exact. Leading term 42·3·8/12 = 84. Crude upper bound (Γ₀(7): ε₂=0, ε₃=2; elliptic correction ≤ 2·42·⅔ = 56; cusp terms only subtract) ⇒ ≤ 140.
- Hence new₇ ≤ 129 (nominal ≈ 73), old ≤ 33 + 258 = 291 (nominal ≈ 33+146 = 179).
- **S_new ≥ 592 − 291 = 301 (rigorous under the model); nominal estimate ≈ 413.**
- Stub S_new≈581 = 592−11 is **wrong/incomplete**: it counts the level-1 old once (multiplicity should be 3) and omits level-7 old entirely. Caveat: multiplicities assume degeneracy maps act on the Perm factor only (ρ̄ is an SL₂ℤ-rep, so this is legitimate in the induced picture); exact old-embedding injectivity ABSENT (Written by MR1 not yet).

## 2. Why R4 ≠ 0 at κ=4
Newspace leading term ( terms of old: level-1 leading 42·3/12=10.5, level-7 leading 84) ⇒ new leading ≈ 588 − 31.5 − 2·(84−10.5) ≈ 409.5; i.e. ~70% of ambient survives. Rigorous floor 301 ≫ 0. Vanishing would require old ≥ 592, impossible since old ≤ 291.

## 3. R5 — W₄₉ on Perm (Soft SF-safe)
Define W₄₉ := Atkin–Lehner/normalizer element (0 −1; 49 0) acting by conjugation on Γ₀(49), realized as the induced involution on the coset factor P¹(ℤ/49) (x ↦ −1/(49x) on cosets) — acts on Perm only, ρ̄ factor untouched. **No ρ(W₇) on V₄₂.** W₄₉² = 1 ⇒ eigenvalues ±1, preserves the newspace.
dim_± = (n ± tr W₄₉)/2. Trace term (fixed-point/class-number contribution) exact: ABSENT; it is lower order (no μ-term), so each eigenspace ≈ n/2: ambient ≈ 296 each, newspace ≈ 207 each (nominal), larger eigenspace ≥ ⌈301/2⌉ = 151 rigorous.
Why ≠0: a sign-cut to 0 needs W₄₉ ≡ ∓1 on the whole space, i.e. |tr| = n, contradicting tr = lower-order. Rigorous smaller-eigenspace floor: ABSENT (needs trace).

## 4. Forbidden twin
ρ(W₇) acting on V₄₂ (Fricke Role A / Path A) — NOT applied. Soft SF F3 CLOSED, Path C CLOSED. W₄₉ here is ≠ Fricke W₇ and acts on Perm only. Admissible only if Owner Writes the Perm-side operator.

## 5. Combined R4∘R5 (order irrelevant; commute)
Nominal ≈ 207 per sign (≈ 413/2); rigorous: larger sign ≥ 151, chosen-sign floor ABSENT but heuristically ≈ 150–207. **Cannot vanish at κ=4. FAIL diagnostic.** Never equals full P5a.

## 6. Scalar sanity (analogy only)
S₄(Γ₀(49)) = 10, old₇ = 2 (S₄(Γ₀(7))=1, ×2), old₁ = 0, new = 8 (Rank 11). Ratio new/ambient 0.8 ~ consistent with §2. Scalar W₄₉ eigen-split: ABSENT (not computed here; not to be imported as ρ̄ data).

## Soft SF risks
- Old multiplicities (3,2) & injectivity are a model, not Owner-Written; risk of invent if promoted.
- dim S₄(Γ₀(7),ρ̄) and tr W₄₉ ABSENT; only bounds shipped.
- Any slide from W₄₉-on-Perm to ρ(W₇)-on-V₄₂ reopens F3 — keep labeled Perm-side.
