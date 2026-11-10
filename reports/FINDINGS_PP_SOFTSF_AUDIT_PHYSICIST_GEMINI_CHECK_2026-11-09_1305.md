# Soft SF FINDINGS: PP audit of Physicist's pure-math check of Gemini's answers, 2026-11-09 ~13:05 CST (America/Chicago)

**Target files**
- PHYSICIST_CHECK_OF_GEMINI_ANSWERS_2026-11-09_1241.md, sha 3ddf528d… (verified MATCH).
- The questions file GEMINI_ROUND_QUESTIONS_2026-11-09_1238.md, sha 62394b2a….

**Request:** made via Physicist, which reported that the Owner approved it in its chat at 12:52 CST. The audit is in scope under the Owner's 12:29 and 12:33 grants (audits, and additive writes only).

**Rules followed:** pure math only. Nothing was sent to Gemini or any outside service. No CERT. tip 7cddb188 untouched.

**Limit:** Gemini's raw answers are not on disk. They were pasted only in Physicist's chat. So I audit Physicist's mathematical statements, not whether Physicist characterized Gemini fairly. Verdicts of the form "Gemini wrong" are confirmed only as far as Physicist's own counter-statement is true.

**Exact checks** were run in Python: the trace-form signature and π/4.

---

## Section A

### A1: CONFIRM (PROVED)
Quadratic spaces over Q_p are classified by dimension, discriminant and Hasse invariant. Γ48⊗Q_23 is split. This is the same argument as my 12:55 FINDINGS, item 6: at odd p the space is unimodular and ≅ H²⁴.

### A2: CONFIRM (PROVED, given the cited theorem)
- **Hypotheses.** Spin_48 for the Q-form of Γ48 is simply connected and absolutely almost simple. It is isotropic, in fact split, at 23.
- **Strong approximation.** By Kneser and Platonov–Rapinchuk (Thm 7.12), G(Q)·G(Q_23) is dense in G(A).
- **Constancy.** Let φ be in the space of π with π_23 trivial. Then φ is left G(Q)-invariant and right G(Q_23)-invariant. Because G(Q_23) is a normal direct factor of G(A), φ is constant on the dense set G(Q)G(Q_23)g. By continuity φ is constant, so π is trivial.
- **Caveat.** This conclusion is for Spin. For SO, the same argument gives only one-dimensional (a spinor-norm character), not trivial.
- **Remark.** G is Q-anisotropic because it is definite at ∞. So every automorphic form is cuspidal, and "cuspidal" adds no constraint.

### A3: CONFIRM the correction, with a refinement (PARTIAL)
- **The correction holds.** The trace form on F[G] is B(x,y) = τ(xy) with τ(Σ a_g g) = a_e. This gives Q(x) = Σ a_g a_{g⁻¹}, with no minus sign, as Physicist says.
- **Refinement, PROVED.** U(140) ≅ C2×C4×C6 has exactly 8 self-inverse elements, the 2-torsion (Z/2)³.
  - So the Gram matrix of Q is the inversion permutation, with eigenvalue +1 of multiplicity 8+20 = 28 and eigenvalue −1 of multiplicity 20. I verified this exactly.
  - Q has signature (28,20), and Q ≅ ⟨1⟩⁸ ⊥ H²⁰ over Q.
  - So Q gives neither the compact SO(48) nor split SO_48, which would need signature (24,24).
  - The other natural form, Σ a_g², is preserved by the regular representation. It is positive-definite but odd (Z⁴⁸), so it is not Γ48.
- **Conclusion.** "The quadratic form" on F[U(140)] is not determined by the data. The embeddings of 49a1 and Q(√35) remain OPEN.

### A4: CONFIRM (outline correct)
- Local Tate invariants take values in Q/Z.
- For a global class, Σ_v inv_v = 0 is a constraint, not a vanishing statement. Poitou–Tate does not force [ξ] = 0.
- M, ξ and Res_v remain undefined, so this is OPEN.

### A5: CONFIRM (OPEN)
2∏_{i=1}^{23}(23^i+1) counts maximal totally singular subspaces (both families), as verified in my 12:55 FINDINGS. The stabilizer is the Siegel parabolic, not this number. Its use as a local factor value is OPEN.

### A6: CONFIRM (OPEN, numerology)
π/4 = 0.785398…, which differs from 0.7858 by 4.0×10⁻⁴.

---

## Section B

### B1: CONFIRM (PROVED)
- Squaring gives P² = γ⁰(γ⁰)*·K²Π² = γ⁰(γ⁰)*.
- In the Majorana representation γ⁰ is imaginary, so P² = −(γ⁰)² = −1.
- In the Dirac and chiral representations γ⁰ is real, so P² = +1.
- A phase c gives |c|²γ⁰γ⁰*, so no phase can change the sign.

### B2: CONDITIONAL. Physicist's statement needs a caveat.
- For an anti-diagonal P = [[0,A],[B,0]], P² = diag(AB, BA).
- If H₋ = H₊⊗C² fibrewise (spinor rank r on H₊ and 2r on H₋), then rank(BA) ≤ r < 2r. So BA = ±1 is impossible for any fibrewise (local) operator.
- It is possible only through an abstract unitary isomorphism of the infinite-dimensional L² spaces, H₊⊗C² ≅ H₊, which is non-local. That needs a chosen ι.
- So "squares to γ⁰γ⁰* on each block" holds only if B = ±A⁻¹ through an explicit isometry. This stays OPEN until ι is fixed.

### B3: CONFIRM, strengthened (PROVED)
- The premise holds in Majorana. α is real and β is imaginary, KΠ fixes p, and conjugating by β gives P H P⁻¹ = −α·p − βm = −H.
- This differs from the mass flip m → −m, which gives α·p − βm.
- **Strengthening.** γ⁵ commutes with α and anticommutes with β. So γ⁵ H(m) γ⁵⁻¹ = H(−m), which means the sign of m is itself unitarily unobservable in the free theory.
- The spectrum ±√(p²+m²) is symmetric. Energy inversion therefore gives no negative inertial mass.

### B4: CONFIRM (a convention, OPEN)
"−Z" requires the map to include C.

### B5: CONFIRM (OPEN)
No derivation was given.

---

## Section C

### C1: CONFIRM (PROVED). The mismatch is a normalization issue, not REFUTED.
- **Derivation.** Varying S = ∫√−g[R/2κ² − F²/48] gives G = κ²T, with T = (1/6)FF_MN − (1/48)gF². I re-derived this: δF²/δg^MN = 4FF_MN, and δ√−g = −½√−g g_MN δg^MN.
- **Physicist is right.** If G = 2κ²T′, then T′ = T/2, which is half, not double.
- **When the doubled tensor 2T is correct.** It is consistent exactly when G = (κ²/2)(2T). This happens, for example, with L_F = −F²/24, or with T defined as −(4/√g)δ/δg.

### C2: CONFIRM (OPEN), plus a new no-go lemma (PROVED, given the stated block formulas)
- **The lemma.** Any source that is isotropic over the 7D factor AdS5×S² forces G_ext = G_S². That gives 6k² − K_S = 10k², so K_S = −4k² < 0.
- **What this rules out.** This includes the natural Freund–Rubin ansatz F = f·vol_K3 (K3 is a 4D factor, with dual F₇ on AdS5×S²), and it holds with or without Λ11. So that ansatz cannot give K_S > 0.
- **What a source needs.** It must distinguish S² from AdS5, for example flux legs on S² such as F ∝ vol_S² ∧ ω₂(K3).
- **Correction to Physicist's wording.** "Needs a 4D or 7D factor" is not an obstacle here: K3 is 4D and AdS5×S² is 7D. The real obstacle is the isotropy lemma above.

### C3: CONFIRM (OPEN)
G_ext = 6k² − K_S is as given in the questions file. The L7 restatement is OPEN.

### C4: CONFIRM
- SO(16)×SO(16) is the non-supersymmetric 10D heterotic string.
- Bosonic M-theory (Horowitz–Susskind) is conjectural and is 27-dimensional, not 11.
- Standard 11D supergravity admits no Λ (Bautier–Deser–Henneaux–Seminara).
- The "61-puncture" meaning is OPEN.

### C5: CONFIRM (PROVED: dim = 35 − 15 = 20)
- For V35 (OPEN), natural 35-dimensional candidates are dim SL(6,R) = 35, dim Λ³(R⁷)* = dim Λ⁴(R⁷)* = 35, and Sym²₀(R⁸) = 35.
- Λ⁴(R⁷) is the one tied to F4. Whether −1/96 and 1/144 follow from it is OPEN.

### C6: CONFIRM (PROVED)
- If T^L_MN = −T^L_NM, then g^MN T^L_MN = 0.
- The standard trace vector is T_L = T^K_{KL}, with the sign set by convention.

---

## Section D

### D: CONFIRM (PROVED)
- A constant-curvature metric that is also Ricci-flat must be flat: Ric = (n−1)c·g forces c = 0.
- A compact flat 4-manifold has χ = 0 by Gauss–Bonnet–Chern, but χ(K3) = 24. So K3 is not flat.
- The W_49 and θ₁ context items match my earlier FINDINGS.

---

## Net
I agree with Physicist that no PROVED or REFUTED status changes. A5, A6, B5, C2, C3, C4 and C5 (V35) remain OPEN.

**New from this audit**
- A3 refinement: the trace form has signature (28,20). PROVED.
- B2: CONDITIONAL, since a fibrewise P² = ±1 is impossible by the rank count.
- B3 strengthening: the γ⁵ equivalence. PROVED.
- C2: the AdS5×S²-isotropy no-go. PROVED, given the block formulas.

No CERT. REPORTS ONLY.
