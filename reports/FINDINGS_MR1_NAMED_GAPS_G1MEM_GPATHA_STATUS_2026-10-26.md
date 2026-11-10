# FINDINGS — MR1 named gaps G1-mem / G-PATH-A STATUS — 2026-10-26 ~21:25 CDT
Soft SF write-only. Authority: Physicist CONTINUE → Auditor; OW blanket 9b993a72…. Proof-or-named-gap only. NO RECS. No invent. Kerr BLOCKED. Tip untouched.

## STATUS: GAP STANDS. G1-mem OPEN (P1/P2/P3 ABSENT; Kr QQ CRT FAIL; rebuild LIVE). G-PATH-A OPEN (f0f61da0…). MR1 does not promote G1.

## Sources (sha256 re-verified this run)
| # | File | sha256 | Class |
|---|------|--------|-------|
| 1 | quantum-comp/reports/EIGEN-TE-RHOBAR-N36-G1MEM_2026-10-26.md | d768dbd9…b29d ✔ (expected match) | Eigen Soft SF GAP |
| 1b | quantum-comp/reports/SOFTSF_PRESS_EIGEN_G1MEM_2026-10-26.md | 01bd5de6…80f7 | PRESS |
| 2 | grok-batches/EIGEN-TE-RHOBAR-N36-CRT36Z-KR-QQ-FAIL_2026-10-26.md | 2eb525c5…353e | Eigen Soft SF FAIL |
| 2b | grok-batches/SOFTSF_PRESS_EIGEN_N36_CRT36Z_KR_QQ_FAIL_2026-10-26.md | 129a1583…8c9b | PRESS |
| 2c | bridges/AUDITOR/FINDINGS_2026-10-26_t2050u_EIGEN_N36_CRT36Z_KR_QQ_FAIL_CONFIRM.md | 463c4415…7f40 | Auditor CONFIRM PRESENT |
| 3 | grok-batches/EIGEN-TE-RHOBAR-N36-KR-QQ-NAMED-GAP-REBUILD-LIVE_2026-10-26.md | 05db5cc2…b45a | Eigen NAMED GAP + LIVE |
| 4 | FINDINGS_MR1_COOK_RESUME_MATHLIT_G1_N36N6_PACKAGING_2026-10-26.md | 6ed0fc31…b0e2 ✔ | MR1 G1 PARTIAL |
| 5 | FINDINGS_MR1_PATH_A_EXACT_RHOBAR_SOFTSF_CORPUS_2026-10-26.md | f0f61da0…1b01 ✔ | MR1 path (a) ABSENT |

## G1-mem — restated named gap (as Written by Eigen d768dbd9…)
- P1 char-0 rank/spanning at m=7 (11700×13305 polar matrix over Q(ζ980), rank 13305−503): ABSENT.
- P2 coordinated Kr over Q(ζ49) + exact char-0 zero-polar check: ABSENT.
- P3 503-block vector-valued Sturm premise for ∞-truncation through q^18: ABSENT.
- Description-only close path (Eigen Written, not run): save Kr from solve36w_z, CRT over Q(ζ49) with coordinated r_p, exact char-0 zero-polar check on 503 vectors ⇒ P1+P2 without P3.

What later landings add:
- CRT36Z FAIL (2eb525c5…, Auditor CONFIRM 463c4415…): e1 6/6 primes rank 503 pivots MATCH; crt36z on 5091737 entries: recon_ok+holdout 539, no_recon 1995671, holdout_fail 3095527, max height ≈39.17. Kr QQ NOT reconstructed. Zero-polar HOLD. Disk crt36z_auto.log tail agrees.
- Rebuild LIVE (05db5cc2…): Kr QQ ABSENT named gap; rebuild_e1_extra_then_crt.sh LIVE (PID 2815455 present this run); latest e1 log solvez_p7867441_e1.log ends "kernel dim 503 … RANK … 503 target 503 … done" (mod-p only, not char-0).

## Disk check (read-only, grok-batches/eigen-n36-503/)
- Kr sobj (coordinated, QQ/Q(ζ49)): ABSENT. Only ∞-RREF n36_basis_q18_inf_QQ_m7_crt6.sobj (+ crt2_NOTCERT) — not Kr.
- CRT Q(ζ49) Kr success artifact: ABSENT (crt36z FAIL log only).
- char-0 zero-polar artifact: ABSENT.
- solve42g LIVE: PIDs 2840611 / 2840664 (python3 solve42g.sage.py 6 1027606441 5, started 21:12 CDT); parent resume_solve42g_serial.sh PID 2816202. Not touched. No compute started, nothing killed.
- G-EXACT (Alt B run_exact.py): not run, not re-checked beyond parallel-open note; remains separate open gap.

## Premise table
| Premise | Status |
|---|---|
| P1 char-0 rank/spanning m=7 | ABSENT |
| P2a coordinated mod-p Kr kernels (e1, rank 503, pivots match) | PRESENT (mod-p only) |
| P2b Kr over QQ/Q(ζ49) via CRT | ABSENT (crt36z FAIL) / rebuild LIVE |
| P2c exact char-0 zero-polar check | ABSENT (HOLD) |
| P3 503-block Sturm premise | ABSENT |
| ∞ basis CERT(∞+ν) 8061c7b2… | PRESENT (stands; does not close G1-mem) |
| G-PATH-A exact ρ̄ path (a) | ABSENT (f0f61da0…) |
| Kerr | OUT-OF-SCOPE (BLOCKED) |
| G-EXACT Alt B run_exact.py | OPEN / OUT-OF-SCOPE here |

## Explicit
- MR1 does not promote G1; G1-mem OPEN. G-PATH-A OPEN, no new invent.
- Exact ν Alt B packaging (6ed0fc31…) stands separate.
- No Eigen private code copied into operative CSVs.
- Tip residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188…dfc91, tip_touched NO.
