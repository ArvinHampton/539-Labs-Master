# FINDINGS (Local-derived): candidate resolutions for the Local Owner-decision items under t4407, 2026-11-09 18:59 CST (America/Chicago)

- **Authority:** Owner t4407 "Pursue all for resolutions", record OWNER_WRITE_MAINCHAT_t4407_PURSUE_ALL_OPEN_ITEMS_FOR_RESOLUTIONS_2026-11-09_1843.md (sha b0b9ae7f…; verified in Physicist transcript pos 18285, cu:405590937).
- **NOTHING HERE IS ADOPTED. The Owner chooses.** Every candidate below is a Local-derived proposal: a precise definition plus the consequences derived from it. A "Recommendation" is Local's advice only.
- **Rules kept:** pure math only (no nonlocal / EH-11D / PT-physics / simulated-physics content). Additive new file; nothing deleted, renamed, moved or overwritten. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md untouched (sha 7cddb188ca340ad9… checked before and after). No CERT. No Gemini. Nothing sent outside. No messages to other agents.
- **Sources read:** 9e34f2dc (open-items pass, 15-row table), ae951f3e (XW) + ed63348d, c2e9b6fe (ε/w erratum: ε = root number, w_N = Fricke eigenvalue, ε = −w_N at weight 2), d2d2d226 + cf86d913 (O3), 0344dc48 (LD-1), 4b25d2ed + ac1dd4e2 (O5 / ι), 24e31966 (O7, not an item here), 5a6e7177 (3:11 blueprint), f283cffd (Ξ := 49a1⊗χ₁₄₀; joint carrier / R_c / baseline neutral), 7b5a725b (Ξ names the curve; O1 OPEN), 9a8ced02 (O1 parity only by derivation), RELABEL ce4d9e80 §4 (980), Addendum J/L 2026-11-05 (K90, T_i = Σα_ik R_pk), tip §1p/§1u/P2 (read-only), RTA R8 definition (grok-batches DEFINITION_RTA_RESIDUALS…_2026-10-26.md:53–55).
- **Grade tags:** each graded claim carries exactly one tag. PROVED = proof given or cited theorem + Local check; COND = conditional, condition named; OPEN = not settled or undefined; REF = refuted by proof or explicit counterexample only. "(cited)" marks a PROVED result carried from an earlier audited/Local file, not re-proved here.
- **Evidence:** evidence_local_owner_candidates_2026-11-09/ (PARI 2.17.2 via cypari2, numpy, scipy, sympy; all local). Every script and log has a .sha256 sidecar. Superseded attempts are kept on disk and flagged in §E.

## S. Summary table (nothing adopted; the Owner chooses)
| # | Item | Candidates | Local recommendation | PROVED / COND / OPEN / REF |
|---|---|---|---|---|
| I1 | O-c | Oc-1, Oc-2, Oc-3 | **Oc-3** | 4 / 2 / 3 / 0 |
| I2 | V₈₄ | V-1, V-2, V-3 | **V-2** | 4 / 1 / 0 / 1 |
| I3 | joint carrier | J-1, J-2, J-3 | **J-3 (+J-2 level)** | 10 / 0 / 2 / 0 |
| I4 | H_{+U} | H-1, H-2, H-3 | **H-1** | 3 / 0 / 1 / 2 |
| I5 | LD-O3a | a-1, a-2, a-3 | **a-1** | 6 / 1 / 0 / 0 |
| I6 | LD-O3b | b-1, b-2, b-3 | **b-1** | 5 / 0 / 0 / 0 |
| I7 | LD-O3c | c-1, c-2, c-3 | **c-1** | 2 / 0 / 0 / 1 |
| I8 | α (O4) | α-1, α-2, α-3, α-4 | **α-1** | 5 / 0 / 1 / 1 |
| I9 | O5 free Dirac | O5-1, O5-2, O5-3 | **O5-1** | 3 / 0 / 0 / 2 |

## I1. O-c — what the RTA "weight-3/2 Ξ shadow" names
Context: OW 7b5a725b makes Ξ the CURVE 49a1⊗χ₁₄₀. The RTA object (R8: residual products of the outer disc-35 series with shifted weight-3/2 series, characteristics 7m, 7m+7/2) predates that naming. 9e34f2dc found the 49a1 Waldspurger packet W₄ ⊂ S_{3/2}(Γ₀(196), χ₂₈) (dim 4) with c(35) = 0 on all of it.

**Oc-1 "49a1 packet".** Definition: Ξ^{(3/2)} := W₄, the common eigenspace of T(p²) = a_p(f), p ∈ {3,11,13,23,29,37}, in S_{3/2}(Γ₀(196), χ₂₈); "the Ξ datum" := the coefficient functional c(35).
- [PROVED] (cited 9e34f2dc 3a, 3c) dim W₄ = 4 and c(35) = 0 identically on W₄.
- [PROVED] 35 is the only squarefree n with χ_{coredisc(n)} = χ₁₄₀: coredisc(n) = 140 forces core(n) = 35, and a squarefree n with core 35 is 35.
- [COND: Waldspurger 1981, cited] c(35)² is proportional to L(f⊗χ₁₄₀, 1) = L(Ξ, 1), which is 0 because ε(Ξ) = −1. So the zero at n = 35 is Ξ's central value.
- [OPEN] W₄ is not exactly f-isotypic (9e34f2dc 3b: the t = 3, 5 lifts of F₁ leave span{f(τ), f(2τ)}). So Oc-1 is pinned only after O-a.

**Oc-2 "Ξ's own packet".** Definition: Ξ^{(3/2)} := the space of g ∈ S_{3/2}(Γ₀(4·19600), ψ) (ψ quadratic, ψ² = 1) with T(p²)g = a_p(f_Ξ)g = χ₁₄₀(p)a_p(f)g for all p ∤ 2·5·7.
- [COND: Waldspurger/Shimura existence, cited] nonzero for a suitable ψ.
- [PROVED] Oc-2 cannot be reached from W₄ by twisting coefficients. Proof: for quadratic ψ and p ∤ cond(ψ), (Σψ(n)c(n)qⁿ)|T(p²) has the same eigenvalue as Σc(n)qⁿ|T(p²), because each of the three terms of T(p²) picks up ψ(n) and a factor ψ(p)^{0 or ±2} = 1. So a twist keeps the eigenvalue a_p(f) and never gives χ₁₄₀(p)a_p(f) when χ₁₄₀(p) = −1.
- [OPEN] An explicit basis (this is O-b, level 78400, not computed).

**Oc-3 "disambiguate".** Definition: Ξ denotes only the curve (OW 7b5a725b). The RTA R8 object keeps its own definition under a new symbol, Ξ_RTA^{(3/2)}. No identification with Oc-1 or Oc-2 is asserted.
- [PROVED] Consistent with every Owner record; no PROVED Local result depends on the identification (all of 9e34f2dc items 2–4 concern f, f_Ξ and W₄ only).
- [OPEN] Any theorem relating Ξ_RTA^{(3/2)} to W₄ or Oc-2. Not computed: R8's level and character have not been matched to Γ₀(196), χ₂₈.

**Recommendation: Oc-3,** with Oc-1's facts recorded as a remark ("Ξ's central value is the n = 35 coefficient of the 49a1 packet"). Reason: the Owner fixed Ξ as the curve, and identifying the older RTA object with any packet would be an unproved claim. Oc-1 also still depends on O-a, and Oc-2 on O-b.

## I2. V₈₄ — adoption of the induced (doubled) carrier
Context: tip P2 is VACATED and ρ(W₇) is CLOSED ABSENT on V₄₂ (R26: no invertible intertwiner). The tip says any Fricke role needs a new carrier and a new Owner Write (Path A V₈₄ "not folded"). k = −2. The tip §1u (cited read-only) gives ρ(−I) = Id on V₄₂.

**V-1 "induce".** Definition: V₈₄ := V₄₂ ⊕ V₄₂ with Ind_{Γ₀(49)}^{Γ₀(49)⁺}ρ: γ ↦ diag(ρ(γ), ρ(W⁻¹γW)) for γ ∈ Γ₀(49), and W ↦ [[0, ρ(W²)], [Id, 0]] = [[0, Id], [Id, 0]].
- [PROVED] This is a representation of Γ₀(49)⁺ (Γ₀(49) is normal of index 2; standard induction). Its restriction to Γ₀(49) is ρ ⊕ ρ^W with ρ^W(γ) := ρ(W⁻¹γW). It needs no ρ(W₇) on V₄₂, so it does not contradict R26.
- [COND: tip §1u ρ(−I) = Id on V₄₂, cited read-only] ρ(W²) = Id. At k = −2 the scalar W² = −49·I slashes trivially: (λ²)^{k/2}·λ^{−k} = 49^{−2}·(−49)² = 1.
- [PROVED] For any form F for (Γ₀(49), ρ) at weight −2, Φ := (F, F|W) is a form for (Γ₀(49)⁺, Ind ρ). Its +1 vectors are the symmetrizations F + F|W, which are nonzero iff F|W ≠ −F (9e34f2dc 4b).
- [PROVED] Consequence: on V₈₄ the +1 law imposes no constraint on F. Every F with F|W ≠ −F gives a +1 vector, so V₈₄ does not force anything.

**V-2 "decline (status quo)".** Definition: V₈₄ is not adopted. The residual carrier stays V₄₂ on Γ₀(49) with P2 VACATED.
- [PROVED] (cited) The +1 Fricke law is still realised, but only on the scalar Eisenstein carrier g₊ = θ₁² − 7θ₁(7·)² at level 49 (XW LD-Ξ1(b)) and on f_Ξ at level 19600 (9e34f2dc 2d: w₁₉₆₀₀ = +1). Nothing in 9e34f2dc or c2e9b6fe changes.

**V-3 "diagonal doubling".** Definition: V₄₂ ⊕ V₄₂ with γ ↦ diag(ρ(γ), ρ(γ)) and W ↦ the plain swap.
- [REF] Not a representation of Γ₀(49)⁺. Proof: it is one iff ρ(WγW⁻¹) = ρ(γ) for all γ ∈ Γ₀(49), i.e. iff Id intertwines ρ and ρ^W. Tip R26 (cited, Auditor-confirmed) says no invertible intertwiner exists on V₄₂. This refutation rests on that cited premise.

**Recommendation: V-2 (do not adopt V₈₄ now).** Reason: V-1 is consistent but its +1 law is tautological and adds no constraint, while adopting it reopens the tip's P2 VACATED decision. V-3 is refuted. V-1 stays available if the Owner later wants Fricke to act on a residual carrier.

## I3. Joint carrier (currently UNDEFINED, Owner neutral)
Context: the withdrawn t4327 text (ed526f70, history only) spoke of "an abelian variety J/ℚ … with the joint level minimized". Neutral per 5f59e33e and f283cffd.

**J-1 "level 980".** Definition: the joint carrier is the space of forms on Γ₀(980) = Γ₀(49) ∩ Γ₀(140), with ρ_{N₂}'s e₀-character χ₁₄₀ restricted.
- [PROVED] (cited RELABEL ce4d9e80 §4) Γ₀(49) ∩ Γ₀(140) = Γ₀(980).
- [PROVED] (cited 9e34f2dc 2g) f_Ξ ∉ S₂(Γ₀(980)). So J-1 does not carry Ξ.
- [PROVED] (cited, PP counterexample) W₄₉ does not normalize Γ₀(980), since WTW⁻¹ = (1,0;−49,1) ∉ Γ₀(980). So J-1 carries no Fricke +1 law either.

**J-2 "modular level 19600".** Definition: the joint carrier is S₂(Γ₀(19600)) (equivalently J₀(19600)), with the χ₁₄₀ e₀-character and Γ₀(49) both restricted to Γ₀(19600).
- [PROVED] 980 | 19600, so Γ₀(19600) ⊂ Γ₀(49) ∩ Γ₀(140) and both restrictions make sense (log c1).
- [PROVED] f_Ξ is new at 19600 and f occurs as old forms f(dτ), d | 400. The least N with both in S₂(Γ₀(N)) is lcm(49, 19600) = 19600 (newform theory: a newform of level M occurs in S₂(Γ₀(N)) iff M | N). Under J-2 this settles "980 vs 19600" as 19600.
- [PROVED] W₁₉₆₀₀ normalizes Γ₀(19600), and w₁₉₆₀₀(f_Ξ) = +1 (cited 9e34f2dc 2d; c2e9b6fe convention).
- [OPEN] What an "equivariant embedding of the vector-valued Weil carrier" (V₄₂) into J-2 means. Undefined, so not attempted.

**J-3 "Weil restriction".** Definition: J := Res_{K/ℚ}(E₄₉), with K = ℚ(√35) (the field of χ₁₄₀ and Λ₀) and E₄₉ = 49a1. This is an abelian surface over ℚ.
- [PROVED] E₄₉ ≅ Ξ over K. Exact check (log c1): c₄(Ξ)/c₄(E) = 140² and c₆(Ξ)/c₆(E) = 140³, so Ξ is the twist by u² = 140 = (2√35)², a square in K.
- [PROVED] J ~ E₄₉ × Ξ over ℚ (isogeny), and L(J, s) = L(E₄₉, s)·L(Ξ, s). This is the standard decomposition Res_{K/ℚ}E_K ~ E × E^{χ_K}. Local check (log c1): for the first 400 primes p ∉ {2,5,7} (193 split, 204 inert), a_𝔭(E/K) = a_p(E) when p splits and a_𝔭 = a_p(E)² − 2p when p is inert, with a_p(Ξ) = χ₁₄₀(p)a_p(E) throughout. The log's label "primes 3..400" is a mislabel for "first 400 primes".
- [PROVED] cond(J) = 49·19600 = 960400. J is a quotient of J₀(19600) up to isogeny, and 19600 is the least such level. This follows from J-2 plus modularity of CM curves (Shimura/Deuring; cited).
- [PROVED] Root number ε(J) = ε(E₄₉)ε(Ξ) = (+1)(−1) = −1. The analytic rank of J is 0 + 1 = 1 (cited c2e9b6fe §4: L(49a1,1) = 0.96665…, L′(Ξ,1) = 4.43262…).
- [OPEN] As in J-2, the Weil-carrier side (V₄₂ / N₂) enters only through K and χ₁₄₀; no equivariant map V₄₂ → (anything attached to J) is defined.

**Recommendation: J-3, with J-2 as its modular level.** Reason: J-3 is canonical (fixed by 49a1 and ℚ(√35) alone, with no free choices). It is an abelian variety over ℚ containing both 49a1 and Ξ, and its minimal modular level 19600 is PROVED. J-1 carries neither Ξ nor Fricke. The Weil-carrier embedding stays OPEN under every candidate.

## I4. H_{+U} — the exact +U Hilbert space (Owner DEF1 gives only H_{−U} = H_{+U}⊗ℂ²; B2 = (B)-M adopted, OW e9c1dbda)
Mathematical definitions only; no physical reading is claimed.

**H-1 "Dirac spinors".** Definition: H_{+U} := L²(ℝ³) ⊗ ℂ⁴ (LR-0 of 4b25d2ed).
- [PROVED] Option M on H_{+U} ⊗ ℂ²: P̂ = (γ⁰Π ⊗ σ_x)K is antiunitary, P̂² = γ⁰γ⁰* = −1 in the Majorana representation, and P̂(H_D⊗1)P̂⁻¹ = −H_D⊗1. Cited from NL B-1…B-4. Local fibre re-check (log c4b): Majorana representation found by exhaustive Pauli search (Clifford err 0), with P̂² = −1 and anticommutation residual 0.
- [PROVED] (cited ac1dd4e2) With the free Dirac H, a unitary intertwiner ι: H_{+U} → H_{−U}, ιH = (H⊗1₂)ι, exists and is explicit (LD-O5).

**H-2 "Dirac spinors × 35 internal components".** Definition: H_{+U} := L²(ℝ³) ⊗ ℂ⁴ ⊗ ℂ³⁵, with K acting coordinatewise in the standard basis of ℂ³⁵.
- [PROVED] P_rev = (γ⁰ ⊗ 1₃₅)KΠ has the same square γ⁰γ⁰* ⊗ 1₃₅ (log c4b, err 0). Option M carries over verbatim, and so does the ι of H-1, since the multiplicity of H_D ⊗ 1₃₅ is still ∞.
- [OPEN] Which real structure on ℂ³⁵, and any link to the "35-component law vector": the records say no law vector was ever built. Not invented here.

**H-3 "finite-dimensional".** Definition: H_{+U} := ℂ^d (e.g. d = 35), with no spatial factor.
- [REF] (cited 4b25d2ed result 2) An anti-diagonal P_rev with P_rev² = ±1 on ℂ^d ⊕ ℂ^{2d} cannot exist (rank 1:2), and neither can a unitary ι.
- [REF] For odd d, Option M's P̂² = −1 is impossible. Proof: P̂ = (A ⊗ σ_x) with A = VK antiunitary on ℂ^d gives P̂² = VV̄ ⊗ 1. If VV̄ = −1 then |det V|² = det(VV̄) = (−1)^d = −1, which is impossible. So P̂² = +1 ≠ −1, contradicting the adopted (B)-M square.

**Recommendation: H-1.** Reason: every adopted or PROVED P_rev result (B2 = (B)-M, ι) already holds on H-1, and it invents no internal structure. H-2 is the conservative extension if the Owner wants a 35-index, but its real structure is OPEN. H-3 contradicts the adopted (B)-M square for d = 35.

## I5. LD-O3a — π away from v = 23 (Codex fixes only π₂₃ = 1; π = χ∘θ with χ quadratic, χ₂₃ = 1, cited d2d2d226 item 3)

**a-1 "trivial".** Definition: π := 1 (χ = 1 at every place).
- [PROVED] (cited d2d2d226 items 3–4) π is automorphic (residual, constants are L² because the volume is finite) and unramified everywhere.
- [PROVED] (cited d2d2d226 item 8c) π carries no datum at Bridge C's primes {2, 5, 7}. This is a fact, not a contradiction.

**a-2 "Ξ-aligned".** Definition: π := χ₁₄₀∘θ, with χ₁₄₀ the idèle-class character of ℚ(√35) and θ the spinor norm.
- [PROVED] π₂₃ = 1: 23 ∤ 140 and (140/23) = +1 (log c2), so χ₁₄₀,₂₃ is unramified and trivial on ℚ₂₃^×. This is consistent with the Codex datum.
- [PROVED] π is automorphic: χ₁₄₀ is trivial on ℚ^×, so χ₁₄₀∘θ is trivial on G(ℚ). π ≠ 1, π is ramified exactly at {2, 5, 7}, and π_∞ is trivial because χ₁₄₀(−1) = +1 (log c2).
- [COND: identification of spinor-norm twists with central twists of the principal parameter, as in d2d2d226 item 6] Λ(s, π, std) = Λ(s, χ₁₄₀)²·∏_{i=1}^{23} Λ(s−i, χ₁₄₀)Λ(s+i, χ₁₄₀). It is entire, and its central factor involves L(1, χ₁₄₀) = 4·Reg(ℚ(√35))/√140. This is the same value as in Λ₀ = √(7/8)·L(1, χ₁₄₀) (PROVED identity, MR1-AM). The link is structural only.

**a-3 "CM-aligned".** Definition: π := χ₋₇∘θ, using the CM character of 49a1.
- [PROVED] (−7/23) = +1, so π₂₃ = 1. π is ramified only at 7, and π_∞ = sign∘θ is nontrivial since χ₋₇(−1) = −1 (log c2).
- [PROVED] The full candidate set is {1} ∪ {χ_D∘θ : D a fundamental discriminant, 23 ∤ D, (D/23) = +1}. It is infinite (Dirichlet), so the Codex datum alone does not determine π. For example χ₋₂₀ is allowed, while χ₅, χ₋₄, χ₂₈ and χ₋₃₅ are excluded (log c2).

**Recommendation: a-1.** Reason: it is the unique choice that adds no datum beyond the Codex. a-2 is the choice to take if the Owner wants π to see Bridge C's primes {2, 5, 7} and χ₁₄₀; that would be a new datum, not a derivation.

## I6. LD-O3b — meaning of "Λ(s, π_𝔸)" (computed for π = 1; for χ ≠ 1 see a-2)

**b-1 "standard".** Definition: Λ(s, π) := the completed L-function of the 48-dim standard representation of SO₄₈(ℂ).
- [PROVED] (given a-1; cited d2d2d226 item 6, re-checked in log c2) Λ = ξ(s)²∏_{i=1}^{23} ξ(s−i)ξ(s+i). Λ(1−s) = Λ(s). The poles are exactly s ∈ {−23, …, 24}, of total order 96, with orders 1, 3, 3, 1 at s = −23, 0, 1, 24.

**b-2 "adjoint".** Definition: Λ(s, π) := the completed adjoint L-function (dim so(48) = 1128).
- [PROVED] (given a-1; Kostant's principal-SL₂ decomposition cited) Ad|_{SL₂} = ⊕_e Sym^{2e} over the exponents e of D₂₄, namely {1, 3, …, 45} ∪ {23}. Hence Λ(s, 1, Ad) = ∏_e ∏_{j=−e}^{e} ξ(s+j). The degree check Σ(2e+1) = 1128 = dim so(48) holds (log c2).
- [PROVED] The functional equation Λ(1−s) = Λ(s) holds, since the shift multiset is symmetric. The poles lie in {−45, …, 46}, of total order 2256, with order 48 at s = 0 and at s = 1 (log c2; ξ has no zeros at real integers, so nothing cancels).

**b-3 "degree one".** Definition: since π = χ∘θ is a character, Λ(s, π) := Λ(s, χ), the Hecke L-function of χ.
- [PROVED] For π = 1, Λ = ξ(s), with Λ(1−s) = Λ(s) and simple poles at 0 and 1.
- [PROVED] b-3 forgets the Satake datum: it is the same for every split SO_{2n}, so it cannot see y_i = 23^{24−i}. This is a fact about the definition.

**Recommendation: b-1.** Reason: "Λ(s, π)" for a classical group conventionally means the standard L-function. It keeps the Codex's 23^{24−i} pattern visible as the shifts ±i, and it is the reading d2d2d226 already used.

## I7. LD-O3c — normalisation of ω₂₃ (Codex contour = 2∏_{i=1}^{23}(23^i+1))

**c-1 "all maximal isotropics".** Definition: ω₂₃^{−1} := #OG(24,48)(𝔽₂₃), the number of maximal totally singular subspaces of (V/23V, B̄), both families.
- [PROVED] #OG(n,2n)(𝔽_q) = ∏_{i=0}^{n−1}(q^i + 1). Brute force matches for (n,q) = (1,3), (2,3), (2,5), (3,3), (2,7) (log c2). At (24, 23) this equals the Codex contour exactly (377 digits, log c2).

**c-2 "one family".** Definition: ω₂₃^{−1} := the number of maximal totally singular subspaces in one SO-orbit = ∏_{i=1}^{23}(23^i + 1).
- [PROVED] The Codex contour equals 2·ω₂₃^{−1} exactly (log c2). The factor 2 = [O : SO] would have to be supplied by the Codex convention.

**c-3 "canonical local volume".** Definition: ω₂₃ := vol(K₂₃) = |SO₄₈(𝔽₂₃)|·23^{−dim} = (1 − 23^{−24})∏_{i=1}^{23}(1 − 23^{−2i}).
- [REF] As the Codex normalisation: 1/vol ≈ 1.0019 and 1/(2·vol) ≈ 0.5009, neither equal to the 377-digit contour (exact rational comparison, log c2). The Siegel-density reading was already REFUTED (d2d2d226 item 7) and is not recounted.

**Recommendation: c-1.** Reason: it reproduces the Codex contour exactly with no extra factor, and it is the reading d2d2d226 already proposed.

## I8. α for O4 — the "α preserves B" check (T_i = Σ_k α_ik R_{p_k}, p_k ∈ K90 = {3,11,37,41,47,53,61,71,79,83,89}; B = LD-1 form, B(g,h) = 1 iff h ≡ −g mod 140)
General lemma, used by all candidates:
- [PROVED] For t = Σ_k α_k p_k ∈ ℝ[A] and T = R_t: B(Tx, Ty) = B(tt*·x, y), where t* = Σα_k p_k^{−1}. So T preserves B iff tt* = 1, iff λ(χ)·λ(χ̄) = 1 for all χ, iff |λ(χ)| = 1 for all χ (α real). Proof: B(x,y) = ε(x z y*), with A abelian and z* = z. Numerical identity check: residual 1.8e−15 (log c3). B is nondegenerate (det 1), which gives the "iff".

**α-1 "single prime".** Definition: α_ik := δ_{k,σ(i)} for a map σ: {1..M} → {1..11}, i.e. T_i = R_{p_σ(i)}.
- [PROVED] Each T_i preserves B, exactly (log c3: R_p^T B R_p = B for all 11 p).
- [PROVED] JT_iJ = −T_i (parity, cited Addendum L). P = T_M⋯T_1 = R_{∏p} is invertible (rank 48).

**α-2 "integral".** Definition: α_ik ∈ ℤ.
- [PROVED] T_i preserves B iff α_i = ±(unit vector), i.e. T_i = ±R_p. Proof: the identity coefficient of tt* is Σ_k α_k², and it must be 1. So α-2 ∩ (B-preserving) = α-1 up to sign.

**α-3 "real B-orthogonal convolutions".** Definition: α_i ∈ ℝ^{11} with t_i t_i* = 1.
- [PROVED] (exact counterexample to "only α-1 preserves B over ℚ") α = ½(R₃ + R₃₇ + R₄₇ − R₅₃) preserves B. Exact Fraction check on all 48×48 basis pairs (log c3d). There are 48 such ±½ four-term solutions, on 6 supports.
- [OPEN] A full classification of real solutions supported on K90. Numerics (log c3) find candidate solutions of support 3–9, but these are not certified; c3c's symbolic recognition step was unreliable and is not used.

**α-4 "uniform".** Definition: α_ik := 1 for all k (the "entry nonzero iff match" reading).
- [REF] T = ΣR_p does not preserve B: the identity coefficient is Σα² = 11 ≠ 1. It is not even a similitude, since UᵀBU ≠ c·B (log c3, exact integer matrices). (rank U = 48.)

**Recommendation: α-1.** Reason: it is exactly B-preserving, it is the unique integral B-preserving choice (α-2), and it keeps the Addendum L parity. α-3 is the right generalisation if the Owner wants real weights; α-4 is refuted. B-preservation does not involve C0 or C_M; the boundary kernel stays OPEN under all candidates.

## I9. O5 — the Hamiltonian H for ι (ac1dd4e2 is CONDITIONAL on "H free Dirac / n_H ∈ {0, ∞}")
Operator-theoretic definitions only.

**O5-1 "free massive Dirac".** Definition: H := α·p + βm on L²(ℝ³)⊗ℂ⁴, with m > 0 and D(H) = H¹.
- [PROVED] (cited ac1dd4e2 items 3–5) H is absolutely continuous on (−∞, −m] ∪ [m, ∞) with uniform multiplicity ∞, and LD-O5 gives an explicit unitary ι with ιH = (H⊗1₂)ι. The Foldy–Wouthuysen step was re-checked (log c4b, err ≤ 1.8e−15, Dirac and Majorana representations).
- [PROVED] In the Majorana representation, AHA⁻¹ = −H. Proof: α_k = γ⁰γ^k is real and β is imaginary, so γ⁰ conj(H(p)) γ⁰⁻¹ = −H(p). Log c4b: residual 0. In the Dirac representation it fails (residual ≈ 6).

**O5-2 "free massless Dirac".** Definition: as O5-1 with m = 0.
- [PROVED] The spectrum is ℝ, absolutely continuous, with multiplicity ∞. U_FW is defined for p ≠ 0, a null set, so ι exists as in O5-1. Majorana anticommutation holds (log c4b, m = 0 rows).

**O5-3 "with a bound state".** Definition: H := H_D + V with V bounded and symmetric such that H has an isolated eigenvalue of finite multiplicity.
- [REF] (cited ac1dd4e2 item 2) No unitary ι with ιH = (H⊗1₂)ι exists. A k-dimensional eigenspace would have to map onto a 2k-dimensional one.
- [REF] For a real scalar V with V(−x) = V(x): A(H_D+V)A⁻¹ = −H_D + V ≠ −(H_D + V) unless V = 0. Proof: A acts by γ⁰(·)*Π, so it fixes such a V. So the Option M energy inversion fails.

**Recommendation: O5-1.** Reason: it is the setting of 4b25d2ed, NL B and ac1dd4e2, and every Local claim holds there unconditionally. O5-2 is equally valid if the Owner wants m = 0, and O5-3 breaks both ι and the inversion. Choosing H is the Owner's (physical) decision; this file only states the mathematics.

## R. Rollup (graded claims in §I1–I9; cited carries included and marked "(cited)")
- **PROVED 42 · CONDITIONAL 4 · OPEN 7 · REFUTED 7.**
- **New Local-derived PROVED in this file** (not carried): Oc-1 squarefree-35 uniqueness; Oc-2 twist invariance of T(p²); V-1 representation, slash triviality and no-constraint consequence; J-2 inclusion and minimal level 19600; J-3 isomorphism over K, the L-factorisation check, the conductor and root number; H-2 square; LD-O3a χ₁₄₀/χ₋₇ candidates and the full candidate set; LD-O3b adjoint degree, functional equation and poles, b-3 facts; LD-O3c brute-force formula check and the one-family identity; the α lemma, α-2, and the exact α-3 counterexample; O5 Majorana anticommutation re-check.
- **New REFUTED:** V-3 (from cited R26), H-3 odd-d square (proof), c-3 Codex normalisation (exact comparison), α-4 (exact), O5-3 inversion with an even scalar V (proof). Carried REFUTED: H-3 rank (4b25d2ed), O5-3 ι (ac1dd4e2).
- **Not covered here (Local work items under t4407, not Owner decisions):** O-a, O-b, 4a interval hardening, 2/5-parts formulation. Their status is unchanged from 9e34f2dc.
- Bridge C stays **PARTIAL**. Nothing adopted.

## E. Evidence (evidence_local_owner_candidates_2026-11-09/; each file has a .sha256 sidecar)
| File | sha256 |
|---|---|
| c1_joint_carrier_weil_restriction.log | 90c47205a19e16442713d00e1aa36882187b9b62893e77ada7fe96ca3b31e7e6 |
| c1_joint_carrier_weil_restriction.py | a4919891181d41d761982993f97c08e088af93568bd2a6f8223d6cf60839df7c |
| c2_O3_candidates.log | e53026075a7342819c150fd59890afdd6e19b3eb8b9984d3b2d59dfb92488240 |
| c2_O3_candidates.py | 19a43fc4c3e13ceaa9a31f175a34eb9e5c60d68b9eab9013b2d02572ff8d1ef4 |
| c3_alpha_O4_candidates.log | a523fad687e38ce671ba7d0cf60b90a8b40ec67886fd329418bd3cb9fdf9de2c |
| c3_alpha_O4_candidates.py | b5ef3a42203f8de0daedfd9b4741edbc545333df887e1640a543f7955bd99fe5 |
| c3b_alpha_exact_nonmonomial.log | 321a64259c4f65f1fd5f67f74b13e90670342f443c0acdbfdcf79e02a51b0b40 |
| c3b_alpha_exact_nonmonomial.py | 9d6e7b8c1d971c9bb275d0ff967f08c8dc88bf9e753b51a4e916a2f9da252197 |
| c3c_alpha_inspect_solutions.log | 632d42bc1c3e6e997c4d6d2ed615337709a202615ec02bb94bce72089990754e |
| c3c_alpha_inspect_solutions.py | 58cc990c94fb3fd20c84573cb6a48da25e2fc1703816daca0476c48435c6ce22 |
| c3d_alpha_exact_half_solutions.log | b39d1f35e7a41dd3ceb11a2494195f462aa509d34f9760d3d9f914800d11ce8d |
| c3d_alpha_exact_half_solutions.py | 6afd18e69ef774aad0f8b78b35cf90221ea96ce8fb6933b9a4218582addb01ad |
| c4_O5_Hplus_candidates.log | a1138d2ac8a4fc622de0dcff8c15dff0bf46c02809dedcae1c6222de5978c03d |
| c4_O5_Hplus_candidates.py | a93655b72e83a3a84e80cce08c90a96b7469b4d718d5e86d9f02c8144dbbd753 |
| c4b_O5_Hplus_candidates_majorana_fixed.log | 38249a0afb2a3d39f3bb8d19372be6c8d80b7661e84584ebe82a57a9f829e168 |
| c4b_O5_Hplus_candidates_majorana_fixed.py | e9b298c8042e123269238692802ebed9fa064a742b45e1acbce23a1de57032d6 |

Custody notes on evidence (all files kept on disk; nothing deleted or overwritten):
- c4_O5_Hplus_candidates.{py,log} is **SUPERSEDED** by c4b_…majorana_fixed. Its hand-typed "Majorana" set was not a Clifford representation (its own log shows Clifford err 4.0), so its Majorana rows are void. Its Dirac rows agree with c4b.
- c3b_alpha_exact_nonmonomial found no full-support three-term solution. That is a null result, kept as is.
- c3c_alpha_inspect_solutions: the numerics are kept as evidence only. Its sympy "exact-recognised" count (30) is unreliable (nsimplify rounding) and is **not used**. The exact result is c3d.
- c1 log: "primes 3..400" means the first 400 primes excluding 2, 5, 7.
- This file was written by gen_findings_t4407.py (same directory, with sidecar), which refuses to overwrite.

Local-derived. For PP audit. Nothing adopted; the Owner chooses. Tip 7cddb188 untouched. No CERT. Nothing sent outside.
