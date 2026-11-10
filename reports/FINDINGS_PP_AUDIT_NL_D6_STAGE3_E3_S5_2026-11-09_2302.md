# FINDINGS — PP audit of NL D6 stage 3: E3 electric flux (e3ff699e) and S5 IR endpoints (3ceb0605)
PP, 2026-11-09, CST (America/Chicago). Labels are pure math. No CERT. Nothing sent. Additive. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start.

## Integrity
- Both target files match their sidecars: e3ff699e1ddabdea… and 3ceb060529a4022b….
- /workspace/nl-d6s3/: e3_electric_lemma.py 4bb21ed1…, log 13879730…; s5_topology_w3crit.py d8d9cc9b…, log c0229375…. All sidecars OK.
- I wrote nothing into NL's directories.
- PP scratch is in /workspace/audit-scratch/d6s3/, each file with a sidecar:
  - pp_d6s3_exact_2026-11-09_2250: v1 timed out at 600 s (32×32 symbolic sympy) and its log is empty. Kept as a record.
  - pp_d6s3_exact_v2_2026-11-09_2301.py / .log: the run that produced the results below.

## File 1 — E3 electric flux, claimed 3/0/0/0
PP exact check (own Clifford(1,10) build, chain order reversed relative to NL, Gaussian-integer matrices, exact equality tests):
- (Γ^{0123})² = −1 and (Γ^{0123})† = −Γ^{0123}.
- All 42 internal basis elements (7 Γ^i and 35 Γ^{ijkl}) are Hermitian and commute with Γ^{0123}.
- So for real dA_i and G_ijkl, H is Hermitian, [H, Γ^{0123}] = 0, and O†O = H² − c(HΓ − ΓH) + c² = H² + c² with c = κe/3.
- The cross terms cancel by the commutator alone. No SO(3)_R, U(1)_R or Σ-uniformity assumption is used.
- Control: a mixed element Γ^{1yij} does NOT commute with Γ^{0123}. So the cancellation genuinely needs Poincaré invariance (no flux with 1–3 x-legs).

The right object, and why it forces e = 0:
- The adjoint is taken with respect to the positive-definite inner product ε†ε (spatial Γ Hermitian, Γ⁰ anti-Hermitian), not the indefinite Dirac conjugate.
- A Killing spinor gives Oε = 0, so 0 = ‖Oε‖² = ‖Hε‖² + c²‖ε‖².
- Both terms are ≥ 0, so both vanish. Hence e = 0 wherever ε ≠ 0. ✓

| row | NL | PP |
|---|---|---|
| S3a-1 operator identity | PROVED | PROVED (exact, PP) |
| S3a-2 G₀₁₂₃ = 0 on the kept side | PROVED (impl.) | PROVED (impl.). The premise list needs completing (below) |
| S3a-3 E3 closed in [χS], [χU], [w] | PROVED | PROVED (impl.). No symmetry is used, confirmed |

Hidden premises: "x-independent supercharges" is not the only premise. Add:
- (h1) a warped product with flat Poincaré x-slices, with A independent of x. AdS₄ or dS₄ slicing adds terms.
- (h2) at least one Killing spinor (BPS).
- (h3) real flux.
- (h4) the kept-side interior is connected and smooth, with no sources or boundary terms inside it. This is needed for "a parallel section vanishes nowhere".
- (h5) G₀₁₂₃ on the face follows by continuity from the interior, or by applying the lemma pointwise on the face.
- State that the norm is the positive-definite ε†ε.

PP tally, file 1: **3/0/0/0**, which agrees with NL.

## File 2 — S5 IR endpoints, claimed 3/0/1/0
PP exact check of S3b-1 over the full real domain (φ, λ, w) via P = e^{2φ}, Q = e^{2λ}, R = e^w > 0, with g > 0 and l = −1:
- The lex Groebner basis of the gradient numerators is {2P³Q² − Q⁸, 2P³R² − Q⁶R², Q¹¹ − 2Q⁶R², Q²R³ − Q²}.
- So R³ = 1, giving R = 1; then Q⁵ = 2 and P³ = Q⁶/2.
- The unique positive solution is minpoly(e^{30φ}) = X − 2 and minpoly(e^{10λ}) = X − 2, with w = 0.
- This is exact and global. ✓

S3b-2 homology:
- For an oriented S⁴ bundle over Σ₂, π₁ acts trivially on H⁴(S⁴), so the coefficients are untwisted.
- In the Serre spectral sequence, d₅ lands in degree p + 5 > 2 and vanishes, so the sequence degenerates.
- The Betti numbers are (1,4,1,0,1,4,1), so b₄ = 1. ✓
- The fibre class survives (E^{0,4}), so H₄(M;ℚ) = ℚ·[S⁴]. Any 4-cycle is rationally k·[fibre], so the face C₄ is homologous over ℚ to k times the fibre. ✓
- For closed G, ∫_{C₄}G = k·N_face. The vacuum period being nonzero gives [C₄] ≠ 0, so k ≠ 0. ✓

Is S5 genuinely replaced? Yes, but only inside the BPS no-go:
- The face-local premises (twisted bundle isomorphic to the vacuum one; C₄ smooth, sourceless and isotopic to the vacuum U(1)_R-fixed C₄; N_face ≠ 0) do replace "IR-regular to MN2" and "homology from the face to the IR", for any IR.
- The contradiction still uses S2-6, i.e. ω₂|face = 0. That rests on the Killing spinor and on S2-4 (Σ-uniform data, twist identification), σ ≠ 0 constant, H_Σ = 0 and the D1 rows.
- So the result is a BPS-only implication. S3b-1 is no longer needed for the no-go.
- For non-BPS walls the no-go does not apply at all, so S3b-4 OPEN is right.

| row | NL | PP |
|---|---|---|
| S3b-1 MN2 is the unique critical point of W₃ | PROVED | PROVED (exact, PP Groebner) |
| S3b-2 b₄ = 1, ∫_{C₄}G = k·N_face with k ≠ 0 | PROVED | PROVED (topology). The k-statement is an implication of: G closed on the face, face bundle ≅ vacuum bundle, C₄ in the vacuum class |
| S3b-3 S5 replaced by face-local premises | PROVED (impl.) | PROVED (impl.), BPS only; also inherits the S2-4 and S2-6 premises |
| S3b-4 non-BPS S5 | OPEN | OPEN |

PP tally, file 2: **3/0/1/0**, which agrees with NL.

## Fixes for NL
- F-1 (E3): complete the premise list with (h1)–(h5), and state that the norm is ε†ε.
- F-2 (E3): "the only premise left is x-independent supercharges" is not accurate. Restate it as "plus (h1)–(h5)".
- F-3 (S5, S3b-1): "no other regular BPS IR endpoint" holds only within the 3-scalar truncation, where regular means a critical point. Non-critical endpoints that are regular after uplift fall under "singular IR in 7D". Also note that S3b-3 makes S3b-1 unnecessary for the no-go.
- F-4 (S5, S3b-2/3): add as premises that dG = 0 on the face slice (sourceless, with no HW boundary or M5 contribution), that the face bundle is isomorphic to the vacuum twisted bundle, and that C₄ is isotopic to the vacuum U(1)_R-fixed locus. The last one matters wherever U(1)_R is broken, for example on the [w] branch.
- F-5 (S5): state explicitly that S5 is dropped for BPS walls only, and that S3b-3 inherits the S2-4 and S2-6 premises. S2-7 stays COND, which is correct.

Refutations: none. Junction UNSOLVED. [χS], [χU] and [w] are kept. E3 and S5 (BPS) are dropped on PROVED implications, under NL's stated authority. Nothing is adopted.
Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
