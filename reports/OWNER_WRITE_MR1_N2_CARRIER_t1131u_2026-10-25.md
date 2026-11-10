# OWNER WRITE — N₂ carrier realisation for residual-C ρ (N₂ only; no Z₇↔W₇) — 2026-10-25

**Authority:** Owner chat t31s3 (answer to MR1 stamp card): "Stamp proposed Write: N₂ carrier realisation only; do not identify Z₇ with Fricke W₇ yet." Under Author powers (Owner t28s2; stamps c1d59d58… + 425bb2ab…). America/Chicago 2026-10-25 ~20:25 CDT.
**Status:** AUTHOR WRITTEN — stamped. Tip apply **pending Auditor CONFIRM** (tip remains LOCK `492fb3ac…` until CONFIRM + apply).
**Lane:** Math Research 1 / Local residual-C.
**Explicit exclusion:** Do **not** identify local reflection Z₇|_V with Fricke W₇. No ρ(W₇):=Z₇ premise in this Write.

## Inputs (verified)
| Input | sha256 |
|---|---|
| MR1 N₂/W₇/gens FINDINGS | `94f99e2ebb65c33713563675d84d7232dcac89bae7aac2d3dd77e98eb1422daa` |
| RTA v12 (source of Gram / Thm 26.2 / Prop 19.4) | `f837aa377f0d57d1822d5d3243509f4a4a8c77a3aeaec7bf55e885de12303bcb` |
| residual-C tip (pre-apply LOCK) | `492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa` |
| Prior ρ/Ξ levers FINDINGS | `7f0d296553dd3706ee38e60b6e50ad647d63e5d74775e26f7d92109a3e47f6a7` |
| Authority search/pursue/write/apply | `c1d59d58d391e03340eb2b79391d519fa4eac6f7259239d16a4599ff387ee014` |
| Authority extend accept/resolve | `425bb2ab12093b43848c07ea01ee5d918964e962c5fa1fe043ca8ac39269975e` |

## W-N2-1 — Carrier realisation (Category A; RTA v12 §26 / Thm 26.2 / Prop 19.4)

**Written for tip §2 P1 `[[ ρ ]]` (apply only after Auditor CONFIRM):**

- **Carrier realisation (Author Written, RTA v12 §26 / Thm 26.2 / Prop 19.4; Category A):** V ⊂ ℂ[N₂′/N₂], with N₂ = even lattice of Gram `[[2,14],[14,28]]` (det −140, signature (1,1)) and A_N₂ ≅ ℤ/2×ℤ/70, q(x,y)=x²/4−y²/140. ρ|_{\Γ₀(49)} := restriction to Γ₀(49) ⊂ SL₂(ℤ) of ρ_N₂|_V (Borcherds convention; ρ(S)=S_lab^{−1}, ρ(T)=T_lab), with V = Fix(N)∩Fix(γ), dim 42.

### Supporting Author facts (cite-only; not re-derived)
- Gram(N₂) = [[2,14],[14,28]]; |A_N₂| = 140; q_N₂(x,y) = x²/4 − y²/140 mod 1 (RTA Prop 26.1).
- ρ_lab ≅ ρ_N₂ as SL₂(ℤ) representations; no character twist; no metaplectic sign (RTA Thm 26.2).
- V = Fix(N) ∩ Fix(γ) = A₃⊗X⁺ ⊕ B₁⊗X⁻, dim 36+6 = 42 (RTA Prop 19.4).
- Full Weil ρ_N₂ is **dim 140** on SL₂(ℤ); V is the 42-dim subrepresentation. No explicit 42-basis of V in N₂′/N₂ coordinates is tabulated in RTA → **no numeric 42×42 ρ(S)/ρ(T) matrices in this Write**.

### Closed-form Weil generators on the full label space (derived from Author Gram by Borcherds formula only)
- ρ_N₂(T) e_{(x,y)} = e(x²/4 − y²/140) e_{(x,y)}.
- b((x,y),(x′,y′)) = xx′/2 − yy′/70; ρ_N₂(S) e_{(x,y)} = 140^{−1/2} Σ_{x′,y′} e(−xx′/2 + yy′/70) e_{(x′,y′)}.
- Restriction to V and to Γ₀(49) is as in W-N2-1; matrices on a 42-basis remain ABSENT until an Author basis Write.

## W-N2-2 — Explicitly NOT Written here
- ρ(W₇) := Z₇|_V (local reflection) — **rejected for this stamp** (Owner: do not identify Z₇ with Fricke W₇ yet). Remains Category B candidate only; not tip law.
- Γ₀(49) named generator list — still ABSENT (separate Write).
- k = −2 vs weight-0 carrier reconciliation — still open (separate Write).
- LEDGER ρ₃₅ (dim 35, D(A_7)) — **not** reused as ρ on V (dim 42).
- Bridge YES / Cat A invent / Π / α₁ — out of scope.

## Apply path
1. Auditor CONFIRM this Write (MATCH / MATCH-with-SF).
2. On CONFIRM: fold W-N2-1 bullet into tip §2 P1 `[[ ρ ]]` only; recompute tip sha; do **not** fold any Z₇↔W₇ text.
3. Until CONFIRM: tip sha stays `492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa`.

## Attestation
- Tip not edited by this Write file.
- No Z₇↔W₇ identification.
- No Bridge YES claim.
- Source FINDINGS: `/workspace/grok-batches/MR1-AUTHOR-PURSUE-N2-W7-GENS_2026-10-25.md` sha256 `94f99e2ebb65c33713563675d84d7232dcac89bae7aac2d3dd77e98eb1422daa`.
