# PR1 FINDINGS — HEPP/QM/GR-lab model-output ABSENT, catalog §2A + §2G (Rule-3 CONTINUE free-pursue) — 2026-10-26

## §0 Authority (live sha256sum, re-hashed before writing; all match)
- Tip Soft SF LOCK (READ-ONLY) `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91
- Catalog (READ-ONLY) `/workspace/obs-data-PR1-HEPP-QM-GR.md` = 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d
- Resume FINDINGS `PR1-FINDINGS-HEPP_QM_GR_LAB_OBS_MATCH_RESUME_COOK_2026-10-26.md` = 5cd1174c17e1f0a131c0213a4a41c814b221917424fe9c6e75d7d4393cbf8483
- NL Rule-5 ACCEPT `bridges/NONLOCAL_QM_EH11D/NL_RULE5_REVIEW_PR1_HEPP_QM_GR_LAB_OBS_MATCH_RESUME_COOK_2026-10-26.md` = 0e634786f74a9f4df03bc161a1b0927a49faae2e491c61c2641ff1a2a59ad708
- Free-pursue `PR1-FINDINGS-HEPP_QM_GR_MISSED_VARS_FREE_PURSUE_2026-10-26.md` = cb43f7d136b6cd9f22983d85b660f48e5a3af06e114e396595ce2dc9104fcd69
- Ten-slots `OWNER_WRITE_TEN_OPEN_SLOTS_LOCKED_CALL_0B65057E_2026-10-26.md` = 60dd4ad2dcdb5bbd727a98175ff1bc332a971528fe68e06fc58aee2e45a30ad1
- Rule-3 `OWNER_WRITE_RULE_3_AUTO_APPROVE_2026-10-26.md` = 6b657e975876fd3fbe1e7eb9c51269c2a327c9d38e5f085efdec07e49dcdb918 (computed live)
- Resume OW `OWNER_WRITE_RESUME_NINE_COOK_CURRENT_STRUCTURE_2026-10-26.md` = fe0d3543028b801643d342466853d85bdce2f1bb47295e936a5c2bd7a3373d1b
- Near-hits inspected (computed live): `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/PP_Chain_Derivation_Closure_CatB_2026-08-31.md` = fce4a9d7c6e2f058ec9ea5d6e959814f73c7fc0f747e9af964a55b8064e99801; `oct17-master/docs/quantum-comp-eigen-matrix-search-2026-10-08/NEUTRINO-EXTRACT.md` = d520d24259470b6c81992ae23221226484ffbc01baa37da85d26c7e4c69fd4b6
- Dependencies cited by short prefix only via the resume FINDINGS (INCONCLUSIVE 8e6d0b8a…, roster 9bd78736…, re-scope 788d765e…). These were not re-hashed here; their authority comes through 5cd1174c…

## §1 Charge
Rule-3 AUTO-APPROVE CONTINUE (free-pursue, proof or named gap). This complements resume FINDINGS 5cd1174c…, whose §4 covered §2B–§2E. This pass covers catalog §2A (solar/neutrino/burst timing, L22–43) and §2G (SME Lorentz/CPT bounds, L230–235). Free-pursue F4 (cb43f7d1…) listed both sections, but resume §4 skipped them.

## §2 Holds
- Tip LOCK 7cddb188… is READ-ONLY. No fold.
- Kerr / Path4 C2–C3 BLOCKED. No Kerr-ringdown rows; none occur in §2A or §2G.
- χ² slots (a), (b) and (c) are ABSENT (60dd4ad2…). Rule-4 INCONCLUSIVE stands.
- Gap-X1 is OPEN. It is not cited, closed, or invented here.
- Nine-only roster.

## §3 Method (same as resume §4)
For each row I searched the corpus with `rg` over /workspace/quantum-comp plus the tip, focusing on reports/OWNER_WRITE_*, E_leak and master-equation material. Keywords:
- §2A: neutrino|Borexino|SN1987A|solar|CNO|pp-chain|LUNA
- §2G: SME|Lorentz|CPT|Kostelecký|birefring|b̃|κ̃

A hit counts only if it is a Written model output that would predict the observable. Script-only, chance-test, qualitative and hosted-input near-hits are rejected.
- No reports/OWNER_WRITE_* file has a Written observable↔model map: `rg -c "observable.{0,20}(map|↔)"` gives 0 non-zero files.
- §2A keyword hits in OWNER_WRITE (rejected):
  - PR2_DE_TRANSFER_NEEDWRITES_t1086u L19/L34: a grep log and an Author voice quote.
  - PR2_AUTHOR_POWERS_OPEN_LEVERS_t1129u L37/L47: Γ_★ "D2 solar-brane route". It is qualitative and the file itself says "Rates OPEN".
  - ITEM4_DM_DE_e_matter_photon L15: a qualitative DM→DE stellar-core parity reversal.
  - None of these outputs a flux, rate, burst energy or timing.
- §2A near-hit (iii): PP_Chain_Derivation_Closure_CatB (fce4a9d7…) L10–13. This is Category B, a "hosted effective theory". Its Φ_pp^lum comes from a luminosity constraint that takes L_sun and SSM as **inputs**, and it says "F_L and F_T not derived". It is not an OWNER_WRITE model output, so it is rejected because it re-hosts SSM inputs.
- §2A near-hit (iv): NEUTRINO-EXTRACT (d520d242…). Its "Bottom line" says the mass formulas fail recomputation and S_ν looks fitted. That is a chance/numerology finding, so it is rejected. It also does not bear on §2A flux or burst rows.
- §2G hits in OWNER_WRITE (rejected):
  - NL_AUTHOR_OPEN_LEVERS_t1118u L12: γ = ordinary Lorentz factor inside Φ(y). This is kinematic; it has no SME coefficient.
  - NL_REVERSE_PARITY_EXPORT_t1086u L40: "Lorentzian extension in 11D" Δt_11D. This is a dilation form with no Written g_11/Φ coefficients. It maps to no b̃, c̃, k or a_T/e_T.
- No Written E_leak/F_friction/master-equation output predicts any §2A or §2G row. This is consistent with B2 in 5cd1174c… (12 terms with no Written coefficients).

## §4 Table (labels + line refs only; no values transcribed)
| # | Catalog row (obs-data L#) | Measurable | Written model output | Class | Status |
|---|---|---|---|---|---|
| A1 | §2A Solar luminosity L☉ (L23–24) | yes | ABSENT (CatB pp-chain takes L_sun as input; rejected (iii)) | MIXED (stellar energy ↔ Γ_★, no map) | ABSENT-for-match |
| A2 | §2A Borexino Phase-II pp flux (L25–26) | yes | ABSENT (Φ_pp^lum is SSM-hosted; rejected (iii)) | MIXED | ABSENT-for-match |
| A3 | §2A Borexino ⁷Be flux (L27) | yes | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| A4 | §2A Borexino pep / Phase-II CNO bound (L28) | yes/bound | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| A5 | §2A CNO detection + Phase-III (L32–35) | yes | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| A6 | §2A SNO ⁸B NC flux (L36) | yes | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| A7 | §2A Solar+KamLAND Δm²₂₁, θ₁₂ (L37–38) | yes | ABSENT (NEUTRINO-EXTRACT mass formulas fail recompute; rejected (iv)) | MIXED | ABSENT-for-match |
| A8 | §2A LUNA d(p,γ)³He S-factor (L39–40) | yes | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| A9 | §2A SN1987A burst counts/duration/binding energy (L41–42) | yes | ABSENT | MIXED (energy-loss channels ↔ E_leak, no map) | ABSENT-for-match |
| A10 | §2A SN1987A ν-vs-light arrival timing (L43) | bound | ABSENT (no Written time-dimensional constant; cb43f7d1… F5) | MIXED | ABSENT-for-match |
| G1 | §2G Electron b̃ sensitivities (S2) (L232) | bound | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| G2 | §2G Electron c̃ / c̃_Q (S2) (L232) | bound | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| G3 | §2G Proton/neutron b̃ (L232 parenthetical) | bound | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| G4 | §2G Photon isotropic k_(V)/c_(I) (S3) (L233) | bound | ABSENT (t1118u γ is kinematic; rejected) | OBSERVATIONAL-ONLY | ABSENT-for-match |
| G5 | §2G Photon birefringent k_(E), κ̃_e− (S3) (L233) | bound | ABSENT | OBSERVATIONAL-ONLY | ABSENT-for-match |
| G6 | §2G Gravity-matter a_T (S5) (L234) | bound | ABSENT (t1086u Δt_11D has no coeffs; rejected) | MIXED (gravity sector, no map) | ABSENT-for-match |
| G7 | §2G Gravity-matter e_T (S5) (L234) | bound | ABSENT | MIXED | ABSENT-for-match |

Catalog caveat L235: the pdftotext column extraction is lossy. That caveat is irrelevant here because no digits are cited.

## §5 Result
**PROVED by inspection:** 17/17 selected rows (§2A 10/10, §2G 7/7) are ABSENT-for-match. 0/17 can enter the observational match.

Combined with the resume table (5cd1174c…, 20/20), the non-Kerr §2A–§2E + §2G coverage is 37/37 ABSENT.

**Named gap:** Owner observable↔model maps (Written prediction functions from E_leak/F_friction/master equation to each observable). There are 0 in the corpus.

**UNPROVEN-GAP:** whether Γ_★ (t1129u) or Δt_11D (t1086u) would be commensurable with A1/A2/A9/A10 or G6/G7 once the rates and coefficients are Written. MIXED is a conjectural tag only.

## §6 Recommendations
1. Keep Rule-4 ingest hot for Written (a), (b) and (c). Re-run only when they land.
2. Owner should write observable↔model maps before any match. Priority candidates: A1/A2 (Γ_★ rate), A9/A10 (burst energy/timing), G6/G7 (gravity-sector Lorentz coefficients).
3. Soft SF → Auditor.
4. NL Rule-5 review of this complement, mirroring 0e634786….

## §7 tip_touched NO
Tip and catalog were not edited. Kerr BLOCKED. No χ², coefficients, data or Gap-X1 cite were invented.
