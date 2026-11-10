# PR1 FINDINGS — OBSERVATIONAL-ONLY P3-path prerequisite checklist (Rule-3 CONTINUE; PM: Continue HEPP COOK) — 2026-10-26
Soft SF · Write-only · Author: PR1 · Partner: NL (Rule-5) · Route: Soft SF → Auditor · tip_touched NO · Kerr BLOCKED · nine-only

## §0 Authority (live sha256sum before writing; all match → no abort)
| Doc | sha256 (live) |
|---|---|
| Tip Soft SF LOCK (READ-ONLY) `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |
| Catalog (READ-ONLY) `/workspace/obs-data-PR1-HEPP-QM-GR.md` | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d |
| MIXED prereq method mirror (MP) `PR1-FINDINGS-MIXED_OBS_MODEL_MAP_PREREQUISITES_2026-10-26.md` | 3f0061e0542f48f7a7df4ba44f88b0e49ff453c693fecae7b7ebcabfb32ee330 |
| Resume FINDINGS (RS) `PR1-FINDINGS-HEPP_QM_GR_LAB_OBS_MATCH_RESUME_COOK_2026-10-26.md` | 5cd1174c17e1f0a131c0213a4a41c814b221917424fe9c6e75d7d4393cbf8483 |
| §2A/§2G FINDINGS (AG) `PR1-FINDINGS-HEPP_QM_GR_LAB_MODELOUT_ABSENT_2A_2G_2026-10-26.md` | 41e91352864d34a3b68c02f80f268749ef829f8200bbaebcaff1b00306eabee6 |
| §2F FINDINGS (2F) `PR1-FINDINGS-HEPP_QM_GR_LAB_MODELOUT_ABSENT_2F_2026-10-26.md` | dbfd82821129d05aaa7bc33319c1c182abc8dc88911277cfe4138701e46d0a1c |
| Ten-slots (TS), Rule-4 re-scope, INCONCLUSIVE | cited via RS §0 L9, L16, L18 (60dd4ad2…, 788d765e…, 8e6d0b8a…); not re-hashed here |

Path hygiene: any oct17-master reference resolves under `/workspace/quantum-comp/oct17-master/...` (none needed here).

## §1 Charge
Rule-3 CONTINUE. The PM directive is to continue the HEPP COOK. This document complements MP (3f0061e0…), which covered MIXED rows. Scope here: catalog rows classed **OBSERVATIONAL-ONLY** in RS §4, AG §4 or 2F §4, across §2A–§2G. MIXED, DERIVABLE and Kerr rows are out of scope. For each selected row I list which Written data/source landings exist and which are still ABSENT before the row could enter match **without** a MIXED observable↔model map.

## §2 Holds
- Auditor Soft SF CONFIRM is **CLEARED** (~19:21 CDT). This lane proceeds under Rule-3 CONTINUE.
- Tip 7cddb188… READ-ONLY. Catalog 6c680789… READ-ONLY. No fold, no edit.
- Kerr / Path4 C2–C3 BLOCKED. Kerr rows are excluded, as listed in RS L73: §2B L47–52, EHT/ISCO L61–75, GP-B L191. Spin-quadrupole and ringdown clauses inside L55 are not used.
- χ² slots (a)(b)(c) are ABSENT (TS via RS L29). Rule-4 stays INCONCLUSIVE (8e6d0b8a…).
- Gap-X1 is OPEN (Local↔PR2). It is not cited, closed or invented here.
- Owner-reserved MIXED Writes (the observable↔model maps in MP §6 / 2F L68) are **not** invented, drafted or implied. No χ², coefficients, data values or predicted values are written here.
- Nine-only roster. No messaging.

## §3 Method (adapted from MP §3)
I dropped the map-owned MP cells (P1 model-output identity, P2 coefficient coverage and P4 time/domain map), because they belong to MIXED rows. I kept the data-side cells and the match gate:
- **P3a — Named source:** does the catalog line itself name an external dataset or a PDG/CODATA/primary-paper citation? I checked this by reading the catalog line.
- **P3b — Numeric observable + uncertainty Written:** does the catalog line carry a value with a stated uncertainty, or a stated-CL bound? I only checked whether these are present; no digits are transcribed. A value given only as an order of magnitude, or with no uncertainty, counts as ABSENT.
- **P3c — Model-side predicted value Written anywhere:** cited from the prior "Written model output" column (RS L54–70, AG §4, 2F L48–54). Every row there is ABSENT, and nothing is re-invented.
- **P3d — Match-entry gate:** could P3a+P3b alone suffice once a model output lands? It is ABSENT if any other named prerequisite is still unwritten. Two such prerequisites apply to every row:
  - (i) the RS B4 (L37) / 788d765e… finding that 0 catalog rows are Rule-4-eligible without an Owner re-scope;
  - (ii) the χ² slot (b) dof / statistic definition, which is ABSENT (RS L34).
  In addition, RS §5.2 (L81) requires an Owner observable↔model statement for **any** §4 row, including OBSERVATIONAL-ONLY rows. This is not a MIXED map, but it is still an unwritten identity of which output is compared with which observable.

Legend: CLOSED = Written in the catalog at the cited line. ABSENT = no Written source (proved by the cited inspection). UNPROVEN-GAP = partially Written, so sufficiency is undecided.

## §4 Table (labels + line refs only; no values)
| Row (src) | Observable (catalog L#) | P3a source | P3b value+unc | P3c model value | P3d gate | Leave ABSENT-for-match? |
|---|---|---|---|---|---|---|
| #3 (RS L54) | GWTC-3 TGR hierarchical PN (L55–56) | CLOSED (arXiv:2112.06861, L55) | CLOSED (asymmetric errors / 90% bounds, L55–56) | ABSENT (RS L54) | ABSENT (B4; slot (b)) | YES |
| #4 (RS L55) | GWTC-4.0 graviton mass / dispersion (L57, L59–60) | CLOSED (arXiv:2603.19020, L57/L59) | CLOSED (90% UL, L57); L59 qualitative only | ABSENT (RS L55) | ABSENT | YES |
| #5 (RS L56) | Photon mass/charge bound (L86) | CLOSED (PDG Live/2025, L86) | CLOSED (stated bounds, L86) | ABSENT (RS L56) | ABSENT | YES |
| #7 (RS L58) | Electron a_e (L94) | CLOSED (Fan 2023; CODATA 2022, L94) | CLOSED (parenthetical unc., L94); SM comparison CONTESTED (L94) | ABSENT (RS L58) | ABSENT | YES |
| #11 (RS L62) | H Lamb shift (L116) | CLOSED (CODATA 2022 input table, L116) | CLOSED (multiple inputs with unc., L116) | ABSENT (RS L62) | ABSENT; which input to use is also unselected (UNPROVEN-GAP) | YES |
| #12 (RS L63) | W boson M_W (L128–131) | CLOSED (PDG Live, L128) | CLOSED (± stated, L128) | ABSENT (RS L63; PREREG T16 rejected RS L46) | ABSENT | YES |
| #13 (RS L64) | Higgs M_H (L136) | CLOSED (PDG Live, L136) | CLOSED (± stated; Γ_H SOFT, L136) | ABSENT (RS L64) | ABSENT | YES |
| #14 (RS L65) | α_s(M_Z) (L140) | CLOSED (PDG QCD review, L140) | CLOSED (± stated, L140) | ABSENT (RS L65) | ABSENT | YES |
| #15 (RS L66) | Stability/EDM/μ→eγ null bounds (L155–161) | CLOSED (PDG 2025 / primaries, L156–158) | CLOSED (90% CL bounds); block tagged [SOFT] (L155) | ABSENT (RS L66) | ABSENT | YES |
| #16 (RS L67) | Mercury perihelion (L164) | CLOSED (Will 2018; PDG §21, L164) | UNPROVEN-GAP: observed anomaly given as "≈" with no Written unc.; the β sub-row carries ± (L164) | ABSENT (RS L67) | ABSENT | YES |
| #17 (RS L68) | VLBI/Cassini γ (L166–169) | CLOSED (A&A 2011; Nature 2003, L167–168) | CLOSED (± stated, L167–168) | ABSENT (RS L68) | ABSENT | YES |
| #18 (RS L69) | Clocks / redshift / Ġ/G (L170–176) | CLOSED (Delva 2018 et al., L172) | CLOSED (± 1σ, L172) | ABSENT (RS L69) | ABSENT | YES |
| #19 (RS L70) | MICROSCOPE / Eöt-Wash η (L177–180) | CLOSED (PRL 2022; PRL 2008, L178–179) | CLOSED (stat/syst, L178–179) | ABSENT (RS L70) | ABSENT | YES |
| A3 (AG §4) | Borexino ⁷Be flux (L27) | CLOSED (Borexino Phase-II, L25) | CLOSED (stat/syst, L27) | ABSENT (AG §4 A3); L29 SSM values are explicitly "not measurements" and not model output | ABSENT | YES |
| A5 (AG §4) | CNO detection + Phase-III (L32–35) | CLOSED (Nature 587, 577, L33) | CLOSED (asymmetric unc., L33); MSW assumed | ABSENT (AG §4 A5) | ABSENT | YES |
| A6 (AG §4) | SNO ⁸B NC flux (L36) | CLOSED (PRC 88, 025501, L36) | CLOSED (stat/syst, L36) | ABSENT (AG §4 A6) | ABSENT | YES |
| A8 (AG §4) | LUNA d(p,γ)³He S-factor (L39–40) | CLOSED (Nature 587, 210, L39) | **ABSENT** (no numeric value in the catalog, L39) | ABSENT (AG §4 A8) | ABSENT (also needs P3b landing) | YES |
| G1 (AG L57) | Electron b̃ sensitivities (L232) | CLOSED (K&R arXiv:0801.0287, L229) | **ABSENT** (orders of magnitude only, L230; lossy extraction, L235) | ABSENT (AG L57) | ABSENT (also needs P3b landing) | YES |
| G4 (AG L60) | Photon isotropic k_(V)/c_(I) (L233) | CLOSED (L229) | **ABSENT** (orders only, L230/L235) | ABSENT (AG L60; t1118u γ rejected) | ABSENT (also needs P3b landing) | YES |
| F4 (2F L48) | Classical radius r_e (L214) | CLOSED (CODATA 2022, L214) | CLOSED (parenthetical unc., L214); a derived constant, not a measured size | ABSENT (2F L48) | ABSENT; UNPROVEN-GAP whether a derived constant is a match target at all | YES |

Not selected: the remaining OBSERVATIONAL-ONLY rows #10, A4, G2, G3, G5, F6, F7 and F10. F6 duplicates #15 (EDM d_e, L157/L216) and F10 points to §2C. They are excluded only to keep the rows distinct; they are not re-classed.

## §5 Result counts (PROVED by cite/inspection)
- Rows: **20** (RS 13, AG 6, 2F 1). All are OBSERVATIONAL-ONLY, non-Kerr and distinct.
- Cells: 80 (4 × 20).
- **P3a CLOSED 20/20.**
- **P3b:**
  - CLOSED 16/20.
  - ABSENT 3/20 (A8, G1, G4).
  - UNPROVEN-GAP 1/20 (#16).
- **P3c ABSENT 20/20.** No Written model prediction exists for any row (RS L75; AG L68; 2F L63).
- **P3d ABSENT 20/20.** P3a+P3b are not sufficient for any row, because B4 re-scope and slot (b) are still unwritten even if a model output lands.
- Overall cells: CLOSED 36/80; ABSENT 43/80; UNPROVEN-GAP 1/80.
- **Rows able to leave ABSENT-for-match: 0/20.** The data side is largely landed (P3a+P3b both CLOSED for 16/20). What blocks these rows is the model side and the match gate, not the observational data.

## §6 Recommendations (Owner data landings only; no maps invented)
1. Owner/PR1 data landings that do not need any map:
   - A8: Write the LUNA S-factor value with its uncertainty from the cited primary.
   - G1/G4: Write per-cell values verified against the K&R PDF, as the L235 caveat requires.
   - #16: Write the observed perihelion anomaly uncertainty from PDG §21 or Will LRR.
   Each of these is a catalog edit, so it is Owner/catalog-owner gated. PR1 did not make them.
2. Owner: Write the Rule-4 re-scope (RS B4 / 788d765e…) and the slot (b) statistic/dof definition. These are the P3d gates shared by all 20 rows.
3. Lamb #11: Owner selection of which CODATA input row is the match target.
4. Model-side P3c stays with the Owner. Nothing is proposed here.
5. Soft SF → Auditor. NL Rule-5 REVIEW, mirroring c46d970f….

## §7 tip_touched NO
The tip was re-hashed after writing (7cddb188…, unchanged) and the catalog was not modified (6c680789…). Kerr BLOCKED and not touched. Nothing was invented: no map, χ², dof, coefficient, data value, predicted value, Gap-X1 cite or MIXED Write. Nine-only.
