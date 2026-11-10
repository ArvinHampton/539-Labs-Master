# FINDINGS 2026-10-24 — Drive unpack + STREAM_IDLE refresh (Auditor ~22:31 CDT)
## Re-verify closes (coordinator request)
- **W-NL-4 CLOSED** (confirmed; do not reopen for runtime hashes — coordinator ack). Canonical `inventory_check/SHA256SUMS` with `../prereg/...` → `sha256sum -c` from that dir → **3/3 OK** (8d36ff85… / a64fb416… / 4788fdae…). Track-root `NONLOCAL_QM_EH11D/SHA256SUMS` is a stub pointing here. Post-hoc design unchanged.
- **W-NL-5 CLOSED** (holds). CL/ZEFF headers still 22:20 CDT = prior close. Future-stamp scan: only W-NL-5 *correction* notes + historical chat UTC + new Drive/STREAM header skew (note below).
- **W-NL-3 CLOSED** (unchanged; not re-opened).

## STREAM_IDLE refresh
- Mirrored identical at NL root and `inventory_check/` — sha **f2c3962b…** (supersedes prior 822cb0bb…), 2127 B, mtime 22:30:50 CDT.
- Content agrees with Drive extract: T1–T5 paper/Drive Cat A ABSENT; zip unpack Cat A ABSENT; Cat B Ω=1/√(1+g₁₁²+g_s²) near-miss unused; GATE_CANDIDATE NO; invent-ban; NL1/two-fork OPEN; W-NL-4 leave post-hoc.

## DRIVE_HUNT_MISSING_VARS.md audit
- File: `inventory_check/DRIVE_HUNT_MISSING_VARS.md` (mtime 22:29:58; header claims 22:35 — see N-NL-7).
- Unpack dir `_drive_unpack/`: **123 files**, **46** pdf→txt — matches claim. **0** `.json` (periodic_table claim ABSENT holds).
- Spot-check Cat B Ω form: A27 export `1oMoNYoh…txt` lines 134,189,273 carry `Ω_{11D} = 1 / √(1 + g_{11}^2 + g_s^2)` — quote matches. Already ledgered EH-Ω1 in NL1_OMEGA_ABSENCE.md. Wrong args ≠ (k,K,b,Φ). Tag CHAT/draft Cat B — **not unlock**.
- Targets Z_eff rule / F_total json / letter→M_S / warp+fibre+flux→Ω: reported **ABSENT** — consistent with STREAM_IDLE and coordinator fold; no contradictory FOUND in this pass.
- **GATE_CANDIDATE: NO.** No Cat A PREREG sketched. No invent. No CHAT→paper promotion.
- Coordinator wording correction (Ω “never written” → Cat B exists but gating ABSENT) is recorded and consistent with invent-ban.

## Notes
- **N-NL-7:** DRIVE_HUNT header “22:35” vs mtime 22:29; STREAM_IDLE header “22:36” vs mtime 22:30 (~6 min ahead). Soft hygiene — not a reopen of W-NL-5 (different files). Fix: align header to mtime.
- Open warnings unchanged: **W-NL-1 / W-NL-2** (Φ/flux→k CHAT-only).
- order68: still PREREG-only (fde25c25…); no RESULTS.

## Tally
Blockers 0 / Warnings 0 new / Notes 1 (N-NL-7). Closes confirmed: W-NL-4, W-NL-5. No PASS/FAIL altered.
