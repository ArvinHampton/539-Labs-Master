# Where s = 7 sits in the Bridge C s-family (s = 5..60)

Prepared 20 Oct 2026 (CDT). Local only: nothing was posted and the repo was not edited. PARI/GP was called through cypari2.

Files:
- `s_family.py` produces `s_family.csv` (one row per s);
- `distinctive.py` produces `distinctive.out`.

Manuscript citations refer to `heavy-daily/2026-10-19-Bridge-C-Clean-v2/tex/`.

## Definitions used

These follow the manuscript: Q_s, A_s = [[2,s],[s,s]], n_s = s(s−2), D_s = 4n_s for odd s and n_s for even s, and the automorph unit ε_s = (s−1)+√n_s (s01_intro.tex:131-134).

- **The field:** K_s = Q(√n_s). Its fundamental unit and class numbers h and h⁺ come from PARI (bnfinit, quadunit, quadregulator). The narrow class number is h⁺ = 2h when the fundamental unit has norm +1.
- **The order of discriminant D_s:** class numbers via quadclassunit and quadunit.
- **Conductor analogue (my choice).** At s = 7 the conductor is 𝔣 = 𝔭₂𝔭₅∞₁∞₂ (s04_rq.tex:52). I generalize it to 𝔣_s = (product of the primes above every p | 2(s−2))·∞₁∞₂ and report the narrow ray class number (bnrinit). Sanity check: this gives **16 at s = 7**, the same as the manuscript's "order 16" (s04_rq.tex:63).
- **Discriminant group order:** |L′/L| = |det A_s| = n_s (35 at s = 7, matching s01_intro.tex:85).

Three facts hold for every s by construction:
- **N(ε_s) = (s−1)² − n_s = 1.** Every s has a norm-+1 automorph unit, so "norm +1" cannot single out s = 7.
- **2 log ε_s increases with s.** It is 4.1269 at s = 5 and 4.9558 at s = 7. s = 7 is not the minimum.
- **dim V, the Eisenstein dimension and the cusp dimension come from the manuscript table (s12_dims.tex:22-45).** The table covers s = 5–51 and 72. I did not recompute these.

## Table summary (full data in s_family.csv)

| s | n_s | sqfree | d_K | h | h⁺ | N(ε_K) | ε_s = ε_K^k | narrow ray no. | dim V | d_cusp |
|---|---|---|---|---|---|---|---|---|---|---|
| 5 | 15 | 15 | 60 | 2 | 4 | + | 1 | 8 | 20 | 2 |
| 6 | 24 | 6 | 24 | 1 | 2 | + | 1 | 2 | 12 | **0** |
| **7** | **35** | **35** | **140** | **2** | **4** | **+** | **1** | **16** | **42** | **6** |
| 8 | 48 | 3 | 12 | 1 | 2 | + | 2 | 2 | 18 | **0** |
| 9 | 63 | 7 | 28 | 1 | 2 | + | 1 | 12 | 72 | 12 |
| 10 | 80 | 5 | 5 | 1 | 1 | − | 6 | 1 | 30 | **0** |
| 11 | 99 | 11 | 44 | 1 | 2 | + | 1 | 16 | 110 | 20 |
| 12 | 120 | 30 | 120 | 2 | 4 | + | 1 | 16 | 42 | 6 |
| 13 | 143 | 143 | 572 | 2 | 4 | + | 1 | 40 | 156 | 30 |

Rows for s = 14..60 are in the CSV.

## Which s lack a cusp part

The manuscript table gives d_cusp = 0 only at **s = 6, 8, 10**. In the authors' words: "d_cusp>0 for every s in the table except s=6,8,10" (s12_dims.tex:49). Every other tabulated s has d_cusp > 0 (44 values). Beyond s = 51 the table lists only s = 72, which has d_cusp = 762.

## Candidate "s = 7 is special" properties: how many s ∈ [5,60] share each

| Property | Holds at 7 | Number of s | Which s |
|---|---|---|---|
| ε_s is the fundamental unit of K (k = 1) | yes | 46 | most s; fails at 8, 10, 18, 20, 27, 32, 34, 50, 52, 56 |
| N(ε_K) = +1 | yes | 51 | fails at 10, 18, 20, 34, 52 |
| n_s squarefree (Z[√n_s] maximal and ε_s fundamental; the proof uses this at s03_main.tex:28) | yes | 19 | 5, 7, 13, 15, 17, 19, 21, 23, 31, 33, 35, 37, 39, 41, 43, 53, 55, 57, 59 |
| n_s = product of two primes (s−2, s twin primes; D = 35 = 5·7) | yes | 6 | 5, 7, 13, 19, 31, 43 |
| h(K) = 2 and h⁺(K) = 4 | yes | 18 | 5, 7, 12, 13, 14, 22, … |
| twin primes **and** h⁺ = 4 | yes | 3 | 5, 7, 13 |
| one narrow class per genus | yes | 42 | — |
| narrow ray number mod 𝔣_s = 16 | yes | 8 | 7, 11, 12, 22, 27, 32, 38, 42 |
| table dim V equals the orbit bound | yes | 43 | fails only at s = 2m²: 8, 18, 32, 50 (s12_dims.tex:14-15) |
| dim V = 42, d_cusp = 6 | yes | 2 | 7, 12 |
| d_cusp > 0 | yes | 44/47 | all tabulated s except 6, 8, 10 |

**No property tested here holds at s = 7 alone.** The narrowest are:
- dim V = 42 with d_cusp = 6, shared with s = 12;
- twin-prime n_s with h⁺ = 4, shared with s = 5 and 13.

**Not tested.** Two s = 7 results exist only at s = 7 because they were only computed there: dim M(ρ) = 2 / S(ρ), and the 36+6 Eisenstein/cusp split with its 12 Maass forms. No other s has these computed, so they cannot be compared. "Unique" would mean "uncomputed elsewhere", not "false elsewhere".

## Is the residual's ray class a single class at other s?

The manuscript proves this at s = 7, where the γ-orbits correspond bijectively to ideals in one narrow ray class 𝒦 (s04_rq.tex:50-57). It states the same for s = 8 and 11: "Multiplicity one (no double counting)", and 2P_s = E_s+1+θ₃−Θ_hol,s exactly to q³⁰⁰⁰ (s17_sfamily.tex:38-40).

My earlier test (`../539_uniqueness/bridgeC_family.out`) confirmed the fundamental-cone identity E_s = Σ_{v+a∈[r,γr)} q^{Q_s(v)} for s = 5–30 and several larger s. I did not verify the single-ray-class identification for general s; that needs the ideal-to-cone bijection for each s.

The genus side does not single out s = 7: 42 of 56 values of s have one narrow class per genus.

## Verdict

**"Every other s has its own analogous structure" is supported.** For each s, the same objects can be computed: a real quadratic field, a norm-+1 automorph unit, class and ray class groups, a discriminant form, and an orbit-bound dim V. For all tabulated s except 6, 8 and 10 there is also a non-zero cusp part.

**s = 7 is a typical member** of the odd, squarefree-n_s subfamily (19 of 56 values of s). Within that it belongs to the twin-prime subfamily (s = 5, 7, 13, 19, 31, 43). No fine invariant computed here is unique to s = 7. The closest coincidences are shared with s = 12 (dim V = 42, d_cusp = 6) and with s = 5 and 13 (twin primes with h⁺ = 4).

**Two caveats:**
- The ray-class conductor 𝔣_s is my generalization; it reproduces 16 at s = 7.
- Invariants the manuscript computed only at s = 7 cannot be compared.
