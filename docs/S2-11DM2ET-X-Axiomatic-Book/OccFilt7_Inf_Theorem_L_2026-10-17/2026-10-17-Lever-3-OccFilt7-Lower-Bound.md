# Lever 3: a lower bound for |g_7(d)| (OccFilt_7(∞)), 2026-10-17

Object: g_7(q) = Σ_{n≥0} q^{n²}/(−q^7;q^7)_n, with coefficient g_7(d) = Σ_n φ_n((d−n²)/7) and φ_n(m) = [x^m] ∏_{j≤n} 1/(1+x^j).
Target: OccFilt_7(∞), i.e. g_7(d) ≠ 0 for every d > 247 with d mod 7 ∈ {0,1,2,4}.
Scripts and data: `./2026-10-17-Lever-3-OccFilt7-Lower-Bound/`

**Status (rev 2, 2026-10-17 evening): Theorem L / OccFilt_7(∞) = {0,1,2,4} — Cat A (computer-assisted), audited once.** See "Lemma L — route 3", "Independent audit of Theorem L" and "Post-audit patches (rev 2)". The first-pass verdict below is kept for the record.

**First-pass verdict (superseded): (b), a conditional reduction, strongly supported by numerics.** There is no full proof, so no proved D0.
OccFilt_7(∞) reduces exactly to a comparison of two power series whose coefficients are all non-negative (Cat A). The missing piece is one explicit inequality, Lemma L below.
The numerics rule out the ADH-type scenario (c).

## Two corrections to the brief

1. **The coefficients of g_7 are not small for large d.** They are small only for d ≲ 300.
   - |g_7(d)| grows like exp(0.3985·√d): about 10^14 at d=10^4, 10^51 at 10^5, and 10^169 at 10^6.
   - The small, sparse picture comes from the d ≤ 3000 window.
2. **The coefficients of (x;x²)_∞ = 1/(−x;x)_∞ are not small or sparse.**
   - Each one equals (−1)^m · A000700(m), where A000700(m) counts partitions of m into distinct odd parts.
   - Its size is about exp(π√(m/6)) / (2^{7/4} 3^{1/4} m^{3/4}). This asymptotic is quoted from the OEIS A000700 formula section, which has no theorem number, so I treat it as a citation only.
   - The coefficients of 1/(−x;x)_n are also unbounded.

## 1. Numerics (Cat B unless marked)

| range | method | rigor | zeros in allowed classes |
|---|---|---|---|
| d ≤ 10^6 | exact big integers (`exact.py`) | exact | the known 24, last 247 |
| d ≤ 10^7 | exact recurrence mod 2 primes near 2^62 (`g7mod.c`) | **rigorous nonvanishing**: g ≢ 0 mod p ⇒ g ≠ 0 | the known 24, last 247 |

- So g_7(d) ≠ 0 for all allowed 247 < d ≤ 10^7. This is a certified computation (A-level fact, computational).
- The modular code was cross-checked against exact values for d ≤ 6000.
- The long-double column in `g7mod` is **not** reliable past about 10^5 because rounding error accumulates. It is not used for any claim.

Growth. A fit of log|g| = c√d + b·log d + e over 2000 < d ≤ 10^6, per residue class mod 14, gives c = 0.39850 to 0.39856 and b ≈ −0.5 in every class (`data/stats_exact_1e6.txt`).

Largest and smallest |g_7(d)| in each window (window from `stats_exact.py`):

| window | max log10\|g\| | min nonzero \|g\| (class: value @ d) |
|---|---|---|
| 248–10^3 | 2.3–3.6 | c0: 2 @756; c1: 2 @414; c2: 2 @268; c4: 20 @263 |
| 10^3–10^4 | 14.3–14.65 | c0: 18 @1134; then increasing |
| 10^4–10^5 | 51.3–51.6 | about 10^14.3–10^14.6 at the window's left end |
| 10^5–10^6 | 169.1–169.4 | about 10^51 at the window's left end |

- **Signs.** Past the last sign change in each class, the sign is fixed per residue mod 14:
  - sign g_7(d) = −(−1)^d in every class;
  - last sign change: class 0 at d = 1127/1134, class 1 at 407, class 2 at 247, class 4 at 60.
- **Class weights.** Class 0 runs at about ½ the size of classes 1, 2, 4. This matches #{n mod 7 : n² ≡ d}, which is 1 for class 0 and 2 for the others.
- **No dominant single n.** Many n contribute; the terms form two smooth bell-shaped profiles (even n and odd n) of opposite sign (see §2).

## 2. Analysis

### Cat A (proved here; elementary, also machine-checked)

**A1. Positivity.** For all n, m:

(−1)^m φ_n(m) = a_n(m) := [x^m] ∏_{odd j≤n}(1+x^j) · ∏_{k=⌊n/2⌋+1}^{n} (1−x^{2k})^{−1} ≥ 0.

*Proof.* Put y = −x and use 1/(1+y^j) = (1−y^j)/(1−x^{2j}).
- The numerator is ∏_{j≤n}(1−y^j) = ∏_{odd j}(1+x^j) · ∏_{k≤⌊n/2⌋}(1−x^{2k}).
- The second factor cancels the first ⌊n/2⌋ factors of ∏_{j≤n}(1−x^{2j}). ∎

So a_n(m) counts pairs (S, λ) of total size m, where:
- S is a set of distinct odd parts ≤ n;
- λ is a partition into even parts 2k with n/2 < k ≤ n.

This was checked exactly for n ≤ 60, m ≤ 3000.

**A2. Splitting.** Since (−1)^{(d−n²)/7} = (−1)^{d+n}:

(−1)^d g_7(d) = E_d − O_d, with E_d = Σ_{n even} a_n((d−n²)/7) ≥ 0 and O_d = Σ_{n odd} a_n((d−n²)/7) ≥ 0.

Equivalently g_7(−q) = E(q) − O(q), where E = Σ_k T_{2k}, O = Σ_k T_{2k+1}, and

T_n(q) = q^{n²} (−q^7;q^{14})_{⌈n/2⌉} / (q^{14(⌊n/2⌋+1)};q^{14})_{⌈n/2⌉}.

Each T_n has non-negative coefficients. This was checked exactly for d ≤ 10^5.

**A3. Ladder identities.**
- T_{2k+1} = T_{2k} · q^{4k+1}/(1−q^{14k+7})
- (1+q^{14k+14}) · T_{2k+2} = q^{4k+3} · T_{2k+1}

So, coefficientwise, E_d ≤ O*_d := Σ_{n odd} a_n((d−(n+1)²)/7) for d ≥ 1. This was checked for d ≤ 10^5 with no violations.

**A4. Reduction.** OccFilt_7(∞) holds if O_d > E_d for every allowed d > D0, and the finite range ≤ D0 is checked.
- Already proved by computation: O_d > E_d exactly for every allowed d in (1127, 10^6].
- The last d with E_d ≥ O_d is 1127 (class 0), 407 (class 1), 247 (class 2), 60 (class 4).
- g_7 ≠ 0 is certified up to 10^7.
- **So any proof of Lemma L with D0 ≤ 10^7 closes OccFilt_7(∞) with no further computation.**

### The missing lemma

**Lemma L (open).** There are explicit η > 0 and D0 ≤ 10^7 such that E_d ≤ (1−η)·O_d for every allowed d ≥ D0.

A sufficient variant, by A3, is **L\***: O*_d ≤ (1−η)·O_d for d ≥ D0.
- Numerically O*_d < O_d for all allowed d > 2738.
- O*/O → 0.8392 at d = 10^5.

L and L* compare sums of non-negative terms. Unlike the original problem, nothing inside E or O cancels. The natural proof route is an effective saddle-point or Wright-type circle-method estimate for the two positive Nahm-type sums E and O, with explicit error constants. This is laborious but standard in kind. I did not carry it out.

### Cat B (heuristic saddle-point analysis, matched to numerics)

Let y ∈ (0,1) be the root of **y^7 + y^2 = 1**, so y = 0.8398331470. Set:
- u0 = −(7/2) ln y = 0.6109321448
- V = (π²/6 − Li2(y^7))/4 − u0²/7 = 0.2779597702

Predictions against measurements:

| quantity | predicted | measured |
|---|---|---|
| growth exponent c = 2√(V/7) | **0.3985400** | fitted 0.39850–0.39856 |
| E_d/O_d → (1−√(1−y²))/y | **0.5443407** | 0.54451 @10^5, 0.544396 @10^6 (gap shrinks like d^{−1/2}) |
| O*/O → y | 0.83983 | 0.839152 @10^5 |
| E/O* → 1/(1+y^{7/2}) | 0.648153 | 0.648886 @10^5 |

Mechanism: at the saddle n ≈ u0/ε, the term ratio T_{2k+1}/T_{2k} = q^{4k+1}/(1−q^{14k+7}) tends to y/(1−y^{7/2}) ≈ 1.8365 > 1. So odd n beat even n by a fixed factor, and the alternating sum loses only a constant factor. It cannot cancel to zero.

### The ADH σ(q) analogy

Andrews–Dyson–Hickerson, *Partitions and indefinite quadratic forms*, Invent. Math. 91 (1988) 391–407 (the citation was verified; no theorem number is used here). For σ(q) = Σ q^{n(n+1)/2}/(−q;q)_n they prove:
- S(n) = T(24n+1), which ties the coefficients to the arithmetic of Q(√6);
- S(n) = 0 for infinitely many n, and limsup |S(n)| = ∞.

H. Cohen's companion paper (same volume, pp. 409–422) links σ to a Maass form.

Why g_7 behaves differently (Cat B):
- σ's coefficients stay tiny. That is the signature of complete cancellation, i.e. quantum-modular / Maass behaviour.
- g_7's coefficients grow like exp(0.3985√d), and E/O sits at 0.5444 with relative drift < 10^{−3} beyond 3·10^4.
- Infinitely many zeros would require E_d = O_d exactly. That flatly contradicts the observed stable ratio.
- The naive saddle heuristic also predicts growth for σ, wrongly, so a heuristic alone could not rule out (c). It is the numerics plus the positive splitting (A2) that rule it out.

**Verdict on (c): no evidence; the evidence strongly points the other way.**

## Category lists

**Cat A**
- A1 positivity identity
- A2 E − O splitting
- A3 ladder identities and E_d ≤ O*_d
- A4 reduction (all elementary, proved above)
- Certified computation: g_7(d) ≠ 0 for 247 < d ≤ 10^7 in the allowed classes
- Exact computation: O_d > E_d for 1127 < d ≤ 10^6
- The ADH σ facts above (as stated in the cited paper)

**Cat B**
- c = 0.39854 and the d^{−1/2} power
- The limits E/O → 0.54434, O*/O → y, E/O* → 1/(1+y^{3.5})
- Class weights 1:2
- The heuristic that zeros are finite
- The A000700 asymptotic (OEIS entry, no theorem number)

**Open:** Lemma L or L*, which would give an explicit D0.

## Files (`2026-10-17-Lever-3-OccFilt7-Lower-Bound/`)

- `g7mod.c` / `g7mod`, `primes.txt`: modular certification (usage: `./g7mod D K prefix`)
- `exact.py`: exact g_7 to D
- `stats_exact.py`: growth tables
- `EO.py`: A1 check, E/O split, ratios
- `Ostar.py`: A3 check and O*
- `data/`:
  - `exact_{100000,1000000}.txt.gz`
  - `D1e{5,6,7}.allowed_zeros.txt` (each lists the same 24 values)
  - `stats_exact_1e6.txt`, `EO_1e6.txt`, `Ostar_1e5.txt`

---

## Lemma L attempt (2026-10-17, second pass)

**Verdict: PARTIAL. Lemma L is NOT proved.** No η or D0 is established.

What this pass adds:
1. two rigorous obstruction results, which show what a proof must look like;
2. exact ladder inequalities;
3. an exact-arithmetic map of where termwise comparisons hold (Cat B);
4. a precise statement of the remaining analytic gap.

Scripts are in `2026-10-17-Lever-3-OccFilt7-Lower-Bound/lemmaL/`. Every test there uses exact Python integers; there is no floating point anywhere.

Notation (as before):
- a_n(m) = (−1)^m φ_n(m) ≥ 0 (A1), with generating function A_n(x) = ∏_{odd j≤n}(1+x^j) / ∏_{k=⌊n/2⌋+1}^{n}(1−x^{2k}).
- For an allowed d, the even-layer term is e_n = a_n((d−n²)/7) for even n, and the odd-layer term is o_n, the same expression for odd n.
- E_d = Σ e_n and O_d = Σ o_n, summed over n with n² ≡ d (mod 7) and n² ≤ d.

### Rigorous results (Cat A)

**L1. Exact ladder in n at fixed m.** For all k ≥ 0 and m ≥ 0:
- A_{2k+1} = A_{2k}/(1−x^{2k+1}). Hence a_{2k+1}(m) = Σ_{i≥0} a_{2k}(m−i(2k+1)) ≥ a_{2k}(m).
- A_{2k+1} = (1+x^{2k+2})·A_{2k+2}. Hence a_{2k+1}(m) = a_{2k+2}(m) + a_{2k+2}(m−2k−2) ≥ a_{2k+2}(m).

*Proof.* A_{2k+1}/A_{2k} = (1+x^{2k+1})/(1−x^{4k+2}) = 1/(1−x^{2k+1}). The numerator gains the factor (1+x^{2k+1}). In the denominator the range k' ∈ (⌊n/2⌋, n] moves from [k+1, 2k] to [k+1, 2k+1], adding (1−x^{4k+2}).
A_{2k+2}/A_{2k+1} = (1−x^{2k+2})/(1−x^{4k+4}) = 1/(1+x^{2k+2}). The numerator is unchanged. The denominator range moves from [k+1, 2k+1] to [k+2, 2k+2], removing (1−x^{2k+2}) and adding (1−x^{4k+4}). ∎

So at fixed m, odd layers are local maxima in n.

**L2. Obstruction 1: no positivity certificate inside a single layer pair (n, n+1).** [q^d]T_n and [q^d]T_{n'} can both be nonzero only if n² ≡ n'² (mod 7), i.e. n' ≡ ±n (mod 7).
- For n' = n+1 this means 7 | 2n+1.
- So telescoping O − E = Σ_k (T_{2k+1} − T_{2k}) cannot be coefficientwise non-negative term by term. At a given d, the kth summand is supported on one residue class unless 7 | 4k+1.
- Any certificate must couple layers n and n' with n + n' ≡ 0 or n − n' ≡ 0 (mod 7), and opposite parity. This rules out route 2 in its naive form.

**L3. Obstruction 2: no fixed-partner termwise injection.** Fix layers n, n' ≥ 3 and a shift s ∈ Z.
- (i) If ⌈n/2⌉ > ⌈n'/2⌉, then a_n(m) ≤ a_{n'}(m+s) fails for all sufficiently large m.
- (ii) If s < 0, it fails at m = 0, since a_n(0) = 1 and a_{n'}(s) = 0.

*Proof of (i).* A_n = N_n(x)/∏_{k=⌊n/2⌋+1}^{n}(1−x^{2k}) with N_n = ∏_{odd j≤n}(1+x^j).
- The pole at x=1 has order exactly ⌈n/2⌉, because N_n(1) = 2^{⌈n/2⌉} ≠ 0.
- At x = −1 the denominator vanishes to order ⌈n/2⌉ and N_n vanishes to the same order (each odd j gives a zero), so there is no pole there.
- Take a primitive r-th root of unity with r ≥ 3. The factor 1−x^{2k} vanishes there only if r | 2k. Two consecutive k cannot both satisfy this, since that would force r | 2.
- For n ≥ 3 the range (n/2, n] contains at least 2 integers, so fewer than ⌈n/2⌉ denominator factors vanish. That pole therefore has order < ⌈n/2⌉.
- For n = 2, A_2 = (1+x)/(1−x^4) has a pole of order 1 at x = i, so the hypothesis n ≥ 3 is needed.
- Partial fractions then give a_n(m) = C_n m^{⌈n/2⌉−1} + O(m^{⌈n/2⌉−2}), with C_n > 0. So larger ⌈n/2⌉ wins as m → ∞. ∎

Consequence: a working injection must choose its partner depending on (n, d), equivalently on ρ = m/n². This matches the numerics below.

**L4.** All earlier Cat A items still stand: A1–A4, certified nonvanishing to 10^7, and O_d > E_d exactly for 1127 < d ≤ 10^6.

### Exact-arithmetic exploration (Cat B: exhaustive on finite ranges, not proofs)

1. **Fixed termwise injections fail for every d tested up to 40000** (`out_pairing.txt`). The tested rules were:
   - reflection n ↦ n' with n + n' ≡ 7 (mod 14) and |n'−n| ≤ 7;
   - n ↦ n+7;
   - n ↦ n−7.

   All failures sit in the two tails, i.e. small n' with huge m (a_1(m) = 1), or n near √d with small m. This is consistent with L3.
   - Failing terms carry up to about 15% of the mass in classes 0 and 1 (gap 7 and gap 5 pairings, `out_window.txt`).
   - In class 2 (gap-1 pairs) they carry only about 10^{−5}.
2. **The averaging rule e_n ≤ (o_prev + o_next)/2 also fails for all d tested up to 40000** (`out_avg.txt`). The failures come from the top tail, at n/√d ≈ 0.6–0.77.
3. **ρ-windows** (`out_regions.txt`, n ≤ 148, m ≤ 6000). For even n, let n_u be the nearest odd partner above and n_d the nearest odd partner below, both with n_u², n_d² ≡ n² (mod 7). Define:
   - U(n,m): a_n(m) ≤ a_{n_u}(m − (n_u²−n²)/7);
   - Dn(n,m): a_n(m) ≤ a_{n_d}(m + (n²−n_d²)/7).

   Findings:
   - U holds for all m > ρ_U(n)·n². ρ_U falls from about 0.68 to 0.51 for gap-7/gap-5 partners, and is about 0.223 for gap-1 partners.
   - Dn holds for every m below ρ_D(n)·n² (no small-m failures at all). ρ_D rises from about 0.51 to above 0.73. Beyond n ≈ 90 no Dn failure appears inside the table.
   - The saddle point sits at ρ* = (1/0.438² − 1)/7 ≈ 0.60, inside the overlap window (ρ_U, ρ_D).
4. **Why a pure injection cannot switch direction.** In classes 1, 2 and 4 the allowed n form a chain with parity pattern O, EE, OO, EE, OO, … Only three injective block rules exist:
   - reflection R, using adjacent partners;
   - S+, both evens of a block move up 7;
   - S−, both evens of a block move down 7.

   Once one block uses S+, every block above it must also use S+, because the next OO block is fully used. So "toward the peak from both sides" is impossible as a pure injection. It is possible as a **fractional transport**:
   - each e_n is split as λ·(S+ target) + (1−λ)·(R target), and similarly between R and S−;
   - near the peak e/o ≈ 0.544, so a block-to-block change in λ of up to 0.84 fits within the odd capacities.

### Exact remaining gap

Lemma L would follow by the fractional transport of item 4, with the two tails absorbed, from the following analytic inputs. All must be explicit and uniform for n ≥ n1.

- **(R1) Ratio bound near the peak.** For ρ = m/n² ∈ [0.55, 0.66]: a_n(m) ≤ θ·a_{n'}(m') with θ ≤ 0.6, for each partner n' ∈ {n_u, n_d, n±7} and the corresponding m'.
- **(R2) Upper side.** U(n,m) holds for all m ≥ 0.66 n².
- **(R3) Lower side.** Dn(n,m) holds for all m ≤ 0.55 n².
- **(R4) Tail bounds.** The even terms falling outside these windows (n < n1, or the small-m and huge-m extremes) total at most η' O_d, with an explicit d-threshold.

(R1)–(R3) are local-limit / saddle-point estimates for a single restricted-partition generating function A_n at m ≍ n², uniform in n. I know of no citable theorem giving them with explicit constants. Proving them is exactly the effective analytic route (route 3). It was not attempted in the remaining time, so no D0 is available. Note that the Chernoff bound E_d ≤ E(r)r^{−d} alone cannot work: it loses a polynomial factor (about d^{3/4}), while the true margin O/E ≈ 1.84 is only a constant.

### Self-audit

| step | status |
|---|---|
| L1 ladder identities and inequalities | rigorous (algebra above; also matches A1/A2 exact checks) |
| L2 residue obstruction | rigorous (elementary congruence) |
| L3 pole-order argument (n, n' ≥ 3) | rigorous (partial fractions plus the consecutive-k argument; n = 2 is a genuine exception, noted) |
| Injection, averaging and ρ-window tables | exhaustive exact checks on finite ranges only (Cat B). Not proofs, and they do not extrapolate. |
| Fractional-transport scheme | heuristic design. Its feasibility depends on (R1)–(R4), which are unproved. |
| Lemma L / O_d > E_d for all d > 1127 | **not proved**. Exact verification covers 1127 < d ≤ 10^6. Nonvanishing of g_7 is certified to 10^7. |

---

## Lemma L — route 3 (R1–R4) (2026-10-17, third pass)

Scripts: `2026-10-17-Lever-3-OccFilt7-Lower-Bound/lemmaL/route3/`. Every constant below comes from `mpmath.iv` interval arithmetic (60–100 bit). Floating point is used only to *choose* free parameters (tilt u_c, τ0, cell centres). Each bound is valid for any value of those parameters.

### Statement proved (computer-assisted)

**Status: Cat A (computer-assisted), audited once** (rev 2; all audit patches pass, see "Post-audit patches (rev 2)").

**Theorem L.** Let η = 0.2272, n1 = 900 and D0 = 8 890 003. For every d ≥ D0 with d mod 7 ∈ {0,1,2,4},
  E_d ≤ (1 − η) O_d, hence g_7(d) = (−1)^d(E_d − O_d) ≠ 0.
Combined with the modular certification g_7(d) ≠ 0 for 247 < d ≤ 10^7 (Task 1, `g7mod`, D1e7), this gives **OccFilt_7(∞) = {0,1,2,4}**, with largest allowed-class zero d = 247.

The exact margin is η = 1 − 0.772733 − 10^−6 ≥ 0.22726. Here 0.772733 is the worst block ratio (class 2, base tilt u ≈ 0.975) and 10^−6 is the tail allowance η_t.

### Proof structure

Notation: a_n(m) = (−1)^m φ_n(m) ≥ 0, with generating function A_n (A1). E_d sums a_n over even n and O_d over odd n, with m = (d−n²)/7 (A2). Write α_n = n/√d and ρ = m/n² = (1/α²−1)/7.

1. **(R1) Tilted model + local CLT (`clt.py`).** At r = e^{−u/n}, S = ΣB_j + ΣG_k gives P(S=m) = a_n(m) r^m / A_n(r) exactly.
   - Lemma (full proof in the subsection "Local CLT lemma: full proof" below; rev 2): if τ0 = nθ0 ≤ 1 and K3θ0 ≤ 1.5σ², then |P(S=m) − g(m−μ)| ≤ δ/(√(2π)σ), where δ = D1 + D2 + D3.
     - D1 = (4√(2π)/(3π))K3/σ³ (Taylor with integral remainder).
     - D2 = erfc(σθ0/√2) (Gaussian tail).
     - D3 = √(2π)σ π^{−1}∫_{θ0}^{π} e^{−B} (minor arc).
   - The minor-arc bound B uses −log|φ| ≥ Σ v_j(1−cos jθ) + ½Σ log(1+λ_k sin² kθ), with closed-form trigonometric sums and the chord bound log(1+λx) ≥ (x/X)log(1+λX). The τ-range splits into three regions: piecewise Taylor for τ ≤ 1.2, the closed form up to T = 12, and Abel/Bernoulli near θ ∈ [T/n, π].
   - The constants σ²/n³ ∈ [S_lo, S_hi], μ/n² ∈ [M_lo, M_hi] and K3/n⁴ are enclosed for all n ≥ n1 by **Lemma S**: Σ_{odd j≤n} f(j) = ½∫_0^n f ± (TV(f) + ½ sup|f|), and the analogous statement for k ∈ (n/2, n].
   - Result: δ ≤ 0.151795 on every u-cell of width 0.01 covering [0.3(1−7/n1), 1.6(1+12/n1)] for n ≥ 893. D2 ≤ 2.1·10⁻²⁵ and D3 ≤ 1.8·10⁻¹⁵ on these cells (≤ 2.3·10⁻¹⁵ on all computed cells). *Rev 2 correction:* the earlier text said "D2 and D3 are below 10^−20", which was false for D3; the audit found 1.3·10⁻¹⁵ in [1.61, 1.62].
2. **(R2/R3) Block lemma (`blocks.py`, `verify_blocks.py`).** Each residue class is partitioned into disjoint blocks of n-width ≤ 14:
   Notation (rev 2, matching `PATTERNS` in blocks.py): a block is a base n_b plus offsets; O/E is the parity of the member n_b + offset.
   - class 1: base n_b ≡ 1 (mod 14), offsets {0 O, 5 E, 7 E, 12 O}, i.e. members ≡ 1, 6, 8, 13 (mod 14);
   - class 2: base n_b ≡ 3 (mod 14), offsets {0 O, 1 E, 7 E, 8 O}, i.e. members ≡ 3, 4, 10, 11 (mod 14);
   - class 4: base n_b ≡ 9 (mod 14), offsets {0 O, 3 E, 7 E, 10 O}, i.e. members ≡ 9, 12, 2, 5 (mod 14). The remnant n ∈ {2, 5} goes to the tail;
   - class 0: base n_b ≡ 0 (mod 14) (even), offsets {−7 O (weight ½), 0 E, +7 O (weight ½)}, i.e. e_{14l} against ½(o_{14l−7} + o_{14l+7}). Each odd term carries total weight 1.

   All block members are written at the common tilt of the block base: T_i = ρ_i P̃_i with P̃_i ∈ [e^{−x_i²/2σ_i²} − δ, 1 + δ]. Interval evaluation over u-boxes of width 0.0025 and all n ≥ 900 gives the following bounds on Σ_E/Σ_O for every block whose base saddle u_b lies in [0.3, 1.6]:

   | class | max ratio | at u |
   |---|---|---|
   | 0 | 0.72313 | 0.6425 |
   | 1 | 0.73974 | 0.6400 |
   | 2 | **0.77273** | 0.9750 |
   | 4 | 0.73562 | 0.6800 |

   (`blocks_N900_0.3_1.6.json`; max δ used = 0.151794. Rev 2: identical after the patches; minimum odd-side factor 1 − gfac − δ ≥ 0.78507 > 0, asserted.)
3. **Window bookkeeping.** μ_n(u)/n² decreases in u. Using rigorous M_lo(0.3) and M_hi(1.6): if a base has α_b ∈ [α1, α2] = [0.30185026151, 0.70434264606], then u_b ∈ [0.3, 1.6]. Here α1 is the rounded-up end and α2 the rounded-down end. Every even n lies in a block whose base satisfies n − 7 ≤ n_b ≤ n. So if d ≥ D0 = ⌈(n1/α1)²⌉, every base in the window has n_b ≥ n1. Even terms whose base is outside the window have α_n ∈ (0, α1 + 7/√d) ∪ (α2, 1]. These are the "bad" evens; there are at most √d of them.
4. **(R4) Tails (`tails.py`).**
   - *Lemma T1/T2.* log A_n(e^{−u/n}) ∈ [nΦ1(u) − ½log 2 − g(u), nΦ1(u) + log 2 + g(u)], where Φ1(u) = ½[∫_0^1 log(1+e^{−uy})dy + ∫_1^2 −log(1−e^{−uy})dy] and g(u) = −log(1−e^{−u}). Proof: both summands are monotone. For odd j, ½∫_j^{j+2} f ≤ f(j) ≤ ½∫_{j−2}^{j} f, with f(1) ≤ log 2. For k ∈ (n/2, n], use one end term ≤ h(n/2) = g(u). Substitution then gives the Φ1 form. (Checked exactly for n ≤ 200 and u ∈ {0.3, 0.6, 1, 2}.)
   - *Chernoff bound.* a_n(m) ≤ A_n(r) r^{−m}, so log e_n ≤ √d F(α_n, u_c) + log 2 + g(u_c) for **any** u_c > 0, where F(α,u) = αΦ1(u) + (1−α²)u/(7α).
   - *Tiny α ≤ 0.005.* Take u = 3.5α². For x ≤ 1, −log(1−e^{−x}) ≤ −log x + x, which gives Φ1(u) ≤ ½(1 − log 2 − log u + 1.5u). Hence F ≤ (α/2)(0.0541 − 2log α + 5.25α²) ≤ 0.0267, and g ≤ log(d/3.5) + 1.
   - *Central odd term.* There is an odd n* of the right residue with α* ∈ [0.438, 0.438 + 14/√d]. Its saddle satisfies u* ∈ [0.5, 0.75], certified by M_lo(0.5) ≥ ρ*_max and M_hi(0.75) ≤ ρ*_min together with the intermediate value theorem. The CLT at x = 0 gives
     log o* ≥ √d Ψ_low − C*(d), where Ψ_low = inf_{u∈[0.5,0.75]} F(α*, u) ≥ 0.395568 (rev 2: the inf is only over the certified range of u*; rev 1 scanned u ∈ [0.02, 10] with unchecked claims outside, giving 0.395057) and C*(d) = ½log 2 + g(0.5) + ½log 2π + 1.5 log(0.45√d) + ½log S_hi − log(1 − 0.152).
   - *Verification.* Over 0.0025-boxes of α covering [0.005, α1 + 7/√D0] ∪ [α2, 1], with u_c chosen per box:
     - max(F_up − Ψ_low) = −0.01481 ≤ −2.5/√D0 (rev 1: −0.01430). Hence T(d) := log(Σ_bad e / (η_t o*)) is decreasing in √d for d ≥ D0.
     - T(D0) ≤ −6.80 with η_t = 10^−6 (rev 1: −5.28; the change comes only from the larger Ψ_low).

     So Σ_bad e ≤ 10^−6 o* for all d ≥ D0.
5. **Assembly.** E_d = E_good + E_bad ≤ 0.772733·O_blocks + 10^−6·o* ≤ (1 − 0.22726)O_d. This holds because blocks are disjoint, class-0 weights sum to 1, and O_blocks, o* ≤ O_d. ∎

### Local CLT lemma: full proof (rev 2, added after audit issue 1)

I checked this derivation line by line against `clt.py` (`constants`, `minor_terms`, `delta_bound`) and `sums.py`. The audit's reconstruction (audit point 1) agrees with it. The one correction to the audit text: ∫_ℝ|θ|³e^{−σ²θ²/4}dθ = 16/σ⁴ (two-sided), i.e. 8/σ⁴ per side. The constant D1 below uses the two-sided value.

**Setting.**
- Fix n and u > 0, and put t = u/n, r = e^{−t}.
- For odd j ≤ n, let p_j = 1/(1+e^{jt}) ≤ ½ and v_j = p_j(1−p_j).
- For k ∈ (n/2, n], i.e. K1 := ⌊n/2⌋+1 ≤ k ≤ n, let w_k = e^{−2kt} and λ_k = 4w_k/(1−w_k)².
- S is the independent sum of B_j ∈ {0, j} with P(B_j = j) = p_j, and G_k = 2k·Geom(w_k) with P(G_k = 2kl) = (1−w_k)w_k^l.
- Then P(S = m) = a_n(m) r^m / A_n(r) (expand A_n(r x) as a product).
- Its characteristic function is φ(θ) = ∏_j(1−p_j+p_j e^{ijθ}) · ∏_k(1−w_k)/(1−w_k e^{2ikθ}).
- μ = ES = Σ j p_j + Σ 2k w_k/(1−w_k) and σ² = Σ j² v_j + Σ (2k)² w_k/(1−w_k)². These are `Fp`/`Gm` and `Fv`/`Gh` in sums.py, and the enclosures μ/n² ∈ [M_lo, M_hi] and σ²/n³ ∈ [S_lo, S_hi] come from Lemma S.

**Lemma (local CLT).** Let θ0 = τ0/n with 0 < τ0 ≤ 1. Let K3 ≥ sup_{|θ|≤θ0}|κ‴(θ)|, where κ = log φ is the branch with κ(0) = 0, and suppose K3θ0 ≤ 1.5σ². Let B(θ) be any function with |φ(θ)| ≤ e^{−B(θ)} on [θ0, π]. Then for every integer m, with x = m − μ and g(x) = e^{−x²/(2σ²)}/(√(2π)σ),

  |P(S = m) − g(x)| ≤ δ/(√(2π)σ),  δ = D1 + D2 + D3,

  D1 = (4√(2π)/(3π))·K3/σ³,  D2 = erfc(σθ0/√2),  D3 = √(2π)σ·(1/π)∫_{θ0}^{π} e^{−B(θ)} dθ.

*Proof.*
- By Fourier inversion on ℤ, P(S=m) = (1/2π)∫_{−π}^{π} φ(θ)e^{−imθ}dθ. Also g(x) = (1/2π)∫_ℝ e^{−σ²θ²/2}e^{−ixθ}dθ.
- Write φ(θ)e^{−imθ} = e^{L(θ)}e^{−ixθ} with L(θ) = κ(θ) − iμθ. Then

  2π|P − g| ≤ ∫_{|θ|≤θ0}|e^{L} − e^{−σ²θ²/2}| + ∫_{|θ|>θ0} e^{−σ²θ²/2} + ∫_{θ0<|θ|≤π}|φ|.

- *Taylor step.* κ(0) = 0, κ′(0) = iμ and κ″(0) = −σ². Taylor's formula with integral remainder gives L(θ) = −σ²θ²/2 + R(θ), where R(θ) = ∫_0^θ ((θ−s)²/2)κ‴(s)ds. So |R| ≤ K3|θ|³/6.
  - On |θ| ≤ θ0 the hypothesis gives |R| ≤ K3θ0θ²/6 ≤ σ²θ²/4.
  - Using |e^z − 1| ≤ |z|e^{|z|}, we get |e^L − e^{−σ²θ²/2}| ≤ e^{−σ²θ²/2}|R|e^{|R|} ≤ (K3|θ|³/6)e^{−σ²θ²/4}.
  - ∫_ℝ|θ|³e^{−σ²θ²/4}dθ = 2·(1/2)(4/σ²)² = 16/σ⁴, so the first integral is ≤ 8K3/(3σ⁴).
  - Dividing by 2π and multiplying by √(2π)σ gives D1 = √(2π)σ·4K3/(3πσ⁴) = (4√(2π)/(3π))K3/σ³.
- *Gaussian tail.* ∫_{|θ|>θ0}e^{−σ²θ²/2}dθ = (√(2π)/σ)·P(|Z| > σθ0) = (√(2π)/σ)erfc(σθ0/√2). After the same normalisation this is D2.
- *Minor arc.* |φ(−θ)| = |φ(θ)|, so the third integral is ≤ 2∫_{θ0}^{π}e^{−B}. After normalisation this is D3. ∎

**Bound for K3 (`constants`, k3 = (k3B + τ0·k3B4)/cos³(τ0/2) + k3G).**
- *Bernoulli factor.* κ_j(θ) = log(1−p+pe^{iy}) with y = jθ. Writing q = pe^{iy}/(1−p+pe^{iy}), d³/dθ³ κ_j = (ij)³q(1−q)(1−2q). Hence
  |κ_j‴| = j³p(1−p)|1−p−pe^{iy}| / |1−p+pe^{iy}|³.
  - Since |1−p+pe^{iy}|² = 1 − 4p(1−p)sin²(y/2) ≥ cos²(y/2), and |y| ≤ nθ0 = τ0 ≤ 1 < π, the denominator is ≥ cos³(τ0/2).
  - |1−p−pe^{iy}| ≤ (1−2p) + p|1−e^{iy}| ≤ (1−2p) + p·jθ0, using p ≤ ½.
  - So |κ_j‴| ≤ j³[p(1−p)(1−2p) + p²(1−p)·jθ0]/cos³(τ0/2).
  - In code: F3 = p(1−p)(1−2p) and F4 = p²(1−p). With jθ0 = (j/n)τ0, the sum Σ_j j⁴F4·θ0 = τ0·Σ j⁴F4/n, which is the τ0·k3B4 term after normalising by n⁴.
- *Geometric factor.* κ_k(θ) = log(1−w) − log(1−we^{iy}) with y = 2kθ. Then d³/dθ³ κ_k = (2ki)³·we^{iy}(1+we^{iy})/(1−we^{iy})³. Since |1−we^{iy}| ≥ 1−w and |1+we^{iy}| ≤ 1+w, |κ_k‴| ≤ (2k)³w(1+w)/(1−w)³ for every θ. In code this is 8·G3.
- K3 is the sum of these bounds. The code also checks the hypothesis K3θ0 ≤ 1.5σ² with k3 (upper end) against S_lo (lower end) in interval arithmetic (`delta_bound`, rev 2). τ0 is chosen by a float fixed-point iteration, which is harmless.
- *Uniformity in n.* D1 = const·k3/(S_lo^{3/2}√n) and D2 = erfc(z), with z ≥ τ0√(S_lo·n/2), are both decreasing in n. The code evaluates them at n = n1.

**Minor-arc inequality (`minor_terms`).**
- |1−p+pe^{iy}|² = 1 − 2v(1−cos y), so log|·| ≤ −v(1−cos y).
- |(1−w)/(1−we^{2ikθ})|² = 1/(1 + λ sin²(kθ)).
- Hence
  −log|φ(θ)| ≥ Σ_{odd j≤n} v_j(1−cos jθ) + ½Σ_{k=K1}^{n} log(1+λ_k sin²kθ).  (MA)
- Monotonicity: jt ≤ u ≤ u_hi and 2kt ≤ 2u_hi, so v_j ≥ v := v(u_hi) and λ_k ≥ λ := λ(e^{−2u_hi}). All summands are ≥ 0, so replacing v_j and λ_k by these lower bounds is legitimate.
- Write τ = nθ and s = 1/n ∈ [0, 1/n1]. All bounds below are of the form B ≥ n·b, with b evaluated over boxes in τ and the whole s-interval, so they hold for every n ≥ n1.
- Closed forms: N = ⌈n/2⌉ is the number of odd j ≤ n, and L = n − K1 + 1 = ⌈n/2⌉.
  - S1 := Σ_{odd j≤n}(1−cos jθ) = N − sin(2Nθ)/(2 sinθ).
  - S2 := Σ_{k=K1}^{n} sin²kθ = L/2 − [sin((2n+1)θ) − sin((2K1−1)θ)]/(4 sinθ).
  - In the code, n even gives 2Nθ = τ, (2n+1)θ = τ(2+s), (2K1−1)θ = τ(1+s) and N/n = L/n = ½. n odd gives 2Nθ = τ(1+s), (2K1−1)θ = τ and N/n = L/n = (1+s)/2. Also n sinθ = τ·sinc(τs) with sinc ∈ [1 − (τs)²/6, 1].
- Chord bound: by concavity, log(1+λx) ≥ (x/X)log(1+λX) for 0 ≤ x ≤ X.
- *Region 1a, θ ∈ [θ0, T/n] with τ ≤ 1.2.*
  - Use 1−cos y ≥ y²/2 − y⁴/24 and sin²y ≥ y² − y⁴/3 (both hold for all real y; the second follows from the first at 2y).
  - Use the chord with X = τ_hi², valid because sin²kθ ≤ (kθ)² ≤ τ².
  - Split j/n and k/n into 50 pieces, with per-piece v and λ lower bounds at the piece's right end. The per-piece sums of (j/n)², (j/n)⁴, (k/n)², (k/n)⁴ are enclosed by `oddsum`/`intsum`, which are monotone-sum bounds valid for n ≥ n1.
  - Each summand is first replaced by its lower bound (v_j ≥ v_i, which needs 1−cos ≥ 0) and then summed, so a negative lower bound of a piece sum is still a valid lower bound.
- *Region 1b, τ ∈ [1.2, T], T = 12.* B ≥ v·S1 + ½·(log(1+λX)/X)·S2, with X = sin²(τ_hi) if τ_hi < π/2 and X = 1 otherwise. (sin² is increasing on [0, π/2]. Rev 2 makes the comparison with π/2 in mpf.) Take the minimum over both parities.
  - Contribution: ∫ e^{−B}dθ ≤ (1/n)Σ_boxes Δτ e^{−n b_box}. With σ ≤ √S_hi·n^{3/2}, the normalised contribution is (√(2π)√S_hi/π)·√n·Σ Δτ e^{−nb}.
  - This is non-increasing in n when n1·b ≥ ½ for every box, which is checked as `mono_ok`.
- *Region 2, θ ∈ [T/n, π − T/n].*
  - |sin(2Nθ)| ≤ 1 and |sin(·) − sin(·)| ≤ 2. With the chord at X = 1: B ≥ v(N − 1/(2 sinθ)) + ½log(1+λ)(L/2 − 1/(2 sinθ)).
  - Use N, L ≥ n/2 and sinθ ≥ sin(T/n) ≥ (T/n)(1 − T²/(6n²)). This gives B ≥ n·b2 with b2 = v/2 + log(1+λ)/8 − (v + log(1+λ)/2)/(2T(1 − T²/(6n1²))).
  - Contribution ≤ √(2π)√S_hi/π · n^{3/2}·π·e^{−n b2}, monotone if n1·b2 ≥ 3/2 (checked).
- *Region 3, θ = π − ψ/n with ψ ∈ [0, T].*
  - Use only the Bernoulli part (sin²(kπ) = 0, so the geometric part is useless here). For odd j, cos(jθ) = −cos(jψ/n), so S1 = N + sin(2Nψ/n)/(2 sin(ψ/n)).
  - For ψ ≤ 0.5, every jψ/n ≤ (1+s)ψ < π/2, so S1 ≥ N ≥ n/2.
  - Hence B ≥ n·b3, and the contribution is ≤ √(2π)√S_hi/π · √n·T·e^{−n b3}, monotone if n1·b3 ≥ ½ (checked).
- Coverage: [θ0, T/n] ∪ [T/n, π−T/n] ∪ [π−T/n, π] = [θ0, π] because n1 > 2T/π.
- Why roots of unity do not matter: B > 0 on the whole minor arc comes from the Bernoulli part. The j = 1 term has span 1, and the bound is in terms of |φ|, not A_n near |x| = 1, so the poles of A_n at roots of unity play no role (audit point 1).

**Numbers (rev 2 rerun).**
- On the cells the block check actually uses (u ∈ [0.29, 1.63], n ≥ 893): δ ≤ 0.1517943006830443, rounded outward to 0.151795, with D2 ≤ 2.1·10⁻²⁵ and D3 ≤ 1.8·10⁻¹⁵.
- Over all computed cells, [0.28, 1.64]: δ ≤ 0.152367 and D3 ≤ 2.3·10⁻¹⁵. The audit found D3 = 1.3·10⁻¹⁵ in [1.61, 1.62].
- On the central-saddle range u ∈ [0.5, 0.75]: δ ≤ 0.1172. R4 uses 0.152.
- So δ equals D1 up to ~10⁻¹⁵.

### Self-audit (Cat A vs Cat B)

- **Cat A (proved here, computer-assisted, interval arithmetic):**
  - (A1) and (A2);
  - the local-CLT lemma;
  - minor-arc bounds;
  - Lemma S;
  - Lemma T1/T2;
  - the Chernoff and tiny-α bounds;
  - block ratios ≤ 0.77273 (n ≥ 900, u ∈ [0.3, 1.6]);
  - R4 tail bound;
  - Theorem L (η = 0.2272, D0 = 8 890 003, n1 = 900);
  - with Task 1's modular certification to 10^7, OccFilt_7(∞) = {0,1,2,4}.

  All proofs are my own derivations, written out in this report and the previous section. None of them relies on a cited theorem.
- **Caveats (honest):**
  1. The proof is computer-assisted. Its correctness rests on the scripts `sums.py`, `clt.py`, `blocks.py`, `verify_blocks.py` and `tails.py`. These have since had one independent referee audit (see below); a formal verification has not been done. They should be reviewed by a second reader before this is called a theorem in print.
  2. A few parameters are chosen by float. This is harmless because the bounds hold for any choice.
  3. (Rev 1) Interval enclosures were converted to Python floats in a few places, with up to ½ ulp rounding. **Fixed in rev 2:** endpoints are kept as mpf, and JSON copies are rounded outward with nextafter.
- **Cat B cross-checks:**
  - Chernoff + T1 holds for all 756 131 nonzero a_n(m) with d ≤ 40 000. Max excess is −0.707, i.e. the bound always holds (`out_crosscheck_R4.txt`).
  - Exact float DP at n = 900, u = 0.6 gives a local-CLT error of 0.0236 in δ-units, against the rigorous δ ≤ 0.152. The exact μ/n² = 0.61600 and σ²/n³ = 1.33551 lie inside the rigorous enclosures [0.6119, 0.6205] and [1.3255, 1.3458].
  - Exact E/O on the 10^6 table is 0.5444 at d ≈ 10^6, well below the block bound 0.7727.
  - Limitation: d ≤ 10^6 is below the n ≥ 900 regime, so the block inequalities cannot be tested on exact data in their range of validity.

---

## Steering deliverable (a)/(b): effective growth and ratio bounds

Closed forms: y is the root of y⁷ + y² = 1 (y = 0.8398331470). Then c = √((Li₂(y²) + 7 ln² y)/7) = 0.398540028615674…, and the limit of E/O is (1 − √(1−y²))/y = 0.5443407160…

**(a) Achieved, in log form (Cat A, computer-assisted; `exponent.py`, `exponent_lower.py`).** For all allowed d ≥ D0 = 8 890 003:

  0.398263 √d − ¾ log d − 2.99 ≤ log|g_7(d)| ≤ 0.39900 √d + ½ log d + 1.11 + log(1 + d^{−1/2}).

- **Lower bound:** |g| ≥ η o*, using the CLT lower bound with σ² ≤ 1.970 n*³ and n* ≤ 0.45√d. Here c_− = 0.398263 is a rigorous lower bound for inf_{u∈[0.5,0.75]} F(α*, u) (rev 2: restricted to the certified range of u*; the value is unchanged to 6 digits).
- **Upper bound:** |g| ≤ E + O ≤ (√d + 1) max_n a_n(m). The rigorous sup of the Chernoff exponent over α ∈ [0.005, 1] is c_+ = 0.398875 ≤ 0.3990, and G0 = 0.41.
- **Tiny α ∈ (0, 0.005] (rev 2):** there each term has log a_n ≤ 0.0267√d + log(d/3.5) + 1 + log 2 (tiny-α bound of R4). This is dominated by 0.3990√d + G0 + log 2 for d ≥ D0, since (0.3990 − 0.0267)√D0 − log(D0/3.5) − 1 ≥ 1094 > 0 and the difference increases in d (checked in `exponent.py`).
- **What this pins down:** the exponent to c ± 5·10^−4, i.e. it encloses c. It does **not** give the multiplicative form exp(c√d + lower order)(1 ± ε(d)). That would need the exponent exactly (Ψ(α*) ≥ c − O(1/d)) and a matched second-order term via a full saddle-point sum over n. Not achieved.
- Cat B: at d = 10^6, log|g| ≈ 390.1 versus c√d = 398.5, consistent with a −¾ log d-type correction.

**(b) Not achieved.** I have no effective bound |E_d/O_d − 0.5443407| ≤ δ(d). What is proved is the one-sided E_d/O_d ≤ 0.77273 for d ≥ D0, which suffices for Lemma L and OccFilt. A two-sided ratio bound would need the summed Gaussian-over-n main term at the joint saddle with an explicit error, i.e. block bounds that are sharp rather than one-sided. The existing machinery (CLT with δ ≤ 0.15) is far too coarse for δ(d) < 0.01. Bringing δ down would need n1 ~ 10^5 or an Edgeworth term.

**Does it close Lemma L / OccFilt?** Yes, through route R1–R4. D0 = 8 890 003 ≤ 10^7, so no certified-computation extension is needed: the existing `g7mod` run to 10^7 (1m36s, 2 primes) covers 247 < d < D0. If an auditor prefers more margin, raising n1 is the lever, since D0 scales like n1². For example, n1 = 1000 needs d ≤ 1.1·10^7. `g7mod` to 4·10^7 is about 3.6e10 operations per prime (minutes), and to 10^8 about 1.4e11 per prime (~3–5 min, ~0.9 GB RAM), so both are feasible.

---

## Independent audit of Theorem L (2026-10-17, adversarial referee pass, ~19:00–19:55 CDT)

Work folder: `2026-10-17-Lever-3-OccFilt7-Lower-Bound/lemmaL/audit/` (see its README). No existing file was modified. The scripts were rerun from copies in `audit/rerun/`.

**Verdict: sound, with fixable gaps.** I found no fatal error. Every issue below is repairable or cosmetic. The main gap is documentation: the local-CLT lemma, which carries the whole proof, has no written proof anywhere. I reconstructed one (point 1 below), and it agrees with the code. Until the authors write it into the report and fix the outward-rounding items, I would label Theorem L "Cat A, computer-assisted, single independent review", not a finished Cat A theorem.

### What was checked, point by point

1. **Local CLT and minor arc (clt.py).** The minor-arc bound is uniform in n and does not depend on sampled n.
   - Every region bound is evaluated with s = 1/n as an interval [0, 1/n1]. The closed forms use the exact parity of n: N = ⌈n/2⌉ odd parts, L = ⌈n/2⌉ even-range indices, and the correct endpoints (2K1−1)θ.
   - Monotonicity in n of √n·e^{−nb} and n^{1.5}e^{−nb} is asserted (`mono_ok`, checked in verify_blocks.py).
   - The three θ-ranges [θ0, T/n], [T/n, π−T/n] and [π−T/n, π] cover (0, π], and |φ(−θ)| = |φ(θ)|.
   - The roots-of-unity issue does not arise. For the tilted measure (r < 1), the inequality −log|φ| ≥ Σ_{odd j} v_j(1−cos jθ) uses the Bernoulli parts. These include j = 1, which has span 1, with v_j ≥ v(u_hi) because jt ≤ u. This gives B ≥ c·n on the whole minor arc, so the poles of A_n at roots of unity play no role. Near θ = π, only the odd-j terms are used, and that is correct, since sin²(kπ) = 0.
   - I re-derived D1 = (4√(2π)/(3π))K3/σ³. It follows from |log φ − iμθ + σ²θ²/2| ≤ K3|θ|³/6, |e^z − 1| ≤ |z|e^{|z|}, K3θ0 ≤ 1.5σ² and ∫θ³e^{−σ²θ²/4} = 8/σ⁴.
   - I re-derived the K3 bound in `constants()`. For the Bernoulli part, |κ'''| = j³p(1−p)|1−p−pe^{ix}|/|1−p+pe^{ix}|³ ≤ j³[p(1−p)(1−2p) + p²(1−p)·jθ]/cos³(τ0/2), using p ≤ ½. For the geometric part, the maximum is at θ = 0. This matches k3 = (k3B + τ0·k3B4)/c3 + k3G.
   - All derivative formulas in sums.py (Fv, Fp, F3, F4, Gh, G3, Gm) are correct.
   - **Gap (repairable):** the report says the lemma was "proved in the Lemma L attempt notes; the proof is restated here". Neither section contains a proof. Fix: write out the derivation above.
2. **Uniformity in n (Lemma S, sums.py).** This is genuine and not a finite grid.
   - Every quantity is expressed through y = x/n. The error term is (TV_y + c·sup)/n1, with TV bounded by interval enclosures of f′ on y-cells over [0, 1+1/n1] or [½, 1+1/n1].
   - The tiling arguments are correct: odd j are midpoints tiling [0, 2N], and k are midpoints tiling [K1−½, n+½].
   - u enters as an interval, so the enclosures hold for all n ≥ n1 and all u in the cell.
   - oddsum and intsum (used in the Taylor pieces) are valid monotone-sum bounds.
3. **Interval hygiene.**
   - No numpy is used. `math.*` and float search only choose parameters (u_c, τ0, cells, boxes).
   - Box and cell edges are reused float values, so there are no gaps. Coverage of member tilts u(1−7s)…u_b(1+12s) is asserted.
   - Integrality is automatic: 7 | d − n_i² follows from the residue patterns, and m_i is an integer.
   - **Leaks (cosmetic, but they break strict directed rounding):** `float(·)` (round-to-nearest) is applied to rigorous endpoints at these places:
     - clt.py l.180–182: δ, S_lo;
     - verify_blocks.py l.19: cells store float(S_lo) and float δ;
     - tails.py l.61–62: α1, α2;
     - tails.py l.76, 89, 91: C*, gap, val.
     - The error is ≤ ½ ulp against margins ≥ 10⁻³, so nothing changes numerically.
     - Fix: keep mpf, or move each value one ulp outward (`math.nextafter`).
   - The τ0 assertion (clt.py l.162) is a float comparison with a 0.1% margin, which is fine.
4. **Block lemma (blocks.py, verify_blocks.py).**
   - The offsets match the residue classes: class 1 {0,5,7,12} = n ≡ 1,6,8,13 (mod 14); class 2 {0,1,7,8}; class 4 {0,3,7,10} with remnant {2,5}; class 0 e_{14l} against ½(o_{14l−7} + o_{14l+7}).
   - The blocks are disjoint and cover every even n with n − 7 ≤ n_b ≤ n. Each odd term carries total weight ≤ 1 (class 0: ½ + ½).
   - The ratio conversion is correct and conservative. Even terms use the upper bound (1+δ). Odd terms use e^{−x²/2σ²} − δ ≥ 1 − gfac − δ, with gfac = X²s(n/n_i)³/(2S_i), where (n/n_i)³ ≤ (1+7·s_max)³ for s_max = 1/(n1−7).
   - The step identity, dmu and dvar (r d/dr derivatives), the r^{(n_i²−n²)/7} factor and the σ_n/σ_i factor are all correct.
   - **Missing safeguard (repairable):** there is no assert that the denominator lower bound is positive. If it were negative, R would be negative and would pass silently. I checked this independently: the minimum odd-side factor is 0.782 (`den_check.txt`).
5. **R4 tails (tails.py).**
   - T1 and T2 are proved correctly from monotone comparisons (f(1) ≤ log 2, end term ≤ g(u)).
   - The Chernoff bound gives √d·F(α, u_c) for any u_c. The tiny-α algebra is correct: 2 − log 2 − log 3.5 = 0.0541, and F ≤ 0.0267 on (0, 0.005].
   - o* is bounded rigorously: u* ∈ [0.5, 0.75] by monotonicity of μ/n² and the IVT; n* ≥ 900; σ² ≤ S_hi·n*³; δ = 0.152 ≥ the cell δ (≈ 0.115).
   - Monotonicity of T(d): d/d(√d) of T is gap + 2.5/√d (½ log d for the count of bad evens plus ¾ log d from C*). So max gap ≤ −2.5/√D0 is the right test, and the tiny branch correctly needs −4.5/√D0.
   - α near 1 is covered by the boxes up to 1 (u_c ≤ 30). The count of bad evens ≤ √d is generous.
   - **Text error (cosmetic):** "D2 and D3 are below 10⁻²⁰" is false. D3 = 1.3·10⁻¹⁵ in cell [1.61, 1.62] (`delta_split.txt`). This is harmless.
6. **Window and D0.**
   - μ/n² is strictly decreasing in u (dμ/du = −σ²/n).
   - α1 = 1/√(1+7·M_lo(0.3)) and α2 = 1/√(1+7·M_hi(1.6)).
   - (900/α1)² = 8 890 002.97, so D0 = 8 890 003 is correct.
   - n_b ≥ α1√D0 ≥ 900, and odd members satisfy n ≥ 893, which is covered by the cells.
   - The "≤ ½ ulp" α1 issue is the same as in point 3.
7. **Reproduction.** I reran tails.py, verify_blocks.py (3 min 17 s), exponent.py and exponent_lower.py. All outputs are identical to the originals: max block ratios 0.723129, 0.739737, 0.772733, 0.735618; δ_max 0.151794; α1, α2, D0; Ψ_low 0.395058; gap −0.014298; T(D0) = −5.2805; c₊ 0.398875; c₋ 0.398263.
8. **Cat B spot tests (long-double a_n(m) from positive-only operations, validated against exact g_7 near d = 10⁶ to relative error 6·10⁻¹⁴).**
   - Local CLT, n ∈ {893, 900, 1306} and u ∈ {0.3, 0.6, 0.975, 1.6}:
     - empirical δ is 0.019–0.031, against rigorous 0.115–0.151 (about 5× slack);
     - the exact μ/n² and σ²/n³ lie inside the Lemma S enclosures in all 11 cases.
   - Blocks at d = 8 890 004…8 890 009 and 9 999 994…9 999 999 (all four classes, base α ∈ [0.27, 0.63]):
     - the maximum empirical block ratio is 0.563 (class 4), 0.559 (classes 0 and 1) and 0.596 (class 2, at α_b ≈ 0.545), all below the rigorous 0.7227–0.7727;
     - the hardest class (2) is the same in the rigorous and empirical computations.
   - E_d/O_d:
     - 0.5443594 at d ≈ D0 and 0.5443583 at d ≈ 10⁷;
     - the gap to the limit (1.76·10⁻⁵ at 10⁷) scales like d^{−1/2} from the 10⁶ value;
     - omitted n-ranges contribute < e^{−70} of the maximum term.
   - Caveat: a signed long-double ladder (division by 1 + x^a) is unstable (`ladder.py`, not used). Exact data and floats must use only positive recurrences.
9. **Closed forms.** I derived these, so the identity is now proved; the asymptotic meaning of c is still Cat B.
   - Φ1(u) = K(u)/u with K = (π²/6 − Li₂(e^{−2u}))/4, using Li₂(z) + Li₂(−z) = ½Li₂(z²). Hence F = αK/u + (1−α²)u/(7α).
   - Stationarity in α gives F = 2u/(7α). Stationarity in u gives K′ = 2u/7, i.e. 1 − e^{−2u} = e^{−4u/7}. With y = e^{−2u/7} this is y⁷ + y² = 1 and u = −(7/2) ln y.
   - Then c² = (4/7)(K − u²/7) = 4V/7. By Euler reflection, Li₂(y⁷) = Li₂(1−y²) = π²/6 − ln(y²)ln(y⁷) − Li₂(y²), so c² = (Li₂(y²) + 7 ln²y)/7.
   - Numerically (40 digits), max_α min_u F = 0.39854002861567432698, with α* = 0.43797869 and u* = u0. This equals the closed form and 2√(V/7).
   - lim E/O: (1−√(1−y²))/y = (1−y^{3.5})/y = 1/(termwise ratio y/(1−y^{3.5})) is an algebraic identity, since 1 − y² = y⁷. It equals 0.54434071603789. That the limit holds is Cat B, though consistent with the 10⁷ data.
   - c as the growth exponent of g_7 is pinned rigorously only to [0.398263, 0.398875].

### Issue list

| # | Severity | Location | Issue | Fix |
|---|---|---|---|---|
| 1 | repairable | md §"Lemma L — route 3", item 1 ("proved in the Lemma L attempt notes") | The local-CLT lemma (D1 constant, K3 bound with cos³(τ0/2), D2, minor-arc inequality) has no written proof; the cited section contains none | Write out the derivation in audit point 1 |
| 2 | cosmetic | clt.py l.180–182; verify_blocks.py l.19; tails.py l.61–62, 76, 89, 91 | float() round-to-nearest of rigorous endpoints | Keep mpf, or nextafter outward |
| 3 | repairable (safeguard) | blocks.py `block_ratio` | No check that the odd-side lower bound is > 0 | `assert den.a > 0` (min is 0.782 in fact) |
| 4 | cosmetic | md item 1 ("D2 and D3 are below 10⁻²⁰") | D3 reaches 1.3·10⁻¹⁵ | Correct the text |
| 5 | cosmetic | md item 2, block patterns "(14l+1 O, +6 E, +8 E, +13 O)" | Mixes residues and offsets; the code uses offsets {0,5,7,12} | Write residues mod 14 or offsets consistently |
| 6 | cosmetic | md Steering (a), upper bound | The sup over α covers [0.005, 1] only; the tiny-α branch (≤ 0.0267√d + log d + 2) is not mentioned | Add one line: it is dominated for d ≥ D0 |
| 7 | cosmetic | tails.py `Psi_low` comment (u ≤ 0.02, u ≥ 10) | The claimed bounds are not interval-checked | Irrelevant, because u* ∈ [0.5, 0.75] is certified; restrict the scan to that interval |

**Sign-off.** On the mathematics I audited (Lemma S, minor arc, D1 and K3 derivation, block algebra, R4, window, D0) I found nothing that invalidates Theorem L. Its outputs reproduce exactly, and all Cat B spot tests sit well inside the rigorous bounds.
- I would sign off on Theorem L as **Cat A (computer-assisted)** once issue 1 is written up and issues 2–3 are patched and rerun.
- As the report stands today, my recommendation is "Cat A pending written CLT lemma".
- Caveat: this is one reviewer's line-by-line reading of about 600 lines of interval code, not a formal verification.
- OccFilt_7(∞) = {0,1,2,4} then follows with cert1e8 (247 < d ≤ 10⁸; its SHA256SUMS verify; not re-run here). D0 < 10⁷, so even the older 10⁷ certificate suffices.

---

## Post-audit patches (rev 2) (2026-10-17, ~20:00–20:40 CDT)

This responds to the issue list of the independent audit above. The audit section itself is unchanged. The rev-1 scripts and outputs are preserved in `lemmaL/route3/rev1/`. Checksums for route3 are in `lemmaL/route3/SHA256SUMS`.

| # | Audit issue | Fix | Status |
|---|---|---|---|
| 1 | No written local-CLT proof | Added the subsection "Local CLT lemma: full proof" to the route-3 section: Fourier set-up, D1 via Taylor with integral remainder (two-sided ∫|θ|³e^{−σ²θ²/4} = 16/σ⁴), the K3 bound with cos³(τ0/2), D2, D3, inequality (MA), and regions 1a, 1b, 2, 3 with their monotonicity conditions. Checked against `constants` / `minor_terms` / `delta_bound` rather than copied. | **pass** |
| 2 | float() of rigorous endpoints | See the list below the table. | **pass** |
| 3 | No positivity check of the odd-side bound | `blocks.py`: `assert lo.a > 0` per odd member and `assert den.a > 0` per block. Rerun minimum of 1 − gfac − δ: 0.78507 (the audit's independent check found 0.782; both are positive, and the audit's number comes from its own script). | **pass** |
| 4 | "D2, D3 < 10⁻²⁰" false | Text corrected: on the cells used, D2 ≤ 2.1·10⁻²⁵ and D3 ≤ 1.8·10⁻¹⁵; on all computed cells, D3 ≤ 2.3·10⁻¹⁵. | **pass** |
| 5 | Mixed residue/offset notation | Block list rewritten as base residue mod 14 + offsets, matching `PATTERNS`: {0,5,7,12}, {0,1,7,8}, {0,3,7,10}, {−7,0,7}, with member residues given explicitly. | **pass** |
| 6 | Steering (a) upper bound omits tiny α | Added a line: on α ≤ 0.005, log a_n ≤ 0.0267√d + log(d/3.5) + 1 + log 2, which is dominated for d ≥ D0 (margin ≥ 1094 at D0, increasing in d). Interval-checked in `exponent.py`. | **pass** |
| 7 | Unchecked Psi_low claims for u ≤ 0.02, u ≥ 10 | `Psi_low` (tails.py) and `exponent_lower.py` now take the inf only over u ∈ [0.5, 0.75], the certified range of u*. The claims outside that range are deleted. This is sufficient because log o* ≥ √d F(α*, u*) − C*. | **pass** |

Issue 2 fixes (all **pass**):
- clt.py l.180–182: `delta_bound` returns mpf endpoints (lower ends `.a`, upper ends `.b`). Two related spots were also fixed:
  - the hypothesis K3θ0 ≤ 1.5σ² is now asserted in interval arithmetic;
  - the region-1b test against π/2 now compares with `PI.a/2` (mpf) instead of `float(PI.a)/2`.
- verify_blocks.py l.19: cells keep the mpf S_lo and δ. Two further changes:
  - the member-tilt cover range u(1−7s)…u(1+12s) is computed with interval outward ends;
  - JSON copies are rounded outward with `math.nextafter`.
- tails.py l.61–62, 76, 89, 91: α1 (upper end), α2 (lower end), D0 = ⌈((N1/α1)²).b⌉, √D0, α*, C*, the gaps, the box values, the tiny-α terms and T are all mpf intervals. Decisions use the conservative endpoint. The α-box edges are exact and contiguous (asserted).
- Same treatment applied to exponent.py and exponent_lower.py.

**Full rerun (rev 2).** Everything was rerun: verify_blocks.py, tails.py, exponent.py, exponent_lower.py and crosscheck_R4.py.

| quantity | rev 1 | rev 2 |
|---|---|---|
| block ratio class 0 / 1 / 2 / 4 | 0.723129 / 0.739737 / 0.772733 / 0.735618 | identical (0.7231289922300419 / 0.7397366846138953 / 0.7727327795670832 / 0.7356179382212146, rounded outward) |
| max δ (cells used) | 0.151794 | 0.1517943006830443 (identical) |
| min odd-side factor | not checked | 0.78507 |
| α1, α2 | 0.30185026151, 0.70434264606 | 0.3018502615078950945…, 0.7043426460624558523… (exact mpf) |
| D0 | 8 890 003 | 8 890 003 (identical) |
| Ψ_low(α*) | 0.395057 (u-scan over [0.02, 10]) | 0.395568 (u ∈ [0.5, 0.75]) |
| max tail gap | −0.014298 | −0.014809 (threshold −2.5/√D0 = −0.000838) |
| tiny-α gap | — | −0.3689 (threshold −4.5/√D0 = −0.00151) |
| T(D0), η_t = 10⁻⁶ | −5.2805 | −6.8025 |
| η | 0.2272 (exact margin ≥ 0.22726) | 0.2272 (exact margin 1 − 0.77273278 − 10⁻⁶ = 0.2272662…) |
| c₊, G0 | 0.398875, 0.41 | 0.3988745037, 0.4097921 |
| c₋ | 0.398263 | 0.3982630074 (u ∈ [0.5, 0.75]) |
| Cat B cross-checks | Chernoff excess −0.707; CLT n = 900: 0.0236 | identical |

**Final statement (unchanged).**
- Theorem L holds with η = 0.2272, n1 = 900 and D0 = 8 890 003.
- With the finite certification, OccFilt_7(∞) = {0,1,2,4}. Any of these certificates covers 247 < d < D0: Task 1 to 10⁷, cert1e8, or cert1e9 (247 < d ≤ 10⁹, `cert1e9/README.md`).
- No margin needed the larger D0 headroom that cert1e9 allows.

**Status: Cat A (computer-assisted), audited once.** All seven patches pass, and the rerun reproduces every constant except two, both of which moved in the favourable direction: Ψ_low and T(D0), because of the narrower certified u-range. Caveat: this is still one independent human-style audit of the interval code, not a formal verification.
