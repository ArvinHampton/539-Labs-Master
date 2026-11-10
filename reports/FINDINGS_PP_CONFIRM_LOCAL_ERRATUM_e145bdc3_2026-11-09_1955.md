# FINDINGS (PP confirm): Local erratum e145bdc3 applying PP edcd9551's 15 fixes, and the ruling on the arb upgrade. 2026-11-09 ~19:55 CST (America/Chicago)

- **Auditor:** Professor Proof (Soft SF). Audit only: no adoption, no CERT, nothing sent outside, no Gemini.
- **Tip:** 7cddb188ca340ad9… matched before and after; read only. Lock 96f8d42e §4 untouched and still purged.
- **Naming:** "resonant algebra" per OW 81b74a31. The OW record sha256 is f1d167d1949a6df231eb908bf3574f0e289e91ce297b4376417ac910f2a037a4 and matches its sidecar. Naming only.
- **PP evidence:** /workspace/audit-scratch/pp_e145bdc3_confirm/, with a sidecar on each file:
  - rerun_arb.log, db136ad0…, identical to the 320c8c7e log;
  - pp_arb_altM.py, 554cfc4c…;
  - pp_arb_altM.log, 9a452cd6….

## 1. Integrity
| Object | sha256 (recomputed) | Sidecar | Status |
|---|---|---|---|
| ERRATUM_LOCAL_BRIDGEC_PASS_9e34f2dc_AND_c2e9b6fe_PP_AUDIT_FIXES_2026-11-09_1952.md | e145bdc3f559fe17b18720a0470543472f25972b1a8ccf54b5f756c6ea2c1c63 | same | MATCH |
| c2e9b6fe (erratum 1819) | c2e9b6fe2cb6b08e… | unchanged | **untouched** |
| 9e34f2dc (Bridge C pass 1822) | 9e34f2dc7fab9b3c… | unchanged | **untouched** |
| PP edcd9551 (1949) | edcd955190294393… | unchanged | untouched |
| q1_quick_checks.py / .log | 14b77302… / 3b3a80c2… | OK / OK | PP rerun is **identical** |
| PP scratch pp_c2e9b6fe_9e34f2dc_local_1822 | 18 sidecars | all OK | matches Local's claim |
| part3_preimage.log (Fix 13 citation) | e2085808… | — | prefix MATCH |

## 2. Fidelity of the 15 fixes
Each line number Local cites was checked against the original files.

| Fix | Target | Line(s) checked | Faithful? | Note |
|---|---|---|---|---|
| 1 | c2e9b6fe §3, XW L68 row | L28 | YES | "both readings true"; cross-reference count 3 → 2 (L69, L97) is correct |
| 2 | c2e9b6fe §5 | L50 | YES | wording exactly as asked |
| 3 | c2e9b6fe §4, L-function line | L46 | YES | labels CONDITIONAL as asked; the upgrade question is ruled in §3 below |
| 4 | c2e9b6fe L25 row | L20, L22 | YES | the q1 log shows STS⁻¹ = S⁻¹TS = [1,0;−1,1] and S⁻¹T⁻¹S = [1,0;1,1] |
| 5 | 9e34f2dc 2c(iii) | L40 | YES | Prop. 3.64 now gives N·m² and is applied to χ₋₂₀ (19600); the χ₁₄₀ route would give 960400 |
| 6 | 2g | L69 | YES | reason "19600 ∤ 980" |
| 7 | 2e | L59 | YES | scope is the χ₁₄₀-twists of F₂ |
| 8 | 3b | L81–82 | YES | 3b-ii withdrawn as REFUTED; F₁ renamed K₁ while row-reduced F₁ keeps its name; methodological note added. The q1 log reproduces S₃(K₁) = −2f(2τ) and S₅(K₁) = f + f(2τ) for n ≤ 20 |
| 9 | 3e O-a | L96 | YES | N1 entered as CONDITIONAL; O-a narrowed |
| 10 | 4a | L107–110 | YES | the exact certificate replaces step (iv); relations now exact; 4a-c added as PROVED |
| 11 | 4b | L113–119, L132–133 | YES | lemma PROVED; V₄₂ application CONDITIONAL on §1u; V₈₄ is an Owner decision |
| 12 | 3d | L88–89 | YES | N2 PROVED. The argument "ε = +1 ⇒ even order; GZK ⇒ not 0 ⇒ ≥ 2" is correct. The q1 log reproduces the 9 rank bounds [2,2] |
| 13 | part3_preimage note | L13 / evidence | YES | the n = 7 failure is correct (c(7) = 0 while L(49a1,1) ≠ 0); file not touched |
| 14 | rollup and table | L144–159, L130–133 | YES | 13/2/6/3 + 1 Owner decision |
| 15 | nomenclature | — | YES | the new file uses "resonant algebra"; "RTA" survives only as a historical alias and in file names |

**Fidelity: 15/15 faithful. No existing file was edited.** Local's statement that the result matches edcd9551 §7 (23/3/6/3 + 1) was correct as of edcd9551; §3 below amends it by one row.

## 3. Ruling: does the 320c8c7e arb certificate upgrade E11?
**What the certificate bounds** (PP pp_j3_lvalues_arb, py 4747836f…, log db136ad0…; sidecars OK; rerun identical):
- **Curves and twist.** E = 49a1 = [1,−1,0,−2,−1] with N = 49 and ε = +1 (exact). Ξ = elltwist(49a1, 140), i.e. the χ₁₄₀-twist, with N = 19600 and ε = −1 (exact).
- **Series.** These come from the functional equation of the weight-2 newform (modularity cited):
  - ε = +1: L(E,1) = 2Σ a_n/n·e^{−2πn/√N}.
  - ε = −1: L′(E,1) = 2Σ a_n/n·E₁(2πn/√N).
  - The a_n are exact integers.
- **Arithmetic.** arb ball arithmetic at 200 bits, with E₁ = −Ei(−x) evaluated rigorously by arb.
- **Truncation error, rigorous.** It uses |a_n| ≤ d(n)√n ≤ 2n (Deligne/Hasse, with d(n) ≤ 2√n), which gives a tail ≤ 4q/(1 − e^{−c}) with q = e^{−c(M+1)}. For E₁ it uses E₁(x) ≤ e^{−x}/x ≤ e^{−x}/(c(M+1)). The tail is added to the ball radius. Both bounds are valid.
- **Results:**
  - L(49a1,1) ∈ [0.96665585280840577337 ± 3.47e−21], which excludes 0.
  - L′(Ξ,1) ∈ [4.4326227316864161623 ± 2.16e−20], which excludes 0.
- **Independent cross-check (pp_arb_altM).** 256 bits, truncations M = 150/250 for 49a1 and M = 1500/2500 for Ξ:
  - L(49a1,1) ∈ [0.9666558528084057733665384 ± 1.96e−26].
  - L′(Ξ,1) ∈ [4.432622731686416162321555 ± 1.59e−25].
  - The balls overlap and exclude 0.

**Which claim goes with which curve.** E11 in c2e9b6fe L46 reads "Analytic rank 1, with L′(Ξ,1) = 4.4326…" and then "For 49a1: analytic rank 0, L(1) = 0.9666…". So "analytic rank 1" belongs to **Ξ**, not to 49a1, and the pairing is right. 49a1 (CM by ℚ(√−7), conductor 49) has analytic rank 0. Local's Fix 3 note pairs them correctly ("analytic rank of Ξ = 1", "L(49a1,1) ≠ 0").

**Ruling: split E11 into E11a and E11b.**
- **E11b: PROVED (upgraded).** This covers:
  - **Analytic rank of Ξ is exactly 1:** L(Ξ,1) = 0 exactly from ε(Ξ) = −1, and L′(Ξ,1) ≠ 0 rigorously.
  - **L(49a1,1) ≠ 0, so the analytic rank of 49a1 is 0.**
  - Both values to the digits stated (L′(Ξ,1) = 4.4326227316864…, L(49a1,1) = 0.9666558528…), since they lie inside the certified balls.
  - Basis: the arb certificate together with the exact conductor and ε. Modularity and the functional equation are standard theorems (BCDT, or CM for these curves).
- **E11a: CONDITIONAL (unchanged).** `lfuncheckfeq` = −135 bits is a floating-point diagnostic. It is not needed, because the functional equation is a theorem.
- **Rollup impact:**
  - c2e9b6fe goes from 10/1/0/0 to **11/1/0/0/0**, since E11 is now two rows, E11a COND and E11b PROVED.
  - 9e34f2dc is unchanged at 13/2/6/3/0, plus 1 Owner decision.
  - **Combined: PROVED 24 · CONDITIONAL 3 · OPEN 6 · REFUTED 3 · PENDING 0, plus 1 Owner decision.**

## 4. Verdicts on e145bdc3
| # | Item | PP |
|---|---|---|
| C1 | sha and sidecars of e145bdc3 and q1; targets untouched | **PROVED** (exact recomputation) |
| C2 | Fixes 1–15 faithful to PP edcd9551 §8 | **PROVED** (15/15, line-checked) |
| C3 | Local's rollup 23/3/6/3 + 1 matches edcd9551 §7 | **PROVED** as of edcd9551; amended to 24/3/6/3 + 1 by §3 |
| C4 | Fix 3 note: the arb certificate upgrades "analytic rank (Ξ) = 1" and "L(49a1,1) ≠ 0" | **PROVED** (upgrade granted, E11b); lfuncheckfeq stays COND (E11a) |

Rollup of this confirmation: **PROVED 4 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · PENDING 0.**

## 5. Remaining items for Local (optional; none blocks anything)
1. Record the E11a/E11b split and the combined rollup 24/3/6/3 + 1 in your next additive file, citing this file and 320c8c7e §1(b) / pp_j3_lvalues_arb.
2. When citing the certificate, name the curve for each claim: "analytic rank 1" for Ξ = 49a1⊗χ₁₄₀, and "L(1) ≠ 0, rank 0" for 49a1.

PP confirm only. Nothing adopted. No CERT. Tip 7cddb188 untouched (read only). No external sends.
