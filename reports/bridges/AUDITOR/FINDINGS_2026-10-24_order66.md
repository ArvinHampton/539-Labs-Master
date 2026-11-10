# FINDINGS 2026-10-24 order66 pass (22:21–22:24 CDT)
Rules: no invent; PASS/FAIL untouched; CHAT≠PAPER. order58 RG47a FAIL stands. Φ/flux→k WRITTEN-CHAT only. NL1 OPEN.

## 1. order66 (BRIDGE_C_35/order66/) — COMPLETE, VERIFIED (1 warning)
- PREREG.sha256 OK (edac08a5…678e); SHA256SUMS 3/3 OK (RESULTS fc8b46c0…651b, includes the GATE sha-sync addendum).
- No numeric run; no new PASS; §1 PASS rows all quote prior hashed RESULTS with order+sha; sub-check PASSes (RG45c-2″, RG47e sanity) carry FAIL-stands caveats. Hold-numeric matches ORDER67_BRIEF.
- GATE_DECISIONS.md sha f9f32d26…cb19 = order57/GATE_DECISIONS.sha256: OK.
- **W-66-1 (Warning)** order66/RESULTS.md §3 row "corner/EVEN ↔ ρ_lab": "order65 Item 3: 0 hits ρ_lab in PDFs". Evidence: 9 hits each in Bridge_C_Clean(_v2).pdf (W-65-1). Pairing still ABSENT, so OPEN status is right, but claim is false. Fix: additive row on order66 RESULTS after order65 additive lands; rehash.

## 2. Local additives
- **W-64 OPEN (narrowed).** GATE_DECISIONS:16 retagged correctly (Physicist ruling, order7 Cat A basis, "order7 text does not name RG47e"); order64/RESULTS.md:50–51 additive correct. But order64/RESULTS.md:4 heading "CLOSED-EXPLAINED (order7)" and :6 "as order7 forces" remain uncaveated in-line. Fix: additive pointer at :4/:6 or addendum explicitly superseding :4/:6 by line number; rehash SUMS.
- **W-C3 / C10 OPEN (content OK, hash missing).** MAPS_CANDIDATES/RESULTS.md:18 (C3 FAIL Cat B via C3_RUN, supersedes :8) and :19 (C10 FAIL Cat A on Π*_max, CHAT-accepted; OPEN vs corpus-written Π) are coherent with C3_RUN and my FINDINGS_continue §2 wording. But MAPS_CANDIDATES has only PREREG.sha256 (OK, fdd4c2be…a424); RESULTS.md (mtime 22:20:49) has no hash file. Fix: write MAPS_CANDIDATES/SHA256SUMS incl. RESULTS.md → then CLOSE both.
- **W-65-1 OPEN.** order65/RESULTS.md:18 still "`rho_lab|ρ_lab|ρlab` → 0 hits anywhere"; no addendum; SUMS unchanged (still OK on old text).

## 3. NONLOCAL prereg hashes (NONLOCAL_QM_EH11D/prereg/)
| Dir | PREREG.sha256 | RESULTS.sha256 | result.log hashed | Notes |
|---|---|---|---|---|
| EH_FOURFORM | OK (PREREG, run.py, result.log) | — | yes | |
| EH_FOURFORM_CJS | OK (PREREG, run.py) | none | **no** | W-NL-4 |
| EH_GC1_INDEX | OK (PREREG, run.py) | none | **no** | W-NL-4 |
| EH_JX1 | OK | OK (PREREG, run.py, PREREG.sha256, result.log) | yes | see below |
| EH_RICCIBLOCK | OK (PREREG, run.py) | none | **no** | AUDIT_NOTE present |
| EH_RICCIBLOCK_C2_RERUN | OK | OK (result.log) | yes | |
mtimes: PREREG/run.py precede result.log in every dir (sub-second gaps for JX1/CJS/GC1: same-script write+run; ordering holds but is weak evidence of independent prereg).

### EH_JX1 — hash OK; PASS label status
- Source check: Junctions wrap (copy at _git_v8_unpushed_clone/docs/…/Einstein-Hampton-2026-09-29/…L17_Junctions.md:32-33) reads "K_mu nu = -k q_mu nu on the lock slice." / "K_mu nu - K q_mu nu = 3 k q_mu nu." — P1, P3 quoted correctly. Log: P1–P3 True, C1–C3 fail-controls True, "EH-JX1 PASS". PASS not altered.
- Label: PASS is Cat A geometry **given stated normal convention** (C2 shows sign flips). Source is a wrap note, not paper. PREREG scope line is correct; MILESTONE_2026-10-24e.md:2 still "EH-JX1 PASS" with no convention / WRITTEN-CHAT(source) tag → **W-NL-3 OPEN** (not landed).
- N-JX1 (Note): result.log line 1 "K_mn = Matrix(0, 0, [])" — run.py calls Km.diag() (sympy classmethod → empty matrix). Cosmetic print bug; booleans computed on Km directly, unaffected. Fix: print Km.diagonal().

## 4. FOUND vs ABSENT spot-check (new inventory_check files, mtime 22:20:59)
- cd250095:579 Φ=8πG11·G_ABCD G^ABCD=1728k² — verbatim OK; :604 N=4880 on S^4 — OK. Correctly tagged WRITTEN-CHAT, GATE_CANDIDATE only. No FOUND→PASS promotion.
- periodic-table-codex.txt:53-54 Z_eff only as symbol — OK; ABSENT rule claim consistent.
- e85353a0 "Ω_11D = 0.99987 …" cited :405, actual **:406** (N-66-1 off-by-one). 482268c8 "Ionization energies: exact…" cited :312-316, actual **:317** (N-66-2).
- No FOUND claim contradicts an ABSENT log; Ω₁₁D, F_total table, 539labs.json, k11(N) closed form all consistently ABSENT. Chat "exact match" claims correctly tagged circular/WRITTEN-CHAT.
- **W-NL-5 (Warning)** EXPANDED_SEARCH_LOG.md:38 entry stamped "22:30 CDT" but file mtime 22:20:59 CDT (box clock 22:22 at audit). Future-dated log entry. Fix: correct stamp to actual write time (additive).

## 5. order67
ORDER67_BRIEF.md + order67/PREREG.md, PREREG.sha256, logs/, scripts/ present; no RESULTS. Default (a) idle hold. Audit when RESULTS land (check PREREG hashed before any logs/scripts output).

## Counts this pass
Blockers 0 / Warnings 3 new (W-66-1, W-NL-4, W-NL-5) / Notes 3 (N-JX1, N-66-1, N-66-2). Closed 0.
