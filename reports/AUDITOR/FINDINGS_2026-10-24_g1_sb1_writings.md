# AUDITOR FINDINGS — G1 reopen + S-B-1 writings pin (t604u)
Date: 2026-10-24 ~23:07 CDT (America/Chicago). Residual-vs-Resonant lock. Flag only; no PASS/FAIL altered; no physics invented.

## Hash
- BRIDGE_C_35/pins/G1_REOPEN_AND_S_B1_WRITINGS_2026-10-24.md sha256 6c66dbc0ba675976805178c65697f38e805fd7078f28f353877ee9eba4742ab2 — MATCH expected (1452 B).
- pins/SHA256SUMS -c: 6/6 OK (re-checked).
- order74 RESULTS: ABSENT (find over /workspace/quantum-comp) → HOLD.

## Claim verdicts
1. G1 — VERIFIED as stated. Pin says "gate review **opened**", "Ξ stays HOLD until the note is accepted", "Residual core not reopened". No PASS claim anywhere → no overclaim. G1 status remains **REJECT (640da80d…) binding** until accept note + gate decision. G1 = opened ≠ PASS.
2. B / sgn(0) / trunc — PARTIAL. Written: B(v,w)=v^T M w; sgn(0):=0; "Degree truncation"; numeric C = P̂_orth − H_s "unblocked". Gaps (flag N-SB1-1): M not defined/cited in pin; truncation degree/rule not specified; prior watch asked for B(c,v) — pin gives generic (v,w), mapping to c not stated. Residual law C: OPEN (stated). CORE_FREEZE intact; maps separate (stated) — consistent.
3. T1–T4 — VERIFIED optional; pin explicitly "Do not close residual law for C".
4. Ω/F tables — NOT SATISFIED. Pin itself says "full table bodies not in this chat extract". NONLOCAL_QM_EH11D/inventory_check/CODEX_FTOTAL_STRUCTURE.md (sha 924ab237…) FOUND but contains only the F-term written-form structure table (F_Coulomb^rel/F_SO/F_torsion/F_flux/F_leak) with Ω₁₁D unvalued and params listed unwritten; states "Numeric Ω₁₁D value … ABSENT". No hashed "channel table" or "component table" body found (rg over NONLOCAL_QM_EH11D, BRIDGE_C_35). Full tables: **ABSENT**. → **W-PO-2 stays OPEN** (+N-PIN-CONF-1).
5. W-PO-3 — chat provenance t604u only; Drive/paper ABSENT; pin itself says flag clears only when original supplied. → **W-PO-3 soft-inherited OPEN**.
6. S-B-1 — Recommendation: **keep OPEN pending order74 ingest**. Pin-only text does not clearly satisfy written-B need (M undefined, truncation degree unspecified, B(c,v) mapping implicit). Status: S-B-1 OPEN (watch, advanced: written sgn(0) and B-form shape now on record).

## Notes
- N-SB1-1 (new, soft): define M, truncation degree, and c-mapping for B before numeric C is computed in order74.
- N-G1-1 (info): "unblocked" for numeric C does not alter G1 REJECT or READY NO.
- Codex hunt (soft): table bodies to be attached/hashed if they exist outside workspace; none found locally.

## Open set
W-NL-1, W-NL-2, W-PO-2 (+N-PIN-CONF-1), W-PO-3, W-PIN-3 watch, S-B-1 watch (+N-SB1-1). W-PO-1 CLOSED. order73 OK. order74 HOLD (RESULTS ABSENT). 0 blockers.
