# RH Explore for Resolutions — Pass 3 (Post P1–P4) (2026-08-08)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Pass:** 3 — after PAO Form C recast, κ attempt, AFE-Moll skeleton, FE bookkeeping  
**Does not prove:** RH · O-TL · B_θ · Form C · κ · Iso_H · DH  
**ZLA. Residual A0–A5⁺/K⁺ not reopened.**

**Priors:** Pass 1–2 explore-all · gap analysis · H1–H5 · resonance/Selberg · Priority 4  
**Results:** `rh_explore_resolutions_pass3_results.json`

---

## 0. Verdict

| Question | Answer |
|----------|--------|
| Unconditional resolutions found? | **0** |
| Map updated after P1–P4? | **Yes** |
| Sharpest B_θ object? | **Form C** (fixed-frequency Dirichlet poly at ρ⋆) |
| RH / O-TL? | **Open** |

---

## 1. What P1–P4 clarified (not closed)

| Clarification | Source | Consequence for resolution search |
|---------------|--------|-----------------------------------|
| Star-phased ψ−x is **not** the PAO engine | P1 | Stop free-t / star-phase attacks; attack **Form C** |
| ε_other unconditional ↔ Iso_H-adjacent | P1 | Amplitude-Ω route couples to Iso_H; Form C prime-side is separate |
| No κ with p>1 | P2 | M1.2 joint window stays blocked under absolute majorants |
| RW / L2 proxies insufficient | P2 | Need stronger-than-random cancellation or different remainder target |
| O-Moll only on AFE surface | P3 | Levinson/Conrey permanently excluded |
| FE path = hygiene | P4 | No phase engine from ξ alone |

---

## 2. Updated cuts

### B_θ — OR-cut (any one unlocks)

```text
B_θ  ◄── Form_C   (was PAO; recast P1)
B_θ  ◄── Iso_H + (RM)
B_θ  ◄── DH + (RM) → Mass-with-A
```

**Form C.**
\[
\limsup_{X\to\infty}
\Bigl|
\sum_{n\le X}
\frac{\Lambda(n)}{n^{\rho_\star}\log n}
\Bigr|
=\infty.
\]

### O-TL — AND-cut (all required)

```text
κ → O-M1.2  ──┐
GO → O-M1.3bis ┼──► O-TL ──► RH
SOC → O-PC     │
AFE-Moll ──────┘
```

### Dual (unchanged structure, sharper names)

| Lower (need large) | Upper (need small) |
|--------------------|--------------------|
| **Form C** at fixed ρ⋆ | **κ** far U-sum on paths |

No edge between them.

---

## 3. Ten routes explored

| ID | Route | Available today? |
|----|-------|:----------------:|
| R1 | Form C via n-aspect large values at fixed complex ρ⋆ | **No** |
| R2 | Iso_H technology → B_θ | **No** |
| R3 | DH polylog → Mass-with-A → B_θ | **No** |
| R4 | κ p>1 on GHK/U → O-M1.2 | **No** |
| R5 | GO → tube path → O-M1.3bis | **No** |
| R6 | SOC strong + FE transfer + path | **No** |
| R7 | AFE-Moll coefficients for Im log P_X | **No** |
| R8 | Full phase stack → O-TL attempt | **No** (all tips open) |
| R9 | Residual algebra → RH | **Dead** (ZLA) |
| R10 | Weaken O-TL to √(log log) | **No** (still not RH) |

**Classical blockers (short):**

- **R1:** free-\(t\) / pretentious tools ≠ fixed off-line complex frequency  
- **R2–R3:** density ≠ isolation; moderate-σ T-powers  
- **R4:** absolute κ=1 only; RW \(p=1/2\) below bar  
- **R5–R6:** correlation / strong scale missing  
- **R7:** wrong objective functionals dominate the literature  
- **R9:** forbidden under ZLA  

---

## 4. Shortest conditional paths (unchanged length)

**To B_θ:** Form C alone · or Iso_H+(RM) · or DH+(RM)  
**Toward O-TL:** κ ∧ GO ∧ SOC ∧ AFE-Moll  
**To RH unconditionally:** *empty*

---

## 5. Dead routes (confirmed post P1–P4)

Absolute far@c1=291 · RW-only κ · Soundararajan-as-Form-C · star-phased PAO engine · Levinson-as-O-Moll · density⇒Iso_H · FE-as-phase-engine · monodromy of P_X · residual⇒RH · c1 cosmetics alone  

---

## 6. Proved assets (do not re-derive)

Signed residual (19) · Form B↔C · E1 · (RM)+hyp implications · typical Ω · hybrid identity · R4.1 · A4⁺/A5⁺ residual closed  

---

## 7. Where resolution effort is still rational

| Priority | Object | Why |
|----------|--------|-----|
| 1 | **Form C** at fixed ρ⋆ | Shortest classical-shaped B_θ object after P1 |
| 2 | **κ** any p>1 on GHK/U | Only scanned route to numeric M1.2 under real c1 |
| 3 | **DH** or **Iso_H** | Alternative B_θ gates with proved implications |
| 4 | **GO** / **SOC** / **AFE-Moll** | O-TL arms; each independent |

Do **not** spend effort on the dead list in §5.

---

## 8. Global one-liner

> After P1–P4, the resolution map is sharper (Form C, AFE-only O-Moll, FE hygiene) but **not shorter**: unconditional resolution count remains **zero**; B_θ is still an OR of three open gates and O-TL an AND of four open arms.

**Status code:** `RH_EXPLORE_RESOLUTIONS_PASS3_2026-08-08`

*Per aspera ad astra.*
