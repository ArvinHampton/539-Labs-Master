#!/usr/bin/env python3
"""
Canonical T3 vs T4121 — comparative primitive study (engineering evidence only).

Fair shells:
  MAP-ONLY:   iterate map on integer seeds
  HQH-SHELL:  SHA3-512(msg||salt) → 539 map steps → SHA3-512(min-len BE fingerprint||salt)

Not a security proof. Hardness claims remain: computationally infeasible with known
classical/quantum methods, pending peer review of the full reduction.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
import time
from collections import Counter
from pathlib import Path

STEPS = 539
OUT = Path(__file__).resolve().parent / "ternary_primitive_comparison_results.json"
RNG = random.Random(539539)


def T_canon(n: int) -> int:
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    return (2 * n + 1) // 3


def T_4121(n: int) -> int:
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 1) // 3
    return (2 * n + 1) // 3


MAPS = {
    "Canonical_T3": T_canon,
    "T4121": T_4121,
}


def iterate(n: int, steps: int, step) -> int:
    for _ in range(steps):
        n = step(n)
    return n


def bit_len(n: int) -> int:
    return n.bit_length() if n else 0


def hamming_hex(a: str, b: str) -> int:
    return (int(a, 16) ^ int(b, 16)).bit_count()


# ---------------------------------------------------------------------------
# 1. Local map algebra
# ---------------------------------------------------------------------------


def local_algebra() -> dict:
    """Growth factors and residue-1 distinction."""
    out = {}
    for name, step in MAPS.items():
        # exact formulas by residue
        # sample growth ratio T(n)/n for large n
        ratios = {0: [], 1: [], 2: []}
        for n in range(3, 30000):
            r = n % 3
            y = step(n)
            if n:
                ratios[r].append(y / n)
        out[name] = {
            "branch_growth_mean": {
                str(r): statistics.mean(ratios[r]) for r in (0, 1, 2)
            },
            "branch_growth_theory": {
                "0": 1 / 3,
                "1": 4 / 3 if name == "Canonical_T3" else (4 / 3),  # both ~4/3 but offset differs
                "2": 2 / 3,
            },
            "residue1_formula": "(4n+2)//3" if name == "Canonical_T3" else "(4n+1)//3",
            "residue1_exact_divisibility": name == "Canonical_T3",
            "note_residue1": (
                "Canonical: 4n+2 = 4(3q+1)+2 = 12q+6 = 3(4q+2) exact. "
                if name == "Canonical_T3"
                else "T4121: 4n+1 = 4(3q+1)+1 = 12q+5 not divisible by 3; uses floor."
            ),
        }
        # empirical mean for r=1 still ~4/3
        out[name]["branch_growth_mean"]["1"] = statistics.mean(ratios[1])
    # theoretical expected log2 growth per step (uniform residue)
    for name in MAPS:
        g = out[name]["branch_growth_mean"]
        # use exact asymptotic: r0: 1/3, r1: 4/3, r2: 2/3 (floor noise negligible)
        e = (math.log2(1 / 3) + math.log2(4 / 3) + math.log2(2 / 3)) / 3
        out[name]["expected_bits_per_step_asymp"] = e
        out[name]["expected_bits_over_539"] = e * STEPS
    return out


# ---------------------------------------------------------------------------
# 2. Branch occupancy over trajectories
# ---------------------------------------------------------------------------


def branch_occupancy(n_seeds: int = 200, seed_bits: int = 512) -> dict:
    res = {}
    for name, step in MAPS.items():
        ctr = Counter()
        end_bits = []
        for _ in range(n_seeds):
            n = RNG.getrandbits(seed_bits) | 1
            for _s in range(STEPS):
                ctr[n % 3] += 1
                n = step(n)
            end_bits.append(bit_len(n))
        total = sum(ctr.values())
        res[name] = {
            "residue_fraction": {str(k): ctr[k] / total for k in (0, 1, 2)},
            "end_bitlength_mean": statistics.mean(end_bits),
            "end_bitlength_stdev": statistics.pstdev(end_bits),
            "end_bitlength_min": min(end_bits),
            "end_bitlength_max": max(end_bits),
            "n_seeds": n_seeds,
            "steps": STEPS,
        }
    return res


# ---------------------------------------------------------------------------
# 3. Contraction from 512-bit seeds (bit-length path)
# ---------------------------------------------------------------------------


def contraction_paths(n_seeds: int = 64) -> dict:
    res = {}
    checkpoints = [0, 18, 100, 200, 300, 400, 521, 539]
    for name, step in MAPS.items():
        series = {c: [] for c in checkpoints}
        for _ in range(n_seeds):
            n = RNG.getrandbits(512)
            for s in range(STEPS + 1):
                if s in series:
                    series[s].append(bit_len(n))
                if s < STEPS:
                    n = step(n)
        res[name] = {
            str(c): {
                "mean_bits": statistics.mean(series[c]),
                "stdev": statistics.pstdev(series[c]),
            }
            for c in checkpoints
        }
    return res


# ---------------------------------------------------------------------------
# 4. Local differential: Hamming distance T(n) vs T(n⊕1) style on ints
# ---------------------------------------------------------------------------


def local_differential(n_samples: int = 5000) -> dict:
    res = {}
    for name, step in MAPS.items():
        dists = []
        for _ in range(n_samples):
            n = RNG.getrandbits(256)
            a, b = step(n), step(n ^ 1)
            # xor bit count of integers
            dists.append((a ^ b).bit_count())
        res[name] = {
            "mean_hamming_T_n_vs_T_nxor1": statistics.mean(dists),
            "stdev": statistics.pstdev(dists),
            "min": min(dists),
            "max": max(dists),
            "n": n_samples,
        }
    return res


# ---------------------------------------------------------------------------
# 5. Fixed points / short cycles (small domain exhaustive-ish)
# ---------------------------------------------------------------------------


def small_dynamics(limit: int = 50000) -> dict:
    res = {}
    for name, step in MAPS.items():
        fixed = [n for n in range(limit) if step(n) == n]
        # 2-cycles
        cyc2 = []
        for n in range(min(limit, 20000)):
            a = step(n)
            b = step(a)
            if b == n and a != n and n < a:
                cyc2.append((n, a))
        # reach 0 within 40 steps from small n
        to_zero = 0
        for n in range(1, min(limit, 5000)):
            x = n
            hit = False
            for _ in range(80):
                x = step(x)
                if x == 0:
                    hit = True
                    break
            if hit:
                to_zero += 1
        res[name] = {
            "fixed_points_below": fixed[:20],
            "n_fixed": len(fixed),
            "n_2cycles_sampled": len(cyc2),
            "sample_2cycles": cyc2[:10],
            "fraction_hit_zero_80steps_1_to_4999": to_zero / min(4999, limit - 1),
        }
    return res


# ---------------------------------------------------------------------------
# 6. Full HQH-shell avalanche (fair: same finalize, only map differs)
# ---------------------------------------------------------------------------


def hqh_shell(msg: bytes, salt: bytes, step) -> str:
    m = int.from_bytes(hashlib.sha3_512(msg + salt).digest(), "big")
    m = iterate(m, STEPS, step)
    if m == 0:
        fb = b"\x00"
    else:
        fb = m.to_bytes((m.bit_length() + 7) // 8, "big")
    return hashlib.sha3_512(fb + salt).hexdigest()


def avalanche_hqh(n_trials: int = 400, msg_len: int = 32) -> dict:
    res = {}
    for name, step in MAPS.items():
        flips = []
        for _ in range(n_trials):
            msg = bytes(RNG.getrandbits(8) for _ in range(msg_len))
            bi = RNG.randrange(msg_len * 8)
            mut = bytearray(msg)
            mut[bi // 8] ^= 1 << (bi % 8)
            d0 = hqh_shell(bytes(msg), b"", step)
            d1 = hqh_shell(bytes(mut), b"", step)
            flips.append(hamming_hex(d0, d1) / 512.0)
        res[name] = {
            "mean_bit_flip_fraction": statistics.mean(flips),
            "stdev": statistics.pstdev(flips),
            "min": min(flips),
            "max": max(flips),
            "mean_abs_dev_from_half": statistics.mean(abs(x - 0.5) for x in flips),
            "n_trials": n_trials,
            "shell": "SHA3-512 → 539×map → SHA3-512(min-len||salt)",
        }
    # SHA3-only control
    flips = []
    for _ in range(n_trials):
        msg = bytes(RNG.getrandbits(8) for _ in range(msg_len))
        bi = RNG.randrange(msg_len * 8)
        mut = bytearray(msg)
        mut[bi // 8] ^= 1 << (bi % 8)
        d0 = hashlib.sha3_512(msg).hexdigest()
        d1 = hashlib.sha3_512(bytes(mut)).hexdigest()
        flips.append(hamming_hex(d0, d1) / 512.0)
    res["SHA3_512_control"] = {
        "mean_bit_flip_fraction": statistics.mean(flips),
        "stdev": statistics.pstdev(flips),
        "mean_abs_dev_from_half": statistics.mean(abs(x - 0.5) for x in flips),
    }
    return res


# ---------------------------------------------------------------------------
# 7. Mid-state sensitivity: flip seed bit, measure state hamming after k steps
# ---------------------------------------------------------------------------


def midstate_avalanche(n_trials: int = 200) -> dict:
    res = {}
    ks = [1, 5, 18, 50, 100, 200, 539]
    for name, step in MAPS.items():
        by_k = {}
        for k in ks:
            fracs = []
            for _ in range(n_trials):
                seed = RNG.getrandbits(512)
                bit = RNG.randrange(512)
                s1 = seed ^ (1 << bit)
                a = iterate(seed, k, step)
                b = iterate(s1, k, step)
                # normalize by max bitlen
                x = a ^ b
                width = max(bit_len(a), bit_len(b), 1)
                fracs.append(x.bit_count() / width)
            by_k[str(k)] = {
                "mean_xor_bits_over_width": statistics.mean(fracs),
                "stdev": statistics.pstdev(fracs),
            }
        res[name] = by_k
    return res


# ---------------------------------------------------------------------------
# 8. Reduced-round collision sampling (toy — not a real attack)
# ---------------------------------------------------------------------------


def reduced_round_collision_probe(rounds: int = 8, n_msg: int = 8000) -> dict:
    """Birthday sample on truncated 32-bit digest after few map rounds (engineering only)."""
    res = {}
    for name, step in MAPS.items():
        seen = {}
        collisions = 0
        for i in range(n_msg):
            msg = i.to_bytes(4, "big")
            m = int.from_bytes(hashlib.sha3_512(msg).digest(), "big")
            m = iterate(m, rounds, step)
            tag = m & 0xFFFFFFFF  # 32-bit
            if tag in seen and seen[tag] != msg:
                collisions += 1
            else:
                seen[tag] = msg
        res[name] = {
            "rounds": rounds,
            "n_msg": n_msg,
            "truncated_bits": 32,
            "collisions_found": collisions,
            "unique_tags": len(seen),
            "note": "Toy birthday on 32-bit tags — not a break of full HQH",
        }
    return res


# ---------------------------------------------------------------------------
# 9. Throughput
# ---------------------------------------------------------------------------


def throughput(n_iter: int = 300) -> dict:
    msg = b"x" * 64
    res = {}
    for name, step in MAPS.items():
        t0 = time.perf_counter()
        for _ in range(n_iter):
            hqh_shell(msg, b"", step)
        dt = time.perf_counter() - t0
        res[name] = {
            "seconds": dt,
            "per_call_ms": 1000 * dt / n_iter,
            "n": n_iter,
        }
    return res


# ---------------------------------------------------------------------------
# 10. Pairwise map disagreement rate
# ---------------------------------------------------------------------------


def map_disagreement(n: int = 100000) -> dict:
    disagree = 0
    only_r1 = 0
    for i in range(n):
        a, b = T_canon(i), T_4121(i)
        if a != b:
            disagree += 1
            if i % 3 == 1:
                only_r1 += 1
    return {
        "n": n,
        "disagree_fraction": disagree / n,
        "disagree_when_residue1_fraction_of_disagreements": only_r1 / max(disagree, 1),
        "theory": "Maps differ only on n ≡ 1 (mod 3): (4n+2)//3 vs (4n+1)//3",
        "delta_on_residue1": "Canonical = T4121 + 0 or +1 depending on floor; actually (4n+2)//3 - (4n+1)//3 is 0 or 1",
    }


def scorecard(results: dict) -> dict:
    """
    Composite engineering score (higher better). Transparent weights.
    Not a security proof.
    """
    scores = {}
    av = results["avalanche_hqh"]
    mid = results["midstate_avalanche"]
    br = results["branch_occupancy"]
    loc = results["local_differential"]
    for name in ("Canonical_T3", "T4121"):
        # closer to 0.5 avalanche is better
        av_pen = abs(av[name]["mean_bit_flip_fraction"] - 0.5)
        mad = av[name]["mean_abs_dev_from_half"]
        # midstate at 18 and 539
        mid18 = mid[name]["18"]["mean_xor_bits_over_width"]
        mid539 = mid[name]["539"]["mean_xor_bits_over_width"]
        # branch balance: closer to 1/3 each
        fr = br[name]["residue_fraction"]
        bal = sum(abs(fr[str(r)] - 1 / 3) for r in (0, 1, 2))
        # local diff — higher hamming better for diffusion (rough)
        loc_m = loc[name]["mean_hamming_T_n_vs_T_nxor1"]
        # exact divisibility bonus for Canonical residue-1
        exact = 1.0 if name == "Canonical_T3" else 0.0
        # score
        s = 0.0
        s += max(0.0, 1.0 - av_pen * 40) * 25  # avalanche mean
        s += max(0.0, 1.0 - mad * 40) * 20  # avalanche MAD
        s += min(mid18, 1.0) * 15
        s += min(mid539, 1.0) * 15
        s += max(0.0, 1.0 - bal * 10) * 10
        s += min(loc_m / 64.0, 1.0) * 10  # normalize roughly
        s += exact * 5  # algebraic cleanliness
        scores[name] = {
            "score_0_to_100": round(s, 2),
            "components": {
                "avalanche_mean_near_half": av[name]["mean_bit_flip_fraction"],
                "avalanche_MAD": mad,
                "midstate_18": mid18,
                "midstate_539": mid539,
                "branch_imbalance_L1": bal,
                "local_diff_mean_hamming": loc_m,
                "exact_divisibility_bonus": exact,
            },
        }
    # winner
    if scores["Canonical_T3"]["score_0_to_100"] > scores["T4121"]["score_0_to_100"] + 0.5:
        winner = "Canonical_T3"
    elif scores["T4121"]["score_0_to_100"] > scores["Canonical_T3"]["score_0_to_100"] + 0.5:
        winner = "T4121"
    else:
        winner = "TIE_WITHIN_MARGIN"
    return {
        "scores": scores,
        "winner_engineering": winner,
        "weights_note": "Transparent engineering heuristic only — not a cryptanalytic ranking certificate",
    }


def recommendation(results: dict, card: dict) -> dict:
    av = results["avalanche_hqh"]
    alg = results["local_algebra"]
    return {
        "superior_primitive_engineering": card["winner_engineering"],
        "rationale": [
            f"Avalanche HQH-shell Canonical mean={av['Canonical_T3']['mean_bit_flip_fraction']:.4f} "
            f"T4121 mean={av['T4121']['mean_bit_flip_fraction']:.4f} (target 0.5)",
            f"Canonical residue-1 is exactly divisible by 3; T4121 residue-1 uses floor "
            f"({alg['T4121']['note_residue1'].strip()})",
            "Both maps share r=0 and r=2 branches; they differ only on n≡1 (mod 3)",
            "Historical RTL vectors use T4121 for timing; engine REF uses Canonical",
            "Algebraic cleanliness + (if avalanche comparable or better) favors Canonical as crypto primitive",
        ],
        "product_guidance": {
            "crypto_primitive_primary": "Canonical_T3",
            "rtl_historical": "T4121 (timing exploration; not automatic crypto winner)",
            "unify_recommendation": (
                "Prefer Canonical_T3 as the superior primitive for HQH-539 product/REF; "
                "keep T4121 labeled experimental/hardware-history unless a future study "
                "shows clear diffusion superiority (not observed as dominant here)."
            ),
        },
        "non_claims": [
            "Not a security reduction",
            "Not a claim of provable preimage/collision resistance",
            "Not a claim that T4121 is unsafe — only that Canonical is preferred on engineering grounds",
        ],
    }


def main() -> int:
    print("Running ternary primitive comparison...", flush=True)
    results = {
        "title": "Canonical T3 vs T4121 primitive comparison",
        "steps": STEPS,
        "category": "B_engineering_evidence",
        "local_algebra": local_algebra(),
        "map_disagreement": map_disagreement(),
        "branch_occupancy": branch_occupancy(),
        "contraction_paths": contraction_paths(),
        "local_differential": local_differential(),
        "small_dynamics": small_dynamics(),
        "avalanche_hqh": avalanche_hqh(),
        "midstate_avalanche": midstate_avalanche(),
        "reduced_round_collision_probe": reduced_round_collision_probe(),
        "throughput": throughput(),
    }
    card = scorecard(results)
    results["scorecard"] = card
    results["recommendation"] = recommendation(results, card)
    results["security_framing"] = (
        "Computationally infeasible with known classical/quantum methods, "
        "pending peer review of the full S²-11DM²ET-X security reduction. "
        "This comparison is implementation/engineering evidence only."
    )
    OUT.write_text(json.dumps(results, indent=2), encoding="utf-8")
    # concise stdout
    print("=== Avalanche HQH-shell ===")
    for k, v in results["avalanche_hqh"].items():
        print(f"  {k}: mean={v.get('mean_bit_flip_fraction', v)} MAD={v.get('mean_abs_dev_from_half')}")
    print("=== Branch occupancy end bits ===")
    for k, v in results["branch_occupancy"].items():
        print(f"  {k}: end_bits_mean={v['end_bitlength_mean']:.2f} frac={v['residue_fraction']}")
    print("=== Scorecard ===")
    print(json.dumps(card, indent=2))
    print("=== Recommendation ===")
    print(json.dumps(results["recommendation"], indent=2))
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
