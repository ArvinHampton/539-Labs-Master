# FINDINGS — PP AUDIT of NL F2 (O6 + O9 + O10): "P_rev acts on the −U sector only" — 2026-11-09 ~15:30 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Additive new file; nothing edited or renamed. Tip 7cddb188… untouched. No CERT. Nothing sent outside. No Gemini.
Authority: OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c (sidecar MATCH), GO (2). Adopted B2 closure: RECORD 09498bf7 / RECORD_PP_B2_ADOPTION_B_M_VERIFIED (OW 68a2b8e1), (B)-M: P̂ = (γ⁰Π⊗U)K on H⊗ℂ², Majorana rep, U = e^{iθ}σ_x, P̂² = −1 a chosen input. LOCK 96f8d42e §4 honored (no purged mapping used).
Scratch: /workspace/audit-scratch/pp_nl_f1f2_1525/ — f2_check.py 2143e491… · f2_check.log 4f9f4828… (numpy; 4³ periodic lattice, dim H = 256; my own Majorana basis γ⁰ = σ₂⊗σ₁, γ¹ = iσ₁⊗1, γ² = iσ₃⊗1, γ³ = iσ₂⊗σ₂, Clifford and pure-imaginary checked; m = 0.7; antilinear maps as M∘K).

## 0. Target verification
| item | expected | on disk | sidecar |
|---|---|---|---|
| NL_DERIVED_F2_PREV_ON_MINUS_U_SECTOR_ONLY_O6_O9_O10_2026-11-09_1528.md | e9bdd871 | e9bdd871a04ddec2e56c99e58bad3f2d50d6172c0f4dd4b05c6a95ed13569ab7 | MATCH |
| /workspace/nl-1511/f2_prev_minusU.py | d73bcb25 | d73bcb2589ec7bf2… | MATCH (prefix) |
| /workspace/nl-1511/f2_prev_minusU.log | 71c4bf50 | 71c4bf508e8da5e3… | MATCH (prefix) |
| cited PP f9522377, 0c3b2b91; NL c915f391; RECORD 09498bf7 | — | all located by sha prefix | — |
- Filename: NL states "1528" is a misnomer (file mtime 15:21 CST). Recorded as is; **not renamed**.

## 1. Formalization and reading (c)
- **(c) not linear/antilinear — PROVED, CONFIRM.** (1⊕A₀)(iψ, iχ) = (iψ, −iA₀χ); lattice: neither i·(…) nor −i·(…).
- Wigner / ±U superselection: CONDITIONAL — CONFIRM (block-diagonal H_tot makes such a rule dynamically consistent; adopting it is the Owner's call).

## 2. R1–R4 on H₋
- **R1 P₋² = −1 — PROVED, CONFIRM.** P₋ = A₀ = γ⁰ΠK; A₀² = γ⁰(γ⁰)* = −(γ⁰)² = −1 since γ⁰ is imaginary. Lattice: MM̄ = −1 exactly.
- **R2 P₋HP₋⁻¹ = −H — PROVED, CONFIRM.** Algebra: KΠ fixes p (both flip it) and the real αʲ, and flips β = γ⁰ (imaginary); then γ⁰ flips αʲ and fixes β, so A₀(α·p + βm)A₀⁻¹ = −α·p − βm. Lattice exact; spectrum = −(reversed spectrum).
- **R3 "P₋ forces Kramers degeneracy" REFUTED — CONFIRM.** CE1 (iσ_yK, σ_z) verified: P² = −1, PHP⁻¹ = −H, simple levels. CE2 verified independently (my basis, my random W): A₀H_pA₀⁻¹ = −H_p, all 256 eigenvalues simple (min spacing 0.0123). E = 0 case PROVED — CONFIRM (ker H is A₀-invariant, A₀ is a quaternionic structure there; lattice: zeroing three ± pairs gives dim ker = 6, even). Free H_D multiplicities 16 and 48, |E|min = m — reproduced.
- **R3 classification "class C" — PROVED only as scoped; QUALIFY.**
  - P₋ is **antiunitary** (contains K) and **anticommutes** with H, so it is particle-hole type, not chiral (a chiral symmetry is unitary and anticommuting). With C² = −1 and no other symmetry imposed, the symmetry class is C. This is correct **in the 0-dimensional / matrix-ensemble sense** (Hamiltonians on H₋ required only to anticommute with P₋).
  - Two limits NL does not state: (i) P₋ contains Π (x ↦ −x), so it is **not an internal (on-site) symmetry**; the Altland–Zirnbauer tenfold way for d-dimensional band topology refers to internal symmetries, so a d-dimensional topological "class C" reading is **OPEN** (it is an inversion-type PHS). (ii) The free H_D itself has further local symmetries (lattice-verified in this Majorana basis): K alone (antiunitary, anticommuting, K² = +1), T = γ¹γ²γ³K (antiunitary, commuting, T² = −1) and the unitary chiral γ¹γ²γ³ (anticommuting). By its internal symmetries, free H_D is in **class DIII**, not C. NL's wording "with nothing else imposed" is the needed scope; the statement must not be read as "H_D is class C".
- **R4 — PROVED (by construction), CONFIRM.** H_{+U}: OPEN — CONFIRM.

## 3. Reconciliation with adopted (B)-M (K1–K4, T1–T3)
- **K1, K2 — PROVED, CONFIRM.** Lattice (dim 512): [S, H_tot] = 0; P̂² = −1; S·P̂ = A₀⊗1₂ exactly; the H₋ block of S·P̂ is A₀ and the off-block is 0.
  - Note (PROVED): NL sets θ = 0 silently. For U = e^{iθ}σ_x, P̂_θ = e^{iθ/2}P̂₀e^{−iθ/2} (lattice-verified), S·P̂_θ = e^{iθ}A₀⊗1₂, and P₋ = e^{iθ}A₀ still has square −1 and anticommutes with H. So K1–K4 and T1–T3 hold for every θ.
- **K3 "P̂ acts within H₋" — REFUTED by proof, CONFIRM.** P̂(H⊗e₂) = H⊗e₁. Lattice: Π₋P̂Π₋ = 0. The proof is valid, and the refutation targets only the literal reading.
- **K4 — PROVED (trivial), CONFIRM.**
- **Tension — OPEN, CONFIRM, with one precision.** The Owner's 1:18 PM verbatim text ("Adopt B2 closure (B)-M, the Majorana pure swap on H⊗ℂ²…") does not itself contain the symbol "P_rev". The identification P_rev = P̂ comes from the B2 context (PP 0c3b2b91 uses P_rev for the closure). The tension with O6 is still genuine.
- **T1/T2/T3 — CONFIRM.** T1: P₋ = (S·P̂)|_{H₋} keeps P² = −1 and anticommutation (PROVED). T2: X = P̂Π₋ maps H₋ → H₊ and sends E to −E, but X² = P̂(Π₋P̂Π₋) = 0 (lattice: 0), so P² = −1 is lost (PROVED). T3 gives the same operator on H₋ as T1 (PROVED). The only difference between T1 and T3 is whether P̂ keeps the name P_rev. Choosing a reading is the Owner's call: OPEN.
- **Consistency with (B)-M: MATCH.** F2 changes nothing in RECORD 09498bf7. P̂² = −1 is still a chosen input, the Majorana rep is used, and P₋ is derived from P̂ by the commuting involution S.

## 4. O9
- **Lemma Q² = η·VV̄; VV̄ = −1_n iff n even — PROVED, CONFIRM.** Also (PROVED): if Q² is a scalar c, then VV̄ = c and conjugating gives c real, so c = ±1. Random check: min‖VV̄ + 1‖ = 2.0 for n = 1 and 3; iσ_y gives exactly −1.
- **"Majorana forced under O9" — PROVED as a statement, attribution CORRECTED.**
  - At n = 1, O9's tensor-form condition is vacuous: every antiunitary on H⊗ℂe₂ is A₀'⊗(phase·K₁).
  - What forces η = −1 is requiring P₋ = γ⁰ΠK_B with P₋² = −1. Then γ⁰(γ⁰)^{*B} = −1, which happens when γ⁰ is imaginary in the K-basis (Majorana). In Dirac or chiral bases γ⁰ is real and the square is +1 (lattice: Dirac γ⁰γ⁰* = +1). Fixed-t symmetry forces the same thing (PP 0c3b2b91, line 113).
  - So the conclusion holds, but O9 does no work in it.
- **n = 3 bullet — CONFIRM, read with "Kramers complement" meaning a factor V with VV̄ = −1.** In the Majorana rep, Local A3 = A₀⊗(S∘K₃) still has Q² = η = −1 (RECORD 09498bf7, item 3). NL restricts its "stays +1" to Dirac and chiral, so the bullet is correct.
- **n = 2 (Option D is tensor-form, not excluded by O9, not adopted) — CONFIRM.** OPEN-3 settled by Owner choice: CONDITIONAL, CONFIRM.

## 5. O10 (−Z rule)
- **Z1 — PROVED, CONFIRM.**
- **Z2 — PROVED, CONFIRM.** Lattice with random real φ and A: A₀(H_D + eφ − eα·A)A₀⁻¹ = −(H_D − eφ∘Π − eα·(A∘Π)) exactly. Independent support: K alone anticommutes with free H_D in the Majorana basis (local C, K² = +1), so A₀ contains the C content.
- **Z3 — PROVED for Zα < √3/2.** Here H_e is essentially self-adjoint on C_c^∞(ℝ³∖{0})⁴, which A₀ preserves, so the closures correspond and σ(H[−Z]) = −σ(H[Z]). For √3/2 ≤ Zα < 1 it is CONDITIONAL on the cited distinguished-extension theory. NL's blanket "PROVED (Zα < 1)" should be split this way (minor).
- **Z4 — REFUTED by counterexample, CONFIRM.** −117 ≠ −236. The affine-uniqueness remark (b = 0 from additivity, a = −1 from Z2) is PROVED given Z2.
- **Z5 — relabel CONDITIONAL.** It rests on an external source (Zenodo 17926999) "PROVED by reading", and under the audit rules a citation is CONDITIONAL.
- Physical readings: OPEN, CONFIRM.

## 6. Tally (counted by PP)
- NL's header says "PROVED 13", but its own list names **15** PROVED items: (c), R1, R2, R3-E=0, R3-class C, R4, K1, K2, K4, O9 lemma, Majorana-forced, Z1, Z2, Z3, Z5.
- NL's parenthetical (merge Z2/Z3/Z5 into Z1) would give **12**, not 13. No stated counting rule yields 13. **Discrepancy confirmed: the strict count is 15.**
- CONDITIONAL 3, OPEN 3, REFUTED 3 as listed: MATCH.
- PP regrade of NL's items: **PROVED 14 · CONDITIONAL 4 · OPEN 4 · REFUTED 3.**
  - Z5 moves to CONDITIONAL.
  - Z3 counts as PROVED for Zα < √3/2.
  - Class C stays PROVED in the 0D sense, and its d-dimensional topological reading is added as OPEN.

## Errors found (all minor; none overturns a verdict)
- E1: tally 13 vs 15 (above).
- E2: Z5 is a citation and should be CONDITIONAL.
- E3: "class C" needs its scope stated: 0D/ensemble, P₋ alone. P₋ is non-internal (contains Π), and free H_D is internally DIII.
- E4: "Majorana forced under O9" is attributed wrongly. O9 is vacuous at n = 1; the K-basis plus P₋² = −1 (or fixed-t symmetry) does the forcing.
- E5: Z3 needs the Zα range split.
- E6: θ = 0 is implicit; harmless, since the phase can be conjugated away.
- No PROVED label was found false.

## Rollup (this audit)
- **PROVED 17:** confirmations of (c), R1, R2, R3-E=0, class C (0D), R4, K1, K2, K4, T1, T2, T3, the θ-independence note, the O9 lemma with the scalar-square extension, Majorana-forced (corrected attribution), Z1/Z2 and the affine remark, Z3 (Zα < √3/2).
- **CONDITIONAL 4:** reading (c)/superselection; O6/O9/O10 as model statements (OW 5a6e7177); Z3 for √3/2 ≤ Zα < 1; Z5.
- **OPEN 4:** the T1/T2/T3 choice; H_{+U}; the d-dimensional class reading of P₋; physical −U/−Z readings.
- **REFUTED 3 (confirmed):** Kramers forcing; K3 literal; Z4.

**Verdict: F2 is CORRECT in substance and consistent with the adopted (B)-M.** P₋² = −1 and P₋HP₋⁻¹ = −H hold on H₋. There is no Kramers degeneracy at E ≠ 0. P₋ is antiunitary, so it is a particle-hole symmetry and not a chiral one; "class C" holds only in the 0D sense for P₋ alone. The K3, Z4 and Kramers refutations are valid. Fixes needed: the tally (15, not 13), Z5 relabeled CONDITIONAL, and the scope of the class-C and Majorana-forced claims. The T1/T2/T3 choice stays with the Owner.
