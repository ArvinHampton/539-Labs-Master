# MR2 FINDINGS — DUAL CONTINUE — coefficient check n ≤ 5311: depth exactly 2 for 7.4.a.a (Path A) — 2026-10-26
STATUS: PARTIAL (MR2 lane). The Path A depth claim is proved below for Auditor Soft SF. Dual-label: filtration 10∥40 BOTH NAMED PARALLEL, NO PICK. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED, no OMS / PS #20. No tip fold. tip_touched NO.
Builds on ckw49 ffde8a16… (SF-E1), theta49-gap eaa124ca…, sturm49 18ec8e93…. Script: MR2-coeff5311.sage (1.7 s wall). No M₁₁₃₈ space was constructed and no weight-1138 Sturm run was done.

Method (light path, no weight-1138 space):
- f = q·∏(1−qⁿ)³(1−q⁷ⁿ)³ · θ_Q, with Q = x²+xy+2y². Here η³(z)η³(7z) ∈ S₃(Γ₀(7), χ₋₇) (eta-quotient criteria) and θ_Q ∈ M₁(Γ₀(7), χ₋₇). The product lies in S₄(Γ₀(7)), which has dim 1, and its leading coefficient is 1, so it equals f = 7.4.a.a (PROVED). It also agrees with the Sage basis to q⁵⁹ and gives a₇ = −7.
- The eta cubes were computed by the Jacobi identity ∏(1−qⁿ)³ = Σ(−1)^m(2m+1)q^{m(m+1)/2}, with precision 5320.

Soft SF facts:
- SF-F1 (PROVED, computational): a_n(f) ≡ n¹³σ₁₉(n) (mod 49) for ALL n with 1 ≤ n ≤ 5311 and 7∤n. Failures: 0, n_checked = 5311.
- SF-F2 (PROVED, elementary): every 7|n coefficient vanishes mod 49 on both sides. On the f side, f^{[7]} = f − a₇V₇f, and since U₇f = a₇f with multiplicative coefficients, a_{7m}(f^{[7]}) = a₇a_m − a₇a_m = 0. On the other side, n¹³ ≡ 0 mod 49. Both constant terms are 0.
- SF-F3 (PROVED): ckw49 SF-E1 puts f^{[7]}E₆^{189} and a lift of θ¹³G₂₀ in M₁₁₃₈(Γ₀(49), Z_(7)) (Chen–Kiming Thm 1(i)). Sturm bound = 5311. Their coefficients agree mod 49 for n ≤ 5311 by F1 and F2. Hence f^{[7]} ≡ θ¹³G₂₀ (mod 49) for all n, so a_p(f) ≡ p¹³+p³² (mod 49) for every p ≠ 7. DEPTH ≥ 2 PROVED.
- SF-F4 (PROVED, finite witness): this fails mod 343 at n = 2 (also at 3, 4, 5, 6, 9, …). Since f is fixed and the (1,3) system p¹³+p³² is fixed, depth ≠ 3.
- SF-F5: with F3 and F4, the depth of the (1,3) Eisenstein-shadow congruence of 7.4.a.a is EXACTLY 2, relative to the stated system p¹³+p³² mod 7^k. This upgrades SF-B3 from NUMERICAL to PROVED, subject to Auditor Soft SF.

Scope caveat: "depth" here means the congruence with this specific θ¹³σ₁₉ system. It is not a claim about all possible mod-343 Eisenstein-type systems.
Does NOT use: filtration pick, L₇ unit, abs-irr BM, OMS lift. Not folded into tip.
