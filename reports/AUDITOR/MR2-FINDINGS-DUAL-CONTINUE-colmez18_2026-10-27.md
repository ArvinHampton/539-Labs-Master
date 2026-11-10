# MR2 FINDINGS — DUAL-CONTINUE — Colmez [18] / β↔ρ — 2026-10-27
Role: Math Research 2, Soft SF writer. REPORTS ONLY — no RECS. Soft SF → Auditor. Kerr BLOCKED (not invoked).
Tip (READ-ONLY, not edited): /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md
- BEFORE sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH
- AFTER  sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH

## Search log (cwd /workspace; rg -il / rg -i over quantum-comp, lit/bm)
| pattern | files | lines |
|---|---|---|
| Colmez | 49 | 197 |
| Astérisque 330 | 2 | 2 (1209.5205 ref list context; 0804.1164 l.3796 ref [18]) |
| V(β) / V(beta) | 9 | 10 |
| VII.4.24 | 3 | 4 (1209.5205 + prior sfr3pp reports only) |
| trianguline | 1 | 1 (0804.1164 l.348, irrelevant) |
| (φ,Γ) ascii/unicode | 0 | 0 |
| sfr3pp | 10 | 10 |
Note: /workspace/lit/bm does not exist; actual path /workspace/quantum-comp/lit/bm.
On-disk result before web: [18] text MISS (confirmed).
Web: WebSearch "Colmez Représentations de GL2(Qp) et (φ,Γ)-modules Astérisque 330 pdf" → free open-access NumDAM copy (SMF digitisation, public).
`curl -sL -o quantum-comp/lit/bm/colmez_ast330.pdf https://www.numdam.org/item/AST_2010__330__281_0.pdf` → sha256 ccf1a070d4fd5d8b5aaf14591fd0c7390f4ec048c986b1f88a32e90f8c933568; pdftotext → colmez_ast330.txt (11952 lines). No paywall bypass.
`rg -n "VII\.4\.2[0-9]"` → Prop VII.4.24 at txt l.11019 (printed p.492–493).

## E1 — Colmez Prop. VII.4.24 (OCR, l.11019–11020; OCR-garbled symbols restored in brackets)
"Proposition VII.4.24. — Si Π est une extension non triviale de B(1,ω) par E_τ, alors V(Π) = V(ω,1,τ^⊥)."
Proof l.11022–11033 (via Prop VII.3.7(iv), VII.3.8). Also used at l.11049, l.11127, l.11246.

## E2 — 1209.5205 definition of β (Lemma 6.7)
β: soc_G β = Sp, ss = Sp⊕1⊕π_α; exact (43) 0→E_φ→β→π_α→0, (44) 0→Sp→β→κ→0; E_φ = ext of 1 by Sp from Ext¹(1,Sp)≅Hom(Qp^×,k) [18, VII.4.18]. ρ: 0→ω→ρ→1→0 cut out by kφ^⊥.

## Matching (Soft SF)
E_φ(BM) ↔ E_τ(Colmez) with τ=φ [both via VII.4.18]; β = nontrivial ext of π_α by E_φ (43) ↔ Π = nontrivial ext of B(1,ω) by E_τ; ρ (line φ^⊥) ↔ V(ω,1,τ^⊥). Then VII.4.24 gives V(β)≅ρ.
Residual dictionary items (not verified on disk this turn):
- D1: π_α (BM notation) = B(1,ω) (Colmez principal series notation, up to BM's twist normalisation χ trivial).
- D2: Colmez V(ω,1,τ^⊥) = the non-split ext 0→ω→·→1→0 of class τ^⊥ (Colmez's V(δ1,δ2,L) convention, §VII.4 / II); and V (Colmez functor) = BM's V (BM l.1363 states [18] defines V; covariant exact).
Kerr not used. No new mathematics invented.

## Optional invent (Soft SF CANDIDATE, NOT OPERATIVE, not tip-folded)
CAND-β↔ρ: "D1 and D2 hold, hence V(β)≅ρ" — label: invented pending mathematical proof. Not needed for orientation (closed without [18]).

## OUTCOME
β↔ρ: NARROWED Soft SF-named — source located (Colmez Ast. 330 Prop VII.4.24, free NumDAM), statement matches modulo named notation dictionary D1, D2. Soft SF closed under invent lift labeled invented pending mathematical proof (cond.) via CAND-β↔ρ.
Orientation 0→ω→ρ→1→0: CLOSED Soft SF (unchanged, no [18]).

## Carry (unchanged)
- filtr invented pending mathematical proof CANDIDATE (10)+40 PARALLEL — both live, NOT OPERATIVE
- INV-Ind: Soft SF closed under invent lift (cond.)
- GAP-SG-K1 — open
- GAP-SK-p3-1 — open
- OPEN-SK-p3 — OPEN
