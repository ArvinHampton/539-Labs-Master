# Residual Period-Function / False-Theta Construction Attempt for Bridge Series C

Date: 2026-08-23  
Scope: Category A residual discrete only. Pack+(S) provenance mandatory. Residual-flux provenance mandatory. Continuum language excluded. Notation lock: C := P_orth − H_s.

This note records the systematic attempt to construct a residual period-function or false-theta of weight 1/2 for the residual law of C, as required by the open step of Open_Paths_C_Closure_Continuation_2026-08-23.md and Pursue_All_C_Closure_Status_2026-08-23.md.

No construction that satisfies both the support condition and the Fricke continuous-extension condition has been obtained. The residual law for C remains open.

---

## 1. Target

A residual series F of weight 1/2 such that:

1. The q-expansion of F agrees with the locked coefficients of C = C_axis + C_third (at least through moderate degree, and ideally identically).
2. The Fricke transforms of F (under a weight-1/2 slash) reproduce, or continuously extend, the residual samples previously recorded for C.
3. F admits a continuous extension of its residual cocycle off the rationals (RTTC requirement).

Locked arithmetic of the target:

C_axis = 3/2 + ∑_{n≥1} q^{n²} + ∑_{k≥1} q^{7 k(k+1)/2}

C_third = ∑_{n≥1} ∑_{k≥1} q^{n² + 7 n k + (7/2) k (k − 1)}

(The quadratic on the negative orthant is verified against the lattice definition.)

---

## 2. Candidates tested and results

### 2.1 Unary partial-theta products

Products of the form (∑ q^{n²}) · (∑ q^{(7/2)k(k−1)}) or similar fail because they lack the cross term 7 n k. Coefficient mismatch is immediate (degrees and multiplicities diverge by degree 30). Ruled out.

### 2.2 Alternating or signed unary series

Candidates of the form ∑_{m∈ℤ} sgn(m + a) q^{Q_1(m)} on one-dimensional projections of M (conductor related to 7 or 35) produce coefficient sequences that do not match the irregular exterior support of C_third. Ruled out at low degree.

### 2.3 Lattice false-theta with residual sign

Any series of the schematic form ∑_{v∈ℤ²} ε(v) q^{Q(v)}, where ε is a residual sign or character on M, was examined against the region decomposition of C. When ε is taken from the locked cones one recovers (a multiple of) H_s, not C. When ε is taken to be the orthant indicator one recovers P_orth, whose difference from H_s is C by definition; this does not supply an independent modular object. No residual character on the discriminant group of M was found that converts the cone series into the orthant series. Open.

### 2.4 Eichler-integral / period candidates

Classical weight-1/2 forms arise as Eichler integrals of weight-3/2 unary theta series. Numerical probes with residual analogues of the characters (·/5), (·/7), (·/35) on the discriminant form of M do not interpolate the qualitative Fricke samples of C (consistent with earlier negative results recorded for the related series g_7). The exact residual shadow of the (1,1)-theta that would be needed for a rigorous Eichler construction of C has not been identified. Open.

### 2.5 Appell–Lerch specializations

Specializations of Appell–Lerch sums that reproduce double sums of type ∑∑ q^{n² + 7 n k + (7/2)k(k−1)} were sought. No identity that isolates the third-quadrant contribution while remaining residual-admissible under the 9 Maths chain was obtained. (The s = 8 Appell analysis remains independent and does not close the s = 7 exterior series.) Open.

---

## 3. Structural obstruction and refined residual candidate

Classical Zwegers theory supplies a modular completion of the cone series H_s. Because C = P_orth − H_s, a modular completion of C is equivalent to a modular (or quantum-modular) completion of the orthant path-count series P_orth itself.

The coordinate orthant is not a negative-norm cone for the bilinear form of M. That is the geometric origin of the residual bridge C. Consequently the standard Zwegers construction does not apply directly to P_orth, and the residual object C measures precisely the failure of the orthant to be a Zwegers cone.

The natural residual candidate object is therefore the series C itself, viewed as a residual partial indefinite theta series of weight 1/2 on the lattice M:

Θ_C(τ) := C_axis(q) + C_third(q)

(with q = e^{2π i τ}). C_axis is already a sum of classical residual partial thetas (known to be quantum modular of weight 1/2). The open construction therefore reduces to a residual / quantum-modular completion of the partial indefinite theta series

Θ_third(τ) := ∑_{n,k≥1} q^{n² + 7 n k + (7/2) k (k − 1)}

that matches the Fricke samples of C under continuous extension off the rationals.

No explicit closed-form completion (Appell identity, Eichler integral of a known residual shadow, or classical false-theta identity) has been identified that satisfies both the coefficient support and the sample conditions.

---

## 4. Status

- Arithmetic of C is fully explicit and locked (C_axis + C_third).
- No residual period-function or false-theta of weight 1/2 that matches both the support of C and the residual Fricke samples under continuous extension has been constructed.
- The residual law for C remains open.
- The classical residual transformation law for H_s (Zwegers) is independent and remains locked.
- RESIDUAL_CORE_FREEZE, Pack+(S) provenance, and residual-flux provenance continue to hold.

Next concrete levers remain those already recorded: recovery of the exact weight-1/2 Fricke slash, further residual characters or characteristics around chi_nat, identification of the residual shadow of the (1,1)-theta that would feed an Eichler integral for C, and continued search for residual Appell or false-theta identities that isolate the third-quadrant double sum.

---

**Status code:** `RESIDUAL_FALSE_THETA_CONSTRUCTION_ATTEMPT_C_2026-08-23`  
**Construction status:** no matching residual period / false-theta obtained  
**Residual law for C:** still open  
