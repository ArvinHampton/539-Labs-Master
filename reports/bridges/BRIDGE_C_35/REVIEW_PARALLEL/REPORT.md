## REVIEW_PARALLEL: audit of the Bridge Series C shadow and foundation work (BRIDGE_C_35, parent through order8)

Reviewer: parallel audit for Arvin Hampton. Written Sat 2026-10-24, about 3:45–4:05 PM CDT (America/Chicago).

- **Scope read:** parent PREREG/REPORT/RESULTS/NOTES, plus order2, 3, 3b, 3c, 4a, 4b, 5, 6, 7 (PREREG/RESULTS/NOTES each) and order8 (PREREG and its logs/data only; order8 RESULTS is not written yet).
- **Hashes:** `sha256sum -c PREREG.sha256` returns OK in every order folder.
- **What was run:** one light check, `scripts/weight_scan.py`. It works only on the recorded arrays `order3/data/parts.npz` and `order4b/data/A2.npz`, and evaluates no new series. Output: `data/weight_scan.json`. It is Category B and recorded nothing new as a verdict.
- **Rules kept:** nothing existing was modified, the ledger was not edited, CORE_FREEZE holds, and there was no push and no send.

Tags:
- **M** = missed variable or unscanned parameter.
- **P** = pattern.
- **Cr** = correlation.
- **X** = contradiction or inconsistency.

Cat = the category of the underlying statement (A = exact or arithmetic; B = numerical or descriptive).

## Summary table
| # | Tag | Cat | Finding | Pointer |
|---|---|---|---|---|
| 1 | X | A | **Theorem 3 sign convention.** The PREREG states (B) for every rational x ≠ 0 with weight \|x\|^{−1}. RESULTS proves it only for x > 0, using (x√35)^{−1}. K2_0 = G_{a,0} is P-even (Q(−ν) = Q(ν)). With M² = 35P, the \|x\| form is P-even-consistent, while the signed form x^{−1} (the radial limit of a holomorphic weight-1 τ-law) forces P-odd, i.e. A0 ≡ 0. So the leading law is an \|τ\|-type P-even law, not the radial shadow of a weight-1 holomorphic law. All tests use x > 0, so this was invisible | `RESULTS.md` Thm 3; `PREREG.md` §3; `order7/RESULTS.md` §0 |
| 2 | Cr/X | A | **order8 M2a restates parent Lemma 2.** 2L = log(6+√35) (log confirms L = 1.23894436514), so A0_E = mean(f)·2L/√35 = 2I·mean(f). This is the ±orthant area from Lemma 2. A pass of M2a is therefore **not independent evidence** of a Θ_E ↔ Φ_orth link, and it should not be counted as a bridge under the lock | `order8/PREREG.md` §2; `RESULTS.md` Lemma 2; `order8/logs/m1.log` |
| 3 | X | B | **order8 M2 preregistered verdict is FAIL; the posthoc run passes.** The logs show A2 errors of 1.16e−3 (x = 1), 6.9e−5 (x = 1/2) and 2.8e−5 (x = 1/3) against the 1e−5 line, with "FAIL" printed. `m2posthoc` passes (≤ 5.2e−6). The grid t = 0.02/(2m)² repeats the scaling flaw disclosed in order2 NOTES. order8 RESULTS must record the preregistered FAIL first | `order8/logs/m2_*.log`, `m2posthoc_*.log`; `order2/NOTES.md` |
| 4 | M | B | **Weight scan incomplete.** A radial expansion of a weight-1 τ-law gives A_j(−1/x) ∝ \|x\|^{j−1} (test convention w = 1, 0, −1 for A0, A1, A2), and the A2 law picks up an A0(x) term from the τ factor and the real-part shift of −1/τ. Tests used only w ∈ {½, 1} for A1 and {0, ½, 1} for A2. The review scan (recorded arrays): A1 never closes for w ∈ {−1, −½, 0, ½, 1, 1.5} (joint 210). **A2 at w = −1 has joint rank 122, not 146**: 24 shared directions, not closed. span[\|x\|A2, A0] gives ε = 0.15. The recorded verdicts stand, but the w = −1 rank drop is unexplained | `REVIEW_PARALLEL/data/weight_scan.json`; `order4b/RESULTS.md`; `order5/RESULTS.md` (b) |
| 5 | M/X | B | **The mixed-law ansatz is not the one a weight-1 law predicts.** order4b T1 and order5(b) test span[A2, \|x\|^{½}A1, \|x\|A0]. The derived form is span[\|x\|A2, A0 (\|x\|^0), A1 terms]. The "decisive" order5(b) falsification is decisive only for its own ansatz. Because order5(b) uses A0(−1/x) as the negative control, any normalisation-dependent A0(−1/x) term is excluded by construction | `order5/PREREG.md` §3 |
| 6 | M | B | **Representative dependence of the companion family is never scanned.** S_{α,β} depends on the representative α, since wt is applied to v, not ν (order2 NOTES; order5 NOTES 4). A1 and A2 change under α → α + λ by finite unary-theta lines and half-lines, while A0 does not. Every order2–order5 closure test of A1/A2 tests one fixed choice (μ ∈ [0,1)²). Non-closure could partly reflect this choice | `order2/NOTES.md`; `order5/NOTES.md` 4 |
| 7 | M | B | **The P-parity split is never applied to A0/A1/A2.** order3b splits by characteristic (24 + 12 = 36). After the order7 lemma, the natural split is P-even/P-odd. dim V^{P=±1} is not recorded | `order3b/RESULTS.md`; `order7/RESULTS.md` |
| 8 | X | A/B | **The parity lemma is the stated blocking reason but lacks its promised exact certificate.** PREREG promised an exact check in Z[e(1/9800)]; it was done at mpmath dps 30 only (disclosed). The argument cites Weil-rep theory. The certificate is cheap and should exist before the lemma blocks a route | `order7/PREREG.md` §0; `order7/NOTES.md` 1 |
| 9 | X | — | **Count "four weight-3/2 unary thetas".** order6 RESULTS lists three distinct q-series: Σn e(5n²τ/2) (c1; shared by the cone and the odd orthant, both paired with θ_{7/2}), Σ R e(R²τ/34) (c2), and Σ m e(35m²τ/4) (c′). "Four" counts c1 twice. The axis half-lines add two quantum shadows (n², 7n²/2) that are not completions | `order6/RESULTS.md` verdicts |
| 10 | P | A | **Wall/cone arithmetic.** For u ⊥ c: Q(u)·\|Q(c)\| = 35·d²/4 with d = \|det(u,c)\|. c1: d = 1 (7/2·5/2 = 35/4); c2: d = 17 (595/2·17/2 = 35·17²/4); c′: d = 2 (1·35). This explains the "unimodular split", "glued over 17 classes" and "glued over 2 classes" of order5/6. −det A = 35 is the common source. Checked by hand | `order5/PREREG.md` §1.1, §1.5; `order6/PREREG.md` §2 |
| 11 | P/Cr | A | **log ε = log(6+√35) recurs consistently.** I = log ε/(2√35) (parent); μ_tot = log ε (order7, 2.478); L = ½ log ε (order8 M1, confirmed). The ±orthant subtends half the unit arc. The automorph γ = [[−1,−7],[2,13]] carries trace 12 = 2·6 | parent, order7, order8 |
| 12 | P | A | **Recurring constants and their sources.** −7/20 = Q(a) is the normaliser. 7/2 = (Aa)₂ = Q(0,1). 595/2 = 17·35/2. 105 = 3 families × 35. 36 = dim V = 24 (K2∪K3) + 12 (K4). 36/t_min is the order3c cutoff (truncation e^{−36}), unrelated to dim V. No written link to 539, T3, O_res or g_k exists, and none is proposed | parent; `order3b/RESULTS.md`; `order3c/NOTES.md` |
| 13 | M | A | **spec(T\|V) was never extracted.** Parent Test A2 ran on the formal 105-symbol span (a superset). Whether 0 ∈ spec(T\|V) is still open, though it is cheap from the exact M_T of entry 94. Map A does not depend on it | `NOTES.md`; `RESULTS.md` A2 row |
| 14 | M | B | **Unfollowed values.** \|A1(1/2)\| = \|A1(5/2)\| = √π/4 (order2, not proved). A2(1/2) ≈ 0 (order3c, 1.6e−15). So at x = 1/2 the series is exactly A1·t^{−1/2} + O(t^{1/2}). order8 M2 predicts A1_E = 0 for the even piece at x = 1, 1/2, 1/3. Rank 44 of Ĥ and Ĝ_O on 120 τ (order5 NOTES 7) and rank 97 of W_420 are unexplained. The descriptive Map 0 value A2(1/6) agrees with order3c | `order2/RESULTS.md`; `order3c/RESULTS.md`; `order5/NOTES.md` |
| 15 | M | — | **Axis companions.** 15 of the 105 have α1 ∈ Z or α2 ∈ Z. order6's generic decomposition and order8 M2 (α1, α2 ∉ Z) exclude them, and they have never been analysed separately | `order6/NOTES.md` 1; `order8/PREREG.md` §2 |
| 16 | X | — | **Stale readings.** order4a NOTES proposes "erf-completion constants" as a refinement, but order5 NOTES 6 shows the erf constants are invisible in A1 and A2, so that refinement cannot act radially. Also, order5 §1.4(ii) shows the cone part enters A1 exactly as a jump-sawtooth (the radial limit of the Eichler integral). That partly rehabilitates the order3 wall-sawtooth idea for the cone walls 7/2 and 595/2; the order3/4a "falsified" verdicts concern full A1, including the orthant. Neither earlier NOTES file is back-annotated | `order4a/NOTES.md`; `order5/NOTES.md` 6 |
| 17 | X | — | **Notation clashes.** "P" denotes P_s (two different series in the RTA manuscript, disclosed), P_orth, the involution P (order7), mod-p primes p, and p = Q(u1) (order2). "v vs ν" is consistent from order5 on, but order2–4 A1/A2 use v-weights. Ĥ in order5 is in ν-signs, while H in order2 lib2 is in v-signs (U_H bridges them) | parent `NOTES.md`; `order5/PREREG.md` §1.2 |
| 18 | X | — | **Minor documentation gaps.** order3c sign control accounts for 8 of 9 x-values (7 with \|C\| > 0.05, plus x = 1/2). The order2 PREREG time is "8:30" against an actual 8:22 (disclosed). The parent RESULTS row A2 says "not decisive" (correct), but REPORT does not mention that spec(T\|V) is still unextracted | `order3c/RESULTS.md`; `order2/NOTES.md` |

## Category A vs B bleed check
- **No case found** where a Category B result is reported as Category A, with these items to watch:
  - order5 "Ĥ's fixed S-law, Category A by citation". Fine, but it rests on Zwegers.
  - order7 parity lemma "Category A by Weil-rep" (finding 8).
  - order7 C2 "Category A by citation (Siegel)" while the coupling is inconclusive (correctly separated).
- **order5 correctly keeps A2(H) ≡ 0 and A2(S_odd) = A2(F) as proof sketches.** However, order6 NOTES and order8 PREREG M2c rely on A2(H) ≡ 0 as if proved. Keep the label "sketch" downstream.

## Effect on the running Φₖ work (order8)
- **Nothing blocks it.** Three redirects:
  1. Record the M2 preregistered FAIL before the posthoc result (finding 3).
  2. Do not count M2a as a link (finding 2). The only new content is M1 (the holomorphic projection). It is a Laplace or holomorphic-projection identity: Θ_E = 𝓗(Φ_orth) is close to tautological for a cone-integrated Siegel theta, so describe it as an identification, not a bridge.
  3. Before citing the parity lemma as "the reason the shadow is blocked", produce the exact M² = 35P certificate (finding 8). Also note that Theorem 3 is already a P-even \|x\|-type law (finding 1), i.e. the same transformation type as y^{−1/2}Φ. A P-even weight-1 obstruction applies to holomorphic τ-laws only.
- **Suggested next preregistrations** (none run here):
  - P-split closure tests (finding 7).
  - A representative scan (finding 6).
  - The derived A2 ansatz span[\|x\|A2, A0, …] with mod-p or mp ranks (findings 4–5).
## REVIEW_PARALLEL notes (process and disclosures). Times are CDT (America/Chicago).

## Process
- 15:42: Inventory. order8 had PREREG, scripts, logs and data, but no RESULTS/NOTES/REPORT; it was still running. Only its logs were read. No order8 file was touched.
- 15:44: `sha256sum -c PREREG.sha256` returned OK for order2 through order8.
- 15:47: Light check `scripts/weight_scan.py` (nice, OMP_NUM_THREADS=1, under 100 MB, under 1 s). Its first launch failed on a relative-path error before reading any data. The paths were fixed in the same file before any statistic was produced; nothing was preregistered for this check.
  - SVD threshold 1e−9, the same as order3.
  - The rows are the 216 positive x of XS, so \|x\| = x throughout. The sign question of finding 1 cannot be tested on these arrays.
- 15:55: Arithmetic checks by hand and in python, all exact identities:
  - Q(c1) = −5/2, Q(c2) = −17/2, Q(c′) = −35.
  - det(u,c) = −1, 17, 2.
  - L = arccosh(7/(2√3.5)) = 1.2389443651 = ½ log(6+√35).
  - I = 0.2094198203.

## Caveats
- The finding 1 argument uses M² = 35P (order7). The double application, for a signed law A0(−1/x) = (x√35)^{−1}MA0(x), gives A0 = −PA0; for the \|x\| law it gives A0 = PA0. That K2_0 is P-even follows from Q(−ν) = Q(ν) and β = 0, up to the A35 `reduce` phases, which were not re-inspected here. Treat finding 1 as an argument to verify, not as a new ledger fact.
- Finding 4/5's statement of the "derived weights" comes from a first-order Taylor treatment of −1/τ along the radial path. The exact coefficient of the A0 term was not derived.
- No new verdicts are claimed. Every recorded verdict in order2–order7 stands as written.
- No Residual↔Resonant link, T3, O_res, 539, crypto or g_k claim is made. No TPC/RH.
## RESULTS (REVIEW_PARALLEL)

See FINDINGS.md for the full table. The light check `data/weight_scan.json` is Category B and was computed on recorded arrays.

## Closure ranks [F | \|x\|^w F(−1/x)]
| F | rank | w = −1 | −½ | 0 | ½ | 1 | 1.5 |
|---|---|---|---|---|---|---|---|
| A0 | 36 | 72 | 72 | 72 | 72 | **36** | 72 |
| A1 | 105 | 210 | 210 | 210 | 210 | 210 | 210 |
| D | 58 | 116 | 116 | 116 | 116 | **98** | 116 |
| R | 105 | 210 | 210 | 210 | 210 | 210 | 210 |
| A2 | 73 | **122** | 146 | 146 | 146 | 146 | – |

## Mixed spans for T = A2(−1/x) (relative residual ε)
- span[\|x\|A2, A0]: rank 109, ε = 0.154.
- span[\|x\|A2, A0, A1]: rank 214 (near saturation), ε = 0.028.
- order4b T1 span reproduced: rank 214, ε = 0.079.

None of these closes.
