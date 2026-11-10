# AUDITOR CORPUS CRAWL — BATCH 21 — CUSTODY SAMPLING (read-only) — 2026-11-09

Role: Auditor (audit-only). Written 2026-11-09 ~2:00 PM CST (America/Chicago). Exclusive create (`noclobber`). No sidecars created or repaired, no edits, no moves, no CERT, nothing external. Computations ran only in /tmp/aud21 on copies. Tip sha 7cddb188…dfc91 re-hashed: unchanged, not edited.
Labels: PROVED / CONDITIONAL / OPEN / REFUTED (by proof or counterexample only). No verdict is changed here.

## §0 Operative Owner decisions applied (unchanged from batch 20)
B13-3 κ := √(2/Λ₀), Λ₀ = 0.783577 (≈1.597622; a DEFINITION). 1.595361 / Λ₀≈0.7858 are SUPERSEDED (C15-3 closed). B10-1 sidecars read-only. B11-1 / B18-1 (OW c4c0f1c0, superseding 0deba43d): W₇=+1 is the AL eigenvalue on 7.4.a.a; Path C stands; P5a OPEN. B12-1 Keeper rule #160 suspended. B2 CONDITIONAL on (B)-M.
Reference set "audited" = every sha256 cited in AUDITOR_CORPUS_CRAWL_BATCH*.md plus manifest covered_b01_08=Y (manifest: BATCH09 DEDUPE TSV).

## §1 The 489 math-marker files whose bytes also exist outside reports/
Counting rule reproduced: .md, math marker, covered_b01_08≠Y, also_outside_reports=Y, sha not in audited set → **489** (496 before excluding 7 whose sha is already audited).
- Live hash = manifest hash: **489/489**. Each one has a byte-identical copy outside reports/ (220 only in quantum-comp/bridges, 219 only in quantum-comp/oct17-master, 50 in bridges + workspace/reports, grok-batches, 539-labs, or distributions).
- **Byte-identical to an audited original: 7 of 496 (the excluded 7). Of the 489: 0.**
- Nearest audited file by name tokens plus line-similarity (difflib): 3 are ≥0.9 similar to an audited file. All 3 differ NON-substantively: PUSH_LOG_2026-09-13_ObjectB_Kernel (a "pending" commit line filled with 80fede28…), Pursue_All_Nine_Open_Paths_2026-08-31 (6 header lines added), U1_LEDGER_RH_BOUND_NOT_C1…2026-09-14 (identical lines; whitespace or EOL only). 1 more pair shares only a basename (README.md, unrelated content).
- **Finding B21-1 (coverage gap):** the other **486 are distinct content that no batch audited.** Batches 9–20 treated "also outside reports" as "copy of an audited file". That assumption was wrong: the outside copies are mirrors, and the mirrors were never audited either. By date: 07:24, 08:68, 09:56, 10:156, 11:126, undated 59. 81 carry PROVED labels; 152 mention CERT; 31 W₇; 31 Owner decision/write; 20 use the superseded Λ₀≈0.7858/1.595361; 7 the (2n+1)/3 display; 3 P5a.
- Stratified sample of 40 (seed 21; top 16, self-audit 12, heavy-daily 5, bridges 4, AUDITOR 3), live=manifest 40/40: ~20 process/ACK/heartbeat, 6 Owner Writes or assignments (governance: lane self-prove→PP→Keeper OW cdab6ac5, four-researchers OW fb83985d, 53991ebf lane authority, Cat A foolproof 8a0325da), and ~14 math content (e.g. NL G8 "Theorem 1" PROVED×4; CLAIM_TABLE_Master "π₁(K⁺)=1 PROVED Cat B"; Architecture_CB4; NCR-g7; RH_E1/M1.3/L1 notes). The substance is real, and none of it is audited. Table A below.
- Flags (no edits made): **B21-2** self-audit/…/Book_HQCC_Corrected_Statement_2026-09-20.md, line 23, prints unfloored "T3(n)=(2n+1)/3" for n≡2 mod 3. That is non-integral, e.g. n=2 gives 5/3 (the same erratum as the GR-paper fix, batch 20). **B21-3** 20 files (all 11-05 Soft SF / Cat B round-two) use Λ₀≈0.7858 → 1.595361. √(2/0.7858)=1.5953611 is recomputed correct as arithmetic, but SUPERSEDED by B13-3 (√(2/0.783577)=1.5976225).

### Table A — §1 sample (40)
| # | sha8 | path | class |
|---|---|---|---|
| 1 | e7648e07 | FINDINGS_LOCAL_SOFTSF_PROVE_OR_REFUTE_T3REF_CAND1_2026-11-05.md | math content: not audited, labels as written stay as written |
| 2 | 257ca026 | MR2-SOFTSF-HEARTBEAT-2026-10-27-1447CDT.md | process |
| 3 | 67d424fa | SOFTSF_PRESS_AGENT_ACK_OWNER_LOCK_PROFESSOR_PROOF_INVENT_PENDING_ROUTE_OW_0e729e89_PLUS_HANDOFF_2026-10-27.md | process |
| 4 | 15e3b22c | PRESS_DF_SOFTSF_AMEND_SM_SCOPE_PP_N1_ANOMALY_LOCK4_PP_THEN_KEEPER_2026-11-05.md | process |
| 5 | 360320c9 | FINDINGS_PR2_ACK_OWNER_ALL_STOP_LOCAL_PURSUE_PP_LOCAL_ONLY_2026-10-28.md | process |
| 6 | a0c2ed5a | OWNER_WRITE_CALL_53991ebf_OPEN_LANE_RESOLUTION_AUTH_ALL_PRIMARIES_2026-11-05.md | Owner Write (governance) |
| 7 | 64e4e26c | WRITE_NL_SELF_PROVE_G8_REPAIR_2026-10-27.md | math content: not audited, labels as written stay as written |
| 8 | 8d00dabd | FINDINGS_MR1_SOFTSF_O4_QUANTUM_MODULAR_C_GS_PARITY_CITE_HOLD_INVENT_2026-11-05.md | math content: not audited, labels as written stay as written |
| 9 | 0bee0825 | SOFTSF_PRESS_PP_ACK_OWNER_LANE_SELF_PROVE_PP_AUDIT_KEEPER_OW_cdab6ac5_2026-10-27.md | process |
| 10 | 89b78bf1 | OWNER_WRITE_CALL_53991ebf_EXTENSION_GR_PREDICTIONS_SECOND_AXIS_2026-11-05.md | Owner assignment |
| 11 | 457ebace | SOFTSF_PRESS_PP_NOTE_NL_PROOF_FOR_AUDIT_PARKED_WHILE_PP_PAUSED_2026-10-27.md | process |
| 12 | f48da4a2 | OWNER_WRITE_FOUR_RESEARCHERS_DOUBLE_DUTY_PP_QUEUE_THRESHOLDS_2026-10-27.md | Owner Write (governance) |
| 13 | 7a0be1d5 | FINDINGS_MR1_RESONANT_MATH_PREDICTIONS_NT_MODULAR_HECKE_HOLD_INVENT_2026-11-05.md | math content: not audited, labels as written stay as written |
| 14 | 8a0325da | OWNER_WRITE_CAT_A_FOOLPROOF_539_CORPUS_LIFT_STOP_2026-11-03.md | Owner Write (governance) |
| 15 | cdab6ac5 | OWNER_WRITE_LANE_SELF_PROVE_PP_AUDIT_KEEPER_2026-10-27.md | Owner Write (governance; Keeper lane) |
| 16 | f4305f21 | FINDINGS_MR1_SOFTSF_PP_PROOF_REVIEW_B_SEC3_APPELL_RC_2026-11-05.md | math content: not audited, labels as written stay as written |
| 17 | 25a668bc | self-audit/repo/PAPERS.md | math content: not audited, labels as written stay as written |
| 18 | d21ae66f | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Architecture_A1_Seed_Equivariance.md | math content: not audited, labels as written stay as written |
| 19 | 6a567531 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/RH_E1_Off_Nearline.md | math content: not audited, labels as written stay as written |
| 20 | 758d54e4 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/U1_GS_NEWOBJ_BANDPAIR7_Residual_Pair_Identity_2026-09-02.md | math content: not audited, labels as written stay as written |
| 21 | 833de071 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/RH_M1_3_Path_Design.md | math content: not audited, labels as written stay as written |
| 22 | ea3898aa | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/CLAIM_TABLE_Master.md | math content: not audited, labels as written stay as written |
| 23 | 047af9ca | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Executive_Summary_2026-09-10_Go_U7.md | math content: not audited, labels as written stay as written |
| 24 | 388ce36a | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Missing_Equations_for_2c77354a_2026-10-03.md | math content: not audited, labels as written stay as written |
| 25 | 984e4e73 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Architecture_CB4_Smooth_Spin_Fill_CatB.md | math content: not audited, labels as written stay as written |
| 26 | 8a3ba2ec | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/RH_Moments_FunctionField_Constants_Survey.md | math content: not audited, labels as written stay as written |
| 27 | 007f4229 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/RH_L1_Phase_Functional_CatA.md | math content: not audited, labels as written stay as written |
| 28 | 6fff772b | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/U7_Slice_Equality_Locked_2026-09-11.md | math content: not audited, labels as written stay as written |
| 29 | 8e7e4df3 | heavy-daily/d7f018c50bd7-Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md | math content: not audited, labels as written stay as written |
| 30 | b7e85b86 | heavy-daily/2d0099b-Executive_Summary_P_TL.md | math content: not audited, labels as written stay as written |
| 31 | f3403b53 | heavy-daily/ab413f5ce307-U1_GS_NEWOBJ_END_Residual_Endomorphism_End_res_C_Q4_2026-08-31.md | math content: not audited, labels as written stay as written |
| 32 | 13eb50e6 | heavy-daily/ingest-2026-09-13-22/U1_LEDGER_OBJECT_B_KERNEL_Obstruction_Written_Data_2026-09-13.md | math content: not audited, labels as written stay as written |
| 33 | 1334f868 | heavy-daily/ingest-2026-09-12-12/PUSH_LOG_2026-09-12.md | math content: not audited, labels as written stay as written |
| 34 | 926f965f | bridges/PROFESSOR_PROOF/PP-NOTE-ABSORB_LOCAL_ACK_FYI_PP_WAKE_LOCAL_WORK_ONLY_2026-10-28.md | process |
| 35 | 6746c902 | bridges/PROFESSOR_PROOF/EIGEN_ACK_OWNER_LOCK_PROFESSOR_PROOF_ROUTE_OW_0e729e89_2026-10-27.md | process (cites PROVED) |
| 36 | b2f20b15 | bridges/PROFESSOR_PROOF/PP-FINDINGS-NOTE_GS_EQ_F_QS_ACCEPT_AMENDS_GS_INVENT_AUDIT_2026-10-28.md | process |
| 37 | 199cfd1a | bridges/PROFESSOR_PROOF/PP-FINDINGS-AUDIT_LOCAL_GS_GAP2_ZETA_CLOSEDFORM_DEDEKIND_S7811_2026-10-28.md | process |
| 38 | 1d947504 | AUDITOR/EIGEN_ACK_OWNER_LOCK_FOUR_RESEARCHERS_DOUBLE_DUTY_OW_fb83985d_2026-10-27.md | process |
| 39 | fe817502 | AUDITOR/EIGEN_ACK_OWNER_RESUME_N36_NAMED_GAP_OW_a26b11d4_2026-10-27.md | process |
| 40 | 03671c2d | AUDITOR/EIGEN_ACK_OWNER_LOCK_LANE_SELF_PROVE_PP_AUDIT_KEEPER_OW_cdab6ac5_2026-10-27.md | process (cites PROVED) |

## §2 Non-.md files with MATCH sidecars (full check)
The 61 in the brief = non-.md, sidecar MATCH, not mirrored outside, not audited. I checked the superset of **73** (adding 12 mirrored ones). Each file was re-hashed live and compared with its `.sha256` sidecar (read-only) and the manifest: **73/73 live = sidecar = manifest.** Types: 27 txt, 15 py, 10 pdf, 5 json, 5 pre-softsf snapshots, 3 csv, 3 tex, 2 out, 1 each mp4/log/sh. No mismatches. Table B.

## §3 Stratified sample of files with NO sidecar (14,901; 51 folders)
Proportional to folder size (≈150) plus 6 from folders with <20 files. Seed 2109, **158 files** total: s_family_paths 59, heavy-daily 33, BRIDGE_C_35 15, self-audit 15, crypto 7, small 6, AUDITOR 4, evidence 4, chronoflux 3, others 12. **Live = manifest 158/158** (no drift since the manifest). Table C.

### Scripts (sandboxed; folder copied to /tmp/aud21/sb, run with timeout 120 s; live sources untouched, hashes re-checked)
Scripts in the sample: 19 (py/sh/sage). Nearly all write output files, and many need local modules (sym_engine, cypari2, cornerlib, arbutil59) or the network (cern_539_pipeline: urllib), so only a subset ran. 12 scripts from §2 and §3 ran, all exit 0:
- **MR2_gap_filtr_68_check_2026-10-27.py (sidecar MATCH) — REPRODUCES** its findings file (MR2-FINDINGS-DUAL-CONTINUE-gap-filtr-68): f = [0,1,−1,−2,−7,16,2,−7,15,−23,−16,−8] (7.4.a.a, a₇=−7, consistent with B18-1's ε=+1); mod-7 rank/augmented = wt4 (3,4), wt6 (5,6), wt8 (5,6), equal to dim M_k(Γ₀(7)) = 1+2⌊k/3⌋ = 3,5,5 (recomputed from g=0, ε₂=0, ε₃=2, 2 cusps). So the computational input to "w(θ³f)∉{6,8} PROVED" (Soft SF) reproduces. Its label is unchanged (PP lane).
- rerun_ow9aec847a_2026-11-03.py: stdout **byte-identical** to the stored .out. theta_pi_fast_pipeline_v3_audit: stdout identical to the stored .out apart from SymPy deprecation warnings captured in the .out.
- verify_lambda22.py: det Gram D₂₂=4, Z₂₂=1, kissing D₂₂=924 (=2·22·21 ✓), fixed-space Gram dets 13/52. m3_counterexample: det 2, 36; W 0 N 2. f4_cx2: CX1 False, CX2 commute True / idempotent False. These reproduce the counterexample outputs as stored; claims are not re-adjudicated.
- codex_items_6_10, gauss_sums, shintani_s (s=7: ζ_E(0)=1/10, ζ_E(−1)=29/1200), CRYPTO h1 (p=7 PASS z=17.5; 11/17/67 FAIL): ran; no PROVED claim attached in-file.
- **B21-4** owner-softsf-scripts-2026-11-05/analyze_lambda_sensitivity & compute_higher_order_derivatives ("document only"): base R_c = 1.595436 (Pack H 1.59543590). That is neither the B13-3 κ (1.597622) nor the superseded 1.595361. The "Effective Λ₀" column prints δ, not Λ₀ (a cosmetic bug). Flag only.
- Not run: rewrite-capable or dependency-bound scripts (mk_pdf, make_rev3_part3, review_edits, pr_packaging_verification.sh, search*.py, extract_d1, s_family A5/A41/A55/A59, PARI part3/rayclass, sage rowvec_recon, cern pipeline). Hash custody only.

## §4 Spot-check of .md files with no math markers
The 3,491 in the brief = no marker, not mirrored outside. Superset pool 4,961 (incl. mirrored). Sample **51** (seed 2104, proportional by folder; 36 from the 3,491 stratum). Live=manifest 51/51. Table D.
- Hidden math claims: few and minor. φ(1001)=720 (Parallel_External_Tracks, recomputed ✓). "Extra zeros of φ_n only (4,5),(6,7) for n≤40, m≤400" (Executive_Summary 09-14): φ_n undefined in-file → OPEN. NL_REACTION_EIGEN_STEP3_Q89 cites "dim 89" for an Ind_{Γ₀(49)} module and δ_W₇. It is cite-only, HOLD pending an Owner join; not dim M₄(Γ₀(49)) (=18 by the dimension formula), so it is not a conflict. order28 PREREG: preregistration, no claim. E_leak CuNc: physical parameters (T₂=70 fs), Cat B; it flags its own A_CuNc=0.031 as unfitted.
- Owner decisions: only references (ACKs of OW cdab6ac5/fb83985d/53991ebf/06748ff2, "Owner token hard stop 90%", full-stop) or "awaiting Owner join". **No new Owner decision found**; none touches κ/Λ₀, P5a, Path C, B2, or Keeper #160. CERT mentions are all "No CERT".

## §5 Updated blockers
B21-1 OPEN (486 unaudited math-content mirrors; ~81 with PROVED labels). B21-2, B21-3, B21-4 flags (no edits). Carried forward: B19-1 erratum (3^539 ≈ 1.473×10^257); B19-3/B20 custody (2 substantive in-place amendments to the GR paper and pins, 2 benign, 1 undetermined); P5a OPEN; B2 CONDITIONAL on (B)-M.

## §6 Recommendation on closing the full-corpus audit
**Not yet.** Custody is clean on everything sampled (489+73+158+51+40 re-hashes, 0 drift). Coverage is not: B21-1 shows 486 math-content files never audited. Options: (a) one more batch pair over the 81 PROVED-bearing files plus the 20 Λ₀≈0.7858 and 7 T3 files (~110), with the rest classified at triage level; or (b) the Owner accepts them as out-of-scope mirrors. Either choice should be recorded as an Owner decision.
A final summary report would need: scope and denominators (22,035 manifest shas, audited / mirrored / sampled / excluded); batch index with sha256s (1–21); custody statement (sidecar MATCH/MISMATCH totals, 5 mismatches and their disposition); the operative Owner-decision ledger in order (B10-1, B11-1, B12-1, B13-3/C15-3, 0deba43d superseded → c4c0f1c0, B2/(B)-M); a claim ledger by label (PROVED/CONDITIONAL/OPEN/REFUTED) for core objects (P5a, Path C, κ, T3, 7.4.a.a, B2, R_c, junction, Layer2, S²-11DM²ET-X); errata list (T3 floor, 3^539, superseded Λ₀, B21-2..4); open blockers and the homonym glossary (D1, R_c, κ, W₇); reproducibility notes (scripts run / not run); and explicit limits (audit-only, no CERT, sampling error bounds).

### Table B — §2 (73)
| # | live sha8 | path | live=sidecar=manifest |
|---|---|---|---|
| 1 | 50f0517a | 539labs/539_Labs_Blueprint_30s.mp4 | YES |
| 2 | 01830934 | 539labs/539_Labs_Technical_Corpus_Codex_2026-11-03.txt | YES |
| 3 | 4f173950 | 539labs/src/cern_539_pipeline.py | YES |
| 4 | be0f32eb | 539labs/src/labs539_core.py | YES |
| 5 | 34e831f8 | FINDINGS_539_LABS_OPS_HQH_CRIT3_OPEN_LEMMAS_C2_FIBER_AND_PI_DOMAIN_2026-11-05.pdf | YES |
| 6 | bbb617ac | GEMINI_REQUEST_PACKET_ALL_TWELVE_DRAFT_2026-11-05.pdf | YES |
| 7 | 0d9e2d5a | GEMINI_REQUEST_PACKET_ALL_TWELVE_DRAFT_2026-11-05.txt | YES |
| 8 | 9844f2eb | GEMINI_REQUEST_PACKET_ALL_TWELVE_DRAFT_2026-11-05_MANIFEST.json | YES |
| 9 | 3ccf185a | MR1_CF980_PRIME_OMEGA_TABLE_2026-10-26.csv | YES |
| 10 | 0bec69fb | MR2_gap_filtr_68_check_2026-10-27.py | YES |
| 11 | 4c30652f | OWNER_ARCHIVAL_formal_corrections_brief_2026-11-05.tex | YES |
| 12 | 7e4270ab | OWNER_DIRECTIVE_GEMINI_COMPUTATION_TOKEN_PRESERVATION_VERIFY_DELIVERY_2026-11-05.json | YES |
| 13 | 31e4de8a | OWNER_DRAFT_LATEX_FORMAL_CORRECTIONS_S2_11DM2ET_2026-11-05.tex | YES |
| 14 | 68e58b2d | PAPER_RESIDUAL_TERNARY_ALGEBRA_BRIDGE_C_2026-11-03.pdf | YES |
| 15 | c2dfd1fe | PAPER_RESIDUAL_TERNARY_ALGEBRA_BRIDGE_C_REDRAFT_2026-11-03.pdf | YES |
| 16 | 2decd4a5 | PHYSICIST_REPORT_NINE_LINEAGE_MATH_STATEMENTS_2026-10-27.pdf | YES |
| 17 | 05e6a8b1 | Pure_Math_Interpretation_S2_11DM2ETX_Extension_of_GR_DRAFT_2026-11-05.pdf | YES |
| 18 | 918a36c9 | REPORT_AGENT_CAT_B_S2_11DM2ETX_LOOSENED_LANGUAGE_CALL_53991ebf_DRAFT_2026-11-05.pdf | YES |
| 19 | 1627997b | bridges/BRIDGE_C_35/REVIEW_2026-10-24/REPORT.pdf | YES |
| 20 | 4200f6a6 | bridges/BRIDGE_C_35/REVIEW_PARALLEL/REPORT.pdf | YES |
| 21 | b741d336 | bridges/BRIDGE_C_35/STREAM_IDLE_LOCAL.md.pre-softsf-match-2eea23dd-b741d336-2026-10-26 | YES |
| 22 | e80ef994 | bridges/BRIDGE_C_35/STREAM_IDLE_LOCAL.md.pre-softsf-tippin-324a2134-e80ef994-2026-10-26 | YES |
| 23 | d73c32e5 | bridges/BRIDGE_C_35/STREAM_IDLE_LOCAL.pre-softsf-tippin-7cddb188-d73c32e5-2026-10-26 | YES |
| 24 | e7afa862 | bridges/BRIDGE_C_35/STREAM_IDLE_LOCAL.pre-softsf-tippin-e84a3a81-e7afa862-2026-10-26 | YES |
| 25 | 49da8a59 | bridges/BRIDGE_C_35/STREAM_IDLE_LOCAL.pre-softsf-tippin-ea4eb298-49da8a59-2026-10-26 | YES |
| 26 | f4b0f37d | bridges/NONLOCAL_QM_EH11D/inventory_check/search_t1133u_human_hits.json | YES |
| 27 | 75e09ace | bridges/NONLOCAL_QM_EH11D/inventory_check/search_t1133u_human_turns.py | YES |
| 28 | dbee2555 | bridges/NONLOCAL_QM_EH11D/inventory_check/search_t1145u_human_hits.json | YES |
| 29 | 2e2c0bf9 | bridges/NONLOCAL_QM_EH11D/inventory_check/search_t1145u_human_turns.py | YES |
| 30 | 23bb0268 | local-t3ref-cand1-evidence-2026-11-05/search-result.json | YES |
| 31 | 9a7dddf6 | local-t3ref-cand1-evidence-2026-11-05/search.py | YES |
| 32 | a183dddd | mr1-n6-modp-q121-d1/GA1_ANNOTATION_EXT_ROWS_2026-10-26.csv | YES |
| 33 | 9b9b73c0 | mr1-n6-modp-q121-d1/N6_D1_nu_columns_modp.csv | YES |
| 34 | 1f13f4af | mr1-n6-modp-q121-d1/extract_d1.log | YES |
| 35 | 2e2a67c2 | mr1-n6-modp-q121-d1/extract_d1.py | YES |
| 36 | dd82f6ae | owner-softsf-scripts-2026-11-05/OWNER_LATEX_SEC6_SEGMENT_softsf_document_only_2026-11-05.tex | YES |
| 37 | 88cd84a6 | owner-softsf-scripts-2026-11-05/analyze_lambda_sensitivity_softsf_document_only.py | YES |
| 38 | 112cdec6 | owner-softsf-scripts-2026-11-05/compute_higher_order_derivatives_softsf_document_only.py | YES |
| 39 | 639945d1 | owner-softsf-scripts-2026-11-05/pr_packaging_verification_softsf_document_only.sh | YES |
| 40 | 33eb416f | s_family_paths/A39_gk_family/proof/out_blocks_k7_check.txt | YES |
| 41 | 643ede81 | s_family_paths/A39_gk_family/proof/out_k11_N900.txt | YES |
| 42 | d8b27b7d | s_family_paths/A39_gk_family/proof/out_k13_N900.txt | YES |
| 43 | 5c00f4b6 | s_family_paths/A39_gk_family/proof/out_k15_N900.txt | YES |
| 44 | fa2208b8 | s_family_paths/A39_gk_family/proof/out_k3_N900.txt | YES |
| 45 | ed024b34 | s_family_paths/A39_gk_family/proof/out_k5_N900.txt | YES |
| 46 | ef9707d9 | s_family_paths/A39_gk_family/proof/out_k9_N900.txt | YES |
| 47 | 1206c13e | s_family_paths/A39_gk_family/proof/out_tails_k11_N900_eta0.01.txt | YES |
| 48 | edcfd61d | s_family_paths/A39_gk_family/proof/out_tails_k13_N900_eta0.01.txt | YES |
| 49 | 00302c29 | s_family_paths/A39_gk_family/proof/out_tails_k15_N900_eta0.01.txt | YES |
| 50 | f6a53d6c | s_family_paths/A39_gk_family/proof/out_tails_k15_N900_eta0.05.txt | YES |
| 51 | 813b602f | s_family_paths/A39_gk_family/proof/out_tails_k9_N900_eta0.01.txt | YES |
| 52 | bfa14a6c | s_family_paths/A39_gk_family/proof/out_tails_k9_N900_eta0.05.txt | YES |
| 53 | 2636e129 | s_family_paths/A41_uniform_oddk/proof/out_k17_N1500.txt | YES |
| 54 | fb92c763 | s_family_paths/A41_uniform_oddk/proof/out_k17_N900.txt | YES |
| 55 | 49ac98c1 | s_family_paths/A41_uniform_oddk/proof/out_k19_N1500.txt | YES |
| 56 | 4e84d687 | s_family_paths/A41_uniform_oddk/proof/out_k19_N900.txt | YES |
| 57 | b2c24072 | s_family_paths/A41_uniform_oddk/proof/out_k21_N1500.txt | YES |
| 58 | 29e867a8 | s_family_paths/A41_uniform_oddk/proof/out_k21_N900.txt | YES |
| 59 | f232674b | s_family_paths/A41_uniform_oddk/proof/out_k23_N1500.txt | YES |
| 60 | 8f37f6ed | s_family_paths/A41_uniform_oddk/proof/out_k25_N1500.txt | YES |
| 61 | 00555109 | s_family_paths/A41_uniform_oddk/proof/out_tails_k17_eta0.05.txt | YES |
| 62 | c48b669e | s_family_paths/A41_uniform_oddk/proof/out_tails_k17_eta0.07.txt | YES |
| 63 | 3a1aea31 | s_family_paths/A57_gk_31_33/proof/DIFF_make_cells.txt | YES |
| 64 | ade964c2 | s_family_paths/A57_gk_31_33/proof/DIFF_params.txt | YES |
| 65 | 878c6d42 | time_review/REVIEW_CatB.pdf | YES |
| 66 | b25baf29 | tubulin-torsion/scripts/codex_items_6_10_2026-11-03.py | YES |
| 67 | 4aeea27d | tubulin-torsion/scripts/f4_cx2_ad_model_2026-11-03.py | YES |
| 68 | 4f5b683f | tubulin-torsion/scripts/m3_counterexample_2026-11-03.py | YES |
| 69 | 02c54016 | tubulin-torsion/scripts/rerun_ow9aec847a_2026-11-03.out | YES |
| 70 | fee41da9 | tubulin-torsion/scripts/rerun_ow9aec847a_2026-11-03.py | YES |
| 71 | 8446d145 | tubulin-torsion/scripts/theta_pi_fast_pipeline_v3_audit_2026-11-03.out | YES |
| 72 | b4de1452 | tubulin-torsion/scripts/theta_pi_fast_pipeline_v3_audit_2026-11-03.py | YES |
| 73 | de2c988d | tubulin-torsion/scripts/verify_lambda22.py | YES |

### Table C — §3 sample (158)
| # | stratum | sha8 (manifest) | path | live=manifest |
|---|---|---|---|---|
| 1 | s_family_paths | add5b221 | s_family_paths/A43_bridge_run/data/exact/eo_k243.json | YES |
| 2 | s_family_paths | 16f03aff | s_family_paths/A56_A49_audit/exact/sec/gexact_k333.json | YES |
| 3 | s_family_paths | 2b559486 | s_family_paths/A43_bridge_run/data/exact/eo_k83.json | YES |
| 4 | s_family_paths | 30d8280c | s_family_paths/A40_gk_audit/exact/eo_k9_D300000.json | YES |
| 5 | s_family_paths | cba0c49b | s_family_paths/C_gue/data/s43_N1419.npz | YES |
| 6 | s_family_paths | d414c26f | s_family_paths/A22_grok_export_search/chats/0ed64ceb-2edb-4436-9146-cf161ab080da.txt | YES |
| 7 | s_family_paths | 226fc1f7 | s_family_paths/A41_uniform_oddk/proof/saddle.py | YES |
| 8 | s_family_paths | 17cc1657 | s_family_paths/A49_gk_runs/exact/eo_k61.json | YES |
| 9 | s_family_paths | 979a63a4 | s_family_paths/A22_grok_export_search/chats/e1fb6d48-434a-4f4e-988d-5e52218a439c.txt | YES |
| 10 | s_family_paths | 5d8dd70d | s_family_paths/A27_drive_review_complete/docs/1opdXc2moL98GwhGc92_phwGBVAGYzs3fRWCdT_bA1IY.bin | YES |
| 11 | s_family_paths | 98645102 | s_family_paths/A29_patterns_all/prereg.md | YES |
| 12 | s_family_paths | 24c3b476 | s_family_paths/A43_bridge_run/data/exact/eo_k37.json | YES |
| 13 | s_family_paths | 7e4b2b3a | s_family_paths/A43_bridge_run/data/cert/z_k451_p1000000000000000003.txt | YES |
| 14 | s_family_paths | 213b967a | s_family_paths/A27_drive_review_complete/docs/1map3RF2uUnmucJhkjlkogjwIJZZEyIY9HIoQkG4SX_U.bin | YES |
| 15 | s_family_paths | 26502a61 | s_family_paths/A56_A49_audit/exact/sec/gexact_k819.json | YES |
| 16 | s_family_paths | 2869ee5a | s_family_paths/A43_bridge_run/data/cert/z_k351_p1000000000000000003.txt | YES |
| 17 | s_family_paths | 03542add | s_family_paths/A27_drive_review_complete/txt/1E8eVYl70kNLnnijRP9cjLcvsGkJXngYZ43y5KG8zeHU.txt | YES |
| 18 | s_family_paths | ff2476bb | s_family_paths/A22_grok_export_search/chats/9cfe9c2a-6533-465e-87f3-bc2d48439658.txt | YES |
| 19 | s_family_paths | ea94f7bf | s_family_paths/A5_classgroup/scripts/float_scan_A5.py | YES |
| 20 | s_family_paths | d51b4c44 | s_family_paths/A56_A49_audit/exact/sec/gexact_k361.json | YES |
| 21 | s_family_paths | 2c5fc918 | s_family_paths/A43_bridge_run/data/cert/z_k315_p1000000000000000003.txt | YES |
| 22 | s_family_paths | da799f3b | s_family_paths/A26_drive_review/raw/f64.json | YES |
| 23 | s_family_paths | 92eba56d | s_family_paths/A51_bridgeC_exact/rank216.json | YES |
| 24 | s_family_paths | 85b4c68f | s_family_paths/A56_A49_audit/exact/sec/gexact_k861.json | YES |
| 25 | s_family_paths | 7d279662 | s_family_paths/A27_drive_review_complete/txt/1SXee4EggOgmBNciRgCYFCRpUe8JkhlQWehYlGwmpfIY.txt | YES |
| 26 | s_family_paths | 33fb7496 | s_family_paths/A22_grok_export_search/chats/c3cfb854-8f8b-4637-a24f-a14516313577.txt | YES |
| 27 | s_family_paths | 9d7d68a2 | s_family_paths/PAPER_gk_v1/data/zero_sets_log.txt | YES |
| 28 | s_family_paths | 208bd439 | s_family_paths/A33_law_vector_chi3/g_K2.npy | YES |
| 29 | s_family_paths | a1f3fe00 | s_family_paths/A2/logs/h13_mm_M8.log | YES |
| 30 | s_family_paths | 7611df07 | s_family_paths/A27_drive_review_complete/txt/1xtlYqH4QKjf4_n7QwX5LerqYdZLxCrkXe2sJdrddGig.txt | YES |
| 31 | s_family_paths | 53bd9d18 | s_family_paths/A56_A49_audit/exact/sec/gexact_k125.json | YES |
| 32 | s_family_paths | a0f6d8a0 | s_family_paths/A40_gk_audit/proof/tails_indep_k7_eta1e-6.json | YES |
| 33 | s_family_paths | d2ea9829 | s_family_paths/A22_grok_export_search/chats/6a65a062-6b49-4838-b7a5-9ace3197d27c.txt | YES |
| 34 | s_family_paths | b551549b | s_family_paths/A22_grok_export_search/chats/7a661eb8-ef7b-472e-9b16-13c213f3a8cc.txt | YES |
| 35 | s_family_paths | 7e32d229 | s_family_paths/A22_grok_export_search/chats/cace90ad-3738-4fc3-bd15-d9e93728d1e6.txt | YES |
| 36 | s_family_paths | 9dd7722e | s_family_paths/A49_gk_runs/proof_A44/tails_k3_eta1e-6.log | YES |
| 37 | s_family_paths | 07614021 | s_family_paths/A11_induction/logs_E0_odd.txt | YES |
| 38 | s_family_paths | 7062cb4c | s_family_paths/A59_clt_rederivation/code/riem59.py | YES |
| 39 | s_family_paths | 20cefd1c | s_family_paths/A49_gk_runs/proof_A41/tails_k5_N1500_0.27_1.38.json | YES |
| 40 | s_family_paths | ac46cea7 | s_family_paths/B/c2_wall/REPORT.md | YES |
| 41 | s_family_paths | a55c7e00 | s_family_paths/A57_gk_31_33/REPORT.md | YES |
| 42 | s_family_paths | ffd21617 | s_family_paths/A43_bridge_run/data/cert/z_k821_p1000000000000000003.txt | YES |
| 43 | s_family_paths | 3fee06ac | s_family_paths/A56_A49_audit/exact/sec/gexact_k719.json | YES |
| 44 | s_family_paths | a7de46b3 | s_family_paths/A26_drive_review/docs/1NbHcZ5UJDkWsqXcmV2aVoLIAuadSVTF6A9Q_o_17jGs.bin | YES |
| 45 | s_family_paths | 7fb236ec | s_family_paths/A43_bridge_run/data/cert/z_k165_p1000000000000000003.txt | YES |
| 46 | s_family_paths | a3906cf7 | s_family_paths/A41_uniform_oddk/proof/tails_indep_k19_N900_eta0.01.json | YES |
| 47 | s_family_paths | 4a1cd27d | s_family_paths/A43_bridge_run/data/exact/eo_k273.json | YES |
| 48 | s_family_paths | b3ac3f09 | s_family_paths/A56_A49_audit/exact/sec/gexact_k615.json | YES |
| 49 | s_family_paths | 9bd66b20 | s_family_paths/A41_uniform_oddk/proof/blocks_k19_N900_0.44_2.3.json | YES |
| 50 | s_family_paths | e5f483d5 | s_family_paths/A27_drive_review_complete/docs/17fykHI-HUS8yFz18q2UJ9OD8yI-C_yVVXiYtSUiTFCQ.bin | YES |
| 51 | s_family_paths | 83fd5d00 | s_family_paths/A27_drive_review_complete/docs/1VKBAhQkr073JbndL5onFUNiDJZv_oiRXPnmJEF5gHk0.bin | YES |
| 52 | s_family_paths | fd9a3eeb | s_family_paths/A43_bridge_run/data/exact/eo_k33.json | YES |
| 53 | s_family_paths | fe70d0ed | s_family_paths/A27_drive_review_complete/txt/1jbslRWmvWnwEYTGKZpk8waP3pJQ2ABay.txt | YES |
| 54 | s_family_paths | 02a494a0 | s_family_paths/C_gue/data/s5_N1997.npz | YES |
| 55 | s_family_paths | 41d1a60b | s_family_paths/A55_small_k_exceptions/gen_tables4.py | YES |
| 56 | s_family_paths | dd3ca978 | s_family_paths/A43_bridge_run/scripts/mk_pdf.py | YES |
| 57 | s_family_paths | afc270f7 | s_family_paths/A27_drive_review_complete/docs/1XtQKiWpbNs9alhwAvhMiAf239T8yUkTMX-uulcQeKNU.bin | YES |
| 58 | s_family_paths | 0e3d8d48 | s_family_paths/A56_A49_audit/exact/sec/gexact_k725.json | YES |
| 59 | s_family_paths | e005a7d3 | s_family_paths/A56_A49_audit/exact/sec/gexact_k531.json | YES |
| 60 | heavy-daily | 3468ef30 | heavy-daily/db56ab3b8efb-Explore_Open_Paths_Discussion_2026-08-31.md | YES |
| 61 | heavy-daily | 784fce71 | heavy-daily/2026-10-19-Open-Items-Pursuit/lift_coeffs_N30.pkl | YES |
| 62 | heavy-daily | ce44f58d | heavy-daily/2026-10-18-Cusp-Onset-Closure/deepB/vrank_98.json | YES |
| 63 | heavy-daily | 00ff8a8d | heavy-daily/2026-08-22-10-nosend.md | YES |
| 64 | heavy-daily | 047b87e3 | heavy-daily/2026-10-18-Analytic-CatB-Push/closed_forms_K17.py | YES |
| 65 | heavy-daily | ebf80ea7 | heavy-daily/2026-08-18-00-u1finite-ingest.md | YES |
| 66 | heavy-daily | 824b111f | heavy-daily/2026-08-19-16-nosend.md | YES |
| 67 | heavy-daily | d1fc0a40 | heavy-daily/2026-10-18-Open-Analytic/gauss_sums.py | YES |
| 68 | heavy-daily | b5be2c1b | heavy-daily/2026-10-18-Analytic-CatB-Push/numerics_D.jsonl | YES |
| 69 | heavy-daily | 2265ea03 | heavy-daily/2026-10-18-Cocycle-Closure/vc_k3.txt | YES |
| 70 | heavy-daily | 98743b65 | heavy-daily/2026-10-18-s8-s11/herg_7.txt | YES |
| 71 | heavy-daily | c3426cfc | heavy-daily/2026-10-19-Bridge-C-Consolidated-rev9/bridge_c_consolidated_rev9.aux | YES |
| 72 | heavy-daily | b66e9da3 | heavy-daily/2026-10-18-s8-s11/rayclass_s.py | YES |
| 73 | heavy-daily | 05c23406 | heavy-daily/2026-10-18-g_s-Closed-Forms/prove_gs.txt | YES |
| 74 | heavy-daily | ac08ad77 | heavy-daily/2026-10-18-PARI-free/part3.py | YES |
| 75 | heavy-daily | 09d091e0 | heavy-daily/2026-10-18-Bridge-C-Consolidated-rev3/make_rev3_part3.py | YES |
| 76 | heavy-daily | 7abb8f70 | heavy-daily/2026-10-18-AtkinLehner-Local/compare.log | YES |
| 77 | heavy-daily | 3e07ab43 | heavy-daily/2026-10-19-Bridge-C-Consolidated-rev9.1/build_rev9_1.log | YES |
| 78 | heavy-daily | 1bdc5ecc | heavy-daily/2026-08-30-12-ingest.md | YES |
| 79 | heavy-daily | 19d503eb | heavy-daily/HEAVY-FIVEGAPS-2026-08-17-16.txt | YES |
| 80 | heavy-daily | 1c2dcd65 | heavy-daily/2026-10-18-Bridge-C-Consolidated-rev4/build_rev4.log | YES |
| 81 | heavy-daily | d21a2d6d | heavy-daily/2026-10-18-s8-s11/shintani_s.py | YES |
| 82 | heavy-daily | 6f198580 | heavy-daily/REFEREE_REPORT_Ramanujan_Journal_Manuscript_2026-08-21.md | YES |
| 83 | heavy-daily | 39ccc651 | heavy-daily/2026-08-29-08-chat.webp | YES |
| 84 | heavy-daily | c3699fb9 | heavy-daily/2026-09-02-09-hourly.md | YES |
| 85 | heavy-daily | 68a9efe0 | heavy-daily/RESIDUAL_VS_RESONANT_2026-08-16.md | YES |
| 86 | heavy-daily | b0921bfe | heavy-daily/2026-10-17-Lever-3-OccFilt7-Lower-Bound/cert1e8/val/D1e7_t4.log | YES |
| 87 | heavy-daily | 4f3a893b | heavy-daily/2026-10-19-Bridge-C-Clean/src/s22_num.src.tex | YES |
| 88 | heavy-daily | 9931c350 | heavy-daily/2026-08-21-18-send.md | YES |
| 89 | heavy-daily | f7c6ec33 | heavy-daily/2026-10-18-Algebraic-Round3/tau_fast_5.json | YES |
| 90 | heavy-daily | 62949283 | heavy-daily/2026-10-18-Neuro-Structural-CatB/data/S014R02.edf | YES |
| 91 | heavy-daily | dd03ee5f | heavy-daily/2026-10-18-Cusp-Onset-Closure/uL_rayclass_23_M1.json | YES |
| 92 | heavy-daily | c3df4e47 | heavy-daily/2026-10-18-Cusp-Onset-Closure/vrank_37_q45.log | YES |
| 93 | bridges/BRIDGE_C_35 | d61b0f9d | bridges/BRIDGE_C_35/order34/REPORT.pdf | YES |
| 94 | bridges/BRIDGE_C_35 | b57ebc7c | bridges/BRIDGE_C_35/order19/RESULTS_ADDENDUM.md | YES |
| 95 | bridges/BRIDGE_C_35 | 2f6d86dd | bridges/BRIDGE_C_35/MAPS_CANDIDATES/PATTERN_S_MARKOV/SHA256SUMS | YES |
| 96 | bridges/BRIDGE_C_35 | edc08117 | bridges/BRIDGE_C_35/order51/REPORT.pdf | YES |
| 97 | bridges/BRIDGE_C_35 | 07ae9d08 | bridges/BRIDGE_C_35/deduce_t700u_ga1b/PREREG.md | YES |
| 98 | bridges/BRIDGE_C_35 | a64a1ca3 | bridges/BRIDGE_C_35/MAPS_CANDIDATES/PATTERN_ST_MARKOV/data/explore.json | YES |
| 99 | bridges/BRIDGE_C_35 | 62d3ab2f | bridges/BRIDGE_C_35/order12/scripts/b3.py | YES |
| 100 | bridges/BRIDGE_C_35 | 93270a32 | bridges/BRIDGE_C_35/order27/REPORT.pdf | YES |
| 101 | bridges/BRIDGE_C_35 | cae72bb0 | bridges/BRIDGE_C_35/order8/data/m3.json | YES |
| 102 | bridges/BRIDGE_C_35 | dd29f34a | bridges/BRIDGE_C_35/scripts/common.py | YES |
| 103 | bridges/BRIDGE_C_35 | afddab84 | bridges/BRIDGE_C_35/MAPS_CANDIDATES/DISCOVER_GRADING_PATH/RESULTS.md | YES |
| 104 | bridges/BRIDGE_C_35 | 2bab79ba | bridges/BRIDGE_C_35/order26/scripts/o26_posthoc.py | YES |
| 105 | bridges/BRIDGE_C_35 | ed4a11a1 | bridges/BRIDGE_C_35/order43/REPORT.pdf | YES |
| 106 | bridges/BRIDGE_C_35 | f6296a76 | bridges/BRIDGE_C_35/MAPS_CANDIDATES/MARKOV_FIBRE_FREQ/REPORT.pdf | YES |
| 107 | bridges/BRIDGE_C_35 | 52a98cac | bridges/BRIDGE_C_35/order13/PREREG.md | YES |
| 108 | self-audit | 464d7a7c | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/rh_execute_all_c1_P3_R4_results.json | YES |
| 109 | self-audit | 8917cc8d | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/RH_Remaining_Analytic_Obligations.md | YES |
| 110 | self-audit | 6f1d9fdd | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Executive_Summary_2026-07-29.md | YES |
| 111 | self-audit | d21aeaf5 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/PUSH_LOG_2026-10-18_Advancements.md | YES |
| 112 | self-audit | fc4bcbbb | self-audit/zenodo/20812393_HQH-539_and_the_Resonant_Path_Problem.pdf | YES |
| 113 | self-audit | 620270fe | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Open_Algebraic_2026-10-18/OUTPUTS_BUNDLE_2026-10-18.txt | YES |
| 114 | self-audit | 79abcc13 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Einstein-Hampton-2026-09-29/Executive_Summary_2026-09-29_Mathlib_11D_Riemann_API.md | YES |
| 115 | self-audit | a53d0741 | self-audit/repo/.git/hooks/push-to-checkout.sample | YES |
| 116 | self-audit | e3ee8ebe | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Executive_Summary_2026-10-03_Proca.md | YES |
| 117 | self-audit | a78dccfd | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Hayward_Black_Hole_Metrics_Investigation_2026-09-05.md | YES |
| 118 | self-audit | c55c711e | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Three_Body_Observational_Alignment.md | YES |
| 119 | self-audit | 59239400 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/O3_Residual_Fibre_Residuals_Beyond_A5plus_2026-08-16.md | YES |
| 120 | self-audit | 340bf451 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/C_third_Closure_2026-10-18/2026-10-18-C_third-Closure.md | YES |
| 121 | self-audit | 6dfff5f3 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/PUSH_LOG_2026-10-03_Spin_Torsion_Spin_Orbit.md | YES |
| 122 | self-audit | 9ce73a8a | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Tensor_Pattern_Closure_2026-10-18/2026-10-18-Tensor-Pattern-Closure.md | YES |
| 123 | crypto | 76afe806 | crypto/PRESENTATION_SUPPORT/LQH_SEARCH_ALL/raw/github/file_539-Labs-repo_docs_M4_top_timing_impl.txt.decoded.txt | YES |
| 124 | crypto | 21a3a3af | crypto/PRESENTATION_SUPPORT/LQH_RECONSTRUCTION/hardware/run_hw_middle.sh | YES |
| 125 | crypto | 3a6ea906 | crypto/RPP_spec_v2_drafts/scripts/review_edits.py | YES |
| 126 | crypto | d363e9bd | crypto/RPP_spec_v1/scripts/p_export_search.py | YES |
| 127 | crypto | cbca24c5 | crypto/RPP_spec_v1/scripts/chats/9c88a1be-0806-4c00-8e18-3b5dcffdd221.txt | YES |
| 128 | crypto | c19f5671 | crypto/RPP_spec_v1/scripts/chats/21ecbd40-9b30-4c28-b119-55c29a0efd99.txt | YES |
| 129 | crypto | 84c09b6a | crypto/PRESENTATION_SUPPORT/LQH_SEARCH_ALL/raw/github/file_539-Labs-repo_artifacts_wp6_canonical_resim_results.json.raw | YES |
| 130 | AUDITOR | dd4bd30e | AUDITOR/FINDINGS_2026-10-27_t1248u_SOFTSF_PRESS_AGENT_ABSORB_PACK_OL_OP_DAILY_NOON_CONFIRM_CONFIRM.md | YES |
| 131 | AUDITOR | aed9b7bc | AUDITOR/FINDINGS_2026-10-27_t1208u_PR1_CHI2_TRIO_INVENT_RESUME_RULE4_2026_10_27_CONFIRM.md | YES |
| 132 | AUDITOR | ba4ae24a | AUDITOR/FINDINGS_2026-10-27_t1113u_EIGEN_R5_RELAY_MR2_SFR3P_ACCEPT_PARTIAL_FLAG_CONFIRM.md | YES |
| 133 | AUDITOR | 56b26918 | AUDITOR/FINDINGS_2026-10-27_t1311u_SOFTSF_PRESS_MR2_DUAL_CONTINUE_GAP_SK_P3_1C_MC_2026_10__CONFIRM.md | YES |
| 134 | evidence | fa92a808 | evidence/MR1_TATE_KUMMER_KRONECKER_2026-11-05/lit/crossref_bruhat_distributions_.bin | YES |
| 135 | evidence | 9094db44 | evidence/MR1_XI_SHADOW_2026-11-05/BF.pdf | YES |
| 136 | evidence | 164bcbcc | evidence/MR1_APPELL_RC_FORENSIC_2026-11-05/governing_verify.txt | YES |
| 137 | evidence | ed753a8d | evidence/MR1_XI_SHADOW_2026-11-05/HILBERT.html | YES |
| 138 | chronoflux | 5218dd32 | chronoflux/zenodo/21364971.txt | YES |
| 139 | chronoflux | 1f7671f2 | chronoflux/images/video/arksector/f07.jpg | YES |
| 140 | chronoflux | ec9800df | chronoflux/images/2026-10-18_2111807021963985267_vthumb0.jpg | YES |
| 141 | top | 3eacced2 | GEMINI_COMPENDIUM_AGENT_QUESTIONS_PROOF_REQUESTS_CONSOLIDATED_2026-11-05.pdf | YES |
| 142 | top | a177a050 | SOFTSF_PRESS_FINDINGS_LOCAL_INVENT_GVI1_BETA_AS_ALPHA_PRINCIPAL_LEVEL_GS_2026-10-27.md | YES |
| 143 | papers | 8b1426b2 | papers/HQH_HARDNESS/_build_crit3.html | YES |
| 144 | papers | 12c230f0 | papers/RTA_FOUNDATION_BOUND/NOTES_v15.md | YES |
| 145 | bridges/_git_v8_unpushed_clone | c3495a26 | bridges/_git_v8_unpushed_clone/reports/s_family_paths/A61_clt_proofs/A61_supporting_files.tgz.b64 | YES |
| 146 | bridges/NONLOCAL_QM_EH11D | 9a865e01 | bridges/NONLOCAL_QM_EH11D/inventory_check/author_candidates/T682U_NL_WRITTEN_SUPPLY_20261025/CAND_Omega0.md | YES |
| 147 | drive-zips | 1794927d | drive-zips/539_Labs_Full_Attachments_2026-06-08/attachments/S²-11DM²ET-X_ Light duality and localized detection (particle) gains non-local enhancement for unification of observational data.pdf | YES |
| 148 | literature | 27800969 | literature/A62_prior_art/notes/ax_2606.31606.pdf | YES |
| 149 | mr2-lit-720-scratch-2026-11-05 | c0d364db | mr2-lit-720-scratch-2026-11-05/1010.4449.txt | YES |
| 150 | resonant_galois | 00e87501 | resonant_galois/PureEven_v2/data/verify_algebra_log.txt | YES |
| 151 | bridges/CRYPTO_RNT_RTA | c4c00a6d | bridges/CRYPTO_RNT_RTA/scripts/h1.py | YES |
| 152 | s_family_observables | abbf3882 | s_family_observables/pages/page-4.png | YES |
| 153 | small-folders | 91355e41 | AUDITOR_V16_DRAFT_QA/page-6.png | YES |
| 154 | small-folders | 605d3922 | agent_45_clarification_verify_work/delivery_verification.txt | YES |
| 155 | small-folders | efb676f6 | AUDITOR_V16_DRAFT_QA/page-1.png | YES |
| 156 | small-folders | 468eea23 | PP_DRAFT_1611_preview/page-1.png | YES |
| 157 | small-folders | 41124221 | eigen-o5-n36-stab-2026-11-05/rowvec_recon.sage | YES |
| 158 | small-folders | 4d08a330 | df_softsf_virgo_2026-11-05/spectrum_SPM_BLUE.npz | YES |

### Table D — §4 sample (51)
| # | sha8 | path | lines | hits |
|---|---|---|---|---|
| 1 | e23cb697 | FINDINGS_PR2_COOK_BLANKET_PURSUE_LOCAL_FP_WAIT_BOARD_2026-10-26.md | 76 | math:1, owner:5 |
| 2 | 30929d51 | SOFTSF_PRESS_MR1_NAMED_GAPS_NU0_SCHEDULE_COSMETIC_2026-10-26.md | 6 | math:3, owner:1 |
| 3 | f3779bf4 | LOCAL_ACK_ACCIDENTAL_STOP_RESUME_NINE_CONTINUE_2026-10-26.md | 28 | math:1, owner:2 |
| 4 | 5db19631 | SOFTSF_PRESS_FINDINGS_PR2_COOK_BLANKET_HYGIENE_LOCAL_R5_PACK_IO_IP_ABSORB_2026-10-27.md | 5 | - |
| 5 | 6497415a | SOFTSF_PRESS_FINDINGS_AGENT_ACK_ALL_AGENTS_RESOLUTION_NO_PER_ITEM_APPROVAL_CALL_53991ebf_2026-11-05.md | 3 | owner:1, CERT:1 |
| 6 | 6936692c | SOFTSF_PRESS_REVIEW_LOCAL_PR2_COOK_BLANKET_HYGIENE_LOCAL_R5_PACK_HR_HS_ABSORB_2026-10-27.md | 6 | - |
| 7 | 21538272 | REVIEW_LOCAL_PR2_COOK_BLANKET_HYGIENE_LOCAL_R5_PACK_HR_HS_ABSORB_2026-10-27.md | 27 | owner:2 |
| 8 | a07262ec | SOFTSF_PRESS_NL_ACK_FOUR_RESEARCHERS_DOUBLE_DUTY_ROLE_UNCHANGED_2026-10-27.md | 3 | owner:1 |
| 9 | 38b0700b | SOFTSF_PRESS_MR2-DUAL-CONTINUE-socK_2026-10-27.md | 9 | owner:2 |
| 10 | 8006acb1 | FINDINGS_PR2_COOK_BLANKET_HYGIENE_LOCAL_R5_PACK_HZ_IF_ABSORB_2026-10-27.md | 22 | math:1, owner:2 |
| 11 | 5fa89b09 | SOFTSF_PRESS_FINDINGS_LOCAL_ACK_OWNER_STANDING_15MIN_STATUS_REPORT_2026-10-27.md | 4 | owner:1 |
| 12 | f0bd2805 | FINDINGS_MR1_SOFTSF_ACK_OW_ALL_RECOMMENDED_PURSUITS_HOLD_INVENT_2026-11-05.md | 25 | math:1, CERT:4 |
| 13 | c26ea31c | FINDINGS_PR2_ACK_OWNER_TOKEN_HARD_STOP_90PCT_2026-10-27.md | 15 | math:1, owner:2 |
| 14 | f7c93b16 | REVIEW_LOCAL_PR2_COOK_BLANKET_HYGIENE_LOCAL_R5_PACK_DT_PACK_EE_ABSORB_2026-10-26.md | 56 | owner:3 |
| 15 | ffff699c | AUDITOR/SOFTSF_PRESS_DEFERRED_2026-10-26/SOFTSF_PRESS_OWNER_WRITE_MR1_PROMOTE_N36_NU21_25_FILLED_MODP_REC_A_AUTO_2026-10-26.md | 5 | math:1 |
| 16 | b388b6f1 | AUDITOR/FINDINGS_2026-10-27_t1211u_DEFERRED_ASYMPTOTIC_KC_CONFIRM.md | 2 | owner:1 |
| 17 | b63db28c | AUDITOR/FINDINGS_2026-10-24_g1_accept.md | 60 | math:5 |
| 18 | 8e47066d | AUDITOR/FINDINGS_2026-10-27_t1514u_SOFTSF_PRESS_FINDINGS_MR1_ACK_OWNER_LOCK_FOUR_RESEARCHERS_DOUBLE_DUT_CONFIRM.md | 2 | owner:1 |
| 19 | dd9dcf17 | AUDITOR/FINDINGS_2026-10-25_t808u_t809u_nl_omega_geometric_CONFIRM.md | 43 | math:8, owner:1 |
| 20 | d781ab26 | AUDITOR/FINDINGS_2026-10-25_t2146u_PR2_PURSUE_WRITE_ABSENT_HOLD_CONFIRM.md | 17 | - |
| 21 | 8ee2be32 | AUDITOR/FINDINGS_2026-10-27_t1639u_SOFTSF_PACK_XL_06_MR2_ACK_FULL_STOP_CONFIRM.md | 2 | owner:2, CERT:1 |
| 22 | a31e98a6 | AUDITOR/FINDINGS_2026-10-27_t1136u_PR2_HYGIENE_LOCAL_R5_PACK_HV_HW_ABSORB_CONFIRM.md | 2 | owner:1 |
| 23 | 8b46aae4 | AUDITOR/FINDINGS_2026-10-26_t2211u_PR2_HYGIENE_PACK_DF_LOCAL_R5_DC_DH_DS_DW_CONFIRM.md | 18 | owner:1 |
| 24 | 2b3ccccf | AUDITOR/FINDINGS_2026-10-27_t1123u_EIGEN_R5_RELAY_MR2_INDCONV_ACCEPT_PARTIAL_FLAG_CONFIRM.md | 3 | owner:1 |
| 25 | e484633e | AUDITOR/FINDINGS_2026-10-27_t1308u_SOFTSF_NOTE_AUDITOR_PACK_OE_OH_MATCH_2026_10_27_CONFIRM.md | 2 | owner:1 |
| 26 | 31e0a9cd | bridges/BRIDGE_C_35/deduce_t761u_accept/INVENTORY.md | 5 | - |
| 27 | 59325b8f | bridges/BRIDGE_C_35/inventory_check/INVENTORY_t721u_GA3_rpkg1_2026-10-25.md | 2 | owner:1 |
| 28 | 033d322e | bridges/BRIDGE_C_35/order28/PREREG.md | 17 | math:4 |
| 29 | e2f6ea0b | bridges/AUDITOR/FINDINGS_AUDITOR_SOFTSF_WRITEONLY_PR1_GR_SECOND_AXIS_b04819c7_2026-11-05.md | 39 | owner:2, CERT:2 |
| 30 | 796bf875 | bridges/NONLOCAL_QM_EH11D/inventory_check/ACK_OWNER_WRITE_NL_AUTHOR_OPEN_LEVERS_t1118u_2026-10-25.md | 15 | math:3 |
| 31 | 0e8dc650 | bridges/AUDITOR/FINDINGS_AUDITOR_SOFTSF_WRITEONLY_PR2_72FILTER_bb329b4f_2026-11-05.md | 43 | owner:2, CERT:2 |
| 32 | 9736c288 | bridges/NONLOCAL_QM_EH11D/NL_REACTION_EIGEN_STEP3_Q89_2026-10-26.md | 23 | math:7, owner:1, P5a:2 |
| 33 | f399ab10 | bridges/NONLOCAL_QM_EH11D/inventory_check/FINDINGS_T682U_NL_WRITTEN_SUPPLY_ABSENT_PLUS_CANDIDATES_2026-10-25.md | 20 | math:2 |
| 34 | 99a638a3 | crypto/RPP_spec_v1/scripts/notion/N_3ada_81c9_Push0730CuNc.md | 49 | math:1 |
| 35 | 3617a0eb | heavy-daily/2026-09-02-22-hourly.md | 29 | - |
| 36 | a5b5ab21 | heavy-daily/2026-09-03-12-heavy-residual.md | 38 | math:2, owner:1 |
| 37 | 99b81434 | heavy-daily/2026-09-04-14-hourly.md | 19 | math:1 |
| 38 | 3bcc34da | heavy-daily/2026-08-26-10-ingest.md | 33 | math:6, owner:2 |
| 39 | fce4a9d7 | heavy-daily/7b7c8aae331f-PP_Chain_Derivation_Closure_CatB_2026-08-31.md | 15 | - |
| 40 | 81158ae4 | heavy-daily/2026-09-14-02-heavy-residual.md | 57 | math:2 |
| 41 | a4896091 | heavy-daily/2026-09-03-08-hourly.md | 7 | - |
| 42 | 140d215c | heavy-daily/2026-08-19-10-ingest.md | 15 | owner:3 |
| 43 | 5ba2bc8f | s_family_paths/A49_gk_runs/analysis/pd_table.md | 11 | - |
| 44 | 9900b181 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Einstein-Hampton-2026-09-28/Advancements_Wrap_2026-09-28_Afternoon.md | 2 | math:1, owner:1 |
| 45 | 55b45670 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/PUSH_LOG_2026-10-03_Algebraic_Bridge.md | 12 | - |
| 46 | ba340ca1 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Quantum_Decoherence_Effects_2026-10-03.md | 13 | - |
| 47 | 8e465169 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Parallel_External_Tracks_ABC_2026-08-18.md | 63 | math:3, owner:3 |
| 48 | e783caf9 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Executive_Summary_2026-09-14_Phi_Stabilization_IDS.md | 28 | math:3 |
| 49 | 2c75306f | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/E_leak_CuNc_Numerical_Patch.md | 88 | math:9 |
| 50 | a4dbcb56 | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Review_Missed_Variables_After_Pursue_All_2026-09-21.md | 18 | - |
| 51 | 159fa52a | self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/PUSH_LOG_2026-08-08_RH_Run_All_Solid.md | 31 | math:1 |
