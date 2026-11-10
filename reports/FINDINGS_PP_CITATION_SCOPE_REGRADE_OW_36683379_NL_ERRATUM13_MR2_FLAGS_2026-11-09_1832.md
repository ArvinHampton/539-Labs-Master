# PP citation-scope note under OW 36683379: regrade of the source-limited marks, and audit of NL erratum 13 and MR2's narrowing flags
Author: Professor Proof (PP). Audit only. Additive new file. No CERT. Nothing adopted. Nothing sent. Tip 7cddb188 untouched.

**Rule.** OW 36683379 (18:15) amends 3f160803. Its sha 36683379e18a… equals its sidecar (MATCH).
- Any source may be cited.
- The grades used are: **cited, math-checked** · **cited, math-unchecked (CONDITIONAL)** · **REFUTED**.
- A citation alone never gives PROVED.

**PP scripts** are in /workspace/audit-scratch/pp_1818_audit/, each with a sidecar:
- pp_1818_checks.py (77d1c85b…) and pp_1818_checks.log (73e7b33b…)
- autcheck_rerun.log (9401128d…) and mathcheck_rerun.log (67186319…)

**Bibliographic data** were checked against Crossref records (api.crossref.org) on 2026-11-09 at about 18:25 CST.

## A. Integrity
- A1 [PROVED] NL_ERRATUM13_CITATION_MATH_CHECKS_OW_36683379_2026-11-09_1818.md = b5190ea8c908200f8dab6455bcd4462143cad8b4e01993c88425c925be003412 = its sidecar.
- A2 [PROVED] MR2_SOURCE_LIMIT_NARROWING_FLAGS_ALL_SOURCES_PER_OW_36683379_2026-11-09.md = a40843225c36e0010ba82375ab440f6ef23eac685aa49aa419caeac7515fce8b = its sidecar. The sidecar carries an absolute path, but the hash agrees.
- A3 [PROVED] All four files in /workspace/nl-junction-1817/ equal their sidecars. PP reran autcheck.py and mathcheck.py, and both outputs are **byte-identical** to NL's logs.
- A4 [REFUTED, bookkeeping] E13's header assigns the hashes to the wrong files. On disk:
  - **autcheck.py = fce1f08f…** and **mathcheck.py = be56e69c…**
  - **autcheck_1821.log = 9401128d…** and **mathcheck_1820.log = 67186319…**
  - E13 states the reverse pairing for both the scripts and the logs. The files themselves are intact.
- A5 [PROVED] The local text /workspace/nl-twist-1609/1203.0303.txt contains (2.12) p=(1+z)(g−1), q=(1−z)(g−1) and (2.13) z = n/(g−1), n∈ℤ.

## B. NL erratum 13: the PROVED re-derivations
**B-M1 SSU reduction [PROVED, agree; math-checked].**
- In flat coordinates, dx₁²+dx₂²+dr²+r²dθ² = r²[(dx₁²+dx₂²+dr²)/r² + dθ²] = r²(g_{H³, upper half-space} + dθ²).
- 4D YM is conformally invariant (Ω⁻⁴·Ω⁴ = 1), and S⁴∖S² ≅_conf ℝ⁴∖ℝ² by stereographic projection.
- M2, the min–max existence, stays **cited, math-unchecked CONDITIONAL**.

**B-M3 Sadun–Segert orbits [PROVED, agree].** The irreducible SO(3) acts on the unit traceless symmetric 3×3 matrices.
- Distinct eigenvalues give stabilizer ℤ₂×ℤ₂ and a 3-dimensional orbit.
- A double eigenvalue gives stabilizer O(2) and a 2-dimensional orbit (ℝP²).
- The action is cohomogeneity 1.

**B-M4 C₂ values [PROVED, agree, and strengthened].**
- Write n± = 2a+1, 2b+1. Then C₂ = (n₊²−n₋²)/8 = T_a − T_b, where T_k = k(k+1)/2 and a, b ≥ 1. This is a sum of consecutive integers b+1…a, all ≥ 2.
- **Exactly the integers ℤ∖{±1} are attained, with no bound at all:**
  - m ≥ 2 is attained by (n₊, n₋) = (2m+1, 2m−1);
  - 0 is attained by a = b;
  - ±1 is impossible, because no run of integers starting at ≥ 2 sums to 1;
  - negative values follow by swapping n₊ and n₋.
- So "except ±1" is right, and "[−60, 60]" undersells the result. PP also checked by enumeration on [−2000, 2000].
- The count rule "number of odd divisors of |C₂| minus [|C₂| triangular]" equals the pair count. This is the classical odd-divisor count of consecutive-sum representations, minus the run that starts at 1. PP checked it for m = 1…300; m = 45 gives 5.
- The sign convention is opposite to MR2's (n₋²−n₊²)/8. This is orientation only.
- M5, the ODE existence and Prop. 2.5, stays **math-unchecked CONDITIONAL**.

**B-M6 Taubes hypotheses [PROVED as stated; scope fix].**
- H²(S⁴) = 0, so b⁺ = 0 for any metric. π₁(E₈) = 0. π₃(E₈) = ℤ.
- **Against the weighted fibre:** Taubes is about the *unweighted* ASD equation for the conformal class of g₄. On the weighted static problem, Y6-vanish (PROVED given J1) shows that smooth static SD/ASD fields vanish identically. So Taubes contributes **nothing to Y14**. E13 already limits M7 to the unweighted problem, but M6 must say this too (fix 2).
- M7 stays **math-unchecked CONDITIONAL**.

**B-M8 BLS Thm 4.2 [PROVED, agree, with clarification].** The manifold is the **round S⁴** and the bundle is the **SO(4) frame bundle (TS⁴)**.
- R^{ab} = e^a∧e^b, and ∇R = 0, so the connection is YM.
- Under so(4) = su(2)₊ ⊕ su(2)₋, PP verified numerically that the su(2)₊ part of the curvature is SD and the su(2)₋ part is ASD.
- So the Levi-Civita connection is **reducible**. It is the BPST-type instanton on S₊ ⊕ the anti-instanton on S₋. It is non-SD only as an so(4) field, and each spinor-bundle piece is BPS.
- E13's argument ("⋆ sends e_a∧e_b to e_c∧e_d, a different so(4) component") is correct. It must add that the spinor pieces are individually SD and ASD (fix 3).
- M9 (Thm 4.1) stays **math-unchecked CONDITIONAL**.

**B-M10 embedding [PROVED, agree].**
- An injective Lie-algebra homomorphism ι gives F′ = ι(F) and D′⋆F′ = ι(D⋆F), and preserves SD/non-SD.
- At bundle level a group homomorphism SU(2)→E₈ is needed. It exists because SU(2) is simply connected.
- The instanton number scales by the Dynkin index of ι, which is 1 for the minimal embedding. Add this (fix 4).

**B-PP2, a new item [PROVED; math-checked, elementary].** Non-BPS E₈ YM fields exist on the round (unweighted) S⁴ for **every** charge k, with no SSU or Sadun–Segert input.
- E₈ ⊃ SO(16) ⊃ SO(4)×SO(12), and Spin(4) = SU(2)₁×SU(2)₂ (commuting).
- Take a BPST charge-k₁ instanton in SU(2)₁ and a charge-k₂ anti-instanton in SU(2)₂. Then [A₁, A₂] = 0, F = F₁+F₂, and D⋆F = 0.
- F is non-SD, with charge k₁−k₂ and energy ∝ k₁+k₂ > |k₁−k₂|.
- This upgrades the *existence* half of 1800 Y12 (round, unweighted). It says nothing about stability, and nothing about Y14 (weighted), which stays OPEN.

**B-M11 [CONDITIONAL, agree; PP adds a partial math check].**
- Suppose the squashed metric's isometries in SO(5) preserve the quadratic form diag(X₀, X₁, X₁, X₂, X₂).
- Then by Schur's lemma the irreducible SO(3) cannot preserve it unless all X_i are equal (round).
- The non-linear isometries are not excluded, so the grade stays CONDITIONAL (math-checked for the linear part).
- The transfer note (each φ_i rotation fixes the S² {μ_i = 0}) [PROVED, agree].

**B-M12 Bolza 3.0571 [PROVED, agree; math-checked].**
- For a regular hyperbolic n-gon with interior angle α, cosh(inradius) = cos(α/2)/sin(π/n) = cot(π/8) at n = 8, α = π/4. So the length is 2 arccosh(1+√2) = 3.0571418390.
- For these values the side length is the same (cosh(s/2) = cos(π/n)/sin(α/2)), and E13 uses that.
- MR2's alternative 4 arccosh(csc(π/8)/2) is **exactly** equal: cosh 2y = csc²(π/8)/2 − 1 = 1+√2.

**B-M13 and B-M14 [CONDITIONAL, agree; now numerically math-checked].**
- PP built the Bolza group: A_k = R^k A R^{−k} with α = 1+√2, β = √(2+2√2). The octagon relation a₀a₁⁻¹a₂a₃⁻¹a₀⁻¹a₁a₂⁻¹a₃ = 1 is verified.
- Over all reduced words of length ≤ 6, the smallest cosh(ℓ/2) values are 1+√2 and 3+2√2, so ℓ = **3.05714 and 4.89690**, followed by 5.828, 6.114, ….
- This supports the systole value and confirms the second length. It is not a proof, since the words are bounded.
- Global maximality (Jenni) stays **math-unchecked CONDITIONAL**.

**B-M15 |Aut⁺| ≥ 48 [PROVED, agree].** Rerun confirmed the order-24 octahedral group, the lifts y → c·y/(cx+d)³, and the hyperelliptic involution.

**B-M16 equality |Aut⁺| = 48 [PP grade: cited lemma, otherwise math-checked; CONDITIONAL].**
- PP enumerated every Möbius map that sends 0, 1, ∞ into the branch set {0, ∞, ±1, ±i}. Exactly **24** preserve the set, so the stabilizer is exactly the octahedral group.
- Together with the uniqueness and centrality of the hyperelliptic involution (standard, e.g. Farkas–Kra III.7; not re-derived), this gives |Aut⁺| = 48.
- Complex conjugation preserves y² = x⁵ − x, so |Isom| = 96.
- The only remaining dependency is that one textbook lemma.

**B-M17 [REFUTED, agree].** The "21 → 42" line is a deduplication bug. The rerun log gives 24 → 48.

**B-M18 BBBW [PROVED given the BBBW parameterization, agree].** Checked against the local text (A5). For g = 2, z = n ∈ ℤ.

**B-M19 HW and related [CONDITIONAL, agree], with a flag.** Conrad and Lü give η = (4π)⁵ = 8×HW (see PP-1 in the 1826 file). With that value u = 1, not 2.

**Is the CONDITIONAL list honest? [PROVED: yes].**
- M2, M5, M7, M9, M13, M19 are genuinely unchecked proofs.
- M14 can now be upgraded to "numerically checked, CONDITIONAL".
- M16 is now "math-checked except one lemma".
- Nothing marked PROVED rests on a citation alone.

**Tallies.**
- E13: 10/9/0/1 = 20 [PROVED]. The arithmetic is right and the lists match.
- 1800 after E13: 15/11/3/2 = 31 [PROVED]. 13+2 PROVED (M12, M15), and Γ2 is kept as one CONDITIONAL item.
- PP-proposed further revision, not adopted: split Y12 into Y12-exist-round (PROVED via B-PP2) and Y12-SSU/SS (CONDITIONAL). That would give 16/11/3/2 = 32.

## C. MR2 narrowing flags (a40843225c36…)
- C1 [PROVED] bibliographic, Crossref:
  - SSU, "Solutions to Yang—Mills equations that are not self-dual", PNAS 86 (1989) 8610–8613, doi 10.1073/pnas.86.22.8610 ✓.
  - Sadun–Segert, "Non-self-dual Yang-Mills connections with nonzero Chern number", Bull. AMS 24 (1991) 163–170, doi 10.1090/S0273-0979-1991-15978-1 ✓.
  - Sadun–Segert, "…with quadrupole symmetry", CMP 145 (1992) 363–391 ✓. Its DOI is **10.1007/BF02099143**, which MR2 omits.
  - BLS, "Stability and gap phenomena for Yang-Mills fields", PNAS 76 (1979) 1550–1553, doi 10.1073/pnas.76.4.1550 ✓.
  - The follow-on is **Bourguignon–Lawson** (no Simons), "Stability and isolation phenomena…", CMP 79 (1981) 189–230 ✓.
  - Taubes JDG 17 (1982) 139–170, doi 10.4310/jdg/1214436701 ✓.
- C2 [REFUTED as the pin for Y12]. MR2 calls Taubes "likely CMP 'Stability in Yang-Mills theories' (10.1007/BF01211160)". That is CMP 91 (1983) 235–263, a different paper. NL's Y12 claim (b⁺ = 0 ⇒ ASD existence) is **JDG 17 (1982) 139**, which MR2 lists only as an alternative.
- C3 [PROVED with fix]. Jenni is Comment. Math. Helv. 59 (1984) 193–203, doi 10.1007/BF02566345. It is located, but the primary was not read. MR2's "1981/1984" should read 1984. The 1979 CMH 54 paper by Jenni is a different one.
- C4 [PROVED]. MR2's stated contents (SSU min–max, charge 0; SS Theorem 1, n± ≠ 1; BLS weak stability ⇒ SD/ASD on S⁴, instability on Sⁿ for n ≥ 5) agree with NL's E13 M2, M5 and M9.
- C5 [PROVED]. MR2's SS sample values (3,3)→0, (3,5)→2, (5,7)→3, (1,3)→1 are correct in MR2's (n₋²−n₊²)/8 convention, read as (n₊, n₋). (1,3) is exactly the excluded n = 1 case, consistent with B-M4.
- C6 [PROVED]. The Bolza numbers and the exact identity are confirmed (B-M12, B-M14).
- C7 [CONDITIONAL, search report]. F1–F3 (7/20, β(κ)) are still ABSENT. This is a search outcome, not a theorem. It is accepted as reported and was not re-searched by PP.
- C8 [PROVED]. 11 flags (F1–F11) and 4 "no-narrowing" notes are counted. No item is upgraded to PROVED by citation, which is consistent with the rule.
- C9 [PROVED, cross-check]. MR2's "math check pending" on SSU, SS and BLS is superseded **step by step** by E13 (M1, M3, M4, M8 math-checked). The headline existence and stability theorems (M2, M5, M9) remain pending in both files, so there is no contradiction. MR2's F11 (its Bolza wall file) now inherits: length math-checked; Aut⁺ = 48 math-checked except one lemma; global maximality pending.

## D. Regrade of earlier PP marks
**fe0c3d92 (PP 1807)**, the line-40 compliance note, item Y12 (line 59) and fix 8:
- The "non-arXiv, unverified under the rule" marks are **withdrawn as origin-based**. The replacements are:
  - **Y12:** existence on the round S⁴ is PROVED via B-PP2 (elementary). The SSU and SS specific families are math-checked for the reduction and the combinatorics (M1, M3, M4) and math-unchecked for existence (M2, M5). The Taubes hypotheses are checked (M6); the conclusion is math-unchecked (M7) and is irrelevant to the weighted problem.
  - **Y13:** math-unchecked CONDITIONAL (M9). The BLS 4.2 example is checked (M8).
  - **Γ2:** length PROVED; second length numerically checked; Aut⁺ = 48 checked except one lemma; Jenni maximality math-unchecked CONDITIONAL.
  - **Y1 (HW λ):** math-unchecked CONDITIONAL, contested (PP-1).
- Erratum-12 item 8 is regraded the same way.
- The 1711/erratum-7 fix 7 (BBBW z ∈ ℤ for g = 2) moves from cited CONDITIONAL to **PROVED given the BBBW parameterization** (M18).

**Other PP files from 2026-11-09** (1530, 1702, 1704, 1730, 1750, 1753/1754, 1757) were scanned.
- No origin-based marks were found. The single hit, in 1530 (the OW c290a274 record), is an on-disk record reference, not a source scope issue.
- Citations that were arXiv-title-checked there are now read as "cited, math-unchecked CONDITIONAL" unless the item says the math was checked. No grade changes.

## Fixes
**NL** (additive erratum 14):
1. Swap the E13 header hash labels (A4).
2. M6: state that Taubes applies to the unweighted problem only, and that Y6-vanish excludes SD on the weighted one.
3. M8: the manifold is round S⁴ on TS⁴; the connection is reducible, with SD on S₊ and ASD on S₋.
4. M10: add the group-level embedding and the Dynkin index.
5. M4: state the exact attained set ℤ∖{±1} (all integers), with the proof.
6. M14 → numerically checked (words ≤ 6). M16 → math-checked except hyperelliptic-involution uniqueness.
7. Consider B-PP2 for Y12; record it as a proposal.
8. M19/Y1: add the Conrad/Lü normalization (u = 1).

**MR2:**
1. Pin Taubes to JDG 17 (1982) 139–170 for Y12, and drop the CMP 91 "likely" (C2).
2. Jenni = CMH 59 (1984) 193–203, doi 10.1007/BF02566345.
3. Add the CMP 145 DOI 10.1007/BF02099143 and name Bourguignon–Lawson for CMP 79.
4. State the SS sign convention, and that (1,3) is the excluded case.
5. Mark SSU, SS and BLS steps as superseded by NL E13 math checks where they apply (C9).

## Rollup (this file)
PROVED 30 · CONDITIONAL 10 · OPEN 0 · REFUTED 3 = 43
- **PROVED (30):**
  - A1, A2, A3, A5
  - B-M1, B-M3, B-M4, B-M6, B-M8, B-M10, B-PP2, M11-transfer, B-M12, B-M15, B-M18
  - CONDITIONAL-list honesty, E13 tally, 1800-31 tally
  - C1, C3, C4, C5, C6, C8, C9
  - D-1807 regrade, D-E12 regrade, D-BBBW regrade, D-scan
  - OW 36683379 sha
- **CONDITIONAL (10):** B-M2, B-M5, B-M7, B-M9, B-M11, B-M13, B-M14, B-M16, B-M19, C7
- **REFUTED (3):** A4, B-M17, C2

Tip 7cddb188 MATCH before and after. No CERT. No message sent. Nothing adopted. Y14 stays OPEN and was not touched.
