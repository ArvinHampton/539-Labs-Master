# HQH-539 verification package

Self-contained reference + KATs + avalanche + AE roundtrip + RTL vector cross-check.

## Security framing (mandatory)

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

KATs and RTL checks bind **implementation identity**, not hardness.

## Run

```bash
pip install cryptography
python3 run_kats.py
python3 -m unittest test_hqh539 test_profiles test_kats_expanded test_ae_roundtrip -v
python3 rtl_vector_crosscheck.py
python3 avalanche.py
python3 benchmark_vs_sha3.py
```

## Profiles

See [DUAL_PROFILES.md](DUAL_PROFILES.md).

| Profile | Use |
|---------|-----|
| REF | Canonical T3 + min-length finalize — engine KATs |
| P32 | Canonical T3 + 32-byte finalize |
| PRODUCT_T4121 | Historical RTL/repo vectors (T4121 + product domain) |
| LEGACY | Orphaned — do not use |
