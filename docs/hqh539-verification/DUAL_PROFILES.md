# HQH-539 digest profiles

**Date:** 2026-07-30  
**Repo:** hqh539-engine  

This document resolves golden-vector drift between the checked-in reference
implementation, product/deploy finalize paths, and an orphaned historical KAT file.

---

## Profiles

| ID | Name | Seed | T3 steps | Finalize | Status |
|----|------|------|----------|----------|--------|
| **REF** | Canonical reference | `SHA3-512(message ‖ salt)` → int BE | Exactly 539 (structured 18+521) | `SHA3-512(fingerprint.to_bytes(⌈bitlen/8⌉, BE) ‖ salt ‖ DOMAIN_SEP)` | **Active / KATs bind here** |
| **P32** | Product / deploy / demo | Same | Same 539 | `SHA3-512((fingerprint mod 2^256).to_bytes(32, BE) ‖ salt ‖ DOMAIN_SEP)` | Documented dual profile (539-Labs-repo deploy/demo) |
| **LEGACY** | Orphaned oracle digests | Unknown (file claimed `hqh539_independent_oracle.py`) | T3 oracle values still match | **No checked-in oracle reproduces digests** | Archived only — do not use for new products |

`DOMAIN_SEP` is currently `b""` in `hqh539.py`.

---

## Why digests differ

1. **REF vs P32:** variable-length minimal big-endian encoding of the integer fingerprint vs fixed 32-byte (256-bit) encoding of the low bits. Different SHA3-512 inputs ⇒ different digests.
2. **LEGACY vs REF:** historical `golden_vectors.json` claimed an independent oracle that is **not** present in this repository. Live `hqh539.py` does not reproduce those digests under any of the finalize variants re-checked (min-len, 32, 64, LE seed, masked 256-bit, etc.). Treated as **orphaned**, not a third supported API.

---

## Canonical choice (2026-07-30)

- **Ship and test against REF** (`hqh539.py` + `golden_vectors.json`).
- **Document P32** for FPGA/API paths that already use 32-byte state (`539-Labs-repo` deploy/demo). Do not mix P32 digests into REF KATs.
- **Do not resurrect LEGACY** as a product profile unless the independent oracle is recovered and re-validated.

---

## Files

| File | Role |
|------|------|
| `hqh539.py` | REF implementation |
| `golden_vectors.json` | REF KATs (aligned 2026-07-30) |
| `golden_vectors_legacy_orphaned.json` | archived LEGACY digests |
| `golden_vectors_p32.json` | P32 KATs for dual-profile tests |
| `profiles.py` | `hqh_539_512_ref` / `hqh_539_512_p32` helpers |
| `test_hqh539.py` | REF KATs |
| `test_profiles.py` | REF vs P32 separation tests |

---

## Security framing

KATs bind **implementation identity**, not hardness. Hardness remains:

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

No dual-profile claim is a security reduction.

---

## Migration

1. Consumers of old engine goldens must re-hash under REF (or explicitly opt into P32).
2. Cross-impl tests must load REF goldens only for REF modules.
3. Master verification package (`docs/hqh539-verification`) uses REF and matches this alignment.


---

## Product / RTL vector profile (2026-07-30 cross-check)

Historical vectors under `rtl_vectors/` (from `539-Labs-repo/test_vectors`) match:

| Piece | Value |
|-------|--------|
| Map | **T4121** (residue 1: `(4n+1)//3`) — not Canonical T3 |
| Steps | 539 |
| Finalize | `SHA3-512(state.to_bytes(32, BE) ‖ SALT_STD ‖ DOMAIN)` |
| SALT_STD | `b"539-LABS-2026-RESONANT-SALT"` |
| DOMAIN | `b":HQH-539-RESONANT:"` |

| ID | Notes |
|----|--------|
| **PRODUCT_T4121** | Matches t3core + pipeline KATs in repo vectors |
| **REF** | Production crypto primitive intent per engine README / Canonical T3 |
| **P32** | Canonical T3 + 32-byte finalize, empty domain (engine helper) |

**Do not mix** PRODUCT_T4121 digests with REF digests. RTL public timing work used T4121; engine REF remains Canonical unless explicitly re-pointed.

Run: `python3 rtl_vector_crosscheck.py`
