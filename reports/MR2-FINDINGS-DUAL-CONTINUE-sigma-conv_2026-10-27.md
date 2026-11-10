# MR2 FINDINGS — DUAL CONTINUE — σ-convention (Paškūnas Rem 6.2 vs Serre/BDJ; Hu–Tan p₁) — 2026-10-27
STATUS: PARTIAL. REPORTS ONLY — no RECS; no P5a; Bridge PARTIAL READY NO; G1 BLOCKED (no OMS / L₇); Kerr BLOCKED; no tip fold.
Dual-label filtration: 10 ∥ 40 — BOTH NAMED PARALLEL, NO PICK.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before = after; tip_touched NO).

## Quotes (lit/bm/1209.5205.txt, Paškūnas)
- Q1 (§6 intro, l.2606–2614): "we will say that ρ is generic, if it is either irreducible, or ρ ≅ (χ₁ *; 0 χ₂), with χ₁χ₂⁻¹ ≠ ω, 1 … the only case not covered … is when ρ ≅ (χω *; 0 χ). We will refer to this case as non-generic."
- Q2 (§6.1, l.2618–2622): π := Ind_P^G χ₁ ⊗ χ₂ω⁻¹ "so that V̌(π^∨) ≅ ρ" (generic reducible).
- Q3 (Rem 6.2, l.2703–2722): "If ρ ≅ (χ₁ *; 0 χ₂ω^{r+1}) ⊗ ω^m, χ₁,χ₂ unramified, χ₁ ≠ χ₂ω^{r+1} then π ≅ (Ind χ₁ ⊗ χ₂ω^r) ⊗ ω∘det. Hence soc_K π ≅ Sym^r k² ⊗ det^m if 0 < r < p−1 and det^m ⊕ Sym^{p−1} k² ⊗ det^m otherwise."
- Q4 (§6.2, l.2809–2826): non-generic ρ ≅ (χω *; 0 χ), β with V̌(β^∨) ≅ ρ; "may assume χ trivial so that ρ ≅ (ω *; 0 1)".
- Q5 (Prop 6.20, l.3189): "If ρ is très ramifié then M(σ) ≠ 0 iff σ ≅ st ≅ Sym^{p−1}k². If ρ is peu ramifié then M(σ) ≠ 0 iff σ = 1 or σ = st."
- Q6 (l.1378): V̌(M) := V(M^∨)^∨(εζ). Q7 (Cor 6.4 proof): "Using our conventions regarding local class field theory this is equivalent to the central character of Θ equal to ζ."
## Quotes (lit/bm/1309.1658.txt, Hu–Tan)
- H1 (Prop 2.11): V̌(I_χ(Sym^r)/(T−λ)^n)^∨ = (χω^{r+1}µ)⁻¹·(ωχ²ω^r) = χµ⁻¹ — same V̌ normalisation as Paškūnas.
- H2 (Thm 5.11, l.2758–2761), ρ̄ ≅ 1⊕ω split: Z(R^ver(k,τ,ρ)/ϖ) = a_{p−3,1}p₁ + a_{0,0}p₂ + a_{p−1,0}(p₂+p₃); Cor 5.10 + Thm 5.11 give ℓ(R_{p₁}/ϖ) = a_{p−3,1}.

## MATCH table
| Item | Paškūnas convention (V̌, Q1–Q5) | Standard Serre/BDJ (ρ̄|I ≅ (ω^{r+1} *; 0 1) ↔ Sym^r) | Match? |
|---|---|---|---|
| Non-generic orientation | (ω *; 0 1) (Q1,Q4) | (ω *; 0 1) ↔ Sym^{p−1} (très) / {Sym⁰,Sym^{p−1}} (peu) | MATCH |
| Prop 6.20 weights | très {st}, peu {1, st} (Q5) | same | MATCH |
| L₀ = ω⊗(ω *;0 1) très (SF-S1) | {Sym⁶⊗det} | {Sym⁶⊗det} | MATCH — SF-S1 UNAFFECTED |
| Generic Sym^r carrier | (1 *; 0 ω^{r+1}) (Q3, χ's trivial) | (ω^{r+1} *; 0 1) | ORIENTATION DIFFERS (unexplained by Q6: ρ^∨⊗det ≅ ρ for 2-dim, so V̌ dual+twist alone does not swap sub/quotient) |
| L₂ = ω⊗(1 *;0 ω): generic? | χ₁/(χ₂ω^{r+1}) = ω⁻¹ ∉ {1,ω} ⇒ generic, Q3 applies (r=0,m=1) | ω⊗(ω^{p−2} *;0 1) ⇒ r=p−3 | — |
| L₂ σ-list | {det, Sym⁶⊗det} | {Sym⁴⊗det²} (p=7) | DIFFER by convention |
| Hu–Tan p₁ ↔ σ_{p−3,1} | component of R for SPLIT 1⊕ω (H2) | FLAG inferred p₁ ↔ extension (1*;0ω) | inference NOT quoted in Hu–Tan (gap G-2) |

## Decision: (C) with residual named gap → STATUS PARTIAL
Both lists are Soft SF-valid, each under its own named convention; FLAG CLEARED as a convention-labeled dual reading (not an error in the literal Rem 6.2 read). Not closed to (A)/(B) because the source of the generic orientation difference between Paškūnas Rem 6.2 and BDJ is not located in the quoted text.

## Soft SF facts
- SF-C1: SF-S1 L₀ = {Sym⁶⊗det} — UNAFFECTED; agrees in both conventions (Q4,Q5).
- SF-C2: SF-S2 RE-LABELED: L₂ σ-list = {det, Sym⁶⊗det} [Paškūnas-Rem-6.2 / V̌ matrix convention] ∥ {Sym⁴⊗det²} [standard BDJ convention]. Both named, no pick.
- SF-C3: Paškūnas is internally consistent: Rem 6.2's excluded case χ₁/(χ₂ω^{r+1}) = ω is exactly Q1/Q4's non-generic (ω *;0 1), the case Prop 6.20 governs.
- SF-C4: Hu–Tan uses the same V̌ normalisation (H1); its p₁ label is on the split ρ̄ = 1⊕ω deformation ring, so it does not by itself fix the weight of a specific non-split L₂.
- SF-C5: SF-S4 RE-LABELED: "endpoints differ by exactly det" holds ONLY under the Paškūnas-Rem-6.2 reading. Under the BDJ reading, L₀ = {Sym⁶⊗det} and L₂ = {Sym⁴⊗det²} are disjoint (no shared weight). SF-S3 (HS-mult 1) holds for every listed σ in both readings.

## FLAG outcomes
- Hu–Tan FLAG on SF-S2: CLEARED as convention-labeled (C); not an inversion error in the reading of Rem 6.2.
- FLAG on SF-S4: RE-LABELED (Paškūnas-convention only).
- Mixing caveat: any downstream use must not combine SF-S1 and SF-S2 across conventions without the label.

## Remaining gaps
- G-1: Which convention the project's L₂ matrix (SF-K5) is written in — undetermined from these files; decides which label applies.
- G-2: Hu–Tan p₁ ↔ non-split (1 *; 0 ω) identification is not quoted; needs Hu–Tan §5 component description.
- G-3: Origin of the generic orientation swap (Paškūnas [53] Prop 6.1/Cor 8.7 or Breuil [6,7] / CLFT normalisation; 1208.3179, 1310.0831 not checked this pass).
