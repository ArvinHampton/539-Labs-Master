# FREEZE LOCK — Canonical 4q+2 + SHA3 sandwich (2026-08-02)

**Status:** LOCKED for peer review and product claims  
**Profile:** Option A / REF (see `RFC_Profile_Freeze_Option_A.md`)  
**Repos:** `hqh539-engine` (implementation), mirrored in `539-Labs-Master/docs/hqh539-verification/`

---

## 1. What is frozen (engineering)

| Element | Locked value | Source of truth |
|---------|--------------|-----------------|
| Map | **Canonical T3** | `hqh539.py::T3` |
| Residue-0 | \(n \mapsto n//3\) | code + KATs |
| Residue-1 | \(n=3q+1 \mapsto (4n+2)//3 = 4q+2\) | code + `Architecture_Residue1_4q2_Map.md` + `explore_residue1_4q2.py` |
| Residue-2 | \(n \mapsto (2n+1)//3\) | code + KATs |
| Depth | Exactly **539** as **18 + 521** | `STEPS`, `PREFIX_ROUNDS`, `SUFFIX_ROUNDS` |
| Seed wrap | `SHA3-512(message ‖ salt)` → big-endian int | `hqh_539` |
| Finalize (REF) | `SHA3-512(min-bytes fingerprint ‖ salt ‖ DOMAIN_SEP)` with `DOMAIN_SEP=b""` | `hqh_539` |
| Primary goldens | `golden_vectors.json` profile **REF** | tests green 2026-08-02 |

**T4121 is not the product primitive.** Historical only.

---

## 2. Residue-1 lock (4q+2)

Verified 2026-08-02:

- Exact integrality: \((4n+2) \equiv 0 \pmod{3}\) on all residue-1 inputs.
- Identity \(T(n)=4q+2\) for \(n=3q+1\) (1000+ q sample in `explore_residue1_4q2.py`).
- Always \(T_{\mathrm{Canonical}}(n) = T_{\mathrm{T4121}}(n)+1\) on residue-1.
- Image always \(\equiv 2 \pmod{4}\).
- Cycle \(1 \leftrightarrow 2\) (not fixed point at 1).
- r1 branch injective on sample of 20 000 q values (stress suite).

RTL sketch (normative for Option A silicon):

```text
q, r = divmod(n, 3)
if r == 0: y = q
if r == 1: y = (q << 2) + 2   // 4q+2
if r == 2: y = (q << 1) | 1   // 2q+1
```

---

## 3. SHA3 sandwich (review package)

Authoritative architecture note: `Architecture_SHA3_Sandwich.md`.

**Locked framing for reviewers:**

1. Bare Canonical \(T^{539}\) **contracts** free integer seeds (see long-orbit stress results).  
2. Collision resistance of HQH-539 **must not** be claimed from r1 injectivity or bare \(T\) alone.  
3. Public primitive is the **full sandwich**: SHA3-512 seed → 539×T3 → SHA3-512 finalize.  
4. Documented collision-path classes (C1–C4) are structural analysis, **not** a completed reduction.  
5. Empirical mid-state observations live in `sha3_sandwich_analysis_results.json` / collision notes — regenerate only with scripted tooling; do not hand-edit claims.

---

## 4. Verification evidence (this lock date)

| Check | Result |
|-------|--------|
| `python3 explore_residue1_4q2.py` | PASS |
| `python3 -m unittest test_hqh539 test_profiles` | 13 OK |
| REF goldens match live `hqh539.py` | PASS |
| Long-orbit stress suite | `long_orbit_stress_results_2026-08-02.json` |

Canonical KAT messages (REF):

| Key | Input | Role |
|-----|-------|------|
| empty | `b""` | empty message |
| canonical | `"The universe counts in threes."` | primary string KAT |
| large_int | `str(10**18)` | large integer encoding |
| salted | message + `b"hqh539-2026"` | salt sensitivity |

---

## 5. Hardness language (mandatory, unchanged)

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

Do **not** say “unbreakable”, “provably secure”, or “information-theoretic” for the public hash.

---

## 6. Explicit non-claims

- No completed classical/quantum security reduction.  
- No claim that pure-map orbits are uniformly length 539 (stress data show small seeds reach 1 far faster; 539 is the **hash packaging depth**, not a measured pure-map stopping time for free seeds).  
- No continuum / brane-clock claim in this freeze.  
- P32 and historical T4121 digests are **not interchangeable** with REF.

---

## 7. Companion artefacts

| Path | Role |
|------|------|
| `Architecture_Residue1_4q2_Map.md` | Algebra of 4q+2 |
| `Architecture_SHA3_Sandwich.md` | Sandwich structure |
| `Architecture_Collision_4q2.md` | Collision portrait |
| `RFC_Profile_Freeze_Option_A.md` | Profile law |
| `rtl_vectors_canonical/` | Canonical RTL KATs |
| `stress_test_long_orbits.py` | Pure-map stress harness |
| `long_orbit_stress_results_2026-08-02.json` | Stress output |

*Per aspera ad astra.*  
— 539 Labs LLC / Arvin B. Hampton — 2026-08-02
