# PR1 FINDINGS — HEPP/QM/GR-lab model-output ABSENT, catalog §2F (Rule-3 CONTINUE after NL Rule-5 ACCEPT of MIXED prereqs) — 2026-10-26

## §0 Authority (live sha256sum before writing; all match)
- Tip Soft SF LOCK (READ-ONLY) `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91
- Catalog (READ-ONLY) `/workspace/obs-data-PR1-HEPP-QM-GR.md` = 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d (brief listed a truncated value; full live hash recomputed, prefix 6c680789… matches)
- Resume FINDINGS `PR1-FINDINGS-HEPP_QM_GR_LAB_OBS_MATCH_RESUME_COOK_2026-10-26.md` = 5cd1174c17e1f0a131c0213a4a41c814b221917424fe9c6e75d7d4393cbf8483
- §2A/§2G FINDINGS `PR1-FINDINGS-HEPP_QM_GR_LAB_MODELOUT_ABSENT_2A_2G_2026-10-26.md` = 41e91352864d34a3b68c02f80f268749ef829f8200bbaebcaff1b00306eabee6
- MIXED prereq `PR1-FINDINGS-MIXED_OBS_MODEL_MAP_PREREQUISITES_2026-10-26.md` = 3f0061e0542f48f7a7df4ba44f88b0e49ff453c693fecae7b7ebcabfb32ee330
- NL Rule-5 ACCEPT MIXED `NL_RULE5_REVIEW_PR1_MIXED_OBS_MODEL_MAP_PREREQUISITES_2026-10-26.md` = c46d970fa9d7f4bb8ea953f99f6059b59c6f74b4b3ad58f649af6c912779303c
- Rule-3 / ten-slots / free-pursue: cited via 41e91352… §0 (6b657e97…, 60dd4ad2…, cb43f7d1…).

## §1 Charge
Rule-3 CONTINUE (PM-directed) after NL Rule-5 ACCEPT (c46d970f…) of MIXED prereqs (3f0061e0…). Apply the resume §4 / 41e91352… method to catalog §2F (L197–229). Coverage then extends to §2A–§2G.

## §2 Holds
- Tip 7cddb188… READ-ONLY; catalog READ-ONLY. No fold.
- Kerr / Path4 C2–C3 BLOCKED. §2F holds no Kerr rows. L223 (v_GW=v_γ) is a propagation-speed bound, not ringdown.
- χ² slots (a)(b)(c) ABSENT (60dd4ad2…). Gap-X1 OPEN, not cited or closed.
- The Owner-reserved MIXED Writes (observable↔model maps named in 3f0061e0…) are not invented or drafted here.
- Nine-only roster.

## §3 Method
1. Header audit (L197): "mechanisms ABSENT (framing only)". Checked by inspection against the frame rows L198–209:
   - (a) L203 says "No dynamics Written".
   - (b) L204 says label only; strike/coupling ABSENT-with-Owner-hold.
   - (c) L205 says the exposure mechanism is ABSENT-with-Owner-hold.
   - (d) L206 says forcing energy and rates are not Written.
   - W4 L208 gives order only, with coefficients/rates OPEN.
   - Exact-c L198–199 says "No numerical observational prediction", "Pointers only".
   - A/B/C L200–201: h_i radius / exposure amplitude ABSENT; C ABSENT.
   - Rev.14 L225 (t1118u 39359cf7…): strike/coupling ABSENT.
   
   Header claim confirmed: L198–209, L225–229 are framing/pointer stubs with 0 Written model outputs. They are excluded from the table as non-measurable.
2. Measurable/bound rows selected: L211–217 (electron) and L219–224 (photon, ER–EPR). L226 is pointers only and L227 says "not cascade measurements", so both are excluded.
3. Corpus search: `rg` over quantum-comp/reports/OWNER_WRITE_* with the pattern `a_e|anomalous magnetic|d_e|EDM|photoelectric|Compton wavelength|g-2|m_e|electron (mass|rest)|m_γ|photon mass`.
   - Hits are AUDITOR_KEEPER_PURSUE_FIVE_MASTER_MUON_G2 L1/9/12/15. These are a pursue directive on *muon* g-2, and L12 itself says "do not assert … unless … rigorous derivation".
   - NL_BLOCK_PURSUE_OPEN_t1145u L16, NL_PURSUE_ALL_DEEPEN_t1133u L19 and NL_PURSUE_RESOLUTIONS_t2147u L56 cover ψ=1 in a muon g-2 context. They are normalisation notes, not an a_e prediction.
   - All are rejected: none outputs an electron/photon observable.
4. Observable↔model map search: `rg -l "observable.{0,20}(map|↔)"`. The only hit is NL_GAP_IA_UNLOCK_PURSUE_BCD_IA L35, which reads "observable↔model maps not invented here" (a negation). Rejected.
5. No Written E_leak/F_friction/master-equation output predicts any §2F row. This agrees with B2 in 5cd1174c….

## §4 Table (labels + line refs only; no values transcribed)
| # | §2F row (obs-data L#) | Measurable | Written model output | Class | Status |
|---|---|---|---|---|---|
| F1 | m_e rest energy (L211) | yes | ABSENT ((a)/(c)/(d) framing only, L203–206) | MIXED (frame ↔ electron, no map) | ABSENT-for-match |
| F2 | a_e exp / CODATA adj. (L212) | yes | ABSENT (muon g-2 OW is directive only; rejected §3.3) | MIXED | ABSENT-for-match |
| F3 | Compton wavelength λ_C (L213) | yes | ABSENT ((b) mechanism held, L204) | MIXED | ABSENT-for-match |
| F4 | Classical radius r_e (L214; derived constant) | derived | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| F5 | Λ(eeee) contact bound / no charge radius (L215) | bound | ABSENT (no Written throat size; h_i radius ABSENT L200) | MIXED | ABSENT-for-match |
| F6 | EDM d_e bound (L216) | bound | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| F7 | Charge e exact / quantisation (L217) | exact | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| F8 | Photoelectric E=hν (L219; → §2C) | yes | ABSENT ((b) coupling held, L204/L225) | MIXED | ABSENT-for-match |
| F9 | Compton Δλ (L220; → §2C) | yes | ABSENT | MIXED | ABSENT-for-match |
| F10 | Single-photon/HOM (L221; → §2C) | yes | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| F11 | m_γ bound (L222) | bound | ABSENT (no Written brane-contact mass) | MIXED | ABSENT-for-match |
| F12 | v_GW=v_γ (L223; → §2B; not Kerr) | bound | ABSENT | MIXED | ABSENT-for-match |
| F13 | Bell no-signalling/Tsirelson (L224; → §2C) | yes/bound | ABSENT ("exposed field" mechanism held, L205) | MIXED | ABSENT-for-match |

F8–F10, F12 and F13 are §2F re-statements of rows that already appear in §2B/§2C. They are counted here as distinct §2F constraint targets, but the cumulative tally below gives both the raw count and the deduplicated count.

## §5 Result
**PROVED by inspection:**
- 13/13 selected §2F rows are ABSENT-for-match; 0/13 can enter the observational match.
- Header L197 is confirmed: 0 Written model outputs in the frame rows L198–209 / L225–229. The WRITTEN items there are labels and order only.

**Cumulative:** the prior total was 37 (20 from 5cd1174c… plus 17 from 41e91352…). Adding these 13 gives **50/50 raw ABSENT**. If the 5 cross-referenced rows F8–F10, F12 and F13 may already be counted in 5cd1174c… §2B/§2C, the conservative distinct count is ≥45/45 ABSENT. That figure is not re-verified row-by-row against 5cd1174c…, so it is flagged as an UNPROVEN-GAP on overlap only.

**Named gap:** the Owner observable↔model maps for the electron/photon frames ((a)–(d), (b) coupling, (c) exposure) are still unwritten. They are Owner-reserved MIXED Writes per 3f0061e0…

## §6 Recommendations
1. Owner priority Writes: a throat-size map (F5), the (b) coupling rule (F3/F8/F9/F11) and an a_e structure map (F2). Each must be Written before any match.
2. Auditor: reconcile F8–F10, F12 and F13 against 5cd1174c… §4 to fix the distinct cumulative count.
3. Soft SF → Auditor; NL Rule-5 review mirroring c46d970f….
4. Keep Rule-4 ingest hot for χ² (a)(b)(c).

## §7 tip_touched NO
Tip and catalog were not edited. Kerr BLOCKED. Nothing was invented: no χ², coefficients, data, maps, Gap-X1 cite or MIXED Writes.
