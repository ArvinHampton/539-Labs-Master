# Status scoreboard freeze (pure Category A)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Primary not closed · RH open.**  
**Axiom ZLA** in force. No model constants.

**Companions:**  
`RH_ND1_Stability_Resolve.md`,  
`RH_Iso_H_Classical_Constraints.md`,  
`RH_Finite_Product_Ivic_MassA.md`,  
`RH_Density_vs_Isolation.md`,  
`RH_Existing_Theorems_Solid_Directions.md`.

---

## Resolved

| Item | Status |
|------|--------|
| Conjugate obstruction | **Closed** — optimal lock → net \((m+1)/\lvert\rho_\star\rvert\) |
| Good points under (RM) | **Strengthened** — positive-density \(u_k\), \(\Phi^\star\ge c\) (S11) |
| (RM)+(Iso_H) ⇒ OP1 | **Proved** (S13) |
| (RM)+(Iso_H) ⇒ B_θ | **Proved** (S16) |
| Left abscissa in \(A\) | **Dies exponentially** under (RM) |
| Absolute average of \(A\) | \(\asymp\) majorant — **no phase saving** (closed as **non-route**) |
| (RM)+(polylog StripDens) ⇒ Mass-with-A | **Proved implication** |
| Classical density shape | **Recorded** (Ingham / Huxley / KLN / Bellotti) |
| Density vs isolation | **Clarified** |
| Maynard–Pratt half-isolation | **Recorded** (local geometry; not Iso_H) |
| Levinson–Ivić horizontal isolation | **Recorded** (near \(\sigma=1\) only; not Iso_H) |

---

## Barrier (after full package)

```text
phase lock ✓ · residual ✓ · conjugate lock ✓ · left abscissa dies ✓
        │
        ▼
(RM)+(Iso_H) ──proved──► B_θ
(RM)+(polylog StripDens) ──proved──► Mass-with-A ──► B_θ
        │
        ├── Iso_H unconditional ✗ OPEN
        ├── polylog StripDens for arbitrary β⋆ > 1/2 ✗ OPEN
        └── absolute average A gives no free saving ✓ (closed as non-route)
```

B_θ is blocked by **abscissa isolation** (or **strong strip density**) on the rightmost line — not by loglog, E1, conjugate phase, or absolute averaging of \(A\).

---

## Not resolved

| Item | Status |
|------|--------|
| (Iso_H) unconditional | **Open** |
| Polylog StripDens for arbitrary \(\beta_\star>1/2\) | **Open** |
| Unconditional Mass-with-A | **Open** |
| Unconditional B_θ | **Open** |
| RH / primary O-TL | **Open** |

---

## Solid directions (frozen)

Aligned with Master solid-direction freeze (`153c903` lineage; current programme list):

| Rank | Direction |
|------|-----------|
| **1** | **Mass-with-A under (RM)** — polylog / average \(A\) on \(K_\star\) |
| **2** | **StripDens** |
| **3** | **Resonance off the line** |
| **4** | **Effective density constants** |
| **5** | **Finite-product approximation off the line** (role: prime side) |
| **6** | **Path continuation from on-line Ω** |

None of these is known to close B_θ or RH.

---

## One-liner

**ND1 and related implications are locked; B_θ still needs unconditional Iso_H or polylog StripDens / Mass-with-A; absolute averaging of \(A\) is a closed non-route; RH remains open.**

*Per aspera ad astra.*
