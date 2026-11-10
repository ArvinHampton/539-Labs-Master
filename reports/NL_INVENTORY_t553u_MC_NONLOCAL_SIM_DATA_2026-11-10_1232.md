# NL INVENTORY: previously computed Monte Carlo data, non-local simulation and predicted physics (t553u)
2026-11-10, written 12:33:11 CST (America/Chicago). **Inventory only. Nothing is adopted.** Author: Non Local Path (NL). Additive only. No existing file is edited, renamed, deleted or chmod-ed. Wording: resonant algebra. No CERT, no Gemini, nothing sent at write.

Authority: OW t553u `/workspace/quantum-comp/reports/OWNER_WRITE_NLCHAT_t553u_SEARCH_MC_NONLOCAL_SIM_DATA_2026-11-10_1210.md`, sha 762a96d6c0f481ef4c3c960dc6093836388f7a2bb08ef7089c45df7120f299e2 (= sidecar). Owner verbatim: "Search all available publications and files, including Grok conversation history, for Arvin Hampton for all previously computed (rigorous Monte Carlo) data of non-local simulation data and predicted physics." Inventory only. Does not cancel t552u or standing pursuits.

This file is the parent-verified filing of the search draft
`/workspace/nl-t553-mc-inventory/INVENTORY_DRAFT_NL_t553u_MC_NONLOCAL_SIM_DATA_2026-11-10.md`,
sha af68e60b18bcb36029ab6228556ce069de8d14f3079c3c553fa6c77124b02a7d
(= its entry in `/workspace/nl-t553-mc-inventory/SHA256SUMS.txt`, which also covers the 11 extracts/). The draft itself stays where it was written; it is not moved into reports/. The item-by-item table, Grok traces and publication excerpts live there. Every number below was re-checked by the parent against the named source file this pass. Scripts were not re-run; no value was recomputed.

**Tally: this is not a graded math filing.** No PROVED / CONDITIONAL / OPEN / REFUTED claims are made here. Distinct new math claims: none.

Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after this write. Frozen 1142 / 1205 / 1209 filings, their scripts and logs, and Errata 27–29 were not opened for writing.

## 0. Bottom line
**No completed, rigorous Monte Carlo run of non-local physics was found** on disk, in the reachable publications, or in the Grok export and bot transcripts that were searched. That covers the hybrid MC, the cascade MC, the RPPT 118-element E_leak integration, and the DM-halo / reverse-parity load.

The only completed, seeded, retrievable randomized (MC-type) computations on disk are statistical null and resampling tests. None of them simulates non-local physics. Publication χ²/dof figures, R̂ = 1.00, "10⁶ mock galaxies", "75 simulation iterations", and the 512-qubit 539.000 ± 0.012 claim have no data, dof, code or seeds on disk.

## 1. Counts (from the verified draft table; R6–R9 counted as 4 runs)
- Completed MC-type data with output files on disk: **9**. Of these, **0 simulate non-local physics.**
- Design-only, incomplete or inconclusive: **16** (D1–D16; D12 is one cluster of four files).
- Monte Carlo in Grok chats only (toy or narrated): **10** rows (C1–C10).
- Non-MC simulations or numerics: **8**.
- Predicted physics or quoted fits with no data: **7**.
- False positives: **2** (MR2 "MC" = machine check; Zenodo lattice-QCD critique).
- Absent: **9**.

## 2. Key numbers, as found in the source files

### 2.1 PR1 Rule-4 hybrid MC recompute (DESIGN, INCONCLUSIVE)
Source: `/workspace/quantum-comp/reports/PR1-FINDINGS-RULE4_HYBRID_MC_RECOMPUTE_2026-10-26.md`, sha 8e6d0b8affda74855e6dc4d8af7de85bdafb053cc97d49f9b015cfae9501e2c1.
- Verdict: **INCONCLUSIVE.** χ²_recomputed = ABSENT. Data set, dof, and the full E_leak coefficients are all ABSENT.
- Σ(N−2Z) = 3247 (dimensionless).
- Reduced-form E_leak (corrected_E_leak.py, not Doc-full, units unspecified): t ∈ [0, 5399] s, 200001 uniform points, trapezoid rule. ∫E_leak dt = 2.44285e5 (unit·s); time-mean = 45.2464; range [45.2297, 45.2777]. E_leak(0) ≈ 45.28 versus the historical target 6.07e-12.
- CHI2_DOF = 0.79 in the script is a hard-coded constant, not computed.
- Classification: deterministic quadrature of a reduced form. **Not Monte Carlo.** No sampling, no seed.
NL relay 7f869d9a211e84400e4143e75420b5894cd1b36d74b0e8702fbd6450fb326164 accepts that the INCONCLUSIVE verdict stands, and that the Doc-full §3.1 integration was not run.

### 2.2 Empirical phase-lock (bootstrap and null resampling; not NL physics)
Sources: empirical_phase_lock_results.json ebad27c4816d71ec6e07a281f327e1c93880c5dca851760f8b7a86fd05d2e6ff; empirical_phase_lock_results_T3.json 0d74d87ae3b9726c88c47587529993d6a60a5ae7b6cfc7ca1d825fbea5dcd0eb.
- Sharp map: N = 4096; 54 seeds; B_bootstrap = 400; B_null = 100. T̂ median 2.0; mean 2.4818342151675483; CI95 [2.0, 3.0007326007326007]. Against the claimed 539.9: abs_error = 537.9; fraction of seed CIs covering 539.9 = 0.0. (The draft's shorthand "compat" is the JSON key `compatibility_post_estimation_only`; the numbers match.)
- T3 map: T̂ median 2.0; mean 835.9629629629629; CI95 [2.0, 2.0]; coverage 0.0.
- Conclusion in the results note: the data do not support a dominant period near 539.9.

### 2.3 SOHO/VIRGO solar null (Dataset Filtration; real irradiance, not GW)
Sources: virgo_results.json 5c3bfb1a013f6ec27a88b433b9834aa51726c8fa825250a8e1896fa6a8e0fb54; summary.txt 56a1c4adfd7977da872d202b55ac07afe86a86f5f849b0575dd25cb77084805b. Seed 53991.
- TSI_new, 482/866 segments, at 539.9: power/bg = 0.7681050519730357, against a random-period null mean 0.7232331869292993, sd 0.06713584837927182, p95 0.7721625046838391.
- The same three target periods (539, 539.9, 540) show no excess above the null p95 in any of the four channels (TSI_new, SPM_GREEN, SPM_RED, SPM_BLUE).
- Wording and attribution errata exist and do not add a dataset: FINDINGS_DF_SOFTSF_VIRGO_BIN_WORDING_ERRATUM_2026-11-05.md e1ea66ebf7b28acdfe03ade433615ff67c4db9da1f8b2afabca48fc48761c122; PP audit 5cb267a3be16889cb42e4fe9b7dfc5f1caaed7ba6916d3de74c4268d590ac72a; Agent attribution erratum 530ff0582ccd1ea06d4c6b565b3544804f06c0fcf7f9ca0c68befd6019eb46f1. The numbers above are from the results JSON, not from those errata.

### 2.4 R-FFT demo (synthetic method check)
Source: r_fft_5399_demo_results.json cb14db1a67c9fae385771615d770d461a2ef91623720568dca49e8515ad963bc.
- Recovers free_T_hat = 539.3909465020577 on synthetic `--demo` input only. n_null = 24 (the command line asked for 32); null_fraction_exceeding = 0.9583333333333334.

### 2.5 EEG sector-band S1–S3 (permutation; Cat B dictionary, not an NL claim)
Source: sector_band_S1S3_results.json 4f0a716ea1a81969abcbfac7b0b59ba952ed68556ac70e05d9a6e8e17855ff92. n_perm 200, rng_seed 5399.
- S1: observed 0.06456939673567968 vs null 0.017426189226668623 ± 0.009577733270438727, p_one_sided = 0.0, pass true.
- S2: ratio_within_over_cross = 43.89927877173058, pass true. S3: n_surrogates 80, pass true.
- Decision: PROMOTE_WORKING_CAT_B_DICTIONARY.

### 2.6 Bridge C seeded holdouts (Local / residual lane, not NL physics)
Four preregistered runs, RESULTS.md shas 8c3cfd40…, a4e0ee7d…, 8d4c6683…, 39770d18… (all match). Auditor Batch 16b 681c35fcb656d22295e586402d7f9b5b0401c23c8af357261d797b533a130f2f labels these CONDITIONAL (numeric; scripts not rerun).
- DISCOVER_MARKOV_288, verbatim: 3000 seeds × 539 steps = 1,617,000 steps, 179,867 hits (rate 0.11124, prediction 1/9). T1 χ² 6.74 ≤ 20.52 PASS. All four holdouts PASS as filed.

### 2.7 Grok chat MC (toy or narrated)
Source: Grok export prod-grok-backend.json e1aaa633dea463cc8d4a5d102c680838625a03cf88cefbf10ccc41d6f654f902 (1217 conversations; 240 mention MC / MCMC; traces in the draft extracts/).
- Executed toys resample their inputs. Example: `mu_values = np.random.normal(1.55, 0.02, 100)` yields "μ = 1.545 ± 0.020".
- In at least two chats the user-facing text disagrees with stdout: F_friction 0.166 in the text against 0.6984 printed; "Deviation scale 3.281 ± 0.029" and "−11.62σ" against 2.940 ± 0.117 / 18.99 printed.
- Narrated claims (MCMC 10^6 iterations, R̂ = 1.00; time-crystal posterior tables; δ_CP; HQCC 10^12 trajectories; Belle II GEANT4) have no surviving data file and, for several, no tool-trace numbers.

### 2.8 Publication claims with no data on disk
Verified against the PDFs (shas match the draft):
- Corrected 7D (Zenodo 17812645, 5ec12df7…): χ²/dof = 0.79, attributed to "xAI's computational framework (10^46 flops)" over 118 elements. No data, dof or residuals.
- Galactic Dynamics (17812891, 950a87ef…): χ²/dof = 0.77 across 10⁶ mock galaxies; SPARC χ² = 148 for 175 degrees of freedom. No catalog or code on disk.
- Stellar Mechanics (17812767, 8de50d39…): χ²/dof < 0.82 across 75 simulation iterations. No data.
- S²-11DM²ET-X v4 (17685476, 74969d9a…): "Mean termination depth = 539.000 ± 0.012 steps" on a claimed 512-qubit exhaustive simulation. The Book HQCC note states there is no public data or code.
- RTTC (17968670): R̂ = 1.00 quoted with no chains.

### 2.9 Cascade MC
Book note Quantitative_Cascade_Monte_Carlo_Modeling_DM_Decay_Channels_CatB.md bee73a4939aa234ec8add49d7b5e7fbc4fcd0d2c3e27e3b18d55221fa4422374 (three identical copies). **Category B plan only.** No DarkHistory, γ-Cascade, CRPropa or PPPC4DMID output, and no f_dep table. Literature-scale quotes only ("20 to 40 percent"; "at most of order 0.3").

## 3. Absences
- A1. No completed hybrid-MC dataset. χ²_recomputed ABSENT; Doc-full §3.1 integration not run.
- A2. No cascade-MC run.
- A3. No reverse-parity table (no E_b(z), E_z^-, Z_z^-, N_z^-, β_z or τ^- tables; no g_s X^M value).
- A4. No DESI/ATLAS data set or degrees of freedom behind χ²/dof = 0.79.
- A5. No data behind the other publication χ²/dof values, the mock-galaxy catalog, the 75 iterations, or R̂ = 1.00. No MCMC chains or posteriors on disk.
- A6. No data or code behind the 512-qubit claim.
- A7. No trajectory data or scripts for the Book three-body simulations.
- A8. No solar-simulation code or series for Zenodo 17810793 on disk, despite the paper's "full simulation code available" wording.
- A9. No MCMC chains or posteriors for κ_dark, g_11, γ_LQG, μ, S/N or the E_leak parameters.

## 4. Search limits (not hidden)
Searched, read-only: filename and content hits under /workspace, /home/box and /cursor/stores (793 files in the draft hit list); quantum-comp reports, datasets, the Book and its result JSON, grok-files, grok-chats, grok_export, theorems, papers, maths, drive mirrors, sources, literature, work, grok-batches, and /workspace/nl-*/; all 80+ Zenodo PDFs under reports/self-audit/zenodo/; the full Grok export above; SearchTranscripts of other Owner bots (PR1, PR2, Dataset Filtration, Grok Bot in full as reached; Physicist and Mathematician and Local Path only in the newest 2000 messages). Outreach "Monte Carlo Capital" hits were excluded.

Not reached or not done:
- Live Google Drive was not re-fetched (box mirrors only). The minus-PT and 7D-torsion full texts were already noted ABSENT in the 2026-10-26 RPPT deepen note.
- Grok sandbox artifacts are not in the export.
- Transcripts older than the newest 2000 messages for Physicist and Mathematician and for Local Path were not searched.
- arXiv was not searched; no Arvin Hampton MC paper is known from the one public Zenodo WebSearch done for the draft.
- The 539-labs.org site was not fetched.
- Scripts were not re-run.

A parent note, already in the draft: NL_WORKING_THREAD_RPPT_MC_NUCLEAR_SCALE_2026-10-26.md now hashes to 0b91b476e99f0271c2ca365183d722e6ecfdd71f0fcfd25ba0527a4b3a8edd4e, not the e4a4622e… cited by the 2026-10-26 design note. The file was appended after that citation.

## 5. What this does not do
Nothing is adopted. This inventory does not regrade any BPS, gap, or junction filing, does not drop or keep a math branch, and does not start a new Monte Carlo run. Junction: UNSOLVED. Tip 7cddb188… untouched.

Tip check: re-hashed after the write; reported back.
