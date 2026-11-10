# FINDINGS — PR2 VANISHING LEAD Rank 17 Fix(S_lab⁻²)=0 wall / wrong-parity wall · 2026-10-26 11:12 CDT (America/Chicago)
Authority: Owner voice LOCK via Physicist (rotate after Rank 27). VANISHING_LEAD_ASSIGNMENTS live sha dea4843d5e41ef1b7c131463e50fd0c80fe3aca50ff45b7c2cd1715a94ec66e0 (sibling .sha256 OK).
Integrity: tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (MATCH; tip_touched NO). Catalog v0.5.11 4ed155d55c3a18ca4bc96a6a6eec4c1806abfc2e270f355f1ea58a197119dd04 UNCHANGED.
Soft SF invent HOLD tip fill else. Soft SF F3 CLOSED. No tip fold. Bridge PARTIAL READY NO. Φ stays REJECTED. Cite-only.
Map source MERGED_VANISHING_MAP_STUB_2026-10-26.md sha b3e0d20b… (MATCH), row 17 (L39): "Fix(S_lab⁻²)=0 wall / wrong-parity wall [CI#24; L V5; MR2 V-FIX0-WALL] | any | −2 | wall kills forms | non-occurring (dim Fix=42), Cat B Owner Write | tip L256,L267 | 7cddb188ca34 | R1 relies on ρ̄(−I)=I, not Fix=0".

## Vanishing point
Rank 17 — the literature wall "if Fix(ρ(−I)) = 0 (wrong parity), every form vanishes". On the Written tip this wall is evaluated and does **not** occur.
- Tip L256 (§1u, Cat B Soft SF Owner Write): "dim Fix(S_lab⁻²)|_{V₄₂} = 42 = dim V₄₂ — ρ(−I) = S_lab⁻² acts as Id on V₄₂; the Fix = 0 wall does not occur."
- Tip L265 (§1v PF-1): "every form for (Γ₀(49), ρ) is valued in Fix(S_lab⁻²). By Owner Write `85d6eab3…` … this space is all of V₄₂. **P2′ therefore imposes no constraint on V₄₂ and is not a forcing premise.** … The Fix=0 wall does not occur."
- Tip L267 (§1v PF-2): "**Ruled out:** Fix=0 (A-WALL); proper Fix-cut of V₄₂; W₇ ±1 eigenspace cut; DMZ W₄₉ scalar wall; k≥0 uniqueness/genus walls at the Written k=−2."
- Owner Write OWNER_WRITE_MR1_FIX_DIM_SLAB_INV2_V42 (85d6eab3…, .sha256 OK) L6–7: "ρ(−I) = ρ(S)² = S_lab⁻² acts as the identity: **dim Fix(S_lab⁻²)|_{V₄₂} = dim ker(S_lab⁻² − Id)|_{V₄₂} = 42 = dim V₄₂.**"
- MR1 closure MR1_SOFTSF_FIX_DIM_42_OWNER_WRITE_CLOSED (c31fa0dc…, .sha256 OK) + AUTHOR_NOTE (d89b5e8c…) — fold closed; cited, not re-read for new content.
- CI#24 (CORPUS_VANISHING_INVENTORY L50, fb298346…): "Fix(S_lab⁻²)=0 wall | — | −2 | wall non-occurring (dim Fix = 42) | Written tip (Cat B; Owner Write 85d6eab3…) | tip L256, L267".
- MR2 V-FIX0-WALL (MR2-FINDINGS-CORPUS-VANISHING-MAP L16, b271f42a…): "Lit wall RULED-OUT-BY-DIM here … Absence of Fix subspace would kill all forms; **absent here** (Fix=V₄₂) | Supports that R1 needs ρ̄(−I)=I not Fix=0".
- Local V5: not located as a separate file in reports/ (cited only via stub tag); MR1 reverse-all V4 (8173e7b3…, L28) carries the same content: "ρ(−I) = S_lab⁻² = **I on V₄₂** (even central character) | numeric / proposed".

## Backwards inference — does the wall apply?
Disposition: **NON-OCCURRING confirmed** (wall does not apply; ABSENT as a live vanishing obstacle).
Fix(S_lab⁻²) = V₄₂ (dim 42), Cat B Owner Write, folded at tip L256 and ruled out at L267. No form is killed by this wall at k = −2 or at any κ of correct parity.

### R1 relies on ρ̄(−I) ≈ I, not Fix = 0
MR1 reverse-all §R1 (L58–60): "ρ̄(−I) = ρ̄(S)² = **I on V₄₂** (central character trivial / even). Odd κ ⇒ slash-central mismatch ⇒ S_κ(Γ₀(49), ρ̄) = {0} **vacuously**." Numeric: reverse-dimcalc .out "ρ̄(−I)−I resid ~1.8e-15". So R1's odd-κ kill uses the *same* fact that makes the Rank-17 wall non-occurring (ρ̄(−I)=I ⇒ Fix=V₄₂); it is a parity/central-character kill at odd κ, not a Fix=0 kill. At even κ (incl. operative κ=4) neither R1 nor this wall removes anything. Status of the ρ̄(−I)=I numeric: proposed (V4); the Fix dim on V₄₂ is Cat B Owner Write.

## Contrast — not to conflate
| Object | Statement | Status | Effect |
|---|---|---|---|
| **Rank 17** Fix(S_lab⁻²) = Fix(ρ(−I)) on V₄₂ | = V₄₂, dim 42 | Cat B Owner Write (tip L256/L267) | wall NON-OCCURRING; P2′ no constraint |
| **Rank 1 (Eigen)** Fix_{Γ₀(49)}(V₄₂) (full group invariants) | = {0} | numeric/proposed (min sv 3.67; stub L23) | no constant-vector witness ⇒ M₀ = 0 nonvacuous (feeds R2) |
| **T-B** (OWNER_WRITE_TB_KAPPA_LEQ0_FIX0, 0f85468b…, .sha256 OK) | "M₀(Γ₀(49), ρ̄) = {0}, and M_κ = {0} for every κ < 0 … Fix_{Γ₀(49)}(V₄₂) = {0} (proposed numeric …)" | Owner LOCKED, **to prove**, route change; "Fix=0 remains a proposed numeric, not proved"; "Does not change operative k=−2, κ=4" | uses Rank-1 Fix_{Γ₀(49)}=0, not Fix(S_lab⁻²) |
The "Fix0" in T-B's name is Fix_{Γ₀(49)} = 0 (Rank 1). Rank 17's Fix is the fixed space of the single central element −I, which is all of V₄₂. Both hold together without contradiction: −I acts trivially, but the full group has no common fixed vector. T-B contrast also in grok-batches/LOCAL-VANISHING-LEAD-T-B-RANK6 (d3c9a43b…), cited, not re-derived.

## What is NOT claimed
No new dimension, matrix or eigenvalue. No claim about ρ(−I) outside V₄₂ (Soft SF F3 CLOSED). No promotion of Rank 1 / T-B Fix_{Γ₀(49)}=0 beyond proposed numeric. P5a κ=4 cusp vanishing and `[[ components — Arvin ]]` stay open (tip PF-2 "Open / ABSENT"). NOT Cat A. Bridge PARTIAL; READY NO.

## Paths checked
MERGED_VANISHING_MAP_STUB (b3e0d20b…); VANISHING_LEAD_ASSIGNMENTS (dea4843d…); residual-c-field-WRITTEN_PREMISES_DRAFT.md L245–275 (7cddb188…, read-only); OWNER_WRITE_MR1_FIX_DIM_SLAB_INV2_V42 (85d6eab3…); OWNER_WRITE_MR1_FIX_DEDUCE_PF1_PF2 (e990cb37…); MR1_SOFTSF_FIX_DIM_42_OWNER_WRITE_CLOSED (+AUTHOR_NOTE); OWNER_WRITE_TB_KAPPA_LEQ0_FIX0 (0f85468b…); CORPUS_VANISHING_INVENTORY (fb298346…); MR2-FINDINGS-CORPUS-VANISHING-MAP (b271f42a…); MR1-AUTHOR-REVERSE-ENGINEER-ALL-VANISHINGS AMEND-2 (8173e7b3…); LOCAL-VANISHING-LEAD-T-B-RANK6 (d3c9a43b…).
