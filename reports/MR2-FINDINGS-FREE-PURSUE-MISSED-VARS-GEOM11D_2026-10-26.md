# MR2 FINDINGS — Free pursue missed variables (geom / 11D / residual lane) — 2026-10-26 (America/Chicago)
Authority: OW 687b27f5… ; ASSIGN d763ac36… ; Invent/proof OW ef6da7e7…. Eight-only. Kerr/Path4 C2–C3 NOT pursued. No Eigen/Ops. CatB-2 BT saturation NOT duplicated (cited only).
tip Soft SF LOCK `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha 7cddb188… before AND after; tip_touched NO (read-only).

**STATUS: PARTIAL** (T1 HIT-distinction proved + named gap; T2 PARTIAL: invariants proved, physics link ABSENT/UNPROVEN; T3 ABSENT)

## (a) What is pursued
- **T1** Residual language collision: BT St⊗χ residual (CatB-2) vs Zwegers/ĝ residual vs tip residual-C `residual_factor ∈ V` (dim 42). Correlation or false synonym?
- **T2** Missed volume variable for Ω₀ / f_warp / f_curv on Path C operative G = Γ₀(49) vs tip convention C_vol = 1.
- **T3** 11D / M-theory compactification source for f_warp, f_curv on disk.

## (b) First findings
### F1 (T1) — PROVED: the three "residuals" are distinct objects (false synonym at the type level); one genuine correlation exists only via quadratic twist
1. *Places differ.* Teitelbaum residual = Γ-invariant harmonic cochain on the Bruhat–Tits tree of PGL₂(ℚ₇) (non-archimedean place p=7). Zwegers residual = non-holomorphic completion / shadow term (archimedean place, R-valued Mordell-type integral). Tip residual_factor = vector in a 42-dim Weil/Siegel-theta span at leading radial order (tip §1b). Objects in different categories (cochain on E(T₇); real-analytic function on H; vector in V) → no identity possible as stated. ∎
2. *Level obstruction (proved).* Teitelbaum's harmonic-cochain uniformisation needs local component at 7 = Steinberg with **unramified** twist, conductor exponent 1 (7 ‖ level; S-arithmetic Γ₀(M)[1/7], 7∤M per CatB-2). Operative G = Γ₀(49) has 7² | level, so a newform on Γ₀(49) is never St⊗(unramified) at 7. The only Steinberg-type option at conductor 7² is St⊗χ with χ ramified (quadratic, conductor 7: a(St⊗χ)=2·a(χ)=2). ∎
3. *Correlation (proved, conditional on form type).* If f ∈ S_k^new(Γ₀(49)) has π_{f,7} ≅ St⊗χ₇ (χ₇ = quadratic char mod 7), then f⊗χ₇ has π_7 ≅ St (unramified twist), conductor 7, so f⊗χ₇ ∈ S_k^new(Γ₀(7)) and **then** Teitelbaum's BT cochain applies. So "BT St⊗χ residual" correlates to tip level 49 only through the twist f ↦ f⊗χ₇. (Standard: conductor of twist; local Langlands for GL₂.)
- **UNPROVEN gap G1:** no map V(dim 42) → harmonic cochains on T₇ (nor to Zwegers shadows) is constructed; whether residual_factor components are twist-images of St-type forms is open. Requires an explicit newform decomposition at level 49 (Eigen lane — not entered).

### F2 (T2) — PROVED invariants; missed variable = vol(Γ₀(49)\H)
- [SL₂(ℤ):Γ₀(49)] = 49(1+1/7) = **56**; cusps = Σ_{d|49} φ(gcd(d,49/d)) = 1+6+1 = **8**; ν₂ = 1+(−1/7) = 0; ν₃ = 1+(−3/7) = **2**; genus g = 1+56/12−0−2/3−8/2 = **1** (checks X₀(49) elliptic). Hyperbolic area **vol = 56·π/3**. ∎ (verified numerically on box).
- Missed variable: tip sets C_vol = residual_B1 = 1 by convention. Petersson-normalised alternative C_vol' = (56π/3)^{-1/2} (or index-56 normalisation relative to SL₂(ℤ)). This is a candidate natural Ω₀ ("volume factor").
- **UNPROVEN gap G2:** no proof that Ω₀ must equal vol(Γ₀(49)\H) (or 56); the convention C_vol=1 is internally consistent, so this is a *choice*, not a forced value. Not a tip fold.
- Name-coincidence note: 8 cusps ≠ "eight agents"; 56 ≠ any η-exponent. No claim.

### F3 (T3) — ABSENT
- No on-disk 11D / M-theory compactification literature supplying f_warp or f_curv for Γ₀(49) found in MR2 corpus scan. Any warp-volume = modular-volume identification is **UNPROVEN** (gap G3: needs a named compactification whose moduli space is X₀(49) — none cited).

## Not claimed
Bridge PARTIAL, READY NO. P5a NOT proved. No Cat A. No tip edit. q^18/η¹⁸ (5dd25a92…) and RH map (9910ade2…) not re-opened: no new proof.

## Soft SF risks (≤3)
1. "St⊗χ residual" wording could be read as level-49 Teitelbaum applicability — F1.2 shows it needs the χ₇ twist.
2. C_vol' = (56π/3)^{-1/2} must not be folded as forcing over C_vol=1 convention.
3. 11D/warp language ABSENT — no physical-load claim.

Soft SF press needed: **yes** (Auditor on ship).
