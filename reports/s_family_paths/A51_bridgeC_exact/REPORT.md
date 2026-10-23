# A51: Bridge C (s = 7), an exact certificate for the law space

**For:** Arvin Hampton (539 Labs) · 2026-10-22, about 6:15 PM CDT.
**Folder:** `reports/s_family_paths/A51_bridgeC_exact/` (new files only).
- Scripts: `rank216.py`, `sl2_exact.py`, `mk_pdf.py`.
- Outputs: `rank216.json`, `sl2_exact.json`, `intertwiner_rerun.json` (a rerun of A35's `exact_intertwiner.py` with output written here).

**Ground rules.** CORE_FREEZE: H_s was not redefined and no certifier code was touched. A35 `symbols.py`/`orbits.py` and A's `weil_family.py` were imported read-only. **Cat A** = proved, or a computer certificate in exact arithmetic (exact rational/cyclotomic arithmetic, or mod-p ranks used only as one-sided bounds). **Cat B** = floating point.

## 0. Audit of ledger v6, entries 32–42
- **The float-only claim.** "105 functions at 216 rationals from three candidate readings span a 36-dimensional space closed under S and T, matching E" comes from A33, where the values were evaluated in floating point (Cat B). A35 replaced it with a *different* exact certificate: 48 rationals with m ≤ 6, two primes. **The 216-point claim itself had never been certified exactly. §1 does that now.**
- **Entry 40, lower bound: citation fix.** The ledger cites `exact_dim.json` for "rank 36 at p = 1 764 001, 6 468 001". That file is stale: it records an earlier run at p = 823 201 and 5 174 401 with 36 points and **eval rank 30**. The rank-36 result at the cited primes is in **`exact_main.json`** (`eval_points` 48, `eval_rank` 36). The mathematics is sound; only the file reference is wrong.
- **Entry 40, closure under S and T.** The S-law (entry 39) is proved by Poisson summation. The closed-form M_S and M_T are exact symbol reductions (`symbols.py`), so this part was already Cat A. The SL₂ relations on V had been checked **mod p only** (two primes). §2 now checks them exactly.
- **Entry 41.**
  - The Hom vanishings are exact: each mod-p dimension is an upper bound for the char-0 dimension, so a mod-p result of 0 proves 0.
  - X·S_V = S_E·X was already exact (reduction modulo Φ₅₈₈₀₀). I reran it here: 0 of 1296 entries fail.
  - The diagonal scalars c_i were *found* in floating point and then *verified* exactly. All 36 are roots of unity ζ₅₈₈₀₀^e (every k = 0), which matches the ledger wording.
- **Entries 32 and 36** (A32): mod-p upper bounds plus an exact cyclotomic verification. Cat A as stated.
- **Entry 42** (K1 ≡ 0): a proof. Cat A.

## 1. The 216-point span claim, now exact (Cat A)
- **Points.** The 216 rationals x = h/m with 1 ≤ m ≤ 15, 1 ≤ h ≤ 3m and gcd(h, m) = 1. This is A33's set: 3·Σ_{m≤15} φ(m) = 216.
- **Functions.** All 105 components K2_μ, K3_μ, K4_μ, μ ∈ D, of the 35-component law vector.
- **Method.**
  - Each G_{α,β}(h/m) is an exact finite mean over a 4m × 4m box, with integer phases mod 9800m. Its value lies in Z[ζ_{9800m}][1/(4m)²].
  - Each value was reduced to F_p via ζ ↦ a primitive Lev-th root of unity, where Lev = lcm_{m≤15}(9800m) = 3 531 528 000. The rank of the 216 × 105 matrix was computed with FLINT `nmod_mat`.
- **Primes** (all ≡ 1 mod 3 531 528 000): p = 17 657 640 001, 21 189 168 001, 35 315 280 001, 42 378 336 001.
- **Result.** The rank is **36 at all four primes**.
- **Why this gives an exact answer.**
  - *Lower bound.* Reduction is a ring homomorphism, so rank can only drop: the char-0 rank is ≥ 36.
  - *Upper bound.* The 12 automorphs give 36 orbits, so the rank is ≤ 36 (proved; entry 40).
  - So the evaluation at the 216 points has **rank exactly 36 = dim V**. Restricted to these 216 points, the 105 functions already separate V.

## 2. Exact closed-form M_S and M_T on V, and the SL₂ relations (Cat A)
- **Set-up.** Work in Z[ζ₉₈₀₀], reducing modulo Φ₉₈₀₀ (degree 3360) with integer coefficients (`sl2_exact.py`). In the basis of the 36 orbit representatives:
  - G_S = √35·M_S has entries that are sums of e(k/9800);
  - M_T is monomial with unit-root entries (checked).
- **√35 inside the field.** √35 = −i·Σ_a (a/35)·ζ₃₅^a, since 35 ≡ 3 mod 4. Checks: (√35)² = 35 exactly, and its numerical value is +5.91608, so this is the positive root.
- **Exact identities verified, all 1296 entries each:**
  - G_S⁴ = 35²·I, i.e. **M_S⁴ = I**;
  - (G_S·M_T)³ = **+√35**·G_S², i.e. **(M_S M_T)³ = M_S²** (the −√35 version fails);
  - G_S²/35 is monomial (a signed permutation, i.e. charge conjugation).
- **Conclusion.** M_S and M_T define an honest SL₂(Z)-representation on V over Q(ζ₉₈₀₀). This upgrades A35's mod-p relation check to exact.

## 3. Intertwiner V ≅ E (Cat A, rerun)
- **Construction.** X = P_E·Π·diag(c)·P_V⁻¹ over Q(ζ₅₈₈₀₀), with c_i = ζ^{e_i}.
- **Exact checks:**
  - P⁻¹P = I on both sides;
  - the T-spectra match eigenvalue by eigenvalue;
  - X·S_V = S_E·X with **0 of 1296** entries failing modulo Φ₅₈₈₀₀;
  - the E/C block is exactly zero.
- **Conclusion.** X is invertible, so **V ≅ E with no twist** (exact).
- **Hom vanishing (from A35, exact upper bounds at p = 1 764 001 and 6 468 001):** Hom(V⊗χᵏ, C) = Hom(C, V⊗χᵏ) = 0 for all k ∈ Z/12. So no χᵏ-twist of the 35-component law vector reaches C.

## 4. The remark spec(C) ⊂ spec(E), checked against A32 (Cat A)
- **Method.** Exact T-exponents on ρ₇|W were taken from `WFam` (A32's construction, exponents mod 29 400). Each 1- or 2-cycle of the monomial T gives eigenvalues e(s/2) and e(s/2 + 1/2).
- **spec(C)** = {19, 31, 59, 111, 131, 139}/140. This matches A45's reading of A32's `results.json`.
- **spec(E):** 36 distinct values, exactly equal to spec(V).
- **spec(C) ⊂ spec(E): true (exact).** So ρ₇|W has 36 distinct T-eigenvalues, 6 of them doubled, and T alone cannot separate C from E. The separation comes from S (entry 32: End(ρ₇|W) = 2).
- **Proposed ledger sentence (for entry 32 or 41):** "spec(T|C) = {19, 31, 59, 111, 131, 139}/140 ⊂ spec(T|E), and T|E has 36 distinct eigenvalues (exact; A51)."

## Now exactly certified (summary)
| Item | Status |
|---|---|
| Rank 36 of the 105 functions at A33's 216 rationals | **Cat A** (new; 4 primes, plus the proved upper bound) |
| Closed-form M_S, M_T on V over Q(ζ₉₈₀₀); M_S⁴ = I, (M_S M_T)³ = M_S² | **Cat A** (new; exact cyclotomic, previously mod p only) |
| dim V = dim E = 36, closure under S and T | Cat A (A35; reconfirmed) |
| V ≅ E, explicit intertwiner over Q(ζ₅₈₈₀₀) | Cat A (A35; rerun, 0/1296 failures) |
| Hom(V⊗χᵏ, C) = 0 for all k | Cat A (A35, mod-p upper bounds) |
| spec(C) ⊂ spec(E) | **Cat A** (new exact check) |

## Remaining gaps and caveats
- **Ledger fix needed.** Entry 40 should cite `A35_lawspace_exact/exact_main.json`, not the stale `exact_dim.json` (which shows rank 30 from an older 36-point run).
- **No character-0 value table.** The Gauss-mean values themselves were never written out in full cyclotomic form. The rank certificate goes through reduction, which is rigorous as a lower bound.
- **The c_i in X were found numerically.** This does not affect rigour, because X was then verified exactly.
- **Scope.** As in A35, the S-law covers the leading radial profiles (the 35-component law vector) only.
- **Upper bound for dim V.** It uses the 12 automorphs found with |entries| ≤ 40. That is enough for the bound; no claim is made that this is the full image of O(A) on D.
