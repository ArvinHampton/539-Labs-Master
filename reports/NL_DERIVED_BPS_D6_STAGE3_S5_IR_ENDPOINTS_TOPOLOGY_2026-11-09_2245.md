# NL DERIVED: D6 stage 3 (b), S5: other IR endpoints or a singular IR
2026-11-09, 2245 CST (America/Chicago). **NL derived proposal.** Additive only. Authority: OW t4426 and OW t4436. Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.
Script: /workspace/nl-d6s3/s5_topology_w3crit.py (d8d9cc9b…, sidecar frozen before the run), log sealed after.

**Tally: PROVED 3 · CONDITIONAL 0 · OPEN 1 · REFUTED 0 · total 4.** **No candidate wall.**

- **S3b-1 (PROVED; exact).** **W₃ has exactly one critical point: MN2.**
  - ∂_wW₃ = (g/2)e^{−2φ+4λ}e^{−2w}(e^w − 1)(e^{2w} + e^w + 1). This vanishes only at w = 0.
  - At w = 0, sympy gives the unique positive solution e^{2φ} = 2^{1/15} and e^{2λ} = 2^{1/5}, i.e. e^{30φ} = e^{10λ} = 2.
  - So every BPS (W₃) kept side in the 3-scalar truncation either ends at MN2 or has a singular IR. There is no other regular BPS IR endpoint.
- **S3b-2 (PROVED).** For any oriented S⁴-bundle M₆ over Bolza, **b₄(M₆) = 1**. Proof:
  - The Serre spectral sequence has E₂^{p,q} = H^p(Σ)⊗H^q(S⁴), with q ∈ {0, 4}.
  - Its only possible differential is d₅ : E^{p,4} → E^{p+5,0}, which vanishes because p+5 > 2. So the sequence degenerates.
  - The Betti numbers are (1,4,1,0,1,4,1).

  Consequences:
  - On a smooth face slice, the closed restriction G|_face has a class fixed rationally by N_face = ∫_{S⁴}G.
  - Hence ∫_{C₄}G|_face = k·N_face, where k = Φ_tw^{vac}/N^{vac} is a topological constant.
  - k ≠ 0, because the vacuum period Φ_tw = (l/g)·vol(Σ)·4π ≠ 0, which forces [C₄] ≠ 0 in H₄(ℝ) ≅ ℝ. The class of the U(1)_R fixed locus does not change under smooth deformation within the bundle.
- **S3b-3 (PROVED, as an implication).** In S2-7 (as completed in Erratum 23), the premises "IR-regular to MN2" (S5) and "homology of C₄ from the face to the IR" can be **replaced** by a premise at the face alone:
  - the face slice is the twisted S⁴ bundle;
  - C₄ is smooth, with no sources meeting it;
  - N_face ≠ 0.

  Then S2-6 (ω₂|face = 0) contradicts k·N_face ≠ 0 whatever the IR is. So **other IR endpoints and a singular IR do not escape the BPS no-go.**
  - Under OW t4436, the S5 escape is **dropped for BPS walls** on this PROVED implication.
  - S2-7 stays **CONDITIONAL** on its remaining premises.
  - This applies to both [χS] and [χU].
- **S3b-4 (OPEN).** S5 for **non-BPS** (NEC) walls with a singular-IR kept side was not addressed. It is kept as a branch, alongside Z2 (S2-13).

Tally check: 3 + 0 + 1 + 0 = 4. Branches:
- S5 (BPS): dropped.
- S5 (non-BPS): kept, OPEN.
- [χS], [χU], [w]: kept.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
