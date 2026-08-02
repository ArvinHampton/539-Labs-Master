# Peer-review brief — Category A only (2026-08-02)

**Audience:** Independent mathematical / cryptographic reviewers  
**Scope:** What 539 Labs currently asserts as **Category A** (checkable math, code, and measurements)  
**Out of scope:** Continuum physics, dual-universe / mirror biology, brane-clock security reductions (Category B)

**Author:** Arvin B. Hampton, 539 Labs LLC  
**Primary code:** [hqh539-engine](https://github.com/ArvinHampton/hqh539-engine)  
**Primary corpus:** [539-Labs-Master](https://github.com/ArvinHampton/539-Labs-Master)

---

## Executive statement

HQH-539 is a **fixed-depth ternary map wrapped in SHA3-512**. The residual discrete algebra and the reference implementation are ready for line-by-line checking. **No completed security reduction is claimed.** Continuum and physical-clock narratives are explicitly **not** part of this Category A package.

Hardness language (only form allowed in this brief):

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

---

## A1. The map (normative)

Canonical T3 (Option A, frozen):

\[
T(n)=\begin{cases}
n/3 & n\equiv 0\pmod{3}\\
(4n+2)/3 = 4q+2 & n=3q+1\\
(2n+1)/3 & n\equiv 2\pmod{3}
\end{cases}
\]

**Checkable facts:**

1. Residue-1 branch is exactly \(4q+2\) with no floor error.  
2. On residue-1, Canonical and T4121 always differ by \(+1\).  
3. \(T(1)=2\), \(T(2)=1\) (2-cycle; avoids T4121’s fixed point at 1).  
4. Implementation: `hqh539.py::T3` matches the formulas above.

**Historical:** T4121 is **not** the product primitive.

---

## A2. The hash packaging (normative)

\[
\mathrm{HQH\text{-}539\text{-}512}(m,s)
=
\mathrm{SHA3\text{-}512}\big(\mathrm{bytes}(T^{539}(\mathrm{int}(\mathrm{SHA3\text{-}512}(m\|s)))) \,\|\, s \,\|\, \varepsilon\big)
\]

with fixed depth **539 = 18 + 521**, and REF finalize using minimal big-endian byte length of the fingerprint (`DOMAIN_SEP = ε`).

**Checkable facts:**

1. Unit tests and `golden_vectors.json` (profile REF) match live code.  
2. REF and P32 digests are **not interchangeable**.  
3. Salt changes the digest (tested).

---

## A3. Pure-map measurements (2026-08-02 stress)

Under **Canonical T3 only**:

| Measurement | Result |
|-------------|--------|
| Steps-to-1 for all \(n\in[1,50\,000]\) | Max **55**, mean **≈22** (none require 539) |
| Seed 20 / 21 / 4880 steps-to-1 | 5 / 6 / **14** |
| 2000 large seeds after exactly 539 steps | Only **2** distinct endpoints in sample |
| Residue rates along 539-step large trajectories | ≈ 0.125 / 0.437 / 0.438 for r0/r1/r2 |
| r1 injectivity (20 000 q sample) | Holds |

**Reviewer takeaway:** 539 is the **hash’s fixed depth**, not a pure-map universal stopping time for free small seeds. Strong contraction after 539 steps on large seeds is empirical Category A; it **cuts against** resting CR on bare \(T\) alone.

---

## A4. SHA3 sandwich (structural Category A)

Documented in `Architecture_SHA3_Sandwich.md` and companion collision notes:

- Public primitive = **seed SHA3 → 539×T3 → finalize SHA3**.  
- Bare \(T^{539}\) is highly contracting on free seeds (A3).  
- r1 injectivity is **not** a CR proof.  
- Collision-path taxonomy (C1–C4) is structural analysis pending formal reduction.

---

## A5. What is **not** Category A (do not review as proven)

| Topic | Label |
|-------|--------|
| Physical 539.9 s brane-leakage clock as security oracle | Category B |
| Uniform 539-step termination of “physical” seeds / 243-tower averaging | Category B |
| Mirror Galaxy / FMO / biophoton / consciousness extensions | Category B |
| Completed reduction to a standard hard problem | **Open** |
| Any absolute “unbreakable” marketing | **Forbidden** |

HQCC theorem materials that use a **charge-preserving** residual map distinct from product Canonical T3 must be reviewed under **that** formulation; do not equate its 4880 orbit with Canonical T3’s 14-step orbit without a written isomorphism.

---

## A6. Minimal review checklist

1. Verify `T3` against §A1 for 1000 random \(n\).  
2. Re-run `python3 -m unittest test_hqh539 test_profiles`.  
3. Re-run `python3 explore_residue1_4q2.py` and `python3 stress_test_long_orbits.py`.  
4. Confirm REF digests for empty / canonical string / large int / salted.  
5. Confirm the hardness sentence is the only security claim in public materials under review.  
6. Reject any continuum claim that lacks residual-flux provenance and Cat B labeling.

---

## A7. Deliverables package (this date)

| Artefact | Location |
|----------|----------|
| Freeze lock | `FREEZE_LOCK_Canonical_4q2_SHA3_2026-08-02.md` |
| Math stress report | `MATH_Long_Orbit_Stress_Report_2026-08-02.md` |
| Stress JSON | `long_orbit_stress_results_2026-08-02.json` |
| Stress harness | `stress_test_long_orbits.py` |
| This brief | `docs/CatA_Peer_Review_Brief_2026-08-02.md` |
| Map architecture | `Architecture_Residue1_4q2_Map.md` |
| Sandwich architecture | `Architecture_SHA3_Sandwich.md` |
| Profile RFC | `RFC_Profile_Freeze_Option_A.md` |

---

## A8. Requested reviewer outcomes

1. Confirmation or counterexample to §A1–A3.  
2. Opinion on whether the sandwich framing (§A4) is correctly scoped (no reduction claimed).  
3. Optional: preferred path toward a **standard-model** reduction (Category A target), independent of continuum Category B.

*Per aspera ad astra.*  
— 539 Labs LLC / Arvin B. Hampton — 2026-08-02
