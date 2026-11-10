# PP-FINDINGS — AUDIT of Local completed G-vi-1 proof attempt
Soft SF · Write-only · Author Professor Proof · REPORTS · No RECS · tip_touched NO · Kerr BLOCKED · OW 3e2b924a… Local Path work only · AUDIT-only (not first-prove) · 2026-10-28 (CDT)

## §0 Live sha table (recomputed 2026-10-28 ~01:08 CDT)
| Item | sha256 | Result |
|---|---|---|
| tip Soft SF LOCK | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | cited as lock id; untouched (tip_touched NO) |
| Packet FINDINGS_LOCAL_GVI1_COMPLETED_PROOF_ATTEMPT_FOR_PP_AUDIT_2026-10-27.md | 9fd345b3f05c54ea2ebb5cf08f5231ea4ceb8cfe8fdf661ccfecb2ed508cadd2 | MATCH |
| Packet PRESS SOFTSF_PRESS_FINDINGS_LOCAL_GVI1_COMPLETED_PROOF_ATTEMPT_FOR_PP_AUDIT_2026-10-27.md | 8a8882e214ecafbead5cba690d264ad755dcceb10134316e59d7eab93fc39165 | recorded (no expected given) |
| G-vi-1 canon (invent-pending) | 480f6d7298face1e9b15b51fd3d747a83b5c7384556721fcdae80994d4e1344d | MATCH |
| Local proof-pursuit attach | dccf3a8c0369985062f44fabb615e0d357d181f7218af99d0b093f49c43dc43c | MATCH |
| Cite-grounded deepen | 40b5fd6726528ef6f3fcae5f482d337eb95035933f9aac32a1c4f138ca42a23b | MATCH |
| Written asymptotic class | b19e12e6c313c98c40e28ce406ec08b3796fe8b0ad0f87a13365da1891c2d949 | MATCH |
| OW Local asymptotics APPROVED | 6081e5ac817cfb4e67c4562f59b3d1f32e718606183def768a828582450c1b00 | MATCH |
Lane authority cdab6ac5… cited in packet: not re-hashed (not in audit cite list).

## §1 Audit verdict per target
| Target | Local label | PP audit | Why |
|---|---|---|---|
| P1 N_s=4s | NOT-FEASIBLE-PENDING | CONFIRM | No ĝ_s transformation law on disk (Rank27); level not derivable. |
| P2 m_s=1, Δ=1/24, pole ∞ only | PARTIAL | CONFIRM (lean NARROW) | Δ=1/24 cite-grounded only for s=1 template f; deepen 40b5fd67 itself flags Δ may scale to s/24 — "PARTIAL" is the most that holds; no part proven for g_s. |
| P3 β_s=π/(2√6·s) | PARTIAL | NARROW | Only the generic law β=4π√Δ/c is met; deepen shows c_min ≠ level on the template (c_min=2), so the specific formula has no support beyond algebra. Label honest only read as "law met, value unsupported". |
| P4 α=−1/2 | MET (conditional) | CONFIRM with caveats | See §1a. |
| P5 A_s=1/√(8s) | PARTIAL | NARROW | Prefactor law 1/√(2c) verified on f with c=2; a(−Δ)=1, \|K\|=1, c=4s for g_s all unproven. Specific value unsupported. |
| PROVED count | 0 | CONFIRM | No target proved; none claimed. |

### §1a P4 question — does b19e12e6 / 40b5fd67 support α=−1/2?
YES, with caveats. b19e12e6 Written states the growth **class** only (a_s(n) ∼ A_s n^α e^{β_s√n}) and explicitly does NOT assign α. The value −1/2 comes from deepen 40b5fd67 (L4 weight-k exponent (k−1)/2−1/4 with Written k=½) and is checked on the template f (Dragonette/Andrews n^{−1/2}). Conditions the packet should state in full: (i) ĝ_s is a weight-½ harmonic Maass completion; (ii) nonzero principal part; (iii) the dominant Kloosterman term does not cancel (template shows c=1 cancels — non-vanishing of leading term is an extra hypothesis); (iv) the asymptotic may hold only along the support subsequence (e.g. n≡0 mod s if g_s=f(q^s)) and for |a_s(n)| up to sign. Packet names only (i)/(ii) via the cites — condition-set incomplete, label not overclaimed.

## §2 Overall
Soft SF audit CONFIRMS Local's PROVED=0 table. No REJECT-label. Label narrowings: P3 and P5 PARTIAL = "general law matched; specific s-dependent value unsupported"; P4 MET is conditional on (i)–(iv) above, not on b19e12e6 alone. Consistency note: later Local invent 05f6bf59… (g_s:=f(q^s)) yields Δ_s=s/24, β_s=π/√(6s), conflicting with canon P2/P3/P5 values — reinforces that P2/P3/P5 must not be upgraded. No hash FAIL.

## §3 Disposition
Soft SF → Keeper (Auditor). Pursuit dccf3a8c stays OPEN; Local may retry where-feasible when ĝ_s transform appears on disk or Owner lifts a named cite. Canon 480f6d stays invented pending proof. No tip text, no fold, Kerr untouched, Local files not amended.
