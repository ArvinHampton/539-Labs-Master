# AUDITOR: Corpus crawl BATCH 20. s_family_paths math-bearing files (82), 2026-10-19 → 2026-10-24, then undated; plus custody re-check of the B19-3 mismatches
Date: 2026-11-09 (America/Chicago). Lane: Auditor, audit-only.

## §0. Owner decisions (recorded in order; via Physicist and Mathematician relay; not confirmed in Auditor chat)
Both files were re-hashed live, and each matches its sidecar (read-only check).

1. **~13:41 CST — SUPERSEDED.** `reports/OWNER_WRITE_CALL_e9c1dbda_B16_1_B11_1_REOPENS_PATHC_LOCK_2026-11-09_1341.md`, sha `0deba43db59d11d8c725eb5c643129f4be33be42d06931c3dae594abd6fc81ca`.
   - Verbatim: "B11-1 reopens the 10-26 Path C lock; the W₇ question is OPEN again and P5a (Γ₀(49)⁺, W₇ = +1) stays the operative version, OPEN."
   - **Superseded by item 2.** Recorded as history only; it has no operative effect.
2. **~13:42 CST — OPERATIVE.** `reports/OWNER_WRITE_CALL_e9c1dbda_B18_1_W7_ON_NEWFORM_PATHC_STANDS_2026-11-09_1342.md`, sha `c4c0f1c0318691c045b136c01c4de7eb86690ae9c8db4d20b07939a6fd8b24ed`.
   - Verbatim: "B11-1's W₇ = +1 means the Atkin–Lehner eigenvalue on the newform 7.4.a.a (ε = +1 from a₇ = −7, standard normalisation); the tip's Path C (ρ(W₇) absent on V₄₂, group Γ₀(49)) stands unchanged; P5a stays OPEN."
   - The file states that it supersedes 0deba43d.

**Applied:**
- **Path C stays in force.** The tip's Path C text (L61, L107, L217, L247) now **agrees** with the operative decision. The tip was not edited; its sha is 7cddb188…dfc91.
- **RESOLVED: B16-1, B17-1, and B18-1 Q1–Q4.**
  - Q1 space = the newform 7.4.a.a.
  - Q2 group = Γ₀(49) for Path C, with ρ(W₇) absent on V₄₂.
  - Q3 normalisation = standard.
  - Q4: Path C is not reversed.
- **P5a stays OPEN.**
- The batch-19 notes (#39/#48 "superseded", and #27 "level-7 W₇ ≠ level-49 W₇") are history and evidence, not verdicts.

**Auditor check of ε = +1 (requested):**
- For a newform f ∈ S_k(Γ₀(N)) with trivial character and p ∥ N, a_p = −p^{k/2−1}·ε_p, where ε_p is the W_p eigenvalue (standard Atkin–Lehner / Li; cited, not re-derived).
- For 7.4.a.a: N = 7, k = 4, so a₇ = −7·ε₇.
- a₇ = −7 was recomputed from η³(z)η³(7z)θ_Q in batch 18 (a₁…a₁₀ = 1, −1, −2, −7, 16, 2, −7, 15, −23, −16).
- Hence **ε₇ = +1. PROVED, given the cited formula.**
- **Consistency with batch 19 #27:** the operator is W₇ = (0, −1; 7, 0) on Γ₀(7), the level-7 Fricke involution. That is exactly the element #27 distinguished from the level-49 Fricke (0, −1; 49, 0). The decision therefore places "+1" on the level-7 operator, and **nothing is asserted for W₄₉ on V₄₂**, consistent with Path C. **Consistent.**
- **Wording note (N20-1, not a blocker).** Older P5a text still reads "(Γ₀(49)⁺, W₇ = +1)". Under the operative decision, "W₇ = +1" must be read as ε₇(7.4.a.a) = +1 (level 7), and the operative group is Γ₀(49). Recorded only; nothing was edited.

## Scope and method
- **Scope.** The 82 math-marker `.md` files in `s_family_paths/` (covered = N, not outside reports/, not in batches 01–19), oldest first.
- **Ordering.** Content date (62), path date (2), name date (1); 17 undated files go last, ordered by path. mtimes carry no weight.
- **Method.** Read-only. Live sha = manifest sha for all 82. Recomputation ran only in /tmp/aud20. No sidecars were created or repaired. No edits; no CERT; nothing external.

## 1. Custody (P/C/O/R = PROVED/CONDITIONAL/OPEN/REFUTED word counts)
| # | date (src) | file (under reports/) | sha256 | sidecar | lines | P/C/O/R | flags |
|---|---|---|---|---|---|---|---|
| 1 | 2026-10-19 (content) | `s_family_paths/A/REPORT.md` | `d8a7d98c49cdf986bb029eabc7d31e6e73905346852dcbcb889f46b92af8ac38` | NONE | 203 | 0/0/0/0 | — |
| 2 | 2026-10-20 (content) | `s_family_paths/A/REPORT_final.md` | `6abee963422bb23f46d43c0520a7d808a71bb0fa643ec0c0f1cea4d2c602f0ff` | NONE | 123 | 0/0/0/0 | — |
| 3 | 2026-10-20 (content) | `s_family_paths/A10_uniform_Spairing/REPORT.md` | `7a65f062361835ad5848c77ff75bc617005c3b4f1690d41b7a0c1d753cce000e` | NONE | 83 | 0/0/0/0 | — |
| 4 | 2026-10-20 (content) | `s_family_paths/A2/REPORT.md` | `f0ccac4b38748abb74bf8d5b085e0867d772892f9faa22cbc65083ea67cb8910` | NONE | 122 | 0/0/0/0 | — |
| 5 | 2026-10-20 (content) | `s_family_paths/A3_chen/REPORT.md` | `a4ea5c5f7d7d7814865ba6e1faa81901a2d73b5cfcd1143474580860fff8e27a` | NONE | 65 | 0/0/0/0 | — |
| 6 | 2026-10-20 (content) | `s_family_paths/A4_dist/REPORT.md` | `74c790a7494094d11b6d2440e52e457591ab653d3a56996715f60d1c540190db` | NONE | 184 | 0/0/0/0 | "junction" homonym |
| 7 | 2026-10-20 (content) | `s_family_paths/A6_certify/REPORT.md` | `151cbcc89168063c695a181bcff7010117bc6a0a7ed187c756f17c7f8edd1c52` | NONE | 122 | 0/0/0/0 | — |
| 8 | 2026-10-20 (content) | `s_family_paths/A7_s21/REPORT.md` | `3335ce0bc57f0f2dc271fd821ba715bb9db7499d75ef5dd5c016665136fcb416` | NONE | 114 | 0/0/0/0 | — |
| 9 | 2026-10-20 (content) | `s_family_paths/A8c_Spairing_even/REPORT.md` | `ec4c29ab310157853df9ca2aae36808fe03ae17d9595f6181f168f0c669ae36c` | NONE | 134 | 0/0/0/0 | — |
| 10 | 2026-10-20 (content) | `s_family_paths/B/REPORT_knot.md` | `6df56740465a07e1f442fdab364936fe290a15e8ee9931886fdbde0b2cc8b903` | NONE | 43 | 0/0/0/0 | — |
| 11 | 2026-10-20 (content) | `s_family_paths/B/c2_wall/REPORT.md` | `ac46cea798448732c9ef1cfc14074d7f89ce65e1d81d507f440778e23fc2169d` | NONE | 108 | 0/0/0/0 | — |
| 12 | 2026-10-20 (content) | `s_family_paths/B/theta_u1_origin/REPORT.md` | `857769c3c0973008c5dea29cac78c4397d9cb021a5f3d2d1cc1a3924120c43d9` | NONE | 59 | 0/0/0/0 | — |
| 13 | 2026-10-20 (content) | `s_family_paths/galois_review/REVIEW.md` | `fb38da84b89bef9d6d4bb515bcf88c79292c867c033ddd347f9b92efc4fc7e71` | NONE | 72 | 0/0/0/0 | S2X |
| 14 | 2026-10-21 (content) | `s_family_paths/A11_induction/REPORT.md` | `0707bb128fa8d23dd9c4876d61babb159c0478d7a5d53989deb5e09ccd42d5f7` | NONE | 144 | 0/0/0/0 | — |
| 15 | 2026-10-21 (content) | `s_family_paths/A12_H1H2_odd/REPORT.md` | `b2a42803b094099e414c5299f21f9db39c57579cd46e0e8a1c60e88008d98761` | NONE | 133 | 0/0/0/0 | — |
| 16 | 2026-10-21 (content) | `s_family_paths/A15_ST_balance/REPORT.md` | `7a1c48702863204e8815b71a11e4bf17bdae07e3aaef7f942794df60bae3921e` | NONE | 244 | 0/0/0/0 | — |
| 17 | 2026-10-21 (content) | `s_family_paths/A18_RTA_foundation/REPORT.md` | `3b34eafca8b48e0ac60e3e4ca30d6fa09a7fbfb0d36bb8be0bdc5ba8e40a4d0e` | NONE | 113 | 0/0/0/0 | S2X |
| 18 | 2026-10-21 (content) | `s_family_paths/A19_9maths_axioms/REPORT.md` | `93f04ac33e954ad20404d49e5a41af07e4222efdde7b6acd7539a2fe57d2fe61` | NONE | 263 | 0/0/0/0 | S2X |
| 19 | 2026-10-21 (content) | `s_family_paths/A20_T3_bulk_vs_shadow/REPORT.md` | `00bce768174ae3a64471fc4a5a205f880dc40c33853200340c99fcee2d147400` | NONE | 138 | 0/0/0/0 | — |
| 20 | 2026-10-21 (content) | `s_family_paths/A21_grok_chat_search/REPORT.md` | `dcf764b8be8576944df50feb4960b70b1df3ba2c27fe1da81f79601236b7c570` | NONE | 134 | 0/0/0/0 | — |
| 21 | 2026-10-21 (content) | `s_family_paths/A22_grok_export_search/REPORT.md` | `100541bd884b06a2c5a9e10752c87879679d3d7c349d0a0ae310d04265008c5b` | NONE | 106 | 0/0/0/0 | — |
| 22 | 2026-10-21 (content) | `s_family_paths/RTA_prereg/REPORT.md` | `c8af349a463fa0858bb1a051326ee1ba3b4e98895d693d5571539c2ff80a549f` | NONE | 96 | 0/0/0/0 | — |
| 23 | 2026-10-22 (content) | `s_family_paths/A23_axiom01_revised/REPORT.md` | `fdb70c0701e588b1ac876946c2472a97995b338dced1bfa54d5b2e2b5a33feb6` | NONE | 172 | 0/0/0/0 | — |
| 24 | 2026-10-22 (content) | `s_family_paths/A24_threshold_1e18/REPORT.md` | `0dec7be3a8de88bdcee853448fa578a330c9b77a81f6304059849e54f46268eb` | NONE | 115 | 0/0/0/0 | — |
| 25 | 2026-10-22 (content) | `s_family_paths/A26_drive_review/REPORT.md` | `4ff0c4c5ef072ca48f3ac7f7d1c3d726e8a615ac95caaa954f8fbbbdbe609b1b` | NONE | 119 | 0/0/0/0 | S2X |
| 26 | 2026-10-22 (content) | `s_family_paths/A27_drive_review_complete/REPORT.md` | `48526ba7b2506b4573f65d9926bc0a51f47fa3486e90afbd138f917686a2fc36` | NONE | 102 | 0/0/0/0 | S2X |
| 27 | 2026-10-22 (content) | `s_family_paths/A28_H3_map_construction/REPORT.md` | `ee8994765b4dfe3312ec2ac5e10dc069090b9070fbd3ec58d6201c70b87a1452` | NONE | 158 | 0/0/0/0 | — |
| 28 | 2026-10-22 (content) | `s_family_paths/A29_patterns_all/REPORT.md` | `d752992b015488f9ce7bd911783e9dd823b7a043e61d7c206871649eceda79b8` | NONE | 153 | 0/0/0/0 | — |
| 29 | 2026-10-22 (content) | `s_family_paths/A29_patterns_all/report_template.md` | `2618a6b36ef34f8f0080b79e2db508d5a81b28532f229c0791fdbfec6011f0d5` | NONE | 85 | 0/0/0/0 | — |
| 30 | 2026-10-22 (content) | `s_family_paths/A31_entry7_check/REFEREE.md` | `e2d954cf5b18a0cbdfe1123f7efa83602b83c94a318d9d14887f4fc1836418ec` | NONE | 70 | 0/0/0/0 | — |
| 31 | 2026-10-22 (content) | `s_family_paths/A34_ledger_checks/REPORT.md` | `985a55a5aca361a8079bc4e87d32edaf4126be0c9da1ebff5d4c409cb89a0804` | NONE | 269 | 0/0/0/0 | "junction" homonym |
| 32 | 2026-10-22 (content) | `s_family_paths/A35_lawspace_exact/REPORT.md` | `57b6f24c70d4cc22b563eb08f83ad1d3071b9dc2366572f9863c5cb3394ae656` | NONE | 129 | 0/0/0/0 | — |
| 33 | 2026-10-22 (content) | `s_family_paths/A36_hecke_character/REPORT.md` | `33782e5469a1a2069f3c3d7d28a063990879659de377c28493fe566f77e8433b` | NONE | 137 | 0/0/0/0 | — |
| 34 | 2026-10-22 (content) | `s_family_paths/A37_dihedral_count/REPORT.md` | `ea07df7bbfd7090949455833d51891a430782d482c27fc2d558c72dd37d25434` | NONE | 75 | 0/0/0/0 | — |
| 35 | 2026-10-22 (content) | `s_family_paths/A38_lemmaL/REPORT.md` | `166ad91504886f59c5ef39c7910e3f9c896cb77695326980745dbe38e592e702` | NONE | 98 | 0/0/0/0 | S2X |
| 36 | 2026-10-22 (content) | `s_family_paths/A39_gk_family/REPORT.md` | `c71069fa81f643276eb65f846bb8fdfaba43b7cf5fed79664903d6c2f164efb3` | NONE | 205 | 0/0/0/0 | — |
| 37 | 2026-10-22 (content) | `s_family_paths/A41_uniform_oddk/REPORT.md` | `7ec18f976ee542e3ad2c75b51ff6f3bc5201b5c5844ebd950e50076d2b8ed802` | NONE | 199 | 0/0/0/0 | — |
| 38 | 2026-10-22 (content) | `s_family_paths/A44_oddk_audit/REPORT.md` | `2a959e0393c2aaa6a69f550fdbd301c7d92c0addd99ddb008967dd32a6dd05ff` | NONE | 186 | 0/0/0/0 | — |
| 39 | 2026-10-22 (content) | `s_family_paths/A45_cross_review/REPORT.md` | `0c6fc2eb1765130314c51355fc1bd93ce825c537551a572c435d4d3c9857c7ab` | NONE | 218 | 0/0/0/0 | — |
| 40 | 2026-10-22 (content) | `s_family_paths/A46_zero_facts_audit/REPORT.md` | `b635bb7778f9fbbee26a7bac239c0caceb788e11e9c70ef87668bf39ad3603aa` | NONE | 75 | 0/0/0/0 | — |
| 41 | 2026-10-22 (content) | `s_family_paths/A47_composite_zeros/REPORT.md` | `1be9005afc0816e16139d985d8371962fa158f68fad4f6774d808941cae24cf2` | NONE | 87 | 0/0/0/0 | — |
| 42 | 2026-10-22 (content) | `s_family_paths/A49_gk_runs/REPORT.md` | `2ece297293e3d9d657fb2ac091c40e3c921ba855647a6097325f61482109b08e` | NONE | 128 | 0/0/0/0 | — |
| 43 | 2026-10-22 (content) | `s_family_paths/A50_proofs/REPORT.md` | `1d7edb3eb0f6eb9f5456b6f9b4a97cf2de651f900a80de8e2d1d8b2e9fe257b5` | NONE | 128 | 0/0/0/0 | — |
| 44 | 2026-10-22 (content) | `s_family_paths/A52_bridgeC_to_RTA_draft/prereg_draft.md` | `25851b855c3c5405dcf1c66632c62532fab68b75e1d5fe73cb96ac3611fb7f82` | NONE | 132 | 0/0/0/0 | W₇ (x↦−1/(7x)), S2X |
| 45 | 2026-10-22 (content) | `s_family_paths/A53_RTA_maps/prereg.md` | `a44f677970db173baf4af4589d598288623012ff55dd98c5346961a58fa33c52` | NONE | 166 | 0/0/0/0 | W₇ (x↦−1/(7x)), S2X |
| 46 | 2026-10-22 (content) | `s_family_paths/A54_proofs2/REPORT.md` | `688ac65268ba71280f62542fcf6a489af50ecc645c8a762dfc909f37f31b9156` | NONE | 99 | 0/0/0/0 | — |
| 47 | 2026-10-22 (content) | `s_family_paths/A55_small_k_exceptions/REPORT.md` | `6812d543b9595fb3016c6eb6649bfdb8184671d81f276bb049fbb09715309aa4` | NONE | 392 | 0/0/0/0 | — |
| 48 | 2026-10-22 (content) | `s_family_paths/A55_small_k_exceptions/template.md` | `3d168ef8cd3ef5a548f0fdadeb8ef70cc0bb986adbf15a4c100a3892a5fdf349` | NONE | 181 | 0/0/0/0 | — |
| 49 | 2026-10-22 (content) | `s_family_paths/A56_A49_audit/REPORT.md` | `074d95fba25c4960900223984297d601d8e421e8ef16f9e13635bae90f17e33a` | NONE | 200 | 0/0/0/0 | — |
| 50 | 2026-10-22 (content) | `s_family_paths/A58_chern_bound_audit/REPORT.md` | `52ae80a0a76d8df7c2e4c6a22ebb89cb09e6228d4432add693c9bcfd99bcfb86` | NONE | 133 | 0/0/0/0 | — |
| 51 | 2026-10-22 (content) | `s_family_paths/A59_clt_rederivation/REPORT.md` | `11e8f69da66a32a4cc187445610a6de01d1ba8a19443d4d794e4f32d52d72dae` | NONE | 131 | 0/0/0/0 | — |
| 52 | 2026-10-22 (content) | `s_family_paths/A61_clt_proofs/REPORT.md` | `f38014404d3de68444c5c436c2a0283f19f2b830b17627b2ba6b516e0c7f3961` | NONE | 97 | 0/0/0/0 | — |
| 53 | 2026-10-22 (content) | `s_family_paths/A61_clt_proofs/prereg.md` | `e2adfff0dd3b2d03cba2a6c18c51c41a75701333305e09983218ffd91550df13` | NONE | 45 | 0/0/0/0 | — |
| 54 | 2026-10-22 (path) | `s_family_paths/LEDGER_CatA_2026-10-22/LEDGER.md` | `4907a400932916dba1d320a85c096ef4e7a4dbefe137021d100f4ecadab15ede` | NONE | 329 | 0/0/0/0 | — |
| 55 | 2026-10-22 (path) | `s_family_paths/LEDGER_CatA_2026-10-22_rev1/LEDGER.md` | `5a730939f342308c9e7668cb28038bb15532428955afb6824f05774e84f432bf` | NONE | 350 | 0/0/0/0 | — |
| 56 | 2026-10-22 (content) | `s_family_paths/LEDGER_CatA_clean/LEDGER.md` | `10b1c3ec89a696feba80ef12e5dea017f4584d7cc6c888afd830b29d32de18b8` | NONE | 253 | 0/0/0/0 | — |
| 57 | 2026-10-22 (content) | `s_family_paths/LEDGER_CatA_clean_v2/LEDGER.md` | `f319045e1ed5a00f88d033541eff670dfe98088e6b8900dac38c61b17ca0f188` | NONE | 305 | 0/0/0/0 | — |
| 58 | 2026-10-22 (content) | `s_family_paths/LEDGER_CatA_clean_v3/LEDGER.md` | `d863d4bf8ceaa53c545ce825204424d1e0aa78dbc0214d37792fdc6b9f674108` | NONE | 362 | 0/0/0/0 | — |
| 59 | 2026-10-22 (content) | `s_family_paths/LEDGER_CatA_clean_v4/LEDGER.md` | `1e5e002e3b920c8a1ffece1cdaa191b8bc8435d829af2a0838f5b5d97abb7796` | NONE | 407 | 0/0/0/0 | — |
| 60 | 2026-10-22 (content) | `s_family_paths/LEDGER_CatA_clean_v5/LEDGER.md` | `418687fa55bd793407c302d070a73f2609b8af547e96630882f5b1b717682d31` | NONE | 446 | 0/0/0/0 | S2X |
| 61 | 2026-10-22 (content) | `s_family_paths/LEDGER_CatA_clean_v6/LEDGER_CatA_clean_v6.md` | `e4733b803144dc1dbabca5a6cd7d3580fbe0666619b30de3afd286b492dc0bee` | NONE | 489 | 0/0/0/0 | — |
| 62 | 2026-10-22 (content) | `s_family_paths/LEDGER_CatA_clean_v7/LEDGER_CatA_clean_v7.md` | `ad4c4031fc2a494a3a8a7d03be990de4078c6b893c1d1e895d0267297381b435` | NONE | 601 | 0/0/0/0 | — |
| 63 | 2026-10-23 (name) | `s_family_paths/LEDGER_CatA_clean_v7/LEDGER_ADDENDUM_T3_2026-10-23.md` | `bf96119724c5abf8284f50151ddb9e576e47163d723063bce4b424be4d371d02` | NONE | 30 | 0/0/0/0 | — |
| 64 | 2026-10-23 (content) | `s_family_paths/LEDGER_CatA_clean_v8/INDEX.md` | `37564057ffc12905ddbd96a3d9032e489a1c8fdb106e79cdc1b34e02e6adb555` | NONE | 116 | 0/0/0/0 | — |
| 65 | 2026-10-24 (content) | `s_family_paths/LEDGER_CatA_clean_v8/LEDGER.md` | `dc060d05932a89d05caeb5771d619d54b0a2ee405bef1195b14bdff1fc5bbd31` | NONE | 764 | 0/0/0/0 | — |
| 66 | — (none) | `s_family_paths/A59_clt_rederivation/DERIVATION.md` | `2240572b886bab2df7aec9294d1eb7235c3a4b159d81bd997239016848ce7936` | NONE | 120 | 0/0/0/0 | — |
| 67 | — (none) | `s_family_paths/A61_clt_proofs/PROOFS.md` | `dce1311e4e9113f26b7ccbd86cded64f3e88a904318848194dd255a832586b67` | NONE | 216 | 0/0/0/0 | — |
| 68 | — (none) | `s_family_paths/LEDGER_CatA_clean_v6/sec7.md` | `b6e32884b3c9e0f0385523e9aa6104fad2a8ce7249a445bac8ccbb1f12451edd` | NONE | 80 | 0/0/0/0 | — |
| 69 | — (none) | `s_family_paths/LEDGER_CatA_clean_v7/sec7_new.md` | `b28ebdc0ca2d2f7432c29c934e5669bb702744e826ccda2c84d5c94aac4bffa7` | NONE | 111 | 0/0/0/0 | — |
| 70 | — (none) | `s_family_paths/LEDGER_CatA_clean_v8/sec_v8_new.md` | `d5736b93bad28d5f3991b6f827af1baa0151be580a2f2071e5b827b2fd800e5c` | NONE | 138 | 0/0/0/0 | — |
| 71 | — (none) | `s_family_paths/PAPER_gk_v1/PAPER_notes_for_arvin.md` | `a50c6bb38bf3d20b9e31cccde6654fe75080659c116c29af41c899919be4b182` | NONE | 49 | 0/0/0/0 | — |
| 72 | — (none) | `s_family_paths/PAPER_gk_v1/sections/00_front.md` | `ca25de561b2035995766a3d2e393630c9528a712eaebaae997960434056222e4` | NONE | 31 | 0/0/0/0 | — |
| 73 | — (none) | `s_family_paths/PAPER_gk_v1/sections/01_defs.md` | `200376aa7d2ad7d27402b2ad5431ff66adcd6f0aa11500cb09d07b94ba89d446` | NONE | 41 | 0/0/0/0 | — |
| 74 | — (none) | `s_family_paths/PAPER_gk_v1/sections/02_series.md` | `49a9ac56525f32b5cf3d762fea5cc6c314a6e7d71af3c023429459295b411012` | NONE | 79 | 0/0/0/0 | — |
| 75 | — (none) | `s_family_paths/PAPER_gk_v1/sections/03_zero.md` | `c910db018bd928d4d80ab5785c34121aa8635cd94265a35a1100112eb3a1974c` | NONE | 79 | 0/0/0/0 | — |
| 76 | — (none) | `s_family_paths/PAPER_gk_v1/sections/04_composite.md` | `d512f65ddce8c9d99a3de0fa4b36c93f14204eb302789737cca2940552372a9a` | NONE | 185 | 0/0/0/0 | — |
| 77 | — (none) | `s_family_paths/PAPER_gk_v1/sections/05_even.md` | `ac318d82aab7603a095d7a0afa916c72e4e2959c4572eec7bf1065687e61bc37` | NONE | 97 | 0/0/0/0 | — |
| 78 | — (none) | `s_family_paths/PAPER_gk_v1/sections/06a_pd_model.md` | `78935b403377e9af315bf5442ab74405f1f9024aa050fa17228b60de67e9f4a8` | NONE | 125 | 0/0/0/0 | — |
| 79 | — (none) | `s_family_paths/PAPER_gk_v1/sections/06b_pd_cells.md` | `d43ecbc958d6debe83ee895cc99aa87fea49105e9009d8414bdcd1db51b03d0d` | NONE | 60 | 0/0/0/0 | — |
| 80 | — (none) | `s_family_paths/PAPER_gk_v1/sections/06c_pd_block.md` | `1749738dfe4c24f374b86ff6c2bb87fe07765f1a7c86bddc0c91cfe438ea581a` | NONE | 121 | 0/0/0/0 | — |
| 81 | — (none) | `s_family_paths/PAPER_gk_v1/sections/06d_pd_cert.md` | `70ad649275cd6ee808bb37b10fea43901efd365a80958e526bd4f079b9d018f8` | NONE | 125 | 0/0/0/0 | — |
| 82 | — (none) | `s_family_paths/PAPER_gk_v1/sections/07_appendix.md` | `0005ae163b2652a5dba77099f06eb4ca8e8224ee7d11e2f4828b743da25d4c3f` | NONE | 54 | 0/0/0/0 | — |

Sidecars: **0 MATCH, 82 NONE**. All of s_family_paths has no sidecar. Recorded only (B10-1).

## 2. Math claims recomputed
| # :line | claim | Auditor | recompute |
|---|---|---|---|
| #2:17 (A/REPORT_final) | Theorem 1a equality case: odd s with s and s−2 both prime powers; "8245 such cases up to 10^6" | count PROVED (for odd 5 ≤ s ≤ 10⁶). The bound itself is CONDITIONAL (proof in REPORT.md §1, not re-derived) | sieve: 8245 |
| #2:18 | d_cusp = 0 iff s ∈ {6, 8, 10} | CONDITIONAL (proof uses d₂ ≤ 2^{k−1} + 6 plus a direct check for s ≤ 18; scan to 10⁶ not rerun) | |
| #33:31 | Q(x) = x₁² + s·x₁x₂ + (s/2)x₂² = N(x₁ + ωx₂), with ω = (s+√n)/2 and n = s(s−2) | PROVED | ω + ω̄ = s; ωω̄ = (s² − n)/4 = s/2 |
| #43:79 | k \| u² − 4 with u odd, u ≥ 3, implies u² ≥ k + 4 | PROVED | u² − 4 ≥ 5 > 0, so u² − 4 ≥ k |
| #47:25 | 1/((1+x)(1+x²)) = (1−x)/(1−x⁴), so φ₂(m) = 1, −1, 0, 0 for m ≡ 0, 1, 2, 3 (mod 4) | PROVED | (1+x)(1+x²)(1−x) = 1 − x⁴ |
| #7:61, #62:24, #65:25 | for odd s ≥ 5, tr_C ρ(S) = 0, so dim C⁺ = dim C⁻ | CONDITIONAL ("Assume TB3", as stated) | |
| #44:51, #45:51 | scalar W₇ slash obstructed (178 of 270 rationals) | CONDITIONAL (finite computation, not rerun; same as 17a #34). Here "W₇" means x ↦ −1/(7x), a homonym of the §0 operator | |
| #6:91 | no specific k ≥ 3 is proved to have 1 − 3/2^k in L (a parity-type problem) | concur: OPEN | |

## 3. Owner-decision checks
- **κ/Λ₀ (old or new), R_c, Layer2, P5a, ρ(W₇), B2:** none in the 82 files. No affected claims.
- **"junction"** (#6, #31) refers to Chen/sieve-type results. This is a homonym; no junction source.

## 4. Bridge items
- **R_c, junction, Layer2 transfer, S²-11DM²ET-X objects:** no source in s_family_paths. S2X hits (#13, #17, #18, #25, #26, #35, #44, #45, #60) are mentions only.
- **Closable: none.**

## 5. Custody re-check of the 5 B19-3 sidecar mismatches (read-only; no sidecar created or repaired)
This repeats and confirms batch 10 (`AUDITOR_CORPUS_CRAWL_BATCH10_SIDECAR_MISMATCH_REVERIFY_2026-11-09.md`). Live hashes are unchanged since batch 10.

| # | file (reports/) | live | sidecar | amended in place? | substantive? |
|---|---|---|---|---|---|
| 1 | **PAPER_S2_11DM2ETX_EXTENSION_OF_GENERAL_RELATIVITY_INTERPRETATION_2026-11-05.md** | de755741… | e140947e… | **YES, two steps:** e140947e → bd39eb4c → de755741 | **YES** (one math correction plus a meaning-level clarification) |
| 2 | **…_CITATION_PINS_2026-11-05.md** | 47ea689a… | 6f01d93b… | **YES, two steps:** 6f01d93b → 0009e735 → 47ea689a | **YES** (same two changes as #1) |
| 3 | FINDINGS_AGENT_LOOSEN_CAT_B_11D_TERNARY_MERGER_CALL_9ee0f248_2026-11-05.md | aea5bebc… | 9b047680… | UNDETERMINED: two separately worded REVISE drafts | framing and wording only; no status or math change |
| 4 | EIGEN_ACK_PRIMARY_MESH_LOCAL_NL_AGENT_2026-10-26.md | b3e7159e… | 707a6dc0… | YES, append-only | NO (VOID notice only) |
| 5 | NL_WORKING_THREAD_RPPT_MC_NUCLEAR_SCALE_2026-10-26.md | 0b91b476… | 7bdf9fc1… | YES, append-only | NO (two stamps) |

### Details: GR-extension paper and its citation pins (priority)
**Step 1. Ternary-floor correction** (ledger `/workspace/audit-scratch/ternary-floor-correction-20261105/ledger.json`, 20 path changes, with backups).
- The sidecar hash is reproduced exactly by the backup (`…/addendum-workspace-reports/backups/…`: e140947e / 6f01d93b).
- Paper L36 changed the T₃ display from "(2n+1)/3, n ≡ 2 (mod 3)" to "⌊(2n+1)/3⌋".
- **Substantive and correct (PROVED):** for n = 3m + 2, (2n+1)/3 = (6m+5)/3 is not an integer, so the floor is needed for T₃ to be integer-valued. The floored form matches the canonical T₃ (2n+1)//3 used throughout the audit.

**Step 2. Candidate-count clarification** (to de755741 / 47ea689a).
- L71 and L73–75: "45 of 72 … the remaining 27 are not provable in their current form" becomes "45 by primary (first-listed) tag [12] … the remaining 27 are not classed PROVABLE-CANDIDATE by that tally, not declared impossible to prove". A tally note was added (46 before / 47 after ABSORB counting any tag).
- L103: "well-posed provable candidates" becomes "classed as provable candidates by primary tag [12]".
- A new reference [12] was added (PP audit c5755654, §3, sha 4e1cf035…).
- **Substantive in meaning:** it withdraws the claim that the 27 are unprovable. The theorem content is unchanged. This step is recorded by PP 0268f75d ("successor hashes are de755741… and 47ea689a…") and by Agent VERIFY 78faf679. Per PP, there is no verbatim OWNER_WRITE for the 14:11 "Apply" instruction (carried forward as B10-2/B10-4 context).
- **Uniformity:** live de755741 / 47ea689a are identical across all reports/, bridges/ and /workspace/reports mirrors (13 and 9 paths). The sidecars still hold the pre-step-1 hashes, knowingly left historical.

**Scope note (batch 07).** The paper's §9 lists "H²(F) ≅ ℚ·[s_αδ]" as established. That holds only for the truncated F; this is a note, not an edit. The paper itself states that the junction conditions and the valuation-to-geometry map "remain open" (L85, L105). This is consistent with junction OPEN.

### Other three files (confirmed this batch)
- **#4:** truncating the live file at byte 933 (dropping the "## VOID — SUPERSEDED by CANCEL OW 419af1a2…" block) reproduces 707a6dc0. The `/workspace/grok-batches/` copy still holds 707a6dc0.
- **#5:** truncating at byte 2462 (before "## Deepen stamp") reproduces 7bdf9fc1. The appended blocks are FINDINGS pointers only.
- **#3:** the 9b047680 version is held by 10 mirrors; the top-level copy is aea5bebc. Neither is a prefix of the other, so the order is not recoverable (the Nov 6 bulk copy reset mtimes). Both state identical statuses (W₇ CLOSED ABSENT, P2 VACATED, invent HOLD, no CERT), which is consistent with Path C as now confirmed in §0.

## 6. Blockers
- **RESOLVED (§0):** B16-1, B17-1, B18-1 (Q1–Q4). C15-3 was closed in batch 19.
- **Still open:** P5a (OPEN, not a blocker on the Auditor side). N20-1 is a wording note only.
- **B19-3:** re-checked. 4 of 5 are explained (2 substantive and documented, 2 append-only benign); #3 is UNDETERMINED but has no math change. No sidecar action, per B10-1.
- **B20-1:** all 82 s_family_paths files have no sidecar.
- **Carried forward:** B7-1…4, B10-2, B10-4, B11-2, B13-1, B13-2, B13-4, B13-5, B14-1…4, B15-2, B16-2…4, B17-2, B17-3, B18-2, B18-3, B19-1, B19-2, B19-4.

## 7. Remaining
- **Math-bearing uncovered (non-copy):** none after batch 20.
- **Left for custody sampling:**
  - 489 math-marker copies also outside reports/;
  - the non-math remainder of 20,656 entries (see 19b §7).
- **Bridge items still without source:** R_c, the junction, the Layer2 transfer, and the S²-11DM²ET-X objects. κ is an Owner definition (B13-3; Λ₀ = ln(6+√35)/√10 = 0.7835772 per #102 of batch 19).

Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 was re-hashed at write time (unchanged). Nothing was modified.
