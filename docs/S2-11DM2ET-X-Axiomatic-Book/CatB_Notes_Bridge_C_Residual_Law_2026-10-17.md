CATEGORY B NOTES
Bridge Series C residual law, 2026-10-17
Every item in this file is CATEGORY B (observed, numerical, heuristic or interpretive) or OPEN. Nothing here is a lock.
Companion to U1_LEDGER_Bridge_C_Residual_Law_Obstruction_2026-10-17.md (Cat A).
Source (verbatim copy). Bridge_C_Residual_Law_2026-10-17/.

Caveats. No HQCC, TPC or RH claim. Residual is not Resonant (539 is a count). CORE_FREEZE untouched.


B1. |G| pattern (observed only)
- |G(h/m)| = 1/m for gcd(m,70) = 1, m > 1, and G(h/m) = 0 when 2 | m or 5 | m: observed for m < 30 (fricke_profile.txt). Not proved.
- For x = h/7, G = (h/7)_Legendre * i/sqrt7 (since Q_s = n^2 mod 7).
- Proposed proof route: Gauss-sum multiplicativity over the mod 2, 5, 7 and coprime parts. Not done.

B2. Vector-valued 35-component law (OPEN)
- Over the 35 characteristic components (Zwegers Cor. 2.9(5) shape), the leading profiles G_mu(x) are expected to transform by the weight-1 Weil representation of the level-70 lattice. A vector-valued leading-order law is therefore expected, for the singular parts only; the cone sums themselves stay non-modular by the Cat A additive obstruction. Not attempted. This is the only route the obstructions leave.

B3. Shintani cone decomposition (heuristic)
- P_s is a cone-restricted norm-form theta of Q(sqrt35). Its Mellin transform Gamma(s) sum_{(n,k)>=0, !=0} Q_s(n,k)^{-s} is a Shintani-type cone zeta with residue I = log eps/(2 sqrt35) at s = 1.
- A natural candidate "law" is a Shintani/Hecke cone decomposition rather than a false theta.
- Not checked: whether the orthant is a union of unit-group fundamental domains. The automorph [[-1,-7],[2,13]] sends (1,0) to (-1,2), not to (0,1).

B4. t^{-1/2} coefficient of C (fit only)
- About 0.8174 from a numerical fit. Not derived analytically (H_s walls are not axis-aligned). Needed to extend the quotient obstruction for C to complex coefficients.
- Fit values for reference: 1/t coefficient of C 0.20961; P_s and C_third t^{-1/2} coefficients 0.52569 / -0.52575 (predicted +-0.525617); t*H_s fit -0.0002.

B5. Sample coincidence (not evidence)
- |sample(1)| = 20.90 is close to I/(2t) = 20.89 at rho = 0.995. Noted only as a numerical coincidence.
- Direct values C(0.995 e(x)) at x = 1/7, 3/7, 5/7, 1: 4.58+18.92i, 3.40-18.24i, 4.27-19.46i, 54.01; G*I/t gives 15.79, 15.79, 15.79, 41.78; Master samples -18.2+7.8i, 0.3-1.8i, 2.1-9.0i, 20.7+2.9i.

B6. Real-quadratic interpretation
- The remainder of C is "weight-1-sized" at q -> 1 with a regulator (log of the fundamental unit of Q(sqrt35)) as coefficient, reminiscent of the class-number formula.
- Classical reason unsigned real-quadratic norm-form thetas are not holomorphic modular: weight-1 Eisenstein series need odd characters, while zeta_K = zeta * L(chi_35) is even. Interpretation only.


OPEN
- Vector-valued law (B2). Proof of the |G| pattern (B1). Analytic t^{-1/2} coefficient of H_s / C (B4). Shintani decomposition (B3). Prescription behind the Master Fricke samples (unrecovered).

Hygiene. CATEGORY B throughout. No HQCC, TPC or RH claim. CORE_FREEZE untouched.
