# MR2 label fixes per PP audit, O4 KK/BF on (D) = AdS₅×S⁴×Σ₂. 2026-11-09, ~16:10 CST (America/Chicago)
Agent: MR2. Authority: Owner KK go-ahead (t4294u, 15:13 CST). This is a new additive file, and nothing existing was edited.
- It supersedes the labels (not the mathematics) in MR2 7824e789316a169dc11eae4d684465e96b4b305cff02e568c43066fea106e8b8 and MR2 cross-check 3d94336786ad76ea3785b437917e6894dd14f9cb1cf9f833e183d981800bd741.
- Source: PP audit FINDINGS_PP_AUDIT_MR2_KK_BF_ADS5S4SIGMA2_2026-11-09_1602.md, sha256 9b557373954788a89d5c44b8eac6d09f1c5c131efdb7386464d85022a9c869fc. I recomputed it, and it equals the sidecar.
- Tip 7cddb188… untouched. No CERT, no Gemini, nothing sent outside, no agent messaged.

## Label changes (each checked against PP's reason; MR2 agrees with all of them)
| # | item | old (file) | new | reason (checked) |
|---|---|---|---|---|
| F1 | 14-plet m²L₅² = −16/3 (S1, Σ-constant) | PROVED [MR2-calc] (7824e789 S1) | **CONDITIONAL** (on DFGHM (4.7) *or* the PPvN/NVvN 7D Lagrangian); arithmetic PROVED | PP K2/K3/K5. Both routes cite results that were read but not re-derived. PP's independent 11D linearization (K4) corroborates −16k²/3 numerically; the exact form is PENDING. |
| F2 | E2 Teichmüller modes, m² = 0, 6 real | PROVED (3d943367 E2) | **CONDITIONAL** (on the X₇-covariant spin-2 structure, L1-spin-2) | PP E2. The arithmetic Δ_L^Σ = 2K cancelling −2Λ_R is correct, but the surrounding Fierz–Pauli structure was not verified component by component. |
| F3 | L1 coupled-scalar sector | PROVED (3d943367 L1-a) | **CONDITIONAL** (on the DFGHM text; it becomes PROVED once PP K4 is exact) | PP §2. The argument is structural plus a citation. |
| F4 | L1 S⁴-TT sector | PROVED (L1-b) | **CONDITIONAL** (not verified component by component) | PP §2 |
| F5 | L1 forms sector | PROVED (L1-c) | **CONDITIONAL** (not verified component by component) | PP §2 |
| F6 | KR eq. (14) ×16 vs KR (4)/(5) | PROVED (C5) | **PROVED, immaterial** (unchanged; confirmed by PP and O1 D2) | 16 = (R₀/r)⁴ |
| F7 | Bolza / KMP: no extra unstable copies | PROVED (7824e789 §3) | **CONDITIONAL** (on the cited λ̂₁ values, not recomputed) | PP K7 |
| F8 | 5D graviton tower 4λ̂ (7824e789 S7) | PROVED | **CONDITIONAL** (same spin-2 structure as F2) | MR2 consistency with PP §2 L1-spin-2 |
| F9 | E1: "≥ −13/3" | REFUTED, corrected statement PROVED | unchanged. Note that the Otal–Rosas input itself is CONDITIONAL (not fetched). | PP E1 |

## Authoritative status (O4, after PP audit)
| item | label |
|---|---|
| (D) = KR (vi) untwisted product; Einstein X₇, L₇ = 2r, (L₅/L₇)² = 2/3 | PROVED |
| 14-plet Σ-constant m²L₅² = −16/3 < −4 ⇒ (D) perturbatively unstable, all N, g, Γ | CONDITIONAL (DFGHM (4.7) or 7D Lagrangian; PP K4 numerical corroboration) |
| Σ-harmonic copies −16/3 + 4λ̂, violating BF iff λ̂ < 1/3 | PROVED (normalization; given the row above) |
| Bolza/KMP: exactly 14 unstable modes; extra copies near degeneration | CONDITIONAL (citations) |
| E1 corrected bound (λ̂ ≤ 1/4 ⇒ m²L² ≤ −13/3); original "≥" | PROVED / REFUTED |
| BF violation ⇒ linear instability | CONDITIONAL (Breitenlohner–Freedman 1982) |
| S⁴ breathing 48, Σ breathing 8 | PROVED (PP C3 plus re-runs) |
| Teichmüller 0; graviton tower; spin-2 shifts 0, 0, +8, +8 | CONDITIONAL (L1-spin-2) |
| L1: scalar, S⁴-TT, forms, vectors, spin-2, special modes, completeness | CONDITIONAL |
| L1 refuted in any sector | not REFUTED |
| √6/2 = (3/2)L₅/L₇ = √(6/d)\|_{d=4}, a probe wall and not a KK mode | PROVED |
| √6/2 ⇒ brane-nucleation instability | CONDITIONAL (probe limit, T₅ calibration) |
| N=4880, g=2 numbers (k, L₅ = 40.567128, L₇, r, ρ, Area); a_D = (8√6/81)(g−1)N³ | PROVED (formula); a_D's CFT meaning CONDITIONAL |
| KR (14) ×16 | PROVED, immaterial |
| PP K4 exact nullspace; K4 at ℓ = 3 | PENDING (PP) |
| fermions; count of genus-2 eigenvalues in (1/4, 1/3); nonlinear endpoint; backreacted nucleation; 1/N corrections | OPEN |

## Rollup (table rows above)
PROVED 6 · CONDITIONAL 6 · PROVED/REFUTED 1 (E1: corrected bound PROVED, original wording REFUTED) · not-REFUTED 1 (L1) · PENDING 1 (2 PP items) · OPEN 1 (a bundle of 5 items). Total 16 rows. The a_D row is PROVED as a formula; its CFT meaning is CONDITIONAL.

Headline: (D) is perturbatively BF-unstable (CONDITIONAL on either of two independent cited derivations, numerically corroborated by PP in 11D) and non-perturbatively unstable at probe level (CONDITIONAL). No N, g or Γ removes this. The Owner's choice stands: accept (D) as unstable, or adopt a supersymmetric twisted solution (MN/BBBW), which needs a new adoption.
