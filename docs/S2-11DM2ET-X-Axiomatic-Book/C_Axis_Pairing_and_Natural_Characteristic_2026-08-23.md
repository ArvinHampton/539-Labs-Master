# Axis pairing of C, natural characteristic, and s=8 Appell second term

Ordinary mathematical English. Packaging provenance Pack+(S) only. Category A residual discrete. Companion to `Review_Missed_Variables_Bridge_C_2026-08-23.md`.

Notation locked there: P_Euler, P_orth, H_s, C = P_orth - H_s, Q_s affine, Q_M = v^T M v. s=7 cones c1 = (-1,1), c2 = (-4,1), M = [[2,7],[7,7]].

---

## 1. Sign weights at s=7 (direct)

B(c1, v) = 5 n, B(c2, v) = -n - 21 k, w(v) = (1/2)(sgn B(c1,v) - sgn B(c2,v)), sgn(0) = 0.

| region | w |
|--------|---|
| interior orthant n>0, k>0 | 1 |
| positive n-axis n>0, k=0 | 1 |
| positive k-axis n=0, k>0 | 1/2 |
| origin | 0 |
| negative n-axis n<0, k=0 | -1 |
| negative k-axis n=0, k<0 | -1/2 |
| third quadrant, through deg 293 | -1 at the points listed below, else 0 |
| mixed signs, Q_s < 294 | 0 |

Interior cancellation: every interior orthant point contributes 0 to C. That is the precise sense in which the cones see the orthant interior. They do not see the axes or the origin in the same way, and they do not see the third quadrant at all.

---

## 2. Axis pairing (locked lattice identity)

Charge coincidences on the axes:

Q_s(n, 0) = n^2 = Q_s(-n, 0) for n >= 1,
Q_s(0, -t) = (7/2) t (t-1) = Q_s(0, t-1) for t >= 1.

The second identity pairs (0,k) with (0, -(k+1)) for k >= 0.

Contribution to C of each pair:

- n-axis, n >= 1: positive point is in the orthant with w = 1, contributes 0; negative point is exterior with w = -1, contributes +1. Net q^{n^2}.
- k-axis, k >= 1: (0,k) contributes 1/2; (0, -(k+1)) contributes 1/2. Net q^{7 k(k+1)/2}.
- origin pair (0,0) with (0,-1): contributes 1 + 1/2 = 3/2.

Hence the axis part of C is exactly

C_axis = 3/2 + sum_{n >= 1} q^{n^2} + sum_{k >= 1} q^{7 k(k+1)/2}.

This is not a classical unary theta (the constant is 3/2, and the triangular series is one-sided). It is a residual axis series. Through degree 80 it accounts for C at degrees 0,1,4,7,9,16,21,25,36,42,49,64,70, and the remaining 1-coefficients in that range are third-quadrant.

---

## 3. Third-quadrant exterior (s=7, through degree 79)

Points with n < 0, k < 0, w = -1, Q_s <= 79, each contributing +1 to C:

(-1,-1) at 8, (-2,-1) at 18, (-1,-2) at 22, (-3,-1) at 30,
(-2,-2) at 39, (-1,-3) at 43, (-4,-1) at 44, (-3,-2) at 58,
(-5,-1) at 60, (-2,-3) at 67, (-1,-4) at 71, (-6,-1) at 78,
(-4,-2) at 79.

This matches the exterior list in d534333. Degrees 42 and 49 are axis, not exterior.

Through degree 80 the observed coefficients of C take values only in {0, 1, 1.5}, with 1.5 only at degree 0. Direct enumeration.

C = C_axis + C_third + C_mixed, with C_mixed = 0 through degree 293.

---

## 4. Natural characteristic of the affine exponent

Q_s(n,k) = (1/2) v^T M v + (s/2) k.

The shift v maps to v + chi that absorbs the linear term satisfies

2 a + s b = 0, a + b = 1/2,

hence

chi_nat(s) = ( s / (2(s-2)) , -1/(s-2) ).

| s | chi_nat |
|---|---------|
| 7 | (7/10, -1/5) |
| 8 | (2/3, -1/6) |
| 11 | (11/18, -1/9) |

For s=7, Q_s(v) = (1/2)(v + chi_nat)^T M (v + chi_nat) + 7/20, verified on sample lattice points including mixed signs.

Also B(c1, chi_nat) = B(c2, chi_nat) = 7/2. The shift is equi-paired to both locked cones.

Evaluating w at v + chi_nat instead of at v resolves the k-axis wall and drops the positive n-axis out of the chamber. H computed with those shifted signs is not P_orth. So chi_nat is the distinguished exponent characteristic; it is not, by itself, a cone realignment that absorbs C. Prior scans that tried chi = (1/7, 0) and (1/2, 0) did not test this point as the exponent shift of Q_s.

No claim is made that a Zwegers sum on L + chi_nat with the locked cones equals P_orth or P_Euler. That remains L-D.

---

## 5. s=8 Appell second term (locked vanishing)

Hickerson–Mortenson h_{2,8,8} at x = q, y tending to q^8:

- second factor j(y ; q^8) vanishes to first order,
- second Appell argument tends to X = -q^{-1},
- m(-q^{-1}, q^6, -1) is finite (6r = 1 has no integer solution for the pole loci X = -q^{-6 r} and X = q^{-6 r}),
- therefore the second term vanishes,
- the first term is independent of y after x = q and equals j(q ; q^2) m(q^{16}, q^{24}, -1).

The All_Levers sentence that the product is finite if and only if m poles is withdrawn. The remaining open piece of L-C is the limit of the theta-correction term theta_{2,8,8} / (Jbar_{0,24} Jbar_{0,6}).

Theorem 0.4 still does not apply to s=7 or s=11 (divisibility). Nothing here supplies a scalar transformation law for Euler g_s.

---

## 6. s=8 and s=11 cone candidates (hygiene)

The pairs in Cone_Vectors do not copy the s=7 interior-weight-1 pattern. Do not quote them as recovering the orthant, and do not quote their “Q” column as Q_M: that file used Q_M at s=7 and Q_s at s=8,11.

---

**Status code:** `C_AXIS_PAIRING_NATURAL_CHARACTERISTIC_S8_APPELL_2026-08-23`

Verification: `scripts/verify_bridge_C_axis_characteristic.py`. Pack+(S) only. Residual law for C as a period function remains unavailable (1b0927c).
