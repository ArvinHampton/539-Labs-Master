# PP audit: Local t4407 candidate resolutions (O-c, V₈₄, joint carrier, H₊U, LD-O3a/b/c, α (O4), O5)
Author: Professor Proof (PP). Audit only. Additive new file. No CERT. Nothing adopted. Nothing sent. Refutations are made only by proof or counterexample. Recommendations are Local's opinions; PP grades the math only.
Citations are graded under OW 3f160803 as amended by OW 36683379: a citation is allowed, but on its own it never makes a result PROVED. A float-only numeric claim is graded CONDITIONAL.
Tip 7cddb188 MATCH before and after (7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; read only). Lock 96f8d42e §4 untouched (stays purged).
PP scripts are in /workspace/audit-scratch/pp_1909_t4407_audit/, each with a .sha256 sidecar:
- pp_v3_r26_structural.py (1e26fc9d…) and its log (e19d5a5d…)
- pp_j3_weil.py (498db75e…) and its log (92a95d5b…)
- pp_j3_lvalues_arb.py (4747836f…) and its log (db136ad0…)
- pp_misc_exact.py (965b6ca7…) and its log (1922150b…)

## 0. Records and integrity
- R1 [PROVED] The target FINDINGS_LOCAL_OWNER_ITEM_CANDIDATE_RESOLUTIONS_t4407_2026-11-09_1859.md hashes to bfa5da3b0c7b1fd8107a6ad2579c915356f055acaad5f2664d244f004a852be6. This equals both the expected sha and its sidecar.
- R2 [PROVED] All 17 evidence files in evidence_local_owner_candidates_2026-11-09/ pass `sha256sum -c` against their sidecars:
  - 16 scripts and logs: c1, c2, c3, c3b, c3c, c3d, c4 and c4b, each a .py and a .log
  - gen_findings_t4407.py (bba18ccf5d5c2183d252b789eea115a9d5972bb15c12a9edd539872bead4fc41)
  The 16 shas listed in Local's §E table equal the on-disk hashes. gen_findings_t4407.py has a sidecar but is missing from the §E table (custody nit, fix F9).
- R3 [PROVED] OW b0b9ae7f is verified on disk. OWNER_WRITE_MAINCHAT_t4407_PURSUE_ALL_OPEN_ITEMS_FOR_RESOLUTIONS_2026-11-09_1843.md hashes to b0b9ae7fecd635e0735a66a7839bdf0148d65f8eba8adf032c68c0ad3c73494d, which equals its sidecar. PP already verified it in FINDINGS_PP_AUDIT_MR2_KK_TRUNCATION_BOLZA_48_96_WALL_Z2_2026-11-09_1858.md R3.
  - The Owner's verbatim words, as quoted in the record: "Pursue all for resolutions" (main chat t4407u, about 18:42 CST).
  - Scope is Physicist's reading. The Local list in the record is "O-c, V₈₄, joint carrier, H₊U, LD-O3a/b/c, α (O4), O5 free Dirac; plus O-a, O-b, 4a interval hardening, 2/5-parts". The record also says "PP: audits each candidate file", and "Nothing is adopted until the Owner chooses in own words."
  - Local's file covers exactly the first group. O-a, O-b, 4a and 2/5-parts are declared out of scope in its §R and are not graded here.
- R4 [PROVED] Local's own tag count reproduces from the text as P 42 / C 4 / O 7 / R 7 (per item: I1 4/2/3/0, I2 4/1/0/1, I3 10/0/2/0, I4 3/0/1/2, I5 6/1/0/0, I6 5/0/0/0, I7 2/0/0/1, I8 5/0/1/1, I9 3/0/0/2).

## 1. Priority checks requested by Local
### (a) V-3 and tip R26
- R26 as filed (grok-batches/MR1-AUTHOR-R26-W7-MATRIX-COMPUTE_2026-10-25.md, sidecar OK; script MR1-R26-w7_intertwiner_diag.py) is **float-only**. V₄₂ is a numeric SVD basis, and the intertwiner space is "dim 1 at SVD tol 1e-8, rank 9". Under the float rule, R26 alone would support V-3 only as CONDITIONAL.
- **PP independent exact proof (pp_v3_r26_structural):**
  1. In SL₂(ℤ), W₇TW₇⁻¹ = (1,0;−49,1) = S T⁴⁹ S⁻¹.
  2. So if an invertible M intertwined ρ and ρ^W := ρ∘Ad(W₇) on V₄₂, then ρ(T)|V would be conjugate in GL(V₄₂) to ρ(S)ρ(T)⁴⁹ρ(S)⁻¹, hence to ρ(T)⁴⁹|V. This uses that V₄₂ is S,T-stable, because V₄₂ is the span of the values of the S,T-closed family u.
  3. ρ(T) is monomial with root-of-unity phases of order dividing 9800 (checked exactly), so it is diagonalizable. Conjugacy would therefore force equal eigenvalue multisets.
  4. ζ ↦ ζ⁴⁹ strictly lowers the largest 7-adic valuation of the eigenvalue orders whenever that valuation is ≥ 1.
  5. PP exhibits exact nonzero vectors in V₄₂ (Fourier-coefficient columns, which span V₄₂ by its v42.py definition) with T c = e(q)c for q = −1/140, −1/35, −9/140 and 1/14. Each has an eigenvalue of order divisible by 7.
     - Nonvanishing is certified mod p = 1029001 ≡ 1 (mod 9800). A nonzero image implies nonzero in characteristic 0.
     - The eigen-relation is verified exactly in ℤ[x]/Φ₉₈₀₀(x) (python-flint), with 0 violating rows.
     - The column is stable when the enumeration box is enlarged (Bx = 20 and 30).
  6. Hence there is no invertible intertwiner.
  The premises are the tip's own definition of ρ (R19: ρ on Γ₀(49) is the restriction of the S,T action, ρ(S) = S_lab⁻¹ and ρ(T) = T_lab) and V₄₂ = span of the columns. These are definitions, not unproved claims.
- **Verdict:** V-3 REFUTED is confirmed. PP's exact proof makes the refutation independent of cited R26. The proof also re-proves R26's qualitative content (ρ^W ≇ ρ on V₄₂) exactly; it does not re-prove R26's "dim 1, rank 9" numerics, which stay float-grade.

### (b) J-3 and the conductor (pp_j3_weil, pp_j3_lvalues_arb)
- [PROVED] E = 49a1 with j = −3375 (CM by ℚ(√−7)). Ξ = E^{χ₁₄₀}, with c₄ ratio 140² and c₆ ratio 140³, so u² = 140 = (2√35)² ∈ K^{×2}. So E ≅ Ξ over K = ℚ(√35), and d_K = 140.
- [PROVED] cond(Ξ) = 19600 = 2⁴·5²·7² (exact, ellglobalred).
- [PROVED] The conductor ideal of E/K is 𝔭₇², where 𝔭₇² = (7), so its norm is 49. Milne's formula then gives cond(Res_{K/ℚ}E_K) = d_K^{2·dim E}·N(f_{E_K}) = 140²·49 = **960400**. This equals cond(E)·cond(Ξ) = 49·19600, as it must, since L(Res, s) = L(E_K, s) = L(E, s)L(Ξ, s).
- [PROVED] Res_{K/ℚ}E_K ~ E × E^{χ_K} (standard; Milne 1972), with χ_K = χ₁₄₀. Local's check of the first 400 primes is exact (integer ellap) and supporting only.
- **Scrutiny of "level 19600":** this is correct as the **minimal modular level**: the least N with J a quotient of J₀(N) up to isogeny is lcm(49, 19600) = 19600. It is **not** the conductor of J. Local states both correctly in §I3 (cond(J) = 960400). Local's message to PP ("~ 49a1×Ξ at level 19600") conflates the two, which is a wording fix (F2).
- [PROVED] ε(J) = (+1)(−1) = −1, with exact root numbers.
- [PROVED] The analytic rank of J is 1. This is **PP-certified by ball arithmetic** (arb, 200 bits, explicit tails using |a_n| ≤ 2n and E₁(x) ≤ e^{−x}/x):
  - L(49a1, 1) ∈ [0.96665585280840577337 ± 3.5e−21] ≠ 0
  - L′(Ξ, 1) ∈ [4.4326227316864161623 ± 2.2e−20] ≠ 0
  As filed, Local's claim rested on cited floats (c2e9b6fe) and would be CONDITIONAL. The PP certificate closes it. Side fact: PARI ellrank gives Mordell–Weil rank bounds [1, 1] for Ξ.
- **Verdict:** every J-3 PROVED tag stands. The fixes are wording (F2) and certificate citation (F3).

### (c) The α-3 exact example (pp_misc_exact)
- [PROVED] t = ½(R₃ + R₃₇ + R₄₇ − R₅₃) satisfies tt* = 1 in ℚ[(ℤ/140)^×]. The identity coefficient is 4·¼ = 1, and every other coefficient cancels.
- [PROVED] TᵀBT = B exactly, by Fraction arithmetic on the full 48×48 matrices. T⁻¹ = T* exactly.
- [PROVED] PP's independent enumeration also finds exactly 48 four-term ±½ solutions on 6 supports. All 11 K90 primes have χ₁₄₀(p) = −1.
- [PROVED] PP re-proves the lemma algebraically: B(R_p e_g, R_q e_h) = [h ≡ −pq⁻¹g], so B(Tx, Ty) = B(R_{tt*}x, y), and B is nondegenerate. Local's 1.8e−15 residual is illustration only; the lemma is proved without it.

## 2. Per-item verdict table (Local tag → PP grade)
| Item / claim | Local | PP | Note |
|---|---|---|---|
| Oc-1 dim W₄=4, c(35)=0 on W₄ (cited 9e34f2dc) | P | PROVED (cited, previously audited) | |
| Oc-1 squarefree n with coredisc 140 is only 35 | P | PROVED | 4n=140 ⇒ n=35; PP scan ≤10⁴ |
| Oc-1 c(35)² ∝ L(Ξ,1)=0 (Waldspurger) | C | CONDITIONAL | ε(Ξ)=−1 exact |
| Oc-1 W₄ not f-isotypic | O | OPEN | |
| Oc-2 nonzero for suitable ψ | C | CONDITIONAL | |
| Oc-2 not reachable by twisting W₄ | P | PROVED (gap closed by PP) | needs a_p(f)≠0 at some p with χ₁₄₀(p)=−1, p∤cond ψ: a₁₁=4, χ₁₄₀(11)=−1; infinitely many by Chebotarev (F4) |
| Oc-2 explicit basis | O | OPEN | |
| Oc-3 consistent with all records; no PROVED result depends on the identification | P | **CONDITIONAL** (regraded) | a record-survey statement, not math; conditional on completeness of Local's survey (F6) |
| Oc-3 relation Ξ_RTA ↔ W₄/Oc-2 | O | OPEN | |
| V-1 Ind is a representation; no conflict with R26 | P | PROVED | normalized W² = −I ∈ Γ₀(49) |
| V-1 ρ(W²)=Id via tip §1u | C | CONDITIONAL (on §1u) | slash scalar check 49⁻²·(−49)² = 1 correct |
| V-1 Φ=(F,F\|W) form; +1 vectors F+F\|W | P | PROVED | |
| V-1 +1 law imposes no constraint | P | PROVED | |
| V-2 cited carriers g₊, f_Ξ (w=+1) | P | PROVED (cited, previously audited) | w = −ε = +1 consistent |
| **V-3 not a representation** | R | **REFUTED (PP exact proof, independent of R26)** | §1(a) |
| J-1 Γ₀(49)∩Γ₀(140)=Γ₀(980) | P | PROVED | |
| J-1 f_Ξ ∉ S₂(Γ₀(980)) | P | PROVED | 19600 ∤ 980 |
| J-1 W₄₉ matrix does not normalize Γ₀(980) | P | PROVED as a matrix fact; **consequence overstated** | W₉₈₀ and the level-980 Atkin–Lehner W₄₉^{(980)} do normalize Γ₀(980), so "J-1 carries no Fricke +1 law" does not follow (F5) |
| J-2 inclusion 980 \| 19600 | P | PROVED | |
| J-2 minimal level 19600 | P | PROVED | |
| J-2 W₁₉₆₀₀ normalizes; w(f_Ξ)=+1 | P | PROVED | |
| J-2 equivariant embedding of V₄₂ | O | OPEN | undefined |
| J-3 E ≅ Ξ over K | P | PROVED | exact |
| J-3 J ~ E×Ξ, L(J)=L(E)L(Ξ) | P | PROVED | Milne; Euler-factor check exact |
| J-3 cond(J)=960400; modular level 19600 | P | PROVED | PP: N(f_{E_K})=49, 140²·49=960400 (F2 wording) |
| J-3 ε(J)=−1, analytic rank 1 | P | PROVED (PP arb certificate) | as filed float-only ⇒ would be COND (F3) |
| J-3 Weil-carrier map | O | OPEN | |
| H-1 Option M P̂²=−1, P̂HP̂⁻¹=−H (Majorana) | P | PROVED | PP re-derived: α_k real, β imaginary |
| H-1 ι exists (cited ac1dd4e2) | P | PROVED (cited, previously audited) | |
| H-2 square γ⁰γ⁰*⊗1₃₅; ι carries over | P | PROVED | |
| H-2 real structure on ℂ³⁵ | O | OPEN | |
| H-3 anti-diagonal ℂ^d⊕ℂ^{2d} impossible | R | REFUTED | rank argument |
| H-3 odd d: Option-M P̂²=−1 impossible | R | REFUTED (scope: A⊗σ_x form) | \|det V\|²=(−1)^d; the text "so P̂²=+1" should read "P̂²≠−1"; a general antiunitary on ℂ^{2d} with square −1 does exist (F7) |
| a-1 automorphic, unramified; no datum at {2,5,7} | P,P | PROVED (cited, previously audited) | |
| a-2 π₂₃=1 | P | PROVED | (140/23)=+1 |
| a-2 automorphic, ramified at {2,5,7}, π_∞ trivial | P | PROVED | |
| a-2 Λ(s,π,std) formula; L(1,χ₁₄₀)=4log ε/√140 | C | CONDITIONAL | PP: h=2 and ε=6+√35 of norm +1 give 0.8376792812… (float match) |
| a-3 (−7/23)=+1, ramified at 7, π_∞ nontrivial | P | PROVED | |
| a-3 candidate set infinite; example list | P | PROVED | PP Jacobi symbols match |
| b-1 Λ = ξ²∏ξ(s∓i), poles 1,3,3,1, total 96 | P | PROVED | PP re-derived |
| b-2 Kostant degree 1128 | P | PROVED | |
| b-2 FE, poles −45..46, total 2256, order 48 at 0 and 1 | P | PROVED | |
| b-3 Λ=ξ for π=1 | P | PROVED | |
| b-3 forgets the Satake datum | P | PROVED | |
| c-1 #OG(n,2n)(𝔽_q) formula, equal to the contour | P | PROVED | theorem plus PP brute force (1,3),(2,3),(2,5),(3,3); exact 377-digit equality |
| c-2 contour = 2·one-family count | P | PROVED | |
| c-3 vol normalisation ≠ contour | R | REFUTED | exact Fractions: 1<1/vol<2 |
| α lemma B-preserving ⇔ tt*=1 | P | PROVED | algebraic; residual illustrative |
| α-1 R_pᵀBR_p=B | P | PROVED | exact |
| α-1 parity (cited Addendum L); P invertible | P | PROVED (parity cited) | |
| α-2 integral ⇒ ±R_p | P | PROVED | identity coefficient Σα²=1 (K90 distinct mod 140) |
| **α-3 exact example; 48 solutions on 6 supports** | P | **PROVED** | §1(c) |
| α-3 full real classification | O | OPEN | c3 numerics uncertified; c3c unused |
| α-4 uniform not B-preserving, not a similitude | R | REFUTED | identity coefficient 11, 23 nonzero off-identity coefficients |
| O5-1 a.c. spectrum, mult ∞, ι (cited) | P | PROVED (cited, previously audited) | FW re-check is float support only |
| O5-1 Majorana AHA⁻¹=−H | P | PROVED | analytic proof; log residual 0 |
| O5-2 m=0 spectrum ℝ, ι exists | P | PROVED | Hahn–Hellinger, uniform multiplicity ∞ |
| O5-3 no ι with a finite-multiplicity eigenvalue | R | REFUTED | k ≠ 2k |
| O5-3 even real scalar V breaks inversion | R | REFUTED | for the stated subclass only |

## 3. PP rollup
- **PROVED 41 · CONDITIONAL 5 · OPEN 7 · REFUTED 7 · PENDING 0** (60 graded claims, the same count as Local's).
- Only one tag changes: Oc-3's record-consistency claim goes from PROVED to CONDITIONAL.
- Two claims Local filed on float or cited support stay PROVED only because of PP's new exact or ball-arithmetic certificates: V-3 is now independent of R26, and J-3's analytic rank uses arb.
- One PROVED claim keeps its grade only with a narrowed scope: J-1's W₄₉ fact (F5).
- One gap is closed by PP: Oc-2's twist argument (F4).
- One REFUTED claim needs a wording and scope fix: H-3 odd d (F7).

## 4. Fix list for Local (additive errata only)
1. **F1 V-3:** replace "rests on cited tip R26" with the exact structural proof (§1(a): W T W⁻¹ = S T⁴⁹ S⁻¹ together with an e(−1/140) eigenvector in V₄₂), or cite this PP file. Record that R26 itself is float-only (SVD tol 1e-8).
2. **F2 J-3 wording:** distinguish **conductor** cond(J) = 960400 = 49·140² = N(f_{E_K})·d_K² (N(f_{E_K}) = 49, f = 𝔭₇²) from **minimal modular level** 19600. Do not write "Res ~ 49a1×Ξ at level 19600" without saying which.
3. **F3 J-3 certificates:** cite a rigorous certificate (this PP arb run) for L(49a1,1) ≠ 0 and L′(Ξ,1) ≠ 0 instead of the c2e9b6fe floats. Cite Milne (1972) for Res_{K/ℚ}E_K ~ E×E^{χ_K}; the 400-prime check is supporting only. Fix the c1 log label "primes 3..400" in any rerun.
4. **F4 Oc-2:** add the condition a_p(f) ≠ 0. Witness: p = 11 gives a₁₁ = 4 and χ₁₄₀(11) = −1. Infinitely many such p exist (split in ℚ(√−7), inert in ℚ(√35); Chebotarev), so one can avoid cond ψ.
5. **F5 J-1:** restrict the consequence to the level-49 matrix W₄₉ = (0,−1;49,0). The level-980 Fricke W₉₈₀ and the Atkin–Lehner W₄₉^{(980)} normalize Γ₀(980), so "J-1 carries no Fricke +1 law" is not proved as stated.
6. **F6 Oc-3:** retag the record-consistency bullet as CONDITIONAL (on completeness of the survey), or move it out of the math rollup.
7. **F7 H-3 odd d:** change "So P̂² = +1 ≠ −1" to "P̂² = VV̄⊗1 ≠ −1". State that the refutation covers the Option-M form A⊗σ_x only, because ℂ^d⊗ℂ² is even-dimensional and admits antiunitaries with square −1.
8. **F8 α lemma:** say that the proof is the group-ring identity. The 1.8e−15 residual is illustration, not evidence.
9. **F9 custody:** add gen_findings_t4407.py (bba18ccf…) to the §E table. Its sidecar already verifies.

## 5. Per-topic grading summary for the Owner (PP grades math only; nothing adopted)
- **O-c:** All three candidates are mathematically coherent.
  - Oc-1's facts are PROVED except for the Waldspurger link, which is CONDITIONAL. Oc-1 is not pinned until O-a.
  - Oc-2 is CONDITIONAL on existence, and its basis is OPEN.
  - Oc-3 is a naming choice with no math risk.
  Local's pick Oc-3 is consistent with its graded consequences.
- **V₈₄:**
  - V-1 is a valid representation (PROVED), but its +1 law adds no constraint (PROVED).
  - V-2 is the status quo, with cited facts.
  - V-3 is REFUTED, now by an exact PP proof.
  Local's pick V-2 is consistent.
- **Joint carrier:**
  - J-1 carries no Ξ (PROVED). Its "no Fricke" consequence is overstated (F5).
  - J-2's minimal level 19600 is PROVED.
  - J-3 is fully PROVED: conductor 960400, modular level 19600, ε = −1, analytic rank 1 certified.
  Local's pick J-3 (+J-2 level) is consistent. The Weil-carrier embedding stays OPEN under every candidate.
- **H₊U:** H-1 and H-2 are PROVED where claimed, with H-2's real structure OPEN. H-3 is REFUTED. Local's pick H-1 is consistent.
- **LD-O3a:**
  - a-1, a-2 and a-3 are all PROVED admissible (π₂₃ = 1).
  - a-2's L-function identification is CONDITIONAL.
  - The Codex datum does not determine π (PROVED).
  Local's pick a-1 is a minimality choice.
- **LD-O3b:** b-1, b-2 and b-3 are all PROVED as stated. The choice is one of convention.
- **LD-O3c:** c-1 matches the contour exactly, and c-2 matches it with a factor 2 (both PROVED). c-3 is REFUTED.
- **α (O4):** α-1 and α-2 are PROVED. The α-3 example is PROVED exactly, with its classification OPEN. α-4 is REFUTED.
- **O5:** O5-1 and O5-2 are PROVED. O5-3 is REFUTED, both for ι and for the even-scalar inversion.

Professor Proof (PP). Audit only. Nothing adopted. No CERT. No Gemini. Nothing sent. Tip 7cddb188 untouched.
