# Seed-orbit package — definition + enumeration results

## Definition (executed)

\(\mathcal{C}_{\mathrm{seed}}(\Sigma)\) = set of **terminal cycles (basins)** of physical seeds \(\Sigma\) under \(T^\sharp\).

**Seeds (no 539):**

| Package | Construction | \(|\Sigma|\) |
|---------|--------------|------------:|
| **S243** | One seed per tower: \(s_\tau=f_\tau\cdot 243+\tau\) | 243 |
| **S4880** | One seed per flux quantum: \(s_{\tau,j}=(f_\tau\cdot 243+\tau)\cdot 64+j+1\) | 4880 |

Flux split (democratic): **20** towers with \(f=21\), **223** with \(f=20\); \(20\cdot21+223\cdot20=4880\).

**Dynamics:** \(T^\sharp\) only.  
**Equivalence:** same terminal cycle.  
**539:** post-hoc comparison only.

Docs: `Phase0_SeedOrbit_Package.md`  
Script: `scripts/phase0_seed_basins.py`  
JSON: `phase0_seed_basins_results.json`

---

## Results

| Package | Seeds | \(N_{\mathrm{basins}}\) | \(=\!539\)? | Steps-to-cycle (med/mean/max) | Cycle lengths |
|---------|------:|------------------------:|:-----------:|-------------------------------|---------------|
| S243 | 243 | **2** | **No** (diff 537) | 11 / 10.9 / 19 | only 1 and 2 |
| S4880 | 4880 | **2** | **No** (diff 537) | 17 / 15.9 / 32 | only 1 and 2 |

Attractors observed: essentially **\{1\}** (or \{0\}) and a **2-cycle**; ~36–49% of seeds flow to an attractor containing 1.

**Cardinality note:** S243 has \(N_{\mathrm{basins}}\le 243<539\) by definition — cannot realize H0 as a basin count.

**S4880** could in principle reach 539 basins; empirically it reaches **2**.

---

## Bott gate

**Closed (negative):** count ≠ 539 for these seed-orbit packages.  
→ **Do not** proceed to a classifying map \(B\mathrm{Spin}/BO\) aimed at this \(\mathcal{C}_{\mathrm{seed}}\) as a 539-element set.

---

## Interpretation

1. Refined seed-orbit \(\mathcal{C}\) is **well-defined** and **executable**.  
2. Under \(T^\sharp\), democratic flux seeds collapse into **two** terminal orbits — consistent with strong contraction (ACE \(N_\star\sim 14\)) and with earlier C2 “2 components” results.  
3. The HQCC claim of **539** classes is **not** “basins of flux seeds under \(T^\sharp\)”.  
4. Long 539 structure still requires **external** constraints (forced length, holographic narrative, phase-lock), not seed-basin combinatorics alone.

---

## What remains if one still wants “539 classes”

Canonical write-up: **`H0_539_Honest_Options.md`**

| Option | Verdict |
|--------|---------|
| 1. Derive \(L_\star\), count paths | Non-circular in principle; **blocked** (no clean \(\Psi\)) |
| 2. Force 539-step iteration by hand | Produces count; **circular**, not a derivation |
| 3. Keep 539 as Category B open; \(T^\sharp\) short depth Category A | **Matches current evidence (default)** |

No classifying-map / Bott work until a verified non-circular 539-object construction exists.

---

## Bottom line

> **Executed:** seed-orbit \(\mathcal{C}\) + enumeration.  
> **Result:** \(N_{\mathrm{basins}}=2\neq 539\) for both S243 and S4880 under \(T^\sharp\).  
> **Bott link** on this package as a 539-set: **not legitimate**.  
> **No-Go / ACE:** reinforced.
