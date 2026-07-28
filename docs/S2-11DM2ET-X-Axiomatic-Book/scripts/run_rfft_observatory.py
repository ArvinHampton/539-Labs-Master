#!/usr/bin/env python3
"""
Free-first R-FFT-539.9 on **real** observatory series only.

Synthetics (pure_noise, pure_G4, multi_k_residual_placeholder, …) are rejected.

Examples
--------
  python run_rfft_observatory.py --list
  python run_rfft_observatory.py --status
  python run_rfft_observatory.py --fetch ligo_h1_strain_open
  python run_rfft_observatory.py --fetch nanograv_12p5yr_residuals
  python run_rfft_observatory.py --analyze ligo_h1_strain_open --decimate 16
  python run_rfft_observatory.py --analyze nanograv_12p5yr_residuals --uniform-dt 86400
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

# Allow running from scripts/ without installing a package
_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from observatory_data import (  # noqa: E402
    fetch_dataset,
    list_observatories,
    load_registry,
    load_series,
    stage_status,
)
from observatory_data.registry import DISMISSED_SYNTHETIC_IDS  # noqa: E402
from r_fft_5399 import full_r_fft_analysis, compare_precondition_modes  # noqa: E402


def cmd_list() -> int:
    reg = load_registry()
    print("Dismissed synthetic IDs (not loadable):")
    for s in sorted(DISMISSED_SYNTHETIC_IDS):
        print(f"  - {s}")
    print("\nObservatory registry (real facilities only):")
    for ds_id in list_observatories(reg):
        e = reg["observatories"][ds_id]
        print(f"  {ds_id}")
        print(f"      facility : {e.get('facility')}")
        print(f"      product  : {e.get('product')}")
        print(f"      portal   : {e.get('portal')}")
        print(f"      loader   : {e.get('loader')}")
    return 0


def cmd_status() -> int:
    st = stage_status()
    print(json.dumps(st, indent=2))
    return 0


def cmd_fetch(dataset_id: str, **kwargs) -> int:
    path = fetch_dataset(dataset_id, **kwargs)
    print(f"Staged: {path}")
    return 0


def cmd_analyze(
    dataset_id: str,
    *,
    decimate: int = 1,
    uniform_dt: float | None = None,
    n_null: int = 32,
    max_n: int | None = 200_000,
    compare: bool = True,
    json_out: Path | None = None,
    event: str | None = None,
    detector: str | None = None,
    pulsar: str | None = None,
    duration: float | None = None,
    edf: Path | None = None,
    channel: str | None = None,
    duration_s: float | None = None,
    start_s: float = 0.0,
) -> int:
    kwargs: dict = {}
    if event:
        kwargs["event"] = event
    if detector:
        kwargs["detector"] = detector
    if pulsar:
        kwargs["pulsar"] = pulsar
    if duration is not None and "physionet" not in dataset_id:
        kwargs["duration"] = duration
    # PhysioNet EEG crop / channel
    if edf is not None:
        kwargs["edf_path"] = edf
    if channel is not None:
        kwargs["channel_name"] = channel
    if "physionet" in dataset_id:
        if duration_s is not None:
            kwargs["duration_s"] = duration_s
        elif duration is not None:
            kwargs["duration_s"] = duration
        kwargs["start_s"] = start_s
    # decimate only applies to open-strain HDF5 loaders
    if dataset_id.endswith("_strain_open") or dataset_id in {
        "ligo_h1_strain_open",
        "ligo_l1_strain_open",
        "virgo_v1_strain_open",
        "kagra_k1_strain_open",
    }:
        kwargs["decimate"] = decimate

    series = load_series(dataset_id, **kwargs)
    print(f"Loaded {dataset_id}: n={series.n} facility={series.facility}")
    print(f"  source: {series.source_url}")
    for n in series.notes:
        print(f"  note: {n}")

    if series.uniform and series.dt is not None:
        y, dt = series.values, float(series.dt)
        if decimate > 1 and "decimate" not in kwargs:
            y = y[::decimate]
            dt *= decimate
            print(f"  post-load decimate={decimate} → n={len(y)}, dt={dt:g} s")
    else:
        # PTA default: 1-day grid unless user overrides
        udt = uniform_dt
        if udt is None and "nanograv" in dataset_id.lower():
            udt = 86400.0
        y, dt = series.to_uniform(dt=udt)
        print(f"  interpolated to uniform dt={dt:g} s, n={len(y)}")

    if max_n is not None and len(y) > max_n:
        # keep contiguous prefix (document truncation)
        y = y[:max_n]
        print(f"  truncated to first max_n={max_n} samples for analysis memory")

    if compare:
        result = compare_precondition_modes(y, dt=dt, n_null=n_null, seed=0)
        free = result["free"]
        print("\n=== FREE-FIRST (primary) ===")
        print(f"  discovery_claim_allowed : {free['discovery_claim_allowed']}")
        print(f"  free_T_hat              : {free['free_T_hat']:.6g}")
        print(f"  free_f_hat              : {free['free_f_hat']:.6g}")
        print(f"  power_5399 (secondary)  : {free['power_5399']:.6g}")
        print(f"  snr_5399 (secondary)    : {free['snr_5399']:.6g}")
        print(f"  null_fraction_exceeding : {free.get('null_fraction_exceeding')}")
        print("\n=== SUMMARY ===")
        for k, v in result["summary"].items():
            print(f"  {k}: {v}")
        payload = {
            "dataset_id": dataset_id,
            "facility": series.facility,
            "is_real": True,
            "synthetic": False,
            "provenance": series.provenance,
            "dt": dt,
            "n": len(y),
            "analysis": result,
        }
    else:
        r = full_r_fft_analysis(
            y, dt=dt, precondition=False, scrambled_g4_control=False, n_null=n_null
        )
        print(r)
        payload = {
            "dataset_id": dataset_id,
            "facility": series.facility,
            "is_real": True,
            "analysis": r.to_dict(),
        }

    if json_out is not None:
        json_out.parent.mkdir(parents=True, exist_ok=True)
        # numpy-safe dump
        def _default(o):
            if isinstance(o, (np.floating, np.integer)):
                return o.item()
            if isinstance(o, np.ndarray):
                return o.tolist()
            raise TypeError(type(o))

        json_out.write_text(json.dumps(payload, indent=2, default=_default), encoding="utf-8")
        print(f"\nWrote {json_out}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Real observatory data + free-first R-FFT")
    p.add_argument("--list", action="store_true", help="List registry + dismissed synthetics")
    p.add_argument("--status", action="store_true", help="Show local staging status")
    p.add_argument("--fetch", metavar="DATASET_ID", help="Download/stage a real dataset")
    p.add_argument("--analyze", metavar="DATASET_ID", help="Load + free-first R-FFT")
    p.add_argument("--event", default=None, help="GWOSC event name (strain loaders)")
    p.add_argument("--detector", default=None, help="H1/L1/V1/K1")
    p.add_argument("--pulsar", default=None, help="NANOGrav pulsar filter")
    p.add_argument("--decimate", type=int, default=1, help="Decimate uniform strain")
    p.add_argument(
        "--duration",
        type=float,
        default=None,
        help="GWOSC open-strain segment length (s), e.g. 32 or 4096",
    )
    p.add_argument(
        "--uniform-dt",
        type=float,
        default=None,
        help="Interpolation dt (s) for uneven series (e.g. PTA)",
    )
    p.add_argument("--n-null", type=int, default=32)
    p.add_argument("--max-n", type=int, default=200_000)
    p.add_argument("--json-out", type=Path, default=None)
    p.add_argument("--edf", type=Path, default=None, help="Local PhysioNet EDF path")
    p.add_argument("--channel", default=None, help="EEG channel name (PhysioNet)")
    p.add_argument(
        "--duration-s",
        type=float,
        default=None,
        help="EEG crop length in seconds (PhysioNet; default 3600 for CHB-MIT)",
    )
    p.add_argument(
        "--start-s",
        type=float,
        default=0.0,
        help="EEG crop start in seconds (PhysioNet)",
    )
    args = p.parse_args(argv)

    if args.list:
        return cmd_list()
    if args.status:
        return cmd_status()
    if args.fetch:
        kw = {}
        if args.event:
            kw["event"] = args.event
        if args.detector:
            kw["detector"] = args.detector
        if args.duration is not None:
            kw["duration"] = args.duration
        return cmd_fetch(args.fetch, **kw)
    if args.analyze:
        return cmd_analyze(
            args.analyze,
            decimate=args.decimate,
            uniform_dt=args.uniform_dt,
            n_null=args.n_null,
            max_n=args.max_n,
            json_out=args.json_out,
            event=args.event,
            detector=args.detector,
            pulsar=args.pulsar,
            duration=args.duration,
            edf=args.edf,
            channel=args.channel,
            duration_s=args.duration_s,
            start_s=args.start_s,
        )

    p.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
