# A61 out/ regeneration note (2026-10-22)

**What happened.** The box restarted at 22:21:44 CDT. The A61 track directory was restored at 22:24:49 CDT with every file re-timestamped and `out/` missing. The track was pushed to GitHub (commit 1bb3229) without `out/`. SHA256SUMS, PROOFS.md, REPORT.md, REPORT.pdf, prereg files and code/ were not changed by this note or by the regeneration.

**Regeneration (not new results).** `code/run_all.sh` was run unchanged (nice -n 10, OMP_NUM_THREADS=1, ulimit -v 3000000 inside the script) on 2026-10-22 from 22:41:10 to 22:41:36 CDT (26.7 s wall). Because the restore also dropped `A59_clt_rederivation/out/` (20 files; `chk04_enclosures_cells.py` reads `cells59_w005.json` from it), the run was done in a sandbox copy (`/workspace/a61sb`) in which `A59_clt_rederivation/out/` was filled from the A59 supporting bundle already on GitHub (`A59_supporting_files.tgz.b64`). The sandbox `cells59_w005.json` has sha256 0b5cc839...0025a, equal to the entry in A59's SHA256SUMS. A56/A57 `proof/` files were read from the box, where they are intact. The 12 resulting files were then copied into `A61_clt_proofs/out/`. The A59 track directory on the box was not touched.

**Comparison with SHA256SUMS (11 out/ entries).** Byte-for-byte match, sha256 equal to SHA256SUMS:
`logs_chk01.txt`, `out_chk02.json`, `out_chk03a.txt`, `out_chk04_cells.json`, `out_chk05_containment.json`, `out_chk06_consts.json`, `out_chk07_minor.json`, `out_chk08.json`, `out_chk09_tiny.json`, `out_tail61_partial.json`, and `out_tail61.json`. Differs: none of the 11 listed files.

Two remarks on `out_tail61.json`: `tail61.py` writes `out_tail61.json` only when called with no arguments (default k = 27, 29, 31, 33), while SHA256SUMS lists `out_tail61.json` and `out_tail61_partial.json` with the same hash, and `run_all.sh` (k = 17..33) produces the 9-k file as `out_tail61_partial.json`. So `out_tail61.json` here is a byte copy of the regenerated `out_tail61_partial.json`; its hash equals the SHA256SUMS entry. It is a reconstruction by copying, not a separate run.

`run_all.log` is not listed in SHA256SUMS (it was in the lost out/ but unhashed). The regenerated one is the output of `time bash run_all.sh`; it cannot be compared with the lost original.

**Substantive numbers (all unchanged):**
- chk01: all 28 symbolic identities verified.
- chk02: max identity defect 1.0e-56; min slack upper (even n) 0.6954, lower 0.2581.
- chk03: 3200 shift tests, 0 violations; item 1 max actual/claimed 0.99990.
- chk04: A56 sharp/c15 and A57 sharp 312 cells each, A59 500 cells, all contiguous and covering every window.
- chk05: 2079 arb containment checks, 0 violations.
- chk06: 1512 checks, 0 violations.
- chk07: 8640 minor-arc tests, 0 violations.
- chk08: exact E-O identity for 6416 (k, d) pairs.
- chk09: 3200 checks, 0 violations.
- tail61, k = 17,19,...,33: D0 = 37947145, 41043238, 42849645, 45550651, 48102974, 49312289, 51557554, 53684094, 55698896; T(D0) = -33.71, -35.07, -30.67, -30.78, -30.50, -25.48, -24.71, -23.84, -22.78; all 9 close (ustar_ok, monotone_ok, T <= 0). D0 for k = 27..33 equals A56/A57/A59, as stated in REPORT.md.

**Other restore losses found.** Re-checking SHA256SUMS of all pushed tracks on the box: only A61 `out/` (now regenerated) and A59 `out/` (20 files, intact on GitHub in the A59 bundle) are missing; the one A56 line reported by sha256sum is the pseudo-entry `exact/sec/* (combined)`, not a loss.
