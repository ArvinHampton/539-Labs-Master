# MR2 FINDINGS — DUAL CONTINUE socK2 — 2026-10-27
STATUS: PARTIAL. Soft SF. REPORTS ONLY — No RECS. No P5a. Bridge PARTIAL READY NO. G1 BLOCKED (no OMS / L₇). Kerr BLOCKED. No tip fold. Full-corpus OPEN.
Lineage: FINDINGS 11b63ff0… / PRESS 38b0700b…; socK ccd3fb0a…/3aa07281…. Auditor Pack GC MATCH. Filtration 10∥40 BOTH NAMED PARALLEL, NO PICK.

## Lit
- INGESTED: Breuil–Paškūnas, "Towards a modulo p Langlands correspondence for GL2", Mem. AMS 216 (2012), author preprint
  https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/supersingular.pdf
  lit/bm/breuil_paskunas_supersingular.pdf sha256 a63c41e222e226f1019282f6b7dab7078afe61f908572f1b0f90523f7fdf2d51
  lit/bm/breuil_paskunas_supersingular.txt sha256 cefcae816aa0414f2d989891366c783161711051597f0d641c77647a64960ba2
  (Note: arXiv 0704.3300 is an unrelated quant-ph paper — not BP; no arXiv record found for BP.)
- MISSED: Barthel–Livné, Duke Math. J. 75(2) (1994) 261–292, doi 10.1215/S0012-7094-94-07508-X — Project Euclid paywalled; only first-page preview free. SF-BL1 MISS.
- BM02: still MISS (not re-sought this pass; no new source).

## Soft SF facts
- SF-SK2a (quote, BP §1 notation): "we denote by Ind_B^Γ χ the F̄p-vector space of functions f : Γ → F̄p such that f(bγ) = χ(b)f(γ) (b ∈ B, γ ∈ Γ) with left action of Γ by right translation on functions. Likewise with Ind_I^K χ."
- SF-SK2b (quote, BP §2): "Ind_B^Γ χ (resp. Ind_B^Γ χ^s) has dimension q + 1 and is isomorphic to Ind_I^K χ (resp. Ind_I^K χ^s) in an obvious way."
- SF-SK2c (quote, BP Thm 2.4 + remark): for χ ≠ χ^s, socle and cosocle filtrations on Ind_B^Γ χ^s coincide, graded pieces ⊕_{ℓ(τ)=i} τ; "σ is then the socle of Ind_B^Γ χ^s by Theorem 2.4." Lemma 2.3: χ = χ^s ⇒ Ind = (0,…,0)⊗η ⊕ (p−1,…,p−1)⊗η (soc_K two weights).
- SF-SK2d (quote, BP §7): principal series written π = Ind_P^G χ, same left-coset-invariant / right-translation convention.
- SF-SK2e (INFERENCE, not a quote): via Iwasawa G = PK, Ind_P^G χ|_K ≅ Ind_{P∩K}^K χ, inflated from Ind_B^Γ χ̄ on K1-invariants; hence soc_K(πα) = soc_Γ(Ind_B^Γ χ̄) given SF-SK2b/c. Gap: no verbatim BP statement "soc_K(Ind_P^G χ) = …" found; that statement is attributed to [BL94], which is MISSED.
- SF-SK2f: for πα = Ind(ω⊗ω⁻¹): χ = ω⊗ω⁻¹ restricted to torus; χ = χ^s iff ω = ω⁻¹ on F_q^× i.e. ω² = 1, false for p>3 (q-1 ∤ 2). So generic branch Thm 2.4 applies (soc irreducible σ), NOT Lemma 2.3 branch. Which weight σ depends on χ vs χ^s labelling (convention flip) — unresolved.

## soc_K equality
Soft SF-named OPEN (narrowed): structural equality soc_K(πα) = soc_Γ(Ind_B^Γ χ̄) supported by BP quotes + inference SF-SK2e; verbatim source (BL94) MISSED.

## Ind-convention
Soft SF-named OPEN (narrowed): BP convention f(bγ)=χ(b)f(γ), right translation = standard normalised-free (unnormalised) induction. Match to our πα = Ind(ω⊗ω⁻¹) holds IF our Ind is unnormalised with same left-B-equivariance; χ ↔ χ^s labelling (which of σ, σ^[s] is socle) not verified against our file. OPEN.

## Carry-forward (unchanged, not re-litigated)
- SF-R3′ OPEN-named. rem62 Rem 6.2 L₂ Soft SF formula stands, no reversal.
- residual-C lattice pick OPEN Soft SF dual-named PARALLEL (residual-mult-bm ∥ end-seg) — REPORTS ONLY, NO PICK.
- BM02 MISS. Kerr BLOCKED. G1 BLOCKED.

## Tip
/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 BEFORE = AFTER. tip_touched NO.

## Remaining gaps
BL94 full text; BM02; verbatim soc_K(Ind_P^G) statement; χ/χ^s labelling vs our πα; residual-C pick (owner); Soft SF → Auditor + Eigen R5.
