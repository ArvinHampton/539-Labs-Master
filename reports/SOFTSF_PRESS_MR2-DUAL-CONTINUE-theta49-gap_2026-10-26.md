# SOFTSF_PRESS — MR2 FINDINGS — DUAL CONTINUE — θ¹³E₂₀ mod-49 comparison for 7.4.a.a (Path A, θ-cross-weight) — 2026-10-26
STATUS: PARTIAL. Dual-label: filtration 10∥40 BOTH NAMED PARALLEL, NO PICK. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED, OMS lift not tried again. No tip fold. tip_touched NO.
Builds on sturm49 18ec8e93… (SF-C1–C3). Scripts: MR2-theta49-light.sage (run, N≤500); MR2-theta49-7.4.a.a.sage (full Sturm run, KILLED on Physicist override, no result).

Soft SF facts:
- SF-D1 (PROVED, elementary): p¹³+p³² = p¹³(1+p¹⁹) = p¹³·σ₁₉(p). So the (1,3) depth-2 system is the a_p-system of θ¹³E₂₀, with E₂₀ the level-1 Eisenstein series where a_n = σ₁₉(n). This is the θ-twisted Eisenstein shadow. It is not a classical finite-order Eisenstein, which matches SF-C2.
- SF-D2 (PROVED, arithmetic): θ^m for m≥2 kills coefficients at 7|n mod 49. The same holds for the 7-depletion f^{[7]} = f − a₇·V₇f (level 49). Mod 49 we have E₆^{7}≡1, so E₆^{189}≡1 (weight 1134 = 27·42). With the Chen–Kiming–Wiese weight shift of θ mod 7² (k ↦ k+2+2·7·6 = k+86), θ¹³E₂₀ has formal weight 20+13·86 = 1138. Also 1138−4 = 1134 ≡ 0 (mod 42), so f^{[7]}·E₆^{189} has weight 1138 and is ≡ f^{[7]} mod 49. Sturm bounds at k=1138: Γ₀(49) is 5311; Γ₀(196) is 31864. Γ₀(196) is the safe level if CKW needs N≥4 prime to 7.
- SF-D3 (COMPUTATIONAL, finite): a_n(f) ≡ n¹³σ₁₉(n) (mod 49) for every n ≤ 500 with 7∤n (Sage, 0 failures). The depth is not 3: mod 343 it fails first at n=2 (also at 3, 4, 5, 6).

NAMED GAP (exact depth = 2 NOT Soft SF-proved): rigour needs (i) the q-expansion check up to the Sturm bound for k=1138 (5311 at Γ₀(49) / 31864 at Γ₀(196)); this run was killed as infeasible on this box. It also needs (ii) the CKW θ-theorem hypotheses (level prime to 7 and N≥4, then lifting to level 49 after depletion) checked in writing. Iterating Sturm mod 7 → mod 7² on the integral difference is standard. SF-B3 therefore stays NUMERICAL, now backed by the θ¹³E₂₀ framing and the explicit weight and bound.

Does NOT use: filtration pick, L₇ unit, abs-irr BM, OMS lift. Not folded into tip.
