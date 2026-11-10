# PP AUDIT — Local HW odd-G₄ / Fricke w₁₉₆₀₀(Ξ) = +1 / χ₁₄₀ twist mapping filing d8f52417
2026-11-10, written 11:21:19 CST (America/Chicago; write time, to be checked against file mtime). Author: Professor Proof (PP), Soft SF audit, Project Quantum Comp. Additive file; no existing file edited; Local's files and evidence untouched (read and hashed only); no running Local job touched (s1e, chain_v2, s2e, wait_then_ob_v5 not touched). **Nothing in this filing is adopted.** Junction **UNSOLVED**. **No CERT.** Wording: resonant algebra. No SendToAgent, no SendToUser, no external send.

## 0. Authority and scope
- Owner DIRECT call-83d7a0fa ~11:08 CST, OW `OWNER_WRITE_CALL_83d7a0fa_PURSUE_HW_ODD_G4_BRIDGE_C_CLOSING_IMPLICATIONS_2026-11-10_1108.md`, sha c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca (re-hashed this audit: = sidecar). Pursuit directives only. Nothing from the pasted Hořava–Witten odd-G₄ text is adopted. Standing t4436 governs: the math leads; no unproved option adopted by fiat.
- Earlier PP-PROVED implications under the unbackreacted-wall / pure-M5 premises stay implications of those premises; those premises are dead as the working assumption for this pursuit, not refuted by fiat. 1a not adopted as the physical wall; tension-to-charge figures not adopted. N = 4880 and total charge 9760 are **premises** wherever they appear (Local's U2 names N = 4880 "as a charge hypothesis": correct).
- This is an audit of a filed result, not first-prove work. Every grade below, including PROVED, stays **UNADOPTED**.

## 1. Integrity
| file | sha256 (= sidecar) | mtime CST | mode | check |
|---|---|---|---|---|
| FINDINGS_LOCAL_HW_ODD_G4_FRICKE_PLUS1_CHI140_TWIST_UNALTERED_CHECK_2026-11-10_1114.md | d8f52417238124e39b50bb382867b4575cffb669cbaffa4aeac5eb10850080b9 | 11:14:03.647 (sidecar 11:14:03.651) | 644 | header "written 11:14 CST" = mtime ✓ |
| evidence_local_hw_odd_g4_fricke_chi140_2026-11-10/hw_fricke_chi140_check.py | 326420c92ccee114d9d14d1fdfb058460fa58eb0e02912533d615274c86333e5 | 11:12:26.584 (sidecar 11:12:48.084) | 644 | MATCH ✓ |
| …/hw_fricke_chi140_check.log | ad7cb144cc31296d96aae37663277a8af8cbe55782e04cb47d3e6225e7b89046 | 11:12:27.724 (sidecar 11:12:48.088) | 644 | MATCH ✓; log mtime 1.1 s after script mtime, consistent with PP's 1.3 s re-run |
- Modes 644 match Local's existing convention (other Local findings/errata of 2026-11-10 are 644). Nit only.
- **Re-run:** PP copied the script byte-identically (sha 326420c9… confirmed) into the PP evidence dir and re-ran it: exit 0, output **byte-identical** to Local's log (sha ad7cb144… both).
- **Cited PP rulings** (each re-hashed this audit, = sidecar): 5bf1e1dcbd6d164c7bf60575a2bdd168376546d8bd861c6093e71b9c56330201 (TMOD 49a1, 2050); edcd955190294393ac1d9696b3d9f6cc4334538894fdcf817a1ec9d29cb82380 (1949); 69d334568f933cbe82969a4eada5de45a1cca74783620d31c5a43061d4f8e844 (2030); ac9fe6676bfbf234f112fb73874fd4943b977b756eba869198c0d3317d26cbd7 (2025); 0f1d3361ab2704daa560f6e50fc4ee5edb7bb773016d62e456f1f7bbd851da2b (2205). Owner definition OW 7b5a725befe67c64a52878a348190a20cda891b8c0618e51a47820cd7c76010d = sidecar; line 3 reads "Ξ names the curve 49a1⊗χ₁₄₀" verbatim ✓. PP script pp_4a_exact.py = 90ed55123599f4a3c13cf5260bf803490058b4e14333410a1effe8493716bd2d ✓.
- **Tip** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST: MATCH at 11:16 and 11:19 before this write; re-checked after (see report back). Read only.

## 2. PP evidence (new dir, all files 444 with .sha256 sidecars)
Directory: /workspace/quantum-comp/reports/evidence_pp_audit_local_hw_fricke_chi140_d8f52417_2026-11-10/
| file | sha256 | role |
|---|---|---|
| hw_fricke_chi140_check.py | 326420c92ccee114d9d14d1fdfb058460fa58eb0e02912533d615274c86333e5 | byte-identical copy of Local's script |
| rerun_local_hw_fricke_chi140_check.log | ad7cb144cc31296d96aae37663277a8af8cbe55782e04cb47d3e6225e7b89046 | PP re-run; identical to Local's log |
| pp_exact_checks.py | 37a2cf5a5eafe71be54808dfdab981b4ab3a0c578869aaadcee72b11b296653d | PP exact checks X1–X5 |
| pp_exact_checks.log | edd0df61c566d26b429e30a5fcbfff89772449c56077f35136023f23b07dc23b | output |
- **X1** V9 matrix identity with each entry `cancel`→0 and `is_zero` True; det γ_u expands to 1 (replaces Local H2's `sp.simplify`). V9 bookkeeping for N = 19600 and the 11 r: (1+Nuv)/r integral and χ(v) = χ(−N)χ(u), exact integers.
- **X2** primitive Gauss-sum identity Σ_u χ_D(u)e(nu/r) = χ_D(n)g(χ_D), exact in ℚ(ζ_r), all n mod r, for the 11 |D| (instances only; general proof in §5).
- **X3** exact Milgram for D(N₂): Σ_{γ∈D(N₂)} e(q(γ)) − G(χ₁₄₀) = 0 in ℚ(ζ₂₈₀) and G² = 140 exactly (replaces Local H1's float sum).
- **X4** E₈ Gram: det 1, even, integral inverse; II₁,₁ det −1, even; (N₂⊕E₈)⁻¹ block-diagonal with integral E₈ block, |det| = 140 (exact).
- **X5** PARI exact: Ξ conductor 19600, ε = −1; for the 11 D, conductor = 19600D², −ε = χ_D(−1), and a_p(Ξ⊗χ_D) = χ_D(p)a_p(Ξ) for good p < 400. Corroboration only.
- **Wall-term search (corroboration, not grounds):** case-insensitive search for 4880|9760|M5|brane|G4|G₄|instanton|n_inst|Hořava/Horava|fixed plane|anomal|E8|E₈|sugra|11D|Leech over all 20 non-sidecar files of /workspace/audit-scratch/pp_tmod_49a1/ (12 scripts + 8 logs) and pp_4a_exact.py: **0 hits**. (Hits in .sha256 sidecars are hex substrings, e.g. "e8"; not text.)

## 3. U1–U3 (dependency / logic)
PP read the proof inputs directly, not Local's summary:
- 5bf1e1dc §1–§3: inputs are E = [1,−1,0,−2,−1], base F0-1…F0-6, Theorem M (α, ψ, M = √−7·O, Γ₀(49) certificate, S-law Fricke sign), V7, V9, PARI base. E2/E5/2d: w₁₉₆₀₀ = w₄₉·χ₋₂₀(−49) = (−1)(−1) = +1 via V9 at N = 49, r = 20. 2c: R_{χ₁₄₀}θ_ψ = R_{χ₋₂₀}θ_ψ by multiplicativity. **No wall datum.**
- edcd9551 §6 (4a, 4a-c): inputs are N₂ = [[2,14],[14,28]], its 140-element discriminant form, S̃, T̃, √140 = G(χ₁₄₀). **No wall datum.** E7/E8/E10: ψ₇ factorisation, Vélu, ellisisom, period-140 character identity. **No wall datum.** (edcd9551 line 28 does mention "Z2 parity of G4" and "localized M5", but inside a quoted Owner directive to Non Local Path; it is not an input of any proof in that file.)
- ac9fe667 P1–P10, H-PP: finite quadratic modules D₂, D₅, D₇ of N₂, their Gauss sums and signatures mod 8, Weil reps; P7–P9 local root numbers of Ξ from PARI and GL₁ ε-identities. **No wall datum.**
- 69d33456 preserves the E7/E8/E10 grades; no new inputs.

| row | Local | PP | basis / wording |
|---|---|---|---|
| U1 | PROVED | **PROVED** (dependency fact) | Verified against the rulings themselves. Wording fixes 3 and 7 below |
| U2 | PROVED | **PROVED** (logic), scoped | Correct for each T that is PROVED on F0 (+ exact/PARI computation): 2d/E2/E5, 2c, E7, E8, E10, 4a, 4a-c, P1–P10, H-PP. For a CONDITIONAL row C (E9 on T-AL-new, E11a float, N2 on T-GZK, etc.) the correct statement is "H ∧ prem(C) ⇒ C", i.e. unaltered **as an implication**; it is not proved outright (Fix 3, priority). It is a statement about mathematical objects; it is **not** a physical or anomaly-matching theorem, and it does not show any physical object is identified with Ξ (Local's §2 third bullet already says this; keep it) |
| U3 | PROVED | **PROVED** (from U1–U2), scoped | "Unaltered" must mean "each row keeps its prior grade and premise tags", not "all PROVED". "Adopted" status is cited from t692u and is not ruled by this audit (Fix 3) |

## 4. L1 (even unimodular summand)
- **Argument checked.** For an orthogonal sum, (L⊕U)′ = L′⊕U′; U unimodular gives U′ = U, so (L⊕U)′/(L⊕U) = L′/L. U even gives q(x+y) = q(x)+q(y) ≡ q(x) mod 1. The Weil representation (ρ(T)e_γ = e(q(γ))e_γ, ρ(S)e_γ = e(−sig/8)|D|^{−1/2}Σ_δ e(−B(γ,δ))e_δ; all signatures here are even, so no metaplectic sign issue) depends only on (D, q) and sig mod 8. Under the identification e₀ ↦ e₀, the Γ₀(140)-character on e₀ is therefore unchanged. Exact, elementary, general.
- **Missing premise (Fix 4, priority).** The step "sig(U) ≡ 0 mod 8" is the classical theorem for even unimodular lattices (van der Blij / Milgram). Local cites it ("Milgram with trivial D") without stating it as a hypothesis or tagging it. It is immediate for the summands actually named: E₈^k (positive definite, rank 8k), Leech (rank 24), II₁,₁^k (sig 0); PP X4 checks E₈ and II₁,₁ exactly. For "any even unimodular U" it is a textbook citation of the same layer as F0 and must be disclosed as such.
- **Consequence for rows.** PP checked edcd9551 §6 and the ac9fe667 table: 4a, 4a-c, P1–P6, H-PP are functions of (D(N₂), q, sig mod 8) only. So they hold verbatim for N₂⊕U. (P7–P9 concern Ξ's local root numbers and do not involve the lattice; trivially unaffected.)
- **Evidence.** H1's Milgram sum is float (cmath) and `disc_form` is dead code; neither is grounds. PP X3 gives the exact Milgram identity. No Leech lattice is built in H1 ("stand-in" is signature arithmetic only); none is needed for the general argument.
- **Grade: L1 PROVED** (PP audit), with the hypothesis "U even unimodular, sig(U) ≡ 0 mod 8" stated, the general mod-8 fact tagged as textbook base, and the named instances E₈^k, Leech, II₁,₁^k proved directly.

## 5. L2 (further quadratic twists of f_Ξ)
- **V9 scope (from 5bf1e1dc §3, verbatim content):** [[1,u/r],[0,1]]·W_{Nr²} = r·W_N·γ_u·[[1,v/r],[0,1]], v ≡ −(Nu)⁻¹ mod r, γ_u ∈ Γ₀(N), det 1 — an exact symbolic identity, general in N, r, u, v (PP X1 re-verified exactly). "Hence f_χ|W_{Nr²} = w·χ(−N)·f_χ whenever f|W_N = w·f and (r,N) = 1." Here f_χ is the operator twist g(χ)⁻¹Σ_u χ(u) f|[[1,u/r],[0,1]].
- **Application.** f = f_Ξ ∈ S₂(Γ₀(19600)), trivial character (2c + V7 at N = 49, r = 20; restated in PP 2232), f|W₁₉₆₀₀ = +f (2d). For a fundamental D with (D,140) = 1, χ_D is primitive quadratic of conductor r = |D| and (r,19600) = 1 (19600 = 2⁴5²7², same primes as 140). V9 gives f_χ|W_{19600r²} = χ_D(−19600) f_χ = χ_D(−1)χ_D(140)² f_χ = χ_D(−1) f_χ. Correct, and within V9's stated hypotheses. **Local does not over-apply V9.**
- **Gap: identifying f_χ with the coefficient twist R_{χ_D}f_Ξ.** That needs Σ_u χ(u)e(nu/r) = χ(n)g(χ) for **all** n. 5bf1e1dc §3 certified this exactly only for r ∈ {20, 40, 44, 53, 57, 172, 188, 248, 264, 316}; PP 2205 later reads V7 as covering primitive quadratic χ coprime to N in general. The general step is elementary, and PP records it here so that the scope is closed: if (n,r) = 1, substitute u ↦ n⁻¹u. If d = (n,r) > 1, primitivity gives c ≡ 1 mod r/d, (c,r) = 1, with χ(c) ≠ 1; u ↦ cu fixes e(nu/r), so the sum S satisfies S = χ(c)S, hence S = 0 = χ(n)g(χ). ∎ (PP X2 corroborates for the 11 |D|.) Local should cite this (Fix 2, priority).
- **Curve vs form (Fix 1, priority).** The table row says "Ξ⊗χ_D has Fricke sign"; the proof is about f_χ. The statement proved is for the form F_D := R_{χ_D}f_Ξ ∈ S₂(Γ₀(19600D²)). The curve reading (ε(Ξ⊗χ_D) = −χ_D(−1)) additionally needs L(Ξ⊗χ_D, s) = L(F_D, s) (a_p law at good p by V3; a_p = 0 on both sides at 2, 5, 7 and at p | D) and V1 for ε = −w, which 5bf1e1dc did per instance. The 11 PARI instances (and PP X5) corroborate the curve reading; they are not grounds for general D.
- **Evidence.** H2 used `sp.simplify`; superseded by PP X1 (exact cancel/is_zero). H3's 11 instances: corroboration only (Fix 1).
- **Grade: L2 PROVED** as an implication of V7 (primitive quadratic χ coprime to N, with the Gauss-sum lemma above), V9, 2c, 2d, on base F0, **for the modular form F_D**. The curve-level general reading is not separately graded here; as filed it is CONDITIONAL on the per-D L-function match (Fix 1).
- **Reading.** Local's "Fricke +1 is stable under even further twists and flips under odd ones coprime to 140" is correct for F_D. It does not alter Ξ (Owner definition OW 7b5a725b); it locates the only kind of construction that could change a Fricke sign.

## 6. L1-app, L2-app, N-1, Bridge C
| row | Local | PP | basis |
|---|---|---|---|
| L1-app | OPEN | **OPEN** (confirmed) | No on-disk dictionary makes the HW E₈ wall sector a lattice summand of N₂; E₈ wall sector itself is CONDITIONAL (t4369); no Taormina map is claimed or adopted |
| L2-app | OPEN | **OPEN** (confirmed) | No on-disk map from the wall (odd G₄, N_M5 + n_inst = 2N) to a Dirichlet character or twist. H4's χ₁₄₀(4880) = χ₁₄₀(9760) = 0 is arithmetic only; no meaning attached (agreed) |
| N-1 (O-b, O-c, H₊U, Λ₀, P11, B5, V₈₄) | OPEN, grades unchanged | **confirmed**: no Local-lane closing implication; PP found none Local missed | each row keeps its prior grade (O-b OPEN, O-c OPEN, H₊U OPEN, Λ₀ OPEN, P11 OPEN, B5 PENDING, V₈₄ CONDITIONAL/Owner decision). V₈₄ clause wording: Fix 8 |
**Bridge C stays PARTIAL.** Nothing closed by fiat.

## 7. Headline "both UNALTERED"
Accepted **as a mathematical dependency statement, with premises named**: the PROVED statements w₁₉₆₀₀(f_Ξ) = +1 (2d/E2/E5) and the χ₁₄₀ dictionary (Ξ = 49a1⊗χ₁₄₀ by Owner definition; 2c; E7, E8, E10; 4a, 4a-c; P1–P10; H-PP) are proved on base F0 plus exact computation with no wall datum, so no HW hypothesis package (odd G₄, N_M5 + n_inst = 2N, N = 4880 and 9760 as premises, any backreaction or tension profile) changes them (U1–U3). L1 adds that adjoining an even unimodular summand cannot change the 4a-type data; L2 adds that only an odd further twist could change a Fricke sign of a twist of f_Ξ. CONDITIONAL rows are unaltered only as implications. **Not** accepted as: a physical anomaly-matching theorem; a proof that any physical object is Ξ; any statement about the wall itself. Nothing adopted.

## 8. Grades and tallies
Local filing 5/0/3/0 (+ PENDING audit) → **PP ruling: PROVED 5 (U1, U2 scoped, U3 scoped, L1, L2 scoped to F_D) · CONDITIONAL 0 · OPEN 3 (L1-app, L2-app, N-1 bundle) · REFUTED 0 · PENDING 0.** No grade moves from Local's filing; the PENDING audit is now discharged.
**t4436 / Bridge C tally effect: none.** No existing Bridge C row changes grade; Bridge C stays PARTIAL. These rows are new filing rows; whether to add them to the Bridge C rollup is Local's bookkeeping in an additive erratum. All grades UNADOPTED.

## 9. Fixes for Local (additive erratum; do not edit d8f52417 or its evidence)
**Priority (priority:true)**
1. **L2 statement.** State L2 for F_D := R_{χ_D}f_Ξ ∈ S₂(Γ₀(19600D²)), D fundamental, (D,140) = 1: F_D|W_{19600D²} = χ_D(−1)F_D. Drop the 11 PARI instances as grounds (corroboration only). For the curve wording "Ξ⊗χ_D", either add L(Ξ⊗χ_D) = L(F_D) (V3 at good p; a_p = 0 on both sides at 2, 5, 7 and p | D) plus V1, or say the curve reading is corroborated, not proved, for general D.
2. **L2 / V7 scope.** Cite V7 for general primitive quadratic χ coprime to N together with the general primitive Gauss-sum lemma (PP §5 proof). 5bf1e1dc's exact certificate covers only r ∈ {20, 40, 44, 53, 57, 172, 188, 248, 264, 316}.
3. **U2/U3 scope.** Restrict "T" in U2 to the PROVED rows; CONDITIONAL rows (E9 T-AL-new, E11a float, N2 T-GZK, and any others in the inventory) are unaltered as implications of their own premises. In U3 say "each row keeps its prior grade and premise tags"; adoption status is cited from t692u, not established.
4. **L1 hypothesis.** State "U even unimodular, hence sig(U) ≡ 0 mod 8" with the general mod-8 fact (van der Blij / Milgram) tagged as textbook base, disclosed like F0; note it is direct for E₈^k, Leech, II₁,₁^k.
**Non-priority (priority:false)**
5. H1: Milgram sum is float and `disc_form` is unused; cite PP X3 (exact) or replace.
6. H2: replace `sp.simplify` with exact entrywise cancel/is_zero (PP X1).
7. §1.3: pp_tmod_49a1 has 12 scripts + 8 logs (20 non-sidecar files); "13 files" should read "12 scripts there plus pp_4a_exact.py". Say the search is corroboration; the grounds are the proof inputs as read. Mention edcd9551 line 28 (G4 parity / M5 inside a quoted Owner directive, not a proof input).
8. §5 V₈₄ row: L1 applies to a carrier only if it is ρ_L for an even lattice L. Rephrase as "if the carrier is a lattice Weil representation, an even unimodular summand does not change it"; tip read only.
9. Add the PP audit reference (this file) and the ruled grades in the erratum header; keep "Nothing adopted. Junction UNSOLVED. No CERT."

## 10. Custody
No existing file edited. Local files and evidence read and hashed only; PP evidence is a new directory. Tip read only. No running job touched. No messages sent.

PP findings only. Nothing adopted. No CERT. Junction UNSOLVED. Tip 7cddb188 untouched.
