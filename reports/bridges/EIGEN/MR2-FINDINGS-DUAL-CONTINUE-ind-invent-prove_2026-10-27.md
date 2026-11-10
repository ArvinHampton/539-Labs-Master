# MR2 FINDINGS — DUAL-CONTINUE ind invent-then-prove (2026-10-27)
Role: Math Research 2 Soft SF writer. Write-only → Auditor; FINDINGS → Eigen Rule 5. REPORTS ONLY. No RECS. No agent messages.

## Gates
- tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH; AFTER 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH. tip_touched NO.
- Invent-lift OW sha256 verified: 04b2c268fd2209d3e2372b697ee38b94cf560bdb738c26d898f34a2e68bcd52c (MATCH to steering 04b2c268…; earlier 922c5230… also observed MATCH at task start 12:20 CDT — file changed between).
- Amend THEN_PROVE_WHERE_FEASIBLE 4a6dca0515f311e4de4e34ca3bcc3db02a59cb17af7ca3b2902eae9e2ff57e1d MATCH.
- HARD GATE (proof-pursuit): this stamp writes NO new invent; it is proof pursuit of existing INV-Ind only.
- Parent 74cd02556c0b526d645eaf4688a29c1ec63f20e0688debc091548775704bc05b MATCH.

## Soft SF STATUS: PROVED (INV-Ind, verbatim specialization) — SF-IC-c′ and OPEN-SK-conv convention components PROVED; downstream residuals named below.

## Proof (Soft SF MATCH, mod p, on-disk)
Source lit/bm/breuil_paskunas_supersingular.txt (Breuil–Paškūnas):
- L501: "G := GL2(F)"; §7 L2204–2209: "We assume F is a finite extension of Qp. Let χ : P → T → F̄p^× be a smooth character … π = Ind_P^G χ." F=Qp admissible.
- L505: P ⊂ G the upper-triangular subgroup (= B of INV-Ind).
- L528–531 (verbatim def, mod p): for closed G0 ⊆ G and smooth R on an F̄p-space, c-Ind_{G0}^G R = functions f : G → R with "f(g′g) = g′·f(g) (g′ ∈ G0, g ∈ G)", support compact mod G0, G acting "by right translation on functions".
- L532–535: same convention for Ind_B^Γ χ: "f(bγ) = χ(b)f(γ)".
- L2254 Lemma 7.2(i): "ϕ(pgu) − ϕ(pg) = χ(p)(ϕ(gu) − ϕ(g)), p ∈ P" — consistent only with left-P transformation f(pg)=χ(p)f(g).
Specialization: G0 = P = B(Qp) closed; R = χ (1-dim, inflated through T); P\G compact (Iwasawa G = PK), so compact-mod-P support is automatic and c-Ind = Ind. Hence Ind_B^G χ = {f : G → F̄p smooth, f(bg)=χ(b)f(g)}, right-translation action — exactly INV-Ind. ∎
Corroborating (not needed for proof): 1005.2008.txt L3250–3254 mod-p classification (iii) "principal series Ind_P^G χ1⊗χ2, χ1≠χ2"; L3304–3305 I1-basis Supp ϕ1 = P s I1 (left-P cosets); 1209.5205.txt L3545–3547 char-0 smooth "f(bg)=χ(b)f(g) … right translations"; 1005.2008.txt L5529–5530 Banach "f(bg)=bf(g)".

## Invent label status
- INV-Ind: "invented pending mathematical proof" label DISCHARGED → Soft SF PROVED (verbatim mod-p source, above).
- SF-IC-c′: mod-p convention component PROVED (char-0→mod-p transfer gap no longer needed: mod-p source verbatim). Remaining conditional: indconv χ/χ^s and sockval (Sym^{p−3}⊗det, p≥5) conditionals carried unchanged — not re-proved here.
- OPEN-SK-conv: function-space convention component PROVED by same cite. BL94/BL95 verbatim MISS stands (not on disk); not required for the convention proof.

## Named residuals (not proved this stamp)
R1 soc_K = soc_Γ verbatim OPEN. R2 sockval CLOSED-conditional p≥5 carried. R3 BL94/BL95 MISS.

## Carried flags (unchanged)
filtr invented pending mathematical proof CANDIDATE (10)+40 PARALLEL live NOT OPERATIVE; GAP-SG-K1 CLOSED Soft SF (70644418…); β↔ρ CLOSED Soft SF verbatim (a93a7677…); GAP-SK-p3-1 OPEN Soft SF; OPEN-SK-p3 OPEN; Kerr BLOCKED; tip LOCK READ-ONLY; P5a not claimed.

No new operative claims. No tip-fold. No RECS.
