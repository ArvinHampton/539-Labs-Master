# FINDINGS: PP audit of (c) NL junction setup (MN2, MN1, BBBW, N=4880, g=2) and (a) the Fricke sign of Ξ = 49a1 ⊗ χ₁₄₀. 2026-11-09 17:02 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. Tip 7cddb188 untouched (re-hashed: MATCH). No CERT. Nothing sent outside. No Gemini. LOCK 96f8d42e §4 not used. No MR2 numbers used. Convention: G = ½T^(EH) (t4315, OW 2d1e877e), i.e. standard 11D sugra.
Authority (each sha256 re-hashed and equal to its sidecar):
- OW 4810280562b2fb0cf94de47b9a92c840643a7dac077e500d26bfa644880f7d24 (t4339): GO for NL's junction setup for the three candidates; b free; no vacuum adopted.
- OW f283cffd365ca7368a9f7b5dfdca7ee177ed54db25a28c1944999a5af755e5b6 (t4337), Owner definitions:
  - brane := a stack of wrapped M5-branes
  - face := the 10D matching hypersurface
  - Ξ := 49a1 twisted by 140
- Everything else stays neutral per 5f59e33e, and the vacuum choice stays on HOLD (t4333 / aaadb280).
Scratch:
- /workspace/audit-scratch/pp_junction_1656/ (re-run copies of NL's scripts)
- /workspace/audit-scratch/pp_xi_1700/xi_fricke.py c4555d16… and .log 39fe2932… (PARI 2.x via cypari2, installed from PyPI)

## Rollup
PROVED 12 · CONDITIONAL 6 · OPEN 4 · PENDING 0 · REFUTED 1 (confirmed NL P3a). **NL fixes requested: 6.**
- **(c) verdict:** NL's set-up is correct. The "no solution" result is valid only in a narrow scope: constant-radius faces, thin shell, a source that is smeared M5 tension and nothing else, and the three pairings P1–P3. It is **not** a general no-go for the junction. Inside that scope it is PROVED for P1, P2 and the end faces, and CONDITIONAL (numerical) for interior faces. N_b = 4880 is reached on no face (CONDITIONAL, numerical). Whether the face is BPS hinges on the Z₂ parity of G₄, which is **OPEN** (no Owner record on disk).
- **(a) verdict:** Ξ = 49a1 ⊗ χ₁₄₀ has conductor **19600 = 2⁴·5²·7²**, root number −1, and Fricke eigenvalue **w₁₉₆₀₀ = +1**. **PROVED** by exact PARI computation, which reproduces the result of PP 1525 (389c2f7c). Side fact (PROVED): Ξ's newform equals the newform of the −20 twist.

---
## (c) NL junction file
### 0. Integrity
- **I1 (PROVED).** NL_DERIVED_JUNCTION_SETUP_…_1655.md sha256 3cd6c8d303b3e07a8bd7d5de3adb9ff6b53f95d217b7d4a160431bdecf07c050 equals its sidecar.
  - All 7 script and log sidecars in /workspace/nl-junction-1646/ match: face.py fd309c48, flowlin.py b72d2296, scan.py cf7b3354, shoot.py 1f342987, verify_sym.py 55bf13d6, face.log 036955e7, scan.log 16920e3c.
- **I2 (PROVED, with one discrepancy).** Re-runs of copies all exit 0.
  - face.log is **byte-identical**.
  - verify_sym prints "ALL ZERO: True".
  - scan's numbers are identical, but my re-run prints two extra header lines ("UV analytic: N_req(x)→10N/3 = 16266.67") that scan.log lacks. The import of face.py prints them, so NL's scan.log was not produced by the current face.py/scan.py pair, or it was trimmed. Fix F1.

### 1. J2/J3: induced metric and extrinsic curvature
- **J2 (PROVED given J1).** h is the restriction of the CLP-uplifted flow metric to r = r_b. Static and 4D-Poincaré invariant, since everything depends on r only and A_r = 0.
- **J3 (PROVED).** Re-run of the symbolic check: K_ab = ½n^r∂_r h_ab, with frame eigenvalues as listed; residual 0 in all four blocks.
- **J3a (PROVED, PP independent derivation).**
  - Exact AdS₅×Σ fixed point: λ and Δ̃ are constant, f = f₀ − ln r, g = g₀. With n^r = Δ̃^{−1/6}e^{−f}: k_x = Δ̃^{−1/6}e^{−f}·(−1/r) = −Δ̃^{−1/6}/L₅ (L₅ = e^{f₀} in L₇ = 1 units), and k_Σ = k_fib = 0. So **K = 4k_x** ✓.
  - Exact AdS₇×S⁴: λ = 0, Δ̃ = 1, f = g = −ln(r−r*). Then k_x = k_Σ = −1/L₇ and k_fib = 0, so **K = 6k_x** ✓.
- **Scope note.** These are faces of the *exact* end geometries. Faces of the flow only approach them asymptotically.

### 2. Israel with M5-stack tension only
Source: S_ab = −N_bT_M5ρ P^{wv}_ab (zero fibre components). κ₁₁²T_M5 = 128π⁸/(32π⁵) = 4π³ ℓ_P³ (PROVED).
- **P1 (PROVED).** Gluing the same flow on both sides gives a C¹ metric, so [K] = 0 and S = 0. N_b ≠ 0 is impossible.
- **P2 (PROVED given J1; rigorous).** (A.15) is a first-order autonomous ODE for y = (f, g, λ₁, λ₂) with a smooth (locally Lipschitz) right-hand side, so Picard–Lindelöf uniqueness applies.
  1. Continuity of h at the face fixes λ₁ and λ₂ (through Δ̃(μ) for all μ), then g, then f up to the x-rescaling.
  2. The fixed-point family f = f₀ − ln(r − r₀) can match any f(r_b) by choosing r₀ < r_b. So there is a fixed-point solution with the same data at r_b.
  3. By uniqueness the interior flow *is* that solution, which contradicts the AdS₇ UV.
  - Note: this uses only continuity of h, not the Israel condition. It assumes the exterior is the BPS fixed point of the same truncation. Non-BPS exteriors are NL P2′ (OPEN).
- **P3 lemma (PP, PROVED).** Z₂ with a pure M5 source needs (a) k_Σ = k_x and (b) k_fib = K for all four fibre eigenvalues. Then K = 4k_x + 2k_Σ + Σk_fib = 6k_x + 4K, so **K = −2k_x and every fibre eigenvalue must equal −2k_x pointwise on S⁴.** This is a sharper test than NL's averaged residual.
- **P3a (REFUTED by proof; NL label correct).**
  - Exact AdS₅×Σ face: k_fib = 0 ≠ −2k_x, and k_Σ = 0 ≠ k_x.
  - Exact AdS₇ throat face: k_fib = 0 ≠ −2k_x.
  - k_x ≠ 0 in both, so neither carries a pure smeared-M5 Israel solution. Scope: the exact end geometries, not flow faces.
- **P3b (CONDITIONAL, numerical; re-run confirmed).** Over 399 interior faces per candidate, the minimum averaged fibre residual is 4.000 for z = 1, 0, 2, 3 and never 0. So there are no solutions on the sampled faces. This is not a proof for every r_b; a proof would follow from showing that some fibre eigenvalue differs from −2k_x on each face (fix F3).
- **P3c (CONDITIONAL, numerical; arithmetic spot-checks PROVED).**
  - The 4D-only fit N_b(r_b) runs from 12568.6 / 12252.1 / 12812.2 / 12942.4 at the AdS₅ end up to 10N/3 = 16266.67 at the throat. That is N_b/N ∈ [2.51, 3.33], so **4880 (N_b/N = 1) is never reached**.
  - IR-end ratio Σ/x = |k_Σ − K|/|k_x − K| = 4|k_x|/3|k_x| = 4/3 (PROVED). So the 4D-only fit is internally inconsistent, as NL says.
- **P3d (PROVED).** UV: |k_x − K| = 5/L₇ and Vol(S⁴_{L₇/2}) = π²L₇⁴/6. So N_b = (2/4π³)(5/L₇)(π²L₇⁴/6) = 5L₇³/(12π), and with L₇³ = 8πN this is **10N/3** ✓.
- **P3e (CONDITIONAL; parity OPEN).**
  - Charge per brane: 2κ²T_M5 = 8π³ = (2π)³ = the flux quantum (PROVED). So N_b = 2N if G₄|_{S⁴} is Z₂-odd, and 0 if even.
  - Tension/charge (odd case): 12568.6/9760 = 1.288 (MN2), 1.255 (MN1), 1.313 (z = 2), 1.326 (z = 3); 5/3 at the UV end. Either way charge ≠ tension, so the face is not BPS.
  - **Parity OPEN:** no Owner record on disk settles the O1 Z₂ parity of C₃/G₄ (grep of OWNER_WRITE*, 16:58).
- **Scope of "no solution" (precise).** It is PROVED or numerically supported only for:
  - (i) constant-r faces of the BPS flows (J1, CONDITIONAL on CLP/BBBW);
  - (ii) a thin-shell source equal to smeared M5 tension, with no fibre pressure, anisotropic Σ stress, worldvolume flux or G₄ legs on Σ;
  - (iii) the pairings P1 (same flow), P2 (throat + BPS fixed-point exterior) and P3 (Z₂ keeping the IR side).
  - Outside that scope it is **OPEN**: non-constant faces, non-BPS exteriors (P2′), localized M5s (J5, codimension 5), extra face sources (J7), and b (J6).
  - **It does not show that the Owner's brane/face junction has no solution.** It shows that pure smeared M5 tension on a constant-radius face cannot close it.

---
## (a) Fricke sign of Ξ = 49a1 ⊗ χ₁₄₀
- **Do the cited files prove it?** Yes, for this exact twist.
  - PP 1525 (389c2f7c, L100) computed elltwist(49a1, 140): conductor 19600, ellrootno −1 ⇒ w = +1, labeled PROVED by computation.
  - Local's RELABEL file ce4d9e80 (L33–36) repeats it citing PP. Its wording "ε = −w = +1" swaps the symbols; the value is right (w_N = −ε = +1).
- **X1 (PROVED, exact; xi_fricke.log).** Recomputed independently:
  - 49a1 = [1,−1,0,−2,−1] has conductor 49, j = −3375 and root number +1.
  - coredisc(140) = 140, so χ₁₄₀ = (140/·) is the character of ℚ(√35).
  - E₁₄₀ = elltwist(49a1, 140) = [0,−105,0,−39200,−2744000]. ellglobalred (Tate's algorithm) gives conductor **19600 = 2⁴·5²·7²**, and ellrootno = **−1**.
  - Twist check: a_p(E₁₄₀) = (140/p)a_p(49a1) for all p < 2000 with p ∤ 980.
- **X2 (PROVED, given the standard weight-2 Atkin–Lehner identity ε = (−1)^{k/2}w_N, the project convention).** The Fricke eigenvalue of the level-19600 newform of Ξ is w = −ε = **+1**.
- **X3 (PROVED; Sturm bound).** E₋₂₀ = elltwist(49a1, −20) = [0,15,0,−800,8000] also has conductor 19600 and root number −1. a_p(E₁₄₀) = a_p(E₋₂₀) for **every prime p ≤ 6721**, the Sturm bound for weight 2 on Γ₀(19600), including a_p = 0 at 2, 5, 7. So **Ξ and the −20 twist have the same newform**: the same L-function and the same Fricke eigenvalue.
  - The two curves are **not isomorphic** over ℚ (ellisisom = 0); they lie in the same isogeny class (size 4).
  - Reason: 49a1 has CM by ℚ(√−7), so a_p = 0 whenever χ₋₇(p) = −1, and χ₁₄₀ = χ₋₂₀χ₋₇.
  - **Flag for the Owner:** t4337 says "the twist by −20 is not Ξ". That is true for the curves, not for the modular form. Any Ξ statement made through the newform or L-function applies equally to the −20 twist.
- The Λ₀ = √(7/8)L(1,χ₁₄₀) link stays a structural link, OPEN as a derivation (per OW f283cffd).

---
## NL fixes requested
- F1. Regenerate scan.log from the current face.py/scan.py, which print a 2-line header, or explain the difference.
- F2. Restate the headline: "no solution **for constant-radius faces with smeared M5 tension as the only source, in pairings P1–P3**". Do not present it as a no-go for the junction.
- F3. P3b: test the pointwise criterion K = −2k_x and k_fib = −2k_x (PP lemma). Showing one fibre eigenvalue ≠ −2k_x on every face would upgrade P3b to PROVED.
- F4. P2: label "PROVED given J1 (BPS system, CONDITIONAL)", and state that the exterior is assumed to be the BPS fixed point of the same truncation.
- F5. P3a: say explicitly that the refuted faces are the exact AdS₅×Σ and AdS₇×S⁴ geometries, not faces of the flow.
- F6. P3e: keep the BPS/charge conclusions explicitly CONDITIONAL on the OPEN Z₂ parity of G₄ (no Owner record).

## Tally detail
- PROVED 12: I1, I2, J2 (given J1), J3, J3a, P1, P2 (given J1), P3 lemma, P3d, X1, X2, X3.
- CONDITIONAL 6: J1 (CLP/BBBW), P3b, P3c, P3e, the 4/3 inconsistency inheritance (via J1), and the 11D lift of N_b values (smearing/Z₂ factor).
- OPEN 4: Z₂ parity of G₄; P2′/J5/J7 sources and faces beyond the scope; b (J6); Λ₀–Ξ derivation.
- REFUTED 1: P3a (pure-M5 Israel on the exact end faces), confirmed.

Tip 7cddb188 untouched. No CERT. Nothing sent outside. No Gemini.
