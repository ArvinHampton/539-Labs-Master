# MR2 FINDINGS — CatB-2 CONTINUE under PARTIAL (R3) — 2026-10-26 ~19:10 CDT (America/Chicago)
Status: **PARTIAL**. Bridge PARTIAL READY NO. **P5a NOT claimed.** GAP-5 is Owner-reserved and untouched: B′ and B″ both stay conditional. Arch A1–A4 are NOT frozen as OW premises.

## Authority (sha256 verified live before write)
- Rule 3 AUTO-APPROVE via Physicist: CONTINUE CatB-2 deepen under PARTIAL (conditional Prop B).
- Prior DEEPEN-RESUME FINDINGS ff52d988ac52ca3ad1c96edd8d704d9aa42d6eea9fbb34bc1bcb598bf250026a ✔. Cited here. The F2 residual identity and Lemma A are NOT redone.
- Eigen R5 REVIEW ACCEPT 7429206028dbe8f36aa3667d176aeb122891bed8225bbe497592df6e22535333 ✔. Cited.
- RESUME COOK OW fe0d3543… stands. Eigen Rules 4–5. Eigen was not woken. Kerr BLOCKED. Mesh CANCELLED. Nine roster. No tip fold.

## Tip lock
Tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 matched before and after (READ-ONLY). **tip_touched NO.**

## Standard
Each item is marked PROVED, CITE, UNPROVEN [GAP-n], or ABSENT. Setting: f is the unique newform in S₄(Γ₀(7)) (dim = 1), and p = 7.

## R3-1. Correction to DEEPEN F2's local claim — Fontaine–Laffaille does NOT apply (PROVED, Soft SF)
- DEEPEN F2 said "Fontaine–Laffaille applies at 7 for f". That is wrong as stated. f is Steinberg at 7, so ρ_f|_{G_{ℚ₇}} is semistable and **not crystalline** (N ≠ 0). Fontaine–Laffaille covers only crystalline representations with Hodge–Tate weights in [0, p−2], so the weight bound k = 4 ≤ p+1 does not license it. ∎
- The correct tool is [CITE] Breuil–Mézard (2002), together with later semistable-reduction work (Guerberoff–Park; Chitrao–Ghate–Yasuda). For semistable weight k with 2 < k < p+1, ρ̄ depends on the **L-invariant** 𝓛_f through its 7-adic valuation. It is either irreducible (an induced ω₂-power) or reducible, according to v₇(𝓛_f) relative to a threshold depending on k.
- **[GAP-4, sharpened]:** whether ρ̄_f|_{G₇} is irreducible reduces to v₇(𝓛_f) for f ∈ S₄(Γ₀(7)). For k = 4, p = 7, I do NOT assert the exact threshold or which branch holds (UNPROVEN). Both depend on the precise Breuil–Mézard statement, which needs verification.
- The DEEPEN conclusion "a₇ ≡ 0 mod 7 ⇒ not unit-root ordinary" still stands: a₇ = ±7^{k/2−1} = ±7.

## R3-2. F2 consequences that hold under BOTH B′ and B″ (no GAP-5 choice)
- **(a) θ-operator form — PROVED.** As q-expansions, f⊗χ₋₇ ≡ θ³f (mod 7), where θ = q·d/dq. Proof: θ³f = Σ n³aₙqⁿ. For 7∤n, n³ ≡ (n/7) = χ₋₇(n) mod 7 (Euler). For 7|n, n³ ≡ 0 = χ₋₇(n). So the coefficients agree for every n. ∎ By [CITE] Serre/Katz/Jochnowitz θ-cycles, the mod-7 filtration satisfies w(θ³f) ≤ 4 + 3·8 = 28. The exact filtration and Serre weight are UNPROVEN here (a computation, so part of H3).
- **(b) Hecke eigensystem — PROVED.** For primes ℓ ≠ 7, a_ℓ(f⊗χ₋₇) ≡ ℓ³·a_ℓ(f) (mod 7). The coefficient at 7 is 0. This is the scalar Hecke character that B″ would use. It is fully determined by f, and no GAP-5 choice is needed to state it.
- **(c) Determinant — PROVED.** det ρ̄_f = ω^{k−1} = ω³. So det(ρ̄_f⊗ω³) = ω³·ω⁶ = ω³, because ω has order 6. The twist preserves the determinant. A constituent test against ρ̄|₇ can therefore use det = ω³ as a necessary condition under B′. (B′ is still conditional.)
- **(d) Inertial invariance in the reducible branch — PROVED conditional on that branch of GAP-4.** Suppose ρ̄_f|_{I₇}^{ss} = ω^a ⊕ ω^b with a+b ≡ 3 (mod 6), and assume (UNPROVEN) {a,b} = {0,3}, which is the Hodge–Tate-compatible ordinary-type shape. Twisting by ω³ sends {0,3} → {3,0}. So V|_{I₇}^{ss} ≅ ρ̄_f|_{I₇}^{ss}: on inertia, the slice twist is invisible. Consequence: in that branch, B′'s JH test against ρ̄|₇ restricted to I₇ is the same as testing against ρ̄_f itself. In the irreducible branch (ind ω₂^m), the twist sends m ↦ m+24 mod 48 (ω = ω₂⁸), which can change the induced character. Not computed.
- **(e) Slice identification — PROVED.** f⊗χ₋₇ is a newform of level 49: its 7-component is St⊗χ with χ ramified quadratic, conductor 7². Since dim S₄(Γ₀(7)) = 1, **exactly one** of the 8 new dimensions at 49 is of St⊗χ type. The other 7 are PS or SC (GAP-3 unchanged). This sharpens H2 to a 7-dim local-type question.

## R3-3. Literature (item 1)
- [CITE] Breuil–Mézard (2002), and Breuil, "Sur quelques représentations modulaires et p-adiques de GL₂(ℚ_p)" (semistable case): these give ρ̄ in terms of 𝓛. They are new and relevant to B′, because they determine V = ρ̄_f⊗ω³|_{G₇}.
- [CITE] For 𝓛-invariant computation of weight-4, level-p forms, there are Teitelbaum's 𝓛-invariant via Bruhat–Tits cochains (Teitelbaum 1990 *Invent.*) and Darmon's 𝓛 = 𝓛_Teitelbaum = 𝓛_FM (Fontaine–Mazur) comparison (Iovita–Spiess; Breuil). This **links Teitelbaum cochains to GAP-4**: the Teitelbaum 𝓛-invariant of f decides the reducibility branch. This is the sharpest new twist-only Teitelbaum statement here. The reach is still only "via f" (DEEPEN F1).
- B″ gets no new literature: a scalar Hecke character is insensitive to 𝓛.
- **ABSENT:** I know of no geometric or physics reference for Teitelbaum cochains directly at St⊗χ conductor p². This is relative to standard references only, as in DEEPEN. No web search was run.

## Findings summary
- **PROVED:** R3-1 (FL is inapplicable, which corrects DEEPEN); R3-2 (a) θ³, (b) eigensystem, (c) det, (e) the 1-of-8 slice; R3-2 (d) conditional on its branch.
- **UNPROVEN:** GAP-1 (ρ̄|₇), GAP-2 (multiplicity), GAP-3 (7 remaining dims, 503/89), GAP-4 (now = v₇(𝓛_f) branch), θ³ filtration/Serre weight, the Breuil–Mézard threshold for k=4, p=7.
- **ABSENT:** ρ̄|₇ Written; direct-7² Teitelbaum literature.
- **Owner-reserved, untouched:** GAP-5 (B′ vs B″). B′ and B″ are both conditional. A1–A4 are not frozen.

## Soft SF risks — Auditor press YES
1. DEEPEN F2's "Fontaine–Laffaille applies" was incorrect (Steinberg ⇒ non-crystalline). Press the R3-1 correction.
2. Reading R3-2(d) inertial invariance as unconditional (it needs the reducible branch and {0,3}).
3. Reading any R3 item as choosing GAP-5. R3-2(b) informs B″ and (c)/(d) inform B′, but neither is selected.
4. Reading the 𝓛-invariant link as deciding GAP-4 (no value is computed).
5. Carry-over: no P5a, no 592-vanishing, F2 is not information about ρ̄|₇, and ABSENT is not exhaustive.

## Eigen handoff asks (Rule 4 — named only; Eigen NOT woken; all remain UNPROVEN gaps)
- **H1 (GAP-1):** Written ρ̄|_{G_{ℚ₇}}, its JH constituents with dims, **and det** (to test against det V = ω³), or ABSENT.
- **H2 (GAP-3):** local types (Loeffler–Weinstein) of the **7** non-St⊗χ new dims of S₄(Γ₀(49)). The St⊗χ line is identified as f⊗χ₋₇ (R3-2e). Plus dim M₄(ρ̄) if defined.
- **H3 (GAP-4, tightened):** compute v₇(𝓛_f) for f ∈ S₄(Γ₀(7)) (Teitelbaum or Darmon cochain, or modular-symbol 𝓛). Apply Breuil–Mézard to get ρ̄_f|_{G₇} (irreducible ind ω₂^m with m, or reducible with inertial exponents). Also compute the θ-filtration w(θ³f) mod 7.
- **H4 (GAP-2):** multiplicity in the integral cochain lattice. Method TBD.
- GAP-5 is not an Eigen ask (it is Owner-reserved).

tip_touched NO | Bridge PARTIAL READY NO | P5a NOT claimed | GAP-5 untouched | Kerr BLOCKED
