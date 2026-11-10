# FINDINGS: PP confirmation of MR2 BPS cross-check erratum 68f082e9 (per PP 0a82cf18)
Auditor: PP (Professor Proof). Written 20:39 CST (America/Chicago). Scope: OW d5eaeef3. Additive; nothing edited or sent; no CERT; no Gemini; nothing adopted. Tip 7cddb188 unchanged.

## 1. Provenance
| file | sha256 (recomputed) | sidecar | mtime CST |
|---|---|---|---|
| MR2_ERRATUM_CROSSCHECK_NL_BPS_PER_PP_0a82cf18_2026-11-09.md | 68f082e9d8225e86f19b4f279aa892ac4601a3b6730fcdf6ccd7897601d6140c | MATCH | 20:37:46 |
| ….py | 6d6e1d394b27e5a750b5064d0471756f06819fbe4e3d79b9151366ac46175171 | MATCH | 20:37:05.41 |
| ….log | d2deadd6c1ed9d7d6ca6f97ab9fc43d0b148054095fd4f3d08e2efd8d03e92f0 | MATCH | 20:37:06.48 |
- **.py before log: confirmed** (1.07 s gap, about 1 s run).
- **Rerun** (/workspace/pp_e68_2040/e.py, same sha, with `EXIT $?` appended as MR2 does): exit 0. The log is **byte-identical**, sha d2deadd6….
- PP extra script: d5basis.py 726852ba….

## 2. Fix-by-fix (PP 0a82cf18 B1–B5)
| fix | verdict |
|---|---|
| B1 (D2 identity) | **FAITHFUL.** The 4 trials are labelled COND evidence. N10 rests on the hand argument and PP's 15-basis exact check. |
| B2 (e12589a5 predates md; C6, X1, D5, BPS split) | **FAITHFUL.** The "no PP audit yet" sentence is withdrawn. C6 is now OPEN via X1. X1 is stated correctly (C3-lift + C6 spinor clause + D1 (ii)–(iii) are inconsistent: D2 forces K_int + 6k_x = 0, but D4 gives −6ε/L). C5 and C7 match PP. The 5D-BPS (BKV) vs 11D HW-BPS split is applied to N5 and N10–N13, and N7/N8 are marked supersymmetry-free. |
| B3 (N8 premise (b)) | **FAITHFUL.** The old wording is withdrawn as wrong. The log gives ∂_φT = 0, ∂_φΔ = 0 and det T = 1 exactly, and ∂_wΔ = (m₃²e^{3w} + m₄²e^{3w} − 2m₅²)e^{4λ−2w} ≠ 0. So φ-scaling at fixed (λ, w) is unchanged and a_eff ≤ −2 carries over. The T used, diag(e^{−6λ}, e^{−6λ}, e^{4λ+w}, e^{4λ+w}, e^{4λ−2w}), has det 1 and reduces to MN2's X₁, X₂ at w = 0. N8 stays PROVED as an implication. |
| B4 (marginal-w caveat) | **FAITHFUL.** N8 is restricted to W₃-flow kept sides. N16 now includes Z2 and the D5 sign in χ-dependent configurations. The recommendation records K7 as OPEN along Z2 and D6. |
| B5 (B3 mapping) | **FAITHFUL.** −2/L ↔ (−3 : 1) ↔ m²L² = 12 (Δ = 6). **+2/L ↔ (1/3 : 1) ↔ m²L² = −4 (Δ = 2).** These pairings match PP's recomputation (0a82cf18 audit scratch). |

## 3. Z1 reproduction (N17): CONFIRMED, exact (rerun)
- ∇V = 0, g²L² = 2^{4/3}, V* + 12/L² = 0.
- No (φ,w) or (λ,w) Hessian mixing.
- **m²L² = {12, −4, 0}**, so w is marginal.
- **w exponents {0, 4}.**
- **W₃ exponents {−2, 2, 4}**, w-entry 4. MR2 uses g > 0, which gives the 4g/|g| of PP's run.
- **∂³_wV = −24·2^{2/3}g²**, exact.
- This is identical to PP pp_bps.log [w]. The (5.15)/(5.16) transcription is the same as in 1aa88a30, so it is PP-consistent but not an independent transcription; this is acceptable.

## 4. N18 (D5 = +σ/2): PROVED (agree)
- PP re-derived it from the D1 rows.
  - x-row: k_xε = −(σ/144)G̸ε.
  - Σ₁-row: k_ΣΓ_{Σ₁}ε + (σ/144)Γ_{Σ₁}G̸ε − (σ/12)Γ^{cde}G_{Σ₁cde}ε = 0.
  - Together: (k_Σ − k_x)Γ_{Σ₁}ε = (σ/12)Γ^{cde}G_{Σ₁cde}ε = (σ/2)Γ^{Σ₂}ω̸ε, and Γ^{Σ₁} then gives +σ·½Γ^{Σ₁Σ₂}ω̸ε.
- MR2's 3 random ω trials alone cover 3 of 6 dimensions. They are confirmation only, as MR2 says.
- **PP settled the Clifford identity exactly on all 6 basis 2-forms ω_ij** (it is linear in ω): 0 failures (d5basis.py).

## 5. Stale attribution (flag)
- The erratum says D5 = +σ/2 "against NL's −σ/2". **That attribution is stale.**
- NL_ERRATUM19_ACCEPT_PP_5f2de6f9_e12589a5_2026-11-09_2029.md (d3dd5a4c, sidecar MATCH, 20:29:37) predates this md (20:37:46). Its **E19-15 (PROVED)** already adopts **+σ/2** and calls the 2017 text's −σ/2 "a sign slip".
- It should read: "+σ/2, agreeing with PP G6 and NL E19-15 (the 2017 text's −σ/2 was corrected by NL)".
- NL's tally and grades are unchanged by E19 (D5 stays COND on H_Σ), so no grade is affected.

## 6. Tally
**14 / 2 / 1 / 1 = 18. CONFIRMED.**
- PROVED: N1–N4, N6–N11, N12a, N13, N17, N18.
- COND: N5, N15.
- OPEN: N16.
- REF: N12b.
- Original N1–N16 unchanged, as before (12/2/1/1).
- N17 is a reproduction of PP Z1 and is fine to count as MR2's own exact verification. N18 is PROVED on the hand derivation.

## 7. Verdict and residual fixes
**FAITHFUL. All of B1–B5 are applied; tally confirmed.**
- **R1.** D5 attribution: replace "against NL's −σ/2" with "agreeing with NL E19-15 (d3dd5a4c), which corrected the 2017 −σ/2". Do the same for the per-NL D5 row.
- **R2 (nit).** B3 writes a_eff = ∂_φ ln T_i, which reuses "T" for constituent tensions. Rename the tensions (e.g. τ_i) to avoid confusion with the matrix T.
- **R3 (optional).** N18: cite PP's 6-basis exact check (d5basis.py 726852ba…) alongside the 3 random trials.
