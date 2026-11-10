# Eigen N36 503-basis — FINDINGS (2026-10-26)

**STATUS: GAP-ABSENT (Step 1 MATCH; Steps 3–4 not runnable without a Written seed for the 36-piece).**

Cite-only. Invent HOLD honored. No Fourier coefficients invented. No 89-CSV column was forced onto N36. MR1 N36 cells ν∈{1,4,9,14,16} stay OPEN.

## Authority (sha256 verified at start)
- CLOSED_A `411024f5044735f2bca7d97e66039400d0117f6489ff3509030fb6f29637b552` OK
- ASSIGN `366004f1c7756a560325dc32697a4750db944a15dde508fd6b6690d52f60dec2` OK
- Open card `06b8ca6eaea9ede212d202d08007426142ab287aad9ff7f7d33798068c7d7f10` (cited)
- Source map ABSENT `67a5a6a3aecf468fbcf8000b1d3295daf4dd64a1769b703b9b8e34abcbd4b14d` (cited)
- RHOS 89 MATCH, N6 only: `a8788e5c63c9f84d6bed66c808db5831ab751d9d0d930b8603fa7e25fedf2efd` (cited; not used for N36)
- reverse-dimcalc `e2b260385fe0b4ce55e04ba364b74163cb3c66d1c4e42fa97696c774e59473e9` (cited)
- 4Q OPERATIVE `11f104c7361970a2dc02b3f6300071a20d32cad76f0055a616ebded1974ebff2` §(d) (cited)
- Exact-lift CRT `3cf5735ca0c2a61a0aeb5e7ed62de00cea47395ece07e4ed18b3330dfe2f2057`: left undisturbed
- Tip Soft SF LOCK: start = end = `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`. **tip_touched NO**

## Step 1 — exact N36 block extraction: MATCH
Script: eigen-n36-503/step1.sage. Output: eigen-n36-503/N36_ST.sobj = (B 140×36, S₃₆, T₃₆, T-eigen-exponents).
- Inputs: V42_exact.sobj `d1e532c8…f520d` and ST_W.sobj `a86980cf…1c72`.
- The dim-36 block is the V42 Eis-closure basis E1 (140×36). Its partner is the cusp6 basis (140×6).
- Exact checks over CF(140) all returned True:
  - S·B = B·S₃₆ and T·B = B·T₃₆
  - S₃₆² = I
  - (S₃₆T₃₆)³ = S₃₆²
  - T₃₆¹⁴⁰ = I
- T₃₆ has 36 distinct eigenvalues ζ₁₄₀^k, with k ∈ {0,6,10,14,19,20,24,26,31,34,35,40,54,55,56,59,66,70,75,76,80,84,90,91,94,96,104,110,111,115,119,124,126,131,136,139}.
- In the ρ̄ (conjugate) convention, the exponents /140 are {0,1,4,9,14,16,21,25,29,30,36,44,46,49,50,56,60,64,65,70,74,81,84,85,86,100,105,106,109,114,116,120,121,126,130,134}.
- **T-ord certification:** the exponents of ρ̄₃₆ that are ≤ 28/140 are exactly {0,1,4,9,14,16,21,25}. This equals the Written T-ord carried in reverse-dimcalc and Card1A, so it is **certified**.
- **Cross-check:** the same convention gives {1,9,29,81,109,121} on cusp6, which equals the Written N6 T-ord.
- The Written 8-set is the low part of the 36-exponent spectrum, not the whole spectrum. The 4Q §(d) mesh slots ν∈{1,4,9,14,16} are on-support.

## Step 1b — exact local decomposition of ρ̄₃₆ (new, exact)
Script: eigen-n36-503/localfac36.sage. Log: localfac36.log. This uses the same CRT-lift method as Card1D factor.sage, applied to the 36-block.
- ρ̄₃₆(S)⁴ = 1 and (ST)³ = S² hold exactly. The local images commute, and S = S₄S₅S₇, T = T₄T₅T₇ hold exactly.
- The local algebra dims are **9, 9, 16**, so ρ̄₃₆ ≅ ρ₄′ ⊗ ρ₅′ ⊗ ρ₇′ with dims **3 ⊗ 3 ⊗ 4**.
- Local T-exponents (/140; the multiplicity is the dim of the other factors):

| factor | dim | T-exponents /140 | as fractions |
|---|---|---|---|
| ρ₄′ | 3 | {0, 70, 105} | {0, 1/2, 3/4} |
| ρ₅′ | 3 | {0, 56, 84} | {0, 2/5, 3/5} |
| ρ₇′ | 4 | {0, 60, 100, 120} | {0, 3/7, 5/7, 6/7} |

- **Contrast with cusp6:** ρ̄|cusp6 ≅ ρ₄ ⊗ ρ₅ ⊗ ρ₇ has dims 1 ⊗ 2 ⊗ 3. The Written seeds are η power (ρ₄), Duke Rogers–Ramanujan (2-dim ρ₅) and Elkies Klein triple (3-dim ρ₇). **None of them realizes the 3-dim ρ₅′, the 4-dim ρ₇′, or the 3-dim ρ₄′.**

## Step 2 — seed search: GAP-ABSENT
I searched these artifacts:
- Card1A OW, Card1B OW, Card1D FINDINGS, Card1F OW and FINDINGS
- V42 FINDINGS 9b218a77…, Step4 FINDINGS 7ef0042b…
- RHOS FINDINGS and seeds, N36 map FINDINGS, reverse-dimcalc (as cited)

Results:
- The only seed ever Written with the 36-piece in scope is the Card1A lattice theta of A = [[2,7],[7,7]]. That lattice is indefinite, so the theta is Maass and non-holomorphic (Step4 Blocker 1). Card1B superseded it and Card1B did not select option B (pos-def Weil seed).
- The Duke/Elkies/η seeds (Card1E/1F) are Written for, and matched exactly to, the **cusp6 local factors only**.
- Applying the RHOS Ind pattern (Φ ⊗ h / Δ^m on Γ₀(49), 8-cusp holomorphy) to the 36-block needs a holomorphic (or weakly holomorphic) ρ̄₃₆-valued seed Φ₃₆. No Φ₃₆, and no S/T-Written classical families for ρ₄′, ρ₅′ or ρ₇′, exists on disk.
- Building one, for example from even unary theta / Weil representations of Z/4, Z/5, Z/7 discriminant forms, would mean asserting transformation laws that are not Written. **Invent HOLD → not done.**

## Steps 3–4: not executed
There is no Written seed, so no 503-form basis or spanning set was produced. **No a_ν mod p rows exist for N36.** The N6/89-CSV was not used.

## What MR1 can fill
**Nothing new for N36.**
- ν = 1, 4, 9, 14, 16 stay OPEN (ν = 1, 9 ABSENT-WRONG-PIECE; ν = 4, 14, 16 ABSENT-NO-503-BASIS).
- ν = 0 stays VACUOUS.
- The N6 fills are unchanged.

## Exact missing Write (any one unblocks Steps 3–4)
- **(W1)** Classical seed families, with verbatim literature S/T matrices like Card1F, for the three local factors:
  - ρ₄′: dim 3, T = {0, 1/2, 3/4}
  - ρ₅′: dim 3, T = {0, 2/5, 3/5}
  - ρ₇′: dim 4, T = {0, 3/7, 5/7, 6/7}
  
  For example, even-part Weil representations / unary theta vectors for these discriminant forms, with their η-twists. Eigen would then intertwine them exactly to localfac36 and run the RHOS Ind solve adapted to 36 (expected 36·56 = 2016-dim Ind type, target rank 503).
- **(W2)** Or an Owner authorization of a seed-free method for the 36-piece, e.g. Γ₀(49) ∩ Γ(140) modular symbols, or scalar weight-4 forms on Γ(140) averaged into ρ̄₃₆ ⊗ Ind (Card1B option, applied to 36).
- **(W3)** Or a positive-definite lattice whose Weil representation contains ρ̄₃₆, with exact containment checked (Card1B option B).

## Artifacts (eigen-n36-503/ARTIFACTS.sha256)
| sha256 | file |
|---|---|
| `6332c54e32ff0be674584cc65776e6301272acb7d71914d54a0c623d3386b40f` | N36_ST.sobj |
| `378936d38f3745a1e486bc675b803c73e97b97e538b167fd96fd3d7b5120f3c3` | step1.sage |
| `73d61dbbb9996fbaed516a2a4e54748449d80239c08734cf267b386611b82e92` | inspect.sage |
| `c55c5a99372cc3c4cafd9502dab976546675379a4a8499574637f74faf0ba63c` | localfac36.sage |
| `fd2533fa3123369699a90515f3166d2b65c9697a27ffe0a28c7216439ce74e06` | localfac36.log |

## Constraints
- invent HOLD.
- tip_touched NO.
- Soft SF F3 CLOSED.
- Bridge PARTIAL READY NO.
- Cards 8–11 not opened.
- No messaging.
- rhos/ CRT not touched: no reads were run as jobs there and no writes were made.
