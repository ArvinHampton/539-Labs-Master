# HQH-539 verification status (2026-07-30)

## Suites

| Suite | Result |
|-------|--------|
| REF goldens + profiles | PASS |
| Expanded KATs | PASS |
| AE roundtrip (KDF + ChaCha20-Poly1305 + package) | PASS (44 tests total with prior) |
| RTL vector cross-check | **PASS** |

## RTL finding

`539-Labs-repo` vectors under `rtl_vectors/` match **PRODUCT_T4121**:

- Map: T4121 `(4n+1)//3` on residue 1  
- Finalize: 32-byte BE state ‖ `SALT_STD` ‖ `b":HQH-539-RESONANT:"`  
- **Not** engine REF (Canonical T3, empty domain, min-length finalize)

Canonical T3 deliberately mismatches those files (expected). See `DUAL_PROFILES.md`.

## Security framing

Implementation checks only. Hardness remains computationally infeasible with known methods, pending peer review of the full reduction.
