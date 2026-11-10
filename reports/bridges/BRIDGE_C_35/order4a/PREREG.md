# PREREG: order4a. An explicit shadow candidate Ξ and the completed A1
Written 2026-10-24, before any order4a run.

## Candidate (fixed now)
Source principle: Zwegers-type completion of indefinite theta series of signature (1,1). The boundary weight sgn is replaced by its erf-completion. The difference is a sum, over wall directions u, of Eichler-type integrals of weight-3/2 unary thetas g_u(τ) = Σ_b (b + y)·e(Q(u)(b + y)²τ)·(character), taken along u. At a rational point x, as t→0+, such an Eichler integral contributes to the t^{−1/2} coefficient a term proportional to (√π/2)Q(u)^{−1/2} times the period-mean of the first Bernoulli weight against the character, N^{−1}Σ_{b mod N} B1(b/N)f(b).

These are exactly the sawtooth groups of order3 Map 1: W[1], W[7/2], W[595/2].

**Candidate:** Ξ_ε = Σ_Q ε_Q·W[Q], with ε ∈ {0,1}³. The primary candidate is ε = (1,1,1), i.e. Ξ = W and completed A1 = A1 − W = D + R. The other 6 non-trivial ε are secondary, and the multiplicity is disclosed.

## Test
Completed A1^c = A1 − Ξ_ε (105 companions × 216 points XS; data: order3/data/parts.npz, read-only).

**Closed at a single weight w** iff rank[A1^c(x) | diag(|x|^w)A1^c(−1/x)] = rank A1^c(x), for some single w ∈ {½, 1}. SVD threshold: 1e-9 relative.

## Sign control (gating)
- A0 at w=1: rank 36 and closed.
- Wrong sign: joint rank > 36.

If the control fails, the verdicts are void.

## Verdict rules
- **Primary:** "candidate confirmed (Category B)" if D+R is closed at w=½ or w=1; otherwise "candidate falsified".
- **Secondary:** list every ε that closes.

## Certification
The entries involve √π, Q^{−1/2} and the transcendental J (the drift), so exact mod-p rank arithmetic is not feasible. Verdicts are Category B. No t-fit is used here: A1 was validated at the cone-scaled grid in order3 Map 0, so no new grid is needed.

## Run order
Hash → scripts + SHA256SUMS → control → tests → RESULTS/NOTES/REPORT. No pushes.
