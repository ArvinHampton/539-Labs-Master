# Eigen N36 503 — W1 classical seeds + intertwiners + mod-p basis — FINDINGS (2026-10-26)

**STATUS: MATCH (mod p).**
- All three local factors are realized by classical Weil-representation theta seeds. The S/T formula is quoted verbatim from Borcherds 1998.
- The seed representation is intertwined exactly with ρ̄₃₆ over CF(140).
- The RHOS-Ind solve, adapted to the 36-piece, reaches **rank 503 = dim S₄(Γ₀(49), ρ̄₃₆)** through q^18 at ∞, at two primes p ≡ 1 mod 980.
- MR1-fillable rows for ν ∈ {1,4,9,14,16} are exported.
- Exact char-0 lift is not done.

Cite-only and invent HOLD hold throughout. No transformation law outside the cited theorem was used. No 89-CSV column was used.

## Authority (sha256 verified at start)
- CLOSED_A W1: `19da5cf82fa1ff61e2aa94a0c92ee52faa7978288609ef763225fe437cf1c184` OK
- ASSIGN W1: `6a8c91e8591b513b7737757a55fc79394f00b254ec3fafad1c2bfa468193e065` OK
- Open prior: `ba1969254c47f1f9de962a237005d39ab67943063a4bf21f39f4a945fa64de68` (cited)
- Source GAP-ABSENT FINDINGS: `a8547419cc5f0f041b29a57d36f00e3279a63e9d2bbbb89c69dbfc0c83bc8349`
- Prior authorize: `411024f5044735f2bca7d97e66039400d0117f6489ff3509030fb6f29637b552`
- Prior ASSIGN: `366004f1c7756a560325dc32697a4750db944a15dde508fd6b6690d52f60dec2`
- 4Q OPERATIVE: `11f104c7…` §(d)
- reverse-dimcalc: `e2b26038…` (dim 503)
- RHOS N6: `a8788e5c…` (not used for N36)
- Exact-lift CRT: `3cf5735c…` — **rhos/ not touched** (no writes; the CRT solve.sage processes were left running)
- Tip Soft SF LOCK: start = end = `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`. **tip_touched NO**

## 1. Literature (verbatim)
**Source:** R. E. Borcherds, *Automorphic forms with singularities on Grassmannians*, Invent. Math. 132 (1998) 491–562, arXiv alg-geom/9609022, §4. The PDF is saved at eigen-n36-503/lit/borcherds.pdf, sha `f0e76c70…02ba`. Quoted:

> ρ_M(T)(e_γ) = e((γ,γ)/2) e_γ,  ρ_M(S)(e_γ) = (√i^{b⁻−b⁺} / √|M′/M|) Σ_{δ∈M′/M} e(−(γ,δ)) e_δ

> **Theorem 4.1.** If p is a homogeneous polynomial of degree (m⁺,m⁻) and (ab;cd, √(cτ+d)) ∈ Mp₂(ℤ) then Θ_M((aτ+b)/(cτ+d), …) = (cτ+d)^{b⁺/2+m⁺} (cτ̄+d)^{b⁻/2+m⁻} ρ_M(…) Θ_M(τ, …), where Θ_M = Σ_γ e_γ θ_{M+γ}.

How it is applied here:
- Lattices are positive definite (b⁻ = 0) and p = 1, so Θ_M is a holomorphic vector-valued modular form of weight rank/2 for ρ_M.
- −1 ∈ Aut(M), so θ_γ = θ_{−γ}. The {±1}-orbit-sum vectors therefore span a ρ_M-subrepresentation, and the theta components are constant on orbits.
- Serre derivative ϑ_k = q d/dq − (k/12)E₂, applied componentwise. This is the same operator RHOS used.

## 2. Seeds (one classical lattice per local factor)
| factor | lattice | weight | orbit classes | q-values (T-exps) | matches localfac36 |
|---|---|---|---|---|---|
| ρ₄′ (dim 3) | D₆ | 3 | {0}, {v}, {s,c} | {0, 1/2, 3/4} | ✔ |
| ρ₅′ (dim 3) | A₄ | 2 | {0}, {±1}, {±2} | {0, 2/5, 3/5} | ✔ |
| ρ₇′ (dim 4) | A₆ | 3 | {0}, {±1}, {±2}, {±3} | {0, 3/7, 5/7, 6/7} | ✔ |

- **Seed vector:** Θ = Θ_{D₆} ⊗ Θ_{A₄} ⊗ Θ_{A₆} = Θ_{D₆⊕A₄⊕A₆}. It has rank 16, weight 8 and 36 components.
- **T-exponents:** the 36 exponents ·140 equal the ρ̄₃₆ spectrum exactly, which includes the Written T-ord {0,1,4,9,14,16,21,25}.
- **S/T matrices:** exact over CF(140) from the quoted formula, using constants √i^{−6}/2, √i^{−4}/√5 and √i^{−6}/√7.
- **Group relations:** S⁴ = 1 and (ST)³ = S² hold exactly for each factor.
- **Numeric S-law check (independent):** Θ(−1/τ) = τ⁸ S_seed Θ(τ) at 200 bits has residual 1.9e−59.
- **Files:** seeds36w.sage / seeds36w.log / seeds36w.sobj.

**Wronskian (cyclic generator) criterion.** For each factor, the sum of leading exponents equals (k·d + d(d−1))/12:

| factor | sum of leading exponents | required |
|---|---|---|
| D₆ | 5/4 | 5/4 |
| A₄ | 1 | 1 |
| A₆ | 2 | 2 |

So each factor's Serre-derivative Wronskian is a nonzero power of η and has no zeros on H. The 36 tensor families ϑ^aΘ_{D₆} ⊗ ϑ^bΘ_{A₄} ⊗ ϑ^cΘ_{A₆} (a ≤ 2, b ≤ 2, c ≤ 3) therefore span ℂ³⁶ pointwise on H. This is the RHOS pattern.

**First attempt (superseded, recorded):**
- I first used D₆ ⊕ B with B = [[2,−1],[−1,18]] (disc −35, rank 8, weight 4). Its intertwiner is also CERT True (seeds36.log).
- Its 12-dim theta fails the Wronskian criterion: the sum of leading exponents is 7, but 12 is required.
- The rank stalled at 16 (m=3) and 28 (m=5) (solve36_m3/m5.log), so I replaced it with D₆ ⊕ A₄ ⊕ A₆.
- B is alone in its genus. The other disc −35 form [[6,1],[1,6]] is in a different genus, so it has different q-values (seedsB2.sage).

## 3. Intertwiner: CERTIFIED exact
- The convention is ρ̄ = S₃₆^{−T}, T₃₆^{−T} from N36_ST.sobj, which is the same as RHOS and Card1F.
- Q = V·diag(d). The kernel of the d-system has dimension 1.
- **S̄·Q == Q·S_seed: True. T̄·Q == Q·T_seed: True. det Q ≠ 0: True.**
- Since the localfac36 local images S_p, T_p are words in S, T (CRT lifts), Q intertwines every local factor too. The seed's own local factors are the tensor factors D₆ / A₄ / A₆.

## 4. Steps 3–4: RHOS Ind adapted to 36 (eigen-n36-503/solve36w.sage)
**Construction.**
- F = Σ_j Φ_j h_j / Δ^m, where h_j ∈ M_{4+12m−wt Φ_j}(Γ₀(49)).
- The h_j are an incremental pivot basis of monomials in E₄, E₆, Δ at τ, 7τ, 49τ.
- Ind slash is done by Hermite decomposition, with the same 8 cusp representatives and widths as RHOS.
- **Cusp-form conditions:** every coefficient with exponent ≤ 0 vanishes, at all 8 cusps.
- **Truncation:** exponents in (0, 18] at ∞, giving 648 slots.

**Rank by m:**

| m | p | unknowns | polar+const eqs | RANK |
|---|---|---|---|---|
| 3 | 7840981 | 3271 | 5241 | 72 |
| 5 | 7840981 | — | — | 472 |
| 7 | 7840981 | 11700 | 13305 | **503** |
| 7 | 7946821 | 11700 | 13305 | **503** |

- **Basis argument:** rank 503 equals dim S₄(Γ₀(49), ρ̄₃₆) from reverse-dimcalc, and the rank cannot exceed it. So the 503 forms are a basis, and truncation at ∞ through q^18 is injective on S₄.
- **Caveat:** the rank was computed mod p at two primes. A char-0 lift (CRT, as in the N6 path (b)) has not been done.

## 5. MR1 fill (mod p = 7840981; second prime 7946821 available)
- **Full basis:** `eigen-n36-503/n36_basis_q18_inf_modp.csv`. It is the 503 × 648 echelon basis. Columns are `c{component}_e{exponent}` in seed (theta-orbit) coordinates.
- **Five on-mesh slots:** `eigen-n36-503/n36_mr1_nu_rows_modp.csv` holds, for each ν, the 503-vector of a_ν (the coefficient at exponent ν/140 of the N36 component whose T-exponent is ν/140). It is given sparsely as row:value.

| ν | seed component | exponent | nonzero basis rows |
|---|---|---|---|
| 1 | 31 | 1/140 | 338 |
| 4 | 9 | 4/140 | 1 |
| 9 | 34 | 9/140 | 327 |
| 14 | 20 | 14/140 | 1 |
| 16 | 6 | 16/140 | 1 |

- ν = 0 stays VACUOUS (cusp form).
- Seed → ρ̄ coordinates: multiply by Q (seeds36w.sobj). Q is diagonal-times-V in the T-eigenbasis, so each a_ν changes only by a fixed CF(140) scalar per component.
- 4Q §(d) is respected: ν = n is on the N36 T-ord for each slot.
- **The 89-CSV (N6) is not used anywhere.**

## Artifacts (eigen-n36-503/ARTIFACTS_W1.sha256)
| sha256 | file |
|---|---|
| `8078d9c9380012aa2675060e09d93b4db9144397b30188eac831cd1a736350a6` | seeds36w.sobj |
| `fa94cca219b0edff72d6a7f8f5b76f02a9745a0370fd3ea6c1030cc784120b6b` | seeds36w.sage |
| `c578c148c98df4f53261d47dd3bdd8ff4d7a97978ee6c6ade914f9177314b9e4` | seeds36w.log |
| `2236118b438197cb6eb28e95dfcae1f5bec2cc9d35ccc9731472b6ed31d88a34` | solve36w.sage |
| `b6708cb55b838cb1dec0f307997b14f0640116136bc25f160787fd91dd5f6649` | solve36w_m7.log |
| `148cb9217c180e8cc00490153c85b426e7aa67e1d0b8d3b369ef8cad427704c5` | solve36w_m7_p7946821.log |
| `156855ea06dad15daf12689b77be0e9c66b71debc1f23832f839c9652dde127b` | n36w_modp_m7_p7840981.sobj |
| `dc1bc9a63184384a6f301af4f3fe8e080292726fc7032052d113367a7247c4c9` | n36w_modp_m7_p7946821.sobj |
| `e707cc96b0cf9c40d671a78c164bcdff5e4f7f81915bc47782e3a909c74f984c` | n36_basis_q18_inf_modp.csv |
| `5e3c31555832444dcd6f90d96e0e75ab5df0f090cb47a81675eefa8140e900ba` | n36_mr1_nu_rows_modp.csv |
| `9e97d0bbf444774e012d28077f05ef9ed19426db2f351ef1e8a0cc6132c81aa9` | export36.sage |
| `f0e76c70f57e63bb145b36ca97635312bb906787f4c521015acc03781c7702ba` | lit/borcherds.pdf |
| `6332c54e32ff0be674584cc65776e6301272acb7d71914d54a0c623d3386b40f` | N36_ST.sobj |

Superseded first attempt: seeds36.* and solve36.* (hashes in the same file).

## Constraints
- invent HOLD.
- tip_touched NO.
- Soft SF F3 CLOSED.
- Bridge PARTIAL READY NO.
- Cards 8–11 not opened.
- No messaging.
- rhos/ untouched.
