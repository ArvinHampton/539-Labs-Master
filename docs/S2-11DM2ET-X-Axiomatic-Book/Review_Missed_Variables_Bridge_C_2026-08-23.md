# Review of missed variables, correlations, patterns, and contradictions — Bridge C

Ordinary mathematical English. Packaging provenance Pack+(S) only. Category A residual discrete. Continuum ARCHIVE. Residual-flux provenance mandatory. Do not reopen residual Cat A. Do not treat 539 as a free-map stop.

Target: Master d534333 (C definition) together with the U1-GS-BRIDGE-C audit 1b0927c, the lever notes of 2026-08-23, Cone_Vectors 2026-08-22, Residual_Exact_Identity, HM / Appell notes, and the locked GS audits eaa0107, 3ba542e, 1d8e558, 517acae, f768a4f. Do not cite 25ed7ea or 3e3b461 as theorems.

Companion lock: `C_Axis_Pairing_and_Natural_Characteristic_2026-08-23.md`.

---

## 0. Verdict in one paragraph

The bridge series C is a real residual object, but several symbols were being used for two different things, two different comparisons were being quoted as one mismatch, the s=8 Appell second term was described in contradictory ways, and the s=8 / s=11 cone candidates were over-identified with the s=7 sign pattern. Direct enumeration through degree 80 (and mixed-sign search through degree 293) corrects the coefficient story without changing the identity C = P_orth - H_s. The missed structural variable is the affine linear piece (s/2)k inside Q_s: it forces a natural characteristic chi_nat = (s/(2(s-2)), -1/(s-2)) that makes the exponent quadratic, but that same shift does not make the coordinate orthant a Zwegers chamber for the locked cones. C is the residual of that affine-versus-homogeneous mismatch. No scalar transformation law for Euler g_s is obtained.

---

## 1. Missed variables (notation collisions)

These collisions are now locked as distinct.

| Symbol as used | Object A | Object B | Collision |
|----------------|----------|----------|-----------|
| P_s | Euler series (-q^s ; q^s)_infty * g_s (eaa0107, 3ba542e, U1 1b0927c) | unsigned orthant sum (d534333, Residual_Exact_Identity, Binomial_Hecke) | same letter, not equal (first mismatch of Euler P vs orthant at degree 14) |
| Q | path charge Q_s(n,k) = n^2 + s n k + (s/2) k(k+1) (affine) | homogeneous Q_M(v) = v^T M v | Cone_Vectors reports Q_M for s=7 (c1 maps to -5, c2 maps to -17) and Q_s for s=8,11 (c1 maps to -4 and -7). Same heading, two formulae |
| H_s | cone-weighted series with exponent Q_s, signs evaluated at integer v | holomorphic projection of a standard Zwegers sum on L + chi | shape only; identification not written (25ed7ea remains a non-theorem) |
| mismatch degree 7 vs 14 | g_7 versus P_orth (eaa0107: degrees 7,8,11,16) | Euler P versus P_orth (3ba542e: from degree 14) | both true; they compare different series |

Mandatory notation after this note:

- g_s = sum_{n >= 0} q^{n^2} / (-q^s ; q^s)_n
- P_Euler = (-q^s ; q^s)_infty * g_s
- P_orth = sum_{n,k >= 0} q^{Q_s(n,k)}
- H_s = sum_{v in Z^2} w(v) q^{Q_s(v)}, with w(v) = (1/2)(sgn B(c1,v) - sgn B(c2,v)) and B(v,w) = v^T M w
- C = P_orth - H_s
- Q_s affine path charge; Q_M = v^T M v homogeneous. Never reuse Q for both.

The identity written in Residual_Exact_Identity and in 25ed7ea,

P_orth = P_Euler,

is false. Direct coefficients for s=7: they agree through degree 13 and first disagree at degree 14 (P_orth has 0, P_Euler has 1). That is the 3ba542e mismatch. The eaa0107 mismatch at 7,8,11,16 is g_7 against P_orth, not P_Euler against P_orth.

---

## 2. Contradictions, with address

### 2.1 Cones recover the orthant

Cone_Vectors (and 3e3b461) claim that c1 = (-1,1), c2 = (-4,1) recover the positive orthant for s=7, and that the s=8,11 candidate pairs bound the orthant by the same sign pattern.

False for the orthant. True for H_s at s=7 interior: w = 1 at every interior orthant point, so those points cancel in C. The identity is P_orth = H_s + C, already the d534333 correction. C is not zero.

False for s=8 and s=11 as a copy of the s=7 pattern. Direct sign census with the candidate cones:

- s=7, c1=(-1,1), c2=(-4,1): interior w is {1} uniformly; third quadrant w is {-1}; C coefficients through degree 80 lie in {0, 1, 1.5}; C(0) = 1.5.
- s=8, c1=(-2,1), c2=(-4,1): interior w is {0, 1/2}, not {1}; C coefficients include 1/2; C(0) = 1.
- s=11, c1=(-2,1), c2=(-4,1): interior w is {0, 1}, not {1}; C coefficients in {0, 1}; C(0) = 1.

The s=7 pair is distinguished. The s=8 and s=11 candidates are not the same construction. Cone_Vectors overstated that.

### 2.2 Orthant axes all have weight 1/2, and C(0) = 1.5 is mysterious

d534333 and the U1 audit write “orthant axes: w = 1/2, contribution 1/2” and “origin contribution 1.5”, with coefficients of C in {0, 1, 1.5}.

The coefficient set and C(0) = 1.5 are correct for s=7. The axis-weight sentence is not.

For s=7, B(c1,v) = 5n and B(c2,v) = -n - 21k. Hence:

- origin (0,0): w = 0
- positive n-axis (n>0, k=0): w = 1, not 1/2
- positive k-axis (n=0, k>0): w = 1/2
- negative n-axis: w = -1
- negative k-axis: w = -1/2

C(0) = 1.5 because two lattice points share charge 0: (0,0) contributes 1 and (0,-1) has Q_s = 0, w = -1/2, and contributes +1/2. That pairing is systematic: Q_s(0,-t) = Q_s(0, t-1) and Q_s(n,0) = Q_s(-n,0). After pairing, half-weights disappear from the net coefficients and the value set {0, 1, 1.5} is accounted for. Closed form for the axis part is in the companion note.

### 2.3 Exterior support lists

d534333 lists exterior degrees 8,18,22,30,39,43,44,58,60,67,71,78,79. Those are exactly the third-quadrant points of weight -1 through degree 79. Correct as an exterior-only list.

U1 lists 8,18,22,30,39,42,43,44,49 as “exterior chamber degrees”. Degrees 42 and 49 are not exterior: 42 is the k-axis pair (0,3) with (0,-4); 49 is the square 7^2 from the n-axis pair. Classification error in U1; the underlying lattice formula is untouched.

Support of C = 1 through degree 80 is the union of axis degrees {1,4,7,9,16,21,25,36,42,49,64,70,...} with the third-quadrant list. Degree 0 is C = 1.5, not 1.

### 2.4 “Third quadrant and mixed signs”

d534333 describes the exterior support as third quadrant and mixed signs. Mixed-sign points with nonzero w exist, but not in the listed range. First mixed-sign nonzero weight is at Q_s = 294, on the cone wall B(c2,v) = 0. First mixed-sign weight +/- 1 is at Q_s = 330 and 337. Through degree 293 the exterior of C is third quadrant only. The phrase “mixed signs” is eventual support, not a description of the degree-100 examples.

### 2.5 s=8 Appell second term

Next_Levers locks: j(y ; q^8) vanishes, m(-q^{-1}, q^6, -1) is finite, second term of h_{2,8,8} vanishes, first term tends to j(q ; q^2) m(q^{16}, q^{24}, -1).

All_Levers says the product j m remains finite if and only if m has a compensating simple pole, and that the residue is not yet evaluated.

Those cannot both stand. Direct pole check: poles of m(X, q^6, -1) occur when X = -q^{-6 r} (or X = q^{-6 r}, according to the 1 - q^{6 r} X factor). X = -q^{-1} meets neither family, because 6r = 1 has no integer solution. So m is finite, j vanishes, and the second term vanishes. Next_Levers is correct. All_Levers “iff pole” is withdrawn. The first-term identification matches the Hickerson–Mortenson substitution at s=8, x=q, y=q^8. The theta-piece limit remains open.

### 2.6 Fibre remainder rho as source of C

d534333 and the 9 Maths filter call C a candidate residual source for the Fricke fibre remainder rho (about 90 percent torsion mass). That is an analogy of shape, not a computed linear relation between radial samples of C and rho. L-B stays open. No correlation is locked.

---

## 3. Missed correlations and the pattern that addresses them

Q_s is not the quadratic form of M. Expanding,

Q_s(n,k) = (1/2) v^T M v + (s/2) k.

The extra term is the binomial linear piece n + s k after 2 binom(n,2) + s n k + s binom(k,2) is rewritten. Completing the square on the pair of linear conditions

2a + s b = 0, a + b = 1/2

gives the natural characteristic

chi_nat(s) = ( s / (2(s-2)) , -1/(s-2) ).

For s=7 this is (7/10, -1/5). Then

Q_s(v) = (1/2) (v + chi_nat)^T M (v + chi_nat) + 7/20.

Prior characteristic scans used chi = (1/7, 0) and (1/2, 0), and reported that a nonzero second component produces large growth. The geometrically forced point was not the scan target. It is recorded here as a missed variable, not as a working completion.

Further correlation: B(c1, chi_nat) = B(c2, chi_nat) = 7/2. The shift is equi-paired to both locked cones. Evaluating signs at v + chi_nat instead of at integer v resolves the k-axis wall (weight 1/2 becomes 1) and simultaneously drops the positive n-axis out of the chamber (weight 1 becomes 0). So one cannot both (i) make the exponent a pure quadratic on L + chi_nat and (ii) keep the coordinate orthant as the Zwegers chamber of the locked cones. That is why C is forced for these cones. C is not a bookkeeping remainder; it is the residual of the affine path-count exponent versus the homogeneous lattice form.

---

## 4. What this review does not reopen

- Pack+(S) packaging, B' = 539 as a count, fibre table, A0–A2, A4/A5 0-stem, A4+/A5+ on K+.
- No-Go on lambda = ln 3 / 539 from residue democracy. Option 3 paused.
- U1 locks: Euler P_s is not P_orth; mixed-scale Euler series is not Zwegers congruence-subgroup input; residual law for C alone unavailable as a period function or false-theta closed form; no scalar transformation law for Euler g_s via P_orth = H_s + C.
- 25ed7ea and 3e3b461 remain non-theorems.
- Continuum, Resonant 18+521 schedule, N_flux, f_max, T3, wrap/DE stay out of the series statements.

---

## 5. Updated lever list

L-A. Residual law for C (false theta or residual quantum modular of weight 1/2). Still unavailable. Axis pairing below is a lattice identity, not that law.

L-B. Vector packaging (H_s, C, P_orth) against the fibre remainder rho. Still uncomputed.

L-C. Finish the s=8 theta-piece limit. Second Appell term now locked as vanishing; first term locked as j(q ; q^2) m(q^{16}, q^{24}, -1). Theta piece open.

L-D. Characteristic scan for a single completed series equal to P_orth. chi_nat is now the distinguished candidate for the exponent; it is not a demonstrated absorber of C.

L-E (new, hygiene). Keep P_Euler, P_orth, Q_s, Q_M, H_s (integer signs) distinct in every later note. Do not quote Cone_Vectors s=8,11 pairs as copies of the s=7 interior-weight-1 pattern.

---

**Status code:** `REVIEW_MISSED_VARIABLES_BRIDGE_C_2026-08-23`

Cite: 1b0927c, d534333, eaa0107, 3ba542e, 1d8e558, 517acae, f768a4f. Pack+(S) only. RESIDUAL_CORE_FREEZE holds.
