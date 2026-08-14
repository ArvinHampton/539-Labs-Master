# RH Conditional Templates Expanded (2026-08-13)

**Status label:** RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
**Category A only where proved. Residual-flux provenance mandatory. ZLA.**
**Does not prove:** DH, Iso_H, unconditional Mass-with-A, O-M1.3bis, O-TL, RH.
**Ranked path item 2.**

This note expands the existing conditional templates under a named density hypothesis so that the constants, height ranges and implication chains are fully explicit. Every statement below that uses DH is conditional on DH. No unconditional progress is claimed.

---

## 1. Named hypothesis

DH(beta-star, C). There exists a finite C such that for all T at least 2,

N(beta-star, T) is O of (log T) to the C.

Here beta-star is a fixed abscissa strictly greater than one-half and at most 0.80. This is the density input that the Step B gap table shows is missing from classical technology at moderate sigma. It is not implied by Ingham, Chourasiya-Simonic, or Guth-Maynard, all of which leave a positive power of T.

---

## 2. Conditional majorant Phi under DH

Recall the template

Phi(sigma, t-star, X) equals Phi-zeros plus Phi-explicit-truncation plus Phi-GHK.

Under DH(beta-star, C), the zero-sum piece on the segment from one-half to beta-star may be replaced by a polylog count. Grouping ordinates in windows of length H and applying DH at abscissa beta-star gives the schematic bound

Phi-zeros(sigma, t, X) is much less than (log t) times (log (t + H)) to the C, over H, plus a density-error term that is itself polylog under DH.

Choosing H of size, for example, (log t) to a fixed power larger than C makes Phi-zeros of size o of any positive power of t, and in particular smaller than a fixed fraction of the on-line reservoir of size asymptotically the square root of X over log X, provided X itself grows at least like a small power of t.

The remaining two pieces are not improved by DH:

- Phi-explicit-truncation remains a classical truncated-explicit-formula remainder.
- Phi-GHK remains the hybrid error. Under a growing X of t this piece is exactly the content of the usable-strip specification. DH does not control it.

Conditional integral test. Assume DH(beta-star, C) and assume a usable GHK strip bound in the sense of the companion specification. Then there exist sigma-star in (one-half, beta-star] and a positive-density set of heights t-star on which

the integral from one-half to sigma-star of Phi is strictly smaller than half the on-line reservoir.

This is a template implication only. It is not an unconditional evaluation of the integral, and it is not a discharge of O-M1.3bis.

---

## 3. Conditional Mass-with-A under DH

Assume the residual-mass / explicit-formula package (RM) as already fixed in the programme notes, and assume DH(beta-star, C) at the abscissa of a rightmost zero on a positive-density height set. Then on that set

A is much less than M log T with M equal to O of (log T) to the C, hence A is O of (log T) to the C plus 1.

That is Mass-with-A in the programme sense. Combined with the already-recorded ND1 chain, this yields B-theta whenever the remaining RM hypotheses of that chain hold.

DH does not imply Iso_H. The implication (RM) plus Iso_H implies B-theta remains a separate recorded chain and is not replaced by DH.

---

## 4. What these templates do not do

They do not prove DH at any moderate abscissa.
They do not evaluate the Phi integral on any concrete height.
They do not open the O-M1.2 joint window under classical density.
They do not discharge O-PC, O-Moll or O-TL.
They do not use residual packaging, 539 or continuum constants as lemmas about zeta.

---

## 5. Programme use

Keep every theorem environment that invokes DH explicitly conditional.
Do not silently replace DH by a classical positive-power density bound.
The templates are ready to accept a future classical improvement if one appears; they do not anticipate one.

*Per aspera ad astra.*
