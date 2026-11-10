# OWNER WRITE — Duke 2005 + Elkies Klein seed S/T + Gannon free-module (Card 1F) + Eigen cusp6-module authorize
Date: 2026-10-26 ~13:46 CDT America/Chicago
Voice: call-fd1cf6e0-4d48-4a73-9e9b-c216e44a478c
Owner decision: Card Duke+Elkies+Gannon CLOSED A (Eigen Card1E follow-on recommended A; Owner opened + approved A)

tip Soft SF LOCK: `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`
tip_touched: NO (this Write is premises only — no tip fold)
invent HOLD tip fill else: STANDS
Soft SF F3 CLOSED: STANDS
Bridge PARTIAL READY NO: STANDS

## Prior locked
- Card 1E classical S/T lit cites OW `9a7fe5510c433335fb1eeb17a35dc099ef80bdf6ac709078fef4ac59f04a3687`
- Eigen Card1E FINDINGS PARTIAL `b3429b706d7419531001918104e1042f2ff0420a7189e6e6d07d6622d37b5e6d`
  - ρ₄ MATCHED η¹⁸ exact; ρ₅ ABSENT; ρ₇ ABSENT; Step 3 module not built
- MR1 classical-gens CITECHECK PARTIAL `f81d7d3378f1a64409ab0fed1e9533e9c8ccc333f7c82161027ab79faeba8ab3`
- Card 1D local-factor OW `ab8a4937eb4087a8c63b1c9addeb5e9a5c085c3428f963bcb10d3fe468e4595a`
- Eigen Card1D FINDINGS PARTIAL `6e8c901c8eb240cb9c4fbce39309c68728e4636daf38c003fe9f1ccb059ff125` (ρ̄|cusp6 ≅ ρ₄⊗ρ₅⊗ρ₇ EXACT)

## Decision A (LOCKED)
Owner Writes the on-disk verbatim classical seed S/T from Duke 2005 and Elkies (Klein model), adopts Gannon free-module + Magnusson–Raum compute method, and AUTHORIZES Eigen to continue the cusp-six module versus dim 89.

Eigen is AUTHORIZED to:
1. Match ρ₅ and ρ₇ to these Written seeds (exact intertwiners over CF(140); dual/conjugate Klein choice resolved against Card1D T-exponents {3/7,5/7,6/7}).
2. Assemble ℂ[E₄,E₆]⊗Ind module through q^18 vs dim 89 (exact; no invent).
3. Ship FINDINGS path+sha. Fill-first GATE for MR1 opens only after module/basis FINDINGS land.

## Source files on disk (this Write)
- Duke 2005 PDF: `/workspace/quantum-comp/reports/literature/duke2005/duke2005.pdf` (UCLA preprint of Bull. AMS 42 (2005) 137–162)
- Duke text extract: `/workspace/quantum-comp/reports/literature/duke2005/d.txt`
- Elkies 1999 PDF: `/workspace/quantum-comp/reports/literature/elkies1999/elkies.pdf` (MSRI Publ. 35 / The Eightfold Way)
- Elkies text extract: `/workspace/quantum-comp/reports/literature/elkies1999/elkies.txt`
- Gannon free-module: `/workspace/quantum-comp/reports/literature/gannon-2202.06676/gannon1310.pdf` (arXiv:1310.4458)
- Compute method: `/workspace/quantum-comp/reports/literature/gannon-2202.06676/2202.06676.pdf` (arXiv:2202.06676)

---

## §1 — Duke 2005 — verbatim S and T (ρ₅ seed family)

Source: W. Duke, "Continued fractions and modular functions", Bull. AMS 42 (2005) 137–162 (UCLA preprint on disk).

### 1a. SU(2) generators of G₆₀ (Duke p.6)
With ζ = e(1/5) = exp(2πi/5), Duke Writes the generators of G₆₀ ⊂ PSL(2,ℂ) represented in SU(2) by:

```
        [ ζ³   0  ]                 1  [ ζ⁴−ζ³    ζ³−ζ² ]
  S  =  [  0  ζ²  ]    and   T  = √5⁻¹ [ ζ³−ζ²    ζ⁴−ζ  ]
```

(Quote reconstruction from pdftotext of Duke p.6: "transformations with generators represented in SU(2) by the matrices S=… and T=… where ζ=e(1/5), giving elliptic transformations of order 5 and 2, respectively [Fri, p.42] (or [Tot, p.28]).")

Also W = TS of order 3 (Duke p.6):
```
          1  [ ζ⁴−ζ²   1−ζ⁴ ]
  W = √5⁻¹ [ ζ−1     ζ−ζ³ ]
```

### 1b. Action on Rogers–Ramanujan continued fraction r (Duke Prop. 2 / (3.2), pp.6–7)
```
  r(τ+1) = S · r(τ) = ζ · r(τ)
  r(−1/τ) = T · r(τ) = [−(1+√5) r(τ) + 2] / [2 r(τ) + 1 + √5]
```
and r(gτ) = r(τ) for all g ∈ Γ(5).

### 1c. ABSENT in Duke 2005 (explicit — invent HOLD)
Duke does **not** Write an explicit 2×2 modular-form multiplier matrix for a Rogers–Ramanujan **vector** (G,H) with entries in terms of sin(2π/5), sin(4π/5). What is Written is the Möbius/SU(2) action on the scalar continued fraction r. Eigen must either (i) derive the exact ρ₅ intertwiner from these Written seeds + η-twist against Card1D targets S₅=[[0,−1],[1,0]], T-exps {2/5,3/5}, or (ii) cite a further Owner-approved Written source for the (G,H) vvmf matrix. No matrix invented here.

---

## §2 — Elkies Klein — verbatim S and T (ρ₇ seed family)

Source: N. D. Elkies, "The Klein quartic in number theory", The Eightfold Way, MSRI Publications 35 (1999). ζ := e^{2πi/7}.

### 2a. Klein model generators (Elkies §1.1, eqs. (1.2)–(1.3), pp.53–54)
Relative to the eigenbasis for g ∈ class 7A (eigenvalues ζ, ζ², ζ⁴ on V = χ₃), Elkies Writes:

```
              [ ζ⁴  0   0 ]                 [ 0  1  0 ]
  ρ(g) =      [  0  ζ²  0 ] ,    ρ(h) =     [ 0  0  1 ]     (1.2)
              [  0  0   ζ ]                 [ 1  0  0 ]
```

and the involution filling out G (image of s = ±[0 −1; 1 0] in PSL₂(𝔽₇)):

```
                 [ ζ−ζ⁶   ζ²−ζ⁵   ζ⁴−ζ³ ]
  ρ(s) = −1/√(−7) [ ζ²−ζ⁵  ζ⁴−ζ³   ζ−ζ⁶ ]     (1.3)
                 [ ζ⁴−ζ³   ζ−ζ⁶   ζ²−ζ⁵ ]
```

(Elkies: "Except for the scaling factor −1/√(−7), it is just the discrete Fourier transform on the space of odd functions 𝔽₇→ℂ: identify such a function f with the vector (f(1),f(2),f(4)) ∈ V.")

T-exponents of (V,ρ)=χ₃ under ρ(g): {4/7, 2/7, 1/7} ≡ {1,2,4}/7. The contragredient (V*,ρ*)=χ̄₃ is the complex-conjugate / dual irrep with T-exponents {3,5,6}/7 (Elkies: Aut(G) switches χ₃↔χ̄₃; X(7) coordinates realize V* — see §2b). **Card1D target {3/7,5/7,6/7} matches the dual (V*,ρ*).**

### 2b. Modular cusp-form basis x,y,z for Γ(7) (Elkies §4, eqs. (4.4)–(4.7), pp.84–85)
```
  x = q^{4/7} (−1 + 4q − 3q² − 5q³ + 5q⁴ + …)
  y = q^{2/7} (1 − 3q − q² + 8q³ − 6q⁵ − …)
  z = q^{1/7} (1 − 3q + 4q³ + 2q⁴ + 3q⁵ − …)
```
These are ζ⁴-, ζ²-, ζ-eigenforms for g; the representation they generate is isomorphic to (V,ρ), and the canonical image of X(7) is the Klein model of (V*,ρ*) with Φ₄(x,y,z)=x³y+y³z+z³x=0.

### 2c. Identification for Eigen
- Use ρ(s) of (1.3) as the classical S-seed and ρ(g) of (1.2) as the classical T-seed for the Klein triple.
- Match to Card1D ρ₇ via the dual (V*,ρ*) (T-exps {3,5,6}/7), with exact intertwiner + any η-twist — exact equality only.

---

## §3 — Gannon free-module + compute method (LOCKED adopt)

### 3a. Free-module theorem
[V] T. Gannon, "The theory of vector-valued modular forms for the modular group", arXiv:1310.4458; Contrib. Math. Comput. Sci. 8 (2014) 247–286. Proves free-module structure of holomorphic vvmf over ℂ[E₄,E₆] for arbitrary multiplier, dimension formula, Serre duality. On disk: `gannon1310.pdf`.

### 3b. Compute method for Ind / general vvmf
[V] T. Magnusson, M. Raum, "On the Computation of General Vector-valued Modular Forms", arXiv:2202.06676. Algorithm for Fourier expansions of vvmf of weight ≥2 for representations with congruence-subgroup kernel (beyond Weil reps / Dirichlet inductions). On disk: `2202.06676.pdf`.
**Note:** arXiv:2202.06676 is Magnusson–Raum, not Gannon. Adopted here as the **method** for the Ind_{Γ₀(49)} / general-vvmf compute step Eigen named; free-module theorem remains Gannon §3a.

---

## §4 — Constraints
- Exact only — not float T-spectra; no coefficients invented in this Write.
- tip Soft SF LOCK untouched; invent HOLD tip fill else; Soft SF F3 CLOSED; Bridge PARTIAL READY NO.
- Tip folds + T-U held; Cards 8–11 not opened by this Write.
- Card4 HOLD numerics + Card6 tip-fold window STAND.
- Duke §1c ABSENT stands until a further Written source or exact derivation from §1a–1b lands in Eigen FINDINGS.
- Soft SF CONFIRM packaging of this OW + source PDFs ordered (Write-only / no tip fold).

## Propagation
Eigen BEGIN ρ₅/ρ₇ intertwiner match from these Written seeds + cusp6 module vs 89 under this Write.
MR1 STAND BY fill-first until Eigen module/basis FINDINGS.
Auditor Soft SF CONFIRM this OW + literature pack (Duke/Elkies/Gannon/2202.06676).
