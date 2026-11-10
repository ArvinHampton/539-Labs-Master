# order61 PREREG (LOCAL Bridge C; RG* labels; CORE_FREEZE; no push/send)
Date 2026-10-24 (America/Chicago). Physicist CLEARED order61. Hashed before any test.
Not invented / not used: P̂_orth, Ξ, k≠0, Map-C6. order58/ and order60/ read-only.

## RG47a-bis (Cat A-numeric)
- Pieces: exactly order58 rg47a.py `parts()` (lib2 PIECES[0]): axis Q=1 = −(√π/2)·w2/√p; axis Q=7/2 = −(√π/2)·w1/√r; corner/EVEN = −mf·(l1·Ja+l2·Jb); times sg. Recomputed by a new script order61/scripts/rg47a_bis.py over the same 216×2×105 sample.
- Target: A1(P_orth) = order56/data/rg46_raw.npy[...,2].
- Statistic: abs_resid = max |A1 − Σpieces| (absolute; no scale, no |A1| filter).
- PASS iff abs_resid ≤ 1e-12 AND control passes.
- Control: flip axis signs (W = −axis_Q1 − axis_Q7/2 + corner); control OK iff max |A1 − W| > 1e-4. Else FAIL(control).
- Also check recomputed pieces equal order58 rg47a_raw.npy (disclosure, max abs diff).
- Dominance table: disclosure only.

## RG47d both-axes closure (Cat A-numeric)
- Object R = Â1 − axis_Q1 − axis_Q7/2, with Â1, ŜÂ1 built exactly as order60 rg47.py (order3 parts.npz, order56 rg46_raw corrections, order58 rg47a_raw pieces on x and −1/x).
- Rank method = order60: SVD, rank = #{s/s0 > 1e-9}; joint = rank [R | |x|^w · R_S]; excess = joint − rank; w ∈ {½, 1}.
- Gate: reproduce order60 Â1 (rank 75, joint 148 at w=½, 150 at w=1). Gate fail → INVALID.
- PASS iff excess ≤ 0 at BOTH w=½ and w=1 (rank tol 1e-9 as above; no ≤1 allowance). Otherwise FAIL.
- If FAIL: characterize residual — singular value spectrum around the cut, corner/EVEN magnitude, per-sample (x row) contributions to the excess directions.
- Control: recompute minus-Q1-only and minus-Q7/2-only; compare to order60 numbers (71/49 and 84/72).
- Sensitivity at tol 1e-6, 1e-12: disclosure only.

## RG48-Weil (optional, conditional)
- Run only if written companion Gram + χ=±i Weil eigenvectors over the FULL basis exist on disk (order12 / Bridge C). Test: P-even target in span (rank tol 1e-9).
- Else SKIP (ABSENT), listing what is missing. Milgram stays Cat B.
