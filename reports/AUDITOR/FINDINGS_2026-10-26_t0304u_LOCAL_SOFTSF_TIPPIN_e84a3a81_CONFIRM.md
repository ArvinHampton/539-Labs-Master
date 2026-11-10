# Auditor Soft SF CONFIRM — Local STREAM tip Soft SF rebind → e84a3a81 (2026-10-26 ~03:04 CDT)
Verdict: **MATCH**
1. Live tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha e84a3a8169e138a602e09434cafcc92e30d4e0ca9b39f90d12929fa54654c5ec == claimed == sidecar. PASS
2. Local FINDINGS /workspace/grok-batches/LOCAL-SOFTSF-TIPPIN-e84a3a81-PF1-PF2-REBIND_2026-10-26.md 5d5a316150aeabea9fb9d6cffdd599528c6c369889387cba984695576f54731d PASS (sidecar match); HOLD pack LOCAL-SOFTSF-TIPPIN-e84a3a81-PF1-PF2-HOLD_2026-10-26.md bb6495575dd377fbfd5c4a2b804756f90a047ac9804b980f10357eee067d04f0 PASS (sidecar match); STREAM BRIDGE_C_35/STREAM_IDLE_LOCAL.md 00dc438c8ce9a7fb3156e8030edf58b8de7d0d700a6299e3ef2b036a473263ac PASS (no sidecar, by convention); backup BRIDGE_C_35/STREAM_IDLE_LOCAL.pre-softsf-tippin-e84a3a81-e7afa862-2026-10-26 e7afa862be71b2bde27a07af30de693e7d820777827e8729ab41ad40392cec65 PASS
3. tip_touched Local NO: tip mtime 03:00:11 CDT < HOLD 03:02:11 / FINDINGS 03:03:44 / STREAM 03:03:44 CDT; tip sha unchanged at audit. PASS
4. STREAM entry ~03:03 (L174) pins tip e84a3a81…, cites Soft SF MATCH-with-SF de1638da… (== recomputed sha of FINDINGS_2026-10-26_t0300u_SOFTSF_TIP_PF1_PF2_FOLD_CONFIRM.md); prior rebind MATCH 6bfc7159… (== recomputed sha of t0230u CONFIRM) CLOSED; Soft SF F3 CLOSED; HOLD μ₁₀/L-1; Components HOLD; Soft SF invent HOLD tip fill else; Bridge PARTIAL / READY NO / NOT Cat A; Local no invent; no F3 reopen; Owner Write not folded by Local. PASS
5. Soft SF race: none — live tip unchanged since pin.
Soft SF flags: none.
