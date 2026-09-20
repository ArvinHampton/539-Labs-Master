#!/usr/bin/env python3
"""Native G4 CMB TT ladder. No Planck theta_* input.

Category B validator. Run from repo root:
  python docs/S2-11DM2ET-X-Axiomatic-Book/scripts/cmb_g4_ladder.py
"""

from __future__ import annotations

G4 = 539.9
D = 11
CUBIC = 27

PLANCK_TT = {
    "peak_1": (220.6, 0.6),
    "trough_1": (416.3, 1.1),
    "peak_2": (538.1, 1.3),
    "trough_2": (675.5, 1.2),
    "peak_3": (809.8, 1.0),
    "trough_3": (1001.1, 1.8),
    "peak_4": (1147.8, 2.3),
    "trough_4": (1290.0, 1.8),
    "peak_5": (1446.8, 1.6),
    "trough_5": (1623.8, 2.1),
    "peak_6": (1779.0, 3.0),
    "trough_6": (1919.0, 4.0),
    "peak_7": (2075.0, 8.0),
}

CLOSED = {
    "peak_1": (D, CUBIC),
    "peak_2": (1, 1),
    "peak_3": (3, 2),
    "peak_4": (17, 8),
    "trough_2": (5, 4),
}

OPEN = {
    "trough_1": (17, 22),
    "trough_3": (13, 7),
    "trough_4": (19, 8),
    "peak_5": (8, 3),
    "trough_5": (3, 1),
    "peak_6": (23, 7),
    "trough_6": (25, 7),
    "peak_7": (23, 6),
}


def ell_from_frac(num: int, den: int) -> float:
    return G4 * num / den


def report(name: str, frac: tuple[int, int], forced: bool) -> dict:
    pl, sig = PLANCK_TT[name]
    model = ell_from_frac(*frac)
    return {
        "name": name,
        "forced": forced,
        "frac": f"{frac[0]}/{frac[1]}",
        "model": model,
        "planck": pl,
        "sigma": sig,
        "resid_pct": 100.0 * (model - pl) / pl,
        "resid_sig": (model - pl) / sig,
    }


def main() -> None:
    rows = [report(k, v, True) for k, v in CLOSED.items()]
    rows += [report(k, v, False) for k, v in OPEN.items()]
    order = list(PLANCK_TT.keys())
    rows.sort(key=lambda r: order.index(r["name"]))
    print(f"G4 = {G4}  D = {D}  cubic = {CUBIC}")
    print(f"{'name':12} {'frac':8} {'model':10} {'Planck':10} {'d%':8} {'d_sigma':8} {'set'}")
    for r in rows:
        tag = "CLOSED" if r["forced"] else "open"
        print(
            f"{r['name']:12} {r['frac']:8} {r['model']:10.2f} {r['planck']:10.1f} "
            f"{r['resid_pct']:7.3f} {r['resid_sig']:7.2f} {tag}"
        )
    closed = [r for r in rows if r["forced"]]
    print(
        "closed mean |d%| = "
        f"{sum(abs(r['resid_pct']) for r in closed) / len(closed):.3f}"
    )


if __name__ == "__main__":
    main()
