# EIGEN-TE-RHOBAR-Q89-ZETA49-CRT — FINDINGS (2026-10-26)
STATUS: GAP (coordinated mod-p solves MATCH rank 89 at 4 primes; Q(ζ49) reconstruction information-insufficient; no char-0 cert)

## Authority (cited; disk re-verified)
- CLOSED_A 2b752efa8d55c22354472881c37862ce2030d2ffcabb881e0fe03e937bba9d61
- ASSIGN d2c89f14f3cb70ec9c3d2fef6f090ad40b8e06f4f6f66b0fa53c8abc1c80d3c7
- Open a5309b5ddff69a8e26d04a406e79a6b1eb58c47f710cd7744398b98935ba99a3 (Rec A)
- PARTIAL FINDINGS 40c2810da7995f54854bb088e220d87dca74ef2758775fee3fc35601151f2232 (stands)
- Prior CLOSED_A 3cf5735c… / ASSIGN 29ede292…; source MATCH mod-p a8788e5c…

## z49 coordination (documented rule)
Fixed ζ = CyclotomicField(49).gen(). For each p≡1 mod 980: r_p = least integer in [1,p) with Φ49(r_p)≡0 mod p;
z49 := r_p, i.e. reduction modulo prime ideal P_p=(p, ζ−r_p). Script solve_z.sage (copy of solve.sage, only z49 line + output name changed).
| p | r_p | kernel | 8-cusp trunc rank |
|---|---|---|---|
| 1027606441 | 8270455 | 89 | 89 |
| 1027611341 | 14650078 | 89 | 89 |
| 1027614281 | 8695957 | 89 | 89 |
| 1027640741 | 6063623 | 89 | 89 |
Outputs q89_modp_m6_zcoord_p*.sobj, logs solveZ_m6_p*.log. Polar systems (11968 eqs) solved exactly mod each P_p.

## Reconstruction (zcoord files only)
- crt_z.sage (QQ CRT of combo RREF): pivots agree; RECON FAILED (crt_z.log) — expected, combos not in QQ.
- zrecon_z.sage (lattice CRT in Z[ζ49], 42 coords + denominator, LLL; 3 ideals recon, 1 held-out) on 8-cusp truncated RREF
  sample (114 entries, all cusps): only 3/114 held-out-verified (trivial ±1 entries). zrecon_z.log.

## Exact blocker
A single prime ideal P_p of degree 1 over p carries log2 p ≈ 30 bits of an element of Z[ζ49] which needs 42 coordinates.
4 ideals ≈ 120 bits ≈ 2.9 bits/coord — cannot reconstruct anything nontrivial. Coordination does not change this
(any P_p choice is valid for lattice CRT; the earlier uncoordinated runs are likewise valid ideals (p, ζ−gen^((p−1)/49))).
Estimated need: truncated 8-cusp basis (cusp-∞ height ≈ 8 bits, den 6) ≳ 15–20 ideals; full combination coefficients
(QQ-height already >60 bits per coord) ≳ 90+ ideals. At ≈20 min/solve, 2-parallel, that is ≈3 h resp. ≳15 h; not launched.
Cheaper routes (not executed, invent HOLD): (a) cache hbasis and loop all 42 roots at one p (42 ideals over one p ⇒ full Z[ζ49]/p);
(b) Galois-on-cusps permutation to read σ_k-conjugate ideals from one solve; (c) dimension argument — NOT available because
hbasis spans only 301/316 etc. of M_k(Γ0(49)) (ansatz not full), so char-0 kernel dim cannot be pinned by mod-p dim alone.
Rank 89 over QQ at cusp ∞ remains CERT via PARTIAL artifacts (untouched).

## Integrity
tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha start=end=7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched NO.
eigen-n36-503/ untouched. q89_basis_q18_cuspinf_QQ.sobj/.csv untouched (c54be5b9 770deb2d ).
Soft SF F3 CLOSED; Bridge PARTIAL READY NO; Cards 8–11 not opened.
