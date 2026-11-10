# Eigen q89 basis through q^18 — FINDINGS (2026-10-26)

**STATUS: PARTIAL.** The seeds are exact and Written. The explicit 89-form weight-4 basis is NOT built, and no coefficients were invented.

## Authority (sha256 re-verified before writing)
- CLOSED_A a8935bf7a7ad73008b219443d675e94c3bc0ffece63dc8ad3e42ab77e8f75487 OK
- ASSIGN 3eece5f191723f340f43d93f177ad481093a128a1810b3271ef780575e6e4992 OK
- Prior Step3 MATCH 88911d8c71ae8e4fd791b944227aaa116c12241365ca985d4376341dfb32959a OK. It stands: dim M4 = 89, and truncation through q^18 is injective.
- Card1F OW 03227e61… and Card1F PARTIAL cd960dd1… are cited. They give the ρ₄/ρ₅/ρ₇ matches.
- Tip Soft SF LOCK start = end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. **tip_touched NO**

## Done: exact seeds through q^39, from Written formulas only (eigen-q89-basis/seeds.sage)
- **Elkies Klein x, y, z** come from the Written product formula (4.6). Prefactors are q^{4/7}, q^{2/7}, q^{1/7}.
  - The series reproduce every Written term of (4.4) through q^10 (assertion passed).
  - The Klein relation (4.7), x³y + y³z + z³x = 0, holds exactly to O(q^38).
- **Rogers–Ramanujan G, H** come from Duke (4.2). The product side equals the sum side exactly (assertion passed).
- **η** is taken from its product formula.
- **ρ₇ (dual V*)**: realized by the Λ² / Rankin–Cohen brackets of (x, y, z), weight 6. T-exponents are {6/7, 5/7, 3/7}, which equals the Card1D target.
- **ρ₅**: realized by η¹⁰·(q^{-1/60}G, q^{11/60}H). T-exponents are {2/5, 3/5}, which equals the target.
- **ρ₄**: the character η^{18−24m}.
- Every ρ̄-irrep factor is pinned by its T-spectrum and the parity of S². So the product seed realizes ρ̄ up to a diagonal intertwiner, because the 6 T-exponents of ρ̄ are distinct.

## Not done: the blocker (computational, not a Written gap)
1. **The weight bound rules out the naive tensor route.** The lowest holomorphic seed product is η⁴ ⊗ (η¹⁰R) ⊗ Λ²(x,y,z), which has weight 8 > 4. With η^{−20} the result is not holomorphic at ∞. Also, Σ(T-exponents of ρ̄) = 7.5, so the 6 SL₂ℤ-generators of M(ρ̄) have total weight 90.
   - So M₄(ρ̄⊗Ind) = {Σ Φ_j·h_j} requires *weakly holomorphic* h_j ∈ M^!_{4−k_j}(Γ₀(49)), with holomorphy imposed at all 8 cusps of Γ₀(49).
   - Doing that needs cusp expansions of the h_j at 1/7·a (over ℚ(ζ₇)). It also needs the exact ρ̄(S) in seed coordinates, i.e. the diagonal normalization of the seed vector against local_factors S̄. Neither is assembled yet.
2. **The Magnusson–Raum route (arXiv:2202.06676) is not implemented.** It needs a custom implementation (products of level-N Eisenstein series, then a Hecke/S-action solve). Within this run it was not built, so no MR coefficients exist.
- No Written source is missing: Elkies (4.6), Duke (4.2) and η are all Written and suffice as seeds. The gap is compute or implementation only.

## Owner ask (one crisp Write, optional)
Authorize Eigen to derive ρ̄(S) in the seed T-eigenbasis numerically and then recognize it exactly in CF(140), certified against local_factors S̄. Then run the Σ Φ_j h_j holomorphy solve over the 8 cusps of Γ₀(49), with exact cusp-width bookkeeping, and target rank 89 through q^18. A further option is mod-p first, with a CRT/lift path.

## Artifacts (eigen-q89-basis/, see ART.sha)
231b21350d596fea3bd0c06f76255b766acb351de231b832f76771efe6bc7082  seeds.sage
bf79c74d873b78e894a86f2ea4c2e52701fe9cd665d0277a6eae7aa09270ee22  seeds.log
79efec1d98dc7b9290faac35ccbb7ba1493eb60983a228e5e942b25510c5413d  seeds.sobj

## Constraints honored
invent HOLD; no tip fold; Soft SF F3 CLOSED; Bridge PARTIAL READY NO; Cards 8–11 not opened; no messaging.
