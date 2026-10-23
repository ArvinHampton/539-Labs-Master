# A52: draft preregistration, Bridge C (s = 7) to Residual Ternary Algebra (RTA)

**For:** Arvin Hampton · 2026-10-22, evening (CDT) · **Status: DRAFT ONLY.** Nothing was run, hashed or finalized. New files only, in `SF/A52_bridgeC_to_RTA_draft/` (`SF/` = `reports/s_family_paths/`). Deliverable: `prereg_draft.md`. Lock in force: RTA and Resonant Number Theory stay unmixed. No TPC or RH claim.

## 1. What RTA is (found)
RTA is defined by one manuscript (`oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md`). Its objects: the three-branch map T3, the packaging arithmetic (539 = 18 + 521 = 3·68 + 5·67), the series g_s and P_s = (−q^s;q^s)_∞ g_s, and the Bridge C series C := P_s − H_s with C_axis, chi_nat, C_third. Its one named open item is the exact weight-1/2 slash prefactor under W_7: x ↦ −1/(7x).
**There are no axioms**: no arity-3 operation, no grading, no identity (A18 confirms; this search agrees). So "Bridge C constrains RTA" can only mean "Bridge C constrains RTA's objects or its open item".

## 2. What Bridge C exactly gives
- The S-law and T-law for the leading 1/t profiles of cone sums, and an exact module V (dim V = dim E = 36) with V ≅ E untwisted and Hom(V⊗χ^k, C) = 0 for all k. So the 35-component law vector lives in E and never touches the 6-dimensional C-summand.
- Derived here by hand, not machine-checked: RTA's series sees the characteristic a = chi_nat(7) (since Q_s = Q(ν+a) − Q(a), Q(a) = −c0). V is irreducible, so RTA's leading profile is a cyclic vector for V: closing it under the modular group needs all of V. And S, T permute the three characteristic blocks (K2-type, K3-type, K4-type) through SL2(Z/2) ≅ S3, so the Z/3 from R = ST is the cyclic order of three characteristic classes (mod 2), which explains why it is balanced everywhere and is not 3-adic.
- Limits: leading profiles only; nothing on t^{-1/2} terms, coefficients of g_s, T3 or 539. The scalar W_7 slash is already obstructed (Residual-Law A5), but that does not decide a vector law.

## 3. Candidate maps (details, data, criteria in `prereg_draft.md` §4)
1. **Map 1, vector-valued Fricke closure (sharpest).** H1: for each of the 105 component functions f of the three families, x ↦ f(7x) lies in V (equivalent to V|W_7 ⊂ V). New: never tested; it is the only structure with RTA-facing content (RTA's open slash). Data: exact Gauss means at the 216 rationals and four primes of A51; no RTA coefficient data. Falsifier: rank of [F | F7] above dim V at any prime (Category A refutation). Confirmation (rank = dim V everywhere) is evidence only until a closed form is proved. Controls: dilations by the 24 other primes up to 97. One confirmatory test, α = 0.05, minimum attainable p = 1/25 = 0.04. My prior: closure fails.
2. **Map 2, transport to RTA's s-family (generic by design).** For odd s in {5, 9, …, 25}: dim V_s = 3·G(s(s−2)) = d_Eis, S,T-closure, V_s ≅ E_s, Hom(V_s⊗χ^k, C_s) = 0. New for s ≠ 7; non-vacuous at s = 9, 15, 21, 25 (non-squarefree discriminant). Exact (Category A) where certified, inconclusive otherwise (declared). Universal statement, no p-value. A pass cannot single out s = 7, 8, 11, T3 or 539.

## 4. Assessment
- **Sharpest: Map 1.** It targets RTA's own named obstruction, is new, needs no RTA coefficient data, has an exact refutation, and both outcomes are informative. Most likely result: a clean negative (no vector Fricke law inside V), which closes that branch. Map 2 is mechanism-backed and likely true, but it extends Bridge C rather than linking it to RTA.
- **Not admitted (and why):** T3 digits to Z/3 (abelian version is equidistributed by ledger entry 47; non-abelian version is the A28/539 numerology); axis/third/mixed to R-eigenspaces (the profile is entirely in C_third, the grading is balanced; Category A obstruction); {−1,0,+1} to E/C (no structure; the Legendre factor comes from Q_s ≡ n² mod 7 and is shared by everything built on Q_s); any use of the A42 target set R or packaging integers (retired M1 to M3).
- **Not claimable:** that Bridge C "is the key" to RTA; any link to Resonant Number Theory; any role for the C-summand in RTA (Hom = 0 says the law cannot see it); any tie of Z/3 or {−1,0,+1} to E/C; any statement about g_s coefficients, T3, 539, or the Master Fricke samples (not radial values of C). What is supportable today: RTA's Bridge C series has a leading profile that is a cyclic vector of an irreducible Eisenstein-type module isomorphic to E (items derived above need a machine check first).
- **Corrections noticed:** the C series is ternary-valued only through degree 101 (first coefficient 2 at q^102); "C" names three different things across the corpus (the cusp summand, the Bridge C series, the s = 7 setting), so the draft names them separately.

## 5. Questions for Arvin
1. Is the 2026-08-24 manuscript the full definition of RTA? If you have an axiom set (an arity-3 operation and identities), please send it; every map above would then need rewriting against it.
2. Which {−1,0,+1}-valued data do you mean: sgn g_s(d), the Legendre factor in G(h/7), or something else?
3. The manuscript says s in {7, 8, 11} are "selected by packaging arithmetic". Is there a derivation? I did not use that selection as a target, because 7 and 11 divide 539 and the A42 maps M1 to M3 were retired on that pattern.
4. Do you approve Map 1's fixed choices: weight convention |7x|^{-1}, the 216 points, the four A51 primes, the 24 prime controls, and "closure is evidence only until proved"?
5. Is Map 2 worth running (it is generic) before Map 1, or only after?
6. Do you want even s (s = 8) handled? The ledger has no d_Eis formula there, so it would be descriptive only.

## 6. Files
- `prereg_draft.md`, `REPORT.md`, `REPORT.pdf`, `mk_pdf.py`.
