# PP audit: MR2 c2 erratum (7b8160bf) and c2′ Killing-spinor attempt (8e766c4c)
Written 2026-11-09 2244 CST by Professor Proof. New additive file in reports/ only. Nothing adopted. Nothing written into MR2's directories. Tip 7cddb188 unchanged.

## Integrity
- 7b8160bf8193… matches its sidecar ✓. Its header says "≈22:40" but the true write time (mtime) is **22:35:58**; noted, cosmetic.
- 8e766c4c51e4… matches its sidecar ✓ (mtime 22:41:19).
- /workspace/mr2-c2ks-2234/: all 10 sidecars match.
  - v3 .py is f0aa2e12…; its sidecar (22:39:33) predates the log 079c41a8… (22:39:47) ✓.
  - v1 (ca015838/0864b05a), v2 (3655a659/d7b758bc) and debug (7dccd49f/b57d274f) are superseded and support no claim ✓.
- mn.pdf is **770d87d8…** ✓. (mn.txt, eab276d8…, is the raw pdftotext output and is not cited.)
- **PP rerun** of frozen v3: exit 0, log **byte-identical** to 079c41a8 ✓.

## Part 1. Erratum 7b8160bf, per PP 7f366e78
1. **Fix 1: faithful in substance.**
   - The refuted sentence is withdrawn, and "bosonic rule ⇔ det_AdS(h) = −1" is stated.
   - Wording nit: the scoped claim says lifts "with an odd O(3)_R part" fail. In fact **every** AdS-orientation-preserving lift fails the bosonic rule, whatever the O(3)_R parity. MR2's parenthetical covers the even case, but the main sentence should say "every lift".
2. **Fix 2 (μ₁² preservation PROVED; rest of Q1 a premise): faithful.**
3. **Fix 3 (register wording): faithful.**
4. **Fix 4 (tally 5/2/1/1 = 9 plus 2 bookkeeping rows): faithful.**
5. **Fix 5 (duplicates): faithful.**
6. **Fix 6 (Γ_{uvαφ₁} frame premise): faithful.** It is superseded by the MN projectors in Part 2.

## Part 2. c2′ Killing-spinor attempt 8e766c4c
- **T1 (re-typing of MN (90)–(92)): CONFIRMED against the PDF.**
  - PP ran pdftotext -layout on 770d87d8 (pp. 32–33). The layout shows every coefficient and structure MR2 typed:
    - (90): k/2 (A¹Γ¹² + A²Γ³⁴); (m/4)e^{−4(λ₁+λ₂)}γ_μ; ½γ_μγ^ν∂_ν(λ₁+λ₂); ½γ^ν(e^{−2λ₁}F¹Γ¹² + e^{−2λ₂}F²Γ³⁴)
    - (91)/(92): (m/4)(e^{2λᵢ} − e^{−4(λ₁+λ₂)}); −¼γ^μ∂_μ(…); −⅛γ^{μν}e^{−2λᵢ}F^iΓ
  - (93): ω_x^{xy} = −1/y, ω_u^{ur} = f′ ✓.
  - (99): γ_rε = ε, γ_xyε = iε, Γ¹²ε = iε ✓, which gives γ_xyΓ¹²ε = −ε ✓.
  - The equations themselves are MN's citation of Liu–Minasian. K1 is therefore an **implication of the cited 7D KSE**, now with a PP-confirmed transcription.
- **K1: PROVED (implication).** Rerun identical:
  - all 9 KSEs vanish on Π (rank 8);
  - k = 4 is unique, matching MN's 1 = 4(a+b) with a = ¼;
  - each projector is necessary (dropping the twist projector breaks x, y, λ1; dropping γ_r breaks t, u, v, z, r).
- **K2: PROVED.** By PP hand arithmetic at (25), with λ₁ = −3λ/2 and e^{5λ} = 2:
  - e^{−4(λ₁+λ₂)} = e^{2λ₂} = 2^{2/5} and e^{2λ₁} = 2^{−3/5};
  - so W³ = 2^{2/5}(1 − μ₂²/2), which is our Δ with MN's μ₂ = our μ₁ ✓.
- **K3: PROVED.** PP's own Cl(1,6)⊗Cl(5) (recursive build, exact; pp_lift.py 00e1d2b3 / log c0d8fe10) gives:
  - L = γ_xγ_z⊗Γ²Γ⁴ satisfies LΠL⁻¹ = Π and Lγ_rL⁻¹ = γ_r. Ad_L on (Γ³⁵, Γ³⁴, Γ⁴⁵) is (+, −, −), a rotation by π about X⁴. L² = +1.
  - L′ = (Γ³⁵)⁻¹L commutes with so(3)_R and with Π, and L′² = −1.
  - On range(Π) (dim 8), L′ has charpoly (λ² + 1)⁴, so eigenvalues ±i with multiplicity 4 each ✓.
  - Building-block signs under L: γ_x, γ_z → −; all other γ_a → +; Γ¹², Γ³⁴ → −. These match the mirrored covariance s_μ (x, z odd) and the invariance of the twist term (A¹Γ¹² with A¹ odd under x ↦ −x).
  - The full-operator covariance rests on MR2's exact frozen run (rerun byte-identical). Its test (L O_μ L⁻¹ = s_μ O_μ, with the background independent of x and z) is a correct criterion.
  - Γ³⁴ → − is harmless only because b = 0 (A² = F² = 0). Note this as a restriction of K3 to the b = 0 fixed point.
- **Controls: PROVED** (PP reproduces). Both P∘r̃ = γ_x⊗Γ²Γ⁴ and r̃ = γ_x⊗Γ² flip γ_r and do not preserve Π.
- **K4 (11D): COND** on D1 (Cvetič et al. 9903214; Nastase–Vaman–van Nieuwenhuizen), which is cited and not re-derived. Given D1, c2′ preserving the KS up to SU(2)_R is **PROVED (implication)**. The image check, 7D L = 11D Γ_uΓ_{φ₁}Γ_{φ₂}Γ_{x³} (u = Σ coordinate, z = x³), is consistent ✓.
- **K5:**
  - SM compatibility: **COND** (fair).
  - c2″ unitary part γ_xγ_t⊗Γ²Γ⁴: **PROVED** (Π kept, γ_r kept, L² = −1; PP reproduces). The antiunitary T step is **OPEN** ✓.
  - E₈: N and 2N preserved is **PROVED (implication)**. c2′ reflects two directions of ℝ⁵ (det +1, S⁴ orientation kept), and f*G = +G (d0f833ff, PP-verified). The bundle lift is **OPEN** ✓.

## Tally
- **MR2: 8/2/2/0 = 12 plus 1 bookkeeping row.** This is arithmetically correct (PROVED rows 1, 2, 3, 4, 6, 8, 10, 11; COND 5, 7; OPEN 9, 12).
- **PP: agrees, 8 PROVED · 2 COND · 2 OPEN · 0 REF = 12** plus bookkeeping; junction UNSOLVED.
  - Row 1 is graded as an implication of the cited KSE, with the transcription confirmed.
  - Row 3 is restricted to b = 0.

## Refutation
None.

## Fixes (additive)
1. Erratum fix 1: "every AdS-orientation-preserving lift fails the bosonic rule", not "with an odd O(3)_R part".
2. Erratum header time ≈22:40 → 22:36 (mtime 22:35:58).
3. 8e766c4c T1: record "PP-confirmed against pdftotext -layout of 770d87d8". K1 is an implication of the cited KSE (MN (90)–(92), via Liu–Minasian).
4. K3: state the restriction to b = 0 (Ad_L flips Γ³⁴, so covariance would fail for A² ≠ 0).

**Verdict:**
- Erratum 7b8160bf: faithful, with one wording nit.
- c2′ KSE: confirmed. B1-c2′ is COND overall (D1 COND; Pin/Spin COND; E₈ bundle OPEN), and B1-c2″ is COND/OPEN.
- Not adopted.
