# order24 RESULTS
PREREG sha256 c5257ac3abb64811536778582c25bd6f5d0e9f01250901507dfbfb243bfc9d6d (RG12, RG13 hashed before numerics). MAPS_ADDENDUM sha256 5bad575bd9d3df31294276d9a8f62880fd903b348ed62f0eda475b71db83f1dc (RG14, hashed after RG12/13 verdicts and before its own run).
| test | value | verdict |
|---|---|---|
| C1 corner formula reproduces CO, SCO | 0.0 | PASS |
| C2 transport Γ_γ^{±1}·CO = Cor_{γ^{∓1}K} (x, −1/x) | 1.6e−14 | PASS |
| C3 commutator ‖Γ_γM − MΓ_γ‖ | 0.0 | (reported) |
| reference: CO under the law | abs 54.4, rel 0.0586 | FAIL (order19) |
| **RG12** γ-average ⅓(Cor_γK + Cor_K + Cor_γ⁻¹K) | abs 23.5 (‖S‖ 607), rel 0.0387; non-vacuity 1.07 | **FAIL** |
| **RG13** γ-defect Cor_γ⁻¹K − Cor_K | abs 104.1 (‖S‖ 1489), rel 0.0699; non-vacuity 1.60 | **FAIL** |
| **RG14** full-orbit average (Γ_γ has order 2; rank Π = 60) | abs 15.9 (‖S‖ 554), rel 0.0287; non-vacuity 0.60 | **FAIL** |
## Reading
Neither γ-construction explains the near-law. Averaging over the γ-orbit lowers the relative defect (0.059 → 0.039 → 0.029) but never below the 1e−3 FAIL line. Because Γ_γ commutes with M and has order 2 on the companions, every γ-average's defect is the image of the CO defect under a polynomial in Γ_γ; the full-orbit projector keeps 60 of 105 dimensions and the defect has a nonzero component there.
## Category A / B
- A (finite exact facts, stated): transport (v8 Prop. transport); Γ_γ has order 2 on the 105 companions and commutes with M (both checked to machine zero on monomial matrices; an exact exponent check would make them formal); hence Cor_{γ^{-2}K} = Cor_K.
- B: all law residuals.
No v9 (no substantial new theorem).
