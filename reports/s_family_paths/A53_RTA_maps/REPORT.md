# A53: Map 1 and Map 2 of the Bridge C to RTA preregistration, run

**For:** Arvin Hampton (539 Labs) · 2026-10-22, about 7:00 PM CDT (America/Chicago).
`SF/` = `/workspace/quantum-comp/reports/s_family_paths/`. Everything is in `SF/A53_RTA_maps/` (new files only). The A52 draft is untouched.

**Authorization.** "Pursue all" was treated as approval to finalize and run the A52 draft with its stated defaults. Map 2 ran after Map 1. Even s is descriptive only and was not run. The s in {7, 8, 11} selection and the packaging integers were not used. The questions about the RTA axioms and the {−1, 0, +1} data were unanswered and no map uses them.

**Freeze.** `prereg.md` was finalized from `prereg_draft.md`. Sections 1 to 6 (objects, predictions, falsifiers, outcomes) are byte-identical to the draft apart from the title and status lines. SHA256, written to `prereg.sha256` before any run:
`a44f677970db173baf4af4589d598288623012ff55dd98c5346961a58fa33c52`.
It was re-verified after the runs and still matches. Implementation details the draft left to "the frozen version" are fixed in prereg section 10 (before any run). Script hashes and every later addition are in `AMENDMENTS.md` with timestamps.

**Ground rules kept.** The ground rules were: H_s is not redefined, no certifier code is touched, new files only, `nice`, `OMP_NUM_THREADS=1`, `ulimit -v 3000000`, one process at a time, nothing pushed or sent. Category A means proved, or an exact certificate (a mod-p rank counts only as a one-sided bound). Everything else is labelled. The object is always the 35-component law vector; 36 appears only as dim V = dim E at s = 7. The Residual-vs-Resonant lock stays in force. Nothing here is a statement about Resonant Number Theory, T3, the packaging integers, TPC or RH.

## Bottom line
1. **Map 1: the closure statement is refuted (Category A).** For the 105 component functions f of the 35-component law vector, the functions x ↦ f(7x) do not lie in V. The rank of [F | F7] is **72 > dim V = 36 at all four primes**. By the preregistered rule this is a negative result: RTA's open weight-1 Fricke slash has no vector-valued form inside V at leading order. The branch is closed, and the lock stays.
2. **Map 1 controls.** The same test with dilation by each of the 24 other primes up to 97 gives rank 72 for 23 of them (refuted as well) and rank 36 at all four primes for one, **d = 29** (it closes). By the preregistered formula the specificity p would be (1 + 1)/25 = 0.08, which is moot because closure fails at 7. No specificity claim is made.
3. **Map 2: no refutation at any s.** For the ten odd s in {5, 9, 11, 13, 15, 17, 19, 21, 23, 25}, the exact lower bound for dim V_s equals 3·G(s(s−2)) exactly (never above, never below). The upper bound is certified, so dim V_s = 3·G(s(s−2)) is **Category A at s = 5, 9, 11, 13, 19, 25**, and **inconclusive at s = 15, 17, 21, 23** (the drafted orbit upper bound does not reach 3G; declared in the draft, not a failure).
4. **Cusp silence (Hom vanishing) is Category A at s = 5, 9, 11, 13, 19, 25**: Hom(V_s⊗χ^k, C_s) = Hom(C_s, V_s⊗χ^k) = 0 for all k in Z/12. At s = 15, 17, 21, 23 it was not attempted (no certified basis of V_s), so it is inconclusive there. The s = 7 anchor reproduces A35.
5. **V_s ≅ E_s** is mod-p evidence only (not Category A): at the six certified s a random mod-p intertwiner V_s → E_s is invertible. Not claimed as proved.
6. **New observation from the exact numbers:** V is *not* irreducible at s = 9, 11, 25 as far as the mod-p data show (End(V_s) ≤ 2 there), while End(V_s) = 1 (so V_s irreducible, Category A) at s = 5, 7, 13, 19. The draft's derived-unchecked cyclic-vector argument assumed irreducibility. It is supported at s = 5, 7, 13, 19 and open at s = 9, 11, 25.

## 1. Map 1 (run first)
**Statement tested** (prereg section 4, weight |7x|^{-1}, so no weight is free): V|W_7 ⊂ V if and only if V∘D_7 ⊂ V, where D_7 f(x) = f(7x).
**Data.** The 105 components K2_μ, K3_μ, K4_μ (μ in D, order 35) at the 216 rationals h/m (1 ≤ m ≤ 15, 1 ≤ h ≤ 3m, gcd = 1), exact Gauss means reduced mod p. Same four A51 primes, Lev = 3 531 528 000. For F7, each point x is replaced by 7x (or by d·x for a control d) and the fraction is reduced first. Statistic: r_p = rank over F_p of the 216 × 210 matrix [F | F_d].

| d | rank F | rank F_d alone | rank [F \| F_d] at p = 17 657 640 001 / 21 189 168 001 / 35 315 280 001 / 42 378 336 001 | verdict |
|---|---|---|---|---|
| **7** | 36 | 36 | 72 / 72 / 72 / 72 | **refuted** (72 > 36) |
| 29 (control) | 36 | 36 | 36 / 36 / 36 / 36 | closes |
| each of 2, 3, 5, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 (23 controls) | 36 | 36 | 72 / 72 / 72 / 72 | refuted |

- **Reproduction check.** rank F = 36 at all four primes, as in A51.
- **Why the verdict is exact.** If every f(7x) lay in V, the column space of [F | F7] on the 216 points would have dimension ≤ dim V = 36 (dim V = 36 is Category A: A35 and A51). A mod-p rank can only be lower than the characteristic-0 rank, so r_p = 72 proves the characteristic-0 rank is at least 72. Hence some component of V∘D_7 is not in V. Category A.
- **A little more, also exact.** V∘D_7 has dimension ≤ 36, so the sum V + V∘D_7 has dimension ≤ 72 and the evaluation rank is 72. So the sum is direct: **no nonzero element of V equals the dilation by 7 of an element of V**, as functions on the rationals.
- **Specificity p-value logic (prereg).** p = (1 + number of controls that close)/25 = 2/25 = 0.08 here. The minimum attainable value 1/25 = 0.04 needs closure at 7 and at no control. Closure fails at 7, so the decision rule gives "refute", the p-value gates only a specificity claim, and no such claim exists.
- **Outcome in the prereg's own list:** outcome 1 (refuted at 7: negative, RTA has no leading-order vector Fricke law inside V, the lock stays, the branch is closed). The drafter's prior (closure unlikely) is confirmed. A prior is not a result; the rank is.
- **Scope.** This concerns the leading 1/t profiles (the 35-component law vector). It says nothing about the t^{-1/2} terms, g_s coefficients, T3 or the Master Fricke samples. It does not contradict the scalar obstruction (Residual-Law A5); it extends the no-slash finding to the vector-valued law inside V.

### The control that closes (d = 29): descriptive, not preregistered
Dilation by 29 closes at all four primes with the same pipeline, so it is not a numerical accident of one prime. I did not look for an explanation beyond one scan (`data/posthoc_dilations.json`, first prime only, post-hoc, no p-value). Among all integers d from 1 to 210 the ones with rank 36 are **1, 29, 109, 149**; 157 values give 72, and the rest give intermediate ranks (45 to 66). So several dilations act with partial overlap. No structural reason is claimed. What can be said: closure at 29 is a fact about V and the dilation, and it is unrelated to 7. This is also why the preregistered control family was needed.

## 2. Map 2 (run second)
**What was run.** Odd s in {5, 9, 11, 13, 15, 17, 19, 21, 23, 25}, plus s = 7 as the anchor. For each s: A_s = [[2, s], [s, s]], n = s(s−2), the three families K2, K3, K4 built from a_s = (s/(2(s−2)), −1/(s−2)) and D_s (3n symbols).
- **Lower bound for dim V_s:** exact mod-p rank of the evaluation matrix of the orbit representatives at points x = h/m, m = 1, …, 24 (up to 540 points), at two primes ≡ 1 mod L·lcm(1..24). The rule stops at rank > 3G, at rank = number of representatives, or at m = 24.
- **Upper bound (drafted):** number of orbit representatives under the automorphs of A_s with all entries of absolute value ≤ 40 (U40). A supplementary, flagged upper bound uses all automorphs found with |a|, |c| ≤ 10^6 (U_ext).
- **Prediction tested:** dim V_s = 3·G(n), G(m) = ∏ over exact prime-power divisors q of m of (q+1)/2.
- **S,T-closure:** the symbol calculus must send every S and T image into the three families, plus mod-p spot checks of the S-law and T-law.
- **Items 3 and 4** (V_s ≅ E_s, Hom vanishing) use the A2 label representation on W_s (dim s(s−1), read-only import), E_s = span of the projection of δ_0, C_s its complement, mod a prime between 10^8 and 2^31.

| s | n | 3G(n) | lower bound (two primes) | U40 | U_ext | points used | dim V_s = 3G(n)? |
|---|---|---|---|---|---|---|---|
| 5 | 15 | 18 | 18 / 18 | 18 | 18 | 18 | **certified** |
| 7 (anchor) | 35 | 36 | 36 / 36 | 36 | 36 | 54 | **certified** (reproduces A51, A35) |
| 9 | 63 | 60 | 60 / 60 | 60 | 60 | 84 | **certified** |
| 11 | 99 | 90 | 90 / 90 | 90 | 90 | 96 | **certified** |
| 13 | 143 | 126 | 126 / 126 | 126 | 126 | 138 | **certified** |
| 15 | 195 | 126 | 126 / 126 | 168 | 168 | 540 | inconclusive (upper bound) |
| 17 | 255 | 162 | 162 / 162 | 216 | 216 | 540 | inconclusive (upper bound) |
| 19 | 323 | 270 | 270 / 270 | 270 | 270 | 288 | **certified** |
| 21 | 399 | 240 | 240 / 240 | 330 | 330 | 540 | inconclusive (upper bound) |
| 23 | 483 | 288 | 288 / 288 | 396 | 396 | 540 | inconclusive (upper bound) |
| 25 | 575 | 468 | 468 / 468 | 468 | 468 | 516 | **certified** |

- **Item 1, reading.** Nothing refuted: the lower bound never exceeded 3G. The formula d_Eis = 3G(n) was tested exactly where n is not squarefree: s = 9 (63 = 9·7), 11 (99 = 9·11) and 25 (575 = 25·23), all certified. **Correction to the draft:** the draft listed s = 15 and 21 as non-squarefree cases, but n = 195 = 3·5·13 and n = 399 = 3·7·19 are squarefree (only s itself is composite). All four inconclusive s (15, 17, 21, 23) have squarefree n divisible by 3, as does the certified s = 5 (n = 15), so the pattern of which s block the upper bound is not explained by squarefreeness; I do not claim an explanation.
- **At s = 15, 17, 21, 23** the lower bound equals 3G and stayed constant over at least 8 consecutive values of m (the rank first reached 3G at m = 11, 13, 16, 17 and did not move to m = 24, 540 points, more than the 168 to 396 representatives). That is finite-range evidence (Category B) that dim V_s = 3G, but it is not an upper bound, so the verdict is **inconclusive**, as declared. The supplementary closure bound (the S,T-closure of the automorph relation space, `supp53.py`) adds no relation at any s run, so it did not help. As a consistency check, at these four s the kernel of the evaluation matrix mod p (dimension 42, 54, 90, 108) is closed under the S and T matrices.
- **Item 2, S,T-closure.** At every s the symbol calculus maps all 3n symbols' S and T images into the three families (exact finite check). The S-law and T-law were spot-checked mod p at 5 symbols × 3 points per s (15 S-law and 15 T-law checks each), and all pass for one square root of n (the same root that makes (ST)^3 = S^2 hold). The laws are proved (Category A) for s = 7 in A35. For the other s I reused the A35 Poisson-summation proof verbatim (signature (1,1), |det| = n) without writing it out again, so closure of V_s is **Category A at s = 7 and, at the other s, a consequence of the same proof plus the passing spot checks** (not independently re-proved here). The generalization of the proof is a derived statement.

### Items 3 and 4 (only at s with a certified basis of V_s)
| s | dim W_s | dim E_s (mod p) | dim C_s | End(V_s) (mod p, upper bound) | Hom(V_s, E_s) | Hom(V_s⊗χ^k, C_s) and Hom(C_s, V_s⊗χ^k), all 12 k | Hom(V_s⊗χ^k, E_s), k ≠ 0 | V_s ~ E_s evidence |
|---|---|---|---|---|---|---|---|---|
| 5 | 20 | 18 | 2 | 1 | 1 | **0** | 0 | invertible element found |
| 7 | 42 | 36 | 6 | 1 | 1 | **0** | 0 | invertible element found |
| 9 | 72 | 60 | 12 | 2 | 2 | **0** | 0 | invertible element found |
| 11 | 110 | 90 | 20 | 2 | 2 | **0** | 0 | invertible element found |
| 13 | 156 | 126 | 30 | 1 | 1 | **0** | 0 | invertible element found |
| 19 | 342 | 270 | 72 | 1 | 1 | **0** | 0 | invertible element found |
| 25 | 600 | 468 | 132 | 2 | 2 | **0** | 0 | invertible element found |
| 15, 17, 21, 23 | | | | not run | | not run | | not run (no certified basis) |

- **Hom vanishing (Category A at the six new s).** Each mod-p Hom dimension is an upper bound for the characteristic-0 dimension, so a computed 0 is exact. This needs V_s to be given exactly: the representatives are a certified basis (lower bound = number of representatives), and S, T on them are the exact closed-form matrices reduced mod p. The unique root of n that makes the relations hold was used for both V_s and W_s (the same root). Both orientations of the V matrices (M and its transpose) were run and give identical numbers. Dimensions of E_s equal d_Eis = 3G(n), consistent with ledger entry 14.
- **So at s = 5, 9, 11, 13, 19, 25 the 35-component law vector's analogue (V_s) has no image in the cusp summand C_s, and no χ^k twist reaches it either.** The same holds at s = 7 (A35, reproduced).
- **V_s ≅ E_s: evidence only.** Hom(V_s, E_s) is nonzero mod p, dim V_s = dim E_s, and a random element of Hom(V_s, E_s) is invertible. That makes V_s ≅ E_s plausible and consistent with s = 7. It is not Category A: no exact cyclotomic lift of the intertwiner was attempted (as stated in prereg section 10.3). A failure could only be declared by an exact certificate, which was not attempted.
- **End(V_s) = 2 at s = 9, 11, 25.** This is an upper bound mod p. At s = 5, 7, 13, 19 End(V_s) = 1 mod p, which proves End = 1 in characteristic 0 (an upper bound of 1 with the identity present), so V_s is irreducible there (Category A). At s = 9, 11, 25 either V_s is irreducible and the mod-p value is accidental, or V_s splits into two non-isomorphic irreducible pieces. This was not resolved. Descriptively, these three s are those with n divisible by 9 or s a prime square; I make no claim about why.

### Even s
Not run. No d_Eis formula for even s exists in the ledger, so no prediction was made, and the lock on s in {7, 8, 11} is respected.

## 3. What this does and does not give
- **Gives (Category A):** (a) the leading-order vector Fricke closure fails: V∘D_7 ⊄ V, and in fact V ∩ (V∘D_7) = 0 on the rationals; (b) the exact module dimension 3·G(s(s−2)) at s = 5, 9, 11, 13, 19, 25 and the s = 7 anchor; (c) cusp silence (no map between V_s⊗χ^k and C_s) at those s; (d) irreducibility of V_s at s = 5, 7, 13, 19.
- **Gives (evidence only):** dim V_s = 3G at s = 15, 17, 21, 23 (finite-range lower bound, saturated, no certified upper bound); V_s ≅ E_s at the six s; the generalized S-law and T-law at spot points.
- **Preregistration outcome (section 6):** Map 1 refuted at 7 (negative, Category A). Map 2 not refuted at any s. The combination in section 6 reads: the Bridge C module structure extends over RTA's odd s-family (certified at six values, saturated lower bound at four more, no failure) but has no vector-valued Fricke form at leading order. That is the clean negative on Map 1 plus a generic positive on Map 2, as the draft anticipated. Map 2 alone can never be a link, so no link criterion is met and the Residual-vs-Resonant lock stays.
- **Does not give:** any statement about RTA's series coefficients, the t^{-1/2} terms, T3, 539, the packaging integers, Resonant Number Theory, or TPC/RH. Map 2 is generic by design and cannot single out any particular s.
- **Not preregistered, reported anyway:** that V_s is possibly reducible at s = 9, 11, 25, and the dilation d = 29 closing. Both are labelled descriptive.

## 4. Deviations and honesty notes
- **Implementation of the Gauss mean.** The exact finite mean uses a box of period 2m instead of the A51 period 4m (the integrand has period 2m, so the number is the same). The code is new wrapper code and matched A51's `Gp` on 28 test pairs with 0 mismatches before freezing. All this is in prereg section 10.
- **Disclosed pre-freeze runs** (s = 7 anchor validation only): see `AMENDMENTS.md`. No Map 1 statistic and no s ≠ 7 quantity was computed before the hash.
- **Post-freeze additions** (supplementary closure bound, kernel check, invertibility of the mod-p intertwiner, the post-hoc dilation scan): `AMENDMENTS.md`, addenda 1 to 4. None changes a preregistered verdict. The invertibility check is stronger than the prereg's "nonzero intertwiner of equal dimensions".
- **Upper bound at s = 15, 17, 21, 23.** The drafted orbit bound (automorphs with entries ≤ 40) and the extended search (|a|, |c| ≤ 10^6) both give the same, too large, count. So the verdict is inconclusive by the draft's own rule, and I did not weaken the rule.
- **Mod-p dimensions.** Used as one-sided bounds only (lower bound by rank, upper bounds for Hom by dimension). No floating point is involved anywhere in these results.
- **The derived-unchecked items from the draft** (items 7 to 9 of section 2: RTA's series sees the characteristic a, cyclic vector, Z/3 from the mod-2 block structure) were not tested by these maps. The only bearing is on item 8, which assumes irreducibility: supported (Category A) at s = 5, 7, 13, 19, open at s = 9, 11, 25.

## 5. Files (all in `SF/A53_RTA_maps/`)
- `prereg.md`, `prereg.sha256`, `AMENDMENTS.md`, `REPORT.md`, `REPORT.pdf`, `mk_pdf.py`.
- `scripts/`: `lib53.py` (general-s symbol calculus, automorphs, evaluator), `map1.py`, `map2.py`, `stagec.py`, `hom53.py`, `run_map2.sh`, `validate_s7.py`, `supp53.py`, `posthoc_dilations.py`, `SHA256SUMS`.
- `data/`: `map1_results.json` (every rank, every prime, every dilation), `map2_s{5,...,25}.json` (rank histories, Hom tables, spot checks), `supp_*.json`, `posthoc_dilations.json`, `prefreeze_validation_s7/`.
- `logs/`: `map1.log`, `map2.log`, supplementary logs.
