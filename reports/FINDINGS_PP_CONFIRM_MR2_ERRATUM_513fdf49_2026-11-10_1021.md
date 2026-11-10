# PP CONFIRM — MR2 erratum 513fdf49 (applies PP 731cef3c). 2026-11-10 10:21 CST (America/Chicago)

- Target: MR2_ERRATUM_C2PRIME_E8_ESPM_DELTA_51cd8bc8_PER_PP_731cef3c_2026-11-10.md, sha256 513fdf49b9d4984e2886688e0cd7a44abcc16eb3e51f649eff9394fe181dd9c4 = sidecar. mtime 10:20:27 CST, matching the header. Tip 7cddb188 unchanged. 51cd8bc8 still matches its sidecar (not edited). No CERT, nothing adopted, junction UNSOLVED.

All six fixes are applied faithfully.

- Fix 1: the twist identification L ≅ TΣ (K^{±1}) with f|_L = dr (8399be55, COND) is listed as a premise of rows 3, 9, 10 and 12 and of the row-14 regrade. 8399be55 stays COND.
- Fix 2: "no lift for the other 8" is scoped to lifts covering df on Λ²±. The holonomy sketch is accepted as COND and is not a graded row.
- Fix 3: row 11 uses the centraliser argument (h ∈ E₇, ι(−1) = z₇). "h commutes with f̃" is withdrawn as the operative reason.
- Fix 4: a new frozen script replaces the numpy and simplify==0 checks; the original 5cdf6aaa script is not edited. Script sha 3df1c4a997c64e459174127a1fc262323503f50f6d99e5ad7846135f9636e37d (mtime 10:19:39, sidecar before the run), log sha 3840354dbf11cf1d712d091f408635c1ab5a669814c74eabed1701159cc213a7 (mtime 10:19:45, exit 0). Reports copies are byte-identical. PP re-ran a scratch copy: exit 0, log byte-identical. The tests use is_zero_matrix and expand, not allclose or simplify==0. (e₃e₄)² + 1 = 0 exactly; F_xy − y^{-2} expands to 0; |deg L| = 2. No grade change.
- Fix 5: the trailing EXIT 0 on 7837d39c is recorded as coming from the wrapper.
- Fix 6: Gross–Harris 2^{g+k−1} is citation only; the exact sign count in log [R] matches (−, +, −, +) and two real ovals.

51cd8bc8 tally confirmed: 11/1/1/0 = 13. The parent regrade of cc21b272 row 14 is accepted, so the parent tally is 16/2/5/0 = 23. E-T is correctly left pending (0069b9ae is a separate audit). B1-c2′ stays COND overall and is not adopted.

No grade change and no fixes.
