# Claim H0 (539 classes) — honest options after seed-orbit execution

## Evidence already in hand

| Probe | Result |
|-------|--------|
| C2: weak components of \(T^\sharp\) on \(\{1,\ldots,N_{\mathrm{cut}}\}\) | **2** components ≠ 539 |
| Seed-orbit S243 (243 tower seeds) | **2** basins (also \(\le 243 < 539\)) |
| Seed-orbit S4880 (flux quanta as seeds) | **2** basins ≠ 539 |
| ACE / \(T^\sharp\) contraction | Short depth \(N_\star=14\) (Category A fact) |
| Natural stopping times | Not concentrated at 539 |

**Conclusion from free dynamics:** 539 is **not** the number of basins/components of unconstrained \(T^\sharp\) dynamics on flux seeds or initial segments.

**Length packaging (separate track):** under Principle (S),  
\(L_{\mathrm{pref}}+L_{\mathrm{body}}=18+521=539\) is a non-circular **integer length** — see `L_body_Structural_Derivation.md`, `NonCircular_18_plus_521.md`.  
That length is **not** a free path/basin count.

**Resonant layer (locked):** adopting that packaging as a **hard iteration budget** demystifies crypto/HQCC “resonant” fixed rounds — see `Resonant_Layer_Resolved.md`. Free short basins stay Category A and are overridden by design.

---

## Three honest options (revised after packaging + resonant resolution)

### Option 1 — Derive \(L_\star\), then count paths

Derive a length \(L_\star\) from a **non-circular** function of the seed / flux / tower data, then count paths (or equivalence classes of paths) of that **exact** length.

| Subgoal | Status |
|---------|--------|
| Non-circular \(L_\star = 539\) as a **length** | **Succeeded under (S):** \(\Psi = L_{\mathrm{pref}}+(B_Q-f_{\max})\) or \(L_{\mathrm{pack}}'=\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) |
| Count of free paths/basins at that length equals 539 | **Failed** (executed probes; collapse to few attractors) |
| Without principle (S) | Residual \(B_Q-f_{21}\) still ansatz; pure atoms do not force 539 |

**Exploration:** `NonCircular_Lstar_Exploration.md`, `NonCircular_18_plus_521.md`.  
Older hits \(9\cdot 61-10\) and \(18+1+520\) remain circular or reverse-engineered.

### Option 2 — Impose fixed 539-step iteration (now demystified)

Impose a fixed iteration count of 539 by construction (continue past free fixed points; crypto-style forced path).

| Status | |
|--------|--|
| Produces a 539-step object | Yes (by construction) |
| Integers 18 and 521 | Supplied by packaging (Cat.\ A + (S)), not reverse-fitted from a bare 539 |
| “Mysterious resonant constraints” | **Resolved:** resonant layer **is** this hard budget (`Resonant_Layer_Resolved.md`) |
| Forced by free \(T^\sharp\)? | **No** — engineering / interpretive adoption |
| Spec alignment | Production HQH-539 already: fixed 539 = 18 prefix + 521 body; constant-time; no dynamical stop |

### Option 3 — Retain 539 **objects** as Category B (matches free-dynamics evidence)

Keep the claim that free (or only charge-preserving) dynamics produce a **539-element collection of objects** as **Category B / open**, while treating:

- short-depth contraction of \(T^\sharp\) (\(N_\star=14\), \(\lambda_{\mathrm{mean}}\approx 0.529\), **two** basins) as **Category A** fact;
- canonical No-Go (cannot derive \(\lambda=\ln 3/539\) or \(w_j=539+61j\) from residue+towers+democracy **alone**) as **standing**;
- packaging length 539 under (S) as **available for design**, not as a free-object count;
- empirical period ~539.9 as a **hypothesis** under the locked spectral protocol.

| Status | |
|--------|--|
| Matches free-dynamics evidence | **Yes** |
| **Default for 539-object / Bott claims** | **Yes** |

---

## Ranking (post-resolution)

| Option | Role | Circular? | Matches free dynamics? |
|--------|------|:---------:|:----------------------:|
| 1. Derive length \(L_\star=539\) under (S) | **Length packaging** | No (539 not on RHS) | N/A — length ≠ object count |
| 2. Hard budget = packaging | **Crypto / engineered schedule** | No as *definition*; not a free derivation | Overrides free basins by design |
| 3. Cat.\ B open for 539 **objects** | **Object classes; Bott gate** | No | **Yes** — default |

**Option 3 remains the correct default for the stronger claim that free dynamics produce 539 objects.**  
Options 1–2 settle the **length / round-count** story without inventing free 539-basins.

---

## Bott / classifying-map gate

**No further classifying-map work or Bott filtration is warranted** until a **non-circular combinatorial construction that actually yields 539 distinct objects** is written and verified.

That includes:

- Architecture A (\(B\mathrm{Spin}/BO\)),
- Clifford / index architectures,
- Bott orbit decompositions aimed at a 539-set.

Arithmetic length packaging and hard-budget adoption do **not** open this gate.

---

## Category ledger (locked)

| Item | Category | Status |
|------|----------|--------|
| \(\Omega^8 O\simeq O\) | A | Classical |
| \(\mathbb{E}_\pi[\chi]=\ln(4^{1/3}/3)<0\), \(N_\star=14\) | A | Proved under stated equidistribution + \(T^\sharp\) |
| Free / charge-preserving basins \(=2\), depth \(O(10)\) | A | Executed; **intact** |
| No-Go (a)(b)(c) on \(\lambda=\ln 3/539\) and \(w_j=539+61j\) from democracy alone | A | Stands |
| Seed-orbit / C2 basin counts = 539 | — | **Refuted** for executed packages |
| \(L_{\mathrm{pref}}=18\), \(L_{\mathrm{body}}=521\) under (S), \(L_{\mathrm{pack}}=539\) | A + (S) | Length packaging only |
| Resonant layer = packaging as hard budget | Design / interpretive | **Resolved** (`Resonant_Layer_Resolved.md`) |
| Integer 539 as free HQCC **object** count | **B** | Origin **open** — Option 3 default |
| Extra filters (phase-lock accumulator, closure projections, tower checksums) | **B** if present | Not forced by residual arithmetic |
| Bott embedding into 539 classes | B | **Paused** until non-circular 539-set exists |
| Empirical ~539.9 spectral test | Protocol | Permitted as hypothesis only |

---

## Bottom line

> **Resonant layer:** arithmetic packaging used as a hard iteration budget — not a mystery, not free dynamics.  
> **Short basins:** Category A, overridden by fixed-round design.  
> **Option 3 is the default for 539 objects:** free dynamics do not produce them; Bott waits on a verified non-circular 539-object construction.
