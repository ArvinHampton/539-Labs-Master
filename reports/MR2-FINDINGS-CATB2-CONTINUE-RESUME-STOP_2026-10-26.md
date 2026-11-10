# MR2 FINDINGS — CatB-2 CONTINUE after RESUME-STOP — 2026-10-26 ~19:25 CDT (America/Chicago)
Status: **PARTIAL (near-saturated)**. Bridge PARTIAL READY NO. **P5a NOT claimed.** GAP-5 (B′ vs B″) is Owner-reserved and untouched. A1–A4 are NOT frozen.

## Authority (sha256 verified live before write)
- RESUME after accidental StopSubagent: a51992d4bf4c77df28dd5e3b5ed2d9c772cceea43a2bbe9eff96b09b8c45a5ef ✔
- Prior R3 FINDINGS: 4538981cec18fffc9a8c6bbcc53132021e6e76b5c7c7194221fc52f4073f5b97 ✔. Cited here. The FL correction (R3-1) and R3-2(a)–(e) are NOT redone.
- Eigen R5 ACCEPT of R3: 2be0d7634f2cceb97b3da2e1cfbbdbf8759fc8ef66fc6ec1310b8ac954b0b9f4 ✔
- RESUME COOK fe0d3543… and Rule 3 AUTO CONTINUE stand. Kerr BLOCKED. Mesh CANCELLED. Eigen was not woken.

## Tip lock
Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 matched before and after (READ-ONLY). **tip_touched NO.**

## Setting
f is the unique newform in S₄(Γ₀(7)), with p = 7 and a₇ = ±7 (slope 1). Each item is marked PROVED, CITE, CITE-VERIFY (a standard result recalled from memory; check the exact statement before relying on it), UNPROVEN [GAP-n], or ABSENT. No web search was run.

## R4-1. Literature not already in DEEPEN/R3 (item 1)
- **(a) Jacquet–Langlands to the definite quaternion algebra B_{7,∞} — CITE plus PROVED arithmetic.** Teitelbaum's 𝓛 (1990) is defined on the JL transfer of f to the quaternion algebra ramified at {7, ∞}, via harmonic cochains on the Bruhat–Tits tree of PGL₂(ℚ₇) modulo the S-arithmetic group from a maximal ℤ[1/7]-order. Eichler mass formula: Σ 1/|O_i^×/±1| = (p−1)/12 = 1/2 (PROVED arithmetic). For p = 7 the class number is 1 [CITE, standard: class number 1 exactly for p ∈ {2,3,5,7,13}], so the single order has |O^×/±1| = 2. **Consequence:** the cochain quotient graph has one vertex and the H3 Teitelbaum computation is very small: weight-4 harmonic cochains with values in Sym²-type coefficients on a one-vertex quotient. This is a precision gain for H3, not a computed value.
- **(b) Coleman-family formula for 𝓛 — CITE-VERIFY.** 𝓛_f = −2·(d/dk) log a_p(k) at k = 4 along the slope-1 Coleman family through f (Stevens; Colmez, "Invariants 𝓛 et dérivées de valeurs propres de Frobenius", 2005, which proves 𝓛_FM = −2 a_p′/a_p in families). This gives a **second, independent route** to v₇(𝓛_f) using only U₇-eigenvalues on overconvergent forms of nearby weights (Pollack–Stevens overconvergent modular symbols). That makes it a cross-check for H3.
- **(c) Exact Breuil–Mézard threshold for k = 4 — CITE-VERIFY, not asserted.** As I recall it, for 2 < k < p+1 the reduction is ind(ω₂^{k−1}) (irreducible) when v_p(𝓛) < 2 − k/2, and reducible when v_p(𝓛) ≥ 2 − k/2 (Breuil–Mézard 2002 Thm 1.2 / Guerberoff–Park). For k = 4 the threshold is **0**: irreducible ⇔ v₇(𝓛_f) < 0. Treat this as a pointer to verify. If it holds, GAP-4 collapses to a sign test (is 𝓛_f 7-integral?), which is weaker than a full valuation. In the irreducible branch m = k−1 = 3, and R3-2(d) gives the twist m ↦ 3+24 = 27 mod 48. ind ω₂^{27} ≇ ind ω₂^{3} (the conjugate exponent is 7·3 = 21 mod 48, not 27), so in that branch the B′ slice twist **would** be visible on inertia. This is conditional on the recalled statement.
- **ABSENT (saturated):** I know of no geometric or physics literature giving Teitelbaum cochains at St⊗χ with conductor 7² directly. This repeats R3. The search covered standard references only, not exhaustively.

## R4-2. Further F2/θ consequences (item 2; no GAP-5, no compute)
- **(a) PROVED.** θ⁶f ≡ f − V(U₇f) (mod 7) as q-expansions, i.e. θ⁶f is the 7-depletion f^{[7]}. Proof: n⁶ ≡ 1 for 7∤n and ≡ 0 for 7|n. ∎ Hence (f⊗χ₋₇)⊗χ₋₇ ≡ θ³(θ³f) = f^{[7]}. The twist is an involution up to depletion, consistent with R3-2(a).
- **(b) PROVED.** Because U₇f = a₇f = ±7f ≡ 0 (mod 7), f^{[7]} ≡ f (mod 7). So **θ⁶f ≡ f (mod 7) exactly**, and f lies in a θ-cycle of length dividing 6 mod 7. By Jochnowitz/Serre filtration theory [CITE], the filtration then satisfies w(θ⁶f) = w(f) = 4. This constrains H3's θ³ filtration: w(θ³f) ∈ {4 + 3(p+1) − j(p−1)}, i.e. it is 28 minus a multiple of 6, and must be ≥ 4. The exact value is UNPROVEN (H3).
- **(c) Residual→resonant reading — PROVED at the q-expansion level only.** The residual slice (f⊗χ₋₇ mod 7) is the θ³-image of f, and θ³ is resonant of order 2 in the length-6 cycle of (b). This is twist-only. It says nothing about ρ̄|₇ beyond R3-2(d) and R4-1(c), and it does not choose GAP-5.

## R4-3. Tightened handoffs (item 3; named only, Eigen NOT woken)
- **H1 (GAP-1):** unchanged. Written ρ̄|_{G_{ℚ₇}}: JH constituents, dims, det (to test against ω³), or ABSENT.
- **H2 (GAP-3):** unchanged from R3. Local types of the 7 non-St⊗χ new dims at level 49.
- **H3 (GAP-4, tightened):** (i) Compute 𝓛_f by Teitelbaum on the one-vertex quotient for B_{7,∞} (R4-1a). (ii) Cross-check with −2a₇′/a₇ via Pollack–Stevens (R4-1b). (iii) First verify the BM threshold statement for k = 4 (R4-1c). If threshold = 0, only "v₇(𝓛_f) < 0?" is needed. (iv) w(θ³f) ∈ {28, 22, …, ≥4} (R4-2b).
- **H4 (GAP-2):** unchanged. Method TBD.
- GAP-5 is not an Eigen ask (it is Owner-reserved).

## Summary
- **PROVED:** R4-1(a) mass arithmetic; R4-2(a),(b),(c).
- **CITE-VERIFY:** R4-1(b) Colmez/Stevens; R4-1(c) BM threshold and the irreducible-branch twist visibility.
- **UNPROVEN:** GAP-1 through GAP-4; the exact filtration.
- **ABSENT/saturated:** direct 7² Teitelbaum literature.
- **Owner-reserved, untouched:** GAP-5.

## Soft SF risks — Auditor press YES
1. R4-1(c) is recalled, not verified. Do not read it as deciding GAP-4 or as fixing the twist-visibility claim.
2. "Class number 1 at p = 7" is a standard CITE. Its use only shrinks the H3 cost.
3. R4-2 is q-expansion/filtration information, not ρ̄|₇.
4. Carry-over from R3: no P5a, no GAP-5 choice, ABSENT is not exhaustive.

tip_touched NO | Bridge PARTIAL READY NO | P5a NOT claimed | GAP-5 untouched | Kerr BLOCKED
