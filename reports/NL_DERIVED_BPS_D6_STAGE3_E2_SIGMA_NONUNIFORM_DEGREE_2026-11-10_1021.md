# NL DERIVED: D6 stage 3 (e), E2: data not uniform on Σ (Bolza). A degree obstruction
2026-11-10, 1021 CST (America/Chicago). **NL derived proposal.** Additive only. Authority: Owner call-83d7a0fa (e72a188b…), OW t4436 (32881263…), OW t4431. Inputs: 2216 (f504d1b9…), PP f530cbc0…, Erratum 23/24, E5 file of today (0a7d8e56…, Lemma CH). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged. No candidate wall.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.
Scripts (sidecars frozen before the runs, logs sealed after):
- /workspace/nl-d6s3-1110/chirality_hw_lock_exact_2026-11-10.py (3ed7f879…) / .log (676f7dc8…);
- /workspace/nl-d6s3-1110/e2_pairs_degree_exact_2026-11-10.py / .log (hashes in the sidecars; this script re-executes the frozen chirality script and adds checks [A]–[C]).
All tests are exact (ℚ(i) ranks and equalities).
**Borel density is not used anywhere in this file.** The twist lock S2-4 is **not** assumed here, since it needs H_Σ.

**Tally: PROVED 4 · CONDITIONAL 0 · OPEN 1 · REFUTED 0 · total 5.**

## 0. Scope and premises
- **E2:** data on Bolza Σ are not assumed uniform (H_Σ dropped). SO(3)_R × U(1)_R are kept. E2∩E5 and E2∩E1 are dealt with in §3.
- Premises:
  - (h1) flat Poincaré slicing with no flux carrying 1–3 x-legs;
  - (P-a) at least one Killing spinor;
  - (ii) the HW ℤ₂ projection Γ^nε = ε on the face (record premise S6);
  - (reg-all) on the whole face part of C₄ the metric is smooth and nondegenerate and ε is continuous;
  - (F-4) the face bundle is isomorphic to the vacuum twisted bundle, and C₄ (the U(1)_R-fixed set on the face) is isotopic to the vacuum one;
  - (gr) near C₄ the wall is a graph over C₄, i.e. n·∂_r > 0 there;
  - Σ is connected of genus g = 2.
- Σ_n̂ := {(z, n̂)} ⊂ C₄ is the "north-pole" section. SO(3)_R acts only on the S² factor of C₄ ≅ Σ×S², since the μ_α directions are untwisted, so the stabiliser U(1)_n̂ is the same for all z.

## 1. Local structure without uniformity
- **E2-1 (PROVED). S2-3 holds without H_Σ.** Its proof uses only:
  - injectivity of ev_p for parallel sections;
  - the U(1)_n̂ weights ±½ at p ∈ C₄;
  - that U(1)_R fixes C₄ pointwise, acts there as ½Γ^{m1m2}, and commutes with SU(2)_R.

  So on E2 the Killing spinors form SU(2)_R doublets, and at each p ∈ C₄ the two members have the same s₂′ and opposite s₃.
- **E2-2 (PROVED; exact). Sector content at a wall point of C₄.**
  - At p ∈ C₄∩face, U(1)_R rotates (m1,m2) and U(1)_n̂ rotates (t,f). So n ∈ span(r, S1, S2), and the tangential face flux is spanned by f₄, ω₁, ω₂ in the adapted frame (n, T1, T2, m, t, f), where T1, T2 ⟂ n are tangent to C₄. By (gr), the T-plane bundle over Σ_n̂ is homotopic to TΣ.
  - Choose a doublet with fixed χ₄ (Lemma CH, E5-3(b)).
  - With s₂′ and χ₄ fixed and Γ^n = +1, log [5] shows that **s₁s₃ is fixed**.
  - Hence each member is **single-sector at every wall point of C₄**: ε₊ in (s₁*, s₂′, +) and ε₋ in (−s₁*, s₂′, −), with s₁* determined by (χ₄, s₂′).
  - **Exactly one of the two members is unlocked** (s₁ = s₂′) at every such point.
  - Flux table, from e2_pairs log [A] (both σ, both s₂′):

    | Partner relation | Realisable at one χ₄? | Forced by equal D1 K |
    |---|---|---|
    | same s₁, opposite s₃ | No | f₄ = ω₂ = 0 (PP C1) |
    | opposite s₁, same s₃ | No | ω₁ = ω₂ = 0 |
    | opposite s₁, opposite s₃ | **Yes, the only realisable pair** | f₄ = ω₁ = 0, ω₂ free (PP C2) |

  - So on E2 **the D1/flux route alone leaves ω₂ free**, and the Bianchi/topology contradiction of S2-7 does not close E2.
- **E2-3 (PROVED). Line-bundle degrees on Σ_n̂.**
  - Fixing χ₄, the Lorentz weight Γ^{12} and (s₁, s₂′, s₃) leaves a 1-dimensional space (log [C]: all such joint spaces have dimension 1). So the sector parts of a Lorentz-weight Killing spinor restricted to Σ_n̂ are sections of complex **line** bundles ℓ(s₁, s₂′, s₃; χ₄, Γ^{12}).
  - Constant x-frame gammas Γ^μ flip χ₄ (and Γ^r) or Γ^{12} and are globally defined. Clifford multiplication by e_t, a trivial line over Σ_n̂, flips s₃ (log [B]: Γ^t keeps s₁, s₂′, χ₄ and Γ^{12}). So the degree depends only on (s₁, s₂′).
  - **Locked lines are trivial.** At the MN2 vacuum (S2-1, exact), each Lorentz-weight, U(1)_R-charge, SU(2)_R-weight Killing spinor is locked and single-sector at C₄ and vanishes nowhere. That gives a nowhere-zero section of a locked line, and by (F-4) and (gr) the face lines are isomorphic to the vacuum ones.
  - **Unlocked lines have degree ±(2g−2) = ±2 ≠ 0.** Clifford multiplication by T^{1,0} (or T^{0,1}) maps ℓ(−s₁, …) isomorphically onto ℓ(s₁, …): log [B] shows Γ^{S1} flips s₁ (and Γ^r) and keeps s₂′, s₃, χ₄ and Γ^{12}. So ℓ_unlocked ≅ T^{1,0}⊗ℓ_locked or T^{0,1}⊗ℓ_locked, of degree 2−2g or 2g−2.

## 2. The E2 no-go
- **E2-4 (PROVED, implication). No HW-BPS wall on E2 with SO(3)_R × U(1)_R.**
  - Premises: those of §0.
  - Proof:
    1. Pick ε ∈ K_ℂ that is a simultaneous eigenvector of χ₄, Γ^{12}, the U(1)_R charge and the SU(2)_R weight +½. These operators commute with each other and with the KSE. Lorentz acts on x-independent Killing spinors algebraically by Γ^{μν}.
    2. Let ε′ = T₋ε be its partner.
    3. By E2-2, one of ε, ε′ restricted to Σ_n̂ (on the face) lies entirely in an unlocked line ℓ. It vanishes nowhere, because parallel sections vanish nowhere and (reg-all) holds.
    4. So ℓ is trivial, which contradicts deg ℓ = ±2 (E2-3). ∎
  - **Not used:** H_Σ, the twist lock, Borel density, ω₂ or its zero set, N_face, Bianchi, the IR endpoint, the D1 rows, and the source profile n(χ), provided (reg-all) holds.
  - It covers **[χU] and [χS]** whenever their wall content leaves the face regular along all of C₄. δ-support at χ = π/2 goes to E4.
  - Under t4436, E2∩(SO(3)_R×U(1)_R) is **proposed for dropping on this PROVED implication, pending PP audit**. It is not dropped by this file.
  - Genus matters: on a torus (g = 1) the unlocked degree would be 0 and the argument would fail. On Bolza (g = 2) it applies.

## 3. What remains
- **E2-5 (OPEN).**
  - **E2∩E5** (no H_Σ and no U(1)_R): no global s₂′, no lock. CH gives only that s₁s₂′s₃ is fixed. Line bundles split by (s₁, s₂′) are not defined without U(1)_R (Γ^{m1m2} is not a symmetry, and the m-plane needs a K- or U(1)_R-fixed structure to be defined at C₄). Not closed.
  - **E2∩E1** (SO(3)_R broken): no doublets. Not closed.
  - E2-4 also needs (reg-all) on **all** of C₄∩face, unlike E5-4, which needs one point. A face that is singular on a nonempty subset of C₄ is not covered. That case is part of E4, and in H_Σ it is all-or-nothing by homogeneity, but not on E2.

## 4. Branch register (t4436; not counted)
- **[χS], [χU]:** kept; covered by E2-4 when (reg-all) holds.
- **[w] / Z2:** kept (E1).
- **E2∩(SO(3)_R×U(1)_R):** proposed drop on E2-4, pending PP audit.
- **E2∩E5, E2∩E1, and E2 with partial face singularity on C₄:** OPEN (E2-5).
- Other branches are unchanged from the E5 file register. S6 is a record premise.

## 5. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 4 | E2-1, E2-2, E2-3, E2-4 |
| CONDITIONAL | 0 | — |
| OPEN | 1 | E2-5 |
| REFUTED | 0 | — |

Check: 4 + 0 + 1 + 0 = 5.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
