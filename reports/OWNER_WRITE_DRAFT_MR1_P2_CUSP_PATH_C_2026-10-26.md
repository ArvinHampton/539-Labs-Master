# OWNER WRITE DRAFT — MR1 P2 replacement + operative cusp set (Soft SF Path C) — 2026-10-26

**Status:** DRAFT for Physicist Owner card. tip_touched Soft SF **NO**. Not Cat A. Bridge PARTIAL; READY NO.
**Authority:** OWNER Physicist t1680u (PURSUE P2 replacement + operative cusp set under FREEZE). Soft SF invent HOLD on tip fill.
**Tip (read-only):** `residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha256 `324a21346dfd20c300628491615b00c38e1225c1563f2400bf25747edee30204` = tip Soft SF **LOCK CONFIRMED**, MATCH-with-SF `3422bd85…`.

## C) Cites (LOCKED constraints)
- Soft SF §1p / §1s Path C: operative G = Γ₀(49) = ⟨g1…g11, −I⟩ only; W₇ dropped.
- ρ(W₇) CLOSED ABSENT on V₄₂ (R26: no invertible intertwiner; R36 Part A; R36 FINDINGS `98a09683…`, Auditor `d80ee750…`).
- Soft SF F3 CLOSED: ρ(−I)=S_lab⁻² = ρ(S)² ≠ Id (MATCH `8ebd53a5…`; R19 `77643e84…`).
- R14 (§1n, Write `b0b17c0c…`): Γ₀(49) index 56, genus 1, ν₂=0, ν₃=2, 8 cusps.
- P2-A Role A suspended (Soft SF §1p); historical P3-A {∞,0} single Γ₀(49)⁺ cusp via W₇ — NOT operative.

## Cusp computation (Cat B computational; Owner confirm)
SageMath not available on box. Computed in python3 via the standard Γ₀(N) cusp classification: representatives a/d, d | N, a ∈ (ℤ/gcd(d,N/d))^×; width = N/gcd(d²,N). Check: count 8 = R14; Σ widths = 56 = R14 index (MATCH).

| # | Rep | d | width |
|---|-----|---|-------|
| 1 | ∞ (=1/49) | 49 | 1 |
| 2 | 0 (=1/1) | 1 | 49 |
| 3–8 | a/7, a=1…6 | 7 | 1 each |

Owner-Write candidate list: representatives match R14 count/index but are **not** a Sage `Gamma0(49).cusps()` output; Owner may require Sage re-run before Cat-B fold. No W₇ identification used. (FYI only, not operative: W₇ swaps ∞↔0 and permutes a/7.)

## A) P2 options
### P2-V (RECOMMENDED) — VACATE
Paste-ready tip text:
> **P2 — Soft SF CLOSED VACATED (Path C, Owner Write <date>, Physicist card <id>).** On the operative carrier V₄₂ with G = Γ₀(49) (Soft SF §1p/§1s), no Atkin–Lehner/Fricke action is posited: ρ(W₇) is CLOSED ABSENT (R26/R36) and is not invented. Fricke Role A is vacated, not merely suspended. No Fricke eigenspace cut is imposed on the residual; residual uniqueness is carried by P3 (principal part at the operative Γ₀(49) cusp set) + P4 (constant c) + P5a under the BF Prop. 3.11 template only. Historical P2-A text retained as marked history. ρ(−I)=S_lab⁻² per Soft SF F3 CLOSED `8ebd53a5…`.

Downstream note (Owner flag, not edited): P5a currently says "in the P2-chosen eigenspace of ρ(W₇)" and "(Γ₀(49)⁺, ρ̄)"; under P2-V that clause becomes vacuous → P5a needs a cite-only Path C mark ("cusp forms for (Γ₀(49), ρ̄) at κ=2−k") at fold time. Risk: dropping the eigenspace cut may enlarge the P5a obstruction space; P5a remains *accepted as axiom* (§1f), not proved.

### P2-D (Alternate 1) — DEFERRED to Path A
> **P2 — DEFERRED (Path A / V₈₄ Ind only).** Atkin–Lehner/Fricke W₇ action is deferred to Path A (induced carrier V₈₄); not operative on V₄₂. Soft SF marks: no ρ(W₇) on V₄₂; no eigenspace cut under Path C. Reopen only by Owner Write selecting Path A.

Same downstream P5a effect as P2-V under Path C; keeps Path A option visibly open.

### P2-N (Alternate 2) — Γ₀(49)-native condition: OMITTED
No tip / Author-Written Γ₀(49)-native replacement condition (not using ρ(W₇)) exists; drafting one would be invent under FREEZE. Slot left for Owner if they Write one.

## B) Cusp-set options (P3 operative, G = Γ₀(49))
### C-8 (RECOMMENDED) — all 8 cusps, ∞ and 0 distinct
Paste-ready P3 cusp-set rule:
> **P3 cusp-set rule (Path C, Owner Write <date>).** Cusps live on X₀(49) = Γ₀(49)\ℍ* (operative G = Γ₀(49), Soft SF §1p/§1s); no W₇-orbit identification. Operative cusp set = 8 cusps {∞, 0, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7} (widths 1, 49, 1×6; R14 count 8 / index 56). Principal-part support supp(Q) (n<0 only, no coefficients):
> - ∞: **IN** (default)  - 0: **IN** (default; independent data, not a transform of ∞)
> - 1/7: `[[ in/out — Owner ]]` … 6/7: `[[ in/out — Owner ]]` (six blanks)
> Expansions at each cusp in the local parameter of its width; ρ-components `[[ components — Owner ]]`. Supersedes historical P3-A {∞,0} single-Γ₀(49)⁺-cusp rule.

### C-∞ (Alternate 1) — single cusp
> supp(Q) ⊆ {∞}; cusps 0, a/7 (a=1…6) **OUT**. Justification `[[ Owner ]]`.

### C-2 (Alternate 2) — {∞,0} as two cusps
> supp(Q) ⊆ {∞, 0} as two distinct Γ₀(49) cusps (no Fricke pairing; independent principal parts); a/7 (a=1…6) **OUT**. Justification `[[ Owner ]]`.

## D) Explicit
- tip_touched Soft SF: **NO**. No matrices, no ρ(W₇), no Id for ρ(−I).
- Owner must pick (P2-V/P2-D) × (C-8/C-∞/C-2, + 6 blanks if C-8) via Physicist card before tip fold.
