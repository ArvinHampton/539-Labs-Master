# order54 RESULTS
PREREG sha256 af2e5c10…1404 (PREREG.sha256), hashed before tests. Script sha in SHA256SUMS.
## RG45c-1: PASS, Category A (source audit)
The written sources force the endpoint convention h(0) = 0. This is the midpoint convention, B̄1(0) = 0. The sources are:
- order5 PREREG: "sgn 0 = 0", and E = erf(√π·) is odd.
- order5 zwegers.py uses np.sign.
- order18 a2.py defines B1b(0) = 0.
Nothing is invented. Explicit sketch: A1(R_j) = √(π/Q(u_j))·Σ_{r<P} m_r·B̄1((r+θ_j)/P), with γ = ½ and EM jump −2 already folded in.
## RG45c-2: FAIL as preregistered (numeric). The failure is a regime problem, not evidence against the formula.
- Wall 1 (u1, Q = 7/2):
  - Every endpoint case (θ+r ∈ Z, m_r ≠ 0; 222 cases in total) matches to ≤ 7.7e−16.
  - The one-sided control is off by up to 0.40, so it fails as the PREREG requires.
  - The non-endpoint cases miss by up to 0.19 (relative).
- Wall 2 (u2, Q = 595/2): the largest miss is 1.39. Only 18 of 630 cases pass.
- Overall: worst relative error 1.39 against the 1e−6 threshold. Verdict: FAIL. data/rg45c.json, logs/rg45c.log.
- POST-HOC diagnosis (logs/posthoc_diag.log; not a verdict):
  - The preregistered t-grid {4,2,1}e−3 is not asymptotic. The Poisson remainder along a line is about exp(−π²/(t·Q(u)·P²)), and P reaches 28 or more. With wall 1 at t = 1e−3 that is about e^−3.6.
  - Worst wall-1 case: at t = 1e−4 the mismatch drops to 3.7e−16, matching the formula exactly.
  - Worst wall-2 case: the mismatch goes 0.97 → 0.95 → 0.18 at t = 1e−3, 1e−4, 2e−5. The wall-2 condition is t ≪ π²/(297.5·784) ≈ 4e−5.
  - So both the formula and the h(0) = 0 endpoint are supported. A rerun needs a new PREREG with t scaled per case to the Poisson scale.
## RG46: SKIPPED. A1(R_j) is a t^{−1/2} coefficient. It is not an explicit Ξ_compl or A1−Ξ_compl object, and nothing links it to the v12 shadow Ξ.
Ξ: unidentified. Bridge: NO.
## Phase-aware k≠0 residual bound: not written; left Open.
Open next:
(a) order55: preregister a rerun of RG45c-2 with t_k = c_k·π²/(40·Q(u_j)·P_j²). Wall 2 needs about 1e5 lines × 500 terms, so use a reduced, preregistered sample and/or apply Poisson analytically along the lines.
(b) Then try matching Σ_j A1(R_j) to the v12 Ξ, and run RG46 only if an explicit object results.
(c) The k≠0 bound.
