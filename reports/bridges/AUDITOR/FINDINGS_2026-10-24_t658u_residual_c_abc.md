# FINDINGS — t658u RESOLVE Extract A/B/C (Local) — audited 2026-10-25 00:00 CDT (America/Chicago)
Mode: audit-only, soft flags only. No PASS/FAIL altered. CORE_FREEZE intact. Local map only (NL separate). Invent-ban stands (no outer_*; t660u not unlocked).

## 1. Paths + live shas
- BRIDGE_C_35/inventory_check/EXTRACT_T658U_RESIDUAL_C_ABC_2026-10-24.md = e5a275a8584bb382fcf089970f2199811334c83ca149a5659846294bf3e501b4 MATCH
- BRIDGE_C_35/inventory_check/SHA256SUMS = bb33297342403963513a9d1011278b3708c776a9be6cb7feb36d6566c628a7bc MATCH; sha256sum -c **13/13 OK**
- Supersession: SUMS 646c5cd2… (6/6, recorded in g1_accept FINDINGS L56 / HASH_INTEGRITY L275) -> bb332973… (13/13). Additive: original entries (hunt ee4f4fc0, missed_vars eb17f7e3, T635U d12dd01d, ingest 2ddadd5e, HD 552541cf/f2f9d897) still present + OK; added 6 oct17-master source docs + EXTRACT_T658U e5a275a8. No prior entry dropped or changed.
- Prior cites live: EXTRACT_T635U d12dd01d… OK; RESIDUAL_IDENTITY_HUNT ee4f4fc0… OK; W7 candidate pin b9a21438… = pins/RESIDUAL_LAW_C_CANDIDATE_W7_2026-10-24.md (+ order76/data verbatim copy) MATCH; FINDINGS_order77 1775ac9f… MATCH; FINDINGS_g1_accept b63db28c… MATCH.

## 2. Claims
- A ABSENT exact residual_slash/Fricke identity — CONFIRMED. Quoted lines verified verbatim (a6a91a3b L25/L37; 7368b855 L24/L58; 7add2a9a L12/L35; 426ea3e0 L51/L153/L163). Definitions only; no δ≡0 proof.
- B ABSENT sample h/δ — CONFIRMED (7368b855 L50 "not yet tabulated"; 1bab65c4 L42 probes only; 1e18a87d L149/L200). Aligns with d12dd01d / ee4f4fc0.
- C ABSENT cocycle completion — CONFIRMED. NM1–NM5 paths+shas all in SUMS, live OK; cited lines verified (a6a91a3b L25/L49; 7368b855 L50; 7add2a9a L35; 426ea3e0 L22/L47/L195; 1e18a87d).
- Zwegers/H_s not C — CONFIRMED (explicit exclusion L36; 426ea3e0 L47 "Not used as a cocycle").
- Posture — CONFIRMED: extract-only; SF-W7-3 fence stated (Closure trees excluded; "Closure" occurrences are only exclusion text); residual-C OPEN; no Bridge YES; order78 not started.

## 3. Soft flags
- SF-T658-1: NM5 (Per_off kernel table) is a weak "near-miss" — no cocycle structure; catalog membership is descriptive only.
- SF-T658-2: NM1 is the same object as W7 pin b9a21438 candidate — per SF-W7-3, candidate ≠ identity; extract respects this.
- SF-T658-3: "ingest" in SUMS is 2ddadd5e (INGEST_G1_ACCEPT_t642u); b63db28c is the AUDITOR g1_accept FINDINGS — different artifacts, no conflict.
- SF-T658-4: SUMS uses ../../../(../) relative paths outside BRIDGE_C_35 (heavy-daily, oct17-master); -c only valid from inventory_check/.
- SF-W7-3 carried.

## 4. Open set
residual-C OPEN; residual_slash identity OPEN; h/δ_W7 sample table ABSENT; W-PO-2/3 OPEN (carry); Bridge PARTIAL / READY NO; order78 NOT authorized.

## 6. Blockers
None for CONFIRM. Invent-ban blocks any outer_*/regulator construction (t660u locked).
