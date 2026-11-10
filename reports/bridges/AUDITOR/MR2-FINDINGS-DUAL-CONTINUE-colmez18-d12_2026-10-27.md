# MR2 FINDINGS — DUAL-CONTINUE — colmez18 D1+D2 notation verify — 2026-10-27
Role: Math Research 2, Soft SF writer. REPORTS ONLY — no RECS. Soft SF → Auditor; FINDINGS → Eigen Rule 5. Kerr BLOCKED (not invoked). No agents messaged.
Tip (READ-ONLY, not edited; tip_touched NO): /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md
- BEFORE sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH (expected 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91)
- AFTER  sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH
Invent lift verified: reports/OWNER_WRITE_INVENT_BAN_LIFTED_ALL_LANES_PURSUE_FREEDOM_RIGHT_AUTHORITY_2026-10-27.md sha256 5cbc33ac93f166eec2b0680e0435b87c4eb97fd762777da6df8932c23eb23640 MATCH; amend reports/OWNER_WRITE_AMEND_INVENT_LABEL_PENDING_MATH_PROOF_2026-10-27.md sha256 c9dd3a0a79a0698ff9d454efeea903d20f3c5b41b085c3fbcdcedc39eb22d64e MATCH. Invent NOT used this turn.
Sources (on-disk only): lit/bm/1209.5205.txt; lit/bm/colmez_ast330.txt (pdftotext of NumDAM PDF sha ccf1a070…3568; OCR-garbled symbols restored in [brackets]).
Absorbed parent: FINDINGS colmez18 sha 2f3adf5f…67d3; PRESS colmez18 sha c38951d5…6708.

## D1 — π_α (BM) = B(1,ω) (Colmez)
- BM 1209.5205.txt l.2814–2815: "π_α := Ind_P^G ω⊗ω^{-1}" (OCR: "πα := IndG / Bω⊗ω −1"); twist χ∘det trivial (l.2812–2814 "(Sp⊕1⊕π_α)⊗χ∘det").
- BM l.1283: "we write χ1⊗χ2 for a character of P, which maps (a b;0 d) to χ1(a)χ2(d)"; l.1277–1279 P = upper triangular.
- Colmez l.4033–4034 (Rem. III.3.4): "on note δ1⊗δ2 le caractère de B défini par (a b;0 d) ↦ δ1(a)δ2(d)" — SAME convention as BM.
- Colmez l.4002–4003: Ind_B W = locally constant φ on G with φ(bg)=b·φ(g), G by translation — smooth induction, as BM.
- Colmez l.4106–4108: "isomorphisme G-équivariant de Ind_B δ1⊗δ2 sur B(δ2ω, δ1) (et donc B(δ1,δ2) = Ind_B δ2⊗δ1ω^{-1})"; l.4110 "B(δ1,δ2) = Ind_B δ2⊗δ1ω^{-1}".
- Substitute δ1=1, δ2=ω: B(1,ω) = Ind_B ω⊗ω^{-1} = π_α. Consistency: Colmez l.4192 B(ω,1) = Ind_B 1⊗1 ⊃ constants, quotient St (l.4196) — matches BM Sp ⊂ Ind 1.
- Soft SF STATUS D1: MATCH — CLOSED Soft SF (verbatim, modulo OCR).
- Residual: GAP-D1-OCR (symbols δ/ω/⊗ restored from OCR garble at l.4106–4110, l.2814). Not a mathematical gap. Soft SF hygiene: RECS-edge phrase removed (REPORTS ONLY).

## D2 — V(ω,1,τ^⊥) = non-split 0→ω→ρ→1→0; V Colmez = BM's V
- Colmez l.10318–10322 (§VII.3): "Si p≠2, H^1(G_Qp,k_L)=Hom(Qp^×,k_L) et H^1(G_Qp,k_L(ω)) … dimension 2, mis en dualité parfaite par le cup-produit … Si τ∈Hom(Qp^×,k_L) est non nul, on note V(ω,1,τ^⊥) l'extension de k_L par k_L(ω) dont la classe dans H^1(G_Qp,k_L(ω)) engendre l'orthogonal de τ." l.10324–10326: V(δω,δ,τ^⊥) extension of k_L(δ) by k_L(δω); every non-trivial such extension is of this form.
- Colmez "extension de A par B" = 0→B→E→A→0 (cf. l.485 E_τ "extension de 1 par St", l.11019 Π "extension de B(1,ω) par E_τ", matching BM (43) 0→E_φ→β→π_α→0). Hence V(ω,1,τ^⊥): 0→ω→V→1→0, class ≠0 (generates a line) ⇒ non-split.
- BM l.2941–2965: same cup-product pairing H^1(k)×H^1(k(ω))→H^2(k(ω))≅k; "kφ^⊥ defines a non-split extension 0→ω→ρ→1→0. It is shown in [18, VII.4.24] that V(β)≅ρ, which implies V̌(β^∨)≅ρ." With τ=φ: ρ = V(ω,1,φ^⊥). Colmez Prop VII.4.24 l.11019–11020 (and parallel Intro Thm l.483–487 (iii)).
- Functor: BM l.1363 "In [18], Colmez has defined an exact and covariant functor V …"; l.1367 "We modify Colmez's functor"; l.1377 V̌(M):=V(M^∨)^∨(εζ); BM ref l.3796 "[18] P. Colmez, … Astérisque 330 (2010) 281–509" = our colmez_ast330. BM l.2963 applies V (unmodified) to β. So V(BM) = V(Colmez) by BM's own definition.
- Soft SF STATUS D2: MATCH — CLOSED Soft SF (verbatim, modulo OCR).
- Residual narrowed: GAP-D2-OCR (glyph restoration l.10318–10326, l.11019–11020); GAP-D2-P2 (Colmez defines V(ω,1,τ^⊥) under p≠2, l.10318; BM standing hypothesis on p not re-cited this turn — named, not asserted). GAP-D2-VCHECK (passage V→V̌ via l.1377 twist (εζ) and duality is BM's own implication l.2964; not re-derived).

## β↔ρ overall
D1 + D2 CLOSED Soft SF ⇒ dictionary BM↔Colmez complete for VII.4.24; β↔ρ: CLOSED Soft SF (verbatim, cond. on GAP-D1-OCR, GAP-D2-OCR, GAP-D2-P2 non-math residuals). NOT OPERATIVE, not tip-folded. CAND-β↔ρ invent (parent) now superseded by verbatim MATCH; its prior status (closed under invent lift (cond.) NOT OPERATIVE) carried unchanged as record. No new invent label used.

## Carried flags (unchanged)
- Orientation 0→ω→ρ→1→0 CLOSED Soft SF without [18] — not reopened.
- filtr invented pending mathematical proof CANDIDATE (10)+40 PARALLEL both live NOT OPERATIVE.
- INV-Ind Soft SF closed under invent lift (cond.).
- GAP-SG-K1; GAP-SK-p3-1 — open, carried.
- Kerr BLOCKED. Tip LOCK READ-ONLY.
