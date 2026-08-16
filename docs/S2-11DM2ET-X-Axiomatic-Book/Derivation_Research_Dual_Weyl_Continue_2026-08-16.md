# Derivation Research Continuation: Dual Weyl Law and Density of States

**Date:** 2026-08-16
**Scope:** Continue derivation research on Step 5 (asymptotic of ρ_int / dual Weyl law) and related operator/kernel steps.
**Status:** Research continuation. No dual Weyl law derived. RH remains open.
**Rule:** Residual discrete packaging does not enter zero-location asymptotics. Residual-flux provenance mandatory on residual objects.

---

## 1. Position after prior digs

- Candidate ρ_int built from dual amplitudes, TMR factors, and a single Higgs-echo Gaussian saturates: ∫_0^T ρ_int → constant.
- Classical N(T) ~ (T/2π) log(T/2π) − T/2π.
- Dual-brane constants (N_flux, G_4, equipartition factor 2, S, echo parameters) are T-independent and cannot supply log T by themselves.
- No dual Weyl law is recorded in the continuum notes.
- M5 / NS5 / D4 flux lattices, D2 interfaces, and Phase Law supply discrete continuum charges and a fixed clock, not a logarithmic density of states.

---

## 2. Three concrete derivation levers (continued research)

### Lever A — Dual archimedean factor

Classical source of the log term is Stirling’s expansion of the Gamma factors in the completed xi function:

arg Γ(1/4 + iT/2) ~ (T/2) log(T/2) − T/2 + …

A dual analogue would require continuum factors Γ_± on each sector such that

(1/π) [arg Γ_−(1/4 + iT/2) + arg Γ_+(1/4 + iT/2)]

reproduces (T/2π) log(T/2π) − T/2π on the interface.

**What the Model supplies:** Phase Law φ(t) = exp(2π i t / G_4 + δφ_11D) and dual sectors ±U.

**What is missing:** An explicit dual Gamma (or dual completed xi) built from dual-brane geometry whose argument change on Re(s)=1/2 yields the classical main term. G_4 alone sets a period; it does not produce Stirling growth.

**Next research action:** Define a candidate dual archimedean factor from the dual continuum metric / warp data (if any) and compute its argument asymptotic. No such factor is recorded.

### Lever B — Energy-dependent dual phase-space volume

Standard Weyl: N(λ) ~ (2π)^{-d} Vol({(x,ξ) : symbol(x,ξ) ≤ λ}).

To obtain T log T growth one needs the phase-space measure of the dual symbol to grow like T log T (or an effective dimension that runs with energy).

**What the Model supplies:** Continuum flux quanta (Φ_NS5, Φ_D4, Φ_C3, Φ_C5) ∈ ℤ^4; D2 world-volume; M5 self-dual H_3 with 10 independent continuum degrees of freedom after self-duality.

**What is missing:** A symbol for H_± (or Φ_±) whose sublevel sets have measure ~ T log T, derived from dual-brane data rather than postulated. Fixed integer flux lattices do not enlarge with ordinate height T.

**Next research action:** Propose a continuum symbol on the dual interface whose level sets involve a logarithmic factor from dual winding / Kaluza–Klein towers, then compute the phase-space volume. No such symbol is recorded.

### Lever C — Operator skeleton from TMR + interface geometry

Construct formal operators

H_± : Dom(H_±) ⊂ ℋ_± → ℋ_±

whose spectral measures are the candidate ρ_±, with interface restriction giving ρ_int.

**Minimal skeleton:**

1. ℋ_± = L²(interface, dual measure_±) or continuum mode space of the D2 world-volume restricted to each sector.
2. H_± = −i d/dt + V_± (phase operator) or a dual Schrödinger operator with potential fixed by TMR phase lock and phonon suppression.
3. Spectrum of H_± on the interface required to accumulate with density ρ_int.

**What the Model supplies:** TMR phase condition cos((k_1−k_2)d − θ); Phase Law period G_4; phonon factor e^{−S}; dual split.

**What is missing:** Explicit domain, potential V_±, and proof that the eigenvalue counting function grows like (T/2π) log(T/2π). The Phase Law is monochromatic at frequency 1/G_4; a single frequency does not generate a logarithmic spectrum of ordinates.

**Next research action:** Write a formal dual Schrödinger or Dirac operator on the interface with TMR-periodic coefficients and compute its spectral asymptotics. No such operator is recorded.

---

## 3. Coefficient targets for a dual Weyl law (if constructed)

If Levers A–C eventually produce counting functions N_±(T), the interface sum must satisfy

N_dual(T) = N_−(T) + N_+(T)

with leading coefficients

α_− + α_+ = 1,    β_− + β_+ = −1/(2π)

in the expansion

N_dual(T) = (α_−+α_+)(T/2π) log(T/2π) + (β_−+β_+) T + E_dual(T).

Dual equipartition suggests the natural split α_− = α_+ = 1/2 at leading order. That split is a Model preference, not a derived theorem. Error E_dual would have to be controlled by dual-brane data alone.

---

## 4. What continuum flux and self-duality do not yet do

M5 self-duality reduces the continuum 3-form to 10 independent degrees of freedom and quantises periods on 3-cycles. Continuum K-theory classifies D-brane charges. These structures:

- fix discrete labels of mode families;
- constrain which fluxes can be turned on independently;
- do not compute a spectral density of eigenvalues growing like log T;
- do not identify that density with the zeros of zeta.

They remain available as geometric input for a future dual symbol or dual archimedean factor; they are not a dual Weyl law.

---

## 5. Ordered next research sequence

1. Formalise a candidate dual archimedean factor from dual continuum geometry and extract its argument asymptotic (Lever A).
2. If that fails to produce log T, define a dual symbol on the interface whose phase-space volume grows with T (Lever B).
3. In parallel, write the weakest operator skeleton H_± consistent with TMR phase lock and dual split, and state the spectral problem whose asymptotics would be the dual Weyl law (Lever C).
4. Only after a dual counting function N_dual(T) exists, attempt coefficient matching and error control.
5. Identification of N_dual with N_zeta remains Step 4 and is independent.

---

## 6. Status after this continuation

| Item | Status |
|------|--------|
| Dual Weyl law | Not derived |
| Dual archimedean factor | Not constructed |
| Energy-dependent dual phase space | Not constructed |
| Operator H_± with log-density spectrum | Not constructed |
| Coefficient match to (T/2π) log(T/2π) | Blocked until N_dual exists |
| RH | Open |

Derivation research continues. No claim of closure.

**Status code:** `DERIVATION_RESEARCH_DUAL_WEYL_CONTINUE_2026-08-16`
