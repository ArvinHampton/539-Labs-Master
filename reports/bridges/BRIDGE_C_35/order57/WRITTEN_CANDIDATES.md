# order57 WRITTEN_CANDIDATES — local-modular written-formula hunt (no invention, no prereg, no tests)
Date 2026-10-24 (America/Chicago). Addendum; AUDIT.md / AUDIT_CORPUS.md untouched. order58 untouched.
Book dir abbreviated BK = oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/ . v12 = reports/papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v12.pdf (sha256 d2fda41b…fd95653), cited by theorem number / pdftotext line.

## 1. P̂_orth / even-corner completion (local) — ABSENT as a completion; FOUND: explicit local even-corner COEFFICIENT plus a written no-go
- FOUND (coefficient, not completion). v12 Thm 39.3 (line ~7380): order-t^0 radial coefficient of the even corner
  A2(S^E)/2 = Σ_r f_r [ B̄1(ρ1/N) B̄1(ρ2/N) + ½ B2(ρ1/N) + (7/4) B2(ρ2/N) ] =: A2^corner,
  where B̄1(u)=u−½ on [0,1), B2(u)={u}²−{u}+1/6. v12 Thm 39.4: A2 = A2^lines + A2^corner, "the completion terms contribute nothing at order t^0".
  §39.1 / Prop 39.8: C2(x)=N² Σ_{k mod N} c_k G_{α,β+λ_k}(x), c_k = (1/N) Σ_{j=0}^{N−1} B2((α2+j)/N) e(−k(α2+j)/N) = Σ_{n≡k(N),n≠0} e((n−k)α2/N)/(2π²n²), with a written S-image formula for C2(−1/x).
- FOUND (no-go). v12 Prop 39.5: if a2(−1/x)=x·35^{−1/2}M a2(x)+cM a0(x) then P a2 = −a2; "A2 − A2^lines satisfies such a law on Q^× only if it vanishes." Remark 39.7 (Cat B): fails at 216 points, residual 54.4.
- ABSENT: any written local P̂_orth. v12 §41 Problem 1: even-corner term "admits no affine weight-one law (Proposition 39.5)". Φ_orth (v12 §37.5) is non-local arc-integral — excluded. Pre-09-01 Zwegers orthant completion (Transformation_Law_CLOSED_2026-08-20.md:12) WITHDRAWN by BK/Executive_Summary_2026-09-01_P_TL.md:19 and NCR-C.

## 2. Explicit Ξ series — FOUND (written in Arvin's book; v12 and prior audits say "not explicit")
- BK/Continue_Resolution_Residual_Shadow_Xi_2026-08-23.md:16–24:
  Ξ = Ξ_even + Ξ_odd; Ξ_even = Σ_{m≥0} outer_even_coeff(m)·Θ_{3/2}(·; a=7m); Ξ_odd = Σ_{m≥0} outer_odd_coeff(m)·Θ_{3/2}(·; a=7m+7/2); Θ_{3/2}(·;a) = Σ (n+a) q^{(n+a)²} "(or its residual χ-twisted analogue)".
- Outer series stated: BK/U1_LEDGER_P_XI_Eichler_TermByTerm_Obstruction_2026-09-02.md:18–20:
  Even (m≥1): 35m²+7m = 42,154,336,588,…; Odd (m≥0): 35m²+42m+49/4 = 12.25,89.25,236.25,…
- Coefficient table: BK/Residual_Coefficient_Tables_and_Fricke_Probe_C_2026-08-23.md:25–37 (deg:coeff) 24.5:3.5, 32.5:4.5, 42.5:5.5, 43:1, 54.5:6.5, 58:2, 67:3, 68.5:7.5, 78:6, 84.5:8.5, 91:7, 102.5:9.5, 106:8.
- Ridge: BK/Per_off_Xi_Term_Table_Listed_Ridge_2026-09-02.md:10–11: N_n = n²+7n+24.5, c_n = n+7/2 (= (n+7/2)² + 12.25, i.e. outer_odd(0) acts as a q-EXPONENT shift, not a multiplier).
- Eichler kernel: h(x) = ψ(x)/√i − ∫_path Ξ(w)(w−x)^{−1/2} dw (Continue_Resolution…:44).
- CAVEATS (must go to Physicist): (a) "outer coeff" values behave as exponents per the ridge table — written text is internally ambiguous; (b) "or its χ-twisted analogue" leaves Θ_{3/2} not uniquely fixed; integer entries 43,58,67,78,106 marked "partial"; (c) Ξ is attached to Θ_third (C_third), NOT to the P_orth even corner; (d) not withdrawn by NCR-C (post-09-01 notes 09-02 and 09-21 still cite it) but BK/Executive_Summary_2026-09-02_P_Xi.md:8–12 proves term-by-term identification with C_axis / Θ_third periods FAILS (half-integer ridge ∩ integer supports = ∅); (e) Pack+(S) "residual discrete" provenance, H7 erf-completion constants (v12 §41 P1) not derived.

## 3. k≠0 residual / phase-aware bound — ABSENT
- Searched orders 42–56, v12 §39, BK. Negative quotes: order55/RESULTS.md:15 "Phase-aware k≠0 bound: not written; Open."; order50/RESULTS.md:6 "(R1) a written tail bound … Open next".
- Nearest written: order50/PREREG.md:16 sketch "c_k = Σ_{n≡k} e(·)/(2π²n²) (tail ≤ Σ 1/(2π²n²))" — trivial modulus bound, not phase-aware, never tested. v12 §39.1 gives the exact c_k Fourier form above (no bound stated). order42/NOTES.md:2 records k=0 vs k≠0 cancellation only.

## 4. Axis false thetas Q=1, 7/2 — no completion (ABSENT); FOUND: written remainder/asymptotic formulas
- Completion ABSENT: order6/RESULTS.md:10 "no completion on H; they are quantum modular", shadows Σ n e(n²τ) (n∈α1+7α2/2+Z), Σ n e(7n²τ/2) (n∈α1+α2+Z) [argument sketch]. BK/Advancements_Wrap_2026-09-21_QM_Theta_C_Axis.md:20 "Unary QM of C_axis stays unwritten. M2 does not fire."
- FOUND (radial remainder, written, Cat A in v12): Thm 35.6 ray terms per half-line direction u:
  A1^ray = (√π / (2√Q(u))) · mean(f),  A2^ray = −mean(f)·l/(2Q(u)) − Σ_{b<N} f(b) B1(b/N),  A0^ray = 0;
  Thm 39.4 line terms A2^lines apply this "to each half-line" (w± weights, finite-part δ, point terms h1h2). Prop 35.11: R[7/2] collects rays ±N(0,1).
- FOUND (exact unary decomposition): v12 Prop 37.12 (a)/(b): half-lines are partial thetas with Eichler partners Σ w e(w²τ) and Σ m′ e((7/2)m′²τ).
- Axis series itself: BK/C_Axis_Pairing_and_Natural_Characteristic_2026-08-23.md:45 C_axis = 3/2 + Σ_{n≥1} q^{n²} + Σ_{k≥1} q^{7k(k+1)/2}.
- These are radial asymptotic remainders, not a quantum-modular cocycle/remainder h_γ; whether that counts as an "accepted remainder" is a Physicist call.

## GATE_PACKET (citation + formula only)
G1 Ξ: BK/Continue_Resolution_Residual_Shadow_Xi_2026-08-23.md:16–24 + U1_LEDGER_P_XI…2026-09-02.md:18–20 + Residual_Coefficient_Tables…2026-08-23.md:25–37. Ξ=Σ_m outer_even(m)Θ_{3/2}(·;7m)+Σ_m outer_odd(m)Θ_{3/2}(·;7m+7/2), Θ_{3/2}(·;a)=Σ(n+a)q^{(n+a)²}, outer_even=35m²+7m (m≥1), outer_odd=35m²+42m+49/4; odd ridge N_n=n²+7n+24.5, c_n=n+7/2. (Ambiguities a–b above.)
G2 even corner t^0: v12 Thm 39.3/39.4: A2^corner = Σ_r f_r[B̄1(ρ1/N)B̄1(ρ2/N)+½B2(ρ1/N)+(7/4)B2(ρ2/N)]; Prop 39.5 no-go for weight-one law.
G3 axis remainder: v12 Thm 35.6: A1^ray=√π/(2√Q(u))·mean(f); A2^ray=−mean(f)l/(2Q(u))−Σ_{b<N}f(b)B1(b/N); Q(u)∈{1,7/2}.
G4 c_k Fourier (input for any future k≠0 bound; no bound written): v12 §39.1 c_k=Σ_{n≡k(N),n≠0} e((n−k)α2/N)/(2π²n²).
