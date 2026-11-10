# FINDINGS (Local) — G-vi-1 proof-pursuit deepen, targets P1–P5, s∈{7,8,11} — 2026-10-27 (CDT, America/Chicago)
Mode: Soft SF Write-only. REPORTS ONLY. No RECS. No tip fold. Kerr BLOCKED. No new invented values (HARD GATE).

## 1. Authority (live sha256)
| item | sha256 |
|---|---|
| tip LOCK `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` (BEFORE) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |
| G-vi-1 canon invent | 480f6d7298face1e9b15b51fd3d747a83b5c7384556721fcdae80994d4e1344d |
| proof-pursuit attach (stays OPEN) | dccf3a8c0369985062f44fabb615e0d357d181f7218af99d0b093f49c43dc43c |
| growth class (Pack KB MET) | b19e12e6c313c98c40e28ce406ec08b3796fe8b0ad0f87a13365da1891c2d949 |
| Rank27 ("No level/multiplier/shadow") | 55b3cf0bce4e5734154b9ed1fd6c3cb78d4c5ba8150bd856b78a272302523517 |

The canon label "invented pending mathematical proof" is unchanged. C1 and the n↔A map (D1 norm f8c95f7c…) belong to the Non Local lane and are not touched here.

## 2. Literature cited (not re-proven)
- L1. Dragonette (1952), Andrews (1966): for Ramanujan's f(q)=Σ q^{n²}/(−q;q)_n², the coefficients satisfy α_f(n) ∼ (−1)^{n−1} e^{π√(n/6 − 1/144)} / (2√(n − 1/24)).
- L2. Bringmann–Ono, Invent. Math. 165 (2006): proof of the Andrews–Dragonette exact formula. It uses q^{−1}f(q^{24}) as the holomorphic part of a weight-½ harmonic Maass form on Γ₀(144) with a Nebentypus-type character.
- L3. Zwegers, thesis (2002): weight-½ completion of mock theta functions; the congruence-subgroup generalization is "could certainly be" done but is not carried out (already cited at tip L434 P6 via Rank27).
- L4. Generic Rademacher/Poincaré leading term for weight k (Bringmann–Manschot class, cited in b19e12e6…): c(n) ≈ (2π/c)·a(−Δ)·K_c·(Δ/n)^{(1−k)/2}·I_{1−k}(4π√(Δn)/c).

## 3. Template check (new, cite-grounded, no new values)
I applied the canon's leading-term formula (canon §4: β = 4π√Δ/c, α = −1/2, A = a(−Δ)|K|/√(2c)) to the cited template f(q), with Δ = 1/24 and a(−Δ) = 1:
- The L1 exponent π√(n/6) equals 4π√(n/24)/c only for **c = 2**, not c = 1. So for f itself the dominant Kloosterman modulus is 2. The c = 1 contribution is absent or cancels (Dragonette/Andrews sum over even k).
- With c = 2: α = −1/2 matches L1's 1/√n. A = |K|/√4 = |K|/2 matches L1's prefactor 1/2 when |K_2| = 1. The (−1)^{n−1} sign is carried by K_2.
- Result: the formula's shape (exponent law, n^{−1/2}, the 1/√(2c) prefactor) reproduces a known weight-½ mock theta asymptotic exactly at leading order. The **choice of c_min is not fixed by the level alone**. It depends on which cusps carry principal parts and on the multiplier. On the template, c_min = 2 is neither 1 nor the level 144 of the L2 rescaled model.

## 4. Target status
| target | status | basis |
|---|---|---|
| P1 N_s = 4s | NOT-FEASIBLE-PENDING | The transformation law of ĝ_s is ABSENT (Rank27). The L2 template is not consistent with a "4 × scaling" level rule: f rescales to level 144 = 24²/4, not to 4·1. No source on disk or in the literature cited here fixes the level of ĝ_s. |
| P2 m_s = 1, Δ = 1/24, pole at ∞ only | PARTIAL | Δ = 1/24 is cite-grounded for the s = 1 template f (L1, L2). For g_s it is still an assertion. Caution: if g_s involves a pure q→q^s substitution of an f-type series, then the polar exponent scales to s/24 (compare superseded parallel invent B). The defining formula of g_s is not on disk in explicit form, so this cannot be decided. "Pole at ∞ only" is also unproven: on the template, the c = 1 cancellation (§3) shows the cusp configuration matters. |
| P3 β_s = π/(2√6·s) | PARTIAL | Two steps are MET: the algebra 4π√(1/24)/(4s) = π/(2√6·s), and the law β = 4π√Δ/c_min (L4, confirmed on the template in §3). The inputs Δ and c_min = N_s = 4s inherit P1/P2, which are NOT-FEASIBLE-PENDING/PARTIAL. The template shows that c_min = N_s is a further unproven step. |
| P4 α = −1/2 | MET (conditional) | Under L4 the exponent is −(1−k)/2 − 1/4 = (k−1)/2 − 1/4, which is independent of N, Δ, a and K. With k = ½ (Written, D1/D2) this gives −1/2, confirmed on the template (L1). The one condition is the growth-class hypothesis in b19e12e6…: ĝ_s is a weight-½ harmonic Maass completion with nonzero principal part. |
| P5 A_s = 1/√(8s), a(−Δ) = 1, K = 1 | PARTIAL | The prefactor law A = a|K|/√(2c) is MET on the template (§3, gives 1/2). a(−Δ) = 1 and \|K\| = 1 for g_s need Fourier/multiplier data, which is ABSENT. c = 4s inherits P1. |

The canon values for s = 7, 8, 11 are unchanged (β_s = 0.091611 / 0.080159 / 0.058298; A_s = 0.133631 / 0.125000 / 0.106600). They stay invented pending proof. No replacement values are proposed.

## 5. What would close each open item (descriptive, not RECS)
P1/P2 need the explicit series g_s and its transformation law (multiplier system, cusp principal parts). P3/P5 then follow from L4 once c_min and the leading Kloosterman value are read off. Without the explicit g_s definition, the multiplier and cusp configuration cannot be computed.

## 6. Non-claims
No proof of modularity for ĝ_s. No Fourier coefficients computed. No C1 evaluation. No READY YES or Bridge YES. G-vi-2 is not affected. The proof-pursuit attach dccf3a8c… stays OPEN. Professor Proof was not re-contacted.

## 7. Tip verify
BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. AFTER: recomputed in the PRESS. tip_touched NO.
