# FINDINGS — PP Soft SF — DERIVED DEFINITIONS: D1-norm (Layer2) and S_eff (conditional T3) — 2026-11-09
Professor Proof (PP). REPORTS ONLY. No CERT. Pure mathematics only. Nothing sent to Gemini, the web, or any outside service. No message to any agent from this file.
Labels: PROVED, CONDITIONAL, OPEN, REFUTED-by-proof. Undefined = OPEN, never "refuted". Every definition below is a **DERIVED PROPOSAL (pending Owner adoption)**; every result that uses one is **CONDITIONAL** on it even when its proof is complete. Results about already-written objects that do not use the proposals are labeled PROVED.

## 0. Header

### 0.1 Authority (sha256 verified live before write)
| Role | File | sha256 (prefix) |
|---|---|---|
| Write-and-derive grant (Owner voice ~1:00 PM CST, transcribed by Physicist) | OWNER_WRITE_CALL_e9c1dbda_WRITE_DERIVE_AUTHORIZATION_2026-11-09_1300.md | 33d25a79 MATCH |
| D₁ / S_eff LOCK (respected, not altered) | OWNER_WRITE_LOCK_D1_Seff_Layer2_T3_2026-11-03.md | 96f8d42e MATCH |
| Locked attach text | /workspace/reports/539labs/ow/ATTACH_Layer2_T3_specs_LOCKED_t3511u_a71f388e.txt | a71f388e MATCH |
| RTA v16 (FROZEN; read only) | reports/papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v16.pdf | 1fe7b8a2 MATCH sidecar |
| tip (BEFORE write) | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188 MATCH — tip_touched NO |

Grant limits honored: additive write only (this new file + sidecar); no existing file modified; RTA v16 and tip untouched; no CERT; no outside service.

### 0.2 Sources (read for this file)
- [L] Lock 96f8d42e…: L12–16 (decision §1 D₁, §2 S_eff, §3, §4 "Kronecker / physical mappings stay PURGED").
- [A] Attach a71f388e…: L8–11 (§1 D₁: domain, class isolation, rank-1, boundary disjointness), L15–21 (§2 S_eff: static budget, error containment, disjoint M, attractor boundary), L27 (physical mappings PURGED).
- [R] RTA v16 (pdftotext): Thm 41.10 (D₁ = "the ℚ-linear functional on H²(F) that isolates the line ℚ·[s_αδ]"; (ii) no temporal/schedule/metric argument; (iii) no shared data with resonant counters; (iv) Layer 2 not constructed), Prop 41.11 (S_eff "defined by the following constraints" (i)–(iv)), Prop 41.12, Prop 41.13(ii), Prop 42.6, Rem 42.7 (carrier O_res = {21+9j : 0≤j≤538}).
- [P] PAPER_RESIDUAL_TERNARY_ALGEBRA_BRIDGE_C_2026-11-03.md (23931ee8…): Def 2.1 (L41), Def 2.7 (L105), Thm 2.9 (L121), Cor 2.10 (L141), Prop 2.12 (L157), Prop 3.1 (L178), L187 (ln(2/3) heuristic, "typical depth ~14 … empirical"), Thm 3.4 (L197), Def 4.1 (L225), L237 (Layer 2 not constructed), Def 4.4 (L239), Prop 4.5 (L243).
- [AU] bridges/AUDITOR/AUDITOR_CORPUS_CRAWL_BATCH07_DEPENDENCY_CLOSURE_2026-11-09.md (1a48abce…) §3: generator model G with Ds = Dt_ωf = ω₂⊗δf; H²(F) ≅ ℚ is the connecting-map image of the deleted class ω₂⊗δf; "~14" B6-4 CONDITIONAL/OPEN.
- [PP1] FINDINGS_PP_SOFTSF_LAYER2_T3_FORMULATE_PROVE_06748ff2_2026-11-05.md (f90e8e61…): L2-D1, PP-L2-1..3, T3-REF, PP-T3-1..3, C-T3-stress-energy REJECTED (L168–169).
- [PP0] FINDINGS_PP_SOFTSF_LAYER2_T3_PROOF_RESUME_GAP_a0c2ed5a_2026-11-05.md (0ac13428…): both items IDLE pending definitions.
- [D1-old] OWNER_WRITE_D1_D2_DEFS_LOCKED_2026-10-26.md (6fba7717…) L15–16; FINDINGS_LOCAL_D1_NORM_IDENTIFICATION_PATH4_2026-10-26.md (f8c95f7c…) L5, L36–40; FINDINGS_LOCAL_D1_NORM_ID_CITE_GROUNDED_2026-10-26.md (2e570d62…) L53–62; FINDINGS_LOCAL_D1_NORM_LAYER2_TRANSFER_2026-10-26.md L5, L44–53; ASSIGN_LOCAL_D1_NORM_LAYER2_TRANSFER_BEGIN_2026-10-26.md L9 (no free algebraic map n=A, n=A/4, n∝A).
- [t61] tubulin-torsion/PROOF_T3_STRESS_ENERGY.md (7be4da98…) row 2: T^{αβγ} ≡ (2/√−g) δS_eff/δK_{αβγ}, "S_eff and K_{αβγ} not defined on disk".
- Checked, no D1/S_eff usage: tubulin-torsion/PROOF_LAMBDA22.md, PROOF_WILSON_C1_CLOSED_FORM_2026-11-03.md, PP-FINDINGS-CATA_FOOLPROOF_RERUN_OW9aec847a_2026-11-03.md (Cat A READY stays = Local F1–F3 cite-lifts; unchanged here).
- Homonym noted, not used: "D1" in FINDINGS_EIGEN_PACK_I_D1_D3_REVIEW_2026-11-05.md = descent blocker ℚ(ζ₄₉)→ℚ (unrelated).

### 0.3 Verification
All numeric/symbolic claims below were checked by `/workspace/audit-scratch/pp_dp_1109/verify.py` (sha 85e00254…; output verify_out.txt sha 960eec9f…) with sympy/exact integer arithmetic, plus a one-line check of L(3^600)=600 and the R/S counterexamples.

---

## (a) D1-norm for the Layer2 D1-norm attempt

### a.1 Usage conflict and options
| Option | Meaning of "D1-norm" | Source | Status of usage |
|---|---|---|---|
| **a-I (10-26 Path4)** | Normalization making L_ĝs = β_s√n comparable with A/4, i.e. an n ↔ A (horizon area) identification | [D1-old]: D1 = Bekenstein–Hawking A/4 target (6fba7717 L16); D1-norm ID ABSENT (f8c95f7c L5, L40) | Superseded for Layer2 by Lock 96f8d42e §1/§3 (D₁ redefined); requires a free n↔A map (forbidden by ASSIGN L9) and a physical/continuum map (PURGED, Lock §4, [A] L27, RTA Prop 41.13(ii)) |
| **a-II (11-03 lock, chosen)** | Fix the scalar left free by Thm 41.10 ("the" functional isolating ℚ·[s_αδ] is only defined up to ℚˣ, PP-L2-1) and take the induced absolute value | [R] Thm 41.10; [P] Cor 2.10; [AU] §3 | Consistent with lock: D₁ itself gets no new argument |
| a-III | A norm on the ambient cycle space (rank β₁ = 19396 ≈ "N≈20,000") | [A] L10; [P] Thm 2.6 | Rejected: lock says the rank-1 core "does not alter" the ambient space; no D₁ data reaches it |

**Pick: a-II.** Reasons: (1) it is the only option whose referent is Owner-locked as Layer2's D₁ (Lock L13, L15); (2) it needs no input the lock forbids (no time, schedule, metric, Λ₀, resonant counter); (3) it fills the single genuine gap in Thm 41.10, the free scalar. a-I is not refuted; it remains OPEN/ABSENT exactly as the 10-26 files record.

### a.2 DEFINITION DP-a — DERIVED PROPOSAL (pending Owner adoption)
Let F be the thin residual form complex of [P] Def 2.7 / [R] §41.7, with F² basis (t_ω, s_αδ, t_ωf) after eliminating t_μ = −B′t_ω, and D¹: F¹→F² given by Dh_α = t_ω, Dv_δ = 0, Dh_αf = t_ωf − s_αδ.
1. **Normalized classifier.** D̂₁ : F² → ℚ is the unique ℚ-linear map with D̂₁(im D¹) = 0 and D̂₁(s_αδ) = 1. Equivalently D̂₁(z) = λ where z = λ s_αδ + Dw ([P] Cor 2.10).
2. **D1-norm.** ‖z‖_{D1} := |D̂₁(z)| (archimedean absolute value on ℚ), z ∈ F²; it descends to H²(F).

The absolute value is applied to the **output** of D₁ (a rational number), not given as an argument to it. D₁ still has domain the static charge-sector data only (Thm 41.10(ii), Lock §1).

### a.3 Statements and proofs
**a-L0 (PROVED; does not use DP-a).** If z = a t_ω + b s_αδ + c t_ωf, then the coefficient λ(z) of [P] Cor 2.10 is λ(z) = b + c. In particular λ(t_μ) = λ(t_ω) = λ(η) = 0 and λ(s_αδ) = λ(t_ωf) = 1, where η = s_αδ − t_ωf.
*Proof.* im D¹ = ⟨t_ω, t_ωf − s_αδ⟩. Write z = a·t_ω + c·(t_ωf − s_αδ) + (b + c)·s_αδ. The first two terms lie in im D¹, and s_αδ ∉ im D¹ ([P] Thm 2.9), so λ = b + c is unique. t_μ = −B′t_ω gives 0, and η gives 1 − 1 = 0. ∎ (sympy: solving φ·D¹ = 0, φ(s)=1 gives φ = (0,1,1).)

**a-L1 (PROVED; does not use DP-a).** Let G be the generator model with G³ = ℚ·u, u = ω₂⊗δf, and D²_G(t_ω) = 0, D²_G(s_αδ) = D²_G(t_ωf) = u ([AU] §3; [P] proof of Thm 2.4). Then for every z ∈ F², D_G z = λ(z)·u. Hence H²(G) = H³(G) = 0, and λ is exactly the connecting isomorphism H²(F) → H³(G³) = ℚ·u of 0 → G³ → G → F → 0, read in the basis u.
*Proof.* D_G(a t_ω + b s + c t_ωf) = (b + c)u = λ(z)u by a-L0. ker D²_G = {b + c = 0} = im D¹, so H²(G) = 0. D²_G is onto ℚu, so H³(G) = 0. The connecting map lifts a class [z] ∈ H²(F) to z ∈ G² and applies D_G. ∎ (sympy: D²_G = (0,1,1) = φ; D²_G·D¹ = 0.)

**a-1 (CONDITIONAL on DP-a; proof complete). Canonical normalization.** D̂₁ = λ. It is the unique functional allowed by Thm 41.10 with D̂₁(s_αδ) = 1. Two characterizations that use no metric data also single it out: (i) it is the unique such functional with D̂₁(F²_ℤ) = ℤ and D̂₁(s_αδ) > 0, where F²_ℤ = ℤ-span of the generators; (ii) it is the connecting-map coefficient of a-L1.
*Proof.* Every functional allowed by Thm 41.10 is c·λ with c ∈ ℚˣ (PP-L2-1). The condition D̂₁(s)=1 forces c = 1. For (i): λ has coefficients (0,1,1), so λ(F²_ℤ) = ℤ (gcd 1). Since (cλ)(F²_ℤ) = cℤ, we need c = ±1, and positivity on s gives c = 1. For (ii), see a-L1. ∎
Caveat: the sign depends on the orientation convention α(a,b) = sgn(a − b) ([P] L69). The norm ‖·‖_{D1} does not depend on that sign.

**a-2 (CONDITIONAL on DP-a). Norm properties.** ‖·‖_{D1} is a seminorm on F² with kernel im D¹ = B²(F). It descends to a norm on H²(F) ≅ ℚ, and [z] ↦ D̂₁(z) is an isometry (H²(F), ‖·‖_{D1}) → (ℚ, |·|). Values: ‖t_μ‖ = ‖t_ω‖ = ‖η‖ = 0 and ‖s_αδ‖ = ‖t_ωf‖ = 1.
*Proof.* This is the absolute value composed with a linear functional whose kernel is B² (a-L0). It is a norm on the quotient because D̂₁ is injective on H² = F²/B². Values come from a-L0. ∎

**a-3 (CONDITIONAL on DP-a). Staticity and lock compliance.** D̂₁ and ‖·‖_{D1} do not depend on B′, the tower labels f (beyond the standing condition that f is nonconstant, which [AU] verified: 241 of 538 δf ≠ 0), the resonant data (W, b), or any time, schedule, metric or Λ₀ variable.
*Proof.* B′ enters F only through t_μ = −B′t_ω, which lies in the kernel (a-L0; sympy confirms with B′ symbolic). The formula b + c involves only basis coordinates. W and b do not occur in F at all ([P] Thm 3.4(c), Prop 4.3). ∎

**a-4 (CONDITIONAL on DP-a). Thin-truncation only.** The D1-norm vanishes identically on the cocycles Z²(G) of the untruncated generator model, and there is no nonzero D1-norm on H²(G) = 0. Thus the D1-norm is an invariant of the thin truncation, consistent with [P] Prop 2.12 and [AU] §3 item 2.
*Proof.* Z²(G) = ker D²_G = {b + c = 0} = ker D̂₁ (a-L1). ∎

**a-5 (OPEN). Layer2 D1-norm → Kerr area A transfer.** DP-a gives "D1-norm" a referent. If DP-a is adopted, this supersedes reason 1 of PP-L2-2 ([PP1] L78: "D₁-norm has no referent"). PP-L2-2 reasons 2 and 3 still stand. The D1-norm takes values in ℚ_{≥0} on a single line and carries no data beyond that one scale. Any map to an astrophysical or SUSY horizon area therefore needs inputs that Lock §1 excludes (metric) or §4 purges (physical/continuum maps). Links (a) n ↔ charge index and (b) SUSY area ↔ Kerr area remain ABSENT ([D1-old] transfer file L44–53). Status: **OPEN, not refuted.** No free map (n = A, A/4, ∝A) is proposed.

### a.4 Owner adoption needed for (a)
Adopt DP-a (the normalization D̂₁(s_αδ) = 1, equivalently the connecting-map or primitive-integral normalization, plus ‖·‖_{D1} = |D̂₁|) as the Layer2 D1-norm. Confirm that this does not count as a "metric normalisation" argument under Thm 41.10(ii). (PP's reading: it does not, because the absolute value acts on D₁'s output.)

---

## (b) S_eff for the conditional T3

### b.1 Usage conflict and options
| Option | Meaning of S_eff | Source | Status |
|---|---|---|---|
| b-I (t61, 10-31) | Effective action functional with T^{αβγ} = (2/√−g) δS_eff/δK_{αβγ} (ternary stress-energy) | [t61] row 2 | Never defined on disk. The symbol was later Owner-locked to a different object (Lock L14, L15). The continuum/physical reading is PURGED (Lock §4, [A] L27, RTA Prop 41.13(ii)). [PP1] L168–169 already rejected it. **Not used.** |
| **b-II (11-03 lock, chosen)** | Static packaging structure: T₃ = 539 cell capacity / hash budget; M onto Residual₅₃₉ × Resonant₅₃₉ with disjoint factors; no global Ω ≡ 0 (mod 539); attractor boundary = free-map depth | [L] L14; [A] L15–21; [R] Prop 41.11; [P] Def 4.4 | RTA defines S_eff only "by constraints" and gives no carrier. That missing carrier is the gap filled here. |
| b-III | S_eff := the ℤ₃ dynamical system (T3, Haar) | [R] Prop 42.6(iii) | Rejected as S_eff itself. The lock calls 539 non-dynamical and treats the free map only as a boundary. It is kept as a component (DP-b item 4). |

**Pick: b-II.** Reasons: the symbol S_eff is Owner-locked (96f8d42e §2) and RTA v16 uses it; b-I would overwrite a locked definition and restore a purged mapping, which the e9c1dbda grant does not authorize. "Kerr UNLOCKED" (Lock L5) does not lift §4.

Options for the undefined Ω ("packaging remainder", Prop 41.11(ii)):
- Ω₁ = (N − f) mod k = 8 (the remainder of the very division defining B′).
- Ω₂ = N − 9B′ = 29 ([P] Prop 2.2(b)).
- Ω₃ = 2 ([P] Prop 4.5, attached to a ℤ[ℤ/3] configuration whose winding functional is undefined).

**Pick Ω₁**, because it is the remainder of the packaging division R = 9B′ + Ω. Results b-2 hold for all three.

### b.2 DEFINITION DP-b — DERIVED PROPOSAL (pending Owner adoption)
Parameter sets P_res = ℕ³ ∋ p = (N, f, k) with k ≥ 1 and N ≥ f, and P_ron = ℕ² ∋ q = (W, b).
1. **S_eff := (p₀, q₀) ∈ P_res × P_ron** with p₀ = (N_flux, f_max, 9) = (4880, 21, 9) and q₀ = (W, b) = (18, 521) ([P] Def 2.1, Def 3.2).
2. **M = M_res × M_ron.** M_res(N,f,k) := O_res(p) = {f + kj : 0 ≤ j < R(p)} with R(p) = ⌊(N − f)/k⌋ (static cells). M_ron(W,b) := {1, …, W + b} (counter set). Residual₅₃₉ := M_res(p₀) = O_res = {21 + 9j : 0 ≤ j ≤ 538} (agrees with RTA Rem 42.7). Resonant₅₃₉ := M_ron(q₀).
3. **Packaging remainder** Ω(p) := (N − f) mod k.
4. **Attractor boundary** d_free := L(N_flux), where L(n) = min{t : T3^t(n) ∈ {0,1}} ([P] Thm 3.4) and T3(3k)=k, T3(3k+1)=4k+2, T3(3k+2)=2k+1.
5. Dual-rail: hardware-only, with no algebraic role (Lock Flag 2, Prop 41.11(iii)).

### b.3 Statements and proofs
**b-L0 (PROVED; arithmetic).** N_flux = ⌊243e³⌋ = 4880, f_max = ⌈4880/243⌉ = 21, R = 4859 = 9·539 + 8, N − 9B′ = 29, W = ⌊e³/ln 3⌋ = 18, 539 = 7²·11, |O_res| = 539, and max O_res = 4863 ≤ 4880. (Exact computation, verify.py.) ∎

**b-1 (CONDITIONAL on DP-b). Disjoint mapping.** M is a product map: pr_res∘M depends only on p and pr_ron∘M only on q. Neither of the integers R(p), S(q) := W + b determines the other: R(4880,21,9) = S(18,521) = 539, but S(18,522) = 540 while R is unchanged, and R(4889,21,9) = 540 while S is unchanged. The two factors share only the cardinality 539, which is an equality of values, not a structure map (RTA Prop 41.12).
*Proof.* By construction (DP-b.2). The counterexamples were computed exactly. ∎

**b-2 (CONDITIONAL on DP-b). No global Ω ≡ 0 (mod 539).** For every p, Ω(p) ∈ {0, …, k−1}. If k ≤ 539, then Ω(p) ≡ 0 (mod 539) ⇔ Ω(p) = 0 ⇔ k | (N − f). At the locked data Ω(p₀) = 8 ≢ 0 (mod 539). Over N ∈ {4880, …, 4888} with f = 21, k = 9, Ω takes every value 0…8 exactly once, so Ω ≡ 0 is neither guaranteed nor excluded globally. The alternative readings give Ω₂ = 29 and Ω₃ = 2, both ≢ 0 (mod 539). This realizes Prop 41.11(ii) by an explicit counterexample.
*Proof.* Division with remainder; values computed. ∎

**b-3 (PROVED; about T3 only). 539 is not a stopping time.** For every m ≥ 0, L(3^m) = m. In particular L(3^600) = 600 > 539, so no uniform 539-step bound holds on ℕ. Also L(N_flux) = 14, with orbit 4880→3253→4338→1446→482→321→107→71→47→31→42→14→9→3→1 (matches [P] Prop 3.1(a)).
*Proof.* T3(3k) = k, so T3^j(3^m) = 3^{m−j}, and 1 is first reached at j = m. The 4880 orbit and L(3^600) = 600 were computed exactly. ∎

**b-4 (PROVED; about T3 only). Haar itinerary and Lyapunov exponent ln(2/3).** (i) For every L ≥ 1 and every word w ∈ {0,1,2}^L, the set {x ∈ ℤ₃ : (T3^j(x) mod 3)_{j<L} = w} is exactly one residue class mod 3^L. Hence under Haar measure μ the itinerary digits are i.i.d. uniform on {0,1,2} (an independent proof of the cylinder part of RTA Prop 42.6(iii)). (ii) Put c(0) = 1/3, c(1) = 4/3, c(2) = 2/3. Then T3(x) = c(r)x + ε_r with ε ∈ {0, 2/3, −1/3}. For μ-a.e. x, (1/n)Σ_{j<n} ln c(r_j(x)) → (1/3)ln(8/27) = ln(2/3). Exactly, for every L, the average of Σ_{j<L} ln c(r_j) over n ∈ ℤ/3^L equals L·ln(2/3).
*Proof.* (i) By induction on L. Write x = 3k + r. Then T3(x) = a_r k + b_r with a_r ∈ {1, 4, 2}, a unit in ℤ₃. The itinerary of x is r followed by the itinerary of T3(x). By induction T3(x) lies in a single class mod 3^{L−1}; because a_r is a unit, that holds iff k lies in a single class mod 3^{L−1}, iff x lies in a single class mod 3^L. Each class has μ-measure 3^{−L}, which gives i.i.d. uniform digits. (ii) The strong law of large numbers applied to the i.i.d. variables ln c(r_j), with mean (ln(1/3) + ln(4/3) + ln(2/3))/3 = ln(2/3) (sympy: exact). The finite identity follows from (i), because each word occurs exactly once mod 3^L (checked exhaustively for L ≤ 8). ∎

**b-5 (CONDITIONAL on DP-b). Attractor boundary.** d_free = L(N_flux) = 14 < 539 = |Resonant₅₃₉|. So the 539-step schedule run from N_flux overruns the free orbit by 525 steps, and T3^{539}(4880) = 2 (the {1,2} 2-cycle). This makes the lock's "external constant-time override" precise: the endpoint is fixed by the parity of 539 − d_free, not by any residual datum.
*Proof.* b-3, plus T3(1) = 2 and T3(2) = 1. 525 is odd, so the orbit ends at 2 (computed exactly). ∎

**b-6 (PROVED; finite computation). Orbits for small n.** For every 1 ≤ n ≤ 10⁶ the T3 orbit reaches 1, with max L(n) = 87 (first attained at n = 481780) < 539. On [1, 50000], max L = 55, attained exactly at 36043 and 36592 (matches [P] Prop 3.1(c)).
*Proof.* Exhaustive exact iteration (verify.py). ∎

**b-7 (CONDITIONAL on DP-b). Ternary stress-energy has no referent.** Under DP-b, S_eff is an element of P_res × P_ron, which is a discrete set of integer tuples, together with maps between finite sets. It is not a functional on any space of tensor fields K_{αβγ}. So δS_eff/δK_{αβγ}, and with it the t61 expression T^{αβγ} = (2/√−g)δS_eff/δK_{αβγ}, is not defined.
*Proof.* A functional derivative needs S_eff to be a differentiable map on a space of fields. DP-b supplies no field argument. ∎

**b-8 (OPEN). Conditional T3 "ternary stress-energy".** b-7 shows it is not definable from the locked or derived S_eff. It is **not refuted**. Defining it would require a new, separately named action functional together with a lift of the §4 purge (see b.4).

**b-9 (OPEN). "Typical depth ~14".** [P] L19 calls ~14 "the typical depth of the free basins", and L187 calls it empirical. Exact computation gives median L = 21 on [1, 50000] and median 28, mean 29.30 on [1, 10⁶]. The Lyapunov heuristic ln n / ln(3/2) gives 20.95 at n = 4880. So ~14 is supported only as the exact value L(4880), which is what DP-b.4 uses, and not as a typical depth. Because "typical ~14" has no precise statement, this is OPEN (not refuted), consistent with [AU] B6-4.

**b-10 (OPEN). Global reach.** Whether every n ∈ ℕ reaches {0} or the {1,2} cycle is Collatz-type. It is checked only for n ≤ 10⁶ (b-6) and is not claimed beyond that (RPP §1.4 item 6; [PP1] gap 6).

### b.4 Owner adoption needed for (b)
1. Adopt DP-b as the carrier of the locked S_eff: (p₀, q₀), M = M_res × M_ron with Residual₅₃₉ = O_res and Resonant₅₃₉ = {1..539}, Ω := (N − f) mod k (or name Ω₂ or Ω₃ instead), and d_free := L(N_flux) = 14.
2. For a ternary stress-energy T3 (b-8) to become provable, the Owner would need to: (i) name a new symbol (not S_eff, which is locked); (ii) explicitly lift Lock §4 / RTA Prop 41.13(ii) for this item; (iii) supply the field content (metric g, 3-index field K_{αβγ}, index ranges) and a Lagrangian density. None of these is proposed here.

---

## Rollup
| # | Result | Label |
|---|---|---|
| a-L0 | λ(z) = b + c on F² | PROVED |
| a-L1 | λ = connecting map H²(F) → H³(G³); H²(G) = H³(G) = 0 | PROVED |
| a-1 | Canonical normalization D̂₁ (three equivalent characterizations) | CONDITIONAL (DP-a) |
| a-2 | ‖·‖_{D1}: seminorm on F², norm on H²(F), isometric to ℚ | CONDITIONAL (DP-a) |
| a-3 | Staticity: independent of B′, f, W, b, time, metric | CONDITIONAL (DP-a) |
| a-4 | Vanishes on Z²(G); thin-truncation-only | CONDITIONAL (DP-a) |
| a-5 | D1-norm → Kerr area transfer | OPEN |
| b-L0 | Packaging arithmetic | PROVED |
| b-1 | Disjoint product M; neither of R, S determines the other | CONDITIONAL (DP-b) |
| b-2 | Ω(p₀) = 8 ≢ 0 (mod 539); no global guarantee | CONDITIONAL (DP-b) |
| b-3 | L(3^m) = m, so 539 is not a stopping time; L(4880) = 14 | PROVED |
| b-4 | Haar i.i.d. itinerary; Lyapunov ln(2/3) a.e. and exact average | PROVED |
| b-5 | d_free = 14; T3^539(4880) = 2 (parity override) | CONDITIONAL (DP-b) |
| b-6 | n ≤ 10⁶ all reach 1, max L = 87 | PROVED |
| b-7 | δS_eff/δK has no referent under DP-b | CONDITIONAL (DP-b) |
| b-8 | Ternary stress-energy T3 | OPEN |
| b-9 | "Typical depth ~14" | OPEN |
| b-10 | Global reach of T3 orbits | OPEN |

**Totals: PROVED 6 · CONDITIONAL 8 · OPEN 4 · REFUTED 0.**

## Explicit non-claims
- No CERT. RTA v16 not modified. tip 7cddb188 not touched; tip AFTER is re-verified in the sidecar step.
- No physical, Kerr, four-forces, SU(3), Kronecker or continuum map is restored (Lock §4).
- No free n ↔ A map. Cat A READY is unchanged (Local F1–F3 only).
- DP-a and DP-b are proposals only. Nothing becomes locked until the Owner adopts it.
