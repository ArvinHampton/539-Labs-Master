# FINDINGS — Eigen N36 Kr RREF height bound (Hadamard / CRT primes) — 2026-11-05

Status: **PARTIAL — rigorous numeric upper bound NOT CLOSED.** No CERT. Tip untouched. No external send.
Inspected ~16:00–16:20 CST (America/Chicago). Weekly usage gate at start: 77.1% (below 90%); proceeded.
Light Sage only (`/workspace/venv_sage_mr1_312/bin/sage`): building-block L1 sizes and arithmetic; **no prime-job relaunch**.

## 0. Matrix that is actually on disk

Source solver: `/workspace/grok-batches/eigen-n36-503/solve36w_z.sage` (m=7).

- **Polar matrix** `MPs`: size **11700 × 13305**, built over `GF(p)` for primes `p≡1 (mod 980)`, `p<2^23`.
- Rows = unknowns `(j, monomial)` in cusp-form coefficient spaces of weights `{66,68,…,80}`; columns = polar(+constant) conditions at 8 cusps × 36 seed components.
- **Left kernel** `Kr`: dimension **503** (all completed e1 runs); object reconstructed is `Kr_rref` (503 × 11700) with identical pivots across tested primes.
- **Field of definition of entries of `MPs` before reduction:** coefficients of Weil/Serre seed series × `Δ^{-m}` lie in `ℚ`; slash of `E4,E6,Δ` introduces **`ζ_49`**, so the polar matrix is naturally over **`ℚ(ζ_49)`**, reduced to `𝔽_p` via a chosen root `r_p` (least root of `Φ_49`, optional Galois power `e`).
- Seeds live in a cyclotomic package of order **140** (`seeds36w.sobj`), but the q-expansions fed into `PhU` are rational/integer lists; `ζ_49` enters through `slash_series`.
- **No** cleared-denominator integer matrix, **no** `ℚ(ζ_49)` polar matrix, and **no** integer 503-row kernel basis are stored. Only mod-p `*.sobj` (`Kr_rref`, pivots, `unk`). `unk` agrees on sampled primes 7840981 and 8007581.

Empirical stabilizer (mod p only): at p∈{7840981,7957601}, `Kr_rref` invariant under `k=2,3,48` / generator `3` of `(ℤ/49)ˣ` — **consistent with** a model over `ℚ`, **not** a proof of Gal(`ℚ(ζ_49)/ℚ`)-descent.

## 1. Definition — height of the RREF  *(definition; adopted here)*

Let `K ∈ Mat_{503×11700}(ℚ)` be the unique reduced-row-echelon basis matrix of the left kernel over `ℚ` (assuming descent; see Gap D1), with pivot set `P` and `K[i,p_i]=1`.

For `x=a/b∈ℚ` in lowest terms (`b>0`, `gcd(|a|,b)=1`), set
`h(x) := max(|a|,b)`.
Define the **RREF height**
`H := max { h(K_{ij}) : 0≤i<503, 0≤j<11700 }`.
(Equivalent bit form: `log₂ H`. Common-denominator row height `max(D, max|n_j|)` for a row written with single `D` is ≥ each entry height and was what the LLL recon scripts probe.)

This matches the quantity controlled by rational reconstruction / CRT holdout tests in `recon_all.sage`.

## 2. Standard theorems (full statements)

### 2.1 Hadamard’s inequality  *(proved — classical)*

Let `B∈Mat_{r×r}(ℂ)` with rows `v_1,…,v_r`. Then
`|det B| ≤ ∏_{i=1}^r ‖v_i‖₂`,
where `‖v‖₂ = (∑_j |v_j|²)^{1/2}`.
Proof sketch: `|det B| = vol(parallelepiped) ≤ ∏ ‖v_i‖₂` by induction / Gram–Schmidt (`|⟨v_k,u⟩|≤‖v_k‖₂`). Over `ℤ` the same bound holds with the Euclidean norm of integer rows. Variant used below: `|det B| ≤ ∏_{i∈S} ‖row_i(A)‖₂` for any selection of `r` rows and `r` columns of a larger matrix `A` (apply Hadamard to that submatrix). Product of the **r largest** row norms of `A` is a valid (often loose) upper bound on every `r×r` minor’s absolute value.

### 2.2 Cramer / Plücker for kernel coordinates  *(proved — classical)*

Let `A∈Mat_{m×n}(K)` have rank `ρ`, with `K` a field. The right kernel has dimension `n−ρ`. Its Plücker coordinates in `⋀^{n−ρ} K^n` are, up to a common scalar, the signed `ρ×ρ` minors of `A`. Concretely: choose a set of `ρ` pivot columns so the corresponding `ρ×ρ` block `B` is invertible; free-column coordinates of a kernel basis vector are given by Cramer ratios `±det(B_j)/det(B)`.

**For the N36 polar matrix:** `MPs` is `11700×13305` with left nullity 503, hence **rank ρ = 11700−503 = 11197**. Left kernel of `MPs` = right kernel of `MPs^T`, so kernel Plücker coordinates are ratios of **`11197×11197` minors** of `MPs^T` (equivalently of `MPs`).

**Correction to intake/`physics-research-1` wording:** saying “`r×r` minors with `r=503` of the N36 matrix” confuses **kernel dimension** with **polar rank**. Minors of size 503 appear only if one first has an explicit integer `503×11700` matrix presenting a `ℤ`-basis of the kernel and then RREFs **that** matrix; no such integer presentation is on disk. Using `r=503` on the polar matrix itself is **not** the Plücker expression for `ker`.

After reducing pivots to 1, each RREF entry is a ratio of two such minors (or a single minor over the pivot minor). If all Plücker coordinates are taken content-primitive over `ℤ`, then `H ≤ max|minor|`. Without a pivot-minor lower bound, the safe ratio bound is `H ≤ (max|minor|)²` in bit-length `2 log₂(max|minor|)`.

### 2.3 Rational reconstruction uniqueness  *(proved — standard)*

**Theorem.** Let `x=a/b∈ℚ` with `h(x)≤H`, and let `M≥1` with `gcd(b,M)=1`. Suppose `u∈ℤ` satisfies `b u ≡ a (mod M)` and `2 H² < M`. Then `x` is the unique rational of height `≤H` reducing to `u mod M`. (Wang / standard CRT rational reconstruction: if `a/b = a'/b'` both reduce to `u` and heights `≤H`, then `a b'−a' b` is divisible by `M` but has absolute value `<M`, hence vanishes.)

**Consequence for a full RREF:** if every entry has height `≤H` and the product `M=∏ p_i` of good reduction primes (avoiding primes dividing any pivot-minor denominator, and with matching pivots) satisfies **`2 H² < M`**, then the CRT system of mod-p RREFs determines at most one rational RREF of height `≤H`. A holdout prime then **verifies** that candidate. Bit form: need
`log₂ M > 1 + 2 log₂ H`.
With mean `log₂ p ≈ 22.918` on the completed N36 e1 list, the prime count satisfies
`N ≳ ⌈(1+2 log₂ H)/22.918⌉`
(plus ≥1 holdout; reconstruction scripts that LLL-jointly lift `s` entries of a row need a slightly larger lattice modulus, classically ~`(s+1)/s` times the single-entry bit budget — not used in the strict per-entry `2H²<M` theorem above).

## 3. Attempted numeric Hadamard bound from construction data  *(conditional envelope — NOT a closed proof)*

### 3.1 What was computed (light)

Building blocks at `m=7`, `NQ=26`, `NL=1324` (Sage):

| quantity | value | `log₂` |
|---|---|---|
| `L1(E4)` | ~1.99×10¹⁴ | 47.50 |
| `L1(E6)` | ~4.59×10²⁰ | 68.64 |
| `L1(Δ)` | ~1.41×10¹⁹ | 63.61 |
| max `L1` of any wt-80 monomial in `{E4,E6,Δ}` (levels 1,7,49 same L1) | ~9.72×10²⁸⁵ | 950.03 |
| max `L1` of Serre-chain×`Δ^{-7}` Phi coeff list | ~2.07×10⁴⁰ | 133.93 |
| Phi coefficient denominator | ≤ 24385536 | — |
| slash clear-denoms | `D_p\|N∈{1,7,49}` ⇒ clear by `≤49^k` for weight-`k` forms | `log₂(49^80)≈449.18` |

Row counts by form weight (from solver log basis sizes × family counts):  
66:293, 68:903, 70:1866, 72:2568, 74:2632, 76:2034, 78:1047, 80:357 (sum **11700**).

**Conditional envelope** (ASSUMED chain in §3.2): bound each row’s Euclidean norm by `√(13305)·(Phi_L1·maxL1(k)·Phi_den·49^k)`, take the product of the **11197 largest** such norms (Hadamard), and set `H ≤ max|minor|`:

- **`log₂ H ≲ 1.6217×10⁷`**
- **decimal digits of `H` ≲ `4.882×10⁶`**
- bits for `2H²`: `≲ 3.243×10⁷` ⇒ **`N ≳ 1.415×10⁶` primes** at ~22.9 bits/prime

(If one wrongly used `r=503` on polar rows: `log₂` envelope ~7.8×10⁵ — still ≫ available supply.)

### 3.2 Gaps that block calling §3.1 a proved bound on `H`  *(exactly what is missing)*

| ID | Gap | Status |
|---|---|---|
| **D1** | Descent: `ker` over `ℚ(ζ_49)` equals the extension of a `ℚ`-kernel. Only mod-p stabilizer evidence (2 primes). | **ASSUMED / unproved** |
| **D2** | Integral model: no cleared-denominator matrix over `ℤ` or `ℤ[ζ_49]` is on disk; §3.1 uses L1/`house` majorants, not measured row norms of an actual integral matrix. | **MISSING DATA** |
| **D3** | Cyclotomic Hadamard: for entries in `ℚ(ζ_49)`, either (i) Weil restriction to a `ℚ`-matrix of size `×φ(49)=×42`, or (ii) house-Hadamard + field-norm control of Gal-invariant Plücker ratios, must be fixed. Norm route can multiply bit-length by up to **42**. Not derived here. | **DEFINITION / PROOF GAP** |
| **D4** | Pivot-minor lower bound: `H ≤ Had` needs content-primitivity or `|det B|≥1` after clearing; otherwise use `H ≤ Had²`. | **ASSUMED** (`H≤Had`) |
| **D5** | `hb()` monomial pivots are computed in `𝔽_p`; identity of `unk` across two primes was checked, not proved for all primes. | **partial evidence** |
| **D6** | Intake `r=503` minor size is the wrong Plücker degree for the polar matrix (correct ρ=**11197**). | **intake error** |

**Bottom line:** a rigorous, closed numeric `log₂ H` from “the matrix data” is **not obtainable** from what is stored. The cyclotomic slash structure plus missing integral polar matrix are the blockers. Do not treat §3.1 as CERT or as a proved upper bound.

### 3.3 Empirical lower bound (heuristic / computational — not Hadamard)

Holdout rational reconstruction fails at 24 training primes with `log₁₀ M ≈ 165.57` (and earlier at 19 primes with generic LLL heights ~10¹²¹). This is **evidence** that true row heights exceed ~10¹²¹ (~400 bits), labelled **heuristic lower** in prior FINDINGS — not a proved lower bound from failed LLL alone (a failed sample of ≤12 nonpivot entries per row does not certify full-RREF height).

## 4. CRT prime count vs supply

| item | value |
|---|---|
| Completed e1 primes (inventory) | **25** (plus incomplete/partial 8022281 artifacts) |
| `∑ log₂ p` over 25 | ≈ **572.95** (~173 decimal digits of `M`) |
| Mean `log₂ p` | ≈ **22.918** |
| Available further `p=980k+1` below `2²³` after 8007581 | **61** (earlier writeups said ~66 incl. counting convention) |
| Total such primes in script range | **99** |
| Primes needed if §3.1 envelope were a true `H` | **≳ 1.4×10⁶** — far beyond supply |
| Primes needed for a hypothetical `log₂ H = 500` | `⌈(1+1000)/22.918⌉ = 44` (+holdout) |
| Primes needed for `log₂ H = 2000` | `⌈(1+4000)/22.918⌉ = 175` (> supply under `p<2²³`) |

**Proved implication of §2.3 alone:** until a proved upper `H` exists, one **cannot** certify from prime count that reconstruction must succeed. The 25-prime failure is compatible with `H` above ~`√(M/2)`.

## 5. Logic review of existing proof material (no hash/tamper validation)

**`/workspace/pqc-gemini-request-intake-20261105-1513/` (12 intakes):**
- Only `eigen.md` states the O5(c) height ask (definition + Hadamard/minor bound + prime count). It does **not** contain a proof.
- `professor-proof.md`, `math1.md`, `math2.md`, `physics1/2`, `local`, `nonlocal`, `labs539`, `dataset`, `agent`, `auditor`: **no** N36 Hadamard/Cramer height derivation.

**`/workspace/quantum-comp/distributions/gemini-incoming-20261105-1536/`:**
- `responses/eigenvalues-and-matrix.md`: explicitly — none of the 21 Gemini files supply an N36 height proof; question remains open.
- `responses/physics-research-1.md`: restates the ask (define height; Cramer+Hadamard with **r=503**; certify `∏p>2H²`); provides **no** derivation or numeric `B`.
- Gemini file bundles under `eigenvalues-and-matrix/files/` / `professor-proof/files/`: no Hadamard/RREF height proof for N36 (per eigen review; spot-checked via search).
- No on-disk proof closes Gaps D1–D4.

**Prior Eigen FINDINGS:** give computational lower heuristics (~10¹²¹) and ESTIMATE prime scaling; repeatedly mark upper height bound as **NEEDS-DEFINITION**. Agree with this report.

## 6. Proof-status board

| Step | Status |
|---|---|
| Height definition (§1) | **Adopted definition** |
| Hadamard inequality (§2.1) | **Proved** (standard) |
| Cramer/Plücker for kernel (§2.2) | **Proved** (standard); **ρ=11197** for polar `MPs` |
| Rational reconstruction `2H²<M` (§2.3) | **Proved** (standard) |
| Polar matrix field = `ℚ(ζ_49)` before reduction | **Proved from construction** (`slash_series` uses `z49`) |
| Kernel descends to `ℚ` | **Assumed** (mod-p evidence only) — Gap D1 |
| Numeric `log₂ H` from stored matrix row norms | **Missing** — no integral matrix on disk — Gap D2 |
| Cyclotomic house/norm → `ℚ`-height | **Gap** — Gap D3 |
| Conditional L1 Hadamard envelope (§3.1) | **Computed under assumptions**; **not** a proved bound on `H` |
| Empiricial `H≳10¹²¹` | **Heuristic lower** from failed recon |
| Primes needed from proved `H` | **Blocked** until upper `H` closed |
| Intake claim “minors r=503 of N36 matrix” | **Incorrect** as Plücker degree of polar matrix |

## 7. What would close a proved numeric bound

1. Fix an integral model of the polar matrix over `ℤ` (clear dens) or a documented house+norm pipeline over `ℤ[ζ_49]` with Gal-descent theorem for `ker` (close D1, D3).
2. Compute (or rigorously majorize) the **actual** Euclidean row norms of that model; apply Hadamard at **ρ=11197** (or build an explicit saturated `ℤ`-kernel basis of size 503×11700 and apply Hadamard at 503 to **that** matrix).
3. Publish `log₂ H` and `N = ⌈(1+2 log₂ H)/mean_log₂ p⌉` with holdout policy.

## 8. Hygiene

- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: not modified this turn (expected SHA-256 `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`).
- No CERT. No messages/Gemini/external send. No tip file touched.
- Companion PRESS: `PRESS_EIGEN_N36_HEIGHT_BOUND_2026-11-05.md`.

