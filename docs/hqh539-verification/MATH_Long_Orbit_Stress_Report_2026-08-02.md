# Math report — pure Canonical T3 long-orbit stress (2026-08-02)

**Category:** A (pure number-theoretic statistics under frozen product map)  
**Map:** Option A Canonical T3 — \(r0: n//3\), \(r1: (4n+2)//3\), \(r2: (2n+1)//3\)  
**Harness:** `stress_test_long_orbits.py`  
**Raw results:** `long_orbit_stress_results_2026-08-02.json`

---

## 1. Purpose

Stress-test residual pure-map claims **without** continuum or security language:

1. Steps-to-1 for named seeds (including 20, 21, 4880).  
2. Census of steps-to-1 on all \(n \in [1, 50\,000]\).  
3. Endpoint statistics after **exactly 539** applications on 2000 large random seeds.  
4. Residue-class hit rates along 539-step trajectories.  
5. r1 injectivity sample and \(1\leftrightarrow 2\) cycle check.

---

## 2. Results (Category A)

### 2.1 Named seeds — steps to reach 1

| Seed | Steps to 1 (Canonical T3) |
|------|---------------------------|
| 1 | 0 (already ≤1) / cycle with 2 |
| 2 | 1 (→1) then cycles \(1\leftrightarrow 2\) if continued |
| 20 | **5** |
| 21 | **6** |
| 4880 | **14** |
| \(10^6\) | (see JSON) |
| \(10^{12}\) | (see JSON) |
| \(10^{18}\) | (see JSON) |

**Important separation:** The HQCC theorem note’s charge-preserving map reports a **7-step** orbit for seed 4880 under a **different** residual rule set. That short orbit remains Category A **for that formulation**. Under the **product Canonical T3** used in HQH-539, 4880 → 1 in **14** steps. Do not mix the two maps in one claim.

### 2.2 Census \(n = 1 \ldots 50\,000\)

| Statistic | Value |
|-----------|-------|
| Failures (cap 50 000 steps) | 0 |
| Min steps | 0 |
| Max steps | **55** |
| Mean steps | **≈ 21.91** |
| Median | (see JSON) |
| p95 / p99 | (see JSON) |

**Interpretation:** Free small seeds under pure Canonical T3 **do not** require 539 steps to reach 1. The number **539** in HQH-539 is the **fixed packaging depth of the hash**, not an empirical pure-map stopping time for arbitrary small integers.

### 2.3 Exactly 539 steps on large seeds

On 2000 random seeds in \([10^{18}, 10^{36})\):

| Statistic | Value |
|-----------|-------|
| Unique endpoints | **2** |
| Min / max / mean of endpoints | see JSON |

**Interpretation:** After fixed depth 539, large free seeds **collapse hard** under Canonical T3 (very few distinct endpoints in this sample). That supports the architectural statement that **bare \(T^{539}\) is highly contracting** — and therefore collision resistance of the public hash must rest on the **SHA3 sandwich**, not on injectivity of a single branch.

### 2.4 Residue hit rates (539 steps × 200 large seeds)

| Residue | Empirical rate |
|---------|----------------|
| 0 | ≈ **0.125** |
| 1 | ≈ **0.437** |
| 2 | ≈ **0.438** |

Not a uniform \(1/3\) mix. Residual analysis and diffusion arguments should use measured kernels, not an assumed balanced residue process.

### 2.5 Structural checks

| Check | Result |
|-------|--------|
| \(T(1)=2\), \(T(2)=1\) | Confirmed |
| \(T(0)=0\) | Confirmed |
| r1 → 4q+2 injective on 20 000 q | Confirmed |
| Goldens / unit tests | Green (separate engineering freeze) |

---

## 3. Residual claims status after stress

| Claim class | Status after this run |
|-------------|------------------------|
| Canonical T3 closed form + integrality | **Category A — solid** |
| Small-seed pure-map steps ≪ 539 | **Category A — measured** |
| Strong contraction after fixed 539 on large seeds | **Category A — empirical sample** |
| Uniform 539-step physical termination / brane clock | **Category B — not supported by pure-map census** |
| Security reduction of HQH-539 | **Open — pending peer review** |

---

## 4. Reproduce

```bash
python3 explore_residue1_4q2.py
python3 -m unittest test_hqh539 test_profiles
python3 stress_test_long_orbits.py
```

---

## 5. Non-claims

- Not a Collatz-style convergence proof for unrestricted heights.  
- Not a proof of preimage/collision resistance.  
- Not validation of 11D continuum or mirror-sector notes.  
- Residual-flux provenance remains mandatory for any continuum application of these numbers.

*Per aspera ad astra.*  
— 539 Labs LLC / Arvin B. Hampton — 2026-08-02
