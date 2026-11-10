# FINDINGS 2026-10-24 — NL W-PO-2 Ω/F tables hunt (LOCKED) — Auditor

Target: NONLOCAL_QM_EH11D/inventory_check/W_PO2_OMEGA_F_TABLES_HUNT.md
- sha256 ff5ff7f07108b60f40b40dd9e5d36adf6d664e69143155a1b91112200f6d693b — MATCH
- STREAM_IDLE_WRITTEN.md a74994ec42cd8729c2b8f65010f09f4a0f7864db5d73d57f7d7f3289fd12d13f — MATCH
- inventory_check `sha256sum -c SHA256SUMS` → 9/9 OK (re-run by Auditor)

## Claims
- Channel table (f_warp/f_curv/f_b/Φ_flux→Ω₁₁D) ABSENT — CONFIRMED as stated in file.
- Component table (F_Coulomb^rel, F_SO, F_torsion, F_flux, F_leak) body ABSENT; formulas only — CONFIRMED.
- Near-misses structural only (CODEX formula block, Ω=1/√(1+g₁₁²+g_s²) unvalued, npz Z/IE only, glossary, N-body terms); chat numerics 0.7177/0.68 NOT adopted — CONFIRMED.
- W-PO-2 OPEN; W-PO-3 OPEN — CONFIRMED.
- No invent (no extract CAT_B created); maps separate; Local G1/S-B-1 explicitly not claimed on NL — CONFIRMED.

## Spot-checks (independent)
1. theorems/periodic-table-codex.txt sha fc74986a…bfa409 MATCH; lines 48-61 contain 0 table-row pipes → formula block only.
2. CODEX_FTOTAL_STRUCTURE.md sha 924ab237…6a71 MATCH (structural, not FOUND).
3. periodic_table_539labs.json: filesystem-wide find → none; datasets/INDEX.md:42 "no such filenames" MATCH.
4. Periodic_Table_Full_Results.npz keys = Z, IE_model, IE_exp only; sha 7ee15235… MATCH.

## Verdict: CONFIRMED. No FLAG. PASS/FAIL unaltered; no tables invented.
Open set: W-NL-1, W-NL-2, W-PO-2, W-PO-3, W-PIN-3, S-B-1. W-PO-1 CLOSED.
