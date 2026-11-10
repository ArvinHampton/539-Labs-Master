# PR1 FINDINGS: Rule-4 χ² ingest PREPARE (Rule-4 HOLD LIFTED), 2026-10-26
Status: Soft SF, write-only, cite-only. This is a prepare/ingest status. It is not a χ² recompute.
**Verdict: PREPARE. Slots (a)(b)(c) are still ABSENT. Ingest surface ready = YES. Decisive recompute NOT RUN. Prior INCONCLUSIVE stands. No χ² numbers, data points, dof or coefficients were invented.**

## 1. Authority (live sha256, verified 2026-10-26 ~17:25 CDT America/Chicago)
| Doc | Path | sha256 |
|---|---|---|
| OW LIFT ALL + PURSUE ALL | reports/OWNER_WRITE_LIFT_ALL_HOLDS_PURSUE_ALL_LANES_2026-10-26.md | 6bc5f5ab5e855b7aab79e25691e97932cd57e71a7fbf790c8b5c29adf451d917 (MATCH) |
| ASSIGN PR1+NL | reports/ASSIGN_PR1_NL_RULE4_HOLD_LIFTED_PURSUE_2026-10-26.md | ef77ea156c372b440df52d1dd4671aeae4dfba61b88f8ba1fc4b1d903955b5e3 (MATCH) |
| NL resume pack | reports/bridges/NONLOCAL_QM_EH11D/ASSIGN_PACK_NL_PR1_RULE4_HOLD_LIFTED_RESUME_2026-10-26.md | 6e26e1e278ab3ba8ec73d7dc6cc55a413c516eb0ef72f97b7246d7e175adba78 |
| Superseded park CLOSED_A | reports/OWNER_WRITE_CARD_PR1_RULE4_AFTER_UNLOCK_ABSENT_CLOSED_A_2026-10-26.md | 6d20f74c6218143709d1a0c7fbc2f5500cb14e9f28d3807e14b24647f0376ccb |
| Prior unlock FINDINGS | reports/PR1-FINDINGS-RULE4_CHI2_INPUTS_UNLOCK_2026-10-26.md | ae0bf4df80c1192a1b23a5fa56fcfc65325ca843e97587d734397a21af791eaa (MATCH) |
| NL Rule-5 relay | reports/bridges/NONLOCAL_QM_EH11D/NL_RELAY_PR1_RULE4_CHI2_INPUTS_UNLOCK_2026-10-26.md | d9aa7ab16a98a31de10f96380262ec16f1d2196984f600c86aa352eec4e4bec6 |
| Prior INCONCLUSIVE | reports/PR1-FINDINGS-RULE4_HYBRID_MC_RECOMPUTE_2026-10-26.md | 8e6d0b8affda74855e6dc4d8af7de85bdafb053cc97d49f9b015cfae9501e2c1 (MATCH) |
| Runnable-spec | reports/bridges/NONLOCAL_QM_EH11D/WRITE_NL_HYBRID_MC_RUNNABLE_SPEC_POST_JOIN_PASS_2026-10-26.md | 27058bad386fc64dff071324e4f4d248a60113c68349917b42656c93025fe980 (MATCH) |
| Sheet params | reports/bridges/NONLOCAL_QM_EH11D/WRITE_NL_RR_NL_SHEET_01_PARAMS_2026-10-26.md | da91ad83ac35a2f3a897dbd1794b90d102b409284012b889d6b74849e3af5998 (MATCH) |
| Corrected 7D A27 | reports/s_family_paths/A27_drive_review_complete/txt/12RM_gft3rNFqCqYoBEsHUvPtDlpIN_lq5YvVu1P8dLY.txt | 4758d180f467a35d139833711029ac4121fa98d79bb3129be1b579d8254250b1 |
| Catalog (read-only, not touched) | /workspace/obs-data-PR1-HEPP-QM-GR.md | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d |
| tip Soft SF LOCK (not touched) | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |

## 2. Source-reconstruct inventory (Written material only)
| Slot | Status | Written basis |
|---|---|---|
| Frozen params ρ_DM=0.31, β_PBH=0.18, κ_dark=0.45, z=1…118 | LANDED | Sheet da91ad83… (cited, not re-litigated) |
| Hybrid-MC procedure | LANDED (procedure only) | Runnable-spec 27058bad… |
| (a) DESI/ATLAS points + errors behind the Doc χ²/dof target | **ABSENT** | Unlock FINDINGS §3(i): no data table exists in the corpus. 0.79 appears only as a hard-coded script constant (grok-files/corrected_E_leak.py, S211DM2ETX_…corrected.py) or as a chat label. |
| (b) dof tied to that fit | **ABSENT** | Unlock FINDINGS §3(ii). The CODATA ν=54/15 values come from a different fit and do not apply. |
| (c) full E_leak–F_friction coefficients (incl. g_s X^M numeric, E_b(z) table) | **ABSENT** | Unlock FINDINGS §3(iii). g_s X^M, E_b(z), E_z^-/Z_z^-/N_z^- tables and the remaining coefficient list are absent from every Written source. Corrected 7D A27 4758d180… gives structure only, with no numeric fit coefficients. |

Chat-only Category-B fragments (E_0, τ^-, σ_inh, δ(t), β_z, Ω_11D, void_η) are **UNUSED**. Script literals are **UNUSED** as coefficient substitutes.

Re-sweep after the unlock FINDINGS mtime: no new Owner-Written χ² inputs were found. The only new files are status/card/press files, and none of the new csv/json/tsv files carry data. **Newly landed inputs: NONE.**

## 3. Ingest surface (acceptance criteria)
An input is accepted only if all of the following hold:
1. **Provenance:** it is an Owner Write (OWNER_WRITE_* with a .sha256 sidecar) or an explicitly Owner-accepted corpus file named by path and sha in an Owner Write. Chat, Category-B and script literals are rejected.
2. **Integrity:** the live sha256 matches the sidecar and the cited sha. Re-verify at ingest time.
3. Per slot:
   - **(a)** Machine-readable or tabulated points, each with observable, z or bin, value and σ (or a covariance matrix). Sample (DESI DR-x / ATLAS Open Data release) and units must be named. The table must be the data set behind the Doc χ²/dof target.
   - **(b)** An explicit integer dof statement tied to (a): N_points minus N_fitted params, with the fitted-param list named. If (a) and (b) are inconsistent, reject.
   - **(c)** A complete E_leak–F_friction coefficient list with numeric values and units. It must include g_s X^M and the E_b(z) table over the z range of (a), and it must cover every symbol listed as ABSENT in unlock FINDINGS §3(iii). No conflict with frozen sheet params da91ad83… is allowed.
4. **Completeness gate:** the decisive Doc-full recompute per runnable-spec 27058bad… runs only when (a), (b) and (c) are all accepted. If any slot is PARTIAL or ABSENT, ship a Soft SF status and leave INCONCLUSIVE in place.
5. Output on gate pass: PR1-FINDINGS-RULE4_HYBRID_MC_DECISIVE_RECOMPUTE_2026-10-26.md → Auditor → NL Rule-5.

Ingest surface ready: **YES**

## 4. Status
- Decisive recompute: **NOT RUN** (inputs ABSENT)
- Prior INCONCLUSIVE 8e6d0b8a… **stands**
- tip Soft SF LOCK 7cddb188… **tip_touched NO**. The catalog was not touched.
- Soft SF invent HOLD lifted for **non-tip only**. Nothing was invented in this FINDINGS.
- Path4 Kerr physical-load **NO**. No Zwegers numerics.
- No Eigen/CRT edits. No messages sent.

Ships to Auditor → NL Rule-5.
