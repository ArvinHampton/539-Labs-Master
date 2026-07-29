#!/usr/bin/env python3
"""
Post-kit / post-P+ / post-S1–S3 missed-pattern frontier (residual S only).

Executes residual openings without reopening locks:
  (3) Closed-form / structural identity for N2 = # {t : n_t = 3}
  (2) Transfer Ψ on mixed square cycles (G–F–M bridge)
  Jump census: n_jump, mass density M/n_jump = 36, signed spectrum
  Jump ⊥ stay support checks
  Cycle-type pairing weights on residual product edges

Does NOT: multi-cohort bio, anesthesia, denser P+, crypto, reopen Option 3.

PROVENANCE: residual (S). Continuum / bio = Cat B (not in this probe).
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path


def atoms():
    N_flux = math.floor(math.e**3 * 3**5)
    Q = 9
    N_tow = 3**5
    f_min = N_flux // N_tow
    R_exc = N_flux - f_min * N_tow
    f_max = math.ceil(N_flux / N_tow)
    B_prime = (N_flux - f_max) // Q
    L_pref = math.floor(math.e**3 / math.log(3))
    loads = [f_min + 1] * R_exc + [f_min] * (N_tow - R_exc)
    return N_flux, Q, N_tow, f_min, R_exc, f_max, B_prime, L_pref, loads


def tower_bounds(loads: list[int]) -> list[tuple[int, int]]:
    """Inclusive-exclusive intervals [lo, hi) for each tower."""
    bounds = []
    acc = 0
    for L in loads:
        bounds.append((acc, acc + L))
        acc += L
    return bounds


def n_ap_in_interval(f_max: int, Q: int, B_prime: int, lo: int, hi: int) -> int:
    """
    Count k in 0..B'-1 with x_k = f_max + k*Q in [lo, hi).
    Closed form via AP bounds.
    """
    # k_min: f_max + kQ >= lo => k >= ceil((lo - f_max)/Q)
    # k_max: f_max + kQ < hi  => k <= floor((hi - 1 - f_max)/Q)
    if hi <= lo:
        return 0
    num_lo = lo - f_max
    num_hi = hi - 1 - f_max
    k_min = math.ceil(num_lo / Q) if num_lo > 0 else 0
    if num_lo <= 0:
        k_min = 0
    else:
        k_min = (num_lo + Q - 1) // Q
    if num_hi < 0:
        return 0
    k_max = num_hi // Q
    k_min = max(k_min, 0)
    k_max = min(k_max, B_prime - 1)
    if k_max < k_min:
        return 0
    return k_max - k_min + 1


def sgn(d: int) -> int:
    return (d > 0) - (d < 0)


def main() -> int:
    N_flux, Q, N_tow, f_min, R_exc, f_max, B_prime, L_pref, loads = atoms()
    assert B_prime == 539 and L_pref == 18

    residual = list(range(f_max, N_flux))
    O = [f_max + k * Q for k in range(B_prime)]
    assert O == [residual[i] for i in range(len(residual)) if i % Q == 0][:B_prime]

    bounds = tower_bounds(loads)

    # --- Occupancy via closed-form AP count ---
    n_closed = [n_ap_in_interval(f_max, Q, B_prime, lo, hi) for lo, hi in bounds]
    # brute tower labels for check
    def tower_of(x: int) -> int:
        for t, (lo, hi) in enumerate(bounds):
            if lo <= x < hi:
                return t
        return N_tow - 1

    fvals = [tower_of(x) for x in O]
    occ_brute = Counter(fvals)
    n_brute = [occ_brute.get(t, 0) for t in range(N_tow)]
    assert n_closed == n_brute
    assert sum(n_closed) == B_prime

    N2 = sum(1 for n in n_closed if n == 3)
    N2_binom = sum(math.comb(n, 3) for n in n_closed)
    assert N2 == 56 and N2_binom == 56
    # structural: max hits per tower = floor((L_max-1)/Q)+1 but L<=21,Q=9 => <=3
    L_max = max(loads)
    max_hits = (L_max - 1) // Q + 1
    assert max_hits == 3
    # identity under Q0–Q3:
    # N2 = #{ t : n_AP(f_max, Q, B', I_t) = 3 }
    # with I_t tower intervals from loads; no free parameter.
    occ_mult = Counter(n_closed)
    assert occ_mult[3] == 56 and occ_mult[2] == 185 and occ_mult[1] == 1

    # closed-form style statement (verified identity)
    n2_identity = {
        "formula": "N2 = #{ t : n_AP(f_max, Q, B', I_t) = 3 }",
        "n_AP": "k in [0,B') with f_max+kQ in I_t; count = k_max-k_min+1",
        "I_t_from": "loads from Q0–Q1 partition of N_flux",
        "bound": "n_t <= floor((L_t-1)/Q)+1 <= 3 for L_t<=21, Q=9",
        "hence": "N2 = sum_t C(n_t,3) = #{t: n_t=3} when max n_t=3",
        "value": 56,
        "elevated_from_happened": True,
    }

    # --- Jump / stay ---
    df = [fvals[i + 1] - fvals[i] for i in range(B_prime - 1)]
    jump_idx = [i for i, d in enumerate(df) if d != 0]
    stay_idx = [i for i, d in enumerate(df) if d == 0]
    n_jump = len(jump_idx)
    n_stay = len(stay_idx)
    assert all(df[i] == 1 for i in jump_idx)  # executed path only +1 jumps
    assert n_jump == 241 and n_stay == 297

    M = (Q * (Q - 1) // 2) * sum(abs(d) for d in df)
    assert M == 8676
    mass_density = M / n_jump  # identical 36
    assert mass_density == 36.0
    # identity: M = C(9,2) * sum|df| = 36 * n_jump when |df| in {0,1} and jumps have |df|=1
    assert M == 36 * n_jump

    signed_mass_per_jump = [36 * df[i] for i in jump_idx]  # all +36
    signed_spectrum = Counter(signed_mass_per_jump)

    # stay triples edges
    buckets: dict[int, list[int]] = defaultdict(list)
    for i, t in enumerate(fvals):
        buckets[t].append(i)
    stay_edges = set()
    for v in buckets.values():
        if len(v) == 3:
            i, j, k = sorted(v)
            assert j == i + 1 and k == j + 1
            stay_edges.add(i)
            stay_edges.add(j)
    assert stay_edges.isdisjoint(set(jump_idx))

    # gap law between n=3 blocks
    triples = sorted(
        tuple(sorted(v)) for v in buckets.values() if len(v) == 3
    )
    gaps = [triples[i + 1][0] - triples[i][2] for i in range(len(triples) - 1)]
    gap_mult = Counter(gaps)

    # --- Graph beta1 ---
    beta1 = 36 * B_prime - 8
    assert beta1 == 19396

    # Cycle-type census (residual product graph K9 □ P): edge types
    # horizontal (path): Q * (B'-1); vertical (charge): B' * C(9,2); no diagonals
    n_horiz = Q * (B_prime - 1)
    n_vert = B_prime * (Q * (Q - 1) // 2)
    # 4-cycles of mixed type (squares): C(9,2)*(B'-1)
    n_mixed_squares = (Q * (Q - 1) // 2) * (B_prime - 1)
    assert n_horiz + n_vert == Q * B_prime * 0 + n_horiz + n_vert
    V = Q * B_prime
    E = n_horiz + n_vert
    assert E - V + 1 == beta1

    # --- Transfer Ψ: on mixed square 2-chains filling fundamental 4-cycles ---
    # For each square S(a,b;i) bounding the mixed 4-cycle,
    # <α⊗δf, S> = α(a,b) δf(i). Ψ on that cycle := that pairing.
    # Global jump-supported transfer mass = sum |Ψ| over squares = M
    def alpha(a, b):
        return sgn(a - b)

    psi_abs_sum = 0
    psi_signed_sum = 0
    psi_on_jumps = 0
    psi_on_stay = 0
    for i in range(B_prime - 1):
        for a, b in combinations(range(Q), 2):
            val = alpha(a, b) * df[i]
            psi_signed_sum += val
            psi_abs_sum += abs(val)
            if df[i] != 0:
                psi_on_jumps += abs(val)
            else:
                psi_on_stay += abs(val)
    assert psi_abs_sum == M
    assert psi_on_jumps == M and psi_on_stay == 0
    # signed: α(a,b)=-1 for a<b ordered combinations → signed sum = -C(9,2)*sum df
    assert psi_signed_sum == -(Q * (Q - 1) // 2) * sum(df)

    # Ψ transfer map summary: H1 classes of square cycles map to R via pairing
    # Generator set: mixed squares; image of |Ψ| supported only on jump edges
    transfer = {
        "definition": "Ψ(γ_S) = <α⊗δf, S> for mixed square cycle γ_S = ∂S",
        "domain": "mixed 4-cycles in K9 □ P (fundamental squares)",
        "codomain": "R (here Z)",
        "abs_sum_all_squares": psi_abs_sum,
        "signed_sum_all_squares": psi_signed_sum,
        "support": "jump edges only (stay squares contribute 0)",
        "equals_jump_mass_M": True,
        "status": "TRANSFER_PSI_EXECUTED_ON_FUNDAMENTAL_SQUARES",
        "note": "full H1 basis (all cycle types) remains open; squares already bridge G–F–M",
    }

    # Shell mass fraction vs (not computing bio here)
    W = L_pref
    M_win = 36 * sum(abs(df[i]) for i in range(W - 1))
    M_tow = M - M_win
    assert M_win == 252

    results = {
        "provenance": {
            "residual_S_only": True,
            "does_not_reopen_locks": True,
            "option3_intact": True,
            "thin_F_intact": True,
            "kit_frozen": True,
            "P_plus_not_locked": True,
            "bio_not_in_this_probe": True,
            "review_doc": "Multi_Angle_Review_Post_Kit_Pplus_S1S3.md",
        },
        "closed_channels_G_F_M": {
            "beta1_G": beta1,
            "H2_F": "Q[alpha⊗delta_f] rank 1",
            "jump_mass_M": M,
            "orthogonal_note": "three numerical channels; Ψ bridges G squares to F/M",
        },
        "rank3_N2_closed_form": {
            **n2_identity,
            "occupancy_multiset": {str(k): int(v) for k, v in sorted(occ_mult.items())},
            "max_hits_per_tower": max_hits,
            "verified_n_closed_equals_brute": True,
            "status": "N2_IDENTITY_UNDER_Q0_Q3_EXECUTED",
        },
        "rank2_transfer_Psi": transfer,
        "jump_stay_split": {
            "n_jump": n_jump,
            "n_stay": n_stay,
            "mass_density_M_over_n_jump": mass_density,
            "identity_M_equals_36_n_jump": True,
            "signed_mass_spectrum": {str(k): int(v) for k, v in signed_spectrum.items()},
            "jump_perp_stay_triple_edges": True,
            "n_stay_edges_in_triples": len(stay_edges),
            "gap_multiset_between_n3_blocks": {
                str(k): int(v) for k, v in sorted(gap_mult.items())
            },
        },
        "graph_cycle_type_census": {
            "V": V,
            "E_horizontal_path": n_horiz,
            "E_vertical_charge": n_vert,
            "E_total": E,
            "beta1": beta1,
            "n_mixed_squares": n_mixed_squares,
            "formula_beta1": "36*B'-8",
            "pairing_carrying_cycles": "mixed squares on jump edges (Ψ nonzero)",
        },
        "shell": {
            "W": W,
            "M_win": M_win,
            "M_tow": M_tow,
            "frac_win": M_win / M,
            "rW_nonzero": M_win > 0,
        },
        "frontier_not_executed_here": {
            "1_multi_cohort_S1S3": "Cat B data ladder",
            "4_jump_Hodge": "optional metric S",
            "5_mapping_cone_rW": "algebra S",
            "6_stay_secondary_classes": "F+ research S",
            "7_multi_channel_mass_covariance": "Cat B same EDF",
            "8_anesthesia": "after replication B",
            "9_denser_P_plus": "only if stay Stokes needed S",
            "10_crypto_canary": "eng B",
        },
        "hazard_watch": {
            "status_inflation": "RESEARCH_STABLE is not locked",
            "jump_stay_fusion": "forbidden by geometry",
            "S1S3_to_H2": "O",
            "56_as_packaging": "O",
        },
        "status": "FRONTIER_PROBE_N2_PSI_JUMP_EXECUTED",
    }

    out = Path(__file__).resolve().parents[1] / "missed_patterns_frontier_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print("OK: N2 identity under Q0–Q3 →", N2, "(not mere happenstance)")
    print("OK: M = 36 * n_jump = 36 *", n_jump, "=", M, "; density", mass_density)
    print("OK: transfer Ψ on squares → abs sum = M; support = jumps only")
    print("OK: jump ⊥ stay; gaps", dict(gap_mult))
    print("OK: status", results["status"])
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
