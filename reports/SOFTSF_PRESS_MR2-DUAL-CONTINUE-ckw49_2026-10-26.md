# SOFTSF_PRESS — MR2 FINDINGS — DUAL CONTINUE — θ-mod-7² hypotheses audit for 7.4.a.a vs θ¹³G₂₀ (closes named gap (ii) of theta49-gap) — 2026-10-26
STATUS: PARTIAL. Dual-label: filtration 10∥40 BOTH NAMED PARALLEL, NO PICK. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED, no OMS / PS #20 retry. No tip fold. tip_touched NO.
Builds on theta49-gap eaa124ca… and sturm49 18ec8e93…. Light script: MR2-ckw49-light.sage (1.1 s). No Sturm k=1138 run.
Literature added to lit/: 1301.3087 (Chen–Kiming, "On the theta operator for modular forms modulo prime powers", Mathematika 62 (2016) 321–336) and 1105.1918 (Chen–Kiming–Wiese, CKW).

CORRECTION (Soft SF): theta49-gap SF-D2 credited the weight shift k ↦ k+2+2p^{m−1}(p−1) to "Chen–Kiming–Wiese". The correct source is Chen–Kiming 1301.3087, Thm 1. CKW 1105.1918 has no θ-operator theorem; it covers strong/weak/dc-weak eigenforms and level-lowering (Prop 2, Thm 5: p≥5, p∤N, abs-irr residual). The weight value k+86 = 1138 is unchanged.

Exact hypotheses, Chen–Kiming Thm 1(i):
p ≥ 5. M_k(N, Z/p^m) := M_k(Γ₁(N), Z) ⊗ Z/p^m, the classical integral-structure definition. θ: M_k → M_{k+k(m)}, with k(m) = 2+2p^{m−1}(p−1), acts by Σa_nq^n ↦ Σna_nq^n and preserves cusp forms. The paper assumes p∤N throughout. The authors remark that (i) and (ii) "hold with the same proofs even if p | N"; only (iii) (optimal filtration) uses p∤N. No N ≥ 4 or N ≥ p hypothesis is in Thm 1(i). N ≥ 5 shows up only for the Katz-forms comparison, which we do not use.

Hypothesis table:
- H1 p ≥ 5: p = 7. MATCH.
- H2 level N prime to p, for applying θ: θ is applied ONLY to G₂₀ at N = 1. MATCH. θ is never applied to f or f^{[7]}, so the p | N remark is not needed.
- H3 input is an integral classical form: G₂₀ = −B₂₀/40 + Σσ₁₉(n)qⁿ, B₂₀ = −174611/330, v₇(B₂₀/40) = 0 (Sage). So G₂₀ ∈ M₂₀(SL₂Z, Z_(7)). MATCH.
- H4 output weight: θ¹³G₂₀ ∈ M_{20+13·86}(1, Z/49) = M₁₁₃₈(1, Z/49), with q-expansion Σn¹³σ₁₉(n)qⁿ. MATCH (Thm 1(i) iterated 13 times, m = 2). Pulled back to Γ₀(49) by inclusion of levels: MATCH.
- H5 the f side needs no θ: f^{[7]} = f − a₇V₇f, a₇ = −7 (Sage). It lies in M₄(Γ₀(49), Z), has integral coefficients, and is classical. MATCH. Weight lift: E₆ ≡ 1 (mod 7) (min v₇ of the E₆−1 coefficients is 1), so E₆^{7} ≡ 1 (mod 49). Checked to q³⁰⁰, and in fact proved by (1+7x)^7 ≡ 1 mod 49. Hence f^{[7]}·E₆^{189} ∈ M₁₁₃₈(Γ₀(49), Z) is ≡ f^{[7]} mod 49. MATCH.
- H6 Sturm mod 7² with Z_(7) coefficients, both forms in M₁₁₃₈(Γ₀(49)): standard (apply Sturm mod 7, divide by 7, apply Sturm mod 7 again). MATCH. Bound = 5311 at Γ₀(49). The Γ₀(196) / bound-31864 route in theta49-gap is NOT needed, because H2 holds at N = 1 without any N ≥ 4 condition.
- H7 residual abs-irr / CKW Thm 5 level-lowering: NOT USED. The route is a pure q-expansion comparison, so this hypothesis is irrelevant. (Not OPEN, not FAIL.)
- H8 θ commuting with T₇ (Thm 1(ii), case ℓ = p needs k ≥ m): not needed. MATCH/NA.

Soft SF facts:
- SF-E1 (PROVED, literature + arithmetic): Named gap (ii) of theta49-gap is CLOSED. Every hypothesis needed for "f^{[7]}E₆^{189} and a classical lift of θ¹³G₂₀ both lie in M₁₁₃₈(Γ₀(49), Z_(7)) and agree mod 49 iff their coefficients agree for n ≤ 5311" is MATCH, from Chen–Kiming Thm 1(i) at N = 1 together with H3, H5 and H6.
- SF-E2 (PROVED, correction): the θ weight shift is credited to Chen–Kiming 1301.3087, not CKW. The relevant Sturm bound is 5311 (Γ₀(49)), not 31864.
- SF-E3 (PROVED, Sage): a₇(f) = −7, v₇(B₂₀/40) = 0, E₆^{7} ≡ 1 mod 49.

REMAINING NAMED GAP (only one left): coefficient check a_n(f^{[7]}) ≡ n¹³σ₁₉(n) mod 49 for 7∤n, n ≤ 5311. For 7|n both sides are ≡ 0 mod 49 (n¹³ ≡ 0; f^{[7]} has no 7|n coefficients). Currently verified only for n ≤ 500 (SF-D3). Exact depth = 2 is NOT promoted. Once that check is done, depth ≥ 2 follows, and depth ≠ 3 is already proved (mod 343 fails at n = 2).

Path C addendum: not required. CKW-hypothesis facts number 3 proved, above the threshold of 2.
Does NOT use: filtration pick, L₇ unit, abs-irr BM, OMS lift. Not folded into tip.
