# order55 PREREG_b — RG45c-2″ (written & hashed after RG45c-2′ FAIL and its post-hoc diagnosis; before this run)
Diagnosis (post-hoc, logs/posthoc_j50*.log): the 4 RG45c-2′ misses (all wall 2, θ2∈Z) equal EXACTLY the one-sided-convention prediction; cause: direct sum computes θ in float (3/5+21·29/35 → 18.000000000000004), so sgn(z) ≠ 0 on the λ=0 line. A numerics defect in the evaluator, not in A1_pred.
Change (only): in direct, lam = (l + θ) is formed exactly (θ as Fraction; lam = l + num/den with λ=0 detected exactly, sgn set to 0 there). Everything else (sample of 254 cases, t schedule, Richardson, PASS bar 1e−6, gating control) IDENTICAL to PREREG.md (sha 0cbb763f…fe22).
RG45c-2′ verdict stays FAIL as preregistered; RG45c-2″ is a separately labelled rerun.
