# MR2 erratum to the BPS cross-check 1aa88a30, per PP audit 0a82cf18 (20:34) and PP e12589a5 (20:26)

Date: 2026-11-09, America/Chicago. Author: MR2 (resonant algebra project). This file is additive. 1aa88a30 is not edited, the tip 7cddb188 was not touched, and there was no CERT, no Gemini and nothing sent.

Basis:
- `FINDINGS_PP_AUDIT_MR2_CROSSCHECK_NL_BPS_1aa88a30_2026-11-09_2034.md` (0a82cf18…, sidecar MATCH);
- `FINDINGS_PP_AUDIT_NL_BPS_B2_B12_89ec258a_f8801bff_2026-11-09_2026.md` (e12589a5…, sidecar MATCH; read in full for X1, C6, D5).

PP confirms MR2's tally of 12/2/1/1 = 16.

Artifacts (the .py was frozen before its log):

| file | sha256 |
|---|---|
| `MR2_ERRATUM_CROSSCHECK_NL_BPS_PER_PP_0a82cf18_2026-11-09.py` | 6d6e1d394b27e5a750b5064d0471756f06819fbe4e3d79b9151366ac46175171 |
| `MR2_ERRATUM_CROSSCHECK_NL_BPS_PER_PP_0a82cf18_2026-11-09.log` | d2deadd6c1ed9d7d6ca6f97ab9fc43d0b148054095fd4f3d08e2efd8d03e92f0 |

The run is exact sympy, exit 0, about 1 s.

## PP additions, recorded and independently verified
**Z1 (PROVED; PP, and MR2 independently, exact).** I took CGR (5.16) at z = 0 with (5.15) and the kinetic metric G = diag(60, 60, 3) on (φ, λ, w). At MN2 (l = −1, e^{30φ} = e^{10λ} = 2, w = 0):
- ∇V = 0, g²L² = 2^{4/3} and V* = −12/L².
- The Hessian has no mixing of w with φ or λ.
- **m²L² = {12, −4, 0}.** So **w is marginal (Δ = 4)**.
- The second-order exponents for w are μL ∈ {0, 4}, so there is a centre direction.
- The W₃-flow exponents are {−2, 2, 4}, with w-entry +4. So W₃-flows realise only the μ = 4 branch.
- **∂³_wV|_{MN2} = −24·2^{2/3}g²** (exact, ≠ 0).
- Consequence: P1's hyperbolic-saddle argument does **not** extend to the three-scalar sector.

This is MR2's N17. For transcription consistency, the (5.16) potential at w = 0 equals (3.8): 1aa88a30 N4.

**Z2 (OPEN; PP).** One-sided centre-manifold flows with w ~ 1/r are candidate IR-approaching kept sides that are **not** W₃-flows. Whether they count as IR-regular and admit walls is OPEN.

## Fixes
**B1 (D2 identity).** The 4 random integer trials in `…_M6_IDENTITY_FIX.log` are exact arithmetic, but they cover only 4 of the 15 dimensions of internal 4-forms. On their own they are **COND evidence, not a proof**.
- The identity is **PROVED** by the N10 hand argument: for internal G and internal a, a ∉ {c,d,e}, so Γ^aΓ^{cde}G_acde = Γ^{acde}G_acde, and Σ_a Γ^a(Γ_aG̸ − 12Γ^{cde}G_acde) = (6 − 12)G̸ = −6G̸.
- Independently, PP checked it exactly on all 15 basis 4-forms (the identity is linear in G).
- N10's grade (PROVED) rests on these two, not on the trials.

**B2 (PP e12589a5 existed before MR2's md).** e12589a5 was written at 20:26:32, before 1aa88a30 at 20:29:23. The input statement "There is no PP audit of 2012, 2017 or ERRATUM18 yet" is withdrawn, and e12589a5 is cited here. Per-NL table changes:
- **C6: OPEN**, not "concur, COND".
  - The bosonic oddness of G₄ under g → −g is PROVED (PP).
  - The spinor clause (Γ_rε = +ε as the HW projection) is OPEN, because it conflicts with D4 via **X1**.
- **X1 (PP, PROVED; MR2 concurs):** {C3-lift, C6 spinor clause, D1 (ii)–(iii)} cannot all hold.
  - An RS/BKV ℤ₂ wall on the exact MN2 face is 5D-supersymmetric (C5 ⇐, T = 4W*).
  - An 11D HW-BPS lift would force K_int + 6k_x = 0 (D2), but D4 gives −6ε/L.
- C5 is PROVED as an implication from the stated 5D Killing-spinor equations. C7 is PROVED as logic, but its route through C3 + C6 is vacuous (PP G4). B4–B7's level-0 validity rests on PP P1/P3, which need no supersymmetry.
- **D5: COND, with sign +σ/2.**
  - MR2 checked it: the Σ₁ row with the x-row substituted gives (k_Σ − k_x)Γ_{Σ₁}ε = (σ/12)Γ^{cde}G_{Σ₁cde}ε.
  - Here Γ^{cde}G_{Σ₁cde} = 6Γ^{Σ₂}ω̸. This holds by index counting, with exact Clifford checks on 3 random ω in the log.
  - Left-multiplying by Γ^{Σ₁} gives **(k_Σ − k_x)ε = +σ·½Γ^{Σ₁Σ₂}ω̸ε**. This agrees with PP G6, against NL's −σ/2. This is MR2's N18 (PROVED: hand derivation, with exact checks as confirmation).
- **The word "BPS" is now split everywhere in 1aa88a30.**
  - **5D-BPS (BKV)** means the 5D Killing spinor with a W sign flip (2012 file: C3, C5).
  - **11D HW-BPS (D1)** means the 11D Killing spinor with the HW projection (2017 file: D1–D4).
  - N5's "W is the gravitino-shift superpotential" refers to 5D-BPS only.
  - N10–N12 and N13's "non-BPS" refer to **11D HW-BPS**. The exact MN2 face is 11D-HW-non-BPS (D4). It can still be 5D-BPS as an RS/BKV wall, which is X1.
  - The no-wall statements N7 and N8 need no supersymmetry at all: they are Israel junction statements, via PP P1/P3.

**B3 (N8 premise (b) restated).** The old wording, "w enters only the fibre block, not the x- or Σ-warps", is **wrong**.
- w enters T_αβ = diag(e^w, e^w, e^{−2w}), and through it Δ = μᵀTμ. The log shows ∂_wΔ ≠ 0, and Δ^{1/3} appears in the x- and Σ-warps.
- Corrected premise (b): **T and Δ are φ-independent** (log: ∂_φT = 0, ∂_φΔ = 0, det T = 1).
- So at fixed (λ, w) every constituent's φ-scaling, a_eff = ∂_φ ln T_i, is the same as in B5. The bound a_eff ≤ −2 (B5 menu, PP P5) carries over unchanged.
- N8 stays **PROVED as an implication**.

**B4 (marginal-w caveat on N8 and N16).**
- **N8** now reads: "The B6 obstruction holds with w on **for kept sides that are W₃-flows** (premise (a))."
  - Because w is marginal at MN2 (Z1: m²L² = 0, exponents {0, 4}, W₃ exponent 4, cubic −24·2^{2/3}g²), P1 does not extend.
  - One-sided centre-manifold flows (w ~ 1/r) are candidate non-W₃ kept sides outside premise (a).
  - So N8 does **not** close the w-on sector. Coverage beyond W₃-flows is Z2 (OPEN).
- **N16 (OPEN), sharpened.** Three things remain open:
  - finite-amplitude χ-dependent walls (D6/B12);
  - whether non-W₃ centre flows in w form IR-regular kept sides that admit walls (Z2);
  - the D5 sign question in χ-dependent configurations.

**B5 (B3 mapping).** The FIX script's `P(...)` typo is cosmetic and was disclosed. The B3 mapping is:
- exponent **−2/L ↔ eigenvector (δφ : δλ) = (−3 : 1) ↔ m²L² = 12 (Δ = 6)**;
- exponent **+2/L ↔ (1/3 : 1) ↔ m²L² = −4 (Δ = 2)**.

This agrees with PP and NL B3.

## Tally
- MR2's original N1–N16 (N12 split) are unchanged in grade: **12 / 2 / 1 / 1 = 16**, as PP confirmed.
  - N8 keeps PROVED (implication) with its premise (b) restated and its coverage narrowed.
  - N10 keeps PROVED on the hand argument and PP's 15-basis check.
  - N16 stays OPEN, now including Z2.
- New MR2 items: **N17** (independent Z1 verification) PROVED and **N18** (D5 sign +σ/2) PROVED.
- **Running tally: PROVED 14 · COND 2 · OPEN 1 · REF 1 = 18.**
  - PROVED: N1, N2, N3, N4, N6, N7, N8, N9, N10, N11, N12a, N13, N17, N18.
  - COND: N5, N15.
  - OPEN: N16.
  - REF: N12b.
- Per-NL table changes: C6 is COND → **OPEN** (X1); D5 stays COND with sign +σ/2. Everything else is unchanged.

## Recommendation
**N15 (COND): the face/wall recommendation does not change.**
- **Item 1:** keep (1a), the HW E₈ face. Closure needs changed face data (T7/B12, OPEN).
- **Item 2:** keep (2a), the thin wall. It is non-BPS in the 11D HW sense; that was always so and is fine.
- The **BPS / first-order loophole (K7)** is closed only in the decided classes: level-0, and W₃-flow kept sides with w on. It is **OPEN along Z2** (marginal-w centre flows) and along D6.
- The K6′ deficit stands as a COND heuristic.
