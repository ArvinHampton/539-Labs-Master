# ERRATUM (Local-derived): PP audit fixes to Bridge C pass 9e34f2dc and erratum c2e9b6fe, 2026-11-09 19:52 CST (America/Chicago)

- **Targets (NOT edited):**
  - "c2e9b6fe": ERRATUM_LOCAL_RELABEL_ce4d9e80_ROOTNUMBER_VS_FRICKE_SYMBOLS_AND_STS_CONTROL_2026-11-09_1819.md, sha256 c2e9b6fe2cb6b08ec24a7f6dfddc967eb7918adb244050d2d67c703b033d42ec.
  - "9e34f2dc": FINDINGS_LOCAL_BRIDGE_C_OPEN_ITEMS_RESOLUTION_PASS_2026-11-09_1822.md, sha256 9e34f2dc7fab9b3c42b6f73fc815b3ff2cfc62e496c6af04ce311ed94b6f39dd.
- **Audit applied:** FINDINGS_PP_AUDIT_LOCAL_ERRATUM_c2e9b6fe_AND_BRIDGEC_PASS_9e34f2dc_2026-11-09_1949.md, sha256 edcd955190294393ac1d9696b3d9f6cc4334538894fdcf817a1ec9d29cb82380 ("PP edcd9551"). Its §8 lists Fixes 1–15, all applied below by reference.
- **Authority:** Owner voice 17:30 (OW ff8a1670, item 4). Verbatim: "Pursue all for resolution to all bots."
- **Nomenclature:** OW voice call-81b74a31, 19:37 CST, record sha256 f1d167d1949a6df231eb908bf3574f0e289e91ce297b4376417ac910f2a037a4. In this file "RTA" reads as **resonant algebra**, with RTA kept only as a historical alias. There is no residual/resonant split. This is a naming change only; no grade changes.
- **Rules:** additive file. Nothing deleted, renamed, moved or overwritten. Tip 7cddb188… untouched (sha checked before and after). No CERT, no Gemini, nothing sent outside. Pure math only.
- **New Local evidence:** evidence_local_pp_edcd9551_fixes_2026-11-09/q1_quick_checks.{py,log}, sha256 14b77302897dea2e4b18d26cda4f1f0eca420d84ce8aa54661ec4f980f789997 / 3b3a80c2db1fdb529db2ca8a6151014d7ce0a156ff5f980c190dd728d709888a, each with a sidecar.
- **PP evidence cited:** /workspace/audit-scratch/pp_c2e9b6fe_9e34f2dc_local_1822/. Local re-ran `sha256sum -c` on its 18 pp_* sidecars: all OK.

## Fixes to c2e9b6fe
**Fix 1 (§3, L28: XW L68 row).**
- **Old:** XW L68 listed as a symbol swap, "corrected" to **w(f⊗χ) = w(f)·χ(−N)**.
- **New:** "XW L68 was **not an error**. ε(f⊗χ) = χ(−N)·ε(f) is true as written, as a root-number statement (Iwaniec–Kowalski Prop. 14.20; Atkin–Li 1978). The w-form is also true, because ε = −w_N at both levels. **Both readings are true.** The actual symbol errors in XW are **only at L69 and L97**."
- The L69 (L29) and L97 (L30) rows stand. This corrects c2e9b6fe's cross-reference count from "3 cross-reference lines in XW" to **2**.

**Fix 2 (§5, L50).**
- **Old:** "ce4d9e80's rollup (PROVED 13 · CONDITIONAL 2 · OPEN 4 · REFUTED 1)".
- **New:** "ce4d9e80 §7's updated rollup for XW (PROVED 13 · CONDITIONAL 2 · OPEN 4 · REFUTED 1)".

**Fix 3 (§4, L46: L-function line).**
- **Old:** stated as facts.
- **New:** "`lfuncheckfeq` = −135 bits, 'analytic rank 1', L′(Ξ,1) = 4.4326… and L(49a1,1) = 0.9666…: **CONDITIONAL** (floating point). Only **L(Ξ,1) = 0** is PROVED, from ε(Ξ) = −1 exactly."
- Local note, which does not change PP edcd9551's count: PP's later arb certificate in 320c8c7e §1(b) bounds L(49a1,1) ∈ [0.96665585280840577337 ± 3.5e−21] and L′(Ξ,1) ∈ [4.4326227316864161623 ± 2.2e−20]. Citing it would make "analytic rank of Ξ = 1" and "L(49a1,1) ≠ 0" PROVED. lfuncheckfeq stays float-only. This is offered to PP and not applied to the tally.

**Fix 4 (§2, L20/L22: L25 row, optional; applied).**
- **New text:** "(1,0;−1,1) = STS⁻¹ **= S⁻¹TS** (S² = −I is central). The old wording 'S⁻¹T⁻¹S' gives (1,0;1,1), a conjugate of T⁻¹. The modulus √140 holds either way, since |tr ρ(T^{±1})| = √140."
- Local check (q1 log): S·T·S⁻¹ = S⁻¹·T·S = [1,0;−1,1] and S⁻¹·T⁻¹·S = [1,0;1,1].

## Fixes to 9e34f2dc
**Fix 5 (2c(iii), L40).**
- **Old:** "R_χ maps S₂(Γ₀(49)) into S₂(Γ₀(lcm(49, m²))) for a primitive χ mod m (Shimura, … Prop. 3.64; cited). lcm(49, 140²) = lcm(49, 20²) = 19600."
- **New:** "Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Prop. 3.64 (cited) gives level **N·m²**. Applied to **χ₋₂₀** (m = 20), it gives R_{χ₋₂₀}f ∈ S₂(Γ₀(49·20²)) = S₂(Γ₀(19600)). By (ii), R_{χ₁₄₀}f = R_{χ₋₂₀}f, so the χ₁₄₀-twist lies there too."
- No lcm statement is attributed to Prop. 3.64. Applied to χ₁₄₀ directly it would only give 49·140² = 960400 (q1 log).

**Fix 6 (2g, L69).**
- **Old reason:** "by multiplicity one it does not occur at level 980 | 19600".
- **New reason:** "**19600 ∤ 980**. By Atkin–Lehner–Li newform theory, a newform of conductor 19600 lies in S₂(Γ₀(M)) only if 19600 | M." PROVED stands.

**Fix 7 (2e, L59).**
- **New scope:** "REFUTED: f_Ξ lies in **the span of the χ₁₄₀-twists of F₂** = {R_{χ₁₄₀}θ₁², R_{χ₁₄₀}(7θ₁(7·)²)}." REFUTED stands for this scope only.

**Fix 8 (3b, L81–82): withdraw 3b-ii; rename F₁ → K₁.**
- **Old (L82):** "For t = 3 and t = 5, one basis vector (F₁) lifts with a component outside that span. So the 4-dimensional space is **not exactly** f-isotypic…"
- **New:** "**WITHDRAWN: REFUTED by counterexample to its evidence** (PP edcd9551 §5, pp_3b3). The vector is **K₁ (matker column 1 of K)**. It is not the row-reduced F₁ of 3a (L78), which is a different vector and keeps its name.
  - PARI `mfshimura` mis-identified the lift by placing it in a level-49 space, which cannot contain f(2τ).
  - Shimura's defining formula A_t(n) = Σ_{d|n} χ₂₈(d)(−4/d)(t/d)·c(tn²/d²) gives **S₃(K₁) = −2f(2τ)** and **S₅(K₁) = f + f(2τ)**.
  - All 4 basis vectors × 23 squarefree t ≤ 35 lie in span{f, f(2τ)} up to n = 30 > Sturm 28 (cited: Shimura's theorem that S_tF ∈ M₂(Γ₀(98))).
  - Methodological note: when PARI `mfshimura` picks a level-N/4 space, check the lift against the T_p relations or use the explicit formula."
- Local check (q1 log): PP's formula lifts for K₁ equal −2f(2τ) and f + f(2τ) coefficientwise for n ≤ 20, using 49a1's a_n (a₂ = 1, a₈ = −3, a₉ = −3, a₁₁ = 4).
- The "(F₁)" in part3_check2.log's header row is read as K₁. The log is not touched.
- 3b-i (t = 1 lifts in span{f, f(2τ)}) stays PROVED.

**Fix 9 (3e O-a, L96): narrowed, and N1 added.**
- **New O-a:** "**N1 (CONDITIONAL, new; PP edcd9551):** K is f-isotypic.
  - Exact: T(p²)K = a_p(f)K for every prime p ≤ 59 with p ∤ 14, including p = 5, 17, 19 (pp_3b4).
  - For all p it is CONDITIONAL on Shimura's Hecke equivariance (cited). On M₂(Γ₀(98)), a₃ = 0 isolates f's eigensystem.
  - **O-a now reduces to:** writing out the eigensystem-isolation argument, and the U/V operators at 2 and 7. OPEN (narrowed)."

**Fix 10 (4a, L107, L109–110): exact certificate replaces step (iv).**
- **Old step (iv):** "|σ_a(β_i)| ≤ 140⁵·5.21×10⁻¹³ ≈ 0.028 < 1 …"
- **New step (iv):** "Exact: PP's pp_4a_exact (py 90ed5512…, log 789473d6…; PP edcd9551 §6).
  - β ≡ 0 in F_p at all 48 embeddings, for 4 split primes p ≡ 1 (mod 140), for every one of the 259 Schreier generators.
  - |σ(β_i)| < 2^{71.3} and |N(β_i)| ≥ P⁴⁸ with P ≈ 2^{108} force β = 0.
  - **A measured float residual is not an upper bound, so the old step (iv) is SUPERSEDED.**"
- **L109, delete-by-reference:** "The relations … were checked at a = 1, 3, 139 to 1.7×10⁻¹³." **New:** "The SL₂(ℤ) relations S⁴ = 1 and (ST)³ = S² of the normalized ρ_{N₂} are verified **exactly** (same mod-p norm argument; PP edcd9551 §6). So 'ρ is a representation' is proved here, not only cited."
- **L110 caveat:** resolved, no longer needed.
- **L108 control (1,0;70,1), new row 4a-c (PROVED):** "Exact: 140·⟨e₀, ρe₀⟩ = Σ_δ(−1)^{140q(δ)} = 0, so the off-e₀ mass is exactly 1."
- 4a stays **PROVED**, now exact and computer-assisted, resting on PP's certificate.

**Fix 11 (4b, L113–119, L132–133).**
- **Old:** "Adoption … (CONDITIONAL, Owner)", counted in CONDITIONAL.
- **New:**
  - The induced-carrier lemma is **PROVED** (elementary).
  - Its application to V₄₂ is **CONDITIONAL on tip §1u** (ρ(−I) = Id on V₄₂, cited read-only).
  - **Adoption of V₈₄ is an Owner decision, not a math grade.** It is removed from the CONDITIONAL tally and listed separately as "1 Owner decision".

**Fix 12 (3d, L88–89): add N2.**
- **New:** "**N2 (PROVED, new; PP edcd9551):** the 9 twists in part3_check2 with ε = +1 and L ≈ 0 (D = 40, 44, 53, 57, 172, 188, 248, 264, 316) have **L(1) = 0 exactly**.
  - ellrank gives bounds [2, 2], so the algebraic rank is 2.
  - By Gross–Zagier–Kolyvagin (cited), analytic rank ≤ 1 would force algebraic rank ≤ 1. Since ε = +1, the analytic rank is even and ≥ 2, so L(1) = 0.
  - The 75/75 count in 3d is now float-dependent only for the nonzero L-values (all ≥ 0.19). 3d stays CONDITIONAL (Waldspurger)."
- Local check (q1 log): all 9 twists of 49a1 have root number +1 and ellrank bounds [2, 2].

**Fix 13 (L13 and evidence: part3_preimage).**
- **Note only:** "The coredisc(−n) zero-pattern table in part3_preimage.log (sha256 e2085808…, L8 onward) is **SUPERSEDED by part3_check2**. That mapping fails at **n = 7**: c(7) = 0 on K, while coredisc(−7) = −7, f⊗χ₋₇ = f and L(f,1) = 0.9666… ≠ 0 (q1 log). No claim uses that table."
- The file is not touched.

**Fix 14 (rollup, L144–159, and table L130–133).** The new 9e34f2dc rollup counts PP's rows N1, N2 and 4a-c:
- **PROVED 13:** 2a, 2b, 2c, 2d, 2f′, 2g, 3a, 3b-i, 3c, 4a, 4a-c, 4b (lemma), N2.
- **CONDITIONAL 2:** 3d, N1.
- **OPEN 6:** O-a (narrowed), O-b, O-c, H₊U, Λ₀ dynamics, 2/5-parts.
- **REFUTED 3:** 2e, 2f, 3b-ii.
- **Owner decision 1 (not counted):** V₈₄ adoption (4b-adopt).
- **Table rows:**
  - Row 3 reads "3a, 3b-i, 3c PROVED; 3d CONDITIONAL; N1 CONDITIONAL; N2 PROVED; 3b-ii REFUTED".
  - Row 4 reads "PROVED (exact, computer-assisted; PP pp_4a_exact)". Its interval-hardening path is closed by PP's certificate.
  - Rows 5–6 read "math PROVED; application CONDITIONAL on §1u; adoption: Owner decision".

**Fix 15 (nomenclature).** All new Local files from now on, this one included, say "resonant algebra" where earlier files said RTA (OW 81b74a31 / f1d167d1), with RTA as a historical alias only. O-c accordingly reads: "is the resonant algebra's 'weight-3/2 Ξ shadow' (DEFINITION_RTA_RESIDUALS…_2026-10-26.md:53–55) this packet?" It remains a definition question for the Owner. No existing file is edited.

## Corrected rollup
- **c2e9b6fe:** PROVED 10 · CONDITIONAL 1 · OPEN 0 · REFUTED 0 (E1–E10 PROVED; E11, the float L-values, CONDITIONAL).
- **9e34f2dc:** PROVED 13 · CONDITIONAL 2 · OPEN 6 · REFUTED 3, plus 1 Owner decision (not counted).
- **Combined: PROVED 23 · CONDITIONAL 3 · OPEN 6 · REFUTED 3, plus 1 Owner decision.**
- **This matches PP edcd9551 §7 exactly (23/3/6/3 + 1).**
- **Relabels from Local's filed counts** (9e34f2dc was 11/2/6/2):
  - 3b-ii: PROVED → REFUTED.
  - 4b-adopt: CONDITIONAL → Owner decision.
  - New: N1 (COND), N2 (PROVED), 4a-c (PROVED).
  - 4a: PROVED, basis now exact.
- Bridge C stays **PARTIAL**.
- **Item-3 status changes from 9e34f2dc:** 3b-i, 3c and N2 PROVED; 3d and N1 CONDITIONAL; 3b-ii REFUTED; O-a narrowed, O-b and O-c OPEN. K is no longer claimed to be not f-isotypic; it is f-isotypic CONDITIONAL on Shimura equivariance (N1).

## Disagreements
- None with PP's 15 fixes. All are applied.
- One observation (Fix 3 note, not applied to the count): PP's own 320c8c7e arb certificate could upgrade "analytic rank 1" and "L(49a1,1) ≠ 0" from CONDITIONAL to PROVED. This is left for PP to decide.

Local-derived. For PP audit. Tip 7cddb188 untouched. No CERT. Nothing sent outside.
