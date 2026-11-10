# MR2 branch attempt: B1-c2′ (and c2″) against the MN2 Killing-spinor projectors, up to SU(2)_R
2026-11-09, written 22:40–22:42 CST (America/Chicago, box clock). Author: MR2. Additive; nothing edited; nothing adopted; no CERT, no Gemini, nothing sent. Junction UNSOLVED. Group A stays the chosen KK scope; c2′/c2″ are separate branches (scope conflict only).
Authority and inputs: OW t445u d64f6fd2ac51628251b8f39a658251fbc15935734b54aead2f0843569caf7def; PP audit 7f366e783088ebe6fa90240bef1da7d822eab16fe679c0b9c4782d40ffbf128b (Task B); MR2 c2 attempt d0f833ffd5c116b7701072b66ef5b56f670b9ae50acb760ecd0085bda2388c76 and its erratum 7b8160bf819317ed89ee700c570351b3252a99fc2bbff20391357880c227df4a.

**Source.** Maldacena–Núñez, hep-th/0007018, fetched from arxiv.org/pdf/hep-th/0007018 into /workspace/mr2-c2ks-2234/mn.pdf (sha 770d87d8387d2df1614fa13f4fb41a1ea1df63317aa15026dbaac8d184b5436b). The relevant parts:
- App. §7.3, eqs. (89)–(99): 7D SO(5) gauged supergravity, U(1)×U(1) truncation (SUSY from Liu–Minasian, their ref. [45]).
- §4.1: N=2 fixed point (25), e^{5λ} = 2, e^{2g−λ} = 1/4, e^{f+2λ} = 1/r, with a = 1/4, b = 0, 2λ₁ + 3λ₂ = 0, λ = λ₂, m = 2.
- Projections (99): γ_r ε = ε, γ_xy ε = iε, Γ¹²ε = iε. Γ³⁴ is not needed when b = 0.
- **Premise T1 (transcription):** pdftotext garbled some symbols. Eqs. (90)–(92) were re-typeset by MR2: δψ_μ = [∇_μ + (k/2)(A¹_μΓ¹² + A²_μΓ³⁴) + (m/4)e^{−4(λ₁+λ₂)}γ_μ + ½γ_μγ^ν∂_ν(λ₁+λ₂) + ½γ^ν(e^{−2λ₁}F¹_{μν}Γ¹² + e^{−2λ₂}F²_{μν}Γ³⁴)]ε, plus the two gaugino variations.
  - Support for T1: the script reproduces MN's (93) spin connection (ω_x^{xy} = −1/y and ω_u^{ur} = f′ = −1/r), and it **derives** k = 4, which is MN's "1 = 4(a+b)".

## Scripts and logs (/workspace/mr2-c2ks-2234/; every .py frozen with its sidecar before running; sidecars MATCH)
| file | sha256 | note |
|---|---|---|
| c2p_KSE_MN_7D_2026-11-09_2237.py / .log | ca0158389662dac0c1223e1a3556bc666d4081705b76103ccb99d63e3d96e4e4 / 0864b05adcef277203a1a82ee859850e1f6eb2ab1a0f8511c4c6b7a9c5d5fd05 | v1, **superseded**: coordinate symbols were not positive, so the vielbein sqrt did not simplify; it reported spurious failures |
| c2p_KSE_MN_7D_v2_2026-11-09_2240.py / .log | 3655a659e8fa7e4bb3ee1362219434a387d162b31a53c9dc0e9373ad78c90239 / d7b758bc90998a882c7a73c37395fa21e095667df26d4cd2cd910c618388f2ba | v2, **superseded**: the ω formula wrongly added e^a_ν∂_μE_b^ν for a ≠ b |
| c2p_KSE_debug_2026-11-09_2242.py / .log | 7dccd49f00add811a0f3a1ddc070cbcaf8941a8b40274db3c8b9ebf6628d5aef / b57d274f386b7eb6c298720cd9cf2e7acf35f5f66ca00a704d2a3fcb130a7a15 | diagnostic only (found the v2 bug); supports no claim |
| **c2p_KSE_MN_7D_v3_2026-11-09_2244.py / .log** | **f0aa2e12bd026df3e5d6dee523e1407420c8916181371c0fc037d4290f91661f / 079c41a8c728efef90edd4890b8eda10442bacd366f5d937a827b6a16753ac57** | the run all claims below rest on; exit 0, 13 s, exact sympy |

The names carry times up to 5 min ahead of the box clock. Mtimes are authoritative: v1 22:37:06/22:37:48, v2 22:38:21/22:38:50, debug 22:39:17, v3 22:39:33 (.py and sidecar) and 22:39:47 (.log).

## K1. The cited projectors solve the full 7D Killing-spinor system at the MN2 fixed point. PROVED (exact), given T1
- Setup: a 32-dim complex module (Cl(1,6) ⊗ Cl(5), anticommutators exact). Π = Π_r Π_tw, with Π_r = (1+γ_r)/2 and Π_tw = (1 − γ_xyΓ¹²)/2. Π has rank 8 of 32.
- With ε = r^{−1/2}ε₀ (Poincaré), **all nine equations** δψ_{t,u,v,z,r,x,y}Π = 0 and δλ^{(1,2)}Π = 0 hold exactly. k = 4 is the unique solution of δψ_xΠ = 0.
- Each projector is necessary:
  - dropping the twist projector breaks δψ_x, δψ_y and δλ⁽¹⁾;
  - dropping γ_r breaks δψ_{t,u,v,z,r}.
- The twist projector depends only on the product γ_xyΓ¹²: both sign pairs (i, i) and (−i, −i) solve the system. This is MN's "related by parity".

## K2. Our MN2 is MN's fixed point. PROVED (arithmetic)
- MN (103): W³ = e^{−4(λ₁+λ₂)}μ₀² + e^{2λ₂}μ₁² + e^{2λ₁}μ₂² = 2^{2/5}(1 − μ₂²/2) at (25).
- This equals our Δ = 2^{2/5}(1 − p/2), with MN's μ₂ (the e^{2λ₁}, 12-plane, twisted) = our μ₁.
- So our φ₁ is the 12-plane and our O(3)_R ℝ³ is SO(5) directions 3, 4, 5.

## K3. c2′ is a symmetry of the Killing-spinor system, up to SU(2)_R. PROVED (exact) in the 7D truncation
- In 7D, c2′ acts as x ↦ −x (Σ), z ↦ −z (Π_{x³}), X² ↦ −X² (φ₁ flip) and X⁴ ↦ −X⁴ (φ₂ flip). Its lift is L = γ_xγ_z ⊗ Γ²Γ⁴.
- **Covariance, at the operator level:** L D_μ L⁻¹ = s_μ D_μ for all 7 gravitino operators, with s = −1 on x and z and +1 otherwise, and L δλ⁽ⁱ⁾ L⁻¹ = δλ⁽ⁱ⁾. Also L Π L⁻¹ = Π.
  - Because this holds for the full operators, not only on range(Π), L maps every 7D Killing spinor of the fixed point to a Killing spinor: the Poincaré ones and also the superconformal ones.
- **SU(2)_R:** Ad_L acts on so(3)_R = span(Γ³⁵, Γ³⁴, Γ⁴⁵) as (+, −, −), i.e. a rotation by π about X⁴.
  - L′ = (Γ³⁵)⁻¹L commutes with all of SU(2)_R and with Π, and satisfies the same covariance.
  - L′² = −1; on the 8-dim Poincaré Killing space its eigenvalues are ±i, each with multiplicity 4.
  - The undressed L² = +1, which matches 8399be55 (i′).
- **Controls**, consistent with d0f833ff and PP: the literal P∘r̃ (L = γ_x ⊗ Γ²Γ⁴) and r̃ alone (γ_x ⊗ Γ²) are **not** covariant and do not preserve Π; they flip γ_r.

## K4. From 7D to 11D. COND
Premise D1: in the standard S⁴ reduction (Cvetič et al. hep-th/9903214 for the uplift, used by MN (103); Nastase–Vaman–van Nieuwenhuizen for the fermions), an O(5) isometry of S⁴ acts on the 7D ε^i through the corresponding Pin(5) element Γ^a. Under D1, L is the 7D image of the 11D lift Γ_uΓ_{φ₁}Γ_{φ₂}Γ_{x³} of d0f833ff, up to a sign.
D1 is a citation, not rederived here: COND. Given D1, **c2′ preserves the MN2 Killing spinors up to an SU(2)_R rotation**: PROVED as an implication.

## K5. Other items
- **Symplectic-Majorana compatibility.** L ∈ Spin(1,6) × USp(4), and the SM condition is invariant under that group. This is standard but not checked explicitly here: COND.
- **c2″.** Its unitary part γ_xγ_t ⊗ Γ²Γ⁴ is covariant and keeps Π: PROVED (log). Lorentzian time reversal is antiunitary, and its action on the SM real structure was not computed: OPEN.
- **E₈ / HW wall.**
  - Charge compatibility: c2′ has f*G = +G and preserves the orientation of S⁴ (two reflections, φ₁ and φ₂). So ∫_{S⁴}G = N and the wall charge 2N (bd47ff5e/f825dfff) are preserved, and c2′ commutes with W̃ (d0f833ff). PROVED as an implication.
  - Lift of c2′ to the wall's E₈ bundle: OPEN. It is automatic if the bundle is a spin-connection-type embedding (1b-ii, itself COND); otherwise it needs the wall's instanton/M5 data.
  - Next step: fix the wall E₈ data under 1a, then check r̃-invariance of the instanton configuration on Σ × S⁴ (~1–2 h once the data are fixed).

## Labels (PP convention)
| # | item | grade |
|---|---|---|
| 1 | K1: the MN (99) projectors solve all 9 KSEs at the N=2 fixed point; k = 4 derived; each projector necessary | PROVED (given T1) |
| 2 | K2: our Δ = MN W³; our φ₁ = MN's 12-plane | PROVED |
| 3 | K3: c2′ lift is covariant for all KSE operators and keeps Π | PROVED |
| 4 | K3: up to the SU(2)_R rotation Γ³⁵, the c2′ lift commutes with SU(2)_R and Π; L′² = −1, eigenvalues ±i (4, 4) | PROVED |
| 5 | K4: 7D↔11D fermion dictionary D1 | COND |
| 6 | K4: c2′ preserves the MN2 Killing spinors up to SU(2)_R (11D) | PROVED as implication of D1 |
| 7 | K5: SM compatibility of L | COND |
| 8 | K5: c2″ unitary part covariant | PROVED |
| 9 | K5: c2″ with antiunitary T | OPEN |
| 10 | K3 controls: literal P∘r̃ and r̃ are not covariant | PROVED |
| 11 | K5: c2′ preserves N and the wall charge 2N | PROVED as implication |
| 12 | K5: c2′ lifts to the wall's E₈ bundle | OPEN |
| — | superseded v1, v2 and the debug script | bookkeeping |
| — | junction | UNSOLVED |

Tally: PROVED 8 (1, 2, 3, 4, 6, 8, 10, 11) · COND 2 (5, 7) · OPEN 2 (9, 12) · REF 0 = 12, plus 1 bookkeeping row and the junction UNSOLVED.

**Branch status (pending PP):**
- B1-c2′: the Killing-spinor keep condition holds up to SU(2)_R, PROVED as an implication of D1. The algebra is PROVED. Pin/Spin and descent are COND (8399be55). The E₈ bundle is OPEN. Overall **COND**; not adopted.
- B1-c2″: **COND/OPEN** (antiunitary step open).
- B1-c2 literal: REF (scoped), unchanged.
Tip 7cddb188 MATCH.
