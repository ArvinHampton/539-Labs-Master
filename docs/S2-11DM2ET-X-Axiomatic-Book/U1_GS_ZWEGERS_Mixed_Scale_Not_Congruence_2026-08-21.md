# U1-GS-ZWEGERS Mixed-Scale g_s Is Not Zwegers Congruence-Subgroup Input 2026-08-21

PURE MATH. Residual Discrete Algebra (539 as COUNT of leftover pieces in nine sector cores) ≠ Resonant Algebra (18+521 hard schedule). A count is not a clock. 539 is leftover COUNT. Resonant Algebra is 18+521 as a HARD SCHEDULE. Do not flatten. Free T3 short (Canonical floor map; exact integer on n=3k+2 is (2n−1)/3). Residual leftover combinatorics CLOSED. U1-DNE terminal at K+. Residual P stays S5. Q4 stays imported D5. Continuum ARCHIVE. Residual-flux provenance mandatory. Do not reopen residual Cat A. Do not import evenness. Do not treat 539 as a free-map stop. Do not redo named E1–E4 constructions. RESIDUAL_CORE_FREEZE still holds for the discrete core.

Cite: Transformation_Law_STATUS_CORRECTION_2026-08-21.md (06084d0). Do not cite Transformation_Law_CLOSED as a theorem. Do not put N_flux, f_max, 18+521, fibre 67/68, or T3 into the q-series theorem.

## The series (locked)

For each positive integer s,
\[
g_s(q)=\sum_{n=0}^\infty \frac{q^{n^2}}{(-q^s;q^s)_n}.
\]
This is not f_0(q^s). The fifth-order mock theta is f_0(q)=\sum q^{n^2}/(-q;q)_n; the level insertion f_0(q^s) has quadratic exponents s n^2. Here the quadratic exponent is n^2 (scale 1) while the Pochhammer runs in base q^s (scale s). Mixed scale.

## Proved Euler double-sum (locked, 2026-08-21)

\[
P_s(q):=(-q^s;q^s)_\infty\, g_s(q)
=\sum_{k=0}^\infty \frac{q^{s k(k+1)/2}}{(q^s;q^s)_k}\sum_{n=0}^\infty q^{n^2+s k n}.
\]
Proof is classical Euler (Pochhammer splitting + Euler's (z;q)_\infty expansion). Absolute convergence in |q|<1. Phi collapse \Phi(m;q)=(q^{m+1};q)_\infty is likewise classical. Residue vanishing: coefficients of g_s vanish off squares modulo s (proved; for s=7 the surviving classes are {0,1,2,4}).

## 1. Quadratic form, cone, character from the double-sum

The exponent in the double sum is the quadratic polynomial
\[
Q_s(n,k)=n^2+s k n+\frac{s}{2}k(k+1)=n^2+s k n+\frac{s}{2}k^2+\frac{s}{2}k.
\]
Homogeneous quadratic part: matrix of the associated bilinear form
\[
B_s=\begin{pmatrix}1& s/2\\ s/2& s/2\end{pmatrix},\qquad\det B_s=\frac{s}{2}-\frac{s^2}{4}=\frac{s(2-s)}{4}.
\]
For s>2 one has det B_s<0, so signature (1,1): indefinite.

For s=7:
\[
Q_7(n,k)=n^2+7 k n+\frac{7}{2}k^2+\frac{7}{2}k,\qquad B_7=\begin{pmatrix}1&7/2\\7/2&7/2\end{pmatrix},\qquad\det B_7=-\frac{35}{4}.
\]
Summation domain: the closed nonnegative orthant n\ge0, k\ge0. There is no written character beyond the trivial one on that orthant; the factors 1/(q^s;q^s)_k are not absorbed into a pure lattice theta character.

Completing the square in n:
\[
Q_s(n,k)=\Bigl(n+\frac{s k}{2}\Bigr)^2+\frac{s(2-s)}{4}k^2+\frac{s}{2}k.
\]
Signature statements after expanding a third Pochhammer remain rewritings of the same identity. They do not by themselves produce Zwegers input.

## 2. Lock: not Zwegers-on-a-congruence-subgroup

The Euler double-sum does not supply Zwegers input of congruence-subgroup type for g_s.

Zwegers' classical completion takes unary (or lattice) indefinite theta series
\[
\sum_{v\in L\cap C}\psi(v)\,q^{Q(v)}
\]
over a lattice L with quadratic form Q of signature (1,1) (or (n,1)), a cone C, and a character ψ, and produces a non-holomorphic modular form on a congruence subgroup whose holomorphic part is that theta series.

The double-sum for P_s is not of that shape:

- It carries Pochhammer denominators (q^s;q^s)_k in the k-sum. Those denominators are generating functions for partitions into parts divisible by s; they are not lattice theta characters.
- The quadratic scale in n is 1 while the Pochhammer and the k-quadratic run at scale s. This is mixed scale, not a level insertion of f_0 into Γ_0(N).
- The sum is restricted to the orthant n,k\ge0 with an extra 1/(q^s;q^s)_k weight; it is not a sum over a full lattice cut by a pair of opposite cones in the Zwegers sense.

Therefore g_s (and P_s) is not the holomorphic part of a weight-1/2 harmonic Maass form on a congruence subgroup obtained by the classical Zwegers indefinite-theta completion from the Euler double-sum alone.

If g_s is modular in any completed sense, the appropriate class is partial theta / quantum modular (radial limits at roots of unity), not harmonic Maass forms on congruence subgroups. Harmonic Maass and quantum modular are different; the double-sum alone selects neither as a theorem. The obstruction above rules out the congruence-subgroup Zwegers route from this input.

## 3. Holomorphic projection recovery

Line-by-line recovery of g_s as the holomorphic projection of a completed non-holomorphic form is unwritten.

Reason: the Zwegers lattice data (quadratic form on a full lattice, cone pair, character, and the error-function completion) are not supplied by the Euler double-sum. Without those data there is no completed form whose holomorphic projection could be checked against g_s term by term. The double-sum is a holomorphic identity only.

## 4. What is proved and what is not

Proved (2026-08-21 status correction):
- Euler double-sum for P_s.
- Φ collapse.
- Residue vanishing of g_s off squares modulo s (in particular for s=7).

Not proved:
- g_s is the holomorphic part of a harmonic Maass form on a congruence subgroup.
- g_s is quantum modular of weight 1/2.
- Level, multiplier, and shadow for any s.

Mechanism language only: after Euler collapse, g_s admits a Hecke-type / partial-theta double-sum representation. Objects of that shape appear among inputs to Zwegers-type completions and to Appell–Lerch dictionaries. That is a research programme, not a theorem that g_s transforms.

## Hygiene

Do not put N_flux, f_max, 18+521, fibre 67/68, or T3 into the q-series theorem. Do not cite Transformation_Law_CLOSED as a theorem. Cite Transformation_Law_STATUS_CORRECTION_2026-08-21. Residual Discrete Algebra is leftover pieces. Resonant Algebra is how long you stir. Free T3 short. Continuum ARCHIVE. A count is not a clock. Residual-flux provenance mandatory.

*End of U1-GS-ZWEGERS note. 2026-08-21.*
