> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** In this report W means Fix(P) (Master: W_P) or the Eisenstein space (Master: V_Eis / d_Eis), depending on the source quoted. This Master copy is redacted: material on out-of-scope work (not part of the framework results) is omitted; the omissions are marked in place. Item C16 is omitted for the same reason. Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# 2026-10-18 Cross-Review — contradictions, missed patterns, Cat B methodology

Scope: every 2026-10-18 report in `heavy-daily/` (s8-s11-Analogues, C_third-Modularity, Zeta-Rational-Curve-Proof,
g_s-Closed-Forms, S-Eigenvalues, V42-Structure, Audit-and-ProfileLaw, rev3-changes-note, Tensor-Pattern-Proof/-Closure,
Cusp-Onset, H_s-Closed-Forms, C_third-Unified, Paths-A-B-C [superseded]; out-of-scope reports not listed in this Master copy) plus `bridge_c_consolidated_rev3.tex`.
Check scripts: `2026-10-18-Cross-Review/` (listed in §6). Local only; nothing pushed.

Convention used here (stated because the reports disagree, see C12): **Cat A** = exact (proved, or exact
integer/rational/symbolic computation on a stated finite set). **Cat B** = numerical (floating-point rank, PSLQ,
truncated series), conjectural, or a model fitted to data. No TPC/RH claims are made or implied.

---

## 1. Contradictions and stale statements (file : line)

| # | Item | Where | Status / resolution |
|---|------|-------|---------------------|
| C1 | s = 11 genera = 2 | s8-s11-Analogues.md:17–18 | Wrong. Disc 396 = 4·9·11 has 3 prime discriminant factors → 4 genera. Corrected in g_s-Closed-Forms.md:169 and rev3.tex:1132. |
| C2 | s = 11 "cusp rank ≥ 73, Eis ≤ 37" | s8-s11:100; rev3.tex:1130 | Superseded: W = 90, cusp = 20 (Cusp-Onset.md table; Paths-A-B-C:75 says "73+ should not be quoted"). rev3 still asserts it. |
| C3 | s = 7 label split "60 Eis-or-zero + 12 cusp" | s8-s11:93 | Superseded by Audit R3.1 / S-Eigenvalues (W = 72, V = 42 = 36+6, 30-dim complement). |
| C4 | Local exponents / local forms | V42-Structure.md:7–17 (forms x²/5, 3x²/7; raw residues) | Superseded by Tensor-Pattern-Proof (q₅ = 2x²/5, q₇ = x²/7; x₄=3a mod 4, x₅=2a mod 5, x₇=6a mod 7). 2x²/5 ≇ x²/5 (2 non-square mod 5) and 3x²/7 ≇ x²/7 (3 non-square mod 7); Closure's 2x²/7 ≅ x²/7 is harmless. Checked in cr1. |
| C5 | S vs S⁻¹ | S-Eigenvalues ("(ST)³ ≠ P on all 140"); Audit R3.7 ("(ST)³ = I on all C¹⁴⁰"); Tensor-Closure:14 (ρ(S) := S⁻¹); rev3.tex:269/275, 1127 ("(ST)³ = I", no convention) | Consistent once stated: on the stored S₇, S₈, S₁₁: S² = P, (S_lab T)³ = I, (S_lab T)³ ≠ S_lab², (S_lab⁻¹T)³ = S_lab⁻² ✓ ⇒ **S_lab = ρ(S)⁻¹** (cr1). rev3 and Audit must state this; Tensor-Pattern-Proof's "M_p ≡ S mod p" is fine on W only. |
| C6 | Three meanings of "D" at s = 11 | s8-s11:88 (70/48/198 = coordinate scale), g_s / Cusp-Onset (order discriminant 140/48/396), rev3.tex:1071 ("D = 99" = s(s−2)) | Not an error but invites mistakes; fix notation. |
| C7 | Three "Theorem G"s | C_third-Modularity:95, 265, 306 (zero-set theorem, = consolidated **Thm D**); g_s-Closed-Forms ("Theorem G" for the g_s identity); rev3 Thm G = Lewis–Zagier period | Rename locally (e.g. "Prop. Z" / "Prop. g") before rev4. |
| C8 | B(c₁,c₂) = −1/5 vs −4(s−2) | C_third-Modularity:52 vs H_s / g_s-Closed-Forms:120–123 | Different cones (quadrant cone vs H_s cone, which only share the ν₁ = 0 wall). Not a contradiction, but g_s:120–123 is H_s data, not g_s data. |
| C9 | rev3 PSLQ / "30 digits only" | rev3.tex:228–230, 443, 486, 996, 999 | Superseded: H_s-Closed-Forms gives H₀ = 0 for all s (B6/B7) and closed H_{−1/2}; cr4 confirms a_H = H_{−1/2}(7) and a_C = C_{−1/2}(7) = 0.829142617 symbolically. (Cat A modulo F1, as stated there.) |
| C10 | rev3 open item 1 contradicts its own appendix | rev3.tex:1069–1074 ("in progress", "no series check run", "s=11: D=99", "E₈ may cover each ideal twice") vs rev3.tex:1121–1123 | Stale; delete/replace in rev4. |
| C11 | rev3 cusp-onset rule | rev3.tex:1135–1138 ("cusp at 11,19,25,41…; h⁺ ≠ genera ⇔ cusp", Cat B) | Refuted: family cusp is generic for every odd s ≥ 5 (Cusp-Onset) and u_L-level counterexamples s = 14, 17, 18, 22, 23. |
| C12 | Inconsistent Cat convention | rev3.tex:111–117 and s8-s11:5 (numerics may be Cat A) vs Audit:10, Cusp-Onset:8–9, H_s:8–9, Paths:12 (numerics = Cat B) | Same object gets different labels: dim V = 42 "Cat A, numerically verified" (rev3:275) vs "numerical" (Audit:39); Lemma P "Cat A conditional" (C_third-Modularity:83) vs listed under Cat B (Audit:87). |
| C13 | **Cusp-Onset floating ranks called exact / Cat A** | Cusp-Onset.md:17 says span is Cat B, but §1.1 (l.29–33) and §6 (l.167) call V − W "exact"; §2.3 verdicts labelled Cat A rest on floating FFT character counts with a threshold and on the s8-s11 "dictionary" (itself Cat B); Paths-A-B-C:79, 137 label SVD dims [A] | **Should be Cat B.** My exact orbit bound (cr2) makes dim V an exact *upper* bound; equality with the SVD rank is still floating (and fails at s = 8, 18, 32 — see N9). Cusp-Onset-Closure's `cert_W_5_6_7_8.json` shows W is *not* certified at s = 5, 7, 8. |
| C14 | rev3 Weil erratum | rev3.tex:278, 1043 ("Weil representation on the 35-element group superseded") | Partly reversed by Tensor-Closure: S = (F₅/√5)⊗(F₇/√7)⊗S₂ exactly, i.e. Weil(2x²/5 ⊕ x²/7) ⊗ 4-dim 2-adic factor. The *old 36-component claim* was wrong; the Weil structure is right. Reword. |
| C15 | rev3 upgrades not taken | rev3.tex:275 (dim V = 42 "numerical"); rev3.tex:390 (E_{−a} = E_a "to q³⁰⁰⁰") | Now exact: V = Fix(N) ∩ Fix(γ) (Tensor-Closure) and Lemma R (C_third-Unified) proves E_{−a} = E_a for all s ≥ 5. |
| C16 | [out of scope for Master; omitted from this copy] | — | — |
| C17 | s = 8 order unit | s8-s11:31–33 ("unit ε = 2+√3" for Z[2√3]) | 2+√3 ∉ Z[2√3]; the order's fundamental unit is 7+4√3 = ε_γ. Statements are right for the maximal order only. |
| C18 | V42 §5 Cat B hypothesis "V^⊥ realised by weight-1 lifts" | V42-Structure §5 | In tension with N7: weight-1 (Zwegers) vectors are P-odd, so they cannot live in Fix(P) ⊃ V^⊥(in W). Closure shows V^⊥ ∩ W is killed by the γ-flip. Retire. |

Consistent everywhere (checked): C_{−1/2}(7) = 0.829142617 (the old 0.8174 is marked superseded wherever it appears);
T-spectrum (36 distinct values, multiplicities 1×12, 2×18, 4×6) = tensor-model T multiset (cr1); V_cusp T-values
{19,31,59,111,131,139}/140; Audit's Fix(P) = 4 + 68 = 72 and 140 = 4 + 2·68.

---

## 2. New connections (tested)

- **N1 — one improper automorph (Cat A).** Lemma E's involution φ(n,k) = (n, −2n−k−1) equals −γR_s with
  R_s = [[1,s],[0,−1]]; R_s a = −a; so Lemma E, Lemma R, V42's R and H₅ ≡ 0 are a single symmetry.
  R_s c₁ = −c₂ holds **only at s = 5**, which is exactly why H₅ ≡ 0, Q(c₁) = Q(c₂) and Δ = 9 there. Adding R_s to
  ⟨γ, −I⟩ gives **no new label relations for any s = 5..25** (cr2b): V42's "R relations = P relations" holds family-wide.
  (cr4, cr2b)
- **N2 — exact orbit-cocycle bound on dim V (Cat A bound; equality Cat B).** From u_{gα,gβ} = u_{α,β}, g ∈ ⟨γ,−I⟩, the
  number of consistent orbits is an exact upper bound. It equals the SVD dim V at 20 of 22 s in 5..25 and fails only at
  s = 8 (20 vs 18) and 18 (90 vs 84). Odd s: bound = s(s−1) and the number of zero labels = 2s−3 (12/12 odd s; Cat A on
  that set). Even s: bound = (s/2)(s/2+1), no zero labels. (cr2) Cusp-Onset-Closure's `vrank_*.json` uses the same
  orbit count (`n_orbits`) independently.
- **N3 — γ acts by a scalar on each p-part (Cat A) and the parity model (Cat B).** On the p-part of L′/Z², γ acts as
  s−1 mod p^e: −1 for p | s and +1 for p | s−2 (12 odd s, exact). This generalises "ε ≡ ±1 mod 𝔭₅, 𝔭₇". Exact:
  dim Fix(P) = 2(s−1)². Model: V = Fix(P) ∩ Fix(γ) with tensor sectors gives dim V = 3E(s)E(s−2) + O(s)O(s−2) = s(s−1),
  Eis = 3∏(p^e+1)/2, cusp = O₁O₂ + 3(E₁E₂ − all-even). This **reproduces V, W and cusp at all 12 odd s**, including the
  controls 2, 6, 12, 30, 84 and the "onset" values 72 (s=19 = 9·8), 132 (s=25 = 12·11), 758 (s=41 = 380 + 378).
  The odd⊗odd sector alone gives 72 and 132; s = 15, 17, 21, 23, 41 need the A₃-mixed sector. Consequence: family-level
  cusp ≥ (s−1)(s−3)/4 > 0 for every odd s ≥ 5. The family cusp is a **local (Weil-parity) phenomenon, not a
  class-group one**, which explains why the h⁺-vs-genera rule (C11) fails. (cr3)
- **N4 — the factor 20 (Cat A identity; meaning Cat B).** The denominator of c₀ (the q^{7/20} phase) is
  4(s−2)/gcd(s,8) = 20, 3, 36 for s = 7, 8, 11. This equals the ideal-norm factor c_s of s8-s11-Analogues, and for odd s equals
  −B(c₁,c₂) = −8Q(c₁) of the H_s cone (at s = 8 they split: 3 vs 24). Equivalently Q_s = (N𝔞 + s)/(4(s−2)) for odd s.
  (cr4)
- **N5 — residue (Cat A).** Res = arccosh(s−1)/√(s(s−2)) = log ε_s/√(s(s−2)), where ε_s = (s−1)+√(s(s−2)) is the
  fundamental Pell solution. For even s this holds in the order, not the maximal order (C17).
- **N6 — Δ and the s = 8 scale (Cat A).** Δ = (s−2)(7s−32) = 4Q(c₁)Q(c₂) = 16(s−2)² − 9s(s−2); B² − 4Q₁Q₂ = 9s(s−2);
  det(c₁,c₂) = 3; gcd(7s−32, s−8) = gcd(24, s−8) = g; gcd(7s−32, s−2) = gcd(18, s−2). Δ is a perfect square only at
  s = 5, 8, 26, 77, 365, 1178, … (< 10⁶), and Q(√Δ) ≠ Q(√(s(s−2))) for every s < 10⁶. So the H_s half-integer data live
  in a different quadratic field from the E-residue except at those s. At s = 8: H_{−1/2} = −√π/6,
  C_{−1/2}(8) = 11√π/24, and (from the in-progress H_s-Closure forms) H_{1/2}(8) = 5√π/54, H_{3/2}(8) = −175√π/324.
  So **s = 8 is the √π-rational framework scale.** (cr4, cr6)
- **N7 — three parities are one (algebra Cat A; same-ρ identification Cat B).** The label parity P = S², the cone-weight
  parity ν ↦ −ν, and integer vs half-integer radial orders coincide. A weight-k vector-valued form has
  ρ(S)²f = (−1)^k f, so the E/Eisenstein sector sits in Fix(P) (72) and the Zwegers/ϑ_hol sector in Fix(−P)
  (dim 68 = 4·(3·3 + 2·4), the mixed 5/7 parities). So Tensor's "mixed parities absent from W" is the statement that
  the half-integer/weight-1 content is exactly the P-odd complement. Cat B: that Zwegers' completed theta transforms
  under this same 140-dim ρ with the S_lab = ρ(S)⁻¹ sign.
- **N8 — rev3 constants are closed forms (Cat A mod F1).** a_H = H_{−1/2}(7) and a_C = C_{−1/2}(7) symbolically;
  h_C(0) = −√π(49−2√14)/140 is consistent. (cr4)
- **N9 — the s/2-square anomaly (Cat B, strong pattern).** The bound minus the SVD rank is 0 at s = 26, 28 (controls)
  and m(m−1) when s = 2m²: s = 8 → 2, 18 → 6, **32 → 12 (272 vs 260) and 50 → 20 (650 vs 630), both predicted in advance and stable from Q25 to Q40** (cr5).
  Cusp-Onset-Closure's independent uncertified ranks agree at s = 50 and give s = 72 → 30 (= m(m−1)). s = 98 gives 47 (not 42),
  but its run is truncation-limited (s = 51 is also short of s(s−1) by 59), so it is inconclusive. Likely mechanism: when
  s/2 is a square the 2-adic/odd local form acquires an extra isotropic/Lagrangian vector, i.e. an extra theta relation.
  Not proved.
- **N10 — weak or no link (Cat B, reported honestly).** ζ_E(0) = (s−4)(s−5)/(12(s−2)) vanishes at s = 4, 5, which
  bracket 32/7 (the root of 7s−32). No mechanism was found; treat it as a coincidence. ζ_E(0)=0 and H₅ ≡ 0 both occur at
  s = 5, but no common cause was found beyond N1 (R₅c₁ = −c₂).
- **N11 — generalisation of 140 (Cat B for s ≠ 7).** Number of labels = order of T = N_s = 4s(s−2) for odd s (checked
  at 7, 11), with SL₂(Z/N_s) ≅ SL₂(Z/4) × ∏SL₂(Z/p^e). The tensor factorisation is proved only at s = 7.

---

## 3. [Section omitted from the Master copy: out of scope]

---

## 4. Status of other in-progress folders (as of 13:28 CDT)

- `2026-10-18-Cusp-Onset-Closure/`: **in progress, no .md.** `batch2` jobs were killed. `cert_W_5_6_7_8.json`: W is not
  certified at s = 5, 7, 8. `vrank_*` uses the orbit bound with floating ranks (`certified_V: False`).
- `2026-10-18-H_s-Closure/`: **in progress, no .md.** It has H_{1/2}, H_{3/2}, H_{5/2} closed forms (`H_closed2.txt`).
  My checks (cr6): its H_{−1/2} equals the H_s-Closed-Forms formula for s = 5..29; H_{±1/2}, H_{3/2} vanish at s = 5
  (consistent with H₅ ≡ 0); s = 8 values lie in √π·Q.
  `H_x.txt` (x ≠ 0): s = 5 is exactly zero, but the s = 7, 9, 10 values are **unstable** (stability error equal to the
  value), so they must not be quoted.
- `2026-10-18-C_third-Closure/`: **in progress, no .md.** `unified_theta_check_s7.txt`: Θ̂ matches the Zwegers K₀ sign
  series to 8e−16, and the completion term vanishes for c₂ = γc₁ (because γa ≡ a mod Z²). The non-γ pair has a nonzero
  shadow, as expected. Cat B (numerical).

---

## 5. Gaps and prioritised next steps

1. **Exact rank certification** (mod-ℓ rank on integer/cyclotomic matrices) of dim V and W for all s ≤ 50, so that the
   orbit bound (N2) becomes an equality. This turns Cusp-Onset's numbers into Cat A and decides N9.
2. **Prove the odd-s parity model (N3)** via the tensor factorisation for general N_s = 4s(s−2) (N11). This would give
   dim V = s(s−1), Eis = 3∏(p^e+1)/2 and the cusp formula as Cat A.
3. **Explain the s = 2m² anomaly (N9).** Test the extra-isotropic-vector mechanism and predict the gap m(m−1) at s = 98
   with adequate truncation.
4. **rev4 erratum list** for rev3: C2, C5, C9, C10, C11, C14, C15, C17 (lines in §1).
5. **Unify the Cat convention and theorem names** (C7, C12, C13). Re-label Cusp-Onset's floating results as Cat B.
6. **Exact u_L-level criterion** (Cusp-Onset-Closure, in progress). Check whether the counterexamples 14, 17, 18, 22, 23
   are explained by the sector decomposition of N3.
7. **H_s radial data at t^{3/2} and at x ≠ 0.** Finish H_s-Closure, and fix or replace the unstable x ≠ 0 numerics.

---

## 6. Scripts (`2026-10-18-Cross-Review/`)

| File | Purpose / result |
|------|------------------|
| `family_s.py` | Copy of Cusp-Onset's family builder (dependency). |
| `cr1_T_spectrum_and_convention.py/.txt` | T multiset = tensor model; V42 raw vs true exponents; S_lab = ρ(S)⁻¹ on S₇, S₈, S₁₁. |
| `cr2_orbit_bound.py/.json` | Exact orbit bound vs SVD dim V, s = 5..25 (N2). |
| `cr2b_with_R.py/.json` | Adding R_s gives no new relations (N1). |
| `cr3_parity_model.py/.json` | γ scalars per p-part, Fix(P) = 2(s−1)², sector model for 12 odd s (N3). |
| `cr4_symbolic_links.py/.txt` | φ = −γR_s, Δ identities, gcds, c₀ denominators, residue/Pell, Δ-square s, C_{−1/2}(7), a_H/a_C (all PASS). |
| `cr5_square_halfs.py`, `cr5.log`, `cr5_square_halfs_26_28_32_50.json` | s/2-square anomaly test: s = 26, 28 gap 0; s = 32 gap 12; s = 50 gap 20 (both as predicted, stable from Q25 to Q40). |
| `cr6_Hs_closure_sanity.py/.txt` | Sanity checks of the in-progress H_s-Closure closed forms (§4). |
