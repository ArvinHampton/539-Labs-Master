# FINDINGS — PP Soft SF audit of NL derived filing dff93e21 (junction-adjacent: GA9, S4 C∧X₈, A15/O5 limited; t552u pursuit)
2026-11-10, written 12:21:29 CST (America/Chicago). Author: Professor Proof (PP). Additive new file. No existing file was edited, moved, renamed, deleted or chmod-ed. Wording: resonant algebra. **Nothing adopted. Junction UNSOLVED. No CERT.** Tip read-only, mode left 644. No messages sent; the parent delivers.

Audited as filed. No first-proof. **No backreacted metric is constructed or ruled out here; that stays with MR2's 1130 lane.** The absence of an in-repo metric is not a resolution. Starting from the junction does not treat it as solved, and nothing below narrows it to solved or finds makeup. The 1142 grades, the 1120 framing, 9760 / N = 4880, 1a and B1-c2′ are not adopted.

The sibling gap filing (debc7d52) is cross-cited only. Its sibling findings, FINDINGS_PP_AUDIT_NL_NONBPS_GAP_FIXEDFACE_FLOW_PROFILE_debc7d52_2026-11-10_1221.md, sha 087acf470ba1c28bf14b94b106fccff1b5f100a65806849f5383d3b37ac9e6f8, grade H2 PROVED as an implication with named premises. That grade is cited only where this filing cites H2 (A15-2), and it does not change A15-2's grade.

## 0. Authority and scope
Authority is identical to the sibling findings §0. Briefly:
- **OW t552u** eae1b39d635c69966a2b32642d395ae402d3c33fcf64db7f0b77cad2d8c60db2 (= sidecar).
  - Owner verbatim: **"Pursue all for resolution."** Pursuit only.
  - **Transcript-VERIFIED verbatim.** In the Non Local Path chat transcript, user cu:405590937 says exactly this. The message is ordered between NL's 1142 report and its 1205 report, which is consistent with about 11:45 AM CST; no per-message clock is shown.
  - The Interpretation section is NL's, not an Owner ruling.
- OW 1130 945d81bb…, 1117 bff79185…, 1108 c6375f85…, t4436 32881263…, t4431 f700141d…: all = sidecar, all continue.
- PP 1137, FINDINGS_PP_AUDIT_NL_E8_INSTANTON_GEOMETRIC_DELTA_79ad0c64_2026-11-10_1137.md, 5cf927959babc94b1719c99b312cfbb9d6366237626c781e8d5c75f21ce15b03: cited only. PP E26 confirm f2e64d448127af7b90bf7d1a4353b7c5e1342cae927b30f75d544cd53a5b1c0d: FAITHFUL, 11:50:00.
- **NL 1142** e7312edb…: an **unaudited** prior filing. A PP findings file for e7312edb appeared on disk at 12:11 during this audit; it is not read or used.
- MR2 9811de14 / f4ee61f2 and their confirms are not mixed in, and L-GN is not used.

## 1. Integrity (PP re-hash)
| object | sha256 (PP) | sidecar | mtime CST | mode |
|---|---|---|---|---|
| filing NL_DERIVED_JUNCTION_GA9_S4_CX8_BACKREACT_LIMITED_2026-11-10_1205.md | dff93e2142227c8713bc2c5343141aeb83a2759f6d88763c7a0fe1c1da3a9970 | MATCH | 12:05:46.776 (header = mtime) | 644 |
| script /workspace/nl-gapjx-t552-1110/gapjx_junction.py | b054521be0b458821afc7d6bf6d44ae48bb1ba41d2181e4f5f2217e6309a0ac9 | MATCH | 12:02:26.341 (sidecar 12:02:26.345) | 444 |
| log /workspace/nl-gapjx-t552-1110/gapjx_junction_run.log | 6326cf4e2e81e345daedcb657722a9161719ab41dfefc088d0f33d0fb8787e3f | MATCH | 12:02:28.213 (sidecar 12:02:28.293) | 444 |
| OW t552u / 1130 / 1117 / 1108 / t4436 / t4431 | eae1b39d… / 945d81bb… / bff79185… / c6375f85… / 32881263… / f700141d… | all MATCH | — | — |
| PP 1137 / E26 / PP E26 confirm / NL 1142 | 5cf92795… / a44b18d9… / f2e64d44… / e7312edb… | all MATCH | — | — |
| tip (before) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | — | 2026-11-06 14:38:54.160 | 644 |

[PASS] lines in the frozen log: **10**, with ALL PASS not counted; [FAIL] lines: 0. The claimed 10/10 holds.

## 2. Evidence
All evidence is in the shared directory `/workspace/quantum-comp/reports/evidence_pp_audit_nl_t552u_gapjx_2026-11-10/`. Every file is mode 444 with a .sha256 sidecar, all MATCH.

**Re-run of NL's script.**
- nl_copy_gapjx_junction.py is a byte copy (b054521b…) of the frozen script; the original was not touched.
- It ran 12:17:33.402–12:17:34.887 CST and exited 0.
- nl_copy_gapjx_junction_rerun.log (6326cf4e…) is **byte-identical** to NL's log. Neither log has wall-clock lines.

**PP independent exact checks.**
- pp_indep_junction_exact_2026-11-10.py (6fc7cde59bfb28f0a5652897c7118329e5e576db496a313ecf37dd754a204b82) was frozen 444 before its run.
- Its log, pp_indep_junction_exact_2026-11-10.log (542fcb65f9fa2c66ede0fd0c646a5a8e962747a3c29b113c6fbc08eac625f952), shows **12/12 PASS**, exit 0.
- Methods: expand()==0, exact matrices and Fraction only; no simplify, powsimp, float, numpy or allclose.

Coverage:
- **PJ0:** J0, re-implemented from T_ab = F_acF_b^c − ¼η_abF². T_tj = 0 is also checked.
- **PJ1:** the J3 identity.
- **PJ2, PJ3:** the GA9-1 and GA9-2 linear programs, **solved independently by exact enumeration of all 3-column vertices**, rather than only checking NL's certificates.
  - Minima: 1/5 and 1/3 in the IR-kept pairing; 6/5 and 4/3 in the UV-kept pairing.
  - NL's duals y = (−1, 0, −¼) and (0, 0, ¼) are verified feasible, with matching objective.
- **PJ4:** within the model, no combination of positive-tension types and magnetic YM is feasible at any of the four end-face demands.
- **PJ5:** the §1 values 1 + w.
- **PJ6:** J4, for every spatial unit vector e, not only basis vectors.
- **PJ7, PJ8:** J8 and J9 with a **general symmetric Y₆ block of K** (off-diagonal entries allowed) and **any unit e ∈ Y₆**. The result is S(k,k) = −(2/κ²)(K(e,e) − k_t). NEC sources therefore need max eig(K|Y₆) ≤ k_t. This is stronger than NL's diagonal test.
- **PJ9, PJ10:** the J5 and J6 exponent arithmetic, redone as exact Fraction exponent pairs (l, N) instead of powsimp(force=True).
- **PJ11:** the S4-1 representative transgression, in an **independent Pauli-matrix realization** of su(2): δ[ε tr FF] = 4∂_c[ε tr(F_ab δA_d)].

**Namespace scan** (namespace_scan.txt):
- Imports are sympy, fractions and itertools only.
- "float" and "simplify" appear only in a comment (L3).
- powsimp and expand_power_base(force=True) in J5/J6 act on monomials in positive symbols. That is exact exponent arithmetic, not simplify-as-grounds, and PP reproduced it without them (PJ9, PJ10).
- The LP tests are pure Fraction.

**Freeze/run timing:** the log was written 1.872 s after the freeze, consistent with PP's measured runtime of 1.48 s. Clean.

**First-draft bugs (disclosed; the drafts are in /tmp and are not grounds):**
- PJ8 draft: the sign of the (|e|² − 1)·K residual term was wrong, which gave a FAIL. It was corrected to S(k,k) + (2/κ²)(K(e,e) − k) − (2/κ²)K(|e|² − 1) = 0 before freezing.
- PJ2 draft: it contained a dead `X if False else Y` construct. It was removed; it had no effect.

## 3. Item-by-item grades (NL claim → PP grade; premises named)
| item | NL | PP | premises / remarks |
|---|---|---|---|
| §1 / J8–J9 | (used by A15-1) | **PROVED (Israel algebra)** | Premises: the Z₂ Israel convention S = −(2/κ²)(K − hK), staticity (K_tj = 0) and Poincaré symmetry on (t, x). Holds for general symmetric K on Y₆ (PJ8). The end-face values −(1/5)ρ_req (UV fibre), 0 (UV Σ) and −(1/3)ρ_req (IR) use the J1 w-values, which are CONDITIONAL inputs. |
| GA9-1 | PROVED given J1, IR-kept | **PROVED (implication)** | Premises: the J1 w-values, IR-kept pairing, and **the block-averaged source model**: smeared −T·h objects of every (σ, φ) type with T of either sign, plus magnetic Y₆ YM only, constrained at trace level (ρ, tr_Σ, tr_fib). The exact LP optimum is \|1 + w_fib\|ρ_req = ρ_req/5 (UV) and ρ_req/3 (IR) (PJ2). The **"O(N)"** reading and the figures "≈ 3253 / ≈ 4190 M5 units" are **CONDITIONAL**, because they rest on the test targets 16266.7 / 12568.6 and J1/J5 scaling (F-3). |
| GA9-2 | PROVED given J1, UV-kept | **PROVED (implication)** | Same model and J1 premises, UV-kept pairing. The optimum is \|w_fib\|·\|ρ_req\| = 6/5 and 4/3 (PJ3). "Independent of which side is kept" holds within the model. |
| GA9-3 | PROVED | **PROVED** | S(k,k) = −Λh(k,k) = 0 for every null k (PJ6). "Only Y₆-localized negative tension can supply the deficit" holds **within the GA9 model** (J3/PJ1), not for arbitrary sources. |
| GA9-4 | CONDITIONAL | **CONDITIONAL** | Premises: the derivative-expansion structure (wall terms ℓ_P^{2k−10}R^k with pure-number coefficients) and J1 scaling L ∝ ℓ_P N^{1/3}. The exponent arithmetic is exact (PJ9). The absence of a wall Einstein–Hilbert term is literature, not re-checked. |
| GA9-5 | CONDITIONAL | **CONDITIONAL** | Literature (OM5 / ℝ⁵/ℤ₂ fixed points, −½ unit each), not re-checked. "No known object" is a survey statement and cannot rule out an unknown source. |
| GA9 | OPEN (narrowed) | **OPEN** | The narrowing is valid only at the grades listed here. One of the ruled-out items is "{E₈ YM, positive-tension branes}", citing 1120 D-D (given J1, ruled) **and 1142 A13 (unaudited)**; only D-D carries weight (F-6). The demanded O(N) object is still not identified. |
| S4-1 | PROVED | **PROVED** | Chern–Weil: δP(R^k) = kP(DδΓ, R^{k−1}) = d[kP(δΓ, R^{k−1})], using symmetry, ad-invariance and DR = 0. The two-line proof is complete. The machine check is degree-2 su(2) only, reproduced independently (PJ11); the degree-4 case is by hand. Dropping the wall term in δ∫C∧X₈ = ±∫G₄∧Y₇ uses P-b (C_tan odd, so it vanishes at the wall) or the double cover; this should be named (F-7). "Linear in G₄; no E₈ field" refers to the bulk C∧X₈ term only. |
| **S4-2** | PROVED (impl. given P-b/GA2) | **CONDITIONAL** | **Grade move, see §4.** The δ-stress is given only as "∝ T_M2·[G_tan]·(∂X₈/∂R · R³)": no derivation of the boundary term, no coefficient, no test. Its existence and form depend on the wall δ(0)/curvature prescription, which S4-4 lists OPEN. "Split-invariant" needs D-C (CONDITIONAL, as the filing's own text says) and a fixed unbackreacted face, and neither is in the label. Not refuted. |
| S4-3 | CONDITIONAL | **CONDITIONAL** | Premises: the standard C∧X₈ coefficient, J1 scaling, and wall δ(0) ≲ 1/ℓ_P. Given these, the exponents N^{−1}/N⁰ (absolute) and N^{−2}/N^{−1} (relative) are exact (PJ10). "Closes the C∧X₈ OPEN caveat in D-D/A13 at leading order" is CONDITIONAL only and does **not** alter PP 1137's ruled D-D scope wording. "1142 A1's sign bound survives" cites an unaudited item. |
| S4-4 | OPEN | **OPEN** | — |
| A15-1 | PROVED | **PROVED (Israel algebra)** | Same premises as §1. Strengthened by PJ8: any unit e, general symmetric K. "Evade only by flipping the sign of K(ê,ê) − k_t at every point" means NEC-only sources need K(ê,ê) ≤ k_t pointwise in every Y₆ direction. It does not construct or exclude any face. |
| **A15-2** | PROVED (bookkeeping) | **CONDITIONAL** | **Grade move, see §4.** The content is that 1142 A1–A3 transfer "verbatim" to backreacted faces. Those are **unaudited** 1142 results, and PP 1142's audit is in flight and not accepted. A PROVED label cannot rest on them. GB2/P1 is a pointwise identity (PP-verified in the sibling evidence, PG2), and the sibling H2 is PROVED only with its own premises (real-analytic, non-constant W on that face). The negative remark is sound bookkeeping: the A9-T dichotomy and the κ bound do **not** transfer, because they use J1 face data. |
| A15-3 | CONDITIONAL | **CONDITIONAL** | Rests on J1 scaling and J5. "No small parameter" neither constructs nor rules out a backreacted metric. |
| A15 | OPEN | **OPEN** | Needs a backreacted metric (MR2's 1130 lane); none is constructed or ruled out here. |
| Vj | CONDITIONAL | **CONDITIONAL** | As filed, with S4-2 now CONDITIONAL. Junction UNSOLVED. |

**Name collision (disclosed).** In this filing, "J1" is both the premise (1120's J1 end-face/flow data, CLP/BBBW, CONDITIONAL; also the label for the NL 1711 T0 w-values) and the **test ID** J1 (the IR-kept LP certificate) in the script and test map. J0–J9 test IDs are likewise read beside the "given J1" premise. In the sibling gap filing, "J1" is used only as the premise, with the same meaning. No grade changes because of this, but it must be disambiguated (F-4).

## 4. Grade moves
| item | from → to | reason |
|---|---|---|
| S4-2 | PROVED → **CONDITIONAL** | The derivation is a sketch with no computed boundary term, no coefficient and no test. It depends on the OPEN δ(0)/wall-curvature prescription (S4-4). Split-invariance needs D-C (CONDITIONAL) and a fixed unbackreacted face, neither named in the label. Not refuted. |
| A15-2 | PROVED → **CONDITIONAL** | Its content is the transfer of unaudited 1142 A1–A3, and a PROVED grade cannot rest on unaudited inputs. It can be re-filed for upgrade once PP's 1142 audit is accepted by the parent. |

No other moves.

## 5. Ruled tally
**PROVED 5 · CONDITIONAL 7 · OPEN 3 · REFUTED 0 = 15** (NL claimed 7/5/3/0).
- PROVED: GA9-1, GA9-2, GA9-3, S4-1, A15-1.
- CONDITIONAL: GA9-4, GA9-5, S4-2, S4-3, A15-2, A15-3, Vj.
- OPEN: GA9, S4-4, A15.

§1/J8–J9 is counted inside A15-1, as NL does. Standing tallies are unchanged: Bridge C PARTIAL 49/10/5/2/1 + V84 (67 rows); t4436 65/15/5/9/2; NL 1120 22/16/5/2 = 45; parent E₈ 18/2/4/0. 1142 remains unaudited in this write.

## 6. Leftover required fixes (next additive NL erratum; do not edit the frozen filing)
1. **F-1 (priority, S4-2).** Restate as CONDITIONAL with premises P-b, GA2, D-C, a fixed unbackreacted face, and a stated wall δ(0)/curvature prescription. Any future upgrade needs the boundary-term derivation: which G₄ components enter (odd tangential only, or also the even G with a leg along x¹¹), and the coefficient.
2. **F-2 (priority, A15-2).** Restate as CONDITIONAL on the pending PP audit of 1142 A1–A3. Keep GB2/P1 as an identity and the sibling H2 with its own premises. Keep the "does not transfer" remark.
3. **F-3 (GA9-1/GA9-2).** Put the block-averaged source model in the label. Scope "O(N)" and the M5-unit figures (≈ 3253, ≈ 4190) as CONDITIONAL, since they rest on the test targets and J1/J5 scaling.
4. **F-4 (names).** Disambiguate the premise "J1" from the test ID "J1", for example by renaming the tests JX0–JX9 in the next erratum's test map. Do not edit the frozen script.
5. **F-5 (A15-1/§1).** State the Israel convention (Z₂, factor 2/κ²), staticity K_tj = 0, and Poincaré symmetry. Optionally record the general-e / max-eigenvalue form (PJ8).
6. **F-6 (GA9 bullet).** Cite 1120 D-D (given J1) for "{E₈ YM, positive-tension branes}". Label 1142 A13 as unaudited.
7. **F-7 (S4-1).** Name P-b, or the double cover, as the reason the wall term drops in the integration by parts. Say that degree 4 is checked by hand only.

Nits:
- The header says "E26 pending PP confirm". This is stale, not misconduct: the confirm f2e64d44 landed at 11:50:00, before 12:05:46. Do not edit the header.
- The §1 phrase "holds on any face" needs the F-5 premises.

## 7. Custody
**Written (additive only):** this file and its sidecar, the sibling findings, and the shared evidence directory. No existing file was edited, moved, renamed, deleted or chmod-ed.

**Not touched:**
- the frozen 1142, 1120, E26, PP 1137 and E26-confirm files;
- the 1130 script and log (e483f4b1… / bf2484a6…, = sidecars);
- MR2 files and other agents' directories;
- running Local jobs (s1e, chain_v2, s2e, wait_then_ob_v5, any ob_v4).

NL's frozen gapjx files are still mode 444 with unchanged hashes.

**Tip after-write hash:** **7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91**, mode 644, mtime 2026-11-06 14:38:54. It was re-hashed at 12:21:29.006 CST, after the sibling findings and its sidecar were written and immediately before this file's write. Unchanged, and never opened for writing.

Nothing adopted. Junction UNSOLVED. No CERT. Resonant algebra. PP findings.
