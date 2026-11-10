# order49 RESULTS: LN real-weight hypothesis
PREREG sha256 03e63b84c882e1db8b3f326981e7d6aee8e589448fcbe744f7638ec758499129 (hashed before certification).
- H1 code audit: β and x enter lines() only through ph() and period(). PASS (0 offending lines).
- H2 exact: phase(α,−β,−x) ≡ −phase(α,β,x) mod M (integer identity; checked on 105 pairs × 4 x × 169 points). PASS.
- H3 exact: reduce(α,−β) keeps α exactly for 105/105 companions. The pointwise ratio is constant (exact integers). PASS.
- H4: periods are invariant under k ↦ −k + c. PASS (structural).
**Verdict: PASS, Category A.** LN, and therefore A2 = LN + CO, satisfies Y(−x) = conj(ΠY(x)), so the x↔1/x theorem extends to them.
Paper: the v11 hypothesis ("Σ_r f_r w_r") did not cover the line terms, so the statement had to change. A thin v12 was drafted: papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v12.pdf (hypothesis widened to real-linear functionals Λ; v11 untouched).
Open next: residual smallness. It is still open and blocked by the order46 obstruction; no written non-fitted prediction exists.
