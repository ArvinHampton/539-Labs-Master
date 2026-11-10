# order62 PREREG (LOCAL Bridge C; RG* labels; CORE_FREEZE; no push/send)
Date 2026-10-24 (America/Chicago). Physicist CLEARED order62. Hashed before any test.
Not invented / not used: P̂_orth, Ξ, k≠0, Map-C6, Weil matrices. order≤61 read-only.

## RG47e (Cat A-numeric)
Inputs exactly as order61 rg47d.py: H, HS (Â1 on x and −1/x); pieces R58 = order61/data/rg47a_bis_raw.npy (j=0 axis_Q1, 1 axis_Q7/2, 2 corner/EVEN). R = H − p0 − p1 (R_S likewise). C = corner on x, C_S = corner on −1/x.
Gate: reproduce order61 R excess (34 at w=½, 2 at w=1); else INVALID.
1. Sanity: R2 = R − C (and R2_S = R_S − C_S). PASS(1) iff max(|R2|,|R2_S|) ≤ 1e−12.
2. Span test at w=1 (primary): with rank = #{s/s0 > 1e−9} as order61,
   excess_proj = rank[R | C | |x|·R_S | |x|·C_S] − rank[R | C].
   PASS(2) iff excess_proj ≤ 0. Also disclose excess of R2 itself (rank[R2 | |x|R2_S] − rank R2) and whether the 2 w=1 defect directions of R lie in span(|x|·C_S) (residual ≤ 1e−9 rel).
RG47e PASS iff PASS(1) AND PASS(2). Otherwise FAIL; characterize carriers (top rows x, denominators, singular values).
3. w=½: same numbers, disclosure only. Sensitivity tol 1e−6, 1e−12: disclosure only.

## RG48-Weil (write-up only)
Run span test only if written companion Gram/discriminant form + χ=±i full-basis Weil ingredients exist on disk. Else SKIP (ABSENT), list missing, OPEN. Milgram stays Cat B.
