# ERRATUM (Local-derived) to FINDINGS_LOCAL_REVERSE_ENGINEER_GEOMETRY_TO_BRIDGE_C_ALGEBRA_2026-11-10_1124.md (sha 845cc6bc5f590e8f2e4e867ea56ed44eaafee941a8e8a37e313c0aa78c5bdd6b), 2026-11-10, written 11:24 CST (America/Chicago)

The original file is unchanged (additive-only rule). There are two clerical corrections in §4, re-read against `evidence_local_reverse_geometry_2026-11-10/reverse_geometry_check_v3.log` (3344e107…). No grade changes.

1. **§4, the R4a "same failure occurs at …" list.** The list as written includes 113, 137, 193, 233 and 281, where (−7/p) = +1. The correct list is: the primes p ≤ 281 with (−7/p) = −1 at which the Jac(Bolza) Frobenius polynomial over 𝔽_p has a quadratic factor with nonzero trace (directly ordinary), namely **17, 41, 73, 89, 97, 241, 257**. At 19, 59, 83, 131, 139, 227 and 251 ((−7/p) = −1, (−2/p) = +1, p ≡ 3 mod 8) the polynomial is an irreducible quartic x⁴ + c x² + p² with p ∤ c, so the surface is still ordinary there. The proof of R4a uses p = 17 only and is unaffected: **R4a PROVED** (PP audit PENDING).
2. **§0 R4b and §4 R4b, "all 21 ordinary split primes".** Read **12**. These are the primes ≤ 281 with (−2/p) = +1 whose Frobenius polynomial has a quadratic factor: 17, 41, 73, 89, 97, 113, 137, 193, 233, 241, 257, 281. All 12 have a² − 4p with squarefree part −2. The quartic primes (p ≡ 3 mod 8) give no rational quadratic factor and are not counted. **R4b stays CONDITIONAL** (citation).

Tip 7cddb188… not edited. Junction UNSOLVED. No CERT. Nothing adopted.
