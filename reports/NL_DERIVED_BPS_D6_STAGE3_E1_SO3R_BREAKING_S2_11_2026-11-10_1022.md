# NL DERIVED: D6 stage 3 (f), E1 (SO(3)_R breaking, w ≠ 0 kept sides) together with S2-11 (other gravitino eigenvalues)
2026-11-10, 1022 CST (America/Chicago). **NL derived proposal.** Additive only. Authority: Owner call-83d7a0fa (e72a188b…), OW t4436 (32881263…), OW t4431. Inputs: 2216 (f504d1b9…: S2-9, S2-10, S2-11), Erratum 23 (E23-2, credit PP f530cbc0 A3), E5 file (0a7d8e56…, Lemma CH), chirality_hw_lock_exact log (676f7dc8…). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged. No candidate wall.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.

**Tally: PROVED 2 · CONDITIONAL 1 · OPEN 1 · REFUTED 0 · total 4.**

## 0. Scope
- **E1:** SO(3)_R is broken, either to SO(2) (the [w] case: T_αβ ∝ diag(e^w, e^w, e^{−2w}), which keeps the rotation of (μ₃, μ₄) and U(1)_R, E5-7) or completely.
- S2-3's doublet argument is unavailable: there is no SU(2)_R, and the stabiliser is at most SO(2).
- Premises where used: (h1), (P-a), (ii) (record premise S6), (reg), H_Σ, (tw), as in the E5 file.

## 1. What survives
- **E1-1 (PROVED, implication). CH constraint on E1∩H_Σ.**
  - The lock E5-2 needs only H_Σ, and Lemma CH (E5-3(d), log [4]) is pointwise. So at every regular face point of C₄, every chiral Killing spinor lies in the single s₃ = s₃(χ₄) part of the locked subspace with Γ^n = +1.
  - If SO(2) ⊂ SO(3)_R survives with fixed points n̂₀ ∈ S² (the [w] case), it acts at (z, n̂₀) as ½Γ^{tf}. Since ev is injective, every Killing spinor then has SO(2) charge exactly ±½, and **the sign is fixed by chirality**.
  - This is consistent: complex conjugation flips both. **No contradiction arises.** With no doublets, E5-4's contradiction is unavailable.
- **E1-2 (PROVED; exact). The flux/D1 route gives no obstruction on E1.**
  - Every single sector with Γ^r = +1 solves D1 with a unique diagonal K for **arbitrary** (f₄, ω₁, ω₂) and both σ (log [7], [9]).
  - With no SU(2)_R partner there is no second row set to equate, so ω₂ ≠ 0, required by (T), is locally allowed.
  - For each Killing spinor, η = sgn(σs₁s₃Φ_tw) is a single sign (conjugation flips s₁ and s₃ together). So the D6-5 indefiniteness of S2-5 does not carry over to E1, and NEC-compatible local data of D6-3 type (η = +1) are not excluded locally.
  - **This is not a wall.** It only shows that the local and topological obstructions do not reach E1.

## 2. S2-11: other gravitino eigenvalues of 5D N=4 along Z2 / [w] flows
- **E1-3 (CONDITIONAL). Inside the (φ, λ, w) truncation the 5D N=4 gravitino mass matrix is W₃·1, so there is no "other eigenvalue".**
  - Argument:
    - In 7D maximal SO(5) gauged supergravity the gravitino shift is (g/20)·T·γ_με, with T = Tr T_ij times the identity on USp(4), plus a two-form term ∝ (γ_μ^{νρ} − 8δ_μ^νγ^ρ)Γ_{ij}Π_A^iΠ_B^jF^{AB}_{νρ}ε.
    - In the truncation the only gauge field strength is the U(1)_R twist F^{12} along Σ. Π_A^i is diagonal, and its (1,2) block depends on λ only, not on w.
    - On the 5D gravitini, which are the locked spinors (S2-1), Γ_{12}γ^{Σ12} is a fixed sign, so the F-term is proportional to γ_μ with a common coefficient.
    - w enters only through Tr T = 2e^{−6λ} + e^{4λ}(2e^w + e^{−2w}).
    - Hence every 5D gravitino sees the same mass function. Its form, (g/2)[e^{−2φ}Tr T + l e^{−8φ+6λ}], is **literally W₃ of S2-9** (term-by-term identity, read off the W₃ formula in 2216 and w3_and_partners.py; verified exact in 2233/PP A1).
  - Consequence: a Z2 / [w] flow is BPS for some 5D N=4 gravitino only if it is a W₃-flow. S2-10 and E23-2 (credit PP f530cbc0 A3: w·w′ ≥ 0) exclude W₃-flows with w ≠ 0 that reach MN2. So **no Z2 centre flow is BPS within the truncation, for any gravitino**.
  - **Condition:** the 7D fermion-shift structure is cited (Pernici–Pilch–van Nieuwenhuizen 7D gauged supergravity; the same form is used in the MN/CGR literature). It was not re-derived here, nor was the identification of the 5D N=4 gravitini with the locked sector checked beyond S2-1. A citation does not make this PROVED.
  - If audited, this resolves S2-11 **inside the truncation only**. Spinors that are not constant on Σ (the unlocked, KK, sectors) are outside the truncation and stay in E1-4 and E2.

## 3. What stays open
- **E1-4 (OPEN).** BPS walls with SO(3)_R broken, outside the 3-scalar truncation, remain open:
  - (r, χ, θ)-dependent bulks;
  - SO(2)-invariant or asymmetric data;
  - the [w] branch with KK spinors;
  - E1∩E2 and E1∩E5.

  Neither CH (E1-1) nor the flux route (E1-2) obstructs them. The (r, χ, θ) BPS system is not derived (S2-8, see the S2-8 file). This is the **main live BPS branch**.

## 4. Branch register (t4436; not counted)
- **[w] / Z2:** kept.
  - BPS inside the truncation: excluded conditionally (E1-3) plus PROVED W₃ monotonicity (E23-2).
  - BPS outside the truncation: OPEN (E1-4).
  - Non-BPS NEC walls: OPEN, with numerical evidence against them (S2-12 and today's Z2-corner file).
- **E1:** kept, OPEN (E1-4).
- **[χS], [χU]:** kept. Their E1 intersections are OPEN.
- S2-11: this file proposes CONDITIONAL resolution inside the truncation (E1-3). The 2216 row stays as filed.
- S6 is a record premise.

## 5. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 2 | E1-1, E1-2 |
| CONDITIONAL | 1 | E1-3 |
| OPEN | 1 | E1-4 |
| REFUTED | 0 | — |

Check: 2 + 1 + 1 + 0 = 4.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
