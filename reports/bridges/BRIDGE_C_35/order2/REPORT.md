# Order 2 of the normalized Bridge Series q^{-7/20}·C: the t^{-1/2} terms and the 105-series companion

**For:** Arvin Hampton (539 Labs) · 2026-10-24, about 8:30 AM CDT (America/Chicago).
**Folder:** `reports/bridges/BRIDGE_C_35/order2/` (new files only). PREREG.md sha256 059257db…3f3a599f3fd was written before any run and still matches. Full proofs are in RESULTS.md; problems and deviations are in NOTES.md.
**Rules kept:** CORE_FREEZE; Category A and Category B kept separate; no TPC or RH claim; nothing pushed or sent; the ledger was not edited.

## Bottom line
1. **The t^{−1/2} term is now an explicit, proved formula (Category A).** It covers q^{−7/20}C and each of the 105 companion series S_{α,β} = Σ wt(v)·e(B(α+v,β))·q^{Q(α+v)} (the 35-component law vector's families, with RTA's orthant-minus-cone weight), at every rational. The order-2 coefficient divided by √π is always algebraic: log(6+√35), present at leading order, drops out. The formula reproduces RTA's written constant a_P = 0.5256172043 to 10 digits.
2. **Where the leading term vanishes, order 2 takes over (Category A).** At all 106 tested points with 2 | m or 5 | m (plus RTA's sample image −1/5) the order-2 coefficient is certified nonzero, with minimum 0.1229. There q^{−7/20}C grows exactly like t^{−1/2}.
3. **No vector-valued law at order 2 inside the companion's span (Category B).** Under x ↦ −1/x, with weight 1/2 or 1, the 105 order-2 profiles do not close: rank 138 > 105. The same pipeline reproduces the leading-order closure (rank 36).
4. **Two preregistration errors, both disclosed:**
   - *The Map 1 numerical grid.* It was scaled to the denominator but not to the long cone edge (21,−1), so the preregistered numerical verdict is "falsified". A post-hoc rerun with the right scale matches the formula to 1e−5 at all 9 points tried.
   - *A sign in the Map 3 weight factor.* This made the preregistered control fail, so Map 3 as written is invalid. The corrected convention passes the control.

## Maps, in plain words, and verdicts
| Map | Plain words | Verdict |
|---|---|---|
| 1 | "The second term of the blow-up of the normalized Bridge Series (and of each companion series) at a rational point is given by an explicit finite formula: corner and edge sums with sawtooth weights, plus a drift term." | **Proved** (Category A). Preregistered numerics: falsified by a grid-design error. Post-hoc correct-scale numerics: agree to ≤ 1e−5 |
| 2 | "Wherever the first term is zero, the second term is not." | **Confirmed** (Category A, 106/106) |
| 3 | "The second terms of the 105 companions do not transform among themselves under x ↦ −1/x with one weight." | As preregistered: invalid (control failed, sign error). Corrected: **confirmed** (Category B) |

## Method
- **Decomposition.** RTA's cone region K₊ = {n ≥ 0, n + 21k ≥ 0} is cut into 21 translated orthants in the basis (21,−1), (0,1). This step is exact. Its walls get weight ½, and K₋ = −K₊.
- **Expansion.** On each orthant piece, a two-step second-order Euler–Maclaurin argument with explicit O(1) remainder bounds gives t·Σ = A0 + A1·√t + O(t). The integrals have algebraic closed forms.
- **Checks:**
  - the piece sum reproduces A0 = I·G to 1e−17;
  - the orthant piece reproduces a_P;
  - interval arithmetic at 60 digits certifies nonvanishing;
  - floating-point SVD is used for the closure test.

## New Category A facts (proposed for ledger v8; not entered)
1. The order-2 (t^{−1/2}) expansion of q^{−7/20}C and of all 105 companion series at every rational, with a full proof.
2. A1/√π is algebraic at every rational.
3. A1 ≠ 0 at all 106 tested points of the leading-order zero set, including RTA's sample image −1/5, where |A1| = 0.42859.

## What it means for RTA (descriptive)
- The vector-valued structure found at leading order, the 36-dimensional V, does not persist at order 2 in finite form inside the companion's own span. The order-2 profiles are 105-dimensional and not S-closed.
- This fits the expected quantum-modular / shadow picture of Residual-Law B3. It is not a proof of that picture. The next object would be the period-function correction (the O(1) term, linked to Ξ), which was not attempted.

## Limits
- Map 3 is floating point on 138 points, so it is Category B.
- The O(1) term, Ξ and the period functions are open.
- Nothing here concerns g_k, T3, 539, Resonant Number Theory, TPC or RH.
- s = 33 / s = 39 work stays on hold because of memory.

## Decision for Arvin
At order 2 the 35-component law vector's modular closure is gone, and the only way forward is the shadow route. Choose one:
- **(a)** Go one order further: the O(1) term. Test the preregistrable claim that A1(−1/x) − |x|^{−1/2}·(explicit S-image) equals the value at x of a smooth function on R∖{0}, the period function built from the unary thetas of the wall directions (Q(u) = 1, 7/2, 595/2). This would identify Ξ's role exactly. It is heavier, but within limits.
- **(b)** Stop at order 2 and fold the three new facts into ledger v8, with the leading-order link (parent Theorem 3) as the bridge result.
