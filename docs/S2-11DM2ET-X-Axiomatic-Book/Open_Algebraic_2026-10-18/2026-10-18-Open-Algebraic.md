> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** Dated update sections are cumulative; later sections supersede earlier 'open' statements. In particular Item 3 (s = 98) is closed in the 18:51 section: dim V(98) = 2406 (Cat A; rev. 5 Theorem 13.16). The m = 17 extra-relation count is a prediction only (no number). Atkin–Lehner local split and old prime-square irreducibility remain open. Category convention for Master (rev. 5): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Naming as in rev. 4: W_P = Fix(P); V_Eis/d_Eis = Eisenstein span/dimension; Theorem G = Lewis–Zagier; Lemma Prod1/Prod2; d_2(k,v). No 'Theorem L' label is introduced (Theorem L = the framework's Parity Dominance Theorem; Lemma L keeps its name). Erratum: ERRATUM_Consolidated_Rev5_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev5_2026-10-18/ (§13). No TPC/RH claim; distinct from HQCC termination claims; CORE_FREEZE holds.

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
