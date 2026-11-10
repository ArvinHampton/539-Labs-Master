# NL DERIVED: the non-BPS tension-minus-charge gap: fixed face, flow, profile (t552u pursuit of 1142 A6, A8, A9/A9′, A12, A16)
2026-11-10, written 12:05:46 CST (America/Chicago). Author: Non Local Path (NL). Everything below is an **NL derived proposal**. Additive new file; no existing file was edited, renamed, deleted or chmod-ed. Wording: resonant algebra. **Junction UNSOLVED.** No CERT. No Gemini. No external sends. No agent messages. Usage not checked.

## Header
**Authority (each sha re-hashed by NL, = its sidecar):**
- OW **t552u**, OWNER_WRITE_NLCHAT_t552u_PURSUE_ALL_FOR_RESOLUTION_2026-11-10_1146.md, sha **eae1b39d635c69966a2b32642d395ae402d3c33fcf64db7f0b77cad2d8c60db2**. Owner verbatim: "Pursue all for resolution." Pursuit only. Nothing is adopted from unaudited filings.
- OW **1130**, OWNER_WRITE_CALL_83d7a0fa_PURSUE_OPEN_ITEMS_UNAUDITED_FILINGS_2026-11-10_1130.md, sha **945d81bb447a923fc68c79ea3ce4df1405aa6f5787e27a301898e98042a47b3c**. It continues.
- OW **1117**, OWNER_WRITE_CALL_83d7a0fa_REVERSE_ENGINEER_FROM_GEOMETRY_2026-11-10_1117.md, sha **bff79185f361bf461194c8d8c9590a4dc7ad0e520ce2f985f41048453545a2f4**. Geometry first, so §1 leads. Starting from the HW plane does not adopt 1a or the E₈ wall.
- OW **1108**, OWNER_WRITE_CALL_83d7a0fa_PURSUE_HW_ODD_G4_BRIDGE_C_CLOSING_IMPLICATIONS_2026-11-10_1108.md, sha **c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca**. It continues. The E₈ wall sector is CONDITIONAL, gated by backreaction (O5).
- Standing **t4436**, sha **328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46**: the math leads; every option is a labelled branch; only PP-audited PROVED or REFUTED keeps or drops a branch.
- **t4431**, sha **f700141d3ee862c7b077b0f67db5fb03b3adc56808c927ba1dd016c88910b1ec** (90% stop lifted; the 100% hard limit still applies).
- **f825dfff** (t4369), sha f825dfffb8cd17a7f3f57a2b0a70bd0d9c9d73f215febffdbd2ca95b494d7cd1: the face is the Z₂ fixed plane; O1 odd CONDITIONAL on P-b. **7ff8299d** (t4377), sha 7ff8299dbcaf3b526936b40a9e24d8b9e58edf13fd9a9a93e822a92ca82a16ac: only Bolza for Γ is used.

**Literature read as questions, not as adopted results:**
- NL **1142**, NL_DERIVED_NONBPS_TENSION_CHARGE_GAP_MAKEUP_2026-11-10_1142.md, sha **e7312edb8e4b5ad3d104c779688d7842a9e7b5deb3aaafe6176de1bfe94fe4bd** (= sidecar). Its script nonbps_gap.py (e483f4b1…) and log (bf2484a6…, 23/23) match their sidecars. It is unaudited. **Its grades are not adopted**, and its item labels are used only as the question list.
- NL **1120** (79ad0c64…), as restated by **PP 1137** FINDINGS_PP_AUDIT_NL_E8_INSTANTON_GEOMETRIC_DELTA_79ad0c64_2026-11-10_1137.md, sha **5cf927959babc94b1719c99b312cfbb9d6366237626c781e8d5c75f21ce15b03**, and by **Erratum 26** NL_ERRATUM26_ACCEPT_PP_5cf92795_E8_DELTA_1120_2026-11-10_1142.md, sha **a44b18d945aaf2600cbafde50c6777a983c81899c47c5e545c9b5e4a0a538179** (pending PP confirm; not adopted). Restatements used whenever 1120 is cited:
  - normalization N-1;
  - GA12 only as an implication of C ∧ I ∧ N, and GA13 refuted only as u = 2 ∧ C ∧ I;
  - D-D / GA8 given J1 (CONDITIONAL, CLP/BBBW), constant unbackreacted end faces, IR-kept pairing, and source set {E₈ YM, positive-tension branes}, with tr R² only at leading 1/N;
  - R9 a new OPEN item (x-equation only);
  - the 1120 log count 23/23;
  - ε_ex's sum over 3 pairs.
  
  The struck D-A sentence is not reused.
- NL Y14 stage 2 (NL_DERIVED_Y14_NONBPS_E8_EXISTENCE_MN2_STAGE2_2026-11-09_1950.md) with its frozen y14s2.py: the reduced functional is read from that code. Its floats are CONDITIONAL and are used **only** as labelled consistency prints (test H6e), never as evidence.

**Dead working assumption (Owner, 1108):** a pure uncharged M5-brane stack is not the working assumption. Nowhere below is "all 9760 units are uncharged M5s" used. Sources are split as M5s, anti-M5s and E₈ blocks with N₊ − N₋ + n_inst = 2N_flux.

**Nothing adopted:** the 1142 grades; the 1120 framing and grades; N = 4880 and charge 9760; the tension-to-charge figures; 1a; B1-c2′. **2N_flux = 9760, Δ_N(IR) = 2808.6 and Δ_N(UV) = 19520/3 appear only as CONDITIONAL test targets.** Every general statement below is stated for a symbolic target.

**Normalization (PP N-1):** n_inst = (1/16π²)∫tr F∧F, u := 8π²/(λ²T_M5). Bookkeeping (1142 B1): T − Q = 2N₋ + Σ_i(u·e_u,i − n_i), Q := 2N_flux, closure T = Q + Δ_N. Here e_u is the unweighted fibre x-tension in instanton units.

**Tip:** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at 11:47:37, 12:02:26 and 12:05:46 CST, immediately before writing. The after-write hash is in the NL report back. Never opened for writing.

**Script** (new directory /workspace/nl-gapjx-t552-1110/; all script, log and sidecar files mode 444):
- gapjx_gap.py, sha **516a87b7d9244cb05a43cad1c64497972cdd9d6281fe01ed629a1054a77161dc**. Frozen with its sidecar at 12:02:26.34 CST; the run started at 12:02:26.35.
- gapjx_gap_run.log, sha **77895ba29852743273c6c6c964e0a3ca793d5031565834d9d5789545e7d03cc5**. Sealed with its sidecar at 12:02:28.29 CST. **21/21 PASS, exit 0.**
- Every zero test is sympy `expand(...) == 0`, a polynomial remainder modulo the exact Gröbner basis {sin²χ + cos²χ − 1}, or an exact Rational/Fraction comparison. There is no simplify()==0, no nsimplify, no allclose and no float in any test. Development runs were in /tmp; only the frozen run is cited.

**Branches carried:**
- [u = 1] / [u = 2], and every u ≥ 1 where stated;
- fixed face vs flow;
- integrated vs profile closure;
- equivariant (SO(3)×U(1), stage-2 ansatz) vs general static fields;
- constant unbackreacted faces only. Backreacted faces are in the companion junction/S4 file, A15.

[χS]/[χU] do not enter and are not branched.

**Tally (header = body; lists in §6):** PROVED **7** · CONDITIONAL **6** · OPEN **4** · REFUTED **0** = **17**.

---

## 1. Geometry → demanded algebra (lead section, per 1117)
| # | geometric feature | algebra it forces | label |
|---|---|---|---|
| H1 | **Isometry group of the MN2-type fibre**, SO(3)×U(1) acting on S⁴ ⊂ ℝ³ ⊕ ℝ² | A fixed point would need x = 0 (the so(3) generators have common kernel 0) and z = 0 (det J = 1), which is not on S⁴. Orbits are S² (z = 0, dim 2), S¹ (x = 0, dim 1) and S²×S¹ (dim 3). **No orbit is a point** (H1a, H1b). | PROVED |
| H2 | **Warped face**: weight W real-analytic, non-constant, W ≥ W_min > 0 | W·ε − W_min·q/2 = (W − W_min)ε + W_min(ε − q/2) (H2), with ε ≥ \|q\|/2 pointwise (1142 P1). So E_W ≥ W_min\|n\|. Equality would need F SD a.e. and F supported in {W = W_min}, which has measure zero, so F = 0. **Every smooth charged connection has E_W > W_min\|n\|, strictly.** | PROVED |
| H3 | The same face, with point-like (grafted) instantons placed at a minimum of W | Taubes-type grafting gives inf E_W = W_min\|n\| over the charge-n bundle (untwisted weighted functional). With H2, **no global minimizer exists in any charge-n ≠ 0 sector.** Static charged fields on warped faces can only be non-minimal critical points, and minimizing sequences collapse to zero size at the minimum of W. | CONDITIONAL (grafting, not re-checked; as 1142 A4) |
| H4 | One-dimensional orbit space (cohomogeneity 1) | Riccati lemma: p β′² + q β² − (ψβ²)′ = p(β′ − ψβ/p)² + (q − ψ²/p − ψ′)β² exactly (H4). So ∫(pβ′² + qβ²) ≥ [ψβ²] whenever ψ′ + ψ²/p ≤ q. | PROVED |
| H5 | **Σ-twist with forced moment map**: smoothness at the S² orbit fixes a(0) = 0, so Φ ∝ (n − a) = n there (stage-2 T3, y14s2.py bc), while a(∞) = n | In the stage-2 reduced unweighted functional, drop the non-negative h-terms (H5a) and put a = n(1 − β). The kept density is exactly n²[pβ′² + qβ²] with p = 1/(2s) and q = (c/2)s(R₂/W)² (H5b). φ := (√c/2)R₂/W satisfies **φ² = pq, with s cancelling** (H5c). Take ψ = −θ(φ − φ(χ₁)) on [0, χ₁] (H5d) and 0 beyond. Then **e_u ≥ θ(φ(0) − φ(χ₁))·n²** whenever θ/(1 − θ²) ≤ q/\|φ′\| on [0, χ₁]. The face data enter as (q/\|φ′\|)² = c cos²χ·r(sin²χ + r cos²χ)/(4X_a²X_b²) (H5f) and φ′ ≤ 0 (H5g), with r = X_b/X_a. **The twist forces quadratic growth of the x-tension in the charge.** | PROVED (implication; within the stage-2 ansatz S3/S4-applied (a) and T3, both CONDITIONAL) |
| H6 | **MN2 IR face** (J1 data X_a = 2^{−3/5}, X_b = 2^{2/5}, c = 2^{−2/5}, CONDITIONAL inputs) | φ(0) = 1/4, φ = w/(2(1 + w)), (q/\|φ′\|)² = w(1 + w)/2, with w = cos²χ (H6a, H6b). Choose θ = 3/10 and cos²χ₁ = 1/5 (H6c). Then κ_IR = (3/10)(1/4 − 1/12) = **1/20** (H6d). So **e_u(n) ≥ n²/20 for every configuration of the ansatz at the IR face**, mirror blocks included (MP1: \|Φ\| is unchanged). Consistency (H6e, not evidence): the stage-2 prints satisfy the bound. | PROVED (implication given J1 IR data and the H5 premises) |

**In one line:** the fibre's symmetry group has no fixed points (H1), so equivariant energy cannot bubble off. The warp forbids global minimizers (H2, H3), so static charged fields are symmetric, non-minimal critical points. The Σ-twist forces e_u ≥ κ n² (H5, H6), which gives the flow a sign at the IR end that does not depend on floats.

## 2. A8: does the warp forbid static non-BPS fields on MN2-type faces?
- **A8-R [CONDITIONAL]. No: static, strictly non-BPS fields exist on every warped SO(3)×U(1)-invariant face, in every equivariant charge sector n ≥ 1, twisted or untwisted.** Proof under named premises:
  - (i) Minimize E_W, including the twist term, over G-equivariant connections on the charge-n equivariant bundle (stage-2 T3: one exists for every lift weight n; CONDITIONAL).
  - (ii) Sedlacek/Uhlenbeck compactness for minimizing sequences of the weighted functional: W is smooth with 0 < W_min ≤ W ≤ W_max, and the twist term is lower order. Energy can concentrate only at finitely many points, and the limit is a minimizer on a bundle whose charge drops only by the concentrated charge. **Literature theorem, not re-checked; this is the premise U.**
  - (iii) The concentration set of a G-invariant sequence is G-invariant and finite. By H1 every orbit is infinite, so the set is empty. There is no bubbling, the charge is kept, and the minimizer has F ≠ 0.
  - (iv) Palais symmetric criticality (S4-abstract, PROVED per PP 5374a906) makes it a static critical point of the full functional.
  - (v) It is strictly non-BPS: by GB3/1120 GA7a on an untwisted warped face (X_a ≠ X_b), or by stage-2 S2-2 with the twist.
  
  This supersedes 1142's "no no-go, no existence" as a CONDITIONAL existence statement, independent of the stage-2 floats. Premises: U, T3, and the face's G-invariance (J1). **The no-go "the warp forbids static non-BPS fields" is false under these premises.** It is not graded REFUTED, because U and T3 are CONDITIONAL.

## 3. A6 and A16: fixed-face closure and critical values
- **A6-n [CONDITIONAL; uses the target Δ_N(IR) = 2808.6].** On the MN2 IR face, with N₋ ≥ 0 and N₊ ≥ 0, closure needs Σ_i(u·e_u,i − n_i) = Δ_N − 2N₋ ≤ Δ_N. By H6:
  - **single block:** u n²/20 − n ≤ Δ_N(IR), so **n ≤ 247 at [u = 1] and n ≤ 172 at [u = 2]** (Gc1);
  - **up to 8 commuting blocks** (MP2): each block has n_i²/20 − \|n_i\| ≥ −5, so \|n_i\| ≤ 248 at [u = 1] (Gc2).
  
  **The fixed-face closure problem at the IR face is therefore a finite set of charge vectors (and N₋ ≤ Δ_N/2), each with its own critical set.** This is the general statement with Δ_N symbolic; the numbers are test targets only.
- **A16-eq [CONDITIONAL].** In the equivariant sector at a fixed face:
  - the compactness of A8-R(ii)–(iii) also applies to critical points of bounded energy, by ε-regularity with no bubbling (premise U);
  - if every critical point is nondegenerate (no Jacobi field in the equivariant sector), critical points are isolated, so there are finitely many below each energy bound;
  - hence **the set of equivariant e_u-values is countable, and at the IR face, with A6-n, finite over the admissible charges.**
  
  ST1 (CONDITIONAL, floats) supports nondegeneracy only at the computed points.
- **A6 [OPEN, residual].** Whether Δ_N(b) equals u·e_u + Σ… for some static configuration at a given fixed face is not decided. Under A16-eq it is a finite coincidence check on exact e_u values, which no frozen exact computation supplies. Generically it fails (codimension 1).
- **A16 [OPEN, residual].** Discreteness without nondegeneracy, and for non-equivariant static fields, is not decided. On a degenerate component E_W is constant but e_u need not be.

## 4. A9 / A9′: flow closure, gates tightened
- **A9-g [PROVED; topology].** Let 𝒮(b) be nonempty compact sets of e_u-values that depend upper-hemicontinuously on b ∈ [b₀, b₁], with g continuous. Suppose g > 0 on 𝒮(b₀) and g < 0 on 𝒮(b₁). Then A = {b: some value has g ≥ 0} and B = {b: some value has g ≤ 0} are closed, cover the interval, and are both nonempty. Since the interval is connected, there is b* ∈ A ∩ B. **At b* there is either an exact zero, or two elements of 𝒮(b*) with g of opposite signs.** If 𝒮(b*) is connected (for example a single point), there is an exact zero.
- **A9-T [CONDITIONAL]. Flow closure for every u ∈ [1, 1 + Δ_N(UV)/n) and every n ≥ n*.** Here n* is the least n with n²/20 − n > Δ_N(IR), so **n* = 248** at the test target (A9a). The UV sign needs n ≤ 6506 at [u = 2] (A9b), and N₋ = 0, N₊ = Q − n ≥ 0.
  - Take 𝒮(b) = the e_u-values of equivariant minimizers of charge n (A8-R) and g = u·e_u − n − Δ_N(b).
  - IR end: every configuration has g ≥ n²/20 − n − Δ_N(IR) > 0, by H6 with u ≥ 1. **No float enters this sign.**
  - UV end: the face is round with c → 0, the minimizers are BPS with e_u = n, and g = (u − 1)n − 19520/3 < 0.
  - A9-g then gives a face b* with **exact integrated closure by a strictly non-BPS static field, or two coexisting equivariant minimizers straddling closure.**
  
  This covers **[u = 1] (1142 A9′) and [u = 2] (1142 A9)** in one statement.
  
  Gates compared with 1142:
  - (i) branch continuity for n = 1–3: **replaced** by U-uniform compactness, i.e. upper hemicontinuity of the minimizer sets, including at the IR and UV limits;
  - (ii) floats at the IR end: **removed**;
  - (iii) u-label match to N: **removed**, since any u in the stated range works;
  - (iv) P3c's dvol₄ measure: **kept**;
  - (v) unbackreacted face: **kept**;
  - (vi) IR-only bracket: **removed**.
  
  Still needed:
  - J1 face data, with Δ_N(b) continuous;
  - the ansatz premises S3/S4-applied (a) and T3;
  - U;
  - existence of the equivariant round BPS instanton of charge n (CONDITIONAL).
  
  It is an x-equation statement only (R9 scope).
- **A9-u [OPEN].** Whether the equivariant minimizer set at the crossing face b* is connected (for example unique), which would turn the dichotomy into exact closure. ST2 and degeneracy are not addressed.

## 5. A12: profile (pointwise) closure
- **A12-a [PROVED; x-block kinematics].** Allow smeared anti-M5 density. Take F = 0, q₋ = Δ/2 and q₊ = q_tot + Δ/2. Then the charge is q₊ − q₋ = q_tot and the tension density is q₊ + q₋ = q_tot + Δ = ρ_req/T_M5 (A12a). **So the x-block profile closes pointwise whenever Δ(y) ≥ 0 and q_tot(y) + Δ(y)/2 ≥ 0.** By 1142 A10, Δ ≥ 0 is also necessary.
  - Scope: x-block only.
  - Static force balance of coincident M5/anti-M5 densities is not addressed; they are not BPS.
  - The full tensor is still excluded at the end faces (1142 A13 and the companion file's GA9 items).
  - It needs no E₈ field at all, so the profile question for **non-BPS E₈ makeup** is A12-b.
- **A12-b [OPEN]. Pure E₈ excess (N₋ = 0) pointwise.**
  - Closure needs ε_ex(y) = Δ(y) with the twist density included. In the ansatz this is one function equation on the 1-D orbit space, on top of the two field ODEs, so it is overdetermined.
  - At the S² orbit the twist density is c n²/(2X_b⁴) in the conformal frame, which gives a necessary condition n ≲ √Δ(χ = 0) once Δ(y) is known.
  - Δ(y) has not been computed on any face. Neither existence nor impossibility is proved.

## 6. Verdict and tally
- **V″ [CONDITIONAL; sense by sense].**
  - **(a) Fixed face:** at the IR face closure is reduced to finitely many charge vectors (A6-n). It is countable or finite under nondegeneracy (A16-eq), and exact equality is OPEN (A6).
  - **(b) Flow:** exact integrated closure by a strictly non-BPS static field exists at some face for every u ∈ [1, 1 + Δ_UV/n) and n ≥ 248, at either u, unless two minimizers straddle closure (A9-T). The 1142 float and u-label gates are gone. The residual is A9-u.
  - **(c) Warp:** it forbids global minimizers (H2, H3) but not static non-BPS fields (A8-R).
  - **(d) Profile:** the x-block closes kinematically with anti-M5 densities (A12-a). Pure-E₈ profile closure is OPEN (A12-b).
  - **(e)** None of this is a geometric solution at the end faces (1142 A13 / 1120 D-D, given J1). **Junction UNSOLVED.**

| label | count | items |
|---|---|---|
| PROVED | 7 | H1, H2, H4, H5, H6, A9-g, A12-a |
| CONDITIONAL | 6 | H3, A8-R, A6-n, A16-eq, A9-T, V″ |
| OPEN | 4 | A6, A16, A9-u, A12-b |
| REFUTED | 0 | — |

Check: 7 + 6 + 4 + 0 = 17. Header = body.

**Test map** (gapjx_gap_run.log, 21/21):

| tests | items |
|---|---|
| H1a–b | H1, A8-R(iii) |
| H2 | H2 |
| H4 | H4 |
| H5a–g | H5 |
| H6a–d | H6 |
| H6e | consistency only, not evidence |
| Gc1–2 | A6-n (test target) |
| A9a–b | A9-T endpoint signs (test targets) |
| A12a | A12-a |

H3, A8-R(ii), A16-eq and A9-T's compactness use literature theorems (Taubes grafting, Sedlacek/Uhlenbeck, ε-regularity) that are not re-checked, so those rows are CONDITIONAL.

Nothing adopted (including the 1142 grades and the 1120 framing). Junction UNSOLVED. No CERT. Tip 7cddb188… untouched. NL derived proposal.
