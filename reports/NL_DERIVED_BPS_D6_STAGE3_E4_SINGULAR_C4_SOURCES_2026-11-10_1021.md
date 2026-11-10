# NL DERIVED: D6 stage 3 (d), E4: singular or degenerate C₄, or sources meeting C₄
2026-11-10, 1021 CST (America/Chicago). **NL derived proposal.** Additive only. Authority: Owner call-83d7a0fa (e72a188b…), OW t4436 (32881263…), OW t4431. Inputs: 2216 (f504d1b9…), 2245 S5 file (3ceb0605…), PP 113e8035…, Erratum 24 (60bbc718…), E5 file (0a7d8e56…, Lemma CH and E5-4), E2 file (197c5bd1…, E2-4). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged. No candidate wall.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after. No new script: the arguments are analytic, and the Clifford facts used are those of chirality_hw_lock_exact_2026-11-10.log (676f7dc8…).

**Tally: PROVED 5 · CONDITIONAL 0 · OPEN 1 · REFUTED 0 · total 6.**

Note on order: the E2 file (1021) was filed before this one because E4's premise map uses E2-4. The content is independent of the filing order.

## 0. The two obstructions whose premises E4 attacks
- **(T+L), the flux route of S2-7 (as completed in Erratum 23/24).**
  - (T) Topology: ∫_{C₄}G|_face = k·N_face ≠ 0. This needs dG = 0 on the face slice and C₄ a cycle in the vacuum class.
  - (L) Local algebra: ω₂ = 0 at a point of C₄ (S2-6), which needs finite face data and D1 there.
- **(CH), the flux-free route.**
  - E5-4 (H_Σ, SO(3)_R) needs regular data at **one** face point of C₄.
  - E2-4 (SO(3)_R×U(1)_R) needs regular data on **all** of C₄∩face.
  - Neither uses G, Bianchi or sources.

## 1. Results
- **E4-1 (PROVED). Homogeneity of C₄ in H_Σ∩SO(3)_R.**
  - On the H² lift, SL(2,ℝ) acts transitively on H². It acts on the fibre through U(1)_R, which fixes {μ_a = 0} pointwise. SO(3)_R acts transitively on the S² = {μ_a = 0} ⊂ S⁴, and the two actions commute.
  - So the symmetry group acts transitively on C₄ = Σ̃×S², and every pointwise property of the data (smoothness, nondegeneracy, continuity of ε) holds at all points of C₄ or at none.
  - Consequence: in H_Σ∩SO(3)_R, the premise (reg) of E5-4 fails **only if the data are singular on all of C₄**.
- **E4-2 (PROVED). Degenerate C₄ forces a singular metric.**
  - If the face-slice metric is smooth and nondegenerate near C₄, the fixed set of the compact group K (in H_Σ), or of U(1)_R (on E2), is a smooth closed totally geodesic submanifold. Proof: exp_p is equivariant, so near a fixed point p the fixed set is exp_p of the fixed subspace of T_p.
  - By (tw) or F-4 it is the vacuum set {μ_a = 0}, a smooth 4-manifold Σ×S².
  - So "degenerate C₄" (a collapsing Σ or S², or a change of dimension) can occur only where the metric itself is singular or degenerate. Degenerate C₄ is therefore a special case of a singular C₄.
- **E4-3 (PROVED). Invariant localised sources meet C₄ only as copies of C₄.**
  - Take a source whose support is a submanifold of dimension 4+2 (an M5-type source localised in the internal space) and is invariant under the H_Σ lift and SO(3)_R.
  - Its support Ŝ in the lift is a union over H² of K-invariant sets Ŝ_p̃ in the fibre (r included). Since dim Ŝ = 2, the sets Ŝ_p̃ are finite. A connected K fixes each point of a finite invariant set, so **Ŝ_p̃ ⊂ Fix K = {μ_a = 0} × {r-values}**.
  - SO(3)_R-invariance then forces smearing over S². So the support is a union of r-translates of C₄: an x×Σ M5 density smeared on the S² at μ_a = 0, which are the α sheets of D6-2/D6-3.
  - Such a source **meets** C₄∩face only if it sits on the face slice, and then it sits on all of it. Sources at r ≠ r_face never meet C₄∩face.
- **E4-4 (PROVED). Stokes identity for face-slice sources (flux route).**
  - Suppose G|_face satisfies d(G|_face) = j₅, a 5-current on the face slice M₆, with the fibre S⁴_ref and C₄ disjoint from supp j₅. Let B be a rational 5-chain with ∂B = C₄ − k·S⁴_ref, which exists because [C₄] = k[S⁴] in H₄(M₆;ℚ) (S3b-2).
  - Then **∫_{C₄}G − k·∫_{S⁴_ref}G = ∫_B j₅**.
  - So (T) fails exactly when face-slice sources have nonzero flux through B. Under symmetry, ω₂·Vol(C₄) = k·N_face + ∫_B j₅, and (L)'s ω₂ = 0 would require ∫_B j₅ = −k·N_face.
  - This escapes the **flux route only**. It does not escape CH (E5-4, E2-4), which never uses G.
- **E4-5 (PROVED, implication). Premise map for E4.**
  - In **H_Σ∩SO(3)_R**: a BPS HW wall evades E5-4 only if, at **every** point of C₄∩face (E4-1), at least one of the following holds:
    - (a) the metric is singular or degenerate (this includes degenerate C₄, E4-2);
    - (b) ε or the supercovariant connection is not continuous up to the face;
    - (c) the face is not a C¹ hypersurface there, so Γ^n is undefined.

    Sources that keep (a)–(c) false (smooth wall densities, sources off the face slice, bulk sources) **do not evade** E5-4, even when they evade the flux route through E4-4.
  - On **E2∩(SO(3)_R×U(1)_R)**: E2-4 is evaded by (a)–(c) holding on **any nonempty** subset of C₄∩face, since (reg-all) is needed.
  - By E4-3, in H_Σ∩SO(3)_R the natural sources realising (a)/(b) on C₄ are S²-smeared x×Σ M5 densities sitting on C₄ on the face slice: the α sheets.
  - **[χS]** profiles with δ-support at χ = π/2 (that is, on C₄) belong here. **[χU]**, if its wall content is smooth at χ = π/2, does not evade CH.

## 2. What stays open
- **E4-6 (OPEN).** It is not known whether a BPS HW wall exists whose face is singular on all of C₄ (in H_Σ∩SO(3)_R) or on part of it (on E2), for example with α-sheet M5 densities on C₄. Then D1 would hold only off C₄, or distributionally.
  - No distributional version of D1 or of CH at a singular C₄ was derived.
  - The branch is kept. It is the main surviving BPS escape inside SO(3)_R-invariant configurations, together with E2∩E5.

## 3. Branch register (t4436; not counted)
- **E4:** kept, OPEN (E4-6) and narrowed by E4-5 to "singular along C₄". Smooth sources, sources off C₄ and degenerate-but-smooth cases are ruled out of the escape by E4-2 and E4-5. This narrowing is proposed, pending PP audit.
- **[χS]:** kept. δ-at-C₄ profiles are in E4.
- **[χU]:** kept.
- **[w] / Z2:** kept (E1).
- Other branches are as in the E5 and E2 registers. S6 is a record premise.

## 4. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 5 | E4-1, E4-2, E4-3, E4-4, E4-5 |
| CONDITIONAL | 0 | — |
| OPEN | 1 | E4-6 |
| REFUTED | 0 | — |

Check: 5 + 0 + 1 + 0 = 6.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
