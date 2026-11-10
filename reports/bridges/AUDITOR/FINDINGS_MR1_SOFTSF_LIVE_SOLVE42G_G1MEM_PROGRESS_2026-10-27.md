# FINDINGS — MR1 Soft SF LIVE: solve42g / G1-mem rebuild progress
Timestamp: 2026-10-27 11:28 CDT (America/Chicago). Read-only inspect. Soft SF Write-only. STATUS: OPEN / GAP STANDS / LIVE PROGRESS.

## LIVE processes (ps, ~11:27 CDT)
- PID 2815455 bash rebuild_e1_extra_then_crt.sh (etime 04:43:30)
- PID 2816202 bash grok-batches/eigen-q89-basis/rhos/resume_solve42g_serial.sh (etime 04:43:15)
- PID 3122540 / 3122633 solve42g.sage.py 6 1027606441 32 (etime ~07:15) — root 32 running

## Progress (solve42g_resume_watch.log)
- 11:01:14 START root=30; 11:11:05 DONE root=30 (roots_so_far=31)
- 11:11:05 START root=31; 11:20:37 DONE root=31 (roots_so_far=32)
- 11:20:37 START root=32 — running; root32 log at "kernel dim (relations incl.) 89", RANK line not yet printed
- => 32/42 roots done, root 32 in progress. 28 per-root logs (root03..root31 present) carry "RANK ... 89 target 89"; earlier roots logged elsewhere (not re-verified here).
- Correction vs prior: root 30 completed 11:11 CDT; root 31 ran 11:11–11:20 CDT.

## ABSENT
- Kr CRT: ABSENT. crt.log (2026-10-26 16:35 CDT) ends "RECON FAILED"; no newer CRT output.
- char-0 cert: ABSENT (certS.log 2026-10-26 14:16 CDT is prior S-cert, not char-0 G1-mem cert).
- exact cells: ABSENT.

## Cites (present in reports tree)
- G-EXACT Soft SF 1fb4ef15… present; G1 Soft SF 6d9b0887… present; G1-mem rebuild 3f14f6d8… present; Eigen G1MEM d768dbd9… present.

## Gates
G1-mem NOT promoted. G-EXACT NOT closed. Exact-ν Owner/Eigen Write-gated. Kerr BLOCKED. Mesh CANCELLED. NO RECS. No invent. No kill/restart.
tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched NO.
