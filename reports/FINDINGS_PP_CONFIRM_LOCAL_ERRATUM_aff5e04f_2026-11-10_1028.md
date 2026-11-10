# PP CONFIRM — Local erratum aff5e04f (applies PP T-theta1 audit df7b06d0 and tally addendum 6b43adda). 2026-11-10 10:28 CST (America/Chicago)

- Target: ERRATUM_LOCAL_T_THETA1_fff902b4_PP_AUDIT_FIXES_2026-11-10_1027.md, sha256 aff5e04f7906a9966bbb80b2faefac787ab40ed3140416cd12c5384d6dd85762 = sidecar. mtime 10:27:02 CST, matching the header. Tip 7cddb188 unchanged. The 1010 findings (fff902b4…), the 1024 a-3 erratum (ba558e64…), and the 1025 D=56 file (92853714…) were not edited. No CERT, nothing adopted, junction UNSOLVED.

All five fixes are applied faithfully.

- F1: the prefactor is identified as j by setting z = 0 and using that θ = θ₃(2τ) has no zeros on H, in place of "branch fixed by PP at z=0".
- F2: §0's claim u = Σ_k χ(k)U(τ,k/7) is withdrawn. The sum is Ũ = G·u with G = i√7 (S_n − χ(n)G ≡ 0 mod Φ₇, G² = −7). §2 is restated for Ũ and divided by G to recover (L).
- F3: the cuspidality argument now includes the uniform-in-x bound, the constancy of ε from connectedness of H, and the coefficient integral. u ∈ S_{3/2}(Γ₀(196), χ₂₈) stays PROVED.
- F4: [1,0,0,2,0,0,0,0,−3] are recorded as the coordinates of u/2; u itself is [2,0,0,4,0,0,0,0,−6]. §5 now says u/2 equals that form. Membership, eigenvalues, and u ∉ K are unaffected.
- F5: in §6, ζ⁷ is corrected to ζ^k. PP's hand proof that T(p²)u = χ₋₇(p)(1+p)u for every prime p ∤ 14 is included. The §6 inversion constant stays COND (float) and outside the row.

The ruled tallies match the 1025 addendum: Oc-3 [COND: T-theta1] is PROVED; t4436 is 65/15/5/9/2; Bridge C stays 49/10/5/2/1 + V₈₄ (67 rows). The 1024 a-3 erratum's 64/16 figure is correctly left as written. The stale 47/11 figure in 1010 §7 is noted and not used. No other row is regraded.

No grade change and no fixes.
