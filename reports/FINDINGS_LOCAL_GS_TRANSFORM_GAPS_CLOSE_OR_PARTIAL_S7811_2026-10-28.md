# FINDINGS — Local: g_s=f(q^s) transform gaps, s∈{7,8,11} — CLOSE-or-PARTIAL — 2026-10-28
Status: PARTIAL. Does not rewrite 05f6bf59… or 82b8f1ed…. tip_touched NO. Kerr BLOCKED/not used.

## Basis (cite-grounded)
- Bringmann–Ono, Invent. Math. 165 (2006): M_f(τ)=q^{-1}f(q^{24}) + nonholomorphic Eichler-type period integral of a weight-3/2 unary theta (Zwegers 2002 thesis, Ch. 4 vector-valued completion) is a weight-1/2 harmonic Maass form on Γ₀(144) with Nebentypus χ₁₂=(12/·).
- Shimura/standard V(t) lemma (e.g. Ono, *Web of Modularity*, CBMS 102, §3): F∈M_{k+1/2}(Γ₀(4N),χ) ⇒ F(tτ) on Γ₀(4Nt), character χ·(4t/·). Applies verbatim to harmonic Maass forms (operator commutes with ξ_{1/2} up to the factor t^{1/2}).

## Gap 1 — Nebentypus from dilation: CLOSED (cite-grounded)
Object: M_f(sτ)=q^{-s}f(q^{24s})+nonhol., i.e. g_s at q↦q^{24} with q^{-s} prefactor.
| s | group | character | #cusps | cusps ≠ ∞ |
|---|---|---|---|---|
| 7 | Γ₀(1008) | χ₁₂·(28/·) | 48 | 47 |
| 8 | Γ₀(1152) | χ₁₂·(32/·)=χ₁₂·(2/·) | 64 | 63 |
| 11 | Γ₀(1584) | χ₁₂·(44/·) | 48 | 47 |
(4t/d)=(t/d) for odd d; (32/·)=(2/·). Shadow: ξ(M_f(sτ)) = s^{1/2}·(shadow)(sτ), weight 3/2 on Γ₀(144s) with conjugate character.

## Gap 2 — Principal parts at cusps ≠ ∞: PARTIAL / ABSENT in closed form
- At ∞: principal part q^{-s} (from q^{-1} under τ→sτ). CLOSED.
- Other cusps a/c of Γ₀(144s): expansion = expansion of M_f at the Γ₀(144) cusp (s·a)/c' after slashing by [[s,0],[0,1]]·γ. Determined in principle by Zwegers' vector-valued S,T transformation of (f, ω) third-order family (Watson relations; f↔ω under S). Explicit table for all 157 non-∞ cusps NOT computed here: requires the full Γ₀(144) cusp data of M_f (Bringmann–Ono give holomorphic-at-other-cusps statements only up to the ω-family components) — recorded ABSENT; reason: no cite-grounded closed table found, derivation not mechanically verified this run.
- Invented pending mathematical proof: principal parts at non-∞ cusps are supported only on cusps whose width-scaled image maps to the ∞-class of Γ₀(144)'s ω-component orbit; elsewhere holomorphic. LABEL: invented pending mathematical proof — NOT Written / not Cat A / not tip fold.

## Gap 3 — Completed transform law under Soft SF
Completed law (cite-grounded for weight/group/character; PARTIAL for cusp data): M_f(sτ) transforms with weight 1/2 under Γ₀(144s), character per table. Remaining ABSENT: explicit non-∞ principal parts; error-term bounds linking to β_s,A_s.

## β_s=π/√(6s), A_s=√s/2, α=−1/2
Remain invented pending mathematical proof. Gap 1 supplies level/character input for a circle-method/Rademacher-type route (Bringmann–Ono exact formula for f coefficients is the template), but exponent/constant derivation for g_s requires Gap 2 cusp data → proof path ADVANCED (inputs partly fixed), NOT closed. Not auto Written.
