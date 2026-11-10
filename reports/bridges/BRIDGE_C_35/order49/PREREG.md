# order49 PREREG: LN satisfies the hypothesis of the x↔1/x theorem (written and hashed before certification)
Object: LN = A2_lines as implemented in order18/scripts/a2.py, function lines(α,β,x).
## Generalised hypothesis H (needed: the line terms are not of the form Σ_r f_r w_r)
Y_j(x) = Λ_{α_j,P}(f), where:
- f(ν) = e(xQ(ν) + B(ν,β_j)) is the phase on α_j + Z²;
- Λ is linear in f, with real coefficients depending only on α_j, the line data, and the periods P of f along lines;
- in particular Λ does not depend on β_j or on x except through f and P.
## Claims (Category A, structural proof plus exact checks)
H1 (code audit): in lines(), β and x enter only through ph() and period(). All other coefficients (sg, Fr, B1, B(u,ν0), Q(u)) are real rationals built from α and u.
H2 (exact): phase_ints(α,−β,−x) ≡ −phase_ints(α,β,x) mod M. This is an integer identity of the formula ((−h)Q2 + 2m(−Bn)). It is checked by exact integer evaluation on all 105 pairs, x ∈ {2, 1/3, 5/7, 9/2}, points |v| ≤ 6.
H3 (exact): for every j, reduce(α_j, −β_j) returns a companion with α' = α_j exactly (not just mod Z²). Then λ = −β_j − β' ∈ A^{−1}Z², so B(v,λ) ∈ Z for v ∈ Z². Hence f_{α,−β} = e(B(α,λ))·f_{α,β'} pointwise, by a constant. Check: exact Fractions for all 105.
H4: period(): the test k1 == k2 is invariant under k ↦ −k + const, so P is the same for f, conj f and c·f. This follows from H2/H3 and the code.
PASS iff H1–H4 all hold. Then LN_{(α,−β)}(−x) = conj(LN_{(α,β)}(x)) and covariance under Π hold, i.e. Y(−x) = conj(ΠY(x)). By the v11 proof, the theorem holds for LN and for A2 = LN + CO.
Paper: the hypothesis of the v11 theorem is narrower than H. The statement must change, so a thin v12 (statement with hypothesis H, plus a proof remark) is drafted if PASS.
Control: the float check from order48 (LN 4.8e−15) is consistency only, not the verdict.
Naming: RG* only, no labels L1–L7. MAPS_CANDIDATES untouched; no Resonant objects; no bridge claim; nothing on residual smallness.
