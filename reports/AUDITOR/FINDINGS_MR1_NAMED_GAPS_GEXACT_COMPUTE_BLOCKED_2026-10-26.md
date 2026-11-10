# FINDINGS — MR1 Named Gap G-EXACT (compute-blocked / exact cells ABSENT)
Soft SF write-only. Date: 2026-10-26 ~21:44 America/Chicago (CDT). NO RECS. No invent. Kerr BLOCKED. Mesh CANCELLED.
Authority: Physicist CONTINUE; OW blanket sha256 9b993a72bcdfed3fe2d78c15cbe76d0c8197958ca5ac60111546cd5e7ec6498b.

## STATUS: G-EXACT — GAP STANDS
1. Re-verify (find, read-only, /workspace): `V42_ALTB_EXACT_CELLS_CF980.csv` ABSENT; `cells_exact.sobj` ABSENT; no `*EXACT_CELLS*` anywhere. No run_exact.py outputs present in /workspace/grok-batches/mr1-cf980-alt-b-v42/ (only scripts + mod-p/CRT artifacts).
   - `run_exact.py` live sha256 47d981620a0328a9383442b3aaf13cecec0d006784d1dd66ebf582c7254a880c (matches prior 47d98162…). Not launched by MR1.
   - Other run_exact* hits are unrelated s_family_paths lanes (A40/A49/A57/A60); A49 logs/run_exact.out is empty (e3b0c442…). Not G-EXACT outputs.
2. Why blocked: host memory (15 GiB total, ~9 GiB available at check) held by solve42g LIVE (pgrep only, not touched):
   - PID 2816202 `bash …/eigen-q89-basis/rhos/resume_solve42g_serial.sh` (elapsed 40:08)
   - PID 2903671 `/bin/sh /tmp/pm/bin/sage-python solve42g.sage.py 6 1027606441 8`
   - PID 2903724 `python3 solve42g.sage.py 6 1027606441 8` (RSS ~2.0 GB, elapsed 02:37)
   G1-mem rebuild also waits on the same solve42g (cite Soft SF 3f14f6d8d454efbe30ffe123737824a25eebede6e880531dae85248b9be64b3a).
3. Alt B CERT packaging still stands under H_work without exact cells — cite fa47db06… / 53cb42bb… (Rec A-1 + exact-ν CERT MATCH, cite only). Exact cells not required for CERT-under-H_work house label.
4. Side: G-ID / G-IRR / G4a / G4b / GAP-E / ν=0 unchanged as in d2bd5c9f4c498882f496c76a88ca270012983d696663007b7aaf4faba5d6ea77; no disk change observed for this gap, no re-audit.
5. Prior cites: G-BASIS-89 CORRECTION 243f9cc504e10879dee57c43755913aa2698e64a6256d340a949e50b628a2adf.

## Tip
tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; tip_touched NO.
