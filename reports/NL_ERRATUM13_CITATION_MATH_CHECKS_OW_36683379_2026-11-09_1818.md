# NL erratum 13: citation scope (OW 36683379, amending OW 3f160803). Math checks of cited results, and a re-grade of the source-limited marks
Author: Non Local Path (NL). Everything below is an **NL derived proposal**. Additive; nothing overwritten. Reading and checking only. No Gemini, no external sends, no CERT. No source or b adopted; MN N=2 is the Owner's working vacuum, CONDITIONAL (OW 19a88b19). Tip 7cddb188 untouched.

**Authority.** OW 36683379 (18:15; sha verified) amends OW 3f160803 (18:14):
- Citations from any source are allowed, provided the cited mathematics is verified.
- Unverified math stays labeled, and a citation alone never makes a claim PROVED.
- The rule applies retroactively to the erratum-12 and PP fe0c3d92 "unverified" marks.

Marks used:
- **cited, math checked:** NL re-derived or recomputed the step.
- **cited, math not yet checked.**

Scripts, with sidecars, in /workspace/nl-junction-1817/:
- mathcheck.py (fce1f08f…) and mathcheck_1820.log (9401128d…)
- autcheck.py (be56e69c…) and autcheck_1821.log (67186319…)

## (a) The Y14-relevant sources
**Sibner–Sibner–Uhlenbeck**, PNAS 86 (1989) 8610.
- **M1 (PROVED; cited, math checked).** The reduction step: flat ℝ⁴∖ℝ² = r²(g_H³ + dθ²), and the 4D YM density |F|²√g is conformally invariant (Ω⁻⁴·Ω⁴ = 1). So U(1)-invariant YM on S⁴∖S² is equivalent to YM–Higgs on H³.
- **M2 (CONDITIONAL; cited, math not yet checked).** The min–max over a non-contractible loop, giving infinitely many non-self-dual, unstable critical points with C₂ = 0.

**Sadun–Segert**, Bull. AMS 24 (1991) 163.
- **M3 (PROVED; cited, math checked).** The SU(2) (SO(3)) action on S⁴ ⊂ {traceless symmetric 3×3} has generic orbits of dimension 3 and singular orbits of dimension 2. It is cohomogeneity 1, so YM reduces to ODEs.
- **M4 (PROVED for |C₂| ≤ 60, finite check; cited, math checked).**
  - C₂ = (n₊² − n₋²)/8 is an integer for odd n±.
  - With n± ≥ 3, every C₂ in [−60, 60] except ±1 is attained.
  - The stated solution count (number of odd factors, minus 1 when |C₂| is triangular) matches the pair count for C₂ = 1–60, including C₂ = 45 → 5.
- **M5 (CONDITIONAL; cited, math not yet checked).** The ODE existence of a non-self-dual solution on each quadrupole bundle with n± ≠ 1, and their Prop. 2.5 (no equivariant self-dual solutions there).

**Taubes**, JDG 17 (1982) 139.
- **M6 (PROVED; cited, math checked).** The hypotheses hold for the fibre S⁴ with any metric:
  - H²(S⁴) = 0, so there are no ASD harmonic 2-forms;
  - H²(S⁴; π₁G) = 0, so the η-obstruction is trivial;
  - E₈ bundles are classified by k ∈ π₃(E₈) = ℤ.
- **M7 (CONDITIONAL; cited, math not yet checked).** The gluing and contraction analysis that yields self-dual connections, for the unweighted problem on the squashed fibre.

**Bourguignon–Lawson–Simons**, PNAS 76 (1979) 1550.
- **M8 (PROVED; cited, math checked).** Their Thm 4.2: the Levi-Civita connection on the S⁴ frame bundle has ∇R = 0, so D⋆R = 0 and it is YM. Its curvature e_a∧e_b is mapped by ⋆ to e_c∧e_d, a different so(4) component, so it is not self-dual or anti-self-dual. This shows the SU(2)/SU(3) restriction in Thm 4.1 is necessary.
- **M9 (CONDITIONAL; cited, math not yet checked).** Thm 4.1: weakly stable SU(2) or SU(3) YM fields on S⁴ are self-dual or anti-self-dual. This is the averaged second variation over conformal fields.

**Embedding.**
- **M10 (PROVED).** An SU(2) connection embedded in E₈ by a Lie algebra homomorphism satisfies D⋆F = 0 and is self-dual iff the original is. So non-BPS SU(2) solutions give non-BPS E₈ solutions.

**Consequences for Y14 (stays OPEN).**
- Round-S⁴ existence (1800 Y12) stays **CONDITIONAL**, because M2 and M5 are not yet checked. Instability (Y13) stays **CONDITIONAL** (M9).
- **M11 (CONDITIONAL, not yet a full isometry computation).** The Sadun–Segert irreducible SO(3) is not an isometry of the squashed fibre: the X_i break SO(5) to U(1)². So their reduction does not transfer.
- **The SSU U(1) reduction does transfer topologically.** Each φ_i rotation fixes the S² at {μ_i = 0}. But the weight W and the squashing turn H³ into a weighted, non-hyperbolic 3-metric. This is the concrete Y14 route: YM–Higgs on that 3-manifold, then min–max.

## (b) Re-applied to earlier source-limited findings
**Bolza** (1800 Γ2; erratum 12, fix 4; sources Wikipedia, Fortier Bourque–Rafi 1807.08367, Jenni 1984).
- **M12 (PROVED; math checked).** For the regular hyperbolic octagon with angles π/4, cosh(s/2) = cot(π/8) = 1+√2. The geodesic joining opposite side midpoints, i.e. twice the inradius, has length **2 arccosh(1+√2) = 3.05714**. The Fortier Bourque–Rafi footnote algebra also checks: cosh²t₁ = 1 + 1/√2, so cosh 2t₁ = 1+√2.
- **M13 (CONDITIONAL; cited, math not yet checked).** That this is the shortest geodesic (the systole), FB-R's local maximality, and Jenni's global maximality.
- **M14 (CONDITIONAL; arithmetic checked, rule not checked).** The second length 4.8969 = 2 arccosh(3+2√2): with the Aurich–Bogomolny–Steiner rule m + n√2 at n = 2, the minimizing odd m is 3. The rule itself is not checked.
- **M15 (PROVED; math checked).** |Aut⁺(Bolza)| ≥ 48.
  - The Möbius maps z → iz and z → (z+1)/(1−z) generate a group of order 24 permuting the branch set {0, ∞, ±1, ±i} (autcheck log).
  - Each lifts: f(Mx)(cx+d)⁶ = const·f(x), so y → const·y/(cx+d)³.
  - Together with the hyperelliptic involution this gives 48 = |GL(2,3)|.
- **M16 (CONDITIONAL; cited, math not yet checked).** Equality |Aut⁺| = 48 (it uses the uniqueness of the hyperelliptic involution to bound the reduced group), and the full isometry group of order 96.
- **M17 (REFUTED, NL script slip).** mathcheck_1820.log's line "order 21 → 42" came from a faulty matrix-deduplication routine. autcheck_1821.log supersedes it. The log is kept, not overwritten.

**BBBW z quantization** (1711; erratum 7, fix 7 "z ∈ ℤ for g = 2", formerly CONDITIONAL on citation).
- **M18 (PROVED given BBBW's parameterization; math checked against the local text of 1203.0303, eqs. 2.12–2.13).** p = (1+z)(g−1) and q = (1−z)(g−1) are Chern numbers. For g = 2, p = 1+z ∈ ℤ, so z ∈ ℤ.

**HW, Ganor–Hanany, Seiberg–Witten, FHMM, OST** (1750 E0, E1, E6, E7; 1800 Y1, Y7, Y8; 1813 Q0–Q2).
- **M19 (CONDITIONAL; cited, math not yet checked).** HW's λ² and the anomaly derivation, the small-instanton transition, M5 anomaly inflow, and the E-string anomaly polynomial.
- What is checked independently is only the arithmetic u = 8π²/(λ²T_M5) = 2 from the printed λ² (1813), and p₁(TS⁴) = 0 (1750 E1-p₁, PROVED).

**Re-grade of the erratum-12 marks.**
- Erratum 12 item "non-arXiv citations (CONDITIONAL, unverified)" is replaced by M1–M10 and M12–M16: per-step "math checked" or "math not yet checked".
- "Γ2 second length (flagged)" is replaced by M14.
- The erratum-12 tally stays 7/5/0/2 (wording only).

**1800 tally after erratum 13.** Γ2 splits into M12 (PROVED), M15 (PROVED) and M13/M16 (CONDITIONAL, kept as one Γ2 item). This gives **PROVED 15 · CONDITIONAL 11 · OPEN 3 · REFUTED 2 = 31**. Y12 and Y13 stay CONDITIONAL; Y14 and Y15 stay OPEN.

## Tally of this erratum
| label | count | items |
|---|---|---|
| PROVED | 10 | M1, M3, M4, M6, M8, M10, M12, M15, M18, plus the Y14 transfer note under M11 that each φ_i rotation fixes an S² (topological) |
| CONDITIONAL | 9 | M2, M5, M7, M9, M11, M13, M14, M16, M19 |
| OPEN | 0 | — (Y14/Y15 are tracked in 1800, not regraded here) |
| REFUTED | 1 | M17 |

Check: 10 + 9 + 0 + 1 = 20.

Tip: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
