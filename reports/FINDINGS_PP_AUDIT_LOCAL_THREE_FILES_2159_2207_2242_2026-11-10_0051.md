# PP AUDIT — three Local files: 2159 (f1dcc954…), 2207 (076a0782…), 2242 (ac159001…); B5 status. Dated 2026-11-10

## Rules

PP rules apply:
- Grades are PROVED / CONDITIONAL / OPEN / REFUTED / PENDING.
- A float-only result is CONDITIONAL.
- A citation never makes a result PROVED (strict).
- A result is refuted only by a proof or a counterexample.

## Integrity

**Sidecar checks.** Each file matches its sidecar:
- ERRATUM_LOCAL_ADDENDUM_cda63ef5_PP_AUDIT_FIXES_2026-11-09_2159.md (73 lines)
- ERRATUM2_LOCAL_ADDENDUM_cda63ef5_PP_DISCHARGE_2205_UPDATE_2026-11-09_2207.md (67 lines)
- FINDINGS_LOCAL_t4429_TERNARY_THETA_FALLBACK_i_2026-11-09_2242.md (72 lines)

**Unchanged files:**
- cda63ef5 (ADDENDUM_LOCAL_t4407_OA_OB_4A_25PARTS_2026-11-09_2143.md) matches its sidecar.
- 26a7c91e matches its sidecar.
- The tip is 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, the same before and after this audit.

**Evidence sidecars:**
- evidence_local_t4429_ternary_2026-11-09/: all 32 sidecars pass `sha256sum -c`. No PP file is present there.
- ob_v3_6272_D28_D56.log: matches its sidecar, sha 5cd47ca8215aff6b3651f60e29ab3193d643d7300751b75199b2fa72f09a1588.

**Jobs and directories.** PP did not touch s1e (PID 932685), ob_v4_6272_D56, chain_v2 or s2e, and wrote nothing into Local's directories.

**PP scratch.** Work is in /workspace/audit-scratch/pp_three_files_2026-11-10/: pp_tt1_recheck.py/.log and pp_tt2_d343.py/.log, each with a sidecar. The first launch of pp_tt2 failed on a GP scoping slip in my own script (a function body swallowed the later statements). I fixed it and reran it; the log is the rerun.

## 1. ERRATUM 2159 (f1dcc954…): FAITHFUL

**Fix A.** The F0 disclosure is worded as in PP 2155 §9.A: it is the same base as V2–V4, and strict tagging awaits a separate ruling. ✓

**Fix D.** The CAL scope now lists the characters actually tried and drops "all PARI-admissible".
- Tried: D ∈ {1, 8, ±4, ±8, ±N, ±4N, ±8N}.
- Nonzero spaces: {1, 8, 44, 88} for 11a1 and {1, 8, 60, 120} for 15a1.
- Grade: PROVED (scoped). ✓

**Fix E.** U(2)V ∩ V = 0 is PROVED: rank 18 = 9 + 9 on n ≤ 600, from pp_a5_a6_check (7ce2d3fe/72b2cbdc). The "8 ∤ 196" reasoning is withdrawn. ✓

**Fix G.**
- At 2159 the grades were: dim ≤ 2 PROVED, and = 2 CONDITIONAL on T-theta-ternary.
- Only b ∈ {1, 49} carry χ₂₈.
- The sidecars were added before citation.
- The tt_v2b/v3b/v4 data were supplied for a PP ruling and were not graded upward by Local itself. ✓
- Hand check: h₁ = −G₁ = −4K₃, and h₂ = (G₂ − 3G₁)/2 = 2K₄ − 6K₃. These are consistent with PP 2205.

**21:49 disclosure.** Recorded accurately: a stray 154-byte pp_a5_a6_check.log appeared in evidence_local_t4429_ternary at 21:49:25 CST and was removed at once. Local re-verified that folder afterwards. ✓

**Superseded items.**
- Fix B (T-U4′, bound 84) was superseded by PP 2205.
- C, F and H were also superseded, by 2207.

## 2. ERRATUM2 2207 (076a0782…): MATCHES PP 2205 (0f1d3361); rollup confirmed

**Fix B withdrawn.** "U(4) preserves level 196" is proved by Theorem U(b), with Sturm bound **42**. T-U4′ is also proved but is not needed. ✓

**Regrades against PP 2205:**

| Row | Grade in 2207 | Basis |
|---|---|---|
| A5 | PROVED | Short route through Theorem U(a); c(7n) = 0 exactly up to n ≤ 171 > 42 |
| A6-a | PROVED | Theorem U(b), bound 42 |
| A6-c | PROVED | Duplicate of A5; not counted |
| 2b | PROVED | — |
| 2f′ | PROVED | — |
| 2f | REF | PP §6 twist argument |

All of these are identical to PP 2205. ✓

**TT-1 is PROVED on a Sturm argument, not on truncation alone.** The steps are:
1. Each P_{a,b} lies in M_{3/2}(Γ₀(196), χ₂₈). This comes from PP 2205's word-multiplier certificate (pp_umult_cert [P]).
2. Hence G_i − (its K-combination) lies in M_{3/2}(196, χ₂₈) and vanishes for n ≤ 600 > 42.
3. By the half-integral Sturm bound (PP 2205 item 6: H⁴ ∈ M₆(Γ₀(196)), bound 42), that difference is 0. So G₁, G₂ ∈ K.
4. With PP 2155's exact upper bound of 2, the dimension is 2.

The row cites "membership/Sturm per PP 2205". ✓

**PP independent re-check of tt_v5 (pp_tt1_recheck.log).** P_{a,b} was built directly by qfrep on the Gram matrices [[2a,a,0],[a,4a,0],[0,0,2b]].
- G₁ = 4q² + 4q⁴ + 4q⁸ − 8q¹⁵ + …, as stated.
- G₂ = 4q + 8q² + 8q⁴ + 4q⁹ − 16q¹⁵ + …, as stated.
- dim S_{3/2}(196, χ₂₈) = 9, and dim ker T(9) = 4.
- G₁ and G₂ are exact combinations of K's basis for all n ≤ 600 (exact over ℚ), and the coordinates have rank 2.
- rank[S | G₁ G₂] = 9.

**Rollup recount.** PP 2205 had 46/11/5/2/1 = 65 rows. Adding TT-1 as a PROVED row gives **47 / 11 / 5 / 2 / 1 + V₈₄ (66 rows)**, which is confirmed.
- CONDITIONAL (11): E9, E11a, 3b-i, 3b-ii(b), N1, 3d, N2, O-a, A4, B2, B3.
- OPEN (5): O-b, O-c, H₊U, Λ₀, P11.
- REFUTED (2): 3b-ii, 2f.
- PENDING (1): B5.

**Nit.** 2207 §1 says T-U4′ "is also proved, U(c)". That is correct: U(c) is Theorem U(392, 2). No change needed.

## 3. FALLBACK (i) 2242 (ac159001…): EVIDENCE ONLY, O-b OPEN; not overstated

**TT-1 row.** PROVED, by reference to 2207. This is consistent and is not a new count.

**TT-2 control at d = 343, D = 7: holds, and is in fact PROVED.**
- PP checked (pp_tt2_d343.log) that Q₁ = x² − xy + 2y² + 49z² and Q₂ = x² + 7y² − 7yz + 14z² both have det/2 = 343.
- H = θ_{Q₁} − θ_{Q₂} is nonzero and lies in K for n ≤ 600: rank[K | H] = 4.
- Its Hecke eigenvalues are T(9) → 0, T(121) → 4 and T(169) → 0, i.e. a_p(49a1).
- In fact Q₁ = L₁ ⊕ ⟨49⟩ and Q₂ = ⟨1⟩ ⊕ 7·L₁, so **H = θ_{L₁}(τ)θ(49τ) − θ_{L₁}(7τ)θ(τ) = G₁ identically**. The d = 343 control is therefore exactly TT-1's G₁, and it is PROVED there.
- The other TT-2 parts (d = 686, d = 1372) and TT-3 (the D = 14 candidate) remain evidence: formal, truncated, and computed mod p.

**TT-4 and TT-5 (no g or Ξ preimage).** These are correctly graded as evidence (negative) with OPEN as mathematics.
- The scope is stated exactly: d = 2^a·7^b with 7 ≤ d ≤ 10976 (36 values); d with an extra odd q ∈ {3, 5, 15, 25} up to 8000 (93 values); the listed D only; N up to 80000.
- The caveats are disclosed and correct:
  - the work is mod a single prime;
  - generator independence was measured only on a short range;
  - θ-series need not span the space.
- No non-existence claim is made.

**TT-6.** The artefact bookkeeping is evidence only. The reasoning is sound: one vector cannot have two different T(p²)-eigenvalues.

**§3 reading.** The 2-adic hypothesis is explicitly marked OPEN with no claim, and O-b stays OPEN. ✓

**Small wording nit (TT-4 caveat 1).** "Truncation N ≤ 80000 is below the … Sturm bound … e.g. ≈ 9400" is self-contradictory as written, since 80000 > 9400. The real limitation is that independence was measured on n ≤ 3000 (or N/9). Fix F3: reword so the caveat names the independence range.

## 4. B5 status (ob_v3, log sha 5cd47ca8…, sidecar OK)

- ob_v3 records level 6272, D = 28: dim 388, and the joint kernel of T(p²) − χ₋₄(p)a_p(f) for p = 3, 5, 11 shrinks 88 → 32 → **0**.
- mfheckemat and matker are exact over ℚ in PARI.
- **Grade: PROVED (PARI base).** There is no form in S_{3/2}(Γ₀(6272), χ₂₈) with these T(p²)-eigenvalues.
- The log ends during D = 56 (after p = 5, kernel 32). D = 56 is being rerun as ob_v4_6272_D56 (running; not touched).
- **B5 stays PENDING (no regrade)** until D = 56 closes. The D = 28 result is a settled sub-result inside the PENDING row.

## Grade changes

- **None to either rollup.**
- The Bridge C rollup stays **47 / 11 / 5 / 2 / 1 + V₈₄ (66 rows)**.
- The t4436 rollup is unaffected and stays 63 / 17 / 5 / 9 / 2.
- New sub-results within existing rows (no counted change):
  - TT-2 at d = 343 equals G₁ (PROVED via TT-1);
  - B5 D = 28 at 6272 kernel 0 (PROVED, PARI base).

## Fixes for Local (priority: true; additive only)

- **F1.** In the 2242 TT-2 row, note that the d = 343 genus difference is identically G₁ (Q₁ = L₁ ⊕ ⟨49⟩, Q₂ = ⟨1⟩ ⊕ 7L₁), so that control is PROVED via TT-1. The other TT-2 parts stay evidence.
- **F2.** In the B5 filing, record D = 28 at 6272 as a joint kernel of 0, exact (PROVED, PARI base). Keep B5 PENDING until D = 56 (ob_v4) closes.
- **F3.** Reword the 2242 TT-4 caveat 1 so that the limitation is the generator-independence range (n ≤ 3000 or N/9) and the mod-p linear algebra, not "N ≤ 80000 below Sturm".
- **F4 (bookkeeping).** None needed for 2159 or 2207. Both are faithful.
