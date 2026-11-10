# order27 RESULTS
PREREG sha256 7ae5821ba48581b6d5783cb591c1ee5dc8a15332ffaf1d034f7fd625be34ece7 (hashed before numerics).
## Transport convention (settled)
Γ_g is defined by G_{gα,gβ} = Σ_k (Γ_g)_{jk} G_k for every automorph, det ±1 alike. The transport Γ_g·Cor_C = Cor_{g⁻¹C} holds for improper g too, because its proof never uses det. The order26 result "Γ_h ≠ I" is correct and not a contradiction: Cor_K is Γ_h-fixed without Γ_h being I.
| check | result | verdict |
|---|---|---|
| Γ_σ = I (exact) | true | PASS |
| X1 Γ_h = Γ_σΓ_{−I} = Γ_{−I}Γ_σ (exact) | true (Γ_{−I} ≠ I) | PASS |
| X2 Γ_{−I}² = Γ_h² = I (exact) | true | PASS |
| X3 [Γ_h, M] = 0 (exact multisets) | 0 mismatches | PASS |
| X4 [Γ_h, Γ_γ] = 0 (exact) | commute | PASS |
| N1 Cor_{hK} = Cor_{−K} = CO | 2.0e−14 | PASS |
| N2 Γ_h·CO = CO | 2.9e−14 | PASS |
| N3 order26 Cor_B reproduced | 7.2e−15 | PASS (consistency) |
| **RG18** orbit {γ^a h^b K, −K} outside span{CO, Γ_γCO} | r_new ≤ 9.8e−15 | **VACUOUS by rule** (predicted) |
Character projector ranks (γ,h) = (+,+) 36, (+,−) 24, (−,+) 18, (−,−) 27.
## Category A (proved; in v10)
Lemma (parity): Cor_{−C} = Cor_C. Proposition: Γ_h = Γ_{−I} ≠ I, Γ_h² = I, it commutes with M and Γ_γ, and Γ_h·CO = Cor_{hK} = CO. Corollary: the ⟨γ,h⟩-orbit of the corner is {CO, Γ_γCO}, so every group average or projection lies in span{Y_+, Y_−}.
## Category B
The numbers above.
## Verdicts
Cor_{hK} = Cor_K: Category A. RG18: VACUOUS (this is a theorem now, not only numerics). v10: yes, 134 pages. Ξ: not identified. E1–E3 OPEN.
Disclosure: the predictions used v9 facts (Γ_γ² = I), so they are a derivation; N3 is a consistency check.
