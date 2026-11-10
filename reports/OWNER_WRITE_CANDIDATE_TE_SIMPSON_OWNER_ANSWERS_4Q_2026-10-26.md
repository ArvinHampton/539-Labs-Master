# OWNER WRITE — T-E Simpson: Owner-APPROVED answers to MR1 four questions (2026-10-26)
Source: Owner voice call-018c4fcf — verbal decision card APPROVED as written (MR1 recommendations).
Authority: Owner spoken approve of Math Research 1 recommended answers (a)–(d).
NO tip fold; nothing here authorizes a fold.
Tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched NO.
Soft SF invent HOLD (tip fill else). Soft SF F3 CLOSED. Bridge PARTIAL READY NO. W-P5a-OP stays open-to-prove; no FAIL retag.

Supersedes HOLD drafts: bc644371… and e757577c… (prior HOLD/NOT OPERATIVE stamps) — this file is now OPERATIVE Owner-approved answers.

Cited:
- FINDINGS_MR1_TE_SIMPSON_SELECTION_RULE_2026-10-26.md sha 97ee90551dfbf9872e3498cd91dfd7ed6365dc8e6c05df24a5f8a3f3c582d2ab
- Live OW OWNER_WRITE_CANDIDATE_TE_SIMPSON_SELECTION_QEXP_2026-10-26.md sha 98f996ae846f051d512f89b0c96f5bea3c173d23f55940f626ae637a09c62784 (N=18; selection LOCKED Simpson)
- Scalar ref tables grok-batches/TE-SIMPSON-QEXP_scalar_G0_49_k4.{py,csv,out} shas d465e8cc… / 1776aa60… / bc098894… (rank 11/18 REF only)
- MR1 recommended answers (a)–(d) as read on voice and Owner-approved

## (a) fill-first meaning — LOCKED (Owner-approved)
**Weight-order fill**, not all-nodes-as-functionals.
On mesh n=0..N with N=18 even: fill slots by descending Simpson composite weight, ascending n within each weight class:
1. w=4 (odd n): 1,3,5,7,9,11,13,15,17
2. w=2 (even interior): 2,4,6,8,10,12,14,16
3. endpoints w=1: n=0, then n=18
"Fill" means: compute / record the Fourier coefficient a_n (per component / isotypic piece) at that index when a basis or spanning set exists; leave OPEN/ABSENT when it does not.

## (b) Stop criterion — LOCKED (Owner-approved)
Stop a piece when either:
1. all 19 mesh slots for that isotypic piece (503 or 89; per component when vector-valued) are filled from a real basis/spanning set, or
2. a rigorous vanishing / identity is proved that makes further slots unnecessary,
whichever comes first.
If the ρ̄ basis is ABSENT: leave COEFFS-OPEN / ABSENT; inventing coefficients is forbidden. Scalar M₄(Γ₀(49)) reference rank 11/18 stays PARTIAL for the missing 7 dims — do not invent fillers.

## (c) ρ̄ Sturm bound — LOCKED provisional (Owner-approved)
Keep **N = B = 18** as provisional **scalar-reference mesh only** (from k·μ/12 = 4·56/12 = 18.67 → n≤18). This is **NOT** a proved ρ̄-Sturm theorem until a component-wise or induced-representation argument is written and Soft SF CONFIRMED. Until then: use N=18 as the computational mesh only; never assert a ρ̄-Sturm theorem from this Write. Live mesh is N=18.

## (d) Fractional-exponent component mapping — LOCKED (Owner-approved)
Map mesh slot n to the coefficient of lattice exponent ν **only when ν = n** on that component’s T-ord support (cite dimcalc T-ord lists N36 [0,1,4,9,14,16,21,25], N6 [1,9,29,81,109,121] as carried, not re-derived).
Otherwise the slot is **vacuous / ABSENT** for that component — do not invent a fill.
n=0 remains vacuous for cusp forms.
No fractional-to-integer interpolation invent.

## Status
Four Owner questions ANSWERED and APPROVED. Tip untouched. No tip invent. Operative for MR1 + Eigen ρ̄ fill once a basis exists.
