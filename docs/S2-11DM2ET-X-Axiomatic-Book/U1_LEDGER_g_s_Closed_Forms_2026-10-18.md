# U1 LEDGER — g_s closed forms (Theorem G_s), P_s / Θ_hol coefficients for all s, cusp onset — 2026-10-18

Package: `g_s_Closed_Forms_2026-10-18/` (report is a Master copy with cross-references to unpublished local folders removed; mathematics unchanged; scripts and outputs verbatim).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim.
Label note: the report calls the g_s result "Theorem G". To avoid a clash with Theorem G of the Bridge-C consolidated paper (zero set of the Gauss mean), Master and the rev2 paper call it **Theorem G_s**. No collision with L1–L7.

## Category A
- **Theorem G_s.** g_s(q) = Σ_{n≥0} q^{n²}/(−q^s;q^s)_n (Master contact 23). For every real s > 0, g_s(e^{−t}) ~ Σ_k c_k(s)t^k with c_k ∈ Q[s] of exact degree k; no t^{−1} and no half-integer terms. c₀ = 2, c₁ = 2(s−3), c₂ = 5s² − 44s + 75, c₃ = (55s³ − 930s² + 3918s − 4683)/3, c₄ = (1073s⁴ − 28864s³ + 214620s² − 593128s + 545835)/12; c₅..c₈ in `prove_gs.txt`. ζ_g(0) = 1, ζ_g(−1) = 6 − 2s, ζ_g(−k) = (−1)^k k! c_k(s). Elementary proof with explicit remainder bound (`prove_gs.py`, all PASS). Pre-registered (sha256 8da9d9a6cab2cb1fd16c545e8660803b5eb3d50d81f033d7267cee9df9ac1794; c₀, c₁ disclosed as not blind) and confirmed on held-out s.
- P_s and Θ_hol through t¹ for all s ≥ 3 (modulo cited 2-D Euler–Maclaurin): P_s t^{−1} = Res/2, t^{−1/2} = √π(s² − 2√(2s))/(4s(s−2)); Θ_hol t^{−1/2} = √π(s²/2 − 2s + √(2s))/(s(s−2)) and no integer-order terms through t¹; Res = arccosh(s−1)/√(s(s−2)). Lemma P at x = 0 holds as an identity in s.
- Identities for all s ≥ 3: 2P_s = E_s + 1 + θ₃ − Θ_hol; P = R + (1+θ₃)/2; C_third = P_s + Θ_hol − θ₃; q⁸f = Θ_hol − θ₃.
- g_s ∉ span_Q{1, θ₃, R, Mm} (exact rank 4 → 5 to q⁴⁰⁰, s = 3..20, 25, 30, 41).
- H_s (M = [[2,s],[s,s]], c₁ = (−1,1), c₂ = (−4,1)) is Zwegers-admissible only for integer s ≥ 5.
- Cusp-onset counts h⁺ vs genera (cross-checked with PARI): onset at s = 11, 19, 25, 41 in the tested range; s = 11 has 4 genera (corrects the s8/s11 report).
- All radial data at x = 0 (ζ_E, Res, P/Θ coefficients, c_k(s)) are s-uniform and blind to the class group.

## Category B
- "h⁺ ≠ #genera ⇔ cusp part"; predicted cusp parts at s = 19, 25, 41.
- Dirichlet-series reading of ζ_g (polynomial growth of coefficients not proved).
- Higher radial coefficients of H_s (hence of C = P_s − H_s) in s: not computed (open).
- A recorded failed guess (lc_k = Li_{−2k}(½)/(4^k k!)) is reported as failed.

## Files not included
`gs_coeffs.pkl`, `PTh_coeffs.pkl` (binary); the pre-registration text and its .sha256 (held locally; the hash is recorded above).
