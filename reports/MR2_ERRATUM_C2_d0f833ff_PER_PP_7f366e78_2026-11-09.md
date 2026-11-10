# MR2 erratum to the c2 attempt d0f833ff, per PP audit 7f366e78
2026-11-09, ≈22:40 CST (America/Chicago). Author: MR2. Additive; nothing edited; nothing adopted; no CERT, no Gemini, nothing sent. Junction UNSOLVED.
- Target: MR2_BRANCH_ATTEMPT_BATCH1_C2_W_x_P_o_r_LIFT_AND_BOSONIC_RULE_PER_OW_t445u_2026-11-09.md, d0f833ffd5c116b7701072b66ef5b56f670b9ae50acb760ecd0085bda2388c76.
- Audit: FINDINGS_PP_AUDIT_MR2_C2_d0f833ff_2026-11-09_2232.md, 7f366e783088ebe6fa90240bef1da7d822eab16fe679c0b9c4782d40ffbf128b (= sidecar).
- Authority: OW t445u, d64f6fd2ac51628251b8f39a658251fbc15935734b54aead2f0843569caf7def ("Open c2").

**Fix 1 (C2/C4 scope; the refuted sentence is withdrawn).** C4's sentence "By C2 no choice of lift of r rescues it" is REFUTED by PP's counterexample: c2′ = P∘r̃∘Π_{x³} is itself a lift over r, and it passes both tests. Corrected statements:
- Over all lifts h ∈ U(1) × O(3)_R × Isom(AdS₅) composed with r̃, the bosonic rule f*G = det(f)·G holds **exactly when det_AdS(h) = −1** (PP pp_c2 [gen]). So the rescues are exactly the c2′/c2″ type. PROVED as an implication of Q1 and the bd47ff5e index sets.
- **Scoped claim:** for lifts that act on AdS₅ by orientation-preserving isometries, every lift over r with an odd O(3)_R part fails the bosonic rule. It is the rule alone that does this.
- The chirality argument does **not** independently exclude r̃∘SO(3)_R lifts, which commute with W̃ (those lifts are excluded by the bosonic rule, as r̃ is). "Two independent ways" applies only to the literal map P∘r̃.

**Fix 2 (Q1).** μ₁²-preservation, and with it the split of the fibre into the φ₁-plane and the O(3)_R ℝ³, is **PROVED**: R₁₁ is strictly increasing in μ₁² (PP 60293840; MR2 04b94770/0f635774), and R is an isometry invariant. Two things remain premises: that the full fibre isometry group is U(1) × O(3)_R, and that G is SO(3)_R-invariant.

**Fix 3 (register wording).** It is not "B1-c2 REF". It reads: **"B1-c2: literal formula REF (scoped to AdS-orientation-preserving lifts); intended content = c2′/c2″ (algebra PROVED, Pin/Spin COND, Killing spinor and E₈ bundle OPEN), kept; nothing adopted."** The Killing-spinor follow-up is in the next file (MR2_BRANCH_ATTEMPT_BATCH1_C2PRIME_KILLING_SPINOR_SU2R_PER_PP_7f366e78_2026-11-09.md).

**Fix 4 (tally).** Row 1 (C0, the two P's) moves to bookkeeping. Grades (PP): PROVED 5 (rows 2, 3 [implication of Q1, scoped], 4, 5, 7) · COND 2 (8, 10) · OPEN 1 (9) · REF 1 (6, scoped) = 9. Plus 2 bookkeeping rows (1, 11) and the junction UNSOLVED.

**Fix 5 (duplicates).** reports/c2_lift_check_2026-11-09_2230.py and .log, and their sidecars, are **byte-identical duplicates** of /workspace/mr2-c2-2226/ (b34e8741…, fbe531ca…; PP cmp ✓). They are kept, not deleted, and they are not evidence beyond the originals.

**Fix 6 (C5 frame premise).** The twist projector test uses Γ_{uvαφ₁}, with α standing for the μ₁-radial leg. That this bivector product is the MN2 twist projector is a **frame premise** in d0f833ff. The next file replaces it with the cited 7D projectors of Maldacena–Núñez (hep-th/0007018, App. eqs. (90)–(99)).

Tip 7cddb188 MATCH.
