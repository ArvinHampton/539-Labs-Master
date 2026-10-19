# Algebraic Round 3 — 2026-10-18 (late, CDT)
Folder: 2026-10-18-Algebraic-Round3/. New files only. Nothing pushed; no existing file edited.
Categories: Cat A = proved or exact (exact finite computation, or mod-ℓ with a lift). Cat B = floating-point or cited-only.
Label convention: Y[i, j(i)] (NOTE_X_CONVENTION.md). Item 1 uses no label operators, only lattice classes.
No TPC/RH claims. This is separate from the HQCC termination claims.

## 1. The k(k−1) extra h-relations at m = 2k²−1: PROVED for all k ≥ 2 (Cat A)

**Proposition K1 (extra h-relations).** Fix k ≥ 2, m = 2k²−1, s = 2m², and let rank_g and rank_h be as defined in hcount.py (rank of the orbit-sum map F → Fun(⟨X,−1⟩-orbits on M♯/M), with F = Fun(M_t♯/M_t)^{⟨γ,−1⟩}). Then
rank_g = m(m+1), rank_h = m(m+1) − k(k−1), so extra = k(k−1).
The same proof gives dim F = 2m² = s.

### Proof
**Step 0 (order model).** M_t = Z e₁ ⊕ Z f, with e₁ = (1,0) and f = (0,1/m) = g e₁. Its Gram matrix is [[2,2m],[2m,2]], and g f = −e₁ + 2m f.
- So (M_t, B, g) ≅ (R_m, Tr(x ȳ), multiplication by ε_m), where R_n = Z[√(n²−1)] and ε_n = n + √(n²−1). The basis is e₁ ↦ 1, f ↦ ε_m, and Q is the norm form.
- Hence C := M_t♯/M_t ≅ R_m/2√d_m R_m, with d_n = n²−1, and |C| = 4(m²−1).
- γ = g² (char. poly. x² − 2mx + 1), so every group used is ⟨h,−1⟩ or ⟨g,−1⟩. Both are abelian.

**Step 1 (the h-overlattice is the same model one level down; Pell self-similarity).** Let u = (e₁+f)/2k. Then
- h e₁ = u, h u = f, h f = −u + 2k f, h⁻¹ f = u, and e₁ = 2k u − f;
- Gram(u, f) = [[2,2k],[2k,2]].

So N₁ := M_t + hM_t = M_t + h⁻¹M_t = Zu ⊕ Zf is even, and hN₁ = N₁. Moreover (N₁, h) ≅ (R_k, ε_k): h plays the role of "g at level k". I := N₁/M_t = ⟨u⟩ is isotropic of order 2k in C, and C₁ := N₁♯/N₁ = I^⊥/I ≅ R_k/2√d_k R_k.
(Symbolic in k: proof_ingredients.py → proof_ingredients.json.)

**Step 2 (reduction to a Hecke operator on C).** Write ι: Fun(C) → Fun(M♯/M) for pullback to the old set. P_X denotes averaging over ⟨X,−1⟩, and (hφ)(y) = φ(h⁻¹y).
- rank_X = dim P_X ι(F). Its Gram form is ⟨ιφ, P_X ιψ⟩.
- g preserves M_t, so P_g ι = ι P̄_g, and rank_g = dim V₀ with V₀ := Fun(C)^{⟨g,−1⟩}.
- Since h² = g, P_h = P_g(1+h)/2.
- ⟨ιφ, h ιψ⟩ = |M_t/M| ⟨φ, τψ⟩_C, where τ = (1/2k)·↑ ∘ h̄ ∘ ↓. Here ↓: Fun(C) → Fun(C₁) sums over I-cosets in I^⊥, and ↑ is its adjoint (pullback along I^⊥ → C₁, extended by 0). Why this holds:
  - y ∈ M_t♯ and h⁻¹y ∈ M_t♯ ⇔ y ∈ N₁♯;
  - M = M_t ∩ hM_t (h²M_t = M_t) is h-stable;
  - as y runs over a class c ⊂ N₁♯, h⁻¹y mod M_t runs uniformly over the coset h̄⁻¹(c̄) + I.

So rank_h = rank of (1+τ) on V₀ (τ commutes with g and −1, and is self-adjoint on V₀).

**Step 3 (spectrum of τ).** ↓↑ = 2k·Id, so on V₀:
- τ² = (1/2k)↑ḡ↓ = (1/2k)↑↓ =: E, an orthogonal projection, and τ³ = τ;
- V₀ = ker↓ ⊕ ↑(Fun(C₁)^{⟨ḡ,−1⟩}), and ↓: V₀ → Fun(C₁)^{⟨ḡ,−1⟩} is onto;
- τ = 0 on ker↓, and τ↑φ = ↑h̄φ.

So the (−1)-eigenspace of τ on V₀ has dim a − b, where a = #⟨h²,−1⟩-orbits and b = #⟨h,−1⟩-orbits on C₁. Hence extra = rank_g − rank_h = a − b.

**Step 4 (Burnside on R_n/2√d R_n).**
- ε_n² = 1 + 2d + 2n√d ≡ 1 mod 2√d, so ⟨ε,−1⟩ acts through {±1, ±ε}.
- Fix(−1) = |√d R/2√d R| = 4.
- Fix(∓ε) = |R/((ε±1)R + 2√dR)| (kernel and cokernel sizes agree on a finite group). Here (ε−1)R + 2√dR = Z((n−1)+√d) ⊕ Z·2(n−1), of index 2(n−1); likewise the ε+1 version has index 2(n+1).

Hence
- #⟨ε,−1⟩-orbits = (4d + 4 + 2(n−1) + 2(n+1))/4 = n(n+1);
- #⟨ε²,−1⟩-orbits = (4d + 4)/2 = 2n².

Level m (C, ε_m = g) gives rank_g = m(m+1) and dim F = 2m² = s. Level k (C₁, ε_k = h) gives a = 2k² and b = k(k+1). So extra = 2k² − k(k+1) = **k(k−1)**. ∎
(Burnside counts brute-forced for n = 2..40: proof_ingredients.json.)

### Corollaries (Cat A)
- τ on V₀ has eigenvalues +1 (mult. k(k+1)), −1 (mult. k(k−1)) and 0 (mult. m(m+1) − 2k²). So tr τ = 2k and rank τ = 2k². This matches the earlier sketch's "Fix = 2k², tr = 2k": the missing subquotient C_h is C₁ = N₁♯/N₁.
- The extra relations are ↑(h̄-odd ⟨ḡ,−1⟩-invariant functions on C₁): explicit, one for each pair of h̄-swapped ⟨ḡ,−1⟩-orbits in C₁.
- The 21:53 empirical identities "#closed = m(m+1) = rank_g" and "rank_g = m(m+1)" are now proved (Step 4 at level m).
- The equal-kernel statement (ker₊ = ker₋ in hcountD's Y-basis) is not re-derived here. It is not needed, because K1 goes through τ directly.

### Exact checks of the reformulation
- tau.py (exact sympy over Q, k = 2, 3, 4): rank(I+τ) = 54, 300, 980 = rank_h of hcount_*.json.
  - Minimal polynomial x³ − x.
  - Characteristic polynomials λ⁴⁸(λ−1)⁶(λ+1)², λ²⁸⁸(λ−1)¹²(λ+1)⁶, λ⁹⁶⁰(λ−1)²⁰(λ+1)¹².
  - Files: tau_2.json, tau_3_4.json.
- tau_fast.py (integer re-implementation, ranks mod two primes): reproduces k = 2, 3, 4. See tau_fast_5_6.log for k = 5, 6.

### Extension to k = 5 and k = 6 (Cat A as a mod-p check of a proved statement)
tau_fast.py, original M♯/M definition (tau_fast_5.json, tau_fast_6.json, tau_fast_5_6.log):

| k | m | \|M♯/M\| | V₀ = m(m+1) | rank(I+τ) | extra | rank τ |
|---|---|---|---|---|---|---|
| 5 | 49 | 960000 | 2450 | 2430 | 20 | 50 |
| 6 | 71 | 2903040 | 5112 | 5082 | 30 | 72 |

- extra = k(k−1) and rank τ = 2k² at both k. Ranks were computed mod 1000003 and mod 998244353, and the two agree. tr τ = 2k (float).
- These ranks are mod-p ranks, so on their own they are lower bounds. The values over Q follow from Proposition K1.

## 2. The factor 7s − 32: exact lattice derivation (Cat A)
Setting: Q₂(n,k) = n² + snk + (s/2)k², with Gram A = [[2,s],[s,s]] and det A = −s(s−2). In rev6 §(H_s), c₁ = (−1,1) and c₂ = (−4,1). File: delta_lattice.py → delta_lattice.json, all identities symbolic in s.

1. **7s − 32 = −2Q(c₂).** The second cone edge has Q(c₂) = −(7s−32)/2. Also c₂ = c₁ − 3e₁ with e₁ = (1,0), B(c₁,e₁) = s−2 and Q(e₁) = 1. Hence
   −2Q(c₂) = (s−2) + 6(s−2) − 18 = 7(s−2) − 18 = 7s − 32.
   So "7" = 1 + 2·3 and "32" = 14 + 18 = 7·2 + 2·3²·Q(e₁).
2. **u₂ spans c₂^⊥.** v := (3s, s−8) = J·A·c₂, with J the rotation by 90°. So B(c₂, x) = det(x, v), v ⊥ c₂, and u₂ = v/g with g = content(Ac₂) = gcd(s−8, 3s) = gcd(24, s−8). This is the definition of g.
3. **Q₂(u₂).** Jᵀ A J = det(A)·A⁻¹, so 2Q(v) = det(A)·2Q(c₂) = s(s−2)(7s−32). Hence Q₂(u₂) = sΔ/(2g²).
   Equivalently, v = 3ν₀ + (s−2)u₁ with ν₀ = (s,−2) ⊥ e₁.
4. **The "u₂-orthogonal part" in Theorem 3.** Take any w with det(w,u₂) = 1. The residual coefficient after completing the square in y is
   det A/(4Q(u₂)) = −g²/(2(7s−32)) = Q(π w),
   where π is the B-orthogonal projection onto R·c₂ along u₂, and π w = (g/(2Q(c₂)))·c₂ because B(w,c₂) = g·det(w,u₂) = g.
   So the 7s−32 in the Gauss phase is exactly the norm of c₂, the generator of u₂^⊥: the projected lattice π(Z²) has generator norm g²/(4Q(c₂)).
5. **Δ itself.**
   - Δ = 4Q(c₁)Q(c₂) = B(c₁,c₂)² + det Gram(c₁,c₂).
   - det Gram(c₁,c₂) = det(c₁,c₂)²·det A = −9s(s−2).
   - B(c₁,c₂) = −4(s−2).
   - Hence Δ = 16(s−2)² − 9s(s−2). The 16 is B(c₁,c₂)²/(s−2)², and the 9 is det(c₁,c₂)² = 3².

**Interpretation.** The only exact content is "7s−32 is the (negative, doubled) norm of the cone edge c₂ = c₁ − 3e₁". The degenerate prime cases follow:
- p | 7s−32 means c₂ is isotropic mod p, which collapses the residual Gauss sum to a delta.
- p | s−2 is the c₁ analogue.

I offer no physical interpretation; any would be Cat B. Not explained here: why the cone has edge c₂ = (−4,1). That is an input of the rev4 §H_s setup.

## 3. Weil-representation inputs replaced by exact computation (Cat A)
Method: weil_cyclic.py, copied unchanged from Open-Algebraic.
- Commutant of (S, T) on the even/odd part, computed mod ℓ ≡ 1 (mod M) with an exactly verified basis. Both square classes of u were run.
- Lift to C: dim End_C ≤ dim End_{F_ℓ} (the rank can only drop mod ℓ).
- For Z/p², δ_{pZ/p²} is an explicit (S,T)-invariant line. So the even commutant over C is ≥ 2, and = 2 forces even = 1 ⊕ R with R irreducible and R ≇ 1.

| M | even dim, commutant | odd dim, commutant | conclusion |
|---|---|---|---|
| 47 | 24, 1 | 23, 1 | even and odd irreducible (**needed for the s = 49 split**) |
| 59 | 30, 1 | 29, 1 | reconfirms the earlier result |
| 71 | 36, 1 | 35, 1 | reconfirms the earlier result |
| 289 = 17² | 145, 2 | 144, 1 | even = 1 ⊕ R₁₄₄, odd irreducible |
| 361 = 19² | 181, 2 | 180, 1 | even = 1 ⊕ R₁₈₀, odd irreducible |
| 529 = 23² | 265, 2 | 264, 1 | even = 1 ⊕ R₂₆₄, odd irreducible |

Files: weil_47_59_71.log / weil_cyclic_47_59_71.json; weil_289_361_529.log / weil_cyclic_289_361_529.json.
With this, (C3) is Cat A for every prime q | s−2 and every p² that appear at s = 9, 25, 49 (s−2 = 7, 23, 47), and also for Z/17², Z/19², Z/23². The general-p statements remain citations.

**Pinned references.**
- Scheithauer, *The Weil representation of SL₂(Z) and some applications*, IMRN 2009, no. 8, 1488–1545:
  - Prop. 4.5: the Γ₀(N) action ρ_D(M)e^γ = χ_D(M) e(−bdγ²/2) e^{dγ};
  - Thm. 4.7: the general formula.
  - Verified on the author's PDF. The proof uses that Γ(N) acts trivially, which is the factoring through (M)p₂(Z/N).
- Cliff–McNeilly–Szechtman, *Weil representations of symplectic groups over rings*, J. London Math. Soc. (2) 62 (2000), 423–436, doi:10.1112/S0024610700001381.
  - Verified via Szechtman, Rocky Mountain J. Math. 35 (2005), whose summary states: for a principal local ring R = O/𝔭^l, the module has exactly l+1 inequivalent irreducible constituents; X/Y has the two irreducible constituents Z± (the ±1 eigenspaces of −1).
  - For Z/p² (l = 2) this gives even = 1 ⊕ R and odd irreducible.
  - The theorem number inside CMS 2000 was **not verified**, so cite it as the "main theorem".
- Nobs–Wolfart (1976): the theorem number is **not verified** in this round, so keep the citation without a number.

## 4. Full runs at s = 121 and s = 3481: not done (documented)
- s = 121 needs the VF table, about 8.3·10⁸ int64 = 6.6 GB, plus about 2·10⁸ LP enumeration steps. The box has 15 GB total, about 3 GB available, and two other user jobs running (sym_engine_K15, sym_engine_e15_ckpt). Not feasible now.
- s = 3481 (s−2 = 7²·71, |label space| ~ s²) is far beyond that. What would be needed:
  1. a sparse or blocked VF (store only T-eigenblocks, about D²/ord(T) per block) or a streaming certificate;
  2. a ≥ 32 GB machine, or reuse of the sector factorisation (Theorem psq6) so that only the factors are computed. The factors are already Cat A from item 3 together with weil_cyclic_3481.json.
- Status: prediction only (factor dimensions, Cat A per factor). The assembled decomposition at s = 121 and s = 3481 is conditional on the tensor-factorisation theorem in rev6, not on a full run.

## Open after this round
- A general-p proof of (C3) without citation.
- s = 121 and s = 3481 full runs.
- The origin of c₂ = (−4,1) in the cone setup.
- Lower bounds: Proposition K1 is about the lattice-level rank_h, which is a proved upper bound on the old lift rank. Equality with the actual theta rank (no further relations) at m = 17, 31, … is not proved.

## 5. Why c₂ = (−4,1)? (added 2026-10-18 ~23:59 CDT; folder 2026-10-18-Algebraic-Round3/c2/)
**Answer.** c₂ is a definition, not a derived object. It was locked for s = 7 in oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Residual_Bridge_Series_C_Definition.md §1 ("Locked residual cones of negative norm (case s = 7)") and then frozen as s varies (rev4 §H_s). Within the natural class c ∈ c₁ + Z e₁ it is **forced at s = 7** by three conditions (Cat A). For s ≠ 7 it is **not** forced, and 7s − 32 is a property of this frozen choice.

**(a) Where the cone sits (Cat A).**
- H_s = Σ w(v) q^{Q₊(v)}, with Zwegers-type weight w = ½(sgn B(c₁,v) − sgn B(c₂,v)).
- B(c₁,v) = (s−2)n, so the c₁-wall is n = 0 (edge u₁ = (0,1)). B(c₂,v) = (s−8)n − 3sk, so the c₂-wall is the edge u₂ ∝ (3s, s−8) (§2 above).
- This is exactly the summation cone {n ≥ 0, 3sk ≥ (s−8)n} of asym_engine.py / gauss_data.py. The cone is the sign condition of an indefinite theta, not the region Q₊ > 0.

**(b) The involution M (proved, Cat A; c2_symbolic.py → c2_symbolic.json, symbolic in s).** M(n,k) = (−n − sk, k) is an integral involution with det −1, and Q₊(Mv) = Q₊(v) exactly, including the linear term. It sends c_a := (−a,1) to c_{s−a}.
- **Proposition (edge-class invariance).** For admissible a, H^{(c₁,c_a)} = H^{(c₁,c_{s−a})}.
- Proof:
  - The difference is ½Σ f(v) q^{Q₊(v)}, with f = sgn B(c_{s−a},·) − sgn B(c_a,·).
  - f is supported in the sector between two positive lines, so each degree has finitely many terms.
  - f∘M = −f and M is a Q₊-preserving bijection, so the sum equals its own negative and vanishes. ∎
- Exact q-series check (h_pair.json): s = 7, 8, 9, 11, 13, through q⁸⁰⁰ or q⁶⁰⁰.
- So only the M-class {c₄, c_{s−4}} matters. At s = 7, c₂ = (−4,1) is equivalent to (−3,1).
- −2Q(c_a) = (2a−1)s − 2a² is M-invariant: a = 4 gives 7s − 32. Also det(c₁,c_a) = a − 1 = 3, so the "3" in c₂ = c₁ − 3e₁ is just a − 1 with a = 4. It is not tied to x = 1/3 or the ternary structure; I found no evidence for that link.

**(c) Forcedness at s = 7 (Cat A, within c₂ ∈ c₁ + Z e₁).**
1. Q(c_a) < 0 ⇔ a ∈ {1, …, 6}. a = 1 is c₁ itself.
2. The closed orthant {n,k ≥ 0} lies strictly inside the w = 1 region, which the definition doc requires ("Interior orthant: w = 1"). This holds ⇔ s − 2a < 0 and s(1−a) < 0 ⇔ a ≥ 4.
3. Maximal |Q(c₂)|, equivalently the longest vanishing of Cmixed:

| a | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| −Q(c_a) | 13/2 | 17/2 | 17/2 | 13/2 | 5/2 |
| first nonzero Cmixed coefficient | q³⁰ | q²⁹⁴ | q²⁹⁴ | q³⁰ | q⁰ |

(cmixed_vs_a_s7.json, exact to q¹²⁰⁰.) The q²⁹⁴ matches rev6's "vanishes through q²⁹³".

Conditions 2 and 3 together give a = 4 uniquely, and condition 3 alone gives the M-class {3,4}. "Forced" depends on accepting conditions 2 and 3 as the selection rule. That rule is my reading, Cat B as motivation; the computations are Cat A. Vectors with second coordinate ≥ 2 were not examined.

**For s ≠ 7 the frozen c₂ is not forced.**
- The deepest class is a ≈ s/2, with −2Q ≈ s(s−2)/2 rather than 7s − 32.
- For s > 8, B(c₂,(1,0)) = s − 8 > 0, so the orthant edge (1,0) leaves the cone.
- Other admissible choices change H_s by a positive-sector sum ½Σ f q^{Q₊}: a holomorphic cone sum with finitely many terms per degree. In Zwegers' language this is ϑ^{c_a,c_{a′}}, whose completion uses c_{a′} instead of c_a.
- Δ(a) = (s−2)((2a−1)s − 2a²). So **7s − 32 is choice-dependent** (invariant only under a ↔ s−a). The factor s − 2 = −2Q(c₁) is the choice-independent part, given c₁.
- First degree at which H^{(a)} differs from H^{(4)}: e.g. s = 11: a = 3 at q⁸⁰, a = 5 at q²⁴² (h_pair.json).

**Category.** Everything above is Cat A except the selection-rule interpretation, which is Cat B. I offer no physical reading.

**Open.**
- Why the original authors chose c₁ = (−1,1). It is the wall n = 0 of the path orthant, which is natural but still a definition.
- Whether a canonical s-dependent choice (e.g. the deepest class) would give cleaner closed forms.
- Whether c with second coordinate ≥ 2 changes the s = 7 uniqueness.

Files: c2/c2_symbolic.py/.json, c2/h_pair.py/.json, c2/cmixed_vs_a.py → cmixed_vs_a_s7.json, c2/c2_choice.py/.json (C-coefficient value sets per choice).

## 6. Follow-up on §5's open items (2026-10-19 ~00:10 CDT; folder 2026-10-18-Algebraic-Round3/c6/)

### 6.1 c₁ = (−1,1) is forced by the wall n = 0 (Cat A)
- A wall n = 0 means B(c₁, v) ∝ n, i.e. A c₁ ∝ (1,0), so c₁ ∝ A⁻¹(1,0) ∝ (−1,1).
- The primitive integral vector on this ray is ±(−1,1). The sign is fixed by the orientation in w (B(c₁, v) = (s−2)n > 0 on the cone).
- Q(c₁) = −(s−2)/2 < 0 for all s > 2, so Zwegers' negativity holds automatically.
- The only other vector giving the same series is the M-image c_{s−1} = (1−s, 1); the §5 proposition applies because w∘M swaps the classes.
- Hence, given that one wall is the orthant edge n = 0, **(s−2) = −2Q(c₁) is intrinsic** to Δ.
- Alternatives at s = 7, with c₂ = (−4,1) (rays_s7.json):

| c₁ | first nonzero Cmixed coefficient |
|---|---|
| (−1,1) and (−6,1) = M-image | q²⁹⁴ |
| (−2,1), (−3,1), (−7,2), (−2,3) | q⁰ |

So any other c₁ destroys the q⁰ normalisation of C.

### 6.2 c₂ with b ≥ 2: (−4,1) is NOT unique; the canonical choice is the k = 0 wall (Cat A)
- **Proposition (axes cone).** Take c₂ = primitive(−s, 2), i.e. ∝ ν₀ = (s, −2), so that B(c₂, v) ∝ −k. This c₂ is M-fixed, and Q(−s, 2) = −s(s−2) < 0. Then w = ½(sgn n + sgn k), and **Cmixed ≡ 0 identically**, i.e. C = Caxis + Cthird.
- Proof:
  - P − H = 1 + ½Σ_{n≥1} q^{n²} + ½Σ_{k≥1} q^{sk(k+1)/2} + Σ_{n,k≤−1} q^{Q₊} + (negative half-axes).
  - Since Q₊(−n,−k) = Q₋(n,k), the negative quadrant gives Cthird.
  - The negative half-axes give ½(1 + Σ_{k≥1} q^{sk(k+1)/2}) + ½Σ_{n≥1} q^{n²}.
  - Altogether P − H = Caxis + Cthird. ∎
  - Exact check, s = 5..13 through q⁶⁰⁰: axes_cmixed.json.
- **Corollary.** For any admissible c₂, Cmixed^{(c₂)} = H^{axes} − H^{(c₂)}. This is a sum over the sector between the c₂-wall and the k = 0 wall, with finitely many terms per degree.
  - For the frozen (−4,1) at s = 7, the first term is the wall point (21,−1) with Q₊ = 21·14 = 294 and weight −½.
  - This is exactly rev6's "Cmixed vanishes through q²⁹³ but not identically".
  - First nonzero degree of the frozen Cmixed: 27, 294, ≡0 (s = 8, where (−4,1) is the axes vector), >600, 375, 242, 189, 168 for s = 6, 7, 8, 9, 10, 11, 12, 13.
- **Uniqueness question at s = 7** (all primitive (−a,b) with b ≤ 6 and negative norm; rays_s7.json):
  - Cmixed vanishing order increases as the ratio a/b approaches 7/2 = s/2 (the axes ray). For example, 10/3, 11/3, 13/4, 15/4, 16/5, 17/5, 18/5 and 19/5 all vanish through q⁷⁰⁰, while (−4,1) vanishes only through q²⁹³.
  - The normalised depth −Q/b² has its supremum at 7/2. Under "orthant strictly inside" (a/b > 7/2) the supremum is not attained, and there are infinitely many better rays.
  - So **(−4,1) is unique only within b = 1** (§5). Among all primitive c it is not unique, even up to M.
  - The optimum under the Cmixed criterion is the axes vector (−7,2), which puts the orthant edge (1,0) on the wall rather than strictly inside.

### 6.3 s-dependent choices: x = 0 radial coefficients through t^{9/2} (Cat B: 70-digit numerics with PSLQ)
- Method: c6/asym_general.py is the proved quadrant Euler–Maclaurin engine of Analytic-CatB-Push with a free second edge. Drivers: run6.py and repslq.py; outputs repslq.json and run6_s*_a*_b*.json.
- Accuracy: the even-order coefficients, which are exactly 0, come out at ≤ 1e−56.
- In every case, c_{t^{−1/2}}/√(2πs) = −1/(2(s−2)) + 1/(2√Δ_norm), where Δ_norm = (s−2)·(−2Q(c₂))/b².
- **Axes choice** (c₂ ∝ (−s,2): b = 2 for odd s, a = s/2 for even s):
  - Δ_norm = s(s−2)²/2, so √Δ_norm = (s−2)√(s/2). The irrationality collapses into the √(2πs) prefactor's field.
  - Leading term: **c_{t^{−1/2}} = −√π/(√(2s)+2)** (s = 7..13, PSLQ).
  - All orders through t^{9/2} were recognised in Q(√(2s)) with small denominators. For example, at s = 7 the denominators are 70, 400, 160000, 134400000, 3072000000, 122880000000, which are products of powers of 2, 5 = s−2 and small primes.
  - The same holds at s = 9, 10, 11, 12, 13.
  - At s = 8 the frozen choice is the axes choice, and Δ = 144 = 12² is a perfect square.
- **Frozen a = 4:** the field is Q(√((s−2)(7s−32))). PSLQ recognises orders t^{−1/2}, t^{1/2}, t^{3/2} (denominators such as 786080000 at s = 7). At t^{5/2} and beyond the relations reach heights of about 10¹¹ at tolerance 10⁻²², so they are **not reliably recognised** at 70 digits. This is consistent with the (s−2)^r(7s−32)^r denominators of rev6.
- **Deepest b = 1 pair for odd s** (a = (s±1)/2): Δ = (s−2)(s²−2s−1)/2. This is a perfect square at s = 11 (Δ = 441). There, PSLQ found purely rational values through t^{3/2}; higher orders were not recognised.
- **Verdict (Cat B).** The axes choice is markedly cleaner: field Q(√(2s)) instead of Q(√Δ), and denominators built from s−2 and small primes instead of (7s−32)^r. It is also the choice for which Cmixed ≡ 0 exactly (Cat A).
- Not done: exact closed forms in s for the axes choice. Route: H^{axes} = P − Caxis − Cthird, so the expansion follows from the proved quadrant lemma applied to P and Cthird. This is feasible symbolically but was not run.

### Open
- Symbolic closed forms in s for the axes choice.
- Whether rev4 §H_s intended c₂ to approximate the axes wall; the source doc gives no reason for (−4,1).
- t^{5/2}+ for the frozen a = 4 needs the existing symbolic engine (rev6 already has those forms).

## 7. Exact closed forms for the parallel object H_s^axes (x = 0), through t^{13/2} (2026-10-19 ~00:25 CDT; folder c7/)
CORE_FREEZE: the locked H_s (c₂ = (−4,1)) is untouched and not redefined. H_s^axes uses c₁ = (−1,1) and c₂ = primitive(−s,2), the k = 0 wall. It is a separate object.

**Method (Cat A).** H^axes = P − Caxis − Cthird exactly (§6.2).
- P is the quadrant sum Σ_{n,k≥0} F(εn, εk) with F = e^{−q(X,Y) − ε(s/2)Y}.
- Cthird is the same with shift α = β = 1 and the linear-term sign reversed.
- Both are expanded with Zagier's 2-D quadrant Euler–Maclaurin lemma, the same proved lemma used by asym_engine.
- Caxis has the exact unary expansion ½√π ε⁻¹ + ½√(2π/s) ε⁻¹ e^{ε²s/8}, because the B_odd(½) = 0 tail vanishes.
- Area integrals ∫∫Y^i e^{−q}:
  - for even i they cancel between P and Cthird ((−λ)^i − λ^i = 0);
  - for odd i, ∫₀^∞ μ^i q(1,μ)^{−(i+2)/2} dμ = R(∞)/(s/2)^{i/2} − R(0), with R the polynomial antiderivative numerator, solved exactly.
- Everything is symbolic in w = √(s/2). There is no g-dependence.
- Script: c7/axes_closed.py (about 10 s for K = 13). Outputs: axes_closed_K13.{json,pkl,log}; R/S form in axes_RS_forms.json (rs_forms.py).

**Result (Cat A, all s ≥ 3).** Write c_r for the coefficient of t^r at q = e^{−t}, x = 0.
- All integer orders vanish identically, an internal consistency check.
- For half-integer orders, c_r = √π·[R^ax_r(s) + S^ax_r(s)·√(2s)], with R^ax, S^ax ∈ Q(s) and denominators (s−2)^{r+3/2} times small integers:

| r | R^ax_r | S^ax_r |
|---|---|---|
| −1/2 | 1/(s−2) | −1/(2(s−2)) |
| 1/2 | s²(s−4)/(24(s−2)²) | −(s−4)(3s−2)/(48(s−2)²) |
| 3/2 | −s³(s−4)(s²−4s+8)/(960(s−2)³) | −(15s⁴−76s³+108s²+96s−128)/(3840(s−2)³) |
| 5/2 | s⁴(s−4)(5s⁴−40s³+126s²−184s+128)/(80640(s−2)⁴) | −(s−4)(105s⁵−730s⁴+2732s³−5208s²+5696s−2560)/(645120(s−2)⁴) |
| 7/2 | −s⁵(s−4)(3s²−12s+16)(7s⁴−56s³+160s²−192s+96)/(3870720(s−2)⁵) | −(315s⁸+2184s⁷−65304s⁶+…−688128)/(61931520(s−2)⁵) |
| 9/2 | s⁶(s−4)(105s⁸−…+24576)/(170311680(s−2)⁶) | −(s−4)(693s⁹−…−13762560)/(5449973760(s−2)⁶) |

The t^{11/2} and t^{13/2} rows are in axes_RS_forms.json.
- Leading term: **c_{−1/2} = √π(2 − √(2s))/(2(s−2)) = −√π/(√(2s)+2)**. This confirms the §6.3 PSLQ pattern, now as Cat A.
- Field Q(√(2s))·√π, with denominators (s−2)^k × small integers. This confirms the §6.3 Cat B observations.
- R^ax_r carries the factor (s−4) for every r ≥ 1/2, and the factor s^{r+3/2}.

**Structural by-product (Cat A).** S^ax_r·√(2s)·√π = √(2πs)·S^ax_r, and S^ax_r **coincides exactly with rev6's R_r** (Theorem H_s(ii), frozen cone) for r = −1/2, 1/2, 3/2, 5/2.
- So the "R-part" (the √(2πs)·rational part) of H_s is independent of the choice of c₂ through t^{5/2}, and presumably at all orders.
- For the frozen cone, the c₂ = (−4,1) wall contributes the √Δ part S_r·√Δ, including all of its g- and (7s−32)-dependence.
- For the axes cone, the corresponding piece is the rational √π part R^ax_r. Caxis and the X-edge integrals of e^{−X²} produce it, and no √Δ or g appears.
- Interpretation: the c₁ wall (n = 0 edge) produces the R-part, and the c₂ wall produces the remaining part. This is a reading of the computation; the coincidence itself is exact through t^{5/2}.

**Verification.**
- Against the 65-digit engine numerics (c6/run6_*.json, axes cases) at s = 7, 8, 9, 10, 11, 12, 13, and at held-out s = 15 and 16 (new runs): |difference| ≤ 3·10⁻⁴⁷ at every order through t^{9/2}, which is the engine's precision (c7/verify.json, "engine"). Cat A in the sense that the closed form is proved; the numerics are a Cat B cross-check.
- Held-out direct summation at s = 20: (H − Σ_{e≤9} c_e ε^e)/ε¹¹ = −1.473e7, −1.623e7, −1.712e7 at t = 0.004, 0.002, 0.001. The predicted c₁₁ + c₁₃t is −1.383e7, −1.598e7, −1.705e7, which converges as expected (c7/verify_direct.json; Cat B).
- The "direct" block in verify.json (t ≥ 0.01, s = 20, 31) is **not** a valid test: t·s is too large for the asymptotic series. It is superseded by verify_direct.json.

**Not done.** x = 1/2 and x = 1/3 for H^axes. The same method applies with residue classes mod 2N (shifts α, β = r/2N, scaling ε → 2Nε) and Gauss-phase weights on the quadrant pieces and the unary sums. It is cheap but was not run this round.
