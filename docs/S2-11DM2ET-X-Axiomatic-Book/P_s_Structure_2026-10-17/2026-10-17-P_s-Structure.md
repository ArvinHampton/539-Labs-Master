# Exact structure of the orthant series P_s (the shared remainder of Bridge C and C_third)
Date: 2026-10-17, 20:47–21:40 CDT. Master tip 48684e3 (unchanged). Read-only throughout; box only.
No Heavy, no Grok, no pushes, no emails. Scripts and outputs: `2026-10-17-P_s-structure/`.
Scope: this is separate from HQCC. Nothing here bears on TPC or RH. CORE_FREEZE holds.

P_s(q) = Σ_{n,k≥0} q^{Q_s(n,k)}, with Q_s = n² + 7nk + (7/2)k(k+1) (Master `Residual_Bridge_Series_C_Definition.md` l.15, l.29).
Notation:
- ε = 6+√35 is the fundamental unit of Q(√35); N(ε) = +1.
- I = log ε/(2√35) = 0.209419820314714631473…

## Verdict
**PARTIAL STRUCTURE (exact), with sharpened obstructions. No closed modular identity for P_s exists in the classes tested.**

1. **Exact decomposition (Cat A, proved; checked to q^3000):**
   **2·P_s = E + 1 + θ_3 − Θ_hol**
   - θ_3 is a weight-1/2 modular form.
   - Θ_hol is the Zwegers weight-1 indefinite-theta holomorphic part from the earlier report.
   - **E is the generating function of one narrow ray class 𝒦 of Q(√35):** E(q) = Σ_{𝔞∈𝒦} q^{(N𝔞+7)/20}.
   - Geometrically, E is the sum of q^{Q_s} over one fundamental domain for the unit ε, acting as the automorph γ = [[−1,−7],[2,13]].
2. **Full radial structure (Cat A).**
   - E(e^{−t}) has an expansion in **integer powers of t only**, with **rational** coefficients after the explicit e^{−7t/20} shift. These come from Hecke partial-zeta values. The residue is log ε/(20√35) and **ζ(0,𝒦) = 1/10 exactly**.
   - Every half-integer power in P_s comes from θ_3 and Θ_hol.
   - The constant and t^{−1/2} coefficients of P_s, C_third, H_s and C are now closed forms (§A3).
   - This **upgrades obstruction 2 for C to Cat A** over ℂ.
3. **Vector-valued route.**
   - The leading (1/t) radial profiles of the 36-component family obey the **exact weight-1 Weil law**, S and T together (Cat A, finite exact check).
   - With quadrant cones the law **fails at order t^{−1/2}** (Cat A, finite computation).
   - With fundamental-domain cones (the E-vector) there is **no** t^{−1/2} term. The order-t^0 S-cocycle ψ(x) is **nonzero but numerically smooth**, which is **evidence for a renormalized weight-1 quantum modular structure** (Cat B).
   - An exact vector-valued modular law is impossible (Baker; Cat A).
4. **Gauss-mean pattern: PROVED (Cat A).**
   - G(h/m) = 0 if 2 | m or 5 | m.
   - |G(h/m)| = 1/m if gcd(m,70) = 1.
   - |G(h/m)| = √7/m if 7 | m and gcd(m,10) = 1.
   - Checked on all 3374 coprime pairs with m ≤ 105.

---

## Category A

### A1. Automorph group and the orthant (`structure.py` → `structure.txt`)
- **Completing the square.** Q_s(v) = Q2(v+a) + 7/20, with Q2(x,y) = x² + 7xy + (7/2)y² and a = (7/10, −1/5). Verified symbolically.
- **Reflections.** In ν = v + a coordinates, let ρ1 = [[1,7],[0,−1]] and ρ2 = [[−1,0],[2,1]].
  - Both are integral reflections (det −1) preserving Q2.
  - ρ1 fixes the ray ν2 = 0; ρ2 fixes the ray ν1 = 0. These are the two walls of the open quadrant C0 = {ν1>0, ν2>0}.
  - γ = ρ2ρ1 = [[−1,−7],[2,13]] has eigenvalues 6±√35, i.e. γ ↔ ε.
  - **Coset behaviour:** ρ1 and ρ2 swap a+Z² with −a+Z², while γ preserves a+Z². All checked symbolically.
- **Consequences.**
  - C0 is a Weyl chamber of ⟨ρ1,ρ2⟩ acting on the positive sector S+.
  - **C0 ∪ ρ2C0 is a fundamental domain for ⟨γ⟩ on S+.**
  - Coset points never lie on the walls, because ν1 ≡ 0.7 and ν2 ≡ 0.8 mod 1.
- **The pieces in lattice terms.** C0 ∩ (a+Z²) is {n ≥ 0, k ≥ 1}, so its sum is R = P_s − Σ_{n≥0}q^{n²}. Because ρ2 swaps the cosets, the ρ2C0 part of coset a equals the (−C0) part, i.e. C_third + Σ_{n≥1}q^{n²}. Hence:
  - **E := R + C_third + Σ_{n≥1} q^{n²} = Σ_{v: v+a ∈ F} q^{Q_s(v)}**, for any γ-fundamental cone F = [r, γr) ⊂ S+.
  - This was verified exactly to q^3000 for r = (1,0), (1,1), (7,−1), (1,2). So E is a γ-orbit sum.
  - **E_{−a} = E_a** (exact to q^3000). The Hecke sign-twisted partner E_a − E_{−a}, which is the holomorphic weight-1 Hecke form in Zwegers' c2 = γc1 setup, **vanishes identically** for this coset. So E has no modular "odd companion".
  - **Odd part:** R − (C_third + Σ_{n≥1}q^{n²}) = −Θ_hol (exact).
  - Adding the two gives **2P_s = E + 1 + θ_3 − Θ_hol** (exact to q^3000).
- **Remark.** This answers the open question in the earlier report (B2). The orthant minus its k=0 row is exactly half of a unit-group fundamental domain. The two halves are swapped by ρ2, which also swaps a ↔ −a.

### A2. E is a ray-class partial theta (algebraic proof; formulas in `structure.txt`)
**Setup.** Put (X,Y) = 10ν ∈ (7,−2) + 10Z² and β = (2X+7Y) + Y√35 ∈ Z[√35]. Then:
- Q2(ν) = N(β)/400 (symbolic check).
- β(γν) = ε·β(ν) (symbolic check).
- β runs over β0 + 10𝔭2, with β0 = −2√35 and 𝔭2 = (2, 1+√35) = Z·2 + Z(7+√35), the ramified prime over 2.
- ν ∈ S+ ⟺ β ≫ 0.

**Ideal-theoretic translation.** Let 𝔡' = gcd((β0), 10𝔭2) = 𝔭2²𝔭5 and 𝔣 = 𝔭2𝔭5.
- Then 𝔞 := (β)𝔡'^{−1} runs over the ideals α·𝔭7 with α ≡ 1 mod^× 𝔣 and sgn α = (−,+).
- That set is **one ray class 𝒦 modulo 𝔣∞1∞2**, containing 𝔭7·(α1) for any such α1.
- The totally positive units ≡ 1 mod^× 𝔣 are exactly ε^Z, since ε ≡ 1 mod 𝔭2 and mod 𝔭5. So γ-orbits correspond bijectively to ideals in 𝒦.
- Since N𝔞 = 20Q_s(v) − 7:
  **E(q) = Σ_{𝔞∈𝒦} q^{(N𝔞+7)/20}**,  so E(e^{−t}) = e^{−7t/20} Σ_{𝔞∈𝒦} e^{−tN𝔞/20}.
- Sanity check: the first exponents give norms 13, 73, 133 = 7·19, 153 = 9·17, 173, …, all ≡ 13 mod 20, with 3 inert and 13 and 17 split.
- Status: Cat A as algebra. The bookkeeping was done by hand and the key identities were checked symbolically. Standard inputs: Z[√35] is the maximal order (35 ≡ 3 mod 4), and its unit group is ±ε^Z.

**Analytic consequences (Cat A, citing Hecke and Siegel–Klingen).**
- Hecke: the partial zeta ζ(s,𝒦) = Σ_{𝔞∈𝒦} N𝔞^{−s} continues meromorphically with only a simple pole, at s = 1.
- So E(e^{−t}) has an asymptotic expansion in **integer powers of t only**:
  E(e^{−t}) = e^{−7t/20} [ 20·Res/t + Σ_{j≥0} ζ(−j,𝒦)(−t/20)^j/j! ]
- Siegel–Klingen: ζ(−j,𝒦) ∈ Q.
- **Computed exactly** (`em_exact.py`, symbolic):
  - Res_{s=1} ζ(s,𝒦) = log ε/(20√35);
  - **ζ(0,𝒦) = 1/10**;
  - E(e^{−t}) = 2I/t + (1−7I)/10 + O(t).
- The vanishing of the t^{−1/2} term is checked independently by the Euler–Maclaurin computation (exactly 0) and numerically (the remainder is O(t): `em_check.txt`).

### A3. Closed-form radial expansions at q = e^{−t} (`em.py`, `em_exact.py`, `closed_forms.py`, `em_check.py`, `hs_decomp_check.py`)
**Method.** 2-D Euler–Maclaurin with Bernoulli polynomials on shifted quadrants.
- For H_s: closed cone ((0,1),(21,−1)), as 21 residues (s,0) plus N·v1 + N·v2, minus half-walls. This decomposition is **exact to q^2000** (`hs_decomp_check.txt`).
- Every coefficient below was confirmed numerically. The remainder after subtracting the three terms scales as √t down to t = 2.5·10^{−5} (`em_check.txt`).

| series | t^{−1} | t^{−1/2} | t^0 |
|---|---|---|---|
| P_s | I | **√π(49−2√14)/140 = 0.5256172043** | **(11−7I)/20 = 0.4767030629** |
| C_third | I | −√π(49−2√14)/140 | (11−7I)/20 |
| R | I | −0.3606097211 | (1−7I)/20 |
| E | 2I | **0** | **(1−7I)/10** |
| H_s | 0 | **√π(√1190−17√14)/170 = −0.3035254127** | 0 (to 30 digits) |
| **C** | I | **a_C = √π(833+204√14−14√1190)/2380 = 0.8291426171** | (11−7I)/20 |

- **Status of the forms.** a_P, b_P and the E row were obtained symbolically. a_H and a_C are explicit Euler–Maclaurin expressions evaluated to 30 digits; their radical forms are PSLQ simplifications at 30 digits.
- **Correction to the earlier report.** Its fitted value 0.8174 for C's t^{−1/2} coefficient was biased; the exact value is 0.82914.
- **Upgrade of obstruction 2 for C (now Cat A).** a_C ≠ 0, so C·g = F is impossible for any holomorphic modular g and F of any weight, level or multiplier, with complex coefficients. The argument is the same as for C_third in the earlier report.
- **Mellin form (Cat A).** For Z(s) = Σ_{(n,k)≥0,≠0} Q_s^{−s}:
  - simple poles at s = 1 (residue I) and s = 1/2 (residue (49−2√14)/140);
  - Z(0) = −(9+7I)/20.

  The log ε in Z(0) comes entirely from the shift 7/20 relative to the ray-class zeta, whose value 1/10 is rational.
- **Consistency.** The decomposition 2P_s = E + 1 + θ_3 − Θ_hol forces the t^{−1/2} coefficient of Θ_hol to be √π − 2a_P = √π(21+2√14)/70.

### A4. Theorem G: proof of the |G(h/m)| pattern (`gauss_pattern.py` → `gauss_pattern.txt`)
G(h/m) = (2m)^{−2} Σ_{n,k mod 2m} e(hQ_s(n,k)/m), with gcd(h,m) = 1.
- **2 | m.** Shift k → k+m. Then (Q_s(n,k+m) − Q_s(n,k))/m = 7n + 7k + (7/2)(m+1). The phase is e(7h(m+1)/2) = −1, because h and m+1 are odd. So G = −G = 0.
- **m odd.** Q_s is m-periodic in each variable, and 2 is invertible mod m. Substitute n' = n + 7·2^{−1}k. Then hQ_s ≡ h[n'² − (35/4)k² + (7/2)k] mod m, and the sum factors as G = m^{−2} g_n g_k, with |g_n| = √m (the quadratic Gauss sum).
  - **5 | m.** Shift (n,k) → (n − m/5, k + m/5). The n- and k-linear parts change by integers. The constant part changes by (7−m)/10 = j/5 with j ≡ 1 mod 5. The phase is e(hj/5) ≠ 1, so G = 0.
  - **gcd(m,35) = 1.** Completing the square in k gives |g_k| = √m, so |G| = 1/m.
  - **7^e ‖ m, 5 ∤ m.** By CRT multiplicativity, the 7-part of g_k is 7·Σ_{k mod 7^{e−1}} e(h(−5/4·k² + k/2)/7^{e−1}), of modulus 7^{(e+1)/2}. Hence |G| = √7/m.
- Verified: all 3374 coprime pairs (h,m) with m ≤ 105, zero mismatches.

### A5. Vector-valued route: the leading order is exact (`weil_test.py` → `weil_test.txt`)
Define G_{α,β}(x) = mean over ν ∈ α+Z² of e(xQ2(ν) + B(ν,β)). This is the 1/t radial profile of any cone sum over that coset and twist, divided by the cone measure.
- **S-law (exact to 1e−14 in all 27 tests).** G_{a,b}(−1/x) = (1/(√35·x)) e(B(a,b)) Σ_{p∈A^{−1}Z²/Z²} G_{b+p,−a}(x).
  - Tested components: (a,0), (p,−a) and (a+p7, p2), at 9 values of x including zeros of G.
- **T-law (exact).** G_{a,b}(x+1) = e(−Q(a) − ½B(A^{−1}A*,a)) G_{a, a+b+½A^{−1}A*}(x).
- This is Zwegers Cor. 2.9(4)–(5) (arXiv:0807.4834) transported to radial profiles: the weight-1 Weil representation on the 35-element discriminant group. It reconciles the earlier scalar W_7 obstruction, which is vector mixing and not a contradiction.
- **Status split.** The general statement (Gauss-sum reciprocity for the indefinite discriminant form) is Cat B as a theorem; it is Cat A on every tested x.
- **Where it breaks.** The law cannot hold at the cusp pair (0, ∞). At x = 0 each cone sum has singular part I·G/t ≠ 0, while at ∞ the cone sums have no q^0 term (Q2 has no nonzero rational zeros, since 35 is not a square). Equivalently, an exact vector-valued modular law with algebraic data would force I ∈ πQ̄ + Q̄, which Baker's theorem excludes.

### A6. Vector-valued route: second order
- **Quadrant vector** (`weil_order2.py` and `.txt`, plus a half-wall variant `weil_order2_halfwall.py` and `.txt`).
  - The t^{−1/2} coefficients have an exact finite formula: Euler–Maclaurin on the residue classes mod 4m. At x ∈ Z it reproduces the Euler–Maclaurin value for R, up to the phase e(−7/20).
  - The weight-1 S-law at this order would require a(−1/x) = (sgn x/√35) e(B) Σ_p a_p(x). It **fails**: |LHS|/|RHS| ranges from 0.49 to 2.97 over 16 tests, under either wall convention.
  - So the quadrant-cone vector is not quantum modular of weight 1.
- **E-vector** (`evector.py`, `evector2.py`; the γ²-averaged components are canonical, since the order of γ on all 36 components' data is k = 2).
  - The t^{−1/2} coefficient is ≈ 0 (≤ 5·10^{−15}) for every component at every tested x, consistent with A2.

---

## Category B
- **B1. Quantum modularity of the E-vector (numerical evidence).**
  - Define κ(x) as the t^0 coefficient of E_{α,β}(e^{2πix}e^{−t}), and the order-t^0 S-cocycle ψ(x) = κ_{a,0}(−1/x) − (x/√35) Σ_p κ_{p,−a}(x). The 1/t parts cancel exactly by A5.
  - On 37 rationals in (0,2] (`psi_grid.txt`), ψ is nonzero, for example ψ(1) = 0.00688 − 0.03826i. It is monotone, and polynomial fits converge geometrically: max residual 9e−5, 1e−5 and 1e−6 at degrees 4, 6 and 8, against |ψ| ≤ 0.105.
  - Near 0, ψ(x) ≈ −0.054i·x².
  - This is consistent with ψ extending real-analytically to (0,∞): **E would be a renormalized weight-1 quantum modular (vector) form**, with the 1/t singular parts I·G(x) removed and the T-law exact.
  - **Not proved.** No closed form for ψ was found. The natural candidate is an Eichler/Shintani-type period integral; not attempted.
- **B2. Consequence for P_s.** P_s = ½E + ½(1+θ_3) − ½Θ_hol.
  - The E part carries all the non-modularity "of regulator type" (log ε) and is at best quantum (B1).
  - θ_3 is modular.
  - Θ_hol is a weight-1 mixed mock form with an explicit Zwegers completion.
  - So, conjecturally, P_s is quantum modular of weight 1 after removing the 1/t singular parts, apart from the t^{−1/2} terms, which are carried entirely by θ_3 and Θ_hol.
- **B3. Appell–Lerch/HM form.** No Appell–Lerch or Hecke-type expression for E or P_s was found or attempted beyond P_s = C_third − q^8 f_{2,7,7}(−q^10,−q^14,q). An Appell–Lerch formula with algebraic data would give a 1/t coefficient in πQ̄ + Q̄, which Baker excludes. That step needs the asymptotics of Appell–Lerch sums at q → 1, which I did not verify, so this obstruction is **conditional**. No Polishchuk-type identity was attempted.
- **B4. Residue formula.** log ε/(20√35) = R_𝔣/(w·√d_K·N𝔣), with d_K = 140, N𝔣 = 10, w = 1. This matches the narrow ray-class residue formula as I recall it; I did not re-check it against a source.

## Self-audit
1. **Exact series identities.** Integer numpy bincounts, with box-edge assertions, to q^3000; the H_s decomposition to q^2000.
2. **Euler–Maclaurin coefficients.**
   - The analytic formulas are verified three ways: symbolic (sympy) for P_s, R, E and a_P; 30-digit quadrature; and the remainder of the direct sums scaling as √t (or t for E) at t down to 2.5e−5.
   - The H_s constant is 0 only to 30 digits; it is not proved symbolically.
3. **Ray-class identification.** Hand algebra with symbolic checks of Q2 = N(β)/400 and β(γν) = εβ. The orbit ↔ ideal bijection uses the unit group ±ε^Z. ζ(0,𝒦) = 1/10 is exact and consistent with Siegel–Klingen rationality, which is an independent sanity check.
4. **Weil tests.** Finite exponential sums in floating point (errors ≤ 1.5e−14). The order-t^{−1/2} formula assumes the usual sector-uniform expansions. Its failure is O(1), so the conclusion is robust; the specific second-order formula is my derivation.
5. **What is not claimed.**
   - ψ is not claimed real-analytic (B1).
   - No vector law beyond leading order is claimed.
   - No statement is made about HQCC, TPC or RH.
   - Master files were not modified.
6. **Citations used.** Zwegers' thesis (local copy at `../2026-10-17-levers-1-2/zwegers.txt`, Cor. 2.9). Hecke (analytic continuation of ray-class partial zetas), Siegel–Klingen (rationality), and Baker (1966): all are standard theorems cited by name; I did not re-check theorem numbers.

## Files (`2026-10-17-P_s-structure/`)
| script | output | content |
|---|---|---|
| `structure.py` | `structure.txt` | A1, A2 |
| `em.py`, `em_exact.py`, `closed_forms.py` | `em.txt`, `em_exact.txt`, `closed_forms.txt` | A3 |
| `em_check.py` | `em_check.txt` | numerical confirmation |
| `hs_decomp_check.py` | `hs_decomp_check.txt` | H_s cone decomposition |
| `gauss_pattern.py` | `gauss_pattern.txt` | A4 |
| `weil_test.py` | `weil_test.txt` | A5 |
| `weil_order2.py`, `weil_order2_halfwall.py` | `.txt` | A6, quadrant vector |
| `evector.py`, `evector2.py` | `evector.txt`, `evector2.txt` | A6, E-vector |
| `psi_grid.py` | `psi_grid.txt` | B1 |

## Next steps
(a) Find ψ in closed form, as a period integral over the γ-fundamental cone; that would settle B1.
(b) Compute ζ(−1,𝒦) to check the t^1 coefficient of E.
(c) Prove the Weil S-law for G_{α,β} in general via Gauss-sum reciprocity.
(d) Run the same structure check for s = 8 and s = 11 (disc 48 and 99).
