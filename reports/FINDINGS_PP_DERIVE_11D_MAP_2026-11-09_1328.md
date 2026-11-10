# FINDINGS — PP DERIVE item (2): the 11D map — 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. Tip 7cddb188… untouched. No CERT. Nothing sent outside.
Authority: OW 68a2b8e1f14e8722… and OW 33d25a790fb1e0da…. LOCK 96f8d42e… read: §4 purges Kronecker/four-force projection mappings, and none is used or revived here. The EH-ds Appendix D phrase "4D Einstein plus the five projections" is deliberately NOT used.
Scripts/logs: /workspace/audit-scratch/pp_derive_1320/item2_map.py (.log), item2_depth_mp.py (.log; 80-digit mpmath), geom.py.

## Rollup
PROVED 4 · CONDITIONAL 3 · OPEN 1 · REFUTED 1.
Verdict: **OPEN as an Owner object.** No Owner record defines "the 11D map". Search of 564 OWNER_WRITE* files: "11D map" appears only in the 1320 authorization itself. OW 9ee0f248 (ae380bf6…) names the goal of merging the "Einstein–Hampton 11D" stream, but defines nothing. Auditor B13 §6 is CONFIRMED.
The two maps the corpus actually uses are treated below as DERIVED PROPOSALS.

## Part A — tree map Φ: T₃ → H^n (the "embedding" of the compendium / Bridge C)
On-disk sources: OWNER_DOCUMENT_ENGINEERING_MATH_DELIVERY_PR_LAMBDA_QI_AB_2026-11-05.md (a5ab59f4…, l.14) has both "isometric embedding Φ: T₃ → H²" and "QI into H¹¹" (a contradiction Soft SF kept). Compendium claim C10 is NL 96f81064…/FINDINGS_NL_COMPENDIUM_LANE_REVIEW.

- **A1 (PROVED, then REFUTED claim).** No tree with a vertex of degree ≥ 3 embeds isometrically into H^n for any n, or into any Riemannian manifold, or into any space whose geodesics do not branch.
  - Proof: take a vertex v with neighbours a, b, c. Then d(a,b) = d(a,v) + d(v,b) = 2, so v is the midpoint of the unique H^n-geodesic from a to b. The same holds for a and c. A geodesic from a through v continues uniquely beyond v, so Φ(b) = Φ(c), which contradicts injectivity. ∎
  - The numeric check (item2_map.log A1) agrees: the unique direction is θ = 0.
  - So the claim "isometric embedding of T₃ (degree 4) into H²/H¹¹" is **REFUTED**.
- **A2 (CONDITIONAL → numerically PROVED to depth 7).** Construction: send each edge to a geodesic of length L in H² and fix all angles at vertices to π/2, so the four directions are orthogonal. With L = 3, the bounds
  (L − ln 2)·d_T − 0.203 ≤ d_H ≤ L·d_T
  hold on 300-node samples at depths 5, 6 and 7, which have 485, 1457 and 4373 nodes. The additive constant −0.202954 is identical at every depth, so the defect is bounded. Here ln 2 is the asymptotic corner defect for a right angle.
  - Full QI for the infinite tree follows from the standard local-to-global lemma for piecewise geodesics with long segments and angles bounded below in H² (e.g. Bridson–Haefliger III.H.1.13). That lemma is cited, not re-proved, so A2 is CONDITIONAL on it.
  - At L = 1 the map is not injective (min ratio 0.0044), so L must be large.
- **A3 (PROVED).** Composing with a totally geodesic H² ⊂ H¹¹ gives a QI embedding T₃ → H¹¹ with the same constants. So "QI into H¹¹" is true but carries no information beyond H². Corollary: a QI fixes distances only up to (λ, c), so it cannot pin a numerical R_c. This agrees with Local AMEND 6bd6d814 and is **PROVED**.
- **DP-MapA (DERIVED PROPOSAL).** Φ_L: T₃ → H² ⊂ H¹¹ with right-angle placement and edge length L. L stays a free parameter, and choosing it is an Owner decision.

## Part B — dimensional-reduction map 11D → 4D, "G₄ = G₁₁/V₇eff" (EH appendix 08b8541a…, §1)
Source metric (corpus, not an Owner record): nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt sha 08b8541aa4a96b680fe1404ad3e722191308ede39 (EH-ds):
ds² = e^{−2A(y)} g₄(x) + dy² + e^{2B} ĝ₆, with faces at y = 0 (+U) and y = b (−U).
- **B1 (PROVED, sympy).** For g₄ = FRW, R₁₁ ⊃ e^{2A}R₄. With A = ky, R₅ − e^{2A}R₄ = −20k², which is x-independent. So the 4D Einstein–Hilbert coefficient per unit fibre volume is √(−g)·e^{2A} = e^{−2A}e^{6B}.
- **B2 (PROVED, sympy).** V₇eff = V̂₆ e^{6B} ∫₀^b e^{−2ky} dy = V̂₆ e^{6B} (1 − e^{−2kb})/(2k). Therefore 1/G₄ = V₇eff/G₁₁. The EH note leaves "V₇eff" undefined, and this supplies it. As kb → ∞, V₇eff → V̂₆ e^{6B}/(2k), which is RS-like.
- **B3 (CONDITIONAL on DP-metric of item 3).** For the fibre S⁴ × Σ_g, V̂₆ = (8π²/3) r⁴ · 4π(g−1)ρ², with r = √6/(4k) and ρ = 1/(2k). The genus g ≥ 2 is needed for finite volume, because H² itself has infinite volume. Then V₇eff = (8π²/3)(9/(64k⁴)) · 4π(g−1)/(4k²) · (1 − e^{−2kb})/(2k).
- **OPEN.** Which of A or B (or a third map, such as the P_rev bridge ι of B2) the Owner means by "the 11D map".

## Owner decisions needed
- **D-Map-1.** Name what "the 11D map" is: the tree map Φ, the reduction 11D → 4D, or something else.
- **D-Map-2.** If it is Φ, adopt the QI version (A2) in place of the refuted isometric version, and fix L.
- **D-Map-3.** If it is the reduction, adopt V₇eff from B2, and fix b and the genus g if DP-metric is adopted.
