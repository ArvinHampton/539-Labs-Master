# MR2 FINDINGS — CatB-2 Teitelbaum / Bruhat–Tits / residual→resonant DEEPEN
Status: **PARTIAL** (Cat B application; extends PURSUE 02aab8ae…, no contradiction)
Authority (live-verified sha256): OW lift 6bc5f5ab…d917 | ASSIGN 8ae280b4…002d | MR2 ACK d4f13375…86f2 | OW Card3 a3c8af2f…62e0 | prior PARTIAL 02aab8ae…312d | Rank 11 570cc005…e756 | Discipline-search dc0420a8… (cited via prior; file not located by name on disk) | Card1D OW ab8a4937…595a | MR1 local-factor CITECHECK f81d7d33…8ab3
tip Soft SF LOCK start/end 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | tip_touched NO | no tip fold | no AUTHOR-WRITE paste | Bridge PARTIAL READY NO | **does NOT prove P5a** | ρ̄|₇ ABSENT

## Cites
- [Cat A] Teitelbaum, Invent. Math. 101 (1990) (harmonic cochains ↔ p-new forms, p-adic Poisson kernel).
- [Cat A] Darmon, Annals 154 (2001) §1 (C_har(Γ₀(M)[1/p],P^{k−2}) ≅ S_k(Γ₀(pM))^{p-new} ⊕ itself; two-copy convention).
- [Cat A] Dasgupta–Teitelbaum, AWS 2007 notes (p‖N hypothesis).
- [Cat A, standard] Atkin–Li / local Langlands: twist-minimality; p²‖N trivial-char newforms have local type St⊗χ_quad, ramified PS π(χ,χ⁻¹) (cond χ=p), or depth-zero SC.
- On-disk: Card1D OW + MR1 CITECHECK give only a FLOAT T-spectrum hint for ρ̄|cusp6 (3-dim mod-7 factor, exps {3,5,6}/7) — not Written, no exact matrices.

## 1. Residual→resonant (Path C Γ₀(49), κ=4, tip k=−2)
- [Cat A] Cochains detect exactly the 7-new, local-type-Steinberg part at level 7M (7∤M). Integral structure: C_har(Γ,P²_{ℤ₇}) is a lattice; congruences mod 7ⁿ between cochains ↔ congruences between St-type forms (Teitelbaum Poisson kernel / L-invariant context).
- [Cat B] Residual torsion → resonant seam: the only seam the cochain picture can carry is one whose residual class lives in the **St⊗χ_quad slice** (twist of level-7 newform). For residual torsion supported on PS or SC types at 7 (7 of 8 level-49 newform dims), the cochain theory gives **no statement** (neither resonance nor obstruction). Cat B claim: residual→resonant via BT is at best a 1-dim (scalar) statement, ×dim ρ̄-multiplicity, which is unknown.
- No resonance/vanish asserted; no ρ̄-twisted cocycle constructed.

## 2. Deepened cochain dims (python3, genus/Cohen–Oesterlé + newform β-sieve; COMPUTED)
| M | 7M | dim S₄(Γ₀(7M)) | dim 7-new | dim C_har(Γ₀(M)[1/7],P²) (Darmon 2×) |
|---|---|---|---|---|
| 1 | 7 | 1 | 1 | 2 |
| 2 | 14 | 4 | 4 | 8 |
| 3 | 21 | 6 | 6 | 12 |
| 4 | 28 | 9 | 9 | 18 |
| 5 | 35 | 10 | 8 | 16 |
| 6 | 42 | 20 | 18 | 36 |
Level 49 check: dim S₄(Γ₀(49))=10, new=8, new(7)=1, S₄(1)=0 — matches prior. Twist route: only M=1 is relevant to trivial-character level 49 (χ₋₇ ⊗ 7.4 newform → St⊗χ_quad at 49, dim 1). M>1 lands at level 49M, not 49 — **no further level-49 slice gained**. Deepen result: the St-slice at level 49 is **exactly** 1 scalar dim; the BT route is saturated.
- Tree side [Cat A, formula]: Γ₀(1)[1/7]=SL₂(ℤ[1/7]) acts on T₇ (degree 8) with quotient one edge, amalgam SL₂(ℤ)*_{Γ₀(7)}SL₂(ℤ); C_har ≅ ker of the P²-restriction/averaging maps, dimension 2 consistent with table. **Sage absent → btquotients not run; formula-only.**

## 3. Local-type constraint on ρ̄|₇ from on-disk material
- Card1D/MR1: float hint of 3-dim mod-7 factor with T-exponents {3,5,6}/7 (=quadratic non-residues mod 7 ×(1/7)). [Cat B observation, not proof] This pattern is compatible with a Weil/Nobs–Wolfart irrep of SL₂(ℤ/7) of dim 3 (one of the two 3-dim (p−1)/2 pieces). If confirmed exactly, ρ̄|₇ would be nontrivial at 7, so ρ̄-isotypic level-49 pieces would **not** reduce to scalar St⊗χ slice — further limiting the BT route. **Not Written; no matrices invented. ρ̄|₇ remains ABSENT.**

## 4. Vanish / non-vanish vs 592 = 503 ⊕ 89
- Seen: scalar St slice dim 1 (nonzero) — no vanishing.
- Not seen: any ρ̄-multiplicity, V₄₂ split, PS/SC pieces, 503 or 89 component decomposition. BT cochains bound nothing about 592. No vanish invented.

## 5. Status
- Bridge PARTIAL READY NO. **Does NOT prove P5a**; W-P5a-OP open-to-prove.
- Remaining non-blocking pendings: Eigen 89-basis exact; Owner-Written ρ̄|₇; Soft SF depth pin.

## Soft SF risks (3) — Auditor press YES
1. Reading the {3,5,6}/7 float hint as a Written ρ̄|₇ local type.
2. Treating "BT saturated at dim 1 scalar" as a vanish statement for the 89 or 503 summand.
3. Claiming residual→resonant beyond the St⊗χ slice (PS/SC are outside Teitelbaum theory at 7²).

Tools: sha256sum, python3+sympy. Sage/Magma unavailable.
