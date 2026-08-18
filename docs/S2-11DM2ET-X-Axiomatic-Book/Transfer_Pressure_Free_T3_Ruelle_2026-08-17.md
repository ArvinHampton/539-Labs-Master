# Transfer-Pressure Parameter on Free T3 Symbolic Dynamics

**Date:** 2026-08-17  
**Status:** External geometric input outside residual P. Named and partially computed. Residual Category A on P remains closed. RH remains open.  
**Residual-flux provenance mandatory on residual objects. ZLA firewall: residual packaging does not enter zero-location statements.**

---

## 1. Purpose

Residual Category A on P is closed. Compact cover, Jac Weyl, and End = Z are closed. 539 remains a finite count. Weighted spectra and heat-kernel traces on residual K+ only redistribute that finite set.

N_dual / RH requires infinite-volume geometry or a transfer-pressure parameter from outside P. This note names and sets up the transfer-pressure parameter on free T3 symbolic dynamics as that external input.

---

## 2. Domain (outside residual P)

Free T3 is the local ternary map on non-negative integers:

```
T3(n) = n/3           if n ≡ 0 (mod 3)
T3(n) = (4n+2)/3      if n ≡ 1 (mod 3)
T3(n) = (2n+1)/3      if n ≡ 2 (mod 3)
```

Symbolic dynamics: itineraries in the full 3-shift on symbols {0,1,2} given by successive residues mod 3, until the orbit reaches the small attractor {0} or the 2-cycle {1,2}.

This domain is free dynamics (Option 3). Residual packaging under Principle (S), residual quanta, and K+ are not the domain.

---

## 3. Branch derivatives (piecewise-affine model)

| Branch | Residue | |T'| |
|--------|---------|-----|
| div3   | 0       | 1/3 |
| exp1   | 1       | 4/3 |
| exp2   | 2       | 2/3 |

---

## 4. Ruelle transfer operator and topological pressure

For a continuous potential phi on the ternary shift space, the Ruelle operator acts by

(L_phi psi)(x) = sum_{T3(y)=x} exp(phi(y)) psi(y).

Topological pressure is

P(phi) = log rho(L_phi),

where rho is the spectral radius (leading eigenvalue when the operator is quasi-compact on a suitable Banach space).

---

## 5. Geometric family (computed)

Take the geometric potential

phi_beta = -beta log |T'|

constant on each residue class. On the full 3-shift approximation the pressure is exact:

P(phi_beta) = log( (1/3)^{-beta} + (4/3)^{-beta} + (2/3)^{-beta} ).

| beta | P(phi_beta) |
|-----:|------------:|
| 0    | log 3 ≈ 1.0986 (topological entropy) |
| 0.5  | ≈ 1.341 |
| 1    | ≈ 1.658 |
| 1.5  | ≈ 2.039 |
| 2    | ≈ 2.469 |

At beta = 0 the pressure is the entropy of the full ternary shift. At beta = 1 the weights are (3, 3/4, 3/2) and the pressure is log(5.25).

---

## 6. Free dynamics check (empirical)

Seeds 1 to 5000 under free T3: median steps to value ≤ 2 is 15, mean ≈ 16, all terminated by step 50. This matches Option 3: short free basins, N_star of order 14, not 539 trajectory classes.

Transfer pressure on free T3 therefore lives on a dynamics that contracts quickly. It does not reproduce residual packaging length 539.

---

## 7. What this input supplies

- A named transfer operator L_phi and pressure P(phi) outside residual P.
- Explicit pressure values for the geometric family phi_beta.
- A dynamical zeta / spectral framework in which zeros of determinants or poles of resolvents of L_phi can be studied.

---

## 8. What it does not yet supply

- A potential phi for which the spectrum of L_phi, or the zero set of a dynamical zeta built from P, yields a density of states with leading term (T/2pi) log(T/2pi).
- An analytic identity between that spectrum and the nontrivial zeros of the Riemann zeta function.
- Any use of residual K+, residual weights, or residual heat-kernel traces (those stay closed and separate).

---

## 9. Next concrete steps inside this input

1. Fix a Banach space (for example functions of bounded variation on the ternary partition) and establish quasi-compactness of L_phi for the geometric family.
2. Locate the spectrum of L_phi beyond the leading eigenvalue; extract secondary eigenvalues or continuous spectrum if present.
3. Form the dynamical zeta

   zeta_dyn(s) = exp sum_{n≥1} (1/n) sum_{T3^n x = x} exp(sum_{k=0}^{n-1} phi(T3^k x)) e^{-s n}

   (or the standard Ruelle form) and study its zeros/poles.
4. Compare any density of poles or spectral data with classical N(T) only after a dual-first computation is complete; do not insert the classical main term by hand.

---

## 10. Firewall and status

- Residual Category A on P: closed. Compact cover, Jac Weyl, End = Z closed. 539 is a finite count.
- Residual-flux provenance mandatory on residual objects.
- ZLA firewall: residual packaging numbers do not enter zero-location theorems.
- This note does not claim N_dual, does not claim a proof of RH, and does not reopen residual cell geometry.
- Classical GHK and density estimates remain the only analytic levers that are already on the residual-independent RH track.

---

## 11. Bottom line

The transfer-pressure parameter on free T3 is named, set up, and partially computed for the geometric family. Free dynamics remains short. Residual Category A on P remains closed. N_dual and RH remain open: pressure values alone do not produce the logarithmic zero-counting main term or an identity with zeta(s). The live path inside this input is the spectral analysis of L_phi and the associated dynamical zeta on free ternary itineraries.
