# NL DERIVED: D6 stage 3 (c), E5: U(1)_R breaking, and the chirality / HW-projection lemma (CH)
2026-11-10, 1019 CST (America/Chicago). **NL derived proposal.** Additive only; no existing file edited.
Authority: Owner call-83d7a0fa record (e72a188b…, sidecar OK); standing OW t4436 (32881263…: the math leads; every option a labelled branch; only PP-audited PROVED/REFUTED keep or drop a branch); OW t4431 (f700141d…). Inputs: 2216 (f504d1b9…), PP f530cbc0… §3, Erratum 23 (4bdfb71c…), 2245 files (e3ff699e…, 3ceb0605…), PP 113e8035…, Erratum 24 (60bbc718…). Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged. No candidate wall.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.
Script: /workspace/nl-d6s3-1110/chirality_hw_lock_exact_2026-11-10.py (3ed7f879…, sidecar frozen before the run); log 676f7dc8… (sealed after). Exact Clifford(1,10) over ℚ(i): exact matrix equality and exact rank only; no `simplify(...)==0`.

**Tally: PROVED 6 · CONDITIONAL 0 · OPEN 1 · REFUTED 0 · total 7.**

## 0. Scope and premises
- **Branch E5:** SO(3)_R kept, U(1)_R broken. Sub-branches: **E5∩H_Σ** (twisted-SL(2,ℝ)-invariant lift, i.e. Σ-uniform up to the twist) and **E5∩¬H_Σ** (= E2∩E5).
- Common premises (labelled where used): (h1) warped product with flat Poincaré x-slices, warp x-independent; no flux with 1–3 x-legs (G₀₁₂₃ allowed); (P-a) at least one Killing spinor; (ii) HW-type ℤ₂: ε(−r) = Γ_nε(r), ε continuous at the wall, so Γ^nε = ε on the face (D1 hypothesis (ii) of 2017; the odd HW ℤ₂ is the **record premise S6**, f825dfff); (reg) at one face point p ∈ C₄ the metric is smooth and nondegenerate and ε and the supercovariant connection are continuous up to the face; (tw) the lift carries the vacuum twisted action (K acts on the fibre through the vacuum U(1)_R rotation of μ_a).
- Frame at p ∈ C₄: (0..3 | r | S1,S2 | m1,m2 | t,f) as in 2216; Γ^{S12} = is₁, Γ^{m1m2} = is₂′, Γ^{tf} = is₃, χ₄ := eigenvalue of Γ^{0123} (±i).

## 1. What H_Σ forces when U(1)_R is broken
- **E5-1 (PROVED). Charge pairing under H_Σ.** Let K ≅ SO(2) be the stabiliser of p̃ ∈ H² in the twisted SL(2,ℝ). SL(2,ℝ)-invariant tensor fields on the lift correspond one-to-one to K-invariant tensor fields on the fibre over p̃ (homogeneous bundle G×_K V: an invariant section s satisfies s(gK) = g·s(eK), well defined iff s(eK) ∈ V^K). K acts on Σ-indices by rotation (charge q_Σ) and on the fibre by the vacuum U(1)_R (charge q_R), so a K-invariant component has **q_R = −q_Σ**.
  - G components with 0 or 2 Σ-legs have q_Σ = 0 (two Σ-legs of a form give the area form), hence are **U(1)_R-invariant**. Components with one Σ-leg have q_R = ∓1. With P-c (no single-Σ-leg G), **all of G is U(1)_R-invariant**.
  - Metric: components with no Σ index and the trace of g_ΣΣ are U(1)_R-invariant. U(1)_R can be broken only by (i) one-Σ-index cross terms g_{Σ M} (q_R = ∓1) and (ii) the traceless part of g_ΣΣ (q_R = ∓2).
  - So **E5∩H_Σ∩P-c requires a nonzero metric term of type (i) or (ii)**; the flux cannot carry the breaking.
- **E5-2 (PROVED, implication). The twist lock and the C₄ isotopy premise survive in E5∩H_Σ.**
  - PP's §3 proof of S2-4 (f530cbc0; checked in Erratum 23) uses only invariance under the twisted SL(2,ℝ) and the stabiliser's spin action. It never uses U(1)_R separately. So on E5∩H_Σ every Killing spinor at C₄ satisfies (Γ^{S12} + Γ^{m1m2})ε = 0.
  - Here C₄ is defined as the K-fixed set over Σ. By (tw), the fixed set of K in the fibre is {μ_a = 0}, which is **the vacuum set itself** in bundle coordinates. So the F-4 premise "C₄ isotopic to the vacuum U(1)_R-fixed locus" (Erratum 24) **holds automatically on E5∩H_Σ**.
  - Frame: K acts on the charge-1 part of T_p as a complex structure on ℂ² ⊃ L_S (the Σ-coordinate line, tangent to C₄). Take e_S orthonormal in L_S and e_m orthonormal in L_S^⊥. Both are K-invariant complex lines, so the stabiliser still acts on spinors as ½(Γ^{S12} + Γ^{m1m2}), even with cross terms of type (i).
  - The unit normal n at p is invariant under K and U(1)_n̂ and orthogonal to x, so **n = ±∂_r**.

## 2. The chirality / HW-projection lemma and the E5∩H_Σ no-go
- **E5-3 (PROVED; exact). Lemma CH.**
  - (a) Γ^{0}Γ^{1}…Γ^{10} = 1 exactly (log [1]).
  - (b) Γ^{0123} commutes with every internal Γ^y (y = r…f) and anticommutes with each Γ^μ (log [2]). So it commutes with the internal spin connection, all internal flux terms, the x-row operator after factoring Γ_μ (including the electric term ∝ Γ^{0123}), the HW projector Γ^n, and the Kosmann action of SO(3)_R, U(1)_R and K.
    - Hence the complexified Killing spinors split by 4D chirality χ₄. Every SU(2)_R multiplet can be chosen chiral, and **both members of a doublet have the same χ₄**.
  - (c) On every nonzero joint eigenspace, χ₄·γ_r·(is₁)(is₂′)(is₃) = 1 (log [3]: a single value over all 16 nonzero spaces, each of dimension 2).
  - (d) On the locked subspace ker(Γ^{S12} + Γ^{m1m2}) with Γ^r = +1 and fixed χ₄, **only one value of s₃ occurs**: dimensions (0, 4) for χ₄ = i and (4, 0) for χ₄ = −i (log [4]). For n = −∂_r the surviving s₃ is reversed, and the conclusion is unchanged.
  - (e) Control: without the lock, both values of s₃ occur, with dimensions (4, 4) (log [6]). So it is the lock that does the work.
- **E5-4 (PROVED, implication). No HW-BPS wall in H_Σ∩SO(3)_R, with or without U(1)_R.**
  - Premises: (h1), (P-a), (ii), (reg) at one face point p ∈ C₄, (tw), H_Σ, SO(3)_R.
  - Proof:
    1. By S2-3, Killing spinors form SU(2)_R doublets. Its proof uses only the U(1)_n̂ weights ±½ at p and the injectivity of ev_p, which holds up to the face under (reg). U(1)_R is used there only for the s₂′ statement, which is not needed here.
    2. Choose a chiral doublet (E5-3(b)). Its members are nonzero at p, have opposite s₃ (weights ±½), share χ₄, are both locked (E5-2) and both satisfy Γ^nε = ε, with n = ±∂_r.
    3. This contradicts E5-3(d). ∎
  - **Not used:** the magnetic-only premise (G₀₁₂₃ is allowed; it is in any case removed by E3), σ, the D1 rows, Bianchi, N_face, the IR endpoint (S5), U(1)_R, and the source profile n(χ), provided the data are regular at one face point of C₄.
  - Consequences:
    - On **E5∩H_Σ**, branch E5 is **proposed for dropping on this PROVED implication, pending PP audit** (t4436).
    - On **scope S** this is an independent, flux-free route to the conclusion of S2-7. S2-7 itself stays CONDITIONAL as filed; this file does not relabel 2216.
    - Covers **[χU]** and **[χS]** whenever the wall content leaves (reg) true at some point of C₄. A [χS] profile with δ-support at χ = π/2 (= C₄) falls under E4.
  - Remark (hygiene, no label): by log [3], the "same s₁, opposite s₃" partner pairs of S2-6 / PP C1 have **opposite** χ₄ at Γ^r = +1. They are therefore never the two members of one SU(2)_R doublet at a wall point. S2-6's algebra stands, but the case it treats is not realised; E5-4 supersedes it as the operative obstruction.
- **E5-5 (PROVED; exact). Without chirality, the D1 rows alone would not close E5.**
  - For both σ and arbitrary (f₄, ω₁, ω₂), each single sector with Γ^r = +1 solves D1 with a unique diagonal K (log [7], [9]); this reproduces the 2100 D6-2 formulas, e.g. k_x = (f₄+ω₁+ω₂)/6 on (+,+,+), σ = +1.
  - The conjugate locked sectors (s₁,−s₁,s₃) and (−s₁,s₁,−s₃) give **identical K** (log [8], 8/8) but have **opposite χ₄**, so they are complex conjugates of each other, not doublet partners.
  - Hence the flux/D1 route by itself leaves ω₂ free on E5. The closure on E5∩H_Σ comes from E5-3/E5-4.

## 3. Where E5 stays open
- **E5-6 (OPEN). E5∩¬H_Σ** (U(1)_R broken and data not uniform on Σ, SO(3)_R kept).
  - The lock (which needs H_Σ) and a global s₂′ (which needs U(1)_R) are both unavailable.
  - At a wall point of C₄, CH (log [3]) gives only that s₁s₂′s₃ is fixed by χ₄, so doublet members have opposite s₁s₂′. No contradiction was found.
  - The degree argument of the E2 file needs U(1)_R. Not attempted further here.
- **E5-7 (PROVED). [w] inside the 3-scalar truncation is not an E5 configuration.**
  - In the uplift used by all Z2 scripts, w enters only T_αβ = e^{4λ}diag(e^w, e^w, e^{−2w}) for α = 3,4,5. Δ = e^{−6λ}cos²χ + sin²χ e^{4λ}(e^w sin²θ + e^{−2w}cos²θ) depends on μ_a only through cos²χ = |μ_a|².
  - So U(1)_R (rotation of μ₁,μ₂) is unbroken on [w], and C₄ = {μ_a = 0} is unchanged there.
  - [w] breaks SO(3)_R to SO(2), so it belongs to E1, where E5-4 does not apply (it needs SO(3)_R). [w]∩E5 exists only outside the truncation.

## 4. Branch register (t4436; not counted)
- **[χS], [χU]:** kept. They are covered by E5-4 on E5∩H_Σ whenever (reg) holds at some point of C₄. δ-support on C₄ goes to E4.
- **[w] / Z2:** kept. On [w], U(1)_R is unbroken (E5-7) and SO(3)_R is broken, so it falls under E1. Z2 is not BPS in the truncation (S2-10, E23-2).
- **E5∩H_Σ:** proposed drop on E5-4 (PROVED implication), **pending PP audit**. Not dropped by this file.
- **E5∩¬H_Σ:** OPEN (E5-6).
- E3 and S5 (BPS) were dropped earlier, unchanged. Open: E1 (+S2-11), E2, E4, S2-8, Z2 corner / S2-13, non-BPS S5 (S3b-4). S6 is a record premise.

## 5. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 6 | E5-1, E5-2, E5-3, E5-4, E5-5, E5-7 |
| CONDITIONAL | 0 | — |
| OPEN | 1 | E5-6 |
| REFUTED | 0 | — |

Check: 6 + 0 + 1 + 0 = 7.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
