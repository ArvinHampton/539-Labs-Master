# MR2 FINDINGS — DUAL CONTINUE — Rem 6.2 sub-slot (2026-10-27)
STATUS: PARTIAL. REPORTS ONLY — no RECS; no P5a; Bridge PARTIAL READY NO; G1 BLOCKED (no OMS / L₇); Kerr BLOCKED; no tip fold; tip_touched NO.
Parent: sigma-gaps FINDINGS 55ba74c1… / PRESS 8f64fac1… (Eigen ACCEPT 73a7fd2c…). Dual-label filtration 10∥40 BOTH NAMED PARALLEL, NO PICK.

## Lit ingested (lit/bm/, MANIFEST.sha256 updated, sha256 -c all OK)
| src | arXiv | pdf sha256 | txt sha256 |
|---|---|---|---|
| [53] Paškūnas, The image of Colmez's Montreal functor (IHES 118, 2013) | 1005.2008v3 | 053eec49b476e949f640f5a5d268142b6711b39c985e245b9ffbf5aafa7c279c | b1ea4b455eb89ea68e5606f08aa228411e49343c45130fdf33d1b6a82d8a19c1 |
| BDJ, On Serre's conjecture for mod ℓ Galois reps over totally real fields (Duke 155, 2010) | 0810.2106v5 | 29515a96071cc632970d41394a6a867f938ba8b09ae39a22862073fbf3ceb237 | 51116792ff45ab098ff3bd071e74e7196c0903b1bae973eeb3641093e83c367c |
MISS (named): BM02 [11] (Breuil–Mézard, Duke 115, 2002) — no arXiv version located. Breuil [6] (Compositio 138, 2003) / [7] (J. Inst. Math. Jussieu 2003) — no arXiv version located. Not ingested; nothing quoted from them.

## Quotes (line numbers = pdftotext -layout of the .txt on disk)
Q1 [53] l.4204–4208: "V(Ind (χ1 ⊗ χ2 ω^{-1})) ≅ χ2" (V covariant exact).
Q2 [53] l.4238–4240: "V̌((Ind_P^G χ1 ⊗ χ2 ω^{-1})^∨) = χ1".
Q3 [53] §8 l.5629: "π1 := Ind_P^G χ, π2 := Ind_P^G χ^s α" with χ = χ1 ⊗ χ2ω^{-1}; l.5664 "S := π1^∨ and Q := κ^∨"; l.5672–5674: "Let ρ := V̌(Q) then since V̌ is exact we get an exact sequence of Galois representations 0 → χ2 → ρ → χ1 → 0."
Q4 [53] l.5741: "Corollary 8.7. The functor V̌ induces an isomorphism Ẽ ≅ R_ρ^{εζ}" (cited by 1209.5205 Prop 6.1 proof, l.2672).
Q5 [53] App B.1 l.10278 + l.10343: "0 → χ1 → ρ12 → χ2 → 0" and "ρ12 = (χ1 *; 0 χ2)" → in [53]'s own matrix notation upper-left = SUB.
Q6 [53] §10 l.6631–6633: block {1, Sp, πα}, "ρ is the non-split extension 0 → 1 → ρ → ω → 0"; App B l.9923–9930: same ρ written "g ↦ (1 *; 0 ω(g))".
Q7 1209.5205 §6 l.2605–2610: generic "ρ ≅ (χ1 *; 0 χ2), with χ1χ2^{-1} ≠ ω, 1. The assumption implies that Ext¹(χ2, χ1) is one dimensional"; non-generic "(χω *; 0 χ)".
Q8 1209.5205 §6.1 l.2618–2621: "ρ ≅ (χ1 *; 0 χ2) non-split, with χ1χ2^{-1} ≠ 1, ω, in which case we let π := Ind_P^G χ1 ⊗ χ2ω^{-1}, so that V̌(π^∨) = χ1."
Q9 1209.5205 proof Prop 6.1 l.2642–2654: generic needs "χ1χ2^{-1} ≠ 1, ω^{±1}"; (34) "0 → (Ind χ2⊗χ1ω^{-1})^∨ → k⊗Ẽ P̃ → (Ind χ1⊗χ2ω^{-1})^∨ → 0 by [53, Prop.8.3]"; (35) for "ρ ≅ (χ *; 0 χω)" by [53, Lem.10.16].
Q10 1209.5205 Rem 6.2 l.2715–2722: "If ρ ≅ (χ1 *; 0 χ2ω^{r+1}) ⊗ ω^m … then π ≅ (Ind χ1⊗χ2ω^r) ⊗ ω^m∘det. Hence socK π = Sym^r k² ⊗ det^m if 0 < r < p−1 and det^m ⊕ Sym^{p−1}k² ⊗ det^m otherwise."
Q11 BDJ l.1134–1136: "ρ|D ∼ (χ1 *; 0 χ2) and let cρ denote the corresponding class in H¹(Kp, χ1χ2^{-1})" → BDJ upper-left = SUB. l.1326–1327: "V ∈ Wp(ρ) iff cρ ∈ Lα for some α = (V, J) ∈ W′(χ1, χ2)"; Lemma 3.12: dim Lα = |J| (non-trivial, non-cyclotomic ratio).

## MATCH — Rem 6.2 sub-slot
M1. Q3+Q4: for π = Ind(χ1⊗χ2ω^{-1}) (the π of Q8), the Galois rep attached via V̌ (the one Prop 6.1 uses through Cor 8.7) has SUB χ2, QUOTIENT χ1. Independently: Q2 + exactness of V̌ applied to (34) gives 0 → χ2 → V̌(k⊗P̃) → χ1 → 0.
M2. Hence in Q8/Q10 the matrix "(χ1 *; 0 χ2…)" carries the SUB in the LOWER-RIGHT slot (χ2ω^{r+1}·ω^m) and the QUOTIENT in the UPPER-LEFT slot (χ1ω^m). Rem 6.2 is consistent with Q8 under this reading (substitute χ2→χ2ω^{r+1}, twist ω^m).
M3. Cross-check vs BDJ (Q11, upper-left = sub): for p=7 test ρ with sub 1, quotient ω² — Rem 6.2 under M2 (χ1=1·ω^2… i.e. m=2, χ1=1, χ2ω^{r+1}=ω^{-2}, r=3) gives socK = Sym³⊗det²; BDJ J=S for (1 *;0 ω²)_{BDJ}: a=2, b=4 → det²⊗Sym³. Agree. Under the old reading (upper-left = sub) Rem 6.2 instead returns BDJ's J=∅ weight, i.e. the weight of the opposite extension. M2 is the reading consistent with [53] and BDJ.
M4. Named residual inconsistency (not a slot ambiguity in Rem 6.2): 1209.5205 §6 intro (Q7: "Ext¹(χ2,χ1)", exclusion "≠ ω,1", non-generic "(χω *;0 χ)") matches upper-left = SUB, while (34)/Q3/Q9 ("≠ ω^{±1}", "(χ *; 0 χω)" → [53] §10) match upper-left = QUOTIENT. Also [53] App B (Q5, Q6) uses upper-left = SUB in its own matrices while [53] §8 Q3 orients ρ:=V̌(Q) with sub χ2 for π1=Ind(χ1⊗χ2ω^{-1}). The Galois/G-rep pairing is pinned by exact-sequence statements (Q1–Q3), not by matrices.
Outcome: Rem 6.2 sub-slot CLOSED Soft SF — SUB = lower-right entry (χ2ω^{r+1}⊗ω^m), via Q3/Q4 + (34) + BDJ cross-check M3. Prior sigma-gaps 3e reading (upper-left = sub, giving Ind(1⊗1)) is superseded.

## Corrected σ-label for L₂ (p=7; L₂: 0 → ω → L₂ → ω² → 0, SF-G1 of parent)
L1. L₂ ss = ω ⊕ ω², ratio ω^{±1} ⇒ NOT [53] block (ii) generic (Q3 hypothesis χ1χ2^{-1} ≠ 1, ω^{±1}); L₂ = ω ⊗ ρ_{[53]§10} with ρ_{§10}: 0 → 1 → ρ → ω → 0 (Q6) — the [53] §10 non-generic-II block, twisted by ω∘det. Matches parent's (35)/Hu–Tan pointer to Ind(ω⊗ω^{-1}).
L2. Paškūnas-side: π = πα ⊗ ω∘det, πα ≅ Ind(ω⊗ω^{-1}) per parent 3b/3d (not re-quoted here: [53] l.6624 writes πα := Ind α, α not expanded in this report). Socle via Rem 6.2's formula for the principal series Ind(1⊗1·ω^4)⊗ω∘det (r=4, m=1) → Sym⁴⊗det; ⊗ω∘det → Sym⁴⊗det². Direct Rem 6.2 under M2 (m=2, χ1=1, χ2ω^{r+1}=ω^{-1}, r=4) also → Sym⁴⊗det².
L3. BDJ-side: W′(ω, ω²), p=7, f=1: J=S → (a,b)=(2,5) → Sym⁴⊗det²; J=∅ → det, det⊗Sym⁶. cρ ≠ 0, dim Lα = |J| ⇒ Wp(L₂) = {Sym⁴⊗det²}.
L4. Corrected labels: Paškūnas-label {Sym⁴⊗det²} ∥ BDJ-label {Sym⁴⊗det²} — now COINCIDE. Old Paškūnas-label {det, Sym⁶⊗det} = BDJ J=∅ set (artifact of upper-left = sub reading). Both labels remain NAMED; NO PICK; dual-label filtration 10∥40 unchanged. HT4 det-exponent sign caveat carried.

## Remaining OPEN (named)
- O1: BM02 [11], Breuil [6]/[7] not on disk (no arXiv). BM02-side label unverified.
- O2: πα's character α not quoted in this report from [53] (relies on parent 3b/3d); Rem 6.2 formula used for socle of a principal series outside §6.1 generic hypothesis — Soft SF via formula, not via a §10-specific socle quote.
- O3: 1209.5205 §6 intro vs proof orientation inconsistency (M4) stays named; not resolvable from text alone.
