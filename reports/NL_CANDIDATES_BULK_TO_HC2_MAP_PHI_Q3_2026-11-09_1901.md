# NL CANDIDATES: the bulk-to-H⊗ℂ² map and Φ Q3 (pointwise vs integrated) on MN N=2 — 2026-11-09 (America/Chicago)
Author: Non Local Path (NL). **Everything below is an NL derived proposal. Nothing is adopted; the Owner chooses.**

**Tally: PROVED 13 · CONDITIONAL 4 · OPEN 4 · REFUTED 0 (total 21).** Item lists in §3.

Authority: OW b0b9ae7f ("Pursue all for resolutions"; NL items include the bulk-to-H⊗ℂ² map and Φ Q3), sidecar MATCH. In force: f825dfff, 19a88b19, 49b04146, 36683379.
Also used: OW 68a2b8e1 ((B)-M adopted: P̂ = (γ⁰Π⊗σ_x)K on H⊗ℂ²), OW t4315 (P_rev = T1 adopted; "Φ pointwise versus integrated" still open), and NL F2 (1528) definitions.
Scripts in /workspace/nl-cand-1854/ (with sidecars):
- map_checks.py 11e97edf…, log 4e70e9a4…
- phi_mn2.py 022b0752…, log 0bb298b5…
- phi_exact.py 052fea13…, log 5eeb94e2…
Limits: new file only. No CERT, no Gemini, nothing sent.

## 1. Bulk-to-H⊗ℂ² map
**Record.**
- H = L²(ℝ³)⊗ℂ⁴ (4D Dirac space), 𝓗 = H⊗ℂ², H₊ = H⊗e₁, H₋ = H⊗e₂.
- A₀ = γ⁰KΠ (Majorana representation), S = 1⊗σ_x, P̂ = S·(A₀⊗1), and P_rev = T1 = (S·P̂)|_{H₋} = P₋.
- No map from 11D fields to 𝓗 is defined (NL 1620 C4/C5, PP 1638 C3). This is the open item.

Common setup for all three candidates: let Ψ be a bulk spinor on the covering space of the HW orbifold. Expand it in KK modes Ψ = Σψ_n(x)⊗χ_n(r, Σ, S⁴). Let χ₀ be the lowest mode in the 49b04146 scope (Bolza × wall-ℤ₂ invariant).
- **Mc (OPEN).** Whether χ₀ exists and is normalizable. The KK spectrum is OPEN.

### M-A Two-sheet map, wall ℤ₂ = S
**Definition.** ι_A(Ψ) := ψ₀^{(side r>r_b)}⊗e₁ + ψ₀^{(mirror side)}⊗e₂. The f825dfff wall ℤ₂ acts as S = 1⊗σ_x.
- **MA1 (PROVED).** [S, H_D⊗1] = 0, so the wall ℤ₂ is a symmetry of H_tot.
- **MA2 (PROVED; script, = NL F2 K1).** A₀⊗1 commutes with S. So the antiunitary behind T1 descends to ℤ₂-invariant states.
- **MA3 (PROVED; script).** P₋ itself (reading (b), zero on H₊) does **not** preserve the S-even subspace. On physical orbifold states, T1 must be read as A₀⊗1.
- **MA4 (PROVED, from f825dfff odd G₄).** Sheet e₂ carries ∫_{S⁴}G₄ = −N_flux when sheet e₁ carries +N_flux. So under M-A, "−U" is the negative-flux sheet.
- **MA5 (PROVED).** The S-projection keeps (e₁ ± e₂) combinations. So a ±U superselection rule (NL F2 reading (c)) is incompatible with M-A.
- **MA6 (CONDITIONAL).** For spinors, the HW projection is chiral (Γ_r-type: ψ(−r) = Γ_r ψ(r), hep-th/9603142, cited), so σ_x alone is incomplete. See M-B.

### M-B Two-sheet map with a chiral lift, S′ = γ⁵⊗σ_x
**Definition.** ι_B = ι_A, with the wall ℤ₂ acting as S′.
- **MB1 (PROVED; script).** In the Majorana representation A₀γ⁵A₀⁻¹ = γ⁵, so A₀⊗1 commutes with S′. P_rev survives the chiral projection.
- **MB2 (PROVED; script).** [S′, H_D⊗1] = 0 iff m = 0. So M-B requires massless 4D modes. That conflicts with a massive free H_D (O5 free Dirac is OPEN; NL F2 used m = 0.7).
- **MB3 (CONDITIONAL).** M-B is consistent with HW's chiral wall spectrum (cited; not re-derived).

### M-C R-symmetry doublet map
**Definition.** ℂ² := the fundamental of SU(2)_R of MN2's 4D N=2, with e₁, e₂ the T₃_R eigenvectors. ι_C sends the 4D supercharge doublet of the MN2 Killing spinors to 𝓗.
- **MC1 (PROVED; script).** T1 acts on e₂ only, so it commutes with U ∈ SU(2)_R iff U is diagonal. T1 therefore breaks SU(2)_R to U(1)_{T₃}, which answers NL 1620 C5 for this map.
- **MC2 (OPEN).** Whether the HW wall's susy halving (N=2 → N=1, which also breaks SU(2)_R) leaves the same U(1). J7's susy question is still OPEN.

**NL recommendation (map).** M-A as the base map: it uses only adopted objects (the f825dfff ℤ₂ and the (B)-M σ_x), and it fixes how T1 acts on physical states (MA2, MA3). Add the M-B refinement only if the Owner wants HW's chiral fermion projection, which forces m = 0 (MB2). Use M-C only if ±U is meant to be an R-charge label.

## 2. Φ Q3: pointwise vs integrated, now on MN2
**Record.**
- NL F3 Q3 / MR2 cross-check Q3: pointwise Φ(p) = 4!|G|²_{W₃₅,p} = G·G, or the integral ∫_{M₇}Φ vol, which needs b. MR2 recommends pointwise. The Owner's choice is OPEN (OW t4315).
- Those files worked on (D). MN2 is now the working vacuum (19a88b19), so the candidates are re-evaluated there.

### Φ-P Pointwise
**Definition.** Φ(p) := G_MNPQG^MNPQ(p).
- **PP1 (PROVED).** From R_MN = (1/12)(G_MPQRG_N^PQR − (1/12)g_MN G²), every direction x with no G legs has R^x_x = −Φ/144 and G^x_x = −Φ/96. So **L7a holds pointwise on every 11D sugra solution**, not only on (D).
- **PP2 (PROVED, computer-assisted, as a property of the MN2 CLP metric; the metric's EOM status stays CONDITIONAL per 19a88b19).**
  - At the MN2 IR fixed point, Φ depends only on χ (sin χ = μ₁).
  - Φ·L₇² runs from 480·2^{2/3} = 761.9525 at χ = 0 to **1728** at μ₁ = 1. In ℓ_p⁻² that is [0.30867, 0.70001].
  - It agrees with PP's independent G² (384096a8 gate log) at four points to all printed digits.
  - Method: Φ = 144[4e^{−2W}/L₅² + ∇²W + 5|∇W|²], with W = ⅙ ln Δ̃ and L₅/L₇ = 2^{−2/5}.
- **PP3 (CONDITIONAL, numerical).** L₅/L₇ = 2^{−2/5} matches the NL 1655 value to 1.5×10⁻⁸. It is not derived here.
- **PP4 (PROVED).** Φ-P needs no b.
- **PP5 (OPEN).** The maximum equals 1728 L₇⁻², the same number as the old lock constant in k² = Φ/1728. NL records this as a coincidence and does not interpret it.

### Φ-A Fibre average (no b)
**Definition.** Φ̄ := ∫_{M₆}Φ dvol₆ / Vol(M₆) at a fixed AdS₅ point.
- **PA1 (PROVED, quadrature).** On MN2, Φ̄ = 1018.336 L₇⁻² = 0.41253 ℓ_p⁻².
- **PA2 (PROVED).** L7a holds for averages, by linearity, but not as a pointwise equation for Φ̄.
- **PA3 (CONDITIONAL).** The value depends on the measure. M₆ with √g₆ was used; the 11D warped measure differs.

### Φ-I Integrated over M₇ (needs b)
**Definition.** Φ_I := ∫_{M₇}Φ vol₇.
- **PI1 (PROVED; MR2 Q3).** It has dimension ℓ_p⁵, so it cannot enter L7a.
- **PI2 (OPEN).** Its value needs b. Under b-1 (single wall), the warp-weighted version is finite, with kb → ∞.

**NL recommendation (Φ Q3).** Φ-P. It is b-free, satisfies L7a identically on every solution (PP1), and is now computed on MN2 (PP2). Keep Φ̄ as a named secondary quantity if a single number is wanted.

## 3. Tally (header checked)
| label | count | items |
|---|---|---|
| PROVED | 13 | MA1, MA2, MA3, MA4, MA5, MB1, MB2, MC1, PP1, PP2, PP4, PA1, PA2 |
| CONDITIONAL | 4 | MA6, MB3, PP3, PA3 |
| OPEN | 4 | Mc, MC2, PP5, PI2 |
| REFUTED | 0 | — |
PI1 is quoted from MR2 (PROVED there) and is not counted. Counting it as well gives PROVED 14, total 22.
Check: 13 + 4 + 4 + 0 = 21.

Tip: 7cddb188 unchanged at start. No CERT. Nothing sent.
