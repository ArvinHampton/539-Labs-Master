#!/usr/bin/env python3
"""Throughput comparison HQH-539-512 vs SHA3-512 (engineering only)."""
from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

from hqh539 import hqh_539_512

OUT = Path(__file__).resolve().parent / "benchmark_results.json"


def bench(fn, msg: bytes, n: int) -> float:
    t0 = time.perf_counter()
    for _ in range(n):
        fn(msg)
    return time.perf_counter() - t0


def main() -> int:
    msg = b"x" * 1024
    n = 200
    t_hqh = bench(lambda m: hqh_539_512(m), msg, n)
    t_sha = bench(lambda m: hashlib.sha3_512(m).hexdigest(), msg, n)
    out = {
        "message_bytes": len(msg),
        "iterations": n,
        "hqh539_512_seconds": t_hqh,
        "sha3_512_seconds": t_sha,
        "hqh_per_call_ms": 1000 * t_hqh / n,
        "sha3_per_call_ms": 1000 * t_sha / n,
        "ratio_hqh_over_sha3": t_hqh / t_sha if t_sha else None,
        "note": "Not a security metric. Pending peer review of any hardness claims.",
        "category": "engineering",
    }
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
