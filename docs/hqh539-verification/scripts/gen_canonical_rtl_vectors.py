#!/usr/bin/env python3
"""Generate Canonical-T3 RTL KATs under rtl_vectors_canonical/ (Option A freeze)."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from hqh539 import DOMAIN_SEP, STEPS, T3, hqh_539_512, iterate_n_steps  # noqa: E402
from profiles import hqh_539_512_p32  # noqa: E402

OUT = ROOT / "rtl_vectors_canonical"
SALT_STD = b"539-LABS-2026-RESONANT-SALT"
N_T3 = 100
N_PHASE3 = 20


def msg_i(i: int) -> bytes:
    return f"Resonant test vector {i} for 539 Labs - STD mode".encode("utf-8")


def seed_of(msg: bytes) -> int:
    return int.from_bytes(hashlib.sha3_512(msg + SALT_STD).digest(), "big")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    # --- t3core ---
    stim_t3, exp_t3 = [], []
    max_bits = 0
    for i in range(N_T3):
        seed = seed_of(msg_i(i))
        state = iterate_n_steps(seed, STEPS)  # Canonical via hqh539.T3
        max_bits = max(max_bits, state.bit_length())
        stim_t3.append(f"{i},{seed:0128x}\n")
        exp_t3.append(f"{i},{state:0256x}\n")
    (OUT / "stimulus_t3core.dat").write_text("".join(stim_t3), encoding="utf-8")
    (OUT / "expected_t3core.dat").write_text("".join(exp_t3), encoding="utf-8")

    # --- pipeline ---
    stim_p, exp_ref, exp_p32 = [], [], []
    for i in range(N_T3):
        msg = msg_i(i)
        seed = seed_of(msg)
        stim_p.append(f"{i},{seed:0128x}\n")
        exp_ref.append(f"{i},{hqh_539_512(msg, SALT_STD)}\n")
        exp_p32.append(f"{i},{hqh_539_512_p32(msg, SALT_STD)}\n")
    (OUT / "stimulus_pipeline.dat").write_text("".join(stim_p), encoding="utf-8")
    (OUT / "expected_pipeline_ref.dat").write_text("".join(exp_ref), encoding="utf-8")
    (OUT / "expected_pipeline_p32.dat").write_text("".join(exp_p32), encoding="utf-8")

    # --- phase3 P32 (from pipeline seeds, Canonical state → 32-byte → SHA3) ---
    stim_ph, exp_ph = [], []
    for i in range(N_PHASE3):
        seed = seed_of(msg_i(i))
        state = iterate_n_steps(seed, STEPS)
        sb = (state & ((1 << 256) - 1)).to_bytes(32, "big")
        digest = hashlib.sha3_512(sb + SALT_STD + DOMAIN_SEP).hexdigest()
        stim_ph.append(f"{i},{sb.hex()}\n")
        exp_ph.append(f"{i},{digest}\n")
    (OUT / "stimulus_phase3_p32.dat").write_text("".join(stim_ph), encoding="utf-8")
    (OUT / "expected_phase3_p32.dat").write_text("".join(exp_ph), encoding="utf-8")

    manifest = {
        "profile": "CANONICAL_PRODUCT_OPTION_A",
        "map": "Canonical_T3",
        "steps": STEPS,
        "domain_sep_ref": DOMAIN_SEP.decode("latin-1") if DOMAIN_SEP else "",
        "salt_std_for_seed": SALT_STD.decode(),
        "n_t3core": N_T3,
        "n_phase3": N_PHASE3,
        "max_state_bits_observed": max_bits,
        "files": {
            "stimulus_t3core.dat": "512-bit seeds",
            "expected_t3core.dat": "Canonical T3^539 → 1024-bit pad",
            "stimulus_pipeline.dat": "same seeds",
            "expected_pipeline_ref.dat": "engine REF hqh_539_512(msg, SALT_STD)",
            "expected_pipeline_p32.dat": "Canonical P32 finalize empty domain",
            "stimulus_phase3_p32.dat": "32-byte state after Canonical^539",
            "expected_phase3_p32.dat": "SHA3-512(state32||SALT_STD||DOMAIN_SEP)",
        },
        "historical_t4121_path": "rtl_vectors/",
        "rfc": "RFC_Profile_Freeze_Option_A.md",
    }
    (OUT / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
