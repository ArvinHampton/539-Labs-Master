# order23 RESULTS
PREREG sha256 e390d61b9330c3e61e7bb10f2b9d8c8b6b7f21cf628d14c2b4d341d1429a2f03 (hashed before numerics; RG9b-corrected, RG10, RG11 hashed there).
| test | value | verdict |
|---|---|---|
| C1 corner formula = CO (x and −1/x) | 0.0 | PASS |
| C2 Γ_σ·G = G | 0.0 | PASS |
| **RG9b corrected** (vertex ¼·[α∈Z²]; 2 such companions) | max abs 7.1e−15 | **PASS** |
| **RG11** Γ_σ·CO = Corner_{σK} | max abs 7.1e−15; displacement 0.0 | **vacuous** (Γ_σ = I exactly) |
| **RG10** U = Corner_K + Corner_{σK}, law U(−1/x) = x·kM·U(x) | abs 108.8 (‖S‖ = 1856), rel 0.0586; fitted κ gives 0.0585 | **FAIL** |
## Reading
Γ_σ is the identity on the 105 companions (σ preserves each, as in Prop. Bcp), so Corner_{σK} = Corner_K and U = 2·A2_corner: the σ-sum adds nothing and RG10 reduces to the order19 law (same relative residual). The geometric near-law does not hold in this form.
## Category A (folded into v8)
Unimodular-cone corner formula; subdivision with vertex term; transport Γ_g·Cor_K = Cor_{g⁻¹K} for automorphs; Γ_σ = I ⇒ Cor_{σK} = Cor_K.
## Paper
RTA_FOUNDATION_BOUND_v8.pdf, 133 pages.
