# Security Labeling Protocol

All claims in this repository fall into one of two categories.

## Category A — Externally Verifiable

Claims that reduce to standard, publicly analyzed cryptographic primitives or assumptions (for example, the collision resistance and preimage resistance properties of SHA3-512 under classical and quantum models such as Grover’s algorithm), or to pure arithmetic / topology that is fully specified and machine-checkable without framework physics. These may be stated without special qualification beyond normal cryptographic caution.

## Category B — Proprietary Framework Claims

Claims that derive from the internal structure of the S²-11DM²ET-X model, the HQCC theorem, the 243 KK-tower analysis, the 539-step resonant dynamics, or the physical 539.9 s brane-leakage clock — and all statements of **cryptographic hardness** of HQH-539 beyond the Category A front-end.

These claims must always carry the explicit label:

> Proprietary framework claim (S²-11DM²ET-X) — not independently verified, pending external cryptanalysis.

Never use absolute language (“unbreakable”, “provably secure”, “information-theoretic”).  
Preferred framing:

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

## Current map baseline

The repository uses the **Canonical T3** map.  
Earlier evaluation of the T4121 variant showed cleaner fixed-point behaviour but reduced observed cryptographic hardness (avalanche and pre-image resistance). The original T3 coefficients were therefore retained.

## HQH-539 security reductions (status)

**No completed, externally verified security reduction is claimed.**

| Criterion | Status (2026-07-31) |
|-----------|---------------------|
| 1. Game-based definitions (Preimage / Second-preimage / Collision) | **Supplied** |
| 2. Hard problem Π (Resonant Path Problem) as combinatorial statement | **Supplied** (difficulty not proven) |
| 3. PPT reduction R with advantage relation | **Unmet** |
| 4. Independent peer review / external cryptanalysis | **Unmet** |

Canonical files:

- `docs/S2-11DM2ET-X-Axiomatic-Book/HQH539_Formal_Games_and_Hard_Problem_Pi.md`
- `docs/S2-11DM2ET-X-Axiomatic-Book/HQH539_Security_Reductions_Exploration.md`

Round count may be cited from non-circular packaging under Principle (S) (18+521 or floor((N_flux − f_max)/9)). That supplies an **engineered fixed-round budget**, not a proof of preimage/collision hardness. Residual carrier O_res may appear only under residual-flux provenance (not free T♯). Continuum / G4 claims are excluded from hardness assumptions.
