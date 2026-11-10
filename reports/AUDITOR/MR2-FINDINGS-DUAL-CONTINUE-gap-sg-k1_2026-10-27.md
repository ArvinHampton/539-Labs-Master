# MR2 FINDINGS — DUAL-CONTINUE gap-sg-k1 (2026-10-27)
REPORTS ONLY — No RECS. Soft SF → Auditor. FINDINGS → Eigen Rule 5. Kerr BLOCKED (not invented). No tip fold. NOT OPERATIVE.

## Tip
BEFORE: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH
AFTER:  7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH — READ-ONLY, tip_touched NO.

## Invent lift verification
- reports/OWNER_WRITE_INVENT_BAN_LIFTED_ALL_LANES_PURSUE_FREEDOM_RIGHT_AUTHORITY_2026-10-27.md sha256 on disk = d087ff9d07f4b58a37aa27c8a85309c16b12969d4e38f661955573dee67de5b4 — **MISMATCH** vs expected 5cbc33ac93f166eec2b0680e0435b87c4eb97fd762777da6df8932c23eb23640 (file mtime 2026-10-27 12:17:58 CDT; its .sha256 sidecar lists d087ff9d…). Earlier sibling colmez18-d12 recorded 5cbc33ac… MATCH.
- Amend reports/OWNER_WRITE_AMEND_INVENT_LABEL_PENDING_MATH_PROOF_2026-10-27.md sha256 c9dd3a0a79a0698ff9d454efeea903d20f3c5b41b085c3fbcdcedc39eb22d64e MATCH.
- Invent **NOT used** this turn (verbatim MATCH found; lift mismatch is moot for this lane). No "invented pending mathematical proof" claim made.

## Soft SF STATUS — GAP-SG-K1
**CLOSED Soft SF (verbatim MATCH, one-line deduction named)** — NOT OPERATIVE.

## Quotes + lines (lit/bm/)
- breuil_paskunas_supersingular.txt l.557: "We call a weight an irreducible representation of K (hence of Γ) on Fp ." — verbatim: every irreducible (smooth, Fp-) K-rep is a Γ = K/K1-rep, i.e. K1 acts trivially. This is the GAP-SG-K1 content.
- breuil_paskunas_supersingular.txt l.499–501: "I1 ⊂ I is the subgroup of matrices that are sent to U ⊂ B via K ↠ Γ" — fixes K ↠ Γ with kernel K1 (cf. l.152–153 "K1 ⊂ I1 the first congruence subgroup of GL2(OF)").
- breuil_paskunas_supersingular.txt l.91–93: weight = irreducible GL2(OF)-rep over Fp; "GL2(OF)-socle is the maximal semi-simple GL2(OF)-subrepresentation".
- breuil_paskunas_supersingular.txt l.525–527: socΓ / socK definitions (separate).
- breuil_paskunas_supersingular.txt l.907–908, l.912–914: K1 trivial on Vr; irreducible Γ-reps = Vr⊗det^a.
- Supporting mechanism (not BP): 1209.5205.txt l.1135: "Let σ be an irreducible smooth k-representation of K. Since P is a pro-p group, σ^P ≠ 0" (pro-p fixed vectors), l.999–1001 pro-p Sylow P.

## Deduction (Soft SF-named, not verbatim in BP)
From l.557 every irreducible K-subrep of π lies in π^{K1}; hence soc_K π = soc_K(π^{K1}) = soc_Γ(π^{K1}) (π^{K1} a Γ-rep, l.159; K-subreps of π^{K1} = Γ-subreps). Applies to π=πα without π being K1-trivial. Residual: none named for GAP-SG-K1; the deduction step is one-line and labeled Soft SF-implicit.
- Consequence for parent: soc_K(πα)=soc_Γ(πα^{K1}) Soft SF-closed (verbatim l.557 + named deduction); parent sock-gamma NARROWED status reads with GAP-SG-K1 CLOSED Soft SF. Not tip-folded.

## Prove attempt (deduction step; no invent claim, INV-SG-K1 not created)
Status: **PROVED** (standard argument, Soft SF; not verbatim BP).
1. K1 is an open normal pro-p subgroup of K=GL2(OF) (kernel of K↠Γ, BP l.499–501, l.152–153).
2. Let σ ⊂ π be an irreducible smooth K-subrep over Fp. σ is finite-dim (smooth + irreducible for profinite K: a nonzero vector has open stabilizer, its K-span is finite-dim). The image of K1 in GL(σ) is a finite p-group acting on an Fp-space, so σ^{K1} ≠ 0 (cf. 1209.5205 l.1135 for pro-p P).
3. K1 normal ⇒ σ^{K1} is K-stable; σ irreducible ⇒ σ^{K1}=σ, so σ ⊂ π^{K1}. (= BP l.557 "hence of Γ".)
4. Hence every irreducible K-subrep of π lies in π^{K1}, so soc_K π = soc_K(π^{K1}). K acts on π^{K1} through Γ (BP l.159), and K-subreps of π^{K1} = Γ-subreps, so soc_K(π^{K1}) = soc_Γ(π^{K1}).
Conclusion: soc_K π = soc_Γ(π^{K1}) for every smooth π over Fp, in particular π=πα (no K1-triviality of π needed). NOT OPERATIVE; not tip-folded.

## Carried flags (unchanged)
- sock-gamma parent (bcc1f2f4…): soc_K(πα)=soc_Γ(πα) NARROWED Soft SF-named; GAP-SG-K1 now CLOSED Soft SF here.
- Eigen ACCEPT Soft SF NARROWED+FLAG 01729d28… (GAP-SG-K1).
- Colmez D1+D2 CLOSED Soft SF β↔ρ verbatim — FINDINGS a93a7677… PRESS 0cff7b28… — NOT OPERATIVE.
- filtr invented pending mathematical proof CANDIDATE (10) + 40 PARALLEL, both live, NOT OPERATIVE.
- INV-Ind Soft SF closed under invent lift (cond.); GAP-SK-p3-1 OPEN Soft SF; OPEN-SK-p3 OPEN; Kerr BLOCKED; tip LOCK.

## Search log
- grep -n -i -E "pro-p|normal subgroup|factor(s)? through|irreducible.*representations? of (K|GL2…)" over BP, 1209.5205, Breuil I/II, bm02 → hits incl. BP l.92, 557; 1209.5205 l.999–1135.
- sed BP l.495–530, 553–560; 1209.5205 l.995–1002, 1125–1140.
