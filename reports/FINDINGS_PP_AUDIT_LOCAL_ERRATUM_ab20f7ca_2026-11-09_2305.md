# PP AUDIT — Local ERRATUM ab20f7ca… (t4436 branches, PP-fix response, filed 23:02 CST)

PP rules apply: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING; float-only = COND; a citation never makes a result PROVED (OW 3f160803 as amended by 36683379, strict); refute only by proof or counterexample.

**Integrity**
- The erratum's sha ab20f7ca… matches its sidecar (223 lines). The original 26a7c91e still matches its sidecar and is unedited.
- All 17 new evidence sidecars verify: s9, s9b, s10, s10b (py/log/txt), s11 (empty log), s11b, gen_erratum.
- s9 (crashed) and s11 (empty log, no .py) are failed launches kept on record. That is acceptable.
- Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 was unchanged before and after this audit.
- PP wrote only to reports/ (this file and its sidecar) and to /workspace/audit-scratch/pp_erratum_ab20f7ca/: copy_s4c.py, pp_check_certs.py and its .log, each with a sidecar.
- PP did not touch s1e (PID 932685), ob_v3 or any Local directory.

## Rulings

### C2 (c-2): ACCEPTED — PROVED (T-fam discharged)

The setting: odd q, n ≥ 1, and V the 2n-dimensional nondegenerate symmetric space with a Lagrangian, i.e. split hyperbolic. Lagrangians exist by hypothesis, and step (a) builds the hyperbolic basis, so V ≅ H^n.

**(a) Witt step: checked.**
- f₁ = x − ½B(x,x)e₁ gives B(f₁,f₁) = B(x,x) − B(x,x)B(e₁,x) = 0 and B(e₁,f₁) = 1. This uses ½, so q must be odd.
- U₁ = U ∩ f₁^⊥ has dimension n−1, because B(e₁,f₁) ≠ 0 means U ⊄ f₁^⊥.
- U₁ ⊂ e₁^⊥, because U is totally singular. So U₁ ⊂ H₁^⊥, and U₁ is a Lagrangian of the nondegenerate H₁^⊥.
- The induction is valid. Equal Gram matrices give an isometry carrying U to W, so O(V) is transitive on X.

**(b) Stabiliser lies in SO: checked.**
- PP recomputed, for g = [[A,C],[0,D]] in the basis (e,f) with B = [[0,I],[I,0]]: gᵀBg = [[0, AᵀD],[DᵀA, CᵀD+DᵀC]].
- So g ∈ O forces AᵀD = I, hence D = A^{−T} and det g = det A·det D = 1.
- This holds over any field with B symmetric; odd characteristic is needed only in (a) and (c).

**(c) Two orbits, swapped by a reflection: checked.**
- v = e₁+f₁ has B(v,v) = 2 ≠ 0 (q odd). The reflection r_v lies in O and has det −1, so det: O → {±1} is onto and |SO| = |O|/2.
- Since Stab_O(U) ⊂ SO: #SO·U = |SO|/|Stab| = (|O|/2)/|Stab| = #X/2.
- r_v(SO·U) = SO·r_vU, because SO is normal in O.
- The two orbits are disjoint: if r_vU = sU with s ∈ SO, then s⁻¹r_v ∈ Stab ⊂ SO, which contradicts det = −1.
- #X = N(n) = ∏_{i=0}^{n−1}(q^i+1) (c-1, PROVED). The i = 0 factor is 2, so each orbit has N(n)/2 = ∏_{i=1}^{n−1}(q^i+1) members.
- At (24, 23) the contour is 2∏_{i=1}^{23}(23^i+1) = #X: exactly two orbits' worth.

**"Family" must mean SO-orbit.** The proof establishes SO-orbits. It does **not** identify them with the parity classes (codim U∩U₀ mod 2) that 26a7c91e named.
- The erratum's remark "r_v changes dim(U∩gU) parity" overstates what is shown. Only dim(U ∩ r_vU) = n−1 is shown.
- Fix C2′: the row must say "SO-orbit". Either drop the remark or restate it as "U ∩ r_vU has codim 1". The parity identification remains unclaimed, and the count does not need it.

s11b's brute force (1,3), (2,3), (2,5), (3,3) is corroboration only.

**Ruling: c-2 COND [T-fam] → PROVED, with the proposed row wording ("SO-orbit").**

### C1 (c-3 normalisation): ACCEPTED, REF unchanged

- dim SO₄₈ = 48·47/2 = 1128.
- |SO⁺₂ₙ(F_q)| = q^{n(n−1)}(q^n−1)∏_{i=1}^{n−1}(q^{2i}−1). The exponent check is n(n−1) + n + n(n−1) = n(2n−1) = 1128 at n = 24, so vol = #SO₄₈(F₂₃)·23^{−1128} = (1−23^{−24})∏_{i=1}^{23}(1−23^{−2i}) exactly.
- 1/vol = 1.0018975…, which reproduces the carried "≈ 1.0019" (bfa5da3b gave 4 digits) to the stated precision.
- The fibre-measure step (smooth SO(L) over ℤ₂₃, Hensel) is the definition of Weil's canonical measure plus standard smoothness.
- The REF does not depend on it: under any stated normalisation, vol is a rational number near 1 and cannot equal a 377-digit integer.

### CNF (a-2/a-3): ACCEPTED — h(140) = 2 and ε = 6+√35, elementary, no GRH; rows rest on T-CNF only

PP recounted the reduced indefinite forms of D = 140 by hand. The conditions are 0 < b < √140 ≈ 11.83, b even, and √D − b < 2|a| < √D + b.
- b = 10: ac = −10, |a| ∈ {1, 2, 5, 10}, giving 8 forms.
- b = 8, 6, 4, 2: ac = −19, −26, −31, −34 has no admissible |a|.
- So there are 8 reduced forms, in 4 cycles of length 2 (s9b), and h⁺ = 4.

The unit:
- √35 = [5; 1, 10] (PP re-derived: x₁ = (√35+5)/10, x₂ = √35+5).
- 6² − 35 = 1 with y = 1 minimal, so ε = 6+√35 is fundamental in ℤ[√35] = O_K, since 35 ≡ 3 mod 4.
- Norm −1 is impossible, because −1 is not a square mod 7. Hence h = h⁺/2 = 2.

The Minkowski argument is also checked:
- The bound is 5.92. 3 is inert, 2 and 5 ramify.
- 𝔭₂ is not principal: x² − 35y² = ±2 would need ±2 to be a square mod 5.
- 𝔭₅ is not principal: 5u² − 7y² = ±1 would need 3y² ≡ ±1 mod 5, and 3y² ∈ {0, 3, 2}. s9b's "−7y² = 2y²" is a typo; the value set printed is correct.
- N(5+√35) = −10, so [𝔭₅] = [𝔭₂].

h(−7) = 1 is checked: (1,1,2) is the only reduced form.

**Ruling:** the L(1,χ₁₄₀) and L(1,χ₋₇) rows now rest on T-CNF (the class number formula) alone. They stay COND [T-CNF]; there is no grade change.

### A1 (α-3 certificates): ACCEPTED — 144/290 verified independently by PP; α-3 stays PROVED

PP's pp_check_certs.py rebuilt every job's equations g_i, product P and saturation generator zP−1 from a copy of s4c, independently of s10/s10b. For every certificate it then checked:
- each listed g is one of the recomputed generators;
- P is not the zero polynomial;
- Σc_i g_i − target expands to exactly 0, where the target is 1 or P^k.

**Result: 144 distinct jobs certified, 0 failures** (s10: 96, s10b: 48).

Logic:
- If 1 ∈ (g, zP−1), there is no common zero with P ≠ 0.
- If P^k ∈ (g), then P vanishes at every common zero, so some α_k = 0.
- Either way, no full-support solution exists.

The remaining **146** GB = [1] verdicts rest on sympy's exact Buchberger, which is now disclosed. That is accepted as exact computer algebra, the same footing PP gave it at 2232.

### O1, J1, H1, O5, J3a, D1: APPLIED AS WRITTEN (verified)

- **O1:** the REF covers every squarefree t, with the pivot proof.
- **J1:** the REF covers any ψ mod 980, with the proof restated correctly. Every unit d mod 19600 occurs as a lower-right entry because gcd(d, 19600) = 1.
- **H1:** "d ≥ 1".
- **O5:** scoped, with O5-3b subject to T-Weyl.
- **J3a:** the unconditional ellrank bound and the 2-torsion fact are cited.
- **D1:** "closed as REFUTED, kept on record".

### PENDING (unchanged)

- Oc-2 at 784 (s1e still running; 6 characters).
- J-2 at 9800 (to be run as s2e after ob_v3).

## Tally

**PP-ruled: 96 rows — PROVED 63 · CONDITIONAL 17 · OPEN 5 · REFUTED 9 · PENDING 2.** The only change from PP 2232 is c-2 → PROVED.

Per item:

| Item | P / C / O / R / PEND |
|---|---|
| O-c | 12/5/2/1/1 |
| V₈₄ | 6/2/0/1/0 |
| J | 16/3/2/1/1 |
| H₊U | 5/0/1/2/0 |
| LD-O3a | 6/3/0/0/0 |
| LD-O3b | 4/3/0/0/0 |
| LD-O3c | 3/0/0/1/0 |
| α | 6/0/0/1/0 |
| O5 | 5/1/0/2/0 |

The Bridge C rollup (46/11/5/2/1 + V₈₄) is separate and unchanged. Nothing is adopted.

## Fixes for Local (priority: true)

- **C2′:** the c-2 row says "SO-orbit", not parity family. Delete the remark "r_v changes dim(U∩gU) parity" or restate it as "dim(U ∩ r_vU) = n−1".
- **CNF′ (cosmetic):** s9b prints "−7y² = 2y²"; it should read 3y². Record this in the next additive file only; do not edit s9b.
- **A1′ (optional):** certificates for the remaining 146 GB = [1] jobs, e.g. with higher degree bounds or by an F4/msolve cross-check. This would not change any grade.
- **Pending:** the s1e 784 result and the final log sidecar go in a follow-up additive file. J-2 9800 runs as s2e.
