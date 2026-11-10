# order22 RESULTS
PREREG sha256 f7ca80834e5c3ddf5a1b454f69164ac52451ac45f600381d06a7039b31cf0982 (hashed before numerics; Maps RG9, RG9b hashed there).
| test | value | verdict |
|---|---|---|
| C1 general corner formula on (e1,e2) reproduces A2_corner | max abs 0.0 | PASS |
| C2 Γ·G = G (γ-invariance of the Gauss means) | 1.8e−16 | PASS |
| **Map RG9**: Γ·A2_corner = Corner_{γ⁻¹K} | e9 = 5.6e−15; non-vacuity ‖Γ·A2c − A2c‖/‖A2c‖ = 1.60 | **PASS (non-vacuous)** |
| **Map RG9b**: Corner(e1,(1,1)) + Corner((1,1),e2) = Corner(e1,e2) | max abs 0.250 | **FAIL** |
## Reading
- RG9: the unit γ does not preserve the corner term (defect 160% of its norm), and it moves it exactly to the corner invariant of the transported cone γ⁻¹K = cone((13,−2),(7,−1)). The γ-defect of A2_corner is therefore entirely geometric: Γ·A2c − A2c = Corner_{γ⁻¹K} − Corner_K.
- RG9b FAIL is recorded by rule. Post-hoc explanation (not a pass): the preregistered additivity ignored the vertex weight. Each subcone carries weight ¼ at ν = 0, so the split puts ½ at the origin against ¼ for the quadrant; the extra ¼·f(0) on companions with α ≡ 0 gives exactly the observed 0.25. The corrected statement (subtract ¼·[0 ∈ α+Z²]·f(0)) must be re-preregistered before it counts.
## Category A
- Transport identity S^E_{γα,γβ} = S^{E∘γ}_{α,β} ⇒ Γ·Corner_K = Corner_{γ⁻¹K} (substitution plus reduction rules); the orthant arc is exactly half the unit arc (cosh L = √(7/2)).
- The general unimodular-cone corner formula (coefficients B(u1,u2)/(4Q(u2)), B(u1,u2)/(4Q(u1))) by the iterated Euler–Maclaurin argument of paper v6.
## Category B
Numerical confirmations above.
