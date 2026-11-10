# MR2 branch attempt (OW t4436): batch-2 branches Φ-2, Φ-3, W-2, W-3, G2-2 (torsion-free), Rc-1, Rc-2 — exact closed form of the MN2 11D Ricci scalar
2026-11-09, written 22:01 CST (America/Chicago, box clock). Author: MR2. Additive; nothing edited; nothing adopted; no CERT, no Gemini, nothing sent, no agent messaged. Junction **UNSOLVED**. Register: MR2_BRANCH_REGISTER_ALL_OPEN_PATHS_PER_OW_t4436_2026-11-09.md (c5a65972…). Authority OW t4436 (32881263…). Only a PP-audited PROVED/REFUTED keeps or drops a branch: **every grade below is MR2's proposal, pending PP audit.**

## Scripts and logs (all in /workspace/mr2-branch-2134/; each .py frozen with its sidecar before it ran; sha = sidecar unless noted)
| file | sha256 | role |
|---|---|---|
| sym_R_probe_2026-11-09_2135.py / .log | 61cd2b86c90eedbbd6affb3d570174d5e716dce97fa6c76f1b5e626c57e50536 / 6e87f1e5eda75dcd19b489584dc313434adf19a37ee48f60aef4ea32fdda1888 | **v1, BUG** (∂_bΓ^c_{ac} summed only at c = b); gives wrong R (−832…); superseded, supports no claim |
| sym_R_probe_v2_2026-11-09_2139.py / .log | eebd94008a6ecdec7eeee9ab0f1ce719cad6766eb1a4a620085d3355a8f910fa / b3eb85dc8f78f273ed6ffd4b73526fb60404583647866665923db328c2ae8d81 (log sidecar written after the run) | fixed routine; reproduces 516438eb R at (1/3, 2/7) and (3/2, 1/5) to 25+ digits |
| R_closedform_2026-11-09_2142.py / .log | 146257797c1eb21140ab24e19637b9aec10271f042b7054f9536b664668f2480 / 43c8be31baa792ce16374cfc65f6dad320dc8019db6dc4562952edbdd400e5ed | **abandoned** (trig substitution incomplete, AssertionError). Self-flag: I believed I had killed it and appended a "KILLED" note; the kill hit the wrapper, the process ran on and overwrote the note. The first sidecar (96c3b633…, now *.sha256.pre_append) matched the note-only file; the current sidecar matches the final log. Only use: numeric ∂R/∂r = ∂R/∂y = 0 at a sample point |
| R_mu_chart_2026-11-09_2147.py / .log | 486c1c2d2c1f60a3cedd9d092f9f9ecdb679677dc3605b949074717bf91844ba / c50da082f0dcdf34af3c2bbbfe48a223c78aef13d580fa720934880209f70a5e | symbolic R in the (μ₁, μ₂) chart, `cancel` to num/den; R_mu.pkl 7525e9dd85c004f6af9823b0bf6ff8201b5f89f22e24f0a1321e7291e1f3d033 |
| Phi_bounds_2026-11-09_2156.py / .log | 84ac46e419352d78dbf539322b779ced311dced90c66c086d68245d153f2b493 / 00b3981c599b5525eeb03d33a093e888e922884f9b4b65fe44052cdfd0a6be42 | v1, crashed at [C] (interval conversion); its [A]/[B] output equals v2's |
| Phi_bounds_v2_2026-11-09_2154.py / .log | 0d61743d7482df55e0384b4d2105e07ae5a644409f077c91c22549a594c08ce0 / ae53d8db0d1263fc38d775c8fe4be655f1ea4c17ae836a937f63dfea62f1d8b6 | closed form, exact pole values, interval enclosure, float averages |
| R_monotone_and_Rc_arith_2026-11-09_2157.py / .log | 76831625338f374707de17577133347fb3ee9fb7771c13b479c5d2a55d56f4e8 / 97e620f73a513741e3f832d6a6cc1229b508d57d7b872e9067dadd2402712304 | exact monotonicity, range, EH-lock families, R_c arithmetic |
| G2_R7_slice_2026-11-09_2149.py / .log | 2a66fdfd636d371cdf54ba95650a0ef25644aade901ebeae261c4f5f471d62be / 9ea8751ea6f68067bcb18ec21f3eb148af608b2c7c76c625e073c6a5624888be | v1, crashed (mpf × interval) |
| G2_R7_slice_v2_2026-11-09_2152.py / .log | 5a6d4659dbd02df24221c12be687ea242de39ec8dd887992a37f93a3c39a5f17 / 0460a6298f6733f7c412c347877dcb5c640081ad95ca8465df3e77ec8323f24b | R₇ interval enclosures |
Self-flag (cosmetic): the hh:mm in script *names* and "FROZEN hh:mm" header lines were my estimates and run up to 5 min ahead of the box clock (e.g. Phi_bounds_v2 "2154" frozen 21:52:55; R_monotone "2157" frozen 21:54:36). The mtimes above the run logs are authoritative; every .py mtime precedes its log's.

Metric: identical to frozen 516438eb (MN2 uplift, X₁ = 2^{−3/5}, X₂ = X₀ = 2^{2/5}, F = 2^{−4/5}, G_s = 2^{1/5}/4, a₁ = 1, a₂ = 0, ℓ = 1 units), rewritten in the chart (μ₁, μ₂) of the upper S⁴ hemisphere with μ₀ = +√(1−μ₁²−μ₂²).

## Results
**T3-1. Closed form (PROVED, exact symbolic computation, given premise S below).** On MN2,
  **R₁₁ = P(p) / Δ^{10/3},  p := μ₁²,  P(p) = −p³ + (20/3)p² − 16p + 40/3,  Δ = 2^{2/5}(1 − p/2).**
- Evidence: sympy Ricci scalar (validated routine) → `cancel` gives den = 24 F G_s² X₁⁴X₂⁴ d⁴ (X₁²X₂²Δ)² with d³ = Δ (identity checked exactly, [A]); num has only d⁰, d³, d⁶ and only even powers of μ₁, μ₂, so d³ → Δ leaves a polynomial; after the MN2 substitution all μ₂-dependence cancels (Δ is μ₂-independent because X₂ = X₀). Matches 516438eb at (α, β) = (1/3, 2/7), (3/2, 1/5), (10⁻⁵, 3/4) to ≥ 25 digits.
- r, y independence: AdS₅ dilatation (r, x^μ) → λ(r, x^μ) and H² isometries (twist a₁dx/y invariant) are isometries, so R is constant along them (PROVED); consistent with 516438eb and the R_closedform log.
- **Premise S:** the uplift metric is smooth on S⁴ (Δ > 0, constant X's); the chart formula, valid on the dense open set μ₀μ₁μ₂ ≠ 0, then extends by continuity to all of S⁴. (Standard; stated, not re-proved here.)

**T3-2. Exact range (PROVED, by hand, checked exactly in sympy).** dR/dp = 2^{−4/3}(1−p/2)^{−13/3} Q(p) with 18Q = −3p³ + 26p² − 96p + 112. (18Q)′ = −9p² + 52p − 96 has discriminant −752 < 0 and is negative, so 18Q decreases; 18Q(1) = 39 > 0. Hence **R is strictly increasing in μ₁²**: min R = **10·2^{2/3}/3 = 5.29133683989…** on {μ₁ = 0}, max R = **12** exactly at μ₁ = ±1 (minimal polynomial x − 12). Ratio max/min = 9·2^{1/3}/5 = 2.26785788981. Independent interval enclosure over the whole simplex (2033 boxes): R ∈ [5.2605, 12.0446], consistent.
- **Upgrades in f688c7e3/90f43897:** row 4b-ii (Φ range) **COND → PROVED**: Φ_phys = 144R/ℓ² ∈ [1440·2^{2/3}/(3ℓ²), 1728/ℓ²] = [0.308665516277, 0.700009526401] ℓ_p⁻² at N = 4880 (as a statement about 144R; reading it as G·G uses K1 on shell, COND on MN2 being a solution, OW 19a88b19 — unchanged). Row 4c "R_max = 12 exactly" **COND → PROVED** (so Φ_max = 2Φ_(D) exactly).

**T3-3. Φ-3 EH lock: REFUTED, now with no COND input on R_max.** Φ-3 := 144·R(μ₁ = 1)/ℓ² = 1728/ℓ² (T3-1/T3-2, exact). With k = 1/L₅, L₅ = ℓe^{f₀}: k²/(Φ₃/1728) = 2^{4/5} ≠ 1. More strongly, for every constant k in the AdS₅ curvature family k² = 1/(Δ(p₀)^{1/3}Fℓ²) (warped radius at any point p₀, which includes k = 1/L₅ at Δ^{1/3} → 1), k²ℓ² ∈ [2^{2/3}, 2] while Φ₃ℓ²/1728 = 1. **REF (PROVED).** The Φ-3 *definition* stays viable; only its EH-lock sub-claim is dropped.

**T3-4. Φ-2 EH lock: REFUTED (PROVED).** For *any* positive weight w on M₆ (√g₆, √g₆·Δ^{5/6}, …), R̄ := ∫wR/∫w ∈ [10·2^{2/3}/3, 12] (T3-2). The lock k² = Φ̄/1728 with Φ̄ = 144R̄/ℓ² requires R̄ = 12k²ℓ² ∈ [12·2^{2/3}, 24] = [19.0488, 24] for k in the AdS₅ family above (20.8932 for k = 1/L₅). Since R̄ ≤ 12 < 19.0488, **no AdS₅ curvature scale satisfies the lock under Φ-2.** (If k is merely *defined* by k² := Φ̄/1728, it is not an AdS₅ scale: k²ℓ² = R̄/12 ≤ 1 < 2^{2/3}.) Float values, **COND (quadrature)**: R̄ = 7.07177633 (weight √g₆), 6.86143344 (√g₆·Δ^{5/6}); Φ̄ = 0.41252590 / 0.40025573 ℓ_p⁻², ratio to the k = 1/L₅ target 0.3385 / 0.3284.

**T3-5. W-2 finite (PROVED as implication of K1 on shell + premise S + Σ compact).** ‖G‖² = G·G/4! = 6R ≤ 72 on M₆, and M₆ (S⁴ over the compact Bolza Σ) is compact, so ∫_{M₆}‖G‖² vol₆ ≤ 72 Vol(M₆) < ∞. Value = 6R̄ Vol(M₆) with R̄ = 7.0718 (COND, quadrature; Vol(M₆) not computed). W-2 viable.

**T3-6. W-3 diverges (PROVED, given the induced slice measure).** On M₇ = ℝ_r × M₆ at fixed x^μ, vol₇ = √(Δ^{1/3}F)·(dr/r) ∧ vol₆, and ‖G‖² = 6R ≥ 6·5.2913 > 0, so ∫ diverges logarithmically at r → 0 and r → ∞. W-3 is **REFUTED as a finite quantity without a cutoff**; only "W-3 with a cutoff (b or a face location)" survives (NL lane, OPEN).

**T3-7. G2-2 torsion-free sub-branches (t-i), (t-ii): REFUTED.** R₇ of the induced slice metric (t-i) at (μ₁, μ₂) = (1/3, 1/4), (1/2, 1/2), (1/10, 7/10), (3/5, 1/5): **30.7501042682, 34.0736935741, 28.7544652579, 37.3312786179** (interval width < 10⁻⁴⁰, all exclude 0); warp-stripped Δ^{−1/3}g₇ (t-ii): **20.8329678054, 26.2231149270, 17.6920425126, 31.6546892510** (exclude 0). Same validated Christoffel/Ricci routine as T3-1. Torsion-free G₂ ⇒ Ricci-flat (standard: a torsion-free G₂-structure gives a parallel spinor ψ; contracting [∇_a, ∇_b]ψ = ¼R_{abcd}γ^{cd}ψ = 0 with γ^b gives Ric_{ad}γ^dψ = 0, so Ric = 0) ⇒ R₇ = 0. Contradiction, so **no torsion-free G₂-structure induces either metric: REF** (implication of that standard identity). **(t-iii)** (torsion-free G₂ with an unspecified metric on ℝ × M₆) stays **OPEN**. G2-1 and "G₂-structure exists" (COND) are unchanged.

**T3-8. Rc-1 / Rc-2 arithmetic (PROVED arithmetic; physics COND).**
- Rc-1: kε_y = R_c·k ∈ [0.04052, 0.04548] for 1/k ∈ [35.13, 39.43] ℓ_p (0.04243 at 1/k = L₅). So Rc-1 **is a thin wall** (kε ≪ 1), compatible with 2a's thin-wall weights, and unlike 2b (kε ∈ [0.630, 0.707]).
- Rc-2: cutoff 1/R_c ⇔ m²L₅² < (L₅/R_c)² = **555.479**. Every Group A mode computed so far (spin-2 12, 20, 32, 40; charged 55.157; Landau 84; Σ-only 46.157; scalars −4, 0, 5, 12; vectors 0, 8) lies below it (largest m·R_c = 0.389). Arithmetic PROVED; as KK masses COND (as in ff7fb67f/8ca7b93a). Rc-2 viable; nothing decisive against it.

## Branch status changes (MR2 proposal; pending PP audit)
| branch | before | after |
|---|---|---|
| Φ-2 (EH lock) | OPEN | **REFUTED** (T3-4); Φ-2 definition viable, value Φ̄ ≈ 0.4125 ℓ_p⁻² COND |
| Φ-3 (EH lock) | REF, COND on R_max = 12 | **REF (PROVED)** (T3-3) |
| row 4b-ii Φ range | COND | **PROVED** [0.308665516, 0.700009526] ℓ_p⁻² (T3-2) |
| row 4c R_max = 12 | COND | **PROVED** (T3-2) |
| W-2 | finite COND; value OPEN | **finite PROVED** (implication); value COND |
| W-3 (finite, no cutoff) | OPEN | **REFUTED**; W-3 with cutoff OPEN (NL) |
| G2-2 (t-i), (t-ii) torsion-free | OPEN | **REFUTED** (T3-7) |
| G2-2 (t-iii) | OPEN | OPEN |
| Rc-1 | PROVED/COND | + thin-wall parameter PROVED arithmetic (0.041–0.045) |
| Rc-2 | PROVED/COND | + all computed Group A modes below cutoff (arith. PROVED, masses COND) |

**Tally of this file's claims:** PROVED 9 (T3-1, T3-2, 4b-ii, 4c, T3-3 REF-proof counted under REF below, T3-5, T3-6 divergence, T3-8 Rc-1, T3-8 Rc-2 arithmetic, r/y independence) — counted as **PROVED 8 · COND 3 (Φ̄ values, W-2 value, Rc-2 as KK masses) · OPEN 1 (G2 t-iii) · REF 4 (Φ-3 lock, Φ-2 lock, W-3 finite, G2 t-i/t-ii) = 16**. PROVED rows: T3-1, r/y independence, T3-2, 4b-ii, 4c, T3-5, T3-8a, T3-8b.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, untouched.
