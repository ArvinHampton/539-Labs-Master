# NL DERIVED: t552u BPS cluster: the fixed-set Euler obstruction (FX), the two-pole argument, and what remains of E1-4, E5∩¬H_Σ, E2∩E1, E4-6 and P8-3
2026-11-10, 1209 CST (America/Chicago). **NL derived proposal.** Resonant algebra. Additive only. No existing file is edited, renamed, deleted or chmod-ed.
Authority: OW t552u "Pursue all for resolution." (OWNER_WRITE_NLCHAT_t552u_PURSUE_ALL_FOR_RESOLUTION_2026-11-10_1146.md, eae1b39d635c69966a2b32642d395ae402d3c33fcf64db7f0b77cad2d8c60db2 = sidecar), pursuit only; OW 1117 geometry-first (bff79185…); standing t4436 (32881263…: the math leads; every option a labelled branch; only PP-audited PROVED/REFUTED keep or drop a branch; nothing by fiat); OW 1108 (c6375f85…), OW 1130 (945d81bb…), t4431 (f700141d…), f825dfff (face = Z2 fixed plane; O1 odd CONDITIONAL on P-b; E8 wall CONDITIONAL). t552u cancels none of these.
Frozen parents (read, not edited): Erratum 24 (60bbc718…), E5 (0a7d8e56…), E2 (197c5bd1…), E4 (4c25565f…), E1 (2f33b65d…), S2-8 (d559cb7d…), Z2 corner (101467fc…), Erratum 25 (01b7141f…; PP confirm 5dd9a6cd…, FAITHFUL with nits), PP resume audit (b39c7756…), E3/S5 of 2026-11-09 (e3ff699e…, 3ceb0605…).
**Nothing adopted. Junction: UNSOLVED. No candidate wall. No CERT.** No Gemini, no Ops, nothing sent, no agent messaged. N = 4880, charge 9760, tension-to-charge figures, 1a and B1-c2′ are not used and not adopted.
Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91: checked 11:47:21 CST (before any work), 12:06:04 CST (before the runs), 12:09:21 CST (immediately before this write). The after-write check is reported to NL.

Script (new directory /workspace/nl-bps-t552-1110/; sidecar frozen before the run, log sealed after; script, log and both sidecars mode 444):
| file | sha256 | time (CST) |
|---|---|---|
| fx_fixed_set_euler_exact_2026-11-10.py | 3ff3ae939a19e6e6fc8712449ae56f99de5ff2be18d365e32073a64139f66cef | sidecar frozen 12:06:04 |
| fx_fixed_set_euler_exact_2026-11-10.log | c3b711e3950dde9046672a31846148f7d1983c4c353b98a3aa4f960d6e548cbf | sealed 12:06:06; **40 passed, 0 failed, exit 0** |
Independent Clifford(1,10) build (Γ^{0…10} = +1, NL representation); exact rank and exact matrix equality over ℚ(i); expand(...)==0 on polynomials. No simplify(...)==0, no allclose. (A dry run of a byte-identical copy was made in /tmp before freezing, to catch typos; it supports no claim.)

**Tally: PROVED 8 · CONDITIONAL 2 · OPEN 3 · REFUTED 0 · total 13.**

## 0. Geometry demands algebra (lead section; summary of the labelled items below, no new claims)
Starting from the geometry of the face (the Z2 fixed plane; its slice M₆ an S⁴-bundle over Bolza Σ), and not from the junction, which stays UNSOLVED:
- **The fixed set of any surviving circle symmetry is a closed 4-manifold F ≅ Σ×S² inside the face** (C₄ for U(1)_R; F₄(n̂) = S²(μ₁,μ₂,μ₅)-bundle for an SO(2) ⊂ SO(3)_R). At every regular point of F the geometry forces the algebra: the HW projection Γ^nε = ε, the 4D chirality χ₄ and the circle weight on the normal plane together fix the chirality of ε as a spinor **of F** (log FX-1). So a Killing spinor restricted to F is a nowhere-zero section of a rank-2 chiral spinᶜ bundle of F.
- **The genus decides.** That bundle has c₂ = ±(2g−2) (log FX-2), i.e. ±χ(Σ) up to sign: ±2 on Bolza, 0 on a torus. So the geometry forbids a regular BPS face whenever such a circle survives, and the only geometric ways out are (i) break every circle with a 4-dimensional fixed set, or (ii) put on F a singular locus around which the spinor winds with total index exactly ±(2g−2) = ±2.
- **The S² has two poles of opposite rotation sense** (Euler number 2). With the H_Σ twist lock this alone forces opposite SO(2) charges at the two poles (log T1), so two regular points suffice there.
- What the geometry does **not** decide here: walls with no circle symmetry at all, a diagonal circle whose Killing spinors are all neutral, and spinor-winding defects. These are the residual OPEN items.

## 1. Premises (labelled where used)
- (h0) = Erratum 24 (h2): x-independent Poincaré supercharges (needed because Γ^{0123} anticommutes with Γ_μX; PP P4). Listed for every item below.
- (h1) flat Poincaré slicing, warp x-independent, no flux with 1–3 x-legs; (P-a) at least one Killing spinor.
- (ii) **the D1 HW hypothesis** Γ^nε = ε on the face (ε(−r) = Γ_nε(r), continuous at the wall). This is not "record premise S6"; S6 is the odd-HW record f825dfff (Erratum 25 Fix 2).
- (or) the face is the oriented topological boundary of the oriented kept side (so the face orientation is global; the HW projection uses one fixed normal convention).
- (lin) the surviving circle acts on the face bundle through the vacuum **linear** action in bundle coordinates (U(1)_R on (μ₁,μ₂); an SO(2) ⊂ SO(3)_R on two of (μ₃,μ₄,μ₅); a diagonal combination), preserving the metric, G, the face and the kept side.
- (F-4top) the face slice is the bundle S(𝓛⊕ℝ³) → Σ (𝓛 the twist line, ℝ³ the untwisted SO(3)_R summand), as in the vacuum (Erratum 24 F-4). deg 𝓛 is even (it is ±(2g−2) = ±2 in the vacuum; evenness is also forced by w₂(M₆) = 0).
- (reg-F) data regular along the whole fixed 4-manifold F ⊂ face: metric smooth and nondegenerate, ε and the supercovariant connection continuous up to the face, face C¹. Weaker variants are stated where used.
- Σ connected, genus g = 2.

## 2. The obstruction
- **T552-A1 (PROVED, implication). Lemma FX (fixed-set chirality).**
  - Premises: (h0), (h1), (P-a), (ii), (or), (lin) for a circle ζ, (reg-F) for a closed connected 4-manifold F ⊂ Fix(ζ) ∩ face slice, on whose normal 2-plane ν ⊂ T(face slice) ζ acts with nonzero weight.
  - Proof:
    1. The complexified Killing space V_ℂ is preserved by the Kosmann action L_ζ (ζ preserves metric, G, face and normal), by χ₄ (CH(b) under (h0)) and by the Lorentz generator Γ^{12} (algebraic on x-independent spinors). They commute, so pick ε ≠ 0 with L_ζε = iqε, χ₄ fixed, Γ^{12} fixed.
    2. At p ∈ F, ζ(p) = 0, so L_ζε(p) = ¼(∇ζ)_{ab}Γ^{ab}ε(p). Since ker ∇ζ(p) = T_pFix and ∇ζ is skew, ∇ζ(p) rotates only ν_p = (T_pFix)^⊥ (orthogonal complement in the metric; as an oriented ζ-representation it is the coordinate normal plane). So ε(p) lies in one eigenspace of Γ^{ν} (one s-value), the same on all of F because the weight and q are constant.
    3. ζ preserves the face and the kept side, so n ∈ ker∇ζ(p) = T_pFix, n ⟂ x, n ⟂ T_pF. Hence T_p = x ⊕ ℝn ⊕ T_pF ⊕ ν_p orthogonally, and Γ^{0…10} = ±Γ^{0123}Γ^n vol_F Γ^{ν}. With χ₄, Γ^n = +1 and the ν-weight fixed, vol_F has a single eigenvalue v (log FX-1, all 16 cases, both normals ±e_r, both choices ν = (t,f) and ν = (m₁,m₂)). The orientation of F is fixed globally by o(face) = o(x)∧o(F)∧o(ν) with (or), so v is constant on F.
    4. With Γ^{12} also fixed the joint space has rank 2 (log FX-1). It is S^v(TF)⊗λ, with λ the ν-weight half-line, so a chiral spinᶜ bundle E of F with det E pulled back from ν.
    5. ε|_F is a nowhere-zero section of E: a nonzero parallel section of the supercovariant connection vanishes nowhere on the connected smooth kept side, and it extends continuously and nonzero to F by (reg-F) and injectivity of ev_p. A rank-2 complex bundle over a closed oriented 4-manifold with a nowhere-zero section has c₂(E)[F] = e(E)[F] = 0.
  - Conclusion: **(P-a) is incompatible with c₂(E)[F] ≠ 0.**
  - Not used: H_Σ, the twist lock, SO(3)_R doublets, U(1)_R (unless ζ = U(1)_R), σ, the D1 rows, flux, Bianchi, N_face, the IR, the source profile n(χ).
- **T552-A2 (PROVED; exact). c₂ on the fixed sets is ±(2g−2) = ±2.**
  - On Σ_g × S² with ring ℚ[α,β]/(α², β²), αβ = 1, S^± = K_Σ^{±1/2}⊠O(∓1) ⊕ K_Σ^{∓1/2}⊠O(±1), twisted by any line with c₁ = kα pulled back from Σ: c₂(S^+⊗λ) = 2g−2 and c₂(S^−⊗λ) = 2−2g, **independent of k** (log FX-2a–c). This agrees with (c₁² − 2χ ∓ 3σ)/4 at χ = 4−4g, σ = 0, c₁² = 0 (FX-2d). Bolza: ±2 (FX-2e). Torus control: 0 (FX-2f).
  - **C₄ (ζ = U(1)_R):** C₄ = S(ℝ³) = Σ×S², ν = π*𝓛, so det E is pulled back from Σ (any k). c₂(E) = ±2.
  - **F₄(n̂) (ζ = SO(2)_n̂ ⊂ SO(3)_R):** F₄ = S(𝓛⊕ℝn̂). Since deg 𝓛 is even, w₂(𝓛⊕ℝ) = 0 and the S²-bundle is trivial (oriented rank-3 bundles over a surface are classified by w₂), so F₄ ≅ Σ×S² with its tangent bundle. ν = n̂^⊥ ⊂ ℝ³ is trivial, so det E is torsion (k = 0). c₂(E) = ±2.
  - σ = 0 for every S²-bundle over a surface (rank-2 unimodular form with isotropic primitive fibre class; FX-2g). χ = χ(S²)χ(Σ) = −4.
- **T552-A3 (PROVED, implication). Every branch that keeps U(1)_R is closed when the face is regular on all of C₄.**
  - Premises: A1 with ζ = U(1)_R and F = C₄, (F-4top) (only the bundle form; no twist degree, no isotopy beyond it), (reg-F) on C₄ ∩ face = C₄.
  - Proof: A1 + A2.
  - Covers: **E2∩E1 with U(1)_R kept** (any SO(3)_R breaking, any Σ-dependence); E1∩H_Σ∩U(1)_R (including the [w] branch, which keeps U(1)_R, E5-7); and it is an independent, SO(3)_R-free route to the conclusion of E2-4. E2-4 is PP-accepted and is **not** regraded or re-opened here; A3 is a separate implication.
- **T552-A4 (PROVED, implication). Every branch that keeps an SO(2) ⊂ SO(3)_R is closed when the face is regular on its fixed 4-manifold.**
  - Premises: A1 with ζ = SO(2)_n̂ (rotation of the two R³ directions ⟂ n̂, (lin)), F = F₄(n̂), (F-4top), (reg-F) on F₄(n̂).
  - Proof: A1 + A2.
  - Covers:
    - **E5∩¬H_Σ (= E2∩E5; E5-6, E2-5).** SO(3)_R is kept, so every n̂ gives such an SO(2). The regular set is SO(3)_R-invariant, so (reg-F) on one F₄(n̂) is equivalent to (reg-F) on all of them. No lock, no U(1)_R and no H_Σ is used.
    - E1 branches whose remnant contains an SO(2) ⊂ SO(3)_R, with or without U(1)_R and H_Σ ([w] keeps the rotation of (μ₃,μ₄)).
  - F₄(n̂) contains Σ×{±n̂} ⊂ C₄ and the SO(3)_R-fixed circle bundle {μ₃ = μ₄ = μ₅ = 0}. A face singular on either set is not covered here (→ A8, A10).
- **T552-A5 (PROVED, implication; exact). Two-pole argument on E1∩H_Σ: two regular points suffice.**
  - Premises: (h0), (h1), (P-a), (ii), (or), (tw), H_Σ, (lin) for an SO(2)_ξ ⊂ SO(3)_R with fixed points ±n̂₀ ∈ S², commuting with the twisted SL(2,ℝ); (reg) at one face point p₊ ∈ C₄ over n̂₀ and one face point p₋ ∈ C₄ over −n̂₀. U(1)_R is not needed.
  - Proof:
    1. At p± the twist lock holds (E5-2 needs only H_Σ). The K-fixed space V_p is 3-dimensional and contains n; ξ fixes n, so the ξ-rotation plane is P_p = n^⊥ ∩ V_p = T_pS² (as in A1 step 3).
    2. Orient P_p by (x, W, n, P) positive, with W = Σ ⊕ m oriented by K. Then the locked, Γ^n = +1, fixed-χ₄ space is 4-dimensional and Γ^P acts on it as the single value i s₃*(χ₄), **the same for n = +e_r and n = −e_r** (log T1-a, T1-b). With (or), o_p(P) is the restriction of one global orientation of S² (o(face) = o(x)∧o(W)∧o(P), with W coordinate-oriented identically at both poles).
    3. A rotation of S² has weight +1 at one pole and −1 at the other with respect to any global orientation (log T1-c, exact linearisation).
    4. For a Killing spinor with L_ξε = iqε: q = +s₃*/2 from p₊ and q = −s₃*/2 from p₋ (log T1-d). Contradiction. ∎
  - Covers **[w]∩H_Σ for all Killing spinors**, including the unlocked/KK spinors outside the 3-scalar truncation (the E1-4 sub-item "[w] with KK spinors") and therefore S2-11's "other gravitino eigenvalues" question **beyond the truncation, on H_Σ**. E1-3 stays CONDITIONAL as filed and is not needed for this BPS no-go.
  - **Note for PP (no label, no regrade):** E1-1's graded content (at (z, n̂₀) the SO(2) charge is ±½ with the sign fixed by χ₄) is used here unchanged. Its gloss "No contradiction arises" holds only when (reg) is available at a single fixed-point section. With (reg) also over −n̂₀, A5 gives a contradiction. Flagged for audit; E1-1 is not regraded by this file.
- **T552-A6 (PROVED, implication; exact sign table). Diagonal circles: closed unless |a| = |b| and every Killing spinor is neutral.**
  - Branch: SO(3)_R × U(1)_R broken to a diagonal U(1)_{a,b} acting with weight a on (μ₁,μ₂) and b on (μ₃,μ₄) (a, b ≠ 0, (lin)). Its fixed set in the face slice is Σ_{n̂₀} ⊔ Σ_{−n̂₀} (2-dimensional), so A1 does not apply.
  - Premises: (h0), (h1), (P-a), (ii), (or), (lin), (F-4) including the vacuum twist degree, so that the pole-section lines have the PP-accepted E2-3 degrees (locked 0, unlocked ±(2g−2) = ±2; Erratum 25 Fix 5); (reg-all) on Σ_{±n̂₀} ∩ face.
  - Proof: at Σ_{n̂₀} the weights on (m, P) are (a, b), and at Σ_{−n̂₀} they are (a, −b) in the o_p orientation (A5 step 3). When a s₂′ + b s₃ = 2q has a unique sign solution at both poles, s₂′ agrees, s₃ flips, and by CH s₁ flips (log D-1a, D-1b). So exactly one pole section carries ε in an unlocked line of degree ±2, which contradicts nonvanishing.
  - The non-unique cases are exactly |a| = |b| with q = 0 (log D-1c). For q ≠ 0 the charged half-lines are canonical even when |a| = |b|.
- **T552-A7 (OPEN). Residual E1-4.**
  - (i) R-symmetry broken to a finite group or to nothing (no circle with a fixed set of dimension ≥ 2), with or without H_Σ. On E1∩H_Σ the lock and CH still give a single s₃ at regular points of C₄, but the rank-2 bundle (two locked lines ⊠ O(s₃)) has c₂ = 0, so FX gives nothing.
  - (ii) Diagonal U(1)_{a,b} with |a| = |b| and all Killing spinors neutral.
  - (iii) Any branch of A3–A6 whose face is singular on the relevant fixed set (→ A8, A10).
  - (iv) Non-linear R-actions on the face bundle (failure of (lin)).
  - E1-4 is narrowed to (i)–(iv). It is not closed.

## 3. E4: singular fixed sets
- **T552-A8 (PROVED, implication). Phase-regularity criterion.**
  - Setting: the premises of A3, A4 or A6, with (reg-F) replaced by "regular on F∖Z" for a closed Z ⊂ F, where the topological bundle E over all of F is the one from (F-4top).
  - (PR) Z is phase-regular if ε/|ε| (a section of E over F∖Z) extends continuously over Z.
  - Then under (PR) the A1/A6 contradiction persists, because ε/|ε| is a global nowhere-zero section.
  - Contrapositive (relative Euler class additivity): a BPS face can evade A3/A4 only if its singular set is **not** phase-regular and carries total relative Euler number e(E, ε)[Z] = c₂(E)[F] = ±(2g−2) = ±2.
  - Applications:
    - **H_Σ∩SO(3)_R singular on all of C₄** (the E4-6 main case): use F = F₄(n̂), Z ⊇ Σ×{±n̂} = F₄∩C₄. If F₄∖C₄ is regular, the escape needs index ±2 concentrated on Σ×{±n̂}.
    - **E2 (SO(3)_R×U(1)_R) with partial singularity Z_Σ×S² ⊂ C₄**: SO(3)_R-invariance makes the singular set meet every F₄(n̂). Same criterion on C₄ or F₄(n̂).
- **T552-A9 (CONDITIONAL). Harmonic (smeared-M5 / α-sheet) singularities are phase-regular.**
  - In the leading-order local model ε = H^{−1/12}ε₀, with ε₀ constant in block-rescaled coordinate frames (H = 1 + Q/ρ after smearing), the rescaled frames extend continuously across Z. So ε/|ε| = ε₀/|ε₀| extends, which is (PR).
  - **Conditions:** the local model is the standard harmonic-function M5 ansatz (cited, not derived for this face). Corrections from the HW boundary, the twist and the flux are not controlled.
  - If audited, the α-sheet densities of E4-3 (restated) cannot evade A3/A4, and the E4-6 main case reduces to spinor-winding (non-PR) defects.
- **T552-A10 (OPEN). Residual E4-6.**
  - Non-phase-regular singular loci carrying total index ±2 (for example conical or frame-winding defects along Σ×{±n̂} or along C₄).
  - Singularities on F₄∖C₄, in particular on the SO(3)_R-fixed circle bundle (PP's non-exhaustive α-sheet counterexample support).
  - Distributional D1/CH at a singular C₄. Not derived.
- **T552-A11 (CONDITIONAL). Failure of (F-4) on E2 keeping the linear form does not escape.**
  - If the face slice is S(𝓛′⊕V₃′) for any line 𝓛′ and any oriented rank-3 V₃′, with U(1)_R rotating 𝓛′, then C₄ = S(V₃′) has χ = −4, σ = 0, and det E pulled back from Σ (c₁² = 0).
  - So c₂(W^±) = (c₁² − 2χ ∓ 3σ)/4 and its W^− analogue give c₂(E) = ±2 ≠ 0.
  - Trivial V₃′ with any deg 𝓛′ is already PROVED inside A3 (FX-2c). Nontrivial V₃′ uses the textbook spinᶜ formula c₂(W^±) = (c₁² − 2χ ∓ 3σ)/4 (Gompf–Stipsicz / Morgan), cited and not re-derived. **CONDITIONAL on that citation.**
  - Failures of (F-4) that change the fixed-set topology or the linear form stay in A10/A7(iv).

## 4. S2-8 / P8-3
- **T552-A12 (PROVED, implication). Where the BPS PDE is still needed, and why it is not an (r,χ) system there.**
  - An (r,χ) cohomogeneity-2 reduction of the 7-dimensional internal space needs 5-dimensional orbits: H_Σ (2) + SO(3)_R×U(1)_R generic fibre orbits S²×S¹ (3). Any smaller connected remnant leaves cohomogeneity ≥ 3: T² gives (r,χ,θ); SO(3)_R alone gives 3; a diagonal U(1) gives 4; nothing gives 5, and dropping H_Σ adds 2.
  - On the full-symmetry branch, walls are excluded without any PDE (E5-4 and E2-4, PP-accepted; A3).
  - After A3–A6 the BPS system is needed **only** on the residual branches A7(i)–(iv) and A10, which all have cohomogeneity ≥ 4 (with H_Σ) or ≥ 6 (without).
  - P8-2's reading (LLM/Toda needs an AdS₅ factor and SU(2)×U(1) isometries) stays CONDITIONAL as filed. On the residual branches the isometry hypothesis (B) fails by construction, so no Toda reduction is available.
- **T552-A13 (OPEN). P8-3 in narrowed form.**
  - The Poincaré BPS system on the A7/A10 residual branches (cohomogeneity ≥ 4, at most a neutral diagonal circle) has not been derived.
  - A suggested next step (not done): a spinor-bilinear (G-structure) analysis of one chiral Poincaré Killing spinor, using A1's "chiral on every fixed 4-manifold" as a boundary condition.

## 5. Branch register (t4436; not counted; nothing adopted; proposals pending PP audit)
- **Proposed drops on PROVED implications, pending PP audit** (not dropped by this file):
  - U(1)_R-kept branches with (reg-F) on C₄ (A3: E2∩E1∩U(1)_R, E1∩H_Σ∩U(1)_R);
  - SO(2) ⊂ SO(3)_R-kept branches with (reg-F) on F₄(n̂) (A4: E5∩¬H_Σ, E1 with an SO(2) remnant);
  - E1∩H_Σ with an SO(2) remnant and (reg) at the two poles (A5: [w]∩H_Σ for all Killing spinors);
  - diagonal-U(1) branches except the |a| = |b| neutral case (A6).
- **Kept, OPEN:** A7(i)–(iv), A10, A13; non-BPS items are in the companion Z2/S5 file of this time.
- **[χS]:** kept. δ-support on C₄ is in A8/A10; harmonic-type δ-support is in A9 (CONDITIONAL).
- **[χU]:** kept. Covered by A3/A4 when its wall content is regular on the relevant fixed set.
- **[w]/Z2:** kept. BPS: [w]∩H_Σ proposed drop (A5, also A3/A4). Non-BPS: OPEN (companion file).
- Already PP-accepted drops are unchanged and not re-opened: E5∩H_Σ∩SO(3)_R (E5-4), E2∩(SO(3)_R×U(1)_R) (E2-4), E3, S5 (BPS only). S2-7 stays CONDITIONAL. E4-3 is used only in its restated form.

## 6. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 8 | A1, A2, A3, A4, A5, A6, A8, A12 |
| CONDITIONAL | 2 | A9, A11 |
| OPEN | 3 | A7, A10, A13 |
| REFUTED | 0 | — |

Check: 8 + 2 + 3 + 0 = 13.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before this write, 12:09:21 CST; after-write check reported to NL).
