# Residual identities vs. Ramanujan / mock theta literature — status report
Date: 2026-10-17 (America/Chicago). Read-only pass: nothing was pushed, emailed, or sent. Scripts and tables: `2026-10-17-mock-theta-check/` (coeffs.py, coeff_table.txt, miss7.py, miss7.txt, oeis.txt).

## 1. Master tip
- The tip has moved. It is now **48684e3e43326733c9a08dba15e6556f6396de0e**, "Add pursue-all after Nu_res limitation lifted", committed 2026-10-14 21:40 CDT. The Sep 14 tip was 9c341c2.
- Commits after Sep 14 that matter here: 3de76f6 (Oct 3: "Kernel construction for Remark 8.5. No kernel. Slash_two empty."), e18ca14 (Oct 13: `42_Discrete_Contacts.md`, 40/42 locked, Remark 8.5 open, Nu_star EMPTY), and 1bd3d9c…48684e3 (Oct 14: Nu_res Category B writing). None of these adds a residual identity. All open-path statuses below still hold on the tip.
- Local clone: /workspace/quantum-comp/oct17-master (depth 30).

## 2. What Master writes (Q1)
All paths are under `docs/S2-11DM2ET-X-Axiomatic-Book/`. The file SHA is the last commit touching that file (`git log -1`).
- **g_s.** `42_Discrete_Contacts.md` (e18ca14), contact 23: g_s = Σ_n q^{n²}/(−q^s;q^s)_n, "mixed scale", s ∈ {7,8,11}. In coefficient form, g_7(d) = Σ_n φ_n((d−n²)/7) with φ_n(m) = [x^m]∏_{j≤n}(1+x^j)^{−1}. This agrees with the locked definition.
  - `U1_LEDGER_PATH2_OR_QM_…_2026-09-14.md` and `U1_LEDGER_G7RAD_OR_ZAGIER_COCYCLE_…_2026-09-21.md` both say "Square at scale 1. Pochhammer at scale s. Not f_0(q^s)."
  - `OccFilt_7_Occupancy_Filter_Definition_2026-09-02.md` says "g_7 is not f_0(q^7)".
  - `Advancements_Wrap_2026-09-22_QM_GS_Theorem_Pursuit.md` (3de76f6) says "g_1 and g_2 remain the only specializations with published quantum modularity" and "f_0 and phi are not g_7".
  - Master gives **no Hecke-type or indefinite-theta form for g_7, g_8 or g_11.**
- **H_s / Bridge Series C** (contacts 25–28). H_s is the "cone-signed, Zwegers-completable piece". C = P_orth − H_s = C_axis + C_third, with coefficients in {0, 1, 1.5}. C_axis = 3/2 + Σq^{n²} + Σq^{7k(k+1)/2}. C_third lives on the quadratic form Q_minus = n² + 7nk + (7/2)k(k−1): signature (1,1), det −35, discriminant 35. The Xi shadow is weight 3/2.
  - Master gives no Θ_third completion formula. I found no `Theta_third :=` definition.
  - QM_Theta_C_Axis is discussed in `Open_Paths_After_QM_Theta_C_Axis_2026-09-21.md`.
- **residual_slash** (contact 34; `U1_LEDGER_P_SLASH_Remark85_Interp_Prod_Obstruction_2026-09-01.md`, 3de76f6). residual_slash(x) = |7x|^{−1/2}·residual_factor(x), where residual_factor = a + bt + ct² + d/(1+t²) and t = 7x − 3.
  - The coefficients a, b, c, d (≈10.6923, 0.2160, 2.7618, −7.5316) come from interpolation at the four samples x = 1/7, 3/7, 5/7, 1. The interpolation determinant is 36.14118.
  - W_7(x) = −1/(7x). Auto_prod_W7 = 1/√7 exactly (a2532a6).
- **U7.** `U1_LEDGER_U7_CLOSURE_Thm04_Continuous_Extension_Slice_2026-09-12.md` and `Go_U7_Q24_Is_Hecke_Cell_02_2026-09-10.md` write the signed f_{2,8,8}(q, q^8, q). Master states it "is not C, not P_orth, not g_8, not Slash_two".

## 3. Category A — verified facts
A1. The Master tip is 48684e3, dated 2026-10-14 (atom feed plus clone).

A2. **g_1 = Ramanujan's 5th-order f_0(q)** and **g_2 = Ramanujan's 3rd-order φ(q)**. These hold by definition, since f_0(q) = Σq^{n²}/(−q;q)_n and φ(q) = Σq^{n²}/(−q²;q²)_n.
- Citation: Hickerson–Mortenson, arXiv:1208.1421 (2012/2014), eqs. (4.5) and (4.11), which also give Appell–Lerch forms. Verified on the arXiv page.
- Coefficient check: my computed series match OEIS A053256 (f_0) and A053250 (φ). This agrees with Master 3de76f6.

A3. **No known identification exists for s = 7, 8, 11**, either on Master or in the classical lists I checked. The base mismatch (q^{n²} against Pochhammer base q^s) puts g_s for s ≥ 3 outside the classical Eulerian families: Watson; Andrews–Berndt LN Parts I–V; Gordon–McIntosh orders 2, 3, 5, 6, 7, 8, 10. This is a statement about the absence of a known identity, not a proof that no mock-modular structure exists.

A4. **There are no classical 11th-order mock theta functions.** The Gordon–McIntosh survey (Partitions, q-Series and Modular Forms, Dev. Math. 23, Springer 2012, pp. 95–144) covers orders 2, 3, 5, 6, 7, 8, 10, according to its abstract and listing. Ramanujan's 7th-order 𝓕_0, 𝓕_1, 𝓕_2 and the Gordon–McIntosh 8th-order S_0, S_1, T_0, T_1, U_0, U_1, V_0, V_1 exist; HM2014 §4, eqs. (4.32)–(4.42), give their Appell–Lerch forms. "Order" is unrelated to the scale s, so g_7 has no a priori link to 7th-order functions.

A5. **HM2014 Theorem 0.4** applies to f_{a,b,c} when ac < b² and a | b, c | b. For (a,b,c) = (2,8,8): 16 < 64, 2 | 8 and 8 | 8, so it applies. f_{2,8,8}(x,y,q) = h_{2,8,8} − θ_{2,8,8}/(J̄_{0,24} J̄_{0,6}) (b²/a − c = 24, b²/c − a = 6). This matches the U7 lock.
- Corollary 0.5 is the Kac–Peterson identity (0.6), which is a special case of Thm 0.4. It concerns that identity, not f_{2,8,8}.

A6. **Residue filter {0,1,2,4} mod 7 is provable in one line.** Every term of g_7 sits at degree n² + 7m, and the squares mod 7 are exactly {0,1,2,4}. Comp_7 therefore vanishes off this set, which is exact.

A7. **Miss_7 reproduced through d = 3000.** There are 24 elements: 2, 7, 14, 16, 18, 21, 28, 32, 35, 36, 42, 43, 44, 57, 60, 63, 78, 79, 85, 100, 107, 135, 191, 247. The last is 247. This is A-grade as a finite computation. The statement for all d (OccFilt_7(∞)) is unproved.

A8. **Auto_prod_W7 = 1/√7** is an exact algebraic identity (a2532a6). Interp_prod_W7 ≠ √7 (a5db06c), so P-slash is obstructed. Theorem 8.4 is Object A only.

A9. The radial values g_7^∘(ζ) = Σζ^{n²}/2^n at ζ^7 = 1 are written on Master (wrap at 3de76f6). They are elementary because q^{7k} → 1. The first-term pole on q = −r is also written there. This is Master-written and A-grade as a restricted identity, not as QM.

## 4. Category B — explorations and numerics
B1. **First 61 coefficients of g_7, g_8, g_11**, computed from the Master definition (`coeff_table.txt`):
- g_7: 1,1,0,0,1,0,0,0,−1,1,0,−1,0,0,0,1,0,0,0,0,0,0,−1,−1,0,1,…
- g_8: 1,1,0,0,1,0,0,0,0,0,0,0,−1,0,0,0,1,…,−1 (q^24),…,−1 (q^33),2 (q^36)
- g_11: 1,1,0,0,1,0,0,0,0,1,0,0,−1,0,0,−1,1,0,0,0,−1,…
- OEIS: no hit for g_7 or g_8. g_11 "matched" A025441 on a 21-term prefix, but A025441 is a nonnegative count while g_11 has signs, so the match is spurious. The coefficients are small and sparse, consistent with a sum of partial/false-theta pieces (φ_n is a signed distinct-parts generating function).

B2. **Comparison with 3rd-order f, 7th-order 𝓕_0/𝓕_1/𝓕_2 and 8th-order S_0/S_1/T_0/T_1** (table in the same file): **no match**, not even up to sign, shift, or q → q^k. The 7th-order functions have positive, growing coefficients. Those of g_7 are bounded and small over the window. I did not tabulate U_0, U_1, V_0, V_1 or the 5th/6th/10th-order functions beyond f_0. Their growth profiles (Watson-type exponential growth) already differ from the bounded window of g_s. This is suggestive only.

B3. **Possible route for a Hecke form of g_s.** Andrews' Bailey-lemma derivation of (q)_∞ f_0(q) = Σ_{n≥0,|j|≤n}(−1)^j q^{5n²/2+n/2−j²}(1−q^{4n+2}) (HM eq. 0.3; Andrews 1986) needs a common base. For g_s one could expand 1/(−q^s;q^s)_n as Σ_m φ_n(m) q^{sm}, use φ_n = φ_∞ in the stable range (PhiStab, 4bb6391), and write g_s = Σ_n q^{n²}·[a partial-theta-like tail]. This is a Category B suggestion and is unexecuted.

B4. **Analogy only.** C_third on an indefinite form of discriminant 35 with signature (1,1) fits the Zwegers setting (thesis, 2002, Ch. 2 indefinite theta functions). It is not written as an f_{a,b,c} on Master. Rewriting C_third's cone in HM variables is the natural test.

B5. **Not checked against the source.** Andrews–Berndt LN Parts I–V entries were not checked page by page; I cite no specific entry numbers. The Zwegers μ/R completion and the Zagier Bourbaki and quantum modular forms references are cited only for concepts, with no theorem numbers.

## 5. Open paths
| Path | Status on 48684e3 | Literature lever? |
|---|---|---|
| Object B | UNOCCUPIED (cfca5e7); Oct 3 "no kernel" (3de76f6) | None. No published theorem supplies a generator or matrix built from Pack+(S) data. HM/Zwegers give completions of known q-series, not a new residual object. **No Cat A lever.** |
| Per_off | HEADER; Convention A vs B UNSELECTED (22dcbf5 / ffa8f76) | None. A convention is a choice, not a theorem. HM Thm 2.3 (changing z in m(x,q,z) costs a theta quotient) is an analogue for "convention ⇒ theta difference". **Cat B route only.** |
| OccFilt_7(∞) | Finite caps at 2500 and 12000; last zero 247 (reproduced to 3000); ∞ unproved (8d03b56) | No majorant in the literature for these mixed-scale coefficients. Possible route: an asymptotic or circle-method lower bound for |g_7(d)| on classes {0,1,2,4}. **Cat B.** |
| Remark 8.5 | OPEN (42 Contacts #36); Oct 3: no kernel | None. Mock-modular completions give two-sided transformation laws for known forms, not uniqueness of a four-sample interpolant. **No lever.** |
| QM of g_s | CONJECTURE; Path 2 empirical (83d0e37) | Only for s = 1, 2: f_0 and φ have published mock/quantum-modular theory (Zwegers; Zagier QMF, f_0/φ examples). Nothing for s = 7, 8, 11. Does not close the path (H_s completion ≠ QM of g_s). **Cat B.** |
| Slash_two | EMPTY (3de76f6) | None found. |

## 6. HQCC distinction
Book HQCC (retired in the 2026-09-20 fix) is not Canonical T3. HQCC termination claims are separate from the residual identities above. Nothing in this report bears on HQCC or uses it.

## 7. Concrete next levers, ranked
1. **Hecke-type form for g_7 (and g_8, g_11) via PhiStab plus a Bailey/partial-theta expansion.** If it lands in an f_{a,b,c} family covered by HM Thm 0.3/0.4, the Appell–Lerch decomposition follows. That would be the first Cat A identity tying g_s to the literature and would feed QM of g_s. Test on s = 1 first (it must reproduce HM 0.3), then s = 2, then s = 7.
2. **Write C_third as f_{a,b,c}(x,y,q).** Q_minus has discriminant 35. Clear the half-integers, identify (a,b,c), and check HM's applicability conditions. A closed form would make the Θ_third completion citable (Zwegers/HM) instead of Category B.
3. **Asymptotics of g_7(d) on the four residue classes** (saddle point on φ_∞ = 1/(−x;x)_∞, which is modular up to a q-power). A rigorous lower bound beyond some d_0, plus the finite check to d_0, would close OccFilt_7(∞) as Cat A.

Hygiene: 539 is a COUNT. Residual ≠ Resonant. CORE_FREEZE holds. Twin Prime and RH are unclaimed.
