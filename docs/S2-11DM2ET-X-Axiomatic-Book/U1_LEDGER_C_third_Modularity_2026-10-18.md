# U1 LEDGER — Modularity status of C_third (modular / mock / quantum modular) — 2026-10-18

Package: `C_third_Modularity_2026-10-18/` (report `2026-10-18-C_third-Modularity.md`, verbatim, scripts and outputs).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim.
(The "Parity Dominance Theorem" — formerly "Theorem L" — is not touched here; Lemma P below is a different, local lemma.)

## Category A
- A1. Identity 2·C_third = q^8 f_{2,7,7}(−q^10, −q^14, q) + 1 + E, checked to q^8000; decomposition C_third = ½(1 − θ₃) + ½ e(7τ/20)[ϑ_hol + E_L]. E built three independent ways.
- A2. **Lemma P (parity splitting).** At every rational x, along q = e(x)e^{−t}: q^8 f, θ₃ and e(7τ/20)ϑ_hol have only half-integer powers of t; E = q^{7/20}E_L has only integer powers t^{−1}, t^0, …. Integer-order data of C_third = those of ½(1+E); half-integer = those of ½q^8 f. Conditional on standard 2-D Euler–Maclaurin and Hecke continuation.
- A3. **Theorem O2 (q^{7/20} phase obstruction).** For Γ of finite index, any finite-dimensional ρ, automorphy factor (cτ+d)^k or |cτ+d|^k, and holomorphic V with V(γτ) = j ρ V + o(1/y) at rationals: C_third ≠ λ·V (also C, P_s, E). Unconditional; uses G(1/m) = e(7/(20m))P(m mod 140)/m for gcd(m,70)=1 (verified for 17 m).
- A4. **Theorem O1 (sign obstruction).** With the holomorphic factor (cτ+d)^k and T^N-finiteness, none of E_L, X = ½(ϑ_hol+E_L), or the 72-component E-vector is λ·V. Hence E is not the holomorphic part of a weight-1 harmonic Maass form, not a holomorphic weight-1 form, not mixed mock with modular factors of weight < 1. Conditional on cited cocycle analyticity (BFOR) and the |x| profile law (checked exactly where used, x = ±1/3).
- A5. **Theorem P (structure).** (i) decomposition; (ii) E_L = Lewis–Zagier f-function of the λ = 1/4 Maass Eisenstein lift, |cx+d| weight-1 cocycle real-analytic off γ^{−1}∞; (iii) Lemma P; (iv) renormalised value c_C(h/m) = ½ + ½e(7x/20)Z_x(0) − (7/20)I·G(x) = α + βI, β = 0 iff 2|m or 5|m; e.g. c_C(0) = 11/20 − (7/20)I, c_C(1/2) = 0, c_C(1/4) = 2 + (3/2)i.
- A6. Verdicts: not modular (Baker E(i), E(ii), O2); not mock/mixed-mock in the stated class (O1, O2); no finite radial limits at all 490 rationals with m ≤ 40; Theorem G zero set re-checked on 1102 rationals (0 mismatches).
- A7. Singular S-law carries |x|: G_{a,0}(−1/x) = Σ_p G_{p,−a}(x)/(√35·|x|) (with signed x the ratio is −1 at every negative x tested). W_7-phase explained by q^{7/20} (108 → 4 distinct phases).
- A8. Baker obstruction E(i) (conditional on Baker 1966 and the q-expansion principle).

## Category B
- The genus formula r_𝒦(N) for all N (checked N ≤ 59 993).
- "No finite radial limit at every rational"; the profile law for all γ, x.
- "No completion of ϑ_hol gives a bounded |·|-cocycle"; the term "quantum modular form" for the |·| factor; the Siegel-theta explanation of |cx+d|.
- Open residual class (§3.4): objects with cocycles of size ≥ 1/y (weight 0 × weight 1 products) are not excluded.

## Cited, not re-checked
Zwegers Cor. 2.9; Hickerson–Mortenson Thm 1.3; Hecke; Baker 1966; q-expansion principle; Lewis–Zagier; Zagier QMF (2010); Bettin–Conrey (2013); BFOR monograph.

## Files not included
`series.npz` (binary), `genus_h_280.pkl`, `radial.pkl` (binary pickles).
