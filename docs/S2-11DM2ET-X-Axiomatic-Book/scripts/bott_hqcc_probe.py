#!/usr/bin/env python3
"""
Computational probes for Bott ↔ HQCC link research (E1–E2).

E1: residue-word orbits under length shift by 8 (Bott period arithmetic).
E2: T^sharp path transitions on Z/27Z; cyclic covers / period-8 statistics.

Does NOT claim a completed link. No use of 539 as an input to definitions.
539 appears only in post-hoc comparison of arithmetic identities.

Usage:
  python bott_hqcc_probe.py
"""
from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np


def T_sharp(n: int) -> int:
    if n <= 0:
        return 0
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 2) // 3
    # charge completion
    def T_corr(k):
        return (n + 1) // 3 + 2 * (3**k)

    def preserve_k():
        t = n % 9
        for k in range(5):
            if T_corr(k) % 9 == t:
                return k
        return None

    def defect(k):
        d = abs(T_corr(k) % 9 - n % 9)
        return min(d, 9 - d)

    mk = preserve_k()
    if mk is not None:
        return T_corr(mk)
    k = min(range(3), key=lambda j: (defect(j), j))
    return T_corr(k)


def arithmetic_bott_hints() -> dict:
    return {
        "539_mod_8": 539 % 8,
        "539_eq_8*67+3": 8 * 67 + 3,
        "520_eq_8*65": 8 * 65,
        "4880_eq_8*610": 8 * 610,
        "243_mod_8": 243 % 8,
        "243_eq_8*30+3": 8 * 30 + 3,
        "61_mod_8": 61 % 8,
        "18_eq_8*2+2": 8 * 2 + 2,
        "pi_k_O_mod8": {
            0: "Z2",
            1: "Z2",
            2: "0",
            3: "Z",
            4: "0",
            5: "0",
            6: "0",
            7: "Z",
        },
        "note": "539≡3 (mod 8) aligns with pi_3(O)=Z line; free Z/8 action on 539 classes impossible",
    }


def E1_residue_words(max_len: int = 16) -> dict:
    """
    Words over alphabet {0,1,2} (residues).
    Orbit under cyclic shift of length by +8 is not a group action on words of fixed length;
    instead: partition words by length mod 8 and by total sum mod 9 (charge toy).
    Count how many words of length L have sum ≡ 0 mod 9 (toy charge-preserving words).
    """
    # count words of length L with sum residues ≡ c mod 9
    # generating function (1 + x*g + x^2*g^2)^L with g^9=1 — use DP
    by_L = {}
    for L in range(0, max_len + 1):
        # dp[j][s] = number of length-j words with sum ≡ s mod 9
        dp = [0] * 9
        dp[0] = 1
        for _ in range(L):
            ndp = [0] * 9
            for s in range(9):
                if dp[s] == 0:
                    continue
                for r in (0, 1, 2):
                    ndp[(s + r) % 9] += dp[s]
            dp = ndp
        by_L[L] = {
            "total": 3**L,
            "sum_mod9": {str(s): dp[s] for s in range(9)},
            "charge0_frac": dp[0] / (3**L) if L > 0 or True else 1.0,
            "L_mod8": L % 8,
        }

    # period-8 pattern in charge-0 counts
    charge0 = [by_L[L]["sum_mod9"]["0"] for L in range(max_len + 1)]
    return {
        "max_len": max_len,
        "charge0_counts_by_L": charge0,
        "charge0_by_L_mod8": {
            str(m): [charge0[L] for L in range(max_len + 1) if L % 8 == m]
            for m in range(8)
        },
        "note": "Toy charge: sum of residues mod 9; not full HQCC Q along T^sharp",
    }


def E2_Tsharp_mod27(n_paths: int = 5000, path_len: int = 64, seed: int = 0) -> dict:
    """
    Sample T^sharp trajectories; record residue sequences mod 27 and 3.
    Study return times mod 8 (Bott arithmetic on discrete time).
    """
    rng = np.random.default_rng(seed)
    starts = rng.integers(10**6, 10**12, size=n_paths, dtype=np.int64)
    # also seeds 20, 21, 243, 4880
    starts = np.concatenate([np.array([20, 21, 243, 4880], dtype=np.int64), starts])

    trans27 = Counter()
    res3_hist = Counter()
    # for each path, times t where n_t mod 3 == 0; look at gaps mod 8
    gaps_mod8 = Counter()
    first_return_mod8 = Counter()

    for s in starts:
        n = int(s)
        residues3 = []
        residues27 = []
        for t in range(path_len):
            residues3.append(n % 3)
            residues27.append(n % 27)
            res3_hist[n % 3] += 1
            n2 = T_sharp(n)
            trans27[(n % 27, n2 % 27)] += 1
            n = n2
        # gaps between consecutive visits to residue 0 mod 3
        times0 = [t for t, r in enumerate(residues3) if r == 0]
        for i in range(1, len(times0)):
            gap = times0[i] - times0[i - 1]
            gaps_mod8[gap % 8] += 1
        if len(times0) >= 2:
            first_return_mod8[(times0[1] - times0[0]) % 8] += 1

    total_gaps = sum(gaps_mod8.values()) or 1
    return {
        "n_paths": len(starts),
        "path_len": path_len,
        "residue3_histogram": {str(k): v for k, v in sorted(res3_hist.items())},
        "residue3_fractions": {
            str(k): v / sum(res3_hist.values()) for k, v in sorted(res3_hist.items())
        },
        "gaps_between_res0_mod8": {
            str(k): gaps_mod8[k] / total_gaps for k in range(8)
        },
        "n_transitions_mod27": len(trans27),
        "top_transitions_mod27": [
            {"from": a, "to": b, "count": c}
            for (a, b), c in trans27.most_common(15)
        ],
        "note": "If Bott time-periodicity dominated returns, gaps mod 8 would be peaked; flat ≈ mixing without period-8 preference",
    }


def E4_path_generating_sketch(max_L: int = 24) -> dict:
    """
    Count T^sharp orbits from seed set that stay charge-feasible longer —
    simplified: count sequences of (n mod 27) of length L under deterministic
    large-n asymptotics is multi-valued; use sampled empirical adjacency.
    """
    # Build empirical adjacency on Z/27 from many steps
    rng = np.random.default_rng(1)
    adj = defaultdict(Counter)
    for s in rng.integers(10**7, 10**12, size=2000):
        n = int(s)
        for _ in range(40):
            n2 = T_sharp(n)
            adj[n % 27][n2 % 27] += 1
            n = n2
    # normalize to stochastic matrix
    P = np.zeros((27, 27))
    for i in range(27):
        tot = sum(adj[i].values()) or 1
        for j, c in adj[i].items():
            P[i, j] = c / tot
    # number of walks of length L averaged — use sum of P^L
    counts = []
    M = np.eye(27)
    for L in range(0, max_L + 1):
        counts.append(float(M.sum()))
        M = M @ P
    # period-8 Fourier of walk-mass sequence
    arr = np.array(counts[1:], dtype=np.float64)  # L=1..max_L
    # mean by L mod 8
    by_m = {m: [] for m in range(8)}
    for L, v in enumerate(arr, start=1):
        by_m[L % 8].append(v)
    return {
        "walk_mass_by_L": counts,
        "mean_walk_mass_by_L_mod8": {str(m): float(np.mean(by_m[m])) if by_m[m] else None for m in range(8)},
        "note": "Empirical walk mass on Z/27; period-8 modulation would show in means by L mod 8",
    }


def main() -> None:
    report = {
        "arithmetic_bott_hints": arithmetic_bott_hints(),
        "E1_residue_words": E1_residue_words(16),
        "E2_Tsharp_mod27": E2_Tsharp_mod27(3000, 64, seed=42),
        "E4_walk_mass": E4_path_generating_sketch(24),
        "programme": "See Bott_HQCC_Link_Research.md Phases 0–4; this is probe only",
        "no_claim": "Does not establish Bott embedding or derive 539 from Bott",
    }

    out = Path(__file__).resolve().parent.parent / "bott_hqcc_probe_results.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("=" * 64)
    print("BOTT ↔ HQCC LINK PROBES (Category B research)")
    print("=" * 64)
    h = report["arithmetic_bott_hints"]
    print("Arithmetic:")
    print(f"  539 = 8*67 + 3  (mod 8 = {h['539_mod_8']})  [pi_3(O)=Z line]")
    print(f"  520 = 8*65,  4880 = 8*610,  243 = 8*30 + 3")
    print(f"  Free Z/8 action on 539 classes: impossible (8 does not divide 539)")
    print()
    e2 = report["E2_Tsharp_mod27"]
    print("E2: residue-3 fractions along T^sharp paths:")
    print(" ", e2["residue3_fractions"])
    print("E2: gaps between res≡0 visits, distribution mod 8:")
    print(" ", {k: f"{v:.3f}" for k, v in e2["gaps_between_res0_mod8"].items()})
    print()
    e4 = report["E4_walk_mass"]
    print("E4: mean walk mass by L mod 8 (empirical Z/27):")
    print(" ", e4["mean_walk_mass_by_L_mod8"])
    print()
    print("Next: Phase 0 formal definition of space C with |pi_0|=539 claimed.")
    print(f"Wrote {out}")
    print("=" * 64)


if __name__ == "__main__":
    main()
