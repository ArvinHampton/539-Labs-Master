# HQH-539 verification package

Self-contained reference + KATs + avalanche + benchmark vs SHA3-512.

## Security framing (mandatory)

> Proprietary framework claim (S²-11DM²ET-X) — not independently verified, pending external cryptanalysis. Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

No “provably secure” / “unbreakable” language. Avalanche and KATs are implementation checks, not hardness proofs.

## Layout

| File | Role |
|------|------|
| `hqh539.py` | Canonical reference (SHA3-512 → 539×T3 as 18+521 → SHA3-512) |
| `golden_vectors.json` | KATs |
| `run_kats.py` | unittest KATs |
| `avalanche.py` | bit-flip diffusion stats vs SHA3-512 |
| `benchmark_vs_sha3.py` | throughput comparison |
| `crypto_hqh.py` | KDF + ChaCha20-Poly1305 AE wrapper (optional dep: cryptography) |
| `constant_time_notes.md` | CT engineering notes |

## Run

```
python3 run_kats.py
python3 avalanche.py
python3 benchmark_vs_sha3.py
```

## Provenance

Round count 539 = packaging L_pack under Principle (S), not free T^sharp dynamics (Option 3 intact). Residual Architecture A through A5⁺ is foundation math, not a crypto reduction.
