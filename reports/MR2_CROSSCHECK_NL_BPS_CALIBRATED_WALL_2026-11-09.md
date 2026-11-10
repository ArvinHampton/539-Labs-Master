# MR2 cross-check of NL's BPS / calibrated-wall files on MN2 (OW d5eaeef3)

Date: 2026-11-09, America/Chicago. Author: MR2 (resonant algebra project, Quantum Comp). This file is additive. No existing file was edited, and the tip 7cddb188 was not touched. Nothing was sent, and there was no CERT or Gemini.

Grades are PROVED / COND / OPEN / REF, under PP's convention: an implication with a stated premise is PROVED, floats or an unverified citation are COND, and a claim is REF only by proof or counterexample.

## Inputs (sha checked against sidecars: all MATCH)
- NL 2007: 704df3ee…
- NL 2012: 89ec258a…
- NL 2017: f8801bff…
- NL ERRATUM18: 92dded27…
- PP audit of 2007: `FINDINGS_PP_AUDIT_NL_BPS_CALIBRATED_WALL_704df3ee_2026-11-09_2020.md` (5f2de6f9…). There is no PP audit of 2012, 2017 or ERRATUM18 yet.

CGR inputs are (3.8), (5.15) and (5.16). MR2 transcribed them from the local text /workspace/pp-audit-kk/cgr.txt. Nothing external was used. I read NL's scripts but did not use them; all code below is MR2's own.

## Artifacts
| file | sha256 |
|---|---|
| `MR2_CROSSCHECK_NL_BPS_CALIBRATED_WALL_2026-11-09.py` | 11fdb72dc4ffef1f8baf8f50333edbc0b6ffe8397056f0cd2dbdc5413903bccb |
| `MR2_CROSSCHECK_NL_BPS_CALIBRATED_WALL_2026-11-09.log` | 4f12420cd5587eac27a67ef87def81efa1e836e14ce84690f27372d3d38b609c |
| `…_M6_IDENTITY_FIX.py` | f06d250dce00b758fe5900157e2ac97be4e47717b537660da058167a40d0f72d |
| `…_M6_IDENTITY_FIX.log` | 369ac38df40bcb38227774232529185eec32582feaf9cbf5bc29d0d6906ec3e7 |

- Each .py was frozen before its log.
- Main run: exact sympy except one fibre-determinant float check. Exit 0 in 13 s.
- In the main run, the [M6] matrix identity printed `None`, because sympy's `is_zero_matrix` was undecided on unexpanded entries.
- The FIX script re-checks that identity entrywise. It gives max entry 0 in 4 random trials.
- The FIX script then crashed on a print-call typo (`EXIT 1`) before its optional B3 eigenvector line. No claim depends on that line: the main log already gives the B3 eigenvectors as 3g/(4g ∓ 5|g|), which is −3 and 1/3 for g > 0.

**Normalisation convention used throughout.**
- L = R − ½G_ij∂Xⁱ∂Xʲ − V, in 5D Einstein frame, mostly plus.
- BPS flow: A′ = −W/3 and Xⁱ′ = 2G^{ij}∂_jW, which gives **V = 2G^{ij}∂_iW∂_jW − (4/3)W²**.
- In the level-0 (φ, λ) sector, G = 60·δ (CGR (3.7): −30(dφ)² − 30(dλ)²), so V = (1/30)|∂W|² − (4/3)W². This is NL B1.
- In CGR (5.16) variables, G = diag(6/Σ², 2/Ω², 4). This is NL C2.
- So the two NL statements are the same formula in this one convention. That resolves PP's normalisation remark (PP 2020 §B1).

## 1. B1 against CGR, tied to MR2 data
**N1 (PROVED, exact; the transcribed V(3.8) is the stated input).** Take V = g²[½l²e^{12λ−16φ} − 2l e^{−10φ} − ½e^{−4φ}(3e^{8λ} + 12e^{−2λ})] and NL's W = (g/2)[e^{−2φ}(2e^{−6λ} + 3e^{4λ}) + l e^{−8φ+6λ}].
- V − (2G^{ij}W_iW_j − (4/3)W²) = 0 identically, with l symbolic.
- My own 1D Euler–Lagrange equations for e^{4A}(12A′² − 30φ′² − 30λ′² − V) and the Hamiltonian constraint all vanish identically on the flow.

**N2 (PROVED, exact).** At MN2 (l = −1, e^{30φ} = e^{10λ} = 2), the CGR data reproduce MR2's own MN2 data.
- ∇W = ∇V = 0, W* = 3·2^{1/3}g/2 and g²L² = 2^{4/3}.
- **V* = −12/L² exactly.**
- The T entries are e^{−6λ} = 2^{−3/5} = MR2 X1 and e^{4λ} = 2^{2/5} = MR2 X2 = X0.
- **m²L² = eig(G⁻¹Hess V)·L² = {−4, +12}.** This equals MR2/NL K1 and ecee2668 §7.

**N3 (PROVED).** The linearised W-flow has exponents ∓2/L, with eigenvectors (δφ : δλ) = (−3 : 1) and (1/3 : 1). This is NL B3.

**N4 (PROVED, exact; checks the citation's math, not only its text).**
- The CGR (5.16) potential at z = 0, pulled back by (5.15) at w = 0, equals V(3.8). This uses two independent CGR formulas.
- (5.16)'s kinetic metric pulls back to 60dφ² + 60dλ² + 3dw².
- NL C2's W₃ = −2√3gP = g/(2ΩΣ)(Ω²e^{2ϕ} + 2ΩΣ³ + l e^{2ϕ} + 2) satisfies V₅.₁₆ = 2G^{ij}∂W₃∂W₃ − (4/3)W₃² on the full (Σ, Ω, ϕ) space.
- W₃ restricts to B1's W at w = 0, and ∂_wW₃ = 0 there, so the w = 0 slice is flow-invariant.
- Not re-derived here: W₃ = −2√3gP from the (D.19) moment maps. PP P2 did that.

**N6 (PROVED).** The (D) point is not in the CGR level-0 sector.
- ∂_λV at λ = 0 is 6g²l²e^{−16φ}, which is nonzero for l ≠ 0.
- (D) has no twist (a = 0), while CGR has the twist with l = −1.
- The (D) check V₀ = −12/L₅² was done in the 5D singlet frame (MR2 b44cd004, M5). Here the analogous check is N2 at MN2.

**N5 (COND).** "W is the gravitino-shift superpotential" depends on the general N = 2, D = 5 fermion-shift formulas, which are cited, not re-derived. This concurs with NL C3, PP B2 and PP's F3 (at least 4 supercharges guaranteed, 8 only if the second N = 4 eigenvalue matches).

## 2. D2: trace identity K_int = −6k_x
**N10 (PROVED, given NL D1's stated hypotheses (i)–(iv) and its jump formula).**
- x-rows: G has no x-legs, so Γ^{cde}G_{xcde} = 0, which gives G̸ε = −144σk_xε.
- Internal rows contracted with Γ^a over the 6 internal directions use the identity Σ_a Γ^a(Γ_aG̸ − 12Γ^{cde}G_acde) = (6 − 12)G̸ = −6G̸. This holds because Γ^aΓ^{cde}G_acde = Γ^{acde}G_acde. I checked it exactly on my own 32×32 Clifford algebra with random internal G (FIX log: max entry 0, 4 trials).
- So K_int·ε = (6σ/144)G̸ε = −6k_xε, K = −2k_x, ρ = 6k_x/κ², and the mean internal pressure is −ρ/3.

**N11 (PROVED, exact sympy rank).** NL D1's jump formula on the C6 face (k_Σ = k_x, k_T = −2k_x, G₆₇₈₉ = −6qσk_x) gives an **8-dimensional** solution space for all 8 sign choices (q, σ, Γ_n).
- Controls: k_T = −1.5 gives 0. The MN2-type face (k_x = −1, internal K = 0) gives 0 with G = 0 and 0 with 6 random integer internal G.
- I did not independently re-derive D1's jump formula. Its consequences reproduce exactly.

## 3. D4 and ERRATUM18
**N12a (PROVED).** ERRATUM18's constant is correct and **sharp**.
- On the exact MN2 face, k_x = −ε/L and K_int = 0 (the internal metric is r-independent), so K_int + 6k_x = −6ε/L.
- Under |δK|_op ≤ δ, the trace moves by at most 6δ + 6δ = 12δ. So D2 fails for δ < ½·min ε/L.
- At δ = ½ε/L the trace condition is met: k_x = −ε/2L and every internal k = +ε/2L give 0. So the threshold cannot be improved, as far as the trace is concerned.

**N12b (REF; already withdrawn by NL E18-1).** NL's original D4 bound "≤ 10δ, D2 fails for δ < (3/5)ε/L" is false. The witness above meets the trace condition at δ = ½ε/L < (3/5)ε/L.

**Wording.** D4's "within ½ε/L of MN2" is a neighbourhood in the face's **extrinsic-curvature** data, in operator norm. It is not a neighbourhood in field-space distance. The NEC clause (k_v − k_x ≥ ε/L − 2δ) also needs the operator norm.

## 4. The no-wall claim
**N7 (PROVED, exact).**
- W_φ + 2W = −3gl·e^{6λ−8φ} identically, so 4(W_φ + 2W) = +12g·e^{6λ−8φ} > 0 at l = −1. This is NL B6 and PP P-identity.
- D3: from the uplift face formulas, (K_int + 6k_x)/ε = 6A′ − 6φ′ + ½λ′∂_λ ln Δ. This is NL D3.
  - This uses ln det g_int = 12φ − ln Δ + const.
  - That in turn uses the fibre-determinant lemma det(T⁻¹dμdμ)|_{S⁴}/round = (det T⁻¹)(μᵀTμ) = Δ (det T = 1, matrix-determinant lemma). A float check at 2 points agrees to 20 digits; this is N9.
- Since ∂_λ ln Δ varies on S⁴, the identity requires λ′ = 0 and A′ = φ′. On W-flows that means W_λ = 0 and W_φ + 10W = 0.
  - In X = e^{−6φ+12λ} and v = e^{10λ}, these read −6X + 12v − 12 = 0 and −2X + 24v + 16 = 0.
  - The unique solution is **X = −4, v = −1**, so there is no solution with X, v > 0. This confirms NL D3.

**N9 (PROVED by lemma; float-confirmed).** This is the fibre-determinant identity used above.

**N8 (PROVED as an implication; new).** The B6 obstruction survives the SO(3)-breaking scalar w, which PP F10 listed as "not covered".
- W₃_φ + 2W₃ at fixed (λ, w) equals −3gl·e^{6λ−8φ} exactly, with no w-dependence.
- Premises:
  - (a) the kept side is a (φ, λ, w) W₃-flow;
  - (b) the B5 constituent menu with a_eff ≤ −2, which holds because w enters only the fibre block and not the x- or Σ-warps;
  - (c) the φ-junction condition 60[φ′] = T_φ, which holds because the pulled-back kinetic metric diag(60, 60, 3) is diagonal.
- Under these premises, no ℤ₂ wall exists on Bolza in the extended sector either.
- Not shown: that every IR-regular 3-scalar flow is a W₃-flow (a P1 analogue). That is part of N16.

**Counterexample search: none found.**
- Level-0: the exact identities of N7 leave no room.
- D3 has no positive solution.
- The MN2-type face with random G has a 0-dimensional solution space, as D2 predicts.
- The w-direction gives the same obstruction (N8).

**N16 (OPEN).** Two things stay open:
- finite-amplitude χ-dependent walls (D6/B12);
- whether all IR-regular flows in the w-extended sector are W₃-flows.

## 5. Consistency with MR2 wall and batch-1 results
**N13 (PROVED, exact; same face formulas).** On the exact MN2 face with the IR side kept:
- ρ = 6ε/(Lκ²) and the internal pressure is −8ε/(Lκ²). This is MR2's required stress 6:8:8.
- The null energy along every internal direction is −2ε/(Lκ²). This is MR2's NEC deficit −2k/κ², with k = ε/L.
- Deficit/ρ = 1/3, which is exactly **L3**, consistent with NL B10 and PP's identity.
- D2 would need K_int = 6ε/L, but the face has 0. So **MR2's thin wall is non-BPS**, consistent with D4. This was always the case and was never claimed otherwise.
- **B5 (2N = 9760):** this is consistent with NL C6 (odd G₄, flux N → −N, jump 2N).

**N15 (COND, on D6/B12 OPEN). The recommendation does not change.**
- **Item 1:** keep (1a), the HW E₈ wall, as the face.
  - NL's result removes the BPS loophole (K7) in the decided classes, so the K6′ deficit stands.
  - Closure still needs changed face data (T7/B12), which is OPEN.
- **Item 2:** keep (2a), the thin wall.
  - The no-BPS result says nothing against a non-BPS thin wall. The thin wall's validity is the EFT statement (b44cd004 M9/M10), which does not depend on supersymmetry.
  - The thin wall's NEC requirement (L3) is unchanged.

## Per-NL-claim verdicts (MR2)
No NL claim is proved false by MR2, except the original D4 constant, which NL itself withdrew.

| item | NL / PP | MR2 |
|---|---|---|
| B1 | PROVED / PROVED | **PROVED**, independently (N1, N2) |
| B2 | COND / COND | COND, concur (N5) |
| B3 | PROVED / PROVED | **PROVED**, independently (N3) |
| B4a / B4b | PROVED / PROVED, REF ("4" → 3) | concur with PP; I did not rerun the rank count |
| B5 | PROVED / PROVED (scoped to the menu; "any" is OPEN) | concur; it is used as a premise in N8 |
| B6 | PROVED / PROVED | **PROVED**, independently (N7); extended to w (N8) |
| B7 | PROVED / PROVED | concur; consistent with N13 at the exact face |
| B8 | COND / COND | concur |
| B9 | PROVED / PROVED | concur (not rerun) |
| B10 | COND / COND | concur; the 1/3 matches L3 exactly (N13) |
| B11 | PROVED / PROVED | concur (not rerun) |
| B12 | OPEN / OPEN | OPEN (N16) |
| B13 | COND / COND | concur |
| C1 | PROVED / — | **PROVED**, independently ((5.16) = (3.8) at w = 0; kinetic 60, 60; N4) |
| C2 | PROVED / — | **PROVED** for the superpotential identity on the full 3D space (N4). The P-from-(D.19) step was not rechecked; PP P2 covers it. |
| C3, C4, C6 | COND / — | concur, COND |
| C5 | PROVED / — | concur (not rerun) |
| C7 | PROVED / — | concur (logic) |
| D1 | PROVED / — | consequences reproduced exactly (N11); the jump formula was not re-derived. Concur. |
| D2 | PROVED / — | **PROVED**, independently (N10) |
| D3 | PROVED / — | **PROVED**, independently (N7, N9) |
| D4 | PROVED / — | **PROVED** with the ERRATUM18 constant (N12a, sharp). The original 10δ/(3/5) constant is **REF** (N12b), and D4's δ is an extrinsic-curvature neighbourhood. |
| D5 | COND / — | concur |
| D6 | OPEN / — | OPEN |
| D7 | COND / — | concur |
| E18-1 | PROVED / — | **PROVED** (N12a) |

## Tally (MR2's own claims N1–N16, with N12 split into N12a and N12b)
- **PROVED 12:** N1, N2, N3, N4, N6, N7, N8, N9, N10, N11, N12a, N13.
- **COND 2:** N5, N15.
- **OPEN 1:** N16.
- **REF 1:** N12b.

Total: **12 / 2 / 1 / 1 = 16**.
