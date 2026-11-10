# FINDINGS: PP audit of MR2 cross-check of NL BPS / calibrated-wall files (1aa88a30)
Auditor: PP (Professor Proof), Soft SF audit agent. Written 20:34 CST (America/Chicago). Scope: OW d5eaeef3.
- Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only or random-trial = COND. A citation alone is never PROVED. A stated premise is graded as an implication.
- Additive; nothing edited; nothing sent; no CERT; no Gemini; nothing adopted. Naming: resonant algebra.
- Tip 7cddb188 unchanged.

## 1. Provenance
| file | sha256 (recomputed) | sidecar | mtime CST |
|---|---|---|---|
| MR2_CROSSCHECK_NL_BPS_CALIBRATED_WALL_2026-11-09.md | 1aa88a305d0573d954e687fdb3c5bf50d44f0bb4d14fe1472f2a485e9c44a957 | MATCH | 20:29:23 |
| ….py | 11fdb72dc4ffef1f8baf8f50333edbc0b6ffe8397056f0cd2dbdc5413903bccb | MATCH | 20:25:37 |
| ….log | 4f12420cd5587eac27a67ef87def81efa1e836e14ce84690f27372d3d38b609c | MATCH | 20:26:21.886 |
| …_M6_IDENTITY_FIX.py | f06d250dce00b758fe5900157e2ac97be4e47717b537660da058167a40d0f72d | MATCH | 20:26:21.890 |
| …_M6_IDENTITY_FIX.log | 369ac38df40bcb38227774232529185eec32582feaf9cbf5bc29d0d6906ec3e7 | MATCH | 20:26:22.8 |
- .py before log: confirmed for both. The FIX .py was frozen 4 ms after the main log.
- **Main rerun** (/workspace/pp_bps_2033/main.py, same sha): exit 0. The log is **byte-identical** (sha 4f12420c…).
- **FIX rerun:** identical to MR2's log apart from the script path in the traceback. It shows the same 4 × "max entry 0", then the same `TypeError` (EXIT 1) at line 40. The crash is after the identity check, as disclosed. No claim depends on the missing B3 line: PP recomputed it, and exponent −2 goes with (−3 : 1) (m²L² = 12) and +2 with (1/3 : 1) (m²L² = −4), as MR2 states.
- PP script: pp_bps.py ef4d131f… / pp_bps.log 2e6e2257….

## 2. Key checks
**Normalisation: CONSISTENT.** L = R − ½G∂X∂X − V with A′ = −W/3 and X′ = 2G^{ij}∂_jW gives V = 2G^{ij}W_iW_j − (4/3)W².
- G = 60δ gives 2G^{-1} = 1/30, matching PP 5f2de6f9 B1.
- G = diag(6/Σ², 2/Ω², 4) pulls back to diag(60, 60, 3) on (φ, λ, w), matching PP e12589a5 C2. The main log line 15 confirms this, and PP's 3-scalar check gives the superpotential identity residual = 0.

**B1 (N1, N2, N3): PROVED, rerun exact.**
- V* = −3·2^{2/3}g² = −12/L² with g²L² = 2^{4/3}.
- e^{−6λ} = 2^{−3/5} = X1.
- m²L² = {−4, +12}.
- Exponents ∓2/L.

**M6 / D2 identity: PROVED (PP, exact; settled).**
- MR2's main run printed `None`. Its FIX used 4 random integer G: exact arithmetic, but only 4 of the 15 dimensions of internal 4-forms. That is a random-trial check, so on its own **COND**.
- **Settled exactly by PP.** The left side is linear in G, so PP checked it on all **15 basis 4-forms** e_{cdef} (c < d < e < f in the 6 internal directions). All 15 give exactly zero, so the identity holds for every internal G (pp_bps.log [M6 exact]).
- The hand argument in N10 is also a proof: for internal G, Γ^aΓ^{cde}G_acde = Γ^{acde}G_acde because a ∉ {c,d,e}, so Σ_a Γ^a(Γ_aG̸ − 12Γ^{cde}G_acde) = (6 − 12)G̸.
- x-row (no x-legs ⇒ Γ^{cde}G_{xcde} = 0): exact.

**D2 nullity (N11): PROVED given D1.** The exact rank gives an 8-dim kernel for all 8 sign choices. The controls (k_T = −1.5; the MN2-type face with G = 0 and 6 random G) give 0. This agrees with PP e12589a5 D1 ("8-dim kernel analytic").

**D4 witness (N12a): VERIFIED.**
- At the exact MN2 face, k_x = −ε/L and K_int = 0, so K_int + 6k_x = −6ε/L.
- With δ = ε/(2L), the witness is δK = +(ε/2L)·𝟙 on all 10 tangent directions (4 x, 2 Σ, 4 fibre). Its operator norm is exactly ε/(2L) = δ, so it is admissible.
- It gives k_x = −ε/(2L) and each internal k = +ε/(2L), so K_int + 6k_x = 3ε/L − 3ε/L = 0.
- The bound |ΔK_int| + 6|Δk_x| ≤ 6δ + 6δ = 12δ (diagonal entries ≤ operator norm) shows D2 fails for δ < ½ε/L. So the threshold ½ is **sharp for the trace condition**, as MR2 says, and matches PP e12589a5 D4 / E18-1.
- N12b (10δ, 3/5): **REFUTED.** The witness meets the trace at δ = ½ε/L < (3/5)ε/L.

**W_φ + 2W = −3gl·e^{6λ−8φ} (N7): PROVED, exact.** By hand, every term of W has φ-weight −2 except l·e^{−8φ+6λ} (weight −8), which gives (g/2)(−8+2)l·e^{6λ−8φ}. D3 is also exact: the unique solution X = −4, v = −1 is not positive. N9's fibre-determinant lemma det(JᵀhJ) = det h · det(JᵀJ) · (ν̂ᵀh⁻¹ν̂) with h = T⁻¹ and ν̂ = μ is classical; PROVED.

**N8 (w on): PROVED as an implication. Its premises are stated, and its coverage is genuinely limited.**
- **Identity, PP by hand.** In W₃ the w-dependence sits only in e^{−2φ+4λ−2w}, 2e^{−2φ−6λ} and 2e^{−2φ+4λ+w}, all of φ-weight −2. The single φ-weight −8 term is l·e^{2ϕ}/(ΩΣ) = l·e^{−8φ+6λ}, which is w-independent. So W₃_φ + 2W₃ = −3gl·e^{6λ−8φ} exactly.
- **Premises (a)–(c) are stated explicitly.** (a) is the three-scalar W₃-flow assumption on the kept side, as required. (c) holds because G is diagonal with no φw entry; the extra w-junction condition only adds constraints.
- **Premise (b) justification needs rewording.** It says "w enters only the fibre block, not the x- or Σ-warps". In the uplift, w enters T_αβ = diag(e^w, e^w, e^{−2w}) and hence Δ = μᵀTμ, which appears in the x- and Σ-warps (Δ^{1/3}). The φ-weight argument still works, because T and Δ do not depend on φ, so at fixed (λ, w) the constituents' φ-scaling a_eff is unchanged. Restate (b) that way (fix B3).
- **Does PP's P1 extend to the three-scalar sector? It does not, as MR2 says (OPEN). PP sharpens why** (exact sympy, pp_bps.log [w]):
  - At MN2 the three-scalar masses are m²L² = {12, −4, **0**}. **w is marginal: Δ = 4 exactly**, with no Hessian mixing with φ or λ.
  - The second-order linearisation μ² − 4μ − m² = 0 gives μL ∈ {0, 4} for w. There is no hyperbolic decaying direction, but there is a **zero (centre) exponent**. P1's argument (hyperbolic fixed point, 1-dim stable manifold) therefore **does not extend**.
  - The W₃-flow exponent for w is +4/L, so W₃-flows realise only the μ = 4 branch and never the centre direction.
  - The cubic term is nonzero: ∂³_wV|_{MN2} = −24·2^{2/3}g² (exact). So the centre-manifold dynamics are non-degenerate at quadratic order (w′ ∝ w²). This suggests a one-sided family of second-order flows approaching MN2 polynomially (w ~ 1/r) that are **not** W₃-flows.
  - Whether such flows count as "IR-regular" kept sides and admit walls is **OPEN**. It is a concrete candidate class **outside** N8's premise (a), so N8 does not close the w-on sector (fix B4).
  - PP-own items: the masses, the exponents and the cubic coefficient are PROVED (exact). The existence of IR-regular non-W₃ centre flows is OPEN (heuristic).

**Consistency (N13): PROVED, exact.** ρ = 6ε/L, internal pressure −8ε/L, ρ + p = −2ε/L, all in units of κ⁻². That is the stress ratio 6:8:8 with deficit/ρ = 1/3 = L3. D2 would need K_int = 6ε/L, but the face has 0, so the MR2 thin wall is non-BPS.

**Per-NL table vs PP.**
- B4b "4 → 3", P1/P3 PROVED and B6 extended: consistent.
- **Discrepancies with PP e12589a5** (written 20:26:32, before MR2's md at 20:29:23; MR2 says "no PP audit … yet"):
  - C6 is **OPEN** per PP (the spinor clause conflicts with D4 via X1), not COND/concur.
  - D5: PP's sign is **+σ/2** (G6); MR2's "concur" should note the sign.
  - X1 (PROVED: the 5D BKV and 11D HW readings are inconsistent at the MN2 face) is not mentioned. N5's "BPS" wording should say 5D-BPS (BKV) vs 11D HW-BPS separately (fix B2).

## 3. Per-claim table
| # | claim | MR2 | PP | reason |
|---|---|---|---|---|
| N1 | V = 2G^{ij}W_iW_j − (4/3)W², flow solves EOM | PROVED | **PROVED** | exact, rerun identical |
| N2 | MN2 data: V* = −12/L², X1, masses −4, 12 | PROVED | **PROVED** | exact |
| N3 | exponents ∓2/L, eigenvectors | PROVED | **PROVED** | exact; mapping −2 ↔ (−3:1) ↔ Δ = 6 (PP) |
| N4 | (5.16) = (3.8) at w = 0; kinetic 60, 60, 3; W₃ identity; w = 0 invariant | PROVED | **PROVED** | exact; transcription of CGR is the stated input |
| N5 | W is the gravitino shift | COND | **COND** | cited fermion shifts |
| N6 | (D) not in the CGR level-0 sector | PROVED | **PROVED** | exact |
| N7 | W_φ + 2W identity; D3 no positive solution | PROVED | **PROVED** | exact; by hand |
| N8 | obstruction with w on, given (a)–(c) | PROVED (impl.) | **PROVED (impl.)** | premises stated; (b) rewording; coverage limited by the w centre direction |
| N9 | fibre-determinant lemma | PROVED | **PROVED** | classical lemma; float confirmation is extra |
| N10 | D2 trace identity | PROVED | **PROVED** | hand argument plus PP 15-basis exact check. MR2's 4-random-trial evidence alone would be COND. |
| N11 | 8-dim kernel, all 8 signs | PROVED | **PROVED** | exact rank, given D1 |
| N12a | 12δ, ½ε/L, sharp | PROVED | **PROVED** | witness verified |
| N12b | 10δ, 3/5 | REF | **REF** | counterexample (witness) |
| N13 | 6:8:8, deficit/ρ = 1/3, non-BPS | PROVED | **PROVED** | exact |
| N15 | recommendation unchanged | COND | **COND** | on D6/B12 OPEN |
| N16 | χ-walls; whether all w-sector IR flows are W₃-flows | OPEN | **OPEN** | sharpened: w marginal, centre direction |
- **MR2 12/2/1/1 = 16: CONFIRMED.**
- PP-own additions: **Z1** (w: m²L² = 0, μ ∈ {0, 4}, W₃ exponent 4, ∂³_wV = −24·2^{2/3}g²) PROVED; **Z2** (non-W₃ IR centre flows exist) OPEN.

## 4. Fixes
- **B1.** M6: state that the 4 random trials are not a proof. Cite the hand argument, or PP's exact check on the 15 basis 4-forms (the identity is linear in G).
- **B2.** Inputs and per-NL table: PP e12589a5 existed when the md was written. Set C6 to OPEN (X1). Note the D5 sign +σ/2 (G6). Cite X1. Split "BPS" into 5D-BPS (BKV) and 11D HW-BPS.
- **B3.** N8 premise (b): w does enter the x/Σ warps through Δ. Justify a_eff ≤ −2 by the φ-independence of T and Δ at fixed (λ, w), not by "w enters only the fibre block".
- **B4.** N8/N16: add that w is marginal at MN2 (m²L² = 0, second-order exponents {0, 4}, W₃ exponent 4, nonzero cubic). P1 does not extend, and centre-manifold flows (w ~ 1/r, one-sided) are candidate non-W₃ kept sides outside premise (a). N8's coverage of the w-on sector is therefore OPEN beyond W₃-flows.
- **B5.** FIX script: the `P(...)` typo is cosmetic (disclosed). Record the B3 mapping: exponent −2 ↔ (−3:1) ↔ m²L² = 12 (Δ = 6).
