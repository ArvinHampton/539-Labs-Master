# PP audit: MR2 B1-c2 attempt (d0f833ff) and nits note (e8ac1980), under OW t445u "Open c2" (d64f6fd2)
Written 2026-11-09 2232 CST by Professor Proof. New additive file in reports/ only. Nothing was adopted and nothing was written into MR2's directories. Tip 7cddb188 is unchanged.

## Integrity
- d0f833ffd5c1… = sidecar ✓. e8ac1980b201… = sidecar ✓. OW t445u d64f6fd2ac51… = sidecar ✓, verbatim "Open c2".
- /workspace/mr2-c2-2226/: .py b34e8741… and .log fbe531ca… match their sidecars ✓. Frozen order by mtime (ns): .py 22:26:36.573, .py.sha256 .577, .log .725, .log.sha256 .729 ✓.
- **Stray copies in reports/** (c2_lift_check_2026-11-09_2230.py/.log plus sidecars, 22:27:24/30) are **byte-identical** to the originals (cmp ✓; same shas). They are kept under the never-delete rule. Treat them as duplicates; they are not evidence beyond the originals.
- **PP rerun** of the frozen .py: exit 0, log **byte-identical** to fbe531ca ✓.

## PP independent exact check (/workspace/audit-scratch/pp_c2_2235/pp_c2.py 9ce9d3ed… / log 25664bcd…)
- **Own Cl(10,1).** Recursive Cl(2k) → Cl(10) with s3 tensor-grading (a different construction from MR2's Jordan–Wigner order), Γ₁₁ = i∏Γ (squares to +1), Γ_t = iE₀. All anticommutators are exact in sympy Gaussian-integer matrices ✓. MR2's np.allclose is effectively exact (entries 0, ±1, ±i), but PP's check is symbolic.
- **Every row of MR2's C3 table is reproduced exactly** (det, f*G, bosonic rule, lift², L W̃ L⁻¹, L B_tw L⁻¹):
  - r̃ {u,φ₁}: +1, −G, FAILS, −1, +, +
  - P {φ₂}: −1, −G, holds, +1, −, +
  - **c2 literal {u,φ₁,φ₂}: −1, +G, FAILS, −1, −, +**
  - c2′ {u,φ₁,φ₂,x³}: +1, +G, holds, +1, +, +
  - c2″ {u,φ₁,φ₂,t}: +1, +G, holds, −1, +, +
  - (i) {u,φ₁,x³}: −1, −G, holds, −1, −, +
  - W {ρ}: −1, −G, holds, +1, +, +
  - PP extra row (ii) {u,φ₁,t}: −1, −G, holds, lift² +1, −, +.
- **Why f*G has a uniform sign.** G (bd47ff5e index sets) is built as a sum of terms, each containing exactly one dφ₂ leg (the S² volume of the O(3)_R ℝ³), exactly one of vol_Σ or Dφ₁, and no AdS leg. So f*G = (sign on vol_Σ / Dφ₁)·(O(3) det)·G. For a lift over r this is −det₃(h). ✓ The 8399be55 controls are reproduced.

## Verdicts
1. **Argument (1), bosonic rule, for literal c2 = W×(P∘r̃): PROVED, given the bd47ff5e index sets.** The rule is f*C = det(f)·C, which is needed because C∧G∧G is odd under orientation reversal. Here det = −1 and f*G = +G.
2. **Argument (2), chirality: PROVED** (exact Clifford), given the HW projection Γ_ρε = ε (f825dfff). The lift of any reflection set S ∌ ρ satisfies L Γ_ρ L⁻¹ = (−1)^{|S|}Γ_ρ = det(f)·Γ_ρ. The Pin⁺/Pin⁻ phase choice does not change this, and SO(3)_R/U(1) Spin factors are even and commute with Γ_ρ. For literal c2, the lift anticommutes with W̃.
3. **Twist argument (C1): PROVED** for maps covering r, meaning fibre-preserving maps over r.
   - r*A = −A + dλ, with dA ∝ vol_Σ ≠ 0.
   - φ₁ ↦ φ₁ + λ′ would need dλ′ = 2A, which is impossible. So φ₁ ↦ −φ₁ + λ + c.
   - PP adds a supporting fact: R₁₁ is strictly increasing in μ₁² (PROVED, PP 60293840), and R is an isometry invariant. So every isometry preserves μ₁², and hence the φ₁-circle and the O(3)_R ℝ³ splitting of the fibre. This proves the "fibre split" part of Q1 but **not** all of it: the full fibre isometry group being U(1)×O(3)_R, and G being SO(3)_R-invariant, are still premises.
   - **Answer: yes.** Every isometry over r that preserves the fibration must flip φ₁.
4. **"No other lift rescues c2" (C2/C4): PROVED only as an implication of Q1, and the statement as written is false without a scope fix.**
   - With h ∈ U(1)×O(3)_R×Isom(AdS₅), the bosonic rule f*G = det(f)G is equivalent to **det_AdS(h) = −1** (pp_c2 [gen]).
   - So the lifts that rescue c2 are exactly those composed with an orientation-reversing AdS₅ isometry, and P∘r̃∘Π_{x³} = **c2′ is itself a lift covering r that passes both tests**.
   - MR2's C2 includes "(plus AdS isometries)", so C4's "no choice of lift of r rescues it" is **refuted by the counterexample c2′** unless the lift is required to act on AdS₅ by an orientation-preserving isometry.
   - With that scope, all such lifts fail the bosonic rule (given Q1). The chirality argument does **not** independently exclude the r̃∘SO(3)_R lifts, which commute with W̃.
   - So "two independent ways" holds for the literal map P∘r̃, but over all AdS-orientation-preserving lifts only argument (1) is decisive.
5. **Row 6, B1-c2 literal: REF**, as an implication of the bd47ff5e index sets, plus Q1 for "all lifts", plus f825dfff for the chirality half. It is **scoped to lifts acting on AdS₅ orientation-preservingly**.
6. **C0, the two P's: confirmed.**
   - 425b4e67 §1c writes W×(P∘r) with P the φ₂-parity of §1b, but describes it as "even, orientation-preserving, commutes with W̃", which is 8399be55 (i′)/(ii′) with P = Π_{x³} (dressing rows "(i′) + φ₂ + P", "(ii′) + φ₂ + T").
   - The formula and the description disagree, so splitting the branch into literal / c2′ / c2″ is **fair**.
   - Under t4436: all three are labelled; c2′/c2″ are kept, not dropped; nothing is adopted; the conflict with Group A is a scope conflict ✓. The refutation applies only to the formula-literal reading.
   - **Note:** the Owner opened "B1-c2" with the 0f635774 criterion, and 425b4e67's stated intent is the (i′)/(ii′) content. The register should therefore read: "B1-c2: literal formula REF (AdS-orientation-preserving lifts); intended content = c2′/c2″, open". It should not read "B1-c2 REF" alone.
7. **c2′/c2″ algebraic keep conditions: PROVED (exact).** They pass the bosonic rule, commute with W̃, keep the HW projection, preserve the twist bivector, and flip φ₁ as C1 requires. The bivector Γ_{uvαφ₁} uses α as the μ₁-radial leg; that this is the right twist projector is a frame premise.
   - Pin/Spin existence and descent: **COND** (8399be55 §A premises).
   - Acting as 5D parity labels: **COND** (interpretive).
   - MN2 Killing spinors and E₈ bundle: **OPEN** ✓.
8. **Nits note e8ac1980: faithful.**
   - (a) It restates the 264fdf1d sidecar timing correctly (.py/.py.sha256 22:02:59, .log 22:03:25, .log.sha256 22:08:04, all re-read ✓).
   - (b) It points from the register c5a65972 to 0f635774, with a pointer in the next revision, and points to d0f833ff for c2 ✓. It is additive, with no grade changes ✓.

## Tally
- **MR2: 6/2/1/1 = 10**, plus row 11 ungraded and row 12 UNSOLVED. This is arithmetically correct for MR2's labels.
- **PP grade: PROVED 5 · COND 2 · OPEN 1 · REF 1 = 9**, plus 2 bookkeeping rows (1: the C0 clerical record; 11: the scope note) and the junction UNSOLVED.
  - Row 1 is a textual fact, not a math claim, so it is moved to bookkeeping.
  - Row 3 is PROVED as an implication of Q1, with the AdS scope fix.
  - Row 6 is REF, with the scope stated above.

## Refutation of MR2
- **One sentence is refuted by counterexample:** C4's "By C2 no choice of lift of r rescues it", read with C2's "(plus AdS isometries)". c2′ = P∘r̃∘Π_{x³} covers r and passes both tests.
- No grade flips once the scope "AdS-orientation-preserving lifts" is added.

## Fixes for MR2 (additive)
1. C2/C4: restrict to lifts acting on AdS₅ by orientation-preserving isometries. State that the bosonic rule ⇔ det_AdS(h) = −1, so the rescues are exactly c2′/c2″-type, and that the chirality argument alone does not exclude r̃∘SO(3)_R lifts.
2. Q1: state that μ₁²-preservation (hence the fibre split) is PROVED from R strictly increasing in μ₁² (PP 60293840). The group being U(1)×O(3)_R and G being SO(3)_R-invariant stay premises.
3. Register: write "B1-c2 literal: REF (scoped); intended content = c2′/c2″ (algebra PROVED, Pin/Spin COND, Killing spinor and E₈ bundle OPEN), kept; nothing adopted". Do not write "B1-c2 REF".
4. Tally: move C0 to bookkeeping, giving 5/2/1/1 = 9 + 2 ungraded (PP grade), or keep MR2's 6/2/1/1 and say that row 1 is clerical.
5. Mark the reports/ copies of c2_lift_check as byte-identical duplicates of /workspace/mr2-c2-2226/ (kept, not evidence).
6. C5: name Γ_{uvαφ₁} (α as the μ₁-radial leg) as a frame premise for the twist projector.

**Verdict:**
- B1-c2 literal is REF by genuine proof: argument (1) given the index sets, and argument (2) given HW. "All lifts" holds as an implication of Q1, once scoped to AdS-orientation-preserving lifts.
- c2′/c2″ algebra is PROVED exactly; both are kept; nothing is adopted.
- The nits note is faithful.
