#!/usr/bin/env python3
"""
Category A stress tests: pure Canonical T3 (Option A / product map).

Does NOT claim physical 539-step termination or continuum HQCC.
Reports empirical orbit statistics under the frozen map only.
"""
from __future__ import annotations

import json
import random
import statistics
import time
from collections import Counter
from pathlib import Path

from hqh539 import STEPS, T3, iterate_n_steps

OUT = Path(__file__).resolve().parent / "long_orbit_stress_results_2026-08-02.json"
MAX_STEPS_SEARCH = 50_000


def steps_to_threshold(n: int, thr: int = 1, cap: int = MAX_STEPS_SEARCH) -> int | None:
    """Steps until n <= thr (or None if cap hit)."""
    if n <= thr:
        return 0
    x = n
    for s in range(1, cap + 1):
        x = T3(x)
        if x <= thr:
            return s
    return None


def residue_histogram(n: int, steps: int = STEPS) -> Counter:
    c: Counter = Counter()
    x = n
    for _ in range(steps):
        c[x % 3] += 1
        x = T3(x)
    return c


def endpoint_after_539(seeds: list[int]) -> dict:
    ends = [iterate_n_steps(s, STEPS) for s in seeds]
    return {
        "n": len(ends),
        "min": min(ends),
        "max": max(ends),
        "mean": float(statistics.mean(ends)),
        "median": float(statistics.median(ends)),
        "unique_endpoints": len(set(ends)),
        "sample_endpoints": ends[:20],
    }


def main() -> None:
    t0 = time.time()
    rng = random.Random(539_2026)

    # --- Named seeds of framework interest ---
    named = {
        1: steps_to_threshold(1),
        2: steps_to_threshold(2),
        20: steps_to_threshold(20),
        21: steps_to_threshold(21),
        4880: steps_to_threshold(4880),
        10**6: steps_to_threshold(10**6),
        10**12: steps_to_threshold(10**12),
        10**18: steps_to_threshold(10**18),
    }
    named_539_end = {str(k): iterate_n_steps(k, STEPS) for k in named}

    # Trajectory of 4880 under Canonical T3 (product map — not HQCC charge map)
    traj_4880 = []
    x = 4880
    for i in range(40):
        traj_4880.append({"step": i, "n": x, "mod3": x % 3})
        x = T3(x)
        if x == 1 and i > 0:
            traj_4880.append({"step": i + 1, "n": x, "mod3": x % 3})
            break

    # --- Small-seed census: all n in [1, N] ---
    N = 50_000
    steps_list = []
    failed = 0
    for n in range(1, N + 1):
        s = steps_to_threshold(n)
        if s is None:
            failed += 1
        else:
            steps_list.append(s)
    census = {
        "range": f"1..{N}",
        "failed_cap": failed,
        "min_steps": min(steps_list) if steps_list else None,
        "max_steps": max(steps_list) if steps_list else None,
        "mean_steps": float(statistics.mean(steps_list)) if steps_list else None,
        "median_steps": float(statistics.median(steps_list)) if steps_list else None,
        "p95_steps": float(sorted(steps_list)[int(0.95 * (len(steps_list) - 1))]) if steps_list else None,
        "p99_steps": float(sorted(steps_list)[int(0.99 * (len(steps_list) - 1))]) if steps_list else None,
        "hist_buckets": dict(Counter((s // 10) * 10 for s in steps_list)),
    }

    # --- Random large seeds: endpoint after exactly 539 steps ---
    large_seeds = [rng.randrange(10**18, 10**36) for _ in range(2000)]
    ep = endpoint_after_539(large_seeds)

    # Residue mix along trajectories for 200 large seeds
    residue_mix = Counter()
    for s in large_seeds[:200]:
        residue_mix.update(residue_histogram(s, STEPS))
    total_r = sum(residue_mix.values()) or 1
    residue_rates = {str(k): residue_mix[k] / total_r for k in (0, 1, 2)}

    # --- r1 branch injectivity sample ---
    r1_injective = True
    seen_y = {}
    for q in range(0, 20_000):
        n = 3 * q + 1
        y = T3(n)
        assert y == 4 * q + 2
        if y in seen_y and seen_y[y] != n:
            r1_injective = False
            break
        seen_y[y] = n

    # --- Cycle check small ---
    assert T3(1) == 2 and T3(2) == 1
    assert T3(0) == 0

    report = {
        "date": "2026-08-02",
        "map": "Canonical T3 Option A: r0=n//3, r1=(4n+2)//3=4q+2, r2=(2n+1)//3",
        "category": "A (pure number-theoretic map statistics only)",
        "non_claims": [
            "No claim that physical seeds terminate in 539 steps",
            "No continuum / 11D / brane-clock claim",
            "No security reduction",
            "HQCC charge-preserving map in theorem note is a separate formulation; this file uses product Canonical T3 only",
        ],
        "named_steps_to_1": {str(k): v for k, v in named.items()},
        "named_after_exactly_539": named_539_end,
        "trajectory_4880_canonical_T3_prefix": traj_4880,
        "census_1_to_N": census,
        "large_seed_after_539": ep,
        "residue_rates_along_539": residue_rates,
        "r1_4q2_injective_sample_20k": r1_injective,
        "cycle_1_2": "confirmed",
        "elapsed_sec": round(time.time() - t0, 3),
    }

    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "wrote": str(OUT),
        "census_max_steps": census["max_steps"],
        "census_mean_steps": census["mean_steps"],
        "named_4880_steps_to_1": named[4880],
        "named_20_steps_to_1": named[20],
        "named_21_steps_to_1": named[21],
        "large_unique_endpoints_2000": ep["unique_endpoints"],
        "residue_rates": residue_rates,
        "r1_injective": r1_injective,
        "elapsed_sec": report["elapsed_sec"],
    }, indent=2))


if __name__ == "__main__":
    main()
