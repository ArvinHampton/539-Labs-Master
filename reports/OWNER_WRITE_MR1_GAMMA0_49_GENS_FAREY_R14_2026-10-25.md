# OWNER_WRITE — MR1 Γ₀(49) gens via Kulkarni Farey symbol (R14)
Category B Author Write under Owner Farey-adopt (2026-10-25 ~21:45 CDT America/Chicago). Ready for Auditor CONFIRM. **No tip fold. tip_touched NO** (tip sha `d5f8b9d33e855d85c4792325d9aa11714bc61e21c6856893fbb355e18ae00c04`).

## Named presentation adopted
**Kulkarni Farey symbol of Γ₀(49)** — R. S. Kulkarni, "An arithmetic-geometric method in the study of the subgroups of the modular group", *Amer. J. Math.* 113 (1991) 1053–1133; as implemented in SageMath `Gamma0(49).farey_symbol()` (`sage.modular.arithgroup.farey_symbol.Farey`, C. Kurth's KFarey implementation; Kurth–Long, "Computations with finite index subgroups of PSL₂(ℤ) using Farey symbols", 2008). Computed on-box with passagemath-schemes 10.5.49 (pip, venv `/tmp/pm`). No on-box literature Farey symbol existed (Auditor t2144u deep-dig CONFIRM: gens ABSENT). Nothing hand-invented: fractions, pairings and generators are the algorithm's output.

**Farey symbol (Sage output):**
- fractions: −∞, 0, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 2/5, 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 1, ∞
- pairings (Sage encoding; −3 = odd/order-3 side): [1, 4, 4, 2, 3, 8, 8, −3, 6, 6, 7, 7, −3, 9, 9, 2, 3, 5, 5, 1]
- paired sides: (0,19), (3,15), (4,16), (1,2), (17,18), (8,9), (10,11), (5,6), (13,14)
- index 56 in PSL₂(ℤ), genus 1, ν₂ = 0, ν₃ = 2, cusps {0, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, ∞} (8). Check: 2g + (c−1) + ν₃ = 2 + 7 + 2 = **11 gens**.

## Generators (side-pairing → generators; Sage `F.generators()`); all det 1, c ≡ 0 mod 49 (verified)
Words in S = (0,−1;1,0), T = (1,1;0,1), verified exactly by multiplication:

| γ | matrix (a,b;c,d) | type | word |
|---|---|---|---|
| g1 | (1,1;0,1) | parabolic | T |
| g2 | (8,−1;49,−6) | parabolic | S T⁻⁷ S T⁻² S T⁻² S T⁻² S T⁻² S T⁻² S T⁻² S T⁻² S T⁻¹ |
| g3 | (38,−7;49,−9) | hyperbolic | S T⁻² S T⁻² S T⁻² S T⁻⁴ S T⁻² S T⁻² S T⁻² S T⁻² S T⁻¹ |
| g4 | (40,−9;49,−11) | hyperbolic | S T⁻² S T⁻² S T⁻² S T⁻² S T⁻⁴ S T⁻² S T⁻² S T⁻² S T⁻¹ |
| g5 | (15,−4;49,−13) | parabolic | S T⁻⁴ S T⁻² S T⁻² S T⁻³ S T⁻² S T⁻² S T⁻¹ |
| g6 | (−18,7;−49,19) | elliptic ord 3 | −I · S T⁻³ S T⁻⁴ S T⁻³ S T⁻² S T⁻¹ |
| g7 | (22,−9;49,−20) | parabolic | S T⁻³ S T⁻² S T⁻² S T⁻² S T⁻⁴ S T⁻² S T⁻¹ |
| g8 | (29,−16;49,−27) | parabolic | S T⁻² S T⁻⁴ S T⁻² S T⁻² S T⁻² S T⁻³ S T⁻¹ |
| g9 | (−30,19;−49,31) | elliptic ord 3 | −I · S T⁻² S T⁻³ S T⁻⁴ S T⁻³ S T⁻¹ |
| g10 | (36,−25;49,−34) | parabolic | S T⁻² S T⁻² S T⁻³ S T⁻² S T⁻² S T⁻⁴ S T⁻¹ |
| g11 | (43,−36;49,−41) | parabolic | S T⁻² S T⁻² S T⁻² S T⁻² S T⁻² S T⁻² S T⁻² S T⁻⁷ S T⁻¹ |

Γ₀(49) = ⟨g1,…,g11, −I⟩ (Farey gens are for the PSL₂ image; −I = S²).
**Γ₀(49)⁺ (tip G):** Γ₀(49)⁺ = ⟨g1,…,g11, W₇⟩, W₇ = (0,−1;49,0) (det 49; normalises Γ₀(49); W₇² = −49·I, scalar — PSL₂-style R4 per tip P1-R1). W₇ ∉ SL₂(ℤ), so it has **no S,T word**.

## Feeding ρ(γᵢ) (mechanics only)
For γ = ε·X₁…X_n (Xⱼ ∈ {S, T^e}, ε = ±I): ρ(γ) = ρ(ε)·ρ(X₁)…ρ(X_n) on V₄₂, with ρ(S) = S_lab⁻¹, ρ(T) = T_lab (ρ_N₂|_V, Borcherds convention, tip §2), ρ(T^e)=T_lab^e, ρ(−I)=ρ(S)² = S_lab⁻². Restriction to Γ₀(49) is the Owner-Written SF-1 label. **No numeric ρ matrices filled here** (none Author-Written). ρ(W₇) is a separate generator image with no S,T word.

## Explicit
- **ρ(W₇) NOT invented** — R15 remains **Owner NEED**.
- No Z₇↔W₇. Exact-c Cat B APPLIED (unchanged). Bridge PARTIAL; READY NO. Not Cat A.
