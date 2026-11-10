# AUDITOR FINDINGS — t674u NL W-PO-2 wide exhaust ABSENT-with-gap — CONFIRM
Stamp: 2026-10-25 00:33 CDT (America/Chicago). Mode: soft-SF only; no PASS/FAIL altered; no invent; Local not audited; no order78.

## Match table (inventory_check/)
| File | Claimed | Recomputed | |
|---|---|---|---|
| FINDINGS_T674U_WPO2_WIDE_EXHAUST_ABSENT_2026-10-25.md | 5b36037b…79018868 | 5b36037b755c4c72cdeecb1906eab48c95a93e883aa7ec7efe9860fe79018868 | MATCH |
| SHA256SUMS | d9f512bf…4ec05314 | d9f512bf038044ffc9dcf659bb3e8e2ce568e26f49547416aaf1ec4502c05314 | MATCH |
| STREAM_IDLE_WRITTEN.md (mirror ../ byte-identical) | 465503c5…b5bdbb | 465503c5ed76a6fb8c49efc7b0c8ab6195d7b3864aa3875557a5305ee5b5bdbb | MATCH, IDLE_AFTER_LOCK (l.81) |
sha256sum -c SHA256SUMS: 24/24 OK, 0 fail.

## Claims
1. No PREREG (nothing uniquely forced): STATED + CONSISTENT; no prereg/*674* dir exists. CONFIRM.
2. W-PO-2 OPEN, W-PO-3 PARTIAL (unchanged): stated; no CLOSED overclaim. CONFIRM.
3. Written supply needed (a) Ω₀ norm+convention, (b) f_warp(k) inside Ω₁₁D/F_total with fixed y*/kb, (c) K + f_curv(K), (d) per-term table: all four present in Verdict table. CONFIRM.
4. Near-misses (Ω_0^Spin bordism collision; ω₀=dz/z; 17-Theorems exp(−2ky) y_max tuned; R_compact/δm_warp; torsion compactification; Ω₁₁D single factor; kb≈0.797 chat; Drive ϕ_warp) all dispositioned non-forcing; none treated FOUND/DEDUCED close. CONFIRM.
5. No free invent; Local Bridge untouched; no NL2; no order78 (grep: none). CONFIRM.
6. Consistent with t665u CONFIRM 2e5bec8185cf8b2829ee2d596891a9107fa8e9c46178455bfdf347eac5b96d73 (recomputed MATCH) and t660u f27c750e44318dc1cd1f9ad718fd08a8ed56d0fb4d5a6a1049ee2844d5b1b2c1 (MATCH): W-PO-2 still OPEN. CONFIRM.

## Soft SF
- SF-T674NL-1 (hygiene): Cat B Ω₁₁D=1/√(1+g₁₁²+g_s²) near-miss is in STREAM l.56 but not in the t674u hits table; disposition (non-forcing) consistent. No action required.
No other SF.

## Open set
W-PO-2 OPEN (Ω₀, f_warp(k), f_curv(K), per-term table ABSENT-with-gap); W-PO-3 PARTIAL; Z-table json ABSENT; two-fork OPEN.
Verdict: CONFIRM t674u ABSENT-with-gap LOCK.
