# AUDITOR: Corpus crawl BATCH 18a. SOFTSF_PRESS and reports/AUDITOR, math-marker, #1–67 (2026-10-24 → 2026-10-26)
Date: 2026-11-09 (America/Chicago). Lane: Auditor, audit-only.

## Scope
- **Selection.** Uncovered `.md` files from the BATCH09 manifest (covered = N, also_outside_reports = N) that carry a math marker (Theorem/Lemma/Proof/PROVED/REFUTED/CONDITIONAL).
  - **(i) PRESS:** top-level `SOFTSF_PRESS_*` (72) plus `PRESS_LOCAL_SOFTSF_*` (3) = **75**. The estimate said 74; the extra one is a PRESS_LOCAL file. `OWNER_WRITE_NL_JOIN_PROOF_SKETCH_PRESS_2026-10-26.md` was already covered in batches 11–13 and is excluded.
  - **(ii) reports/AUDITOR/:** **58** files. This includes the 5 in `AUDITOR/SOFTSF_PRESS_DEFERRED_2026-10-26/`.
- **Total and split.** 133 files: 18a = #1–67 (Auditor 53, PRESS 14); 18b = #68–133 (PRESS 61, Auditor 5).

## Ordering
- Files are sorted by filename date, then by filename.
- Two files are dated from their content: AUDIT_STATUS.md and HASH_INTEGRITY.md.
- mtimes carry no weight.

## Older Auditor records
reports/AUDITOR/* are earlier Auditor-lane records. They are checked against the current Owner decisions, and **their verdicts are not re-adopted**.

## Method and limits
- Read-only. Live sha256 = manifest sha for all 133.
- Recomputation ran only in /tmp/aud18.
- No sidecars were created (B10-1). No edits.
- The tip was **read** for referent text only. Nothing was written to it, and its sha is unchanged: 7cddb188…dfc91.
- No CERT; nothing external.

## Owner decisions applied
These are relayed by Physicist and not confirmed in Auditor chat:
- **B11-1:** operative P5a = Γ₀(49)⁺, W₇ = +1 axiom version, OPEN.
- **B12-1.**
- **B13-3:** κ := √(2/0.783577) ≈ 1.597622, a DEFINITION.
- **B10-1.**
- **B2:** CONDITIONAL on (B)-M.

## 1. Custody (P/C/O/R = PROVED/CONDITIONAL/OPEN/REFUTED word counts)
| # | date (src) | file (under reports/) | lane | sha256 | sidecar | lines | P/C/O/R | flags |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-24 (content) | `AUDITOR/AUDIT_STATUS.md` | older Auditor record | `cce1034a8486392c6b6f096c6697f2b13093c5842f0fac696cbbcb9c124f7f42` | NONE | 456 | 0/0/94/0 | W₇ |
| 2 | 2026-10-24 (name) | `AUDITOR/FINDINGS_2026-10-24_continue.md` | older Auditor record | `07cdfe95ff630d37b3ac6fccd1dbf5ff924e70c12d9666fd32bd5f9dad01c874` | MATCH | 82 | 0/0/12/0 | S2X |
| 3 | 2026-10-24 (name) | `AUDITOR/FINDINGS_2026-10-24_hygiene_61_62.md` | older Auditor record | `fa170e5d16c2fdada2d23870a234cbddfced86f1b64b8ecbf702847794189f73` | MATCH | 35 | 0/0/2/0 | — |
| 4 | 2026-10-24 (name) | `AUDITOR/FINDINGS_2026-10-24_order65_nl.md` | older Auditor record | `803fdeecfbb4409ac41862cf42290de52f309151fe3bbd5a2d39a2370427a489` | MATCH | 35 | 0/0/8/0 | — |
| 5 | 2026-10-24 (content) | `AUDITOR/HASH_INTEGRITY.md` | older Auditor record | `de07249389445fc9fb7c4b9ef85df24f8321b6eade485a5a0d2976357b7f910c` | NONE | 588 | 0/0/8/0 | ρ(W₇)/PathC, P5a, W₇ |
| 6 | 2026-10-25 (name) | `AUDITOR/AUTHOR_WRITTEN_IDENTITY_GAPS_SEARCH_2026-10-25.md` | older Auditor record | `b28c5ffe8c398b7f762ab8ec571b50c2102ffae44d4108030a5228faae9f7575` | NONE | 37 | 0/0/1/0 | — |
| 7 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_OWNER_WRITE_ITEM2_residual_factor_B1_CONFIRM.md` | older Auditor record | `f70af1097c81a5db9b2207ea245de55722f552bc268272ecdf7e052745ca65f1` | MATCH | 32 | 0/0/2/0 | W₇ |
| 8 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_local_geometric_bridge_chase_CONFIRM.md` | older Auditor record | `88ad1aa02b5089caf788ebd99e8b84cf767476660f2f63bc28669598543ab9e3` | MATCH | 41 | 0/0/3/1 | W₇ |
| 9 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_local_l1_l7_contact_CONFIRM.md` | older Auditor record | `4d400babcd0a56d7cc8b8fc47bc3a400bd2c1f450398017ec4dc752fa65b12c5` | MATCH | 36 | 0/0/2/0 | — |
| 10 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_paper_v13_partial_claim_audit.md` | older Auditor record | `1c9ff854f3dc3df85158c67ff3bff7772037e5ca0ef0f08e3cdebfe418dbb2b9` | MATCH | 38 | 0/0/2/0 | W₇ |
| 11 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t1049u_AUTHORITY_OPEN_DEADLOCKS_CONFIRM.md` | older Auditor record | `8e2488b4cecebaa8669ba8257dccd82dcf4def1383dcfdf32fdd353e309b48a1` | MATCH | 64 | 0/0/6/0 | ρ(W₇)/PathC, W₇ |
| 12 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t2101u_NL_PURSUE_ALL_APPROVED_CONFIRM.md` | older Auditor record | `209a26ed723111e72655b1240fa795bd8db672a43400230b95f412653d51f953` | MATCH | 29 | 0/0/1/0 | — |
| 13 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t2135u_PR1_SOFTSF_TIPPIN_788_CONFIRM.md` | older Auditor record | `7280b419d6b1a7dfa64d7735fd09037e122da2ccf910f9d030f062a356997867` | MATCH | 22 | 0/0/0/0 | — |
| 14 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t2148u_PR2_DEEPEN_CORPUS_CONFIRM.md` | older Auditor record | `aab0304fffce32b00159c28b01a640e658f842728cb079c8e2755d2cb91b025d` | MATCH | 23 | 0/0/0/0 | — |
| 15 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t2154u_MR1_R19_RHO_GAMMA_I_LISTING_CONFIRM.md` | older Auditor record | `45dec19b6390728b7c962a04ea096a4b8a3a02e33aa544592c492a4a81498fe6` | MATCH | 20 | 0/0/0/0 | ρ(W₇)/PathC, W₇ |
| 16 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t674u_nl_wpo2_wide_exhaust.md` | older Auditor record | `e2690d136a8adf8cde8d3ec6bbda211193bf1fee3782d1522af372dfddd2dc9b` | MATCH | 27 | 0/0/4/0 | — |
| 17 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t875u_nl_l1_l7_SF1_reCONFIRM.md` | older Auditor record | `bca79d0454da85949f13fb890c9a7110a7739bf082b18e32ee6442458f63f3fb` | MATCH | 25 | 0/0/1/0 | — |
| 18 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t875u_nl_l1_l7_theorems_CONFIRM.md` | older Auditor record | `1886ae2abd22810fe72ee41d20a9f8a3fbd8e1714dbcccc5ca281aed138e9e16` | MATCH | 35 | 0/0/2/0 | — |
| 19 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t876u_nl_l1_l7_zenodo_align_CONFIRM.md` | older Auditor record | `72ed1a619d4d564e73aa259bb1df4cedf2d7c3a86da6db7c251e45e16dac0c94` | MATCH | 42 | 0/0/2/0 | — |
| 20 | 2026-10-25 (name) | `AUDITOR/FINDINGS_2026-10-25_t928u_grokipedia_artifact_inventory.md` | older Auditor record | `f8d2f7e6ae917ae7898f2943dd1ddf09954bf209d8c9e9977b4fb647c403f385` | MATCH | 58 | 0/0/0/0 | — |
| 21 | 2026-10-25 (name) | `AUDITOR/OWNER_VOICE_APPROVE_PURSUE_ALL_BRIEF_t2101u_2026-10-25.md` | older Auditor record | `b8312e9fdab19bf53127a61e29b2a79084aae5941777597d2cd4ff7fd594e568` | MATCH | 18 | 0/0/0/0 | ρ(W₇)/PathC, W₇ |
| 22 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t0035u_MR2_SOFTSF_TIP_1O_FOLD_CONFIRM.md` | older Auditor record | `c6e05a66ccfbe4852f1480b4f9d120cf0f91e76d53c7f121e6454401c274bf6e` | MATCH | 33 | 0/0/0/0 | — |
| 23 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t1556u_WRITEONLY_SMITH_EIGEN_NLJOIN_CONFIRM.md` | older Auditor record | `329923f9eae09522a8f437fbf151b26ccb10e6350b0bfa9f09f764d891c6ddf6` | MATCH | 31 | 0/0/1/0 | — |
| 24 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t1954u_KEEPER_RETRIEVAL_BATCH23.md` | older Auditor record | `128c5da075368b2c4241304b6db24a4586de2580e78ed4c736b8f15ddb822492` | MATCH | 24 | 0/0/1/0 | — |
| 25 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2053u_KEEPER_RETRIEVAL_BATCH31.md` | older Auditor record | `4e9333d43a897300660302e985429c71fa4ab7e2f6a2d774801bbea0883400e7` | MATCH | 29 | 0/0/0/0 | S2X |
| 26 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2054u_KEEPER_RETRIEVAL_BATCH32.md` | older Auditor record | `1286dc4d3645378b9c32845647680edc31a933cb6cfae445b145c60b39a3281b` | MATCH | 29 | 0/0/1/0 | — |
| 27 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2111u_OWNER_WRITE_BLANKET_PURSUE_WRITE_AUTHORITY_CONFIRM.md` | older Auditor record | `62fe7149f2b4807d398e0ebdb90446d1130706dbaac4267c56069a86c377d119` | MATCH | 22 | 0/0/0/0 | — |
| 28 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2124u_MR2_DUAL_CONTINUE_BM_INGEST_JH_CONFIRM.md` | older Auditor record | `38f50643981184cd265083dfdfad46639fcf0152f782ba9b124d9d9a0c906c07` | MATCH | 19 | 0/1/0/0 | — |
| 29 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2125u_EIGEN_RULE5_ACCEPT_MR2_BM_INGEST_JH_CONFIRM.md` | older Auditor record | `d18e98c6ae3cf63932d03184616a87f17e311415368e1084901b4dccb30ac5df` | MATCH | 19 | 1/1/0/0 | — |
| 30 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2126u_EIGEN_RULE5_ACCEPT_MR2_RESID_REDUCIBLE_CONFIRM.md` | older Auditor record | `c3ec1ab59c1bd9d0038d6daea156f397d03a92b954f83fce94d33cdbe70563bf` | MATCH | 19 | 1/0/0/0 | — |
| 31 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2134u_EIGEN_RULE5_ACCEPT_MR2_EISDEPTH49_CONFIRM.md` | older Auditor record | `de896a023ebc9573bf85cd5f5231f856ba41c92e8411798827dac68a5984dc28` | MATCH | 19 | 1/0/0/0 | B2 |
| 32 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2135u_MR2_DUAL_CONTINUE_STURM49_CONFIRM.md` | older Auditor record | `e2d94f6e883c66d6a848e99fbcb0b8782709212ed1882f0a796b61ad4891ca8d` | MATCH | 19 | 2/0/0/0 | — |
| 33 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2136u_EIGEN_REVIEW_RELAY_MR2_STURM49_CONFIRM.md` | older Auditor record | `07e52b67afb6d80e67aa3aa5a7bdf4c53dfc1af19f8f614bc6d52a2193d297d6` | MATCH | 21 | 1/0/0/0 | — |
| 34 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2152u_MR2_DUAL_CONTINUE_THETA49_GAP_CONFIRM.md` | older Auditor record | `61e96b89299a54885c1ce0df100ea3fc01abb0be32d45c0cb821f3dd5a616d50` | MATCH | 19 | 1/0/0/0 | — |
| 35 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2153u_EIGEN_REVIEW_RELAY_MR2_THETA49_GAP_CONFIRM.md` | older Auditor record | `63fca52292a2c0cf172496bbede353c0001d58229de9735e52c886e068f2ca2a` | MATCH | 21 | 1/0/0/0 | — |
| 36 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2155u_EIGEN_REVIEW_RELAY_MR2_CKW49_CONFIRM.md` | older Auditor record | `075e851fe2d659f2f27d8847ace82e1243062fc2a1cae78cb76d638d16ef4d79` | MATCH | 21 | 1/0/1/0 | — |
| 37 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2158u_MR2_DUAL_CONTINUE_COEFF5311_CONFIRM.md` | older Auditor record | `80647770a31ee5146874a14b18f93ba2be1a205934ac2d7158a4cdc474693b0c` | MATCH | 21 | 2/0/0/0 | — |
| 38 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2203u_EIGEN_REVIEW_RELAY_MR2_CATB2_LATTICE_SEG_CONFIRM.md` | older Auditor record | `38f6cff1c9b2b36f476b307e2e178cd85bf995bdcf06a548a10a35eba08c4585` | MATCH | 21 | 1/0/1/0 | — |
| 39 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2205u_EIGEN_REVIEW_RELAY_MR2_END_SEG_CONFIRM.md` | older Auditor record | `33a1ca268ce924f40802c334dabd1458a22e154e8b8dd19a715121a81aa600ae` | MATCH | 21 | 1/0/0/0 | — |
| 40 | 2026-10-26 (name) | `AUDITOR/FINDINGS_2026-10-26_t2205u_MR2_DUAL_CONTINUE_KAPPA7_TRES_CONFIRM.md` | older Auditor record | `fa2b7ec39cca4883712b1ca45e3020d73f2d89a47478d3caa81650d5ef2f97d1` | MATCH | 22 | 1/0/0/0 | — |
| 41 | 2026-10-26 (name) | `AUDITOR/FINDINGS_AUDITOR_KEEPER_FIVE_MASTER_EQS_MUON_G2_CORPUS_2026-10-26.md` | older Auditor record | `1c947eb29ead041a00eb3a08cd5957649f1dd69d905294f0e9d080453b352e15` | MATCH | 41 | 0/0/0/0 | S2X |
| 42 | 2026-10-26 (name) | `AUDITOR/SOFTSF_PRESS_DEFERRED_2026-10-26/SOFTSF_PRESS_MR1_MESH_N_GT18_W7_SLASH_PREMISE_2026-10-26.md` | older Auditor record | `f60a75c157bc450746cbab745ed94284b3b34b13e7afa60500b92f02f3a30bc5` | MATCH | 10 | 1/0/1/0 | ρ(W₇)/PathC, W₇ |
| 43 | 2026-10-26 (name) | `AUDITOR/SOFTSF_PRESS_DEFERRED_2026-10-26/SOFTSF_PRESS_MR1_N6_MODP_Q121_D1_GA1_2026-10-26.md` | older Auditor record | `85198c6dc920ba937e6bcddd62cda6dec52badad270d80ba57e2e826da8309e7` | MATCH | 15 | 0/0/3/1 | W₇ |
| 44 | 2026-10-26 (name) | `AUDITOR/SOFTSF_PRESS_DEFERRED_2026-10-26/SOFTSF_PRESS_OWNER_WRITE_TEN_OPEN_SLOTS_LOCKED_CALL_0B65057E_2026-10-26.md` | older Auditor record | `7806ad0f1ed5a05da7e63b488818cf8c6c44dad595a1b727731075e911930220` | MATCH | 7 | 0/0/0/0 | — |
| 45 | 2026-10-26 (name) | `AUDITOR/SOFTSF_PRESS_DEFERRED_2026-10-26/SOFTSF_PRESS_PR1_E_LEAK_ALIAS_AXIOM_N_SCRIPT7D_MAP_2026-10-26.md` | older Auditor record | `6fc4619e1cf4cd1d6cc0d3fbe906fb5ff67f638af035777c0534d9a2d47fc47f` | MATCH | 25 | 0/0/0/0 | junction |
| 46 | 2026-10-26 (name) | `AUDITOR/SOFTSF_PRESS_DEFERRED_2026-10-26/SOFTSF_PRESS_PR1_HEPP_QM_GR_MISSED_VARS_FREE_PURSUE_2026-10-26.md` | older Auditor record | `70c3b6db7aba075312c41208d89026547b2bd8a3311982ffc9cbc07e3a39d388` | MATCH | 9 | 4/0/0/0 | — |
| 47 | 2026-10-26 (name) | `AUDITOR/_BRIEF_KEEPER_BATCH19_2026-10-26.md` | older Auditor record | `704b0c82a3e33b2186fee95cb4f3318b6259da6896b355d7f99ae65e3edd077b` | NONE | 36 | 0/0/1/0 | — |
| 48 | 2026-10-26 (name) | `AUDITOR/_BRIEF_KEEPER_BATCH1_2026-10-26.md` | older Auditor record | `55e41b8a3f056cbc9a45759c31f21d281e8be37715226cc0d49afd6fea834406` | NONE | 40 | 0/0/2/0 | — |
| 49 | 2026-10-26 (name) | `AUDITOR/_BRIEF_KEEPER_BATCH23_2026-10-26.md` | older Auditor record | `1268f1d21a83afb2bb93d52ce3c34ebb92875185b6f10e341c4b45b0e689e828` | NONE | 37 | 0/0/1/0 | — |
| 50 | 2026-10-26 (name) | `AUDITOR/_BRIEF_KEEPER_BATCH2_2026-10-26.md` | older Auditor record | `ab2a28f78093a9d58df99ccf66d0961b84e4c7cee1c06337af896cc5124507da` | NONE | 33 | 0/0/2/0 | — |
| 51 | 2026-10-26 (name) | `AUDITOR/_BRIEF_KEEPER_BATCH31_2026-10-26.md` | older Auditor record | `c81e66e3096af604ca6b149e64c21b58cb58e037ec8f2b6da8b80754f8f05754` | NONE | 35 | 0/0/1/0 | S2X |
| 52 | 2026-10-26 (name) | `AUDITOR/_BRIEF_KEEPER_BATCH32_2026-10-26.md` | older Auditor record | `61473240b51a22a307ba7d0f27f424d88b73bc25da0e283972e0059312914468` | NONE | 35 | 0/0/1/0 | — |
| 53 | 2026-10-26 (name) | `AUDITOR/_BRIEF_SOFTSF_CONFIRM_AM_THROUGH_BB_2026-10-26.md` | older Auditor record | `4335a2536d482acdc1756845a997962dce511dd4051762f60048a9d36bb7a0a4` | NONE | 110 | 0/2/9/0 | — |
| 54 | 2026-10-26 (name) | `SOFTSF_PRESS_MR1_COOK_RESUME_MATHLIT_G1_N36N6_PACKAGING_2026-10-26.md` | PRESS | `8ca2091e3e0137e7e6a94def9d4f13b1c4cd90d3181b7e936ea371209645b6d5` | MATCH | 7 | 0/0/0/0 | — |
| 55 | 2026-10-26 (name) | `SOFTSF_PRESS_MR1_PROMOTE_N36_NU21_25_FILLED_MODP_2026-10-26.md` | PRESS | `6177b32ab28a50b0a1304050f272eea91dc95613eb4c16141119948ea2b83c37` | MATCH | 31 | 0/0/2/0 | — |
| 56 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-G1blocked_2026-10-26.md` | PRESS | `14dce9869e9cdebaa87fd3ed6f77d77e7cf60b54824f66d20ce8f2362703e254` | MATCH | 22 | 1/0/0/0 | P5a |
| 57 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-bm-sigma_2026-10-26.md` | PRESS | `d2e5b4c1e2307235dab7d1bdbfa174f8a03b7a7b13a2a9f186d4fc2210c35814` | MATCH | 29 | 4/0/0/0 | P5a |
| 58 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-catb2-lattice-seg_2026-10-26.md` | PRESS | `002d1d38d243f923e2be1e3c7720bc9a3935f66dcbeb422cdef59754798749a9` | MATCH | 25 | 4/0/0/0 | ρ(W₇)/PathC, P5a |
| 59 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-ckw49_2026-10-26.md` | PRESS | `59a80c5cdc076921ccc1cedeb4e7fd617cfab3fc1d34eb80b78a631fd363ae60` | MATCH | 30 | 3/0/1/0 | ρ(W₇)/PathC, P5a |
| 60 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-coeff5311_2026-10-26.md` | PRESS | `44954717dbab9191f1398a1f71fc97800ce38c7a2e6f677a1965eb63a3a170b2` | MATCH | 18 | 7/0/0/0 | P5a |
| 61 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-end-seg_2026-10-26.md` | PRESS | `7d81b0497f4f7db5f90a15910ace676f60ae0178a7992a28048c3c0562f3823c` | MATCH | 29 | 6/0/1/0 | P5a |
| 62 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-hu-tan-L1_2026-10-26.md` | PRESS | `de21dd078afddf67be3fcb33e9abe1b1956c58a305391c9e023c36a394e2f357` | MATCH | 36 | 4/0/1/0 | P5a |
| 63 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-kappa7-tres_2026-10-26.md` | PRESS | `397f1e928ec03794ae22f56f35e34d4d96a4c6cb700aad4ccab0bbd1e502ba0d` | MATCH | 26 | 5/0/0/0 | P5a |
| 64 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-residual-mult-bm_2026-10-26.md` | PRESS | `973815a806add3c108c68b936a5c024e571f273dda2ba17900a83060d69dbeae` | MATCH | 40 | 4/0/4/0 | P5a |
| 65 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-sturm49_2026-10-26.md` | PRESS | `d2c5ddcd189a326adcfb7bb0d3672337cd0459b8cda0d407ddf43ee55ed92414` | MATCH | 5 | 2/0/0/0 | — |
| 66 | 2026-10-26 (name) | `SOFTSF_PRESS_MR2-DUAL-CONTINUE-theta49-gap_2026-10-26.md` | PRESS | `083f06bb7d55fc5ec2b6eed35a9bc17699628c9f0c8c9071889f068b037493d7` | MATCH | 13 | 2/0/0/0 | P5a |
| 67 | 2026-10-26 (name) | `SOFTSF_PRESS_OWNER_WRITE_BLANKET_OWNER_PURSUE_WRITE_AUTHORITY_ALL_LANES_2026-10-26.md` | PRESS | `1bf3d2f7dda96f3cde3eeec6b4db105629ed21a304ffed1cc460026cfefd642a` | MATCH | 4 | 0/0/0/0 | — |

Sidecars for #1–67: 57 MATCH, 10 NONE, 0 MISMATCH.

## 2. Math claims recomputed
| # :line | claim | Auditor | recompute |
|---|---|---|---|
| #11:25 | W₇ = (0,−1;49,0) and W₇² = −49·I, a scalar, so the identity projectively | PROVED | direct product |
| #63:8–9 (SF-K1) | H¹(G_{Q,{7,∞}}, μ₇) = Z[1/7]^×/7 ⊕ Cl[7] = ⟨κ(7)⟩ | PROVED | −1 = (−1)⁷ is a 7th power; Cl(Z[1/7]) = 1 |
| #63:11 (SF-K2) | κ(7)\|G_Q₇ is très ramifié: v₇(7) = 1 ≢ 0 (mod 7), so it is not in ⟨κ(8)⟩ | PROVED | Q₇^×/7 ≅ ⟨7⟩ × (1+7Z₇)/(1+49Z₇) ≅ F₇²; 8 ∈ 1+7Z₇ \ 1+49Z₇ |
| #61:15–16 | v_λ(7) = 6 in Q(ζ₇); (a+λy)⁷ ≡ a⁷ (mod λ⁷), then Kummer's lemma (7 regular) | PROVED, with Kummer's lemma cited | binomial terms 7·(…) lie in λ⁶·λ |
| #64:29 (SF-M2) | multiplicity 1 for every nonzero z(σ) | CONDITIONAL on cited BM / HS inputs | not rerun |
| #65 (SF-C1) | Sturm bound 19 for Γ₀(49), weight 4 | PROVED | ⌈4·56/12⌉ = 19 |
| #66 (SF-D1, D2) | p¹³ + p³² = p¹³σ₁₉(p); CKW shift k ↦ k + 86; 20 + 13·86 = 1138; 1138 − 4 = 1134 = 27·42 = 6·189; E₆⁷ ≡ 1 (mod 49); Sturm bounds 5311 (Γ₀(49)) and 31864 (Γ₀(196), index 336) | PROVED (arithmetic). E₆⁷ ≡ 1 mod 49 follows from 504 = 7·72 | all recomputed |
| #60 (SF-F1, F2) | f = η³(z)η³(7z)θ_Q = 7.4.a.a; a_n ≡ n¹³σ₁₉(n) (mod 49) for all 7 ∤ n ≤ 5311; a_{7m}(f^{[7]}) = 0 | PROVED (finite computation, rerun) | rerun in /tmp: a₁…a₁₀ = 1, −1, −2, −7, 16, 2, −7, 15, −23, −16; a₇ = −7; 0 failures; mod 343 fails at n = 2 (residue 196) |
| #42:5 | "W₇-slash route refuted on current carrier" (G2: ρ(W₇) absent on V₄₂, R26 rank 9) | **re-labelled CONDITIONAL**. R26 is numeric; under the pure-math standard this is not a refutation by proof. Not re-adopted | |
| #11:24,40 | ρ(W₇) = +1 on the form space (W-D4) is "an Owner premise, not derived" | concur: it is a premise, not a theorem | |

## 3. Owner-decision checks (older Auditor records)
- **κ/Λ₀ old values:** none in #1–67. The κ hits are homonyms:
  - Kummer classes κ(7), κ(8) (#40, #57, #61–#64);
  - tunnel κL (#1:437–439);
  - κ_dark (#41).
- **B2:** #31 uses "SF-B2" for an Eisenstein mod-49 lift. This is a homonym, not B2 / (B)-M.
- **P5a hits (#56–#66):** "No P5a" status boilerplate only. #5:579 records the 10-26 P5a rewrite fold "(Γ₀(49), to prove)" that produced the current tip 7cddb188.
- **R_c, junction, Layer2:** see §4.

## 4. Bridge items
- **R_c, Layer2, S²-11DM²ET-X:** no source in #1–67.
- **Junction:** #45 lists "7D junction readings" in a deferred PR1 E-leak queue. It is a mention only, so the junction stays OPEN.
