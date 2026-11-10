# MR2 FINDINGS — CatB-2 Teitelbaum / Bruhat–Tits harmonic cochains PURSUE (Owner Card 3)
Status: **PARTIAL** (Cat B application; non-squarefree caveat LOCKED)
Owner Write sha a3c8af2f585287673db601167967195e556fa4ce382ae52f73f4fcf8fbcc62e0 (verified) | tip Soft SF LOCK start/end 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | tip_touched Soft SF NO | Soft SF invent HOLD | Soft SF F3 CLOSED | Opt 1 Weil NOT selected | CatB-1 Weil/BKM NOT selected (idle) | Bridge PARTIAL READY NO | **no tip fold** | **does NOT prove P5a** | W-P5a-OP open-to-prove (no FAIL retag)

## Cites
- Owner Write Card 3: OWNER_WRITE_MR2_CATB2_TEITELBAUM_AUTHORIZE_CARD3_2026-10-26.md sha a3c8af2f… — Card 3 APPROVED / AUTHORIZED CatB-2; CatB-1 NOT selected.
- Discipline-search FINDINGS dc0420a8e09cf3e8ee18879f6d82a5080f6a8db8ef2076de079fa64db8470829 — CatB-2 block / row 2.
- Rank 11 FINDINGS 570cc00584bfa735284b99cd3e391b5acff6a7afcca24043dbe8f572b9f0e756 — reused and extended; not contradicted.
- Cat A literature: J. Teitelbaum, "Values of p-adic L-functions and a p-adic Poisson kernel", Invent. Math. 101 (1990), doi:10.1007/bf01231508. Application to residual/P5a seam = Cat B under this Write.

## 1. Setup (Path C Γ₀(49), κ=4, tip k=−2)
Residual torsion cocycles are encoded as Γ-invariant harmonic cochains c: E(T₇)→P² (Sym², dim 3) on the Bruhat–Tits tree T₇ of PGL₂(ℚ₇), with harmonicity Σ_{s(e)=v} c(e)=0 and c(ē)=−c(e). Γ must be an S-arithmetic group with 7 inverted: Γ₀(M)[1/7], 7∤M, or a definite-quaternion {7}-unit group.

## 2. Caveat check (non-squarefree) — FAILS for native application
- Teitelbaum's identification C_har(Γ₀(M)[1/7],P^{κ−2}) ≅ S_κ(Γ₀(7M))^{7-new} requires 7‖level. For N=49=7², there is no M with 7M=49 and 7∤M. **No native level-49 harmonic-cochain space exists in this theory.**
- Only reachable piece: M=1 → level 7 Steinberg newforms, then the ramified quadratic twist χ₋₇ gives the St⊗χ_quad newforms at level 49 (Rank 11 piece (a)). Visibility is **via twist only**.
- Ramified PS π(χ,χ⁻¹) (cond χ=7) and depth-zero supercuspidals at 7 lie outside p‖N theory. → **PARTIAL**, not full applicability.

## 3. What the cochain space sees / does not see
| Piece of S₄(Γ₀(49)) scalar | dim | Seen by cochains? |
|---|---|---|
| Old from level 1 | 0 | No |
| Old from level 7 (St at 7) | 2 | At level 7 only (not as level-49 cochains) |
| New St⊗χ_quad (Steinberg slice) | 1 | Via χ-twist only (PARTIAL) |
| New PS + supercuspidal | 7 | **No** |
| Total | 10 | — |
Does NOT see: full S₄(Γ₀(49),ρ̄) (dim 592), any ρ̄-isotypic or V₄₂ split, PS/SC pieces.

## 4. Numeric
- Scalar (Rank 11 reused, re-evaluated this run via genus formula, python3): dim S₄(Γ₀(1))=0, S₄(Γ₀(7))=1, S₄(Γ₀(49))=10; new(49)=8; St-slice=1; PS+SC=7. dim C_har(Γ₀(1)[1/7],P²)=2 (Darmon two-copy convention). Still valid.
- Sage btquotients test: **not run** — Sage not on box. Cochain dimension above is formula-derived (Teitelbaum iso), not a btquotients computation.
- ρ̄-twisted / V₄₂ split: **ABSENT**. No Written local type of ρ̄ at 7; no matrices or Weil dictionary invented.

## 5. Consequences
- Scalar Steinberg slice is nonzero (dim 1); no vanishing obtained. ρ̄-slice s UNKNOWN; even s=0 would leave o₁+o₇+r of 592.
- **Does NOT prove P5a. Bridge PARTIAL READY NO.** W-P5a-OP stays open-to-prove.

## Soft SF risks (3)
1. Non-squarefree overclaim: treating level-49 as a native cochain space; it is reachable only by twist from level 7.
2. Conflating the scalar St-slice (dim 1) with any ρ̄/V₄₂ vanish or with P5a.
3. Tip-fold temptation: no tip text warranted; FINDINGS-only.

## AUTHOR-WRITE candidate
None written (FINDINGS-only). No clean tip paste is justified at PARTIAL with ρ̄ ABSENT.

Tools: sha256sum (input verify, tip start/end), python3 (genus formula). Sage/Magma unavailable.
