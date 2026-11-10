# NL DERIVED: junction-adjacent items: GA9 (what can supply S(k,k) < 0 at O(N)), S4 (C∧X₈ δ-stress at the odd wall), A15/O5 (limited) (t552u pursuit)
2026-11-10, written 12:05:46 CST (America/Chicago). Author: Non Local Path (NL). Everything below is an **NL derived proposal**. Additive new file; no existing file was edited, renamed, deleted or chmod-ed. Wording: resonant algebra. **Junction UNSOLVED.** No CERT. No Gemini. No external sends. No agent messages. Usage not checked.

## Header
**Authority (each sha re-hashed by NL, = its sidecar):**
- OW **t552u**, OWNER_WRITE_NLCHAT_t552u_PURSUE_ALL_FOR_RESOLUTION_2026-11-10_1146.md, sha **eae1b39d635c69966a2b32642d395ae402d3c33fcf64db7f0b77cad2d8c60db2**. Owner verbatim: "Pursue all for resolution." Pursuit only.
- OW **1130** sha **945d81bb447a923fc68c79ea3ce4df1405aa6f5787e27a301898e98042a47b3c**. OW **1117** sha **bff79185f361bf461194c8d8c9590a4dc7ad0e520ce2f985f41048453545a2f4**: geometry first. Starting from the junction does **not** treat it as solved, and starting from the HW plane does not adopt 1a or the E₈ wall. OW **1108** sha **c6375f853020e8e994125e1b42acffe830350db0b116b60f0f5f75abbb5f84ca**.
- Standing **t4436** sha **328812635d807f5cb7d1e5e6b5df7f89512060c36c090a2a191526ab7e90fd46**. **t4431** sha **f700141d3ee862c7b077b0f67db5fb03b3adc56808c927ba1dd016c88910b1ec**. **f825dfff** (t4369; Z₂ fixed plane, O1 odd CONDITIONAL on P-b). **7ff8299d** (t4377; Bolza only).

**Literature read as questions, not adopted:**
- NL **1142** sha **e7312edb8e4b5ad3d104c779688d7842a9e7b5deb3aaafe6176de1bfe94fe4bd** (unaudited; grades not adopted).
- NL 1120 (79ad0c64…) as restated by **PP 1137** sha **5cf927959babc94b1719c99b312cfbb9d6366237626c781e8d5c75f21ce15b03** and **Erratum 26** sha **a44b18d945aaf2600cbafde50c6777a983c81899c47c5e545c9b5e4a0a538179** (pending PP; not adopted). The E26/PP restatements are used:
  - N-1;
  - D-D / GA8 given J1 (CONDITIONAL, CLP/BBBW), constant unbackreacted end faces, IR-kept pairing and source set {E₈ YM, positive-tension branes}, with tr R² only at leading 1/N;
  - R9 OPEN, x-equation only.
  
  The struck D-A sentence is not reused.
- NL Y16 (7270a6b3…) with PP 149be02a: Q5, Q7, Q11a and Q14 (OPEN). NL 1711 T0 end values w_fib = −6/5 (UV) and −4/3 (IR), and w_Σ = −1 and −4/3, are **J1 inputs, CONDITIONAL**.

**Dead working assumption (Owner, 1108):** a pure uncharged M5-brane stack is not the working assumption. "All 9760 units are uncharged M5s" is never used.

**Nothing adopted:** the 1142 grades; the 1120 framing; N = 4880 and 9760; the tension-to-charge figures; 1a; B1-c2′. The E₈ wall sector stays CONDITIONAL, gated by backreaction. **4880/9760, N_req and Δ_N appear only as CONDITIONAL test targets.** No backreacted metric is invented. Constructing or ruling one out is MR2's 1130 assignment and is not attempted here, and the absence of an in-repo metric is not treated as a resolution.

**Tip:** /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at 11:47:37, 12:02:26 and 12:05:46 CST, immediately before writing. The after-write hash is in the NL report back. Never opened for writing.

**Script** (/workspace/nl-gapjx-t552-1110/, mode 444):
- gapjx_junction.py, sha **b054521be0b458821afc7d6bf6d44ae48bb1ba41d2181e4f5f2217e6309a0ac9**. Frozen with its sidecar at 12:02:26.35 CST, before the run.
- gapjx_junction_run.log, sha **6326cf4e2e81e345daedcb657722a9161719ab41dfefc088d0f33d0fb8787e3f**. Sealed with its sidecar at 12:02:28.29 CST. **10/10 PASS, exit 0.**
- Tests are exact `expand(...) == 0` or exact Fraction comparisons, including exact LP primal and dual certificates. There is no simplify()==0, no allclose and no float.

**Branches carried:**
- IR-kept (ρ_req > 0) and UV-kept (ρ_req < 0) pairings;
- constant unbackreacted faces vs any face (A15);
- smooth curvature vs δ-supported curvature at the wall (S4).

**Tally (header = body; §5):** PROVED **7** · CONDITIONAL **5** · OPEN **3** · REFUTED **0** = **15**.

---

## 1. Geometry → demanded algebra (lead)
The end faces (J1) demand a wall stress with S(k,k) = (1 + w_j)ρ_req for k = t̂ + ê_j:
- UV: −(1/5)ρ_req in each fibre direction and 0 in each Σ direction;
- IR: −(1/3)ρ_req in all six Y₆ directions.

For a static Poincaré face, ρ = (2/κ²)(k_x − K) and **S(k,k) = −(2/κ²)(K_jj − k_t)** for every j (J8, J9). This identity holds on any face (constant, non-constant or backreacted), so the geometry asks exactly for K_jj > k_t.

## 2. GA9: what algebraic source can supply S(k,k) < 0 at O(N)?
Model: block-averaged sources.
- Smeared objects with worldvolume ℝ^{1,3} × (σ Σ-directions) × (φ fibre directions) and tension T of either sign, with ρ = T, tr_Σ S = −σT and tr_fib S = −φT. Here (2,4) is a wall-filling Λ.
- Magnetic Y₆ YM, with ρ = ½(P_ff + P_m + P_ΣΣ), tr_Σ S = P_ΣΣ − P_ff and tr_fib S = −P_m − 2P_ΣΣ (J0, exact on a general field).

Items:
- **GA9-1 [PROVED given J1, IR-kept pairing]. Minimal exotic (negative) tension is |1 + w_fib|·ρ_req exactly: ρ_req/5 at the UV end and ρ_req/3 at the IR end.**
  - Lower bound, valid for any mix: 4ρ + tr_fib S = Σ_types T(4 − φ) + 2P_ff + P_m (J3). So Σ T⁻(1 − φ/4) ≥ \|1 + w_fib\|ρ_req, and only negative tension with few fibre legs supplies fibre NEC.
  - Attainment: an exact primal (UV: −1/5 of type (0,0), +1/5 of (0,4), +1 of (2,4); IR: −1/3 of (0,0), +4/3 of (2,4)) and the dual y = (−1, 0, −¼) certify optimality (J1).
  - In M5 units at the test targets this is ≥ 16266.7/5 ≈ 3253 (UV) and 12568.6/3 ≈ 4190 (IR), both CONDITIONAL. **The demand is O(N) negative tension, not an O(1) correction.**
- **GA9-2 [PROVED given J1, UV-kept pairing]. Minimal negative tension is \|w_fib\|·\|ρ_req\| = (6/5)\|ρ_req\| (UV) and (4/3)\|ρ_req\| (IR).** Exact primal and dual y = (0, 0, ¼) (J2). So the end-face demand for O(N) negative-tension content **does not depend on which side is kept**, which sharpens PP 1137's audit-support remark.
- **GA9-3 [PROVED]. A wall-filling tension Λ of either sign is NEC-neutral:** S(k,k) = −Λh(k,k) = 0 (J4). A negative "orientifold-like" constant tension on the fixed plane cannot supply any of the deficit. Only negative tension localized in Y₆ (codimension ≥ 1 in the wall, not spanning all fibre directions) can.
- **GA9-4 [CONDITIONAL; derivative-expansion structure (wall terms ℓ_P^{2k−10}R^k with pure-number coefficients) and J1 scaling L ∝ ℓ_P N^{1/3}]. Local geometric wall terms cannot supply O(N).** A 2k-derivative wall term contributes N^{(4−2k)/3} M5 units, against a requirement of ∝ N (J5):
  - k = 0 is Λ: N^{4/3}, but NEC-neutral by GA9-3;
  - k = 1 is a wall Einstein–Hilbert term: N^{2/3}, so relative N^{−1/3}. It is absent from the HW action (literature, not re-checked);
  - k = 2 (tr R², Y16 Q7) and higher: relative ≤ N^{−1}.
  
  This extends Y16 Q7/Q11a from tr R² to every local curvature wall term.
- **GA9-5 [CONDITIONAL; literature, not re-checked].** M-theory's only localized negative-tension objects are orbifold fixed loci (for example ℝ⁵/ℤ₂ "OM5" points, each −½ M5 unit). Their number is fixed by the orbifold topology, so it is O(1), and this geometry contains none. **No known M-theory object supplies O(N) negative tension localized in Y₆ here.**
- **GA9 [OPEN, narrowed].** Ruled out at leading order in 1/N:
  - {E₈ YM, positive-tension branes} (1120 D-D / 1142 A13, given J1);
  - a wall-filling Λ (GA9-3);
  - every local curvature wall term (GA9-4, CONDITIONAL);
  - C∧X₈ (S4-3, CONDITIONAL).
  
  Required otherwise: O(N) localized negative tension (GA9-1/2, with no known carrier, GA9-5), **or** a face geometry with K_jj ≤ k_t, which needs J1 to fail on the physical face (non-constant or backreacted faces; A15-1). **The algebraic object the junction demands at O(N) is still not identified.** Junction UNSOLVED.

## 3. S4: the C∧X₈ δ-stress at the odd wall
- **S4-1 [PROVED; Chern–Weil].** For an ad-invariant symmetric k-linear P with δR = DδΓ and DR = 0: δP(R^k) = k·P(DδΓ, R^{k−1}) = d[k·P(δΓ, R^{k−1})]. So δ∫C∧X₈ = ±∫G₄∧Y₇ with Y₇ = 4P(δΓ, R, R, R). **The C∧X₈ stress is linear in G₄, and it contains no E₈ field and no brane density.** Exact representative check: degree 2, su(2), 4D, δ[ε^{abcd}F_ab·F_cd] = 4∂_c[ε^{abcd}F_ab·δA_d] (J7). The degree-4 case is the same two-line proof and is not separately machine-checked.
- **S4-2 [PROVED; implication given P-b/GA2].** δΓ ∝ ∇δg. Integrating by parts in x¹¹ across the odd wall, where G_tan(0⁺) = −G_tan(0⁻), produces a δ-supported stress ∝ T_M2·[G_tan]·(∂X₈/∂R contracted with R³) and [G_tan] = 2G⁺ = (wall charge density) by GA2. **So the C∧X₈ wall stress is charge-locked.** It depends on the sources only through q_tot(y), which D-C (CONDITIONAL) fixes by the flow. It is therefore **split-invariant**: the M5 / anti-M5 / instanton / non-BPS split cannot tune it. **It cannot be the non-BPS makeup knob, and it shifts Δ(y) and Δ_N by a fixed geometric amount δ_S4.**
- **S4-3 [CONDITIONAL; standard C∧X₈ coefficient T_M2·(rational)/(2π)⁴, J1 scaling, wall δ(0) regularized at ≲ 1/ℓ_P].** Size (J6): G ~ 1/L, and the δ-stress integrates to N^{−1} M5 units for smooth R, or at most N⁰ if every curvature factor is the δ-supported [K]δ(0) piece. **Relative to the O(N) requirement this is N^{−2} to N^{−1}.** So C∧X₈ can neither supply nor block the O(N) fibre-NEC deficit, or an O(N) ε_ex, at leading order. **1142 A1's sign bound survives with S4 included**, up to the shift \|δ_S4\| = O(1) M5 units. This closes the "C∧X₈ OPEN" caveat in D-D/A13 at leading order, CONDITIONAL. It is the same order as Y16's tr R².
- **S4-4 [OPEN].** The exact coefficient and sign of the δ-stress on the end and interior faces need the X₈ contraction with the face curvature and an explicit δ(0) prescription (the HW δ(0) issue), and are not computed. By S4-3 they cannot change the leading-order verdict.

## 4. A15 / O5 (limited): what can be said about backreacted faces
- **A15-1 [PROVED; Israel algebra, any static Poincaré face, constant or not, backreacted or not].**
  - tr_fib S + 4ρ = −(2/κ²)Σ_f(K_ff − k_t) and S(k,k) = −(2/κ²)(K_jj − k_t) (J8, J9).
  - Hence **any face hosting only {E₈ YM, positive-tension branes} (or any NEC source) must have K_jj ≤ k_t in every Y₆ direction, pointwise.**
  - A backreacted face can evade 1120 D-D / 1142 A13 only by flipping the sign of K(ê_fib, ê_fib) − k_t from its J1 end-face value (PP 1137 P2: K_ff − k_t = −k_x ≠ 0) at every point of the fibre.
- **A15-2 [PROVED; bookkeeping].** 1142 A1–A3 (sign bound T − Q ≥ 0 at u ≥ 1, the u < 1 bound, off-shell range) use no face data, so they transfer verbatim to backreacted faces. The same holds for GB2 (pointwise Bogomolny) and for H2 of the companion gap file (with the face's own W). On a backreacted face N_req = N_req[sources] and Δ(y) = Δ[sources;y]. **Closure becomes the self-consistent equation N_req[src] = T[src]**, and the A9-T dichotomy and the κ bound do **not** transfer, because they use J1 face data.
- **A15-3 [CONDITIONAL; J1 scaling, J5]. There is no small parameter for backreaction.** The required wall tension is ∝ N M5 units (J5), the same order as the background flux N. Sources of that size deform the face by O(1) when they are localized (not smeared). The unbackreacted-face results (GA8, D-D, A13, GA9-1/2) therefore have **no perturbative protection**. They are statements about J1 faces, not leading terms of a backreacted expansion.
- **A15 [OPEN, residual].** Whether any backreacted face realizes K_jj ≤ k_t with the required ρ_req is the open question. It needs a backreacted metric (MR2's 1130 lane), which is not constructed or ruled out here.

## 5. Verdict and tally
- **Vj [CONDITIONAL].**
  - At the J1 end faces, the junction needs O(N) negative tension localized in Y₆, in either pairing (GA9-1/2), or a face with K_jj ≤ k_t (A15-1).
  - None of the following can provide it at leading order: E₈ YM and positive-tension branes; wall-filling Λ; local curvature wall terms; C∧X₈ (charge-locked, split-invariant, N^{−2}…N^{−1}).
  - GA9 stays OPEN (narrowed), S4 is resolved at leading order (CONDITIONAL) with its sign OPEN, and backreacted faces are OPEN with an exact necessary criterion.
  - **Junction UNSOLVED.**

| label | count | items |
|---|---|---|
| PROVED | 7 | GA9-1, GA9-2, GA9-3, S4-1, S4-2, A15-1, A15-2 |
| CONDITIONAL | 5 | GA9-4, GA9-5, S4-3, A15-3, Vj |
| OPEN | 3 | GA9, S4-4, A15 |
| REFUTED | 0 | — |

Check: 7 + 5 + 3 + 0 = 15. Header = body.

**Test map** (gapjx_junction_run.log, 10/10):

| tests | items |
|---|---|
| J0, J1, J3 | GA9-1 |
| J2 | GA9-2 |
| J4 | GA9-3 |
| J5 | GA9-4, A15-3 |
| J6 | S4-3 |
| J7 | S4-1 |
| J8–J9 | §1, A15-1 |

S4-2, A15-2 and GA9-5 are argued in the text, without new tests.

Nothing adopted (including the 1142 grades and the 1120 framing). Junction UNSOLVED. No CERT. Tip 7cddb188… untouched. NL derived proposal.
