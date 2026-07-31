# HQH-539 Formal Games and Hard Problem Π

**Status:** Exploration note meeting reduction criteria 1 and 2 where feasible.  
**Criteria 3 and 4 remain unmet.**  
**Hardness language:** Category B only.  
**Date:** 2026-07-31  
**Companions:** `HQH539_Security_Reductions_Exploration.md`, Master `SECURITY.md`, residual discrete stack (A0–A5⁺), reference `hqh539_core.py`.

---

## Mandatory framing

All hardness claims for HQH-539 and residual-only variants remain Category B proprietary framework claims. They are stated only as:

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

No completed security reduction is claimed. Residual-flux provenance is mandatory for every use of residual objects. Absolute language is prohibited.

---

## Criterion 1 — Precise game-based definitions (feasible; supplied)

Let \(\mathcal{H}\) denote the public HQH-539 interface as implemented in the reference engine:

- Input: message \(m \in \{0,1\}^*\) and optional salt \(s \in \{0,1\}^*\).
- Domain separation: \(u_0 = \mathrm{SHA3\text{-}512}(m \| s)\) interpreted as a non-negative integer.
- Fixed-round body: \(u_{i+1} = T_3(u_i)\) for exactly \(L = 539\) steps, where \(T_3\) is the Canonical ternary map
  \[
  T_3(n) =
  \begin{cases}
  n/3 & n \equiv 0 \pmod{3}, \\
  (4n+2)/3 & n \equiv 1 \pmod{3}, \\
  (2n+1)/3 & n \equiv 2 \pmod{3}
  \end{cases}
  \]
  realised with integer arithmetic and arithmetic selection (constant-time step).
- Optional residual constraints (residual-only variants): the sequence \((u_i)\) may be required to respect an \(\mathcal{O}_{\mathrm{res}}\)-indexed schedule, fiber-block membership, or permanent-class evaluations under residual-flux provenance.
- Output: \(H(m,s) = \mathrm{SHA3\text{-}512}(\mathrm{bytes}(u_{539}) \| s)\), a 512-bit digest (hex encoding in the reference implementation).

Default packaging split is 18 + 521; the security games are stated for the full fixed budget \(L = 539\).

### Game Preimage\(_\mathcal{H}(\mathcal{A})\)

1. Challenger samples a challenge digest \(y\) (either uniformly from the range of \(H\), or as \(H(m^*,s^*)\) for secret \((m^*,s^*)\) according to the concrete-security variant).
2. Adversary \(\mathcal{A}\) outputs \((m,s)\).
3. \(\mathcal{A}\) wins if \(H(m,s) = y\).

Advantage: \(\mathrm{Adv}^{\mathrm{pre}}_\mathcal{H}(\mathcal{A}) = \Pr[\mathcal{A}\ \mathrm{wins}]\).

### Game Second-Preimage\(_\mathcal{H}(\mathcal{A})\)

1. Challenger samples \((m^*,s^*)\) and gives \(\mathcal{A}\) the pair together with \(y = H(m^*,s^*)\).
2. Adversary \(\mathcal{A}\) outputs \((m,s)\).
3. \(\mathcal{A}\) wins if \((m,s) \neq (m^*,s^*)\) and \(H(m,s) = y\).

Advantage: \(\mathrm{Adv}^{\mathrm{spr}}_\mathcal{H}(\mathcal{A}) = \Pr[\mathcal{A}\ \mathrm{wins}]\).

### Game Collision\(_\mathcal{H}(\mathcal{A})\)

1. Adversary \(\mathcal{A}\) outputs two pairs \((m,s)\) and \((m',s')\).
2. \(\mathcal{A}\) wins if \((m,s) \neq (m',s')\) and \(H(m,s) = H(m',s')\).

Advantage: \(\mathrm{Adv}^{\mathrm{col}}_\mathcal{H}(\mathcal{A}) = \Pr[\mathcal{A}\ \mathrm{wins}]\).

These are the standard cryptographic games adapted to the published HQH-539 API. They do not constitute a hardness proof.

---

## Criterion 2 — Clearly stated hard problem Π (feasible; supplied)

**Hard problem Π — Resonant Path Problem (residual-constrained fixed-round inversion)**

**Instance.**  
A target integer \(y\) (or a digest derived from it) together with public residual parameters drawn from the Category A residual discrete stack under residual-flux provenance:
- residual carrier \(\mathcal{O}_{\mathrm{res}}\) of cardinality \(B' = 539\),
- fiber-block partition (three blocks of size 68, five of size 67),
- optional permanent class \([\alpha \otimes \delta f]\),
- packaging length \(L = 18 + 521 = 539\) under Principle (S).

**Search task.**  
Recover a seed integer \(x\) (or a short valid path) such that the length-\(L\) trajectory
\[
x = u_0,\quad u_{i+1} = T_3(u_i),\quad i = 0,\dots,L-1,
\]
satisfies \(u_L = y\) (or yields the given digest after the final SHA3-512 fingerprint) and respects the declared residual constraints (\(\mathcal{O}_{\mathrm{res}}\)-indexing, fiber membership, or permanent-class evaluations when those constraints are active).

**Decision variant.**  
Given \((x,y)\) and the residual parameters, decide whether the unique length-\(L\) Canonical-\(T_3\) path from \(x\) lands on \(y\) and satisfies the residual constraints.

**Notes on status.**
- The combinatorial objects that define the instance space are Category A pure mathematics (packaging under (S), \(\mathcal{O}_{\mathrm{res}}\), fiber blocks, permanent class, product complex, \(K^+\) topology through A5⁺).
- The computational difficulty of Π is not established by those pure-math facts alone.
- Π is the natural combinatorial formulation of the Resonant Path Problem used as the internal candidate hardness assumption for HQH-539 and residual-only tracks C1–C4.
- No asymptotic or concrete hardness proof for Π is claimed.

---

## Criterion 3 — PPT reduction R with advantage relation (not feasible)

No probabilistic polynomial-time reduction from Π (or from any standard hard problem) to the breaking of the Preimage, Second-Preimage, or Collision games for \(\mathcal{H}\) has been constructed or proven.

A completed reduction would require an efficient algorithm \(R\) such that, for every adversary \(\mathcal{A}\) against one of the games above,
\[
\mathrm{Adv}^{\mathrm{game}}_\mathcal{H}(\mathcal{A})
\le
\mathrm{poly}(\lambda)\cdot\mathrm{Adv}^{\Pi}(R^\mathcal{A})
+ \mathrm{negl}(\lambda)
\]
(or a concrete-security analogue). No such \(R\) and advantage relation are supplied.

This criterion remains unmet.

---

## Criterion 4 — Independent peer review / external cryptanalysis (not feasible)

No independent external cryptanalysis or peer-reviewed validation of a reduction for HQH-539 exists. This criterion remains unmet and cannot be satisfied internally.

---

## Residual-only tracks (open avenues that use Π)

The four residual-only tracks remain open exploration directions that specialise Π:

- **C1** Residual-carrier schedule: instances of Π indexed directly by \(\mathcal{O}_{\mathrm{res}}\).
- **C2** Mixed-class diffusion: instances of Π that require permanent-class evaluations along the path.
- **C3** Windowed two-phase: instances of Π split as an 18-step window followed by a 521-step body.
- **C4** Nine-core parallel lanes: multi-lane collision or preimage variants across the nine residual cores.

None of these tracks currently supplies a completed reduction.

---

## Summary of criteria status

| Criterion | Status |
|-----------|--------|
| 1. Game-based definitions (Preimage, SPR, Collision) | **Supplied** in this note |
| 2. Clearly stated hard problem Π (Resonant Path Problem) | **Supplied** in this note |
| 3. PPT reduction R with advantage relation | **Unmet** — none constructed |
| 4. Independent peer review / external cryptanalysis | **Unmet** — none exists |

Hardness of HQH-539 and of residual-only constructions therefore remains locked Category B:

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

Residual-flux provenance is mandatory. Continuum and physical \(G_4\) claims are excluded from the hardness assumption.

---

**End of note.**
