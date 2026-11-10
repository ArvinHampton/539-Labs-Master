# FINDINGS (PP audit): Local 845cc6bc reverse-engineer-from-geometry → Bridge C algebra, with clerical erratum 286e4f02. 2026-11-10, written 11:39:10 CST (America/Chicago)

- **Author:** Professor Proof (PP), Soft SF audit. Additive; no existing file edited. **Nothing adopted. Junction UNSOLVED. No CERT.** Wording: resonant algebra. No messages sent.
- **Filing audited:** Local `FINDINGS_LOCAL_REVERSE_ENGINEER_GEOMETRY_TO_BRIDGE_C_ALGEBRA_2026-11-10_1124.md` (845cc6bc…), read together with the clerical erratum `ERRATUM_LOCAL_REVERSE_ENGINEER_GEOMETRY_PRIME_LIST_2026-11-10_1124.md` (286e4f02…). Lane: local-modular / Bridge C / Ξ / resonant algebra only. The parallel PP audits of NL 79ad0c64 and MR2 f4ee61f2 are not mixed in here.

## 0. Authority
- **OW 1117** `OWNER_WRITE_CALL_83d7a0fa_REVERSE_ENGINEER_FROM_GEOMETRY_2026-11-10_1117.md` (bff79185…). This is a method directive: start from the geometry and report which geometric features force which algebraic forms. PP audits as filed: no first-prove, no regrade by fiat. The junction as a starting point is not treated as solved.
- **OW 1108** (c6375f85…) stands as context. Nothing is adopted from pasted HW text. N = 4880 and 9760 are premises or labelled targets, not adopted. Tension-to-charge figures and 1a are not adopted. The E₈ wall sector stays CONDITIONAL, gated by backreaction. Unbackreacted-wall and pure-M5 premises are dead as working assumptions, but not refuted by fiat. This file does not use N = 4880 or 9760 (R9). Verified: neither appears as a premise of any graded row.
- **t4436** (32881263…): the math leads; COND stays COND; branches stay separate; only PP-audited PROVED/REFUTED keeps or drops a branch.
- **PP citation rule 2030** (`FINDINGS_PP_CORRECTION_1949_CITATION_GRADES_edcd9551_2026-11-09_2030.md`, 69d33456…): "a citation never makes a result PROVED by itself … every row that was PROVED only through a cited theorem PP has not verified becomes CONDITIONAL on that named theorem." Applied below, notably to R4a.
- **Base F0** as pinned in PP 5bf1e1dc (`FINDINGS_PP_TMOD_49a1_ATTEMPT_2026-11-09_2050.md` §1). F0-1…F0-4 are Silverman AEC facts **for elliptic curves** (III.4, III.5–6, II.2, II.4, V.1, VII.2–3). F0-5 is Poisson summation; F0-6 is O_{ℚ(√−7)} plus reciprocity. F0 contains **no** abelian-variety reduction or isogeny-invariance theorem and **no** Deuring reduction criterion.
- **PP d37a456d** (audit of Local 1114 d8f52417): grades 5/0/3/0 stand. U1 PROVED (dependency). U2/U3 PROVED, scoped to PROVED rows. L1 PROVED (sig(U) ≡ 0 mod 8 must be stated as a hypothesis or textbook tag). L2 PROVED for the form F_D. L1-app, L2-app and N-1 are OPEN. These are applied here as already ruled, not re-audited.

## 1. Integrity (re-hashed 11:29–11:37 CST; sha = sidecar in every row)
| File | sha256 | sidecar | mode |
|---|---|---|---|
| Local findings 1124 | 845cc6bc5f590e8f2e4e867ea56ed44eaafee941a8e8a37e313c0aa78c5bdd6b | MATCH | 644 (Local convention; nit) |
| Local erratum 1124 | 286e4f027716fa5c50b3b3d79af7dd6b0b7a3a1531f23d8d8d7f6c80880c002c | MATCH | 644 |
| v3.py (load-bearing) | 5c32161f01439bb61721f9d597705d19b901a3f568e36df50e9244b5be66ae28 | MATCH | 644 |
| v3.log (load-bearing) | 3344e1076feba1b3af8b0ab967206ff741ce18fa3c0ad26d0efa4518e82ad1eb | MATCH | 644 |
| v1 .py / .log (crashed, not load-bearing) | 21a35587… / 8d452cac… | MATCH / MATCH | 644 |
| v2 .py / .log (crashed, not load-bearing) | c62e6a92… / e6e3f754… | MATCH / MATCH | 644 |
| OW 1117 | bff79185f361bf461194c8d8c9590a4dc7ad0e520ce2f985f41048453545a2f4 | MATCH | 644 |
| OW 1108 | c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca | MATCH | |
| OW t4436 | 328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46 | MATCH | |
| OW t4369 (face, charge equation) | f825dfffb8cd17a7f3f57a2b0a70bd0d9c9d73f215febffdbd2ca95b494d7cd1 | MATCH | |
| OW t4337 (brane, face, Ξ) | f283cffd365ca7368a9f7b5dfdca7ee177ed54db25a28c1944999a5af755e5b6 | MATCH | |
| OW t4414 (Group A) | 8b26c786643a31b7c2648fe05b3413f9e868be11643c3dac6f94421857f46af3 | MATCH | |
| Local 1114 d8f52417 | d8f52417238124e39b50bb382867b4575cffb669cbaffa4aeac5eb10850080b9 | MATCH | |
| PP d37a456d | d37a456d60edfdf050e01434f0c54605104bf4b460f9375253477623a98891a9 | MATCH | 444 |
| PP 1528 O3/SO48 (R5a) | 3b6f80729c31a8604a81ebbfec720fe0684e9e448afb6a86419f69c492ee057d | MATCH | |
| PP 2030 citation rule | 69d334568f933cbe82969a4eada5de45a1cca74783620d31c5a43061d4f8e844 | MATCH | |
| PP 5bf1e1dc (F0, Theorem M) | 5bf1e1dcbd6d164c7bf60575a2bdd168376546d8bd861c6093e71b9c56330201 | MATCH | |
| PP ac9fe667 (4a third proof, P5, P7 ε_p table) | ac9fe6676bfbf234f112fb73874fd4943b977b756eba869198c0d3317d26cbd7 | MATCH | |
| PP 1858 KK/Bolza (J = −1 on H¹, PP-verified) | 1fe6c5746510abc0f007de6e3281fba3b5145ddb9250965a07fefc73d705005c | MATCH | |
| t692u adoption inventory 1034 | 93a3a556365b12e9993cdf789262c0f530bcdec855e1ecceada19964b6b210bd | MATCH | |
| OW t692u 1028 | 314ac8b6328518aa3896bc963b901ca7c43c10988df51052390fea655a570b29 | MATCH | |
| **Tip** `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST | before: MATCH (11:29) | read only |

Header vs mtime of the Local files: findings header 11:24 (minute precision) vs mtime 11:24:03; erratum 11:24 vs 11:24:19. Both consistent. v1/v2 disclosure confirmed: v1 crashed in G2 (cypari2 `gen_to_integer` on a t_COL), and v2 crashed in G5 (`matkerint` on a t_VEC). Their completed sections are byte-identical to v3 (v1 G1, v2 G1–G4, diffed), but they are **not** used as grounds.

## 2. PP evidence (`evidence_pp_audit_local_reverse_geometry_845cc6bc_2026-11-10/`, every file 444 with a .sha256 sidecar)
| File | sha256 | Role |
|---|---|---|
| reverse_geometry_check_v3.py | 5c32161f01439bb61721f9d597705d19b901a3f568e36df50e9244b5be66ae28 | byte-identical copy of Local v3 (cp -p) |
| rerun_v3.log | 3344e1076feba1b3af8b0ab967206ff741ce18fa3c0ad26d0efa4518e82ad1eb | PP re-run 11:34 CST (PARI 2.17.2 / cypari2). **Byte-identical to Local v3.log**, including the PARI stack banner (`cmp` clean) |
| rerun_v3.exit | 19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061 | `exit=0` |
| pp_checks_845cc6bc.py / .log (v1) | c01ea05c2b9de8c8e05991515a3d7141d3ae3962516cd6afce0d3c19f25fb16c / a64f70cbf23fd3e43c8fd1dabcbc50c724f976e844db26c871c0b9999d16b79d | PP v1, **kept as written**. It had 2 FAILs from PP check-expectation bugs, not math: (i) the expected sign of disc(x⁵−x), which is −256, not +256; (ii) the factor-set string compare used `**` vs `^`. Not grounds |
| pp_checks_845cc6bc_v2.py / .log | 702244d0be626793ef7a900086b1becdeb3b07f869abbddacc03a0113e54841d / 1e6fe516398c9919045cfa64ca3b71a54a86dedbcbee167e35cb37c564277f54 | **Load-bearing PP checks.** The only diffs from v1 are the two expectation fixes plus a header line. Run 11:35:56 CST, `ALL_CHECKS PASS (40)`, `EXIT 0`. Pure Python integers and Fractions plus SymPy exact (`expand(...)==0`). No PARI, no floats, no simplify, no allclose |

PP v2 checks, all exact: the R5b Kronecker symbols by Euler's criterion, cross-checked with sympy.jacobi; (−7/17) = −1; (−7/p) = +1 for p = 113, 137, 193, 233, 281. For N₂: det −140, even, sig 0, Smith form (2, 70), |D| = 140 by enumeration, 2-torsion 4, dimensions 72/68, 140 a fundamental discriminant, and nondegeneracy of the discriminant bilinear form. The R2 congruence as an `expand` identity. For R4a: disc(x⁵−x) = −2⁸, #C(𝔽₁₇) = 30, #C(𝔽₂₈₉) = 286, the char poly reconstructed from these counts = (x²+6x+17)² (expand-difference 0), x² coefficient 70 ≢ 0 (mod 17), s_f ≡ (−6)^f ≢ 0 (mod 17) for f ≤ 60 (plus the one-line induction in §3.4), and a₁₇(49a1) = 0 by point count. For the erratum: independent point-count char polys at all 58 primes 5 ≤ p ≤ 281 have factor sets **identical** to v3 G3, and the derived lists equal both erratum lists.

## 3. Priority audits

### 3.1 Lemma PL (parity lock). Local PROVED → **PP PROVED, scoped to sig even (textbook tag required); the odd-sig clause is out of scope as stated**
- **Formula.** In the standard convention (Borcherds, Invent. Math. 132 (1998) §4; Bruinier, LNM 1780 §1.1), ρ_L(T)e_γ = e(q(γ))e_γ and ρ_L(S)e_γ = e(−sig/8)|D|^{−1/2} Σ_δ e(−(γ,δ))e_δ, with Z = S² = (−I, i) ∈ Mp₂(ℤ). Then ρ_L(Z)e_γ = e(−sig/4)|D|^{−1} Σ_β [Σ_δ e(−(γ+β,δ))] e_β = e(−sig/4)e_{−γ}. This is character orthogonality on the nondegenerate form D, whose nondegeneracy for N₂ PP checked exactly (audit support only). The formula is therefore elementary given the definition of ρ_L. **That ρ_L is a representation** (Weil/Milgram) is the textbook layer and must be **tagged**, as L1's van der Blij/Milgram tag was in d37a456d. The dual convention ρ_L^* gives e(+sig/4). For sig even both conventions give the same real sign, so the conclusion is convention-independent.
- **Proof step.** −I ∈ Γ₀(N) (c = 0), with d = −1, and −0 = 0 in L′/L. Hence ρ_L(−I)e₀ = e(−sig/4)e₀ = χ(−1)e₀. Correct.
- **Metaplectic scope (priority fix F2).** ρ_L factors through SL₂(ℤ) iff sig is even (ρ_L(Z²) = e(−sig/2) = (−1)^{sig}). For odd sig, "ρ_L(γ) for γ ∈ Γ₀(N)" and "ρ_L(−I)" are not defined without a choice of lift; on the full preimage the hypothesis is vacuous, because Z² has d = 1 but acts by −1. So the sentence "odd sig admits no such real character" is not a statement about Γ₀(N) as written. Restrict PL to sig even, or restate it on the metaplectic preimage with the lift Z = (−I, i) named. The sig ≡ 0 / 2 (mod 4) conclusions are PROVED.
- **N₂ instance** (not carrying the general lemma). Exact: det −140, even, sig (1,1) → 0, D ≅ ℤ/2 × ℤ/70, |D| = 140, 2-torsion 4, ρ(−I) = permutation γ ↦ −γ with eigenspaces +72/−68, χ₁₄₀(−1) = sign(140) = +1. The e₀ instance is in fact already the γ = −I case of **4a** (PP-proved, adopted).
- **§1.3 "Consequence" remark.** "The e₀ character would become χ₁₄₀·χ_M" presupposes that M's own e₀ line carries a character. This is not proved in the file and is ungraded. Label it as a remark (nit N5). "Even unimodular ⇒ sig ≡ 0 mod 8" needs the same textbook tag as L1 (Serre, *A Course in Arithmetic* V §2; van der Blij/Milgram).

### 3.2 Lemma JM. Local PROVED → **PP PROVED (elementary); application OPEN**
- ρ′(γ)Je₀ = Jρ(γ)e₀ = χ₁₄₀(d)Je₀, and Je₀ ≠ 0, so Je₀ spans a χ₁₄₀-line. If V′ = V, J commutes with ρ, J² = 1 and J preserves ℂe₀, then J|ℂe₀ = ±1. Correct and complete.
- Nit N6: the §0 R3b row ("σ-equivariant involution on the line") omits the hypothesis **J preserves ℂe₀**, which §3 states. Carry it into the table.
- **P-J is a Local proposal, not on disk.** The application (R3a) stays **OPEN**, and R3b's sign stays OPEN. Nothing here treats the junction as solved or as set up. Confirmed.

### 3.3 R2 (charge parity). Local PROVED (elementary), "FORCED, purely from geometry" → **PP PROVED as an implication of P-charge; not an unconditional physical constraint**
- Premise **P-charge**: N_M5 + n_inst = 2N_flux with N_M5, n_inst, N_flux ∈ ℤ. This is the OW t4369 (f825dfff) "Face charge" line, inside the HW package whose E₈ wall sector is CONDITIONAL (OW t4369/1108). Integrality is part of the premise and should be stated.
- Algebra: (a−b) − 2(c−b) − (a+b−2c) ≡ 0 (expand), so a + b = 2c ⇒ a ≡ b (mod 2). PROVED.
- **v3 G5 "parity" line is tautological**: `all((a+b)%2==0 for … if (a+b)%2==0)` filters on its own conclusion. It is **not grounds** (priority fix F4: drop it or relabel it as a non-check). The Gram [[2,−2],[−2,5]] / det 6 illustration is arithmetically correct (b₁ = (1,−1,0), b₂ = (0,2,1) is a ℤ-basis of the kernel). It is non-load-bearing and stays that way. N = 4880 and 9760 are not used. χ₁₄₀(4880) = 0 has no meaning and is not a closure.

### 3.4 R4a (load-bearing). Local PROVED → **PP CONDITIONAL on [T-Deu, T-ST, T-Frob]; exact sub-result R4a-17 PROVED. Grade moves.**
Audit, step by step:
1. **Good reduction at 17.** disc(x⁵−x) = **−2⁸** ("a power of 2" holds up to sign; nit N3). For the odd-degree model y² = f(x) with p odd and p ∤ disc f, C has good reduction at p, and so does Jac(C). **PROVED** (this is the standard smoothness criterion for this model, and elementary).
2. **Frobenius char poly at 17.** P(x) = (x²+6x+17)² = x⁴+12x³+70x²+204x+289. PARI (v3 G3, re-run byte-identical) is cross-checked by PP point counts: #C(𝔽₁₇) = 30 and #C(𝔽₂₈₉) = 286 (one point at ∞) give S₁ = −12 and S₂ = 4, and the reconstructed polynomial equals (x²+6x+17)² exactly. Note: the v3 log prints only the factor list, not the multiplicity; the square is established by the PP reconstruction. **PROVED** as an exact computation on the PARI base, independently corroborated.
3. **Ordinarity: Local's criterion is wrong as stated, but the conclusion holds (priority fix F1).** For an abelian surface, "trace ≢ 0 mod p" gives only p-rank ≥ 1. Ordinary (p-rank 2) ⇔ the x² coefficient a₂ ≢ 0 (mod p). Here a₂ = 70 ≡ 2 (mod 17): ordinary. Equivalently, x²+6x+17 has exactly one 17-adic unit root (Newton polygon: v(17) = 1, v(6) = 0). "Stays ordinary over every 𝔽_{17^f}" was unjustified in the file. Audit support: s_f = α^f+ᾱ^f satisfies s_f = −6s_{f−1} − 17s_{f−2}, so s_f ≡ (−6)^f ≢ 0 (mod 17) for all f ≥ 1 (one-line induction; also checked for f ≤ 60). Also α^f ∉ ℚ, since α is a 17-adic unit at one place and has |α| = √17. So x² − s_f x + 17^f is irreducible over ℚ, and the char poly over 𝔽_{17^f} is its square.
4. **Deuring (T-Deu).** "Every elliptic curve with CM by an order in K = ℚ(√−7) has supersingular reduction at every place of good reduction above an inert p" is Deuring's reduction criterion (e.g. Lang, *Elliptic Functions*, 2nd ed., Ch. 13 §4, Thm 12). PP checked that it is **not** inside F0 (F0-1…F0-4 are the AEC items listed in 5bf1e1dc §1). It is load-bearing for the general claim, and PP has not verified it in this audit, so by the 2030 rule it is a **named citation: CONDITIONAL until pinned**. (−7/17) = −1 is PROVED.
5. **a₁₇(49a1) = a₁₇(Ξ) = 0.** PROVED (PARI G1; PP point count for 49a1). This covers only curves geometrically isomorphic to 49a1, i.e. twists. The **general** claim ("any elliptic factor with CM by ℚ(√−7)", including the j = 255³ curve with CM by ℤ[√−7], and any curve over a number field) needs T-Deu, or else an extra citation that all ℚ(√−7)-CM curves are ℚ̄-isogenous to 49a1. The 49a1 data are corroboration, not grounds.
6. **Reducing an isogeny (T-ST).** The file cites "base F0: isogeny and reduction facts, Silverman AEC". That covers elliptic curves only. The step needs, for abelian varieties over a number field F: (i) if A ∼_F Jac(C)_F then A, and each isogeny factor, has good reduction at every place v | 17. This is the isogeny invariance of good reduction: Serre–Tate, *Good reduction of abelian varieties* (1968), via Néron–Ogg–Shafarevich. It also answers "does such a place exist": every v | 17 works, after any finite extension of F needed to define E′, the CM and the isogeny. (ii) The isogeny extends to the Néron models, and its reduction is an isogeny (ψφ = [n] reduces to ψ̃φ̃ = [n]). Neither is in F0. **CONDITIONAL until pinned.** There is no mathematical gap, but the step is cited, not verified.
7. **Equal Frobenius char polys (T-Frob).** An isogeny over 𝔽_q induces a Frobenius-equivariant isomorphism V_ℓÃ ≅ V_ℓB̃ (ℓ ≠ 17), so the char polys agree (e.g. Mumford, *Abelian Varieties* §19, Thm 4; Tate 1966 for the converse, which is not needed). It applies over every 𝔽_{17^f}. This is the abelian-variety analogue of F0-3, but it is not in F0. **CONDITIONAL until pinned.** With it, the contradiction is clean: P_{Ẽ′} divides (x²−s_f x+17^f)² with the quadratic irreducible, so P_{Ẽ′} = x²−s_f x+17^f with s_f ≢ 0 (mod 17). Ẽ′ is then ordinary, contradicting T-Deu. PP records this two-line repair as audit support. Local's text ("ordinary vs a supersingular factor, impossible by equal char polys") is correct once step 3 is fixed.
8. **One prime suffices iff steps 4, 6 and 7 hold.** They are standard, but per the 2030 rule they are named, unverified citations. So: **R4a CONDITIONAL [T-Deu, T-ST, T-Frob]**, with exact sub-result **R4a-17 PROVED**: Jac(C) has good, ordinary reduction at 17, with P = (x²+6x+17)², irreducible-squared at every 𝔽_{17^f}. The other listed primes are corroboration only.
9. **Wording (nit N4).** "Not isogenous to any twist of 49a1, including Ξ" compares a surface with elliptic curves. Read it as "no twist of 49a1 (including Ξ), and no elliptic curve with CM by ℚ(√−7), is a ℚ̄-isogeny factor of Jac(C)."
10. **Erratum item 1: ACCEPTED.** PP independent point counts at all 58 primes 5 ≤ p ≤ 281 reproduce v3 G3. The primes with (−7/p) = −1 and a quadratic factor of nonzero trace are exactly **17, 41, 73, 89, 97, 241, 257**. The quartic-ordinary primes x⁴+cx²+p², p ∤ c, are exactly **19, 59, 83, 131, 139, 227, 251**, all ≡ 3 (mod 8). Their ordinarity criterion is right: Newton polygon slopes 0, 0, 1, 1 since v(c) = 0. PP verified exactly that 113, 137, 193, 233, 281 have (−7/p) = +1, so they were wrongly listed. The R4a argument uses only p = 17 and is unaffected (its grade moves for the citation reasons above, not because of the list).

### 3.5 R4d. Local PROVED → **PP PROVED (elementary; specify coefficients)**
- Local's route: ι² = 1 acts semisimply on H¹(Σ;ℚ), and H¹(Σ;ℚ)^ι ≅ H¹(Σ/ι;ℚ) = H¹(ℙ¹;ℚ) = 0 (transfer for finite groups: tag, e.g. Bredon III.2 / Hatcher 3G.1). So ι* = −1. This is correct for H¹ with ℤ, ℚ, ℝ or ℂ coefficients, for H¹_dR, and for étale ℚ_ℓ. **Not** for 𝔽₂ coefficients, where −1 = +1 (as in PP 1858: "J acts trivially on H¹(Σ;ℤ₂)"). State the coefficient ring (nit N7).
- Audit support, a fully elementary alternative: div(x − x(P)) = P + ιP − 2∞, so ι* = −1 on Pic⁰ = Jac(Σ). This is consistent with the prior PP verification (1858: "J = −1 on H¹ (PP-verified)"). No grade raise is involved; Local's PROVED stands.

### 3.6 R5b. Local PROVED → **PP PROVED (exact); COMPATIBLE, not forcing**
- PP Euler criterion: (D/23) = +1 for D = 140, −20, −7, 35, 8 and −1 for D = 5, 28, −35, −4, −8. This matches log G4. "Triviality at 23 ⇔ (D/23) = +1" is correct for quadratic χ_D with 23 ∤ D (23 splits in ℚ(√D)). Several D pass, so χ = χ₁₄₀ is **not** forced. R5a is cited from PP 1528, not re-proved (§4).

### 3.7 CONTRADICTS rows. Verdict: each refutes only an off-disk dictionary; **no Owner or PP record, and no Bridge C row, is regraded**
- PP searched reports/ for "Bolza" together with CM, √−7, 49a1 or Ξ. No on-disk record asserts "Ξ ⊂ H¹(Σ_Bolza)", D_W or D_Z. MR2's vacuum list mentions Γ = Bolza and Ξ = 49a1⊗χ₁₄₀ side by side, with no identification.
- **R1c (D_W)**, scope split (lead-table grade move, priority fix F3). The "odd ⇒ Fricke −1" contradiction (Q = 19600) rests on **2d/E2 Fricke +1 (PP-proved, adopted)**: **PROVED as implication of D_W**. The Q = 25 and Q = 784 contradictions, and the Q ∈ {16, 49, 400, 1225} compatibilities, rest on the W_Q reading w_p = ε_p, which is CONDITIONAL. They are therefore **CONDITIONAL [w_p = ε_p; multiplicativity of AL eigenvalues on newforms, Atkin–Lehner 1970]**, not "PROVED as conditionals". "Odd ↦ ε = −1 COMPATIBLE" holds on ε(Ξ) = −1 (ellrootno, exact). D_W itself is OPEN.
- **R1d (D_Z): PROVED as implication of D_Z**, on PL (sig 0) and, independently, on 4a at γ = −I. D_Z is OPEN.
- **R3c: faithful.** It cites 2g (f_Ξ ∉ S₂/M₂(Γ₀(980))) and J-1 REFUTED as a Ξ carrier for any nebentypus mod 980 (t692u inventory 1034 rows 16, 21–23; t4436 REFUTED list). f_Ξ ∈ S₂(Γ₀(19600)) is 2c (adopted). "Minimal level 19600" stays **CONDITIONAL [T-AL-new]**, matching t4436 J-3 minimal modular level and E9. Cited, not re-proved.
- **R4a**: the contradiction refutes only the hypothetical "Ξ's CM is sourced from Jac(Bolza)". It is now **CONDITIONAL [T-Deu, T-ST, T-Frob]** (§3.4). It does not touch Theorem M or the Owner definition of Ξ.

### 3.8 R1b and R4b conditionals
- **R1b.** The ε_p table (ε₂ = −1, ε₅ = +1, ε₇ = −1) is the already PP-proved, adopted **P7** (ac9fe667), and the W_Q products are arithmetic. **Sign table PROVED (as values of ε_p).** The reading "W_Q eigenvalue = ∏_{p|Q} ε_p" is **CONDITIONAL** [w_p = ε_p, local AL/root-number identity; AL multiplicativity]. ∏w_p = +1 = w₁₉₆₀₀ is consistency with PP-proved Fricke +1 (2d/E2) and ε(Ξ) = −1, **not** a proof of the citation. PARI instances cannot support the general identity. Selection: **OPEN** (undefined). Grades stand.
- **R4b. CONDITIONAL stands** on the citation Jac(Bolza) ∼_{ℚ̄} E² with E CM by ℤ[√−2]. Corrected count **12** (erratum item 2 **ACCEPTED**: list verified exactly, all a²−4p ∈ −2·□). The 12 primes are corroboration only. R4a does **not** depend on R4b.

## 4. Remaining lead-table rows
| Row | Local | PP | Basis |
|---|---|---|---|
| R1a | COMPATIBLE; PROVED (= U1–U3) | **PROVED as a dependency statement**, d37a456d scopes | U1 dependency; U2/U3 only for PROVED rows (CONDITIONAL rows unaltered only as implications); N = 4880 is a premise; not a physical theorem |
| R1b | table PROVED / reading COND / selection OPEN | **stand** | §3.8 |
| R1c | CONTRADICTS; PROVED as conditionals | **split**: Q = 19600 PROVED ⇐ D_W; Q = 25, 784 and the compat rows CONDITIONAL [w_p = ε_p] | §3.7 |
| R1d | CONTRADICTS; PL PROVED | **PROVED ⇐ D_Z** | PL (sig 0) + 4a |
| R1e | COMPATIBLE; L1 PROVED (PP PENDING) | **L1 PROVED per d37a456d** (sig(U) ≡ 0 mod 8 tagged); L1-app OPEN | "PP PENDING" stale (N1). Use the d37a456d Fix-8 wording: "if the carrier is a lattice Weil representation, an even unimodular summand does not change it" |
| R2 | FORCED; PROVED | **PROVED ⇐ P-charge** (t4369, integers) | §3.3 |
| R2′ | OPEN | **OPEN** | L2-app OPEN (d37a456d) |
| R3a | FORCED given P-J; JM PROVED; app OPEN | **JM PROVED; application OPEN** | §3.2 |
| R3b | ±1 PROVED given P-J + P-fix; sign OPEN | **agree**; add "J preserves ℂe₀" (N6) | §3.2 |
| R3c | CONTRADICTS; PROVED (2g/J-1); min level COND | **faithful citation** | §3.7 |
| R4a | CONTRADICTS; PROVED | **CONDITIONAL [T-Deu, T-ST, T-Frob]**; R4a-17 PROVED | §3.4 |
| R4b | CONDITIONAL | **CONDITIONAL**; count 12 | §3.8 |
| R4c | OPEN | **OPEN** | no dictionary on disk |
| R4d | FORCED; PROVED | **PROVED** (coefficients ≠ 𝔽₂) | §3.5 |
| R5a | FORCED; PP-PROVED, tags COND | **cited, not re-audited** | PP 1528 items 3–4 read "PROVED, CONFIRM (citation tag: strong approximation / Borel–Harish-Chandra)". Those rulings predate the 2030 strict rule. Whether that rule retro-tags them is not ruled here. Local should quote 1528 verbatim rather than paraphrase (N8). Forced only given the split-SO48 framework + LD-1 + those tags |
| R5b | COMPATIBLE; PROVED | **PROVED** | §3.6. π away from 23: OPEN (LD-O3a, 1528 item 5) |
| R6 | NOT FORCED; OPEN | **OPEN** | Bridge C Λ₀ is OPEN. Note (N9): the closed form L(1, χ₁₄₀) = 4 log(6+√35)/√140 is t4436 a-2, CONDITIONAL [T-CNF]; "the identity is proved" (§6) should say which identity |
| R7 | COMPATIBLE (formal); NO DICTIONARY | **faithful** | 4b lemma adopted; V₄₂ application CONDITIONAL on tip §1u; V₈₄ not adopted; V-3 REFUTED (t692u 1034 §1.5, row 22) |
| R8 | NOT FORCED; grades unchanged | **faithful** | O-b, O-c, H₊U, P11 OPEN; B5 PENDING; J-2 / J-3 embeddings OPEN (undefined) per t692u 1034 §3.1–3.2 |
| R9 | NO DICTIONARY; not used | **confirmed** | 1a, tension-to-charge, N = 4880 and 9760 are used by no graded row |

**Force-class labels.** FORCED / COMPATIBLE / NOT FORCED / CONTRADICTS are acceptable as descriptive labels. They are not grades, and every FORCED or CONTRADICTS label must carry its premise.

**Bottom line: not accurate as written (priority fix F5).** "One forced algebraic form that comes *purely from the geometry*: R2" overstates the case on two counts. (i) R2 is forced only as an **implication of the t4369 charge equation P-charge**, an Owner-recorded HW-package premise inside a CONDITIONAL E₈ wall sector. It is not "pure geometry". (ii) R4d is also labelled FORCED from geometry: a forced ℤ/2 fact about Σ, with no dictionary into Bridge C. The accurate scoping: "Among Bridge C / Ξ / resonant-algebra forms, the only one forced by an on-disk geometric record without an additional Local premise is R2, as an implication of P-charge. R4d is a forced geometric fact with no Bridge C dictionary. PL (R1d), JM (R3a/b) and R5a are forced only given their stated premises (D_Z; P-J (+ P-fix); split SO48 + LD-1 + 1528 tags). Fricke +1 and the χ₁₄₀ mapping are compatible and proved independently (U1 dependency scope), not demanded by the wall." Also (ii) of the bottom line, "sourcing Ξ's CM from Bolza is excluded", must read **CONDITIONAL [T-Deu, T-ST, T-Frob]**.

## 5. Stale tag
The 1124 header (and §0 R1d/R1e/R4a, §7) marks 1114 L1/L2 as "PP audit PENDING". This is stale relative to d37a456d (11:21 CST): L1 PROVED (tag sig(U) ≡ 0 mod 8) and L2 PROVED for F_D (curve reading needs L-match + V1). U1–U3 must be read with the d37a456d scopes. Nit N1, not this package's job to absorb. Local's separate d37a456d erratum is not awaited and is not audited here.

## 6. Ruled tally of this filing's new statements
- **Local (after the clerical erratum):** PROVED 6 (PL, JM incl. R3b ±1, R2, R4a, R4d, R5b); CONDITIONAL 2 (R1b W_Q reading, R4b).
- **PP ruling: PROVED 5 / CONDITIONAL 3 / OPEN (unchanged list) / REFUTED 0.**
  - PROVED 5: PL (sig even, tag), JM incl. R3b ±1, R2 (⇐ P-charge), R4d, R5b.
  - CONDITIONAL 3: R1b W_Q reading [w_p = ε_p]; R4b [Bolza ∼ E², CM ℤ[√−2]]; **R4a [T-Deu, T-ST, T-Frob]**.
  - Exact sub-result R4a-17 is PROVED. Like N2's ε sub-result, it is not counted as a separate row.
  - OPEN, unchanged: D_W, D_Z, P-J (so the JM application), R1b selection, L1-app, R2′, R4c, R5 π away from 23, R8 rows.
  - REFUTED of Owner/PP records: **none**.
  - Lead-table scope move: R1c split (§3.7).
- **Grade moves vs Local:** R4a PROVED → CONDITIONAL; R1c "PROVED as conditionals" → split (Q = 19600 PROVED ⇐ D_W; the rest CONDITIONAL). PL and R2 grades stand with scope fixes. Everything else stands.
- **Erratum 286e4f02: ACCEPTED** (both items verified exactly).
- **Other standing tallies: unchanged and not rewritten.** Bridge C 49/10/5/2/1 + V₈₄ (67 rows), **PARTIAL**. t4436 65/15/5/9/2. d37a456d 5/0/3/0. No existing row is regraded. Nothing in this filing is adopted. The R4a CONDITIONAL is a grade on a new, unadopted Local statement.

## 7. Fixes for an additive Local erratum (do not edit 845cc6bc, 286e4f02 or the evidence)
**Priority:**
- **F1 (R4a).** Replace "trace −12 ≢ 0 (mod 17), so ordinary" with the g = 2 criterion (a₂ = 70 ≢ 0 mod 17, or one unit root of x²+6x+17). Justify "ordinary over every 𝔽_{17^f}" (s_f ≡ (−6)^f mod 17). State the irreducible-square factor argument.
- **F2 (PL).** Restrict to sig even, or state it on the Mp₂ preimage with Z = (−I, i). Tag the Weil-representation convention and its representation property (Borcherds 1998 §4 / Bruinier LNM 1780 §1.1; Weil/Milgram). Tag "even unimodular ⇒ sig ≡ 0 mod 8".
- **F3 (R4a grade).** Regrade R4a to CONDITIONAL [T-Deu: Deuring reduction; T-ST: Serre–Tate/NOS isogeny invariance of good reduction and Néron-model reduction of isogenies; T-Frob: isogenous AVs over 𝔽_q have equal Frobenius char polys]. Record R4a-17 as the PROVED exact sub-result. Replace "base F0 (Silverman AEC)" here, because F0 is elliptic-curve only. Split R1c as in §3.7.
- **F4 (R2).** Grade R2 as "PROVED as implication of P-charge (t4369; N_M5, n_inst, N_flux ∈ ℤ)". Remove or relabel the tautological v3 G5 parity line, which is not a check.
- **F5 (bottom line).** Rescope as in §4: R2 ⇐ P-charge; R4d also forced but has no Bridge C dictionary; the R4a exclusion is CONDITIONAL.

**Nits (non-priority):**
- N1: stale "L1/L2 PP audit PENDING" tags.
- N2: modes 644 (Local convention).
- N3: disc(x⁵−x) = −2⁸.
- N4: R4a wording ("isogeny factor", not "isogenous to Ξ").
- N5: the §1.3 χ₁₄₀·χ_M remark is unproved; label it a remark.
- N6: R3b table must carry "J preserves ℂe₀".
- N7: R4d coefficient ring (not 𝔽₂).
- N8: quote the PP 1528 R5a grades verbatim.
- N9: R6 should name the identity and its a-2 [T-CNF] status.
- N10: the v3 G3 print shows factors without multiplicities. Print the full factorization, or state that the square comes from the degree-4 char poly.
- N11: the 1124 R4b "21" is superseded by the erratum's 12 (accepted).

## 8. Custody
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, MATCH before this write (11:29 CST); after-write re-check is in the report back. Read only.
- Local findings, erratum, evidence (v1/v2/v3) and sidecars: read and hashed only. v3.py was copied (not moved) into the PP evidence directory. No running Local job (s1e, chain_v2, s2e, wait_then_ob_v5) or other agent directory was touched. No existing file was edited, moved, renamed or deleted.
- No SendToAgent, SendToUser or external send. Nothing adopted.

PP findings only. Nothing adopted. Tip 7cddb188 untouched. Junction UNSOLVED. No CERT.
