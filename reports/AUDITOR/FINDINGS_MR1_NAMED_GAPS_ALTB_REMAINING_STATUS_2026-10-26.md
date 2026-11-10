# FINDINGS — MR1 Named Gaps (Alt B) Remaining Status — Soft SF write-only
Time: 2026-10-26 21:26 America/Chicago (CDT). Executor: Math Research 1 (shared box).
Authority: Physicist CONTINUE Soft SF next FINDINGS on open named gaps → Auditor (no invent, no RECS); OW blanket `OWNER_WRITE_BLANKET_OWNER_PURSUE_WRITE_AUTHORITY_ALL_LANES_2026-10-26.md` 9b993a72bcdfed3fe2d78c15cbe76d0c8197958ca5ac60111546cd5e7ec6498b (MATCH).

**STATUS: GAP STANDS** — no named gap below newly closed or PARTIAL; no premise newly PRESENT from disk.

## Sources (sha256sum live, 21:26 CDT)
| Source | sha256 | Check |
|---|---|---|
| tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH (pre) |
| FINDINGS_MR1_CF980_ALT_B_FAMILY_PY_V42_CRT | fa47db06e268a6f73579c547af25851ba267720f8259cf281e76a9614ff46b32 | MATCH |
| WRITTEN_CHOICES_MR1_CF980_ALT_B_V42 | 255b5a1079cf5bd9383015a2c6dcb3bebc40513bdb45389a40997aec7ed75de8 | live |
| FINDINGS_MR1_EXACT_LIFT_CF980_CRT (G4a/G4b/G4c' defs) | adcae95625de96d918ed456d412b142c612d12834146c0fa77ec5703ab451d73 | live |
| OW GAP-E scoping Cook Rec A | b33a5e85a6d5e2121a7f9cd9fdc2462998bc1f6c127186788ac06656b5abcb74 | MATCH |
| Prior FINDINGS G1-mem/G-PATH-A | 27dd3cc38f9dde89db02a3b96d31fff91790c4f75df680189b35f6be223eddc3 | MATCH (cite only) |
| CRT_LIFT_SCALED70_CF980.csv | 338c9a12cbac384a31b3f547eaece0e1300f4e061a0485bf642e1fab9da18aaf | MATCH .sha256 |
| run_exact.py | 47d981620a0328a9383442b3aaf13cecec0d006784d1dd66ebf582c7254a880c | live (not run) |
| Packaging companion (separate DONE, not this close) | 6ed0fc314c638b11a97f78099b727381d764e0851f705c9dc7c3beabce74e0b2 | MATCH |

## Premise table
| Gap | Status | Basis |
|---|---|---|
| G-EXACT | GAP STANDS | Alt B run_exact.py unfinished; `V42_ALTB_EXACT_CELLS_CF980.csv` ABSENT, `cells_exact.sobj` ABSENT (find /workspace). CERT-under-H_work rests on CRT+p4 (fa47db06…). Not launched. |
| G-ID | GAP STANDS | V36/V6 vs float V_Eis/V_cusp spectra-only; not certified; not needed under Alt B. |
| G-IRR | GAP STANDS | Exact irreducibility of V36/V6 not proved; float commutant dim 1 cited only; not used by cells. |
| G4a | OPEN / GAP STANDS | ℚ(ζ₄₉) containment not asserted (EXACT_LIFT §5 adcae956…; Alt B fa47db06…). |
| G4b | OPEN / GAP STANDS | True height bound unknown; H_work=10^18 is working bound only (Alt B CERT-under-H_work via Written C11 on 70·c). |
| G4c' | STANDS | ω_p convention / no remap; not a close target here. |
| GAP-E | LOCKED OPEN | Off-mesh per OW b33a5e85…. |
| ν=0 slot | OPEN (EXPECTED) | Per TEN_OPEN_SLOTS ACK; no fill invented. |
| G1-mem / G-PATH-A | remain OPEN | cite 27dd3cc3… / f0f61da0… only; not re-opened. |

## Disk / process checks (read-only)
- LIVE jobs (not touched): PID 2815455 `bash rebuild_e1_extra_then_crt.sh`; PID 2816202 `resume_solve42g_serial.sh`; PID 2868790 sage-python wrapper; PID 2868896 `python3 solve42g.sage.py 6 1027606441 6` (RSS ≈2.9 GB).
- free -h: total 15Gi, used 7.0Gi, free 3.4Gi, available 8.7Gi, swap 0B. Memory not safe for a long exact CF(140) run while LIVE jobs run → run_exact not launched.

## Explicit
No invent. No Card-1A ID invented. G1 not promoted. tip_touched NO. Kerr BLOCKED. No Eigen jobs started/killed. NO RECS.
