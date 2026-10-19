# Open items, algebraic/dimension track (2026-10-18)
Folder 2026-10-18-Open-Algebraic/: cusp_sectors.py, cusp_sectors.json. This builds on General-s-Tensor (the exact tensor factorisation for odd s) and cites Cusp-Onset-Closure for its certified ranks. Local only; nothing pushed. Naming: W_P = Fix(P), of dim 2(s−1)²; d_Eis = the Eisenstein dimension.

## Item 5: the odd-parity sectors are cusp. Cat A (main new result)
**Lemma.** Let F be a vector-valued Maass form of eigenvalue ¼ for ρ, with moderate growth, and let σ ⊂ C^N be a ρ-invariant subspace on which ρ(T) has no eigenvalue 1. Then the projection F_σ is a cusp form.

*Proof.*
- F_σ(τ+1) = ρ_σ(T)F_σ(τ). In a ρ(T)-eigenbasis, a component with eigenvalue e(r), r ∉ Z, has Fourier frequencies in r + Z. So it has no zero mode, i.e. no √y(a + b log y) constant term at ∞.
- SL₂(Z) has one cusp, and F_σ(γτ) = ρ_σ(γ)F_σ(τ). So the expansion at any cusp is a linear combination of components at ∞, which also have no constant term.
- Moderate growth with no constant terms at every cusp means F_σ is cuspidal (rapid decay). ∎

**Applying it with the exact tensor factorisation.**
- ρ(T) acts on a sector as T₂ ⊗ ⊗_p T_{q_p}, and the exponents have coprime denominators (4 and the p^e). So a tensor vector is T-invariant iff every local factor is T-invariant.
- Local T-invariants:
  - B₁ (the odd characteristic): none, since T = i.
  - A₃: one (00+01).
  - W_{p^e}⁺: 1 + (p^{⌊e/2⌋}−1)/2.
  - W_{p^e}⁻: (p^{⌊e/2⌋}−1)/2. This is zero for e = 1 and positive for e ≥ 2. For example, Z/9 has the odd T-invariant vector e₃ − e₆.

**Consequences.**
- (a) The whole odd-characteristic sector B₁ ⊗ (Z/s)⁻ ⊗ (Z/(s−2))⁻ lifts to cusp forms, for every odd s. So **cusp ≥ (s−1)(s−3)/4 is Cat A** wherever this sector lies in V. That holds at every odd s certified in Cusp-Onset-Closure (5–51). For general s it is conditional on item 1.
- (b) Every non-all-even sector containing an odd local factor at a prime with e = 1 is cusp. When no prime with e ≥ 2 carries the odd parity, this gives cusp ≥ dim V − 3∏(p^e+1)/2, i.e. **d_Eis ≤ 3∏(p^e+1)/2 (Cat A)**.
  - Exact sector table (cusp_sectors.json): this covers every non-all-even sector ("undecided" = 0) at s = 5, 7, 9, …, 51, 99 (all tested s ≤ 99).
  - First undecided cases: s = 225 = 9·25 (16128 dims) and 1225 = 25·49. There the odd parities sit only on prime powers with e ≥ 2, whose odd parts have T-invariants (isotropic, oldform-type vectors).
- Not proved:
  - That the all-even sector carries no cusp content, and that its lift is genuinely Eisenstein (nonzero constant term). So d_Eis = 3∏(p^e+1)/2 is Cat A as an upper bound and Cat B as an equality.
  - Note that the genus Eisenstein series lie in the T-invariants of this sector.

## Item 4: exact Weil conjugacy and d_Eis for odd s. Superseded, Cat A
- The floating conjugacy check (1e−15) is no longer needed. General-s-Tensor gives the exact factorisation S = [e(−2xy/n)/√n] ⊗ S₂ and T = diag e(−x²/n) ⊗ T₂ for all odd s. It is symbolic and verified with Fractions at 8 values of s.
- So the all-even sector A₃ ⊗ ⊗_p W_{p^e}⁺ has dimension exactly 3∏(p^e+1)/2 (Cat A).
- d_Eis equals this sector dimension only modulo the Eisenstein identification in item 5 (≤ is Cat A, = is Cat B).
- W₂ for 2-power k ≥ 6 (even s, first case s = 64): **open**, not attempted here (even-s factorisation not built; item 2).

## Item 1: general lower bound dim V ≥ s(s−1) for odd s. Reduction Cat A, full proof open
- **Kernel invariance (Cat A).** The relations kernel K = {x : xᵀF ≡ 0} is ρ(γ)ᵀ-invariant, because F(γτ) = ρ(γ)F(τ). So V is a ρ-invariant subspace of the exact upper-bound space U = Fix(N) ∩ Fix(γ) = ⊕ (matched sectors).
- **Reduction (Cat A).** U is multiplicity-free: distinct parity patterns give distinct representations of SL₂(Z/4) × ∏SL₂(Z/p^e).
  - If n = s(s−2) is squarefree, every sector is irreducible (W_p^± is irreducible for e = 1; A₃ and B₁ are irreducible). Then V = ⊕_{σ : F_σ ≠ 0} σ.
  - So dim V = s(s−1) iff each of the at most 2^{ω(n)} matched sectors has a nonzero lift. That is a finite, per-sector nonvanishing statement.
  - For prime powers, W_{p^e}^± is reducible (new/old pieces from the isotropic subgroups p^k Z/p^e). The reduction then needs the finer decomposition.
- **Missing.** A uniform nonvanishing argument, e.g. a frequency q whose coefficient vector c(q) has nonzero projection onto every sector. The coefficients are cone sums over ν with Q(ν) = q, which I could not control uniformly in s. **Open.** The certified equalities at odd s ≤ 51 (Cusp-Onset-Closure) remain the Cat A evidence.

## Item 2: even s. Open
- Structure (Cat A, elementary): the gcd of the entries of A is 2, so L′/Z² ≅ Z/2 × Z/(s(s−2)/2). The lattice is even (Q integral, w_c = 0), and a ∈ L′ exactly when the BES collapse (e.g. s = 8).
- I have not built the even-s factorisation. The odd-s proof uses a cyclic L′/Z², w_c = g/2 and the a₂ characteristic, none of which carries over directly. The 2-adic module depends on s mod 8 and on k (2^k ‖ 2t(t−1), t = s/2).
- A general proof of the gap m(m−1) at s = 2m²: **open (B)**. Cusp-Onset-Closure's half-cone bound (Cat A upper bound) and the rational square root (γ+I)/(2m) of γ for s = 2m² are the leading mechanism. I did not extend them.

## Item 3: s = 98 (2406 vs 2408). Open
- No new computation here. Cusp-Onset-Closure's exact lower bound stays at 2406 for Q = 40, 70 and 130; the half-cone upper bound is 2408.
- Since the gap at m = 7 is the first one where 7 | m and 49 | s, an extra relation from the 7-adic local factor (49 = 7², an isotropic subgroup 7Z/49) is a plausible source. This parallels the e ≥ 2 T-invariant phenomenon in item 5.
- Untested (Cat B suggestion). Next steps: build the even-s tensor factorisation and test U ∩ (relations from the 7Z/49 isotropic subgroup); or compute the exact rank with a finer basis.

## Item 6: u_L criterion arithmetic. Open
- Ambiguous-class count |Ḡ^σ| = 2^{ω(s)}φ(s−2): the right tool is Chevalley's ambiguous class number formula for ray class groups, |Cl_𝔪(K)^G| = |Cl_𝔪(Q)|·∏_v e_v / ([K:Q]·[E_{Q,𝔪} : E_{Q,𝔪} ∩ N K^×]).
  - The remaining work is evaluating the local ramification factors and the unit-norm index for 𝔪 = M(s). I did not carry this out, so it stays **Cat B** (verified per s in Cusp-Onset-Closure).
- Coset property for deep bad primes in general, coverage at s = 32, 34, 36, 40, and the mixed-prime and (1,12)/(12,1) parts at s = 24: **not attempted** (computational track; open).

## Item 7: Z₅, Z₇, Z₂ versus the classical Atkin–Lehner operators. Open (Cat B)
- Exact facts: Z_p commutes with ρ (Cat A) and gives the sector signs.
- Identifying Z_p with W_p on scalar newforms would need an explicit vector-to-scalar dictionary for this level-4n module, of Bruinier–Bundschuh type for prime level, plus a comparison of root numbers. Not done.

## Status summary
| Item | Status |
|---|---|
| 5: odd/non-even sectors are cusp | **Cat A**: lemma plus exact factorisation. cusp ≥ (s−1)(s−3)/4 (where the B₁ sector is in V); d_Eis ≤ 3∏(p^e+1)/2 when no odd parity is carried only by e ≥ 2 primes (all tested s ≤ 99). Eisenstein equality is B. |
| 4: d_Eis for odd s | Exact sector dimension (Cat A); the conjugacy check is superseded. W₂ for k ≥ 6 is open. |
| 1: general lower bound | Reduction to per-sector nonvanishing (Cat A, squarefree n); full proof open. |
| 2: even s and the general gap | Open (structure only). |
| 3: s = 98 | Open; 7-adic isotropic mechanism suggested (B). |
| 6: ambiguous count and coverage | Open (Chevalley formula identified; not evaluated). |
| 7: Atkin–Lehner identification | Open (B). |

---
## Update, 14:15 CDT: Item 2 progress (even s), with new partials for Item 3
Scripts are in `2026-10-18-Open-Algebraic/`: `even_probe.py`, `even_exact.py` (output `even_exact_6_8_10_12_14_18_32.json`), `even_sectors.py` (`even_sectors.json`), `gap_locate.py` (`gap_locate.json`/`.log`).

**2a. Exact even-s tensor factorisation (Cat A at s = 6, 8, 10, 12, 14, 18, 32).** Write each label α = α_odd + α_2 using the CRT idempotents of D. For even s the odd part of every β is 0, so no gauge change is needed. The map label ↦ (α_odd, (α_2, β_2)) is a bijection onto O × T₂, where O = L′_odd is cyclic of odd order and |T₂| = 8, 16, 16, 8, 8, 32, 64. With exact Fractions:
- supp S = supp_odd × supp_2. The S exponent splits as f(x,y) + h(A,B) mod 1. T fixes the odd coordinate, and its exponent splits the same way.
- Odd factor: S ∝ e(+B(x,y)) and T = e(+Q(x)) on L′_odd, with full support. This is the (conjugate-convention) Weil representation of the odd discriminant form, so it factors further over the odd primes by CRT.
- Negation and γ are monomial and split as (odd map) ⊗ (2-adic map with a phase independent of the odd coordinate).
- dim Fix(N) ∩ Fix(γ), computed sector by sector, equals the direct computation and the orbit bound (s/2)(s/2+1) at every tested s. The per-sector [odd, 2-adic] dimensions are in `even_sectors.json`. Examples: s = 18 gives 5·18; s = 32 gives 8·34; s = 12 gives 6·6 + 3·2.

**2b. Where the s = 2m² gap sits (exact incidence kernels, m = 2..5; m = 6 still running).** I placed the left kernel of the half-cone incidence matrix (dimension exactly m(m−1)) inside the factorisation:
- s = 18 (m = 3, factor Z/9) and s = 50 (m = 5, factor Z/25 in Z/75): every relation has odd side inside the line spanned by the isotropic vector δ_{t^⊥}. Here t generates the isotropic subgroup (m)Z/m². The vector is invariant under translation by t and supported on t^⊥ (Cat A, exact kernel; the side test is floating SVD on exact vectors).
  - s = 18: relations = (isotropic line) ⊗ (6-dim subspace of the 2-adic N = + sector).
  - s = 50: the complementary part (Z/3 ⊗ 2-adic) carries 20 = m(m−1) dimensions.
- s = 8 and 32 (m = 2, 4; the m-part is 2-adic): the relations are a 1- or 4-dimensional 2-adic piece times the odd U-sector (Z/3, and Z/15 of dim 8).
- Supported statement (Cat B; the mechanism is exact per s): **the gap = (isotropic δ-line of the Z/m² factor) ⊗ (an m(m−1)-dim subspace of the complementary factor).** This turns the "7Z/49 hypothesis" for s = 98 into a precise prediction: the half-cone relations are δ_{7Z/49-perp} ⊗ (42-dim). Any extra 2 relations at s = 98 must come from outside the half-cone mechanism.
- Still open: a closed-form proof that the complementary subspace has dimension m(m−1) for all m. I have not derived it from √γ = (γ+I)/(2m).

**Item 3 (s = 98): still open.** No direct s = 98 computation in this update. Neither the exact sector rank nor the extra relations were attempted: the s = 98 incidence kernel plus the factorisation is beyond what I ran here, and s = 72 alone has needed over 10 minutes at 5.7 GB. Next step: run gap_locate at 98 (flint kernel), then compare the Q130 Fourier kernel (vrank) against δ_iso ⊗ (·).

**Items 1, 6, 7 and W at k ≥ 6: no new computation in this update.** They are still open, with the status unchanged from above.

---
## Update, ~15:10 CDT: items 1, gap, s = 72/98, s = 64, item 7
Scripts and outputs are in `2026-10-18-Open-Algebraic/`.

### (a) Item 1: sector-wise nonvanishing (`item1_lead.py` → `item1_lead_5_7_9_11_13_15_17_19_21_23_25.json`)
- **Method.** For each odd p | s(s−2), the local involution Z_p acts by x ↦ u_p x, where u_p ≡ −1 at p and +1 elsewhere (CRT).
  - Z_p is an isometry of Δ that commutes with ±γ and with ρ, so it permutes the ⟨γ,−1⟩-orbits.
  - Sector ε: P_ε = ∏(1 + ε_p Z_p), an integer matrix on orbit indicators.
  - The projected coefficients are c_ε(O,q) = Σ_S ε_S N_{Z_S O}(q). These are exact integers from the vrank cone counts.
- **Result (Cat A, exact integer ranks, Qmax = 30), at every odd s = 5..25:**
  - For every sector occurring in U, rank of the projected lift = dim of the sector in U, so the lift is injective on every sector.
  - Σ over sectors = s(s−1), so dim V = s(s−1) is re-certified sector by sector.
  - Sectors occurring: only ε with Z_{all} = −1 = id on orbits, so 2 sectors at single-odd-prime-pair s and 4 at s = 15, 17, 21, 23. Example: s = 7 gives (+,+) 36 and (−,−) 6.
- **Leading coefficient (Cat A at s = 5..25).** In every sector the minimal-|q| nonzero coefficient sits at 2D²Q = −2s(s−2), i.e. ν₀ = (s, −2) (Q = −2s(s−2)).
  - Its value is c_ε = ±4 and it is cancellation-free: exactly one of the 2^r terms N_{Z_S O₀}(q) is nonzero.
  - So every sector's lift has a provably nonzero leading coefficient ±4.
- **General argument (Cat B; one lemma remains).**
  - Lemma needed: the cone points of norm −2s(s−2) are ±ν₀ and their γ-translates (4 of them, one orbit O₀), and u_S ν₀ ∉ ±γ^ℤ ν₀ mod Δ for S ≠ ∅.
  - Given the lemma, c_ε(O₀, q_min) = ±4 ≠ 0 for every ε.
  - Nonzero then gives injective wherever the ε-sector is irreducible: squarefree odd part, where it is ⊗ of local irreducibles with A₃/B₁.
  - With e ≥ 2 the ε-sector is reducible. There injectivity is only the exact rank (Cat A per s), not the uniform argument.

### (b) Gap m(m−1) (`gap_g.py` → `gap_g.json`; `gap_locate.json`)
- g = (γ+I)/(2m) is integral away from m, so it acts on the complement factor (labels with zero m-part). I checked g² = γ there for m = 2..7.
- **Odd m (3, 5, 7):**
  - On the complement, Fix(N, γ) has dim 2m² and splits as g = +1: m(m+1) and g = −1: **m(m−1)**.
  - With gap_locate (relations = isotropic δ-line of Z/m² ⊗ complement piece) this matches the gap exactly at m = 3, 5. The match is in dimension; the subspace identity is not checked.
  - It predicts 42 at m = 7, which is the half-cone gap.
- Proof reduction: gap = (2m² − tr(g | Fix(N,γ)))/2, so it suffices to show tr(g | Fix(N,γ) on the complement) = 2m. I have **not proved** this trace identity in general; the numbers are floating ranks on exact monomial matrices (B).
- **Even m (2, 4, 6):** the m-part involves the 2-adic factor and the gap is not a pure tensor. s = 72 has odd side rank 18 (isotropic line of Z/9 ⊗ the 18-dim Fix(N,γ) of Z/35) and 2-adic side rank 4.
- **Status:** general proof open. The odd-m g-eigenspace identification is B (holds for m = 3, 5, 7).

### (c) s = 72 and s = 98
- s = 72 gap_locate finished: kernel 30 = m(m−1). Odd side: invariant under 3Z/9 translation and supported on t^⊥ (as above).
- **s = 98 not attempted.** s = 72 alone peaked near 8 GB of the box's 15 GB, so 98 does not fit.
- Cheaper test: the complement computation at m = 7 (192 labels) gives exactly 42 g-odd vectors. So the half-cone mechanism accounts for exactly 42 relations at s = 98, and the extra 2 (2406 vs 2408) cannot come from it. Either the vrank lower bound is not saturated at Q130, or there is a second mechanism. Open.

### (d) s = 64 (k = 6) (`s64_W.py` → `s64_W.json`; `w2_orbits.py` → `w2_orbits_16_32_48_64.json`)
- **P-invariant label space (Cat A, exact count).** Fix(negation) splits as W₂^± · W_odd^±. At s = 64: W₂^+ = 66, W₂^- = 62, W₃₁^± = 16/15, giving **dim W_P = 1986**, equal to the direct count. (s = 16, 32, 48 also match: 114, 482, 1106.)
- **Cyclic span W₂ = span ρ₂·δ₀:**
  - Upper bound: isometries of Δ₂ commute with ρ and fix δ₀, so W₂ ≤ #O(Δ₂)-orbits = **42** (Cat A, exact, new).
  - Float Krylov gives **36**, equal to the conjectured 2^{k−1} + 4 (B), and also reproduces 12 and 21 at k = 4, 5.
  - So W₂(k = 6) ∈ [36, 42] Cat A, with 36 the expected value. dim W(s = 64) = 16 · W₂ ∈ [576, 672], with 576 expected.
  - The orbit bound is not tight at k = 5 either (22 vs 21). An exact upper bound needs a cyclotomic or mod-ℓ two-sided certificate.

### (e) Item 7: dictionary at s = 7 (partial)
- Under the Weil-rep ↔ Γ₀(N) dictionary F ↦ F₀(Nτ), the scalar Atkin–Lehner W_{p^e} corresponds to the local partial Fourier transform S_p (up to Gauss sum), **not** to Z_p.
  - Exactly (Cat A, earlier local models): S₅² = +Z₅ and S₇² = −Z₇, i.e. S_p² = χ_p(−1) Z_p. This matches W_p² = χ_p(−1) for the quadratic nebentypus (χ₅(−1) = +1, χ₇(−1) = −1).
  - So Z_p ↔ χ_p(−1) W_p², and Z_p acts trivially on every F₀-image.
- Corollary (Cat A, one line): δ₀ is fixed by every Z_p, so ε-odd sectors (including the 6-dim cusp sector (−,−) at s = 7) have zero 0-component. Their scalar images must use the other components F_x.
- Not done: numerical W₅, W₇, W₄ eigenvalues on the actual forms.
  - The s = 7 cusp forms in `2026-10-17-cusp-part/cusp_forms.txt` are dihedral Maass forms whose stated level is 140·N(f) = 19600, not 140.
  - The literal "level 140" dictionary would need twisting by the conductor-140 ray-class character first.
  - Next step: Atkin–Li pseudo-eigenvalues λ_p = g(χ_p)/(√p · conj ψ(𝔭)) per form, compared with ε_p.

---
## Update, ~15:50 CDT: the two identities, s = 64 certificate, item 7 levels

### (1) Orbit lemma (item 1): proved for all odd s, in a corrected form (Cat A)
Files: `lemma1.py`/`lemma1.log`/`lemma1.json`, `lemma1b.py`/`lemma1b.json`, `lemma1c.py`/`lemma1c.json`, `item1_27.log`.
- **Setup.** 2·Qi(X) = y² − d·x₂² with y = 2x₁ + s·x₂ and d = s(s−2) = (s−1)² − 1. The minimal norm Qi = −2s(s−2) means y² − d·x₂² = −4d. γ acts as multiplication by the fundamental unit ε = (s−1) + √d of Z[√d] (tr γ = 2(s−1)).
- **(i) Reduced classes (Nagell bound).** Every solution class has a representative with 0 < x₂ ≤ √(4d)/√(2(s−2)) = √(2s). x₂ = 2 gives y = 0, i.e. ±ν₀ = ±(s, −2). Extra classes exist exactly when (c² − 4)·d is a square for some 3 ≤ c ≤ √(2s).
  - c = 3 never occurs for odd s: it forces (s−1)² − 5z² = 1, and every Pell solution has s−1 odd.
  - **The original lemma is false in general.** Extra classes occur at s = 27 (c = 4), 245, 363, 847, 2025, … (16 cases with s ≤ 30001).
- **(ii) γ²ν₀ ≡ ν₀ in Δ (mod (D, 2D), D = 2s(s−2)), symbolically.** First coordinate: s(2s−3) − s = 2s(s−2). Second: −4(s−1)² + 4 = −4s(s−2). So O₀ = {±ν₀, ±γν₀}.
- **(iii) Stabiliser of O₀ in ⟨Z_p⟩ is exactly {1, Z_all}, symbolically.**
  - u·ν₀ ≡ σ·ν₀ forces u ≡ σ mod D, so S = ∅ or S = all.
  - u·ν₀ ≡ σ·γν₀ forces u ≡ σ(s−1) mod 2s(s−2). That is impossible because u is odd and s−1 is even.
  - Checked exactly for every odd s ≤ 401 (`lemma1b.json`).
- **(iv) Extra classes never land in Z_S O₀, symbolically.**
  - Points of Z_S O₀ have x₂ ≡ ±2u or ±u(2−2s) mod 2D, so c ≡ ±2 mod every odd p^e ∥ s(s−2).
  - Then s(s−2) | (c² − 4) ≤ 2s − 4 < s(s−2), a contradiction.
  - Checked exactly at all 16 exceptions (`lemma1c.json`). At s = 27 the full sector run stays cancellation-free and certifies dim V = 702 (exact).
- **Conclusion (Cat A, all odd s).** c_ε(O₀, q_min) = (1 + ε_all)·N_{O₀}(q_min). This is nonzero for every sector with ε_all = +1, the only sectors seen at s ≤ 27.
  - Nonzero lift implies injective wherever the sector is irreducible (squarefree odd part). With e ≥ 2 injectivity is still only the exact per-s rank.
  - Not proved in general: that sectors with ε_all = −1 vanish on orbit space (Z_all trivial on all orbits). Observed at every tested s.

### (2) Gap m(m−1) for odd m
Files: `gap_exact.py` → `gap_exact.json`; `gap_subspace.py` → `gap_subspace.json`.
- **Exact dimensions (orbit/stabiliser-character method with exact Fraction phases):**

| m | complement labels | N=1,g=1 | N=1,g=−1 | tr(g \| Fix(N,γ)) |
|---|---|---|---|---|
| 3 | 32 | 12 | 6 | 6 = 2m |
| 5 | 96 | 30 | 20 | 10 = 2m |
| 7 | 192 | 56 | 42 | 14 = 2m |

  So tr = 2m and dim(g = −1) = m(m−1) hold exactly at m = 3, 5, 7 (Cat A per m).
- **Subspaces coincide at m = 3, 5.** The exact half-cone kernel (flint) equals δ_iso(Z/m²) ⊗ X, where X = {N = 1, g = −1} on the complement.
  - m-side rank 1, equal to the indicator of mZ/m².
  - Complement side rank = dim X (6, 20), with residual about 1e-15.
  - Dimensions and kernel are exact; the membership residual is floating on exact data, so this is B+.
- **Not done:** a symbolic Gauss-sum proof of tr = 2m for all odd m, so general m(m−1) stays B. The intended route: tr(g | Fix) = ¼ Σ_{h ∈ ⟨N,γ⟩} tr(gh), with each tr(gh) a quadratic Gauss sum over the fixed module of gh on the complement.

### (3) s = 64: W₂ = 36 (Cat A)
Files: `w2_cert.py` → `w2_cert_64.json`, `w2_cert_32.json`, `w2_Y.npy`, `w2_orbs.json`.
- **Certificate.** Y is the span of 6 explicit ±1 combinations of O(Δ₂)-orbit indicators, one for each of q = 1/32, 1/8, 1/4, 9/32, 17/32, 25/32. Verified exactly in Z[ζ₆₄]:
  - Y is S-invariant, and T-invariant (each vector is a T-eigenvector);
  - Y ⊥ δ₀.
- **Consequence.** W₂ ⊂ Fix(O) ∩ Y^⊥, of dimension 42 − 6 = 36. With the exact lower bound 36, **W₂(k = 6) = 36 exactly** and dim W(s = 64) = 36·16 = 576.
- The same method gives W₂(k = 5) ≤ 22 − 1 = 21 at s = 32, consistent with the certified value.

### (4) Item 7: level 140 vs 19600; Atkin–Li not done
- **Reconciliation.** K = Q(√35) has discriminant 140, and the cusp ray-class characters have conductor of norm 140, so the newform level is 140·140 = 140². The vector-valued components are Γ(140)-modular (the Weil-rep level is 140), and F_x(140τ) lives on Γ₀(140²) ∩ Γ₁(140). The scalar Γ₀(140) dictionary F ↦ F₀ only sees the δ₀ component, which is zero on every sector with some ε_p = −1, including the whole cusp sector.
- **Consistency.** The cusp forms cannot appear at level 140. They appear at level 19600 exactly through the non-zero components, so the two levels do not conflict.
- **Atkin–Li comparison not done.** At level 19600, 5² and 7² divide N and the nebentypus has conductor p at each. The simple p ∥ N pseudo-eigenvalue formula does not apply; one needs the local root numbers of the dihedral representation, i.e. ε(½, ψ_𝔭) for the ramified ray-class characters. Next step: compute ψ on 𝔭₅ and 𝔭₇ from `characters.json` and compare the local root numbers with ε_p = −1.

---
## Update, ~16:30 CDT: final algebraic round

### (a) Sectors with ε_all = −1 (`zall.py`/`zall.json`, `zall2.py`/`zall2.json`)
- **Exact check.** On the label set of Δ (vrank coordinates mod (D, 2D)), Z_all acts exactly as negation, element by element, at s = 5, 7, 9, 11, 13, 15, 21, 25, 27. Since the orbits are ⟨γ, −1⟩-orbits, Z_all fixes every orbit, so P_ε = 0 whenever ε_all = −1. **Cat A at those s.**
- **Symbolic reduction.** u_all + 1 ≡ 0 on the odd part and ≡ 2 mod 4, so Z_all·x − (−x) = (u_all+1)·x vanishes in Z/D × Z/2D iff x₂ is even. Every Δ label has x₂ ∈ {0, 2} mod 4: checked exactly at all the s above (`els_2adic_residues`). So **ε_all = −1 sectors vanish for every odd s for which the Δ labels have x₂ even.**
- Note: on the whole of Z/D × Z/2D, Z_all is *not* an element of ⟨γ, −1⟩ (`zall.json`). The statement really needs the parity restriction.
- **Still open:** a symbolic proof that x₂ is even on Δ (a fact about F.ALS: L₀′/L₀ with L₀ = {n₂ even}). I haven't written it down, so the general claim is A modulo this parity fact.

### (b) Trace identity and exact subspace (`gap_exact_sub.py` → `gap_exact_sub.json`)
- **Exact subspace equality at m = 3, 5 (Cat A).**
  - Every half-cone kernel vector (exact integers) is exactly δ_iso(Z/m²) ⊗ c: rank 1 in rational arithmetic, with m-side equal to the indicator of mZ/m².
  - c satisfies N·c = c and g·c = −c exactly: all phases met are 0 or ½.
  - dim K = dim X = m(m−1) (both exact), so **K = δ_iso ⊗ X exactly**.
- **Trace structure (exact at m = 3, 5).** On the complement, gh is a pure permutation on its fixed labels (all phases 0) for h ∈ {1, N, γ, Nγ}, so tr(gh) = #Fix(gh).

| m | #Fix(g) = #Fix(gγ) | #Fix(gN) = #Fix(gNγ) | tr(g \| Fix(N,γ)) = (F₁ + F₂)/2 |
|---|---|---|---|
| 3 | 4 | 8 | 6 |
| 5 | 8 | 12 | 10 |

- **Partial symbolic argument (B).** For odd p^e ∥ m² − 1, g acts on the cyclic p-part as the scalar m ≡ ±1: +1 if p | m−1, −1 if p | m+1. This holds because g has trace 2m, determinant 1, and m² ≡ 1. So the fixed-point counts factor as (odd part) × (2-adic part), and the identity reduces to a 2-adic fixed-point count, F₁ + F₂ = 4m. The 2-adic count for general k is **not done**, so tr = 2m for all odd m stays B. It is exact per m at 3, 5, 7.

### (c) Reducible sectors at p² | s(s−2) (`finer.py` → `finer_9_11.json` not written; results are in the console line below)
- Π f(x) = 1_{t^⊥}(x)·(1/p)·Σ_j f(x + jt), where t generates the isotropic order-p subgroup of the p-part. Π commutes with ρ, ±1, γ (γt = (s−1)t ∈ ⟨t⟩) and the Z_q, so it splits each ε-sector into old (im Π) and new (im (1−Π)) pieces.
- **Exact (Cat A).**
  - s = 9: (+,+) old 12 and new 48, (−,−) new 12. Every piece is injective; 12 + 48 + 12 = 72.
  - s = 11: (+,+) old 18 and new 72, (−,−) new 20. All injective; total 110.
  - The (−,−) sector has no old piece.
- s = 25 hit the 760 s limit (Fraction arithmetic) and is not done.
- **Still open:** a uniform argument that each finer piece is irreducible and has a nonzero leading coefficient.

### (d) Atkin–Li at s = 7: not done
- `2026-10-17-cusp-part/characters.json` has only conductor ideals and types (conductor norms 1 or 5), not values. The s = 7 cusp characters have conductor norm 140, ramified at 𝔭₂, 𝔭₅, 𝔭₇, so ψ(𝔭_p) = 0 and a_p = 0. The Atkin–Li formula through a_p degenerates.
- The comparison needs the local root numbers ε(ψ_𝔭) = local Gauss sums of ψ on (O/𝔭^{f_𝔭})^×, which need the character values on local unit generators (presumably in `cusp_chars.pkl`). Not extracted this round.

---
## Update (box time Sun Oct 18 17:38 CDT 2026): closing proofs

### (a) x₂ is even on every Δ label, for all odd s: PROVED (Cat A)
- From `family_s.py`: D = lcm(s(s−2), 2(s−2)) = 2s(s−2) for odd s, det A = −s(s−2), and D·A⁻¹ = (D/det)·adj A = −2·[[s, −s], [−s, 2]].
  - So every L′ element D·A⁻¹n has second coordinate 2s·n₁ − 4n₂, which is even.
  - The shift is a = (D·s/(2(s−2)), −D/(s−2)) = (s², −2s), with even second coordinate.
  - ALS = L′ ∪ (L′ + a) mod D, and D is even, so every α ∈ ALS has α₂ even.
- vrank's Δ coordinates are (α₁ mod D, α₂ + εD mod 2D) with ε ∈ {0, 1}. Since D is even, x₂ is even.
- Combined with the previous update: (u_all + 1)·x ≡ 0 in Z/D × Z/2D, so Z_all = negation on Δ. Every ⟨γ, −1⟩-orbit is Z_all-stable, so P_ε = 0 whenever ε_all = −1. **ε_all = −1 sectors vanish for every odd s.**
- With the orbit lemma, **every surviving sector (ε_all = +1) has nonzero leading coefficient, for all odd s (Cat A).**

### (b) Complement g-split for all odd m: PROVED (Cat A)
Setup: s = 2m², m odd. For even s, A·a = (0, s/2) ∈ Z², so a ∈ L′ and the labels are L′/Z² (the Weil rep of L′/Z²). The complement C is the prime-to-m part of L′/Z² ≅ Z/2 × Z/(2m²(m²−1)), so C ≅ Z/2 × Z/(2(m²−1)), of order 4(m²−1) and exponent 2(m²−1).
1. **g acts by permutations.** g ∈ SO(A)(Z_(ℓ)) for ℓ ∤ m (sympy: gᵀAg = A, g² = γ). Isometries act in the Weil rep by δ_x ↦ δ_{gx} with no phase.
2. **γ = 1 on C.** γ ≡ (s−1)·I on L′/Z² (Cusp-Onset-Closure A2, Cat A), and s − 2 = 2(m²−1) is divisible by the exponent of C. So Fix(N, γ) = Fix(N) on C, and g² = γ = 1 there.
3. **Fixed-point counts.** ker(g ∓ 1 on C) = ((g ∓ 1)⁻¹Z² ∩ L′)/Z², localized away from m. Exactly (sympy):
   - A(g−1)⁻¹ = [[−1, m], [−m(2m+1), −m²]] and A(g+1)⁻¹ = [[1, m], [m(2m−1), m²]], both integral. So (g ∓ 1)⁻¹Z² ⊂ A⁻¹Z² = L′.
   - Hence #Fix(g) = |det(g−1)| = 2(m−1) and #Fix(−g) = |det(g+1)| = 2(m+1). Both are prime to m.
   - This matches the exact counts: m = 3 gives 4 and 8; m = 5 gives 8·1 and 4·3 with the odd factor.
4. **Trace.** tr(g | Fix N) = ½(tr g + tr gN) = ½(2(m−1) + 2(m+1)) = **2m**.
5. **Dimensions.** dim Fix(N) on C = (|C| + |C[2]|)/2 = (4(m²−1) + 4)/2 = 2m². Since g² = 1, dim{N = 1, g = −1} = (2m² − 2m)/2 = **m(m−1)** for every odd m.
- **Gap status.** K = δ_iso ⊗ X is exact at m = 3, 5 (previous update). For general odd m, "gap = m(m−1)" still needs the identification of the half-cone kernel with δ_iso ⊗ X (B). The dimension of X itself is now Cat A for all odd m. Even m is not treated.

### (d) s = 7 Atkin–Lehner data (`al_s7.py` → `al_s7.json`)
- I recomputed the 24 cusp ray-class characters with PARI (bnrinit over Q(√35), modulus 𝔭₂³𝔭₅𝔭₇·∞₁∞₂). All have conductor exponents (𝔭₂, 𝔭₅, 𝔭₇) = (2, 1, 1), norm 140.
- Global root numbers (lfunrootres, numerical, B) are non-real roots of unity, e.g. 0.93345 − 0.35870i. The characters have order 24 and are not self-dual, so W_N maps f to a multiple of f̄. The Atkin–Lehner "eigenvalues" are pseudo-eigenvalues of modulus 1, **not ±1**.
- Hence the local signs ε₅ = ε₇ = −1 cannot be compared with W_p eigenvalues directly. This is consistent with the dictionary result Z_p ↔ χ_p(−1)·W_p², not W_p.
- Exact pattern observed (B, numerical): the archimedean-twisted partner (inf [1,1]) of each ψ (inf [0,0]) has root number exactly −w(ψ).
- Not done: separating the global root number into local factors at 5 and 7.

### (c) Finer old/new pieces (`finer.py` → `finer.log`, `finer_9_11_25.json`)
- Now exact integer arithmetic (flint fmpz). A bug in the lift map was fixed (orbit totals N_O, not per-element counts). The odd-s results are unchanged; s = 25 is now done.
- **Exact (Cat A):**

| s | (+,+) old | (+,+) new | (−,−) new | total |
|---|---|---|---|---|
| 9 | 12 | 48 | 12 | 72 |
| 11 | 18 | 72 | 20 | 110 |
| 25 | 36 | 432 | 132 | 600 |

  Every piece is injective.
- **Leading coefficient.** In every new piece the ν₀ coefficient (2D²Q = −2s(s−2)) is nonzero. In every old piece it is zero, since ν₀ ∉ t^⊥. So the uniform argument covers the new pieces (where nonzero lift gives injectivity, given irreducibility); old-piece nonvanishing is exact per s only. Irreducibility of the pieces is not proved.

### (e) s = 98: the discrepancy is isolated to the 7-adic OLD pieces (`finer.py 98 40` → `finer98.log`)
- Exact ranks at Qmax = 40 (flint, about 0.9 GB):

| ε (3, 7) | piece | dim | lift rank | deficit |
|---|---|---|---|---|
| (+,+) | old | 68 | 42 | 26 |
| (+,+) | new | 1632 | 1632 | 0 |
| (−,+) | old | 30 | 12 | 18 |
| (−,+) | new | 720 | 720 | 0 |

  The piece ranks sum to 2406, equal to the total exact rank. So **all 44 missing dimensions live in the 98-dim old space** (functions on t^⊥ invariant under the 7Z/49 translation). The half-cone mechanism accounts for 42 of them (δ_iso ⊗ X, inside old). **The 2 extra relations, if real, are in the old pieces.**
- Old-only rank at Qmax = 130 is running (`finer_old.py` → `finerOld98_q130.log`).

---
## Update (box time Sun Oct 18 18:36 CDT 2026): resume after interruption
Earlier sections are unchanged. Status of each item:
- (a) **Proved (Cat A)** in the 17:38 section. D·A⁻¹ = −2·adj A gives even second coordinates on L′; a = (s², −2s); D is even. So Z_all = negation on Δ and the ε_all = −1 sectors vanish for all odd s. Not redone.
- (b) **Proved (Cat A)** in the 17:38 section, for the complement: #Fix(g) = |det(g−1)| = 2(m−1) and #Fix(−g) = |det(g+1)| = 2(m+1), because A(g∓1)⁻¹ is integral. γ = 1 on C, so tr = 2m and dim{N = 1, g = −1} = m(m−1) for all odd m. Identifying the half-cone kernel with δ_iso ⊗ X is exact only at m = 3, 5.
- (c) **Exact at s = 9, 11, 25** (flint integer ranks; `finer.py` → `finer.log`, `finer_9_11_25.json`). Every old/new piece is injective. The ν₀ coefficient is nonzero on every new piece and zero on every old piece. Partial: no uniform irreducibility proof, and no uniform leading vector for old pieces.
- (d) **Partial, unchanged** (`al_s7.py` → `al_s7.json`). Global root numbers are non-real, so the pseudo-eigenvalues are not ±1. The local factors at 5 and 7 were not separated.

### (e) s = 98: new exact results (memory capped with ulimit at 6 GB)
- Exact old-piece ranks are stable from Qmax = 40 to Qmax = 130 (`finerOld98_q130.log`): (+,+) old 68 → 42 and (−,+) old 30 → 12, so the old lift rank is 54. New pieces are injective. Total exact rank 2406 (Q40).
- `old98_g.py` → `old_g_18.json`, `old_g_50.json`, `old_g_98.json` (exact orbit counts on t^⊥/⟨t⟩). g = (γ+I)/(2m) is well defined on the old classes, with g² = γ.

| s | m | classes | ⟨γ,−1⟩-orbits | ⟨g,−1⟩-orbits | g-deficit | observed old deficit |
|---|---|---|---|---|---|---|
| 18 | 3 | 32 | 18 | 12 | 6 | 6 |
| 50 | 5 | 96 | 50 | 30 | 20 | 20 |
| 98 | 7 | 192 | 98 | 56 | 42 | **44** |

- At s = 98 the g-symmetry accounts for exactly 42 of the 44 missing old dimensions. **The 2 extra relations are confirmed exactly within the 98-dim old space (old lift rank 54 at Q40 and Q130), but their mechanism is not g.** The upper bound 56 on old rank is the half-cone/g bound; the lower bound 54 is exact. So dim V(98) ∈ [2406, 2408] stands, and the discrepancy is now localized to a 56-dim space.
- Lead (B): only at m = 7 among m = 3, 5, 7 is tr g + 2 = 2m + 2 a square (16). So h = (g+I)/4 ∈ SO(A)(Q) with h² = g (exact, sympy). This mirrors the s = 2m² criterion one level up (m = 2k² − 1). But h does **not** act single-valued on the 7-adic old classes (`old98_h.py` → `old_h_98.json`: 0 of 192 single-valued). If h explains the 2 relations, it must act on a 2-adic overlattice instead. Untested.

---
## Update (box time Sun Oct 18 18:44 CDT 2026): s = 98 extra relations found
### (e') The 2 extra relations at s = 98 come from h = (g+I)/4 (`old98_rel.py` → `old98_rel_Q40.json`; `old98_h2.py` → `old98_h2.json`)
- **Exact computation at Qmax = 40 (flint), in the old space.** There are 98 ⟨γ,−1⟩-orbits of classes on t^⊥/⟨t⟩.
  - Lift rank 54, kernel 44.
  - The 84 g-relations e_c − e_{gc} have rank 42 and all lie in the kernel (exact).
  - Rank(g-relations + kernel) = 44.
  - So the kernel is the 42 g-relations plus exactly **2 g-symmetric extra relations**, each a ±1 combination supported on a single T-eigenvalue:
    - R₁: q = 11/12, class orbits +{9, 41, 57, 89} and −{17, 32, 64, 81}, each of size 2.
    - R₂: q = 1/4, +{1 (size 1), 49 (size 2), 96 (size 1)} and −{24 (size 2), 72 (size 2)}, so 4 elements on each side.
- **Mechanism.** h = (g+I)/4 satisfies h² = g and hᵀAh = A (exact, sympy). It is multivalued on individual 7-adic classes, but as a set map on class orbits (all lifts mod Z² + Z·t, exact rational arithmetic) it sends **the + set of R₁ exactly onto its − set and back, and likewise for R₂**.
  - So each extra relation is θ(+set) = θ(h·(+set)) = θ(−set): an h-symmetry on a coarser 2-adic overlattice whose cosets are these unions.
  - This occurs only when 2m + 2 is a square (m = 2k² − 1; m = 7 is the first case > 1).
- **Status.**
  - The relation vectors are exact at Q40, and the old rank 54 is unchanged at Q130 (exact).
  - The h set-map property is exact.
  - The theta identity itself is not yet proved from an explicit h-invariant overlattice. Writing down that lattice is the remaining step.
  - If proved, **dim V(98) = 2406** (Cat A lower bound 2406, matching an upper bound 2408 − 2). Until then: lower bound 2406 exact, mechanism for the last 2 identified, B+.

### (b') At m = 7
- In the old space the half-cone/g relations are exactly the 42 = m(m−1) vectors e_c − e_{gc}, all in the exact kernel. This matches dim{N = 1, g = −1} = m(m−1) (Cat A for all odd m).
- The identification "half-cone kernel = δ_iso ⊗ X" at m = 7 holds at the level of dimension and location (the 7-adic old space), not checked vector by vector. The 2 extra relations are not of this type; they come from h.

### (c'), (d'): not attempted this round.

---
## Update (box time Sun Oct 18 18:51 CDT 2026): dim V(98) = 2406 closed
### 1. The h-lattice and the theta identities: dim V(98) = 2406 (Cat A) (`h_lattice.py` → `h_lattice.json`)
- **Lattice.** M = ∩_{k=0..7} h^k·M₇ with M₇ = Z² + Z·t₀, where t₀ = t/D is the 7-torsion isotropic vector. Explicitly (exact sympy HNF):
  - basis M = ⟨(4, 0), (1, 1/7)⟩, with [M₇ : M] = 4;
  - Gram matrix (2Q) = [[32, 64], [64, 32]], det −3072, even.
- **Invariance (exact).** h·M = M and h·M^♯ = M^♯ (M^♯ the A-dual). h is an isometry (hᵀAh = A), so it induces an automorphism of the discriminant form M^♯/M.
- **Coset maps (exact).** Let S₁± and S₂± be the + and − point sets of R₁ and R₂: unions of M₇-cosets, refined to M-cosets.
  - R₁ has 32 + 32 M-cosets and R₂ has 16 + 16.
  - h maps S_i^+ bijectively onto S_i^− as sets of M-cosets, for i = 1, 2.
- **Theta identity (proof).**
  - S_i^± is γ-invariant: it is a union of ⟨γ,−1⟩-class-orbits, and γ = h⁴ preserves M.
  - The four vrank cones ±[e₁, γe₁) and ±[f, γf) are fundamental domains for ⟨γ⟩ on the four open sectors cut out by the isotropic lines.
  - h has eigenvalues 2 ± √3 > 0, so it preserves each sector and commutes with γ. It therefore maps a fundamental domain to a fundamental domain, and the number of points of a γ-invariant set of given norm in a fundamental domain does not depend on the choice.
  - Since h(S⁺) = S⁻ and Q∘h = Q, the coefficients N_{S⁺}(q) = N_{S⁻}(q) for every q, i.e. θ(R_i⁺) = θ(R_i⁻) identically.
- **Conclusion.**
  - The 42 g-relations are proved identities: same argument with g on M₇, which is well defined (`old_g_98.json`) and has positive eigenvalues 7 ± √48.
  - The 2 h-relations are proved identities.
  - All 44 are independent (exact rank 44, `old98_rel_Q40.json`). So dim V ≤ 2450 − 44 = 2406. With the exact lower bound 2406: **dim V(98) = 2406 (Cat A).** The half-cone bound 2408 was not sharp.
- **m = 17 (s = 578): prediction only, not run.** 2m + 2 = 36 = 6², so h = (g+I)/6 exists in SO(A)(Q) with h² = g. The same mechanism predicts extra h-relations beyond m(m−1) = 272. Their number is #⟨g,−1⟩-orbits − #⟨h,−1⟩-orbits on the h-stable coarsening of the old classes. I did not compute that count, so no number is claimed. In general, extras are predicted exactly when m = 2k² − 1 (m = 7, 17, 31, …).

### 2. Half-cone/g relations = δ_iso ⊗ X
- **General proof for odd m (Cat A), given that g acts on M₇-classes.**
  - The m-part of L′/Z² is Z/m² (prime m) and t^⊥ = ⟨t⟩, so t^⊥/⟨t⟩ = (trivial m-part) ⊕ C. The old space (t^⊥-supported, t-invariant functions) is exactly δ_iso ⊗ Fun(C).
  - The g-relations are e_c − e_{gc} on ⟨γ,−1⟩-orbits, i.e. the image of (1 − g) on Fix(N, γ)|_C = Fix(N)|_C (γ = 1 on C).
  - Since g² = 1 on C, im(1 − g) is exactly the g = −1 eigenspace X. Hence span{g-relations} = δ_iso ⊗ X, of dimension m(m−1) (from (b)).
- **Check at m = 7 (exact).** The 84 g-relation vectors in the 98-dim old space have rank 42 = m(m−1) (exact, flint). Each is supported on old classes, i.e. lies in δ_iso ⊗ Fun(C). By the argument above they span δ_iso ⊗ X.
- **Remaining gaps.**
  - "g is well defined on M₇-classes" is exact at m = 3, 5, 7 (`old_g_*.json`) but not proved symbolically for all odd m.
  - For composite odd m the m-part is not cyclic and the isotropic subgroup has order m. Not treated.
  - That the half-cone kernel contains nothing beyond the g-relations is false in general (m = 7 has the h-relations), but the half-cone *bound* uses only g. So "half-cone relations = δ_iso ⊗ X" holds in that sense.

### 3. s = 7 local root numbers: blocker, not done
- **Method.** For ψ of conductor 𝔭₂²𝔭₅𝔭₇: the local character ψ_𝔭 on (O/𝔭)^× is ψ(u_𝔭)^{-1}, where u_𝔭 ≡ u mod 𝔭 and ≡ 1 mod the rest of the conductor (idealchinese, then bnrisprincipal). From that:
  - the local Gauss sum τ(ψ_𝔭) = Σ ψ_𝔭(u)·e(Tr(u/(𝔭·𝔡)));
  - the local root number ε_𝔭 = τ/√N𝔭, times the Langlands λ-factor for the induction K_𝔭/Q_p, which is ramified at 5 and 7 (λ = Gauss sum of the quadratic character).
- **Blocker.** This needs a correct additive character on O_𝔭 (inverse different 𝔡⁻¹ of Q(√35), ramified at 5 and 7) plus the λ-factor convention. I didn't implement it this session, and without it the comparison would be unreliable.
- **Known so far.** The global root numbers (B) are non-real, so W_p acts by pseudo-eigenvalues of modulus 1, and the sector-sign comparison has to be with χ_p(−1)·W_p², which is consistent (from earlier).

### 4. Old prime-square pieces: blocker, partial
- **Uniform leading vector.** The old piece is the lift of the overlattice M₇ = Z² + Z·t family: discriminant t^⊥/⟨t⟩, the form A on M₇. Its minimal-norm vector is the ν₀ analogue for M₇, i.e. the minimal |Q| over M₇^♯-cosets in the cone. The Nagell/orbit argument of item 1 carries over with d replaced by d/p² (the order Z[√(d/p²)]). Not written out or checked.
- **Irreducibility at s = 9, 11, 25.** Not tested. It needs ρ restricted to the old/new piece of U = Fix(N, γ) as a matrix representation (commutant dimension via ρ(S), ρ(T) on the piece). The pieces are currently built in orbit coordinates, where ρ(S) is not available; it needs the label-space projector. Blocker: building ρ on the old piece (about 1 h of work).

---
## Update (box time Sun Oct 18 19:02 CDT 2026): rev5 open items
### 3. g acts on the old classes, for all m (including composite): PROVED (Cat A) (`hcount.py` → `hcount_3_5_7_9_15_17.json`)
- **Explicit t₀.** t₀ = (0, 1/m). It lies in L′, since A·t₀ = (s/m, s/m) = (2m, 2m) ∈ Z². It has order m mod Z² and Qi(t₀) = s/m² = 2, so Q(t₀) = 1 and t₀ is isotropic. The m-part of L′/Z² ≅ Z/2 × Z/(2m²(m²−1)) is cyclic of order m², so ⟨t₀⟩ is its unique subgroup of order m.
- **Invariance.** M_t = Z² + Z·t₀ = Z ⊕ (1/m)Z, and g = [[0, −m], [1/m, 2m]]:
  - g(1, 0) = (0, 1/m) and g(0, 1/m) = (−1, 2);
  - g⁻¹ = [[2m, m], [−1/m, 0]], with g⁻¹(1, 0) = (2m, −1/m) and g⁻¹(0, 1/m) = (1, 0).
  - So **g·M_t = M_t for every m ≥ 1.** Exact check also passes at m = 3, 5, 7, 9, 15, 17.
- **Composite odd m.** In the cyclic m-part, t^⊥ = mZ/m² = ⟨t₀⟩ (B is nondegenerate there), so the old space is δ_iso ⊗ Fun(C) as for prime m. The complement results (γ = 1 on C; #Fix(±g) = 2(m ∓ 1); dim X = m(m−1)) used only the prime-to-m part. Hence **span{g-relations} = δ_iso ⊗ X, of dimension m(m−1), for all odd m (Cat A).** The relations are proved identities, by the fundamental-domain argument with g·M_t = M_t and g's eigenvalues m ± √(m²−1) > 0.
- Consequence: **dim V(2m²) ≤ (s/2)(s/2+1) − m(m−1) for all odd m (Cat A).**

### 4. m = 17 (s = 578): exact lattice-level counts (`hcount.py 17` → `hcount_17.json`; validated by `hcount_7.json`)
- **Method.** Purely lattice-theoretic, with no theta counts.
  - h = (g+I)/6: an isometry with h² = g (exact).
  - M = ∩_{k<4} h^k·M_t = ⟨(6, 0), (1, 1/17)⟩, Gram [[72, 216], [216, 72]], h·M = M, |M^♯/M| = 41472, all enumerated.
  - F = Fun(M_t^♯/M_t)^{⟨γ,−1⟩}.
  - rank_X = rank of the orbit-sum map F → Fun(⟨X,−1⟩-orbits on M^♯/M), computed exactly (flint).
  - Every θ(f) with f ∈ F factors through this map (θ(u) = θ(u∘X) for γ-invariant M-coset functions, by the fundamental-domain argument). So rank_X is a **proved upper bound** on the old lift rank.
- **Validation at m = 7.** dim F = 98, rank_g = 56, rank_h = 54, predicted extra = 2, matching the exact Fourier result.
- **m = 17.**
  - 1152 old classes, dim F = 578 = s;
  - rank_g = 306, giving deficit 272 = m(m−1);
  - rank_h = 300, giving **6 extra relations (Cat A as relations / upper bound)**.
  - Upper bound: dim V(578) ≤ 289·290 − 272 − 6 = 83532.
  - Not shown: that there are no further relations (lower bound); I did not attempt it, per instructions.
- **Pattern (B, two data points).** With 2m + 2 = (2k)², the extra count is k(k−1): k = 2 gives 2, k = 3 gives 6.

### 1. s = 7 local root numbers: blocker (attempted)
- **Plan.** At 𝔭₅ and 𝔭₇ (conductor exponent 1, tame, ramified, residue field F_p):
  - ε(ψ_𝔭) = ψ_𝔭(c_𝔭)·τ(ψ̄_𝔭|F_p^×)/√p, with c_𝔭 a generator of 𝔭·𝔡_𝔭;
  - ε(Ind) = ε(ψ_𝔭)·λ(K_𝔭/Q_p), with λ = ε(η_p, ½) = g(η_p)/√p (Langlands; Tate, "Number theoretic background", §3);
  - ψ_𝔭 on F_p^× is read from ψ((x)) with x ≡ u mod 𝔭 and ≡ 1 mod the other conductor primes (PARI idealchinese + bnrisprincipal).
- **Blocker.** The required check (product of local factors = global root number) also needs the **wild 2-adic factor** at 𝔭₂² and the archimedean factors. ε at 𝔭₂² needs a non-tame Gauss sum over (O/𝔭₂²)^× with an additive character of conductor 𝔡_{𝔭₂}⁻¹. Without it the product check is circular (ε₂ would be defined as w/(ε₅ε₇ε_∞)), so ε₅ and ε₇ could not be validated and I am not reporting values.
- Next step: implement the 2-adic local Gauss sum via PARI (ideallist / idealstar of 𝔭₂² with explicit generators) and an additive character e(Tr(x)/·) on 𝔡⁻¹.

### 2. Prime-square old pieces in label space: blocker (attempted)
- **Plan.** Π_label = (1/p)·Σ_j T_t^j·1_{t^⊥}, acting on labels (α, β) by α ↦ α + t, β fixed, with the Weil phase e(B(t, β)) needed for ρ-equivariance. Then compute the commutant dimension of ρ on the old/new piece of U = Fix(N) ∩ Fix(γ) at s = 9, 11, 25.
- **Blocker.** For odd s the label space carries the a/w_c twist, and the phase of the t-translation on labels with β = −a is not determined by the Δ-picture used so far. A wrong phase makes Π non-equivariant, which would invalidate the commutant test. I have not fixed this phase convention; the test is to check [Π, S] = 0 numerically and then exactly.
- The uniform leading vector for old pieces (minimal vector of M_t^♯ in the cone, with d → d/p²) is also not written out. It is the same Nagell argument with the order Z[√(d/p²)]: no new idea is needed, but it is not checked at s = 9, 11, 25.

---
## Update (box time Sun Oct 18 19:16 CDT 2026): m = 31, irreducibility in label space
### 3. m = 31 (s = 1922): extra = 12 = k(k−1) confirmed (Cat A as upper bound) (`hcount.py 31` → `hcount_31.json`)
- h = (g+I)/8. M = ⟨(8, 0), (1, 1/31)⟩, Gram [[128, 512], [512, 128]], |M^♯/M| = 245760, all enumerated.
- About 30 s run time, well under the 6 GB cap.
- 3840 old classes, dim F = 1922 = s; rank_g = 992, giving 930 = m(m−1); rank_h = 980, giving **12 extra relations = k(k−1) at k = 4**.
- Data: k = 2, 3, 4 give 2, 6, 12.
- **General proof sketch (B, not completed).** It mirrors the g case one level down:
  - tr h = (tr g + 2)/r = r = 2k and det h = 1, so |det(h−1)| = 2(k−1) and |det(h+1)| = 2(k+1);
  - h² = g = ±1 on the relevant classes, so the h = −1 eigenspace would have dim (2k² − 2k)/2 = k(k−1), provided the analogous "Fix = 2k², tr = 2k" holds on the h-relevant 2-adic part.
  - Not proved: identifying that part, i.e. the analogue of the complement C with γ = 1.

### 2. Irreducibility of the sectors in label space (`commutant.py` → `commutant_9.json`, `commutant_11.json`; `krylov_irr.py` → `krylov_irr_9.json`, `krylov_irr_11.json`)
- **Approach.** I avoided the translation-phase problem entirely by working with the ε-sectors E of U = Fix(N) ∩ Fix(γ) directly in label space. N, γ and the Z_p act with their exact label phases (red), and they commute with S to about 1e-15, so E is ρ-invariant.
- **Commutant dimension** (solved inside the T-eigenspace blocks; floating SVD, B):

| s | sector | dim | commutant | meaning |
|---|---|---|---|---|
| 9 | (+,+) | 60 | 2 | two non-isomorphic irreducibles |
| 9 | (−,−) | 12 | 1 | irreducible |
| 11 | (+,+) | 90 | 1 | irreducible |
| 11 | (−,−) | 20 | 1 | irreducible |

- **Cyclic span of simple-T-eigenvalue eigenvectors** (B): at s = 9 (+,+) it is 48, so the pieces are 48 (new) + 12 (old), matching the orbit-space split. At s = 11 every span is the full 90.
- **Correction (important).** At s = 11 the (+,+) sector is irreducible, so the orbit-space old/new split 18/72 from `finer.py` is **not** a ρ-decomposition there. The Δ-picture translation projector is not ρ-equivariant at s = 11 (presumably the label phase issue). The exact injectivity ranks in `finer.log` remain true as linear-algebra statements, but "old/new pieces" should only be read as ρ-pieces at s = 9.
- **Consequences (B, because the commutants are floating).**
  - At s = 11 both sectors are irreducible, so a nonzero ν₀ coefficient already gives injectivity.
  - At s = 9 the (+,+) sector has two irreducible pieces. The ν₀ coefficient handles the new piece; the old piece is covered by the exact rank.
- **s = 25:** not done. The label-space build (N = 2300, Python loops) plus the SVD exceeded the 700 s limit. A vectorised builder is needed.
- **Leading vector with d/p²:** not written out this round.

### 1. s = 7 local root numbers: still blocked
- I did not implement the wild 2-adic Gauss sum this round. The blocker from the previous section stands: without ε at 𝔭₂², the product check against the global root numbers is circular, so no ε₅ or ε₇ values are reported.

---
## Update (box time Sun Oct 18 19:37 CDT 2026): projector diagnosis, erratum wording
### 2. Why the finer.py "old/new" projector is not ρ-equivariant for odd s (exact diagnosis)
- For odd s the lattice (Z², A) is **odd**: Q(n) = nᵀAn/2 has s·n₂²/2 ∉ Z. So Q is not well defined mod 1 on L′/Z², and the family's T-action uses the shifted form q′(x) = Q(x) + B(x, w_c) (characteristic vector w_c).
- **Exact check** on L′/Z² (`family_s` exact Fractions), counting the order-p elements t:

| s | p | order-p elements | Q-isotropic | q′-isotropic | B(t, w_c) |
|---|---|---|---|---|---|
| 9 | 3 | 2 | 1 | 0 | 1/3 |
| 11 | 3 | 2 | 1 | 0 | 1/3 |
| 25 | 5 | 4 | 2 | 0 | 1/5, 2/5 |

- Hence **there is no q′-isotropic subgroup of order p** at these s. A translation-averaging operator with trivial phases cannot commute with T. finer.py tested isotropy with the untwisted Qi in the Δ = L₀′/L₀ coordinates, which is the wrong criterion for the label family.
- At s = 9 the image of Π happens to have the dimension (12) of a genuine ρ-invariant summand: the commutant there is 2, with pieces 48 + 12 (B). At s = 11 the (+,+) sector is irreducible (commutant 1, B), so no such summand exists. The s = 9 agreement is therefore dimensional, not a proof that Π is equivariant there.
- For **even** s (e.g. s = 98) the lattice is even, Q is well defined on L′/Z², and t₀ = (0, 1/m) is genuinely isotropic (Q(t₀) = 1). So the s = 98 old space and Theorem s98 are unaffected; that proof uses only theta identities, not equivariance of Π.

### Proposed erratum for rev5 §13.6, Proposition prop:psq5 (wording only; pushed files NOT edited)
> **Erratum (Prop. 13.x, "Prime-square sectors").** The "old/new pieces" in the table are the image and kernel of the translation-averaging projector Π computed in the Δ = L₀′/L₀ orbit model, with isotropy tested for the untwisted form Q. For odd s the lattice is odd and the family's T-action uses q′ = Q + B(·, w_c), for which no order-p isotropic subgroup exists at s = 9, 11, 25 (exact). So **Π is not ρ-equivariant, and the "pieces" are not subrepresentations in general.** At s = 11 the (+,+) sector is irreducible (floating commutant computation), so the 18/72 split is not a decomposition into ρ-pieces. The exact rank statements (every listed subspace has injective lift; the ν₀ coefficient is nonzero on the listed "new" subspaces) remain correct as linear-algebra statements. The phrase "splits each sector into old and new pieces" should read "splits each sector (as a vector space) into the image and kernel of Π", and the open item "irreducibility of the pieces" should be replaced by "irreducibility of the sectors: (+,+) at s = 9 has two irreducible summands (48 + 12); all other sectors at s = 9, 11 are irreducible (floating, Cat B)".

Also, in the Prop. orbit5 commentary: "Injectivity therefore follows wherever the sector is irreducible (squarefree s(s−2))" can add "and also at s = 11, where the sectors are irreducible (Cat B)".

### 1. Exact commutants and s = 25: not completed
- s = 9 and 11 remain floating (B). I did not implement the exact (cyclotomic or mod-ℓ) commutant this round.
- The s = 25 label-space run (`krylov_irr.py 25`) ran for more than 20 min wall time (about 157 min CPU, 2.8 GB) without finishing the sector build and Krylov step, and was stopped. Needed: a vectorised S builder (the current one makes N·|L′| ≈ 1.3·10⁶ Python reduce calls) plus a sparse or iterative null-space instead of a dense SVD of an 11500 × 2300 matrix.

### 3. h-extra count k(k−1) in general: not proved
- Exact data: k = 2, 3, 4 give 2, 6, 12 (`hcount_7.json`, `hcount_17.json`, `hcount_31.json`).
- tr h = 2k and |det(h ∓ 1)| = 2(k ∓ 1) (exact, symbolic). The mirror of the g proof needs a subquotient C_h of M^♯/M on which h² = 1, with |C_h| and |C_h[2]| giving dim Fix(N) = 2k². I have not identified C_h; at m = 7 the extra relations are not simple pairs (R₂ has 3 + 2 class orbits). Open.

### 4. Leading vector for prime-square pieces: superseded
- Item 2 shows the "old piece" is not a ρ-piece for odd s. A leading-vector argument for it is therefore not meaningful as stated.
- The relevant statements now:
  - At s = 11 the sectors are irreducible, so the existing ν₀ argument (Prop. orbit5) already gives injectivity.
  - At s = 9 the 12-dim summand needs its own nonzero coefficient. The exact rank already certifies it, but a uniform argument is not written.

## Update 2026-10-18 20:34 CDT — closing the (+,+) splits (s=9, s=25)
Script: split_modl.py. Logs/json: split_modl_9.json, split_modl_25.log.
Method, all over F_ℓ (same ℓ as before):
- Diagonalize T on the sector; it is semisimple mod ℓ (eigenspace dims = charpoly multiplicities, asserted).
- A commuting X is block-diagonal in that eigenbasis. Random linear functionals of S′X−XS′ give a nullspace that contains the true mod-ℓ commutant, so its dimension is a rigorous upper bound.
- The nullspace basis is then verified exactly (S′X = XS′ checked entrywise), so the mod-ℓ commutant is exactly that dimension.
- The eigenspaces of a non-scalar X give the invariant complement.
- s=9 (+,+): commutant mod ℓ = 2 exactly. X-eigenspaces have dims 12 and 48; each is S- and T-stable, the Krylov rank equals the dimension, and the sum has rank 60. So Ē = W̄48 ⊕ W̄12, two non-isomorphic irreducibles.
- s=25 (+,+): commutant mod ℓ = 2 exactly (84 / large-block unknowns, verified). An X-eigenspace of dim 36 is S-stable with Krylov rank 36. With the earlier Krylov ≥432 and commutant 2, this forces Ē = W̄432 ⊕ W̄36, two irreducibles. (The direct check on the 432-eigenspace hit the 40-min timeout; it is not needed for the conclusion.)
Lift to char 0: the image G is finite and its order involves only primes dividing 2·3·D, so ℓ ∤ |G|.
- The commutant is the G-fixed space of End(E). Its projector (1/|G|)Σg is defined over the localized ring O_λ, as is the sector projector. So dim_C commutant = dim_Fℓ commutant = 2.
- Unitarity then gives E = W1 ⊕ W2 with W1, W2 irreducible and non-isomorphic. Their reductions are the mod-ℓ summands, so the dimensions agree.
=> s=9 (+,+) = 48+12 and s=25 (+,+) = 432+36: **Cat A**, assuming ℓ ∤ |G| (true for the ℓ used; this was not machine-checked against |G| itself).
Guess 3(s−1)/2: holds at s=9 (12) and s=25 (36). At s=49 it predicts 72.
s=49 is NOT run: N=9212. The current dense nmod pipeline needs about 0.7 GB per N×N matrix plus a 4N×N stacked sector system (about 2.7 GB) and Python list conversions (about 85M ints, over 5 GB), so it would exceed the 6 GB cap. It would need a permutation-based sector basis plus applying S in blocks mod ℓ.
Conceptual link to the p-adic factor of the level-s/p² Weil representation: not investigated (needs s=49 first).

## Update 2026-10-18 21:02 CDT — lift check, s=49 split, p² pattern, h-orbit data
Files: lift_check.py, lift_check.json, sec_sparse.py, sec_sparse_{9,25,49}.json, sec_sparse_49.log, hcountB.py, hcountB_7_17.json, hcountB_31.json.
1. Lift check (exact, machine). N = Kbig, a multiple of ord(T). The Weil representation is congruence with level ord(T), so G is a quotient of Mp2(Z/N), and |Mp2(Z/N)| = 2·N³·∏_{p|N}(1−p^{−2}), which includes the primes of p²−1.
   - s=9: N=63504=2^4·3^4·7^2, order=334493080879104=2^18·3^12·7^4; ℓ=444529 does not divide it.
   - s=25: N=5290000=2^4·5^4·23^2, order=2^18·3^3·5^10·11·23^4; ℓ=21160001 does not divide it.
   - s=49: N=84860944=2^4·7^4·47^2, order=2^20·3^3·7^10·23·47^4; ℓ=1272914161 does not divide it.
   => The lift step is closed: (+,+) splits at s=9, 25 are **Cat A**. The only standard input is "Weil rep factors through Mp2(Z/ord T)".
2. s=49 (+,+), sparse pipeline (monomial maps → orbit basis; only sector rows of S; max RSS 1.11 GB; 21 min):
   - N=9212, sector dim 1800, mod-ℓ commutant = 2 (upper bound from 2664 unknowns; basis verified exactly).
   - Pieces 72 + 1728, each S,T-invariant.
   - With item 1 (ℓ ∤ |Mp2(Z/N)|): **Cat A** split 1728 + 72. The 3(s−1)/2 guess holds at s=9, 25, 49.
   - Re-run of s=9/25 in the same pipeline: 12+48 and 36+432, consistent.
3a. Prime-square pattern. Exact at p=3, 5, 7:
   - sector dim = 3·(p²−1)/2·(p²+1)/2 (60, 468, 1800);
   - complement = 3·(p²−1)/2;
   - big piece = 3·((p²−1)/2)² (48, 432, 1728).
   This is consistent with sector ≅ A ⊗ (1 ⊕ R), where dim A = 3(p²−1)/2 and dim R = (p²−1)/2, with complement A⊗1. No identification with a lower-level Weil piece was made. The general statement is **OPEN** (3 data points, exact).
3b. k(k−1) for m=2k²−1. Exact new data: h acts as an involution on ⟨g,γ,−1⟩-orbits on M#/M. Among the g-orbits meeting old classes:
   - m=7: 104 orbits, 4 h-fixed;
   - m=17: 744 orbits, 6 h-fixed;
   - m=31: 2432 orbits, 8 h-fixed.
   So the h-fixed count is 2k (= tr h), exact at k=2, 3, 4. The numbers of old orbits moved to non-old orbits are 48, 438, 1440.
   No derivation of k(k−1) from this. The general k(k−1) proof is **OPEN**.

## Update 2026-10-18 21:15 CDT — RETRACTION of sector results; valid sectors; p-old identification; (b) pair counts
**Retraction (important).** In the vecfam/Family label model, the maps 'neg' and Z_q (q | s−2) do NOT commute with S, T.
- At s=9 and s=11: |[X,S]| ≈ 1.95 and |[X,T]| ≈ 1.47. Also XSX⁻¹ ≠ cS.
- commutant_9.json already recorded max_commutator_with_S=0.2457 (0.198 at s=11). This was not noticed earlier.
- The ε-sectors that used neg and Z_q are therefore not ρ-invariant: S-leak 2.02 at s=9 (+,+), 2.05 at (−,−), 2.53 and 2.19 at s=11.
**Withdrawn:**
- all commutant/irreducibility/split claims on those sectors: the floating commutants (s=9 60→2, 12→1; s=11 90, 20);
- irr_modl/split_modl/sec_sparse results;
- "48+12, 432+36, 1728+72 Cat A";
- the s=9 (−,−), s=11, s=25 (−,−) irreducibility claims.
The lift_check numbers (ℓ ∤ |Mp2(Z/N)|) remain correct.
Maps verified to commute (|[X,S]| = |[X,T]| = 0.0): γ, and Z_p for p | s.

**Valid sector** V_s = Fix(γ) ∩ Fix(Z_p), p | s. Script sec_valid.py; outputs sec_valid_{9,25}.json.
- s=9: dim 105. Mod-ℓ commutant 4 (verified exactly). Pieces 9+12+36+48, each S,T-invariant, summing to 105, with distinct X-eigenvalues.
- s=25: dim 897. Commutant 4. Pieces 33+36+396+432.
- Via ℓ ∤ |Mp2(Z/N)| (lift_check.json): 4 pairwise non-isomorphic irreducibles. **Cat A** at s=9 and s=25 (modulo the standard "Weil rep factors through Mp2(Z/ord T)").
- So 12, 48 and 36, 432 are genuine irreducible constituents of V_s.

**(a) p-old identification.** Script p_old.py; outputs p_old_{9,25}.json, p_old_49.log.
- Method: F = vectors in V_s fixed by T_p = T^c (c ≡ 1 mod N_p, ≡ 0 mod N/N_p) and by S T_p S⁻¹. These two elements generate the image of the p-local SL2 factor.
- s=9: dim F = 21 = 12+9, and dim V/dim F = 5 = (p²+1)/2.
- s=25: dim F = 69 = 36+33, ratio 13.
- s=49: dim F = 141 = 3·47, ratio 25.
- In all three, F is S,T-invariant (rank check). Exact.
- Consistent decomposition: V_s ≅ F ⊗ ρ_p^{even}, with ρ_p^{even} = 1 ⊕ R, dim R = (p²−1)/2 (trivial = p-old from isotropic pZ/p²; R irreducible p-new — Nobs–Wolfart / Cliff–McNeilly–Szechtman, cited, not re-proved).
- F = 3(s−1)/2 ⊕ 3(s−3)/2 (12+9, 36+33), i.e. 3 ⊗ (even ⊕ odd part of the Weil rep of Z/(s−2)).
- Pieces: F_±⊗1 and F_±⊗R give 3(s−1)/2, 3(s−3)/2, 3(s−1)(s−1)/4, 3(s−3)(s−1)/4. Matches s=9 and s=25 exactly.
- Status:
  - the identification is **exact at p=3,5** (full split) and **p=7** (dim F and ratio only; the full split at s=49 was not run, est. about 2.5 h);
  - the general proof is **OPEN**. It needs (i) γ trivial on the p-factor in general, (ii) dim F_± = 3(s∓1… )/2 from the q-adic and 2-adic factors, and (iii) irreducibility when s−2 is composite (e.g. p=11, s−2=119).
**(b) h pair counts** (hcountB_*.json):

| k | old→old h-moved g-orbits | pairs | k(k−1) | rank_g |
|---|---|---|---|---|
| 2 | 52 | 26 | 2 | 56 |
| 3 | 300 | 150 | 6 | 306 |
| 4 | 984 | 492 | 12 | 992 |

- No formula of the form "half of the pairs minus corrections" matches k(k−1).
- Exact observation: old→old moved = rank_g − 2k at k=2,3,4.
- The k(k−1) proof is **OPEN**; the integrality attempt was not reached.

## Update 2026-10-18 21:18 CDT — the 21:16 retraction is itself wrong (see 2026-10-18-Symmetry-Audit.md)
- The neg/Z_q non-commutation was a transpose-convention bug in my map builders (X[j,i] instead of Y[i,j]).
- With Y = Family.Pmatrix's convention, all maps commute exactly.
- Correct-convention sectors reproduce:
  - 12+48 (s=9), 18+72 (s=11), 36+432 (s=25), each with commutant 2, Cat A, invariance certified;
  - (−,−) irreducible.
- The sec_valid "Fix(γ)∩Fix(Z_p)" results stand as statements about that larger space only.

## Update 2026-10-18 21:51 CDT — s=49 corrected; prime-square structure theorem; k(k−1) status
(All operators in the corrected Y = Pmatrix convention.)
**1. s=49 (+,+), Cat A.**
- sec_fixed.py, log sec_fixed_49.log: dim 1800; invariance certificate 0 failures (300 sampled rows); mod-ℓ commutant = 2 (2664 unknowns, basis verified exactly); pieces 72 + 1728, each S,T-invariant. ℓ=1272914161 ∤ |Mp2(Z/N)| (lift_check.json).
- p_old_fixed_49_1,1.json: the p=7 local invariants have dim 72, are S,T-invariant, and dim(+,+)/72 = 25 = (p²+1)/2.
- So the 72 piece is the p-local invariant piece.

**2. Prime-square structure.**
Setting: s = p², p odd. Cited inputs:
- (C1) rev4 Thm tensorodd (Cat A there, symbolic):
  - ρ ≅ ρ_(s) ⊗ ρ_(s−2) ⊗ ρ₂ in tensor coordinates, where ρ_m is the Weil rep of Z/m (CRT part of e(−2xy/n));
  - neg = ⊗_p Z_p ⊗ I₄ and γ = Z_(s) ⊗ I ⊗ Z₂;
  - ρ₂ = A₃ ⊕ B₁ with A₃ irreducible.
- (C2) The image of SL₂(Z) (or Mp₂) is the product of the local images. This is CRT surjectivity SL₂(Z) → ∏ SL₂(Z/p^e), as in rev4.
- (C3) Nobs–Wolfart / Cliff–McNeilly–Szechtman, cited and not re-proved:
  - for Z/p² with a nondegenerate form, the even part W⁺ = 1 ⊕ R, where 1 = span(δ_{pZ/p²}) is the unique SL₂-invariant line and R is irreducible of dim (p²−1)/2;
  - for a prime q, the even part (dim (q+1)/2) and the odd part (dim (q−1)/2) of the Weil rep of Z/q are irreducible.

Theorem (proved from C1–C3). Let ε = (ε_q)_{q | s−2} be the signs, with Z_(s) = +. The sector Σ_ε = W_p⁺ ⊗ (⊗_q W_q^{ε_q}) ⊗ A₃. (γ = +1 with Z_(s) = + forces Z₂ = +, hence A₃.)
- (i) The p-local invariants of Σ_ε are 1 ⊗ (⊗_q W_q^{ε_q}) ⊗ A₃, of dim 3·∏_q dim W_q^{ε_q}. Summed over the ε with Z_(s−2) = +, this gives 3·E(s−2) = 3(s−1)/2.
- (ii) If s−2 is squarefree, each W_q^{ε_q} is irreducible (C3). The complement R ⊗ (⊗ W_q^{ε_q}) ⊗ A₃ is an outer tensor product of irreducibles of the product group (C2), hence irreducible. The invariant piece is also irreducible, and the two are non-isomorphic (one is p-trivial, the other is not).
- (iii) When s−2 is prime (p = 3, 5, 7: s−2 = 7, 23, 47), the "(+,+)" sector is one Σ_ε. Its pieces are 3(s−1)/2 and 3(s−1)(s−1)/4 = 12+48, 36+432, 72+1728. This matches the exact runs, so the theorem is confirmed by data at p = 3, 5, 7.
- Caveats:
  - for composite squarefree s−2 (p = 11: 119 = 7·17), the sector splits per prime sign. For (+,+,+) the invariant piece is 3·4·9 = 108 and the complement is 3·60·36 = 6480. 3(s−1)/2 = 180 is the total over (ε₇,ε₁₇) ∈ {(+,+),(−,−)}, i.e. 108 + 72;
  - if q² | s−2, the complement is reducible (C3 for Z/q²).
- Status: **Cat A conditional on the cited C3**. C1 and C2 are proved in rev4.
- s=121 was not run: VF needs a D² table with D = 28798, i.e. 8.3·10⁸ int64 = 6.6 GB, plus a 2·10⁸-iteration LP enumeration. Over the cap; prediction only.

**3. k(k−1).**
- Exact identities: rank_g = m(m+1) at m = 7, 17, 31 (56, 306, 992). Old→old pairs P = (rank_g − 2k)/2 = k(k−1)(2k²+2k+1) (26, 150, 492).
- This "fit" is an algebraic identity given m = 2k²−1. It does not involve rank_h, so it gives no handle on rank_g − rank_h.
- The h-integrality analogue (A(h∓1)⁻¹, |det(h∓1)| = 2(k∓1)) was not turned into a count.
- **OPEN**; nothing new proved.

## Update 2026-10-18 21:53 CDT — closed h-orbits (k=2,3,4); factor-dimension check at s=121
**1. Burnside-style count** (hcountC.py, hcountC_7_17_31.json; exact).
Definitions: g-orbit = ⟨g,γ,−1⟩-orbit on M#/M. An old g-orbit is one that meets old classes; all of them turned out to be fully old.

| k (m) | old g-orbits | closed (O and hO old) | closed h-fixed | closed non-fixed | rank of span V(O) | rank span{V(O)−V(hO)} | rank_g − rank_h |
|---|---|---|---|---|---|---|---|
| 2 (7) | 104 | 56 | 4 | 52 | 56 | 12 | 2 |
| 3 (17) | 744 | 306 | 6 | 300 | 306 | 48 | 6 |
| 4 (31) | 2432 | 992 | 8 | 984 | 992 | 120 | 12 |

- Exact fits at three points:
  - #closed = m(m+1) = rank_g;
  - h-fixed closed = 2k;
  - rank of the differences = 2k(k²−1) (12, 48, 120).
- The difference span is NOT k(k−1). k(k−1) is the drop rank_g − rank_h, which is a different quantity: the drop of the merged-column span, not the dimension of the difference span. The proposed identification fails.
- No formula proof for #closed: m(m+1) is an empirical identity here, matching rank_g. The k(k−1) proof remains **OPEN**.

**2. s=121 factor dimensions** (factor_dims.py, factor_dims2.py, factor_dims_121.json; exact mod ℓ; both square classes of the form unit u checked).
This checks the factor dimensions only; it is NOT a full label-space run.
- Z/121 even part: dim 61, commutant 2, normalised-invariant line dim 1. So 1 ⊕ R, with R of dim 60.
- Z/121 odd part: dim 60, irreducible.
- Z/7: even 4 and odd 3, both irreducible. Z/17: even 9 and odd 8, both irreducible.
- With A₃ = 3 (rev4):
  - sector (ε₁₁,ε₇,ε₁₇) = (+,+,+): p-invariants 1·4·9·3 = **108**, complement 60·4·9·3 = 6480 (irreducible by the outer-tensor argument);
  - (+,−,−): p-invariants 1·3·8·3 = **72**, complement 4320;
  - total 180 = 3(s−1)/2.
- These are the predictions, computed from exact factor data plus the cited tensor factorization.

## Update 2026-10-18 22:10 CDT — h-eigenspace data; Weil Z/p² re-derived for p ≤ 13 (and 59); non-squarefree s−2 (s=3481)
**1. k(k−1), h-eigenspaces** (hcountD.py, hcountD_7_17_31.json; exact).
Setup: Y = old g-orbits ∪ their h-images; h is an involution on Y. V maps Fun(Y) to the old-class function space (dim_F).

| k | \|Y\| | h-fixed | dim + | dim − | rank on + | rank on − | ker + | ker − | rank_g | rank_g − rank(+) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 152 | 4 | 78 | 74 | 54 | 50 | 24 | 24 | 56 | 2 |
| 3 | 1182 | 6 | 594 | 588 | 300 | 294 | 294 | 294 | 306 | 6 |
| 4 | 3872 | 8 | 1940 | 1932 | 980 | 972 | 960 | 960 | 992 | 12 |

- rank on the + eigenspace = rank_h exactly. So the extra relations are the drop when restricting to h-even (symmetrised) functions.
- dim± = (|Y| ± 2k)/2: the trace formula with tr h = 2k holds exactly.
- Exact empirical facts: ker+ = ker−, hence rank+ − rank− = 2k.
- Consequence: extra = k(k−1) ⇔ rank+ + rank− = 2(m(m+1) − k²) (checked at 3 points).
- No proof of ker+ = ker− or of that sum. X (the space where the drop lives) is not identified. **OPEN.**
**2a. Even Weil rep of Z/p² = 1 ⊕ R** (weil_cyclic.py; weil_cyclic_9_25_49_121_169_71.json, weil_cyclic_3481.log; exact, both square classes of u).
- Results:
  - even part: dim (p²+1)/2, mod-ℓ commutant = 2 (basis verified exactly) for p = 3, 5, 7, 11, 13, 59;
  - odd part: dim (p²−1)/2, commutant 1;
  - Z/71: even 36 and odd 35, both commutant 1.
- Char-0 argument, needing no |G| hypothesis: the char-0 commutant is at most the mod-ℓ commutant (semicontinuity). The char-0 even part contains the explicit invariant line spanned by δ_{pZ/p²} and its orthogonal complement, so its commutant is ≥ 2.
- Hence even = 1 ⊕ R with R irreducible of dim (p²−1)/2, and odd is irreducible. **Cat A for p ∈ {3,5,7,11,13,59}**; the general p case is still cited (NW/CMS).
- (A bug in the first version — the f_0 = 2e_0 normalisation — gave commutant 1; it was fixed before the reported run.)
- By-product: with C1 (rev4 tensor theorem) this gives a char-0 invariant decomposition of (+,+) at s = 9, 25, 49 directly. So "commutant = 2" there no longer needs the ℓ ∤ |Mp2(Z/N)| lift.
**2b. Weil rep factors through Mp2(Z/N), N = level** — written outline, still partly cited:
- (i) Kernel-of-the-level statement: ρ_D(T^N) = 1, and for γ ∈ Γ0(N) Scheithauer's/Borcherds' formula gives ρ_D(γ)e_x = χ_D(γ) e(bd q(x)) e_{dx}. For γ ∈ Γ(N), d ≡ 1 and b ≡ 0 mod N, so ρ_D(γ) = χ_D(γ)·I. χ_D is a quadratic (Jacobi-symbol) character of d, trivial for d ≡ 1 mod N, up to the metaplectic sign for odd signature.
- (ii) Hence ker ⊇ Γ(N) (or its metaplectic lift), and the image is a quotient of Mp2(Z/N).
- The Γ0(N) formula in (i) is cited, not re-derived. **Status: cited/outlined**, not Cat A.
- No current result depends on (b) any more (see the 2a by-product), except the s=49 1728/72 irreducibility: 72 is irreducible via 2a + C1, and so is 1728 = R₇ ⊗ W₄₇⁺ ⊗ A₃ (2a for p=7 plus q=47: even part irreducible, cited for q=47, not run).
**3. Non-squarefree s−2.** Smallest odd prime-square: s = 59² = 3481, s−2 = 3479 = 7²·71.
- Exact factor data (this checks factor dimensions only, NOT a full run):
  - Z/3481: even 1741 = 1 ⊕ 1740, odd 1740 irreducible;
  - Z/49: even 25 = 1 ⊕ 24, odd 24 irreducible;
  - Z/71: even 36 and odd 35, both irreducible;
  - A₃ = 3.
- Predicted sector decomposition (ε₅₉ = +):
  - (+,+,+), with factors W₅₉⁺ ⊗ W₄₉⁺ ⊗ W₇₁⁺ ⊗ A₃:
    - p-invariants 108 (1·1·36·3) + 2592 (1·24·36·3) = 2700;
    - complement 187920 (1740·1·36·3) ⊕ 4510080 (1740·24·36·3), i.e. reducible, two irreducibles.
  - (+,−,−): p-invariants 24·35·3 = 2520 (irreducible); complement 1740·2520 = 4384800 (irreducible).
  - Total p-invariants 2700 + 2520 = 5220 = 3(s−1)/2.
