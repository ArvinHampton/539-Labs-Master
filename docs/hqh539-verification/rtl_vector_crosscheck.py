#!/usr/bin/env python3
"""
Cross-check 539-Labs-repo RTL test_vectors against engine T3 maps + finalize profiles.

Findings (2026-07-30):
  - stimulus/expected t3core + pipeline were generated with **T4121** map, not Canonical T3
  - Phase3 / pipeline finalize uses:
        SHA3-512( state.to_bytes(32, BE) || SALT_STD || DOMAIN_SEP )
    with SALT_STD = b"539-LABS-2026-RESONANT-SALT"
         DOMAIN_SEP = b":HQH-539-RESONANT:"   (product domain; engine REF uses b"")

Layers checked:
  SHA3      — hashlib (Category A)
  T3core    — T4121^539, 1024-bit pad (hardware Phase 2 vectors)
  T3core_C  — optional recompute under Canonical T3 (expect mismatch vs these files)
  Phase3    — 32-byte state + SALT + DOMAIN
  Pipeline  — e2e under T4121 + P32 + product domain

Not a security reduction.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from hqh539 import STEPS, T3, iterate_n_steps

ROOT = Path(__file__).resolve().parent
VEC = ROOT / "rtl_vectors"
OUT = ROOT / "rtl_crosscheck_results.json"

SALT_STD = b"539-LABS-2026-RESONANT-SALT"
DOMAIN_PRODUCT = b":HQH-539-RESONANT:"


def T4121(n: int) -> int:
    """Experimental map used by published RTL timing / historical vectors."""
    r = n % 3
    if r == 0:
        return n // 3
    if r == 1:
        return (4 * n + 1) // 3
    return (2 * n + 1) // 3


def iterate_map(n: int, steps: int, step_fn) -> int:
    state = n
    for _ in range(steps):
        state = step_fn(state)
    return state


def load_pairs(stim_name: str, exp_name: str):
    stim, exp = {}, {}
    for line in (VEC / stim_name).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, hexv = line.split(",", 1)
        stim[int(i)] = hexv.strip().lower()
    for line in (VEC / exp_name).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        i, hexv = line.split(",", 1)
        exp[int(i)] = hexv.strip().lower()
    return stim, exp


def load_sequential(stim_name: str, exp_name: str):
    def parse(line: str) -> str:
        line = line.strip()
        if "," in line and line.split(",", 1)[0].isdigit():
            return line.split(",", 1)[1].strip().lower()
        return line.lower()

    s = [parse(x) for x in (VEC / stim_name).read_text().splitlines() if x.strip()]
    e = [parse(x) for x in (VEC / exp_name).read_text().splitlines() if x.strip()]
    return s, e


def check_sha3() -> dict:
    stim, exp = load_sequential("stimulus_sha3.dat", "expected_sha3.dat")
    ok = fail = 0
    for s, e in zip(stim, exp):
        raw = bytes.fromhex(s)
        got = hashlib.sha3_512(raw).hexdigest()
        if got == e:
            ok += 1
        else:
            fail += 1
    return {"layer": "SHA3-512_standalone", "n": len(stim), "pass": ok, "fail": fail, "category": "A"}


def check_t3core(map_name: str, step_fn) -> dict:
    stim, exp = load_pairs("stimulus_t3core.dat", "expected_t3core.dat")
    ok = fail = 0
    bit_max = 0
    samples = []
    for i in sorted(stim):
        seed = int(stim[i], 16)
        state = iterate_map(seed, STEPS, step_fn)
        bit_max = max(bit_max, state.bit_length())
        got = f"{state:0256x}"
        if got == exp[i]:
            ok += 1
        else:
            fail += 1
            if len(samples) < 3:
                samples.append({"i": i, "bits": state.bit_length(), "got_tail": got[-32:], "exp_tail": exp[i][-32:]})
    return {
        "layer": f"T3core_{map_name}",
        "n": len(stim),
        "pass": ok,
        "fail": fail,
        "max_state_bits": bit_max,
        "samples_fail": samples,
        "category": "A_map_plus_fixed_steps",
    }


def check_phase3() -> dict:
    stim, exp = load_pairs("stimulus_phase3.dat", "expected_phase3.dat")
    ok = fail = 0
    for i in sorted(stim):
        sb = bytes.fromhex(stim[i])
        if len(sb) < 32:
            sb = sb.rjust(32, b"\x00")
        elif len(sb) > 32:
            sb = sb[-32:]
        got = hashlib.sha3_512(sb + SALT_STD + DOMAIN_PRODUCT).hexdigest()
        if got == exp[i]:
            ok += 1
        else:
            fail += 1
    return {
        "layer": "Phase3_product_domain",
        "n": len(stim),
        "pass": ok,
        "fail": fail,
        "salt": SALT_STD.decode(),
        "domain_sep": DOMAIN_PRODUCT.decode(),
        "finalize": "SHA3-512(state_32be || SALT_STD || DOMAIN_PRODUCT)",
        "category": "A_wrapper",
    }


def check_pipeline() -> dict:
    stim, exp = load_pairs("stimulus_pipeline.dat", "expected_pipeline.dat")
    ok_seed = 0
    match = {"T4121_p32_product": 0, "canon_p32_product": 0, "canon_ref_empty_domain": 0}
    for i in sorted(stim):
        msg = f"Resonant test vector {i} for 539 Labs - STD mode".encode("utf-8")
        seed_live = int.from_bytes(hashlib.sha3_512(msg + SALT_STD).digest(), "big")
        if seed_live == int(stim[i], 16):
            ok_seed += 1
        # T4121 product
        st = iterate_map(int(stim[i], 16), STEPS, T4121)
        try:
            sb = st.to_bytes(32, "big")
        except OverflowError:
            sb = (st & ((1 << 256) - 1)).to_bytes(32, "big")
        if hashlib.sha3_512(sb + SALT_STD + DOMAIN_PRODUCT).hexdigest() == exp[i]:
            match["T4121_p32_product"] += 1
        # Canonical + product domain
        stc = iterate_map(int(stim[i], 16), STEPS, T3)
        try:
            sbc = stc.to_bytes(32, "big")
        except OverflowError:
            sbc = (stc & ((1 << 256) - 1)).to_bytes(32, "big")
        if hashlib.sha3_512(sbc + SALT_STD + DOMAIN_PRODUCT).hexdigest() == exp[i]:
            match["canon_p32_product"] += 1
        # Canonical REF-style min finalize + empty domain + salt in seed only
        nb = max(1, (stc.bit_length() + 7) // 8)
        if (
            hashlib.sha3_512(stc.to_bytes(nb, "big") + SALT_STD).hexdigest() == exp[i]
        ):
            match["canon_ref_empty_domain"] += 1

    n = len(stim)
    if match["T4121_p32_product"] == n:
        profile = "PRODUCT_T4121_P32_DOMAIN"
    elif match["canon_p32_product"] == n:
        profile = "PRODUCT_CANON_P32_DOMAIN"
    else:
        profile = "UNKNOWN_OR_MIXED"
    return {
        "layer": "Pipeline_e2e",
        "n": n,
        "seed_match": {"pass": ok_seed, "fail": n - ok_seed},
        "digest_matches": match,
        "inferred_profile": profile,
        "note": (
            "Repo pipeline vectors match T4121 + 32-byte finalize + "
            "SALT_STD + DOMAIN b':HQH-539-RESONANT:'. "
            "They do NOT match engine REF (Canonical T3, empty DOMAIN_SEP, min-length finalize)."
        ),
        "category": "engineering_crosscheck",
    }


def main() -> int:
    if not VEC.is_dir():
        print("Missing rtl_vectors/", file=sys.stderr)
        return 1

    t4121 = check_t3core("T4121", T4121)
    canon = check_t3core("Canonical", T3)
    results = {
        "status": "RTL_VECTOR_CROSSCHECK",
        "vector_source": "539-Labs-repo/test_vectors (mirrored under rtl_vectors/)",
        "sha3": check_sha3(),
        "t3core_T4121": t4121,
        "t3core_Canonical_expect_mismatch": canon,
        "phase3": check_phase3(),
        "pipeline": check_pipeline(),
        "profile_map": {
            "REF_engine": "Canonical T3 + min-length finalize + DOMAIN_SEP=b''",
            "P32_engine": "Canonical T3 + 32-byte finalize + DOMAIN_SEP=b''",
            "PRODUCT_RTL_vectors": "T4121 + 32-byte finalize + DOMAIN b':HQH-539-RESONANT:' + SALT_STD",
        },
        "security_framing": (
            "Implementation/RTL consistency only. Not a security reduction. "
            "Hardness: computationally infeasible with known methods, pending peer review."
        ),
    }
    gates = {
        "sha3_pass": results["sha3"]["fail"] == 0,
        "t3core_T4121_pass": t4121["fail"] == 0 and t4121["pass"] > 0,
        "phase3_pass": results["phase3"]["fail"] == 0,
        "pipeline_T4121_product_pass": results["pipeline"]["digest_matches"]["T4121_p32_product"]
        == results["pipeline"]["n"],
        "canonical_differs_from_vector_files": canon["fail"] > 0,
    }
    results["gates"] = gates
    results["overall"] = (
        "PASS"
        if all(
            [
                gates["sha3_pass"],
                gates["t3core_T4121_pass"],
                gates["phase3_pass"],
                gates["pipeline_T4121_product_pass"],
            ]
        )
        else "FAIL"
    )
    OUT.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))
    print("wrote", OUT)
    return 0 if results["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
