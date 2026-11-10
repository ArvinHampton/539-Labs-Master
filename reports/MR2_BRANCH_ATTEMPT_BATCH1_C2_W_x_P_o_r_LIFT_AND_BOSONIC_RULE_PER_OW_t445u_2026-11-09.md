# MR2 branch attempt: B1-c2, W × (P∘r), r ∈ Isom(Bolza) \ Aut⁺ (per OW t445u "Open c2")
2026-11-09, written ≈22:28–22:33 CST (America/Chicago, box clock). Author: MR2. Additive; nothing edited; nothing adopted; no CERT, no Gemini, nothing sent, no agent messaged. Junction UNSOLVED. Group A (Aut⁺(48) × wall ℤ₂, OW 8b26c786) stays the chosen KK scope. c2 is kept as a separate branch; its conflict with A is a scope conflict only.

**Authority.** OWNER_WRITE_PPCHAT_t445u_OPEN_C2_2026-11-09_2224.md, sha d64f6fd2ac51628251b8f39a658251fbc15935734b54aead2f0843569caf7def = sidecar; Owner's words "Open c2". Criterion and next computation: MR2 erratum 0f6357745f045edb308ed37b45b9b4fdb1a5cada80b0a93dc4ef2fe5e4f9089f, fix 8. Keep = Pin/Spin lift of W × (P∘r) exists, commutes with W̃, compatible with the chiral HW projection. Drop = proof of no consistent lift, or incompatibility with HW chirality or the MN2 twist.

**Inputs (sha-checked).** 425b4e67e5cc58ac8607d9f0c668f2e5d48f3d2bc3363e011ebd194800ecd85a (batch 1, defines c2); 8399be55265f2cb0a42a69db4f6ffcb0e2ecc711fc6cc83aef3c4c47c85f41a1 (Pin⁺ check, cases (i′)/(ii′)); bd47ff5e8f62a6226680a93107cacae8c8be573399e1f101a2dc57635f03fbfb (MN2 G₄ index sets {u,v,α,φ₂}, {u,v,β,φ₂}, {u,α,β,φ₂}, {α,β,φ₁,φ₂}; PP-audited in FINDINGS_PP_AUDIT_MR2_MN2_Z2_WALL_CURVATURE_E8_2026-11-09_1840.md).

## Script and log (frozen before running; sidecars MATCH, both written at 22:26:36 by the same command, the .py sidecar first)
| file | sha256 |
|---|---|
| /workspace/mr2-c2-2226/c2_lift_check_2026-11-09_2230.py | b34e8741b9733eed3cad526d312527e6378412d84b8485627a6347a823cfbef1 |
| /workspace/mr2-c2-2226/c2_lift_check_2026-11-09_2230.log (exit 0, < 1 s) | fbe531ca96e4d49a48892068433f21370781648761e36395c6bf93f061f0c20e |

Identical copies were placed in reports/ (22:27) with their own sidecars (same shas). The "2230" in the name is ~4 min ahead of the box clock; mtimes (22:26:36) are authoritative.

## C0. Clerical self-error in 425b4e67 (disclosed)
425b4e67 §1c says (c2) "is 8399be55 cases (i′)/(ii′)" and "reflects an even number of wall-tangent directions, is orientation-preserving". That conflates two different "P"s. In 425b4e67, P is the φ₂-parity (φ₂ → −φ₂, C → −C). In 8399be55, "P" in "(i) + P" is the 4D spatial parity Π_{x³}, and (i′) = {u, φ₁, x³} + φ₂. So:
- **B1-c2 (literal)** = W × (P∘r̃), P∘r̃ reflects {u, φ₁, φ₂}: three wall-tangent directions, orientation-**reversing**.
- **B1-c2′** = W × (P∘r̃∘Π_{x³}) = 8399be55 (i′) with W; **B1-c2″** = W × (P∘r̃∘T) = (ii′) with W. These are the orientation-preserving maps 425b4e67 described.
Both readings are kept as labelled branches; MR2 picks neither.

## C1. The lift of r to the twisted fibre must flip φ₁. PROVED
r reverses the orientation of Σ, so r*vol_Σ = −vol_Σ and r*A = −A + dλ for the twist connection (dA ∝ vol_Σ). An isometry covering r must send Dφ₁ = dφ₁ + A to ±Dφ₁. If φ₁ ↦ φ₁ + c, then f*Dφ₁ = dφ₁ − A + dλ, which is neither, because 2A is not closed. So φ₁ ↦ −φ₁ + λ + c, and locally at the fixed geodesic of r: r̃ = {u, φ₁}.

## C2. All lifts covering r. PROVED as an implication of premise Q1
Q1 (premise): the MN2 fibre isometries commuting with the twist are U(1)_{φ₁} × O(3)_R, with G₄ invariant under SO(3)_R (MN2's SU(2)_R) and the P-coset being the det −1 part of O(3)_R (μ₀ ↦ −μ₀ = P ∘ (π-rotation)).
Then every isometry covering r is r̃∘h or P∘r̃∘h, h in the identity component (plus AdS isometries). Orientation, the G₄ sign and the [W̃, ·] sign are locally constant, so the table in C3 covers all of them.

## C3. Bosonic rule f*C = det(f)·C and the Clifford lift (log [B], [C]). PROVED (exact), given the bd47ff5e index sets
Pullback sign on each G₄ component = (−1)^{|S ∩ I|}. It is uniform over the four index sets for every candidate. Lifts are products of Cl(10,1) gammas (mostly plus, Γ₀² = −1), verified exactly; W̃ = Γ_ρ.

| map (reflected set S) | det | f*G | bosonic rule | lift² | [W̃, lift] | HW projection Γ_ρε = ε | twist bivector Γ_{uv}Γ_{μ₁φ₁} |
|---|---|---|---|---|---|---|---|
| r̃ = {u, φ₁} | +1 | −G | FAILS | −1 | +1 | kept | preserved |
| P = {φ₂} | −1 | −G | holds | +1 | **−1** | opposite chirality | preserved |
| **c2 literal: P∘r̃ = {u, φ₁, φ₂}** | −1 | **+G** | **FAILS** | −1 | **−1** | **opposite chirality** | preserved |
| c2′: P∘r̃∘Π_{x³} | +1 | +G | holds | +1 | +1 | kept | preserved |
| c2″: P∘r̃∘T (Lorentzian) | +1 | +G | holds | −1 | +1 | kept | preserved |
| (i): r̃∘Π_{x³} (control) | −1 | −G | holds | −1 | −1 | opposite chirality | preserved |
| W = {ρ} (doubled MN2, G odd) | −1 | −G | holds | +1 | +1 | kept | preserved |

Controls: the r̃, P, (i), (i′) and (ii′) entries reproduce 8399be55 (bare s fails; (i) r̃² = −1 and [W̃, r̃] = −1; (i′) +1, +1; (ii′) −1, +1) and 425b4e67 (P with HW: opposite chirality).

## C4. Verdict on B1-c2 (literal). REF, PROVED as an implication of the bd47ff5e index sets and Q1
W × (P∘r) meets the drop criterion of 0f635774 twice, independently:
1. P∘r̃ is not a symmetry of 11D supergravity, even bulk-only: det = −1 but f*G = +G. C ↦ −C cannot be applied by hand, since the C∧G∧G term then flips sign.
2. Its lift (unique up to ± in Pin⁺) anticommutes with W̃, so it maps the HW projection to the opposite 10D chirality, which is incompatible with the chiral E₈ wall (f825dfff premise, as in 8399be55 §B).
By C2 no choice of lift of r rescues it.

## C5. B1-c2′ and B1-c2″ (the (i′)/(ii′) reading)
- Bosonic rule, [W̃, lift] = +1, HW projection kept, twist bivector preserved: **PROVED** (C3). The keep criterion's algebraic part holds.
- Pin/Spin existence, δ = 0 and descent of the class: **COND**, as in 8399be55 (premises 1–4 of its §A, not rederived).
- Preservation of the MN2 Killing spinors (that the lift maps the MN2 supercharges to themselves) and invariance of the E₈ wall bundle: **OPEN**.
- Interpretation: c2′/c2″ include the 5D spacetime parity Π_{x³} or T, so as a truncation they act by 5D parity labels, not as an internal symmetry. **COND** (interpretive).
- Next computation: write the MN2 Killing-spinor projectors (Γ_{uv}Γ_{μ₁φ₁} twist projector plus the SU(2)_R doublet condition) in the frame of the log and check that the c2′ lift commutes with them, up to an SU(2)_R rotation (~45–60 min). Keep = commutes; drop = no SU(2)_R compensator exists.

## Labels
| # | item | grade |
|---|---|---|
| 1 | C0: 425b4e67 conflated two P's; c2 splits into literal, c2′, c2″ | PROVED (clerical) |
| 2 | C1: the lift of r must flip φ₁ | PROVED |
| 3 | C2: every lift covering r is r̃∘h or P∘r̃∘h | PROVED as implication of Q1 |
| 4 | C3: bosonic sign table | PROVED (given bd47ff5e index sets) |
| 5 | C3: Clifford squares, [W̃, ·], twist bivector | PROVED (exact) |
| 6 | C4: B1-c2 literal, W × (P∘r) | **REF** (implication of the bd47ff5e index sets and Q1; the HW part is also given f825dfff) |
| 7 | C5: c2′/c2″ algebraic keep conditions | PROVED |
| 8 | C5: c2′/c2″ Pin/Spin existence and descent | COND |
| 9 | C5: c2′/c2″ Killing spinors and E₈ bundle | OPEN |
| 10 | C5: c2′/c2″ act as 5D parity labels | COND |
| 11 | Group A vs c2′/c2″: scope conflict, nothing adopted | bookkeeping, ungraded |
| 12 | junction | UNSOLVED |

Tally (graded rows 1–10, PP style): PROVED 6 (1, 2, 3, 4, 5, 7) / COND 2 (8, 10) / OPEN 1 (9) / REF 1 (6) = 10; plus row 11 ungraded and row 12 UNSOLVED.

Register delta (pending PP audit): B1-c2 parked → **REF (literal)**; new sub-branches **B1-c2′, B1-c2″: COND** (algebra PROVED, Killing spinor OPEN). Tip 7cddb188 MATCH (22:27 CST).
