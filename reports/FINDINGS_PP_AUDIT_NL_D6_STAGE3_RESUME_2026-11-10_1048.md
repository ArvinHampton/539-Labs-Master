# FINDINGS — PP audit of the NL D6 stage-3 resume (Erratum 24, E5, E2, E4, E1, S2-8, Z2 corner)
PP, 2026-11-10, all times CST (America/Chicago). Labels are pure math (PROVED / CONDITIONAL / OPEN / REFUTED / PENDING). Additive; no existing file edited. No CERT, no Gemini, nothing sent, nothing adopted. **Junction: UNSOLVED.** "Resonant algebra" is the term in use (RTA is a historical alias only).
Authority: Owner call-83d7a0fa (OWNER_WRITE_CALL_83d7a0fa_STATUS_ROUND_THEN_RESUME_PURSUIT_2026-11-10_0953.md, e72a188b…, verified earlier), standing OW t4436 (32881263…). These are NL-derived proposals: only this audit keeps or drops a branch.
Baseline: PP f530cbc0 (stage 2), PP ac4446d6 (Erratum 23 confirm), PP 113e8035 (stage-3 E3/S5) and the 2245 tallies (E3 3/0/0/0, S5 3/0/1/0; 2216 revised 8/2/3/0). No Local t4436 or MR2 E8 tallies are mixed in.

## 0. Integrity
- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start (10:31) and before writing (10:46). Not touched.
- All 7 target files match their sidecars (re-verified at 10:31 and at 10:46):
  60bbc718… (Erratum 24, mtime 09:57:04), 0a7d8e56… (E5, 10:19:44), 197c5bd1… (E2, 10:21:12), 4c25565f… (E4, 10:21:44), 2f33b65d… (E1, 10:22:21), d559cb7d… (S2-8, 10:22:43), 101467fc… (Z2, 10:27:43). Header HHMM agrees with mtime to within one minute for all seven (Erratum 24's "0958" label is ~1 min ahead of its 09:57 mtime; harmless).
- /workspace/nl-d6s3-1110/: all 12 .py/.log match their sidecars, with the full shas given in the brief. Every script mtime precedes its log mtime (chirality 10:11:37 → 10:11:41; e2 10:20:04 → 10:20:12; continuation v2 10:13:29 → 10:25:58; relabel v2 10:16:41 → 10:24:35; v1 continuation 10:10:16 → 10:12:52; v1 relabel 10:15:56 → 10:15:57). Shared definitions file /workspace/nl-bps-d6-2057/z2_centre_flow_faces.py = 21bcbc3f… = sidecar.
- Script hygiene: no `allclose`, no `simplify(...)==0` in any NL script. The chirality and e2 scripts use exact Gaussian-integer matrix equality and exact rank over ℚ(i), and exact linear `sp.solve`. Dead code (unused `proj`, an empty loop at lines 130–134 of the chirality script) is harmless. The Z2 scripts are float and are graded as float.
- I wrote nothing into /workspace/nl-d6s3-1110/ or any Local or MR2 directory. I did not touch Local jobs (observed read-only: 932685, 1015729 and 1096505 present; 1088107/1088109 no longer present at 10:39, not my doing). All re-runs ran under `nice -n 19` with low memory.

## 1. PP evidence (/workspace/audit-scratch/pp_nl_d6s3_1030/, every file chmod a-w, each with a .sha256 sidecar)
| file | sha256 | content |
|---|---|---|
| pp_d6s3_resume_exact_2026-11-10_1045.py | 0dc4c51002d30257efb6272366801539b14f0b7f54b7ae0d3c09b19316730d06 | PP's own exact checks P1–P12. Sidecar frozen before the run. The "1045" suffix is a label; real mtime 10:40:34 (authoritative) |
| pp_d6s3_resume_exact_2026-11-10_1045.log | 53be779cc3e3be5d180e61d95164eb43170eac637c98fbf1b44ef4be3b85d202 | exit 0, 10:40:38 |
| chirality_hw_lock_exact_2026-11-10.py (copy) | 3ed7f879… (identical to NL's) | re-run from scratch |
| rerun_chirality.log | 676f7dc85c40318b90f3ba9dcdec6582834eae4cb45dec61a8aae613fd12ab9c | **byte-identical** to NL's log (cmp) |
| e2_pairs_degree_exact_2026-11-10.py (copy) | 5a23b6716a684d125e6a0252b5784516f730313bd4772dced42c8bf14c1d0209 | NL's script with only the exec path changed to the PP copy (diff = 1 line) |
| rerun_e2.log | 66f95d9a7442dac16f8503ce0424c75bf21174d062d20ded3cc2db9f44c3efdd | **byte-identical** to NL's log (cmp) |
| z2_corner_relabel_v2_2026-11-10.py (copy) | d8ba9274… (identical) | re-run (float) |
| rerun_relabel_v2.log | 545d7167987b2a0c2c21c9405a124728dd8a9578db619e8ffa7bc72e3767963c | every data line identical to NL's 2171c250 log. The only diffs are the script path inside two ComplexWarning lines |
| rerun_*.exit | 28d3b9e8… | all "exit 0" |

PP's own build (P1–P12) is independent of NL's. It uses a reversed Pauli chain, with frame labels assigned to generators by a fixed shuffle. It lands in the **other** inequivalent Clifford(1,10) representation: Γ^{0…10} = −1, whereas NL's has +1. Every conclusion below holds in both representations.
- P1/P2: Clifford relations exact; vol = c·1 with c = −1.
- P3: Γ^{0123} commutes with all 7 internal Γ^y, all 21 internal Γ^{ab}, all 35 internal Γ^{abcd} and Γ_yΓ^{0123}; it anticommutes with all 4 Γ^μ.
- P4 (control for premise (h0)): Γ^{0123} commutes with an internal X but **anticommutes** with Γ_μX for every μ.
- P5: Γ^{0123}·Γ^r·Γ^{S12}·Γ^{m1m2}·Γ^{tf} = c·1 as an operator identity, which is stronger than an enumeration of eigenspaces.
- P6: for **both** lock orientations Γ^{S12} ± Γ^{m1m2}, both χ₄ and both Γ^r, exactly one s₃ occurs: dimensions (4,0) or (0,4) in all 8 cases.
- P7: control without the lock gives (4,4).
- P8: with χ₄, s₂′ and Γ^r = +1 fixed, s₁s₃ is fixed. Fixing (χ₄, Γ^{12}, s₁, s₂′, s₃) gives dimension 1, without fixing Γ^r separately.
- P9: Γ^{S1} flips s₁ and Γ^r and keeps χ₄, s₂′, s₃, Γ^{12}. Γ^t flips s₃ and Γ^r and keeps the rest. Γ^0 flips χ₄ and Γ^r.
- P10: a charge-conjugation matrix B (product of the 7 real Γ's) satisfies B Γ̄_M = Γ_M B, and B X̄ = X B for X ∈ {Γ^{0123}, Γ^{12}, Γ^{S12}, Γ^{m1m2}, Γ^{tf}}. So conjugation maps the line (χ₄, Γ^{12}, s₁, s₂′, s₃) antilinearly onto (−χ₄, −Γ^{12}, −s₁, −s₂′, −s₃).
- P11: the K-invariant symmetric forms on the weight-1 4-plane (L_S ⊕ L_S^⊥) form a 4-dimensional space. With U(1)_R added the space is 2-dimensional (diagonal only).
- P12: there are exactly 3 U(1)_R × U(1)_n̂-invariant tangential 4-forms on the E2 face (no n-leg and no x-leg): T1T2m1m2, T1T2tf, m1m2tf.

## 2. Load-bearing item A — E5-3 / Lemma CH, including the chirality step (b)
**Hand proof (PP), independent of the script.**
- (a) Γ^{0…10} = c·1 with c = ±1 according to the representation (NL +1, PP −1). Only constancy is used.
- (b) Γ^{0123} is a product of 4 gammas. It therefore commutes with any gamma outside {0,1,2,3}, since passing it through costs (−1)^4. It anticommutes with each Γ^μ inside, at a cost of (−1)^3.
  - Under (h1) (flat Poincaré slices, warp x-independent, no G with 1–3 x-legs), the internal rows D_y contain only:
    - the internal spin connection (Γ^{ab} internal);
    - internal G terms (Γ_y^{abcd} and Γ^{abc});
    - the electric term Γ_y^{0123}G_{0123} = ±Γ_yΓ^{0123}G_{0123}.
    All of these commute with Γ^{0123} (P3).
  - The x-rows are D_μ = ∂_μ + Γ_μX, where X = ½Γ^y∂_yA + (internal G̸)/288 + c′G_{0123}Γ^{0123}. X commutes with Γ^{0123}.
  - The HW projector Γ^n has n internal, so it commutes.
  - The Kosmann action of an internal, x-independent, warp-preserving Killing vector ξ is ξ^y∇_y + ¼(dξ)_{ab}Γ^{ab}. Here dξ has only internal–internal legs, because ∇_μξ_ν = e^{2A}η_{μν}ξ·∂A is symmetric. So it commutes too.
- **Gap found in (b): an unlisted premise.** Γ^{0123} anticommutes with Γ_μX (P4). It therefore maps the solution space of ∂_με + Γ_μXε = 0 into that of ∂_με − Γ_μXε = 0. It preserves the Killing-spinor space only on x-independent spinors, ∂_με = 0, where the x-row reduces to Xε = 0.
  - Concretely, superconformal-type spinors ε = (1 + x^μΓ_μ…)η mix chiralities.
  - So (b) holds under **(h0) = Erratum 24 (h2): x-independent (Poincaré) supercharges**. E5 §0 lists only "(P-a) at least one Killing spinor". E2-4 step 1 uses x-independence ("Lorentz acts on x-independent Killing spinors algebraically") without listing it.
  - Since (h2) is already the program premise on record (Erratum 24, PP 113e8035), this is a premise-list completion and not a defect in the math. It is the same treatment PP gave S3a-2.
- Under (h0), V_ℂ (complexified x-independent Killing spinors) splits as V₊ ⊕ V₋ by χ₄ = ±i. Each summand is invariant under SU(2)_R, U(1)_R, K, Lorentz and the HW condition, so every irreducible SU(2)_R multiplet lies in one V_±. **Both members of a doublet share χ₄. ✓**
- (c) From P5 (or NL [3]), on joint eigenspaces χ₄·g_n·(is₁)(is₂′)(is₃) = c.
- (d) On ker(Γ^{S12} ± Γ^{m1m2}) we have s₂′ = ∓s₁. So (is₁)(is₂′) = ±1 is a fixed sign, and with χ₄ and g_n fixed, **s₃ = −i·c/(±χ₄g_n) is determined**. This holds for either lock orientation and either representation (P6).
- (e) Without the lock, both s₃ occur (P7).

**Ruling: E5-3 PROVED (exact + hand proof). Part (b) is graded as an implication under (h0)/(h2) and (h1); NL must list (h0) (Fix 1).** NL's script is corroboration: re-run byte-identical, and PP's independent build agrees in the other representation.

## 3. Load-bearing item B — E5-4 (no HW-BPS wall in H_Σ ∩ SO(3)_R, with or without U(1)_R)
**Premises (complete list, PP):**
- (h0)/(h2) x-independent supercharges;
- (h1);
- (P-a) at least one Killing spinor;
- (ii) the D1 HW projection Γ^nε = ε on the face (not S6);
- (reg) at one face point p ∈ C₄ ∩ face (C₄ ∩ face ≠ ∅ is implicit here);
- (tw);
- H_Σ;
- SO(3)_R acting on the S² factor and commuting with the twisted SL(2,ℝ).

**Check of the inputs:**
- **E5-1 (PROVED).** Homogeneous-bundle correspondence: K-invariant fibre tensors over p̃ ⇔ SL(2,ℝ)-invariant fields. A component is K-invariant iff q_Σ + q_R = 0. The two-Σ-leg area form has q_Σ = 0, so U(1)_R breaking can only sit in one-Σ-index metric terms (q = ±1) or the traceless g_ΣΣ (q = ±2). With P-c, the flux cannot carry it. ✓
- **E5-2 (PROVED, implication).** PP's §3 proof (f530cbc0) uses only the cocompact surface group, a finite-dimensional representation of the twisted SL(2,ℝ), the conjugates of a hyperbolic generator, and the stabiliser action. U(1)_R is never used separately, so the lock holds on E5 ∩ H_Σ. ✓
  - The frame claim also holds with cross terms. K acts on T_p isometrically, so its weight spaces are orthogonal, and on the weight-1 4-plane it acts by a metric-compatible complex structure J.
  - C₄ is G-invariant, hence K-invariant, so L_S = T_pC₄ ∩ (weight 1) is J-invariant, and so is L_S^⊥. So K acts on spinors at p as ½(Γ^{S12} ± Γ^{m1m2}), with the sign fixed by J. Both signs give (d) (P6).
  - n = ±e_r follows even more directly: C₄ ⊂ face gives n ⟂ T_pC₄ ⊃ T_pS², and n is K-invariant and ⟂ x. So n is the unit vector of span(x, r, TS²) orthogonal to x and TS².
  - "C₄ isotopic to the vacuum locus holds automatically" is correct, because by (tw) the K-fixed set is {μ_a = 0} in bundle coordinates.
- **PP proof of E5-4 (streamlined; it does not even need the doublet decomposition).**
  1. Take V₊ ≠ 0 (otherwise use V₋). It is a finite-dimensional complex representation of su(2)_R (Kosmann).
  2. Let U(1)_n̂ ⊂ SU(2)_R be the stabiliser of the S²-point of p. At its zero p, (L_ξε)(p) = ½Γ^{tf}ε(p). So by injectivity and equivariance of ev_p (reg), the U(1)_n̂-weights on V₊ are s₃/2 for the s₃ values that occur at p.
  3. Every ε ∈ V₊ satisfies at p: χ₄ = i, Γ^n = +1 (ii, with n = ±e_r), and the lock (E5-2). By (d), ε(p) has the single value s₃ = s₃*.
  4. So V₊ has the single U(1)_n̂-weight s₃*/2 ≠ 0. But the weights of any nonzero finite-dimensional su(2)-representation are symmetric under w ↦ −w. Contradiction. ∎
  NL's version (a chiral doublet with opposite s₃) is the same argument restricted to one irreducible summand. It is correct.
- Flux, Bianchi, N_face, IR, σ, the D1 rows and n(χ) are indeed unused. U(1)_R is unused.

**Ruling: E5-4 PROVED (implication), under the premise list above.** **Proposed drop of E5 ∩ H_Σ (∩ SO(3)_R, with or without U(1)_R): ACCEPTED** on this PROVED implication, conditional on the premise list being recorded by NL (Fix 1, Fix 2). This also gives an independent, flux-free route to the S2-7 conclusion on scope S. S2-7 itself stays COND as filed, and its grade is not changed by this audit.

## 4. Load-bearing item C — E2-4 (degree obstruction on E2 with SO(3)_R × U(1)_R)
**Premises (complete list, PP):**
- (h0)/(h2), (h1), (P-a);
- (ii) the D1 HW projection, **not** "record premise S6" (Fix 2);
- (reg-all) on all of C₄ ∩ face;
- (F-4) face bundle ≅ vacuum twisted bundle, and C₄ ≅ Σ×S² isotopic to the vacuum locus, with SO(3)_R acting only on S² and U(1)_R fixing C₄ pointwise and acting there as ½Γ^{m1m2};
- Σ connected, of genus 2.
(gr) is listed by NL but not needed: Σ_n̂ ⊂ C₄ ⊂ face gives T_pΣ_n̂ ⟂ n, so the T-plane **is** TΣ_n̂.

**Step-by-step check:**
1. **E2-1 (PROVED).** S2-3's proof uses only ev_p injectivity, the U(1)_n̂ isotropy action ½Γ^{tf} at p, and the commuting U(1)_R. H_Σ is not used. Doublets of fixed U(1)_R charge have a common s₂′ and opposite s₃. ✓
2. **E2-2 (PROVED, sector content).**
   - Joint weight spaces of U(1)_R × U(1)_n̂ are orthogonal, so n ∈ span(r, S1, S2), and an orthonormal frame (x | n | T1, T2 = TΣ_n̂ | m | t, f) exists continuously over Σ_n̂.
   - With χ₄, s₂′ and Γ^n = +1 fixed, s₁s₃ is fixed (P8; NL [5]). So each doublet member is single-sector at every wall point, the members have opposite s₁, and **exactly one is unlocked**. ✓
   - *Scope note (Fix 4):* the "forced by equal D1 K" column of the flux table is computed with **diagonal** K (one k_S on the Σ/T-plane). On E2 the T-plane has no isotropy, so K|_T is a general symmetric 2×2. The column therefore does not transfer as stated. The conclusion "the D1/flux route leaves ω₂ free" survives, because enlarging the K family only adds solutions. Not load-bearing for E2-4. The 3 invariant tangential face fluxes are confirmed (P12).
3. **E2-3 (PROVED; PP hand version).**
   - Fixing (χ₄, Γ^{12}, s₁, s₂′, s₃) gives a complex line ℓ ⊂ S|_{Σ_n̂} (P8: dimension 1).
   - Constant x-gammas give isomorphisms flipping χ₄ and/or Γ^{12}. Clifford multiplication by e_t (a nowhere-zero section of the trivial tf-plane bundle over Σ_n̂) flips s₃. So deg ℓ depends only on (s₁, s₂′) (P9).
   - Clifford multiplication by TΣ gives ℓ(s₁, s₂′) ≅ T^{1,0} ⊗ ℓ(−s₁, s₂′) or T^{0,1} ⊗ ℓ(−s₁, s₂′). So d(+, s₂′) − d(−, s₂′) = ε₀(2g−2), with ε₀ = ±1 independent of s₂′.
   - Conjugation (P10) gives d(−s₁, −s₂′) = −d(s₁, s₂′), so d = a·s₁ + b·s₂′ and 2a = ε₀(2g−2).
   - The vacuum (S2-1 exact, plus F-4) gives a nowhere-zero section of a locked line, so a − b = 0. Hence **both locked lines have degree 0, and both unlocked lines have degree 2a·s₁ = ±(2g−2) = ±2**. ✓
   - *Wording (Fix 5):* "locked lines are trivial" should read "have degree 0". Only the degree is used, and isomorphism classes can differ by 2-torsion through the spin structure.
4. **E2-4 (PROVED, implication).**
   - Take ε a joint eigenvector of χ₄, Γ^{12}, the U(1)_R charge and SU(2)_R weight +½. These commute with each other and with the KSE under (h0). Let ε′ = T₋ε ≠ 0.
   - s₁* is fixed by (χ₄, s₂′) and the continuous orientations, so the same member, say ε_u, is unlocked at **every** point of the connected Σ_n̂.
   - ε_u|_{Σ_n̂} is a continuous section of ℓ_unlocked. It vanishes nowhere, by (reg-all) and the parallel-section/ODE uniqueness argument up to the face.
   - So deg ℓ_unlocked = 0, contradicting ±2. ∎
   - The genus dependence (it fails at g = 1) is correctly noted.

**Ruling: E2-4 PROVED (implication), under the premise list above.** **Proposed drop of E2 ∩ (SO(3)_R × U(1)_R): ACCEPTED** on this PROVED implication, with Fix 1 and Fix 2 recorded. Not covered: a face singular on any nonempty part of C₄, E2 ∩ E5, E2 ∩ E1, and failure of (F-4) on E2.

## 5. Remaining files
### File 1 — Erratum 24 (60bbc718), claimed 0/0/0/0. Verdict: **FAITHFUL**
- E23-α credits E23-2 to PP (f530cbc0 A3, pp_d6s2_exact 2225), re-derived by NL ✓.
- E23-β: 2/0/0/0 is a row count and 0/0/0/0 distinct ✓.
- F-1/F-2: (h1)–(h5) and the ε†ε norm, with the "only premise" sentence retracted ✓. (h2) explicitly includes "x-independent (Poincaré supercharge)", which is the anchor for (h0) above.
- F-3 (truncation-only gloss; S3b-1 not needed for the no-go) ✓.
- F-4 (dG = 0 on the face slice, face bundle ≅ vacuum, C₄ isotopic) ✓.
- F-5 (BPS only; S2-4 and S2-6 premises inherited; S2-7 COND; S3b-4 OPEN) ✓.
- Earlier tallies are unchanged: 2216 8/2/3/0, E3 3/0/0/0, S5 3/0/1/0 ✓.
- PP tally **0/0/0/0**, agrees.

### File 2 — E5 (0a7d8e56), claimed 6/0/1/0
| id | NL | PP |
|---|---|---|
| E5-1 | PROVED | PROVED |
| E5-2 | PROVED (impl.) | PROVED (impl.) |
| E5-3 | PROVED (exact) | PROVED (exact + hand). (b) needs (h0) listed (Fix 1) |
| E5-4 | PROVED (impl.) | PROVED (impl.). Drop of E5 ∩ H_Σ accepted |
| E5-5 | PROVED (exact) | PROVED (exact), scoped to diagonal K. On E5 without U(1)_R the K-invariant forms on the weight-1 plane are 4-dimensional (P11), so "unique diagonal K" is an ansatz statement. The non-obstruction conclusion survives (Fix 4). The conjugate-pair statement (same K, opposite χ₄) is exact ✓ |
| E5-6 | OPEN | OPEN |
| E5-7 | PROVED | PROVED (implication), relative to the uplift ansatz in z2_centre_flow_faces.py (21bcbc3f). T = diag(e^{−6λ}, e^{−6λ}, e^{4λ+w}, e^{4λ+w}, e^{4λ−2w}) is SO(2)_{12}-invariant, and Δ depends on μ₁, μ₂ only through cos²χ. Checked against the source lines |

The remark that S2-6/C1's "same s₁, opposite s₃" pairs have opposite χ₄ at Γ^r = +1 is correct by (c). S2-3, S2-5 and S2-6 remain PROVED as implications; S2-6's antecedent is simply unrealised under HW + CH. **PP tally 6/0/1/0, agrees.**

### File 3 — E2 (197c5bd1), claimed 4/0/1/0
E2-1 PROVED, E2-2 PROVED (sector content; flux column scoped, Fix 4), E2-3 PROVED (Fix 5 wording), E2-4 PROVED (impl.), E2-5 OPEN. **PP tally 4/0/1/0, agrees.** NL's nit is confirmed: §0 (ii) still reads "(record premise S6)". The same mislabel also appears in **E1 §0** ("(ii) (record premise S6)"). Fix 2.

### File 4 — E4 (4c25565f), claimed 5/0/1/0
- **E4-1 PROVED.** SL(2,ℝ) × SO(3)_R acts transitively on C₄ by isometries preserving the face and the Killing-spinor space, so (reg) is all-or-nothing on C₄ ∩ face in H_Σ ∩ SO(3)_R ✓.
- **E4-2 PROVED (impl.).** The fixed set of a compact isometry group is a closed, totally geodesic submanifold (exp is equivariant). *Wording (Fix 7):* in H_Σ the fixed set of K_{p̃} is the S² over p̃. C₄ is the union over Σ, and its smoothness follows from homogeneity. C₄ itself is not "the fixed set of K".
- **E4-3: the derivation is defective, but the operative claim is PROVED once restated (Fix 3, priority).**
  - The premise "internal support of dimension 2, invariant under H_Σ and SO(3)_R" is inconsistent. Ŝ_p̃ would be discrete, hence K-fixed, hence ⊂ {μ_a = 0}, but the SO(3)_R orbit of such a point is a 2-sphere. So no such support exists.
  - "Finite" also needs compactness in r. The "smearing" step changes the object.
  - The smeared classification "the support is a union of r-translates of C₄ (α sheets)" is **not exhaustive**. The SO(3)_R-fixed U(1)_R orbits {μ₃ = μ₄ = μ₅ = 0} (circles at |μ_a| = 1), smeared over H² at any r, give H_Σ × SO(3)_R-invariant supports. They are disjoint from C₄.
  - What survives, and is all that E4-5 uses: **an invariant source support meets C₄ ∩ face iff it contains all of C₄ ∩ face** (E4-1 transitivity). PP grades this restated E4-3 PROVED. As filed, the classification sentence is not accepted.
- **E4-4 PROVED.** Stokes: ∫_B j₅ = ∫_{∂B}G = ∫_{C₄}G − k∫_{S⁴}G, with B a rational 5-chain transverse to supp j₅ ✓. It escapes the flux route only ✓.
- **E4-5 PROVED (impl.).** This is the contrapositive of E5-4/E2-4 combined with E4-1. Its list (a)–(c) is complete for failure of (reg). The other E5-4/E2-4 premises ((h0), (ii), (tw), F-4, P-a) are branch-defining and should be named as such. "Natural sources are α sheets" should be replaced by the restated E4-3 (Fix 3).
- **E4-6 OPEN.**
- **PP tally 5/0/1/0 with E4-3 restated** (as filed: 4 PROVED + E4-3 not accepted as written). This is a counting note, not a REFUTED row: the title claim stands.

### File 5 — E1 (2f33b65d), claimed 2/1/1/0
- **E1-1 PROVED (impl.).** Lock + CH at a regular face point gives s₃ = s₃(χ₄). With a residual SO(2) fixing n̂₀ (the [w] case), the charge is ±½ with its sign tied to χ₄. Conjugation flips both, so there is no contradiction. n = ±e_r holds here without SO(3)_R, by the C₄ ⊂ face argument of §3 ✓.
- **E1-2 PROVED (exact, existence).** This is a non-obstruction statement in the diagonal-K family. On [w], U(1)_R is kept, so diagonal K is forced (P11); elsewhere it is a subfamily (Fix 4).
- **E1-3 CONDITIONAL.** It rests on the cited 7D fermion-shift structure (Pernici–Pilch–van Nieuwenhuizen) and the gravitino ↔ locked identification. Not upgraded: a citation is not a proof.
- **E1-4 OPEN.**
- **PP tally 2/1/1/0, agrees.** Fix 2 also applies here.

### File 6 — S2-8 (d559cb7d), claimed 1/1/1/0
- **P8-1 PROVED (impl.).** It inherits the full premise lists of E5-4 and E2-4, including (h0), (ii), (reg)/(reg-all), (tw)/(F-4). The PDE is indeed unused there; only the KSE's parallel structure is used.
- **P8-2 CONDITIONAL.** It rests on a reading of LLM's hypotheses; not upgraded.
- **P8-3 OPEN.**
- **PP tally 1/1/1/0, agrees.**

### File 7 — Z2 corner (101467fc), claimed 1/1/1/0
- **Z-1 PROVED.** The flow is autonomous and w is continuous along an orbit with w → 0⁻ in the IR, so by the IVT the orbit passes through every w_s ∈ (w_t, 0). The label is not unique if w is non-monotone, but existence is all that is claimed ✓.
- **Z-2 CONDITIONAL (float). Not upgraded.** All figures were checked against the **v2** logs:
  - 48/54 solved; residuals ≤ 5.6e−17; all six marches reach d₆ = −0.1875 and FAIL at −0.20 (mesh); UV reach 0.06L; min margin over solved flows +0.70712.
  - Relabel: w_t = −0.05 has 25 hits, D ∈ [−0.37172, −2.459e−4], 11 corner orbits D ∈ [−0.372, −0.206]. w_t = −0.10 has 28 hits, D up to +0.0845, 7 corner orbits down to −0.286. w_t = −0.30 has 37 hits, D ≥ −0.188, no corner orbit.
  - No NEC face; overall min +0.50017; corner-orbit min +0.7071; D2 deviation 3.000 on corner orbits; overall min 5.749e−3 at (w_t = −0.30, a = +0.015) with margin +0.707.
  - PP re-ran relabel v2 from a scratch copy, and every data line is identical (545d7167).
  - v1 (both) is cited as record only and is not used as grounds ✓.
- **Z-3 OPEN** (S2-13; non-BPS S5 OPEN; S6 a record premise) ✓.
- Hygiene: see Fix 8 (v1 stop time) and Fix 9 (ComplexWarning).
- **PP tally 1/1/1/0, agrees.**

## 6. Tallies
| file | NL | PP |
|---|---|---|
| Erratum 24 | 0/0/0/0 | 0/0/0/0 |
| E5 | 6/0/1/0 = 7 | 6/0/1/0 |
| E2 | 4/0/1/0 = 5 | 4/0/1/0 |
| E4 | 5/0/1/0 = 6 | 5/0/1/0 with E4-3 restated (Fix 3); as filed E4-3 not accepted as written |
| E1 | 2/1/1/0 = 4 | 2/1/1/0 |
| S2-8 | 1/1/1/0 = 3 | 1/1/1/0 |
| Z2 corner | 1/1/1/0 = 3 | 1/1/1/0 |
| **resume total** | **19/3/6/0 = 28** | **19/3/6/0 = 28** (18 + E4-3 restated) |
Refutations: none. **No previously ruled grade changes**: 2216 stays 8/2/3/0 with S2-7 COND and S2-11 OPEN as filed; E3 3/0/0/0; S5 3/0/1/0; Erratum 23 0/0/0/0 distinct.

## 7. Branch register after this audit (t4436; nothing adopted; junction UNSOLVED)
- **Dropped (PP-audited PROVED implications):**
  - **E5 ∩ H_Σ ∩ SO(3)_R**, with or without U(1)_R, which includes scope S (E5-4);
  - **E2 ∩ (SO(3)_R × U(1)_R)** (E2-4).
  Both are dropped under the premise lists in §3 and §4. Earlier drops are unchanged: E3; S5 (BPS only).
- **Kept / OPEN:**
  - E5 ∩ ¬H_Σ = E2 ∩ E5 (E5-6/E2-5);
  - E2 ∩ E1; E1 as a whole (E1-4), including E1 ∩ H_Σ, where E1-1 gives a constraint but no contradiction, and [w] with KK spinors;
  - E4: singular on all of C₄ (H_Σ ∩ SO(3)_R), or on any nonempty part of C₄ (E2) (E4-6);
  - premise failures not covered by either drop: (F-4) failing on E2, x-dependent (non-Poincaré) supercharges, a face not meeting C₄;
  - S2-8 / P8-3; Z2 corner S2-13 (Z-3); non-BPS Z2 walls; non-BPS S5 (S3b-4).
- **CONDITIONAL:** E1-3 (BPS Z2 excluded inside the truncation, on a citation); P8-2; Z-2 (float).
- [χS], [χU] and [w]/Z2 are all kept. Their regular-on-C₄ parts in the dropped sub-branches are covered, and δ-support on C₄ goes to E4. S6 is a record premise, not a math escape.

## 8. Fixes for NL (next additive file; do not edit any existing file)
1. **(priority)** List **(h0) = Erratum 24 (h2): x-independent Poincaré supercharges** among the premises of E5-3(b), E5-4, E2-4 and E1-1, and let P8-1 inherit it. State why: Γ^{0123} anticommutes with Γ_μX (PP P4), so the χ₄ split holds only on ∂_με = 0.
2. **(priority)** E2 §0 (ii) **and E1 §0** call the HW projection "record premise S6". Restate (ii) as the D1 HW hypothesis Γ^nε = ε (ε(−r) = Γ_nε(r), continuous at the wall). S6 is the odd-HW record (f825dfff), as the E5 file already says.
3. **(priority)** E4-3: replace the "dimension 2 / finite / smearing" derivation by "an H_Σ × SO(3)_R-invariant source support meets C₄ ∩ face iff it contains C₄ ∩ face (E4-1)". Record that the α-sheet classification is not exhaustive (the SO(3)_R-fixed U(1)_R circles at μ₃ = μ₄ = μ₅ = 0, disjoint from C₄). In E4-5, replace "natural sources … are the α sheets" accordingly.
4. Scope the diagonal-K statements: the E2-2 "forced by equal D1 K" column, E5-5's "unique diagonal K" and E1-2. On E2, K|_T is a general symmetric 2×2. On E5 without U(1)_R, the K-invariant forms on the weight-1 plane are 4-dimensional (P11). The "ω₂ free / no obstruction" conclusions survive; the forcing column does not transfer.
5. E2-3: say "locked lines have **degree 0**". Make explicit that both locked lines have degree 0 (conjugation antisymmetry, PP P10, or both U(1)_R charges in the vacuum). Then unlocked = ±(2g−2) follows. Note that (gr) is not needed for T-plane ≅ TΣ_n̂.
6. (optional) E5-4: record PP's streamlined proof (SU(2) weight symmetry on V₊; no doublet decomposition needed) and that n = ±e_r follows from C₄ ⊂ face. Add "C₄ ∩ face ≠ ∅" to (reg).
7. E4-2 wording: the fixed set of K_{p̃} is the S² over p̃. C₄ is the union over Σ, and its smoothness follows from homogeneity.
8. Z2 file: the v1 continuation stop time "about 10:0x CST" is inconsistent with the record. The v1 script mtime is 10:10:16 and its log mtime is 10:12:52 CST (sidecar 10:13:07). Record ≈10:12–10:13 CST in the next erratum, without editing.
9. Relabel v2 casts complex values to real (ComplexWarning lines in the log) without printing max|imag|. Print it as continuation v2 does (cf. PP f530cbc0 Fix 5). Float only; no grade effect.
10. E2 header: list the full script and log shas instead of "hashes in the sidecars".
11. (hygiene) Dead code in chirality_hw_lock_exact (unused `proj`, empty loop at lines 130–134). Harmless; leave it frozen and note it.

## 9. Not done / limits
- The continuation-v2 Z2 run (~12 min of float BVPs) was not re-run. Its figures were checked line by line against the sealed v2 log. Z-2 stays CONDITIONAL in any case.
- E1-3's 7D citation and P8-2's LLM reading were not re-derived. They stay CONDITIONAL.

Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
