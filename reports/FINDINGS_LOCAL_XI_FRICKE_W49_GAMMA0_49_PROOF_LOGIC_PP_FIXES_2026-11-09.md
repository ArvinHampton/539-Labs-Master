# FINDINGS — Local Path: Ξ / Fricke W_49^Fricke / Γ₀(49) proof-logic draft with PP fixes — 2026-11-09

- Lane: Local Path, Bridge C A1→Ξ→RTA (local modular only). PP-confirmed draft: rollup 9 PROVED / 3 CONDITIONAL / 6 OPEN / 0 REFUTED.
- Written Nov 9, 2026 (~12:40 CST, America/Chicago) under the Owner's 12:29 CST additive-write grant (new dated file; no existing file edited).
- No CERT. Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` untouched, sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (re-checked). Residual≠Resonant. No new constants, no compute runs, no external/Gemini send.
- PP fixes applied: (1) C7 no longer cites E7 (E7 = V₃₅∩D₇V₃₅=0, a Γ₀(7)/W₇-neighbor statement, reports/FINDINGS_MR1_RESONANT_MATH_PREDICTIONS_NT_MODULAR_HECKE_HOLD_INVENT_2026-11-05.md:75–81); (2) the Fricke involution is written W_49^Fricke (τ↦−1/(49τ)), distinct from DMZ's Jacobi index-49 operator W₄₉^DMZ; C10 restated as forced carrier constraint.

Abbreviations: T = /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md; P = reports/FINDINGS_LOCAL_SOFTSF_PROOF_LOGIC_PASS_BRIDGEC_12INTAKES_2026-11-05.md; MR1CD = bridges/LOCAL/FINDINGS_MR1_SOFTSF_OWNER_CD_T3REF_QI_RC_TIERE_MODULAR_HOLD_INVENT_2026-11-05.md; MR1R = distributions/gemini-incoming-20261105-1536/responses/math-research-1.md (a70e3c45…); PF = /workspace/grok-batches/FINDINGS_MR1_PURSUE_MISSED_VARS_PATTERNS_2026-10-26.md; DEF = /workspace/grok-batches/DEFINITION_RTA_RESIDUALS_TO_FIFTH_ORDER_ORTHANT_CONES_LIMA_CHAIN_2026-10-26.md; O = bridges/AUDITOR/FINDINGS_MR1_RESONANT_MATH_PREDICTIONS_NT_MODULAR_HECKE_HOLD_INVENT_2026-11-05.md. (Paths relative to /workspace/quantum-comp unless absolute.)

## 1. The step as written in the corpus
- P:66 row 12 — Ξ / Fricke W₇ / Γ₀(49) map ABSENT/OPEN (no Written Ξ, Fricke positive law, T3_ref→modular map). P:67 row 13 — A1→Ξ→RTA theorem ABSENT/OPEN.
- T:22 "W₇ here = Fricke τ ↦ −1/(49τ)"; T:195 W₇=(0,−1;49,0); Γ₀(49) index 56, genus 1, ν₂=0, ν₃=2, 8 cusps. In this file the tip's "W₇" is written W_49^Fricke.
- T:283, T:309 operative G=Γ₀(49), W_49^Fricke ∉ G, P2 VACATED; T:217 ρ(W₇) CLOSED ABSENT on V₄₂.
- MR1R:11–13 asks (2) define Ξ, (3) positive Fricke eigen-law for C, (4) any T3_ref→modular derivation.
- MR1CD:29, :59 T3_ref→Fricke/residual-C map ABSENT/OPEN.
- DEF:53–55 R8: Ξ = residual weight-3/2 shadow (outer disc-35 series × shifted wt-3/2 series, characteristics 7m, 7m+7/2). DEF:57–59 R9 residual law at "Fricke samples 1/7, 3/7, 5/7, 1" OPEN. O:120–123 "Ξ is not written as an explicit series."

## 2. Classical checks
- **C1 PROVED.** W := W_49^Fricke = (0,−1;49,0) normalizes Γ₀(49): W(a,b;49c,d)W⁻¹ = (d,−c;−49b,a). W² = −49·I (scalar) ⇒ involution in PSL₂(ℝ).
- **C2 PROVED.** Atkin–Lehner W_Q requires Q‖N; for N=49, Q∈{1,49} (gcd(7,7)=7). det(7a,b;49c,7d)=49(ad−bc)≠7. No determinant-7 "W₇" exists at level 49 (= PF:33). The tip's "W₇" (T:22) is a name for W_49^Fricke; no contradiction with PF.
- **C3 PROVED.** W_49^Fricke ∉ Γ₀(49) (T:283): normalized to det 1 it is (0,−1/7;7,0), non-integral.
- **C4 PROVED** (T:195, T:260): index 49(1+1/7)=56; ν₂=0 (−1 non-residue mod 7); ν₃=2 (−3≡4 square mod 7, Hensel); cusps φ(1)+φ(7)+φ(1)=8, widths 1, 49, 1×6 (sum 56); g = 1+56/12−2/3−8/2 = 1.
- **C5 PROVED.** A=diag(7,1): A(a,b;49c,d)A⁻¹=(a,7b;7c,d), so AΓ₀(49)A⁻¹ = Γ₀(7)∩Γ⁰(7) ⊇ Γ(7); A·W_49^Fricke·A⁻¹ = (0,−7;7,0) ~ S. Normalizer of Γ₀(49) in PSL₂(ℝ) = Γ₀(49)⁺ = ⟨Γ₀(49), W_49^Fricke⟩ (Atkin–Lehner, Math. Ann. 185 (1970) 134–160; Conway–Norton 1979 §3, h=1; extra normalizer elements only when 4|N or 9|N).
- **C6 PROVED.** W_49^Fricke swaps ∞↔0; a/7 ↦ −1/(7a), fixed only if a²≡−1 (mod 7), impossible ⇒ no fixed cusp. Consistent with operative T:260 ("no W₇-orbit merge").
- **C7 PROVED.** dim S₂(Γ₀(49)) = g = 1 ⇒ S₂ = ℂf, f|₂W_49^Fricke = εf, ε=±1. W(i/7)=i/7 gives a fixed point on X₀(49); holomorphic Lefschetz: #Fix = 2−2ε > 0 ⇒ ε = −1, #Fix = 4. f is the newform LMFDB 49.2.a.a, attached to Cremona 49a1 (CM by ℤ[(1+√−7)/2], j = −3375); root number w = −ε = +1, consistent with analytic rank 0 in Cremona's tables (Cremona, *Algorithms for Modular Elliptic Curves*, Table 1; Atkin–Lehner 1970 for W_N theory). [PP fix: E7 is not cited here.]
- **C8 PROVED.** X₀(49) genus 1 ⇒ no Hauptmodul; Riemann–Hurwitz with 4 fixed points ⇒ X₀(49)⁺ genus 0 (has one). No corpus claim of a Hauptmodul for X₀(49) found (rg 'Hauptmodul': no hits) — nothing to refute.
- **C9 CONDITIONAL** on DMZ §4.6 eq. 4.39–4.41: the Jacobi index-49 operator W₄₉^DMZ acts on J_{k,49} as (−1)^k (T:317). This is not W_49^Fricke (T:22 naming note); cited, not re-proved.

## 3. Corpus claims
- **C10 CONDITIONAL (forced carrier constraint).** T:316 "scalar W₇ slash law (f|W₇=±f) is already excluded" (and RTA Thm 11.5(iii), T:40, not read). The unrestricted scalar reading is refuted by C7 (49a1 / 49.2.a.a has f|W_49^Fricke = −f), so T:316 can only stand as a constraint on the residual's carrier (vector-valued V), not as a statement about scalar forms on Γ₀(49).
- **C11 CONDITIONAL** on R26/R36 (no invertible intertwiner; not re-proved): ρ(W₇) CLOSED ABSENT on V₄₂, P2 VACATED (T:217, T:309).
- **C12 OPEN.** Invented Role A ε=+1 on V₄₂ (bridges/AUDITOR/FINDINGS_MR1_INVENT_CLOSE_EXACTNU_PATHA_FRICKE_ROLEA_2026-10-27.md:33–36): different space from S₂, not contradicted by C7, unproved.
- **C13 OPEN.** Positive Fricke eigen-law for residual C (MR1R:12): cannot be carried by the scalar weight-2 newform (C7); needs a Written carrier with a W_49^Fricke action — none.
- **C14 OPEN.** Ξ (DEF:53–55) has no stated level, multiplier or group; no Γ₀(49) link (O:120–123; reports/FINDINGS_LOCAL_BRIDGE_C_A1_XI_RTA_STATUS_SNAP_SOFTSF_2026-10-27.md:13,48 "Ξ unidentified"). Written ρ is SL₂(ℤ)-level 140, "not a representation of Γ₀(49)⁺" (/workspace/grok-batches/MR1-AUTHOR-PURSUE-N2-W7-GENS_2026-10-25.md:31); Weil↔Γ₀(49) dictionary "not supplied" (T:297).
- **C15 OPEN.** R9 law from Fricke samples at 1/7, 3/7, 5/7, 1 (DEF:57–59).
- **C16 OPEN.** T3_ref→W_49^Fricke/Γ₀(49)/residual-C map (MR1CD:29, :59; O2 at O:125–127). Answer to MR1 ask 4: none Written.
- **C17 OPEN.** A1→Ξ→RTA theorem (P:67).
- **C18 PROVED (relevance OPEN).** Level-7 weight-3 η-quotients with character (·/−7) (bridges/EIGEN/MR2-FINDINGS-DUAL-CONTINUE-gap-filtr-68_2026-10-27.md:14): Ligozat congruences hold by hand — h: Σδr=24, Σ(7/δ)r=24; u: 0, 48; v: 48, 0. Not a Ξ / W_49^Fricke claim.
- Nonlocal items (EH11D, reverse-parity PT): out of lane, OPEN, not rejected.

## 4. Minimum Owner definitions (no new constants)
(i) Ξ as a specific function: group (Γ₀(49), Γ₀(49)⁺, or Mp₂(ℤ)+lattice), weight 3/2, multiplier/ρ. (ii) The carrier on which W_49^Fricke acts, and the "positive law" as an equation (e.g. Ξ|W = +Ξ or a ρ(W) relation). (iii) The T3_ref→modular map: domain, codomain, property (e.g. equivariance). (iv) The Weil(level 140)↔Γ₀(49) dictionary, or dropping level 49 from Ξ. (v) A1→Ξ→RTA as a theorem with hypotheses.

## 5. Rollup
PROVED 9 · CONDITIONAL 3 · OPEN 6 · REFUTED 0 (PP-confirmed). No CERT. Tip untouched. Residual≠Resonant.
