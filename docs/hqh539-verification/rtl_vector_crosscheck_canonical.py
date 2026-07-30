#!/usr/bin/env python3
"""Cross-check rtl_vectors_canonical/ under Option A (Canonical T3)."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from hqh539 import DOMAIN_SEP, STEPS, iterate_n_steps, hqh_539_512
from profiles import hqh_539_512_p32

ROOT = Path(__file__).resolve().parent
VEC = ROOT / "rtl_vectors_canonical"
OUT = ROOT / "rtl_crosscheck_canonical_results.json"
SALT_STD = b"539-LABS-2026-RESONANT-SALT"


def load_pairs(stim: str, exp: str):
    s, e = {}, {}
    for line in (VEC / stim).read_text().splitlines():
        if not line.strip():
            continue
        i, h = line.split(",", 1)
        s[int(i)] = h.strip().lower()
    for line in (VEC / exp).read_text().splitlines():
        if not line.strip():
            continue
        i, h = line.split(",", 1)
        e[int(i)] = h.strip().lower()
    return s, e


def main() -> int:
    if not VEC.is_dir():
        print("missing", VEC, file=sys.stderr)
        return 1

    # t3core
    stim, exp = load_pairs("stimulus_t3core.dat", "expected_t3core.dat")
    t3_ok = t3_fail = 0
    for i in stim:
        state = iterate_n_steps(int(stim[i], 16), STEPS)
        if f"{state:0256x}" == exp[i]:
            t3_ok += 1
        else:
            t3_fail += 1

    # pipeline REF
    stim_p, exp_ref = load_pairs("stimulus_pipeline.dat", "expected_pipeline_ref.dat")
    _, exp_p32 = load_pairs("stimulus_pipeline.dat", "expected_pipeline_p32.dat")
    ref_ok = p32_ok = seed_ok = 0
    for i in stim_p:
        msg = f"Resonant test vector {i} for 539 Labs - STD mode".encode()
        seed = int.from_bytes(hashlib.sha3_512(msg + SALT_STD).digest(), "big")
        if f"{seed:0128x}" == stim_p[i]:
            seed_ok += 1
        if hqh_539_512(msg, SALT_STD) == exp_ref[i]:
            ref_ok += 1
        if hqh_539_512_p32(msg, SALT_STD) == exp_p32[i]:
            p32_ok += 1

    # phase3
    stim_ph, exp_ph = load_pairs("stimulus_phase3_p32.dat", "expected_phase3_p32.dat")
    ph_ok = ph_fail = 0
    for i in stim_ph:
        sb = bytes.fromhex(stim_ph[i])
        got = hashlib.sha3_512(sb + SALT_STD + DOMAIN_SEP).hexdigest()
        if got == exp_ph[i]:
            ph_ok += 1
        else:
            ph_fail += 1

    n = len(stim)
    results = {
        "profile": "CANONICAL_OPTION_A",
        "t3core": {"pass": t3_ok, "fail": t3_fail, "n": n},
        "pipeline_ref": {"pass": ref_ok, "fail": n - ref_ok, "n": n},
        "pipeline_p32": {"pass": p32_ok, "fail": n - p32_ok, "n": n},
        "seeds": {"pass": seed_ok, "fail": n - seed_ok},
        "phase3_p32": {"pass": ph_ok, "fail": ph_fail, "n": len(stim_ph)},
        "overall": (
            "PASS"
            if t3_fail == 0
            and ref_ok == n
            and p32_ok == n
            and seed_ok == n
            and ph_fail == 0
            else "FAIL"
        ),
        "rfc": "RFC_Profile_Freeze_Option_A.md",
    }
    OUT.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))
    return 0 if results["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
