# A33: The 35-component "law vector" (Residual-Law B3) and the χ³ sector

**For:** Arvin Hampton (539 Labs) · 2026-10-22, about 10:36 AM CDT.

**Folder:** `reports/s_family_paths/A33_law_vector_chi3/`
- Scripts: `law.py`, `module.py`, `to_rho7.py`, `spec_check.py`, `sectors.py`, `exact_z7.py`.
- Outputs: `weil_fit.json`, `module.json`, `module.npz`, `to_rho7.json`, `spec_check.json`, `sectors.json`, `exact_z7.json`, `g_K*.npy`.
- Preregistration: `prereg.md`, SHA-256 `b5bff8ae8652c9e86bf1410e1f8890a3126e1d0d3fd7721138b5c11048e0752c`. It was hashed at 10:28 AM CDT, before any computation, and re-verified when this report was written.

**Ground rules**
- CORE_FREEZE: H_s was not redefined and certifier code was not touched.
- A32 outputs, `RTA_prereg/results/run_all.py` (EC, the source of ρ_7|W, E and C) and `weil_family` were imported read-only.
- New files only. Nothing was pushed or sent. No TPC or RH claims.
- **Cat A** = exact or proved. **Cat B** = floating point or interpretation.

## Verdict: **does not land** (Cat B for the full statement; the key vanishing is Cat A)
- **Exact (Cat A):** every candidate law vector built from the source's profiles is **even under the local reflection Z₇**.
  - So its ρ₅⁻⊗ρ₇⁻ component, which A32's χ³ map Φ needs, is identically zero.
  - The one exception is the (a,a) characteristic K1. That candidate is identically zero numerically (Cat B) and does not appear in the source's laws.
- **Floating point (Cat B, large gaps):** the profiles do not form a ρ₃₅-module at all.
  - Together with their S and T translates, they span a **36-dimensional irreducible** SL₂(Z)-module V.
  - **V ≅ E**, the 36-dimensional part of ρ_7|W, **with no twist**.
  - **Hom(V⊗χᵏ, C) = 0 for all 12 k** (and for duals). So neither law·η⁶ nor law/η⁶, nor any other η^{2k} twist, reaches C.

## 1. Where the law is defined (sources)
- **Primary source.** `docs/.../Bridge_C_Residual_Law_2026-10-17/2026-10-17-Bridge-C-Residual-Law.md`, line 173, **B3 "Vector-valued escape"**. It says:
  - over the 35 characteristic components (Zwegers Cor. 2.9(5) shape), the leading profiles G_μ(x) should transform by the weight-1 Weil representation;
  - the expected law covers **the singular parts only**, and the cone sums themselves stay non-modular;
  - status: **"Not attempted"**.
- **Other places the same item appears.**
  - Line 31 and next step (b) at line 196 of the same file.
  - The same text is filed as **B2** in `CatB_Notes_Bridge_C_Residual_Law_2026-10-17.md`.
  - `ERRATUM_Bridge_C_tminushalf_Coefficient_2026-10-17.md` E3: the leading order was later checked.
  - `P_s_Structure_2026-10-17/2026-10-17-P_s-Structure.md` §A5, `weil_test.py`: the S-law and T-law were checked at 27 + 6 points. The scripts there already speak of a **"36-component family"**.
  - RTA_prereg Amendment 2 and A32 only cite it.
- **What the law is.** It is **not a q-series and not an eta or theta quotient.**
  - Its components are functions on Q:
    G_{α,β}(x) = mean over ν ∈ α+Z² of e(x·Q(ν) + B(ν,β)), with Q(ν) = ½νᵀAν and A = [[2,7],[7,7]].
  - Each one is the coefficient of the 1/t singularity of a cone sum at q = e(x)e^{−t}.
  - The law expresses weight 1 in "profile form": g(−1/x) = x^{−1}·M_S·g(x) and g(x+1) = M_T·g(x).
  - **There is no principal part and no Fourier expansion.** Baker's theorem excludes an exact holomorphic vector-valued law with algebraic data (P_s ledger, A5).
  - So item (2) of the brief, "q-expansions", does not apply. What can be built exactly is the finite Gauss-mean value at each rational x.
- **What the source leaves open.** It does not say which 35 pairs (α,β) make up the vector. The preregistered candidates, with μ ∈ D = A⁻¹Z²/Z² and the source's characteristic a = (7/10, −1/5), are:
  - K1 = G_{a+μ, a}
  - K2 = G_{a+μ, 0}
  - K3 = G_{μ, a}
  - K4 = G_{μ, 0}
  - Fact (Cat A): a ≡ ½A⁻¹A* mod A⁻¹Z².

## 2. Construction and transformation tests
- **How the values were computed.** Each G is an exact finite mean over a 4m × 4m box. The phases are integers mod 9800m, so no phase rounding occurs; the exponentials themselves are evaluated in floating point.
  - Coverage: 216 rationals h/m with m ≤ 15 (138 rationals with m ≤ 12 in `law.py`).
- **Each candidate against ρ₃₅⊗χᵏ** (A32 labels; ε = i; all 12 k; ρ and dual; weight factor x^{±1}), from `weil_fit.json`:
  - **K1:** identically 0 (|g| ≤ 4·10⁻¹⁶). It trivially satisfies every law.
  - **K4:** the S-law holds as ρ₃₅⊗χ, with error 7·10⁻¹⁵ and weight factor x^{−1}. **The T-law fails** (error 1): T moves the twist β from 0 to the class of a.
  - **K2, K3:** they fail both laws.
  - **None of the 35-vectors is a ρ₃₅⊗χᵏ vector.** This is expected for the **odd** lattice A_7. As with θ₂, θ₃, θ₄, T permutes the characteristic classes: K4 →T K3 →S K2.
- **The module V** (`module.py`).
  - The 105 functions K2∪K3∪K4 span a space of **dimension 36**, with singular values 1.57 against 3·10⁻¹⁴.
  - The space is closed under S and T: the out-of-span residual is 4·10⁻¹⁵.
  - The fitted M_S and M_T satisfy S⁴ = 1 and (ST)³ = S² to 2·10⁻¹⁴.
  - dim End(V) = 1, so V is irreducible (Cat B).

## 3. Decomposition and the χ³ map
- **Exact (Cat A), from `exact_z7.py`, all in rational arithmetic.**
  - γ = [[−1,−7],[2,13]] satisfies γᵀAγ = A and det γ = 1.
  - γ⁻¹ acts on D **exactly as the local reflection Z₇**: identity on D₅ and −1 on D₇.
  - γ⁻¹a − a = (7, −1) ∈ Z².
  - Changing variables ν ↦ γν gives G_{α,β} = G_{γ⁻¹α, γ⁻¹β}. Shifting β by λ ∈ A⁻¹Z² multiplies G by e(B(α,λ)).
  - Checking these phases for all 35 μ gives **g_μ = g_{Z₇μ} exactly for K2, K3 and K4**. So each of these has **zero Z₇-odd part, and in particular zero ρ₅⁻⊗ρ₇⁻ part**.
  - For K1 the phase is ½, so K1 is exactly Z₇-odd. K1 is nevertheless 0 on every test point (Cat B); this was not proved in general.
- **Sector norms (Cat B), from `sectors.json`, maximum over the test rationals.**

| candidate | (+,+) | (+,−) | (−,+) | (−,−) | max\|Φ g\| |
|---|---|---|---|---|---|
| K2 | 1.0 | 3e−17 | 0.95 | 3e−17 | 2e−16 |
| K3 | 1.0 | 6e−17 | 0.95 | 2e−17 | 2e−16 |
| K4 | 1.0 | 6e−17 | 9e−17 | 3e−17 | 2e−16 |
| K1 | 4e−16 | 2e−17 | 2e−16 | 1e−17 | 1e−17 |

- **Module level (Cat B), from `to_rho7.py` and `spec_check.py`.**
  - Hom(V⊗χᵏ, X) was computed for X ∈ {W, E, C}, their duals, all 12 k, and both transpose conventions.
  - The **only** non-zero result is **k = 0 into E (and hence W), with dimension 1**.
  - Every χᵏ twist into C is 0, **including χ³** (the η⁶ multiplier, weight 3) **and χ⁹** (the η⁻⁶ direction).
  - V has 36 distinct T-eigenvalues (in units of 1/140), and they **coincide exactly with those of E**.
  - Smallest singular values for Hom(V, E): 3·10⁻¹⁵, then 0.297.
  - Hom(V, ρ₃₅-sector⊗χᵏ) = 0 for all 4 sectors × 12 k × {ρ, ρ*}.
- **About weight.** A32's Φ intertwines ρ₃₅⊗χ³, and χ³ is the multiplier of η⁶ (weight 3).
  - The law has profile weight 1, so a twist law·η^{±6} would have weight 1 ± 3 as a representation-theoretic object.
  - **As actual functions this twist is undefined:** η vanishes radially at every rational, so η⁶ times a 1/t profile has zero leading profile.
  - At the representation level, every twist is covered by Hom(V⊗χᵏ, C) = 0 above. Weight compatibility therefore cannot rescue a landing.

## 4. Verdict and reasons
**Does not land.**
1. **(Cat A)** Every non-zero candidate 35-vector built from the source's profiles has an exactly vanishing ρ₅⁻⊗ρ₇⁻ component. The reason is the lattice automorph γ, which acts as Z₇ on D and fixes the characteristic.
2. **(Cat B)** The law is not a ρ₃₅⊗χᵏ object. Its SL₂(Z)-span is a 36-dimensional irreducible V ≅ E, untwisted, and no twist χᵏ maps it to C.

**What is not claimed**
- A general proof of the Weil law for G at all x. The source has it as Cat B; here it is Cat A only per tested point, and the module matrices are fitted.
- An exact (cyclotomic) certificate of V ≅ E.
- K1 ≡ 0 in general.
- Any statement about cone sums beyond leading order.

**Possible follow-up:** an exact certificate of V ≅ E. Write M_S and M_T in closed form from the S-law and T-law, then rerun A32's mod-p rank method.

**Ledger suggestion (Cat B):** "The B3 leading-order law vector lives in E (≅, untwisted, 36-dim), not in C; its ρ₅⁻⊗ρ₇⁻ part vanishes exactly by the automorph γ."
