#!/usr/bin/env python3
"""
Phase 0 refined: basins / terminal orbits of physical seeds under T^sharp.

Sigma_243:  one seed per tower (243 seeds). Bound: N_basins <= 243 < 539.
Sigma_4880: one seed per flux quantum (20*21+223*20=4880). Bound: N_basins <= 4880.

No insertion of 539 into seed construction or dynamics.
Compare N_basins to 539 only post-hoc.

Usage:
  python phase0_seed_basins.py
  python phase0_seed_basins.py --package both --max-steps 5000
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def T_sharp(n: int) -> int:
    if n <= 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3

    def Tc(k: int) -> int:
        return (n + 1) // 3 + 2 * (3**k)

    t = n % 9
    for k in range(5):
        if Tc(k) % 9 == t:
            return Tc(k)

    def defect(k: int) -> int:
        d = abs(Tc(k) % 9 - t)
        return min(d, 9 - d)

    k = min(range(3), key=lambda j: (defect(j), j))
    return Tc(k)


def flux_assignment() -> list[int]:
    """f_tau: 20 towers with 21, 223 with 20."""
    return [21 if tau < 20 else 20 for tau in range(243)]


def seeds_S243() -> list[int]:
    f = flux_assignment()
    return [f[tau] * 243 + tau for tau in range(243)]


def seeds_S4880() -> list[int]:
    """One seed per flux unit: sum f_tau = 4880."""
    f = flux_assignment()
    out = []
    for tau in range(243):
        for j in range(f[tau]):
            out.append((f[tau] * 243 + tau) * 64 + j + 1)
    return out


# backward-compatible alias
def seeds_S5083() -> list[int]:
    return seeds_S4880()


def terminal_cycle(seed: int, max_steps: int) -> tuple[frozenset[int], int, bool]:
    """
    Returns (cycle_frozenset, steps_to_enter_cycle, hit_one).
    """
    seen: dict[int, int] = {}
    n = int(seed)
    for t in range(max_steps + 1):
        if n in seen:
            t0 = seen[n]
            # reconstruct cycle
            path_n = int(seed)
            for _ in range(t0):
                path_n = T_sharp(path_n)
            cyc = []
            start = path_n
            while True:
                cyc.append(path_n)
                path_n = T_sharp(path_n)
                if path_n == start:
                    break
                if len(cyc) > max_steps:
                    break
            return frozenset(cyc), t0, (1 in cyc or start == 1)
        seen[n] = t
        if n <= 1:
            return frozenset({n}), t, True
        n = T_sharp(n)
    # no cycle found — treat last state as pseudo-attractor singleton
    return frozenset({n}), max_steps, n <= 1


def cycle_key(cyc: frozenset[int]) -> str:
    if not cyc:
        return "empty"
    m = min(cyc)
    return f"min={m}|size={len(cyc)}|sum={sum(cyc)}"


def enumerate_basins(seeds: list[int], max_steps: int) -> dict:
    attractors: dict[str, frozenset[int]] = {}
    seed_to_attr: dict[int, str] = {}
    hit_one = 0
    steps_list = []
    cycle_lens = Counter()

    for s in seeds:
        cyc, t_enter, h1 = terminal_cycle(s, max_steps)
        key = cycle_key(cyc)
        attractors[key] = cyc
        seed_to_attr[s] = key
        if h1:
            hit_one += 1
        steps_list.append(t_enter)
        cycle_lens[len(cyc)] += 1

    n_basins = len(attractors)
    claimed = 539
    return {
        "n_seeds": len(seeds),
        "n_basins": n_basins,
        "n_hit_one_attractor": hit_one,
        "fraction_hit_one": hit_one / len(seeds) if seeds else 0.0,
        "steps_to_cycle": {
            "median": sorted(steps_list)[len(steps_list) // 2] if steps_list else None,
            "mean": sum(steps_list) / len(steps_list) if steps_list else None,
            "max": max(steps_list) if steps_list else None,
            "min": min(steps_list) if steps_list else None,
        },
        "cycle_length_histogram": {str(k): v for k, v in sorted(cycle_lens.items())},
        "attractor_keys_sample": list(attractors.keys())[:20],
        "post_hoc": {
            "claimed_539": claimed,
            "n_basins_equals_539": n_basins == claimed,
            "abs_diff": abs(n_basins - claimed),
            "n_basins_le_n_seeds": n_basins <= len(seeds),
            "S243_cardinality_bound_blocks_539": len(seeds) == 243 and claimed > 243,
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", choices=["S243", "S4880", "S5083", "both"], default="both")
    ap.add_argument("--max-steps", type=int, default=5000)
    args = ap.parse_args()

    report: dict = {
        "map": "T_sharp",
        "max_steps": args.max_steps,
        "flux_split": {"towers_21": 20, "towers_20": 223, "check_sum": 20 * 21 + 223 * 20},
        "definition": "C_seed = basins of physical seeds under T^sharp; 539 not an input",
    }
    assert report["flux_split"]["check_sum"] == 4880

    packages = []
    if args.package in ("S243", "both"):
        packages.append(("S243", seeds_S243()))
    if args.package in ("S4880", "S5083", "both"):
        packages.append(("S4880", seeds_S4880()))

    print("=" * 68)
    print("PHASE 0 REFINED — Seed-orbit basins under T^sharp")
    print("=" * 68)
    print("Flux: 20 towers x 21 + 223 towers x 20 = 4880")
    print(f"max_steps = {args.max_steps}")
    print()

    for name, seeds in packages:
        # uniqueness check
        assert len(seeds) == len(set(seeds)), f"{name} seeds not unique"
        res = enumerate_basins(seeds, args.max_steps)
        report[name] = {
            "seed_formula": (
                "s_tau = f_tau*243 + tau"
                if name == "S243"
                else "s_(tau,j) = (f_tau*243+tau)*64 + j + 1"
            ),
            "n_seeds_expected": 243 if name == "S243" else 4880,
            "n_seeds_actual": len(seeds),
            "seed_min": min(seeds),
            "seed_max": max(seeds),
            "basins": res,
        }
        print(f"--- {name} ---")
        print(f"  seeds = {len(seeds)} (unique)")
        print(f"  N_basins = {res['n_basins']}")
        print(f"  fraction attractor contains 1 = {res['fraction_hit_one']:.3f}")
        print(f"  steps-to-cycle median/mean/max = "
              f"{res['steps_to_cycle']['median']}/"
              f"{res['steps_to_cycle']['mean']:.1f}/"
              f"{res['steps_to_cycle']['max']}")
        print(f"  cycle length hist = {res['cycle_length_histogram']}")
        print(f"  post-hoc N_basins == 539? {res['post_hoc']['n_basins_equals_539']} "
              f"(diff {res['post_hoc']['abs_diff']})")
        if name == "S243":
            print("  note: |basins| <= 243 < 539 — S243 cannot realize H0 as basin count")
        print()

    print("--- Bott gate ---")
    s243_ok = report.get("S243", {}).get("basins", {}).get("post_hoc", {}).get("n_basins_equals_539")
    s4880_ok = report.get("S4880", {}).get("basins", {}).get("post_hoc", {}).get("n_basins_equals_539")
    if s243_ok or s4880_ok:
        print("  Count matched 539 → classifying map into BSpin/BO becomes legitimate next question.")
    else:
        print("  Count did NOT match 539 → do not force Bott link on this package; refine C or abandon H0 for basins.")
    print("=" * 68)

    out = Path(__file__).resolve().parent.parent / "phase0_seed_basins_results.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
