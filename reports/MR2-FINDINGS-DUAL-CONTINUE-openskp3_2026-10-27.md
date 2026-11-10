# MR2 FINDINGS — DUAL-CONTINUE — OPEN-SK-p3 (2026-10-27)
Role: Math Research 2, Soft SF writer. REPORTS ONLY — No RECS. Soft SF → Auditor.
Label clause: per OWNER_WRITE_AMEND_INVENT_LABEL_PENDING_MATH_PROOF_2026-10-27.md, invent stamps read "invented pending mathematical proof".
Tip (READ-ONLY, not edited) BEFORE sha256: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91

## Soft SF STATUS: OPEN-SK-p3 = OPEN Soft SF, named gap GAP-SK-p3-1
GAP-SK-p3-1: corpus has no passage computing soc_K(πα) at p=3. 1209.5205 §3 (l.1275) "From now on we assume¹ that p ≥ 5" — global standing hypothesis covering Rem 6.2 (l.2695) and its use at l.2795; footnote 1 text not recoverable from the .txt extraction (MISS in text layer).

## Evidence (verbatim-located)
- 1209.5205 l.6, l.121 (Thm 1.1 "Assume p ≥ 5"), l.1275, l.2617 ("We assume that p ≥ 5"). p=3 hits: 0.
- Rem 6.2 (l.2695): ρ abs. irr., ρ|I ≅ (ω2^{r+1} ⊕ ω2^{p(r+1)})⊗ω^m ⇒ soc_K π ≅ (Sym^r ⊕ Sym^{p-1-r}⊗det^r)⊗det^m, 0≤r≤p−1, cites [6],[7] (Breuil GL2(Qp) I/II). Form is p-uniform; scope is under p≥5.
- Formal p=3 specialization (NOT sourced): soc_K π ≅ (Sym^r ⊕ Sym^{2−r}⊗det^r)⊗det^m, r∈{0,1,2}; r=0 gives Sym^0 ⊕ Sym^2 (Sym^{p-3}=Sym^0 at p=3). Stamp: **invented pending mathematical proof** (candidate; NOT OPERATIVE).
- 1005.2008 Rem 5.43 (l.4096–4098): blocks at p=3 computed in [56]; Ind_P^G α reducible at p=3 (ss ≅ ω∘det ⊕ Sp⊗ω∘det). Concerns principal-series block (iv), not supersingular socle. l.4670: "should also work for p = 3, but we have not" — unproven.
- breuil_paskunas_supersingular l.1317 (p=3 case-by-case "also impossible"), l.1744/1809 (f=1,p=3, r0=s0=p−1 special cases), l.3500 (p=3: only ρ irreducible, r0=1). Generic-f Serre-weight context; no direct soc_K(πα) statement for Qp, p=3.
- breuil_GL2Qp_II l.2103–2122: p=3, k=6 examples (crystalline reductions), no socle statement for πα. breuil_GL2Qp_I: 0 p=3 hits; l.1533/1548 "au moins pour p > 2".
- bm02_multiplicite l.7543 §6.2: p=3 supercuspidal-type example (multiplicity), not soc_K(πα).
- 1309.1658: 0 p=3 hits; Sym0 2, p−3 pattern 9 (generic, not p=3-specific).

## Carry (unchanged)
- filtr CANDIDATE (10)+40 PARALLEL: both live, NOT OPERATIVE (invented pending mathematical proof).
- INV-Ind: Soft SF-INVENTED-CLOSED → re-stamped "invented pending mathematical proof".
- GAP-SG-K1 (sock-gamma NARROWED) open. sockval CLOSED-conditional p≥5 via Rem 6.2.
- Colmez [18] MISS (not in corpus).
No tip fold; no Kerr; no P5a.

## Search log
cwd /workspace/quantum-comp/lit/bm
1. grep -n -i -E "p ?= ?3|p ?＝ ?3|Sym\^\{?0|Sym\^\{?p-3|p>3|p ?≥ ?5" 1209.5205.txt → 4 hits (p≥5: l.6,121,1275,2617); Rem 6.2 grep → l.2695, 2795
2. per-file counts (p=3 / Sym0 / p−3): 1209.5205 0/0/0; 1309.1658 0/2/9; 1005.2008 3/0/0; breuil_paskunas_supersingular 5/0/34; breuil_GL2Qp_I 0/0/4; breuil_GL2Qp_II 5/0/4; bm02_multiplicite 1/0/0
3. grep "assumption|we assume" 1209.5205 → footnote-1 body not found
4. sed contexts: 1209.5205 l.1270–1290, 2690–2715; 1005.2008 l.4094–4102; BP l.1314–1319, 3498–3503
Tip AFTER sha256: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH
