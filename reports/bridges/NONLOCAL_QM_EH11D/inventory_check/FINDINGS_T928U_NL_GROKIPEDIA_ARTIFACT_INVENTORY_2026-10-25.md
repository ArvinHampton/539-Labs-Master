# FINDINGS T928U — NL Grokipedia artifact inventory (2026-10-25)

## Metadata
- Stream: NL (Non Local Path), Project Quantum Comp. Owner task T928U. Generated 2026-10-25 16:45 CDT. Root /workspace/quantum-comp unless noted. Targets: grokipedia.com/page/Arvin_Hampton ; grokipedia.com/page/The_17_Theorems_of_Entanglement

## Method
Inventory only. No Grokipedia edits, no wiki file edits, no new numbers (invent-ban). sha256 computed live. Searched with rg: 0.0034, decoherence, femtosecond, 9 Maths, theorem-lemma, Residual Ternary, 17 Theorems, sympy, *.ipynb, *.lean, l7_recheck over quantum-comp/, grok-batches/, stage_*, stage1017, grokipedia-edit, zenodo-arvin-hampton-full.md. No .ipynb found. Mirrors under reports/self-audit/repo and reports/bridges/_git_v8_unpushed_clone hold identical-path copies of oct17-master lean/ and scripts/ (not re-listed).

## Priority packages
| What | Where | sha256 | Supports | Shareable |
|---|---|---|---|---|
| Lean L1–L7 (L5_linear, L7 fibre lock; built Lake/Mathlib v4.34.0, 29 Sep 2026) | `oct17-master/lean/EinsteinHamptonCurvature.lean` | `53f9a4a81c3b05a3e3eb5cedf396a67ec4e6ba3bee0485e020d95f6c4d5b7aa6` | EH L1–L7, L5/L7 | Zenodo-depositable (internal repo) |
| Lean EH base | `oct17-master/lean/EinsteinHampton.lean` | `822316dc8a8f38a51392f3a3ce5ce75820c0d968de7b370ade9f36bbc1737df3` | EH equation | Zenodo-depositable |
| Lean EH Riemann | `oct17-master/lean/EinsteinHamptonRiemann.lean` | `47e11358c3562bb049923ecef942acd7c0ab4b5a60189a6953707a48756291d3` | EH curvature | Zenodo-depositable |
| Lean 11D Riemann API | `oct17-master/lean/Mathlib11DRiemannAPI.lean` | `3159cd56a981ff66cd8d7d0777ad57aa7580c37dc77a2bb9ed154143c7e7f6e3` | EH curvature infra | Zenodo-depositable |
| Lean EH copy 28 Sep | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Einstein-Hampton-2026-09-28/EinsteinHamptonCurvature.lean` | `ef6e7ed35c78f46c9b1fda344a9e0965152b9e05787c77b0e251eedb82d7c9a5` | EH L1–L7 | Zenodo-depositable |
| Lean EH copy 28 Sep | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Einstein-Hampton-2026-09-28/EinsteinHampton.lean` | `ef6e7ed35c78f46c9b1fda344a9e0965152b9e05787c77b0e251eedb82d7c9a5` | EH | Zenodo-depositable |
| Lean EH copy 29 Sep | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Einstein-Hampton-2026-09-29/EinsteinHamptonCurvature.lean` | `ef6e7ed35c78f46c9b1fda344a9e0965152b9e05787c77b0e251eedb82d7c9a5` | EH L1–L7 | Zenodo-depositable |
| Coordinate proofs L1–L7, 'Checked in SymPy' (28 Sep) | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Einstein-Hampton-2026-09-28/Coordinate_Proofs_L1_L7_Before_Rewrite_2026-09-28.md` | `d60e8fdecc54f36a725f187a50d818167fa517e46411f37100a2b143b33e9e01` | EH L1–L7 SymPy | Zenodo-depositable |
| Advancements Wrap EH | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Einstein-Hampton-2026-09-28/Advancements_Wrap_2026-09-28_Afternoon.md` | `9900b18160fa0adb056ad180b7b0d68ab86c82d16afc44a90fe4663ee71699bd` | EH context | Zenodo-depositable |
| SymPy L7 recheck script | `reports/bridges/NONLOCAL_QM_EH11D/inventory_check/l7_recheck.py` | `c66f370264e609366aff00b549a9266953d95ea8a2e4ee64465dd8861bbc8acc` | EH L7 | Zenodo-depositable |
| SymPy L7 recheck output | `reports/bridges/NONLOCAL_QM_EH11D/inventory_check/l7_recheck.log` | `c9f1054081da89be11eb050aa6555871798bce226a7310a7dcf32e0bd3011dd9` | EH L7 | Zenodo-depositable |
| EH Rewrite Appendix PDF | `reports/self-audit/zenodo/23010998_Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.pdf` | `b51bb6211aa3c2444ec649e5cdebe93576a966ac506757dd0641f6dce8ea7e68` | EH L1–L7 | PUBLIC https://doi.org/10.5281/zenodo.23010998 |
| txt extract of 23010998 | `nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt` | `08b8541a1b40e16961984833915437aa4a96b680fe1404ad3e722191308ede39` | EH L1–L7 | public via DOI |
| Lean assumptions ledger | `reports/bridges/NONLOCAL_QM_EH11D/inventory_check/LEAN_L1L7_ASSUMPTIONS.md` | `8354a4f2fc132f38bb70bcde450e5814659679b08876d21daba333246a255476` | EH L1–L7 | internal-only |
| FINDINGS T875U | `reports/bridges/NONLOCAL_QM_EH11D/inventory_check/FINDINGS_T875U_NL_L1_L7_THEOREMS_2026-10-25.md` | `e72f5cd811da3d474bcd4d729dcad24eb81dbed6d675a93f83332dd01275de78` | EH L1–L7 | internal-only |
| FINDINGS T876U ALIGN | `reports/bridges/NONLOCAL_QM_EH11D/inventory_check/FINDINGS_T876U_NL_L1_L7_ZENODO_ALIGN_2026-10-25.md` | `5a4fc4e75d719ad238fa85b9fbc100fce20ae227d40ac4e026fcace316a42473` | EH L1–L7 vs Zenodo | internal-only |
| 17 Theorems v5 text (Thm 5 coherence length; prints ~0.3–0.4 ly) | `theorems/17-theorems-v5.txt` | `5a6a1d87a9f9bb16f1dddff2c9c38f0a6ad24f81904918334cbc0e00eba66488` | 17 Theorems, entanglement, decoherence length | PUBLIC https://doi.org/10.5281/zenodo.18442276 |
| Audit: 17 Thms vs tubulin; hbar/29.3 meV = 22.5 fs (printed as as); decoherence ~0.002–0.004 ly; 'decoherence time … empty' | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Seventeen_Theorems_Against_Four_Tubulin_Ingredients_2026-10-03.md` | `be51a1b0c20466466ab19e8b54b8f3dd8762c5c77f05cedd7a43adb0efe95ea5` | 17 Theorems decoherence / fs | Zenodo-depositable (Cat B audit) |
| Prefix-lock correction log | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/PUSH_LOG_2026-10-03_Correction_18as.md` | `a4bac91e7477789e7ce0963957bfd81bc8ea329e31bc8e6422b32c6ada300bfe` | fs/as prefix | internal-only |

## Full artifact table (additional)
| What | Where | sha256 | Supports | Shareable |
|---|---|---|---|---|
| Theorems 18–40 text | `theorems/theorems-18-40.txt` | `157175ed7deaabf642ab4e1f72fba2997b6fb20e2f27af70190855966aed11bd` | entanglement theorems | internal-only |
| Grokipedia page snapshot (READ ONLY, untouched) | `grokipedia/The_17_Theorems_of_Entanglement.md` | `ef5de280346ffe4c593aca06b20f4beb10b49879969888f004da4214e3614979` | reference | public page |
| SymPy HQCC ternary map | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/scripts/hqcc_ternary_map_sympy.py` | `865b4e191e64b7a6ff301aed6e489155a931d01dc8f94fefe31d72a7e9385882` | Residual Ternary (adjacent; not named RTA) | Zenodo-depositable |
| SymPy Lagrangian/Hamiltonian | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/scripts/model_lagrangian_hamiltonian_sympy.py` | `9f9e1653311375e803267d4483d1c57de2157a53c03ecb47a7bd4cfd36cf969b` | framework | Zenodo-depositable |
| SymPy neutrino mass | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/scripts/neutrino_mass_formula_sympy.py` | `cfcfe11e39658d2f199bed73d833dc57399355ecb8d558089f234e50c58e7925` | framework | Zenodo-depositable |
| numeric checks script (femto mention) | `eigen-matrix-search/checks/numeric_checks.py` | `94afbbb13fd91622bf3d016b74d862a487b8de256270fb0a411d5ecad5e4790b` | numerics | Zenodo-depositable |
| numeric checks output | `eigen-matrix-search/checks/numeric_checks.json` | `04b09792d4483c7286478c2342edf3cb95fba2e0cbac213c35f116cfd1f90e3b` | numerics | Zenodo-depositable |
| Grok chat: '0.0034 ly = printed 0.34 ly /100', ~215 AU, Cat B | `grok_export/qc-chats/13613e94-88e1-45df-b49f-eb27394c2f05.md` | `f7e4681d634384682124efd97183bb0c9016042f8899194ece0a38c275579fa3` | 0.0034 ly (chat only) | NOT shareable (chat export) |
| Grok chat: coherence ~0.0034 ly | `grok_export/qc-chats/e9c3a0f9-adc1-4ed2-84e6-71def0d5ef88.md` | `f578dd76dccac20020b0f047febccedb98cd7a0390da11c491e88af20bec81bf` | 0.0034 ly (chat only) | NOT shareable |
| batch findings mentioning 9 Maths / Residual Ternary | `../grok-batches/FINDINGS-MERGED.md` | `cb2cbcefc555937382cdea16526a6f98f11be19d6f40ed3506cff1e23abc67e5` | 9 Maths, RTA (secondary) | internal-only |
| X/539labs.org recovery notes for '9 Maths of Unification' | `x/POSTS.md` | `dd63327d88d71878d24b76f8e6051b814cc225400fb0d95df69b7e3b713b399c` | 9 Maths (external pointer) | internal-only |

## Gaps
- **0.0034 ly**: ABSENT from Written/Author sources. Written 17 Theorems v5 prints ~0.3–0.4 ly (L_coh≈0.34 ly). 0.0034 appears only in Grok chat exports (13613e94, e9c3a0f9) as a /100 correction, and the 2026-10-03 audit gives a 0.002–0.004 ly range. Other 0.0034 rg hits (s_family_paths tsv/json, rh results) are unrelated numerics.
- **Decoherence time in fs**: ABSENT as a Written decoherence time. Only fs figure is hbar/29.3 meV = 22.5 fs (prefix-locked, printed as 22.5 as), a settling time, not decoherence; audit states decoherence-time slot 'empty'.
- **9 Maths / theorem–lemma chain**: ABSENT as computational artifact (no script/Lean/notebook); only external 539labs.org pointers and batch notes.
- **Residual Ternary Algebra**: ABSENT as named computation; only chat exports + grok-batches; hqcc_ternary_map_sympy.py adjacent only.
- **Notebooks (.ipynb)**: none found.

## Shareability summary
- Total listed: 30. Public (DOI/page): 4 (23010998 PDF, its txt, 17-theorems v5 via 18442276, Grokipedia snapshot). Zenodo-depositable: 17. Internal/NOT shareable: 9.

## Idle
T928U complete. Stub/Local/residual-c/Grokipedia untouched. NL stream idle.
