# FINDINGS — Local Path DERIVE: B2 construction A — P_rev on H₊ ⊕ H₋ via an explicit isometry ι — 2026-11-09

- Lane: Local Path. Written Nov 9, 2026 (~1:20 PM CST, America/Chicago) under Owner DIRECT (Physicist transcript pos 17629, cu:405590937, ~1:06 PM CST). Additive new file. No CERT. Tip 7cddb188… untouched (read-only). Nothing sent outside. Derived independently of NL's construction-B/A files (not read before this file was written).
- Pure math. Small numpy fibre checks only (no files kept).

## 0. Sources (Owner-Written vs derived)
- **Owner-Written DEF1** (Zenodo 18442276, relayed; quoted in reports/NL_OWNER_DEFS_PREV_TEH_FORMAL_CHECK_2026-11-09_1232.md:6,8): P_rev = γ⁰KΠ (K complex conjugation, Π: x↦−x), mapping H_{+U} → H_{−U} = H_{+U}⊗ℂ². No embedding of γ⁰ψ*(−x) into the ℂ² factor is given (ibid. :8).
- **B2 as stated** (reports/GEMINI_ROUND_QUESTIONS_2026-11-09_1238.md:13): "P_rev maps H_{+U} into H_{−U} = H_{+U}⊗ℂ², so P_rev² is undefined. Standard way: direct sum H₊⊕H₋, or a fixed embedding ι?" Related: B1 (:12) P_rev² = γ⁰γ⁰* (= −1 only in Majorana rep); B3 (:14) P_rev H P_rev⁻¹ = −H (Majorana).
- PP audit reports/FINDINGS_PP_SOFTSF_AUDIT_NL_K3S2_BLOCK_SOURCES_PREV_EMBEDDING_2026-11-09_1304.md:25–38: B2 CONDITIONAL on ι; literal H₋ = H₊⊗ℂ² has rank 2r (:33).
- NL proposal reports/NL_DERIVED_PROPOSAL_K3S2_BLOCK_SOURCES_AND_PREV_EMBEDDING_2026-11-09_1310.md:24–33 (Options M, D on 𝓗 = H⊗ℂ²).
- **Local-derived reading LR-0:** H₊ := L²(ℝ³)⊗ℂ⁴ (Dirac spinors; Owner's exact H_{+U}, incl. any "35-component" structure, is OPEN), H₋ := H₊⊗ℂ² (literal), A := γ⁰KΠ antiunitary on H₊, η := A² = γ⁰γ⁰* ∈ {±1} (η=−1 Majorana, +1 Dirac/chiral; PP 1245 item 1). Free Dirac H = α·p + βm on H₊; on H₋ the Hamiltonian is H⊗1₂ (as in NL :30), on the sum H_tot := H ⊕ (H⊗1₂).
- Fact used: in momentum space A acts fibrewise as ψ̃(p) ↦ γ⁰·conj ψ̃(p) (Fourier of ψ*(−x)), so all fibre identities can be checked at fixed p.

## 1. Local-derived definitions
- **LD-A1 (partial form).** For a linear isometry ι: H₊→H₋ (ι*ι = 1), Q_ι := [[0, Aι*],[ιA, 0]] on H₊⊕H₋ (antilinear). Owner's map is recovered: Q_ι|_{H₊} = ι∘P_rev.
- **LD-A2 (literal local ι).** ι_e(ψ) := ψ⊗e for a unit e∈ℂ² (take e = e₁).
- **LD-A3 (complement fix).** With R := H₋ ⊖ ιH₊ and an antiunitary J on R with J² = η: Q_{ι,J} := Q_ι on H₊⊕ιH₊, ⊕ J on R. For ι = ι_{e₁}, R = H₊⊗e₂ and J(φ⊗e₂) := Aφ⊗e₂; equivalently on H₊⊕H₋ ≅ H₊⊗ℂ³: Q_{ι,J} = A⊗(S∘K₃), S = permutation (1 2) fixing the 3rd basis vector.
- **LD-A4 (infinite-dim unitary ι).** U: H₊→H₋ unitary (exists: both separable ∞-dim). Explicit interleaving: for an ONB (f_n)_{n≥0} of H₊ (e.g. Hermite functions ⊗ spinor basis), U f_{2n} := f_n⊗e₁, U f_{2n+1} := f_n⊗e₂. Q_U := [[0, AU*],[UA, 0]].

## 2. Results
1. **PROVED — partial form.** Q_ι² = η·diag(1_{H₊}, ιι*), where ιι* is the projection onto ιH₊. Q_ι is antilinear, isometric on H₊ ⊕ ιH₊, zero on 0⊕R (partial antiunitary). (BC = Aι*ιA = A² = η; CB = ιA·Aι* = η ιι*.) Numpy fibre check (4+8 dims, Majorana): Q² = −diag(1,P), rank 8 of 12. Q_ι² = ±1 ⇔ ιι* = 1 ⇔ ι unitary.
2. **PROVED — finite-dimensional obstruction (any anti-diagonal form).** If Q = [[0,B],[C,0]] with B, C (anti)linear and Q² = ε·1, then BC = ε1_{H₊}, CB = ε1_{H₋}, so C is bijective and dim H₊ = dim H₋. With dim H₋ = 2·dim H₊ < ∞ this is impossible. **REFUTED** (by this proof): "an anti-diagonal, sector-swapping P_rev with P_rev² = ±1 exists on the literal finite-dim H₊⊕(H₊⊗ℂ²)." Cokernel of any isometry ι: R = H₋⊖ιH₊ with dim R = dim H₊.
3. **PROVED — complement fix (LD-A3), any dimension, x-local.** Q_{ι,J} is antiunitary on all of H₊⊕H₋, Q_{ι,J}² = η·1, and Q_{ι,J}(H₊) = ιH₊ ⊂ H₋ (maps H₊ into H₋ as the Owner requires), but does not map H₋ into H₊ (R is mapped to itself). For ι_{e₁}: Q = A⊗(S K₃), Q² = A²⊗SS̄ = η. Q H_tot Q⁻¹ = (AHA⁻¹)⊗1₃ = −H_tot iff AHA⁻¹ = −H, i.e. in the Majorana rep (PROVED there, NL 1232 item 3; fails in Dirac rep). Numpy check (Majorana, random p, m): Q² = −1, QH_totQ⁻¹ = −H_tot, Q unitary-antilinear.
4. **PROVED — no D-type Kramers sign from a tensor complement.** A tensor-form Q = A⊗(VK₃) on H₊⊗ℂ³ has Q² = η·VV̄; VV̄ = −1 on ℂ³ is impossible (|det V|² = det(VV̄) = (−1)³). So in the Dirac rep (η=+1) a tensor-form complement always gives Q² = +1. (A non-tensor J with J² = −1 on R exists, since R ≅ L²⊗ℂ⁴ is even/∞-dim, but it is not built from P_rev; OPEN whether the Owner wants that.)
5. **PROVED — infinite-dim unitary ι (LD-A4).** Q_U is antiunitary on H₊⊕H₋, swaps the sectors, Q_U² = η·1. So the literal reading admits a genuine involutive (η=+1) / Kramers (η=−1) sector swap in infinite dimension.
6. **PROVED — every unitary ι is non-local.** If ι commutes with all multiplication operators M_f (f∈L^∞(ℝ³)), ι is decomposable, ι = ∫⊕ ι(x) with ι(x): ℂ⁴→ℂ⁸ isometric a.e. (commutant of L^∞ = decomposable operators), hence never surjective; so a unitary ι cannot be x-local. The interleaving U of LD-A4 mixes positions.
7. **PROVED (existence) / OPEN (explicit) — energy inversion with unitary ι.** Q_U H_tot Q_U⁻¹ = −H_tot iff (with AHA⁻¹ = −H, Majorana) U H U* = H⊗1₂. Such U exists: by Foldy–Wouthuysen, H ≅ diag(+E(p)·1₂, −E(p)·1₂), E = √(p²+m²), whose spectral measure on (−∞,−m]∪[m,∞) is absolutely continuous with uniform infinite multiplicity; H⊗1₂ has the same spectrum and multiplicity, so H ≅ H⊗1₂ (Hahn–Hellinger). The Hermite interleaving of LD-A4 does **not** generally intertwine H (no claim); an explicit intertwiner is OPEN.
8. **What B2 requires and which version meets it.** B2 (GEMINI_ROUND_QUESTIONS :13) asks for a well-defined operator for which P_rev² makes sense; B1/B3 add P_rev² = −1 and P_rev H P_rev⁻¹ = −H.
   - LD-A1 (partial): defines P_rev² but only as η·diag(1, ιι*) — meets "defined", not "= ±1". PROVED.
   - LD-A3 (complement, local ι_{e₁}): Q² = η·1 on the literal H₊⊕(H₊⊗ℂ²), maps H₊→H₋, x-local; with Majorana rep also Q² = −1 and anti-commutes with H_tot. Meets B2 + B1 + B3 in the Majorana rep. PROVED; adoption CONDITIONAL on the Owner accepting that P_rev acts on R by J = A (not a pure swap).
   - LD-A4 (unitary ι): meets B2 (pure swap, Q² = η) at the cost of non-locality (6); B3 additionally needs an intertwining U (7). PROVED existence; adoption CONDITIONAL.
   - B2 is **not closed** here: which version (and representation) is the definition remains the Owner's choice. CONDITIONAL.

## 3. Preliminary comparison with NL Options M and D (definitions level; NL B not yet read)
- NL (proposal :27–31) re-reads H₋ as H⊗e₂ inside 𝓗 = H⊗ℂ² (equal rank), P̂ = A⊗(U K₂). Local's LD-A3 restricted to H₊⊕ιH₊ (≅ H⊗ℂ² via ψ↦ψ⊗e₀, ιψ = ψ⊗e₁) is A⊗(σ_x K₂) — **identical to Option M** (same rep, U = σ_x). Hence: LD-A3 = Option M ⊕ (A on the extra copy R). PROVED.
- Option D (Dirac rep, U = iσ_y, Q² = −1 from UŪ = −1): Local's tensor constructions in the Dirac rep give Q² = +1 (result 4), so LD-A3(Dirac) and Option D are **inequivalent** (different squares). PROVED.
- Bare antiunitaries with square −1 on separable ∞-dim spaces are all unitarily equivalent (quaternionic structure unique up to unitary), so M and D are equivalent as bare operators; as pairs (Q, H_tot) they are inequivalent, since QHQ⁻¹ = −H is invariant under joint conjugation and holds for M but not D. PROVED.
- LD-A4 vs M: same algebraic form (anti-diagonal, Q² = η) but on the literal 1:2-rank spaces, possible only in infinite dimension and only with non-local ι; unitarily equivalent to M ⊗ (identification U) as bare operators when η = −1. Equivalence with the dynamics is CONDITIONAL on U intertwining H (result 7).
- Preliminary until NL files construction B; to be cross-checked.

## 4. Rollup
PROVED 9 (results 1, 2, 3, 4, 5, 6, 7-existence, comparison M-identity, M/D bare-vs-pair) · CONDITIONAL 2 (adoption of A3 / A4 as P_rev; B2 status) · OPEN 3 (Owner's exact H_{+U}; non-tensor Kramers J in Dirac rep; explicit intertwining U) · REFUTED 1 (anti-diagonal involutive P_rev on the literal finite-dim sum). No CERT. Tip untouched. B2 not closed.
