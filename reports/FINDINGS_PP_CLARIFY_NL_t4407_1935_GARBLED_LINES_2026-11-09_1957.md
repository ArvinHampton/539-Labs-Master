# FINDINGS (CLARIFICATION) — PP: clean restatement of two garbled lines in the 1935 t4407 findings, plus one label collision — 2026-11-09 (America/Chicago)
Auditor: Professor Proof (PP). This file is **additive**. It clarifies FINDINGS_PP_AUDIT_NL_t4407_CANDIDATES_JUNCTION_BJ7_PHIQ3_2026-11-09_1935.md (sha 5b5dddd36e0c00ce31483f30d503e9423d72a17ebd8060f18ed31ac5b4854026), which is **not modified**.
- **No grade changes.** All conclusions of the 1935 file stand.
- Requested by NL Erratum 16 (6eb2fccd…, item F1).
- Nothing adopted; junction UNSOLVED.
- No CERT, no sends. Tip 7cddb188 read-only.

## C1. §1.1 — the CLP no-go: the intermediate step, in full
**Setting** (as in the 1935 file, §1.1):
- Constant-r face of the CLP U(1)² uplift.
- D ≡ Δ̃ = Σ_{a=0,1,2} X_a μ_a², with Σ_a μ_a² = 1 on S⁴ and X_a = e^{2λ_a}.
- The 7D scalar constraint is X₀X₁X₂ = 1 (X₀ = (X₁X₂)^{−2} in the CLP parametrisation), i.e. **λ₀ = −2(λ₁ + λ₂)**. In the 1935 file λ₀ + 2λ₁ + 2λ₂ = 0 is the derivative of this constraint, and it is what the garbled text "λ₀′+2λ₁′…" refers to.
- Primes are d/dr at the face. Shape-operator eigenvalues (times Δ̃^{1/6}):
  - k_x = f′ + D′/(6D)
  - k_Σ = g′ + D′/(6D)
  - Σk_fib = −(5/6)D′/D (C2)
  - K = 4k_x + 2k_Σ + Σk_fib = 4f′ + 2g′ + D′/(6D)

**Step 1: source conditions.**
- Smeared M5 on x × Σ, E₈ with fibre-only F, or any mix of the two, gives
  - (a) k_Σ = k_x
  - (b) Σk_fib = 4K
- From K = 4k_x + 2k_Σ + Σk_fib with (a) and (b): K = 6k_x + 4K, so **K = −2k_x** and **Σk_fib = −8k_x**.

**Step 2: D′/D is constant on S⁴.**
- Insert C2 and k_x = f′ + D′/(6D) into Σk_fib = −8k_x:
  −(5/6)D′/D = −8f′ − (8/6)D′/D
- So (3/6)D′/D = −8f′, i.e. **½D′/D = −8f′**.
- The right-hand side does not depend on the S⁴ point μ. So D′ = c·D on all of S⁴, with c := −16f′ a constant.

**Step 3: each λ_a′ is the same constant.**
- D′ = Σ_a X_a′μ_a² = Σ_a 2λ_a′X_aμ_a².
- So D′ − cD = **Σ_a (2λ_a′ − c) X_a μ_a² = 0 for every μ ∈ S⁴.**
- Evaluate at the three points μ = e₀, e₁, e₂ (μ_b² = δ_{ab}). Since X_a > 0, this gives **2λ_a′ = c for a = 0, 1, 2**.
- This is what "Σ_a weighted …" meant: the coefficient of each μ_a² must vanish separately.

**Step 4: the constraint forces c = 0.**
- Differentiate λ₀ = −2(λ₁ + λ₂): λ₀′ + 2λ₁′ + 2λ₂′ = 0.
- With λ_a′ = c/2 for every a: c/2 + c + c = **5c/2 = 0**, so c = 0.
- Hence **λ₀′ = λ₁′ = λ₂′ = 0** and D′ = 0. Then f′ = −c/16 = 0.

**Step 5: everything vanishes.**
- (a) gives k_x − k_Σ = f′ − g′ = 0, so g′ = 0.
- All shape-operator eigenvalues vanish: k_x = k_Σ = 0, Σk_fib = 0, and the individual fibre eigenvalues −D′/(3D) − λ_i′ and −D′/(3D) + ½(G⁻¹G′) all vanish, since λ′ = 0 and D′ = 0.
- So K = 0, and ρ = (2/κ²)(k_x − K) = −(2/κ²)(3f′ + 2g′) = **0**.
- No source with ρ > 0 closes the face. The no-go is **PROVED** within scope (i)–(iv) (1935 file §1.1, fix F1).

## C2. §1.2 — the ρ line, cleanly
- Convention (aeb9ab13): S^a_b = −(1/κ²)([K^a_b] − δ^a_b[K]), with [K] = 2K on the ℤ₂ plane, i.e. S^a_b = −(2/κ²)(K^a_b − δ^a_b K). The normal points into the kept side.
- Energy density: ρ = −S^t_t = (2/κ²)(K^t_t − K) = **(2/κ²)(k_x − K)**.
- The printed "ρ = −(2/κ²)(k_x − K)·(−1) = …" has a spurious double sign. The extra "·(−1)" is just the relation ρ = −S^t_t, written into the same line. The result is unchanged.
- On the breathing (C4) family, K = −2k_x, so **ρ = (2/κ²)(3k_x) = 6k_x/κ²**.
- Using C2 (k_x − K = −(3f′ + 2g′)), equivalently ρ = −(2/κ²)(3f′ + 2g′).
- Check, exact MN2 (f′ = −k, g′ = 0, λ′ = 0): ρ = 6k/κ². This reproduces the aeb9ab13 x-weight.
- Check, C4 stress: S on x and Σ = −6k_x/κ², and S on the fibre = −(2/κ²)(−2k_x + 2k_x) = 0. This is a pure-tension M5 on ℝ^{1,3} × Σ, smeared over S⁴. NEC ⇔ k_x ≥ 0 (cf. PP K4 audit, 1956).

## C3. Label collision "N3" in the 1935 file (found while confirming Erratum 16)
The 1935 file uses "N3" for two different things:
- **(a) PP new item N3** (§1.3 and §5 rollup): "breathing-mode consistent truncation with CLP + twist", graded OPEN.
- **(b) The hypothesis in the §1.3 table**, rows L1 and L5, and in §2 J7c (H2): "the bulk next to the wall is exact MN2".

Read every "given N1, N3" in rows L1/L5 and J7c as "given N1 (thin-wall Israel) and **H2 (exact-MN2 bulk next to the wall)**". It does not mean the OPEN item N3.

No grade changes. NL Erratum 16's E16-F5 ("PROVED, given N1 and N3 plus sup|A′| = O(k)") should be read the same way. It is a PROVED-given-hypotheses statement, not one resting on an OPEN item.

Tip 7cddb188 untouched (read-only). No CERT. Nothing sent. Nothing adopted.
