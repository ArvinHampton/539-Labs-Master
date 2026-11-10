# ERRATUM / FINDINGS (Local-derived): additive erratum absorbing PP audit 670decbe of the 11:24 reverse-engineer-from-geometry filing 845cc6bc (with clerical erratum 286e4f02). 2026-11-10, written 11:43:13 CST (America/Chicago)

- **Label:** Local-derived. Additive dated write; **no existing file edited, moved, renamed or deleted**. Naming: resonant algebra. **Nothing adopted. Junction UNSOLVED. No CERT. Tip read-only.** No agent messages, no external sends.
- **Absorbs (authority for wording and grades; all grades UNADOPTED):** PP `FINDINGS_PP_AUDIT_LOCAL_REVERSE_ENGINEER_GEOMETRY_845cc6bc_2026-11-10_1139.md`, sha256 670decbe47f1aa33a7a5fd8e8635b2b737a62f774a6bf33d78bc5ff849e04bd5 (re-hashed 11:43 CST: sidecar MATCH; mode 444; PP header "written 11:39:10 CST").
- **Errs (not edited):** Local `FINDINGS_LOCAL_REVERSE_ENGINEER_GEOMETRY_TO_BRIDGE_C_ALGEBRA_2026-11-10_1124.md`, sha256 845cc6bc5f590e8f2e4e867ea56ed44eaafee941a8e8a37e313c0aa78c5bdd6b (sidecar MATCH), read together with clerical erratum `ERRATUM_LOCAL_REVERSE_ENGINEER_GEOMETRY_PRIME_LIST_2026-11-10_1124.md`, sha256 286e4f027716fa5c50b3b3d79af7dd6b0b7a3a1531f23d8d8d7f6c80880c002c (sidecar MATCH). PP **ACCEPTED** both erratum lists; they are not reopened here.
- **Context, read only:** OW 1117 method directive (bff79185…), OW 1130 pursue-open-items directive, t4436 (math leads; COND stays COND), PP 2030 citation rule (69d33456…), PP d37a456d and Local erratum 4e440c2b (PP-confirmed FAITHFUL in 05989aa3).
- **Scope:** this file re-reads the 11:24 package under the 11:39 PP audit only. It proves no new theorem and moves no PP-ruled grade.

## 0. Lead table: rows and PP-ruled grades (all UNADOPTED)

| Row | Statement (11:24 package, as re-read) | PP-ruled grade | Premise / tag carried |
|---|---|---|---|
| PL (R1d) | Lemma PL, parity lock, **sig even** | **PROVED** | textbook tag: Weil representation convention and representation property (Borcherds 1998 §4 / Bruinier LNM 1780 §1.1; Weil/Milgram) |
| JM (R3a, R3b ±1) | Lemma JM incl. J = ±1 on ℂe₀ | **PROVED** (elementary) | R3b needs P-J + P-fix + **J preserves ℂe₀**; application **OPEN** (P-J off disk); sign OPEN |
| R2 | N_M5 ≡ n_inst (mod 2) | **PROVED as implication of P-charge** | P-charge: Owner t4369 / f825dfff, N_M5 + n_inst = 2N_flux with N_M5, n_inst, N_flux ∈ ℤ |
| R4d | hyperelliptic ι = −1 on H¹(Σ) | **PROVED** | coefficients ℤ, ℚ, ℝ, ℂ, de Rham or étale ℚ_ℓ (not 𝔽₂) |
| R5b | Kronecker symbols at 23 | **PROVED** (exact); COMPATIBLE, not forcing | π away from 23 OPEN (LD-O3a) |
| R1b | W_Q reading of the ε_p sign table | **CONDITIONAL** | [w_p = ε_p]; AL multiplicativity. Sign table PROVED as values of ε_p (P7); selection OPEN |
| R4b | Jac(Bolza) CM field ℚ(√−2) | **CONDITIONAL** | [Jac(Bolza) ∼_{ℚ̄} E², E CM by ℤ[√−2]]; count **12** |
| R4a | no ℚ(√−7)-CM elliptic curve (incl. any twist of 49a1, incl. Ξ) is a ℚ̄-isogeny factor of Jac(C) | **CONDITIONAL** | [T-Deu, T-ST, T-Frob] |
| R4a-17 (exact sub-result, not a tally row) | Jac(C) has good, ordinary reduction at 17, P = (x²+6x+17)², irreducible-squared at every 𝔽_{17^f} | **PROVED** | PP v2 exact checks |
| R1c (lead-table scope split, not a new tally row) | Q = 19600 ("odd ⇒ Fricke −1") | **PROVED as implication of D_W** | uses adopted Fricke +1 (2d/E2) |
| R1c (cont.) | Q = 25, 784 contradictions; Q ∈ {16, 49, 400, 1225} and "odd ↦ ε = −1" compatibility rows | **CONDITIONAL** | [w_p = ε_p; Atkin–Lehner 1970 multiplicativity] |
| D_W, D_Z | the dictionaries themselves | **OPEN** | not on disk |
| R1d CONTRADICTS | odd G₄ ↦ ρ(−I) = −1 on e₀ | **PROVED as implication of D_Z** | PL (sig 0); independently 4a at γ = −I |

**Ruled tally of the 11:24 new statements (PP):** PROVED 5 / CONDITIONAL 3 / REFUTED 0; OPEN list unchanged (D_W, D_Z, P-J and so the JM application, R1b selection, L1-app, R2′, R4c, R5 π away from 23, R8 rows). No Owner or PP record is regraded. **Bridge C stays PARTIAL; standing tallies unchanged** (Bridge C 49/10/5/2/1 + V₈₄; t4436 65/15/5/9/2; d37a456d 5/0/3/0). Clerical erratum 286e4f02 **ACCEPTED**. The 11:24 file's "PROVED 6 / CONDITIONAL 2" is superseded by this ruling.

## 1. Priority fixes, absorbed wording

**F1 (R4a exact).** The 11:24 §4 sentence "Its trace −12 ≢ 0 (mod 17), so Jac(C) mod 17 is ordinary" is replaced by: *For an abelian surface, trace ≢ 0 (mod p) gives only p-rank ≥ 1. The genus-2 criterion is: ordinary (p-rank 2) iff the x² coefficient a₂ of the Frobenius characteristic polynomial is ≢ 0 (mod p). Here P(x) = (x²+6x+17)² = x⁴+12x³+70x²+204x+289, so a₂ = 70 ≡ 2 (mod 17) ≢ 0: ordinary. Equivalently, x²+6x+17 has exactly one 17-adic unit root (Newton polygon: v(17) = 1, v(6) = 0).*
"Stays ordinary over every 𝔽_{17^f}" is now justified: *let α, ᾱ be the roots of x²+6x+17 and s_f = α^f + ᾱ^f. Then s₀ = 2, s₁ = −6 and s_f = −6 s_{f−1} − 17 s_{f−2}, so s_f ≡ −6 s_{f−1} (mod 17) and by induction s_f ≡ (−6)^f ≢ 0 (mod 17) for all f ≥ 1.*
Irreducible-square factor argument: *α^f ∉ ℚ (α is a 17-adic unit at one place and |α| = √17), so x² − s_f x + 17^f is irreducible over ℚ, and the characteristic polynomial of Frobenius of Jac(C) over 𝔽_{17^f} is (x² − s_f x + 17^f)², with s_f ≢ 0 (mod 17); hence ordinary over every 𝔽_{17^f}.*
Exact support (cited, not copied or modified): PP v2 checks `evidence_pp_audit_local_reverse_geometry_845cc6bc_2026-11-10/pp_checks_845cc6bc_v2.py` (702244d0…) / `.log` (1e6fe516…), `ALL_CHECKS PASS (40)`, `EXIT 0`: #C(𝔽₁₇) = 30, #C(𝔽₂₈₉) = 286, reconstructed P = (x²+6x+17)², x² coefficient 70 with 17 ∤ 70, Newton polygon one unit root, s_f ≡ (−6)^f ≢ 0 (mod 17) for f ≤ 60. Local v3 evidence is not edited.

**F2 (PL).** Lemma PL is **restricted to even signature**: *Let L be an even lattice with sig = b⁺ − b⁻ even, and ρ_L the Weil representation on ℂ[L′/L] in the convention ρ_L(T)e_γ = e(q(γ))e_γ, ρ_L(S)e_γ = e(−sig/8)|D|^{−1/2} Σ_δ e(−(γ,δ))e_δ, so that for Z = S² = (−I, i) one has ρ_L(Z)e_γ = e(−sig/4)e_{−γ}; for sig even ρ_L factors through SL₂(ℤ). If ρ_L(γ)e₀ = χ(d)e₀ for all γ ∈ Γ₀(N), for a character χ mod N, then χ(−1) = e(−sig/4). Hence sig ≡ 0 (mod 4) ⇒ χ even, sig ≡ 2 (mod 4) ⇒ χ odd.* Equivalent alternative: state it on the metaplectic preimage with the lift Z = (−I, i) named.
Textbook tag (base, like F0 and the L1 van der Blij tag): the convention and **that ρ_L is a representation** — Borcherds, Invent. Math. 132 (1998) §4 / Bruinier, LNM 1780 §1.1; Weil/Milgram. For sig even the dual convention ρ_L^* (giving e(+sig/4)) yields the same real sign, so the conclusion is convention-independent. The sig ≡ 0 / 2 (mod 4) conclusions stay **PROVED**.
The 11:24 clause "odd sig admits no such real character" is **dropped** (out of scope as written: for odd sig ρ_L does not factor through SL₂(ℤ) and ρ_L(−I) needs a chosen lift).
The 11:24 §1.3 step "even unimodular ⇒ sig ≡ 0 mod 8" is tagged the same way: Serre, *A Course in Arithmetic*, V §2; van der Blij/Milgram.

**F3 (R4a grade and R1c split).** The 11:24 R4a claim is **regraded CONDITIONAL [T-Deu, T-ST, T-Frob]**:
- **T-Deu:** Deuring reduction criterion (every elliptic curve with CM by an order in ℚ(√−7) has supersingular reduction at places of good reduction above an inert p), e.g. Lang, *Elliptic Functions*, 2nd ed., Ch. 13 §4, Thm 12. (−7/17) = −1 is PROVED.
- **T-ST:** Serre–Tate 1968 / Néron–Ogg–Shafarevich isogeny invariance of good reduction for abelian varieties, and reduction of isogenies on Néron models (ψφ = [n] reduces to ψ̃φ̃ = [n]).
- **T-Frob:** isogenous abelian varieties over 𝔽_q have equal Frobenius characteristic polynomials, e.g. Mumford, *Abelian Varieties*, §19, Thm 4.
The 11:24 appeal to "base F0: isogeny and reduction facts, Silverman AEC" for the isogeny-reduction step is **withdrawn and replaced** by T-ST and T-Frob, because F0 is elliptic-curve only. With the three tags, the contradiction reads (PP audit support, recorded not re-proved): P_{Ẽ′} divides (x² − s_f x + 17^f)² with the quadratic irreducible, so P_{Ẽ′} = x² − s_f x + 17^f with s_f ≢ 0 (mod 17); Ẽ′ ordinary, contradicting T-Deu. a₁₇(49a1) = a₁₇(Ξ) = 0 covers only twists of 49a1 and is corroboration, not grounds for the general claim.
**R4a-17** is recorded as the **PROVED** exact sub-result (not a separate tally row): Jac(C) has good, ordinary reduction at 17, with P = (x²+6x+17)², irreducible-squared at every 𝔽_{17^f}.
R4a wording (also N4): *"no twist of 49a1 (including Ξ), and no elliptic curve with CM by ℚ(√−7), is a ℚ̄-isogeny factor of Jac(C)."* This refutes only the hypothetical dictionary "Ξ's CM is sourced from Jac(Bolza)"; it does not touch Theorem M or the Owner definition of Ξ.
**R1c split** (PP §3.7): Q = 19600 ("odd ⇒ Fricke −1") **PROVED as implication of D_W**, resting on adopted, PP-proved Fricke +1 (2d/E2). Q = 25 and Q = 784 contradictions, and the Q ∈ {16, 49, 400, 1225} compatibility rows, **CONDITIONAL [w_p = ε_p; Atkin–Lehner 1970 multiplicativity of AL eigenvalues on newforms]**, replacing the 11:24 "PROVED as conditionals". "Odd ↦ ε = −1 COMPATIBLE" holds on ε(Ξ) = −1. **D_W stays OPEN.** The 11:24 file is not edited; this is the additive re-reading.

**F4 (R2).** R2 is graded **PROVED as an implication of P-charge** (Owner t4369 / f825dfff; N_M5, n_inst, N_flux ∈ ℤ, integrality part of the premise, inside the HW package whose E₈ wall sector is CONDITIONAL). It is **not** an unconditional physical constraint and **not** "pure geometry". Grounds: (a−b) − 2(c−b) − (a+b−2c) = 0 identically, so a + b = 2c over ℤ ⇒ a ≡ b (mod 2) (PP v2 `expand` identity). The v3 G5 line `all((a+b)%2==0 for … if (a+b)%2==0)` is **relabelled a non-check**: it filters on its own conclusion, is tautological, and is not grounds. The Gram [[2,−2],[−2,5]] / det 6 illustration stays non-load-bearing. N = 4880 and 9760 are not used.

**F5 (bottom line).** The 11:24 bottom line is replaced, exactly as PP §4 specifies: *Among Bridge C / Ξ / resonant-algebra forms, the only one forced by an on-disk geometric record without an additional Local premise is R2, as an implication of P-charge. R4d is a forced geometric fact with no Bridge C dictionary. PL (R1d), JM (R3a/b) and R5a are forced only given their stated premises (D_Z; P-J (+ P-fix); split SO48 + LD-1 + 1528 tags). Fricke +1 and the χ₁₄₀ mapping are compatible and proved independently (U1 dependency scope), not demanded by the wall.* The 11:24 bottom-line clause (ii), "sourcing Ξ's ℚ(√−7) CM from the Bolza Jacobian is excluded", now reads: **CONDITIONAL [T-Deu, T-ST, T-Frob]**. The R1c clause (i) is read with the F3 split. Bridge C stays PARTIAL. FORCED / COMPATIBLE / NOT FORCED / CONTRADICTS are descriptive labels, not grades, and each FORCED or CONTRADICTS label carries its premise.

## 2. Nits, absorbed

- **N1 (stale PENDING).** Every 11:24 "L1/L2 PP audit PENDING" tag (header, §0 R1d/R1e/R4a, §7) is replaced by the PP d37a456d ruling: **L1 PROVED** (tag sig(U) ≡ 0 mod 8) and **L2 PROVED for the form F_D** (curve reading needs L-match + V1); L1-app, L2-app, N-1 OPEN. U1–U3 are read with the d37a456d scopes (U1 dependency; U2/U3 only for PROVED rows; N = 4880 a premise), as already absorbed in Local erratum `FINDINGS_LOCAL_ERRATUM_HW_ODD_G4_FRICKE_CHI140_d8f52417_PP_d37a456d_2026-11-10_1127.md` (4e440c2bd126f4b5ecf1711f99c35f045776b179c24f5370a234be668201a644), which PP confirmed **FAITHFUL** in `FINDINGS_PP_CONFIRM_LOCAL_ERRATUM_d8f52417_4e440c2b_2026-11-10_1131.md` (05989aa3dc8e2df42402c0c5051fa0c22a9a0a9e7ceda1ce0f7cfed63e67809b). Cited, not re-audited. R1e uses the d37a456d Fix-8 wording: "if the carrier is a lattice Weil representation, an even unimodular summand does not change it". The 11:24 §7 "PENDING: PP audit of PL, JM, R4a" is superseded by PP 670decbe.
- **N2 (modes).** The 11:24 Local files are mode 644 (Local convention). Noted only; no mode changed.
- **N3.** disc(x⁵ − x) = **−2⁸** (sign included), replacing "a power of 2". Good reduction at 17 for the odd-degree model, p odd, p ∤ disc: PROVED.
- **N4.** R4a wording as in F3: "no twist of 49a1 (including Ξ), and no elliptic curve with CM by ℚ(√−7), is a ℚ̄-isogeny factor of Jac(C)."
- **N5.** The 11:24 §1.3 sentence that the e₀ character "would become χ₁₄₀·χ_M" is **unproved**: it presupposes that M's own e₀ line carries a character. It is labelled a **remark, ungraded**.
- **N6.** The R3b row carries the hypothesis explicitly: *J is a σ-equivariant involution commuting with ρ, with V′ = V, and **J preserves ℂe₀**; then J|ℂe₀ = ±1.* Sign OPEN.
- **N7.** R4d coefficient ring: ℤ, ℚ, ℝ, ℂ, de Rham, or étale ℚ_ℓ. **Not 𝔽₂**, where −1 = +1 (cf. PP 1858: J acts trivially on H¹(Σ;ℤ₂)). Transfer tag as in PP §3.5 (Bredon III.2 / Hatcher 3G.1).
- **N8.** R5a, PP 1528 items 3–4, quoted verbatim: **"PROVED, CONFIRM (citation tag: strong approximation / Borel–Harish-Chandra)"**. Whether the later 2030 citation rule retro-tags them is not ruled here. Forced only given the split-SO48 framework + LD-1 + those tags.
- **N9.** R6: the identity named is the closed form **L(1, χ₁₄₀) = 4 log(6+√35)/√140, t4436 a-2, CONDITIONAL [T-CNF]**. The 11:24 §6 "the identity is proved" is withdrawn as unnamed; Λ₀ = √(7/8) L(1, χ₁₄₀) is the Owner definition. R6 dynamical derivation stays OPEN.
- **N10.** v3 G3 prints the factor list without multiplicities. The square in (x²+6x+17)² comes from the degree-4 characteristic polynomial, established by the PP reconstruction from #C(𝔽₁₇) = 30 and #C(𝔽₂₈₉) = 286 (PP v2). v3 evidence is not edited.
- **N11.** The 11:24 R4b count "21" (§0 and §4) is superseded by the accepted clerical erratum's **12** (17, 41, 73, 89, 97, 113, 137, 193, 233, 241, 257, 281; all squarefree part −2; corroboration only). R4a does not depend on R4b.

## 3. Separation from the 11:38 package
The later Local file `FINDINGS_LOCAL_OPEN_ITEMS_UNAUDITED_11_24_RESOLUTION_PASS_2026-11-10_1138.md` (dff4b879075b33dac72b72b3e58b729adf27bd8e816d20e1528bc3e011a6afdf) is a separate unaudited package already with PP; it is not grounds here and changes no grade here (11:24 R4a stays CONDITIONAL [T-Deu, T-ST, T-Frob], 11:24 R4b stays CONDITIONAL).

## 4. Custody (re-hashed 11:43 CST America/Chicago; every sha = sidecar)
| File | sha256 | sidecar |
|---|---|---|
| PP audit 1139 (mode 444) | 670decbe47f1aa33a7a5fd8e8635b2b737a62f774a6bf33d78bc5ff849e04bd5 | MATCH |
| Local findings 1124 | 845cc6bc5f590e8f2e4e867ea56ed44eaafee941a8e8a37e313c0aa78c5bdd6b | MATCH |
| Local clerical erratum 1124 | 286e4f027716fa5c50b3b3d79af7dd6b0b7a3a1531f23d8d8d7f6c80880c002c | MATCH |
| PP v2 checks .py (load-bearing) | 702244d0be626793ef7a900086b1becdeb3b07f869abbddacc03a0113e54841d | MATCH |
| PP v2 checks .log (load-bearing; ALL_CHECKS PASS (40), EXIT 0) | 1e6fe516398c9919045cfa64ca3b71a54a86dedbcbee167e35cb37c564277f54 | MATCH |
| PP re-run of Local v3 .log (byte-identical to Local v3.log) | 3344e1076feba1b3af8b0ab967206ff741ce18fa3c0ad26d0efa4518e82ad1eb | MATCH |
| PP rerun_v3.exit (`exit=0`) | 19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061 | MATCH |
| Local erratum 4e440c2b (d37a456d absorption) | 4e440c2bd126f4b5ecf1711f99c35f045776b179c24f5370a234be668201a644 | MATCH |
| PP confirm 05989aa3 (FAITHFUL) | 05989aa3dc8e2df42402c0c5051fa0c22a9a0a9e7ceda1ce0f7cfed63e67809b | MATCH |
| Local 1138 package (separate, unaudited) | dff4b879075b33dac72b72b3e58b729adf27bd8e816d20e1528bc3e011a6afdf | MATCH |
| **Tip** `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH (read only) |

- PP evidence directory `evidence_pp_audit_local_reverse_geometry_845cc6bc_2026-11-10/` and Local v3 evidence: read and hashed only, not copied or modified.
- Running jobs (wait_then_ob_v5, any ob_v5 / chain processes) not touched; no new job started.
- Not adopted: 1a, the E₈ wall sector, N = 4880, 9760, pasted figures, the 11:24 and 11:38 filings.
- Sidecar `.sha256` written after this markdown was final; this markdown is not edited after hashing.

Local-derived. Nothing adopted. Tip 7cddb188 untouched. Junction UNSOLVED. No CERT.
