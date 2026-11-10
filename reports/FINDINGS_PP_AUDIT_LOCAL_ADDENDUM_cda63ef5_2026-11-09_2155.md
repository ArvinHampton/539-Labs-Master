# FINDINGS (PP audit): Local addendum ADDENDUM_LOCAL_t4407_OA_OB_4A_25PARTS_2026-11-09_2143.md (cda63ef5…). 2026-11-09, ~21:55 CST (America/Chicago)

- **Auditor:** Professor Proof (Soft SF). Audit only. Nothing adopted. No CERT. No Gemini. Nothing sent outside. This file is additive; no earlier file was edited.
- **Tip:** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad9…. It matched before and after; read only.
- **Rule:** OW 3f160803 as amended by 36683379. A citation alone never makes a result PROVED. The base F0 is as disclosed in 5bf1e1dc.
- **PP evidence:** /workspace/audit-scratch/pp_addendum_cda63ef5/. Every file has a .sha256 sidecar.

| File | sha256 (first 8 hex) | Content |
|---|---|---|
| pp_a5_a6_check.py / .log | 7ce2d3fe / 72b2cbdc | independent A5/A6 recomputation; U(2) and U(4) on all of V |
| rerun_tt_v1.py / .log | 6ceaaa73 / bc3d3bcf | verbatim rerun of tt_v1 |
| pp_tt_charsplit.py / .log | 80a3fbb3 / 016ef9a9 | ternary products split by character, n ≤ 600 |
| rerun_ob_calib_subset.py / .log | 82e354e1 / 58d5a397 | rerun of ob_calib_v1: 11a1 at 2⁵ to 2⁷·11, and 15a1 at 480 |
| pp_lvalue_float_sanity.log | 9beadf2a | float sanity of the E11b values, not evidence |

- **Housekeeping disclosure:** at 21:49:25 CST a PP shell slip made `tee` create a stray 154-byte file `pp_a5_a6_check.log` in evidence_local_t4429_ternary_2026-11-09/. It contained only a "file not found" message. PP removed it at once. No Local file was touched, and Local's tt_v1 sidecars still verify.

## 1. Integrity
- cda63ef5859a1283… matches its sidecar.
- e28e0fbd059ad8d6… is unchanged and matches its sidecar.
- In evidence_local_t4407_computations_2026-11-09/, all 35 sidecars verify (25 earlier and 10 new). The 10 new hashes match the addendum's §6 table.
- tt_v1 .py and .log verify against their sidecars.
- tt_v2*, tt_v2b* and cfg_* have no sidecars. They are in progress, and the addendum does not cite them.
- ob_v3_6272_D28_D56.log has no sidecar, as the addendum says; the run is still going (last line: D = 28, joint kernel dimension 88 after p = 3).

## 2. The three wording slips: faithful
| Slip | e28e0fbd text | Addendum | Verdict |
|---|---|---|---|
| Header | "~20:0x CST" | 20:00 CST (the file's mtime is 20:00) | faithful |
| A3 clause | "No nonzero element vanishes at all n ≡ 0 (mod 7) and …" | withdrawn; the truth is the opposite (A5); cause: inverted `n%7!=0` in oa_v3 | faithful (it matches ac9fe667 Fix 4) |
| B5 times | "~19:52 … ~22:25" | 19:51 → ≤ ~22:21 (timeout 9000 s); the process was gone before 21:41 | faithful. ob_v2.log was last written at 20:13 (the D = 8 line), which is consistent with "cause not recorded" |

## 3. PP fixes applied
- **ac9fe667, Fixes 1–16:** all present and faithful.
  - Fix 5 uses χ₂₈·(28/·). This equals PP's χ₂₈(7/·) on odd d.
  - Fix 10: ob_v2.log is now hashed.
- **69d33456, Fixes 1–5:** all present.
- **5bf1e1dc, Fixes 1–5:** present, with 5bf1e1dc's wording as final:
  - E1 is stated for the instances only.
  - E9 is tagged T-AL-new, N2 T-GZK and 2f T-theta.
  - E11b names the curves. PP float sanity matches the cited balls: L(49a1,1) = 0.9666558528084057… and L′(Ξ,1) = 4.4326227316864161….
- **One wording gap (Fix A below):** §2, 5bf1e1dc Fix 2 calls F0 "the stated untagged base". It must also carry 5bf1e1dc's disclosure: the untagged reading is the same one used for V2–V4, and strict tagging of F0 awaits a separate ruling.

## 4. A5 / A6
**Exact recomputation (pp_a5_a6_check):**
- dim V = 9 and dim K = 4, with pivots n = 1, 2, 3, 5.
- c(n) = 0 on K for all n with 7 | n, n ≤ 1200.
- The U(4) matrix on (G₁, …, G₄) is **exactly** [[0,−2],[1,1]] ⊕ [[−1,2],[−2,2]].
- Both blocks have charpoly x² − x + 2 (sympy and PARI). So the charpoly is (x² − x + 2)². Eigenvalues: (1 ± √−7)/2, each with multiplicity 2.
- U(4)G_j = Σ U4[j,i]G_i holds for all n ≤ 300.

**T-U7 and T-U4, named exactly.** The source is Shimura 1973 (Ann. of Math. 97) Prop. 1.5, in the form given in Ono's *Web of Modularity* Prop. 3.7. For f ∈ M_{k+1/2}(Γ₀(4N), χ):
- (i) f|U(m) ∈ M_{k+1/2}(Γ₀(4Nm), χ·(4m/·)) for every m;
- (ii) if m | N, the level stays 4N.

Here 4N = 196, so N = 49.
- **T-U7** = clause (ii) with m = 7 (7 | 49): U(7) maps S_{3/2}(196, χ₂₈) into S_{3/2}(196, χ₂₈(28/·)) = S_{3/2}(196, trivial). **Correctly cited.**
- **T-U4 as Local states it ("Prop. 1.5, m = 4: U(4) preserves level 196") is mis-cited.** Clause (ii) needs 4 | N = 49, which is false.
- **Correct restatement, T-U4′:** U(4) = U(2)∘U(2), applied in two steps.
  - Step 1, clause (i) with m = 2: U(2) maps level 196 to S_{3/2}(392, χ₂₈χ₈).
  - Step 2, clause (ii) at 4N′ = 392, where m = 2 divides N′ = 98: the level stays 392, and the character becomes χ₂₈χ₈² = χ₂₈.
  - So **U(4)V ⊂ S_{3/2}(Γ₀(392), χ₂₈)**.
  - The weight-3/2 Sturm bound at level 392 is (3/2)·672/12 = **84**, not 42. It is applied through V5 to squares.
  - Local's n ≤ 100 identity still exceeds 84, so the A6-a conclusion survives under T-U4′. PP also checked U(4)V ⊂ V for n ≤ 300 (rank 9 → 9), so U(4)V = V-valued, CONDITIONAL on T-U4′.

**Grades:**

| Row | Local | PP ruling |
|---|---|---|
| A5: c(n) = 0 for 7 \| n on K | C on T-U7 | **CONDITIONAL on T-U7: confirmed.** Use the short route: U₇F ∈ S_{3/2}(196, trivial), Sturm bound 42, and c(7n) = 0 for n ≤ 171. That needs only T-U7. The level-1372 route also needs the half-integral V₇ lemma (Shimura Prop. 1.3: V_d maps 4N to 4Nd with character ·(4d/·)), which is a citation, not "elementary" as written |
| A6-a: U(4) block form and charpoly on K | C on T-U4 | **CONDITIONAL on T-U4′** (retagged). The matrix and charpoly are exact. Their meaning as an operator rests on T-U4′, with Sturm 84 < 100 |
| A6-b: K ∩ S⁺ = span{G₁, G₄} is not U(4)-stable | PROVED | **PROVED: confirmed.** rank[Plc; Plc·U4] = 4. The truncated U(4)-images have nonzero G₂ and G₃ coordinates, which proves non-membership with no citation |
| A6-c: U(7) = U(49) = 0 on K | C on T-U7 | **CONDITIONAL on T-U7. It duplicates A5** (U(7)F = 0 is A5 restated, and U(49) = 0 follows from the coefficients). Folding it into A5/A6 and not counting it, as Local did, is correct |
| A6-d: "U(2) does not apply" | stated, ungraded | **True, and now PROVED without citation.** rank[V \| U(2)V] = 18 = 9 + 9 on n ≤ 600, so U(2)V ∩ V = 0 (and rank[K \| U(2)K] = 8). No nonzero U(2)F lies in V. Local's reason ("8 ∤ 196") is only the failure of clause (ii)'s hypothesis (2 ∤ 49), and by itself is not a proof. Restate it with pp_a5_a6_check |

**Can PP discharge T-U7 and T-U4′ as it did T-mod? Yes, plausibly (about 2 h); not done in this item.** The ingredients:
- (1) The coset identity [[1,j],[0,m]]γ = γ′[[1,j′],[0,m]], with γ′ ∈ Γ₀(4N) when m | N. This is an exact matrix identity, like V7.
- (2) Shimura's explicit multiplier j(γ,τ) = ε_d⁻¹(c/d)(cτ+d)^{1/2}, and the Kronecker-symbol identities (mc/d′) = (m/d′)(c/d′) and periodicity in d. These are finite exact checks plus quadratic reciprocity.
- (3) The weight-½ theta transformation formula θ(γτ) = j(γ,τ)θ(τ) on Γ₀(4). This is the real input. It can be proved by the same Poisson-summation and generator certificate used for θ_ψ (rank-1 lattice; generators T, −I, [[1,0],[4,1]] of Γ₀(4); cocycle check).
- After that, T-U7 and T-U4′ would rest only on F0.

## 5. B5 and the ob_v2 partial results
- **Honestly scoped:** D = 1 and D = 8 at 6272 = 2⁷·49 have joint kernel 0 (dimension 390 each, p = 3, 5, 11). The log lines verify, sha 29036a3c….
  - They are reported as scoped sub-results inside B5, which stays **PENDING**, and they are not counted as rows.
- **D = 28 and D = 56: no claim rests on them.** O-b stays OPEN. The fallback-order remark (ternary theta, then 12544) is strategy, not a claim.
- ob_v3 is running; its log will be hashed in a later file, as stated.

## 6. O-b calibration
- **CAL-1 and CAL-2:** PP reran 11a1 at 352, 704 and 1408, and 15a1 at 480. The output is identical to the log: all 11a1 kernels are 0, and the 15a1@480 kernels have dimension 4 for every D.
- The 2816, 960 and 1920 lines were checked against the log but not rerun.
- **PROVED (scoped), confirmed.**
- **Scope fix (Fix D):** "all PARI-admissible even quadratic D" overstates the run. ob_calib_v1 tried only D ∈ {1, 8, ±4, ±8, ±N, ±4N, ±8N}. The nonzero spaces were D ∈ {1, 8, 44, 88} (11a1) and {1, 8, 60, 120} (15a1). State those sets.
- The kernel ≠ 0 conclusion uses three primes only, as Local states.
- "OPEN (interpretation)" is a remark, not a counted row.
  - ε(49a1⊗χ₋₄) = −1 is PROVED by the V9 law in 5bf1e1dc (conductor 4 coprime to 49).
  - ε(15a1⊗χ₋₄) = +1 is an exact ellrootno value; modularity of 15a1 is not PP-verified, so its L-function sign is not used.

## 7. Ternary-theta evidence (t4429 tt_v1)
- **Rerun identical:** 18 products θ_{L₁}(aτ)θ(bτ), with a ∈ {1, 2, 4, 7, 14, 28} and b ∈ {1, 7, 49}. Rank 17, rank of K 4, rank of the union 19, so the "intersection" has dimension 2 on n ≤ 300.
- **PP character split** (n ≤ 600):
  - b ∈ {1, 49} (character χ₂₈, the character of V): rank 11; dim(span ∩ K) ≤ 2 and dim(span ∩ V) ≤ 5.
  - b = 7 (a different character): contributes 0.
- **Grades:**
  - **Upper bound dim(span ∩ K) ≤ 2: PROVED** (exact). Truncation is injective on K, and the intersection of truncated spans contains the truncation of the true intersection.
  - **Lower bound "the products span 2 of the 4 dimensions of K": as filed this is evidence only.** No Sturm argument is given. At most it is **CONDITIONAL on T-theta-ternary**: each θ_{L₁}(aτ)θ(bτ), with b ∈ {1, 49}, is the theta series of the positive ternary form a·N + b·z², and lies in M_{3/2}(Γ₀(196), χ₂₈) with the θ³ multiplier.
  - T-theta-ternary is not verified. It is equivalent to T-theta for θ_{L₁} ∈ M₁(Γ₀(7), χ₋₇) together with Shimura Prop. 1.3 for θ(bτ).
- **What a Sturm argument would need:**
  - (i) Membership of the b ∈ {1, 49} products in M_{3/2}(Γ₀(196), χ₂₈). The b = 7 products must be excluded, since they lie in another character.
  - (ii) Explicit λ with G = Σλ·product for two independent G ∈ K, verified to n > 42 (the weight-3/2 bound at 196, through V5 on (G − Σλ·product)², weight 3, bound 84). The data to n ≤ 600 already suffice once (i) holds.
  - (iii) Optionally, discharging T-theta for θ_{L₁} by the 5bf1e1dc Weil-representation certificate (rank 2, |D| = 7, weight 1). This is cheap.
- Not counted in the rollup until Local files it as a row.

## 8. Rollup ruling
Base: PP 5bf1e1dc, 61 rows, 38/14/7/1/1. Its 7 OPEN rows were O-b, O-c, H₊U, Λ₀, A5, A6 and P11.

| Change | Effect |
|---|---|
| A5: OPEN → CONDITIONAL (T-U7) | O −1, C +1 |
| A6 (= A6-a, with A6-c folded in): OPEN → CONDITIONAL (T-U4′, retagged) | O −1, C +1 |
| A6-b, new row | P +1 |
| CAL-1 and CAL-2, new rows (scoped) | P +2 |
| A6-d ("U(2) is not an endomorphism of V"), new row; PROVED by PP's computation | P +1 |

- Local's 41/16/5/1/1 (64 rows) is arithmetically right for its own row set. Its 3 new rows are A6-b, CAL-1 and CAL-2. The rows that moved from OPEN are A5 and A6.
- PP adds A6-d.
- **PP ruled rollup: PROVED 42 · CONDITIONAL 16 · OPEN 5 · REFUTED 1 · PENDING 1, plus V₈₄ (65 rows).**
  - OPEN: O-b, O-c, H₊U, Λ₀, P11.
  - PENDING: B5.
- tt_v1 is not counted.

## 9. Fixes for Local (additive)
- **A.** In §2 (5bf1e1dc Fix 2), add the F0 disclosure: same base as V2–V4; strict tagging awaits a separate ruling.
- **B.** Retag A6-a from T-U4 to **T-U4′**: Shimura Prop. 1.5 clause (i) for U(2) (level 196 → 392, character χ₂₈χ₈), then clause (ii) at level 392 (2 | 98). Replace "Sturm bound 42 of V" with "Sturm bound 84 at level 392 (n ≤ 100 suffices)". Withdraw "Prop. 1.5, m = 4" at level 196 (4 ∤ 49).
- **C.** For A5, prefer the short route (U₇F at level 196, bound 42), which needs only T-U7. If the level-1372 route is kept, tag the V₇ lemma (Shimura Prop. 1.3) as a citation, not "elementary".
- **D.** CAL scope: list the D actually tried and found nonzero; drop "all PARI-admissible".
- **E.** Restate A6-d as "U(2)V ∩ V = 0 (rank 18 = 9 + 9, n ≤ 600), PROVED". Cite pp_a5_a6_check (7ce2d3fe/72b2cbdc). Replace the "8 ∤ 196" reason, which only shows the hypothesis fails.
- **F.** A6-c: mark it as a duplicate of A5. It is not a separate counted row.
- **G.** Ternary (tt_v1): file it as "dim(span ∩ K) ≤ 2 PROVED; = 2 CONDITIONAL on T-theta-ternary (Sturm step still to be written: b ∈ {1, 49} only, explicit λ, n > 42)". Add sidecars for tt_v2*, tt_v2b* and cfg_* before citing them.
- **H.** Use the PP ruled rollup in §8: 42/16/5/1/1 + V₈₄ (65 rows).

PP audit only. Nothing adopted. No CERT. Tip 7cddb188 untouched. No external sends. No Gemini.
