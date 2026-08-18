# Transfer-Pressure Parameter on Free T3 Symbolic Dynamics

**Date:** 2026-08-17  
**Status:** External geometric / analytic input outside residual P. Residual Category A closed. RH open.  
**Residual-flux provenance mandatory on any residual reference. ZLA firewall intact.**

---

## 1. Purpose

Residual Category A on the residual complex P (K^{+}, packaging under Principle (S), fiber blocks, permanent class, A4⁺/A5⁺) is closed. 539 is a finite count. Weighted residual spectra and heat-kernel traces only redistribute that finite set.

N_dual / RH requires either infinite-volume geometry or a transfer-pressure parameter from outside residual P. This note names and sets up the transfer-pressure parameter on free T3 symbolic dynamics.

No claim is made that the construction produces N_dual or proves the Riemann Hypothesis.

---

## 2. Domain (outside residual P)

Free T3 is the local ternary map on non-negative integers:

- if n ≡ 0 (mod 3) → T3(n) = n/3
- if n ≡ 1 (mod 3) → T3(n) = (4n + 2)/3
- if n ≡ 2 (mod 3) → T3(n) = (2n + 1)/3

Symbolic dynamics: itineraries in the full 3-shift on symbols {0, 1, 2} given by successive residues mod 3 until the orbit reaches the small attractor {0, 1, 2}. This domain is free dynamics under Option 3. Residual packaging under Principle (S), residual quanta, and K⁺ are not the domain.

Branch derivatives (piecewise-affine model):

| Branch | Residue | |T′| |
|--------|---------|-----|
| div3   | 0       | 1/3 |
| exp1   | 1       | 4/3 |
| exp2   | 2       | 2/3 |

---

## 3. Ruelle transfer operator and topological pressure

For a continuous potential φ on the ternary shift space, the Ruelle operator acts by

(L_φ ψ)(x) = ∑_{T3(y)=x} e^{φ(y)} ψ(y).

Topological pressure is

P(φ) = log ρ(L_φ),

where ρ is the spectral radius (leading eigenvalue when the operator is quasi-compact on a suitable Banach space).

---

## 4. Geometric family (computed)

Take the geometric potential φ_β = −β log|T′| on the three branches (constant on each residue class). On the full 3-shift approximation the pressure is exact:

P(φ_β) = log( (1/3)^{−β} + (4/3)^{−β} + (2/3)^{−β} ).

| β   | P(φ_β)          |
|----:|----------------:|
| 0   | log 3 ≈ 1.0986  |
| 0.5 | ≈ 1.341         |
| 1   | ≈ 1.658         |
| 1.5 | ≈ 2.039         |
| 2   | ≈ 2.469         |

At β = 0 the pressure recovers the topological entropy of the full ternary shift. At β = 1 the weights are (3, 3/4, 3/2) and the pressure is log(5.25).

---

## 5. Free dynamics check (empirical)

Seeds 1…5000 under free T3: median steps to ≤ 2 is 15, mean ≈ 16, all terminated by step 50. This matches Option 3 locked facts: short free basins, N_star of order 14, not 539 trajectory classes.

Transfer pressure on free T3 therefore lives on a dynamics that contracts quickly. It does not reproduce residual packaging length 539.

---

## 6. What this input supplies

- A named transfer operator L_φ and pressure P(φ) outside residual P.
- Explicit pressure values for the geometric family φ_β.
- A dynamical zeta / spectral framework in which zeros of determinants or poles of resolvents of L_φ can be studied.

## 7. What this input does not supply

- A potential φ for which the spectrum of L_φ, or the zero set of a dynamical zeta built from P, yields a density of states with leading term (T/2π) log(T/2π).
- An analytic identity between that spectrum and the nontrivial zeros of the Riemann zeta function.
- Any use of residual K⁺, residual weights, or residual heat-kernel traces (those stay closed and separate).

---

## 8. Next concrete steps inside this input

1. Fix a Banach space (for example functions of bounded variation on the ternary partition) and establish quasi-compactness of L_φ for the geometric family.
2. Locate the spectrum of L_φ beyond the leading eigenvalue; extract secondary eigenvalues or continuous spectrum if present.
3. Form the dynamical zeta

   ζ_dyn(s) = exp ∑_{n≥1} (1/n) ∑_{T3^n x = x} exp(∑_{k=0}^{n−1} φ(T3^k x)) e^{−s n}

   (or the standard Ruelle form) and study its zeros/poles.
4. Compare any density of poles or spectral data with classical N(T) only after a dual-first computation is complete; do not insert the classical main term by hand.

---

## 9. Status freeze

- Residual Category A on residual P: closed. 539 remains a finite count.
- Compact cover, Jac Weyl, End = ℤ: closed.
- Transfer-pressure parameter on free T3: named, set up, geometric family computed.
- Free dynamics: short (Option 3).
- N_dual: not obtained.
- Analytic identity with zeros of zeta: not obtained.
- Riemann Hypothesis: open.
- ZLA firewall: residual packaging numbers do not enter a zero-location theorem.
- Residual-flux provenance: mandatory on any residual reference.

No residual-P prompt is useful for further residual combinatorics. Live path is spectral analysis of L_φ and the associated dynamical zeta on free ternary itineraries.

---

End of note.
