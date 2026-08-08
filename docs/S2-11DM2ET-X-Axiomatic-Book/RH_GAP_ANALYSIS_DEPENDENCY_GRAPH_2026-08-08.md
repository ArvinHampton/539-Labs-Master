# Gap Analysis of the RH Dependency Graph (2026-08-08)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure A · ZLA  
**Input graph:** Pass 2 (`rh_explore_all_resolutions_pass2_results.json`) · H1–H5 conditionals  
**Does not prove:** RH · O-TL · B_θ · any named conditional  
**Does:** locate the precise cuts where proved structure ends and open hypotheses begin

---

## 0. What a “gap” means here

In the dependency graph \(G=(V,E)\):

- A node is **proved** if its standing is a classical theorem or a programme-proved reduction.
- A node is **conditional** if it is a named hypothesis (PAO, κ, DH, Iso_H, GO, SOC, O-Moll).
- An edge \(u\to v\) of kind `proved_if_hyp` means: **if** \(u\) holds, **then** \(v\) is a theorem.
- A **gap** is a minimal set of open nodes whose simultaneous failure blocks every path from the proved subgraph to a goal (`B_θ`, `O-TL`, `RH`).

The graph has **three nested goals** with different cuts:

| Goal | Nature | Min-cut type |
|------|--------|--------------|
| `B_θ` | Off-line residual lower bound | **OR-cut** of three 1–2 node gates |
| `O-TL` | Target lemma / phase programme | **AND-cut** of four obligation arms |
| `RH` | Full zero-location | Superordinate; **not** implied by `B_θ` alone |

---

## 1. Proved subgraph (no gap inside)

The following sit entirely on the **closed** side of every cut:

```text
Imp_signed_residual_formula
Imp_self_loglog_cancel
Imp_E1_CU1
Imp_typical_Omega_online
Imp_OPC_hybrid_identity
Imp_R41_GHK_strip
Imp_RM_IsoH_Btheta          (implication only — hyp open)
Imp_RM_polylog_MassA       (implication only — hyp open)
Imp_RM_MassA_Btheta        (implication only — hyp open)
Imp_monodromy_withdrawn    (dead non-route)
```

**Structural remark.** The signed residual formula is a **bridge**, not a gap:

```text
S_X  =  ρ⋆ ∫(ψ−x) x^{−ρ⋆−1}(log x)^{−1} dx  + B_X + E_X
```

is **proved**. The gap is not the identity; it is a **lower bound** on the integral (PAO).

E1 fixes \(C_U=1\) for absolute far-sums; the gap for M1.2 is not \(C_U\), it is **signed κ**.

Typical on-line Ω is proved; the gap in O-PC is the **strong / off-line** remainder (SOC), not the typical scale.

---

## 2. Gap family A — the B_θ OR-cut

Three independent conditional gates feed `B_θ`:

```text
                 ┌── PAO ─────────────────────────────┐
                 │   (H1: phase-aligned Ω of residual) │
  proved (RM) ───┼── Iso_H ──► Imp ──► B_θ            ├──► B_θ
                 │                                     │
                 └── DH ──► Mass-with-A ──► Imp ──► B_θ┘
```

### Min-cut statement (B_θ)

> Every path from classical input to `B_θ` hits **at least one** of  
> \(\{\mathrm{PAO},\ \mathrm{Iso\_H},\ \mathrm{DH}\}\).  
> These three form an **OR-min-cut**: proving **any one** (with (RM) where required) unlocks `B_θ`.

| Gate | Gap content (analytic) | Not the gap |
|------|------------------------|-------------|
| **PAO** | Phase lock of \(\psi-x=\Omega(x^{\beta_⋆})\) with weight \(x^{i\gamma_⋆}\) on positive log-measure | The residual formula itself; ZF upper bounds |
| **Iso_H** | Unbounded isolation on the vertical line \(\mathrm{Re}=\beta_⋆\) | Finite-height isolation; FE conjugate; density counts; multiplicity |
| **DH** | Polylog \(N(\beta_⋆,T)\) at moderate \(\beta_⋆>1/2\) | Power-of-\(T\) density; log-power only near \(\sigma=1\) |

### Specific gap depth (PAO — sharpest classical object)

Classical Ω supplies amplitude:

\[
\psi(x)-x=\Omega\bigl(x^{\beta_⋆}/|\rho_⋆|\bigr).
\]

PAO requires **alignment**:

\[
\operatorname{Re}\Bigl(e^{-i\gamma_⋆\log x}(\psi(x)-x)x^{-\beta_⋆}\Bigr)\ge c
\quad\text{on sets of log-measure }\gg 1.
\]

**Gap type:** multiplicative resonance / phase correlation between prime-power Chebyshev error and the ordinate of the putative zero.  
**Not closed by:** amplitude Ω, ZF upper bounds, or EF bookkeeping.

### Specific gap depth (Iso_H vs DH)

- Density controls **bulk** zeros with \(\beta\ge\sigma\).  
- Iso_H controls **ordinate cardinality on one line**.  
- **Missing edge (correctly absent):** `density → Iso_H` is a **dead non-route**, not a missing proof link.

**Gap type for Iso_H:** new vertical-line isolation technology (does not exist classically).  
**Gap type for DH:** zero-density exponent must hit \(0\) at moderate \(\sigma\) (classical exponents stay positive).

---

## 3. Gap family B — the O-TL AND-cut

`O-TL` has **four parallel obligation arms**; the programme treats them as **jointly necessary** for the primary target lemma:

```text
                    kappa_J_p ──► O-M1.2 ──┐
                    GO ─────────► O-M1.3bis ┼──► O-TL ──► RH
                    SOC ──► O-PC_strong ──► O-PC ──┤
                    O-Moll ────────────────────────┘
```

### Min-cut statement (O-TL)

> Under the programme’s obligation list, a path to `O-TL` requires **all four** arms  
> \(\{\mathrm{O\text{-}M1.2},\ \mathrm{O\text{-}M1.3bis},\ \mathrm{O\text{-}PC_{strong}},\ \mathrm{O\text{-}Moll}\}\).  
> This is an **AND-cut**: partial closes do not discharge O-TL.

| Arm | Open node at the tip | Specific analytic gap |
|-----|----------------------|------------------------|
| M1.2 | **κ ≤ J^{−p}** (p ≳ 1.12; safer ∼2) | Uniform **upper** bound on signed far \(U\)-sums; absolute κ=1 and RW \(J^{-1/2}\) insufficient under real \(c_1\) |
| M1.3bis | **GO(θ,X)** | Correlation of large hybrid Ω times with **wide ordinate gaps** (tube Φ_local) |
| O-PC | **SOC(X)+transfer** | Jump from proved **typical** \(\sqrt{\log\log}\) to **strong** \(\log\log\), then off-line transfer |
| O-Moll | **phase mollifier** | No classical object targets \(A_X/\theta_X\) at maximal abscissa |

### Partial edges that look like progress but do not cross the cut

| Proved feed | Touches | Why it does not close the arm |
|-------------|---------|-------------------------------|
| E1 \(C_U=1\) | κ node | Improves absolute constant; **κ still ∼1** without cancellation theorem |
| Typical Ω | O-PC | Wrong scale for O-TL; no off-line |
| R4.1 GHK strip | O-PC | Error control only; not a phase lower bound |
| Hybrid identity | O-PC | Bookkeeping; peels to OPC-Core still open |
| Architecture M1.2 | O-M1.2 | Sketch accepted; **numeric joint window** still empty under absolute far |

---

## 4. The dual gap (H1 vs H2) — one analytic tension, two graph nodes

```text
  H1 PAO:   need LOWER bound on oscillatory residual  (resonance / alignment)
  H2 κ:     need UPPER bound on oscillatory far sum   (cancellation)
```

These are **dual** demands on phase-sensitive sums:

| | H1 (PAO) | H2 (κ) |
|--|----------|--------|
| Goal node | `B_θ` | `O-M1.2` → `O-TL` |
| Bound type | limsup large | limsup small (relative to absolute) |
| Heuristic | phases **align** | phases **cancel** |
| Classical bar | log-measure alignment | p ≳ 1.12 in \(J^{-p}\) |

**Gap analysis consequence:** there is **no single classical theorem** that simultaneously feeds both gates. Closing the dual pair requires **two** independent analytic advances (or a deep structure theorem that controls both regimes). The graph correctly keeps them as **separate open nodes** with **no edge** between them.

---

## 5. Gap family C — the RH assembly gap

```text
O-TL ──programme_primary──► RH
B_θ  ──related_off_line──► RH
```

### Specific gap

Even if `B_θ` were proved, the edge `B_θ → RH` is only **related**, not a proved implication in the programme.  
Even if `O-TL` were proved at the stated scale, closing RH still requires the target lemma to force zeros onto the critical line in full generality.

**Min-cut for RH (programme reading):**

> RH is blocked by **O-TL** as primary, with `B_θ` a parallel off-line engine that does **not** substitute for O-TL.

**Correctly missing edges (not gaps to fill by citation):**

| Absent edge | Why absent |
|-------------|------------|
| `B_θ → O-TL` | Different objects (residual mass vs phase functional at zeros) |
| `Mass-with-A → O-TL` | Density/mass package ≠ path phase accumulation |
| `typical Ω → O-TL` | Wrong scale / location |
| `residual 539 → anything in RH` | ZLA forbidden |
| `density → Iso_H` | Dead non-route |

---

## 6. Where is “the” gap? (single-sentence hierarchy)

1. **If the goal is B_θ:** the gap is the **OR-cut** \(\{\mathrm{PAO},\mathrm{Iso\_H},\mathrm{DH}\}\) — three mutually alternative missing inputs to already-proved implications.  
2. **If the goal is O-TL:** the gap is the **AND-cut** of four arms, with tip nodes \(\{\kappa,\mathrm{GO},\mathrm{SOC},\mathrm{O\text{-}Moll}\}\).  
3. **If the goal is RH:** the gap is **O-TL** (primary), plus the non-implication of RH from `B_θ` alone.  
4. **The sharpest single classical object on the B_θ side:** **PAO** (phase-aligned Ω of the signed residual).  
5. **The sharpest single quantitative obstruction on the O-TL/M1.2 side:** **κ ≤ J^{−p}** with \(p\gtrsim 1.12\) (safer \(p\sim 2\)) under real \(c_1\).  
6. **The structural dual:** PAO (lower) vs κ (upper) — two gaps, opposite phase demands, no edge between them.

---

## 7. Cut diagram (proved | open)

```text
 PROVED SUBGRAPH                    OPEN CUT                         GOALS
 ─────────────────                  ────────                         ─────
 signed residual formula ──► [ PAO ] ─────────────────────────────► B_θ
 (RM)+implications ────────► [ Iso_H ] ──► Imp ───────────────────► B_θ
 (RM)+implications ────────► [ DH ] ──► MassA ──► Imp ────────────► B_θ

 E1 C_U=1 ─────────────────► [ κ ≤ J^{-p} ] ──► O-M1.2 ──┐
 tube design / mean gaps ──► [ GO ] ──────────► O-M1.3bis┼──► O-TL ──► RH
 typical Ω + identity ─────► [ SOC ] ──► O-PC_strong ───┤
 (empty shelf) ────────────► [ O-Moll ] ─────────────────┘
```

Everything left of the brackets is **not** where the programme is stuck.  
Everything inside the brackets **is** the gap.

---

## 8. What would close each atomic gap (success criteria)

| Node | Minimal success criterion (ZLA-clean) |
|------|----------------------------------------|
| PAO | Sequence of log-intervals with phase-aligned \(\psi-x\) Ω and measure \(\to\infty\) or \(\gg\log\log\) |
| Iso_H | For rightmost \(\beta_⋆\), \(N_{\mathrm{line}}(\beta_⋆,T)=2\) (conj pair) for all large \(T\) (up to EF) |
| DH | \(N(\beta_⋆,T)=O((\log T)^C)\) some \(C\), some \(\beta_⋆\in(1/2,1)\) on a usable set |
| κ | Theorem: far_signed \(\le J^{-p}\cdot\) far_abs on M1.3 paths, \(p\ge 1.12\), under executable \(c_1\) |
| GO | Infinitely many \(t_n\) with hybrid Ω scale **and** gap \(\ge\theta\cdot\) mean gap |
| SOC | Strong \(\lvert\Delta_X\rvert\gg\log\log X\) + transfer path to maximal abscissa |
| O-Moll | Explicit Dirichlet/hybrid mollifier with proved boost of \(A_X\) or \(\theta_X\) at O-TL locations |

None of these criteria is met by the classical corpus as of this note.

---

## 9. Non-gaps (do not waste effort)

- Re-deriving signed residual formula, E1, hybrid identity, typical Ω, R4.1  
- Reopening A0–A5⁺ / K⁺ or injecting residual integers into ζ lemmas  
- Absolute far-sum cosmetics or \(c_1\) padding alone  
- Monodromy of zero-free \(P_X\) as phase engine  
- Density ⇒ Iso_H  

---

## 10. One-line gap statement

> **The dependency graph is not missing edges among proved nodes; it is missing the open tips of three alternative B_θ gates (PAO / Iso_H / DH) and four conjunctive O-TL arms (κ / GO / SOC / O-Moll), with RH further gated by O-TL rather than by B_θ alone — and with PAO vs κ a dual lower/upper phase obstruction.**

**Status code:** `RH_GAP_ANALYSIS_DEPENDENCY_GRAPH_2026-08-08`

*Per aspera ad astra.*
