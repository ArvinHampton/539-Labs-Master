# Bridge C (s = 7) and the 35-component law vector against RTA: a preregistered bridge map

**For:** Arvin Hampton (539 Labs) · 2026-10-24, about 8:15 AM CDT (America/Chicago).
**Folder:** `reports/bridges/BRIDGE_C_35/` (new files only). `SF/` = `reports/s_family_paths/`.
**Files:** PREREG.md (+ PREREG.sha256, written before any run), RESULTS.md (proofs and data), NOTES.md (problems found and fixed), `scripts/`, `data/`, `logs/`.
**Rules kept:** CORE_FREEZE (H_s not redefined, certifier code untouched; A35 `symbols.py` imported read-only). Category A = proof or exact certificate; Category B = floating point. No TPC or RH claim. Nothing pushed or sent.

## Bottom line
1. **Map A, confirmed (Category A).** The leading radial profile of RTA's Bridge Series C is **not** in the span V of the 35-component law vector: rank 37 > dim V = 36 at all four A51 primes. The obstruction is a single factor: the profile equals I·e(7x/20)·K2_0(x), and **q^{−7/20}·C has profile I·K2_0 ∈ V**.
2. **Map B, confirmed and proved (Category A).** After removing q^{7/20}, RTA's C carries the exact vector-valued S-law of the 35-component law vector at leading order. Explicit formula: Λ_C(−1/x) = I·e(−7/(20x))·(x√35)^{−1}·Σ_{p∈D} e(−B(p,2a))·K3_p(x). The module is V (dim 36) with the exact matrices of ledger entry 94. Proof complete; identity checked exactly at all 216 points.
3. **The numerical side test of Map B on the real series** triggered its preregistered "falsified" rule at 2 of 30 points. A disclosed post-hoc rerun with smaller t passes 10 of the 11 points that had not passed; the 11th is inconclusive. Since Map B is proved, the miss is an underpowered t-grid. It is recorded, not hidden.
4. **Map C (descriptive):** at RTA's four Fricke sample points the leading magnitudes give non-constant ratios to |7x|^{−1/2} (√7, √(7/3), 0, 1). This matches the known scalar obstruction and is not counted as a link.
5. **No map exists from written objects** to the g_k family (including the MIX classes k = 4, 8, 12), T3, O_res or 539. That is a valid negative result.

## 1. Inventory
**Certified on the Bridge C / 35-component side (Category A).**
- A = [[2,7],[7,7]], D of order 35, a = chi_nat(7) = (7/10, −1/5). K2, K3, K4 Gauss-mean families; K1 ≡ 0 (ledger v7 §3, entries 37–42).
- T-law and S-law (entry 39, proof by Poisson summation). dim V = 36 (entry 40; exact source `SF/A35_lawspace_exact/exact_main.json`, not the stale `exact_dim.json`).
- Rank 36 at the 216 rationals at four primes (entry 93; `SF/A51_bridgeC_exact/rank216.json`). Exact M_S⁴ = I and (M_S M_T)³ = M_S² over Q(ζ₉₈₀₀) (entry 94).
- V ≅ E, Hom(V⊗χ^k, C) = 0 (entry 41). spec(C) ⊂ spec(E) (entry 95). End(V) = 1 at s = 7 (A53).
- Zero/magnitude law of the RTA Gauss mean (entry 18). A46/A47 zero facts (entries 77–78, 86–90) and the sign rule (entry 85) are about g_k.
- Refuted: V∘D_7 ⊄ V (A53 Map 1).

**Written on the RTA side.**
- RTA manuscript (`oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md`):
  - T3 and packaging (539 = 3·68 + 5·67; ledger entries 98–100 in `LEDGER_ADDENDUM_T3_2026-10-23.md`);
  - g_s;
  - §9–10: orthant series P_orth, cone series H_7 with c1 = (−1,1), c2 = (−4,1), Bridge Series C = P_orth − H_7, C_axis, chi_nat, C_third;
  - §12: the open weight-1/2 slash.
- Residual-Law note (`reports/heavy-daily/2026-10-17-Bridge-C-Residual-Law.md`): radial asymptotics (A2, proof sketch), Baker obstruction (A3), scalar W_7 obstruction (A5), and the unattempted "vector-valued escape" B3.
- g_k family: ledger v7 §7, entries 73–92. The MIX classes for k ≡ 0 mod 4 are entry 83.
- RTA has no axioms (A18).

**Status of "A52".** The A52 draft was already frozen and run as A53 (2026-10-22), so it was not reused. This report is the new preregistered map set.

## 2. The preregistered maps (plain words)
- **Map A.** "The first-order blow-up of RTA's C at each rational point is one of the functions spanned by the 35-component law vector." Prediction: **no**, because of an extra phase. Test: an exact rank test.
- **Map B.** "Strip the factor q^{7/20} from C. The first-order blow-up then obeys the 35-component law vector's own transformation rule under x ↦ −1/x, with an explicit formula." Prediction: **yes**. Tests: an exact identity at 216 points, a proof, and a numerical check on the actual series.
- **Map C.** "At RTA's four Fricke sample points, the leading magnitudes do not follow a single |7x|^{−1/2} law." This is descriptive only.

## 3. Results
| Map | Verdict | Evidence |
|---|---|---|
| A | **Confirmed** (Category A) | rank [105 components \| G] = 37 at p = 17 657 640 001, 21 189 168 001, 35 315 280 001, 42 378 336 001; G = e(7x/20)K2_0 checked exactly at all points |
| A2 (spectral route) | Not decisive | 0 lies in the formal T-spectrum |
| B | **Confirmed, proved** (Category A) | Theorem 3 + Lemma 2 (RESULTS); exact identity 216/216 at two primes |
| B-radial | Preregistered rule: falsified (2/30 > 10 %); post-hoc smaller t: 10/11 pass, 1 inconclusive | Category B; explained by the t-grid |
| C | Confirmed (descriptive) | ratios 2.6458, 1.5275, 0, 1 |

**Proof outline.** The full proofs are in RESULTS.md.
- *Theorem 1.* Aa = (0, 7/2) gives Q_7(ν) = Q(ν+a) + 7/20. So the RTA mean is G = e(7x/20)·K2_0. The rank 37 then forbids G ∈ V, because reduction mod p cannot raise rank.
- *Lemma 2.* This is a sum–integral comparison on closed sectors where Q is positive definite, with remainder O(t^{−1/2}):
  - the orthant gives I = log(6+√35)/(2√35);
  - the cone series H_7 cancels between K₊ and −K₊, because negation permutes residues mod 2m.
- *Theorem 3.* Combine the S-law (entry 39) and the β-shift rule (entry 37) with A(2a) ∈ Z².

## 4. New Category A facts
These are proposed ledger entries. The ledger itself was not edited.
1. The leading profile of RTA's C is not in V. The profile of q^{−7/20}C is I·K2_0 ∈ V, and it is a cyclic vector of V.
2. A full proof of the radial asymptotics of P_orth, H_7 and C at every rational. This upgrades a written sketch.
3. The explicit leading-order vector-valued S-law of RTA's C, with module V.

## 5. Problems found (details in NOTES.md)
- The RTA manuscript uses P_s for two different series: (−q^s;q^s)_∞ g_s in §7 and the orthant sum in §9. The A52 draft repeats this.
- A52 items 7–8 are wrong as written for C itself. Theorem 1 gives the corrected form.
- Two scripts needed fixes, each made as a new file: a json crash after the results were printed, and a broken post-hoc edit that computed nothing.

## 6. Scope and limits
- The link is at leading order (1/t) only. It says nothing about the t^{−1/2} terms or the coefficients of C.
- It gives no W_7 law: the scalar W_7 law is obstructed (A5), and V∘D_7 ⊄ V (A53).
- Nothing here concerns g_k, T3, 539, Resonant Number Theory, TPC or RH. The Residual-vs-Resonant lock is unchanged.
- The s = 33 / s = 39 sector_exact work stays on hold: it needs more than 3 GB.

## 7. Decision for Arvin
The confirmed link (Map B) says that **q^{−7/20}·C, not C itself, is the RTA object that sits inside the 35-component law vector's module**. Choose one:
- **(a)** Adopt q^{−7/20}C as RTA's normalized Bridge Series and pursue the next order: the t^{−1/2} terms (shadow side), using the 105 shifted and twisted cone series as the vector-valued companion of C. This is the one written direction (Residual-Law B3) still open.
- **(b)** Stop the RNT/RTA bridge search at leading order and fold the three facts above into ledger v8.

The g_k / MIX route would need a new written object linking g_k to Gauss means. None exists today.
