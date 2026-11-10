# Map-RG1 (Residual Geometric). Preregistered 2026-10-24, about 5:45 PM CDT, before any RG1 test
Working claim (Arvin, opinion, NOT proved): "the hybrid shadow is the residual geometric bridge". This file does not upgrade that claim. It fixes one falsifiable map.

**Residual object.** The residual (mismatched-cone) geometry of C: the weight W = orth − H, the orthant cone(e1,e2) minus the Hecke cone, in v-signs. Its negative-cone endpoints are c′ = (7,−2) (Q = −35), c1 = (−1,1) (Q = −5/2), and c2 (Q = −595/2·…). Each endpoint c has an orthogonal positive ray c^⊥ and an endpoint reflection ρ_c, the integral isometry fixing c and negating c^⊥ (or the reverse):
- ρ_{c′}(ν) = (−ν1−7ν2, ν2);
- ρ_{c1}: (u, m) ↦ (u, −m) with u = ν1, m = ν1+ν2, i.e. ν ↦ (ν1, −2ν1−ν2).

**Map RG1.** Each endpoint c of the residual geometry sends companion j to its sector shadow at c:
- P-odd sector: the ξ₁ unary theta at |Q(c)|.
- P-even sector: the Laplacian defect B_j(ĉ).
- **Selection rule (new):** B_j(ĉ) ≡ 0 **iff** ρ_c preserves companion j, meaning ρ_c(α+Z²) = α+Z² and e(B(ρ_c ν, β)) = e(B(ν,β)) on α+Z².
  - Sufficiency is proved for c′ (PREREG §1) and the same argument works for c1 (Category A).
  - **Necessity is the new, unproved prediction.**
- Criterion at c1 (exact): 2(α1+α2) ∈ Z, and 14(b0+b1)·m ∈ Z for all m ∈ α1+α2+Z, i.e. 14(b0+b1)(α1+α2) ∈ Z and 14(b0+b1) ∈ Z.

**Prediction P-RG1.** On the 105 companions, the set Z1 = {j : |B_j(ĉ1)|/Σ|terms| ≤ 1e−25} (from order14 c1.py data) equals the set R1 = {j : the ρ_{c1} criterion holds} (exact rational).
- **Pass:** Z1 = R1 exactly.
- **FAIL:** any j in Z1 ∖ R1 (vanishing without a symmetry, which refutes necessity) or in R1 ∖ Z1 (which would refute the Category A sufficiency and indicate a bug).
- Also reported: for every j outside R1, min over 3 τ of |B_j(ĉ1)|/Σ|terms|. It is predicted > 1e−6, a clear gap.

**OPEN (needs new data):** the O_res / Resonant geometric counterpart. Predicted form: an object whose zero pattern across its components is fixed by the same endpoint-reflection rule.
