# AUDITOR CONFIRM — MR1 Owner Write: N₂ carrier realisation (t1131u) — 2026-10-25 (America/Chicago, ~20:30 CDT)

**Verdict: MATCH-with-SF**
Bridge: PARTIAL / READY: NO. Tip: LOCK (not edited, not folded).

## Hashes (all recomputed by Auditor)
| Item | Path | sha256 | Status |
|---|---|---|---|
| Owner Write | quantum-comp/reports/OWNER_WRITE_MR1_N2_CARRIER_t1131u_2026-10-25.md | e5da6bfa32cc817e2a996c02258d90202a68eb8355619482c0958a24bc633c5e | MATCH expected |
| Source FINDINGS | grok-batches/MR1-AUTHOR-PURSUE-N2-W7-GENS_2026-10-25.md | 94f99e2ebb65c33713563675d84d7232dcac89bae7aac2d3dd77e98eb1422daa | MATCH expected |
| RTA v12 | quantum-comp/reports/self-audit/zenodo/RTA_v12.txt | f837aa377f0d57d1822d5d3243509f4a4a8c77a3aeaec7bf55e885de12303bcb | MATCH expected |
| residual-C tip | residual-c-field-WRITTEN_PREMISES_DRAFT.md | 492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa | before = after; UNTOUCHED |

## W-N2-1 vs RTA (line refs are in RTA_v12.txt)
| Claim in W-N2-1 | RTA ref | Result |
|---|---|---|
| N₂ Gram [[2,14],[14,28]], det −140 | l.5032 "N2 := {x ∈ Z : x2 ≡ 0 mod 2}, Gram … det = −140" | PASS |
| Even, signature (1,1); ≅⟨2⟩⊕⟨−70⟩ | l.5039–5043 Prop 26.1(i) | PASS |
| A_N₂ ≅ Z/2×Z/70, |A|=140, q=x²/4−y²/140 | l.5046 Prop 26.1(ii) | PASS |
| ρ_lab ≅ ρ_N₂ on SL₂(Z); no twist, no metaplectic sign | l.5095–5096 Thm 26.2(i); l.5157–5158 Rem 26.4 | PASS |
| V = Fix(N)∩Fix(γ) = A₃⊗X⁺ ⊕ B₁⊗X⁻, dim 36+6=42 | l.3796–3798 Prop 19.4(ii); l.2651 | PASS |
| ρ(S)=S_lab^{−1}, ρ(T)=T_lab (Borcherds) | Thm 11.6 (l.~2632–2655, as quoted in source); Thm 26.2 | PASS |
| Weil T/S closed forms (140-dim) | Borcherds formula on Prop 26.1 data, sign 0 | PASS (derived, no invented numbers) |
| ρ|_{Γ₀(49)} := restriction to Γ₀(49) ⊂ SL₂(Z) | Not in RTA (no level-49 content) | PASS as a restriction premise; see SF-1 |
| No 42×42 matrices claimed | — | PASS (stated ABSENT) |

## Explicit Z₇ ↔ W₇ check — PASS (no identification)
- The Write says "Do not identify local reflection Z₇|_V with Fricke W₇. No ρ(W₇):=Z₇ premise" and puts ρ(W₇):=Z₇|_V under W-N2-2 "NOT Written … rejected for this stamp". The W-N2-1 bullet has no W₇ text.
- The source FINDINGS proposes ρ(W₇):=Z₇|_V only as a **Category B candidate needing a stamp**, and flags it "unproved" (Z₇ commutes with SL₂(Z); Fricke-49 does not normalise SL₂(Z)). It does not assert the identification. That matches RTA l.3822: "Category B. Calling Z5, Z7, Z2 the Atkin–Lehner operators … (not checked on the forms)."
- The Owner stamp t31s3 (relayed) excludes the candidate, and the Write follows that.

## Write ↔ source consistency — PASS
The W-N2-1 text is verbatim the first bullet of the source "Proposed Write". The second (W₇) bullet was dropped, as the stamp requires. The Weil formulas, ABSENT list, ρ₃₅≠V₄₂ and no-Bridge-YES statements are consistent across both files.

## Soft SF
- **SF-1 (label scope):** W-N2-1 is tagged "Category A, RTA §26/Thm 26.2/Prop 19.4". However, the Γ₀(49) restriction clause is not RTA content: RTA has no level-49 data. It is a trivial restriction because Γ₀(49) ⊂ SL₂(Z), and it is valid. Recommendation: at fold, mark the Γ₀(49) restriction as an Owner-Written premise, and keep Category A for the N₂/Weil/V content.
- **SF-2 (relayed authority):** Owner stamp t31s3 is cited by MR1/Physicist. The Auditor did not see it directly.
- **SF-3 (open, carried):** the k=−2 vs weight-0 carrier, the Γ₀(49) generators, a W₇ rule, and a 42-basis are all still ABSENT. The Write states this correctly.
- No hard SF: no Z₇↔W₇ identification found.

## Status flags
Tip LOCK 492fb3ac… untouched. Auditor did NOT fold. Fold W-N2-1 → tip §2 P1 [[ ρ ]] only via a later stamped fold + CONFIRM. Bridge PARTIAL / READY NO. No outbound messages.
