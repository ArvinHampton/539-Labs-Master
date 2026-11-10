# RELABEL — Local Path: Ξ Weil-carrier file after the PP 15:25 audit — 2026-11-09

- **Target:** reports/FINDINGS_LOCAL_DERIVE_XI_WEIL_VECTOR_CARRIER_FRICKE_PLUS1_DICTIONARY_2026-11-09.md (sha ae951f3e7aa5be4b3829cc34fa29ea2d841ff08bff09529b4bf7f4c7effbb091), cited below as "XW". Its citation addendum is ADDENDUM_LOCAL_XI_WEIL_CARRIER_CITE_MR1_AMEND_2026-11-09.md (ed63348d…). Neither file is edited.
- **Audit:** reports/FINDINGS_PP_AUDIT_LOCAL_XI_WEIL_CARRIER_FRICKE_DICTIONARY_2026-11-09_1525.md, sha 389c2f7cd9ea86f4117e502636ab359077ff3f4f0b8f0437eaf1f6c06e40409d (verified). Verdict MATCH.
- **Written:** ~3:35 PM CST (America/Chicago). Additive file. Tip 7cddb188… read-only; sha re-checked. No CERT. Nothing sent outside.
- **Local checks:**
  - numpy: explicit 140×140 Weil representation of N₂, ρ(T) = diag e(q), ρ(S) = 140^{−1/2}(e(−(γ,δ)));
  - PARI 2.x via cypari2, run locally.
  - No files kept.

## 1. Dictionary item 2 (e₀-character χ₁₄₀ on Γ₀(140)) → CONDITIONAL, on a weaker hypothesis
- **Hypothesis H (standard; cited, not proved here):** the Weil representation of an even-signature discriminant form of level N is trivial on Γ(N), i.e. factors through SL₂(ℤ/N). References: Nobs–Wolfart; Skoruppa; Scheithauer, "The Weil representation of SL₂(ℤ) and some applications".
- **PROVED given H.**
  - The image of Γ₀(140) in SL₂(ℤ/140) is the Borel subgroup B = {(d⁻¹, b; 0, d)}. Every element of B equals T^k·M̄_d, where M_d ∈ Γ₀(140) is any fixed lift with lower-right entry d.
  - ρ(T)e₀ = e₀, since q(0) = 0.
  - Exhaustive check: ρ(M_d)e₀ = χ₁₄₀(d)·e₀ for **all 48** d ∈ (ℤ/140)*, plus 48 second lifts with c ∈ {280, 420, 700} (both 48/48), and ρ(−I)e₀ = ρ(S)²e₀ = χ₁₄₀(−1)e₀.
  - Hence ρ(γ)e₀ = χ₁₄₀(d)e₀ for every γ ∈ Γ₀(140), given H.
  - Control: (1,0;70,1) ∈ Γ₀(70)∖Γ₀(140) does not have e₀ as an eigenvector.
- **Status:** CONDITIONAL on H. The dependence on the general character formula χ_L(d) = ((−1)^{(b⁺−b⁻)/2}|D|/d) (Bruinier, LNM 1780) is removed. This is not an outright proof, because H is cited.

## 2. Dictionary item 4 (W_49^Fricke does not extend Weil(N₂)) — conclusion PROVED, argument replaced
- **PP's trace values, verified locally:**
  - |tr ρ(T)| = 11.8321595662, which equals √140 = 11.8321595662 (Milgram).
  - WTW⁻¹ = (1,0;−49,1) ∈ Γ₀(49): tr ρ = −31.3049517i, so |tr| = 31.3049516850, which equals 14√5 = 31.3049516850.
  - Control: (1,0;−1,1) = S⁻¹T⁻¹S-type conjugate in SL₂(ℤ) gives |tr| = √140, as conjugation invariance requires.
  - **Agreement with PP: exact.**
- **Logic (PROVED).**
  - Suppose some invertible A on V = ℂ¹⁴⁰ and scalars c(γ) satisfied ρ(WγW⁻¹) = c(γ)·Aρ(γ)A⁻¹ for all γ ∈ Γ₀(49). This covers any linear or projective extension of ρ|Γ₀(49) to Γ₀(49)⁺ on V.
  - Then tr ρ(WγW⁻¹) = c(γ)·tr ρ(γ). Both ρ(WγW⁻¹) and ρ(γ) are unitary, and conjugation preserves eigenvalues, so |c(γ)| = 1 and the trace moduli are equal.
  - For γ = T the moduli are √140 ≠ 14√5. Contradiction.
- **Replacement.** XW's descent argument (WγW⁻¹ mod 140 not determined by γ mod 140) is insufficient on its own, as PP notes; this argument replaces it. Supplement from PP (agreed): W₄₉ is not an Atkin–Lehner operator of Γ₀(140), since 49 ∤ 140.

## 3. LD-Ξ3 (twist) → PROVED by computation
Locally computed with PARI:
- 49a1 = [1,−1,0,−2,−1] has conductor 49, root number +1 and j = −3375.
- elltwist(·,−20) and elltwist(·,140) both have **conductor 19600** and **root number −1**. Hence the Fricke eigenvalue of the twisted newform is ε = −w = **+1**.
- elltwist(·,−7) has conductor 49, root number +1, and a_p identical to 49a1's for all p < 200, consistent with f⊗χ_{−7} = f (CM).
- The Atkin–Li citation is no longer needed.

## 4. Dictionary item 7 ("any joint carrier lives at level 980") → OPEN
- **PROVED (kept):** lcm(49,140) = 980 = 2²·5·7² and Γ₀(49) ∩ Γ₀(140) = Γ₀(980).
- **PP-reported, agreed (PROVED by counterexample):** (0,−1;49,0) does not normalize Γ₀(980), since WTW⁻¹ = (1,0;−49,1) ∉ Γ₀(980).
- **OPEN:**
  - "joint carrier" is undefined;
  - whether level 980 is necessary or minimal is not proved;
  - the twist joint object (LD-Ξ3) sits at 19600, not 980.
- XW's sentence was an overclaim.

## 5. PP bonus finding — recorded as PP-reported, and Local-verified
- θ_{L₄₉}² ∈ M₄(Γ₀(49)) is the theta of L₄₉⊕L₄₉ (rank 8, 49-modular).
- Local PARI check: dim E₄ = 8 and dim S₄ = 10 (Sturm bound 10). Solving exactly on 61 coefficients against the Eisenstein ⊕ cusp bases gives residual 0.
- The cusp part is nonzero. Its q-expansion begins (136/35)q + (384/35)q² + (64/5)q³ + (688/35)q⁴ + …, and mfatkin with Q = 49 fixes it exactly (difference 0).
- So θ_{L₄₉}² has a **nonzero cuspidal Fricke +1 component** in S₄(Γ₀(49))⁺. **PROVED** (PP-reported; Local-verified).
- Weight-4 cusp coordinates differ from PP's listed [8/105, 56/15, …] only by choice of basis. Not compared further.

## 6. Timestamp correction
XW's header says "Written ~3:30 PM CST". The actual file mtime is **2026-11-09 15:19:30 CST** (America/Chicago), for both XW and its .sha256 sidecar. The header time was an estimate and is wrong; the mtime is authoritative.

## 7. Updated rollup for XW (ae951f3e)
- **Before:** PROVED 12 · CONDITIONAL 1 · OPEN 3 · REFUTED 1.
- **After:** **PROVED 13 · CONDITIONAL 2 · OPEN 4 · REFUTED 1.**
- **Changes:**
  - Dict 2: PROVED → CONDITIONAL (on H). PROVED −1, CONDITIONAL +1.
  - Dict 4: PROVED, with the argument replaced (trace). No count change.
  - LD-Ξ3: PROVED, basis changed to computation. No count change.
  - Dict 7: split into 7a (lcm / Γ₀(980) intersection), PROVED +1, and 7b (minimal "joint carrier" level), OPEN +1. Item 7 was not counted in XW's rollup.
  - New: θ_{L₄₉}² nonzero cuspidal +1 component, PROVED +1 (PP-reported, Local-verified).
- **Not relabelled:** PP notes the general CM conductor formula is CONDITIONAL (literature). XW's bridge item stays PROVED on the specific data: 49a1 has conductor 49, computed by PARI here, and ℚ(√−7) has discriminant −7. The general formula is used only as context.

No CERT. Tip untouched. 49a1's sign stays −1. B2 and Ξ (weight 3/2) unaffected.
