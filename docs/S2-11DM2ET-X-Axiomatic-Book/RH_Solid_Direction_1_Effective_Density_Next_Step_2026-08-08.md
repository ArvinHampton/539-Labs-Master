# RH Solid Direction 1 — Effective Density at Moderate σ (Next Step)

**Date:** 2026-08-08  
**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA in force  
**Does not prove:** Iso_H · Mass-with-A · B_θ · O-TL · RH  
**Feed:** (RM)+(polylog StripDens) ⇒ Mass-with-A (proved implication only)

---

## 1. Why this direction first

Among the five frozen solid directions, effective density at moderate σ is the only classical bulk-count route that could, if strengthened to polylog N_vert near a rightmost abscissa β⋆ only moderately larger than 1/2, feed Mass-with-A without needing full Iso_H. It is therefore the natural concrete next analytic step after baseline hygiene.

---

## 2. Concrete target (not a theorem)

**Working target T1 (open).** For some fixed β⋆ ∈ (1/2, 4/5] and some C < ∞,

N(β⋆, T) := #{ ρ = β + iγ : β ≥ β⋆, 0 < γ ≤ T } = O((log T)^C)

uniformly for large T, using only classical zero-density / explicit-formula technology admissible under ZLA (no model constants, no residual-algebra lemmas about ζ).

If T1 holds for the β⋆ of a rightmost zero on a positive-density height set under (RM), then Mass-with-A follows from the already-proved implication chain. T1 is not known for any β⋆ ≤ 4/5.

---

## 3. Classical ledger (what can be used)

| Tool | Role | Ceiling at moderate σ |
|------|------|------------------------|
| Ingham A(σ) = 3/(2−σ) | Classical density shape | Positive power of T remains |
| Huxley / Guth–Maynard | Improved A(σ) in parts of [0.7, 1) | Still not polylog N_vert at σ ~ 0.6–0.8 |
| Explicit density (KLN, Kadiri, Chourasiya–Simonič) | Effective constants | Useful for numerical M1.2 (A,B,C); not polylog at moderate σ |
| Density hypothesis | Conditional polylog-class counts | Not proved |
| Maynard–Pratt / Hypothesis F | Finite vertical lines ⇒ better density | Converse direction; not Iso_H |

**Locked distinction:** density vs isolation (`RH_Density_vs_Isolation.md`). Better density is not Iso_H; half-isolation is not Iso_H.

---

## 4. Executable next steps (this programme)

### Step A — Fix a numerical density majorant tree (O-M1.2 support)

1. Choose a concrete classical density theorem with explicit constants (e.g. an effective Ingham or KLN form).
2. Feed it into the existing M1.2 remainder architecture (`RH_M1_2_Effective_Density.md`, `scripts/rh_M1_2_remainder_diagnostic.py`).
3. Produce numerical (A,B,C) triples on a finite height band so that the uniform M1.2 architecture has concrete majorants — still conditional on classical density, still not O-TL.

**Success criterion:** a short note with explicit (A,B,C) and the density theorem cited; no RH claim.

### Step B — Map polylog gap at moderate σ

1. For β⋆ ∈ {0.55, 0.60, 0.65, 0.70, 0.75, 0.80}, record the best published A(σ)(1−σ) exponent and the implied N(β⋆,T) ≪ T^{θ} (log T)^c growth.
2. State the gap to O((log T)^C) in one table.
3. Mark any range where Bellotti / near-1 technology already gives polylog-class control (near σ = 1 only).

**Success criterion:** one comparison table; barrier location unchanged if no new theorem appears.

### Step C — Conditional Mass-with-A template under a named density hypothesis

1. State a named density hypothesis DH(β⋆,C): N(β⋆,T) = O((log T)^C).
2. Under (RM)+DH(β⋆,C), write the Mass-with-A implication as a formal template (already essentially present via (RM)+(polylog StripDens)).
3. Keep DH explicitly conditional; do not treat it as proved.

**Success criterion:** one page of ZLA-clean implication language; RH still open.

### Step D — Do not do

- Do not import residual packaging, 539, or continuum model constants into ζ lemmas.
- Do not weaken O-TL to √(log log X) without an explicit programme decision.
- Do not claim Iso_H from density.

---

## 5. Recommended order of attack

1. **Step B** first (cheap, freezes the classical gap table).
2. **Step A** second (feeds O-M1.2 numerical constants).
3. **Step C** third (templates conditional Mass-with-A without overclaim).

If Step B shows a classical breakthrough in the literature after 2025–2026, re-evaluate the solid-direction ranking.

---

## 6. Interface to other solid directions

| Direction | Interface |
|-----------|-----------|
| 2 Iso_H | Density does not imply Iso_H; Iso_H is stronger isolation |
| 3 Path from on-line Ω | Independent bypass; can run in parallel |
| 4 Resonance off the line | Independent bypass for O-PC / O-TL |
| 5 Mass-with-A under (RM) | Direct consumer of polylog density / StripDens |

---

## 7. Status after this note

- Baseline A4⁺/A5⁺ hygiene closed on K⁺ (corpus).
- Residual P⁺ permanent-class survival optional lock recorded.
- RH Direction 1 next-step programme written; **no analytic obligation discharged**.
- Primary O-TL and RH remain open.

**Status code:** `RH_SOLID_DIR1_EFFECTIVE_DENSITY_NEXT_STEP_2026-08-08`

*Per aspera ad astra.*
