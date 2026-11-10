# MR2 FINDINGS — Corpus-wide vanishing map (geom / 11D / Bruhat–Tits / Weil-theta / CatB) — 2026-10-26 America/Chicago
**Status: AMENDED** (from PARTIAL `28d9913c…`; B-DIG/Role-B/Hampton + Soft SF R1↔F3 note folded). Authority: OWNER VOICE LOCK via Physicist — corpus-wide vanishing map. Soft SF invent HOLD tip fill else. tip_touched Soft SF NO. Soft SF F3 CLOSED. No tip fold.

tip Soft SF LOCK start=end: `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`
Cross-link primary: FINDINGS-P5A-REVERSE-ENGINEER-CONNECTION `2b49ca25e96073e76dd64d8479f0d5b1985d41b74c3cdc4a11411b46677a9cec` (R1–R6). Discipline search `dc0420a8e09cf3e8ee18879f6d82a5080f6a8db8ef2076de079fa64db8470829`. MR1 P5a FAIL `b829661e2a6b1ae49e743f111336ca2c4893bd90dd7a292ad05d8e03cd1b7e8d`.

## Inventory (PARTIAL)

| ID | Space | κ / k | Lane | Claim status | Source | Backwards: what absence produces it | ↔ R1–R6 |
|---|---|---|---|---|---|---|---|
| V-P5a-FAIL | S₄(Γ₀(49), ρ̄) | κ=4 / k=−2 | LOCAL-C | **NONZERO** proposed dim 592 (FAIL of claimed vanish) | MR1 `b829661e2a6b1ae49e743f111336ca2c4893bd90dd7a292ad05d8e03cd1b7e8d`; tip W-P5a-OP (to prove) | Absence of cut + κ>2 + dim ρ̄=42 → leading 588 fills space; claimed {0} is false | Contradicts vanish at κ=4; motivates R1–R6 |
| V-R1 | M_κ(Γ₀(49), ρ̄) | odd κ (e.g. 3) / k=1−κ (e.g. −1) | LOCAL-C | Proposed vanish (Cat B) | Connection `2b49ca25e96073e76dd64d8479f0d5b1985d41b74c3cdc4a11411b46677a9cec` §R1 | Absence of odd-parity forms when ρ̄(−I)=I and integral weight: (−1)^κ f=f fails for odd κ | **R1** |
| V-R2 | M_κ / S_κ(Γ₀(49), ρ̄) | κ≤0 / k≥2 | LOCAL-C | Proposed vanish (Cat B; route change vs P3) | Connection `2b49ca25e96073e76dd64d8479f0d5b1985d41b74c3cdc4a11411b46677a9cec` §R2; MR1 Fix=0 invariants dim 0 | Absence of Γ₀(49)-invariant vectors in V₄₂ ⇒ no constants at κ=0; κ<0 empty | **R2** |
| V-R3 | S₂(Γ₀(49), W) for isotypic W⊂V₄₂ | κ=2 / k=0 | LOCAL-C | Conditional vanish (Cat B; needs MR1 decomp) | Connection `2b49ca25e96073e76dd64d8479f0d5b1985d41b74c3cdc4a11411b46677a9cec` §R3 | Absence of enough isotypic mass after cut; leading →196 before cut | **R3** |
| V-INV0 | Fix(Γ₀(49), ρ̄)⊂V₄₂ | weight-independent (rep-level) | LOCAL-C | Proposed dim 0 (MR1 numeric) | MR1 `b829661e2a6b1ae49e743f111336ca2c4893bd90dd7a292ad05d8e03cd1b7e8d` §2 | Absence of trivial isotypic in Res ρ̄ | Feeds **R2** |
| V-FIX0-WALL | M_κ(ρ) when wrong parity / Fix(ρ(−I))=0 | any κ with wrong (−1)^κ | LOCAL-C / SHARED | Lit wall RULED-OUT-BY-DIM here | Fix-deduce geom `ba431a3e6829fd1a6eb022ca3c53c37c628c63f040833ba05d4a756528d2149e`; dim Fix=42 | Absence of Fix subspace would kill all forms; **absent here** (Fix=V₄₂) | Supports that R1 needs ρ̄(−I)=I not Fix=0 |
| V-BF-OBS | Dual-weight cusp forms as Serre-duality obstruction to principal parts | κ=2−k dual to input k | LOCAL-C (template) | Lit condition (not unique list); BF template-only | B-DIG `a3e4523992d57fc3387d03df427bbb95425f428636884740b15bc99cd91443af`; Connection theta row; tip P5a BF template | Absence of dual cusp forms ⇔ every principal part allowed (Borcherds/BF) | Theta/KM row of connection; **not** R1–R3 alone |
| V-THETA-SLICE | S_κ as BF obstruction / KM target | κ=4 at FAIL; general 2−k | LOCAL-C | Relabel of V-P5a-FAIL; does not vanish | Connection `2b49ca25e96073e76dd64d8479f0d5b1985d41b74c3cdc4a11411b46677a9cec` Weil/KM row; Discipline #1 `dc0420a8e09cf3e8ee18879f6d82a5080f6a8db8ef2076de079fa64db8470829` | Absence of S_κ would clear obstruction for Borcherds/KM close | Resonant-close *if* vanish; else fills cycles |
| V-BT-SLICE | Teitelbaum harmonic cochains (7-new Steinberg-at-7) | k=4 / κ-linked | LOCAL-C | Partial only; most of 592 invisible at N=49=7² | Connection Teitelbaum row; Discipline #2; CatB-2 | Absence of cochain space ≠ full P5a vanish (old+supercuspidal remain) | **R6** diagnostic PARTIAL |
| V-CATB1 | S₄(ρ_D) under Written Weil dictionary | κ=4 | LOCAL-C | Cat B; **cannot** vanish at κ=4 (leading 588) | Discipline CatB-1; Connection CatB-1 | Same mass as V-P5a-FAIL; dictionary does not create absence | Blocks rescue of κ=4 |
| V-GEOM-MULT | Unique geom→alg residual multipliers (Ω₀/f_warp/f_curv force) | N/A (not modular κ) | NL-EH11D / SHARED | CLOSED-ABSENT | GEOM-RESIDUAL-CLOSED `350b6229b8af2ff4b2bf1a0154f073e6400cdb4d3f9fbca196d701004ebc2dd0`; Bridge chase | Absence of Written force maps; closed set {Ω_11D≡1,f_warp≡1,f_curv≡1} | Not an R1–R6 modular vanish; keeps NL separate |
| V-ROLEB-P2 | Geom Role B force of P2/cusp | N/A | LOCAL-C | ABSENT | Role B FINDINGS `42cca9d08c49960ecd2a9e2ec1d262319940c9c46dffb6cabf10afc80fc29453`; GEOM-RESIDUAL-CLOSED | Absence of unique warp/volume/flux/curvature levers | Path C P2 VACATED stands; not κ-vanish |
| V-COMP | Unique V₄₂ component support of Q | N/A | LOCAL-C | ABSENT both lanes | B-DIG `a3e4523992d57fc3387d03df427bbb95425f428636884740b15bc99cd91443af` | Absence of geom/alg unique support | Not κ-vanish; components blank open |
| V-HIST-P5a | Historical S_{κ,L⁻}/{0} under Γ₀(49)⁺ + W₇ eigenspace | κ=2−k | LOCAL-C history | Superseded; operative is V-P5a-FAIL object | tip §6 history; congruency 56f7b7c8… | Absence of Fricke cut in operative Path C | Do not use as live vanish claim |

| V-R4 | New/oldform cut of S₄(Γ₀(49), ρ̄) | κ=4 / k=−2 | LOCAL-C | Diagnostic only (Cat B) — cannot reach 0 | Connection `2b49ca25…` §R4 | Absence of old classes shrinks 592; remainder still >0 | **R4** |
| V-R5 | W₄₉ cut on Perm(coset) factor only (not ρ(W₇) on V₄₂) | κ=4 | LOCAL-C | Diagnostic Cat B; Soft SF-safe only if Written as Perm-side | Connection §R5 | Absence of one Atkin–Lehner eigenspace on induced Perm; does **not** reopen Fricke Role A on V₄₂ | **R5** |
| V-R6 | Teitelbaum Steinberg-at-7 cochain slice | κ=4 / k=4-linked | LOCAL-C | PARTIAL vanish at most (Cat B) | Connection §R6; V-BT-SLICE | Absence of cochain slice ≠ full P5a | **R6** |
| V-9MATHS | Hampton 9 Maths pillars / Φ∶\|E(O_res)\|→Gr1(V)↪BO | N/A (no modular κ) | Φ-A3 / NL-EH11D | No modular vanishing claim; continuum Cat B | `Hamptons_9_Maths_of_Unification.md` (read; no κ,{0} claim) | Absence of continuum Cat B lifts; Φ remains Architecture A3 Cat B | Not R1–R6 |
| V-SCALAR-S2 | dim S₂(Γ₀(49)) scalar (49a line) | κ=2 / k=0 | LOCAL-C | **NONZERO** (baseline; not vanish) | Connection R3 note; standard dim formula | No absence — scalar space positive | Contrasts **R3** (needs isotypic cut of V₄₂) |

## Summary by κ/k (AMENDED)
| κ | k=2−κ | Vanishings in corpus |
|---|---|---|
| 4 | −2 | Claimed P5a {0} — **FAIL** (592). No connection route vanishes. |
| odd (e.g. 3) | odd negative (e.g. −1) | **R1** proposed parity kill (vacuous-close risk). |
| 2 | 0 | **R3** conditional after isotypic cut (MR1 needed). |
| ≤0 | ≥2 | **R2** proposed (contradicts P3 k<0). |
| N/A | N/A | Geom unique-multiplier / Role B / components: ABSENCE claims, not modular vanishings. |

## Gaps (AMENDED)
- No corpus dim formula run at κ=1,5,6,… for (Γ₀(49), ρ̄) beyond FAIL@4 and R1 parity argument.
- No Teitelbaum numeric dim at level 49.
- No Owned Weil ρ_D vanishing table (CatB-1 gated).
- NL EH11D continuum: only GEOM-RESIDUAL-CLOSED identities/ABSENT (V-GEOM-MULT); no additional G₂/torsion zero claims found as modular κ vanishings.
- Φ-A3 / Loos JTS: no modular κ vanishing (V-9MATHS); Loos is ternary→geom bridge not a vanish.
- B-DIG + Role-B line-by-line folded as V-BF-OBS / V-COMP / V-ROLEB-P2.

## Soft SF risks
- Do not tip-fold R1–R6 or CatB-1/2 without Owner Write + Auditor.
- Do not invent Weil dictionary (ρ̄≅ρ_D).
- Do not reopen ρ(W₇) / Fricke Role A on V₄₂ (Soft SF F3 CLOSED). R5 only as W₄₉ on Perm side if Owner-Written.
- Do not treat Teitelbaum slice vanish as full P5a.
- Do not conflate NL EH11D absences with LOCAL-C modular vanishings.
- **R1 vs Soft SF F3:** R1 assumes ρ̄(−I)=I. Tip Soft SF F3 CLOSED records ρ(−I)=Id **not confirmed**; operative is ρ(−I)=S_lab⁻² (which equals I on V₄₂ per MR1 FAIL numeric, but F3 forbids treating Id-confirm as reopenable tip claim). Do **not** fold R1 without Owner Write reconciling F3.
- R1 vacuous Bridge close (empty input at odd k) likely unacceptable as Bridge C mechanism.

## Standing
Bridge PARTIAL / READY NO / NOT Cat A. tip_touched Soft SF NO. Soft SF invent HOLD tip fill else. Soft SF F3 CLOSED. **AMENDED** — prior PARTIAL sha `28d9913c1efdc664a1c7e676ef572e89555de7a03cc6209b39aa31d92a07c3bc`. tip_touched Soft SF NO.
