# Directional Corpus Resolve — All Five Open Directions

**Date:** 2026-07-31  
**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Does not prove Iso_H, Hypothesis F, unconditional Mass-with-A, B_θ, or RH.**

**Mandate.** Resolve every solid direction as far as the classical directional corpus allows. Record proved implications, closed non-routes, and remaining open cores. No invention.

**Freeze inputs.** Density vs isolation locked; solid directions frozen; ND1 acceptance locked.

---

# 0. Directional corpus (canonical pillars)

| Pillar | Role in this resolve |
|--------|----------------------|
| Explicit formula (von Mangoldt / hybrid GHK) | Master identity for Φ⋆, S_X, signed residual |
| Zero density (Ingham, Huxley, Guth–Maynard, KLN, Bellotti) | StripDens majorants for A |
| Multiplicity / isolation near σ=1 (Ivić, Levinson) | Local m; not Iso_H |
| Half-isolation + Hypothesis F (Maynard–Pratt) | Density under finite lines; not Iso_H |
| Littlewood Ω± | On-line path source for direction 3 |
| Resonance (Soundararajan, Aistleitner, Bondarenko–Seip, …) | Large values off-line for direction 4 |
| FE + conjugate symmetry | Only forced same-abscissa partner is ρ̄⋆ |
| Classical zero-free regions | Edge isolation ≠ Iso_H |

---

# D1 — Effective density at moderate σ

## Corpus strength (classical)

Write N(σ,T) ≪ T^{A(σ)(1−σ)} (log T)^c.

| σ range | Classical shape | Polylog M? |
|---------|-----------------|------------|
| Near 1 (σ ≥ 0.98) | Explicit / log-power bounds (KLN, Bellotti) | Sometimes yes |
| σ ≥ 5/6 | Huxley-type density-hypothesis range in parts | No in general |
| 0.7–0.8 | Guth–Maynard improves A(σ) in mid-range | No |
| 1/2–0.7 | Ingham A(σ) = 3/(2−σ) still competitive | No |
| Density hypothesis (open) | A(σ) = 2 | Would feed Mass-with-A for all β⋆ |

**Lemma D1.1 (strip majorant).** For δ > 0 fixed and T ≥ 2,

\[
N_{\mathrm{vert}}(\beta_\star,\delta,T)
:=
\#\{\rho:\ \beta\in[\beta_\star-\delta,\beta_\star],\ |\gamma|\le T\}
\le
N(\beta_\star-\delta,T).
\]

Under (RM), same-abscissa count N_line(β⋆,T) ≤ N_vert(β⋆,δ,T) for any δ.

**Lemma D1.2 (A from density).** Under (RM),

\[
A^{\mathrm{H}}_T
\ll
(\log T)\cdot N_{\mathrm{line}}(\beta_\star,T)
+
(\text{near-strip contribution}).
\]

Hence polylog N_line ⇒ polylog A on the hard core.

## What D1 resolves

| Item | Standing |
|------|----------|
| Power-of-T density at moderate σ | Classical (not enough for Mass-with-A) |
| Polylog density near σ=1 | Classical / explicit in ranges |
| Unconditional polylog M for arbitrary β⋆ ∈ (1/2,1) | **OPEN** |
| Density hypothesis | **OPEN** |

## Resolve statement (D1)

> **Resolved as far as corpus allows:** bulk density feeds A by majorization; classical exponents at moderate σ remain powers of T. **Not resolved:** polylog StripDens for a rightmost zero only moderately larger than 1/2.

**Feed to B_θ:** blocked at polylog M.

---

# D2 — (Iso_H) technology

## Definition (programme)

**Iso_H.** There exists C such that for all T ≥ 2,

\[
N_{\mathrm{line}}(\beta_\star,T)
:=
\#\{\gamma:\ \zeta(\beta_\star+i\gamma)=0,\ |\gamma|\le T\}
=
O\bigl((\log T)^C\bigr).
\]

(Or the stronger finite-line form: N_line(β⋆,T) = O(1) as T → ∞ after counting multiplicity at finitely many ordinates.)

## Corpus inventory vs Iso_H

| Corpus tool | What it gives | Iso_H? |
|-------------|---------------|--------|
| Zeros are discrete | Finite on compact height segments | No (T→∞ open) |
| FE | Only forced same-abscissa partner is conjugate | No |
| Ivić multiplicity | m(β+iγ) controlled by (1−β) and log log γ | No (single point) |
| Levinson isolation hypothesis | Horizontal rectangles near σ=1 → better zero-free region | No |
| Half-isolation | Few one-sided local zeros; short detecting polynomials | No |
| Hypothesis F | Finite vertical lines **assumed** → density ~ T^{2(1−σ)} | Converse of Iso_H |

**Lemma D2.1 (ND1 bridge — already proved).**  
(RM)+(Iso_H) ⇒ A = O(1) on K⋆ (after diagonal T) ⇒ Mass-with-A ⇒ OP1 ⇒ B_θ.

**Lemma D2.2 (corpus does not prove Iso_H).**  
No theorem in the directional corpus yields N_line(β⋆,T) = O((log T)^C) for fixed β⋆ > 1/2 as T → ∞.

**Lemma D2.3 (Hypothesis F is not a proof path for Iso_H).**  
Hypothesis F assumes finitely many vertical lines globally. Maynard–Pratt then improves density. That assumes the conclusion structure Iso_H needs; it does not prove it.

## What D2 resolves

| Item | Standing |
|------|----------|
| Local isolation tools catalogued | Done |
| (RM)+(Iso_H)⇒B_θ | Proved (ND1) |
| Unconditional Iso_H | **OPEN** |
| Hypothesis F | **OPEN** (and not equivalent to Iso_H alone) |

## Resolve statement (D2)

> **Resolved as far as corpus allows:** Iso_H is the cleanest isolation input; the implication to B_θ is proved; every classical isolation tool stops short of Iso_H. **Not resolved:** unconditional Iso_H.

**Feed to B_θ:** blocked at Iso_H premise.

---

# D3 — Path continuation from on-line Ω

## Corpus strength

**Littlewood (1914).** ψ(x) − x = Ω±(x^{1/2} log log log x) (and analogues for θ, π). Proof uses Diophantine approximation on ordinates of zeros on (or near) the critical line to force simultaneous phase alignment. Typically ineffective (no bound on first sign change).

## Path-continuation programme (pure)

Start from a large on-line Ω configuration of the explicit formula, then continuously deform phase / contour so a putative off-line rightmost zero ρ⋆ is forced to contribute a large main term on a positive-density subset of the locked progression u_k = u_0 + 2πk/|γ⋆|.

**Obstruction (corpus-level).**  
- On-line Ω uses many critical-line zeros with free Diophantine phases.  
- Off-line Φ⋆ is dominated by a single abscissa β⋆ > 1/2 with locked arithmetic progression.  
- Transfer requires control of the tail of other zeros and the EF remainder while keeping the lock.  
- No classical theorem states a continuous deformation that preserves a divergent-mass lower bound from the critical line to a fixed off-line abscissa.

**Lemma D3.1.** Littlewood Ω supplies arbitrarily large |ψ − x| / x^{1/2} (log factors). It does **not** by itself supply Φ⋆(u_k) ≥ c⋆ on a set with ∑ δ_k/u_k = ∞ under (RM) alone when β⋆ > 1/2.

**Lemma D3.2 (conditional path).** If one assumes a uniform lower bound for the on-line residual on a continuum of phases that includes the locked progression of ρ⋆, and if the off-line competitor tail is O(1), then OP1 follows. The second premise is essentially Iso_H / Mass-with-A again.

## What D3 resolves

| Item | Standing |
|------|----------|
| On-line Ω classical | Done (Littlewood) |
| Continuous transfer off-line without isolation | **OPEN** |
| Path that bypasses Iso_H entirely | **OPEN** (no corpus theorem) |

## Resolve statement (D3)

> **Resolved as far as corpus allows:** on-line Ω is a classical source of large oscillations; the transfer problem to off-line locked Φ⋆ is not solved by any classical theorem and reduces to tail/isolation control. **Not resolved:** path continuation that yields OP1 unconditionally under RM alone.

**Feed to B_θ:** blocked at off-line transfer.

---

# D4 — Resonance off the line

## Corpus strength

Resonance method (Soundararajan; Hilberdink; Aistleitner; Bondarenko–Seip; later strip large-value theorems): construct a Dirichlet polynomial R(t) maximizing

∫ |R(t)|² ζ(σ+it) w(t) dt  (or partial sums)

subject to coefficient constraints. Yields large |ζ(σ+it)| for 1/2 < σ < 1 and large values of short Dirichlet polynomials.

## Resonance for Φ⋆ / S_X(ρ⋆) (programme)

Need a resonator that forces |S_X(ρ⋆)| or Re Φ⋆ large on a positive-density subset of the locked progression associated with a fixed off-line zero ρ⋆.

**Obstruction (corpus-level).**  
- Classical resonators use integer frequencies (primes / integers).  
- Φ⋆ frequencies are ordinates of zeros (unknown).  
- The phase lock u_k = u_0 + 2πk/|γ⋆| is an arithmetic progression in the continuous variable u, not a free t-interval for Dirichlet polynomials in t.  
- Large values of ζ(β⋆ + it) do not automatically give large Φ⋆(u_k) at discrete locked u_k.

**Lemma D4.1.** Classical resonance proves large max_{t∈[T,2T]} |ζ(σ+it)| for fixed σ ∈ (1/2,1). It does not prove large Φ⋆ on the locked set K⋆ under (RM).

**Lemma D4.2 (conditional resonance hit).** If a resonator produces large values of the competitor sum at ordinates that meet the locked progression (Hit) and residual phase is controlled (Res), then OP2-type lower bounds follow (programme OP notes). Both (Res) and (Hit) remain open premises; L4 forbids smuggling RH.

## What D4 resolves

| Item | Standing |
|------|----------|
| Large values of ζ off the line | Classical (resonance) |
| Resonator for Φ⋆ / S_X(ρ⋆) on locked progression | **OPEN** |
| (Res)+(Hit)⇒OP2 | Proved as implication (programme); premises open |

## Resolve statement (D4)

> **Resolved as far as corpus allows:** resonance is a powerful large-value engine for ζ(σ+it); it does not by itself hit the locked zero-ordinate residual Φ⋆. **Not resolved:** resonance lower bound for S_X(ρ⋆) or Φ⋆ on K⋆.

**Feed to B_θ:** blocked at locked-progression resonator.

---

# D5 — Mass-with-A under (RM)

## Definition (programme)

**Mass-with-A.** There exists a positive-density (or positive lower density) subset of K⋆ such that

\[
\sum_{k\in K_\star'}
\frac{\delta_k}{u_k}
=
\infty,
\qquad
\delta_k
\asymp
\frac{c_\star}{\max(A(u_k),1)},
\]

so that integrating Φ⋆ ≥ c⋆/2 over stability intervals yields divergent ∫ du/u mass (OP1).

## Proved (this programme + corpus)

| Item | Standing |
|------|----------|
| Positive-density K⋆, Φ⋆ ≥ c⋆ under RM | Proved |
| Left abscissa dies in A | Proved |
| Conjugate O(1) after lock | Proved |
| Absolute Cesàro mean of A ≍ majorant | Proved (no free saving) |
| (RM)+(Iso_H) ⇒ A = O(1) ⇒ Mass-with-A | Proved |
| (RM)+(polylog StripDens) ⇒ polylog A ⇒ Mass-with-A | Proved |

## Corpus ceiling

To get Mass-with-A under (RM) **alone**, one needs either:

1. Polylog control of N_line or N_vert at β⋆ (D1 open at moderate σ), or  
2. Iso_H (D2 open), or  
3. A bypass that makes δ_k large without controlling A (D3/D4 open).

No classical theorem supplies (1) or (2) for arbitrary β⋆ > 1/2.

## What D5 resolves

| Item | Standing |
|------|----------|
| Mass-with-A as formal target | Locked |
| Implications from Iso_H / StripDens | Proved |
| Absolute averaging non-route | Proved |
| Mass-with-A under RM alone | **OPEN** |

## Resolve statement (D5)

> **Resolved as far as corpus allows:** Mass-with-A is the correct intermediate; its implications to B_θ are proved; absolute averaging is closed as a non-route. **Not resolved:** Mass-with-A from (RM) without isolation/density input.

**Feed to B_θ:** blocked at A-control (or bypass).

---

# Global resolve scoreboard

## Closed by this directional resolve

| Item | Standing |
|------|----------|
| Density vs isolation distinction | Locked |
| D1 corpus ceiling (power of T at moderate σ) | Recorded |
| D2 corpus ceiling (no tool = Iso_H) | Recorded |
| D3 corpus ceiling (Ω on-line only) | Recorded |
| D4 corpus ceiling (ζ large values ≠ Φ⋆ lock) | Recorded |
| D5 implications + absolute-A non-route | Locked |
| (RM)+(Iso_H)⇒B_θ | Proved |
| (RM)+(polylog StripDens)⇒Mass-with-A⇒B_θ | Proved |
| E1, signed residual, phase lock, good points | Proved (prior) |

## Still open (all five decisive cores)

| Direction | Decisive open core |
|-----------|-------------------|
| D1 | Polylog M at moderate β⋆ |
| D2 | Unconditional Iso_H |
| D3 | Off-line path transfer of Ω |
| D4 | Locked-progression resonator for Φ⋆ |
| D5 | Mass-with-A under RM alone |

## Barrier (unchanged, now fully documented)

```
phase lock ✓ · residual ✓ · conjugate lock ✓ · left dies ✓ · abs-avg A non-route ✓
        │
        ▼
(RM)+(Iso_H) ──proved──► B_θ
(RM)+(polylog StripDens) ──proved──► Mass-with-A ──► B_θ
        │
        ├── Iso_H unconditional ✗
        ├── polylog StripDens moderate β⋆ ✗
        ├── path transfer ✗
        └── locked resonance ✗
```

B_θ is blocked by abscissa isolation or strong strip density (or an off-line lower bound that bypasses A). The directional corpus does not close any of these premises.

---

# Non-claims (mandatory)

1. No proof of Iso_H.  
2. No proof of Hypothesis F.  
3. No unconditional Mass-with-A.  
4. No unconditional B_θ.  
5. No RH.  
6. No claim that classical density at moderate σ is polylog.  
7. No claim that resonance or Littlewood Ω transfers off-line without extra premises.

---

# One-liner

> All five open directions resolved against the directional corpus: implications and ceilings locked; every decisive core remains open; RH open.

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · primary not closed · RH open.
