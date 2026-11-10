# Local-derived. Writes FINDINGS_LOCAL_t4436_ALL_MENU_BRANCHES_2026-11-09_<HHMM>.md (+ .sha256). Refuses to overwrite anything.
import os, hashlib, datetime, glob, collections
R='/workspace/quantum-comp/reports'; EV=R+'/evidence_local_t4436_branches_2026-11-09'
now=datetime.datetime.now(); HHMM=now.strftime('%H%M')
OUT=f'{R}/FINDINGS_LOCAL_t4436_ALL_MENU_BRANCHES_2026-11-09_{HHMM}.md'
assert not os.path.exists(OUT) and not os.path.exists(OUT+'.sha256'), 'refusing to overwrite'
sha=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
TIP='/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md'; tip0=sha(TIP)
assert tip0=='7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91'
# rows: (item, branch, grade, tags, text)
P,C,O,X,N='PROVED','COND','OPEN','REF','PENDING'
rows=[
# ---- O-c
('O-c','Oc-1',P,'','W₄ (menu definition, T(p²) = a_p(f) for p ∈ {3,11,13,23,29,37}) equals K = ker T(9) in S_{3/2}(Γ₀(196),χ₂₈); dim 4; rank[W₄|K] = 4 (s1b §2). New.'),
('O-c','Oc-1',P,'','c(35) = 0 on K; 35 is the only squarefree n with coredisc 140 (carried, 9e34f2dc 3c / bfa5da3b; re-checked s1b §2).'),
('O-c','Oc-1',P,'','L(Ξ,1) = 0: FE sign −1 of L(Ξ,s) is proved on base F0 (PP 5bf1e1dc §2–3).'),
('O-c','Oc-1',C,'T-Wald','c(35)² ∝ L(Ξ,1) (Waldspurger 1981). Both sides are now separately PROVED zero; only the link is cited.'),
('O-c','Oc-1',C,'C2, C3','K is f-isotypic (= N1/O-a). This replaces the OPEN tag of bfa5da3b L30.'),
('O-c','Oc-1',P,'','TT-1: dim(span{θ_{L₁}(aτ)θ(bτ)} ∩ K) = 2 with explicit G₁, G₂ (PP 0f1d3361 §5; carried, not recomputed).'),
('O-c','Oc-2',P,'','Twist invariance of T(p²) eigenvalues under quadratic coefficient twists, with the a_p(f) ≠ 0 condition (witness p = 11) (carried, bfa5da3b + erratum F4).'),
('O-c','Oc-2',P,'','No Oc-2 vector (T(121) eigenvalue a₁₁(Ξ) = −4) in S_{3/2}(Γ₀(N),χ_D) for N = 196, every admissible D (1: dim 6; 28: dim 9; −4, −7: dim 0; T(p²), p ∈ {11,37,53,71}, s1b §5) and N = 392, every admissible D (1, 8: dim 18; 28, 56: dim 17; −4, −8, −7, −56: dim 0; s1e), and N = 784 for D ∈ {1 (dim 36), −4 (dim 0)} (s1e). Exact PARI Hecke matrices. New.'),
('O-c','Oc-2',N,'','Same test at N = 784 for D ∈ {8, −8, −7, 28, −56, 56}: s1e still running at filing (T(121) on the D = 8 space).'),
('O-c','Oc-2',P,'','No unary-theta-type eigensystem (T(p²) eigenvalue ±(1+p)) can belong to Oc-2: |a_p(Ξ)| ≤ 2√p < p+1 (V4 Hasse, PP-verified). New.'),
('O-c','Oc-2',C,'T-Wald','Oc-2 is nonzero for a suitable ψ at level 78400 (Waldspurger/Shimura existence).'),
('O-c','Oc-2',O,'','Explicit basis = O-b (B5 PENDING in the t4407/t4429 stream; not touched here).'),
('O-c','Oc-3',C,'REC','Consistent with every Owner record; no PROVED Local result depends on an identification (record-survey statement, erratum F6).'),
('O-c','Oc-3',P,'','Literal R8 reading (552541cf L20–24: Θ_{3/2}(·;a) = Σ_{n∈ℤ}(n+a)q^{(n+a)²}, untwisted, a = 7m or 7m+7/2): each series is identically 0 (k ↦ −k on ℤ or on ½+ℤ), so Ξ_RTA ≡ 0. New.'),
('O-c','Oc-3',P,'','Ξ_odd has exponents in ¼+ℤ (also after q ↦ q^t, t squarefree); a nonzero Ξ_odd is not 1-periodic, so it lies in no M_{3/2}(Γ₀(N),ψ). New.'),
('O-c','Oc-3',P,'','Square-class test (s1c, n ≤ 1200): for every squarefree t ≤ 400 (243 values), no nonzero F ∈ K has c(n) = 0 for all n ∉ t·□; in S = S_{3/2}(Γ₀(196),χ₂₈) (dim 9) only t = 1 gives a nonzero subspace, of dimension 1. New.'),
('O-c','Oc-3',X,'','Hypothesis "R8\'s Ξ is a nonzero element of W₄ = K" (the Oc-1 identification): REFUTED for every reading of R8 whose q-expansion lies in one square class t·□ (t squarefree ≤ 400) plus non-integral exponents, i.e. for any coefficients outer_coeff(m), any twist ψ, any such rescaling. Proof: rows above. New; PP audit requested.'),
('O-c','Oc-3',P,'','χ₋₇-twisted reading: Σ_{n∈ℤ}χ₋₇(n+7m)(n+7m)q^{(n+7m)²} = 2u for every m, u := Σ_{k≥1}χ₋₇(k)k q^{k²}; so Ξ_even = 2(Σ_m c_m)·u for summable (c_m). u\'s coefficients (n ≤ 600 > 42) are consistent with S (coordinates [1,0,0,2,0,0,0,0,−3]), u spans the unique square-supported line of S, and u ∉ K (rank 4 → 5) (s1b §4, s1c). New.'),
('O-c','Oc-3',C,'T-theta1','u ∈ S_{3/2}(Γ₀(196),χ₂₈) (unary weight-3/2 theta), hence T(p²)u = χ₋₇(p)(1+p)u (computed: −4, −6, 12, −14 at p = 3, 5, 11, 13). An Eisenstein-type system, never 49a1\'s or Ξ\'s. PP 0f1d3361\'s Θ2 + θ³-cocycle certificate method should discharge T-theta1.'),
('O-c','Oc-3',P,'','The other 8 unary twists (ψ = 1, χ₋₄, χ₋₃, χ₋₈, χ₋₂₀, χ₋₃₅, χ₂₈, χ₁₄₀) are not in S and not in K: rank rises (s1b §4). New.'),
('O-c','Oc-3',O,'','Ξ_RTA itself: outer_even_coeff(m), outer_odd_coeff(m) are undefined in the source (552541cf L20–24), so the object is not determined.'),
# ---- V84
('V₈₄','V-1',P,'','Ind_{Γ₀(49)}^{Γ₀(49)⁺}ρ is a representation; it needs no ρ(W₇) on V₄₂ (carried, bfa5da3b).'),
('V₈₄','V-1',C,'tip §1u','ρ(W²) = ρ(−I) = Id on V₄₂ (float illustration: V₄₂ ⊂ Fix(S²), v42.txt).'),
('V₈₄','V-1',P,'','Φ = (F, F|W) is a form for Ind ρ; +1 vectors are the symmetrizations; the +1 law imposes no constraint (carried).'),
('V₈₄','V-1',P,'','Lemma: ρ^W(T) is conjugate to ρ(T)⁴⁹ (W₇TW₇⁻¹ = ST⁴⁹S⁻¹, erratum F1), whose eigenvalue orders divide 9800/49 = 200, prime to 7. So Hom_{Γ₀(49)}(V_X, ρ^W) = 0 for every irreducible subrepresentation V_X having a T-eigenvalue of order divisible by 7 (Schur). New (generalises PP 320c8c7e §1(a)).'),
('V₈₄','V-1',C,'F-V42, tip §1u','Ind ρ = Ind V_Eis ⊕ Ind V_cusp with both summands irreducible (dims 72, 12) and End(Ind ρ) ≅ ℂ² (Mackey + lemma). F-V42 = the float decomposition V₄₂ = V_Eis(36) ⊕ V_cusp(6), each with commutant 1 and T-eigenvalues e(1/14), e(19/140) (v42.txt). New.'),
('V₈₄','V-2',P,'','w₁₉₆₀₀(f_Ξ) = +1 (PP 5bf1e1dc row 2d, now PROVED).'),
('V₈₄','V-2',P,'','θ₁(−1/(7τ)) = −i√7·τ·θ₁(τ) and g₊|₂W₄₉ = +g₊ (g₊ = θ₁² − 7θ₁(7τ)²) as identities on ℍ. Proof: Poisson (F0-5) gives θ_L(−1/τ) = (τ/i)(1/√7)θ_{L#}(τ) with θ_{L#}(τ) = θ₁(τ/7); then g₊(−1/(49τ)) = 49τ²g₊(τ). Numerical illustration s3: residuals ≤ 4e−39. New.'),
('V₈₄','V-2',P,'','g₊ ∈ M₂(Γ₀(49)), g₊ ≠ 0 (q-expansion −6 + 4q + 12q² + …): θ₁ = θ_{L₁} ∈ M₁(Γ₀(7),χ₋₇) (PP 0f1d3361 §4), θ₁(7τ) ∈ M₁(Γ₀(49),χ₋₇), χ₋₇² = 1. Formerly cited (XW LD-Ξ1(b)). New.'),
('V₈₄','V-3',X,'','Not a representation of Γ₀(49)⁺: no invertible intertwiner ρ ≅ ρ^W (PP exact proof 320c8c7e §1(a)).'),
# ---- J
('J','J-1',P,'','Γ₀(49) ∩ Γ₀(140) = Γ₀(980) (carried).'),
('J','J-1',P,'','f_Ξ ∉ S₂(Γ₀(980)) and ∉ M₂(Γ₀(980)) (PP pp_2g_980, citation-free).'),
('J','J-1',P,'','W₄₉ does not normalize Γ₀(980); W₉₈₀ and W₄₉^{(980)} do (narrowed, erratum F5).'),
('J','J-1',P,'','With nebentypus χ₁₄₀: neither f_Ξ nor f_{49a1} lies in S₂(Γ₀(980),χ₁₄₀) (dim 152) or M₂(Γ₀(980),χ₁₄₀) (dim 184); mod-p rank rises by 1 (s7). New.'),
('J','J-1',P,'','f(dτ), d | 20 (6 copies) lie in S₂(Γ₀(980)) (PP Theorem M + level raising, elementary).'),
('J','J-1',X,'','Hypothesis "J-1 carries Ξ", with trivial or χ₁₄₀ nebentypus: REFUTED (rows above). J-1 survives only as a level carrying 49a1. New; PP audit requested.'),
('J','J-2',P,'','980 | 19600 (carried).'),
('J','J-2',P,'','f_Ξ ∈ S₂(Γ₀(19600)) (PP 5bf1e1dc V7).'),
('J','J-2',P,'','f_Ξ ∉ S₂ and ∉ M₂ of Γ₀(2800) and Γ₀(3920); mod-p rank of the integer-scaled coefficient matrix rises (445→446, 516→517, 625→626, 720→721); 49a1 control behaves correctly (in at 3920, out at 2800) (s2c). New.'),
('J','J-2',N,'','Same test at Γ₀(9800), the last maximal proper divisor. s2c was OOM-killed by the kernel; s2d was killed by Local at 22:10 CST to protect the other stream\'s running ob_v3 job. Needs about 5+ GB free.'),
('J','J-2',C,'T-AL-new','f_Ξ is a newform of level 19600 (= E9).'),
('J','J-2',P,'','f(dτ), d | 400 (15 copies) lie in S₂(Γ₀(19600)).'),
('J','J-2',O,'','"Equivariant embedding of the Weil carrier V₄₂" is undefined.'),
('J','J-3',P,'','E₄₉ ≅ Ξ over K = ℚ(√35) (c₄, c₆ ratios 140², 140³; carried).'),
('J','J-3',P,'','J := Res_{K/ℚ}E_K ~ E × Ξ, elementary: J(R) = E(R⊗K), Ξ(R) ≅ {P ∈ E(R⊗K): σP = −P}; (P,Q) ↦ P+Q and P ↦ (P+σP, P−σP) compose to [2] both ways. Replaces the Milne citation. New.'),
('J','J-3',P,'','L(J,s) = L(E,s)L(Ξ,s), both factors modular (PP Theorem M, V7; base F0).'),
('J','J-3',C,'T-cond','cond(J) = 960400 = 49·19600 (Milne 1972 / isogeny invariance of the conductor; still cited).'),
('J','J-3',C,'T-AL-new','Minimal modular level 19600 (J a quotient of J₀(N) up to isogeny); also depends on the J-2 9800 row.'),
('J','J-3',P,'','Analytic rank of J = 0 + 1 = 1 (PP 5bf1e1dc E11b, arb certificate, no GZK).'),
('J','J-3',P,'','Algebraic rank J(ℚ) = rank E(K) = rank E(ℚ) + rank Ξ(ℚ) = 0 + 1 = 1: ellrank bounds [0,0] for 49a1 and [1,1] for Ξ; P = (8730, 810550) on PARI\'s model of elltwist(E,140), ellorder 0, ĥ(P) ≈ 6.7821; torsion ℤ/2 for each (s7). New.'),
('J','J-3',P,'','Hence algebraic rank = analytic rank = 1 for J, without GZK (two separately proved facts). New.'),
('J','J-3',P,'','ε(J) = ε(E)ε(Ξ) = −1 (signs proved, PP 5bf1e1dc).'),
('J','J-3',O,'','V₄₂-equivariant map into anything attached to J: undefined.'),
# ---- H+U
('H₊U','H-1',P,'','Option M on H₊⊗ℂ²: P̂² = −1 and P̂(H_D⊗1)P̂⁻¹ = −H_D⊗1 in the Majorana representation; exact sympy (s5). (Carried; re-proved exactly.)'),
('H₊U','H-1',P,'','A unitary ι with ιH = (H⊗1₂)ι exists when H is O5-1 or O5-2 (carried, ac1dd4e2); fails under O5-3 (row O5-3).'),
('H₊U','H-2',P,'','(γ⁰⊗1₃₅)K squares to −1; Option M and ι carry over (carried, c4b).'),
('H₊U','H-2',P,'','Every real structure C = UK on ℂ³⁵ (C² = +1) is unitarily conjugate to K (U symmetric unitary = QQᵀ, C = QKQ⁻¹); C² = −1 is impossible in odd dimension. So "which real structure" is immaterial up to unitary equivalence. New (s5 illustration).'),
('H₊U','H-2',O,'','Any link to the "35-component law vector" (never built in the records).'),
('H₊U','H-3',X,'','For every finite d there is no unitary ι: ℂ^d → ℂ^d⊗ℂ² (dimensions d ≠ 2d). New, generalises 4b25d2ed.'),
('H₊U','H-3',X,'','Odd d: the Option-M form P̂ = (A⊗σ_x)K cannot square to −1 (scoped, erratum F7).'),
('H₊U','H-3',P,'','Even d: antiunitaries with square −1 exist (e.g. 1_{d/2}⊗iσ_yK), so only ι kills H-3 for even d. New.'),
# ---- LD-O3a
('LD-O3a','a-1',P,'','π = 1 is automorphic and unramified everywhere (carried, d2d2d226 3–4).'),
('LD-O3a','a-1',P,'','π carries no datum at {2,5,7} (carried).'),
('LD-O3a','a-2',P,'','π₂₃ = 1: (140/23) = +1 (s6).'),
('LD-O3a','a-2',P,'','π = χ₁₄₀∘θ is automorphic, ≠ 1, ramified exactly at {2,5,7}; π_∞ trivial since χ₁₄₀(−1) = +1 (carried).'),
('LD-O3a','a-2',C,'T-spin','Λ(s,π,std) = Λ(s,χ₁₄₀)²∏_{i=1}^{23}Λ(s−i,χ₁₄₀)Λ(s+i,χ₁₄₀) (spinor-norm twist = central twist of the parameter, d2d2d226 item 6).'),
('LD-O3a','a-2',C,'T-CNF','L(1,χ₁₄₀) = 2h·log ε/√140 = 4·log(6+√35)/√140 (h = 2, ε = 6+√35 of norm +1, PARI quadclassunit); lfun agrees to 3e−62 (s6). New.'),
('LD-O3a','a-3',P,'','(−7/23) = +1, so π₂₃ = 1; π is ramified only at 7; π_∞ = sign∘θ is nontrivial (carried; s6).'),
('LD-O3a','a-3',P,'','The full candidate set {1} ∪ {χ_D∘θ: (D/23) = +1} is infinite (carried).'),
('LD-O3a','a-3',C,'T-CNF','L(1,χ₋₇) = π/√7; lfun agrees to 60 digits (s6). New.'),
# ---- LD-O3b
('LD-O3b','b-1',P,'','Under a-1: Λ = ξ(s)²∏ξ(s−i)ξ(s+i), Λ(1−s) = Λ(s), poles at −23…24 of total order 96 (carried).'),
('LD-O3b','b-1',C,'T-spin, T-Dir','Under a-2 or a-3: Λ is entire with Λ(1−s,π) = Λ(s,π) (root numbers +1: Gauss sums g(χ₁₄₀) = √140, g(χ₋₇) = i√7, numerically to 76 digits, s6). So b-1 sees the a-choice (poles vs entire). New.'),
('LD-O3b','b-2',P,'','Exponents of D₂₄: {1,3,…,45} ∪ {23}; Σ(2e+1) = 1128 = dim so(48) (s6).'),
('LD-O3b','b-2',C,'T-Kostant','Ad|_{principal SL₂} = ⊕Sym^{2e}; hence Λ(s,1,Ad) = ∏_e∏_{j=−e}^{e}ξ(s+j), FE, order-48 poles at 0 and 1. Under the strict rule, Kostant is a citation (bfa5da3b graded this PROVED; regraded here).'),
('LD-O3b','b-2',C,'T-spin','Under a-2 or a-3, Λ(s,π,Ad) = Λ(s,1,Ad): the twisting parameter is central in SO₄₈(ℂ) and dies in Ad. So b-2 cannot see the a-choice. New.'),
('LD-O3b','b-3',P,'','For π = 1, Λ = ξ(s) with simple poles at 0 and 1 (carried).'),
('LD-O3b','b-3',P,'','b-3 is the same for every split SO_{2n} and forgets y_i = 23^{24−i} (carried).'),
# ---- LD-O3c
('LD-O3c','c-1',P,'','#{maximal totally singular subspaces of the split 2n-dim form over F_q} = ∏_{i=0}^{n−1}(q^i+1). Proof: count pairs (v,U) with v ∈ U isotropic; there are (q^n−1)(q^{n−1}+1) nonzero isotropic vectors; U ∋ v ↔ maximal isotropic in v^⊥/v (split, dim 2n−2); so N(n) = (q^{n−1}+1)N(n−1). Brute force agrees at (n,q) = (1,23), (2,3), (2,5), (2,7), (2,23), (3,3), (3,5), (4,3) (s6).'),
('LD-O3c','c-1',P,'','At (24, 23) this equals the Codex contour 2∏_{i=1}^{23}(23^i+1) exactly (377 digits), given the Bridge C split SO₄₈ form (s6).'),
('LD-O3c','c-2',P,'','One SO-orbit has ∏_{i=1}^{n−1}(q^i+1) members: the two families (parity of codim U∩U₀) have equal size in every brute-force case (s6). The Codex contour is exactly 2× this.'),
('LD-O3c','c-3',X,'','vol(K₂₃)⁻¹ ≈ 1.0019 ≠ contour (exact rational comparison; carried).'),
# ---- alpha
('α','α-1',P,'','Each T_i = R_{p_σ(i)} preserves B exactly (carried).'),
('α','α-1',P,'','JT_iJ = −T_i; P = T_M⋯T_1 = R_{∏p} is invertible (carried).'),
('α','α-2',P,'','Integral α with B-preservation ⇔ α_i = ±e_k (identity coefficient Σα² = 1). α-2 collapses to α-1 up to sign (carried).'),
('α','α-3',P,'','COMPLETE CLASSIFICATION (closes bfa5da3b L158 OPEN): the real α ∈ ℝ^{11} supported on K90 with t t* = 1 (⇔ R_t preserves B) are exactly 70: the 22 vectors ±e_k, and 48 four-term vectors with entries ±½ on 6 supports (3,37,47,53), (3,41,53,71), (3,53,79,89), (37,41,47,71), (37,47,79,89), (41,71,79,89), 8 each. Method: one-monomial sieve (2047 → 38 nontrivial supports), then for each support and each of 16 real-character sign vectors (χ(t) = ±1 for real χ, rank 4), an exact lex Gröbner basis over ℚ with saturation; all 608 jobs decided (290 GB = [1], 146 forced-zero, 100 linear-inconsistent, 72 solved) (s4c; s4d re-examines the 32 empty "solved" jobs). New.'),
('α','α-3',P,'','Structure: each multi-prime solution is ±g·[½(1+a) + ½(1−a)b] with b = 111 (b² = 1; 111 ≡ −1 mod 4, 1 mod 5, −1 mod 7). For any abelian A and b² = 1 this t has tt* = 1, since the cross terms cancel. All 48 arise this way (s8). New.'),
('α','α-3',P,'','The parity JTJ = −T and B-preservation hold for all 70 (linearity; nondegenerate B). New.'),
('α','α-4',X,'','α ≡ 1: identity coefficient Σα² = 11 ≠ 1, and not a similitude (exact; carried).'),
# ---- O5
('O5','O5-1',P,'','Free massive Dirac: a.c. spectrum (−∞,−m] ∪ [m,∞) with infinite multiplicity; explicit ι (carried, ac1dd4e2).'),
('O5','O5-1',P,'','A H A⁻¹ = −H holds exactly in the Majorana representation and fails in the Dirac representation (exact sympy, s5).'),
('O5','O5-2',P,'','m = 0: spectrum ℝ, multiplicity ∞, ι exists (carried).'),
('O5','O5-2',P,'','Majorana inversion holds exactly at m = 0; it fails in the Dirac representation (s5). New.'),
('O5','O5-3',X,'','For every bounded symmetric V such that H_D+V has an isolated eigenvalue of finite multiplicity, no unitary ι exists (k-dim eigenspace vs 2k) (carried, general).'),
('O5','O5-3',X,'','O5-3a (V real scalar, even): A(H_D+V)A⁻¹ = −H_D+V ≠ −(H_D+V) for V ≠ 0 (carried; exact s5).'),
('O5','O5-3',P,'','O5-3b (V = βW(x), W real even): A(H_D+βW)A⁻¹ = −(H_D+βW) exactly in Majorana (s5). The inversion survives; ι still fails (row above). New.'),
('O5','O5-3',C,'T-Weyl','Some O5-3b potential has an isolated eigenvalue in (−m,m): variational bound on H² = p² + M² − iβ(α·∇M) with a wide mass well, plus Weyl stability of σ_ess(H²) = [m²,∞). New, sketch only.'),
]
status={
'Oc-1':'ALIVE as a naming of the 49a1 packet; the identification "R8 Ξ = W₄ element" is REFUTED (Oc-3 row)',
'Oc-2':'OPEN (alive); no vector at levels 196, 392, 784 (partly); explicit basis = O-b stream',
'Oc-3':'ALIVE, strengthened: any square-class reading of R8 gives 0, a non-member of S, or the χ₋₇ unary theta (Eisenstein-type), never a 49a1/Ξ packet vector',
'V-1':'ALIVE (consistent, imposes no constraint; irreducible structure COND)',
'V-2':'ALIVE (all rows PROVED)',
'V-3':'REFUTED (PP-proved)',
'J-1':'REFUTED as a carrier of Ξ (new, awaiting PP audit); survives only as a 49a1 level',
'J-2':'ALIVE; minimal-divisor claim PENDING at 9800',
'J-3':'ALIVE, strengthened (rank 1 = analytic rank 1, no GZK)',
'H-1':'ALIVE','H-2':'ALIVE (real-structure question closed; law-vector link OPEN)','H-3':'REFUTED for every finite d (ι by dimension; new generalisation awaiting PP audit)',
'a-1':'ALIVE','a-2':'ALIVE','a-3':'ALIVE','b-1':'ALIVE (sensitive to the a-choice)','b-2':'ALIVE (insensitive to the a-choice; Kostant now tagged)','b-3':'ALIVE',
'c-1':'ALIVE (matches the contour exactly)','c-2':'ALIVE (matches up to the factor 2 = number of families)','c-3':'REFUTED',
'α-1':'ALIVE','α-2':'ALIVE (≡ α-1 up to sign)','α-3':'ALIVE, CLASSIFIED (70 solutions)','α-4':'REFUTED',
'O5-1':'ALIVE','O5-2':'ALIVE','O5-3':'REFUTED for ι in all sub-branches (inversion survives in O5-3b)'}
key={'Oc-1':'W₄ = K; K f-isotypic COND C2/C3','Oc-2':'no Ξ-eigenvector at 196/392/784 (partial)','Oc-3':'R8 shape can never be a nonzero W₄ vector','V-1':'Hom(V_X,ρ^W)=0 lemma; Ind irreducible COND','V-2':'g₊ Fricke +1 and modularity PROVED','V-3':'not a representation',
'J-1':'f_Ξ ∉ S₂/M₂(980, 1 or χ₁₄₀)','J-2':'f_Ξ ∉ levels 2800, 3920','J-3':'J ~ E×Ξ elementary; rank 1 = an. rank 1','H-1':'exact Option M','H-2':'real structure unique up to unitary equivalence','H-3':'no ι for any finite d',
'a-1':'unramified','a-2':'L(1,χ₁₄₀) = 4log(6+√35)/√140 (COND T-CNF)','a-3':'π_∞ nontrivial','b-1':'entire under a-2/a-3, poles under a-1','b-2':'a-independent','b-3':'forgets Satake','c-1':'= contour, proof given','c-2':'= contour/2','c-3':'≠ contour',
'α-1':'B-preserving','α-2':'= α-1 up to sign','α-3':'exactly 22 + 48 solutions','α-4':'Σα² = 11','O5-1':'Majorana inversion','O5-2':'m = 0 fine','O5-3':'ι impossible'}
decide={'Oc-1':'discharge C2/C3 (N1)','Oc-2':'O-b stream (B5/6272/fallbacks); finish s1e at 784','Oc-3':'a definition of outer_coeff(m); T-theta1 discharge','V-1':'exact (non-float) decomposition of V₄₂; exact ρ(−I) on V₄₂','V-2':'—','V-3':'—',
'J-1':'PP audit of the REF','J-2':'level-9800 rank test (≈5 GB); T-AL-new','J-3':'T-cond, T-AL-new','H-1':'—','H-2':'a definition of the 35-component law vector','H-3':'PP audit',
'a-1':'—','a-2':'T-spin, T-CNF discharge','a-3':'T-CNF','b-1':'T-spin, T-Dir','b-2':'T-Kostant, T-spin','b-3':'—','c-1':'—','c-2':'—','c-3':'—','α-1':'—','α-2':'—','α-3':'PP audit of s4c/s4d','α-4':'—','O5-1':'—','O5-2':'—','O5-3':'T-Weyl (existence only)'}
order=['Oc-1','Oc-2','Oc-3','V-1','V-2','V-3','J-1','J-2','J-3','H-1','H-2','H-3','a-1','a-2','a-3','b-1','b-2','b-3','c-1','c-2','c-3','α-1','α-2','α-3','α-4','O5-1','O5-2','O5-3']
cnt=lambda rs: collections.Counter(r[2] for r in rs)
L=[]; w=L.append
w(f'# FINDINGS (Local-derived): all Local menu branches pursued under Owner t4436, 2026-11-09 {now.strftime("%H:%M")} CST (America/Chicago)\n')
w('- **Authority:** Owner t4436 "Let the math lead the pursuits on all open paths", record OWNER_WRITE_MAINCHAT_t4436_LET_MATH_LEAD_ALL_OPEN_PATHS_2026-11-09_2127.md (sha 32881263…). Every candidate on the menu is a labelled branch. **Nothing is adopted; no branch is "chosen".** Branches are kept or dropped only by PROVED/REFUTED results after PP audit; new REF rows here are marked "PP audit requested".')
w('- **Sources:** menu bfa5da3b (FINDINGS_LOCAL_OWNER_ITEM_CANDIDATE_RESOLUTIONS_t4407_…_1859.md), erratum 511c6ca5 (with PP 320c8c7e and cf7fabc3), evidence_local_owner_candidates_2026-11-09/, PP 2030 (69d33456…), PP 2050 (5bf1e1dc…; T-mod for 49a1 and its twists PROVED), PP 2155 (7c26a452…), PP 2205 (0f1d3361…; T-U7, T-U4, T-theta discharged; θ_{L₁} ∈ M₁(Γ₀(7),χ₋₇) certified). Each PP sha was verified against its sidecar at filing. R8: BOOK/Continue_Resolution_Residual_Shadow_Xi_2026-08-23.md (552541cf…), read only.')
w('- **Grades:** PROVED / COND (condition tags named) / OPEN / REF / PENDING. A citation alone never makes PROVED (OW 36683379). "Carried" = taken from an audited file and not recomputed here. Base F0 and the PARI computational base are as disclosed in PP 5bf1e1dc and 69d33456.')
w('- **Tags:** PP\'s C2, C3, T-AL-new, T-GZK. New Local tags, each a named cited theorem: T-Wald (Waldspurger 1981); T-theta1 (modularity of the unary weight-3/2 theta Σχ₋₇(k)k q^{k²} on Γ₀(196)); F-V42 (the float irreducible decomposition in v42.txt); tip §1u (ρ(−I) = Id on V₄₂, read only); T-cond (conductor of a Weil restriction / isogeny invariance); T-CNF (Dirichlet class number formula); T-spin (spinor-norm twist = central twist of the L-parameter, d2d2d226 item 6); T-Dir (entire continuation and FE of Dirichlet L-functions); T-Kostant (principal-SL₂ decomposition of the adjoint); T-Weyl (Weyl stability of the essential spectrum); REC (record survey).')
w('- **Naming:** "resonant algebra" (RTA is a historical alias only; "Ξ_RTA" = the R8 object of the resonant algebra). **Rules kept:** additive files only; nothing deleted, renamed, moved or overwritten (superseded and failed runs stay on disk, §E). The t4407/t4429 dirs and the A5/A6/ob_v2/O-b fallback files were not touched. No CERT, no Gemini, nothing sent outside. Pure math only. Tip sha checked (§T).\n')
w('## S. Per-branch table (nothing adopted)\n')
w('| Item | Branch | Status | Key result | P / C / O / R / PEND | What would decide it |')
w('|---|---|---|---|---|---|')
for b in order:
    rs=[r for r in rows if r[1]==b]; c=cnt(rs); it=rs[0][0]
    w(f'| {it} | {b} | {status[b]} | {key[b]} | {c[P]} / {c[C]} / {c[O]} / {c[X]} / {c[N]} | {decide[b]} |')
w('')
w('## B. Branch rows (Local-derived)\n')
cur=None
for it,b,g,t,txt in rows:
    if b!=cur:
        w(f'\n**{b}** ({it}) — {status[b]}'); cur=b
    tag=f'{g}: {t}' if t else g
    w(f'- [{tag}] {txt}')
w('')
c=cnt(rows); n=len(rows)
w('## R. Rollup (this file\'s graded rows only; the PP Bridge C rollup 46/11/5/2/1 + V₈₄ of PP 0f1d3361 is separate and unchanged)\n')
w(f'- **{n} rows: PROVED {c[P]} · CONDITIONAL {c[C]} · OPEN {c[O]} · REFUTED {c[X]} · PENDING {c[N]}.**')
items=collections.OrderedDict()
for r in rows: items.setdefault(r[0],[]).append(r)
for it,rs in items.items():
    cc=cnt(rs); w(f'  - {it}: {cc[P]}/{cc[C]}/{cc[O]}/{cc[X]}/{cc[N]}')
cc=collections.Counter(t.strip() for r in rows if r[2]==C for t in r[3].split(','))
w('- COND tags used: '+', '.join(f'{k} ×{v}' for k,v in sorted(cc.items())))
w('- Branches REFUTED (dropped once PP-audited): V-3 (PP-proved), c-3, α-4, H-3 (all d; new generalisation, audit requested), O5-3 (ι; inversion survives in O5-3b), J-1 as a Ξ-carrier (new, audit requested). REFUTED sub-hypothesis: "R8 Ξ is a nonzero W₄ element" (Oc-3 row; audit requested).')
w('- Branches ALIVE: Oc-1, Oc-3, V-1, V-2, J-2, J-3, H-1, H-2, a-1, a-2, a-3, b-1, b-2, b-3, c-1, c-2, α-1, α-2, α-3, O5-1, O5-2. OPEN: Oc-2. PENDING rows: Oc-2 at 784 (6 characters), J-2 at 9800.')
w('- Changes from bfa5da3b + 511c6ca5: α-3 classification OPEN → PROVED; H-2 real-structure OPEN → PROVED immaterial; Oc-1 f-isotypy OPEN → COND C2/C3; V-2 g₊ cited → PROVED; J-3 Milne → elementary proof, and rank equality without GZK added; J-3 conductor PROVED → COND T-cond and b-2 Kostant PROVED → COND T-Kostant under the strict rule. Bridge C stays PARTIAL. Nothing adopted.\n')
w('## N. What to compute next\n')
for i,s in enumerate([
 'J-2: rank test of f_Ξ against S₂ and M₂ of Γ₀(9800) (s2d script ready; needs about 5 GB, so run when the O-b stream is idle). Closes "least divisor level = 19600".',
 'Oc-2: let s1e finish level 784 (D = 8, −8, −7, 28, −56, 56); 1568/3136/6272 belong to the O-b stream.',
 'T-theta1: certify u = Σχ₋₇(k)k q^{k²} ∈ S_{3/2}(Γ₀(196),χ₂₈) by PP 0f1d3361\'s Θ2 + θ³-cocycle method (unary theta with harmonic polynomial k); then the Oc-3 χ₋₇ row is PROVED.',
 'V-1: exact decomposition of V₄₂ over ℚ(ζ₁₄₀) (removes F-V42), and an exact ρ(S)² = Id on V₄₂ by character orthogonality on L′/L (removes the tip §1u dependence without touching the tip).',
 'J-3: discharge T-cond (conductor via E × Ξ, Tate\'s algorithm already exact for each factor; needs isogeny invariance, elementary via Tate modules).',
 'a-2/a-3/b-1/b-2: discharge T-spin by computing Satake parameters of χ∘θ at good primes directly; T-CNF and T-Dir are textbook (F0-type) and could be put on the F0 list by PP ruling.',
 'O5-3b: an explicit separable potential with a provable bound state (1-D Jackiw–Rebbi-type reduction), or a Weyl-free compactness argument.',
 'H-2: needs a definition of the "35-component law vector" (records say none was built). Not math until defined.',
 'Oc-3: needs a definition of outer_even/odd_coeff(m) from the resonant-algebra sources; until then Ξ_RTA stays OPEN.']):
    w(f'{i+1}. {s}')
w('')
w('## E. Evidence (evidence_local_t4436_branches_2026-11-09/; every file has a .sha256 sidecar)\n')
w('| File | sha256 |'); w('|---|---|')
files=sorted(f for f in glob.glob(EV+'/**/*',recursive=True) if os.path.isfile(f) and not f.endswith('.sha256'))
for f in files:
    rel=os.path.relpath(f,EV)
    if rel=='s1e_oc2_small_levels_p11.log' or rel=='gen_findings_t4436.py': w(f'| {rel} | {sha(f)} (at filing; {"still being written by the running job; a final sidecar is added when it ends" if rel.endswith(".log") else "generator"}) |')
    else: w(f'| {rel} | {sha(f)} |')
w('\nCustody notes (all kept on disk; nothing deleted or overwritten):')
for s in ['s4_alpha_full_classification: support-by-support Gröbner basis stalled; killed 21:50 CST; **empty log kept**. Superseded by s4c.',
 's4b_alpha_classification_realchar: a 7-variable Gröbner basis stalled; killed about 22:00 CST; log holds only the real-character matrix (rank 4). Superseded by s4c.',
 's1_oc_branches: crashed at block [4] on a leftover dummy matsolve. Superseded by s1b; blocks [1]–[3] are identical.',
 's1b_oc_branches: blocks [1]–[4] and level 196 of [5] complete; stalled on mfinit([196,3/2,−8]) (conductor ∤ N); killed about 22:08. Continued by s1d → s1e.',
 's1d_oc2_small_levels: T(p²) up to p = 71 too slow; killed about 22:15 with no output. Superseded by s1e (T(121) first).',
 's2b_j2_minimal_level: **its M₂ rows are UNRELIABLE.** mftobasis(…,1) on full spaces returned "solutions" contradicted by the direct rank test. Its S₂ rows agree with s2c. Killed about 22:05. Superseded by s2c.',
 's2c_j2_minimal_level_rank: levels 2800 and 3920 complete; OOM-killed by the kernel at 9800.',
 's2d_j2_level9800_capped: killed by Local at about 22:10 to avoid memory pressure on the other stream\'s ob_v3 job; header-only log.',
 '__pycache__/s4c…pyc: created when s4d imported s4c; kept, with sidecar.',
 'gen_findings_t4436.py wrote this file and refuses to overwrite.']:
    w(f'- {s}')
w('')
tip1=sha(TIP)
w(f'## T. Tip check\n- /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 = {tip1} at filing (expected 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91: {"MATCH" if tip1==tip0 else "MISMATCH"}). Read only.\n')
w('Local-derived. For PP audit. Nothing adopted; no branch chosen; the math decides (t4436). No CERT. Nothing sent outside.')
txt='\n'.join(L)+'\n'
with open(OUT,'x') as fh: fh.write(txt)
with open(OUT+'.sha256','x') as fh: fh.write(f'{sha(OUT)}  {os.path.basename(OUT)}\n')
print(OUT, sha(OUT)); print('rows',n,dict(c))
