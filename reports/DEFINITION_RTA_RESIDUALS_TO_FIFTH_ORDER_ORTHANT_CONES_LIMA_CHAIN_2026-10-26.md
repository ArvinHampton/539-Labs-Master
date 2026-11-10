# Definition Layout — RTA Residuals to the Mismatched Orthant Cones of the Fifth Order (Theorem–Lemma Chain)

Date: 2026-10-26 (America/Chicago)
Authority: Owner voice (Arvin Hampton), definition-and-layout only. No lock change. Tip Soft SF LOCK untouched. Cite-only from corpus on disk; no new mathematics.

## 1. Scope and voice aliases
- "Lima chain" = **theorem–lemma chain** of the 9 Maths: `/workspace/quantum-comp/maths/theorem-lemma-chain-9-maths.txt` (sha256 904104d26c0c029df9a9e39f7ef5235f4b3a2f7befb0349e7bdf0187a6df5a0a, verified).
- "monogen's fifth order" = **Ramanujan's fifth-order mock theta function f_0**. The word "monogen" does not appear as a Written term in the cited corpus files (ABSENT); alias recorded as voice-only.
- Short-hash cites below are the first 16 hex of sha256. `BOOK` = `/workspace/quantum-comp/oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/`.

## 2. Ordered residual chain

**R0 — Root budget (Axiom 0.1, 9 Maths).**
Definition: The chain's root axiom states C3 terminates in exactly 539 steps and forces the flux budget N_flux = ⌊e³ × 3⁵⌋ = 4880. This is the integer from which every residual below is cut.
Cite: theorem-lemma-chain-9-maths.txt, Axiom 0.1 ("Nflux=⌊e3×35⌋=4880"); NINE-MATHS.md (18357bbd69b05755) line 36 notes 539 is an axiom, not a free-map measurement.
Role: 9 Maths root. Note: the chain file itself contains no occurrence of the word "residual".

**R1 — Residual pool R.**
Definition: With fixed N_flux = 4880 and f_max = 21, the residual pool is R = N_flux − f_max = 4859.
Cite: BOOK/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md (8e7e4df3a25c849a) line 79.
Role: first RTA residual — the leftover flux after the maximal face count is removed ("Residual Discrete Algebra is leftover pieces", Residual_Law_for_Bridge_C_L_A_Pursuit, c48144bfbd4dae37, line 96).

**R2 — Residual cardinality B′ (and remainder 8).**
Definition: B′ = ⌊R/9⌋ = ⌊4859/9⌋ = 539, since 4859 = 9·539 + 8; the numeral 539 does not appear on the right-hand side.
Cite: RTA manuscript lines 81–85.
Role: RTA packaging identity; links back to the R0 axiom's 539 without using it as input.

**R3 — Residual core O_res and its packaging.**
Definition: O_res is the ordered B′-core of a charge class (|O_res| = B′ = 539), with fibre blocks 68/67 and packaging L_pack = 18 + 521 = 539 under Principle (S); residual 0-class B′ = 539 under A5⁺.
Cite: `/workspace/quantum-comp/grok-chats/extracts/EXISTING-13-RESIDUAL-NOTES.md` sections R2/R3 (citing 09-architecture-a.md lines 18–35, 02-pure-math-status.md).
Role: Category A residual object that carries the packaging integers.

**R4 — Packaging–Weyl pattern PW(7,11;3⁵) selecting residual s-values.**
Definition: The packaging integers organise around 7, 11 and 3⁵ (B′ = 7²·11, window 18 = 7+11, fibre 68 = 3·11+5·7, fibre 67 = 7·11−5·2, towers 243 = 3⁵); packaging under Principle (S) selects the residual values s ∈ {7, 8, 11}.
Cite: BOOK/Discrete_Bridge_E8_to_Fifth_Order_2026-08-24.md (3290fcbc0439c2dc) §1–§2 steps 2–3.
Role: Bridge from RTA packaging to the series parameter s.

**R5 — Residual series g_s (fifth-order shape).**
Definition: g_s(q) = Σ_{n≥0} q^{n²}/(−q^s; q^s)_n; at s = 1 it has the shape of Ramanujan's fifth-order mock theta f_0; the residual values of interest are s ∈ {7, 8, 11}.
Cite: RTA manuscript Definition 6.1 (lines 131–135); Discrete_Bridge step 4.
Role: the point of contact with the fifth order.

**R6 — Orthant path counts P_s and cone series H_s.**
Definition: P_s = Σ_{n,k≥0} q^{Q_s(n,k)} (orthant path counts; P_s = (−q^s;q^s)_∞ · g_s) and H_s = Σ_{v∈Z²} w(v) q^{Q_s(v)} (cone-weighted full-lattice series), on an indefinite lattice of signature (1,1); H_s is the holomorphic projection of a Zwegers-completable indefinite theta.
Cite: RTA manuscript lines 145, 178; BOOK/Residual_Bridge_Series_C_Definition.md (98a23b037b6a7cac) lines 29–31, 98.
Role: the two indexings of the same lattice whose disagreement is the next residual.

**R7 — Bridge Series C = mismatched orthant cones (C7 at s = 7).**
Definition: C := P_orth − H_s, so P_s = H_s + C; "The coordinate orthant is not a cone chamber of the indefinite lattice … C records the residual mismatch between those two indexings of the same lattice." Explicitly C = Σ_{v∈orthant}(1−w(v))q^{Q(v)} − Σ_{v∉orthant} w(v)q^{Q(v)}. At s = 7: Orthant–Cone Mismatch Series C7 := P_orth − H7, Q(n,k) = n² + 7nk + (7/2)k(k+1), C7 = C_axis + C_third, coefficients in {0,1,1.5}, support residues 0,1,2,4 mod 7.
Cite: Residual_Bridge_Series_C_Definition.md lines 36, 73–80; Residual_Law_…_L_A_Pursuit line 31; Discrete_Bridge §1; Executive_Summary_2026-08-23_Residual_Quantum_Modular_C.md (b4fb8f53af1d148f) line 15: "after the shift to chi_nat the coordinate orthant is not a Zwegers cone … C is forced as the residual measure of the orthant-cone mismatch."
Role: 9 Maths NSFA contact ("C is the residual measure of orthant-versus-cone mismatch in the indefinite metric", Definition line 88).

**R8 — Residual shadow Ξ and residual period.**
Definition: Ξ is the residual weight-3/2 shadow (residual products of the outer disc-35 series with shifted weight-3/2 series, characteristics 7m and 7m+7/2); its formal Eichler integral plus the axis period is the residual period candidate, i.e. the residual analogue of a weight-1/2 quantum modular form's modularity error.
Cite: BOOK/Continue_Resolution_Residual_Shadow_Xi_2026-08-23.md (552541cf11545d5e) lines 12–30, 59; Executive_Summary_…_C lines 13–24.
Role: RTTC contact; maps C onto Zagier's quantum-modular paradigm.

**R9 — Residual law for C (OPEN).**
Definition: the continuous modular completion of C whose period matches the Fricke samples at 1/7, 3/7, 5/7, 1 under an exact weight-1/2 slash prefactor. Not written; status OPEN.
Cite: Residual_Law_…_L_A_Pursuit lines 63–75; RTA manuscript lines 224–226.
Role: terminal open node of the chain.

## 3. Linkage
- R0 → R1 because the residual pool is defined by subtracting f_max = 21 from the axiom-forced N_flux = 4880.
- R1 → R2 because B′ is the floor of the residual pool divided by 9.
- R2 → R3 because O_res is the ordered core of cardinality B′, packaged 18 + 521 with fibres 68/67.
- R3 → R4 because those same packaging integers factor through 7, 11 and 3⁵ and so select s ∈ {7, 8, 11}.
- R4 → R5 because the selected s-values are the parameters of g_s, whose s = 1 case is Ramanujan's fifth-order f_0.
- R5 → R6 because multiplying g_s by (−q^s;q^s)_∞ gives the orthant path counts P_s, re-indexed against the cone series H_s.
- R6 → R7 because the orthant is not a cone chamber, so P_s and H_s disagree by exactly C = P_orth − H_s.
- R7 → R8 because C is treated as a weight-1/2-type residual series whose shadow is Ξ.
- R8 → R9 because the period of Ξ has not yet been matched to the samples of C, so the residual law stays open.

## 4. Layout reading
When the work is laid out, it starts with one number from the axiom: the flux budget 4880. Take away the maximal face count 21 and what is left over, 4859, is the residual pool. Divide that leftover by nine and you get 539 without ever putting 539 in. That residual core packages as 18 plus 521, and its packaging numbers are built from 7, 11 and three to the fifth, which picks out the residual values s equals 7, 8 and 11. Those values feed the series g_s, which at s equals 1 is the shape of Ramanujan's fifth-order mock theta f-zero. When you count g_s's terms over the coordinate orthant and compare them with the cone-weighted count on the same indefinite lattice, they do not agree, because the orthant is not a cone. That disagreement is the Bridge Series C — the mismatched orthant cones, C7 at s equals 7. Its shadow Xi links it to quantum modular forms, and its full modular law is still open.

## 5. ABSENT / OPEN gaps
- ABSENT: the word "residual" in theorem-lemma-chain-9-maths.txt; no Written step there connecting a lemma to R1–R9 (links come from RTA/Bridge-C notes, which cite "the Theorem-Lemmas of the 9 Maths" as filter, NSFA/TTC/RTTC/RNT).
- ABSENT: a Written derivation of "residuals of the five master equations" → orthant cones. That framing is Owner memory framing only, not a Write.
- ABSENT: "monogen" as a Written term.
- ABSENT: an explicit Written link from RTA/C to the Resonant Path Problem Π (Owner framing only; not located in these sources).
- OPEN: residual law for C / C7 (weight-1/2 slash prefactor; quantitative Fricke match).
- OPEN: quantum modularity of g_s and C (stated as open conjecture, RTA manuscript line 226).
- OPEN: a scalar transformation law for Euler-weighted g_s even if C closes (L_A_Pursuit line 77).

## 6. Constraints footer
invent HOLD · tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 · tip_touched NO · no tip fold · Soft SF F3 CLOSED · Bridge PARTIAL READY NO · definition-only · no Owner Write CLOSED_A · no agent messaging.
