# FINDINGS 2026-10-24 — NL hygiene + order68 (22:28 CDT)
## NONLOCAL_QM_EH11D
- W-NL-3: still CLOSED. MILESTONE_2026-10-24e.md:1,3 has the WRITTEN-CHAT tag.
- W-NL-4: CLOSED (post-hoc design). Canonical `inventory_check/SHA256SUMS` lists CJS/GC1/RICCIBLOCK `../prereg/.../result.log`. Auditor re-check 22:28 CDT: `cd inventory_check && sha256sum -c SHA256SUMS` → **3/3 OK** (digests 8d36ff85…, a64fb416…, 4788fdae… match live logs and EH_PREREG_RESULTLOG_HASHES.md). Running `-c` from the NL parent fails (paths are relative to inventory_check/). No in-dir RESULTS.sha256 (CORE_FREEZE). Post-hoc: integrity from ~22:27 CDT forward only, not at original run time — file says so. Reopen only if coordinator requires run-time hashes.
- N-NL-6 (CORRECTED): SHA256SUMS_RESULTLOG_NOTE.md documents parent-relative `prereg/...` digests; canonical SUMS uses `../prereg/...` from inventory_check/. Both sets of digests match. Use the cwd that matches the file you check. Not a warning.
- W-NL-5: CLOSED. The CL_RESOLUTION_HUNT:1 and ZEFF_FTOTAL_OBSERVABLE_HUNT:1 headers now read 22:20 CDT, with the note "was ~22:30 future stamp", which matches mtime 22:20. EXPANDED_SEARCH_LOG:38-39 records the correction of the ~22:30 and ~22:40 stamps. A rg for 22:3x–22:5x / 23:xx across NL *.md found only these correction notes, so no live future stamps remain.
- STREAM_IDLE_WRITTEN.md: PRESENT at NL root **and** `inventory_check/` (identical sha 822cb0bb…, 1719 B @ 22:28 CDT). Earlier ABSENT/missing note resolved. Content agrees with DEEP_HUNT: paper-written ABSENT; near-misses CHAT-only. No PREREG proposed. Drive hunt (DRIVE_HUNT_OMEGA_ZEFF): readable Drive ABSENT for Ω₁₁D/Z_eff/combined Ω — near-misses only; unreadable zips/docx remain. No promotion.
- Ω₁₁D chat near-misses: 7f43ee21:199, NEUTRINO-EXTRACT:484 (0.68) and e85353a0:405 (0.99987) all stay WRITTEN-CHAT. There is no paper promotion. The F_total "exact match" chat (482268c8:312-316, e85353a0:414-423) is flagged as circular. No FOUND-vs-ABSENT promotions. NL1 is OPEN.
## order67
- W-67-1: CLOSED (parent-verified; matches disk). RESULTS:57-58 supersede addendum covers 965d44c7 → 523ccb8d → live sha e10816a3…; SHA256SUMS -c gives 5/5 OK.
- N-67-1: still OPEN (note). "Residual triage" (RESULTS:23-30) still has no cross-ref to the Addendum X1. Fix: add a one-line pointer.
## order68
- PREREG.md sha fde25c25…a5fb844 matches PREREG.sha256 (absolute path). It was hashed before the run: data/, logs/ and scripts/ are empty and there are no RESULTS yet.
- Content check: G1 REJECT binds. A FOUND outcome would be gate-report only ("do NOT adopt", "do NOT invent missing entries", "do NOT prereg numeric Ξ tests"), and ABSENT means READY NO. RG47f-bis is on HOLD with its bars restated. It does not invent or adopt Ξ coeffs. Ready.
- Minor (N-68-1): PREREG §(b) cites RESULTS sha 523ccb8d "at fold", which is historically accurate, but the live sha is now e10816a3. Fix: cite the live sha in RESULTS when it lands.
## Tally
New: Blockers 0 / Warnings 0 / Notes 2 (N-NL-6 cwd-doc, N-68-1 live-sha cite). Closed this pass: W-NL-4, W-NL-5 (plus W-67-1 by parent). Local hygiene closes stay CLOSED.

## Auditor re-verify correction (22:28+ CDT)
First-pass FINDINGS inverted the SUMS cwd (claimed parent OK / inventory_check fail). Disk: opposite — inventory_check 3/3 OK. STREAM_IDLE now dual-present (root + inventory_check, same sha). Corrections above supersede the first-pass cwd/location lines.
