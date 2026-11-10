# PR1 FINDINGS — DERIVABLE-class obs-match checklist (Rule-3 CONTINUE COOK, reports-only) — 2026-10-26
Soft SF · Write-only · Author: PR1 · Partner: NL (Rule-5) · Route: Soft SF → Auditor · tip_touched NO · Kerr BLOCKED · nine-only · Soft SF CONFIRM CLEARED

## §0 Authority (live sha256sum before writing; all match → no abort)
| Doc | sha256 (live) |
|---|---|
| Tip Soft SF LOCK (READ-ONLY) `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |
| Catalog (READ-ONLY) `/workspace/obs-data-PR1-HEPP-QM-GR.md` | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d |
| MIXED complement (MP) `PR1-FINDINGS-MIXED_OBS_MODEL_MAP_PREREQUISITES_2026-10-26.md` | 3f0061e0542f48f7a7df4ba44f88b0e49ff453c693fecae7b7ebcabfb32ee330 |
| OBS-ONLY P3 complement (OP) `PR1-FINDINGS-OBSERVATIONAL_ONLY_P3_PATH_PREREQUISITES_2026-10-26.md` | 72c599849403e2b99c6acba6815756c38b60129b9031c3d1147dc61bf844c146 |
| GAP-X2 NL table, amended (GX) `bridges/NONLOCAL_QM_EH11D/FINDINGS_NL_GAP_X2_SYMBOL_OWNERSHIP_TABLE_2026-10-26.md` | 02abbc69c333c3ea90b8813cb4cd582e68ff32869680d14779fb8a9f139bc842 |
| PR1 Rule-5 REVIEW of GX (RV) `PR1-RULE5_REVIEW_NL_GAP_X2_SYMBOL_OWNERSHIP_2026-10-26.md` | 405f45e6a8092b62e618e2e264914152f678890c4e8d361d5fe593f515a42e4f |
| Resume (RS) `PR1-FINDINGS-HEPP_QM_GR_LAB_OBS_MATCH_RESUME_COOK_2026-10-26.md` | 5cd1174c17e1f0a131c0213a4a41c814b221917424fe9c6e75d7d4393cbf8483 |
| §2A/§2G (AG) `PR1-FINDINGS-HEPP_QM_GR_LAB_MODELOUT_ABSENT_2A_2G_2026-10-26.md` | 41e91352864d34a3b68c02f80f268749ef829f8200bbaebcaff1b00306eabee6 |
| §2F (2F) `PR1-FINDINGS-HEPP_QM_GR_LAB_MODELOUT_ABSENT_2F_2026-10-26.md` | dbfd82821129d05aaa7bc33319c1c182abc8dc88911277cfe4138701e46d0a1c |
| Alias/axiom-N/script↔7D (AL) `PR1-FINDINGS-E_LEAK_ALIAS_AXIOM_N_SCRIPT7D_MAP_2026-10-26.md` | 84b21c4cd9cde78e043577943e1713bc269a029c55cff582b2901354a87ef967 |
| NL-GS-INDEX-01 (GI) `bridges/NONLOCAL_QM_EH11D/WRITE_NL_GS_INDEX_01_INDEPENDENCE_PURSUE_2026-10-26.md` | 4212ae4dc3564fbe52963047e19f8b2a5da87dd54e1258d4335b4c7bfa0568fe |
| GAP-I-A adequacy (IA) `bridges/NONLOCAL_QM_EH11D/WRITE_NL_GAP_I_A_ADEQUACY_DEF_NL_GS_IND_8_2026-10-26.md` | d1eed178cf912cf6a73071e5a1d5e849df41c7864712d087f38bf75b5e8cdc42 |
| GAP-I BCD deepen (BD) `bridges/NONLOCAL_QM_EH11D/WRITE_NL_GAP_I_BCD_X_M_W_PHI_DEEPEN_2026-10-26.md` | 815116c8d403420f83331db0d872d090dc4b52fa1fabd5c84751be95fa7062ba |
| ZX UNLINK (ZX) `bridges/NONLOCAL_QM_EH11D/WRITE_NL_ZX_MAP_01_PHI_IOTA_OR_UNLINK_2026-10-26.md` | 263e5a5b5b905f90d763091ab6d9d748b080424b5dac6dd01ab18b60f4cee855 |

Path hygiene: oct17-master would resolve under `/workspace/quantum-comp/oct17-master/...`; none needed here.

## §1 Charge
Rule-3 CONTINUE COOK, reports-only. PM: next observational slot without inventing anything; Soft SF stamp on every ABSENT/PARTIAL leaf; no RECS. Scope: rows classed **DERIVABLE(-UNDER-PROOF)**. MIXED (MP), OBSERVATIONAL-ONLY (OP) and Kerr rows are out of scope.

## §2 Holds
- Tip and catalog READ-ONLY; tip_touched NO.
- Kerr / Path4 C2–C3 BLOCKED; not loaded.
- I invent no maps, χ², coefficients, data, Gap-X1, MIXED Writes or derived numeric predictions.
- Labels and line refs only. No messaging.

## §3 Method
1. Source set. `grep -c DERIVABLE` gives 0 on the catalog, RS, AG and 2F, so they carry no DERIVABLE tags. The only DERIVABLE set in the corpus is GX §3 (class definition at GX L29; counts at GX L97: DERIVABLE-UNDER-PROOF 7 of 60). RV L25 re-counts 60 = 41 + 12 + 7 and gives PASS. OP L18 confirms that DERIVABLE was excluded from the OBS-ONLY scope.
2. The 7 rows are GX L52 (row 17), L89 (54), L90 (55), L91 (56), L92 (57), L93 (58) and L95 (60).
3. Each row was checked against the Written corpus with rg over reports/ and bridges/NONLOCAL_QM_EH11D for later Writes. The cites are GI, IA, BD, ZX and AL. Nothing was carried in from outside the corpus.
4. Derivation status values: YES = a Written chain fully discharges the row; PARTIAL = some Written proof exists but a named gap remains; ABSENT = there is no Written chain.
5. Match status: CLOSED only when a Written derived output has been compared with Written observational data. GX classes DERIVABLE rows as needing "no observational number" (GX L29), so a row can only enter match through a MIXED or OBS row's map. Those maps are ABSENT per MP.

## §4 Table
| # | Identity (label + cite) | Claimed derivation path (Written only) | Written derivation? | Obs-match status | Soft SF stamp |
|---|---|---|---|---|---|
| D1 | g_s index s / s-independence — GX row 17, L52 | NL-JOIN-1 946a5910… P1 identity under LOCK e41ceac4…, with s∈{7,8,11} per 7ab9a254… (GX L52). GI gives the annihilation condition and Lemmas I3/I4 under candidate DEF NL-GS-IND-8 (GI L3, L44–L50). IA L3: GAP-I-A adequacy is still UNPROVEN-GAP | **PARTIAL**: the identity is proof-backed; the adequacy of independence is UNPROVEN-GAP (IA L3); there is no Owner pick of s | ABSENT-for-match: numeric ABSENT (GX L52 "unlock §3(iii)") | **Soft SF: PARTIAL (derivation) / ABSENT (match)** |
| D2 | Residual weight map w(g_s, X^M) — GX row 54, L89 | ABSENT. GX L89: UNPROVEN-GAP; w≡1 is INVENT-under-lift, sheet-only. GI L28: ABSENT. BD L22 (K4): no Written w anywhere outside NL gap-naming | **ABSENT** | ABSENT-for-match | **Soft SF: ABSENT / ABSENT** |
| D3 | Residual↔NL map (DESIGN item 5) — GX row 55, L90 | Join LOCK 7588bc8f… + NL-JOIN-1 946a5910… P2, structural only (GX L90) | **YES (structural only; no numerics)** | ABSENT-for-match: no Written numeric output or observable attached (GX L90 "no numerics") | **Soft SF: ABSENT (match)** |
| D4 | Alias table (δ/δ(t), Δ/ΔE, Ω/Ω_11D, τ/τ^-, T/T_rad, shared τ/L/v_0) — GX row 56, L91 | AL classes the pairs under axioms N/N′ only (e.g. AL L41–L42 "DISTINCT-under-N"). The axioms are not Owner-Written (GX L91) | **ABSENT** unconditionally; the conditional-under-N classifications exist (AL) | ABSENT-for-match; exact k_min is UNPROVEN-GAP (GX L91) | **Soft SF: ABSENT / ABSENT** |
| D5 | Script↔7D term map (corrected_E_leak.py a7865388…) — GX row 57, L92 | AL §4 map: no script term is PROVED to instantiate a 7D term. Product-vs-sum and E5 non-correspondences are PROVED (AL L56, L62). term4 target has two candidates, UNPROVEN (AL L57) | **PARTIAL**: the negatives are proved; there is no positive map | ABSENT-for-match: script literals are not Written values (GX L92, AL L62) | **Soft SF: PARTIAL / ABSENT** |
| D6 | z↔x map + reverse-parity involution (RPPT↔δ_W₇) — GX row 58, L93 | ZX Written UNLINK NL-ZX-01: no φ, no ι (ZX L25). R1 corpus absence (ZX L29). Re-link is named GAP-ZX-R (ZX L42). GX L93: negatives T2.1/T2.2/T2.4 are proof-backed | **PARTIAL**: UNLINK and the negatives are Written; the map itself is ABSENT by Written choice | ABSENT-for-match: no z→x route may carry a statement or stratum (ZX L25) | **Soft SF: PARTIAL / ABSENT** |
| D7 | MC provenance (seed, N_samples, integrator/tol, SymPy ver) — GX row 60, L95 | ABSENT. GX L95: UNPROVEN-GAP (f82989d7… T3.4), schema choice; placeholders allowed, values not | **ABSENT** | ABSENT-for-match | **Soft SF: ABSENT / ABSENT** |

## §5 Counts
- DERIVABLE rows: 7 (GX L97; RV L25 PASS). Catalog/RS/AG/2F DERIVABLE tags: 0.
- Written derivation: YES 1 (D3, structural only); PARTIAL 3 (D1, D5, D6); ABSENT 3 (D2, D4, D7).
- Obs-match: CLOSED 0; PARTIAL 0; ABSENT-for-match 7.
- Soft SF stamps applied: 7 of 7 rows. That is 6 derivation stamps (3 PARTIAL + 3 ABSENT) and 7 match ABSENT stamps.
- Next observational slot without invention: **none in the DERIVABLE class.** None of the 7 rows carries an observable, so a match needs a MIXED map (ABSENT per MP) or OBS data (ABSENT per OP).

## §6 Leaves for Soft SF (listed, not ranked; no RECS)
- PARTIAL: D1 g_s s-independence adequacy (GAP-I-A); D5 script↔7D positive map; D6 z↔x re-link (GAP-ZX-R).
- ABSENT: D2 w(g_s, X^M); D4 alias table / Owner-Written axioms N, N′; D7 MC provenance values.
- ABSENT-for-match: D1–D7 (all).

## §7 Explicit
- tip_touched **NO** (tip 7cddb188… verified before and after the write).
- Catalog 6c680789… unchanged. Kerr BLOCKED, not touched. Nine-only. No messaging. Soft SF CONFIRM CLEARED.
