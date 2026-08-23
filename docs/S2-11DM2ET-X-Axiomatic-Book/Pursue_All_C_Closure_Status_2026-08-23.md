# Pursue All for Closure of Residual Law for Bridge Series C

Date: 2026-08-23  
Scope: Category A residual discrete only. Pack+(S) provenance mandatory. Residual-flux provenance mandatory. Continuum language excluded. Notation lock: C := P_orth − H_s (unsigned orthant path counts minus cone-weighted series). Distinct from Euler-weighted P_s / g_s.

This note consolidates every lever under the directive “Pursue all for closure of C”. It records the new Category A facts obtained in the parallel review and restates the precise open step for a residual law of C.

Cites: Residual_Bridge_Series_C_Definition.md, U1_GS_BRIDGE_C_AUDIT_d534333_2026-08-23.md, Nine_Maths_Filter_Bridge_C_and_Next_Levers.md, Residual_Law_for_Bridge_C_L_A_Pursuit_2026-08-23.md, C_Axis_Pairing_and_Natural_Characteristic_2026-08-23.md, Review_Missed_Variables_Bridge_C_2026-08-23.md, scripts/verify_bridge_C_axis_characteristic.py.

---

## 0. Executive status of the residual law for C

The residual law for C (a period-function or residual false-theta construction whose Fricke transforms match the residual samples and admit continuous extension off ℚ) remains open.

What has been closed under the present pursue-all:

- Explicit lattice formula for C and its region decomposition (already locked).
- Axis pairing identity that accounts for every axis contribution as a residual series C_axis.
- Natural characteristic chi_nat of the affine quadratic Q_s.
- Verified coefficient support and value set through moderate degree (independent enumeration + verification script).
- s = 8 second Appell term vanishing and first-term Appell–Lerch expression.

What remains open for a residual law of C itself:

- A completed period-function / residual false-theta (or residual quantum-modular form of weight 1/2) that reproduces the verified support (C_axis + third-quadrant exterior) and matches the residual Fricke samples under continuous extension.

The classical residual transformation law for the cone series H_s remains locked via Zwegers and is independent of the law for C.

---

## 1. L-A status (residual law for C)

### Locked Category A facts

1. Lattice formula (s = 7):
   C = ∑_{orthant} (1 − w(v)) q^{Q(v)} − ∑_{exterior} w(v) q^{Q(v)},
   with w(v) = (1/2)(sgn B(c1,v) − sgn B(c2,v)), c1 = (−1,1), c2 = (−4,1).

2. Axis pairing identity (new):
   C_axis = 3/2 + ∑_{n ≥ 1} q^{n²} + ∑_{k ≥ 1} q^{7 k(k+1)/2}.
   This is exact. The constant 3/2 arises from the charge-0 pair (0,0) + (0,−1). Positive n-axis points cancel against their negative partners (net +1 per square); positive k-axis half-weights pair with negative partners (net +1 per 7-triangular number). Half-weights disappear from the net coefficients after pairing.

3. Decomposition:
   C = C_axis + C_third + C_mixed,
   where C_mixed = 0 through degree 293 and C_third consists of the pure third-quadrant points of weight −1 (degrees 8, 18, 22, 30, 39, 43, 44, 58, 60, 67, 71, 78, 79, \ldots).

4. Coefficient value set through degree 80: {0, 1, 1.5} with 1.5 only at the origin. Verified by independent lattice enumeration and by scripts/verify_bridge_C_axis_characteristic.py (PASS).

5. Fricke samples remain qualitative residual defect markers (weight 1/2 slash, ρ ≈ 0.995). Exact slash prefactor used for the published complex values has not been recovered; raw holomorphic radial sums do not match the published magnitudes.

### Open for residual law

No period-function or residual false-theta has been constructed that simultaneously matches the verified support (C_axis + C_third) and the residual Fricke samples under continuous extension. That construction remains the exact missing step.

---

## 2. L-B status (vector packaging and fibre remainder ρ)

Prior fibre decomposition of the Fricke cocycle of the residual series split as α h_1 + β + ρ with approximately 90 % of the mass in the torsion remainder ρ. C remains a candidate residual source for that remainder: both measure a failure of a scalar orthant/chamber identification to close without an extra residual series.

No quantitative numerical table of the fibre coefficients α, β, ρ has been recovered from the repository under the present search. Linear correlation of the Fricke samples of C against concrete ρ values therefore cannot yet be performed. L-B stays qualitative: C is the natural residual object that accounts for the torsion mass left after the cone series is completed.

Vector packaging of the triple (H_s, C, P_orth) against the signed pairings of the 9 Maths chain is consistent with the residual geometry but has not produced a new closed identity beyond P_orth = H_s + C.

---

## 3. L-C status (s = 8 Appell limit)

### Locked

- Second Appell term of h_{2,8,8} vanishes as y → q^8:
  j(y; q^8) vanishes to first order while m(−q^{−1}, q^6, −1) remains finite (pole locus 6r = 1 has no integer solution).
- First term is independent of y after residual specialisation x = q and equals
  j(q; q²) m(q^{16}, q^{24}, −1).

### Open

Finite limit of the theta-correction piece
θ_{2,8,8}(q, y, q) / (J̄_{0,24} J̄_{0,6})
as y → q^8. Until that limit is established (or interpreted as a principal value), the residual Appell expression for the path-count series at s = 8 is incomplete.

Nothing in the s = 8 Appell analysis supplies a scalar residual transformation law for the Euler series g_s or for C itself.

---

## 4. L-D status (characteristic scan)

### Locked

Natural characteristic of the affine exponent:
chi_nat(s) = ( s / (2(s − 2)) , −1/(s − 2) ).

| s  | chi_nat          |
|----|------------------|
| 7  | (7/10, −1/5)     |
| 8  | (2/3, −1/6)      |
| 11 | (11/18, −1/9)    |

For s = 7 the shift is equi-paired to both locked cones: B(c1, chi_nat) = B(c2, chi_nat) = 7/2. It absorbs the linear term of Q_s so that
Q_s(v) = (1/2)(v + chi_nat)^T M (v + chi_nat) + 7/20.
Verification on sample lattice points (including mixed signs) passes.

Evaluating the weight function at the shifted points resolves the k-axis wall but does not make the resulting signed series equal to P_orth. Therefore chi_nat is the distinguished exponent characteristic; it is not, by itself, a cone realignment that absorbs C.

### Open under L-D

Prior moderate-growth candidates χ = (1/7, 0) and χ = (1/2, 0) do not absorb C. A systematic scan of residual characteristics (including shifts of the form chi_nat + lattice vector or characters on the discriminant group of M) that would make the holomorphic projection of a single completed series equal to P_orth remains open. No such χ has been exhibited.

---

## 5. Hygiene corrections locked by the pursue-all

- P_orth, P_Euler and g_s are three distinct series. First orthant-versus-Euler mismatch occurs at degree 14; first g-versus-orthant mismatch at degree 7.
- Q_s (affine) is distinct from the homogeneous quadratic form Q_M = v^T M v.
- The s = 7 cone pair produces uniform interior weight 1. The candidate pairs listed for s = 8 and s = 11 do not copy that pattern; interior weights for those candidates are not uniformly 1. Do not quote them as recovering the orthant.
- Axis weights for s = 7 are not uniformly 1/2: positive n-axis has w = 1, positive k-axis has w = 1/2. After the axis pairing the net coefficients are integers (or 1.5 at the origin).

All of the above are residual discrete arithmetic facts. Residual packaging provenance Pack+(S) only.

---

## 6. Remaining exact steps for closure of a residual law for C

1. Construct a residual period-function or false-theta (weight 1/2) whose support is compatible with C_axis + C_third and whose Fricke transforms reproduce the residual samples under continuous extension off ℚ.
2. Recover or restate the precise weight-1/2 Fricke slash and radial prescription used for the published samples so that numerical matching becomes rigorous.
3. Finish the finite-limit analysis of the s = 8 theta-correction piece (L-C).
4. Continue the characteristic scan for a residual χ that absorbs C into a single Zwegers-type sum (L-D), testing in particular shifts around chi_nat.
5. If concrete numerical values of the fibre remainder ρ become available, perform the linear correlation (L-B).

Until step 1 is completed, the residual law for C remains open. No continuum claims. No classical identification of C is required or claimed. RESIDUAL_CORE_FREEZE and all prior Category A locks (packaging identities, Zwegers completion of H_s, residual discrete core through A5+) remain intact.

---

**Status code:** `PURSUE_ALL_C_CLOSURE_STATUS_2026-08-23`  
**Residual law for C:** open  
**New Category A locks under this pursue-all:** C_axis identity, chi_nat, axis pairing, s = 8 second Appell vanishing, coefficient value set and third-quadrant support verified by script.  
