# RH Usable GHK Strip Specification (2026-08-13)

**Status label:** RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
**Category A only where proved. Residual-flux provenance mandatory. ZLA.**
**Does not prove:** O-PC strong, O-TL, RH, any off-line resonance lemma.
**Direction:** Solid Direction 4, obstacle O4.1. Ranked path item 1.

This note distinguishes the already-recorded fixed-X strip arithmetic (R4.1) from the usable bound that Direction 3, Direction 4 and the O-M1.2 joint window actually need. No such usable bound is claimed.

---

## 1. What R4.1 already records

For admissible hybrid constants c1, c2 of the programme weight f-star and for each fixed X greater than or equal to 3,

|E_GHK(sigma + i t, X)| is at most c1 times X to the fourth over t squared times (log X) squared, plus c2 times X to the minus sigma times log X.

Hence, for each fixed X, there exists a height t0 of X such that for all |t| at least t0 and all sigma in a thin strip to the right of one-half, the first term is negligible and the error is controlled by the second term alone. That arithmetic is recorded and is not reopened.

R4.1 therefore controls the pure GHK multiplicative error off the line when X is held fixed and height tends to infinity.

---

## 2. Why R4.1 is not yet a usable programme input

Path continuation (Direction 3) and offline conversion (Direction 4 / O-PC) require an X that grows with height. Under a growing family X = X(t) the first term c1 X to the fourth over t squared is no longer automatically small. The O-M1.2 joint window at the reference height 3 times 10 to the 12 likewise needs an X large enough to kill the far-zero sum, which drives the same first term to explode under the present c1 equal to 291.

A usable strip bound is therefore a statement about a growing family X of t, not about a single fixed X.

---

## 3. Precise success criterion for a usable bound

A classical statement counts as a usable thin-strip GHK bound for the programme if and only if all of the following hold.

There exist a width delta-zero greater than 0, a height T0, an admissible family X = X(t) for t at least T0, and an explicit constant kappa less than one-half, such that for every sigma in the closed interval from one-half to one-half plus delta-zero and every t at least T0,

|E_GHK(sigma + i t, X(t))| is at most kappa times the square root of X(t) over log X(t).

The family X of t must be admissible under the zero-density language architecture (no residual-algebra input, no 539, no continuum constants). The constant kappa must be small enough that the offline conversion and the path-continuation integral test can absorb it; one-half is the programme default.

Until a theorem of this shape is obtained or cited, obstacle O4.1 remains open and the offline path cannot close.

---

## 4. What a refinement of the weight would have to do

Smoothing the cutoff, changing the support, or reducing c1 can help only if the resulting first term stays below the model size for some growing X of t that is still large enough for the far-zero sum or for the path majorant. At the reference height, the far-sum architecture currently wants log X of order 7224, which makes X to the fourth hopeless under any reasonable c1. Therefore a weight refinement that only shrinks c1, without changing the far-sum architecture or the remainder target, does not open the joint window at that height.

Legitimate remaining levers inside classical technology:

- a different X-strategy that does not require such a large X (this needs a stronger density input, which is itself open);
- a weaker remainder target of size o of log log X rather than a fixed fraction of the reservoir;
- restriction to a height range where stronger zero-spacing or zero-density inputs are available;
- a genuinely better decay of the hybrid kernel in a thin strip, strong enough to meet the criterion of section 3 for some growing X of t.

None of these is claimed achieved in the present pass.

---

## 5. Obstacles still standing after a usable bound

Even if section 3 were supplied, O4.2 (nearby zeros in a disk of radius about 1 over log X), O4.3 (continuous argument versus principal imaginary part) and O4.4 (correlation of torus maximisers with zeros) would remain. A usable GHK strip bound is necessary for the offline path; it is not sufficient.

---

## Global non-claims

No usable growing-X strip bound is claimed. R4.1 is not upgraded. O-PC, O-M1.3bis and O-TL remain open. The Riemann Hypothesis remains open. Residual packaging, 539 and continuum constants are not used as lemmas about zeta.

*Per aspera ad astra.*
