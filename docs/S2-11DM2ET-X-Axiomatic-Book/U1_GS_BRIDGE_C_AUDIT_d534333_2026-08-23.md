# U1-GS-BRIDGE-C Audit of Master d534333 Residual Bridge Series C

PURE MATH. Residual Discrete Algebra (539 as COUNT of leftover pieces) is not Resonant Algebra (18+521 hard schedule). A count is not a clock. Free T3 short. Residual leftover combinatorics CLOSED. U1-DNE terminal at K+. Residual P stays S5. Q4 stays imported D5. Continuum ARCHIVE. Residual-flux provenance mandatory. Do not reopen residual Cat A. Do not import evenness. Do not treat 539 as a free-map stop.

Do NOT redo named E1-E4 constructions. Do NOT redo U1-GS-ZWEGERS (1d8e558), U1-GS-QM (517acae), U1-GS-RADIAL (f768a4f), U1-GS-TL-AUDIT (3ba542e), or U1-GS-LOCK-AUDIT (eaa0107) as if unwritten. Those already lock: Euler-weighted P_s is not the unsigned orthant sum (mismatch from degree 7); mixed-scale Euler series is not Zwegers congruence-subgroup input; 25ed7ea is not a theorem. Cat B wrap ARCHIVE. RESIDUAL_CORE_FREEZE still holds.

ONE target: Master d534333 defines C := P_orth - H_s where P_orth is the UNSIGNED orthant sum and H_s is the cone-weighted lattice series. That C is a new residual object. It is not Euler P_s.

Cite: eaa0107, 3ba542e, 1d8e558, 517acae, f768a4f. Do not cite 25ed7ea or 3e3b461 modular lock as theorems.

---

## 0. Notation lock (mandatory)

- Euler P_s := (-q^s ; q^s)_infty * g_s = the weighted double-sum with denominators 1/(q^s ; q^s)_k .
- P_orth := the unsigned orthant sum sum_{n,k >= 0} q^{Q_s(n,k)} .
- H_s := the cone-weighted full-lattice series sum_{v in Z^2} w(v) q^{Q_s(v)} .
- C := P_orth - H_s .

d534333 writes "P_s" for the unsigned orthant sum. That usage conflicts with the locked Euler notation of eaa0107 and 3ba542e. In this audit the symbol P_s is reserved for the Euler-weighted series; the orthant sum is written P_orth. The identity in d534333 is therefore the residual identity

P_orth = H_s + C .

It does not identify Euler P_s with anything. Coefficient mismatch between Euler P_s and P_orth begins at degree 7 (eaa0107) / degree 14 under the alternate expansion of 3ba542e. The mismatch is already locked; it is not reopened here.

Residue support of the quadratic form and the matrix M_s may stay as form data. No N_flux, f_max, T3, wrap/DE, or Resonant 18+521 schedule is imported into the series statements.

---

## 1. Explicit residual series for C (s = 7)

Lattice data (locked residual, Pack+(S) only):

M = [[2, s], [s, s]], s = 7, signature (1,1), det = -35.

Q_7(n,k) = n^2 + 7 n k + (7/2) k(k+1) .

Negative-norm cones: c1 = (-1,1), c2 = (-4,1) .

Sign weight: w(v) = (1/2) (sgn B(c1,v) - sgn B(c2,v)) .

The lattice formula already written in d534333 is exact:

C = sum_{v in orthant} (1 - w(v)) q^{Q(v)}  -  sum_{v not in orthant} w(v) q^{Q(v)} .

Region decomposition (verified by direct enumeration through degree 50):

- Origin: contribution 1.5 .
- Interior orthant points: w = 1, contribution 0 .
- Orthant axes: w = 1/2, contribution 1/2 per axis point; after clearing the half-weights the net coefficients on pure axis degrees become integers 0 or 1 .
- Exterior points carrying w = -1: contribution +1 .
- All other exterior points: contribution 0 .

Observed coefficients of C through degree 50 take values only in the set {0, 1, 1.5}. Support of the non-zero coefficients is the union of

1. residual axis degrees (squares together with the 7-triangular numbers that arise on the axes), and
2. exterior chamber degrees (explicit low examples: 8, 18, 22, 30, 39, 42, 43, 44, 49, ...).

No independent closed form (classical unary theta product, single false-theta series, or eta-quotient expression) that reproduces these coefficients was found or claimed. The lattice-weight difference formula is therefore the explicit residual series expression for C. It is a rewrite of P_orth - H_s and nothing more; there is no further simplification locked.

Status on evaluable item 1: lattice formula is the explicit residual series (axis + exterior support). Locked as rewrite-only; no independent closed form.

---

## 2. Residual law for C alone

d534333 records approximate Fricke samples of a putative period function h_C at the points 1/7, 3/7, 5/7, 1 (weight 1/2 slash, radial parameter rho = 0.995). Those samples are numerical observations only.

A residual law (false-theta expression, or quantum-modular cocycle with controlled real-analytic extension off Q) is not supplied. The exact missing analytic step is:

- either an explicit false-theta (or residual indefinite series) whose Fricke transforms reproduce the observed samples and whose growth permits continuous extension, or
- a rigorous integral representation of a period function for the difference series C (analogous to the Eichler integral of a unary shadow) that is shown to converge and to match the radial limits on a dense set of rationals.

Until that step is written, the residual law for C alone is unavailable. Approximate samples do not constitute a law.

Because P_orth is not Euler P_s, even a completed law for C would yield modular information only for the orthant series. It would not by itself supply a scalar transformation law for Euler g_s or for Euler P_s. No such claim is made.

Status on evaluable item 2: residual law for C locked unavailable; missing step is the analytic continuation / explicit false-theta or period-function construction described above.

---

## 3. Hygiene and non-flattening

C is a residual discrete object measuring the orthant-versus-cone mismatch on the indefinite lattice M. It may contact residual arithmetic (residue support of Q mod 7, chamber geometry of M) as form data. It is not flattened into the Resonant Algebra schedule 18+521, nor is it used to identify Euler P_s with a classical or residual modular object. The 9 Maths filter notes in the companion file of d534333 correctly treat C as residual-admissible under NSFA / TTC / RTTC / RNT without requiring classical unary identification; that residual-admissibility statement is left untouched. No continuum language, no free-map termination claim, and no reopening of residual Category A closures appear.

---

## 4. Summary of locks from this audit

- Notation: P_orth (unsigned orthant) distinct from Euler P_s (weighted). C := P_orth - H_s is a new residual object.
- Explicit series: lattice-weight difference formula with axis + exterior support is the explicit residual expression; locked as rewrite-only, no independent closed form.
- Residual law for C: unavailable. Exact missing step is a completed period function or explicit false-theta for the difference series.
- No scalar transformation law for Euler g_s is obtained via P_orth = H_s + C.
- Prior GS locks (1d8e558, 517acae, f768a4f, 3ba542e, eaa0107) remain in force and are cited. 25ed7ea and 3e3b461 modular claims stay non-theorems.

Status code: U1_GS_BRIDGE_C_AUDIT_d534333_REWRITE_ONLY_LAW_UNAVAILABLE

Residual Discrete Algebra is leftover pieces. Resonant Algebra is how long you stir. Free T3 short. Continuum ARCHIVE. A count is not a clock. Residual-flux provenance mandatory.

*End of U1-GS-BRIDGE-C audit. 2026-08-23.*
