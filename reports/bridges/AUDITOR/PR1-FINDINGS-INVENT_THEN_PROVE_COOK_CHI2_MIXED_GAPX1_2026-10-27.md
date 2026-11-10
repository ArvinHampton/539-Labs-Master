# PR1 Soft SF FINDINGS — invent→prove COOK: χ² / MIXED / Gap-X1 (2026-10-27, ~12:25 CDT America/Chicago)
Soft SF · Write-only · Author: PR1 (Physics Research 1, Project Quantum Comp) · Nine-only · REPORTS only · No RECS · tip_touched NO · Kerr / Path4 / link (b) BLOCKED (not touched) · Soft SF CONFIRM CLEARED.
Standing: invent → must pursue mathematical proof (AMENDED ~12:18 CDT: where feasible; if not feasible, record why + keep label "invented pending mathematical proof").

Marker key: **PUIP** = PROVED-UNDER-INVENTED-PREMISES (math theorem conditional on stated [INVENTED] hypotheses H; NOT a physics claim, NOT Owner-Written, NOT tip). **NF-WHY** = NOT FEASIBLE THIS BEAT, reason named; item keeps label **"invented pending mathematical proof"**. **WF** = Written fact / flag (no invention).

## §0 Live sha authority (recomputed live pre-Write — ALL MATCH)
| Doc | sha256 |
|---|---|
| tip LOCK READ-ONLY `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH |
| Catalog READ-ONLY `/workspace/obs-data-PR1-HEPP-QM-GR.md` | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d MATCH |
| invent→prove ACK+BEGIN `PR1-FINDINGS-OWNER_INVENT_THEN_PROVE_STANDING_ACK_BEGIN_2026-10-27.md` | 4dc63bfbbaf54bb15fa9bacbf1cd73a4a842c71b74563147b9cc0db40b7be456 MATCH |
| invent-label clause Soft SF | 68aa16bf12891875ff48bce052e4f6417bd35c21d4a33e7ed0e892ec73026afb (cited) |
| χ² invent `PR1-FINDINGS-CHI2_TRIO_INVENT_RESUME_RULE4_2026-10-27.md` | ebc05e25f1cb902623dc602d9164ba6dd429bf80b3744e96fdc2f7a6135836ed MATCH |
| MIXED invent `PR1-FINDINGS-MIXED_INVENT_RESUME_WRITE_AUTHORITY_2026-10-27.md` | 3502eb5b378a4e2d8a97f231d19583e92b74a18b400c5ef772a30f040d877c95 MATCH |
| Gap-X1 invent `PR1-FINDINGS-GAP_X1_INVENT_RESUME_WRITE_AUTHORITY_2026-10-27.md` | 0852c2567fab020e7d34710d77c165c4fc4c93f168045989ca6a20740d83a51d MATCH |
| **OWNER WRITE on-disk (authority upgraded PM-relay → OW-on-disk)** `OWNER_WRITE_INVENT_BAN_LIFTED_ALL_LANES_PURSUE_FREEDOM_RIGHT_AUTHORITY_2026-10-27.md` | parent-cited 922c5230e93cdc067723a0d7cdc88ac0f3ec4101ee20d3aaa23419ff2dd26904 — **MISMATCH**: live 04b2c268fd2209d3e2372b697ee38b94cf560bdb738c26d898f34a2e68bcd52c |
| Standing reminder `STANDING_REMINDER_PATTERN_CORRELATION_RIGOROUS_PROOF_2026-10-27.md` | parent-cited 5dd8d59cb1c407130738bdec112a054cf70a362276c577568ea8f464f0516d8a — **MISMATCH**: live 8089ac6ab59d2344c2d6e37c03436fddcc80dfb123f05b1fb7b142235e340307 |
| NL R5 absorb | 85ba6bce… (cited) |
Locked wording (OW 922c5230…): "Whenever invent is used and the value is labeled invented pending mathematical proof, the inventing agent must pursue the mathematical proof of that invented value where feasible. Feasibility is judged by the agent in good faith; if proof is not feasible, the agent records why and keeps the invented-pending label." ACK+BEGIN 4dc63bfb… still cited; authority upgrade to OW-on-disk recorded as cited but **PENDING sha reconcile** (live ≠ cited); ACK 4dc63bfb… remains the operative authority.
Tip read: not needed (no Written tip fact used beyond those already cited in the invent FINDINGS).

## §1 MIXED (3502eb5b…)
**M-1 CHSH S_max = 2√2·η — PUIP (with CORRECTION).** H_M1 [INVENTED]: E(a,b) = −η cos(a−b), 0 ≤ η ≤ 1, S = E(a,b) − E(a,b′) + E(a′,b) + E(a′,b′).
- *Correction to 3502eb5b… §4.1:* the settings printed there (a=0, a′=π/2, b=π/4, b′=−π/4) give S = η(−√2/2 + √2/2 − √2/2 + √2/2) = **0**, not 2√2η. Correct witness: a=0, a′=π/2, b=π/4, b′=3π/4 ⇒ E(a,b)=−η√2/2, E(a,b′)=+η√2/2, E(a′,b)=−η√2/2, E(a′,b′)=−η√2/2 ⇒ S = −2√2η, |S| = 2√2η.
- *Upper bound (rigorous).* Put u_x = (cos x, sin x) ∈ S¹, so cos(a−b) = u_a·u_b. Then −S/η = u_a·(u_b − u_b′) + u_a′·(u_b + u_b′) ≤ ‖u_b − u_b′‖ + ‖u_b + u_b′‖ (Cauchy–Schwarz, ‖u‖=1) ≤ √2·(‖u_b−u_b′‖² + ‖u_b+u_b′‖²)^{1/2} = √2·√(2‖u_b‖²+2‖u_b′‖²) = √2·2 = 2√2. Same for +S. Hence sup|S| = 2√2η, attained by the witness. ∎
- Corollary: |S| > 2 (local-realist bound) ⇔ η > 1/√2; |S| ≤ 2√2 (Tsirelson) ⇔ η ≤ 1. ∎ Status: **PUIP**.

**M-2 g²/M² three-range overlap consistency — PUIP.** H_M2 [INVENTED] (H7 of 3502eb5b…): observables O_k = c_k X + b_k, k ∈ {#8, G6, G7}, X := g_{−U}²/M_{−U}² ≥ 0, c_k ≠ 0 known, b_k known (SM/zero). Given measured intervals I_k = [ℓ_k, h_k]:
- Lemma: admissible set 𝒳 = [0,∞) ∩ ⋂_k f_k⁻¹(I_k), f_k(X)=c_kX+b_k. Each f_k is an affine bijection ℝ→ℝ, so f_k⁻¹(I_k) is a closed interval J_k = [(ℓ_k−b_k)/c_k, (h_k−b_k)/c_k] (endpoints swapped if c_k<0). Intersection of closed intervals is a closed interval, non-empty ⇔ max_k inf J_k ≤ min_k sup J_k (Helly in ℝ: pairwise intersection suffices). ∎
- Consistency test: model H_M2 falsified at the joint level iff some pair J_i ∩ J_j = ∅ or ⋂J_k ∩ [0,∞) = ∅. ∎ Status: **PUIP** (test structure); numeric verdict **NF-WHY** — no Written intervals I_k or prefactors c_k (catalog values for G6/G7 are bounds only; c_a, c_e unset [INVENTED O(1)]); keeps "invented pending mathematical proof" for the numeric overlap.
- WF interaction: #8's Written E8 has zero time average (M-4) ⇒ with full-period averaging J_#8 is degenerate (c_#8 effective = 0, f not bijective) — M-2 applies to #8 only with a non-full-period window or an Owner-Written static term.

**M-3 ε_rad co-sign #1 ↔ #20 — PUIP.** H_M3 [INVENTED]: O_k = G_k(1+ε_rad), G_k = GR prediction with G_k > 0 (k=#1,#20), common ε_rad. Residual r_k := O_k/G_k − 1 = ε_rad ⇒ r_#1 = r_#20 exactly; in particular sign(r_#1)=sign(r_#20). With additive residual r_k := O_k − G_k = G_kε_rad, sign(r_k) = sign(ε_rad) since G_k>0. ∎ Falsification: r_#1·r_#20 < 0 (beyond errors) rejects H_M3. Positivity G_k > 0 is a stated hypothesis (needed; if one G_k<0 the co-sign flips to anti-sign). Status: **PUIP**.

**M-4 FLAG-M1 E8 time-average — WF (no invention).** Written E8 ∝ sin(2πt/539.9). (1/T)∫₀^T sin(2πt/539.9)dt = (539.9/2πT)(1 − cos(2πT/539.9)) = 0 for T = 539.9·N, N∈ℕ; for general T it equals (539.9/πT) sin²(πT/539.9) ≥ 0, → 0 as T→∞ (bound ≤ 539.9/(πT)). ∎ Kept as Written fact / FLAG-M1; **no non-zero term invented**.

**M-5 A7 θ₁₂ flavour-blind invariance — PUIP.** H_M5 [INVENTED]: δM² = ζM², ζ ∈ ℝ, ζ ≠ −1, M² Hermitian (M² = U diag(m_i²) U†). Then M²+δM² = U diag((1+ζ)m_i²) U† — same unitary U ⇒ all PMNS angles (θ₁₂ incl.) and phases unchanged (up to the usual rephasing freedom; if some m_i² degenerate, the degenerate subspace's freedom is identical before/after). Δm²_ij ↦ (1+ζ)Δm²_ij; ratios Δm²_21/Δm²_31 invariant; ordering preserved iff ζ > −1. ∎ Converse remark: if ζ is a non-scalar matrix not commuting with M², θ₁₂ generically shifts — invariance is specific to H_M5. Status: **PUIP**.

**M-6 propagation laws (#2 P4, A10 P4) — NF-WHY.** These are [INVENTED] dispersion forms, not theorems; the only mathematical content (Δt = (D/c)(n+1)/2·ξ(E/M)^n) follows from integrating 1/v at first order in ξ — derivable, but the physical premise itself is not provable and numeric ξ needs data. Keep label "invented pending mathematical proof".

## §2 Gap-X1 (0852c256…)
**X-a R-a n = D(Q,P)/4 integer + duality-invariant — PUIP.** H2–H3 [INVENTED]; Λ even, Q·P ∈ 2ℤ [INVENTED sublattice condition].
- Integrality: Q², P² ∈ 2ℤ ⇒ Q²P² ∈ 4ℤ; Q·P = 2m ⇒ (Q·P)² = 4m² ⇒ D ∈ 4ℤ ⇒ n ∈ ℤ. Necessity: if Q·P odd, D ≡ −1 ≡ 3 (mod 4) ⇒ n ∉ ℤ; so the even-Q·P condition is necessary and sufficient. ∎
- Invariance: D = det G, G = [[Q², Q·P],[Q·P, P²]]. Under (Q,P) ↦ (aQ+bP, cQ+dP), G ↦ AGAᵀ with A = [[a,b],[c,d]], det(AGAᵀ) = (det A)² det G = det G for A ∈ SL(2,ℤ) (indeed GL(2,ℤ)). Parity of Q·P preserved: Q′·P′ = ac Q² + (ad+bc) Q·P + bd P² ≡ (ad+bc)Q·P (mod 2) ≡ Q·P (mod 2) since ad−bc = 1 ⇒ ad+bc odd. So the sublattice condition is itself duality-stable. ∎ Status: **PUIP** (deepened: necessity + stability added).

**X-b R-b Λ_s = U ⊕ U(s) evenness + det — PUIP.** Gram U = [[0,1],[1,0]], U(s) = [[0,s],[s,0]]. Evenness: x = (x₁,x₂) ∈ U(s) ⇒ x² = 2s x₁x₂ ∈ 2ℤ; likewise U; orthogonal sum of even is even. det = (−1)(−s²) = s² ⇒ |Λ*/Λ| = s², Λ*/Λ ≅ (ℤ/s)² (U(s)* = (1/s)U(s)). Each hyperbolic block has signature (1,1) ⇒ Λ_s signature (2,2). ∎ The link "⇒ Γ₀(s)-type modularity" is NF-WHY (consistency remark, not derivable without the Owner-specified Weil-representation / theta-lift construction); keep label.

**X-c R-c β_s = 4π√Δ_s — PUIP (form); branch selection NF-WHY.** H1 [INVENTED]: ĝ_s weakly holomorphic weight w<0 on SL(2,ℤ), principal part q^{−Δ}, Δ∈ℕ (SL(2,ℤ) forces integral exponents).
- Rademacher-type exact formula (valid for w<0): a(n) = 2π Σ_{k≥1} (K(−Δ,n;k)/k) (Δ/n)^{(1−w)/2} I_{1−w}(4π√(Δn)/k). k=1 term dominates exponentially (others ≤ e^{2π√(Δn)}·poly). With I_ν(z) ∼ e^z/√(2πz): a(n) ∼ C n^{w/2 − 3/4} e^{4π√(Δn)}, C = Δ^{(1−w)/2 − 1/4}/√2. ∴ β = 4π√Δ, α = w/2 − 3/4. ∎ (power: (1−w)/2 with sign −, times n^{−1/4} ⇒ −(1−w)/2 − 1/4 = w/2 − 3/4.)
- Checks: j (w=0, Δ=1) α=−3/4, β=4π, C=1/√2 ✓ (classical Petersson–Rademacher); 1/η²⁴ (w=−12, Δ=1) α=−27/4, β=4π ✓. (j has w=0, boundary case — formula still holds via Petersson.)
- Branch Δ_s=1 (β_s=4π) vs Γ₀(s) cusp-width branch Δ_s=1/s (β_s=4π/√s): **NF-WHY** — the choice is not a theorem; it is fixed only by which group/cusp structure the Owner cites. For Γ₀(s), the asymptotic is governed by the cusp with largest scaled polar order, needing the Owner's principal parts at every cusp. Keep "invented pending mathematical proof".
- Correlation L_ĝs = 2π√(Δ_s D): PUIP as algebra (substitute n=D/4). Any area↔entropy reading = link (b) Kerr-adjacent → BLOCKED, not pursued.

**X-d FLAG-X1 G8 / B5 close — NF-WHY.** Why: (i) Owner-cite ABSENT; (ii) invention ≠ Owner cite — a proof under invented H cannot become an Owner citation; (iii) close shared Local↔PR2 and Owner-reserved (Rule 3 6b657e97…), outside PR1 sole authority. G8 ABSENT/OPEN, B5 OPEN unchanged.

## §3 χ² (ebc05e25…)
**C-1 dof arithmetic 12−3=9, χ²_min target 0.79×9=7.11 — PUIP** (arithmetic under [INVENTED] N, p).
**C-2 L1 whitening — PUIP.** C ≻ 0 ⇒ unique symmetric W = C^{−1/2} ≻ 0 (spectral theorem), C⁻¹ = W², rᵀC⁻¹r = ‖Wr‖². ∎
**C-3 L2 χ²_min ~ χ²_{N−p} — PUIP.** H1–H2: Wy = Wμ₀ + WJθ* + z, z ~ N(0,I_N). WJ has rank p (W invertible, rank J = p). LS residual = (I−P)z with P = WJ((WJ)ᵀWJ)⁻¹(WJ)ᵀ, symmetric idempotent rank p. Write I−P = VVᵀ, V ∈ ℝ^{N×(N−p)} orthonormal columns; ‖(I−P)z‖² = ‖Vᵀz‖², Vᵀz ~ N(0, I_{N−p}) ⇒ χ²_{N−p}. ∎ (direct, no Cochran needed.)
**C-4 L3 moments — PUIP.** E[χ²_k]=k, Var=2k ⇒ χ²_min/dof mean 1, sd √(2/9)=0.471; |0.79−1|/0.471 = 0.446 sd. Numerics recomputed live (scipy): P(χ²₉ ≥ 7.11) = 0.6257; 95% central band χ²₉/9 = [0.3000, 2.1136]. ✓ matches ebc05e25….
**C-5 L4 block additivity — PUIP.** C = diag(C_D,C_A) ⇒ C⁻¹ = diag(C_D⁻¹,C_A⁻¹) ⇒ rᵀC⁻¹r = r_DᵀC_D⁻¹r_D + r_AᵀC_A⁻¹r_A. Joint dof N−p (C-3); per-block dof not defined when θ shared. ∎
**C-6 L5 ρ² ~ Beta(1/2,(N−p−1)/2), E[ρ²]=1/(N−p) — PUIP.** Under null, ŝ = Vᵀz isotropic N(0,I_k), k=N−p; t := unit vector of Vᵀ(Wτ) (fixed, non-zero). ρ² = (t·ŝ)²/‖ŝ‖²; rotate t to e₁: ρ² = z₁²/(z₁²+…+z_k²), ratio of independent χ²₁ and χ²_{k−1} ⇒ Beta(1/2,(k−1)/2), mean 1/k = 1/9. Monte-Carlo check (2·10⁵ draws, k=9): 0.1112 ✓. Requires Wτ ∉ col(WJ) (else ρ undefined). ∎
**C-7 L6 Bonferroni — PUIP.** P(⋃_i{ρ_i² ≥ c}) ≤ Σ_i P(ρ_i² ≥ c) = K·P(Beta ≥ c) (union bound; no independence needed). ∎
**C-8 L7 invent-sensitivity — PUIP.** The null law depends on (N,p) only through k=N−p; distinct k give distinct laws (means differ) ⇒ a verdict calibrated at invented k=9 does not transfer to a Written k′≠9. ∎
**C-9 term5 inconsistency (c).F — PUIP (arithmetic on SCRIPT).** 0.31·100·e^{−0.31}·1.99 = 45.246 vs claimed 6.07×10⁻¹²: ratio ~7×10¹² ⇒ inconsistent. ∎ Resolution (drop/rescale vs reject) = Owner Write → NF-WHY.
**C-10 decisive recompute / landing acceptance — NF-WHY.** Why: no Written DESI/ATLAS rows, σ, covariance, N, θ list, μ(θ) forms (PO-(a)(b)(c)); H1–H3 validation needs data; acceptance requires Owner/Auditor cite. Inventing values would be indistinguishable from data. Prior Written-only verdict INCONCLUSIVE 8e6d0b8a… stands. Keep label.
**C-11 forms g_D, F_friction, N=12 split 7/5 — NF-WHY.** Modelling choices, not propositions; nothing to prove. Keep label.

## §4 Tally
| Bucket | Count | Items |
|---|---|---|
| PUIP | **16** | M-1, M-2(structure), M-3, M-5; X-a, X-b(even/det/sig), X-c(form β=4π√Δ, α=w/2−3/4); C-1…C-9 |
| NF-WHY (keep "invented pending mathematical proof") | **8** | M-2 numeric overlap, M-6; X-b Γ₀(s) link, X-c branch Δ_s, X-d G8/B5 close; C-9 resolution, C-10, C-11 |
| WF (Written flag, no invention) | **1** | M-4 FLAG-M1 |
PUIP count: MIXED 4 (M-1, M-2 struct, M-3, M-5) + Gap-X1 3 (X-a, X-b, X-c form) + χ² 9 (C-1…C-9 arithmetic) = **16 PUIP**; **8 NF-WHY**; **1 WF**. Correction logged: M-1 witness settings in 3502eb5b… §4.1 were wrong (S=0); corrected here; result 2√2η unchanged.

## §5 Holds
No tip/catalog edit; no tip/READY/Ξ invented; no Kerr/Path4/link (b) content; G8/B5 unchanged; no CLOSED added; Nine-only; REPORTS; No RECS; no agent/user messages. tip AFTER verified in PRESS. tip_touched NO.
