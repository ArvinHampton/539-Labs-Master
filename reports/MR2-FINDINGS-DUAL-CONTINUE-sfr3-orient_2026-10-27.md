# MR2 FINDINGS — DUAL CONTINUE — SF-R3 orientation (2026-10-27)
STATUS: PARTIAL. REPORTS ONLY — no RECS; no P5a; Bridge PARTIAL READY NO; G1 BLOCKED (no OMS / L₇); Kerr BLOCKED; no tip fold; tip_touched NO. Full-corpus OPEN.
Parent: rem62-slot FINDINGS 03c9dead… / PRESS 9db9088f…. Dual-label filtration 10∥40 BOTH NAMED PARALLEL, NO PICK.
Line numbers = lit/bm/*.txt on disk (1209.5205.txt, 1005.2008.txt = [53]).

## MATCH table — orientation per statement
| # | source / line | quote | upper-left = | pinned by |
|---|---|---|---|---|
| T1 | 1209 §6 intro l.2607–2611 | "ρ ≅ (χ1 *; 0 χ2), with χ1χ2^{-1} ≠ ω, 1. The assumption implies that Ext¹_{GQp}(χ2, χ1) is one dimensional" | SUB (Ext¹(quot,sub)=H¹(χ1χ2^{-1}); excl. ω = 2-dim H¹(ω)) | Ext convention, cf. T6 |
| T2 | 1209 §6 intro l.2612–2614 | "the only case not covered … is when ρ ≅ (χω *; 0 χ)" | SUB ⇒ 0→χω→ρ→χ→0 = χ⊗(0→ω→ρ→1) | matrix only |
| T3 | 1209 §6.1 l.2619–2622 | "ρ ≅ (χ1 *; 0 χ2) non-split … π := Ind_P^G χ1⊗χ2ω^{-1}, so that V̌(π^∨) = χ1" | QUOTIENT | [53] l.5672–5674 "0 → χ2 → ρ → χ1 → 0" (V̌ exact, π1=Ind χ1⊗χ2ω^{-1}) |
| T4 | 1209 Prop 6.1 pf (34) l.2650–2674 | "0 → (Ind χ2⊗χ1ω^{-1})^∨ → k⊗̂P̃ → (Ind χ1⊗χ2ω^{-1})^∨ → 0 by [53, Prop.8.3]"; generic excl. "ω^{±1}" | QUOTIENT | V̌ exact + [53] Prop 8.3 / l.5674 |
| T5 | 1209 Prop 6.1 pf (35) l.2667–2678 | "If ρ ≅ (χ *; 0 χω) then by [53, Lem.10.16] … → (Ind χω⊗χω^{-1})^∨ → 0" | SUB: [53]§10 ρ is "0 → 1 → ρ → ω → 0" (l.6633, l.9923); ⊗χ gives sub χ, quot χω | [53] l.6633 |
| T6 | 1209 l.2965–2967 | "H¹(GQp, k(ω)) ≅ Ext¹_{GQp}(1, ω), kφ⊥ defines a non-split extension 0 → ω → ρ → 1 → 0" | (Ext¹(quot,sub) convention, same as T1) | exact seq. |
| T7 | 1209 Rem 6.2 l.2715–2722 | "ρ ≅ (χ1 *; 0 χ2ω^{r+1}) ⊗ ω^m … π ≅ (Ind χ1⊗χ2ω^r)⊗ω^m∘det" | QUOTIENT (same pairing as T3) | T3/T4 + BDJ cross-check (parent M3) |
| T8 | [53] App B l.10278/10343 | "0 → χ1 → ρ12 → χ2 → 0", "ρ12 = (χ1 *; 0 χ2)" | SUB | exact seq. |
| T9 | [53] App B l.9923–9930 | "0 → 1 → ρ → ω → 0" written "(1 *; 0 ω(g))" | SUB | exact seq. |
| T10 | [53] §8 l.5628–5674 | "π1 := Ind χ, χ = χ1⊗χ2ω^{-1}" … "ρ := V̌(Q) … 0 → χ2 → ρ → χ1 → 0" | (no matrix; exact seq. only) | — |

## Observations
- O-a. [53] is internally uniform: every matrix (T8, T9) has upper-left = SUB; §8 (T10) uses exact sequences only. No contradiction inside [53].
- O-b. 1209.5205 is NOT uniform: T1, T5 (and Ext convention T6) read upper-left = SUB; T3, T4, T7 read upper-left = QUOTIENT. Split is not intro-vs-proof: inside Prop 6.1 proof, (34)-case (T4) is QUOTIENT and (35)-case (T5) is SUB.
- O-c. T2 vs T5: under T1's own convention T2 = χ⊗(0→ω→ρ→1), which is NOT [53]§10's ρ (0→1→ρ→ω); T5 under SUB = χ⊗[53]§10 ρ ✓. T2 matches [53]§10 only under QUOTIENT reading. So T2 also disagrees with T1's convention or with T5. Non-generic: H¹(ω^{-1}) = Ext¹(ω,1) is 1-dim (p≥5), H¹(ω) 2-dim — T1 exclusion "≠ ω" (2-dim case) is consistent with SUB; the excluded-from-generic set in T4 "ω^{±1}" covers both.

## Decision (SF-R3)
Outcome (A), per-statement, with cited rule: RULE R — wherever 1209.5205 pairs a matrix with a [53] citation, the orientation is fixed by the exact sequence in the cited [53] statement (V̌ exact: [53] l.5672–5674 for (34)/§6.1/Rem 6.2; [53] l.6633 for (35)). Under R: §6.1, (34), Rem 6.2 → sub = lower-right; (35) → sub = upper-left. No statement used downstream is left ambiguous.
Residual (C), named SF-R3′ OPEN: 1209.5205 has no single global matrix convention (O-b, O-c); T2 (intro non-generic matrix) carries no [53] citation and cannot be pinned by R. Not resolvable from text; possibly typo/notation drift. FLAG: not cleared as a "paper-internal dual" (B rejected — it is inconsistency, not a deliberate dual).

## Effect (REPORTS ONLY)
- E1. L₂ (0→ω→L₂→ω²→0) = ω⊗[53]§10 ρ = T5 with χ=ω: "(ω *; 0 ω²)" under SUB. (35) quotient Ind(χω⊗χω^{-1}) at χ=ω = Ind(ω²⊗1) = Ind(α)⊗ω∘det = πα⊗ω∘det ✓ consistent with parent L1/L2.
- E2. πα character now quoted: [53] l.3096–3099 "α : T → k× be the character α(diag(λ,μ)) := ω(λμ^{-1})" ⇒ α = ω⊗ω^{-1}; [53] intro l.244 block (iv) "{η∘det, Sp⊗η∘det, (Ind_P^G ω⊗ω^{-1})⊗η∘det}". Parent gap O2(α) CLOSED Soft SF.
- E3. L₂ σ-label unchanged: Paškūnas-label {Sym⁴⊗det²} ∥ BDJ-label {Sym⁴⊗det²}, both NAMED, NO PICK. Rule R confirms the rem62-slot sub-slot (Rem 6.2 sub = lower-right) — no reversal. SF-S4 / prior bm-sigma facts: rem62-slot supersession of sigma-gaps 3e stands; nothing further superseded.
- E4. HT4 det-exponent sign caveat carried.

## Facts
SF-O1 [53] matrix convention uniform upper-left=SUB (T8,T9). SF-O2 1209.5205 mixed: SUB at T1,T5; QUOT at T3,T4,T7. SF-O3 Rule R closes every [53]-cited statement. SF-O4 SF-R3′ OPEN: T2 uncited, inconsistent. SF-O5 α = ω⊗ω^{-1} quoted [53] l.3099. SF-O6 L₂ labels unchanged {Sym⁴⊗det²}∥{Sym⁴⊗det²}.

## Remaining OPEN (named)
- G1. L₂ socle: no §10-specific socle statement found in [53] (grep socK/socle in §10: none giving soc_K πα). 1209 Rem 6.3 (l.2725) gives socK π ≅ socK(k⊗̂P̃)^∨ "from (34), (35) and [16, 3.2]" — relation only, value via Breuil [16] not on disk. Socle still via Rem 6.2 formula outside its hypothesis.
- G2. BM02 [11], Breuil [6]/[7]/[16]: not on disk, nothing quoted.
- G3. SF-R3′ (T2) as above.
