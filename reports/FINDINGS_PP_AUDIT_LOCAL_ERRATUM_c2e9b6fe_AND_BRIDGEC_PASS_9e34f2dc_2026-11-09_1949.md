# FINDINGS (PP audit): Local ERRATUM c2e9b6fe (ε vs w_N, STS⁻¹) and Bridge C open-items pass 9e34f2dc, 2026-11-09 ~19:49 CST (America/Chicago)

- **Auditor:** Professor Proof (Soft SF). Audit only. Nothing adopted. No CERT. Nothing sent outside. No Gemini.
- **Tip** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91. It matched before and after this audit and was read only. Lock 96f8d42e §4 untouched and stays purged.
- **Nomenclature (OW 81b74a31):** this file says "resonant algebra" for the object Local's files call RTA. That is a naming change only; no grade depends on it. Existing files are not edited.
- **Citations (OW 3f160803/36683379):** citations are allowed. A citation never makes a result PROVED by itself; below, every PROVED item that cites a theorem also has that theorem's hypotheses checked.
- **Prior partial work:** /workspace/audit-scratch/ had no directory mentioning c2e9b6fe, 9e34f2dc or local_1822 (searched to depth 4). Nothing was reused. This audit's evidence is in /workspace/audit-scratch/pp_c2e9b6fe_9e34f2dc_local_1822/, and every pp_* script and log there has a .sha256 sidecar. Key files:
  - pp_4a_exact.py / .log (90ed5512… / 789473d6…)
  - pp_3b4.py / .log (4b399987… / 2d039cfa…)
  - pp_3b3.log (9d777728…)
  - pp_extra.log (a0d871cb…)
  - pp_extra2.log (ac247d3b…)
  - pp_980b.log (ca8a1163…)

## 0. Integrity and authority
| Object | Full sha256 (computed) | Sidecar | Status |
|---|---|---|---|
| ERRATUM_LOCAL_RELABEL_ce4d9e80_…_1819.md | c2e9b6fe2cb6b08ec24a7f6dfddc967eb7918adb244050d2d67c703b033d42ec | same | MATCH |
| FINDINGS_LOCAL_BRIDGE_C_OPEN_ITEMS_RESOLUTION_PASS_…_1822.md | 9e34f2dc7fab9b3c42b6f73fc815b3ff2cfc62e496c6af04ce311ed94b6f39dd | same | MATCH |
| OWNER_WRITE_VOICE_9c8fa1db_t4358_PURSUE_ALL_OPEN_ITEMS_TO_RESOLUTION_ALL_BOTS_2026-11-09_1730.md | ff8a16701cd0832fc449c91fc9b2a2dc4ff84bf743a4fd757e07d21ddbacd441 | same | MATCH, OW verified |
| evidence_local_bridgeC_resolution_2026-11-09/ (12 files) | each recomputed | each sidecar | 12/12 OK |
| Cited targets: RELABEL ce4d9e80…, XW ae951f3e…, PP 5cbd050a… | recomputed | n/a | prefixes MATCH; quoted lines (ce4d9e80 L25, L36; XW L68, L69, L97; PP 5cbd050a L70) confirmed verbatim |

**OW ff8a1670, verbatim (whole body):**
> # OWNER WRITE — voice call-9c8fa1db — 2026-11-09 ~17:30 CST (America/Chicago)
> Source: Owner direct, live voice. "Pursue all for resolution to all bots."
> Each responsible bot works its open items to resolution and reports its resolution path and ETA.
> 1. Non Local Path (cap ~35 min): derive the Z2 parity of G4 (derivation, not declaration; both parities until derived; per OW 9a8ced02); continue faces that vary in more directions (mixed / x-dependent), since pure-M5 r_b(mu,phi) and r_b(sigma) have no solution; radial-profile ODEs; nonlinear localized-M5 effects.
> 2. Math Research 2: whatever blocks vacuum adoption after PP's EFT re-audit (full Riemann invariant, Sigma systole, non-AdS5-block check).
> 3. Professor Proof: finish the EFT re-audit (aaadb280 gate); audit NL 53096d43 (templates) and e2065e05 (non-constant face / localized M5, parity).
> 4. Local Path: open items on Bridge C A1->Xi->RTA (Bridge C PARTIAL), including the ce4d9e80 symbol fix.
> 5. Warden: confirm the three-hour check-in with Arvin in its own chat; Owner stated on voice that all bots are both nice-to-have and client-facing.
> Unchanged: no vacuum, source or b adopted; O1 OPEN; tip 7cddb188 untouched; No CERT; no Gemini; additive writes only.

Item 4 covers both Local files, so Local's authority line is correct. The verbatim phrase is "Pursue all for resolution to all bots."; "pursue all to resolution" is a paraphrase. Item 4's "RTA" is the Owner's own wording, quoted unchanged.

## 1. Reruns
| Local script | PP rerun | Result |
|---|---|---|
| part1_twist_newform | full | identical to Local's log, apart from a PARI stack banner |
| part3_check2 | full | identical |
| part3_halfint | full | identical |
| part4_gamma0_140_weil_e0 | full, single-thread | identical, apart from timings (float residual 5.2097e-13) |
| part3_search | timed out at 600 s after the level-392 rows; those rows are identical | PP reran the level-980 rows separately (pp_980b): trivial character and character 5 both give dim 66 with f-eigenspace 0, matching Local |
| part3_preimage | timed out at 1200 s under parallel load, so no comparable log | its outputs that the claims use were reproduced independently: dim 9, K of dim 4, row-reduced F₁ (n ≤ 60) identical, c(35) = 0 on K. Its coredisc(−n) zero-pattern table is not used by any claim; check2 supersedes it |

## 2. ε versus w_N (the convention used throughout)
- ε(E) = global root number (ellrootno). w_N(f) = eigenvalue under f|₂W_N, W_N = (0,−1;N,0). At weight 2, ε = (−1)^{k/2}w_N = −w_N.
- **Exact check at level 49:** mfatkininit gives w₄₉(f) = −1, and ellrootno(49a1) = +1, consistent with ε = −w.
- **Twist law (Iwaniec–Kowalski Prop. 14.20; Atkin–Li 1978):** ε(f⊗χ) = χ(−N)·ε(f) for χ primitive with conductor prime to N. For real odd χ the factor is τ(χ)²/r = χ(−1).
  - Because ε = −w at both levels, the same law holds with w in place of ε.
  - So XW L68 was already true as a root-number statement. Erratum §3's "correction" of L68 is harmless, but L68 was not an error.
  - The actual swaps are XW L69 (it plugs in ε(f) = −1 where w₄₉(f) = −1 and ε(49a1) = +1) and XW L97.
- **Data, exact:** ε(49a1) = +1. χ₋₂₀(−49) = −1. ε(Ξ) = ε(−20 twist) = −1. Hence w₁₉₆₀₀(f_Ξ) = +1.

## 3. Verdict table: ERRATUM c2e9b6fe
| # | Claim | Local | PP | Basis |
|---|---|---|---|---|
| E1 | ε = −w_N at weight 2 | stated | **PROVED** | standard identity (cited), checked exactly at level 49 (§2) |
| E2 | ce4d9e80 L36 → "w₁₉₆₀₀ = −ε = +1 (ε = −1)" | fix | **PROVED** | ellrootno(Ξ) = −1, exact |
| E3 | ce4d9e80 L25 → (1,0;−1,1) = STS⁻¹ | fix | **PROVED** | hand product, and PARI S·T·S⁻¹ = [1,0;−1,1], S⁻¹T⁻¹S = [1,0;1,1]. Note STS⁻¹ = S⁻¹TS since S² = −I is central. The trace modulus √140 is unaffected, because \|tr ρ(T^{±1})\| = √140 either way |
| E4 | XW L68 restated with w | fix | **PROVED** (statement true) | not an error originally (§2); see Fix 1 |
| E5 | XW L69 → w₁₉₆₀₀ = w₄₉·χ₋₂₀(−49) = +1 | fix | **PROVED** | exact (§2) |
| E6 | XW L97 → w₄₉ = −1 (ε = +1) | fix | **PROVED** | mfatkininit / ellrootno |
| E7 | §4 table: a-invariants, conductors, ε, j for 49a1, Ξ, the −20 twist and the −7 twist | PROVED | **PROVED** | rerun identical (Tate's algorithm, exact) |
| E8 | Ξ and the −20 twist are 7-isogenous, not isomorphic | PROVED | **PROVED** | PP independent: ψ₇(Ξ) factors as degrees 3 and 21. The isogeny with the cubic kernel (Vélu, ellisogeny) has image of conductor 19600, isomorphic to the −20 twist. ellisisom(Ξ, −20 twist) = 0 |
| E9 | Same newform: a_n equal for n ≤ 7000 > Sturm 6721 on Γ₀(19600) | PROVED | **PROVED** | index 40320; rerun identical; modularity of both curves cited (BCDT, or CM) |
| E10 | χ₁₄₀ = χ₋₂₀χ₋₇ | checked n ≤ 1000 | **PROVED** | both have period 140; PP checked n = 1..140 exactly |
| E11 | lfuncheckfeq −135 bits; analytic rank 1; L′(Ξ,1) = 4.4326…; L(49a1,1) = 0.9666… | listed as facts | **CONDITIONAL** (floating point) | L(Ξ,1) = 0 is PROVED from ε = −1. The value of L′ and "rank exactly 1" are float-only |

Erratum rollup (PP): **PROVED 10 · CONDITIONAL 1 · OPEN 0 · REFUTED 0 · PENDING 0.** Erratum §5's "no label changes" stands. Its wording "ce4d9e80's rollup (13/2/4/1)" refers to ce4d9e80 §7's updated rollup for XW; the numbers are quoted correctly (Fix 2).

## 4. Verdict table: Bridge C pass 9e34f2dc
| # | Claim | Local | PP | Basis / notes |
|---|---|---|---|---|
| 2a | f = ½Σ_{α∈O}(α\|√−7)·α·q^{Nα} | PROVED (Hecke cited) | **PROVED** | Hypotheses checked: ψ(−α) = ψ(α) since (−1\|7)(−1) = 1; ψ is multiplicative; its conductor is (√−7); the nebentypus χ₋₇(n)(n/7) = 1. Level 7·7 = 49. Sturm bound 10; coefficients match to n ≤ 600 (rerun) |
| 2b | θ_{L₄₉} = Eis + 1·f in M₂(Γ₀(49)) | PROVED | **PROVED** | exact mftobasis (rerun identical) |
| 2c | f_Ξ = R_{χ₁₄₀}f = R_{χ₋₂₀}f | PROVED | **PROVED** | (i) and (ii) correct. (iii) As cited, Shimura Prop. 3.64 gives level N·m², not lcm(N, m²). Apply it to χ₋₂₀ instead: 49·20² = 19600 (Fix 5). Sturm comparison n ≤ 7000 rerun |
| 2d | w₁₉₆₀₀(f_Ξ) = χ₋₂₀(−49)·w₄₉(f) = +1 | PROVED | **PROVED** | §2. The sign flip comes from χ₋₂₀(−1) = −1, with χ₋₂₀(49) = +1 (exact) |
| 2e | f_Ξ ∉ span of the χ₁₄₀-twists of F₂ | REFUTED | **REFUTED** (confirmed) | R(θ₁(7·)²) ≡ 0. The q¹ coefficient forces c = 1/4, and then the q³ coefficient is −4 where f_Ξ has 0. The scope is the χ₁₄₀ twist only (Fix 7) |
| 2f | f_Ξ is a twist of cusp(θ_{L₄₉}²) | REFUTED | **REFUTED** (confirmed) | twisting preserves weight (4 ≠ 2) |
| 2f′ | rank{f², cusp(θ_{L₄₉}²)} = 2 in S₄(Γ₀(49)), dim 10 | PROVED | **PROVED** | exact (rerun) |
| 2g | f_Ξ ∉ S₂(Γ₀(980)) | PROVED | **PROVED** | Atkin–Lehner–Li: a newform of conductor 19600 cannot lie in S₂(Γ₀(M)) when 19600 ∤ M. Local's reason "980 \| 19600" should read "19600 ∤ 980" (Fix 6) |
| 3a | S_{3/2}(196, triv) has dim 6, Kohnen⁺ = 0, T(9) charpoly (x+2)²(x²−2)²; χ₂₈ space has dim 9 and K of dim 4; level-392 and 980 rows | PROVED | **PROVED** | PP reran every item, including the T(9) charpoly and the level-980 rows (pp_extra, pp_980b) |
| 3b-i | t = 1 lifts of K lie in span{f(τ), f(2τ)} | PROVED | **PROVED** | Shimura's explicit formula (PP) agrees with PARI for t = 1. Sturm bound for M₂(Γ₀(98)) is 28 |
| 3b-ii | "For t = 3, 5 one basis vector lifts outside span{f, f(2τ)}, so K is not exactly f-isotypic" | PROVED | **REFUTED** | Counterexample to the evidence (§5). PARI `mfshimura` mis-identifies the lift: it places it in a level-49 space, which cannot contain f(2τ). Shimura's defining formula A_t(n) = Σ_{d\|n} χ₂₈(d)(−4/d)(t/d)·c(tn²/d²) gives S₃(K₁) = −2f(2τ) and S₅(K₁) = f + f(2τ). All 4 basis vectors × 23 squarefree t ≤ 35 lie in span{f, f(2τ)} up to n = 30 > Sturm 28. This uses Shimura's theorem (cited) that S_t F ∈ M₂(Γ₀(98)) |
| N1 (new) | K is f-isotypic | — | **CONDITIONAL** | Exact: T(p²)K = a_p(f)K for every prime p ≤ 59 with p ∤ 14, including 5, 17, 19 (pp_3b4). For all p this needs Shimura's Hecke equivariance (cited). On M₂(Γ₀(98)), a₃ = 0 isolates f's eigensystem among 14a, the 98 newforms and the Eisenstein systems. U/V at 2 and 7 not examined |
| 3c | c(35) = 0 on K; coredisc(35) = 140 | PROVED | **PROVED** | exact; L(Ξ,1) = 0 is forced by ε = −1 |
| 3d | 75/75 Waldspurger zero pattern | CONDITIONAL | **CONDITIONAL** (confirmed) | See N2. The nonzero L-values are float only (all ≥ 0.19) |
| N2 (new) | The 9 twists with ε = +1 and L = 0 in check2 (D = 40, 44, 53, 57, 172, 188, 248, 264, 316) have L(1) = 0 exactly | — | **PROVED** | ellrank bounds [2, 2] (descent upper bound plus points), so the algebraic rank is 2. By Gross–Zagier–Kolyvagin (cited), analytic rank ≤ 1 would force algebraic rank ≤ 1, so L(1) = 0 |
| O-a | exact f-isotypic subspace | OPEN | **OPEN** (narrowed) | see N1 |
| O-b | preimage of f_Ξ at level 78400 | OPEN | **OPEN** | — |
| O-c | is the resonant algebra's "weight-3/2 Ξ shadow" this packet? | OPEN | **OPEN** | a definition question for the Owner, not a theorem |
| 4a | ρ_{N₂}(γ)e₀ = χ₁₄₀(d)e₀ for all γ ∈ Γ₀(140) | PROVED (float, "caveat for PP") | **PROVED** (PP exact certificate) | §6. Local's own step (iv) is not rigorous as filed, because a measured float residual is not a bound. It is superseded |
| 4a-c | Control (1,0;70,1): the e₀-component is 0 | float 4e−16 | **PROVED** | exact: 140·⟨e₀, ρe₀⟩ = Σ_δ(−1)^{140q(δ)} = 0, so the off-e₀ mass is exactly 1 (ρ is unitary) |
| 4b | Induced-carrier lemma (W normalizes Γ₀(49); W² = −49I; +1 vectors are F + F\|W) | PROVED | **PROVED** | elementary. Applying it to V₄₂ uses ρ(−I) = Id from tip §1u, cited read-only, so the application is CONDITIONAL on §1u, as in PP 1911 V-1 |
| 4b-adopt | adoption of V₈₄ | "CONDITIONAL" | not a math grade: **Owner decision** | not counted (Fix 11) |
| H₊U | exact H_{+U} | OPEN | **OPEN** | undefined; Owner |
| Λ₀ | dynamical derivation | OPEN | **OPEN** | physics lane |
| 2/5 | "2- and 5-parts without twisting" | OPEN | **OPEN** | needs a statement |

**Tally check of Local's own rollup:** the items Local lists add up to PROVED 11, CONDITIONAL 2, OPEN 6, REFUTED 2, so the arithmetic is consistent.

**PP regrade of 9e34f2dc (Local's items plus the PP rows N1, N2, 4a-c):** **PROVED 13 · CONDITIONAL 2 · OPEN 6 · REFUTED 3 · PENDING 0.** One Owner decision (4b-adopt) is not counted.
- **PROVED 13:** 2a, 2b, 2c, 2d, 2f′, 2g, 3a, 3b-i, 3c, 4a, 4a-c, 4b, N2.
- **CONDITIONAL 2:** 3d, N1.
- **OPEN 6:** O-a, O-b, O-c, H₊U, Λ₀, 2/5.
- **REFUTED 3:** 2e, 2f, 3b-ii.
- **Changes from Local:** 3b-ii moves from PROVED to REFUTED. 4b-adopt moves from CONDITIONAL to Owner decision. N1, N2 and 4a-c are new. 4a stays PROVED, but now rests on PP's exact certificate rather than Local's float argument.

## 5. Item 3b-ii detail (pp_3b3, pp_3b4)
- K₁ = the first matker basis vector of K. Local calls it "F₁", but check2 indexes K's columns, not the row-reduced F₁ (Fix 8).
- **PARI `mfshimura(m, K₁, 3)`:** a₁…a₁₂ = 0, −2, 0, −2, 0, 0, 0, 2, −2, 0, −10, 0. Its space has level 49, and the result is not a T₃-eigenform.
- **Shimura's formula:** 0, −2, 0, −2, 0, 0, 0, 2, 0, 0, 0, 0 … = −2f(2τ). It satisfies a₉ = −3a₁ and a₃ = 0, as T₃-eigenvalue 0 requires.
- For K₂ (level 98 was chosen), PARI and the formula agree term by term.
- **Conclusion:** the rank-3 result in check2 is a PARI identification artifact. With the defining formula, every lift tested is f-isotypic.

## 6. Item 4a exact certificate (pp_4a_exact)
- **Setup:** the discriminant form of N₂ = [[2,14],[14,28]] (det −140, 140 elements) was rebuilt independently. S̃ = (ζ^{−B(γ,δ)}) and T̃ = diag ζ^{Q(γ)}, with ρ(S) = S̃/√140 and ρ(S⁻¹) = S̃*/√140. For a word with s S-letters, 140^{s/2}ρ(g)e₀ has entries in ℤ[ζ₁₄₀]. Here √140 = G(χ₁₄₀) = Σχ₁₄₀(n)ζⁿ ∈ ℤ[ζ], and G² = χ(−1)·140 = 140.
- **Group side:** BFS over P¹(ℤ/140) gives 288 cosets (= 6·6·8). The 259 nontrivial Schreier generators have length ≤ 39 and at most 10 S-letters. These match Local's numbers and were rebuilt independently.
- **Exact test:** let β = Ũe₀ − 140^{⌊s/2⌋}·G^{(s mod 2)}·χ₁₄₀(d)·e₀ ∈ ℤ[ζ]^{140}. PP computed β in F_p at all 48 primitive 140th roots, for 4 primes p ≡ 1 (mod 140): 134217301, 134216881, 134216461, 134216041. Such p splits completely, so this is exactly β mod pℤ[ζ]. The result is **β ≡ 0 for every generator, every embedding and every prime.**
- **Lifting to β = 0:** every embedding satisfies |σ(β_i)| ≤ L1 ≤ 140¹⁰ + 48·140⁵ < 2^{71.3}. If β_i ≠ 0, then β_i ∈ Pℤ[ζ] gives |N(β_i)| ≥ P⁴⁸ with P = ∏p ≈ 2^{108}, while |N(β_i)| ≤ (2^{71.3})⁴⁸. That is a contradiction, so β = 0.
- **ρ is a representation of SL₂(ℤ) (proved, not cited):** the relations S̃S̃* = 140I, S̃² = 140·P_{γ↦−γ}, (S̃T̃)³ = G·S̃² and S̃⁴ = 140²I were verified by the same mod-p and norm argument at all 48 embeddings. These are exactly S⁴ = 1 and (ST)³ = S² for the normalized ρ, which are the defining relations of SL₂(ℤ).
- **Conclusion:** γ ↦ χ₁₄₀(d) is a character of Γ₀(140), and the stabilizer of the e₀ line with that character is a subgroup containing all the generators. So it is all of Γ₀(140). **PROVED, exact, computer-assisted.**
- χ₁₄₀ (built as χ₋₄χ₅χ₋₇) equals the Kronecker symbol (140/·) on one period.
- **ε versus w:** 4a involves only χ₁₄₀(d), which is neither a root number nor a Fricke sign.

## 7. Overall rollup (this audit; both files)
**PROVED 23 · CONDITIONAL 3 · OPEN 6 · REFUTED 3 · PENDING 0.** One Owner decision is not counted.
- Erratum: 10 / 1 / 0 / 0 / 0.
- Bridge C pass: 13 / 2 / 6 / 3 / 0.
- Bridge C overall stays **PARTIAL**.

## 8. Fixes for Local (numbered)
1. **Erratum §3, XW L68:** not a symbol error. ε(f⊗χ) = χ(−N)ε(f) is true as written, and the w-form holds too, because ε = −w on both sides. Restate L68 as "both readings true; error only at L69 and L97."
2. **Erratum §5:** change "ce4d9e80's rollup (13/2/4/1)" to "ce4d9e80 §7's updated rollup for XW (13/2/4/1)".
3. **Erratum §4, L-function line:** label lfuncheckfeq, "analytic rank 1" and L′(Ξ,1) = 4.4326… as CONDITIONAL (floating point). Only L(Ξ,1) = 0 (from ε = −1) is PROVED.
4. **Erratum L25 (optional):** add "= S⁻¹TS". Also note that the old wording "S⁻¹T⁻¹S" gives (1,0;1,1), a conjugate of T⁻¹, and that the √140 modulus holds either way.
5. **9e34f2dc 2c(iii):** Shimura Prop. 3.64 gives level N·m². Either apply it to χ₋₂₀ (49·20² = 19600) or cite an lcm(N, m²) result correctly. As written, lcm(49, 140²) is attributed to a proposition that does not state it.
6. **2g:** the reason is "19600 ∤ 980" (newform theory), not "980 | 19600".
7. **2e:** state the scope as "the span of the χ₁₄₀-twists of F₂".
8. **3b:** withdraw "not exactly f-isotypic" (REFUTED, §5). Note that PARI `mfshimura` can return a mis-identified lift when it picks a level-N/4 space; use Shimura's explicit formula, or check that the lift satisfies the T_p relations. Also rename "F₁" in 3b to "K₁ (matker column 1)"; the row-reduced F₁ of 3a is a different vector.
9. **3e O-a:** update it. T(p²)K = a_p(f)K is exact for every p ≤ 59 with p ∤ 14, including 5. Full f-isotypy is CONDITIONAL on Shimura equivariance (N1). What remains is the eigensystem-isolation argument written out, plus U/V at 2 and 7.
10. **4a:** replace step (iv) (a float residual × 140⁵ < 1) with an exact certificate. A measured float residual is not an upper bound. Cite PP pp_4a_exact (90ed5512…/789473d6…) or reproduce it. Drop "dependencies … checked to 1.7e−13"; the relations are now exact.
11. **4b:** adopting V₈₄ is an Owner decision, not a CONDITIONAL math label, so remove it from the CONDITIONAL tally. Mark the application of the lemma to V₄₂ CONDITIONAL on tip §1u (cited read-only).
12. **3d:** add N2. The nine ε = +1, L = 0 twists are rank-2 curves (ellrank [2,2]), so L(1) = 0 is exact via Gross–Zagier–Kolyvagin. The 75/75 count is then float-dependent only for the nonzero values.
13. **part3_preimage:** mark its coredisc(−n) zero-pattern table as superseded by check2. That mapping fails at n = 7, where c = 0 but L ≠ 0.
14. **Rollups:** after Fixes 8 and 11, 9e34f2dc reads PROVED 13 · CONDITIONAL 2 · OPEN 6 · REFUTED 3, with one Owner decision (this counts PP's N1, N2 and 4a-c).
15. **Nomenclature (OW 81b74a31):** in new files say "resonant algebra" rather than RTA. Do not edit existing files.

PP audit only. Nothing adopted. No CERT. Tip 7cddb188 untouched (read only). Lock 96f8d42e §4 stays purged. No external sends.
