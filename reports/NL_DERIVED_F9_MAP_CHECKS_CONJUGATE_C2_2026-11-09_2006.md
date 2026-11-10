# NL DERIVED: F9 script fix — map_checks with the ℂ² factor conjugated
2026-11-09, 20:06 CST (America/Chicago). **NL derived proposal.** Nothing here is adopted. Junction status: **UNSOLVED**, unchanged.

Authority: **OW t4426** OWNER_WRITE_MAINCHAT_t4426_PURSUE_ALL_OPEN_JUNCTION_ROUTES_2026-11-09_1956.md = d5eaeef3f6b53270bd09e30053f6cdbf442d191c58a0a9fda30daff83907ffb3 ("Pursue all open"; queued F9). Also E16-F9 (NL_ERRATUM16_ACCEPT_PP_5b5dddd3_3982a4b8_fb515bef_2026-11-09_1951.md = 6eb2fccd…), PP 5b5dddd3 F9, and the 1901 target NL_CANDIDATES_BULK_TO_HC2_MAP_PHI_Q3_2026-11-09_1901.md = ff95449ae3c374ea3975df2ec142681c0b1a3fa39fb5a3322431df33bba85c55. Naming per OW f1d167d1: where the algebra is named it is "resonant algebra" (it is not named in this file). OW 36683379: citations checked, never upgrade alone.

Limits: additive only. The original script /workspace/nl-cand-1854/map_checks.py (11e97edf8d6ab1f651aa9389bc704e8218388d944307a10ce73e69f9d5c024d8) is **not edited** (re-checked after the run). No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after. χ-smearing does not enter this item.

**Tally: PROVED 2 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · total 2**

## 1. Script and run

New dated directory `/workspace/nl-f9-map-2005/`, all with sidecars:
- map_checks_conjugate_C2_2026-11-09_2005.py = 493f79190367a849cda3456d873abb72bbb5f6ed8cf045cd3f8f36d33abcb6c7, **frozen before execution**
- map_checks_conjugate_C2_2026-11-09_2005.log = d8b48524ddc31cce5b9162833769b934c400ff3dc85296a203e43199d5fc487a, written after the run

The new script is a copy of the 11e97edf… original, plus the F9 MC1 block. The original MA2, MA3, MB1, MB2 checks are reproduced byte-for-byte in the printed lines and give the same booleans as map_checks.log (4e70e9a4…). The original (incorrect) linear-projector test is also reproduced, labelled as not used: a generic SU(2) element fails to commute with |e₂⟩⟨e₂|, while U = exp(−i θ σ_z) does commute with it. That is why 1901 MC1 claimed a residual U(1)_{T₃}.

The F9 fix uses the same conjugation convention as A0c2 already did on H⊗ℂ² (M ↦ (γ⁰⊗1) M.conj() (γ⁰⊗1)⁻¹, which conjugates both factors). T1 is antiunitary: T1 = (A₀ ⊗ P₂) ∘ K in the e-basis, with P₂ = |e₂⟩⟨e₂|. The condition T1 U = U T1 is **P₂ Ū = U P₂**, not [U, P₂] = 0.

## 2. Results

- **F9-cex (PROVED; exact 2×2 algebra, confirmed numerically and by the H⊗ℂ² lift).** T1 does not commute with the U(1)_{T₃} element U(θ) = diag(e^{−iθ}, e^{iθ}) except at the centre. Exactly,
  P₂ Ū(θ) − U(θ) P₂ = diag(0, −2i sin θ).
  At θ = π/2 this is diag(0, −2i) ≠ 0, which is the E16-F9a counterexample. On a generic vector in H⊗ℂ², T1 ∘ (1⊗U(0.9)) differs from (1⊗U(0.9)) ∘ T1 (residual 2.228…). This confirms, by a new script, that 1901 MC1 as stated is REFUTED (the refutation itself was already counted in E16-F9a and is not re-counted here).

- **F9-b (PROVED; exact 2×2 algebra, confirmed by the H⊗ℂ² lift).** For a general 2×2 matrix U = [[a, b], [c, d]],
  P₂ Ū − U P₂ = [[0, −b], [c̄, d̄ − d]].
  So P₂ Ū = U P₂ forces b = 0, c = 0 and d real. In SU(2) (ad − bc = 1 and a = d̄) this is d² = 1, hence **U = ±I**: the commutant of T1 in SU(2)_R is the centre ℤ₂. Further, P₂ Ū(θ) − U(−θ) P₂ = 0 identically, so **T1 U(θ) = U(−θ) T1** (equivalently T1 U(θ) T1⁻¹ = U(−θ) on the range of T1). On a generic vector the H⊗ℂ² residual of T1 ∘ (1⊗U(0.9)) − (1⊗U(−0.9)) ∘ T1 is 0. Both ±I commute with T1. A0c2(1⊗U(θ)) = 1⊗Ū(θ) holds, so the conjugation of the ℂ² factor is the same operation A0c2 already used.

## 3. Impact

- The 1901 revised tally remains **9/7/4/1** as in E16 §4 (MC1 REFUTED; MA1, MA4, MA5, PA1 CONDITIONAL; PP3 PROVED). This file does not re-open or re-count those items.
- The queued E16-F9 script fix is now done. The original script is untouched.
- **The count gap is unchanged. The junction remains UNSOLVED.** Nothing in the map algebra affects either.

## 4. Tally (header checked)

| label | count | items |
|---|---|---|
| PROVED | 2 | F9-cex, F9-b |
| CONDITIONAL | 0 | — |
| OPEN | 0 | — |
| REFUTED | 0 | — |

Check: 2 + 0 + 0 + 0 = 2. The reproduction of the original MA/MB lines and of the incorrect linear-projector test is hygiene and carries no label. MC1's REFUTED grade lives in E16, not here.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
