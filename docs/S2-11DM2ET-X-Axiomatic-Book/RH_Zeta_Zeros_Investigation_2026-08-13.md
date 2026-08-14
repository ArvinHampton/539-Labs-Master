# Investigation: zeros of the Riemann zeta function (2026-08-13)

**Status label:** RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF
**Category:** pure A. Axiom ZLA in force. No model constants.
**Does not prove:** RH, Iso_H, Mass-with-A, B_theta, O-TL, any zero-free strip down to 1/2+delta.
**Does not use:** residual packaging integers, 539, O_res, K+, T-sharp, flux 4880.

This note records what is classically known about the zeros of zeta, what the programme already has locked about those zeros, and what remains open. It is an investigation, not a theorem that locates every nontrivial zero.

---

## 1. The function and the two families of zeros

The Riemann zeta function is first defined by the Dirichlet series

    zeta(s) = sum_{n=1}^infty n^{-s}

for Re(s) > 1, equivalently by the Euler product over primes. It admits analytic continuation to a meromorphic function on the whole plane, with a single simple pole at s = 1, and satisfies the functional equation relating zeta(s) to zeta(1-s) through the completed function xi.

There are two families of zeros.

**Trivial zeros.** These sit at the negative even integers s = -2, -4, -6, … . They come from the poles of the Gamma factor in the functional equation. They are completely understood and play no role in the Riemann Hypothesis.

**Nontrivial zeros.** These lie in the critical strip 0 < Re(s) < 1. They are customarily written rho = beta + i gamma, with 0 < beta < 1 and gamma real. They are symmetric: if rho is a zero then so is 1-rho and so is the complex conjugate. The first one on the critical line is approximately 1/2 + 14.134725 i.

The Riemann Hypothesis asserts that every nontrivial zero has beta = 1/2. That assertion remains open.

---

## 2. How many nontrivial zeros, and where they must live

The counting function N(T) is the number of nontrivial zeros with 0 < gamma ≤ T, counted with multiplicity. The Riemann–von Mangoldt formula gives

    N(T) = (T / 2 pi) log(T / 2 pi) - T / 2 pi + O(log T).

There are therefore infinitely many nontrivial zeros, and their ordinates have mean spacing 2 pi / log(T / 2 pi) at height T.

A classical zero-free region of Vinogradov–Korobov type keeps zeros out of a thin neighbourhood of the line Re(s) = 1:

    beta ≤ 1 - c / ( (log |gamma|)^{2/3} (log log |gamma|)^{1/3} )

for an explicit positive c (Ford; later explicit constants by Bellotti and others). This is a region next to Re(s) = 1, not a strip down to 1/2 + delta. It is compatible with RH and far weaker than RH.

The zero-density function N(sigma, T) counts nontrivial zeros with beta ≥ sigma and |gamma| ≤ T. Classical bounds of Ingham, Huxley, and Guth–Maynard (2024, published 2026) give

    N(sigma, T) ≪ T^{A(sigma)(1-sigma) + o(1)}

with A(sigma) a positive piecewise function. At every moderate abscissa sigma ≤ 0.98 the leading power of T remains strictly positive. In particular there is still no polylogarithmic bound on N(sigma, T) at moderate sigma. That gap is recorded in RH_StepB_Density_Gap_Table_2026-08-08.md and is the barrier on Solid Direction 1.

---

## 3. Zeros known to lie on the critical line

Three independent kinds of evidence put zeros on the line Re(s) = 1/2. None of them is RH.

### 3.1 Infinitely many, then a positive proportion

Hardy (1914) proved that infinitely many nontrivial zeros lie on the critical line. Selberg proved that a positive proportion do. Levinson (1974) raised the proportion to more than one third, and those zeros are simple. Conrey (1989) raised it to more than two fifths. Pratt, Robles, Zaharescu and Zeindler (published 2020; arXiv 2018) raised it to more than five twelfths, slightly over 41.6 percent. These are theorems about a lower bound on the density of zeros that do lie on the line. They say nothing about the remaining zeros.

### 3.2 Finite-height verification

Platt and Trudgian (Bull. London Math. Soc. 2021; arXiv:2004.09765) verified, with interval arithmetic, that every nontrivial zero with 0 < gamma ≤ 3 · 10^{12} lies on the critical line. That is a finite-height theorem. It does not constrain zeros of unbounded height. In the programme it does not supply Iso_H, which is an unbounded isolation statement about a putative rightmost off-line zero.

### 3.3 Announced 2026 proportion (not locked here)

On 10 August 2026 Anthropic announced that a combination of the Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh work with Bombieri (2000), found with assistance of their model Claude and examined by Conrey and Goldston, raises the Levinson-type lower bound from 41.6 percent to 67.2 percent, with a Lean formalization. The announcement itself states that the techniques are not expected to prove RH.

This note records the announcement. It does **not** lock 67.2 percent as a programme theorem. Even if the bound is later accepted in the journal literature, two structural facts remain:

- A proportion strictly less than 1 leaves a positive-density set of zeros unlocated.
- A proportion equal to 1 would still not be RH. Density one on the line permits a sparse sequence of off-line zeros of density zero. RH requires every zero.

The announcement therefore does not discharge Iso_H, Mass-with-A, B_theta, O-M1.2, O-PC, O-Moll, or O-TL.

---

## 4. Density is not isolation

The programme already has this distinction locked (RH_Density_vs_Isolation.md).

Density bounds N(sigma, T), a bulk count of zeros in a rectangle. Isolation constrains the local geometry around a single putative off-line zero. Mass-with-A can be fed by a polylogarithmic density bound or by a strong isolation hypothesis Iso_H. Half-isolation (Maynard–Pratt) and Levinson–Ivić horizontal isolation near sigma = 1 are different geometric objects; neither is Iso_H.

Consequences already locked:

- (RM) + Iso_H implies B_theta.
- (RM) + polylog StripDens implies Mass-with-A, which implies B_theta.
- Unconditional Iso_H is open.
- Polylog StripDens at arbitrary beta_star > 1/2 is open.
- Absolute averaging of the phase A is a closed non-route.

A better Levinson-type proportion on the line does not produce Iso_H. A better Guth–Maynard exponent does not produce polylog N(sigma, T) at moderate sigma. Finite-height verification does not produce unbounded isolation.

---

## 5. What the zeros do in the debt-argument

The explicit formula writes the Chebyshev function, or a smooth hybrid remainder, as a sum over nontrivial zeros plus archimedean and prime-power terms. In the programme that identity is the backbone of M1, of the GHK hybrid P_X Z_X, and of the majorant Phi.

- Distant zeros are controlled, if at all, by zero-density estimates. That is O-M1.2. The present hybrid constant and the positive-power density table leave the joint window empty.
- Nearby zeros and continuous argument enter O-PC. There is still no usable growing-X GHK strip bound.
- A putative rightmost off-line zero is the object of Form C / Iso_H / B_theta. Those engines are vacuous if RH is true. They are RH-failure tools, not a proof of RH.
- The on-line phase gates O-Moll and O-TL live on the critical line itself and remain open.

None of these obligations is discharged by knowing more zeros on the line at finite height, or by raising the Levinson proportion.

---

## 6. What may not be said about the zeros

ZLA: a theorem locating zeros of zeta may mention only zeta, its Euler product, its zeros, and classical number-theoretic auxiliaries. Residual packaging integers, 539, O_res, K+, T-sharp, and flux 4880 are inadmissible.

The residual No-Go theorem (NoGo_Theorem_Canonical.md) is not a theorem about these zeros. It does not constrain beta or gamma. See NoGo_Theorem_RH_Investigation_2026-08-13.md.

Forbidden inferences:

- Finite-height verification implies RH.
- A Levinson proportion, even 67.2 percent or 100 percent density, implies RH.
- Zero-density estimates imply Iso_H.
- Residual 539, or N-star = 14, locates a zero.
- The debt-argument has proved RH.

---

## 7. Verdict

The nontrivial zeros of zeta live in the critical strip, are counted by N(T), and are known to lie on the critical line in three incomplete senses: infinitely many (Hardy), a positive and improving proportion (Selberg through PRZZ, with an announced 2026 raise not locked here), and all zeros up to height 3 · 10^{12} (Platt–Trudgian). Classical zero-free regions keep them away from Re(s) = 1. Classical density bounds still leave a positive power of T at moderate sigma.

The Riemann Hypothesis asserts that every nontrivial zero has real part 1/2. That assertion is not implied by any of the facts above. In this programme it remains an open debt-argument on five classical obligations. Residual-flux provenance is mandatory and does not enter the zeta ledger.

*Per aspera ad astra.*
