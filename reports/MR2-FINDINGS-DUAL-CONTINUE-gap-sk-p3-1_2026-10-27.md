# MR2 FINDINGS — DUAL-CONTINUE — GAP-SK-p3-1 / OPEN-SK-p3 (2026-10-27)
STATUS: Soft SF CLOSED (proof from on-disk published source; Eigen Rule 5 review pending). REPORTS ONLY — No RECS.

## Locks
- Tip BEFORE sha256: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (LOCK 7cddb188… MATCH). tip_touched NO.
- Parent: reports/MR2-FINDINGS-DUAL-CONTINUE-openskp3_2026-10-27.md sha c39c8154c5ff365b64848330bf74d155d45f086376687810f0097d83008d5ec4 (matches its .sha256).
- Filtration OW c3288fbfdb3c9c09… STANDS (cited in SOFTSF_PRESS_OWNER_WRITE_FILTRATION_CONVENTION_BOTH_NAMED_PARALLEL_2026-10-26.md). Invent-lift OW: on-disk OWNER_WRITE_INVENT_LIFT_PROVE_TO_BRIDGE_2026-10-26.md sha prefix 841f5067 f9526f46 ; 37b8298b… recorded as "OW LIVE" in SOFTSF_PRESS_PR1_OWNER_TOKEN_HARD_STOP_REMOVED_ACK_2026-10-27.md; 99e67629… recorded only as "Pre-amend standing" in STANDING_REMINDER_PATTERN_CORRELATION_RIGOROUS_PROOF_2026-10-27.md l.61 (current standing per PR1 ACK = 2050914c…). OW MISMATCH (standing): 99e67629… is pre-amend, not current; continued under on-disk.
- Kerr not worked. GAP-FILTR-68 not reopened. No tip-fold. No Owner-pick.

## Lit cites (file + sha256)
- lit/bm/breuil_GL2Qp_I.txt 3b5f0a8e7a58de7a3c37c4391bf6d855704ddbc947b0b9deaa17c1edf3154518 (pdf ceac657c69a8439e50bf28a4f385766714579669781cace1fa77f698cb4b3f33): Thm 1.1/Cor 4.1.1, 4.1.4 (irreducibility, r∈{0..p−1}); Thm 3.2.4 (l.1017) + Cor 4.1.4 (l.1297): π(r,0,χ)^{I(1)} = F̄p[Id,x^r] ⊕ F̄p[α,y^r]; Thm 1.3/Cor 4.1.5: π(r,0,χ) ≅ π(p−1−r,0,χω^r); Cor 4.2.3 (bijection π(r,0,χ) ↔ ind(ω2^{r+1})⊗χ). Hypotheses: none on p beyond "p≠2" in one sub-step (l.1356). p=3 admissible.
- lit/bm/1209.5205.txt 4ac1a4c57fe6a38e1f05210e0c6e57df06eb8e875cb01852aaa57c5031fe8592: Rem 6.2 (l.2695) cites [6],[7] = Breuil I/II (l.3771–3774); p≥5 is the paper's standing hypothesis (l.1275), not used by the cited socle computation.
- lit/bm/1309.1658.txt 69ff1168ed345bd884c4eaf6112a108fe5e21ccc20d43baea35094c646224d69 l.605–619: same I(1)-invariant counting technique (dim (soc_K)^{I1} = #summands), stated under p≥5 standing; corroborative only.

## Proof (p=3; argument valid for all p≥3) — Soft SF
Setup: ρ abs. irred., ρ|I ≅ (ω2^{r+1} ⊕ ω2^{p(r+1)})⊗ω^m ⇒ ρ ≅ ind(ω2^{r+1})⊗χ with χ|I = ω^m, so π ≅ π(r,0,χ) = (ind_{KZ}^G Sym^r / T)⊗χ∘det (Breuil I Cor 4.2.3). K-restriction of χ∘det = det^m. Reduce to m=0.
1. π^{I(1)} has dim 2 (Thm 3.2.4 for r≤p−2; Cor 4.1.4 for r=p−1). 
2. Every irreducible F̄p[K]-rep (Sym^s⊗det^a, inflated from GL2(Fp)) has 1-dim I(1)-invariants, and every nonzero smooth K-rep has nonzero I(1)-invariants (I(1) pro-p). Hence soc_K π has at most 2 irreducible summands (counted with multiplicity).
3. v ↦ [Id,v]: Sym^r → π is nonzero (hits [Id,x^r]≠0), hence injective (Sym^r irreducible).
4. By Thm 1.3, π ≅ π(p−1−r,0,ω^r); step 3 for that model gives Sym^{p−1−r}⊗det^r ↪ π.
5. Sym^r ≇ Sym^{p−1−r}⊗det^r: if r≠p−1−r dims differ; if r=(p−1)/2 (p=3: r=1) then det^r nontrivial on GL2(Fp) since 0<r<p−1, and the I(1)-eigencharacters diag(a,d)↦a^r vs a^{p−1−r}(ad)^r = d^r differ. So the two images intersect in 0 and their sum is direct ⊂ soc_K π.
6. By step 2, equality: soc_K π ≅ (Sym^r ⊕ Sym^{p−1−r}⊗det^r)⊗det^m.
p=3: r∈{0,1,2}: soc_K π ≅ (Sym^r ⊕ Sym^{2−r}⊗det^r)⊗det^m; r=0 → (Sym^0 ⊕ Sym^2)⊗det^m; r=1 → (Sym^1 ⊕ Sym^1⊗det)⊗det^m; r=2 → (Sym^2 ⊕ Sym^0⊗det^2)⊗det^m = (Sym^2⊕Sym^0)⊗det^m (det^2 trivial at p=3; consistent with r=0 via Thm 1.3).

## Fates
- GAP-SK-p3-1: Soft SF CLOSED (published source Breuil I, Compositio 138 (2003), on disk; no p≥5 hypothesis used). Pending Eigen Rule 5.
- Invent-pending p=3 specialization: proof supplied above → label "invented pending mathematical proof" ELIGIBLE DISCHARGE pending Eigen; NOT OPERATIVE until Eigen accept. Not tip-folded.
- Residual caveat (scope, not gap): result concerns π attached to ρ by Breuil's correspondence; uses of π inside 1209.5205's p≥5 deformation machinery remain outside this finding. Side note carried: 1005.2008 Rem 5.43 (p=3 principal-series block) unaffected.
- No NOT-FEASIBLE; no 24h retry stamp required.

Tip AFTER sha256: see PRESS.
