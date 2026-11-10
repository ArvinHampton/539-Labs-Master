# FINDINGS (PP): twist modularity for half-integral weight, discharged on F0 for every conductor 2 ≤ r ≤ 30; B3 → PROVED (sufficient reduction); B2 split. 2026-11-10 (America/Chicago)

- **Auditor:** Professor Proof (Soft SF). Owner DIRECT (OW e72a188b, call-83d7a0fa): "resume pursuit; discharge B2/B3 if the math allows".
- **Status:** additive; no earlier file is edited. Nothing is adopted. No CERT. No Gemini. Nothing is sent outside. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 matched before and after.
- **Writes:** only this file and its sidecar in reports/, plus PP scratch /workspace/audit-scratch/pp_discharge_b2_b3/. No PP file is in any Local directory.
- **Jobs not touched:** s1e (932685), ob_v4_6272_D56 (1045533/1045534), chain (1015729).
- **Rule:** OW 3f160803 as amended by 36683379. **Shimura 1973 Lemma 3.6 is not used as a proof anywhere below.**
- **Base:**
  - F0;
  - V5;
  - the weight-½ input Θ1–Θ4 of PP 0f1d3361 §1: θ(τ+1) = θ(τ) and θ(Uⁿτ) = √(4nτ+1)θ(τ) from Poisson summation; j(γ,τ) := θ(γτ)/θ(τ) is evaluated exactly along T/U/−I words with exact winding counts in ℚ(i);
  - PARI only for the consistency check in §4, which is not part of the proof.
- **Convention (as in 0f1d3361):** F ∈ M_{k/2}(Γ₀(L), χ), k odd, means F(γτ) = χ(d)·j(γ,τ)^k·F(τ) for γ ∈ Γ₀(L), together with holomorphy on H and at the cusps; S means cuspidal.

## Evidence (scratch: /workspace/audit-scratch/pp_discharge_b2_b3/, every file has a .sha256 sidecar)

| File | sha256 (first 8 hex) | Content |
|---|---|---|
| umult_core.py | 79ef37b0 | Verbatim lines 1–83 of PP pp_umult_cert.py (2fc9db47): word decomposition, exact J, Schreier generators |
| pp_twist_cert.py | c2af2f99 | Twist multiplier certificate |
| pp_twist_cert_r5_r3.log | (sidecar) | First run, r = 5, 3, plus control |
| pp_twist_cert_r2_30.log | 4f63297b | All r = 2…30, plus control |
| pp_twist_pari_sanity.py / .log | (sidecar) / b62f5880 | PARI consistency check, r = 3 (not proof) |

## 1. Theorem TW(r) (PP)

**Statement.** Fix an integer r with 2 ≤ r ≤ 30. Let N ≥ 1, let k ≥ 1 be odd, let χ be a Dirichlet character mod 4N, and let ψ be a **primitive** Dirichlet character mod r. If F = Σc(n)qⁿ ∈ M_{k/2}(Γ₀(4N), χ), then

  F⊗ψ := Σ ψ(n)c(n)qⁿ ∈ M_{k/2}(Γ₀(4Nr²), χψ²),

and F ∈ S implies F⊗ψ ∈ S. For p ∤ 4Nr and T(p²)F = λ_pF, the Hecke property is T(p²)(F⊗ψ) = ψ(p)²λ_p(F⊗ψ). That eigenvalue algebra is already PP-verified term by term (e28e0fbd B2) and is not reopened here.

**Proof.**

1. **Gauss-sum identity (elementary, F0).** Let ψ be primitive mod r and g(ψ̄) = Σ_{u mod r} ψ̄(u)e(u/r). Then Σ_u ψ̄(u)e(nu/r) = ψ(n)g(ψ̄) for **every** n.
   - If gcd(n,r) = 1, substitute u ↦ un⁻¹.
   - If e = gcd(n,r) > 1, write r = e·r₁. Primitivity gives a unit v ≡ 1 (mod r₁) with ψ(v) ≠ 1. The substitution u ↦ uv leaves e(nu/r) unchanged, so the sum equals ψ̄(v) times itself, hence 0.
   - |g(ψ̄)|² = r ≠ 0.
   - Hence **F⊗ψ = g(ψ̄)⁻¹ Σ_{u ∈ (ℤ/r)^×} ψ̄(u)·F(τ + u/r).**
2. **Coset identity (exact, all of Γ₀(4Nr²)).** Let B_u = [[1, u/r],[0, 1]] and γ = [[a, b],[c, d]] ∈ Γ₀(4Nr²). Put u′ ≡ ud² (mod r) and γ′ := B_uγB_{u′}⁻¹. Then:
   - γ′ = [[a + cu/r, b + (du − au′)/r − cuu′/r²],[c, d − cu′/r]].
   - It is integral because r | c/r and du − au′ ≡ du(1 − ad) = −bcdu ≡ 0 (mod r).
   - c′ = c ≡ 0 (mod 4N), and d′ = d − cu′/r ≡ d (mod 4N), since c/r ≡ 0 (mod 4Nr). So γ′ ∈ Γ₀(4N) and χ(d′) = χ(d).
   - u ↦ u′ is a bijection of (ℤ/r)^×.
   - The certificate (step 4) also checks integrality and B_uγτ = γ′B_{u′}τ exactly, at two Gaussian-rational points, for every generator.
3. **The multiplier ratio is a constant 1-cocycle.**
   - Define ρ_u(γ) := j(γ′, τ + u′/r)/j(γ, τ). Both squares equal ±(cτ + d), because c′ = c and d′ + cu′/r = d. So ρ_u(γ)² is a constant ±1, and ρ_u(γ) is a continuous fourth root of unity on the connected H, hence a constant.
   - From the cocycle property of j and B_uγ₁γ₂B_{u″}⁻¹ = (B_uγ₁B_{u₁}⁻¹)(B_{u₁}γ₂B_{u″}⁻¹), with u₁ = ud₁² and u″ = u(d₁d₂)², one gets **ρ_u(γ₁γ₂) = ρ_u(γ₁)·ρ_{ud₁²}(γ₂)**.
   - So if ρ_u(g) = 1 for every generator g and every unit u, then ρ ≡ 1 on all of Γ₀(4r²), and inverses are covered by the same identity.
   - **ρ involves only θ, not F or N.** A certificate on Γ₀(4r²) therefore covers every Γ₀(4Nr²) ⊂ Γ₀(4r²).
4. **Certificate (pp_twist_cert, exact over ℚ(i)).** For each r = 2, …, 30, every Schreier generator g of Γ₀(4r²) (Schreier transversal for S, T, exactly as in 0f1d3361), every unit u mod r, and two points τ₀ ∈ {1/3 + 2i/3, −2/7 + i/5}:
   - γ′ is integral;
   - **ρ_u(g) = 1 exactly, and is the same at both τ₀.**

   | r | Γ₀(4r²) index | Schreier generators | (g,u) pairs, all ρ = 1 |
   |---|---|---|---|
   | 3 | 72 | 33 | 66 |
   | 5 | 180 | 82 | 328 |
   | 7 | 336 | 166 | 996 |
   | 11 | 792 | 368 | 3680 |
   | 20 | 2880 | 1334 | 10672 |
   | 28 | 5376 | 2475 | 29700 |
   | 30 | 8640 | 3960 | 31680 |

   - All r = 2…30 pass with no exception, no non-integral γ′ and no non-constant ratio; the full table is in pp_twist_cert_r2_30.log. (r = 2 has no primitive character; it is included only as a check.)
   - **Control:** pairing u′ = ud instead of ud² at r = 5 gives a non-integral γ′ in 232 of 328 (g,u) pairs, so the integrality test is not vacuous. The ρ test detecting nontrivial values is the established 0f1d3361 control: (196, 2) gave a j′-dependent ρ on 98 of 166 generators.
5. **Transformation law.** For γ ∈ Γ₀(4Nr²):
   - (F⊗ψ)(γτ) = g⁻¹Σ_u ψ̄(u)F(γ′B_{u′}τ) = g⁻¹Σ_u ψ̄(u)χ(d)j(γ′, B_{u′}τ)^k F(B_{u′}τ) = χ(d)j(γ,τ)^k·g⁻¹Σ_{u′} ψ̄(u′)ψ(d)²F(τ + u′/r).
   - This uses ρ = 1 and ψ̄(u) = ψ̄(u′d⁻²) = ψ̄(u′)ψ(d)².
   - Hence (F⊗ψ)(γτ) = χψ²(d)·j(γ,τ)^k·(F⊗ψ)(τ).
6. **Holomorphy and cusps (E-cusp, as in 0f1d3361 §2.5).** F⊗ψ is a finite combination of translates of F.
   - If y^{k/4}|F| is bounded on H (cusp case), so is y^{k/4}|F⊗ψ|, and the form is cuspidal.
   - In the M case, polynomial growth of every F|ξ at each cusp is preserved by the same finite combination, so F⊗ψ is holomorphic at the cusps.

**Scope and leftover.**
- TW(r) is PROVED for **2 ≤ r ≤ 30**, all N, all odd k, all χ, and all primitive ψ mod r.
- **General r stays CONDITIONAL (T-twist-general).** The argument is uniform in r except step 4, the finite certificate; the identity ρ ≡ 1 for arbitrary r is not proved here.
- Imprimitive ψ is not covered, because step 1 needs primitivity.

## 2. B3 → PROVED, as an implication (sufficient reduction only)

**Statement.** Let ψ₅ be either character of order 4 mod 5. It is primitive, since 5 is prime and ψ₅ ≠ 1, and ψ₅² = χ₅ = (·/5).

Suppose G ∈ S_{3/2}(Γ₀(4M), χ_D), for **any** M ≥ 1 and quadratic χ_D, satisfies T(p²)G = χ₋₄(p)a_p(f)G for p ∤ 4M. Then:
- H := G⊗ψ₅ ∈ S_{3/2}(Γ₀(100M), χ_Dχ₅) by TW(5);
- T(p²)H = ψ₅(p)²χ₋₄(p)a_p(f)H = χ₋₂₀(p)a_p(f)H = a_p(f_Ξ)H for p ∤ 20M;
- H ≠ 0 ⇔ c_G(n) ≠ 0 for some 5 ∤ n;
- the rational combination (G⊗ψ₅ + G⊗ψ̄₅)/2 has the (1, −1, 0) pattern.

The arithmetic is carried from e28e0fbd: conductor of f⊗χ₋₄ is 784, and with M = 784, 100M = 78400.

**Grade: B3 PROVED**, as an implication. It is a **sufficient reduction only**: the existence of G is not claimed (O-b stays OPEN), and the converse is not claimed.

## 3. B2: split

- **B2 [2 ≤ r ≤ 30]: PROVED** (TW(r) plus the PP-verified eigenvalue algebra). It covers the one instance any Bridge C row uses, r = 5 (B3). B2′ needs no modularity.
  - No row uses r > 30: a ψ with ψ² ∈ {χ₋₂₀, χ₁₄₀} does not exist (B1), so the conductor-20 and conductor-140 cases never arise.
- **B2 [general r]: CONDITIONAL [T-twist-general]**, with the condition named above. This is not a citation of Lemma 3.6; it is an uncertified finite identity for each r > 30.
- **B2′:** PROVED, unchanged and not reopened.

## 4. Consistency check (PARI base; not part of the proof)

- Take F = Kc[1] ∈ K ⊂ S_{3/2}(Γ₀(196), χ₂₈) and ψ = χ₋₃ (primitive mod 3, ψ² trivial on units).
- F⊗ψ lies in the span of S_{3/2}(Γ₀(1764), χ₂₈) (dim 146): rank 146 → 146, and an exact combination exists, on n ≤ 700. That is past the Sturm bound 504 = (3/2)·4032/12, so **with membership certified by TW(3)** this is an identity of forms.
- It also confirms that the certificate's convention matches PARI's χ(d)j³ convention at a new level.

## 5. Rollup (Bridge C)

- **Before:** 47 PROVED · 11 COND · 5 OPEN · 2 REF · 1 PENDING + V₈₄ (66 rows).
- **Ruled, with B2 split into two rows:** **49 PROVED · 10 COND · 5 OPEN · 2 REF · 1 PENDING + V₈₄ (67 rows).**
  - B3 COND → PROVED.
  - New row B2[r ≤ 30] PROVED.
  - B2[general] stays COND.
- **If the B2 row is kept unsplit:** **48 · 10 · 5 · 2 · 1 + V₈₄ (66 rows)**, with B2 COND [T-twist-general] and the r ≤ 30 range noted in the row.
- **CONDITIONAL (10):** E9, E11a, 3b-i, 3b-ii(b), N1, 3d, N2, O-a, A4, B2[general].
- **OPEN (5):** O-b, O-c, H₊U, Λ₀, P11.
- **REF (2):** 3b-ii, 2f.
- **PENDING (1):** B5. D = 28 at 6272 has joint kernel 0 (PROVED sub-result); D = 56 is running as ob_v4.
- Nothing is adopted. Bridge C stays PARTIAL.

## 6. For Local (priority: true; additive)

1. Split B2 as in §3, or keep one row with the r ≤ 30 scope. Retag B2 from "Shimura 1973 Lemma 3.6" to **TW(r), PP 2026-11-10**. For r > 30, use COND [T-twist-general].
2. B3: PROVED (sufficient reduction only); cite TW(5).
3. Use the rollup in §5.
