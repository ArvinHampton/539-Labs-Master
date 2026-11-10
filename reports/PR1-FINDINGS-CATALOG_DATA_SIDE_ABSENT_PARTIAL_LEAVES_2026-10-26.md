# PR1 FINDINGS — Catalog data-side ABSENT/PARTIAL leaves (Soft SF) — 2026-10-26
Rule-3 CONTINUE COOK, reports-only. Physics Research 1. Soft SF Write-only. No RECS.

## §0 Authority (all recomputed live, 2026-10-26 ~20:58 CDT America/Chicago)
| Doc | sha256 (live) |
|---|---|
| Tip Soft SF LOCK (READ-ONLY) `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |
| Catalog (READ-ONLY) `/workspace/obs-data-PR1-HEPP-QM-GR.md` (346 lines) | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d |
| OBS-ONLY P3 (OP) `PR1-FINDINGS-OBSERVATIONAL_ONLY_P3_PATH_PREREQUISITES_2026-10-26.md` | 72c599849403e2b99c6acba6815756c38b60129b9031c3d1147dc61bf844c146 |
| MIXED (MP, exclusion set) `PR1-FINDINGS-MIXED_OBS_MODEL_MAP_PREREQUISITES_2026-10-26.md` | 3f0061e0542f48f7a7df4ba44f88b0e49ff453c693fecae7b7ebcabfb32ee330 |
| DERIVABLE (DV, exclusion set) `PR1-FINDINGS-DERIVABLE_CLASS_OBS_MATCH_CHECKLIST_2026-10-26.md` | a86a8b2243033239ec83686278bb37ace0c88004235745ecb631ea99e851a5b6 |
Path hygiene: reports under `/workspace/quantum-comp/reports/` (oct17-master tree not used or edited). Tip and catalog matched the expected hashes, so no abort.

## §1 Charge
List every catalog §2A–§2G (non-Kerr) data-side leave that names an observable but has no Written value with uncertainty (or bound with a stated CL), and give each one a Soft SF ABSENT/PARTIAL stamp. Start from the OP §5 P3b gaps (A8, G1, G4, #16). Do not invent any missing number.

## §2 Holds
- Soft SF CONFIRM **CLEARED** (not HOLD) for this reports-only Write.
- Kerr **BLOCKED**. Rows that mention Kerr are excluded: L47, L50–52, L63 (Kerr-consistency clause), L70–73 (ISCO/a∗/efficiency).
- Nine-only. invent-ban ON. Catalog and tip READ-ONLY.
- Exclusions: MIXED rows from MP (#1, #2, #6 Bell L88–93, #8, #9 Casimir, #20, A1, A2, A7, A9/A10 SN1987A L41–43, G6, G7); DERIVABLE D1–D7 from DV; model-output ABSENT (already tabled, OP/RS/AG/2F).

## §3 Method
1. Hashes were recomputed and matched before any reading (§0).
2. Seed: OP §4 rows A8, G1, G4 (P3b ABSENT) and #16 (P3b UNPROVEN-GAP).
3. Each bullet and sub-bullet of catalog L22–L235 was read line by line. A leave is **ABSENT** when the line names an observable but gives no Written number, or gives order of magnitude only. A leave is **PARTIAL** when a number is Written but has no uncertainty or CL (≈, ~, "level", "about", a textbook figure, an un-transcribed cell) or when only some sub-quantities are Written.
4. Rows already covered by MP, DV, or Kerr were dropped (§2). Rows that are CLOSED for value+unc/CL were not stamped.
5. Labels and line refs only. No catalog number is transcribed into any new prediction.

## §4 Table (Soft SF per leave; catalog L# live)
| # | Leave (label) | Catalog L# | Defect (data-side) | Soft SF |
|---|---|---|---|---|
| S1 | A8 LUNA d(p,γ)³He S-factor | L39–40 | Source cited; no numeric value, no unc | **ABSENT** |
| S2 | G1 electron b̃_X,Y,Z,T | L231–232, L235 | Orders of magnitude only; extraction warned lossy | **ABSENT** |
| S3 | G4 photon isotropic k_(V)00^(3) / c_(I)00^(4) | L231, L233, L235 | Orders only; lossy | **ABSENT** |
| S4 | #16 Mercury observed perihelion anomaly | L164 | Observed value given as "≈" with no Written unc; radar ~0.5% agreement is secondary, not re-fetched (β sub-row does carry ±) | **PARTIAL (UNPROVEN-GAP)** |
| S5 | Electron c̃_X,Y,Z / c̃_Q (S2) | L232, L235 | Orders only | **ABSENT** |
| S6 | Proton / neutron b̃ (S2) | L232, L235 | Orders only | **ABSENT** |
| S7 | Photon k_(V)00^(5) (S3) | L233, L235 | Orders only | **ABSENT** |
| S8 | Photon anisotropic k_(E)2m^(4) and (κ̃_e−)_XY (S3) | L233, L235 | Orders only | **ABSENT** |
| S9 | GWTC-4.0 SME d=5 k_ℓm⁽⁵⁾, the remaining coefficients | L57 | k₀₀⁽⁵⁾ bound with CL is Written; the others are "not transcribed" | **PARTIAL** |
| S10 | GWTC-4.0 TGR PN-bound improvement / ringdown credible-region | L59 | The improvement factor range is qualitative; no per-coefficient bound Written at this line | **PARTIAL** |
| S11 | M87\* central brightness depression ratio | L61 | "~" with no unc (diameter and M carry ±) | **PARTIAL** |
| S12 | EHT M87\* 2017 polarimetry (LP fraction, \|m\|_net, β₂) | L72 | Approximate ranges and peaks only; no unc/CL | **PARTIAL** |
| S13 | EHT 2018 LP fraction; Sgr A\* 2018 variability/PSD slopes | L75 | "∼" values/ranges with no unc (ring diameter carries ±) | **PARTIAL** |
| S14 | Single-photon antibunching parameter α | L82 | "≈" with no Written unc | **PARTIAL** |
| S15 | HOM coincidence dip (visibility) | L84 | Observable named; no number | **ABSENT** |
| S16 | Massive-object interference mass reach / collapse bounds | L111–112 | Threshold ("above") only; collapse bounds have no number | **PARTIAL** |
| S17 | Josephson/QH universality | L113 | "~" level, no unc/CL | **PARTIAL** |
| S18 | A_FB^b deviation | L134 | Significance only; no Written A_FB^b value+unc | **PARTIAL** |
| S19 | LHC BSM resonance null | L160 | Qualitative null; no bound/CL Written | **ABSENT** |
| S20 | GP-A redshift (Vessot 1980 primary) | L171 | "10⁻⁴ level"; secondary \|α\| bounds with no stated CL; primary digits not obtained | **PARTIAL** |
| S21 | Optical-clock height / gradient redshift | L173 | Observable named; no number | **ABSENT** |
| S22 | GPS net clock offset | L174 | Textbook figure, no unc, not re-fetched | **PARTIAL** |
| S23 | LAGEOS/LARES frame-dragging | L192 | "about 2%" with no unc [CONTESTED] | **PARTIAL** |

## §5 Counts
- Leaves stamped: **23** (4 seed + 19 scan). All are non-Kerr, and none overlaps MP or DV.
- **ABSENT 10** (S1, S2, S3, S5, S6, S7, S8, S15, S19, S21).
- **PARTIAL 13** (S4, S9–S14, S16–S18, S20, S22, S23). S4 is carried as PARTIAL/UNPROVEN-GAP.
- By section: §2A 1; §2B 5 (S9–S13); §2C 4 (S14–S17); §2D 2 (S18, S19); §2E 5 (S4, S20–S23); §2F 0 new (its electron/photon rows duplicate §2C/§2D, or are CLOSED by stated CL at L215); §2G 6 (S2, S3, S5–S8).
- Values invented: **0**.

## §6 Leaves for Soft SF (listed, not ranked)
S1 · S2 · S3 · S4 · S5 · S6 · S7 · S8 · S9 · S10 · S11 · S12 · S13 · S14 · S15 · S16 · S17 · S18 · S19 · S20 · S21 · S22 · S23.
Any landing of a missing value is a catalog edit, which is Owner/catalog-owner gated. PR1 made none.

## §7 tip_touched NO
The tip and catalog were re-hashed after writing (see PRESS). Kerr BLOCKED and not touched. Nothing was invented: no value, map, χ², coefficient, Gap-X1 cite, or MIXED Write. No catalog or tip edits. No messaging. Nine-only.
