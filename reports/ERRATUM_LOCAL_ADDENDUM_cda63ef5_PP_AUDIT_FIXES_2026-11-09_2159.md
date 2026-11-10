# ERRATUM (Local-derived) to ADDENDUM_LOCAL_t4407_OA_OB_4A_25PARTS_2026-11-09_2143.md (cda63ef5…), applying PP audit 7c26a452. 2026-11-09, written 21:59 CST (America/Chicago)

- **Scope.** Additive. cda63ef5 and e28e0fbd are NOT edited; this file corrects them by reference. No CERT. No Gemini. Nothing sent outside. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad9… unchanged (checked before and after writing).
- **Source audit:** FINDINGS_PP_AUDIT_LOCAL_ADDENDUM_cda63ef5_2026-11-09_2155.md, sha256 7c26a4520da9a657e2cffebdf28e6f557c65867ac10387c6b6cab85259076dce (matches its sidecar).
- **Rule:** OW 3f160803 as amended by 36683379 (a citation alone never makes a claim PROVED). Convention unchanged: ε = root number, w_N = Fricke eigenvalue, ε = −w_N at weight 2. "Resonant algebra" (RTA historical alias only).
- PP is attempting to discharge T-U7 and T-U4′ itself; Local does not duplicate that work.

## Fixes A–H (PP 7c26a452 §9), applied by reference

**A. §2 of cda63ef5 (5bf1e1dc Fix 2), F0 disclosure added.** Where cda63ef5 calls F0 "the stated untagged base", read: *F0 is the stated untagged base; this untagged reading is the same base used for V2–V4, and strict tagging of F0 awaits a separate ruling (5bf1e1dc disclosure).*

**B. A6-a retagged T-U4 → T-U4′.** Withdraw "Shimura 1973 Prop. 1.5, m = 4: U(4) preserves S_{3/2}(Γ₀(196), χ₂₈)" (mis-cited: clause (ii) needs 4 | N = 49, false). Replace with:
- **T-U4′:** U(4) = U(2)∘U(2). Prop. 1.5 clause (i), m = 2: level 196 → 392, character χ₂₈χ₈. Then clause (ii) at 4N′ = 392 (2 | N′ = 98): level stays 392, character χ₂₈χ₈² = χ₂₈. Hence U(4)V ⊆ S_{3/2}(Γ₀(392), χ₂₈).
- Replace "Sturm bound 42 of V" by "Sturm bound 84 at level 392 (weight 3/2, through V5 to squares); the identity checked to n ≤ 100 suffices".
- A6-a: U(4) on (G₁..G₄) = [[0,−2],[1,1]] ⊕ [[−1,2],[−2,2]], charpoly (x²−x+2)² — exact; operator meaning **CONDITIONAL on T-U4′**. (PP pp_a5_a6_check 7ce2d3fe/72b2cbdc confirms the matrix exactly and U(4)V ⊂ V on n ≤ 300.)

**C. A5: short route adopted.** A5 rests only on T-U7: U₇F ∈ S_{3/2}(Γ₀(196), χ₂₈·(28/·)) = S_{3/2}(196, trivial) for F ∈ K; weight-3/2 Sturm bound at 196 is 42 (84 via V5 on squares); c(7n) = 0 exactly for 7n ≤ 1200 (n ≤ 171) from oa_v8_a5_a6 (1ef57388/45713d8a) and oa_v9_u7_check (5e0f097d/87deb235). **A5: CONDITIONAL on T-U7.** The level-1372 route in cda63ef5 §1 is withdrawn as the stated route; the sentence "V₇ … raises the level by 7, which is elementary" is withdrawn: the half-integral V₇ lemma is Shimura 1973 Prop. 1.3 (V_d: 4N → 4Nd, character ·(4d/·)), a citation, not elementary.

**D. CAL-1/CAL-2 scope.** Replace "all PARI-admissible even quadratic D" by the sets actually tried in ob_calib_v1 (22703a32/07588005): D ∈ {1, 8, ±4, ±8, ±N, ±4N, ±8N} with N the conductor (11 or 15). Spaces that were nonzero: D ∈ {1, 8, 44, 88} (11a1) and D ∈ {1, 8, 60, 120} (15a1). Results unchanged: 11a1⊗χ₋₄ joint kernels 0 at 352, 704, 1408, 2816; 15a1⊗χ₋₄ at 480 kernel dimension 4 for each tried D with nonzero space (three primes only). PROVED (scoped), as PP confirmed.

**E. A6-d restated.** Replace "U(2) does not apply … because 8 ∤ 196" by: **U(2)V ∩ V = 0, PROVED** (rank[V | U(2)V] = 18 = 9 + 9 on n ≤ 600; also rank[K | U(2)K] = 8), per PP pp_a5_a6_check (7ce2d3fe/72b2cbdc). The "8 ∤ 196" reasoning is withdrawn (it only shows clause (ii)'s hypothesis 2 | 49 fails).

**F. A6-c** (U(7) = U(49) = 0 on K, CONDITIONAL on T-U7) is marked a **duplicate of A5**; not a separate counted row.

**G. Ternary theta (t4429 tt_v1).** Filed as: **dim(span ∩ K) ≤ 2 PROVED** (exact; truncation injective on K). **= 2 CONDITIONAL on T-theta-ternary.** Only b ∈ {1, 49} carry V's character χ₂₈ (PP character split; b = 7 contributes 0).
- New Local data toward the Sturm step (PP's items (ii)), supplied for PP ruling, not self-graded upward:
  - tt_v2b run1 (formal T(p²) eigen-solve, D = 7 ≙ χ₂₈ mod squares) isolates exactly two eigen-combinations, both using b ∈ {1, 49} only: h₁ = θ_{L₁}(7τ)θ(τ) − θ_{L₁}(τ)θ(49τ), h₂ = θ_{L₁}(14τ)θ(τ) − θ_{L₁}(2τ)θ(49τ) (L₁: x²+xy+2y²).
  - tt_v3b (exact over ℚ, n ≤ 600 > 84): **h₁ = −4·K₃ and h₂ = −6·K₃ + 2·K₄** (coordinates on the matker columns K₁..K₄), identity exact for all n ≤ 600. So with (i) T-theta-ternary placing h₁, h₂ in M_{3/2}(Γ₀(196), χ₂₈), Sturm (42; 84 via V5 on squares) gives h₁, h₂ ∈ K, independent ⇒ dim = 2. The script's last (rank) line crashed on a GP type error after these results; rank 2 is read off the coordinates. Kept as filed.
  - tt_v4 run1 (all positive ternary forms of discriminant 343): the same 2-dim kernel arises as θ_{Q₁} − θ_{Q₂}, Q₁ = x²+2y²+49z²−xy, Q₂ = x²+7y²+14z²−7yz — a genuine genus-difference (Gross/Pacetti–Tornaría form).
- Sidecars now exist for tt_v2*, tt_v2b*, tt_v2c*, cfg_*, tt_v3*, tt_v3b*, tt_v4* (table below), so they may be cited.

**H. Rollup: PP-ruled 42 PROVED · 16 CONDITIONAL · 5 OPEN · 1 REFUTED · 1 PENDING, plus V₈₄ (65 rows).** OPEN: O-b, O-c, H₊U, Λ₀, P11. PENDING: B5. Local's 41/16/5/1/1 proposal is superseded. tt rows are not counted.

## Disclosed PP event
PP disclosed (7c26a452, housekeeping) that at 21:49:25 CST a PP shell slip made `tee` create a stray 154-byte `pp_a5_a6_check.log` in evidence_local_t4429_ternary_2026-11-09/, containing only a "file not found" message, which PP removed at once. Local records it as a disclosed PP event. Local re-verified after the event: every sidecar in evidence_local_t4429_ternary_2026-11-09/ passes `sha256sum -c` (list below; tt_v1 pair created 21:44, before the event, still OK), and no file named pp_a5_a6_check.log is present there now.

## Status of streams (no claims)
- **B5:** PENDING. ob_v3_6272_D28_D56 running (started 21:41 CST, 6e9 stack, timeout 10800 s); at writing: D = 28, dim 388, joint kernel 88 after p = 3, 32 after p = 5. B5 will be filed as its own FINDINGS file when ob_v3 closes.
- **Fallback (i), ternary theta for g = 49a1⊗χ₋₄ (conductor 784):** evidence only, no claim.
  - tt_v2b/v2c: products of χ-twisted binary CM thetas × unary thetas (600 generators, rank 549): kernel at N = 12000 (13–15) was spurious — it vanishes at N = 30000 for all D ∈ {±1, ±2, ±7, ±14}, while the f-control keeps stable kernels (15 at D = 7, 13 at D = 14).
  - tt_v4 run2 (running): all ternary forms of discriminant 2^a·7^b ≤ 10976, D ∈ {±1,±2,±5,±7,±10,±14,±35,±70}. At writing, d ≤ 784: g null for every d and D; f-control recovered at d = 343 (D = 7, dim 2) and also at d = 686 with **D = 14** (dim 2, formal candidate only).
- **Fallback (ii), level 12544:** not started; waits for ob_v3 to close (memory).

## Usage checkpoints
89.6% of the weekly limit at 21:58 CST (resets Tue Nov 10, 09:49 CST). Earlier: 87.8% (21:45), 84.1% (21:04), 74.4% (20:03).

## Evidence: evidence_local_t4429_ternary_2026-11-09/ (sidecar sha256, full)

| File | sha256 |
|---|---|
| cfg_v2_f196.json | 02fc390a5573e8a79bbce1f54e2a1069b3404d9c86bc265bc3d1aacf1134a4cb |
| cfg_v2_g_run2.json | 4591e58f4519ee79034a17c471a482e6a00cc44cf0ea988ba878a4222422c88f |
| cfg_v2c_g_run3.json | 993500108e020d5088a4d2216bc3d98ba9b9f198b8a7ab78b8cc70c6b5f7f81f |
| tt_v1_level196_test.log | 812c702b07895aa366f61721c3f90544a8729f1b06037ba9632438eef27ffa90 |
| tt_v1_level196_test.py | 6ceaaa738ceb3665c46e4a8d91de734f78c049810c169fadeb695c7ca0821bfa |
| tt_v2_run1_f196_validation.log | 9cb3847b5991ca71ab319815da1135ce1e5063d06e4929201ee9a609445dd859 |
| tt_v2_twisted_products_eigensolve.py | 98c10b0105bcdd301d531263d107407050335a6f63d3ecd44e8cbfd9b5f3a707 |
| tt_v2b_run1_f196_validation.log | 67746888c228ecb02ac62b7891dc396557b411c3c7ad7dc688b3b9ac7ecf7fd4 |
| tt_v2b_run2_g_unarycoset1.log | 00c7f961d0767123d81d549c727c473e8f68c7dbd81b109649f35caa8b58b3bb |
| tt_v2b_twisted_products_eigensolve.py | 5fd0929de022f7da4d0f511d8a325534a54be2f7c4ae63e567573be49982e262 |
| tt_v2c_run3_g_N30000.log | 0accc3832406a0e5aa1267331303a729bfb51d9ed9f04eb18bb4fe1af96f9c2b |
| tt_v2c_run4_f_samegens_N30000.log | 571e6c3915e10ffd2d36514b715b55fc39c62789627d206b385b719056c65c06 |
| tt_v2c_twisted_products_eigensolve.py | 992cb12fe7af5bf454e546dbd6668e0ae48ecc1518ac2a80fa1ae3b2bca01b36 |
| tt_v3_sturm196_explicit.log | ca1ee83da248867109856bb2f2e31c8687c324d1a92a5b870c345f628969e35b |
| tt_v3_sturm196_explicit.py | e3fb3fc88c50354fc6d2459630b9c8a1ae6c022ef62d2ed242182b83c8fb8ac5 |
| tt_v3b_sturm196_explicit.log | ea512df7dee3c25759fcceb7227ce4b754de1af9b1de9308175cb26f7c62d8b3 |
| tt_v3b_sturm196_explicit.py | 21fd18fe3c1bd171a7bfd1b68eb5d96ecb78a934993c8a93dba1d51457b878d9 |
| tt_v4_run1_d343_1372_validation.log | 643627c672b6c970bd990f8c3c43bd3991f5d096fd0bd9e596515755cc80dc82 |
| tt_v4_ternary_genus_eigensolve.py | d30db9b46167113678868e5ff5afb3bb3dcedbeb8d582f9c8147c49f50a92da2 |

sha256sum -c result in that folder at writing: 19 OK, 0 failed. tt_v4_run2_g_scan_2a7b_le11000.log is still being written and has no sidecar yet.

Local-derived. Erratum only; nothing adopted by PP is implied.
