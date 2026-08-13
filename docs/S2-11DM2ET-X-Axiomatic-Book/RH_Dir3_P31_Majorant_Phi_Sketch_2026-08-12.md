# RH Direction 3 — P3.1 Majorant Φ Sketch (2026-08-12)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** O-M1.3bis · O-TL · RH · any numerical bound on the integral  
**Base:** RH_Solid_Direction_3_Path_Continuation_Next_Step_2026-08-08.md

---

## 1. Target

Along a horizontal (or slightly inclined) path from ½ + i t_* to σ_* + i t_*,

|∂_σ Δ_X(σ + i t_*)| ≤ Φ(σ, t_*, X)

where Φ is an explicit majorant built only from classical objects admissible under ZLA. If the integral of Φ from ½ to σ_* is strictly smaller than half the on-line reservoir size, a large on-line value survives continuation.

---

## 2. Building blocks for Φ (template language)

Φ is assembled from three classical pieces. Constants are tracked symbolically; no numerical evaluation is claimed in this sketch.

1. Truncated explicit formula for ζ′/ζ  
   On the segment ½ ≤ σ ≤ 1 the logarithmic derivative admits a truncated explicit formula whose main term is a sum over zeros and whose remainder is controlled by the usual truncated von Mangoldt sum and the height of the truncation. The contribution of a zero ρ = β + iγ to |ζ′/ζ(σ + i t)| is bounded by a standard kernel of the form 1 / |σ + i t − ρ| (or a smoothed version). The zero-sum piece of Φ is therefore a sum of such kernels.

2. Classical density bound for the zero sum  
   The sum over zeros is estimated by grouping ordinates and applying a classical density theorem (Ingham shape, Chourasiya–Simonič, or Guth–Maynard in the ranges where they improve the exponent). The resulting contribution to Φ is of the schematic form

   Φ_zeros(σ, t, X) ≪ (log t) · N(σ − δ, t + H) / H + density-error term,

   where the density exponent is taken from the frozen Step B table. At moderate σ the density still carries a positive power of t; the sketch records that power and does not replace it by a polylog.

3. GHK / hybrid remainder  
   The hybrid discrepancy piece that appears in the programme definition of Δ_X contributes an error E_GHK(σ + i t, X). Off the critical line the growth of this error must be controlled. The sketch treats |E_GHK| as a separate additive term inside Φ and records that a uniform bound of size ≪ √X / log X (or any weaker explicit multiple) in a thin strip is precisely the content of obstacle O4.1 of Direction 4. Until that bound is available the majorant carries a placeholder growth factor.

---

## 3. Formal template (no claim of smallness)

Φ(σ, t_*, X) := Φ_zeros(σ, t_*, X) + Φ_explicit-truncation(σ, t_*, X) + Φ_GHK(σ, t_*, X)

with each piece expanded as above. The integral test remains

∫_{1/2}^{σ_*} Φ(σ, t_*, X) dσ   ?<   (1/2) |Δ_X(½ + i t_*)|.

Under the present classical density exponents the left-hand side is expected to be larger than the typical on-line reservoir on most heights; the sketch does not assert the opposite. A conditional version under a named density hypothesis DH(β⋆, C) can be written by substituting the polylog count into Φ_zeros, but that remains conditional.

---

## 4. Explicit non-claims

- No evaluation of the integral on any concrete height.
- No claim that the integral is smaller than the reservoir.
- No discharge of O-M1.3bis or O-TL.
- No use of residual packaging, 539, or continuum model constants inside the zeta majorant (ZLA).
- Monodromy of a zero-free path about a zero is not used (P3.3 freeze).

**Status code:** `RH_DIR3_P31_MAJORANT_PHI_SKETCH_2026-08-12`

*Per aspera ad astra.*
