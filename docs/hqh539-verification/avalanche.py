#!/usr/bin/env python3
"""Avalanche statistics for HQH-539-512 vs SHA3-512 (engineering evidence only)."""
from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path

from hqh539 import hqh_539_512

OUT = Path(__file__).resolve().parent / "avalanche_results.json"


def bit_diff_hex(a: str, b: str) -> int:
    x = int(a, 16) ^ int(b, 16)
    return x.bit_count()


def avalanche_hqh(n_trials: int = 256, msg_len: int = 32, seed: int = 539) -> dict:
    rng = random.Random(seed)
    flips = []
    for _ in range(n_trials):
        msg = bytes(rng.getrandbits(8) for _ in range(msg_len))
        # flip one random bit
        bi = rng.randrange(msg_len * 8)
        b = bytearray(msg)
        b[bi // 8] ^= 1 << (bi % 8)
        d0 = hqh_539_512(bytes(msg))
        d1 = hqh_539_512(bytes(b))
        flips.append(bit_diff_hex(d0, d1) / 512.0)
    mean = sum(flips) / len(flips)
    return {
        "algorithm": "HQH-539-512",
        "n_trials": n_trials,
        "msg_len_bytes": msg_len,
        "mean_bit_flip_fraction": mean,
        "min": min(flips),
        "max": max(flips),
        "target_nominal": 0.5,
        "category": "B_engineering_evidence_only",
        "not_a_security_proof": True,
    }


def avalanche_sha3(n_trials: int = 256, msg_len: int = 32, seed: int = 539) -> dict:
    rng = random.Random(seed)
    flips = []
    for _ in range(n_trials):
        msg = bytes(rng.getrandbits(8) for _ in range(msg_len))
        bi = rng.randrange(msg_len * 8)
        b = bytearray(msg)
        b[bi // 8] ^= 1 << (bi % 8)
        d0 = hashlib.sha3_512(msg).hexdigest()
        d1 = hashlib.sha3_512(bytes(b)).hexdigest()
        flips.append(bit_diff_hex(d0, d1) / 512.0)
    mean = sum(flips) / len(flips)
    return {
        "algorithm": "SHA3-512",
        "n_trials": n_trials,
        "mean_bit_flip_fraction": mean,
        "min": min(flips),
        "max": max(flips),
        "category": "A_standard_primitive",
    }


def main() -> int:
    hqh = avalanche_hqh()
    sha = avalanche_sha3()
    out = {
        "hqh539": hqh,
        "sha3_512": sha,
        "framing": (
            "Avalanche is internal engineering evidence only. "
            "Not a security reduction. Hardness claims remain: computationally "
            "infeasible with known classical/quantum methods, pending peer review."
        ),
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
