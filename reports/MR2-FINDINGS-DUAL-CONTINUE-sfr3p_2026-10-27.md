# MR2 FINDINGS — DUAL CONTINUE — SF-R3′ (2026-10-27)
STATUS: PARTIAL. REPORTS ONLY — no RECS; no P5a; Bridge PARTIAL READY NO; G1 BLOCKED (no OMS / L₇); Kerr BLOCKED; no tip fold; tip_touched NO. Full-corpus OPEN.
Parent: sfr3-orient FINDINGS 5c090f80… / PRESS 8cd3aa74…. Dual-label filtration 10∥40 BOTH NAMED PARALLEL, NO PICK.

## Quotes (1209.5205.txt)
- Q1 l.2607–2611 (T1): "we will say that ρ is generic, if it is either irreducible, or ρ ≅ (χ1 ∗; 0 χ2), with χ1χ2^{-1} ≠ ω, 1. The assumption implies that Ext¹_{GQp}(χ2, χ1) is one dimensional, hence ρ is uniquely determined by the ordered pair (χ1, χ2)."
- Q2 l.2612–2615 (T2): "Since we assume that End_{GQp}(ρ) = k, the only case not covered by the above is when ρ ≅ (χω ∗; 0 χ). We will refer to this case as non-generic. This division is somewhat artificial…" — NO citation.
- Q3 l.2670–2678 (T5/(35)): "If ρ ≅ (χ ∗; 0 χω) then by [53, Lem.10.16] we have an exact non-split sequence 0 → (τ1 ⊗ χ∘det)^∨ → k⊗̂_{Ẽ}P̃ → (Ind_P^G χω ⊗ χω^{-1})^∨ → 0".
- [53] §10 / App B (from parent T9): "0 → 1 → ρ → ω → 0" = "(1 ∗; 0 ω)".

## Comparison
- C1. Literal: Q2 diag = (χω, χ); Q3 diag = (χ, χω). Swapped. Same ρ only if Q2 and Q3 use opposite matrix conventions.
- C2. Q2 is exactly the Q1 template at χ1χ2^{-1} = ω (χ1=χω, χ2=χ) — i.e. Q2 is the literal complement of Q1's "≠ ω" clause (the "1" clause is removed by End=k only for split/… — not argued in text).
- C3. Under Q1's own Ext convention (Ext¹(χ2,χ1) ⇒ sub χ1 = upper-left): Q2 = 0→χω→ρ→χ→0, Ext¹(χ,χω)=H¹(ω) 2-dim (p≥5) — non-unique, matching Q1's reason for exclusion; but this ρ ≠ χ⊗[53]§10 ρ (0→χ→ρ→χω).
- C4. Under QUOTIENT-upper-left reading (as T3/T4/T7): Q2 = 0→χ→ρ→χω→0 = χ⊗[53]§10 ρ = Q3 under Rule R ✓. But then Q1's Ext sentence would read Ext¹(quot,sub) reversed, contradicting Q1.

## Decision
Outcome (C) SF-named OPEN, with named sub-reading (B′):
- (A) rejected: correcting Q2 to "(χ ∗; 0 χω)" makes it match (35) but breaks C2 (Q2 is the literal Q1-complement); choosing which to keep would invent intent. Typo remains a hypothesis, not established.
- (B′) named reading: "Q2 inherits Q1's template literally; Q3 is pinned by Rule R to [53] l.6633." Under B′ Q2 and Q3 denote the same isomorphism class only if Q2 is read QUOTIENT-upper-left (C4). No single convention makes Q1, Q2, Q3 all consistent.
- FLAG: SF-R3′ stays OPEN-named (notation drift between Q1/Q2 and Q3). Downstream unaffected: every statement actually used is [53]-cited and fixed by Rule R; Q2 is definitional/intro only.

## L₂ socle gap
- Rem 6.3 l.2725: "It follows from (34), (35) and [16, 3.2] that soc_K π ≅ soc_K (k⊗̂_{Ẽ}P̃)^∨."
- [16] = Buzzard–Gee, IMRN 2009 (NOT Breuil) = arXiv 0804.1164; ingested lit/bm/0804.1164.txt. [16, 3.2] = BG Lemma 3.2 (l.381): "If 0 ≤ r ≤ p−1 and F is a quotient of I(σr) which has finite length…, every Jordan–Hoelder factor of F is a subquotient of I(σr)/(T−λ) = π(r,λ,1)". No explicit soc_K πα stated in [16]. soc_K πα NOT quoted — gap remains.
- MISSES named: Breuil [6] (Compositio, Sur quelques… I), [7] (J. Inst. Math. Jussieu, II) not obtained (not arXiv); BM02 not obtained. soc_K πα would come from [6]/[7]/BL94 — OPEN.

## Facts
SF-P1 Q2 quoted verbatim l.2612–2615, uncited. SF-P2 Q2 vs Q3 diagonals swapped. SF-P3 Q2 = Q1 template at χ1χ2^{-1}=ω. SF-P4 no uniform convention reconciles Q1,Q2,Q3. SF-P5 Outcome (C) + named reading B′; (A) rejected as invention. SF-P6 Rule R and all [53]-cited orientations unchanged. SF-P7 [16]=Buzzard–Gee arXiv 0804.1164, ingested; [16,3.2]=Lemma 3.2 (JH factors), no soc_K πα. SF-P8 soc_K πα gap OPEN; [6][7] BM02 misses named.

## Tip
/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (expected 7cddb188…dfc91 MATCH). tip_touched NO.
Lit: 1209.5205.txt, 1005.2008.txt, 0810.2106 (not re-read), 0804.1164.txt (new, sha256 3d477f97262081c974e5d1de7d231a17b9702443dd554a00f4dc1bd3fc205214).
Tip sha256 AFTER 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH. tip_touched NO.
