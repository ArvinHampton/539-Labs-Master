# MR2 FINDINGS — DUAL CONTINUE — SF-R3″ (sfr3pp) (2026-10-27)
STATUS: SF-R3′ NARROWED → CLOSED Soft SF (orientation), non-BL. REPORTS ONLY — no RECS; no P5a; no tip fold; Kerr BLOCKED; residual-C pick OPEN dual (filtration 10∥40 BOTH NAMED PARALLEL, NO PICK). tip_touched NO.
Parent: sfr3p FINDINGS 7f9b7d22…; sfr3-orient 5c090f80…; rem62-slot 03c9dead….

## 1. SF-R3′ as recorded (sfr3p l.21)
"FLAG: SF-R3′ stays OPEN-named (notation drift between Q1/Q2 and Q3)." with SF-P4 "no uniform convention reconciles Q1,Q2,Q3"; Q2 = 1209.5205 l.2612–2615 "(χω ∗; 0 χ) … non-generic", uncited.

## 2. New on-disk evidence (1209.5205.txt, all non-BL)
- E1 l.2618: "6.1. Generic case." / l.2809: "6.2. Non-generic case. We deal with the case ρ ≅ (χω ∗; 0 χ)." → Q3 (l.2670–2671, "(χ ∗; 0 χω) then by [53, Lem.10.16]") lies in §6.1 GENERIC; Q2 belongs to §6.2 NON-GENERIC. Q2 and Q3 are different cases, not required to be the same ρ.
- E2 l.2825–2826: "may assume that χ is trivial so that ρ ≅ (ω ∗; 0 1)".
- E3 l.2965–2968: "Since H¹(GQp, k(ω)) ≅ Ext¹_{GQp}(1, ω), kφ⊥ defines a non-split extension 0 → ω → ρ → 1 → 0. It is shown in [18, VII.4.24] that V(β) ≅ ρ, which implies that V̌(β∨) ≅ ρ."  ([18] = Colmez, Astérisque 330, l.3796; NOT on disk; NOT BL.)
- E4 [53]=1005.2008 l.6631–6632: "ρ is the non-split extension 0 → 1 → ρ → ω → 0" (§10 "Non-generic case II" in [53]'s terminology); [53] l.311: "For non-generic cases, (iii) and (iv) see the introductions to §9 and §10."

## 3. Analysis
- A1. E2+E3: in-text, (ω ∗; 0 1) ↔ 0→ω→ρ→1→0, i.e. SUB = UPPER-LEFT. This is exactly Q1's convention (Ext¹(χ2,χ1), sub χ1 upper-left) = sfr3p reading C3.
- A2. Under uniform sub-upper-left: Q1 ✓; Q2 = 0→χω→ρ→χ→0 ✓ (matches E3, Ext¹(χ,χω)=H¹(ω) 2-dim, φ-parametrised, consistent with Q1's exclusion reason); Q3 = 0→χ→ρ→χω→0 = χ⊗[53]§10 ρ (E4) ✓, consistent with Rule R (lower-right = quotient χω).
- A3. Hence sfr3p SF-P4 ("no uniform convention") was an artefact of assuming Q2 and Q3 denote the same ρ; E1 shows they are distinct cases. Correction recorded (not a fold): SF-P4 superseded by A2.
- A4. Terminology drift (fact, not a gap): [53] calls 0→1→ρ→ω "non-generic case II" (E4); 1209.5205 Q1 places (χ ∗; 0 χω) in "generic" (χ1χ2⁻¹=ω⁻¹≠ω,1 for p≥5). Orientation unaffected.
- A5. Typo reading (A) remains Soft SF-rejected — now positively: Q2 orientation is confirmed by E2/E3, not a typo.

## 4. Classification
SF-R3′ → CLOSED Soft SF (orientation of the intro matrix fixed in-text by E3 under Q1's convention). NOT BL-dependent.
Remaining gap (named, narrow): the identification V(β)≅ρ in E3 is cited to Colmez [18, VII.4.24], not on disk (MISS). The orientation statement "0 → ω → ρ → 1 → 0" itself is in-text and does not depend on [18]; only the β↔ρ link does.

## 5. Carried unchanged
SF-IC-c′ (BL-blocked); OPEN-SK-conv (BL-blocked); soc_K=soc_Γ verbatim (BL-blocked); OPEN-SK-p3; soc_K value CLOSED-conditional p≥5; residual-C pick OPEN dual (10∥40 both named parallel, no pick). Rule R unchanged.

## 6. Search log (cwd /workspace/quantum-comp/lit/bm; counts are lines from rg -c)
1. `for f in *.txt; do echo "$f $(rg -c -i 'non-generic|nongeneric' $f)"; done` → 1005.2008:6, 1209.5205:3, 1309.1658:1, 1310.0831:1, all others 0 (empty).
2. `rg -n -i 'non-generic|nongeneric' 1209.5205.txt 1309.1658.txt 1310.0831.txt 1208.3179.txt` → hits 1209.5205 l.25,2615,2809; 1309.1658 l.242; 1310.0831 l.366 (5 total).
3. `rg -n -i 'non-generic|nongeneric' 1005.2008.txt` → l.49,59,311,637,5907,6620 (6).
4. `rg -n -i 'generic' 1209.5205.txt | head` → 10 lines shown (l.14,24,25,861,2606,2615,2616,2618,2809 …).
5. `rg -c '0 → ω → ρ' 1209.5205.txt` → 1 (l.2966).
6. `rg -n '^6\.[12]\. ' 1209.5205.txt` → 4 (l.24,25,2618,2809).
7. `rg -c 'Lem.10.16' 1209.5205.txt` → 1 (l.2671).
8. `rg -n '\[18\]' 1209.5205.txt | tail -3` → l.1809,3138,3796 (shown 3).
9. `ls | rg -ci colmez` → 0 (Colmez [18] not on disk).
Reads: `sed -n` 2805–2825, 2825–2850, 2862–3010 of 1209.5205.txt; 630–650, 6620–6645, 305–315 of 1005.2008.txt.

## Tip
/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH. AFTER: see PRESS / report (verified identical). tip_touched NO.
