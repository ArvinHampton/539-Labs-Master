# order55 RESULTS (local modular sources only; no non-local QM / EH-11D / reverse-parity PT / simulated-physics objects used)
## RG45c-2′ (PREREG.md sha 0cbb763f…fe22): FAIL as preregistered
254 cases (XS[:6] × j∈{0,5,…,100} × 2 walls + 2 order54 worst), t_k = c_k·π²/(40·Q(u_j)·P*²), c=(1,½,¼).
250/254 ≤ 6.8e−9; 4 wall-2 cases (x=1/13,1/12,1/11 j=50; 1/12 j=85; all θ2∈Z) miss by ≈1.5e−2. Control FAIL(good) (0.335, 52 endpoint cases). data/rg45c2p.json, logs/rg45c2p.log.
Post-hoc (logs/posthoc_j50*.log): miss is t-independent (identical at c=1,¼,1/16) and equals EXACTLY the one-sided B̄1(0)=−½ prediction. Cause: evaluator formed θ2 in float (3/5+21·29/35 → 18.000000000000004), so sgn(z)≠0 on the λ=0 line. Numerics defect, not formula.
## RG45c-2″ (PREREG_b.md sha 30adcc9b…ffd6, hashed before run; only change: exact λ=0 detection): PASS
Same 254 cases, same bar: worst rel err 6.8e−9 (wall 1), 2.5e−14 (wall 2); 0 errors; control FAIL(good) (max dev 0.335 on 52 endpoint cases).
⇒ A1(R_j) = √(π/Q(u_j))·Σ_{r<P} m_r·B̄1((r+θ_j)/P) with midpoint B̄1(0)=0 is CONFIRMED (Category A-numeric) on the preregistered sample; endpoint convention numerically tested (one-sided convention refuted). data/rg45c2pp.json.
## Ξ_compl := Σ_j A1(R_j) (order51's missing "t^{-1/2} coefficient of the completion term") is now explicit and confirmed.
## RG46: SKIPPED — obstruction documented (not invented around)
Forming A1 − Ξ_compl against order2/order3 A1 (parts.npz) needs the identification of order2's cone weight with the Zwegers sign. Written sources disagree in a way not resolved in writing:
- order2 lib2: H-weights ½(sgn n + sgn(n+21k)) on INTEGER v (walls through v=0, sgn0=0);
- completion (order5/51/54): sgn of ν-forms, ν=α+v, labels θ1=α1, θ2=α1+21α2 (e.g. θ2=18, θ1=4/5 occur).
H_v − H_ν is a finite strip of wall lines contributing O(t^{−1/2}); its sign/orientation bookkeeping, and the S-law target (weight / multiplier for the completed t^{−1/2} coefficient; order3b closure criterion is the candidate test) are not written. Choosing them now would be inventing. Ξ: not identified. Bridge: NO.
## Phase-aware k≠0 bound: not written; Open.
## Open next (order56)
(a) Write (Category A) the H_v→H_ν strip correction from order2 PIECES/WALLS + order52 orientation (−c1,c2); then Â1 := A1 − [strip] − Ξ_compl is forced.
(b) Prereg RG46: order3b rank-closure of Â1 at w∈{½,1} over XS (216×105), A0 gating control; match to v12 local shadow Ξ (order13/15 unary thetas 5n²/2, R²/34, 35m²/4) as Category B.
(c) k≠0 phase-aware bound.
## Note 2026-10-24 (America/Chicago; Auditor hygiene, additive): Primary preregistered verdict is RG45c-2′ = FAIL (PREREG.md). RG45c-2″ PASS is a post-diagnostic PASS only (PREREG_b hashed after the RG45c-2′ FAIL and diagnosis); it does not replace the primary verdict. No numeric claims changed.
