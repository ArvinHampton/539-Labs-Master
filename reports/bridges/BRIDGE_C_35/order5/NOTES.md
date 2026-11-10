# order5 notes (descriptive; disclosures)
1. **zwegers.py, first launch.** The first launch (about 2:14 PM CDT) hit float overflow (inf·0 → NaN) and was killed. No statistic was read from it. The fix was a rewrite of the series summation in an overflow-safe form (erfcx, masked exponent). Tests, thresholds, τ-grid and controls were unchanged. SHA256SUMS was regenerated before the rerun.
2. **bchunk.py, first launch.** The first launch failed on a NameError (`_ET` is not exported by `import *`), before any data was written. It was fixed and relaunched.
3. **Order deviation.** The mp-vs-float cross-check (bcross.py) ran after btest.py, not before. It passed at 3.7e−13, so the verdict is unaffected. Recorded verdicts stand.
4. **Odd combinations.** S_{α,β} depends on the representative α, not only on α mod Z², because the weight wt is applied to v, not to ν. So S_{−α,−β} with −α ∉ [0,1)² is not a member of the 105-family up to a phase. Two consequences:
   - the fixed-matrix residual is undefined for the odd objects, and only the rank test was used, as scripted;
   - the odd objects can have a rank above 73 (A2^c_odd has rank 99).
   The completion Ĥ uses ν-signs and depends only on α mod Z², so test Z is unaffected.
5. **P2 precision.** The P2 residual is 6.8e−15, not 1e−30 like P1. This is consistent with double rounding of three O(10) numbers after conversion to complex. It is far below the 1e−11 pass line.
6. **Reading (descriptive, Category B):**
   - Because A2(H) ≡ 0, the whole O(1) coefficient A2 comes from the closed-orthant piece, so A2^c = A2.
   - The H part contributes to A1 only through the full-line unary thetas U_H and the jump-sawtooth radial limit of the Eichler integral of its shadow.
   - The erf constants (√10, √(2/17), √35) are invisible in A1 and A2. They are fixed only by the S-law (test Z), where a 25% change gives residual 0.11.
7. **Rank of Ĥ.** Ĥ on 120 interior τ has rank 44 (Ĝ_O also 44). This is descriptive.
8. **Still open:** completion of the double orthant and of the axis false thetas; smoothness of their S-defects; a written full proof of §1.4.
9. **Process.** nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no external sends. Nothing outside order5/ was modified.
