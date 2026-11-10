# JOINT — Local addendum to NL B2 closures (A) vs (B) comparison — 2026-11-09

- Lane: Local Path. Written Nov 9, 2026 (~1:30 PM CST, America/Chicago) under Owner DIRECT (~1:06 PM CST, Physicist pos 17629). Additive new file; NL files not edited. No CERT. Tip 7cddb188… untouched. Nothing sent outside. **B2 is NOT closed.**
- Local A (written first, independently): reports/FINDINGS_LOCAL_DERIVE_PREV_CONSTRUCTION_A_DIRECT_SUM_ISOMETRY_2026-11-09.md, sha 4b25d2edf14b887038186ac2d4b580bacb106b3811456fceeea702f08c8a783f.
- NL files checked: NL_DERIVED_B2_CLOSURE_A_DIRECT_SUM_NONLOCAL_IOTA_2026-11-09_1315.md (988f1436…) = "NL-A"; NL_DERIVED_B2_CLOSURE_B_TWO_SECTOR_HxC2_OPTIONS_M_D_2026-11-09_1315.md (5907eaf3…) = "NL-B"; NL_B2_CLOSURES_A_VS_B_COMPARISON_2026-11-09_1316.md (cd227dc7…) = "CMP".
- Notation: A₀ := γ⁰KΠ on H = L²(ℝ³)⊗ℂ⁴; η := A₀² = γ⁰γ⁰* (−1 Majorana, +1 Dirac/chiral). Small numpy fibre checks only.

## 1. NL's closure (A), item by item
- **A-1 (NL-A:5) — CONFIRM.** Q(ψ,χ) = (Bχ, Aψ) ⇒ Q² = (BAψ, ABχ); Q² = ε ⇔ BA = ε, AB = ε ⇔ A bijective, B = εA⁻¹; isometry of Q ⇔ A, B isometric. Same as Local A result 2. Scope: anti-diagonal (pure-swap) Q only.
- **A-2 (NL-A:6) — CONFIRM.** V := A∘(KΠ) is linear unitary with V M_f V⁻¹ = M_f, hence decomposable with fibres u(x): ℂ⁴→ℂ⁸ unitary a.e., impossible. Same as Local A result 6.
- **A-3 (NL-A:7) — CONFIRM.** e_{2N}↦e_N⊗f₁, e_{2N+1}↦e_N⊗f₂ is a bijection of orthonormal bases ⇒ unitary. Same as Local LD-A4.
- **A-4 (NL-A:8) — CONFIRM math, DISPUTE conclusion.** With B = εA⁻¹ one has Q² = ε for either ε (true). But εA⁻¹ = εη·(A₀∘ι*) since A₀⁻¹ = ηA₀. Choosing ε is choosing the backward map ±A₀ι*. If B2 requires the same operator in both directions (B = A₀∘ι*, Local LD-A1/A4), then Q² = η, fixed by the representation and independent of ι. So "P_rev² = −1 has no mathematical content in (A)" holds only if the backward sign is left free; the same freedom exists in (B) (see §3, point 1).
- **A-5 (NL-A:9–12).** (i) CONFIRM: the formula holds only up to ι. (iii) CONFIRM: ι is basis-dependent. **(ii) DISPUTE.** It is correct that Q H_tot Q⁻¹ = −H_tot forces H₋ = −A H₊ A⁻¹. But "non-local because ι is" does not follow. In the Majorana rep, H₋ = −ιA₀HA₀⁻¹ι* = ιHι*. This equals the local H⊗1₂ iff ι intertwines H with H⊗1₂. Such a unitary ι exists: free Dirac H ≅ diag(E·1₂, −E·1₂) (Foldy–Wouthuysen) has absolutely continuous spectrum of uniform infinite multiplicity, as does H⊗1₂, so H ≅ H⊗1₂ (Hahn–Hellinger). Local A result 7. That ι is necessarily non-local (A-2), but H₋ itself can be the local H⊗1₂. Hence "non-local −U dynamics is required" is REFUTED as a necessity (existence counterexample); the Hermite ι of A-3 need not intertwine (explicit intertwiner OPEN).
- **A-6 (NL-A:13) — CONFIRM.** Q² = ε on H₊⊕ran ι₀, 0 on H₊⊗f₂. Same as Local A result 1, i.e. Q² = η·diag(1, ιι*).
- **NL-A:14, "a local version needs equal fibre ranks, i.e. closure (B)" — DISPUTE.** This holds only for pure-swap Q. Local LD-A3 (complement fix) gives a local P_rev on the literal H₊⊕(H₊⊗ℂ²):
  - Q = A₀⊗(S∘K₃) on H⊗ℂ³, with S the permutation (1 2) and ι = ι_{e₁};
  - Q is antiunitary with Q² = η·1 on the full space;
  - Q(H₊) ⊂ H₋, and P_rev ψ = γ⁰ψ*(−x)⊗e₁ literally;
  - Q is x-local;
  - in the Majorana rep it anti-commutes with H ⊕ (H⊗1₂);
  - cost: it does not map all of H₋ into H₊, since R = H₊⊗e₂ is mapped to itself by A₀.

## 2. NL's closure (B)
- **B-1 — CONFIRM.** P̂ is antiunitary.
- **B-2 — CONFIRM.** (γ⁰Π⊗U)K(γ⁰Π⊗U)K = γ⁰γ̄⁰ ⊗ UŪ (Π real, Π² = 1). Here "γ⁰*" means the complex conjugate.
- **B-3 — CONFIRM.** U = [[0,a],[b,0]] ⇒ UŪ = diag(ab̄, bā), so P̂² = η·ab̄ when ab̄ = ±1.
- **Option M — CONFIRM.** Numpy (Majorana, random p, m): P̂² = −1 and P̂(H⊗1)P̂⁻¹ = −H⊗1. The H⊗σ_z remark is confirmed: σ_xσ̄_zσ_x = −σ_z, so P̂ commutes.
- **Option D — CONFIRM.** Numpy (Dirac rep): A₀² = +1, (iσ_y)(iσ_y)‾ = −1, P̂² = −1. A₀HA₀⁻¹ ≠ ±H, so P̂ is not a fixed-t symmetry.
- **Local identity (PROVED, Local A §3).** Local LD-A3 restricted to H₊⊕ιH₊ ≅ H⊗ℂ² is exactly Option M. So LD-A3 = M ⊕ (A₀ on the cokernel R).

## 3. Disagreements with CMP (NL-1316)
1. **Row "P² = −1" — DISPUTE ("free in (A), forced in (B)").** Both constructions give P² = η·s, where η is fixed by the representation and s = ±1 is the relative sign of the backward map:
   - in (B), s = ab̄. Numpy: Majorana with U = iσ_y gives P̂² = +1;
   - in (A), s = εη.

   Option M's −1 is "forced" only after fixing U = σ_x. The analogous fix in (A), B = A₀ι*, forces Q² = η just as rigidly. The two are on equal footing.
2. **Row "Fixed-t symmetry: (A) only with non-local H₋" — DISPUTE.** A unitary intertwining ι gives the local H₋ = H⊗1₂ (existence PROVED; explicit form OPEN).
3. **Missing column — Local A3 (complement, literal 4/8 fibres).**
   - inter-sector map: local;
   - Owner formula: holds literally (⊗e₁);
   - P²: η (−1 in Majorana);
   - fixed-t symmetry: Majorana only;
   - canonical: up to the unit vector e and the choice of J on R;
   - not a pure swap.
4. **Assessment line (CMP:14), "Option M is the only closure in which…" — DISPUTE as stated.** On the literal space, Local A3 also has the Owner formula literally, P² = −1 (Majorana) and the fixed-t symmetry. It differs from M only by the extra sector R on which P_rev acts as A₀. M is the only one among pure-swap, equal-rank closures (CONFIRM in that restricted form).
5. **Agreements:**
   - fibre ranks 4/8 vs 4/4;
   - the (A) pure-swap ι is non-local and non-canonical;
   - D is not a dynamical symmetry;
   - the gamma representation needed is Majorana for M and Dirac/chiral for D.

## 4. Status
B2 remains **CONDITIONAL** on the Owner's choice among:
- (B)-M;
- (B)-D;
- (A) pure-swap with non-local ι;
- Local A3, complement on the literal space.

Physical reading: OPEN. Not a CERT. Preliminary until PP audits.

## Rollup
CONFIRM 13 (A-1, A-2, A-3, A-4 math, A-5(i), A-5(iii), A-6, B-1, B-2, B-3, M, M-remark, D) · DISPUTE 6 (A-4 conclusion, A-5(ii), NL-A:14, CMP rows P² and fixed-t, CMP:14 "only closure") · new PROVED 2 (LD-A3 = M ⊕ A₀|_R; P² = η·s sign bookkeeping) · OPEN 1 (explicit intertwining ι) · REFUTED 1 (the necessity of non-local −U dynamics in (A)).
