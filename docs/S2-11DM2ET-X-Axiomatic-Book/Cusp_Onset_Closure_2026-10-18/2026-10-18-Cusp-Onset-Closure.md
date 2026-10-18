> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** W here = the Eisenstein space (Master: V_Eis, d_Eis). The function W_2(k,u) is written d_2(k,v) on Master, with v the odd part of 2t(t−1). cert_W_5_6_7_8.json does not certify d_Eis at s = 5, 7, 8 and is not used. Uncertified (floating) entries are Cat B. Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# Cusp-Onset — Closure (Path A follow-up: A1–A4, with Cross-Review N2, N3, N9, C13)

Date: 2026-10-18, written about 13:49 CDT. Local only; nothing pushed. Builds on `2026-10-18-Cusp-Onset.md` and uses `2026-10-18-Cross-Review.md`.

Labels:
- **Cat A** = exact or proved.
- **Cat B** = numerical, conjectural, a pattern on finitely many cases, or citation only.
- No TPC/RH claims.

**C13 relabelling.** The floating-point (SVD/FFT) ranks and verdicts in `2026-10-18-Cusp-Onset.md` and `Paths-A-B-C.md` are **Cat B**. This report replaces them, where possible, with exact integer-matrix ranks, exact orbit bounds and certified local counts (§3). Only those replacements are Cat A.

Scripts and data: `2026-10-18-Cusp-Onset-Closure/`. Key files are listed in §6.

## 0. Status at a glance

| Item | Result | Status |
|---|---|---|
| **A1** Closed criterion for a cusp part in u_L | Coprime part is Eisenstein ⇔ σ acts trivially on Ḡ = G/(S+⟨j⟩), i.e. H̄ = 1 | **A** (reduction) |
| A1, odd s with c = 1 | Eis ⇔ h(Q(√(s(s−2)))) = 2^{ω(s)}. Number of non-genus characters = φ(s−2)(h − 2^{ω(s)}) | A given the ambiguous-class count \|Ḡ^σ\| = 2^{ω(s)}φ(s−2). That count is B in general (verified at every tested s) |
| A1 against all computed s | Matches at every s with a complete coprime part (§1.3). This includes the Cross-Review counterexamples 14, 17, 18, 22, 23 (all CUSP, H̄ = 2) and **s = 18, newly complete at B = 150000** | A per s (exact finite computations) |
| A1 vs N3 sectors | The N3 local sectors do **not** decide the u_L verdict. Family cusp > 0 at 5, 7, 13, 15, where u_L is Eisenstein. The decision is class-group data (H̄) | A (table §1.4) |
| **A2** γ on L′/Z² | γ ≡ (s−1)·I on all of L′/Z². Proof: (γ − (s−1)I)A⁻¹ = [[0,−1],[1,0]] | **A** (new short proof of N3's scalar statement) |
| A2 dim V ≤ orbit bound | s(s−1) (odd), (s/2)(s/2+1) (even) | **A** (Burnside, §2.1) |
| A2 dim V exact | Certified for **every s = 5..51 and s = 72** (exact rational rank = upper bound) | **A per s** |
| A2 dim V = s(s−1) for all odd s | Holds at all 24 odd s ≤ 51. No general proof of the lower bound | B for general s |
| **N9** gap at s = 2m² | Mechanism found: γ has a rational square root g = (γ+I)/(2m) in SO(A)(Q) **iff s = 2m²**. Splitting cones at g gives a new exact upper bound with gap exactly m(m−1) at m = 2..7. It equals the exact lower bound at m = 2..6 (s = 8, 18, 32, 50, 72). At m = 7 the lower bound is 2 short | Mechanism and bound **A**. Gap = m(m−1) for all m is B |
| s = 98 | Upper bound 2408 (gap 42 = 7·6). Exact lower bound **2406, unchanged at Q = 40, 70 and 130** (50326 modes). The true value is probably 2406 (gap 44), so the half-cone bound would not be tight at m = 7 | **Not certified** (B). Gap = m(m−1) is confirmed only for m ≤ 6 |
| A2 dim W, odd s | 3∏_{p^e ∥ s(s−2), p odd}(p^e+1)/2 | A modulo one numerically checked conjugacy (§2.3) |
| A2 dim W, even s | W₂(k,u)·∏(p^e+1)/2, with W₂ = 2^{k−1} + {4, 6, 5} | A for k ≤ 5 (covers every even s ≤ 62; s = 64 already has k = 6). k ≥ 6: B (lower bounds only) |
| **A4** Exact V, W, cusp = V − W | Table §3, s = 5..51 and 72 | A per s (W as in the two rows above) |
| **A3** Deep bad-prime parts at s = 9, 16, 24 (and 18) | All tested c-parts are complete and genus-pure at 9, 16, 24. At s = 18 the coprime part is non-pure, so CUSP. Structure: every T_𝔠 is a union of S-cosets | A per tested c-part. Reduction lemma (§4) A given the S-invariance, which is B in general |

## 1. A1 — the closed criterion

### 1.1 Reduction (Cat A, from the earlier part of this session)
Notation:
- G = Cl⁺_{M∞₁∞₂}, the narrow ray class group mod M, with M = 2dc and d = 2(s−2).
- T ⊂ G is the E-class set of u_L's coprime part.
- S = Stab(T). T is a single S-coset.
- j = [M−1] = [−1], of order 2.
- Ḡ = G/(S + ⟨j⟩), H = (1−σ)G, H̄ = image of H in Ḡ.

**Criterion.** The coprime part is Eisenstein (genus-pure) ⇔ (1−σ)Ḡ ⊆ {0, x̄}, where x̄ = σk̄ − k̄. In every complete case x̄ = 0, so the criterion is **Eis ⇔ H̄ = 1 ⇔ σ acts trivially on Ḡ**. Then the number of non-genus pure characters is |Ḡ| − |Ḡ^σ|.

### 1.2 Odd s, c = 1 (s(s−2) squarefree)
- |Cl⁺_{(s−2)∞∞}| = 2hφ(s−2), hence |Ḡ| = hφ(s−2). This is Cat A, with proof sketch:
  - E = ⟨−1, ε⟩, where ε = s−1+√(s(s−2)) is fundamental;
  - [E : E⁺_{m,1}] = 2m;
  - φ_K(m) = mφ(m), since every p | m ramifies.
- |Ḡ^σ| = 2^{ω(s)}φ(s−2). Verified in `gbar_arith_5_43.json` at all tested s; a general proof needs a Chevalley-type ambiguous-class count (Cat B).
- Hence: **Eis ⇔ h = 2^{ω(s)}**, and #non-genus characters = φ(s−2)(h − 2^{ω(s)}).
- `predict_c1.json`, s ≤ 121, class numbers certified by bnfcertify: **Eis only at s = 5, 7, 13, 15.**
- Confirmed by exact runs at:
  - 17 (16), 19 (32), 21 (72), 23 (24), 31 (112), 33, 35, 37, 39, 41 (240);
  - new runs at 53 (320), 55 (208), 57 (160). These have incomplete coverage, but the counts match.
- N3 link (Cat A): for c = 1 and odd s, M = 4(s−2). So no prime p | s divides the modulus (`n3_vs_uL.json`, column `primes_of_s_in_M`). u_L's cusp characters are unramified at every p | s, which is exactly the N3 sector where γ ≡ −1.

### 1.3 Verdicts against all computed s

| s | H̄ | criterion | exact verdict | coverage |
|---|---|---|---|---|
| 5, 7, 13, 15 | 1 | Eis | Eis | complete |
| 9 | 1 | Eis | Eis (coprime part plus 29 deep 3-parts, §4) | complete per part |
| 16, 20, 24 | 1 | Eis | Eis (16 and 24 via deep runs at B = 30000; 20 at Nmax 80000) | complete per tested part |
| 14, 17, 22, 23, 19, 21 | 2 | CUSP | CUSP | complete |
| **18** | 2 | CUSP | **CUSP**: coprime part complete at B = 150000 (G = 2048), \|T\| = 32, not genus-pure | complete (new, `deepB/s18big/`) |
| 25, 29 | 3 | CUSP | CUSP (88 and 72 non-genus characters, Nmax 80000) | complete |
| 31, 33, …, 41, 53, 55, 57 | > 1 | CUSP | CUSP, counts as predicted | complete, or incomplete with matching counts |
| 32, 34, 36, 40 | 2 | CUSP | not yet complete | **open** (prediction only) |

### 1.4 The Cross-Review counterexamples vs N3 sectors (`n3_vs_uL.py/.json`)
Cross-Review C11 found that the "h⁺ vs genera" rule fails at s = 14, 17, 18, 22, 23. Every one of these has H̄ = 2, and the criterion and the exact verdict agree (CUSP).

N3's local sector model governs the **family** cusp space V − W. That space is non-zero at every odd s ≥ 5, including 5, 7, 13, 15, where u_L is Eisenstein:

| s | family cusp (exact) | u_L |
|---|---|---|
| 5 | 2 | Eis |
| 7 | 6 | Eis |
| 13 | 30 | Eis |
| 15 | 84 | Eis |
| 14 | 8 | CUSP |
| 17 | 110 | CUSP |
| 18 | 24 | CUSP |
| 22 | 24 | CUSP |
| 23 | 218 | CUSP |

So the counterexamples **do not fit** a purely local sector explanation. Whether the single vector u_L ∈ V meets the cusp space is a class-group question, H̄ ≠ 1, layered on top of the local structure. Status: A for the table; the interpretation is B.

## 2. A2 — dimensions

### 2.1 γ is a scalar on L′/Z² (Cat A; proves N3's first claim for all s)
Set N := γ − (s−1)I = [[−s,−s],[2,s]]. Then:
- N² = s(s−2)·I;
- **N·A⁻¹ = [[0,−1],[1,0]]**, by direct multiplication with A⁻¹ = −(1/(s(s−2)))[[s,−s],[−s,2]].

So N maps L′ = A⁻¹Z² into Z², i.e. **γ acts on L′/Z² as multiplication by s−1**.

On a p-part with p odd: p divides exactly one of s and s−2, so s−1 ≡ +1 (if p | s−2) or −1 (if p | s) mod p^e. On the odd parts of the odd-s group Δ = L₀′/L₀ the same holds, because those parts agree with L′/Z².

Consequences, by Burnside over ⟨γ, −1⟩ (where −R acts trivially):
- |Fix γ| = 2(s−2), |Fix(−γ)| = 2s, |Δ[2]| = 4;
- **#orbits = s(s−1) for odd s and (s/2)(s/2+1) for even s.** This is an exact upper bound on dim V (Cat A).

### 2.2 Exact lower bound and certification (N2) — Cat A per s
`vrank.py` forms the integer matrix N_O(q), counting points of orbit O at norm q in the four cones, and computes its exact rational rank with flint's `fmpz_mat.rank`. No floating point is involved, so rank ≤ dim V exactly.

**Rank = upper bound at every s = 5..51 and at s = 72.** For s = 8, 18, 32 and 50 the upper bound used is the half-cone bound of §2.4. This replaces the requested mod-ℓ certification with a stronger rank over Q.

- s = 5..25: Qmax 40.
- s = 26..34: Qmax 30.
- s = 35..49: Qmax 45.
- s = 50: Qmax 20 and 60 (both give 630).
- s = 51: Qmax 45. Qmax 20 had given 2491, which shows that the earlier "short by 59" was truncation.
- s = 72: Qmax 20.

**Odd s: dim V = s(s−1) at all 24 odd s ≤ 51.** A general proof of the lower bound is open (B).

### 2.3 dim W
**Odd s.** The family representation is conjugate to the Weil representation ρ_{L₀} of L₀ = {n₂ even}.

The intertwiner is M[(α,β),γ] = e(B(γ,β)) for γ ∈ α + {0, e₂} + L₀. It comes from the exact lattice decomposition α + Z² = ⊔_ε (α + εe₂ + L₀). Numerically:
- S_fam M = M S_{L₀} and T_fam M = M T_{L₀} to 1e−15;
- cond(M) = 1, i.e. M/√2 is unitary;
- M⁻¹c = δ₀.

This holds at s = 5, 7, …, 21 (`weil_L0_5_21.log`). Because it is a floating check, this step is **Cat B**. The rest is exact:
- Δ₂ ≅ A₁(ε)², giving W₂ = 3 (certified).
- Odd Δ_p is cyclic, giving W_p = (p^e+1)/2. Hand proof for e = 1; exact certification for p^e = 9, 25, 27, 49, 81, 121, 125, 169 (`local_weil.json`).
- The Weil representation of an orthogonal sum is the tensor product of the local ones (standard).

So **dim W = 3∏(p^e+1)/2**: A modulo the conjugacy step, for every odd s whose p^e with e ≥ 2 lie in the certified list. That covers every odd s ≤ 51.

**Even s.** The family is literally the Weil representation of L′/Z² (exact identity of the code's S and T matrices). A ≅ [2] ⊕ [−2t(t−1)] with t = s/2, so Δ₂ = A₁ ⊕ C_{2^k}(u). W₂ is:
- 2^{k−1} + 4 for k even;
- 2^{k−1} + 6 for k odd, u ≡ 1 mod 4;
- 2^{k−1} + 5 for k odd, u ≡ 3 mod 4.

This is certified exactly for k ≤ 4 (all u) and k = 5 (u ≡ 1, 3, 5, 7 mod 8, which is all classes); see `exact_local2_*.json` and `local_weil.json`. For k = 6..9 only exact lower bounds are available (36, 69/70, 132, 261/262), so the general formula is **B**. Every even s ≤ 62 has k ≤ 5. The first exception is s = 64 (k = 6).

**The older mod-ℓ Krylov file** `cert_W_5_6_7_8.json` did not certify W at s = 5, 7, 8 (Cross-Review C13). It is superseded by the local computation above and is no longer used.

### 2.4 N9 — the s = 2m² gap, explained (`n9_halfcone.py`, `n9_halfcone_*.json`)
- **Fact (Cat A).** γ ∈ SO(A)(Z) has a square root g ∈ SO(A)(Q) with det g = 1 iff tr γ + 2 = 2s is a perfect square, i.e. **s = 2m²**. Then g = (γ+I)/(2m) = [[0,−m],[1/m,2m]], with gᵀAg = A and g² = γ (checked exactly at s = 8, 18, 32). In unit language: ε_s = η² with η = m + √(m²−1).
  - Square roots with det −1 occur at s = 2m²+2 (10, 20, 34, …). V is full there, which is consistent with the earlier observation that a unit power alone is not the cause.
- **Exact upper bound (Cat A).** Split each cone [r, γr) as [r, gr) ⊔ g[r, gr), for r = e₁ and r = f. Then every coset theta is a 0/1 combination of half-cone thetas h_r(y) over cosets of Λ = Z² ∩ g⁻¹Z² = mZ ⊕ Z. Treating the h_r(y) as free symbols can only over-count, so the rank of the incidence matrix is an exact upper bound for dim V.

| s = 2m² | m | orbit bound | half-cone upper bound | exact lower bound (vrank) | gap | dim V |
|---|---|---|---|---|---|---|
| 8 | 2 | 20 | **18** | 18 | 2 | **18 (A)** |
| 18 | 3 | 90 | **84** | 84 | 6 | **84 (A)** |
| 32 | 4 | 272 | **260** | 260 | 12 | **260 (A)** |
| 50 | 5 | 650 | **630** | 630 (Q20, Q60) | 20 | **630 (A)** |
| 72 | 6 | 1332 | **1302** | 1302 (Q20) | 30 | **1302 (A)** |
| 98 | 7 | 2450 | **2408** | 2406 (Q40, Q70, Q130) | 42 (upper) / 44 (lower) | 2406–2408 (not certified) |

**Explanation.** When s = 2m², the "half-period" automorph g makes the half-cone thetas common building blocks of several orbit thetas. This produces exactly m(m−1) extra linear relations. The s = 8 relations found earlier, N_{O12} = N_{O7} + N_{O9} and N_{O2} = N_{O15} + N_{O19}, are instances. The Cross-Review's "extra isotropic vector" guess is replaced by this concrete mechanism.

- The gap equals m(m−1) **exactly** in the upper bound for m = 2..7 (A per m).
- A closed proof that the gap is m(m−1) for all m is open (B).
- s = 98: the half-cone upper bound gives gap 42, matching m(m−1). The exact lower bound is 2406 at Q = 40, 70 and 130 (`vrank_98_q*.log`, the last finished at about 13:50 CDT), so the truncation explanation now looks unlikely.
  - Most likely dim V(98) = 2406. That would mean two further relations not captured by the half-cone mechanism; possibly 7 | m and 49 | s matter.
  - **So "gap = m(m−1)" is certified only for m = 2..6. At m = 7 the gap is 42 or 44 (open, B).**

## 3. A4 — exact V, W, cusp (`certified_table.py` → `certified_table.json`)
- V: exact (lower = upper).
- W: local formula; certified local factors at every s listed.
- Cusp = V − W.

All entries are **Cat A per s**, except that W at odd s inherits the floating conjugacy check of §2.3 (B for that one step).

| s | V | W | cusp | | s | V | W | cusp |
|---|---|---|---|---|---|---|---|---|
| 5 | 20 | 18 | 2 | | 6 | 12 | 12 | 0 |
| 7 | 42 | 36 | 6 | | 8 | 18 | 18 | 0 |
| 9 | 72 | 60 | 12 | | 10 | 30 | 30 | 0 |
| 11 | 110 | 90 | 20 | | 12 | 42 | 36 | 6 |
| 13 | 156 | 126 | 30 | | 14 | 56 | 48 | 8 |
| 15 | 210 | 126 | 84 | | 16 | 72 | 48 | 24 |
| 17 | 272 | 162 | 110 | | 18 | 84 | 60 | 24 |
| 19 | 342 | 270 | 72 | | 20 | 110 | 90 | 20 |
| 21 | 420 | 240 | 180 | | 22 | 132 | 108 | 24 |
| 23 | 506 | 288 | 218 | | 24 | 156 | 120 | 36 |
| 25 | 600 | 468 | 132 | | 26 | 182 | 126 | 56 |
| 27 | 702 | 546 | 156 | | 28 | 210 | 168 | 42 |
| 29 | 812 | 630 | 182 | | 30 | 240 | 144 | 96 |
| 31 | 930 | 720 | 210 | | 32 | 260 | 126 | 134 |
| 33 | 1056 | 576 | 480 | | 34 | 306 | 198 | 108 |
| 35 | 1190 | 432 | 758 | | 36 | 342 | 270 | 72 |
| 37 | 1332 | 684 | 648 | | 38 | 380 | 300 | 80 |
| 39 | 1482 | 798 | 684 | | 40 | 420 | 270 | 150 |
| 41 | 1640 | 882 | 758 | | 42 | 462 | 240 | 222 |
| 43 | 1806 | 1386 | 420 | | 44 | 506 | 288 | 218 |
| 45 | 1980 | 990 | 990 | | 46 | 552 | 432 | 120 |
| 47 | 2162 | 1080 | 1082 | | 48 | 600 | 288 | 312 |
| 49 | 2352 | 1800 | 552 | | 50 | 630 | 312 | 318 |
| 51 | 2550 | 1350 | 1200 | | 72 | 1302 | 540 | 762 |

Agreement with Cross-Review N3: 72 (s = 19), 132 (s = 25) and 758 (s = 41) are reproduced. The family cusp vanishes only at s = 6, 8, 10 in this range.

## 4. A3 — deep bad-prime parts (`deepB/`, `deep_translate.py/.json`)
`deep_cparts.py` enumerates only ν whose c-part is exactly 𝔠, using an exact matsolvemod lattice solve. It checks that every class of G is observable (completeness) and tests genus-purity exactly. For two split primes, σ swaps (e₁,e₂) ↔ (e₂,e₁) and maps T to σT, which preserves the purity verdict, so only e₁ ≤ e₂ is run.

| s | prime | c-parts tested | B | complete | genus-pure |
|---|---|---|---|---|---|
| 9 | 3 (split) | 29: all (e₁,e₂) with e₁ ≤ e₂ ≤ 7, plus 𝔠 = 1 | 3000 | all | all |
| 9 | 2, 7 | 𝔠 = 1 only (no other parts occur) | 3000 | yes | yes |
| 16 | 2 | 𝔠 = 1 and 𝔭₂ | 30000 | all | all |
| 16 | 7 | 𝔠 = 1 | 30000 | yes | yes |
| 24 | 2 | 15 parts, exponents up to 8. The main run also lists (1,12) and (12,1), which were not tested | 30000 | all | all |
| 24 | 11 | 𝔠 = 1 | 30000 | yes | yes |
| 18 | 3 | 𝔠 = 1, 𝔭₃^{1..4} | 30000 | no (G = 2048) | 3-parts pure; coprime part **non-pure** |
| 18 | coprime | 𝔠 = 1 | **150000** | **yes** | **no**, so CUSP |

At B = 4000 the s = 16 and 24 runs were incomplete. Their "non-pure" flags were artifacts of the missing classes, and they disappear at B = 30000.

Mixed c-parts (two different bad primes at once) were not enumerated. The main runs at Nmax 20000 and 80000 show none at s = 16 and 24.

**Structure (Cat B, verified on every tested c-part at 9, 16, 18, 24).** Every T_𝔠 is a union of cosets of S₀ = Stab(T_∅), and T_∅ is a single S₀-coset. The T sets depend on 𝔠 only through a finite periodic pattern; at s = 9 there are 13 distinct sets among 29 parts, e.g. (1,1) ~ (1,7) ~ (3,5) ~ (7,7). So they are not literally equal across exponents, but they are translates or unions of translates.

**Reduction lemma (Cat A, given the S-invariance).** Suppose H̄ = 1 (i.e. H ⊆ S + ⟨j⟩) and T_𝔠 is S-invariant. Then f_𝔠 = (1+σ)(1+j)1_{T_𝔠} is H-invariant. Proof:
1. (1+j)1_{T_𝔠} is (S+⟨j⟩)-invariant, hence H-invariant.
2. σH = H, because σ(g − σg) = −(g − σg). So composing with σ preserves H-invariance.

Hence **every c-part is genus-pure and u_L is Eisenstein**: deep bad primes cannot create a cusp part when the coprime criterion says Eis. Conversely, if H̄ ≠ 1 the coprime part already gives CUSP.

So the full u_L verdict is decided by the coprime criterion of §1, provided T_𝔠 is S-invariant for all 𝔠.
- Likely proof of the S-invariance: S is realised by multiplication by λ ≡ 1 on the coset lattice, coprime to M. Such λ preserves c-parts.
- This proof is **not** written out, so the general statement stays Cat B. The verdicts at s = 9, 16, 24 are exact on the tested parts (A per part), and Eis overall is Cat B because there are infinitely many parts.

## 5. Open items
1. A general proof of dim V = s(s−1) for odd s (lower bound) and of the even-s formula. Certified only up to s = 51, plus s = 72.
2. N9 for general m. The gap is exactly m(m−1) for m = 2..6. At s = 98 the bounds 2406 ≤ dim V ≤ 2408 do not meet, and the lower bound has been stable from Q = 40 to 130, so find the two missing relations or prove they are absent.
3. W₂ for k ≥ 6, where 2^k ∥ 2t(t−1) and t = s/2 (first case s = 64): exact lower bounds only.
4. An exact (non-floating) check of the odd-s Weil conjugacy; currently 1e−15 at s ≤ 21.
5. The ambiguous-class count |Ḡ^σ| = 2^{ω(s)}φ(s−2) in general.
6. S-invariance of T_𝔠 in general (§4).
7. Complete coverage at s = 32, 34, 36, 40 (predicted CUSP).

## 6. Files (all under `2026-10-18-Cusp-Onset-Closure/`)
- **Criterion:**
  - `uL_rayclass_exact.py` (with `crit`), `summarize_rc.py`;
  - `uL_rayclass_{5..44}_M1.json`, `big/uL_rayclass_{9,20,25,29,32,34,36,40}_M1.json`, `new/` (s = 53, 55, 57);
  - `gbar_arith.py/.json`, `predict_c1.py/.json`, `conductor.py`;
  - `n3_vs_uL.py/.json`.
- **Dimensions:**
  - `burnside_V.py/.json`, `orbits_V.py`, `vrank.py`;
  - `vrank_*.json/.log` (5–51, 72, 98), `batch_vrank35_50.sh`;
  - `n9_halfcone.py`, `n9_halfcone.json` (s = 8, 18, 32), `n9_halfcone_8_18_32_50_72_98.json`, `gamma_scalar_proof.py/.txt` (§2.1 and the s = 2m² square root, symbolic);
  - `weil_L0.py`, `weil_L0_5_21.log`;
  - `local_weil.py/.json`, `exact_local2.py` + logs/JSON, `lower_2adic.py/.json/.log`;
  - `certified_table.py/.json`;
  - superseded: `cert_rank.py`, `cert_W_5_6_7_8.json`, `affine_sym.py`, `scalar_sym.py`, `kron_test*.py`.
- **Deep parts:**
  - `deep_cparts.py`, `deep9.log`;
  - `deepB/` (B = 30000 runs, `deep_cparts_s{9,16,18,24}_p*.json`);
  - `deepB/s18big/` (s = 18 coprime part, B = 150000);
  - `deep_translate.py/.json`.

