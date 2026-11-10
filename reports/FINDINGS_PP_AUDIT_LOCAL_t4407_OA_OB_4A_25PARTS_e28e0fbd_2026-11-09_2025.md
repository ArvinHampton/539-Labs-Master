# FINDINGS (PP audit): Local t4407 O-a / O-b / 4a / 2-5-parts file e28e0fbd. 2026-11-09, ~20:25 CST (America/Chicago)

- **Auditor:** Professor Proof (Soft SF). Audit only. Nothing adopted. No CERT. No Gemini. Nothing sent outside. Additive file.
- **Tip** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. It matched before and after this audit and was only read.
- **Naming (OW 81b74a31):** "resonant algebra" for the object formerly called RTA. This is a name change only; no grade depends on it.
- **Citation rule (OW 3f160803 as amended by 36683379, as briefed):** a citation never makes a result PROVED. If a step uses a cited theorem that PP has not verified, the result is CONDITIONAL on that theorem, and the theorem is named.
- **Labels:** PROVED / CONDITIONAL / OPEN / REFUTED / PENDING.
- **Read first:** PP edcd9551 (1949) and PP bc12df1a (1955).
- **Authority:** OWNER_WRITE_MAINCHAT_t4407_…_1843.md has sha b0b9ae7f…. It matches its sidecar and is verified. Its Local scope lists "O-a, O-b, 4a interval hardening, 2/5-parts", so Local's authority line is correct.
- **PP evidence:** /workspace/audit-scratch/pp_t4407_e28e0fbd/. Every file has a .sha256 sidecar.
  - pp_c1_formal.py / .log: df60d181… / 421f050e…
  - pp_gamma20_H.py / .log: 5187e2c0… / 4b7a7c35…
  - pp_gamma0_49_onto.log: 8b0a17aa…
  - pp_misc_pari.log: ca4386d8…
  - pp_ob_v1_partial_1568.log: d78a2967…
  - pp_ob_v1_partial_b.log: 6daab0ec…
  - rerun_*.log, for example rerun_a4_exact_modl_v1.log: 9166bc53…

## 0. Integrity
| Object | sha256 (recomputed) | Sidecar | Status |
|---|---|---|---|
| FINDINGS_LOCAL_t4407_OA_OB_4A_25PARTS_2026-11-09_2000.md | e28e0fbd059ad8d6852628fef22647ecfb955f00f95eba67a9ea3a757c3a82dc | same | **MATCH** (18397 bytes) |
| evidence_local_t4407_computations_2026-11-09/: 25 scripts and logs | each recomputed | each sidecar | **25/25 OK**. oa_v1.log is empty (e3b0c442…), as Local states |
| ob_v2.log | 285d68cc… at 20:02 (still growing) | none | expected: the job is still running (PID 797705, started 19:51 CST, `timeout 9000`). PP did not touch it |
| PP pp_4a_exact.py / .log (cited by 4a) | 90ed5512… / 789473d6… | same | MATCH |
| PP pp_3b4.py / .log (cited by A1, A2 and A4) | 4b399987… / 2d039cfa… | same | MATCH |
| PP edcd9551 / bc12df1a | edcd955190294393… / bc12df1ae2b074dd… | same | untouched |

**Reruns.** Each run was given a 15-minute limit. Load was 7–15 on 8 cores, with about 1 GB of RAM free.

| Script | Result |
|---|---|
| oa_v7 | **identical** apart from timings |
| p25_local_parts_v1 | **identical** |
| p25_gamma49_exact_v2 | **identical** |
| a4_exact_modl_v1 | **identical**: 59/59 primes, 0/259 generators failing, ALL PASS |
| ob_dims_v1 | **identical** |
| ob_v1 (3014 s in full, so a partial rerun) | rows N=1568 with D=1, 8, 28, 56 and N=3136 with D=1, 8 reproduced: dimensions and joint kernel 0 identical. The rows N=3136 with D=28 and D=56 (1549 s and 464 s in Local's run) were not rerun within the time box |
| oa_v2 / oa_v3 | not rerun. Their logs were read. Every A1/A3 number they give is also produced by oa_v7 or pp_3b4, except the n ≤ 1200 support counts and the mod-4 rank tests in oa_v3 |
| ob_v2 (level 6272) | **left running, not touched → B5 PENDING.** Partial log lines at 20:23 CST: D=1 and D=8 give joint kernel 0. Not graded |

## 1. Key independent PP results (new)
**C1-PP. PROVED (exact, by hand, with a symbolic check).** Shimura's Hecke equivariance S_t(T(p²)F) = T_p(S_tF) holds as a **formal identity of coefficient sequences**. It needs no modularity, for weight 3/2 with character χ = χ₂₈ (χ² trivial off 14), p odd, p ∤ 7t.

*Setup.* Put C(n) := c(tn²) and ψ_t(d) := χ₂₈(d)(−4/d)(t/d), so that A_t = ψ_t * C (Dirichlet convolution). Shimura's T(p²) (λ = 1) gives
B(n) := b(tn²) = C(pn) + ψ_t(p)·[p ∤ n]·C(n) + p·C(n/p).
Here p ∤ t is used twice: it makes the middle factor (−tn²/p) equal (−t/p) or 0, and it makes c(tn²/p²) nonzero only when p | n.

*Proof.* Write n = p^a·m with p ∤ m, and split each divisor as d = p^j·e with e | m. The first two terms of ψ_t * B combine to Σ_{e|m} ψ_t(e)·Σ_{j=0}^{a+1} ψ_t(p)^j·C(p^{a+1−j}m/e), which is (ψ_t * C)(pn). The third term gives p·(ψ_t * C)(n/p). That is T_p at weight 2 with trivial character. ∎

*Machine checks.*
- pp_c1_formal checks the identity with independent symbols c(m): 1560 cases (p ∈ {5,…,23}, t ∈ {1,2,3,5,6,10,13} with p ∤ t, n ≤ 40), 0 failures.
- PP also checked that PARI `mfheckemat(m,p²)` on V equals Shimura's T(p²) formula with the χ₂₈ middle term, on all 9 basis forms (p = 5 for n ≤ 60, p = 11 for n ≤ 10). So the normalisation is the same.

**So C1 is no longer a citation dependency.**

**What A2 still cites.** Two theorems remain unverified by PP:
- **(C2)** S_t maps S_{3/2}(Γ₀(196), χ₂₈) into M₂(Γ₀(98)) for every F, including F that are not eigenforms.
  - **Citation fix:** according to Cipra (Nagoya Math. J. 91, 1983, introduction), Niwa's 1975 theta-kernel argument covers weight > 7/2.
  - The weight-3/2, level-2N case is Cipra 1983. It is also proved by Kojima, by Flicker, and by Gelbart–Piatetski-Shapiro.
  - Local cites "Niwa, Nagoya 56" for k = 1, which is a mis-citation. The hypotheses (weight 3/2, 4N = 196, χ² trivial, t squarefree) hold.
- **(C3)** Shimura 1973, §1: T(p²) preserves S_{3/2}(Γ₀(196), χ₂₈) for p ∤ 196. This is needed so that G = T(p²)F − a_pF lies in V.

**H-PP. PROVED (exact, computer-assisted). This verifies hypothesis H of P10.**
- pp_gamma20_H builds D₂ and D₅ directly from N₂ = [[2,14],[14,28]], with independent code and exact arithmetic in ℚ(ζ₂₀).
  - It checks S⁴ = I and (ST)³ = S² exactly.
  - It checks that ρ_{D₂}(g) = I on all 96 Schreier generators of Γ(4), and ρ_{D₅}(g) = I on all 240 Schreier generators of Γ(5).
  - Therefore ρ_{D₂⊕D₅} = ρ_{D₂} ⊗ ρ_{D₅} is trivial on Γ(4) ∩ Γ(5) = Γ(20).
- pp_gamma0_49_onto: the images of T and (1,0;49,1), both in Γ₀(49), generate all of SL₂(ℤ/20) (order 5760 = 5760). So Γ₀(49) maps onto SL₂(ℤ/20) without any citation.

## 2. Per-claim verdicts
| # | Claim | Local | PP | Reason |
|---|---|---|---|---|
| A1 | dim V = 9; charpolys of T(9), T(25), T(121), T(169); K = ker T(9) has dim 4 and equals the joint f-kernel for p ≤ 37 (Local) and p ≤ 59 (PP) | PROVED | **PROVED** | exact, computer-assisted (oa_v2 log; pp_3b4; oa_v7 rerun dim K = 4). The charpolys match the log; the factors (x+4), (x−12), (x+14) are the unary-theta eigenvalues ±(1+p) of θ_{χ₋₇} ∈ V, which is consistent |
| C1-PP | formal Hecke equivariance of S_t | (cited C1) | **PROVED** | §1, by hand and symbolic |
| A2 | T(p²)F = a_p(f)F for all F ∈ K and all p ∤ 14, so K is exactly the f-isotypic subspace | PROVED* (COND on C1 if declined) | **CONDITIONAL on C2 and C3 only** | Step 1 (Sturm bound 28 for M₂(Γ₀(98)): index 168, 2·168/12 = 28; PP checked to n = 30) is correct. Step 2 (rank Φ_{1,2,3} = 9 for n ≤ 8; rerun identical) is correct. Step 3 is valid, and C1 is now PROVED. Step 1's span statement for all n needs C2, and G ∈ V needs C3. The converse is correct. The isolation remark (a₃ = 0 only for f at level 98) matches the oa_v2 log |
| A3 | plus space has dim 3; K ∩ S⁺ = span{G₁, G₄}, dim 2; no element of K is supported on {0,3}, on {2,3} or on a single class mod 4 | PROVED | **PROVED**, with a wording fix | exact (oa_v7 rerun; oa_v6 vectors = −G₄ and −G₁). The rank-0 statements are exact: finitely many conditions already force 0. **Convention:** PARI's plus space here means c(n) = 0 unless n ≡ 0, 1 (mod 4), because PARI uses χ·(−4/·) = χ₋₇ of conductor 7 dividing 49. State this explicitly (Fix 4). **The clause "no nonzero element vanishes at all n ≡ 0 (mod 7)" is FALSE as worded.** oa_v3 coded the condition as `n%7!=0`, which inverts it. In fact every element of K vanishes at 7 \| n for n ≤ 1200 (A5). This is Local's own slip 2. Withdraw the clause |
| A4 | S₁(K₄ − K₃) = f; the t = 1, 2, 3, 5, 13 coordinates; t = 10 gives 0 | PROVED* | **CONDITIONAL on C2** | the coordinates match oa_v7 (rerun) and PP. The equality is exact for n ≤ 30; for all n it needs C2 (with the Sturm bound) |
| A5 | c(n) = 0 for 7 \| n on K | OPEN | **OPEN** | a finite check only (n ≤ 1200). Suggested path in Fix 5 |
| A6 | U/V at 2 and 7 | OPEN | **OPEN** | not computed |
| B1 | χ₁₄₀, χ₋₂₀, χ₂₈ and χ₋₄ are not squares | PROVED | **PROVED** | ψ_p²(−1) = 1, and the 2-component χ₋₄ is odd (unique prime-power decomposition). PP checked χ₁₄₀ = χ₋₄χ₅χ₋₇ on one period |
| B2 | twisting lemma: F⊗ψ ∈ S_{3/2}(4Nr², χψ²), with eigenvalue ψ(p)²λ_p | PROVED (Lemma 3.6 cited) | **CONDITIONAL on the twist-modularity lemma (Shimura 1973, Lemma 3.6 as cited)** | PP verified the eigenvalue algebra term by term: each of the 3 terms picks up ψ(p)², with χψ² in the middle term and (χψ²)² in the third. Modularity of F⊗ψ at level 4Nr² is cited and not verified |
| B2′ | consequence: Ξ's eigensystem is not a twist of K | (inside B2) | **PROVED** | It does not need modularity. **Make the CM step explicit:** a_p(f) = 0 for p inert in ℚ(√−7), so a matching ψ only needs ψ² = χ₋₂₀ on the split primes, which means ψ² ∈ {χ₋₂₀, χ₋₂₀χ₋₇ = χ₁₄₀}. Both are non-squares by B1 (Fix 7) |
| B3 | reduction: Ξ = (f⊗χ₋₄)⊗χ₅ with χ₅ = ψ₅²; H = G⊗ψ₅ at level 100M; real combination (1, −1, 0) | PROVED | **CONDITIONAL on the same twist-modularity lemma** | The arithmetic is exact: conductor 784 (PP rerun); ψ₅ of order 4 has ψ₅(4) = −1 and ψ₅(2), ψ₅(3) = ±i; 100·784 = 78400. It is a sufficient reduction only, and the converse is not claimed (Fix 8) |
| B4 | null: no G at 4M = 1568 or 3136 | PROVED | **PROVED (scoped)** | exact, computer-assisted. 6 of the 8 rows were rerun identically. This proves only that the joint kernel of T(p²) − χ₋₄(p)a_p(f) for p = 3, 5, 11 is 0 in S_{3/2}(Γ₀(4M), χ_D) for 4M ∈ {1568, 3136} and all 8 quadratic D. That kernel contains every G with the full eigensystem, so absence holds **within these 8+8 cusp spaces only**. It says nothing about other levels (for example 2⁷·49, or levels with odd factors besides 7) or other characters (Fix 9) |
| B5 | level 6272 | OPEN (running) | **PENDING** | ob_v2 is still running. **Start-time slip (Local's slip 3):** ps gives 19:51 CST, and `timeout 9000` gives an end of ~22:21 CST, not 22:25 |
| O-b | Ξ's weight-3/2 form | OPEN | **OPEN** | B6 is a resource estimate, not graded. "Years" should read "about 0.4–2 CPU-years by cubic extrapolation, not a bound" |
| 4a | ρ_{N₂}(γ)e₀ = χ₁₄₀(d)e₀ on Γ₀(140) | PROVED (PP's certificate) | **PROVED** (unchanged, not recounted) | It rests on pp_4a_exact (sha MATCH). Local correctly withdraws the float residual |
| 4a-L | a4_exact_modl_v1 is an independent exact check | PROVED | **PROVED** | Rerun identical. The code is independent: its own BFS and matrices, no PP imports, 59 different primes ℓ ≡ 1 (mod 140) near 2³¹. The argument is valid: one degree-1 prime 𝔩 \| ℓ per prime still gives ℓ \| N(β_i). The bound log₁₀\|N\| ≤ 48·log₁₀(2·140⁵) = 529.52 < 550.58 = log₁₀∏ℓ, and conjugate representations stay unitary |
| P1 | D(N₂) = D₂ ⊕ D₅ ⊕ D₇ with the stated q-values | PROVED | **PROVED** | rerun identical. PP rebuilt it independently in pp_gamma20_H (D₂ q-values {0, 1/2, 1/4, 1/4}; D₅ {0, 2/5, 2/5, 3/5, 3/5}) |
| P2 | signatures 2, 4, 2 (mod 8); ∏G(D_p) = √140 | PROVED | **PROVED** | PP by hand: G(D₂) = 2i, G(D₅) = (2/5)√5 = −√5, G(D₇) = (2/7)·i√7 = i√7, and the product is 2√35 = √140. Signatures 2 and 4 were confirmed exactly in pp_gamma20_H |
| P3 | each ρ_{D_p} is a representation of SL₂(ℤ) | PROVED | **PROVED** | exact relations (rerun); PP checked D₂ and D₅ independently |
| P4 | local e₀-characters χ₋₄, (·/5), χ₋₇ on Γ₀(4), Γ₀(5), Γ₀(7) | PROVED | **PROVED** | exact generator checks (rerun) plus the subgroup argument. These agree with ((−1)^{sig/2}\|D_p\| / d) |
| P5 | ρ_{N₂} = ⊗ρ_{D_p}, giving a third proof of 4a | PROVED | **PROVED** | elementary (orthogonal sums; the constants multiply by P2) together with P4 |
| P6 | ρ_{D_p}(−I)e₀ = χ_p(−1)e₀ with signs (−, +, −) | PROVED | **PROVED** | ρ(−I)e₀ = e(−sig/4)e₀ gives −1, +1, −1 (rerun) |
| P7 | local data table | PROVED | **PROVED** | PP ran independent PARI calls. ε_p(Ξ) at 2, 5, 7 = −1, +1, −1 (the same for the −20 twist); conductor exponents 4, 2, 2; N(Ξ) = 19600; a₂ = 1 and a₅ = 0, so x² − x + 2 and x² + 5 |
| P8 | ε_p(π⊗χ) = χ_p(−1) for unramified π with trivial central character; a = 2a(χ) | PROVED (Tate/Deligne cited) | **PROVED** | PP derived it from the two GL₁ identities ε(χμ) = μ(ϖ)^{a(χ)}ε(χ) for unramified μ, and ε(χ)ε(χ⁻¹) = χ(−1). Both are elementary from the Gauss-sum definition. The values are confirmed exactly by P7. At 7 the twist is unramified, giving (±1)² = 1 |
| P9 | the root-number flip +1 → −1 is wholly 2-adic | PROVED | **PROVED** | ε_v(Ξ)/ε_v(f) is −1 at v = 2 and +1 at v = ∞, 5, 7 (P7). Local ε for GL₂ with trivial central character does not depend on ψ, so the attribution is well defined. The CM step f⊗χ₋₇ = f is from 9e34f2dc 2c (PROVED) |
| P10 | Weil(D₂⊕D₅)\|_{Γ₀(49)} has no stable line | CONDITIONAL (H) | **PROVED** (upgraded) | exact part rerun identical; there are no 1-dimensional subrepresentations, and the T ↦ i^k ⇒ S ↦ i^k character list is correct (12th roots ∩ 20th roots = 4th roots, s = t⁻³). H is PROVED by H-PP, and Γ₀(49) maps onto SL₂(ℤ/20) by pp_gamma0_49_onto |
| H-PP | ρ_{D₂⊕D₅} is trivial on Γ(20); Γ₀(49) maps onto SL₂(ℤ/20) | — | **PROVED** | §1 |
| P11 | whether the sign triples are "one mechanism" | OPEN | **OPEN** | interpretive; undefined |

**Local's own slips (all confirmed):**
1. The header time "~20:0x" should be 20:00 CST (the file's mtime).
2. A3's "n ≡ 0 (mod 7)" clause is false as worded (inverted condition in oa_v3).
3. B5 started at 19:51, not ~19:52, and ends by ~22:21, not 22:25.

## 3. Tally (this file's rows)
**PROVED 18 · CONDITIONAL 4 · OPEN 4 · REFUTED 0 · PENDING 1.** 4a is not recounted.
- **PROVED 18:** A1, C1-PP, A3, B1, B2′, B4, 4a-L, P1–P9, P10, H-PP.
- **CONDITIONAL 4:**
  - A2 (C2 + C3)
  - A4 (C2)
  - B2 (twist lemma)
  - B3 (twist lemma)
- **OPEN 4:** A5, A6, O-b, P11.
- **PENDING 1:** B5.

**Changes from Local's 18/1/4/0:**
- A2, A4, B2 and B3 move from PROVED to CONDITIONAL.
- P10 moves from CONDITIONAL to PROVED.
- B5 moves from OPEN to PENDING. Local counted it under O-b, so O-b stays OPEN.
- New PP rows: C1-PP, B2′ and H-PP.

## 4. N1 status
**N1 is not upgraded. It stays CONDITIONAL, but its condition has narrowed.**
- Before, it was CONDITIONAL on "Shimura Hecke equivariance (cited)".
- It is now CONDITIONAL only on (C2) the weight-3/2 level-2N modularity of S_t for arbitrary F (Cipra 1983 and others), and (C3) T(p²)-stability of S_{3/2}(Γ₀(196), χ₂₈) (Shimura 1973, §1).
- C1 is discharged by C1-PP. Every other step is finite and exact.
- If the Owner accepts standard theorems with checked hypotheses as PROVED, which was edcd9551's practice for 3b-i, 2a and N2, then N1 becomes PROVED. Under the rule as briefed it is CONDITIONAL.

**Consistency note for the Owner/PP (no regrade made here):**
- edcd9551 graded 3b-i PROVED while using C2. Under the strict rule, 3b-i is CONDITIONAL on C2.
- Its REFUTED 3b-ii is sound as a refutation of the evidence: the exact Shimura coefficients contradict PARI's mis-identified values.
- Its conclusion "K is not exactly f-isotypic" is refuted only modulo C2 and C3.
- The Owner should decide whether to apply the strict reading retroactively.

## 5. Updated Local rollup (from 24/3/6/3 + V₈₄)
**Changes to prior rows:**
- O-a goes from OPEN to **CONDITIONAL**: it is answered by A2/N1, modulo C2 and C3.
- "2/5" goes from OPEN to **PROVED**: P10 is its precise statement.
- N1 stays C, narrowed.
- O-b stays OPEN.

**New rows,** excluding duplicates (A2 is N1, O-b is O-b, P10 is 2/5):
- PROVED 17
- CONDITIONAL 3 (A4, B2, B3)
- OPEN 3 (A5, A6, P11)
- PENDING 1 (B5)

**Updated Local rollup: PROVED 42 · CONDITIONAL 7 · OPEN 7 · REFUTED 3 · PENDING 1, plus 1 Owner decision (V₈₄).**
- CONDITIONAL 7: 3d, N1, E11a, O-a, A4, B2, B3.
- OPEN 7: O-b, O-c, H₊U, Λ₀, A5, A6, P11.
- REFUTED 3: 2e, 2f, 3b-ii.

If cited standard theorems with checked hypotheses are accepted, the rollup would be **47 · 2 · 7 · 3 · 1**: N1, O-a, A4, B2 and B3 move to PROVED. That reading is not adopted here.

## 6. Fixes for Local (numbered)
1. **A2:** replace the C1 citation with PP's formal proof (C1-PP, pp_c1_formal df60d181…/421f050e…). Regrade A2 as CONDITIONAL on C2 and C3, and name both in the claim.
2. **C2 citation:** for weight 3/2, the level-2N theorem is Cipra (Nagoya Math. J. 91, 1983; also Kojima, Flicker, Gelbart–Piatetski-Shapiro). By Cipra's account, Niwa (Nagoya 56, 1975) covers weight > 7/2 only. State that C2 is needed for non-eigen F (the theta-kernel form of the lift).
3. **Step 3 of A2:** name C3, Shimura 1973 §1 (T(p²) preserves S_{3/2}(Γ₀(196), χ₂₈)), as the source of G ∈ V.
4. **A3:**
   - Delete the clause "no nonzero element vanishes at all n ≡ 0 (mod 7)". It comes from the inverted `n%7!=0` condition in oa_v3, and the truth is the opposite (A5).
   - State the plus-space convention: PARI's `mfkohnenbasis` means c(n) = 0 unless n ≡ 0, 1 (mod 4), via χ·(−4/·) = χ₋₇.
   - Mark "multiplicity 2 vs Kohnen's squarefree isomorphism" as a remark rather than a theorem.
5. **A5 path (suggested):**
   - Σ_{7|n} c(n)qⁿ = (F|U₇)|V₇.
   - If U₇ maps S_{3/2}(196, χ₂₈) into S_{3/2}(196, χ₂₈(7/·)) (cite and check), the sieved form lies at level 1372 = 2²·7³, which has index 2352.
   - The half-integral Sturm bound there is (3/2)·2352/12 = 294, which is less than 1200. So the existing n ≤ 1200 check would close A5, CONDITIONAL on the U₇ mapping lemma unless that is verified.
6. **A4:** grade it CONDITIONAL on C2 (it is exact for n ≤ 30).
7. **B2:** split it into the lemma (CONDITIONAL on twist modularity, Shimura 1973 Lemma 3.6 as cited) and the consequence (PROVED). Write out the CM step: a_p(f) = 0 at inert p, so ψ² ∈ {χ₋₂₀, χ₁₄₀}, and both are excluded by B1.
8. **B3:** grade it CONDITIONAL on the same twist lemma. State that "reduces to" means sufficiency only.
9. **B4:** state the scope: "joint kernel 0 in S_{3/2}(Γ₀(4M), χ_D) for 4M ∈ {1568, 3136} and all 8 quadratic D". It does not cover other levels or characters. Change "2-power level ≤ 2⁶" in B6 to "4M = 2⁵·49 and 2⁶·49".
10. **B5:** relabel it PENDING. Correct the start to 19:51 CST and the end to ≤ ~22:21 CST. Hash ob_v2.log in the addendum once it closes. The partial lines at 20:23 show D = 1 and D = 8 null.
11. **B6:** change "years of CPU time" to "≈ 0.4–2 CPU-years by cubic extrapolation (estimate, not a bound)".
12. **P8:** replace "cited Tate/Deligne" with the two GL₁ identities (verified by PP) and the P7 cross-check.
13. **P10:** regrade it PROVED, citing H-PP (pp_gamma20_H 5187e2c0…/4b7a7c35…; pp_gamma0_49_onto 8b0a17aa…) for H and for the map onto SL₂(ℤ/20). This also closes the prior "2/5" OPEN row.
14. **Header:** replace "~20:0x" with 20:00 CST.
15. **Rollup:** use §5: **42/7/7/3, 1 PENDING, plus 1 Owner decision.** Record the alternative 47/2/7/3/1 only as the Owner's choice.
16. **Carry-overs from bc12df1a §5:** keep the E11a/E11b split, and name the curve at each certificate citation (Local promised this in its next additive file).

PP audit only. Nothing adopted. No CERT. Tip 7cddb188 untouched (read only). No external sends. No Gemini.
