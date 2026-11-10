# NL DERIVED: completeness and regularity of the T7 (r,χ) reduction, with Z1, J4 and J7b
2026-11-09, 21:03 CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED**, unchanged. The count-gap status is unchanged.

Authority: **OW t4426** OWNER_WRITE_MAINCHAT_t4426_PURSUE_ALL_OPEN_JUNCTION_ROUTES_2026-11-09_1956.md = d5eaeef3f6b53270bd09e30053f6cdbf442d191c58a0a9fda30daff83907ffb3 ("Pursue all open"; χ-smearing is NOT decided; this is item 6). **OW t4431** OWNER_WRITE_MAINCHAT_t4431_LIFT_90_PERCENT_STOP_2026-11-09_2020.md = f700141d3ee862c7b077b0f67db5fb03b3adc56808c927ba1dd016c88910b1ec (the 90% stop is lifted; usage is still reported). Also OW 19a88b19 (MN N=2 working vacuum, CONDITIONAL; junction UNSOLVED); OW f825dfff (odd HW-type ℤ₂ wall, IR side kept); OW 36683379 (citations checked, never upgrade alone); OW f1d167d1 (the algebra is not named in this file). Builds on 1943 (b103f08f…; T7, T8, T10), 1948 (9a29b6da… as filed; K1–K8, with E18's K6/K6′ revision), PP 3982a4b8 (J4, J7), E16 (E16-J4 CONDITIONAL, E16-J7a PROVED, E16-J7b OPEN; E16-A4, A5), PP Z1 in 0a82cf18 / 1aa88a30 and MR2 N17. CGR arXiv 1906.08900 eqs. (3.2)–(3.8), (5.7), (5.15)–(5.16), (6.1)–(6.2).

Limits: additive only. No existing script or report is edited (including 1943, 1948, E16, E18, and the PP/MR2 Z1 sources). No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after. Usage 84.1% at the start of this write (weekly reset Tue Nov 10 09:49 CST).

χ-smearing is not decided (OW t4426). The **χ-smeared** [χS] and **χ-uniform** [χU] branches are labelled where the wall-source hypothesis matters (R7). Z1/w and the bulk inventory do not depend on it.

**Tally: PROVED 5 · CONDITIONAL 2 · OPEN 2 · REFUTED 0 · total 9**

## 1. Question

Is the H-invariant cohomogeneity-two reduction of 1943 T7, which is the arena of the 1948 KK count, complete and consistent, and are the fields regular at the S⁴ poles, at the IR end, and at the wall? Fold in J4 (interval or analytic argument for the singlet-toy shoot) and J7b (the IR comparison of A_E′) from PP 3982a4b8 / E16. Record PP's Z1 (w is marginal at MN2, with Δ=4 and a nonzero cubic) and how w enters the reduction.

Script and log, new dated directory `/workspace/nl-t7-reg-2055/`, sidecars:
- t7_w_Z1_j7b_poles_2026-11-09_2101.py = a6d853803e2a1fb02d7d9565f6e76ddd65f3a920e79cfe18233d64b92b29d07b, **frozen before execution**
- t7_w_Z1_j7b_poles_2026-11-09_2101.log = d8a25604c1cfa926d01f3afbb5a8e2bc8f551efdacc0efb536dc090231156d40

## 2. R1 (PROVED). The T7 ansatz is the complete H-invariant configuration; consistency is at the EOM level

H = Poincaré(1,3) × SO(3) (on μ^{3,4,5}) × U(1)_{φ₁} × (PSL(2,ℝ) of H², lifted by the twist). This is the group of 1943 T7. Every element is a symmetry of 11D supergravity, so E[Φ] is H-invariant whenever Φ is, and the reduced equations on invariant Φ are exactly the 11D equations restricted to that sector (E16-A4). Compactness / Palais is not used and is not claimed. The sector is a locally homogeneous proper consistent subsector of the Aut⁺(Bolza)×wall ℤ₂ scope, not all of it (E16-A5b). It is infinite-dimensional: fields are functions of (r, χ).

The H-invariant tensors are, up to 2-dimensional diffeomorphisms of (r, χ) and a U(1)_{φ₁} fibre gauge:

- Metric: e^{2A} η_{μν} dx^μ dx^ν, g_{rr}, g_{rχ}, g_{χχ}, e^{2G} ds²(Σ) (with the twist), R_{φ₁}² (Dφ₁)², R_{S²}² ds²(S²), and a U(1)_{φ₁} connection A_r dr + A_χ dχ on the (r, χ) base (its field strength is one invariant scalar F_{rχ}). After (r, χ) diffeomorphisms, five physical warp functions remain, plus that F_{rχ}.
- G₄: the H-invariant 4-forms are spanned by vol(S²)∧Dφ₁∧dχ, vol(S²)∧Dφ₁∧dr, vol(Σ)∧vol(S²), vol(Σ)∧Dφ₁∧dχ, vol(Σ)∧Dφ₁∧dr, vol(Σ)∧dχ∧dr, and vol(ℝ^{1,3}). (There is no H-invariant 1-form on Σ or on S².) Bianchi, Maxwell and residual gauge will cut this list; the on-shell independent count is not computed here (R8).

This inventory is the precise content of T7's claim that "the H-invariant ansatz is the most general H-invariant configuration." It contains MN2, β(r,χ), squashing X_a(r,χ):X_b(r,χ) (with T^{αβ}∝1 by SO(3)), g_{rχ}, and G₄ components with dr∧dχ legs, as T7 stated. It is a consistent reduction, not a finite consistent truncation (T3, T6 remain as in 1943).

## 3. R2 (PROVED). Z1 reproduced independently

From CGR (3.8) at ψ=0 with T=diag(e^w, e^w, e^{−2w}) and the kinetic metric G=diag(60, 60, 3) on (φ, λ, w) coming from (3.7) — the w kinetic is (1/4)Tr(T^{−1}dT T^{−1}dT)=(3/2)(dw)² — at the MN2 point e^{30φ}=e^{10λ}=2, w=0, l=−1:

- ∇V=0, V_*=−3·2^{2/3} g², g² L²=2^{4/3}, V_*=−12/L².
- The Hessian does not mix w with φ or λ.
- m² L² = {12, −4, 0}. So **w is marginal, Δ=4**, with linear exponents μL ∈ {0, 4}.
- ∂³_w V|_{MN2} = −24·2^{2/3} g², exactly (ratio 1 to PP's Z1 / MR2 N17).

This is an independent exact check, not an upgrade by citation. The cubic is nonzero, so the centre-manifold equation is non-degenerate at quadratic order (w′ ∝ w²). Existence of IR-regular non-W₃ centre flows remains Z2 (OPEN, not re-counted here; see R9).

## 4. R3 (PROVED). w does not enter T7, nor the 1948 H-invariant count

T=diag(e^w, e^w, e^{−2w}) is invariant under the SO(2) that rotates the two equal eigenvalues, and is not invariant under a generic SO(3) rotation in a mixed plane unless w=0 (script: R T R^T − T has entries (1−e^{3w}) e^{−2w} sin²θ and (1/2)(1−e^{3w}) e^{−2w} sin 2θ, which vanish identically if and only if w=0). T7's H contains the full SO(3). Therefore w is projected out of T7, and it is not an H-invariant mode in the 1948 KK operator. The 1948 count (and E18's K6/K6′ revision) is unchanged by Z1.

w does enter the *larger* CGR subtruncations that keep only SO(2)_R ⊂ SO(3) (CGR §5.2.2, §5.3, T_{αβ}=diag(e^w, e^w, e^{−2w})). Those are not T7. In that larger sector the Δ=4 mode would contribute one IR condition at the linear level (K2: codimension 1 at Δ=4), and the cubic would prevent the constant branch from being a flat modulus; that is a different reduction, not used in 1948.

This is a bulk symmetry statement. It is the same on the **χ-smeared** and **χ-uniform** branches.

## 5. R4 (PROVED). Regularity at the S⁴ poles: conditions, and the MN2 background

Chart: D̃ = X_b cos²χ + X_a sin²χ, with the φ₁ circle shrinking at χ=0 (μ₁=sin χ) and the SO(3) S² shrinking at χ=π/2.

Necessary conditions for a T7 metric to be regular at the poles: the shrinking-circle (resp. S²) radius must vanish as χ (resp. π/2−χ), the cone ratio g_{angle}/((proper radius)² g_{χχ}) must tend to 1, and the warps A, G and the unshrunk fibre radius must be even and smooth in the Cartesian coordinates about the pole. g_{rχ} must vanish at the poles (odd). G₄ components must admit a smooth extension in those Cartesian coordinates (the coefficient of vol(S²)∧Dφ₁∧dχ is the regular Freund–Rubin term if it is finite).

The MN2 background satisfies them. The fibre is the smooth ellipsoid {μ·μ=1} ⊂ (ℝ⁵, T^{−1}), with T positive definite. Directly, lim_{χ→0} g_{φ₁}/(χ² g_{χχ})=1 and lim_{χ→π/2} g_{S²}/((π/2−χ)² g_{χχ})=1, with X_a, X_b>0 and D̃>0 on [0, π/2] (script). Overall Δ^{1/3} and Δ^{−2/3} factors are common and smooth. So the exact MN2 IR end, as a background, is regular at both poles.

Whether a general T7 *solution* (with χ-dependent warps) satisfies the same conditions is a boundary condition on that solution, not automatic; it is part of T10 (R8).

## 6. R5 (PROVED). J7b for the singlet toy: the N4 inequality holds kinematically

E16-J7a: at the singlet-toy face, A_E′ = a−2a=−a. The 5D Einstein-frame warp in the toy is A_E = A+(2B+4C)/3, so A_E′=A′+(2/3)B′+(4/3)C′, which reproduces −a at the wall (A′=B′=a, C′=−2a) and −1 at the IR (A′=−1, B′=C′=0). The singlet class is a 5D Einstein-scalar theory, and NEC holds in the bulk (11D sugra) and at a positive-tension face. So N4's hypothesis is satisfied in the toy, and A_E″≤0 along any solution.

The flux Q is constant (E1). Matching the IR value q²=24 gives a=q/6=√6/3 on the whole E8 wall family (e^{−2B_w}=6e^{−2C_w}, one parameter C_w). Thus

k_{x,E} = √6 / 3 < 1 = 1/L_{5,E},

exactly (1−a=1−√6/3>0). Equivalently A_E′(wall)=−√6/3 ≥ A_E′(IR)=−1. This is the comparison E16-J7b asked for, and it does **not** require a solution to exist: it is a property of the wall family at the IR flux. It holds, and it is not an obstruction (it does not constrain C_w further). The 1936 and E16 files are not edited; this file is the additive record that E16-J7b is discharged for the singlet toy.

## 7. R6 (CONDITIONAL). J4: no interval or analytic no-go; "no toy solution" stays CONDITIONAL

The queued interval/analytic argument was not obtained. New exact geometry of the wall curve, which does not upgrade S4:

- On the whole wall family A′=Q e^{−4C}/6 is strictly positive (Q>0). The IR has A′=−1. Hence (A′+1)²≥1 on the wall, so |Y−FP|≥1, with equality impossible (A′→0 only as C→+∞, where |B| and |C| diverge). A numeric minimum on C∈C_0+[−4,4] is ≈1.966 at C−C_0≈0.348.
- This only says the wall curve does not pass near the fixed point. It does not prevent W^s from meeting the wall far from the FP.

PP's W^s sweep (1440 directions, |Y|≤60, minimum wall residual 2.309, float and box-limited) and NL's C_w scan remain the evidence. Coverage caveats of E16-J4 still apply (unbounded C_w; the |δC|^{≈0.14} approach law; the box). "No toy solution" stays **CONDITIONAL**. S3's genericity heuristic is unchanged. The singlet-toy codimension does not carry over to MN2 (T8).

## 8. R7 (CONDITIONAL). Wall regularity and HW compatibility, both χ-branches

T7's bulk proof does not include the wall. HW compatibility still requires the E₈ data and the source densities to be H-invariant up to gauge (E16-A5a). f825dfff fixes only the total ∫(n_{M5}+n_{inst})=9760.

- **[χS]:** pointwise-in-χ Israel (T8) needs a smeared H-invariant density n(χ). Admissibility of that smearing is the existing T8 hypothesis, still CONDITIONAL.
- **[χU]:** a χ-independent density is a special case of n(χ). It is H-invariant, but it can satisfy the pointwise Israel conditions only if the T7 fields at the wall happen to have χ-independent extrinsic curvatures of C4 type. That is a stronger, generally over-constraining requirement, not a second consistent default.

Regularity at the wall, in either branch, means finite warps, the pole conditions of R4 imposed at r=r_w, and Israel. No T7 wall solution has been constructed (R8).

## 9. R8 (OPEN). PDEs, the (r,χ) spectrum, and IR conditions beyond (φ,λ)

The H-invariant field equations as PDEs, with exact residuals, have not been written (T10, A8). The linearized H-invariant spectrum on MN2, other than the (φ,λ) zero-modes of K1 (Δ=2 and Δ=6), has not been computed (K3). IR regularity conditions for the genuine χ-dependent modes, and a relaxation solve with error control, remain open. The on-shell independent field count after Bianchi and gauge, needed for a sharp function-space version of the 1948 count, is likewise open. This file does not attempt that shoot.

IR regularity of the MN2 *background* itself is the standard AdS₅ end (K2 for (φ,λ); the geometry is the regular one of R4). That is already in 1948 and is not re-counted.

## 10. R9 (OPEN). J7b / N4 in the T7–MN2 sector, and the w-on sector

N4 is CONDITIONAL on a 5D Einstein-scalar description. T7 is cohomogeneity two, not a finite 5D scalar theory, so the c-theorem that gives k_{x,E}≤1/L_{5,E} has not been proved in T7 (a χ-integrated warp may exist, but it is not derived here). J7b for a future MN2/T7 shoot therefore remains open, unlike the toy (R5).

Separately, Z2 (IR-regular non-W₃ centre-manifold flows in w) is a question in the larger SO(2)_R sector, which is not T7 (R3). It is not opened or closed here.

## 11. What this does not change

The junction remains **UNSOLVED**. χ-smearing remains undecided. Nothing is adopted. Z1 does not change the 1948 / E18 KK count, because w is not H-invariant. J7b is satisfied in the toy and is not an obstruction; J4 is not upgraded. T6, T9, T10, K3 and K7 stay as previously labelled. The breathing-mode route is still the T7 PDE sector, with existence OPEN.
