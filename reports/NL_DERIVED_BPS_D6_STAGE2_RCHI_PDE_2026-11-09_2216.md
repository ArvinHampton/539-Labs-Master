# NL DERIVED: D6 stage 2, η from the MN2 Killing spinor at C₄; (r,χ) BPS conditions; IR-regular Z2 kept sides
2026-11-09, 2216 CST (America/Chicago). **NL derived proposal.** This file is additive only and does not edit NL_DERIVED_BPS_D6_NONLINEAR_RCHI_KSE_2026-11-09_2100.md (ff2c74bc…).
- Authority: OW t4426 d5eaeef3. Usage stop lifted under OW t4431. OW t4436 (32881263…): "Let the math lead the pursuits on all open paths". So every branch is carried separately, and a branch is narrowed or dropped only on PROVED or REFUTED.
- Nothing is adopted. **Junction: UNSOLVED. Count gap: unchanged.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.

Scripts are in /workspace/nl-d6s2-2110/. **Every .py sidecar was frozen before its run.**

| Script | .py sha | Log sha |
|---|---|---|
| eta_c4_sectors.py | 46b2918e… | e3b5f52c… |
| w3_and_partners.py | 42abc959… | e2f2fd0a… |
| w3_symbolic.py | db57d70b… | b7067459… |
| z2_bvp_ir_regular.py | c72e7162… | 37e7f960… |
| z2_bvp_continuation.py | 9353d5ed… | b4036905… |

Disclosures:
- z2_bvp_continuation.py was run twice. The first run was interrupted by the shell and lost its piped output. The second run, of the same frozen script, was killed by me while a hard case was running; the log says so.
- Logs were sealed after the runs.

**Tally: PROVED 7 · CONDITIONAL 3 · OPEN 3 · REFUTED 0 · total 13.**

> **No candidate wall found.** Conditional on the twist lock (S2-4), D6 is closed as a no-go for SO(3)_R-invariant BPS walls (S2-7). It stays OPEN on the escape branches in §5. Z2 stays OPEN.

## 1. Killing-spinor sectors at C₄ and η (decides D6-5)
Conventions:
- Frame (0..3, r, S1, S2, m1, m2, t, f), where m1,m2 are tangent to S⁴ along μ₁,μ₂ at C₄ = {μ_a = 0}, and t,f are tangent to the S² of μ_α.
- Γ^{S12} = is₁, Γ^{m1m2} = is₂′ (with s₂′ = −s₂ in the 2100 (χ,ν) orientation), Γ^{tf} = is₃.
- b(s) := s₂′s₃f₄ + s₁s₃ω₂ + s₁s₂′ω₁.

Items:
- **S2-1 (PROVED; exact).** MN2 flux and sectors at C₄, from CGR (2.5)–(2.7), (3.1)–(3.3), with g = 1 and l = −1.
  - In the orthonormal frame: f₄ = 2·2^{1/3}, ω₂ = l·2^{1/3}, ω₁ = 0, and A′_frame = Δ^{−1/6}e^{2φ}/L = 2^{1/3}/2.
  - The 11D x-row A′Γ^r ε = −(1/144)G̸ε reads A′γ_r = b(s)/6 on each sector.
  - **Exactly the twist-locked sectors s₁ = −s₂′ have |b| = 6A′** (|b| = 3·2^{1/3}). The other four have |b| = 2A′, so they cannot carry Killing-spinor components.
  - On the locked sectors γ_r = s₂′s₃.
  - This also confirms, independently, that the 1/144 KSE normalisation matches the G normalisation of CGR (2.6).
- **S2-2 (PROVED).** The F2 formulas of 2100 D6-2 were checked against an explicit 32×32 Clifford algebra: 5 random flux sets × 8 sectors, max deviation 6.7×10⁻¹⁶ including off-diagonal entries. In the (m1m2) orientation: α = σs₂′s₃f₄, β₁ = σs₁s₂′ω₁, β₂ = σs₁s₃ω₂.
- **S2-3 (PROVED).** For any SO(3)_R-invariant configuration, the preserved Killing spinors are a sum of SU(2) **doublets**. At every p ∈ C₄, the two members of each doublet take **s₃ = +1 and s₃ = −1**, with the same s₂′. Proof:
  - Killing spinors are parallel sections of the supercovariant connection, so the evaluation map ev_p is injective.
  - ev_p intertwines the stabiliser U(1)_{n̂(p)}, which acts at p as ½Γ^{tf}. Spinors at p carry only weights ±½, so only spin-½ multiplets can occur.
  - U(1)_R fixes C₄ and acts at p as ½Γ^{m1m2}. It commutes with SU(2)_R, so both members of a doublet carry the same s₂′.
  - Check: no nonzero spin-½ vector has a fixed-sign weight along every axis (eta_c4_sectors.py, Part 4).
- **S2-4 (CONDITIONAL). Twist lock.** In any Σ-uniform (H_Σ) configuration, every Killing-spinor component at C₄ has s₁ = −s₂′.
  - At the vacuum this is exact (S2-1).
  - In general: the lift to H² is invariant under the twisted SL(2,ℝ), whose stabiliser acts at p as ½(Γ^{S12} + Γ^{m1m2}). Killing spinors on Bolza are Γ-invariant. Borel density then makes them SL(2,ℝ)-invariant, which forces (Γ^{S12} + Γ^{m1m2})ε(p) = 0.
  - **Condition:** this uses Borel density for the cocompact Fuchsian group (a cited theorem, whose application was checked but which was not re-proved here), together with H_Σ.
- **S2-5 (PROVED, as an implication).** SO(3)_R + twist lock ⇒ on the two members of every preserved doublet, s₁ is the same and s₃ is opposite. Hence **η = sgn(σs₁s₃Φ_tw) takes both values, +1 and −1**. η is not a single sign.
  - D6-5 is thereby decided, conditionally on S2-4: η is indefinite, and a wall must satisfy D1 on both signs at once.
- **S2-6 (PROVED, as an implication).** For HW-BPS, Γ^nε = ε at every p ∈ C₄. At C₄, n ∥ ∂_r: U(1)_R invariance and smoothness give ∂_ρ r_w = 0 and g_{rρ} = 0 there.
  - D1 then has to hold on both doublet partners with the same geometric K.
  - With the twist lock, this forces **f₄ = ω₂ = 0 at C₄ on the face** (Part 3; both locked pairs).
  - Without the twist lock: if the partners share s₁, then f₄ = ω₂ = 0; if they have opposite s₁, then f₄ = ω₁ = 0 with ω₂ free (w3_and_partners.py (b)).
  - The x-row needs equal γ_r on both partners, which already gives f₄ = ω₂ for locked pairs.
- **S2-7 (CONDITIONAL). D6 no-go in scope S.** Scope S:
  - (S1) SO(3)_R × U(1)_R invariance;
  - (S2) Σ-uniform data;
  - (S3) magnetic flux only, G_{0123} = 0;
  - (S4) a smooth kept side with C₄ non-degenerate and no sources meeting C₄;
  - (S5) the kept side IR-regular to MN2;
  - (S6) the odd HW ℤ₂.

  Under S there is **no HW-BPS odd ℤ₂ wall with any (r,χ) dependence**:
  - By symmetry, the pullback of G to C₄ is ω₂·vol, with ω₂ constant on C₄.
  - Bulk Bianchi on the kept side gives ∫_{C₄}G|_face = Φ_tw = (l/g)·vol ≠ 0, from the twist term of (2.6) (2100 D6-4).
  - This contradicts S2-6, which requires ω₂|face = 0.
  - The argument is purely local at C₄. It uses neither the source profile nor the bulk PDE, so it applies equally to **[χU] and [χS]**.
  - **Conditions:** S2-4, plus D6-4's smoothness and no-source assumptions. Under OW t4436 the [χU] and [χS] branches are therefore *conditionally* narrowed to the escapes in §5, not dropped.

## 2. The (r,χ) BPS system
- **S2-8 (OPEN).** The general Poincaré-invariant (r,χ) BPS system outside the 5D truncation was **not** derived. Its suggested reduction to an LLM/SU(∞)-Toda-type PDE (LLM hep-th/0409174, which covers the AdS₅ limit) is a citation only and gives no label.
  - What *was* tested against the boundary conditions is the following: S2-7 shows that the D2/D1 rows at C₄ together with the odd ℤ₂ projection cannot be met by **any** solution of the system in scope S. Solving the PDE is not needed for that conclusion.
  - The PDE is still needed for the escape branches E1–E5 in §5, and there it is OPEN.

## 3. W₃ and the BPS status of Z2
- **S2-9 (PROVED; exact).** W₃ = (g/2)[e^{−2φ}(2e^{−6λ} + e^{4λ}(2e^{w} + e^{−2w})) + l e^{−8φ+6λ}] reproduces V(φ,λ,w) exactly: V = 2G^{ij}W_iW_j − (4/3)W², with G = diag(60,60,3), checked with sympy to an identical 0.
  - It is critical at MN2, with L = 2^{2/3}.
  - The linearised W₃-flow exponents are {+2, −2, +4}/L, and the w exponent is +4.
- **S2-10 (PROVED).** Z2 centre flows (w ~ −1/(cr), linear exponent 0) are **not W₃-flows**.
  - An IR-regular W₃-flow has w ≡ 0 at linear order, because e^{4r/L} grows in the IR.
  - The SO(3)_R breaking (T_αβ ∝ diag(e^w, e^w, e^{−2w})) also puts Z2 kept sides **outside scope S1**, so S2-7 does not cover them.
- **S2-11 (OPEN).** Whether Z2 flows are BPS with respect to some other gravitino-mass eigenvalue of 5D N=4 (MN2 is maximally supersymmetric there) was not checked.

## 4. Z2, with IR regularity properly verified
- **S2-12 (CONDITIONAL; numerical).** This replaces the crude slaved initial data of 2100 D6-7.
  - **Method:** each IR-regular kept side is solved as a **boundary-value problem** on r ∈ [0, 30].
    - At R = 30, all four IR-growing modes are removed: μL = +6 and the double +2 in (φ,λ), and μL = +4 in w, i.e. w′ = cw².
    - At r = 0, w(0) = w_m ∈ {−0.05, −0.1, −0.3} and the Δ6 amplitude is d₆.
    - The solution is then continued toward the UV by IVP.
  - **IR regularity:**
    - boundary residuals ≤ 3×10⁻¹²;
    - w(R) ≈ −0.010 to −0.013, and d(1/w)/dr near R is −2.557 to −2.572, against the leading-order −c = −2.520, a 1.5–2% difference consistent with the O(w³) correction;
    - **the w_m = −0.3 data are now genuinely on the centre-stable manifold**.
  - **Coverage:**
    - First pass: 30 of 39 solved, for d₆ ∈ [−0.15, +0.30] at each w_m. The 9 failures, d₆ ∈ {−0.20, −0.25, −0.30}, hit the mesh limit.
    - Continuation pass: added d₆ = −0.175 (w_m = −0.05).
    - **Blocked: d₆ ≤ −0.20.** Those BVPs did not converge at 10⁶ nodes. The neighbouring flows already hit a UV singularity within 0.07–0.10 L of r = 0, so the domain is close to singular there.
  - **Result:** no face of any solved flow satisfies the 11D NEC on the 9×7 (χ,θ) grid.
    - Minimum worst-direction margin: **+0.500** (flows reaching 30L, d₆ ≥ +0.05). It is about +0.626 at w_m = −0.3, d₆ = +0.30, and +0.707 for flows that end near r = 0.
    - It is always set by fibre directions.
    - The D2 trace reaches 0.019 at a single grid point (w_m = −0.3, d₆ = +0.2), where the NEC margin is +0.68. It is never zero at every point of S⁴, and Z2 is not BPS in any case (S2-10).
  - **Conditions:** float accuracy, a finite grid, finite d₆ ranges, and the unsolved d₆ ≤ −0.2 corner.
- **S2-13 (OPEN). The Z2 branch** (marginal w creep) is kept as its own branch:
  - BPS walls: OPEN (outside scope S; S2-11);
  - non-BPS NEC walls: OPEN, with numerical evidence against them (S2-12).

## 5. Branch register (per OW t4436; cross-references, not counted)
- **[χU]** and **[χS]**: conditionally narrowed by S2-7 to the escapes below. Neither is dropped (S2-7 is CONDITIONAL).
- **Z2:** OPEN (S2-13).
- **E1, SO(3)_R breaking:** (r,χ,θ)-dependent bulks, or w ≠ 0 BPS kept sides (W₃ with w is not IR-regular, S2-9). The stabiliser is then SO(2), so the doublet argument fails. OPEN.
- **E2, Σ-non-uniform data on Bolza:** OPEN.
- **E3, electric G_{0123} on the face:** S2-6's x-row step survives, since the c₄ term is common to both partners, but D1 needs re-deriving. OPEN.
- **E4, singular or degenerate C₄, or sources meeting C₄:** OPEN.
- **E5, U(1)_R breaking:** OPEN.
- Inherited and unchanged: NEC-violating sources; a > −2 (P6); UV side kept; non-BPS walls in general.

## 6. Impact
- No candidate wall was found.
- D6: CONDITIONAL no-go in scope S, OPEN on E1–E5.
- η: indefinite, conditional on the twist lock.
- Z2: OPEN.
- Gap unchanged; junction UNSOLVED. Nothing is adopted.

## 7. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 7 | S2-1, 2, 3, 5, 6, 9, 10 |
| CONDITIONAL | 3 | S2-4, 7, 12 |
| OPEN | 3 | S2-8, 11, 13 |
| REFUTED | 0 | — |

Check: 7 + 3 + 3 + 0 = 13.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
