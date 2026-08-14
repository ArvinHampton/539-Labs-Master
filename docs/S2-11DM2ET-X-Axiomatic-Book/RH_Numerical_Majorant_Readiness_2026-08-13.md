# RH Numerical Majorant Readiness (2026-08-13)

**Status label:** RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
**Category A only where proved. Residual-flux provenance mandatory. ZLA.**
**Does not prove:** O-M1.2, O-TL, RH.
**Ranked path item 3.**

This note records the numerical architecture that would convert a classical density statement into concrete majorants A, B, C, and records why tightening the present GHK constant c1 alone cannot open the joint window at the reference height.

---

## 1. Frozen arithmetic at the reference height

At gamma equal to 3 times 10 to the 12 and under the current far-zero architecture:

- the log X required to drive the far-sum down to 0.4 is about 7224;
- at that X the GHK first term, proportional to c1 times X to the fourth over gamma squared, is not finite in any useful sense;
- a scan over polylog, exponential-log-power and power families for X produced zero joint successes under c1 equal to 291.

That obstruction is frozen. It is not reopened by the present pass.

---

## 2. Why c1 tightening alone fails at this height

The first GHK term scales as c1 times X to the fourth. The far-sum wants X of size exp of 7224. No reduction of c1 by a polynomial, or even by an exponential of a moderate power of log gamma, can compensate X to the fourth at that size. Therefore a weight-only refinement that leaves the far-sum architecture and the remainder target unchanged does not open the joint window at H_RH.

---

## 3. What would open a window

A non-empty joint window at some height appears only if at least one of the following changes.

A. The far-sum architecture is fed a stronger density input, so that the required log X drops into a range where X to the fourth over gamma squared is comparable to the model size. This is exactly the polylog-at-moderate-sigma gap. It is open.

B. The remainder target is weakened from a fixed fraction of the reservoir to a size o of log log X, which some path designs can tolerate. This is a change of goal, not a theorem, and must be declared if used.

C. The height is restricted to a range that carries a stronger classical zero-spacing or zero-density input than the uniform moderate-sigma table. No such restricted range is claimed here to open the window.

D. A usable growing-X GHK strip bound (companion specification) is supplied together with an X-strategy that is already small enough for the first term. This still needs A or B or C to make X small enough.

---

## 4. Ready conversion recipe (not executed)

If a named classical density theorem D supplies N(beta-star, T) much less than T to the alpha times a polylog, the conversion is:

1. Recompute the far-sum majorant A under D in place of the Ingham or Chourasiya-Simonic exponent.
2. Recompute the required log X for far-sum at most the chosen target.
3. Evaluate the GHK majorant B at that X and at the programme c1, c2.
4. Record whether A and B are simultaneously below target. That pair, together with the explicit-truncation majorant C, is the numerical triple for O-M1.2 under D.

The recipe is ready. It is not run against any new D in this pass, because no new D converting the positive power of T into a polylog at moderate sigma is available.

---

## Global non-claims

O-M1.2 remains open. The joint window at H_RH remains empty under current classical density and current c1. No new density theorem is claimed. Residual packaging is not used in the majorants.

*Per aspera ad astra.*
