# U1 LEDGER: S and T spectra for the Theorem F representation (2026-10-18)
Setup: A=[[2,7],[7,7]], odd lattice Z², |L′/Z²|=35, 140 labels, S/T laws as in rev2 Theorem F. The builder is family.py (unchanged from 2026-10-17). The rebuilt S and T match the stored matrices exactly.

## Cat A (numerical, verified)
| Item | Result | Residual |
|---|---|---|
| P=S², P²=I, [P,T]=0 | dim Fix(P)=72 | 1.4e-15, 8.8e-16 |
| S²=I, (ST)³=I on Fix(P) | holds | 9.6e-16, 2.2e-15 |
| S spectrum on Fix(P) (72) | ±1, **n₊=36, n₋=36, tr=0** | eigenvalues within 1.8e-15 |
| Function span V | dim 42 | singular values 17.1 → 1.8e-13 |
| S on V_Eis (36) | **n₊=18, n₋=18**, tr 0 | S-inv 3.2e-16, T-inv 8.0e-16 |
| S on V_cusp (6) | **n₊=3, n₋=3**, tr 0 | S-inv 4.5e-16, T-inv 3.1e-16 |
| Order of T on Fix(P) | 140 | T¹⁴⁰−I: 7.5e-14 |
| Cusp forms | 24 characters → 12 σ-pairs (12 forms), realised span 6 | content-matrix rank 6 |
| f partners (positive frequency) | span the same 42 | rank 42 |

T spectrum on Fix(P), listed as r:multiplicity for eigenvalue e(r) (angles fit denominator 840 to 5e-13):
0:1, 3/70:2, 1/14:1, 1/10:1, 19/140:4, 1/7:1, 6/35:2, 13/70:2, 31/140:4, 17/70:2, 1/4:2, 2/7:1, 27/70:2, 11/28:2, 2/5:1, 59/140:4, 33/70:2, 1/2:1, 15/28:2, 19/35:2, 4/7:1, 3/5:1, 9/14:1, 13/20:2, 47/70:2, 24/35:2, 26/35:2, 11/14:1, 111/140:4, 23/28:2, 17/20:2, 31/35:2, 9/10:1, 131/140:4, 34/35:2, 139/140:4.
On V_Eis: the same 36 values, each with multiplicity 1. On V_cusp: r = 19/140, 31/140, 59/140, 111/140, 131/140, 139/140.
Traces are integers because the eigenvalues are ±1, so tr = 0 is exact given the numerics. No closed Gauss-sum proof is given.

## Cat B (interpretation)
- Fix(P) ⊇ V with a 30-dim T-stable complement. The T-multiplicities on Fix(P) are 1, 2, 4, against 1, 1, 2 on V, so the complement has multiplicities 0, 1, 2. Its structure is not analysed.

## Open
- Realisation of the 30-dim complement. The structure behind the 6 cusp combinations. A closed-form trace.
Evidence: S_Spectrum_2026-10-18/. Erratum: ERRATUM_Theorem_F_Function_Span_42_2026-10-18.md.
