# MR2 FINDINGS — DUAL CONTINUE — sigma-gaps (G-1 / G-2 / G-3 from sigma-conv 79332047…) — 2026-10-27
STATUS: PARTIAL. REPORTS ONLY — no RECS; no P5a; Bridge PARTIAL READY NO; G1 BLOCKED (no OMS / L₇); Kerr BLOCKED; no tip fold.
Dual-label filtration: 10 ∥ 40 — BOTH NAMED PARALLEL, NO PICK. sigma-conv dual σ-label (SF-C2) RETAINED, NO PICK.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before = after; tip_touched NO).
Builds on: sigma-conv 79332047… (SF-C1–C5), kappa7-tres fd5e0dc1… (SF-K4/K5), end-seg 0111d12e… (SF-H3), bm-sigma c72bae05… (SF-S2), hu-tan-L1 c925e73d…, residual-mult-bm 0e00b2d2….

## G-1 — In what convention is the project's L₂ written?
| # | Source (quoted) | Content | Soft SF reading |
|---|---|---|---|
| 1a | end-seg l.20: "the endpoint with sub ω and quotient ω² realises κ(u) ∈ H¹(G_S, ω⁻¹)" | L₂ defined by SUB/QUOTIENT | intrinsic Galois-module statement |
| 1b | kappa7-tres SF-K4: "L₂ (sub ω, quotient ω²) has class in H¹(G_Q₇, ω⁻¹)" | same, local | intrinsic |
| 1c | kappa7-tres SF-K5: "L₂ = the unique ramified non-split extension of ω² by ω" | iso class fixed, "no further choices" | intrinsic |
| 1d | residual-mult-bm l.21: "L₂ ≅ (ω *; 0 ω²)" ; bm-sigma SF-S2: "L₂ ≅ ω ⊗ (1 *; 0 ω)" | matrix form | upper-left = SUB (consistent with 1a–1c) |
Outcome G-1: CLOSED Soft SF. The project's L₂ is specified convention-free as 0 → ω → L₂ → ω² → 0; the matrices in 1d are the standard "upper-left entry = sub" transcription. The open question therefore moves entirely to how each SOURCE's matrix encodes sub/quotient (→ G-2, G-3); L₂ itself carries no V̌ convention.

## G-2 — Is Hu–Tan p₁ the component for the extension (1 *; 0 ω)?
| # | Hu–Tan quote (lit/bm/1309.1658.txt) | Line |
|---|---|---|
| 2a | "consider a non-split extension 0 → 1 → ρ1 → ω → 0. The construction of R1 = Rver(ρ1) provides the following description of the pseudodeformation ring" | l.1287–1288 |
| 2b | "Recall that ρ1 denotes a non-split extension of ω by 1 … Theorem 4.2. … Ann(M1(Θ)) ≅ I_irr^ps ∩ I_1^ps … Z1(Rps/(I_irr^ps ∩ I_1^ps, ϖ)) = a_{p−3,1} J" | l.1688–1702 |
| 2c | proof: "V̌(N1) is isomorphic to the universal deformation of ρ1 by [25, Cor 10.72] … Z1(Rver(k,τ,ρ1)/ϖ) = a_{p−3,1} Z1(M1(σ_{p−3,1})) = a_{p−3,1} J" | l.1710–1724 |
| 2d | I_1^ps: traces of reducible reps "containing a one-dimensional sub-representation lifting 1 … with the higher Hodge-Tate weight" | l.1640–1644 |
| 2e | "Proposition 5.2 (ii) The quotient ring Rver/(I1ver + (ϖ)) has at most one minimal prime ideal p1" | l.2234 |
| 2f | "Proposition 5.5. For i = 1, 2 … ℓ(Rver(k,τ,ρ)_{p_i}/ϖ) = ℓ(R_J^ps/(I_irr^ps ∩ I_i^ps, ϖ))" | l.2413–2416 |
| 2g | "Theorem 5.11 … Z(Rver(k,τ,ρ)/ϖ) = a_{p−3,1} p1 + a_{0,0} p2 + a_{p−1,0}(p2+p3)" ; "Proof. Theorem 4.2, Theorem 4.10 and Proposition 5.5 imply ℓ(Rver(k,τ,ρ)_{p1}/ϖ) = a_{p−3,1}" | l.2758–2764 |
| 2h | N1 = projective envelope of πα^∨, "πα := Ind_P^G (ω ⊗ ω^{-1})" | l.1676–1681 |
MATCH: p₁ (2e,2g) ↔ type-1 ideal I₁ (2d) ↔ M1 / ρ1 (2b,2c,2f); ρ1 is quoted with explicit exact sequence 0→1→ρ1→ω→0 (2a), i.e. (1 *; 0 ω) sub-upper-left; its BM weight is σ_{p−3,1} = Sym^{p−3}⊗det (2c).
Outcome G-2: CLOSED Soft SF (the hu-tan-L1 inference is now quote-supported: the p₁ multiplicity a_{p−3,1} is that of the non-split ρ1 = (1 *; 0 ω) ring, in Hu–Tan's own sequence notation, with the same V̌ as Paškūnas, SF-C4/H1).

## G-3 — Source of the generic orientation swap
| # | Quote | Line | Bearing |
|---|---|---|---|
| 3a | Paškūnas §6 intro: non-generic "ρ ≅ (χω *; 0 χ)" | 1209.5205 l.2610–2612 | intro orientation |
| 3b | Paškūnas Prop 6.1 proof: "If ρ ≅ (χ *; 0 χω) then by [53, Lem.10.16] … 0 → (τ1⊗χ∘det)^∨ → k⊗̂P̃ → (Ind χω⊗χω^{-1})^∨ → 0" (35); generic Ind case stated for "χ1χ2^{-1} ≠ 1, ω^{±1}" | l.2650–2668 | OPPOSITE orientation to 3a for the same [53 §10] / πα=Ind(ω⊗ω^{-1}) object; ratio ω^{-1} excluded from the Ind case |
| 3c | Paškūnas §6.2: "β … semi-simplification (Sp ⊕ 1 ⊕ πα)⊗χ∘det, πα := Ind ω⊗ω^{-1} … V̌(β^∨) ≅ ρ … ρ ≅ (ω *; 0 1)" | l.2809–2826 | πα attached to 3a orientation |
| 3d | Hu–Tan: ρ1 with 0→1→ρ1→ω→0 uses N1 ↞ πα^∨, πα = Ind(ω⊗ω^{-1}), and [25, Cor 10.72] | 1309.1658 l.1676–1710 | πα attached to sub=1 (3b orientation, read sub-upper-left) |
| 3e | Paškūnas Rem 6.2: "(χ1 *; 0 χ2ω^{r+1})⊗ω^m … π ≅ (Ind χ1⊗χ2ω^r)⊗ω∘det" | l.2715–2722 | for (1 *;0 ω) (r=0,m=0) gives Ind(1⊗1), ≠ the Ind(ω⊗ω^{-1}) of 3b/3d |
| 3f | Paškūnas: CLFT "so that uniformizers correspond to geometric Frobenii"; "V̌(M) := V(M^∨)^∨(εζ)" | l.1351–1352; l.1378 | normalisation only; no sub/quot swap stated |
| 3g | Gee–Kisin 1208.3179: "normalise so that uniformizers correspond to geometric Frobenius elements"; "all of our definitions are dual to those of [BM02], but … can be translated into their setting by taking duals" | l.260; l.292–293 | a NAMED duality vs Breuil–Mézard's original HT convention; not stated as a sub/quot swap |
| 3h | Emerton–Gee–… 1310.0831: same geometric-Frobenius CLFT normalisation; "We write all matrix transposes on the left" | l.700–704 | no orientation statement found |
Outcome G-3: PARTIAL Soft SF. Located: (i) a quoted internal orientation inconsistency in Paškūnas (3a vs 3b, same [53 §10]/πα object written (χω *;0 χ) and (χ *;0 χω)); (ii) a quoted mismatch between Rem 6.2's Ind formula (3e) and Prop 6.1/(35) + Hu–Tan (3b,3d) on the ratio-ω^{-1} case; (iii) a named convention duality in Gee–Kisin (3g). Remains OPEN (named reason): no quoted line in 1209.5205 / 1208.3179 / 1310.0831 states which matrix slot is the sub in Paškūnas Rem 6.2, nor derives Rem 6.2 from [53] (Prop 6.1 / Cor 8.7 of [53] not on disk); BM02 / BDJ / Breuil [6,7] not on disk.

## Soft SF facts
- SF-G1 (CLOSED): project L₂ is intrinsic, 0 → ω → L₂ → ω² → 0 (end-seg SF-H3, kappa7-tres SF-K4/K5); no V̌/matrix convention enters its definition.
- SF-G2 (CLOSED): Hu–Tan p₁ ↔ I₁ ↔ ρ1 with 0→1→ρ1→ω→0, multiplicity a_{p−3,1}, weight σ_{p−3,1} (Thm 4.2, Prop 5.2(ii), 5.5, Thm 5.11). The hu-tan-L1 p₁ ↔ (1 *; 0 ω) link is quote-supported.
- SF-G3 (fact, label only): under SF-G1 + SF-G2 the intrinsic L₂ = ω ⊗ ρ1 lies on the BDJ-labelled side of SF-C2 ({Sym⁴⊗det²}, p=7, det exponent sign per HT4 caveat); the Paškūnas-Rem-6.2-labelled list {det, Sym⁶⊗det} rests on Rem 6.2's matrix, which 3b/3d/3e show is not consistent with Prop 6.1 (35) for this ratio. Both labels remain NAMED; NO PICK.
- SF-G4 (PARTIAL): Paškūnas 1209.5205 writes the [53 §10]/πα non-generic object in both orientations (3a vs 3b).
- SF-G5 (PARTIAL): Gee–Kisin states its definitions are dual to [BM02] (3g); 1310.0831 gives no orientation statement.
- SF-C1 (L₀ = {Sym⁶⊗det}) UNAFFECTED.

## Remaining gaps
- G-3 OPEN remainder: no quoted sub/quotient slot convention for Paškūnas Rem 6.2; [53] (Paškūnas, Montreal functor), Breuil [6,7], BM02, BDJ not on disk.
- Twist-exponent sign (det^{±1}) for ω-twist remains convention-labelled (bm-sigma caveat, HT4).
