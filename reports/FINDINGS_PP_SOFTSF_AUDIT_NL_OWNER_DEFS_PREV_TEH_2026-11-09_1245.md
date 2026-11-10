# Soft SF FINDINGS: PP math audit of NL FINDINGS_NL_OWNER_DEFS_PREV_TEH_2026-11-09_1233.md (sha 76e63cc2…)
Prepared 2026-11-09 ~12:45 CST (America/Chicago).

**Authority:** Owner DIRECT on the Nov 9 ~12:33 CST voice call, relayed by Physicist. New dated file only. tip 7cddb188 untouched. No CERT.

**Method:** derived by hand. I re-solved items 13 and 14(ii) with exact rational arithmetic in Python (fractions); nothing is saved apart from this file.

**VERDICT:** CONFIRM. Every PROVED and REFUTED item checks out. One normalization caveat applies to item 11.

## Focus items

1. **PROVED.**
   - P_rev² = γ⁰Kγ⁰K = γ⁰γ⁰*.
   - In the Majorana representation γ⁰ is imaginary, so P_rev² = −(γ⁰)² = −1. In the Dirac representation γ⁰ is real, so P_rev² = +1. The mostly-plus convention gives the same signs.
   - A phase drops out: (e^{iθ}A)² = e^{iθ}e^{−iθ}A².
   - In the Majorana representation, CPψ = (γ⁰ψ(−x))* = −γ⁰ψ*(−x), so CP = −P_rev.
   - Note: P_rev² depends on the representation because K does. Item 2 (codomain and embedding) is correctly CONDITIONAL.

3. **PROVED** (energy inversion, Majorana representation only).
   - KΠ fixes p = −i∇, because both K and Π send p to −p.
   - So P H P⁻¹ = γ⁰(α*·p + β*m)γ⁰.
   - In the Majorana representation, α_i is real and β* = −β. Using γ⁰α_iγ⁰ = −α_i, this gives −H.
   - In the Dirac representation, α₂ is imaginary, so the p₂ term keeps its sign while p₁ and p₃ flip, and β stays fixed. The result is neither +H nor −H.
   - For an antiunitary A, A e^{−iHt} A⁻¹ = e^{+i(AHA⁻¹)t}. This is a symmetry exactly when AHA⁻¹ = −H.
   - H(−m) ≠ −H(m), so this is not a mass flip. Negative inertial mass stays OPEN.

10. **REFUTED-by-proof**, confirmed.
    - A compact simply connected 4-manifold of constant curvature K has three possibilities:
      - K > 0 gives S⁴, with χ = 2.
      - K = 0 gives χ = 0 (flat, by Chern–Gauss–Bonnet).
      - K < 0 has universal cover H⁴, so π₁ is infinite.
    - K3 has χ = 24 and π₁ = 1, so no case applies.
    - The repair (Yau's Ricci-flat metric, holonomy SU(2)) is correct.

11. **PROVED** as arithmetic, with a convention caveat.
    - δ(F_{MPQR}F^{MPQR})/δg^{MN} = 4F_{MPQR}F_N^{PQR}.
    - With L_F = −F²/48 and T = −(2/√g)δ(√g L)/δg^{MN}, T = (1/6)FF − (1/48)gF². The Owner's (1/3)FF − (1/24)gF² is exactly twice that.
    - Caveat: whether the factor 2 is an error depends on how T and the Einstein equation are normalized, for example −(1/√g)δ/δg versus −(2/√g)δ/δg, or G = κ²T versus G = 2κ²T. Label it a normalization mismatch, conditional on the Owner's stated convention, not REFUTED.

13. **PROVED.**
    - For AdS₅ (Ric = −4k²g) × an Einstein 6-fold (Ric = Kg), R = −20k² + 6K, G_ext = 6k² − 3K and G_fib = 10k² − 2K.
    - L7 gives 6k² − 3K = −Φ/96 and 4k² + K = Φ/144.
    - The exact solution is k² = Φ/1728 and K = Φ/216 = 8k².
    - If K = 0, then k = Φ = 0.

14. **Block formulas PROVED.**
    - For AdS₅ × K3 (Ricci-flat) × S² (K_S), G_ext = 6k² − K_S, G_K3 = 10k² − K_S and G_S² = 10k².
    - **(i) REFUTED-by-proof.** An isotropic internal source, including Λ₁₁g, forces G_K3 = G_S², which gives K_S = 0. That contradicts round S².
    - **(ii) REFUTED-by-proof.** 6k² − K_S = −Φ/96 and 4k² + K_S = Φ/144 give k² = −Φ/2880 and K_S = Φ/120, both exact.
      - So k² ≥ 0 forces Φ ≤ 0, and then K_S ≤ 0.
      - This contradicts K_S = 1/r² > 0. It holds even at Φ = 0, because K_S = 0 there.

## Other PROVED items (all hold)

| Item | Check |
|---|---|
| 4 | P′T′ = e^{i(α−β)}PT and T′P′ = e^{i(β−α)}TP, so the factor is e^{2i(α−β)}. Commuting versus anticommuting is a convention; OPEN as a physics claim is fine. |
| 5 | C² = 1, so C·P_rev·T = ±PT. |
| 6 | Z ↦ 119 − Z is a bijection on {1,…,118}. |
| 12 | g = k²y²η, so ∂_y g = (2/y)g. With e^{−ky}, the warp matches L2. |
| 15 | T_matter needs −2∂L/∂g. |
| 16 | 11D supergravity has no cosmological-constant deformation. |
| 19 | Λ₅ = −6k². |

## Labels
OPEN and CONDITIONAL labels (items 2, 7, 8, 9, 17, 18, 20) are appropriately not refuted.

No CERT. REPORTS ONLY.
