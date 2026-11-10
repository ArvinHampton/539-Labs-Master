# MR2 FINDINGS — DUAL-CONTINUE sock-gamma (2026-10-27)
REPORTS ONLY — No RECS. Soft SF → Auditor. Kerr BLOCKED (not invented). No tip fold. No P5a.

## STATUS
- soc_K(πα)=soc_Γ(πα) verbatim: **NARROWED Soft SF-named** (not CLOSED). No BL94/BL95 used.
- OPEN-SK-p3: **OPEN** (p=3 text found only in Γ-extension case analyses; no soc_K(πα) value at p=3).

## Quotes + lines (lit/bm/breuil_paskunas_supersingular.txt, 6172 lines)
- l.525–527: "We denote by socΓ S = S0 its socle and by cosocΓ S its cosocle ... If S ∈ RepK , we denote by socK S its K-socle." — two separate definitions; NO equality stated.
- l.91–93: "socGL2(OF) π denotes the socle of π seen as a GL2(OF)-representation. Recall that a weight is an irreducible representation of GL2(OF) over Fp".
- l.906–907: "Vr ... is stable under the action of K and that K1 acts trivially on Vr".
- l.912–914: "Given an irreducible representation σ of Γ, there exists a unique pair (r, a) ... such that σ ≅ Vr ⊗ det^a".
- l.224/228: Thm 1.2 hyp "K1 acts trivially on D0"; "(a) socK π = socK D0".
- l.3803 (Prop 13.1) "socΓ D0 = ⊕σ∈D σ" vs l.3972 (Thm 13.8) "socK D0(ρ) = ⊕σ∈D(ρ) σ" — same D0 type object, socle written with Γ in §13.1 and K in §13.8; the switch is used silently (strongest on-disk evidence; implicit, not stated).
- l.1590: Prop 5.1 "Let τ be a representation of K such that K1 acts trivially."
- l.2690: "Ω|K is an injective envelope of socK π in RepK,χ".
- Other socK/socΓ hits (all usage, no equality): 301, 967–1007, 1222–1235, 1405–1566, 1722–1826, 2974–3158, 3296, 3817–3843, 5635–5786.
- p=3 lines: 1317, 1744, 1780, 1809, 3500 (Γ-lemma case analyses / generic ρ remark) — none give soc_K(πα).
- 1209.5205.txt l.2695 Rem 6.2: "socK π ≅ (Symr k² ⊕ Symp−1−r k² ⊗ detr) ⊗ detm" — socK only; no socΓ.
- Breuil GL2Qp I/II: 0 hits socΓ/socK.

## Analysis
BP never states soc_K S = soc_Γ S. Chain on disk: weights are irreducible K-reps (l.92); irreducible Γ-reps are Vr⊗det^a (l.912); K1 acts trivially on Vr (l.907); §13 interchanges socΓ D0 / socK D0 for K1-trivial D0 (l.3803 vs 3972). This gives soc_K = soc_Γ for K1-trivial objects (Soft SF-implicit). Named remaining gap **GAP-SG-K1**: no verbatim BP line that every irreducible smooth K-rep is K1-trivial (i.e. soc_K π = soc_Γ(π^{K1})) for π=πα which is not K1-trivial. Not invented here.

## Carried flags
- filtration: **INVENTED CANDIDATE (10, Γ₀(7)-geometric)** + **Katz 40 Soft SF-named PARALLEL**; both live per OW both-named-parallel until Owner pick / Auditor Soft SF CONFIRM. NOT operative (Eigen Rule 5 flag).
- INV-Ind: Soft SF-INVENTED-CLOSED (SF-IC-c′ / OPEN-SK-conv, conditional).
- soc_K(πα)=Sym^{p−3}⊗det p≥5: CLOSED-conditional (sockval).
- OPEN-SK-p3 OPEN; BL94/BL95 MISS; Kerr BLOCKED; P5a not claimed.

## Tip
BEFORE: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91
AFTER: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — READ-ONLY, not edited.

## Search log
- grep -n -i -E "soc_?{?(Γ|K|\Gamma)|socle" bp.txt | wc -l → 154 (socle-family incl. filtration words)
- grep -n -E "soc_?{?(Γ|K)" bp.txt → ~75 lines listed above
- grep -n -i "p = 3|p=3" bp.txt → 5
- grep -n "K1 acts trivially|..." bp.txt → 4 (224, 908, 1590, 1854)
- grep -c socΓ/socK: 1209.5205 19; Breuil I 0; Breuil II 0
- grep "Remark 6.2" 1209.5205 → 2695, 2795
