# MR2 FINDINGS — CatB-2 Teitelbaum / BT / residual→resonant DEEPEN (resume COOK) — 2026-10-26 ~19:00 CDT (America/Chicago)
Status: **PARTIAL** (slice sharpened, with one new PROVED residual identity and named conditions for Prop B. ρ̄|₇ is still ABSENT. Bridge PARTIAL READY NO. **Does NOT prove P5a.**)

## Authority (live sha256 verified before write)
- OW RESUME NINE COOK: fe0d3543028b801643d342466853d85bdce2f1bb47295e936a5c2bd7a3373d1b ✔
- Soft SF PRESS of that OW: 0d60200944d94dcfe9e18d4067e29070027d7f568ffd811bfb1ccf6081f846f1 ✔
- Prior CatB-2 CONTINUE: f0ac57fbe5752619ff3fbe69a2260ede117a33de77ed1dd10d072dcc10d8b998 ✔. This report cites it and deepens from its gaps. Lemma A is not redone.
- Pairing: Eigen↔MR2 Rules 4–5 (OW e7f50719…). Eigen was not woken. Kerr BLOCKED. Mesh CANCELLED. Cat-A gate OFF. Nine roster.
- FREE-PURSUE (0bc25f00…) and ARCHIMEDEAN (2841b2ba…) are not needed and not cited. G2 Ω₀ is not tip-folded.

## Tip lock
Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 matched at start and end. **tip_touched NO.**

## Standard
Every item is marked PROVED (argument given), CITE (standard literature), UNPROVEN [GAP-n], or ABSENT.

## F1. Literature on Teitelbaum cochains at conductor 7² / St⊗χ / twist-to-level-7
- [CITE] Teitelbaum (1990) and Darmon (2001) build harmonic cochains on the Bruhat–Tits tree for forms that are Steinberg at p, which needs p‖N. At N = 49 the St⊗χ₋₇ line can be reached **only** by untwisting to level 7 (Lemma A, CONTINUE) and then twisting back. The cochain is attached to f (level 7), not to f⊗χ₋₇ directly.
- [CITE] Loeffler–Weinstein ("On the computation of local components of a newform") gives the algorithm that would determine the local types (PS/SC/St⊗χ) of the 8 new dims at 49. Running it is computation, which is Eigen's lane (see handoff H2).
- [CITE] Pollack–Stevens (overconvergent modular symbols) handles a finite-slope p-stabilised form. It reaches the twisted line only through f. It gives no new constraint at 7².
- **ABSENT:** I know of no geometric or physics paper that puts Teitelbaum cochains *directly* at conductor p² with St⊗χ type, i.e. without untwisting. This scan was from standard references. No new web hit was sought or used, so saturation is relative to those references. Nothing in this item goes beyond CONTINUE except the explicit statement "via f only".

## F2. Residual identity on the slice — PROVED (new)
- **Claim:** f⊗χ₋₇ ≡ f⊗ω³ (mod 7), where ω is the mod-7 cyclotomic character. Equivalently, ρ̄_{f⊗χ₋₇} ≅ ρ̄_f ⊗ ω³.
- **Proof:** χ₋₇ is the Legendre symbol (·/7). By Euler's criterion, (a/7) ≡ a³ (mod 7) for every a prime to 7. So χ₋₇ mod 7 = ω^{(7−1)/2} = ω³. Twisting the Galois representation by this character gives the stated isomorphism. ∎
- **Consequence:** a mod-7 residual class on the slice is the *Teitelbaum class of f twisted by ω³*. It is not a new residual object. Resonance on the slice therefore reduces to how ρ̄_f ⊗ ω³ relates to ρ̄|₇.
- Weight 4 ≤ p+1 = 8, so Fontaine–Laffaille applies at 7 for f [CITE]. f has level 7 and weight 4, and is Steinberg at 7, so a_7(f) = ±7^{1} = ±7 and a_7 ≡ 0 (mod 7). Hence ρ̄_f|_{I_7} is **not ordinary-split by a unit root**. Whether ρ̄_f|_{G_7} is irreducible (the "supersingular-like" case) is **[GAP-4]** (UNPROVEN here; Eigen can compute it).

## F3. Prop B sharpened — named conditions (slice only)
CONTINUE's Prop B assumed that "the slice, as an SL₂(ℤ/7)-representation, is a character". That step is **not justified**: the slice is a Hecke eigenline, not obviously an SL₂(ℤ/7)-module. I am restating Prop B so that every hypothesis is named:
- **B1 [GAP-5, new]:** an SL₂(ℤ/7) (or G_{ℚ₇}) action on the mod-7 slice must be specified. The natural candidate is ρ̄_f⊗ω³ restricted to G_{ℚ₇} (from F2), which is 2-dimensional, *not* a character. So CONTINUE's Schur argument applies only if the action is the scalar Hecke action. This must be decided by Owner/Written definition.
- **B2 [GAP-1]:** ρ̄|₇ is Written. It is ABSENT.
- **Prop B′ [PROVED conditional]:** Let the slice carry the action V = ρ̄_f⊗ω³|_{G_7} (B1). If both ρ̄|₇ and V are semisimple and they share no Jordan–Hölder constituent, then Hom(ρ̄|₇, V) = 0, so there is no resonant close on the slice. Proof: a nonzero map between semisimple modules forces a common simple summand (Schur). ∎
- **Prop B″ [PROVED conditional]:** If the action is instead the scalar Hecke character (CONTINUE's reading) and ρ̄|₇ has no 1-dim constituent, the original Prop B holds.
- Under the {3,5,6}/7 float hint (non-Written), a 3-dim irreducible ρ̄|₇ shares no constituent with a ≤2-dim V. **Both** B′ and B″ would then give slice non-resonance. This is conditional on GAP-1, and on B1 for the choice of reading.
- GAP-2 (multiplicity) and GAP-3 (PS/SC, 7 of the 8 new dims, and 503/89) stand **unchanged**. Slice non-resonance ≠ vanishing of the 592-space. **P5a is NOT claimed.**

## F4. Fillable vs blocked
- **Filled:** F1 literature statement (with an ABSENT stamp), F2 residual identity (PROVED), the B1 correction to CONTINUE, and Prop B′/B″ (conditional, PROVED).
- **Blocked:** GAP-1, GAP-2, GAP-3, GAP-4, GAP-5.

## Soft SF risks — Auditor press YES
1. CONTINUE's Prop B rested on an unjustified "slice = character" step. F3/B1 corrects this, and the Auditor should press the correction.
2. Reading B′/B″ under the float hint as *proved* non-resonance (it depends on GAP-1).
3. Reading slice non-resonance as P5a or as 592-vanishing.
4. Reading F2 (a mod-7 identity) as information about ρ̄|₇ (it is information about ρ̄_f only).
5. Treating the literature ABSENT stamp as exhaustive.

## Eigen handoff asks (Rule 4 — partner asks, for the parent to send; NOT filled here)
- **H1 (GAP-1):** the Written local type of ρ̄ at 7 (ρ̄|_{G_{ℚ₇}}, its semisimplification, and its dims of constituents), or a confirmation that it is still ABSENT.
- **H2 (GAP-3 / GAP-A3 overlap):** the newform decomposition of S₄(Γ₀(49)) new (8 dims), with the local type at 7 of each (Loeffler–Weinstein), plus dim M₄(ρ̄) (the GAP-A3 overlap) if defined in Eigen's frame.
- **H3 (GAP-4):** ρ̄_f|_{G_{ℚ₇}} for f ∈ S₄(Γ₀(7)): is it irreducible or reducible mod 7?
- **H4 (GAP-2):** the multiplicity of ρ̄ in the integral cochain lattice, if Eigen has a method.
- GAP-5 (which action to use, B1) is an Owner/Written definition question, not an Eigen one.

tip_touched NO | Bridge PARTIAL READY NO | P5a NOT claimed | Kerr BLOCKED | no Eigen material used
