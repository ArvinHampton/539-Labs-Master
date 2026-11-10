# MR2 FINDINGS — DUAL CONTINUE — BM ingest + JH multiplicities (PARTIAL) — 2026-10-26
Supersedes nothing; advances beyond b04066dc… (ABGT v7(L7(7.4.a.a))=0). No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. No tip fold.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188…dfc91 verified before/after; tip_touched NO.
Filtration BOTH NAMED PARALLEL, NO PICK: [Γ₀(7)-geometric] w(θ³f)=10 ∥ [Katz level-1] w(θ³f)=40.

## Status: PARTIAL (path A)
## Lit ingested → /workspace/quantum-comp/lit/bm/ (MANIFEST.sha256)
- 1209.5205 Paškūnas, "On the Breuil–Mézard conjecture" (Thm 1.1: p≥5, End_{G_Qp}(ρ̄)=k; §7 covers semistable non-crystalline, no p assumption in Thm 7.1).
- 1208.3179 Gee–Kisin, BM for potentially Barsotti–Tate (λ=0; weight 2 only).
- 1310.0831 CEGGPS, patching & p-adic LLC.
- Search log: WebSearch "Breuil-Mézard … Kisin semistable multiplicity" (hits: Kisin JAMS 2009, Gee–Kisin, Kisin JAMS 2008, Emerton–Gee geometric perspective [no open PDF fetched]). arXiv API query timed out. Three wrong-ID guesses discarded.

## Soft SF facts
SF-1 (CITE, 1209.5205 Thm 1.1 + §1): for ρ̄:G_Q7→GL2(k) with End=k and p=7≥5, z1(R^ψ(w,τ)/ϖ)=Σ_σ m_σ(w,τ) z(σ,ρ̄), with σ(w,τ)=σ(τ)⊗Sym^{b−a−1}⊗det^a and σ(τ)=st̃⊗χ∘det when τ≅χ⊕χ (semistable case).
SF-2 (Sage/GAP MeatAxe, proved computation, script jh_st_sym2_gl2f7.sage): over F7, JH factors of st⊗Sym² (=Sym⁶⊗Sym², dim 21) for GL2(F7) are Sym⁶⊗det, Sym⁴⊗det² (×2), Sym², det (dims 7+5+5+3+1=21). Sym² irreducible.
SF-3 (consequence of SF-1+SF-2): for weight k=4 (b−a−1=2), trivial inertial type, semistable ring of ρ̄=ρ̄_{7.4.a.a,7}|G_Q7 (up to det^a twist): e = μ(Sym⁶⊗det)+2μ(Sym⁴⊗det²)+μ(Sym²)+μ(det) — CONDITIONAL on End_{G_Q7}(ρ̄)=k (NOT verified here).

## ABSENT / gaps
- No BM statement found that yields v7(L7(7.4.a.a)) or any L-value residue: BM concerns local deformation-ring multiplicities, not p-adic L-values. ABSENT for L-value use.
- Hypothesis End=k for ρ̄|G_Q7 unverified (depends on reduction of semistable rep with a7=−7, i.e. L-invariant). Gap named.
- Path B (Pollack–Stevens) not attempted this run.
