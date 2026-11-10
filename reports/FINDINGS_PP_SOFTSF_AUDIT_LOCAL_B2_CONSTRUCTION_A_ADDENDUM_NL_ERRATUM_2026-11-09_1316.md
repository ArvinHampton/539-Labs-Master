# Soft SF FINDINGS: PP audit of Local B2 construction A, the Local addendum to the A-vs-B comparison, and NL's erratum

- Date: 2026-11-09, 13:16 CST (America/Chicago). Author: Professor Proof (PP), Soft SF audit lane.
- Authority: Owner DIRECT ~1:06 PM CST (relayed by Physicist): PP audits both B2 closures, and B2 stays open until they are compared. Write/derive authority: OWNER_WRITE_CALL_e9c1dbda_WRITE_DERIVE_AUTHORIZATION_2026-11-09_1300.md (33d25a79…).
- Ground rules: additive new file only. No existing file edited. Tip 7cddb188… untouched. No CERT. No outside service. Pure math only. Labels: PROVED / CONDITIONAL / OPEN / REFUTED. Refutation is by proof or counterexample only.

## 0. Inputs (sha256 verified, all MATCH)
| File | sha256 | Prefix given | Status |
|---|---|---|---|
| FINDINGS_LOCAL_DERIVE_PREV_CONSTRUCTION_A_DIRECT_SUM_ISOMETRY_2026-11-09.md ("LA") | 4b25d2edf14b887038186ac2d4b580bacb106b3811456fceeea702f08c8a783f | 4b25d2ed | MATCH |
| JOINT_LOCAL_NL_B2_CLOSURES_A_VS_B_COMPARISON_LOCAL_ADDENDUM_2026-11-09.md ("LADD") | 94973661dc30b7419bab116d261d881897d341b77e201a9d299e3021d5b433ea | 94973661 | MATCH |
| NL_ERRATUM_B2_CLOSURE_A_AND_COMPARISON_A5ii_2026-11-09_1312.md ("NLE") | 2aedc5bbb36d33015257ae4022636a2fd01840bd14045cd5b203dca38497d920 | 2aedc5bb | MATCH |
| Context: FINDINGS_PP_SOFTSF_AUDIT_NL_B2_CLOSURES_A_B_COMPARISON_2026-11-09_1309.md ("PP-1309") | f95223774c21222c9e8ca71dbf711fb1234f6fad69a553e32daf495c2245b0ce | f9522377 | MATCH |
| Context: NL_DERIVED_B2_CLOSURE_A_DIRECT_SUM_NONLOCAL_IOTA_2026-11-09_1315.md ("NL-A") | 988f1436f5c7… | 988f1436 | MATCH |
| Context: NL_DERIVED_B2_CLOSURE_B_TWO_SECTOR_HxC2_OPTIONS_M_D_2026-11-09_1315.md ("NL-B") | 5907eaf37a2b… | 5907eaf3 | MATCH |
| Context: NL_B2_CLOSURES_A_VS_B_COMPARISON_2026-11-09_1316.md ("CMP") | cd227dc78ad8… | cd227dc7 | MATCH |

Scripts: /workspace/audit-scratch/pp_b2_local_1312/checks.py (sha256 0a7d0a6ebb7932b77ccea77deec74aba26d0a967d028924a12fe712e0e6d1229). Output: checks_output.txt (ad85b0762eb4f81e8f8b6c38802eaf9a670b08592850b8ac3ccee279d7f85836).
- The script checks the Clifford algebra for the Majorana, Dirac and chiral representations.
- It runs truncated fibre models (H₊ = ℂ^{4N}, H₋ = ℂ^{8N}).
- It includes a 4³ periodic lattice free Dirac operator, H = Σ αᵏ(−iDᵏ) + βm with central differences, Π: x ↦ −x.
- Antilinear maps are stored as M∘K, so (MK)² = M M̄ and (MK)X(MK)⁻¹ = M X̄ M⁻¹.

**Notation.** A₀ := γ⁰KΠ on H₊ = L²(ℝ³)⊗ℂ⁴, and η := A₀² = γ⁰γ̄⁰. Then η = −1 in the Majorana representation and η = +1 in the Dirac and chiral representations (numpy-checked). The literal minus sector is H₋ = H₊⊗ℂ². H_tot := H ⊕ (H⊗1₂). In the Majorana representation A₀HA₀⁻¹ = −H; in the Dirac and chiral representations this fails (numpy-checked).

## 1. Item (i): Q_ι = [[0, A₀ι*],[ιA₀, 0]]
**Claim (LA result 1; LADD A-6): Q_ι² = η·diag(1, ιι*). Verdict: PROVED, under these conditions:**
- A₀ is antilinear with A₀² = η·1;
- ι: H₊ → H₋ is linear and isometric (ι*ι = 1).

**Proof.**
- Q_ι²(ψ,χ) = (A₀ι*ιA₀ψ, ιA₀A₀ι*χ) = (A₀²ψ, η ιι*χ). Here ι* is linear, so it passes through A₀ unchanged as an operator.
- ιι* is the orthogonal projection onto ran ι.
- Q_ι is isometric on H₊ ⊕ ran ι and is 0 on 0 ⊕ R, where R = H₋ ⊖ ran ι. So Q_ι is a partial antiunitary.

**Numerical check.** With a random isometry ℂ¹² → ℂ²⁴ in the Majorana representation, Q² = −diag(1, ιι*) holds, with rank 24 of 36.

**General injective ι (not isometric): PROVED (new).**
- Q_ι² = η·diag(A₀(ι*ι)A₀⁻¹, ιι*). This uses A₀XA₀ = η·A₀XA₀⁻¹, which follows from A₀ = ηA₀⁻¹.
- This is scalar iff ι*ι = 1 and ιι* = 1, that is, iff ι is unitary. Then Q_ι is antiunitary and Q_ι² = η·1.
- Numerical checks: for a random non-isometric T the formula matches and Q² is not scalar. For a unitary ι (equal-dimension stand-in), Q² = −1 and Q is antiunitary.
- A pure-swap Q with Q² = ±1 also exists for a non-unitary bijective ι, namely B = εC⁻¹ = εη·A₀ι⁻¹ (NL A-1). It is then not isometric, and it uses ι⁻¹, not ι*.
- **Consequence.** In finite dimension, and for any non-surjective isometry (for example ι_e: ψ ↦ ψ⊗e), Q_ι² = η·diag(1, P) with P ≠ 1. So B2 gets a defined square, but not ±1.

## 2. Item (ii): Local's dispute of NL A-4, and PP-1309 point (3)
**Reconciliation. PROVED: both statements hold. They answer different questions.**

(a) **Sign rule.**
- For unitary ι and C := ιA₀, we have C⁻¹ = A₀⁻¹ι* = η·A₀ι* (numpy-checked).
- By NL A-1, a pure swap has Q² = ε iff B = εC⁻¹ = (εη)·A₀ι*.
- So if B is free, either sign is reachable. That is PP-1309 point (3) / NL A-4 math, and it stands.
- If B is required to be A₀∘ι*, i.e. the same formula P_rev∘ι* in the backward direction, then ε = η. The square is fixed by the representation and does not depend on ι. That is Local's point, and it stands.
- Numerical check: B = +A₀ι* gives Q² = −1 (Majorana); B = −A₀ι* gives Q² = +1. Both are antiunitary.

(b) **Structural reason (new).**
- Q_ι = S_ι·D, where S_ι = [[0, ι*],[ι, 0]] is a linear unitary involution and D = A₀ ⊕ ιA₀ι* is the "same P_rev on each sector".
- S_ι commutes with D, so Q_ι² = S_ι²·D² = 1·η.
- The other sign corresponds to S'_ι = [[0, −ι*],[ι, 0]], with S'² = −1. These are exactly the (A)-analogues of σ_x and iσ_y in (B).
- Numerical check: Q = S_ιD, [S_ι, D] = 0, S_ι² = 1.

(c) **The same bookkeeping holds in (B).**
- P̂ = A₀⊗(UK₂) with U = [[0,a],[b,0]] gives P̂² = η·(a b̄).
- The forward map is ψ⊗e₁ ↦ b·A₀ψ⊗e₂ and the backward map is a·A₀.
- "The same formula both ways" (a = b) gives P̂² = η, exactly as B = A₀ι* does in (A).
- Fixed-t symmetry does not fix a b̄. In the Majorana representation, U = iσ_y gives P̂² = +1 and P̂(H⊗1)P̂⁻¹ = −H⊗1 (numpy-checked).

**Verdicts.**
- **PP-1309 point (3): STANDS (PROVED).** The sign is a convention when the backward map is free, for every bijective ι with B = εA⁻¹.
- **Local's claim: PROVED.** With B = A₀ι* fixed, Q² = η is forced for every unitary ι.
- **Answer to the brief's question:** a convention once B is free, forced (= η) once B = A₀ι* is fixed. The same holds in (B), with the convention parameter a b̄.
- **NL-A A-4 conclusion, "P_rev² = −1 has no mathematical content in (A) unless ι is fixed by some further structure": REFUTED by proof.**
  - Fixing ι is neither necessary nor sufficient. For every unitary ι, B = A₀ι* gives Q² = η.
  - For any fixed ι with ε free, both signs remain possible.
  - The content comes from fixing the backward formula, not ι.
- **CMP row "P² = −1: free choice in (A), forced in (B)": REFUTED by counterexample.**
  - (B) in the Majorana representation with U = iσ_y swaps the sectors, is canonical up to phase, is a fixed-t symmetry, and has P̂² = +1. So in (B) the sign is not forced by CMP's criteria.
  - In (A) with B = A₀ι*, Q² = η is forced.
  - Correct statement (PROVED): in both closures P² = η·s, where s is the relative sign of the backward map. With the same-formula convention (s = +1) and the Majorana representation (needed for fixed-t symmetry), P² = −1 in both. The two closures are on equal footing.

## 3. Item (iii): Local complement fix Q = A₀⊗(S∘K₃)
**Setup.** H₊⊕H₋ ≅ H⊗ℂ³ with slots (H₊, H₊⊗e₁, H₊⊗e₂). S is the permutation (1 2), fixing slot 3. ι = ι_{e₁}, and R = H₊⊗e₂.

**Properties (LA result 3, LADD NL-A:14 bullets): PROVED.**
1. Q is antiunitary: A₀ is antiunitary and S is a real permutation. Q² = A₀² ⊗ S S̄ = η·1 on the full space.
2. Q(H₊) = ιH₊ ⊂ H₋. Literally, Qψ = γ⁰ψ*(−x)⊗e₁, which is the Owner formula plus a constant x-independent embedding e₁.
3. Q H_tot Q⁻¹ = (A₀HA₀⁻¹)⊗1₃. This equals −H_tot iff A₀HA₀⁻¹ = −H, i.e. in the Majorana representation (for m > 0, by PP-1309's iff).
4. Q is local in the same sense as NL-A A-2: W := Q∘(ΠK) = γ⁰⊗S is pointwise constant and commutes with every M_f.
5. Q is not a pure swap. Q(R) = R, so Q(H₋) ⊄ H₊.
   - Moreover, no local antiunitary Q can map all of H₋ into H₊. That would need a fibrewise isometry ℂ⁸ → ℂ⁴ (NL-A A-2 / PP-1309 A-2 argument).

**Numerical check (4³ lattice, ⊗ℂ³, dim 768).**
- Majorana: Q² = −1, antiunitary, QH_totQ⁻¹ = −H_tot, Q∘ΠK commutes with a random M_f, Q maps H₊ into slot 2, and Q maps R → R.
- Dirac and chiral: Q² = +1, antiunitary, local, but QH_totQ⁻¹ ≠ −H_tot.

**Identity with Option M (LA §3, LADD §2): PROVED.**
- The restriction of Q to H₊ ⊕ ιH₊ equals Option M, A₀⊗(σ_xK₂), entrywise (numpy-checked in all three representations).
- So Q = M ⊕ (A₀ on R).

**Does it refute "Option M is the only closure"? Verdict, split by scope:**
- **Unrestricted claim: REFUTED by counterexample.** The claim is "Option M is the only closure in which the Owner formula holds literally (local), P² = −1, and P_rev is a fixed-t symmetry of free Dirac" (CMP:14, NLE E5, and PP-1309 line 44, which confirmed it).
  - In the Majorana representation, Q = A₀⊗SK₃ meets all three criteria on the literal space H₊⊕(H₊⊗ℂ²).
  - Its P² = −1 is "forced" in the same sense as M's. Q² scalar requires J² equal to the square on the swapped block, and the same-formula convention gives η = −1.
  - It is not Option M: it acts on fibre rank 4+8 and is not a pure swap.
  - Note: M itself uses the re-read H₋ = H⊗e₂ (rank 4), not the literal H₊⊗ℂ² (rank 8). On literalness of the space, A3 is closer to the Owner text than M.
- **PP-1309 uniqueness theorem (line 24–26): NOT refuted, PROVED in its exact scope.** The scope:
  - space 𝓗 = H⊗ℂ² (equal fibre ranks 4/4);
  - P̂ = (γ⁰Π⊗U)K with U ∈ U(2) constant and anti-diagonal (pure sector swap);
  - hypotheses P̂² = −1 and P̂(H⊗1)P̂⁻¹ = −H⊗1, with m > 0.
  - Conclusion: Majorana class and U = e^{iθ}σ_x.
  - A3 lies outside the hypotheses (rank 4+8, not anti-diagonal), so it is consistent with the theorem.
- **Extension (new, PROVED).** On H⊕H, take any pure-swap antiunitary Q whose forward map is the literal C = A₀ (into the H⊗e₂ copy).
  - NL A-1 forces B = εC⁻¹ = εη·A₀. So Q is automatically of tensor form, with U = [[0, εη],[1, 0]].
  - A fixed-t symmetry with H₋ = H forces A₀HA₀⁻¹ = −H, i.e. Majorana (η = −1).
  - P² = ε is then a choice, with ε = −1 ⇔ U = σ_x.
  - So within pure swaps with a literal forward map, M is unique given P² = −1. P² = −1 is selected, not forced.
  - Uniqueness for pure swaps with a non-literal forward map (an x-dependent fibre unitary u(x) composed with A₀) is OPEN.
- **NL-A:14, "a local version needs equal fibre ranks, i.e. closure (B)": PROVED within NL-A's stated anti-diagonal setup (NL-A A-2), REFUTED unscoped (counterexample A3).**

## 4. Item (iv): finite-dimensional REFUTED claim
**Claim refuted (LA result 2):** "On the literal finite-dimensional H₊⊕(H₊⊗ℂ²), an anti-diagonal sector-swapping P_rev with P_rev² = ±1 exists." **Verdict: REFUTED by proof. Local's proof is PROVED and correct.**

**Proof.**
- Write Q = [[0,B],[C,0]] with B, C (anti)linear. Then Q² = diag(BC, CB).
- Q² = ε·1 forces BC = ε·1_{H₊} and CB = ε·1_{H₋}.
- So C is injective and surjective, and a bijection preserves complex dimension even if antilinear. That forces dim H₋ = dim H₊, contradicting dim H₋ = 2·dim H₊ = 2n with 1 ≤ n < ∞.
- Even "Q² invertible" is impossible.

**Quantitative strengthening (new, PROVED).**
- rank(CB) ≤ n, so by Eckart–Young ‖CB − ε·1_{2n}‖_F ≥ √n, with equality for CB = ε·(rank-n projector).
- Numerical check, n = 4: the random minimum is 18.39 ≥ 2, and the projector attains exactly 2.000.

**Notes.**
- No file asserted the refuted statement. The REFUTED label settles a candidate reading of B2.
- The result is consistent with PP-1309 A-2 and the earlier B2 rank obstruction (PP 1304).
- The obstruction disappears in infinite dimension (LA result 5, a unitary ι exists) or without the anti-diagonal form (A3).

## 5. Other Local claims (LA and LADD)
- **LA result 4 (no Kramers tensor complement): PROVED.**
  - Q = A₀⊗VK₃ has Q² = η·VV̄. VV̄ = −1₃ is impossible because det(VV̄) = |det V|² > 0 while det(−1₃) = −1.
  - Numerical check: min ‖VV̄ + 1‖ over 20 000 random U(3) is 2.003. On ℂ², (iσ_y)(iσ_y)‾ = −1.
  - A non-tensor J with J² = −1 on R exists, since R is infinite-dimensional and separable. Whether the Owner wants such a J is OPEN.
- **LA result 5 (Q_U with unitary U swaps sectors, Q_U² = η): PROVED.** See §1.
- **LA result 6 (no unitary ι is x-local): PROVED.**
  - The commutant of L^∞ consists of the decomposable operators, so ι(x): ℂ⁴ → ℂ⁸ would be an isometry, which is never surjective.
- **LA result 7 (H ≅ H⊗1₂, existence of an intertwining unitary ι): PROVED (existence).**
  - By Foldy–Wouthuysen, H is unitarily equivalent to multiplication by ±ω(p).
  - Both H and H⊗1₂ are absolutely continuous on (−∞,−m]∪[m,∞) with uniform multiplicity ℵ₀ (level sets of ω are spheres), so Hahn–Hellinger applies. This also holds for m = 0.
  - An explicit intertwiner is OPEN.
  - In the Majorana representation, H₋ = −ιA₀HA₀⁻¹ι* = ιHι*. For the intertwining ι this is the local H⊗1₂.
  - The existence is intrinsically infinite-dimensional, since no finite truncation has equal dimensions.
- **LADD A-5(ii) dispute: CONFIRM (PROVED).** It is the same counterexample as PP-1309 A-5(ii).
- **LA §3 / LADD M-vs-D, "bare operators equivalent, pairs inequivalent": PROVED.**
  - Separable infinite-dimensional quaternionic structures (J² = −1) are unique up to unitary equivalence.
  - QHQ⁻¹ = −H is invariant under joint unitary conjugation. M satisfies it; D (Dirac representation) does not.
  - LA §3's LD-A3(Dirac) vs D inequivalence (squares +1 vs −1): PROVED.
- **LADD §4 status (B2 CONDITIONAL on the Owner's choice among four candidates): CONFIRM.**

## 6. NL erratum 2aedc5bb vs PP-1309
- **E1 (A-5(ii) withdrawn, REFUTED; Foldy–Wouthuysen / Hahn–Hellinger proof): CONFIRM.** It matches PP-1309 A-5(ii) exactly, including ι = V and A = V∘A_M.
- **E2 (fixed-t symmetry with local H₋ for a suitable non-local ι PROVED; Hermite-ι locality OPEN): CONFIRM.**
- **E3 (comparison row correction): CONFIRM in substance, with a minor quotation fix.**
  - The CMP table cell actually reads "Only with non-local H₋". The phrase "requires non-local −U dynamics" is in the CMP assessment line.
  - Both are superseded by E3's replacement, which matches PP-1309 line 42.
- **E4 (sharper Option M uniqueness): CONFIRM, with the exact scope of §3.** P̂² = −1 is a hypothesis that selects U = e^{iθ}σ_x; it is not an output.
- **E5 ("Option M remains the only closure that meets all three criteria"; "(A) fails because P² is a convention"): REFUTED as stated.**
  - (1) The "forced vs convention" criterion does not discriminate between (A) and (B) (§2).
  - (2) Local A3 meets all three criteria (§3).
  - Corrected statement: "Option M is the unique pure-swap, equal-rank, tensor-form closure with P̂² = −1 and fixed-t symmetry. On the literal rank-4/8 space, Local A3 (= M ⊕ A₀|_R, not a pure swap) meets the same three criteria." The (A) pure-swap closure with unitary ι differs from both by needing a non-local ι.

## 7. Errata to PP's own PP-1309 (f9522377): an erratum IS needed (additive, recorded here; f9522377 is not edited)
- **PP-E1 (line 44).** "NL's assessment stands … Option M remains the unique closure meeting all three criteria (literal local formula, forced P² = −1, fixed-t symmetry)" is WITHDRAWN. It is REFUTED by counterexample (Local A3, §3) and by the non-discriminating sign criterion (§2). Replace it with the corrected statement in §6, E5.
- **PP-E2 (line 33, A-4).** The statement "So P² = ±1 is a convention in (A)" stays PROVED. Add: "It is equally a convention in (B) (a b̄ free). In both, the square is forced to η once the backward map is fixed to the same formula (B = A₀ι* in (A), a = b in (B))."
- **PP-E3 (lines 24–26), scope clarification only, no change of verdict.** The uniqueness theorem is scoped to 𝓗 = H⊗ℂ², P̂ = (γ⁰Π⊗U)K with constant anti-diagonal U, and m > 0. P̂² = −1 is a hypothesis. It does not cover non-pure-swap closures on the literal 4/8 space.
- **PP-E4 (line 31, A-2), scope note.** The Hahn–Hellinger obstruction applies to bijective inter-sector maps (pure swaps). It does not exclude a local non-swap Q such as A3.
- All other PP-1309 verdicts stand: B-1 to B-4, Option M, the σ_z remark, Option D, A-1 to A-3, A-5(i), A-5(ii) REFUTED, A-5(iii), A-6, and the Fixed-t row correction.

## 8. B2 status
- The comparison the Owner required is now complete on PP's side: (A) NL, (A) Local LA/LA3, (B) M/D, and the Local addendum have all been audited.
- **B2 is still NOT closed: CONDITIONAL on Owner adoption.** The mathematically valid candidates are:
  1. (B)-M on H⊗ℂ² with re-read H₋ (Majorana, P² = −1, fixed-t symmetry, local, pure swap);
  2. Local A3 on the literal H₊⊕(H₊⊗ℂ²) (Majorana, P² = −1, fixed-t symmetry, local, not a pure swap; R is mapped to itself);
  3. (A) pure swap with unitary non-local ι (P² = η with the same-formula convention; fixed-t symmetry with local H₋ for an intertwining ι, whose explicit form is OPEN);
  4. (B)-D (Dirac representation, P² = −1, not a fixed-t symmetry).
- Candidates 1 and 2 meet the three CMP criteria on equal footing. They differ in literal H₋ rank and in pure-swap structure, and that choice is the Owner's.
- No CERT. PP does not close B2.

## 9. Rollup
**PROVED 14:**
1. (i) Q_ι² = η·diag(1, ιι*);
2. (i) general-ι formula; scalar ⇔ unitary;
3. (ii) reconciliation and S_ι·D factorization;
4. (ii) the same η·s bookkeeping in (B);
5. (iii) A3 properties 1–5;
6. (iii) A3 = M ⊕ A₀|_R;
7. (iii) PP uniqueness in exact scope, plus the literal-forward-map extension;
8. (iv) Local's finite-dimensional proof, plus the Eckart–Young bound;
9. LA result 4;
10. LA result 6;
11. LA result 7 (existence);
12. M/D bare vs pair;
13. LADD A-5(ii) dispute;
14. NLE E1–E4.

**CONDITIONAL 1:** B2 adoption among the four candidates (Owner's choice; this includes whether a non-pure-swap P_rev acting on R is acceptable).

**OPEN 6:**
1. explicit intertwining ι;
2. locality of H₋ under the Hermite ι;
3. a non-tensor Kramers J on R in the Dirac representation (whether the Owner wants it);
4. the Owner's exact H_{+U};
5. uniqueness for pure swaps with a non-literal forward map;
6. physical reading.

**REFUTED 5:**
1. NL-A A-4 conclusion ("no content unless ι is fixed");
2. CMP row "P²: free in (A), forced in (B)";
3. the unrestricted "Option M is the only closure meeting all three criteria" (CMP:14 / NLE E5 / PP-1309 line 44);
4. NL-A:14 unscoped ("local needs equal ranks");
5. the anti-diagonal P_rev with P² = ±1 on the literal finite-dimensional sum.

PP-1309 erratum: YES (PP-E1 withdrawn claim; PP-E2 to PP-E4 scope clarifications), recorded in §7.

No CERT. REPORTS ONLY. Tip 7cddb188… untouched.
