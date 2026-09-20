#!/usr/bin/env python3
"""G4 CMB / BAO validator. No Planck theta_* input."""
from __future__ import annotations
import math

G4 = 539.9
D = 11
CUBIC = 27
N_FLUX = 4880
KAPPA = 243 / 539
MU = 1.55

PLANCK_TT = {
    "peak_1": (220.6, 0.6),
    "peak_2": (538.1, 1.3),
    "peak_3": (809.8, 1.0),
    "peak_4": (1147.8, 2.3),
    "trough_2": (675.5, 1.2),
}
CLOSED_TT = {
    "peak_1": (D, CUBIC),
    "peak_2": (1, 1),
    "peak_3": (3, 2),
    "peak_4": (17, 8),
    "trough_2": (5, 4),
}
PLANCK_EE = {1: 145.0, 2: 398.3, 3: 690.4, 4: 993.1, 5: 1296.4}
PLANCK_TT_H = {1: 5733.0, 2: 2586.0, 3: 2518.0}
PLANCK_EE_H = {1: 1.11, 2: 21.45, 3: 38.1}
R_D_FID = 147.09


def main() -> None:
    print("== TT positions ==")
    for name, (n, d) in CLOSED_TT.items():
        model = G4 * n / d
        pl, sig = PLANCK_TT[name]
        print(f"{name:10} {n}/{d:<2} {model:8.2f}  Planck {pl:7.1f}  {100*(model-pl)/pl:+6.3f}%")
    print("\n== EE positions ==")
    e1 = G4 * 3 / D
    print(f"EE1        3/{D:<2} {e1:8.2f}  Planck {PLANCK_EE[1]:7.1f}  {100*(e1-PLANCK_EE[1])/PLANCK_EE[1]:+6.3f}%")
    for n in range(2, 6):
        model = G4 * (6 * n - 4) / D
        pl = PLANCK_EE[n]
        print(f"EE{n}        {6*n-4}/{D:<2} {model:8.2f}  Planck {pl:7.1f}  {100*(model-pl)/pl:+6.3f}%")
    ell_D = G4 * 8 / 3
    ell_t = G4 * 11 / 5
    ell_S = 1.0 / math.sqrt(1.0 / ell_D**2 + 1.0 / ell_t**2)
    print(f"\n== Silk ==\nell_D={ell_D:.2f}  ell_t={ell_t:.2f}  ell_S={ell_S:.2f}")
    r12 = 1.0 / KAPPA
    p12 = PLANCK_TT_H[1] / PLANCK_TT_H[2]
    ell1 = G4 * D / CUBIC
    ell3 = G4 * 3 / 2
    silk = math.exp(-(ell3**2 - ell1**2) / (3 * G4) ** 2)
    r31 = (1.0 - KAPPA) * silk
    p31 = PLANCK_TT_H[3] / PLANCK_TT_H[1]
    print(f"\n== Heights ==\nP1/P2 model={r12:.4f}  Planck={p12:.4f}  {100*(r12-p12)/p12:+.3f}%")
    print(f"P3/P1 model={r31:.4f}  Planck={p31:.4f}  {100*(r31-p31)/p31:+.3f}%")
    a21 = G4 / CUBIC
    p21 = PLANCK_EE_H[2] / PLANCK_EE_H[1]
    a32 = D / 6.0
    p32 = PLANCK_EE_H[3] / PLANCK_EE_H[2]
    print(f"\n== EE amplitudes ==\nEE2/EE1 model={a21:.3f}  Planck={p21:.3f}  {100*(a21-p21)/p21:+.2f}%")
    print(f"EE3/EE2 model={a32:.3f}  Planck={p32:.3f}  {100*(a32-p32)/p32:+.2f}%")
    d_m = 3 * (N_FLUX - 3**5)
    ell_a = G4 * (MU - 1.0)
    r_d = math.pi * d_m / ell_a
    print(f"\n== BAO ==\nD_M(z_*)={d_m} Mpc  ell_A={ell_a:.3f}  r_d={r_d:.3f} Mpc  fid={R_D_FID}  {100*(r_d-R_D_FID)/R_D_FID:+.3f}%")


if __name__ == "__main__":
    main()
