# 539 Labs — GitHub repository map

**Account:** [ArvinHampton](https://github.com/ArvinHampton)  
**Updated:** 2026-08-04  
**Canonical science corpus:** this repository (`539-Labs-Master`)

This map tells you which repo to open for which job. Prefer the **role** column over historical names.

---

## 1. Science and foundation (primary)

| Repository | Visibility | Role | Start here |
|------------|------------|------|------------|
| **[539-Labs-Master](https://github.com/ArvinHampton/539-Labs-Master)** | Public | **Canonical living corpus** — axiomatic book, residual stack, security ledger, verification package, claim tables | [README](README.md), [PROGRAMME_BASELINE](docs/S2-11DM2ET-X-Axiomatic-Book/PROGRAMME_BASELINE.md) |
| [539-Labs-Corpus](https://github.com/ArvinHampton/539-Labs-Corpus) | Public | **Satellite / mirror slice** — muon g−2 freeze, RH pure-Cat-A extracts, session summaries. Not a second master. | Points into Master living book |

Do **not** duplicate large bulk datasets (RFFT archives) into either corpus. Keep them offline.

---

## 2. HQH-539 product and crypto engineering

| Repository | Visibility | Role | Notes |
|------------|------------|------|-------|
| [hqh539-engine](https://github.com/ArvinHampton/hqh539-engine) | Public | **Live Streamlit + Stripe engine** (hash, AE portal, billing) | Production runtime; Canonical T3 profiles |
| [539-Labs-repo](https://github.com/ArvinHampton/539-Labs-repo) | Public | **FPGA / RTL / Vivado / demo / deploy / TDP** engineering workspace | README historically said “private”; content is public engineering |
| [HQH-539-RTL](https://github.com/ArvinHampton/HQH-539-RTL) | Public | Kerckhoffs-facing RTL publication | **Stub as of 2026-07-31** (README only). Full RTL lives under `539-Labs-repo/rtl/` until populated |
| [HQH-539-512-Encryption-Generator-for-High-Volume-Data-PPV-](https://github.com/ArvinHampton/HQH-539-512-Encryption-Generator-for-High-Volume-Data-PPV-) | Public | Historical high-volume encrypt product name / Streamlit lineage | Prefer `hqh539-engine` for current code |
| [HQH-539-512](https://github.com/ArvinHampton/HQH-539-512) | Public | Early marketing / codex stub | **Rewritten 2026-07-31** for Category B framing; not a full implementation |

**Security rule (all product repos):** hardness is Category B only. No completed reduction. Locked phrasing in Master `SECURITY.md`.

---

## 3. Pure-math experimental side tracks

| Repository | Visibility | Role |
|------------|------------|------|
| [resonant-galois](https://github.com/ArvinHampton/resonant-galois) | Public | Experimental constructive A5/A6 Inverse Galois templates (ternary-matrix) |

---

## 4. Private / non-crypto product lines

| Repository | Visibility | Role |
|------------|------------|------|
| [Clay-P-vs-NP-CatB-Exploratory-Mapping](https://github.com/ArvinHampton/Clay-P-vs-NP-CatB-Exploratory-Mapping) | Private | **P vs NP Category B dual-universe exploratory mapping only** — no Clay proof claimed; residual core untouched; residual-flux provenance mandatory. Living multi-problem Clay suite stays in Master `Clay-Mappings-CatB/` |
| [re-free-magnet-corpus](https://github.com/ArvinHampton/re-free-magnet-corpus) | Private | RE-free permanent magnet investigation |
| [jaxtins-garage](https://github.com/ArvinHampton/jaxtins-garage) | Private | Family auto-mechanics game |
| [jaxtins-racing](https://github.com/ArvinHampton/jaxtins-racing) | Private | Racing companion |
| [jaxtins-console](https://github.com/ArvinHampton/jaxtins-console) | Private | Unity/console port notes |

---

## 5. Accidental / archival stubs (do not use as sources of truth)

| Repository | Issue | Action |
|------------|-------|--------|
| [Dockerfile](https://github.com/ArvinHampton/Dockerfile) | Misnamed empty-ish container for a single README | **Archived intent** — use `hqh539-engine` |
| [requirements.txt](https://github.com/ArvinHampton/requirements.txt) | Empty / misnamed repo | **Archived intent** — use engine `requirements.txt` |

---

## 6. Where to put new work

| Kind of work | Target |
|--------------|--------|
| Pure residual algebra, Architecture A, packaging, No-Go, ACE | `539-Labs-Master/docs/S2-11DM2ET-X-Axiomatic-Book/` |
| Security games, reductions, hardness language | Same + root `SECURITY.md` |
| HQH verification KATs / avalanche / goldens | `docs/hqh539-verification/` in Master (and mirror from engine) |
| Live product UI / Stripe / deploy | `hqh539-engine` |
| SystemVerilog / Vivado / TDP | `539-Labs-repo` |
| Session freeze that must stay small | Optional extract into `539-Labs-Corpus` with pointer to Master |
| Private P vs NP Cat B exploratory share-slice | `Clay-P-vs-NP-CatB-Exploratory-Mapping` (full Clay suite stays in Master) |
| Galois experiments | `resonant-galois` |

---

## 7. Mandatory claim discipline

1. **Category A** — externally checkable (map definition, packaging integers under (S), SHA3-512 interface properties, measured synth metrics).  
2. **Category B** — framework / hardness / continuum / G4. Always: *computationally infeasible with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.*  
3. Residual objects require **residual-flux provenance** (not free \(T^\sharp\)).  
4. Free dynamics remain **Option 3** (two short basins). No free 539-classes.

See: [`SECURITY.md`](SECURITY.md), [`HQH539_Security_Reductions_Exploration.md`](docs/S2-11DM2ET-X-Axiomatic-Book/HQH539_Security_Reductions_Exploration.md), [`HQH539_Formal_Games_and_Hard_Problem_Pi.md`](docs/S2-11DM2ET-X-Axiomatic-Book/HQH539_Formal_Games_and_Hard_Problem_Pi.md).
