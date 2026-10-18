> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** W here = Fix(P), dim 72 (Master: W_P). S here is S_lab; rho(S) := S_lab^{-1} (rev. 4, Remark 11.2). Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# Tensor pattern: closure of the open items (2026-10-18)
Continues 2026-10-18-Tensor-Pattern-Proof.md. Scripts and outputs are in 2026-10-18-Tensor-Pattern-Closure/: exact.py, factor.py/.txt, gaction.py/.txt, local2.py/.txt, closure_exact.py/.txt, rank_modp.py/.txt, rho2.py/.txt, cusp_sector.txt, family.py. Local only; nothing pushed.

## Key finding: S and T factor exactly as tensor products (Cat A)
- Every entry of S is a single term e(r)/√35 with r ∈ Q (35 nonzero entries per row). T is monomial. So both matrices are exact over Q(ζ₁₄₀), with denominators ≤ 70 for S and ≤ 140 for T (exact.py).
- Use the adapted basis u′_{x,ε,δ} := u_{xg+εa₂, −δa₂}, where g = (14,6)/70 generates L′/Z² ≅ Z/35 and a₂ = (½,0). This works because a = a₂ + a_odd with a_odd = (1/5,−1/5) ∈ L′. Write x ↔ (x₅,x₇) by CRT. Then exactly (factor.py):
  - S = (F₅/√5) ⊗ (F₇/√7) ⊗ S₂ with F_p[x,y] = e(4xy/p);
  - T = T₅ ⊗ T₇ ⊗ T₂ with T_p = diag e(2x²/p).
- S₂ and T₂ are 4×4 monomial matrices on the theta characteristics (ε,δ) ∈ {0,½}²:
  - S₂: 00↦00, 01↔10, 11↦−11;
  - T₂: 00↔01, 10↦i·10, 11↦i·11.

## 1. Factorization through SL₂(Z/140) and the local multiplicities: Cat A
- **Convention.** The label matrices satisfy the SL₂ relations with S replaced by S⁻¹. Define ρ(S) := S⁻¹ and ρ(T) := T. This explains the earlier residual of 1 for "(ST)³ ≠ P on all 140 labels". On W, S = S⁻¹, so nothing changes there.
- **Local factors.**
  - ρ_p(S) = γ_p·conj(F_p)/√p and ρ_p(T) = T_p, with γ₅ = −1 and γ₇ = e(3/4).
  - Exactly in Z[ζ_p]: (conj(F_p)·T_p)³ = c·Z_p with c² = +125 (p=5) and c² = −343 (p=7) (closure_exact.py (c)). This gives γ_p up to a sign. The sign follows from Gauss's sign of the quadratic Gauss sum (and agrees numerically, with a separation of 2p^{3/2}).
  - ρ_p is then exactly the Weil representation of (Z/p, q_p = 2x²/p): T ↦ e(q), and S ↦ γ/√p · e(−b) with b(x,y) = 4xy/p the bilinear form of q_p.
  - By the congruence theorem for Weil representations of finite quadratic modules of odd level, ρ_p factors through SL₂(Z/p). The hypothesis (an exact match with the Weil formula, level p) is checked above. References: Nobs–Wolfart 1976; Skoruppa; Strömberg, Math. Z. 2013.
  - The ± halves of W_p are irreducible of dims (p±1)/2. This is classical, and matches the norm-1 characters found earlier.
- **2-adic factor.** ρ₂ := (e(3/4)·S₂⁻¹, T₂) satisfies S⁴ = I, (ST)³ = S² = −I and T⁴ = I exactly (Fractions). The pair group (ρ₂(g), g mod 4) has exactly 48 elements, so ρ₂ factors through SL₂(Z/4) and is faithful (rho2.py).
- **Product.** ρ₅(S)⊗ρ₇(S)⊗ρ₂(S) = S⁻¹ exactly (the scalars γ cancel) and ρ₅(T)⊗ρ₇(T)⊗ρ₂(T) = T. So ρ on all 140 labels, and hence on W, factors through SL₂(Z/140).
- **P and W.** P = ρ(−I) = γ₅²Z₅ ⊗ γ₇²Z₇ ⊗ (−I₄) = Z₅⊗Z₇⊗I₄. Hence W = Fix(P) = (W₅⁺⊗W₇⁺ ⊕ W₅⁻⊗W₇⁻) ⊗ C⁴ exactly. Mixed parities are excluded, and the restrictions are exactly 16·W₅⁺ + 12·W₅⁻, 12·W₇⁺ + 8·W₇⁻ and 18·(A₃+B₁).
- **S spectrum.** It is exact via Gauss sums:
  - tr ρ₅(S)|W₅^± = (−1, 0);
  - tr ρ₇(S)|W₇^± = (0, −1);
  - tr ρ₂(S)|A₃ = −i and tr ρ₂(S)|B₁ = i.

  So tr S = 0 on all four pieces, with n± = 18/18 (V_Eis), 3/3 (V_cusp), 6/6 (B₁⊗X⁺) and 9/9 (A₃⊗X⁻); 36/36 on W.

## 2. The lift kills V^⊥: Cat A
- Two exact identities of functions:
  - negation, u_{−α,−β} = u_{α,β}, which acts on u′ as Z₅⊗Z₇⊗I₄;
  - the unit γ = 6+√35, u_{γα,γβ} = u_{α,β}, which holds by construction (γ-orbit average, with γ² label-trivial). It acts as I₅⊗Z₇⊗diag(1,1,1,−1) (closure_exact.py (a), exact).
- So V ⊆ Fix(N) ∩ Fix(γ). Exactly, that is Z₅Z₇ = +1 and Z₇Z₂ = +1, i.e. even⊗even⊗{00,01,10} ⊕ odd⊗odd⊗{11} = A₃⊗X⁺ ⊕ B₁⊗X⁻, of dim 42. The orbit-cocycle count gives 42 free orbits.
- Lower bound: the exact Fourier matrix (sums of 4900th roots of unity divided by 2, |Q| ≤ 25) has rank 42 modulo a prime above ℓ = 29401 ≡ 1 mod 4900. Rank cannot increase under reduction, so the rank in characteristic 0 is ≥ 42 (rank_modp.py).
- **Hence V = A₃⊗X⁺ ⊕ B₁⊗X⁻ exactly, and V^⊥ is killed.** The mechanism is the γ phase flip: the unit acts by −1 at 7 and by −1 on the odd characteristic. This is the analogue of R3.4.
- Bonus (exact): the forced zeros are the 6 inconsistent orbits. They are exactly the 11 labels (x₅x₇ = 0, ε = δ = 1), i.e. indices 71, 95, 107, 117, 127, 129, 131, 133, 135, 137, 139, matching the earlier numerical list.

## 3. 2-adic origin of A₃ and B₁: Cat A
- The 2-adic factor is the action on the four theta characteristics [ε,δ] ∈ {0,½}² carried by the a₂-shift and the β = −a₂ character (the w_c twist of the odd lattice). It transforms like the Jacobi characteristics: S swaps 01↔10, T swaps 00↔01, and the odd characteristic 11 is fixed with a sign.
- A₃ = span of the 3 even characteristics (00, 01, 10). It is irreducible (character norm 1, exact Gaussian-integer values) with T-spectrum {1, −1, i}.
- B₁ = the odd characteristic 11: S ↦ e(1/4), T ↦ e(1/4).
- ⟨A₃,B₁⟩ = 0. The image of ρ₂ is SL₂(Z/4), of order 48.

## 4. Arithmetic of the Eisenstein/cusp assignment
- Cat A:
  - The fitF cusp labels are exactly the 24 nonzero labels with (ε,δ) = (1,1), i.e. the odd-characteristic sector (cusp_sector.txt).
  - The local actions of the fundamental unit are ε₀ = 6+√35 ≡ 6 ≡ +1 mod 𝔭₅ and ≡ −1 mod 𝔭₇, which is the exact origin of I₅⊗Z₇ in γ.
- Cat B (argument; not formalised):
  - A Hecke character ψ contributes only if ψ(ε₀) = 1 and ψ(−1) = 1.
  - With ψ₅(ε₀) = 1 and ψ₇(ε₀) = ψ₇(−1), oddness at 7 forces the odd 2-adic characteristic, and P forces the same parity at 5 and 7.
  - Genus characters χ∘N have ψ_p(−1) = χ_p(N(−1)) = 1 at the ramified primes, so they are even and land in X⁺, in the even-characteristic sector A₃. This is the Eisenstein part.
  - Characters that are odd at 5 and 7 cannot be genus characters, so they are not σ-invariant. Their Hecke–Maass theta series are cusp forms (Maass), which gives B₁⊗X⁻.

## 5. Other open items
- **Proportionality constants (Cat A).** Each of the 42 classes is a free orbit of ⟨N,γ⟩ (sizes 1/2/4: 3/15/24, matching the earlier numerical classes). The constants are ±1 in the u′ basis, and roots of unity e(r) with denominators in {1, 2, 5, 10} in the original u basis.
- **Atkin–Lehner-type involutions.** The local reflections Z₅ and Z₇ and Z₂ = diag(1,1,1,−1) commute exactly with ρ (Cat A).
  - V_Eis: (Z₅,Z₇,Z₂) = (+,+,+); V_cusp: (−,−,−); B₁⊗X⁺: (+,+,−); A₃⊗X⁻: (−,−,+).
  - So Z₅Z₇ = +1 on W (this is P), and Z₇Z₂ = +1 exactly on V (this is γ).
  - S commutes with all three, and n± = d/2 in every eigenspace (exact traces above).
  - Identifying Z₅, Z₇, Z₂ with the classical Atkin–Lehner operators W₅, W₇, W₄ on the lifted forms is Cat B (not checked on the forms).

## Status summary
- Cat A: tensor factorization; congruence through SL₂(Z/140) (exact plus the cited Weil theorem); local multiplicities; P = Z₅Z₇; W structure; V = A₃⊗X⁺ ⊕ B₁⊗X⁻ (exact upper bound plus exact modular lower bound); zero labels; proportionality constants; 2-adic factor = theta characteristics; exact S traces and n±; commuting involutions.
- Cat B: the Hecke-character derivation of the Eisenstein/cusp assignment (the exact label-sector match is Cat A); naming Z_p as Atkin–Lehner.
- Remaining dependency: the classification "cusp" for the odd sector rests on the earlier numerical ray-class fits (fitF) together with the classical Maass theorem; it is not re-proved exactly.
