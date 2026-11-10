# FINDINGS (Local-derived): Bridge C A1→Ξ→RTA, open-items resolution pass, 2026-11-09 ~18:22 CST (America/Chicago)

- **Authority:** Owner voice 17:30 CST, OW ff8a1670… (t4358), item 4. Ξ := the **curve** 49a1⊗χ₁₄₀ (OW 7b5a725b, 17:03; PP 5cbd050a). Neutral state per OW 5f59e33e and f283cffd.
- **Rules:**
  - Pure math only. Vacuum, source and b are not adopted.
  - Joint carrier, R_c's role, DP-a, Layer2 and the baseline stay neutral or undefined. Nothing here defines them.
  - Additive file. Tip 7cddb188… untouched (sha checked before and after). No CERT. Nothing sent outside. No Gemini. No web computation.
- **Companion erratum:** ERRATUM_LOCAL_RELABEL_ce4d9e80_ROOTNUMBER_VS_FRICKE_SYMBOLS_AND_STS_CONTROL_2026-11-09_1819.md (c2e9b6fe…). Convention: ε = root number, w_N = Fricke eigenvalue, ε = −w_N at weight 2.
- **Builds on:** XW ae951f3e, ADDENDUM ed63348d, RELABEL ce4d9e80, PP 389c2f7c (1525), PP 5cbd050a (1702), carry-forward 60778d10, MR1 0ea030ae, O3 d2d2d226/cf86d913, O5 ac1dd4e2, O7 24e31966, and the PP 1528 audits.
- **Evidence directory:** evidence_local_bridgeC_resolution_2026-11-09/. Every script and log has a .sha256 sidecar. Tools: PARI 2.17.2 via cypari2, plus numpy and sympy, all local.
  - part1_twist_newform.{py,log}: twist, isogeny, newform, carrier decomposition.
  - part3_search.{py,log}: weight-3/2 space search (run stopped by its timeout at level 980; the rows printed are complete).
  - part3_preimage.{py,log} and part3_check2.{py,log}: weight-3/2 eigenspace, Shimura lifts, zero pattern.
  - part4_gamma0_140_weil_e0.{py,log}: χ₁₄₀ on Γ₀(140).
- **Notation:**
  - f := the newform of 49a1 (S₂(Γ₀(49)) = ℂf, w₄₉ = −1). f_Ξ := the newform of Ξ.
  - R_χ(Σa_nq^n) := Σχ(n)a_nq^n.
  - O = ℤ[(1+√−7)/2], with norm form L₁ = [[2,1],[1,4]]. L₄₉ = L₁⊕L₁(7). θ_{L₄₉} = θ₁(τ)θ₁(7τ).

---
## Item 2: Ξ's newform and the level-49 Weil carrier (was OPEN, now resolved)
**2a. f as a CM theta series of the carrier lattice L₁ (PROVED: Hecke's theorem cited, plus a Local check).**
- f = ½·Σ_{α∈O} (α | √−7)·α·q^{N(α)}.
- Here (α | √−7) is the Legendre symbol of α mod √−7 in O/(√−7) ≅ 𝔽₇. Writing α = x + yω, it equals ((x+4y)/7), and Re α = x + y/2.
- Checked equal to `ellan(49a1)` for all n ≤ 600. The Sturm bound for S₂(Γ₀(49)) is 10.
- Modularity of the left side is Hecke's theorem for theta series of the Grössencharacter ψ((α)) = (α|√−7)·α of ℚ(√−7), of conductor (√−7). It is cited, not re-proved.
- So f is the theta series of the **same lattice L₁** that builds the Weil carrier: harmonic polynomial P(α) = α of degree 1, weighted by a character of O/(√−7).

**2b. The cusp part of the carrier theta θ_{L₄₉} is exactly f (PROVED, exact, Local-verified).**
- θ_{L₄₉} = θ₁(τ)θ₁(7τ) ∈ M₂(Γ₀(49)). It is a product of two forms in M₁(Γ₀(7),χ₋₇) and M₁(Γ₀(49),χ₋₇); built with `mffromqf`.
- Exact linear algebra in M₂(Γ₀(49)) gives **θ_{L₄₉} = E + 1·f**, with E in the 7-dimensional Eisenstein space. Dimensions: dim M₂ = 8, dim E₂ = 7, dim S₂ = 1; the coefficient check through n ≤ 200 passes.
- So π_cusp(θ_{L₄₉}) = f, with no extra constant.
- The Fricke signs agree: θ_{L₄₉}|W = −θ_{L₄₉} (XW), and `mfatkininit` gives w₄₉(f) = −1.

**2c. Ξ's newform is an exact twist of the carrier's cusp part (PROVED).**
- **f_Ξ = R_{χ₁₄₀}(f) = R_{χ₋₂₀}(f) = R_{χ₁₄₀}(π_cusp θ_{L₄₉}).**
- Proof:
  - (i) a_n(f) = 0 when 7 | n, since a₇ = 0 at additive reduction.
  - (ii) For 7 ∤ n with a_n(f) ≠ 0, n is the norm of an ideal prime to (√−7), so χ₋₇(n) = 1. Hence χ₁₄₀(n) = χ₋₂₀(n)·χ₋₇(n) = χ₋₂₀(n).
  - (iii) R_χ maps S₂(Γ₀(49)) into S₂(Γ₀(lcm(49, m²))) for a primitive χ mod m (Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions*, Prop. 3.64; cited). lcm(49, 140²) = lcm(49, 20²) = **19600**.
  - (iv) Both R_{χ₁₄₀}f and f_Ξ lie in S₂(Γ₀(19600)), and their coefficients agree for all n ≤ 7000, above the Sturm bound 6721 (part1 log).
- **Explicit twist operator:** R_χ f(τ) = g(χ)⁻¹·Σ_{u mod m} χ(u) f(τ + u/m), for χ real and primitive mod m. Here g(χ₁₄₀) = √140 and g(χ₋₂₀) = i√20 (standard).
- **CM form of Ξ:** f_Ξ = ½·Σ_{α∈O} χ₋₂₀(Nα)·(α|√−7)·α·q^{Nα}, again a theta series on L₁. Also R_{χ₋₇}f_Ξ = f_Ξ (checked n ≤ 7000).
- **Level relation:** this is twist level-raising, 49 → 49·20² = 19600. It is not Ribet level-raising. 49a1 is the twist-minimal member of Ξ's twist class.

**2d. Equivariance and sign law (PROVED; Atkin–Li cited, Local-verified).**
- **W₁₉₆₀₀(R_{χ₋₂₀}f) = χ₋₂₀(−49)·w₄₉(f)·R_{χ₋₂₀}f** (Atkin–Li 1978; χ₋₂₀ quadratic with conductor 20 prime to 49).
- So w₁₉₆₀₀(f_Ξ) = (−1)·(−1) = **+1**, confirmed by ε(Ξ) = −1 and `lfuncheckfeq` = −135 bits.
- The flip comes only from **χ₋₂₀(−1) = −1**, the odd 2·5 part of χ₁₄₀; χ₋₂₀(49) = +1.
- Using χ₁₄₀ directly in Atkin–Li is not allowed (its conductor shares 7 with 49). 2c makes that unnecessary.
- **Signs on record:**
  - f: −1 at level 49.
  - θ_{L₄₉}: −1, weight 2.
  - g₊: +1, Eisenstein.
  - θ_{L₄₉}²: +1, weight 4.
  - f_Ξ: **+1** at level 19600.
  - f²: +1 at weight 4 (`mfatkininit`, exact).

**2e. REFUTED (counterexample): "f_Ξ lies in the span of twists of the weight-2 carrier F₂ = (θ₁², 7θ₁(7·)²)."**
- R_{χ₁₄₀}(θ₁(7·)²) = 0 identically, since every exponent is divisible by 7.
- R_{χ₁₄₀}(θ₁²) = 4q − 16q³ + 52q⁹ − 48q¹¹ + …, while f_Ξ = q − 3q⁹ − 4q¹¹ + ….
- The q¹ coefficient forces the factor 1/4, but then the q³ coefficient is −4 where f_Ξ has 0.
- So the link to the carrier goes through **θ_{L₄₉}** (2b and 2c), not through g₊ or F₂.

**2f. REFUTED (weight): "f_Ξ is a twist of the cusp part of θ_{L₄₉}²."**
- Twisting preserves weight, and the weights are 4 and 2.
- PROVED (exact): the cusp part of θ_{L₄₉}² is **not** proportional to f². The rank of {f², cusp(θ_{L₄₉}²)} in S₄(Γ₀(49)) is 2, with dim S₄ = 10, even though both are Fricke +1.

**2g. PROVED (pure fact; no joint-carrier definition): f_Ξ ∉ S₂(Γ₀(980)).** Ξ has conductor 19600, so f_Ξ is new at 19600, and by multiplicity one it does not occur at level 980 | 19600. Whether this bears on a "joint carrier" stays undefined, since the Owner holds that neutral.

## Item 3: weight 3/2 versus the integral-weight carriers (was OPEN, now PARTIAL)
**3a. PROVED (exact).**
- S_{3/2}(Γ₀(196)) with trivial character has dim 6, and its Kohnen plus space is 0. It has **no** T(p²)-eigenvector with eigenvalues a_p(f): T(9) has characteristic polynomial (x+2)²(x²−2)², with no root a₃(f) = 0.
- S_{3/2}(Γ₀(196), χ₂₈), with χ₂₈ = χ₋₄χ₋₇, has dim 9. Its common eigenspace for T(p²) = a_p(f), p ∈ {3,11,13,23,29,37}, has **dim 4**.
- Search rows (part3_search.log):
  - level 392: trivial character and character 8 give 0; character 28 gives dim 6.
  - level 980: trivial character and character 5 give 0.
- Row-reduced q-expansions (n = 0..60) are in part3_preimage.log. The first is F₁ = q − 2q⁸ + q⁹ − 2q¹⁶ + q²⁵ + 2q²⁹ − 2q³² + 2q³⁷ + 4q⁶⁰ + ….

**3b. PROVED (exact), with a limit.**
- All four t = 1 Shimura lifts (`mfshimura`) lie in span{f(τ), f(2τ)}, the old space of f at level 98. So the packet maps onto f.
- For t = 3 and t = 5, one basis vector (F₁) lifts with a component outside that span. So the 4-dimensional space is **not exactly** f-isotypic, and that subspace is still to be pinned (3e, O-a).

**3c. PROVED (exact): c(35) = 0 on the whole 4-dimensional space.**
- 35 is the index with coredisc(35) = 140, i.e. χ_{coredisc(35)} = χ₁₄₀, the character defining Ξ.
- This matches L(Ξ,1) = 0, which is forced by ε(Ξ) = −1. The analytic rank is 1, with L′(Ξ,1) = 4.43262273….

**3d. CONDITIONAL (Waldspurger, cited) interpretation of exact data.**
- For all **75/75** squarefree n ≤ 120: c(n) ≢ 0 on the space ⇔ L(f⊗χ_{coredisc(n)}, 1) ≠ 0 (part3_check2.log).
- The twist index works out as χ₋ₙ·χ₂₈·χ₋₇ = χ_{coredisc(n)}, using f⊗χ₋₇ = f.
- Reading: Ξ has **no new** half-integral-weight object. Its central value sits at index **n = 35** inside the 49a1 Waldspurger packet in S_{3/2}(Γ₀(196), χ₂₈).
- References: Waldspurger, J. Math. Pures Appl. 60 (1981) 375–484; Shimura, Ann. of Math. 97 (1973).
- Kohnen–Zagier does not apply directly, since 49 is not squarefree.

**3e. OPEN, each with a precise reason.**
- (O-a) The exact f-isotypic subspace, cut out by all T(p²) including p = 5, 17, 19, … and by the U/V operators at 2 and 7.
- (O-b) A form whose own Shimura lift is f_Ξ, i.e. with T(p²)-eigenvalues χ₁₄₀(p)a_p(f), at level 4·19600 = 78400. Not computed: the space is too large for this pass.
- (O-c) Whether the RTA "weight-3/2 Ξ shadow" (DEFINITION_RTA_RESIDUALS…_2026-10-26.md:53–55) **is** this packet. That object predates the Owner naming Ξ as the curve, so this is a definition question, not a theorem.

## Item 4: the two CONDITIONAL items
**4a. χ₁₄₀ on all of Γ₀(140): CONDITIONAL → PROVED (computer-assisted, exact by a norm argument).**
- **Statement:** for every γ = (a,b;c,d) ∈ Γ₀(140), ρ_{N₂}(γ)e₀ = χ₁₄₀(d)·e₀.
- **Proof.**
  - (i) d ↦ d mod 140 is a homomorphism Γ₀(140) → (ℤ/140)*, because the lower-right entry of a product is c₁b₂ + d₁d₂ ≡ d₁d₂. So γ ↦ χ₁₄₀(d) is a character, and {γ : ρ(γ)e₀ = χ₁₄₀(d)e₀} is a subgroup.
  - (ii) There are 288 cosets (via P¹(ℤ/140)) and **259 nontrivial Schreier generators**, with word length ≤ 39 and at most 10 S-letters.
  - (iii) For every generator and every one of the **48 Galois twists** ρ_a (ζ₁₄₀ ↦ ζ₁₄₀^a, √140 ↦ χ₁₄₀(a)√140, since √140 is the Gauss sum of χ₁₄₀), the max residual is **5.21×10⁻¹³**.
  - (iv) Exactness. Let β := 140^{⌈k/2⌉}(ρ(g)e₀ − χ₁₄₀(d)e₀). Its entries lie in ℤ[ζ₁₄₀], and its Galois conjugates are exactly the twisted computations. So |σ_a(β_i)| ≤ 140⁵·5.21×10⁻¹³ ≈ 0.028 < 1 for all a. Then |N(β_i)| < 1, and since N(β_i) ∈ ℤ, β_i = 0.
  - Control: (1,0;70,1) sends e₀ completely off e₀: e₀-component 4×10⁻¹⁶, off-mass 1.0.
- **Dependencies:** the cited hypothesis H (factorization through SL₂(ℤ/140)) is **no longer used**. It uses only that ρ_{N₂} is a representation of SL₂(ℤ), which is the definition of the Weil representation for even signature (Bruinier, LNM 1780, §1.1). The relations S⁴ = 1 and (ST)³ = S² were checked at a = 1, 3, 139 to 1.7×10⁻¹³.
- **Caveat for PP:** the floating-point error is measured, not interval-bounded; the margin is about 35×. Hardening with interval arithmetic is Local work of about 30 min.
- **"Is it the Weil character?"** Yes. χ₁₄₀(d) is exactly the character by which Γ₀(140) acts on the e₀-line of Weil(N₂).

**4b. Induced-carrier step (LD-Ξ2): split into math (PROVED) and adoption (CONDITIONAL, Owner).**
- **Math (PROVED).**
  - W normalizes Γ₀(49), and W² = −49·I is scalar.
  - For any representation ρ of Γ₀(49) on V with ρ(−I) = (−1)^k·Id, the weight-k action of Γ₀(49)⁺ modulo scalars on pairs (F, F|W) is the representation induced from the index-2 normal subgroup. W acts by the block swap [[0, Id],[Id, 0]].
  - Its +1 eigenvectors are exactly F + F|W, which is nonzero iff F|W ≠ −F.
- **The one mathematical condition, ρ(−I) = Id on V₄₂ (even k),** is recorded in the tip (§1u: dim Fix(S_lab⁻²)|_{V₄₂} = 42). It is cited read-only, not re-derived.
- **Adoption** of the doubled carrier V₄₂⊕V₄₂ (Path A V₈₄) is an **Owner decision**; the tip lists it as "not folded". This is not a math lemma.

## Item 5: exact H_{+U}: OPEN (undefined)
- No record defines H_{+U}. Owner DEF1 gives only H_{−U} = H_{+U}⊗ℂ² (ac1dd4e2 L41; PP 1530 R4 "H_{+U}: OPEN — CONFIRM").
- Not attempted, because inventing it is outside the derive grant. Blocked on the Owner.

## Item 6: triage, open-item table (all Local items)
| # | Item | Label now | Resolution path | Blocked on | ETA |
|---|---|---|---|---|---|
| 1 | ce4d9e80 ε/w symbol swap + STS⁻¹ name | RESOLVED (erratum 1819) | PP audit | PP | done (Local) |
| 2 | Ξ newform ↔ level-49 Weil carrier | **PROVED** (2a–2d, 2g); 2 REFUTED (2e, 2f) | PP audit | PP | done (Local) |
| 3 | Weight-3/2 vs integral weight | **PARTIAL**: 3a–3c PROVED, 3d CONDITIONAL (Waldspurger) | O-a: Hecke/U-operator cut (Local); O-b: twist-family theory or bigger compute (Local); O-c: Owner says which object "weight-3/2 Ξ" names | Local (O-a, O-b); Owner (O-c) | O-a ~1 h; O-b ~3–6 h, may not be feasible at level 78400; O-c Owner decision |
| 4 | χ₁₄₀ on all of Γ₀(140) | **PROVED** (computer-assisted) | optional interval-arithmetic hardening; PP audit | Local / PP | ~30 min |
| 5 | Induced-carrier step | math PROVED; adoption CONDITIONAL | Owner adopts or declines V₈₄ | Owner | Owner decision |
| 6 | Doubled carrier V₄₂⊕V₄₂ (Path A V₈₄) | Owner decision | same as 5 | Owner | Owner decision |
| 7 | Joint carrier, incl. minimal level 980 vs 19600 | UNDEFINED (Owner neutral). Fact 2g: f_Ξ ∉ S₂(Γ₀(980)) | Owner defines it, or it stays undefined | Owner | Owner decision |
| 8 | Exact H_{+U} | OPEN (undefined) | Owner definition | Owner | Owner decision |
| 9 | O3 LD-O3a/b/c (Λ(s,π), ω₂₃) | Owner decision | Owner adopts or declines | Owner | Owner decision |
| 10 | O4 α preserves B | HOLD (α undefined) | Owner defines α, then Local check | Owner, then Local | Owner decision, then ~1 h |
| 11 | O5 explicit ι | CONDITIONAL on H being free Dirac, a physical choice that is not adopted | Owner/physics choice | Owner | Owner decision |
| 12 | O7 Cand-1⁺ full statement | OPEN (Collatz-type; verified ≤ 10¹⁰; any other cycle has length ≥ 79,335) | a new idea is needed | Local (research) | no finite ETA |
| 13 | Λ₀ dynamical derivation (why ℚ(√35)) | OPEN; physics, out of the pure-math lane | physics lanes | other lanes / Owner | no finite ETA in the Local lane |
| 14 | "2- and 5-parts on Γ₀(49) without twisting" (XW) | OPEN (needs a precise statement) | 2d gives a partial answer: the 2·5 part χ₋₂₀ is exactly what flips the Fricke sign | Local (formulation) | ~1 h once stated |
| 15 | Bridge C overall | **PARTIAL** | items 3 (O-c), 5–11 and 13 sit with the Owner or other lanes | Owner | Owner decision |

## Rollup (this file)
- **Relabels:**
  - Item 2: OPEN → PROVED.
  - χ₁₄₀ on Γ₀(140): CONDITIONAL → PROVED (computer-assisted).
  - Weight-3/2: OPEN → PARTIAL.
  - Induced carrier: CONDITIONAL → math PROVED + adoption CONDITIONAL.
- **PROVED 11:**
  - 2a (citing Hecke), 2b, 2c, 2d (citing Atkin–Li, Local-verified), 2g;
  - the f² vs cusp(θ_{L₄₉}²) rank-2 fact;
  - 3a, 3b, 3c;
  - 4a;
  - 4b (math).
- **CONDITIONAL 2:** 3d (Waldspurger) and 4b (Owner adoption).
- **OPEN 6:** O-a, O-b, O-c, H_{+U}, the Λ₀ dynamical derivation, and the "2/5-parts" formulation. The joint carrier is UNDEFINED and not counted.
- **REFUTED 2:** 2e and 2f.
- **Unchanged triage:** O3 (Owner decision), O4 (HOLD), O5 (CONDITIONAL, physical), O7 (OPEN, no finite ETA), V₈₄ (Owner decision).

Local-derived. For PP audit. Tip 7cddb188 untouched. No CERT. Nothing sent outside.
