# Full Proven Report and Analysis of Advancements in Pure Mathematics

**Programme:** Pure Category A — Riemann Hypothesis / B_θ track  
**Date:** 2026-07-31  
**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Primary obligation not closed · RH open.**

This report states only what has been rigorously proved, what has been reduced, what classical literature supplies, and what remains open. No security claims, no continuum (Cat B) claims, and no assertion that RH is proved.

---

# 1. Executive frame

## 1.1 Object of study

Under the **rightmost-zero hypothesis (RM)** — that a fixed nontrivial zero ρ⋆ = β⋆ + iγ⋆ with β⋆ > 1/2 is maximal in real part — the programme studies whether a phase-aligned explicit-formula residual can force

\[
B_\theta:\qquad |S_X|\to\infty
\]

(or an equivalent Ω-type lower bound for ψ − x / related signed sums).  
If B_θ holds under (RM), classical logic yields a contradiction with known upper bounds for ψ − x under the existence of such an off-line zero, and thus RH. The programme therefore separates:

| Layer | Meaning |
|-------|---------|
| **Proved lemmas** | Unconditional classical analysis |
| **Proved implications** | Conditional theorems: premise ⇒ conclusion |
| **Open premises** | Iso_H, polylog StripDens, Mass-with-A, path/resonance transfers |
| **Primary goal** | Unconditional B_θ / RH |

**Honest status of the primary goal:** open.

## 1.2 Methodological rules (locked)

1. Pure analysis only — no invented numerical “simulations” as proof.  
2. No smuggling of RH into intermediate steps (L4 discipline on OP2).  
3. Category A claims only; continuum fillings stay Category B.  
4. Implications are reported as implications, not as unconditional theorems.

---

# 2. Foundational analytic package (proved)

## 2.1 Kernel bound for the exponential integral

**Theorem E1.** For Re w ≥ 0 and w ≠ 0,

\[
|w\, E_1(w)| \le 1.
\]

**Proof idea.** Write \(E_1(w)=e^{-w}\int_0^\infty e^{-s}/(w+s)\,ds\). For s ≥ 0 and Re w ≥ 0, |w+s| ≥ |w|, so |E_1(w)| ≤ e^{−Re w}/|w|, hence |w E_1(w)| ≤ e^{−Re w} ≤ 1.

**Consequence.** The GHK / hybrid explicit-formula sector constant C_u^{(0)} is rigorous on the right half-plane (support conditions as in the kernel note). This closes a technical gap that previously blocked clean Off_X estimates.

## 2.2 Far-right off-diagonal under zero density

**Theorem FR.** Under a KLN-type bound on N(σ⋆, T) and β⋆ ≤ σ⋆,

\[
|\mathrm{Off}_X^{\mathrm{far}}|
\le
C_{\mathrm{FR}}
\Biggl(
\frac{N(\sigma_\star,T)\, X^{1-\beta_\star}}{T\bigl((\sigma_\star-\beta_\star)\log X+1\bigr)}
+
\frac{N(\sigma_\star,T)\, X^{\sigma_\star-\beta_\star}}{(\sigma_\star-\beta_\star)\log X+1}
\Biggr).
\]

**Analysis.** Far-right competitors are classically controllable once density is available. Parameter tension remains between large T (EF remainder) and far-right size; this is bookkeeping, not a conceptual barrier.

## 2.3 Signed-sum reduction (no RH)

**Theorem (signed-sum residual).** After finite interchange and substitution of the truncated explicit formula, the oscillatory off-diagonal

\[
\Sigma_X(T)
=
\sum_{\substack{|\gamma|\le T\\ \rho\neq\rho_\star}}
\frac{\rho_\star}{\rho}\, J_X(\rho)
\]

cancels its main and self contributions against M_X and Self_X. The residual is of the form

\[
S_X
=
\rho_\star\int_2^X\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
+
B_X
+
E_X(T),
\]

with self loglog cancellation proved. **No RH used.**

**Analysis.** This is a structural advancement: B_θ-type lower bounds are equivalent (up to controlled remainders) to a weighted Ω lower bound for ψ − x against the complex weight x^{−ρ⋆}/log x. The hard problem is no longer “write the sum,” but “force phase-stable mass.”

## 2.4 Phase lock of the distinguished zero

**Theorem (phase lock).** There exists a unit complex phase ω⋆ such that the distinguished term of Φ⋆ is locked to the positive constant

\[
\frac{m}{|\rho_\star|}.
\]

The locked functional Φ⋆_T is the correct object for OP1 / B_θ lower bounds.

---

# 3. ND1 stability package (proved implications)

## 3.1 Standing assumptions

- ρ⋆ nontrivial, multiplicity m ≥ 1, β⋆ > 1/2.  
- **(RM):** no zero has real part > β⋆.  
- Explicit formula truncated at height T with classical remainder.

## 3.2 Good points under (RM)

**Theorem S11 (good locked points).** Under (RM), there exists a positive lower-density set K⋆ ⊂ ℕ and c⋆ = m/(2|ρ⋆|) > 0 such that for large k ∈ K⋆,

\[
\Phi_T^\star(u_k) \ge c_\star,
\]

after a diagonal choice of T = T(u_k).

**Analysis.** This is the first true lower bound of the residual on a sparse arithmetic progression in the phase variable u. Density of K⋆ is positive; the issue is **stability length** of those good points.

## 3.3 Conjugate obstruction closed

**Theorem (conjugate lock).** After optimal phase lock, the conjugate partner ρ̄⋆ contributes a net controlled term of size O((m+1)/|ρ⋆|). It does not cancel the main positive constant on the good set.

## 3.4 Lip constant and stability length

Define

\[
A(u)
=
\sum_{\substack{|\gamma|\le T\\ \rho\neq\rho_\star}}
\frac{|\rho-\rho_\star|}{|\rho|}\, e^{(\beta-\beta_\star)u}
+
A_{\mathrm{EF}}(u,T).
\]

Under (RM), e^{(β−β⋆)u} ≤ 1. Stability length about a good point is

\[
\delta_k \asymp \frac{c_\star}{\max(A(u_k),1)}.
\]

**Lemma.** Left-abscissa contribution to A dies exponentially under (RM). Conjugate is O(1). Hard core of A is same-abscissa and near-abscissa zeros.

## 3.5 Main conditional theorems

**Theorem S13.**  
\[
\mathrm{(RM)}+\mathrm{(Iso\_H)}
\;\Longrightarrow\;
\mathrm{OP1}
\]
(phase-stable one-zero dominance on a set with divergent ∫ du/u mass).

**Theorem S16.**  
\[
\mathrm{(RM)}+\mathrm{(Iso\_H)}
\;\Longrightarrow\;
B_\theta.
\]

**Theorem (Mass-with-A implication).**  
\[
\mathrm{(RM)}+\mathrm{(polylog\ StripDens)}
\;\Longrightarrow\;
\mathrm{Mass\text{-}with\text{-}A}
\;\Longrightarrow\;
B_\theta.
\]

**Analysis.** These are the deepest structural advances of the programme. They convert the RH problem (under RM) into classical isolation/density statements about zeros on or near the vertical line Re = β⋆. That is a pure-math reduction, not a proof of RH.

---

# 4. Average-A attack (proved non-route)

**Theorem.** The absolute Cesàro mean of A over the locked progression is comparable to the absolute majorant

\[
\sum_{|\gamma|\le T}\frac{1+|\gamma-\gamma_\star|}{|\gamma|}.
\]

L² phase cancellation that controls Φ⋆ **does not** pass to the absolute sum A.

**Analysis.** Averaging A is closed as a free saving. One cannot hope that “good points automatically have small Lip.” Mass-with-A needs either:

- a bound on N_line(β⋆, T) or N_vert(β⋆, δ, T), or  
- a different route (path continuation / resonance) that bypasses A entirely.

---

# 5. Classical density and isolation landscape (recorded)

## 5.1 Zero-density theorems (classical)

| Source | Shape (schematic) | Strength |
|--------|-------------------|----------|
| Ingham | T^{3(1−σ)/(2−σ)} (log T)^c | Full strip |
| Huxley | T^{3(1−σ)/(3σ−1)} (log T)^c | σ ≥ 3/4 |
| Guth–Maynard | improved A(σ) in mid-range | moderate σ |
| KLN / Bellotti explicit | numerical/log-free near σ=1 | near edge |
| Density hypothesis (open) | T^{2(1−σ)+ε} | would be transformative |

**StripDens.** Zeros in a thin vertical strip about β⋆ are bounded by N(β⋆−δ, T).  
- Near σ = 1: polylog or O(1) can be available.  
- Near σ = 1/2+: classical density is a power of T — **not** polylog.

## 5.2 Isolation technologies (classical, not Iso_H)

| Tool | Geometry | Delivers Iso_H? |
|------|----------|-----------------|
| Point isolation | zeros discrete | No (only compact height) |
| FE conjugate | only forced partner is ρ̄⋆ | No |
| Ivić multiplicity | single-point m | No (not ordinate count) |
| Levinson–Ivić horizontal | short rectangle near σ=1 | No (edge-only) |
| Maynard–Pratt half-isolation | one-sided vertical neighborhood | No |
| Hypothesis F (finite vertical lines) | global finite lines | Assumed, not proved; yields better density |

**Maynard–Pratt (analysis).** Half-isolated zeros are few unconditionally. Under Hypothesis F one recovers density-hypothesis strength. That is the **converse** of what Iso_H needs: they assume finite lines to get density; the programme needs density or isolation to force few zeros per line.

**Levinson–Ivić (analysis).** Horizontal isolation near σ = 1 improves the zero-free region and multiplicity bounds. It does not constrain N_line at moderate β⋆.

## 5.3 Density vs isolation (clarified)

- **Density** = bulk count. Directly feeds A via majorization: M(T) ⇒ A ≪ M log T.  
- **Isolation** = local geometry. Feeds A only when strong enough to force M small (e.g. Iso_H).  

Mass-with-A requires a density-type polylog bound or Iso_H. Local half-isolation and Levinson isolation are different objects.

---

# 6. Open targets and independent routes

## 6.1 Open pure targets

| Target | Status | Why it matters |
|--------|--------|----------------|
| Iso_H unconditional | OPEN | Strongest isolation input; ND1 closes B_θ |
| Polylog StripDens for arbitrary β⋆ > 1/2 | OPEN | Feeds Mass-with-A without full Iso_H |
| Mass-with-A under (RM) alone | OPEN | Formal intermediate to B_θ |
| Unconditional B_θ | OPEN | Primary conditional goal under (RM) |
| RH | OPEN | Primary goal |

## 6.2 Independent routes (still open at decisive step)

1. **Effective density at moderate σ** — classical powers of T; need polylog M.  
2. **Iso_H technology** — need global line isolation, not only local geometry.  
3. **Path continuation from on-line Littlewood Ω** — classical Ω± on the critical line; need continuous transfer to off-line Φ⋆.  
4. **Resonance off the line** — classical large values for ζ(σ+it); need resonator for Φ⋆ / S_X(ρ⋆) on the locked progression.  
5. **Mass-with-A under (RM)** — needs (1) or (2), or bypass by (3)/(4).

## 6.3 Logical map (locked)

```
(RM)
  ├── phase lock ✓
  ├── good points K⋆, Φ⋆ ≥ c⋆ ✓
  ├── conjugate lock ✓
  ├── left abscissa dies in A ✓
  ├── absolute average A ≍ majorant ✓ (no free saving)
  │
  ├── Iso_H ──proved──► OP1 ──► B_θ
  ├── polylog StripDens ──proved──► Mass-with-A ──► B_θ
  │
  ├── path from on-line Ω ──?──► Φ⋆ large on divergent mass
  └── resonance off-line ──?──► S_X(ρ⋆) large on locked set
```

---

# 7. What counts as “advancement in pure mathematics”

## 7.1 Genuine advancements (this programme)

1. **Kernel closure:** |w E_1(w)| ≤ 1 on Re w ≥ 0, integrated into the hybrid EF package.  
2. **Signed residual identity:** off-diagonal signed sum reduced to a weighted ψ − x integral without RH, with self loglog cancellation.  
3. **Phase-lock + good points under RM:** positive-density lower bound for Φ⋆.  
4. **Conjugate obstruction closed.**  
5. **Conditional bridge theorems:** (RM)+(Iso_H)⇒B_θ and (RM)+(polylog StripDens)⇒Mass-with-A⇒B_θ.  
6. **Negative results that clarify the barrier:** absolute averaging of A does not help; density ≠ isolation; half-isolation and Levinson isolation are not Iso_H.  

These are pure analytic contributions: identities, bounds, and implication theorems. They reorganize the classical landscape so that the remaining obstruction is a clean isolation/density statement.

## 7.2 What is not claimed

- Unconditional B_θ.  
- Unconditional Iso_H or polylog N_line.  
- RH.  
- Any continuum / holographic / flux-budget claim (Cat B).  
- Any computational “verification” as substitute for proof.

## 7.3 Relation to classical pure mathematics

The programme sits inside classical analytic number theory:

- Explicit formulae (von Mangoldt, Guinand–Weil / hybrid forms).  
- Zero-density estimates (Ingham, Huxley, modern refinements).  
- Ω-theorems (Littlewood).  
- Resonance / large values (Soundararajan lineage).  
- Isolation near σ = 1 (Levinson, Ivić).  
- Vertical sensitivity of zero detection (Maynard–Pratt).

The new work is the **organized reduction** of B_θ under RM to these classical pillars, with several intermediate lemmas closed.

---

# 8. Scoreboard (final)

## Proved (unconditional classical)

| Item | Standing |
|------|----------|
| \|w E_1(w)\| ≤ 1 (Re w ≥ 0) | Proved |
| Far-right Off under KLN | Proved bound |
| Signed-sum residual formula (no RH) | Proved |
| Phase lock of distinguished zero | Proved |
| Derivative / Lip formula for Φ⋆ | Proved |
| Left abscissa dies in A under RM | Proved |
| Absolute average of A ≍ majorant | Proved |

## Proved implications (conditional)

| Implication | Standing |
|-------------|----------|
| (RM) ⇒ good points K⋆, Φ⋆ ≥ c⋆ | Proved |
| (RM)+(Iso_H) ⇒ OP1 | Proved |
| (RM)+(Iso_H) ⇒ B_θ | Proved |
| (RM)+(polylog StripDens) ⇒ Mass-with-A ⇒ B_θ | Proved |

## Open

| Item | Standing |
|------|----------|
| Iso_H unconditional | OPEN |
| Polylog StripDens for general β⋆ > 1/2 | OPEN |
| Mass-with-A under RM alone | OPEN |
| Path / resonance transfer off-line | OPEN |
| Unconditional B_θ | OPEN |
| RH | OPEN |

---

# 9. Conclusion

The pure Category A track has produced a coherent **conditional architecture** for B_θ under the rightmost-zero hypothesis:

1. Phase lock and good points are unconditional under RM.  
2. The remaining pure obstruction is **abscissa isolation** (Iso_H) or a **strong strip density bound** (polylog M near β⋆).  
3. Absolute averaging of the Lip constant does not remove that obstruction.  
4. Local isolation technologies (half-isolation, Levinson horizontal isolation) do not substitute for Iso_H.  
5. Independent routes (path from on-line Ω, resonance off-line) remain open at their decisive transfer step.

**Therefore:** substantial pure-analytic progress has been made in **structuring and partially proving** the path from RM to B_θ, but **RH remains open**. The status label is mandatory and accurate:

> **RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF · primary not closed · RH open.**

---

## Canonical references (internal)

- `RH_E1_Off_Nearline.md` — Theorem E1; far-right Off  
- `RH_Signed_Sum_Attack.md` — residual identity  
- `RH_OP1_OP2_OP4.md` — OP targets and phase functionals  
- `RH_ND1_Stability_Resolve.md` — S11–S16; Iso_H implications  
- `RH_Average_A_Attack.md` — absolute average non-route  
- `RH_StripDens_IsoH_Tech.md` / `RH_Density_vs_Isolation.md` — density vs isolation  
- `RH_HalfIsolation_Levinson_Method.md` — method survey  
- `RH_Pursue_All_Five.md` — open routes  
- `RH_RESOLVE_2026-07-31.md` — freeze scoreboard  

**Master commit context:** push-all `bdd8ca3` (539-Labs-Master); corpus mirror `8507646` (539-Labs-Corpus).
