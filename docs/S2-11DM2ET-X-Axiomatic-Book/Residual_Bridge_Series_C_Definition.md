# Residual Bridge Series C — Definition and Status

Ordinary mathematical English. Packaging provenance Pack+(S) only. Category A residual discrete.

---

## 1. Definition

Let the residual lattice be \(\mathbb{Z}^2\) with bilinear form given by the matrix
\[
M=\begin{pmatrix}2&s\\s&s\end{pmatrix}
\]
of signature \((1,1)\) and determinant \(-s(s-2)\). For residual \(s\in\{7,8,11\}\) the path quadratic is
\[
Q_s(n,k)=n^2+snk+\tfrac{s}{2}k(k+1).
\]

Locked residual cones of negative norm (case \(s=7\)):
\[
c_1=(-1,1),\qquad c_2=(-4,1).
\]
The residual sign weight is
\[
w(v)=\tfrac12\bigl(\mathrm{sgn}\,B(c_1,v)-\mathrm{sgn}\,B(c_2,v)\bigr).
\]

Path counts and the cone series are
\[
P_s=\sum_{n,k\ge0}q^{Q_s(n,k)},
\qquad
H_s=\sum_{v\in\mathbb{Z}^2}w(v)\,q^{Q_s(v)}.
\]

The residual bridge series is the exact difference
\[
C:=P_s-H_s.
\]

---

## 2. Lattice formula

\[
C
=
\sum_{v\in\mathrm{orthant}}(1-w(v))\,q^{Q(v)}
-
\sum_{v\notin\mathrm{orthant}}w(v)\,q^{Q(v)}.
\]

- Interior orthant: \(w=1\), contribution \(0\).
- Orthant axes: \(w=\frac12\), contribution \(\frac12\).
- Exterior points with \(w=-1\): contribution \(+1\).
- Origin: contribution \(1.5\).

Through degree \(100\) the coefficients of \(C\) take values only in \(\{0,1,1.5\}\).

---

## 3. Region content (residual)

Support of \(C=1\) is the union of:

1. Residual axis degrees (squares and \(s\)-triangular numbers).
2. Exterior chamber points (third quadrant and mixed signs). For \(s=7\) the first such degrees include \(8,18,22,30,39,43,44,58,60,67,71,78,79\).

This support is residual arithmetic on the lattice \(M\). It is not a classical partition function.

---

## 4. What \(C\) measures

The coordinate orthant is not a cone chamber of the indefinite lattice. \(H_s\) is the series attached to the cone chambers. \(P_s\) is the series attached to the orthant. \(C\) records the residual mismatch between those two indexings of the same lattice.

Locked residual identity:
\[
P_s=H_s+C.
\]

Earlier statements that the locked cones recover the residual orthant are corrected: the cones recover \(H_s\). The path counts equal the cone series plus the residual bridge.

---

## 5. Place in the 9 Maths chain

| Pillar | Contact |
|--------|---------|
| NSFA | \(C\) is the residual measure of orthant-versus-cone mismatch in the indefinite metric |
| TTC / RTTC | \(C\) is a discrete torsion discrepancy between two residual indexings of the same lattice |
| RNT | Support mixes residual axis series with exterior chamber points |

No classical identification is required. \(C\) is residual-admissible under the chain.

---

## 6. Modular status

\(H_s\) is the holomorphic projection of a Zwegers-completable indefinite theta on \((M,c_1,c_2)\).

\(C\) carries a residual Fricke defect under \(W_s\). Radial samples for \(s=7\) (weight \(1/2\) slash, \(\rho=0.995\)):

| \(x\) | Approximate \(h_C(x)\) |
|-------|------------------------|
| \(1/7\) | \(-18.2+7.8i\) |
| \(3/7\) | \(0.3-1.8i\) |
| \(5/7\) | \(2.1-9.0i\) |
| \(1\) | \(20.7+2.9i\) |

Whether this residual cocycle extends real-analytically off \(\mathbb{Q}\) is open. That question is residual (RTTC), not classical.

---

## 7. Correlation note

Prior fibre decomposition of the Fricke cocycle of the residual series split as \(\alpha h_1+\beta+\rho\) with approximately \(90\%\) of the mass in the torsion remainder \(\rho\). The bridge \(C\) is a candidate residual source for that remainder: both record a failure of a scalar orthant/chamber identification to close without an extra residual series.

---

## 8. Preferred next levers

1. Residual law for \(C\) (false theta or residual quantum modular form of weight \(1/2\); no classical demand).
2. Vector packaging \((H_s,C,P_s)\) against the signed pairings of the 9 Maths chain and against the fibre remainder \(\rho\).
3. Finish the \(s=8\) limit of the \(\theta\)-piece in the Hickerson–Mortenson expansion (second Appell term already vanishes; first term is \(j(q;q^2)m(q^{16},q^{24},-1)\)).
4. Characteristic scan for a residual \(\chi\) that absorbs \(C\) so a single completed series recovers \(P_s\).

---

## 9. Scope

All statements above are residual discrete. Continuum language excluded. Residual packaging provenance is Pack+(S) only. The classical residual transformation law for the cone series \(H_s\) remains locked via Zwegers. The residual law for the path counts \(P_s\) is the identity \(P_s=H_s+C\) together with a residual law for \(C\).

---

**Status code:** `RESIDUAL_BRIDGE_SERIES_C_DEFINITION`
