# order47 PREREG: exact certification of the order45 matrix identities (written and hashed before the run)
Ring: Z[ζ], with ζ = e(1/9800), L = 9800 (the exponent ring of S_rows; M_jk = Σ_{e∈S(j,k)} ζ^e).
Π: the monomial matrix Π_{j,π(j)} = ζ^{g_j}, where (π(j), g_j) = reduce(α_j, −β_j) (the map (α,β) ↦ (α,−β)). Complex conjugation acts by ζ^e ↦ ζ^{−e}.
## Identities
X1: conj(M)·Π·M = 35·Π. X2: M·M^† = 35·I, where M^† = conj(M)ᵀ.
(X1 is equivalent to conj(kM)Π = Π(kM)^{−1} given X2, with k = 35^{−1/2}.)
## Exact method (fixed)
- Each entry of the left-hand side minus the right-hand side is formed as an integer coefficient vector c ∈ Z^{9800} on ζ^e, by exact exponent addition mod 9800 (products of monomials).
- Zero test in Z[ζ]: since 9800 = 70·140 and Φ_9800(x) = Φ_70(x^140), the elements x^r·y^i (r < 140, i < 24, y = x^140) form a Z-basis of Z[ζ] (degree 140·24 = 3360 = φ(9800)).
- An element Σ c_e ζ^e is zero iff, for every r mod 140, the integer polynomial Σ_q c_{140q+r} y^q reduced modulo Φ_70(y) (monic, integer, exact division) is 0.
- All arithmetic is integer (Python int); there is no floating point in the verdict.
PASS (each identity): all 105² entries are zero exactly. FAIL: any nonzero entry; the count of nonzero entries is reported.
Controls: (a) exact check of M² = 35·P with P = Γ_{−I} (known; validates the machinery); (b) a deliberately wrong identity (M·M^† = 34·I) must FAIL.
## Consequence (fixed now)
If X1 and X2 PASS, then with fact (i) (C2b(−x) = conj(Π·C2b(x)), proved: conjugate the summand, real B2 weights, reduction rules) the order45 identity follows:
R(1/x) = −x^{−1}·conj(Π(kM)^{−1}R(x)), where R(x) = C2b(−1/x) − x·k·M·C2b(x).
Hence ‖R(1/x)‖ = ‖R(x)‖/x is Category A, and v11 is drafted. The proof uses only X1, X2 and (i); the same argument applies verbatim to every real-weight Bernoulli sum (C2a, C11, A2_corner). The v11 statement is written for real-weight sums in general.
Naming: RG* only, no labels L1–L7; "36" only as dim V. MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim.
