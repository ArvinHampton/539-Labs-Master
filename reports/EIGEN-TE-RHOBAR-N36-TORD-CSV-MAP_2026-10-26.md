# Eigen Written map — N36 T-ord ↔ RHOS CSV /140 columns (2026-10-26)

**STATUS: MATCH (map Write) — N36 cells map to ABSENT in RHOS 89-CSV.**

Cite-only. invent HOLD. No Fourier coefficients invented. No false identification of N36 lattice exponents with N6 seed-spectrum CSV columns.

## Authority (sha256 verified at Write)
- CLOSED_A `3242e26ef3b79795d89953593ce7b6676e119f8a2e8d6a324da8ae1fe741042a` — OWNER_WRITE_CARD_MR1_N36_TORD_CSV_MAP_CLOSED_A_2026-10-26.md
- ASSIGN Eigen map `c471c8326e77186f8e1089d9e62d77a3fde7dc1ef0e1502dc9b39cc82bf4b442` — ASSIGN_EIGEN_N36_TORD_CSV_MAP_WRITE_2026-10-26.md
- Open card `a497b261f52df6484bd3351881a037e1a901e275d55f5b6000291cfdc4525f24`
- Source MR1 PARTIAL `3dce9e1f6a2d69e249c2bf5cd79e988150b729cf4d02e71be89ca3e5d3e13656`
- RHOS MATCH (mod p) `a8788e5c63c9f84d6bed66c808db5831ab751d9d0d930b8603fa7e25fedf2efd`
- 4Q OPERATIVE `11f104c7361970a2dc02b3f6300071a20d32cad76f0055a616ebded1974ebff2` §(d)
- reverse-dimcalc .out `e2b260385fe0b4ce55e04ba364b74163cb3c66d1c4e42fa97696c774e59473e9`
- CSV `3fb6519f0bef8db0af9e85f614b9139912a3174c750b34ed7765aa1aa9fcb749` (`eigen-q89-basis/rhos/q89_basis_q18_modp.csv`)
- Tip Soft SF LOCK start = end = `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`. **tip_touched NO**

## 1. Written isotypic pieces (reverse-dimcalc, carried)
| label | ρ̄-piece dim | T-ord support (exponents of T̄ /140) | k=4 S-dim |
|---|---|---|---|
| **N36** | 36 | `{0,1,4,9,14,16,21,25}` | **503** |
| **N6** | 6 | `{1,9,29,81,109,121}` | **89** |

Ambient: 503+89=592 (Card1B / reverse-dimcalc). Names N36 / N6 are the dim-36 / dim-6 representation pieces, not level labels.

## 2. What the RHOS CSV columns are (cite RHOS FINDINGS + export header)
- Path: `eigen-q89-basis/rhos/q89_basis_q18_modp.csv` (89 rows × 6048 cols).
- Column schema (export.sage / CSV header): `a{i}_c{j}_e{frac}` where
  - **seed component** `a0..a5` ↔ T-exponents `{1,9,29,81,109,121}/140` (exact N6 spectrum; RHOS §1–2),
  - **cusp rep** `c0..c7` = the 8 Γ₀(49) cusp T-cycle representatives used in the holomorphy solve,
  - **exponent** = seed offset + Ind truncation index (denominators /140 on width-1 reps; /980 on the width-49 rep).
- The CSV is the **truncated image of the 89-dimensional N6-piece** M₄(ρ̄|cusp6 ⊗ Ind) only. It is **not** a basis for the 503-dimensional N36-piece.

## 3. 4Q §(d) rule (OPERATIVE, Owner-approved)
Map mesh slot n to the coefficient of lattice exponent ν **only when ν = n on that component’s T-ord support**. Otherwise the slot is vacuous / ABSENT for that component — do not invent a fill. n=0 remains vacuous for cusp forms. No fractional-to-integer interpolation invent.

## 4. The Written map (N36 ν → CSV column)

| N36 ν | on N36 T-ord? | equal to some N6 seed exp? | RHOS CSV column under 4Q§(d)? | map status for MR1 fill |
|---|---|---|---|---|
| 0 | yes | no | none (cusp-form n=0) | **VACUOUS** (already; 4Q§d) |
| 1 | yes | yes (N6 also has 1) | **none for N36** — `a0_c*_e1/140` is the **N6** coefficient, wrong isotypic piece | **ABSENT-WRONG-PIECE** |
| 4 | yes | no | none (4 ∉ N6 seed spectrum; no CSV col is an N36 Fourier coeff) | **ABSENT-NO-503-BASIS** |
| 9 | yes | yes (N6 also has 9) | **none for N36** — `a1_c*_e9/140` is the **N6** coefficient | **ABSENT-WRONG-PIECE** |
| 14 | yes | no | none | **ABSENT-NO-503-BASIS** |
| 16 | yes | no | none | **ABSENT-NO-503-BASIS** |

### Explicit non-identifications (invent HOLD)
- Do **not** fill N36 ν=1 from `a0_c0_e1/140` (or any `a0_c*_e1/140`). That column is N6.
- Do **not** fill N36 ν=9 from `a1_c0_e9/140` (or any `a1_c*_e9/140`). That column is N6.
- Do **not** invent a scaling / width / Ind rewrite that would send N36 ν∈{4,14,16} into a /140 or /980 CSV column. No such rewrite is Written.
- N6 fills already performed by MR1 (ν=1 → `a0_c0_e1/140`, ν=9 → `a1_c0_e9/140`) remain valid **for the N6 piece only**.

## 5. Consequence for MR1 ASSIGN (fill-after-map)
Under this Written map, the five open N36 cells ν∈{1,4,9,14,16} are **not fillable mod-p from the RHOS 89-CSV**. Correct post-map cell status:
- ν=1,9 → OPEN / ABSENT-WRONG-PIECE (await 503-basis)
- ν=4,14,16 → OPEN / ABSENT-NO-503-BASIS
- ν=0 stays VACUOUS

A future Owner Write would be required to authorize construction of an explicit 503-piece basis (or another Written source) before those cells can become FILLED-MODP.

## 6. Parallel track (not blocked)
Exact char-0 lift of the **89 / N6** basis continues under CLOSED_A `3cf5735c…` / ASSIGN `29ede292…` path (b) CRT. This map Write does not touch that lift.

## Constraints
invent HOLD; tip Soft SF LOCK tip_touched NO; Soft SF F3 CLOSED; Bridge PARTIAL READY NO; Cards 8–11 not opened.
