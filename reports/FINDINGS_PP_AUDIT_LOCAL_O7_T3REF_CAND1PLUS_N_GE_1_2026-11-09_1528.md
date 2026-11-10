# FINDINGS — PP audit of Local O7: T3_ref Local-T3ref-Cand-1⁺ (n ≥ 1) proof attempt — 2026-11-09 15:28 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Authority: GO (2) under OW 5a6e7177… (verified). Additive; the audited files are unchanged. Tip 7cddb188… untouched. No CERT. Nothing sent outside. No Gemini.
PP scripts/logs: /workspace/audit-scratch/pp_local_o3o5o7_1521/: descent.c (independent C/OpenMP, uint64 with overflow guard) → descent_1e10_pp.txt (sha 9a52e246…); o7_checks.py → o7_checks.log (sha 89845dc6…); manifest SCRATCH_MANIFEST.sha256.

## 0. Hashes
- FINDINGS_LOCAL_T3REF_CAND1PLUS_N_GE_1_PROOF_ATTEMPT_2026-11-09.md: 24e31966d55181d72d589a4faaa87bbd64eb4495c71530cf11955aede7bbefe6 — **MATCH**.
- Evidence dir reports/local-t3ref-cand1plus-n1-evidence-2026-11-09/: descent_vectorized.py, descent_1e10_result.txt, cycle_and_density.py, cycle_and_density_result.txt — all four **MATCH** their sidecars (sha256sum -c OK). Scripts inspected: logic is correct (residues 0,2 dropped by item 1; first-descent loop keeps x ≥ n; overflow assert < 2⁶¹; step cap 2000).

## 1. Audit
- **Map / statement:** T(3k)=k, T(3k+1)=4k+2, T(3k+2)=2k+1 with affine forms (1,0),(4,2),(2,−1) over 3. Checked: 2(3k+2)−1 = 6k+3. Cand-1⁺ as stated. CONFIRM.
1. **Reduction (D) — PROVED, CONFIRM.** Strong induction is valid because T maps ℕ_{≥1} to ℕ_{≥1}. Run-length identity T(x)+2 = 4(x+2)/3 on x ≡ 1 (mod 3) verified algebraically and for x < 10⁶; ascending runs have length v₃(n+2).
2. **LL-1 (residue-vector bijection, affine on classes) — PROVED, CONFIRM.** The proof is correct, since A_i is prime to 3 and the class lift is preserved. PP brute-force check for j ≤ 8: the map is a bijection onto {0,1,2}^j and invariant on n + 3^j·t.
3. **Density 0 — PROVED, CONFIRM.** The density is **natural density** (upper density ≤ the bad-class fraction for every j, hence 0).
   - μ = (1/3)ln(8/27) = −0.405465, σ² = 0.320302 (recomputed). The Chebyshev bound P(S_j ≥ 0) ≤ σ²/(jμ²) is correct.
   - Exact bad-class fractions recomputed with exact integer test 2^{2c₁+c₂} ≥ 3^j: j=10: 0.0150892; 20: 5.9923×10⁻⁴; 40: 1.26641×10⁻⁶; 80: 2.20908×10⁻¹¹. These are identical to Local's and below the Chebyshev bounds 0.195 / 0.097 / 0.049 / 0.024.
   - On good classes, finitely many exceptions per class: correct.
   - This is a Terras/Everett-type statement and does not touch E = ∅.
4. **Verification n ≤ 10¹⁰ — PROVED (computer-assisted), CONFIRM by independent rerun.** PP C program, every n in [3, 10¹⁰] (all residues, not only 1 mod 3): all descend; max first-descent steps **62** (at n = 9,316,379,509); max peak **4,698,479,263,742** (from n = 9,428,826,220). These exactly match Local's figures; 3.7 s wall.
   - 10⁷ rerun: max steps 40 (n = 635,929), peak 569,520,126 (n = 8,562,103), matching the 11-05 figures.
   - Extra spot check (evidence only): 20,000 random n in [10¹⁰, 10³⁰] (seed 20261109) all reach {1,2}, max 278 steps.
5. **Cycle length ≥ 79,335 — PROVED (given item 4), CONFIRM.** Method: the Steiner/Simons–de Weger-type product identity 3^p = 2^u∏(1+β_i/n_i), with β ∈ {0, ½, −½}, plus the minimum element > N. This gives |p·log₂3 − u| ≤ p·(−log₂(1 − 1/(2(N+1)))), and a direct search returns the least admissible p. It is a crude bound, not Baker-type, which is fine for a lower bound.
   - PP recompute at 80 digits: least p = **79,335**, u = 125,743, distance 5.28707×10⁻⁶ ≤ bound 5.72281×10⁻⁶.
   - 79,335 is a convergent denominator of log₂3 (cf [1;1,1,2,2,3,1,5,2,23,2,2,1,1,55,…]; denominators …, 15601, 31867, **79335**, 111202, …).
   - For N = 10⁷: p ≥ 9,616 (u = 15,241). This is a semiconvergent, 14·665 + 306, not a convergent; Local does not claim otherwise.
   - "Every element > 10¹⁰" is correct: an element ≤ N would put {1,2} in the cycle.
6. **Cand-1⁺ — OPEN, CONFIRM.** The gap is stated exactly: exclude long cycles (≥ 79,335, all elements > 10¹⁰) and divergent orbits inside the density-0 set E. The Conway (1972) undecidability remark is context for the general class only. Citation tag: CONDITIONAL until pinned.
7. **Not REFUTED — CONFIRM.** No counterexample ≤ 10¹⁰ (independently reproduced).
§2's weaker PROVED forms (specific starts; "almost all n" in natural density) are correct offers for the Owner's choice.

## 2. PP rollup
Local's rollup **PROVED 5 (items 1, 2, 3, 4 computer-assisted, 5 given 4) · CONDITIONAL 0 · OPEN 1 (Cand-1⁺) · REFUTED 0 — CONFIRMED.**
- Errors found: none.
- The n=0 refutation 1b7316a4 is unaffected.
No CERT. Tip untouched.
