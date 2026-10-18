> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** Errata R3.1–R3.7 keep their names. The rev3 planning note 2026-10-18-rev3-changes-note.md is included in this folder for provenance. Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# Audit of Bridge C rev2, profile law, and rev3 (18 October 2026)

For Arvin Hampton. All work is local. Nothing was pushed or sent. rev2 was not modified (md5 7767c43a1557750d80a3892bfef166c1).
This report makes no HQCC, TPC or RH claims. No new labels collide with L1–L7: errata are called R3.1–R3.7, and the new theorem, corollary and proposition are numbered (5.1, 5.2, 7.1), not lettered. "Theorem L" (now the Parity Dominance Theorem) appears only in the Lever-3 reports, not in the paper, and nothing here touches it.

Folders:
- `2026-10-18-Audit-and-ProfileLaw/`: scripts and outputs for every check below.
- `2026-10-18-Bridge-C-Consolidated-rev3/`: `bridge_c_consolidated_rev3.tex`, the PDF (32 pages), the edit scripts and the build log.

Categories. **Cat A** means proved, or checked exactly in rational/cyclotomic arithmetic. **Cat B** means cited, conditional or numerical only. Each item below says which one it is.

---

## PATH 1: skeptical-referee audit

| item | verdict | finding / fix |
|---|---|---|
| (a) Theorem F S-law by Poisson (§5.2–5.3) | **confirmed, 2 gaps (fixed in rev3)** | Gap 1: to integrate over the closed geodesic, the proof needs the majorant transformation Θ_{α,β}(τ,γz)=Θ_{γ⁻¹α,γ⁻¹β}(τ,z), plus the fact that γ² fixes all 140 labels and γ does not. Now stated, and checked exactly. Gap 2: A* was never defined. It is now defined as A*=(2,7), with ½A⁻¹A*=(½,0). |
| (a) odd lattice, w_c, T-law | **confirmed** | w_c=A⁻¹(0,½)=(1/10,−1/35)≡a≡(½,0) mod L'. The identity e(Q(n))=e(B(n,w_c)) holds because Q(n)≡n₂/2. I rechecked u_L(w+1)=e(13/20)u_L by hand. |
| (a) group relations | **confirmed, upgraded** | Rebuilt S, T, P from the formulas; they match the stored matrices to 7e-16. Checked exactly at all 48 Galois conjugates over Q(ζ₁₄₀), using σ_j√35=χ₁₄₀(j)√35 and the fact that an algebraic integer whose conjugates all have modulus <½ is 0. Results: S²=P, P²=I, [P,T]=0, and **(ST)³=I on all of C¹⁴⁰** (R3.7). dim Fix(P)=72. T has order 140. tr S on Fix(P)=0, so S has eigenvalues ±1 with multiplicity 36/36. |
| (b) Lemma 6.1 (Green form) | **confirmed, minor gap** | Holomorphy needs truncation at z+iη because the integrand is singular at the endpoint. With ∂̄F_η=−T_n∂_{w̄}R^{1/2}→0 the argument closes. Independent mpmath quadrature at 3 points z and n∈{0,±1,±2,3} agrees to ≤7e-22. |
| (c) Theorem O2 | **confirmed after fix** | Gap: the comparison of 1/y coefficients assumed V has a 1/y expansion. Fix: apply Cayley–Hamilton, Σa_iλρ(γ₀)^{n+i}V(τ)=0, before taking limits. The proof also needs sector-uniform 1/t asymptotics at x_n. The Gauss input G(1/m)=e(7·20̄/m)(35/m)/m holds for all m<1200; it now also follows from Corollary 5.2(iii). |
| (c) Theorem O1 | **confirmed after 2 fixes** | Fix 1: get the individual limits by inverting a Vandermonde system. Fix 2: replace N by lcm(N,70). The profile-law input it relied on is now proved (Theorem 5.1), so O1 is no longer conditional on it. |
| (c) Lemma P | **confirmed (minor precision)** | Checked: period 2m; an involution that preserves the phase (B((1,1),ν₀)∈½Z, 4m²xQ(1,1)=46mh); B_p(1−s)=(−1)^pB_p(s). Part (b) needs two things stated: γ^k fixing the classes mod 2m, and vertical growth of Hecke L-functions. Still conditional on F1 and Hecke, as the paper already says. |
| (d) ζ rational-curve proof (Thm A.1) | **confirmed** | sympy rederivation of every step. Lemma E checked by brute force for s=3..30. Both closed forms and the vanishing t^{±1/2} sums check out. |
| (d) Theorem G_s (Thm A.2) | **confirmed** | c₀..c₄ rederived independently; the remainder is O(t⁵) numerically at s=3 and 7.5. |
| (e) counts | **2 errors, 3 imprecisions** | Confirmed: 140 labels; 70 classes; 35 entries per S row; Fix(P) 72 (4 P-fixed labels plus 68 pairs); PSL₂ relations; level 70; \|L'/Z²\|=35; 3374/490/1102/270 pairs, of which 178 have exactly one zero and 60 have both nonzero; Shintani \|det\|=2,23,58,43,130; 21 classes; the radial constants. The errors and imprecisions are R3.1–R3.5 below. |

## New errata (R3.x; these do not collide with L1–L7)
- **R3.1 (error).** The 60+12 split is wrong. The function span V has dim 42 = 36 Eisenstein + 6 cusp, and both parts are S,T-invariant. The old 60/12 were ranks of label rows of ½(I+P). Confirmed by independent code: rank gap 6.4 vs 6e-15 at |Q|≤12, and 10.0 vs 1.6e-14 at |Q|≤25.
- **R3.2 (error).** There is no 12-dimensional cusp part. The 12 dihedral forms appear only in 6 fixed linear combinations.
- **R3.3.** There are 24 cusp labels, not 28: β=−a, 70α₁∈{7,21,49,63}, and 7 divides the denominator of α₂.
- **R3.4.** 11 labels give u≡0, so 129 functions are nonzero. **This is proved exactly** (new, Cat A). For each of the 11, either γ or −γ maps α+Z² onto itself and multiplies the phase by −1, so the sum over ν mod γ² equals its own negative. A rational-arithmetic check confirms these are exactly 11 labels (`zero_labels_check.py/.txt`).
- **R3.5.** The "cyclic span 36" is a rank after projection to Fix(P). The label-space Krylov dimension is 60.
- **R3.6.** A* was undefined. It is now defined, and the profile law is restated and proved.
- **R3.7 (refinement).** (ST)³=I holds on all of C¹⁴⁰. Only S²=I needs the restriction to Fix(P).

## Spectra (Cat A where marked)
- **S** (Cat A, exact): ±1 with multiplicity 36/36 on Fix(P). On V it is 21/21, split as 18/18 on V_Eis and 3/3 on V_cusp; the V numbers are numerical, confirmed by two independent codes.
- **T** (Cat A, exact phases): on Fix(P), 36 distinct values e(r) with multiplicities 1 (12 values), 2 (18 values) and 4 (6 values: r=19,31,59,111,131,139 /140). Each of the 36 occurs once on V_Eis. The 6 multiplicity-4 values make up V_cusp.
- This leaves an open 30-dimensional T-stable complement W of V in Fix(P) that no lift function realises. It is listed as open.

## PATH 3: profile law (Cat A, proved)

**Theorem 5.1.** For all rational α,β and rational x≠0:
G_{α,β}(−1/x) = e(B(α,β)) / (√35·|x|) · Σ_{p∈L'/Z²} G_{β+p,−α}(x), and G_{α,β}(x+1) = e(−Q(α)−B(α,w_c)) G_{α,α+β+w_c}(x).

Proof outline (the full proof is in rev3 §5.1):
1. A Gaussian-regularised Poisson lemma for periodic weights on lattice cosets, uniform in complex symmetric N near I.
2. Apply it to g(ν)=e(B(ν,β))exp(−πνᵀZ_εν) with Z_ε=εI+(i/x)A, using AZ_ε⁻¹A=−ixA+εx²N_ε and N_ε=(I−iεxA⁻¹)⁻¹.
3. (det Z_ε det N_ε)^{1/2}→√35/|x|. The eigenvalue arguments ±π/4 cancel because A has signature (1,1), and this holds for either sign of x.
4. Compare the ε⁻¹ coefficients.

The T-law follows directly from Q(n)≡n₂/2.

**Numerics, independent of the proof (all max deviations):**
- All 140 labels at 4 values of x: 3.3e-15 (560 tests, 280 nonzero).
- 13 labels × 12 values of x: 3.2e-15.
- 100 random rational pairs outside the family: 2.2e-15 to 3.2e-15 (63 nonzero).
- T-law: 5.6e-16.
- With x in place of |x|, the ratio is −1 at x<0, which confirms the |x|.

Status: Cat A, proved. Like all of this work it has not been externally refereed, and it has had no audit pass separate from its derivation.

**Corollary 5.2 (Cat A given 5.1; (iv) also uses R1):**
- (i) G(γx)=|cx+d|⁻¹ρ(γ)G(x) for all γ∈SL₂(Z). Checked for random words to 6.6e-16.
- (ii) G_{a,0}(x/(140x+1))|140x+1| = G_{a,0}(x). This upgrades Theorem P(ii) from Cat B to Cat A.
- (iii) m·G_{a,0}(1/m) depends only on m mod 70. This is a second proof of the O2 Gauss input.
- (iv) The fundamental-domain 1/t coefficients satisfy |x|s(−1/x)=S s(x).

## PATH 2: rev3
`2026-10-18-Bridge-C-Consolidated-rev3/bridge_c_consolidated_rev3.pdf`, **32 pages** (rev2 had 26). Built with pdflatex: no errors, no undefined references, no overfull boxes. The 33 hyperref "Token not allowed" warnings are pre-existing (rev2 has the same kind).

Changes:
- The abstract and Theorems F/G/H are updated.
- §5.1 now holds Theorem 5.1 with its proof and Corollary 5.2.
- §7.2 has the corrected cusp labels and the exact vanishing of 11 labels.
- New §7.3 / Proposition 7.1 covers the spectra, W and the 6 combinations.
- The status table, audit section, reconciliation and open problems are updated.
- Appendix C has the O1/O2/Lemma P audit notes.
- New Appendix B lists the verdicts, the errata R3.1–R3.7 and the status changes.
- Sources: [S14] S-Eigenvalues.md and [S15] this report.

## Cat B (unchanged)
- Maass's dihedral construction, cuspidality ⇔ χ≠χ∘σ, levels and newform status.
- Identifying the 24 cusp rows of Φ as Lewis–Zagier period functions.
- Lemma P's dependence on F1 and Hecke.
- Every external citation.

## Files in `2026-10-18-Audit-and-ProfileLaw/`
- `profile_law_check.py/.txt` and `profile_law_random.py/.txt/.log`: profile-law checks.
- `thmF_exact.py/.txt`: S, T, P relations, Fix(P), T spectrum, tr S.
- `vspace_check.py`, `vspace_check_X12.txt`, `vspace_check_X25.txt`: dims 42/36/6, invariance, cusp labels, zero labels.
- `zero_labels_check.py/.txt`: exact proof that 11 labels vanish.
- `green_lemma_check.py/.txt`: Lemma 6.1.
- `o2_counts_check.py/.txt`: O2 Gauss input, Theorem D, counts.
- `zeta_gs_check.py/.txt`: ζ curve and G_s.
- `profile_corollaries.py/.txt`: Corollary 5.2 (i) and (ii).
