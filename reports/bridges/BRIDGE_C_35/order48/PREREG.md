# order48 PREREG: predictions of v11 Theorem xinv for other real-weight sums (written and hashed before numerics)
Prediction (from the proof; blind for these objects): R_Y(1/x) = −x^{−1}·conj(Π(kM)^{−1}R_Y(x)) for Y ∈ {C11, C2a, C2b, A2_corner (CO)} (stored order18/19 arrays). The theorem's hypothesis covers each of these.
Contrast object: A2_lines (LN). Its line weights involve the sign/orientation data of the order16 line formula; whether they are real and β-independent is not asserted, so the result is reported only, with no prediction.
Pairs: all x ∈ XS with 1/x ∈ XS and x > 1 (paired with 1/x).
Data: Y(x) and Y(−1/x) are both stored at grid points, so R_Y(1/x) uses the stored values at the point 1/x. No new evaluation.
PASS per object iff max over pairs of ‖R_Y(1/x) − pred‖/‖R_Y(1/x)‖ ≤ 1e−10. FAIL iff ≥ 1e−6.
Naming: RG* only, no labels L1–L7. MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim.
