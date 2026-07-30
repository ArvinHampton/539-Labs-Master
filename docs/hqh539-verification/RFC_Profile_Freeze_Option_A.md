# RFC: Profile Freeze — Option A (Canonical REF is law)

**Status:** ACCEPTED / FROZEN  
**Date:** 2026-07-30  
**Applies to:** HQH-539 product, engine KATs, KDF/AE, public primitive claims  
**Companions:** `DUAL_PROFILES.md`, `Architecture_Ternary_Primitive_Comparison.md`, `rtl_vector_crosscheck.py`

---

## 1. Decision

**Option A is frozen:**

> **Canonical T3 + engine REF finalize is the sole primary cryptographic primitive for HQH-539.**

| Field | Frozen value |
|-------|----------------|
| Map | **Canonical T3**: \(0\to n//3\), \(1\to(4n+2)//3\), \(2\to(2n+1)//3\) |
| Steps | Exactly **539** (packaging \(18+521\)) |
| Seed | `SHA3-512(message ‖ salt)` → big-endian integer |
| Finalize (REF) | `SHA3-512(fingerprint.to_bytes(⌈bitlen/8⌉, BE) ‖ salt ‖ DOMAIN_SEP)` |
| `DOMAIN_SEP` (engine REF) | `b""` |
| Primary KATs | `golden_vectors.json` (profile **REF**) |
| KDF / AE | `crypto_hqh.py` → REF only |

**T4121 is not the product primitive.** It remains a historical / experimental RTL artefact only.

---

## 2. What is demoted

| Profile / artefact | New status |
|--------------------|------------|
| PRODUCT_T4121 (`rtl_vectors/` from 539-Labs-repo) | **Historical** — timing / Kerckhoffs inspection; not ship target |
| P32 (Canonical + 32-byte finalize, empty domain) | **Optional compat shape** — not primary unless a future RFC elevates it |
| LEGACY orphan goldens | **Archived — do not use** |

Digests from historical T4121 vectors **must not** be compared to REF digests without an explicit profile tag.

---

## 3. Why A (one paragraph)

Comparative engineering (`compare_ternary_primitives.py`) preferred Canonical T3: exact residue-1 divisibility, cleaner fixed points, tighter contraction variance, avalanche MAD at least as good as T4121. T4121’s published win was FPGA timing, not diffusion dominance. Engine REF and crypto_hqh already ship Canonical. Freezing A removes specification fragmentation for peer review and product claims.

---

## 4. Normative rules (must)

1. Any public “HQH-539” digest without a profile tag **means REF / Canonical**.  
2. New unit tests and goldens bind **REF** only unless marked `profile=…`.  
3. New product RTL / software vectors **must** use Canonical T3.  
4. Historical T4121 files stay in-tree under a **historical** path or label; do not silently overwrite.  
5. Security marketing uses only the locked hardness sentence; freeze does **not** complete a reduction.

---

## 5. Hardness language (unchanged)

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

---

## 6. Follow-on work (bound by this freeze)

| ID | Work | Status |
|----|------|--------|
| A1 | This RFC | **Frozen** |
| A2 | Plan + generate **Canonical** RTL KATs | See `PLAN_Canonical_RTL_Revector.md` |
| A3 | Point 539-Labs-repo / future silicon at Canonical vectors | Planned |
| A4 | Optional: elevate P32 or product DOMAIN in a **new** RFC only | Not in this freeze |

---

## 7. Acceptance

| Check | Result |
|-------|--------|
| Engine `hqh539.py` is Canonical | Yes |
| REF goldens match live code | Yes |
| Primitive comparison prefers Canonical | Yes |
| Option A recorded in DUAL_PROFILES | Yes (this RFC) |

**RFC status: ACCEPTED.**

*Per aspera ad astra.*
