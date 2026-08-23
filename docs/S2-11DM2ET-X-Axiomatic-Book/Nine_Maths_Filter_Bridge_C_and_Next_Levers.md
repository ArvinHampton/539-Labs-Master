# Nine Maths filter on the bridge series and next levers

Ordinary mathematical English. Packaging provenance Pack+(S) only.

---

## 0. Correction of scope

The bridge series \(C=P_s-H_s\) is **not required to be a classical unary theta**. It is a residual object. Demanding a classical closed form was an unnecessary restriction. New residual series are admissible under the 9 Maths chain (especially NSFA, RNT, TTC/RTTC).

---

## 1. Theorem–lemma chain (9 Maths) — relevant contacts

| Pillar | Content that contacts the present series |
|--------|------------------------------------------|
| 1 TTC | Discrete torsion on residual cores; cocycles |
| 2 NSFA | Indefinite-metric functionals; signature \((1,1)\) lattice \(M\) |
| 3–4 BMMT/HMT | Residual measures on cores and chambers |
| 6 RNT | Integer pairings, linking, residue support mod 7 |
| 7 RTTC | Resonant enrichment of torsion cocycles; period functions |
| 8 ROT | Even/odd modes; sub-harmonic envelopes |
| 9 MCP | Phase sectors (weakest contact here) |

Vector structure already recorded in programme work: signed pairings \(1\leftrightarrow7\), \(2\leftrightarrow9\), \(3\leftrightarrow4\), \(5\leftrightarrow8\), \(6\leftrightarrow6\); even/odd eigenspaces; fibre split of cocycles with a large torsion remainder.

---

## 2. Filter of current objects through the chain

**Lattice \(M=\bigl(\begin{smallmatrix}2&7\\7&7\end{smallmatrix}\bigr)\), \(\det=-35\).**  
Pure NSFA: indefinite metric of signature \((1,1)\). Locked.

**Cones \(c_1=(-1,1)\), \(c_2=(-4,1)\).**  
Negative-norm vectors defining chambers in the NSFA geometry. Locked.

**Sign series \(H_s\).**  
Holomorphic projection of the cone-chamber series. Zwegers-completable. Prior lock.

**Path counts \(P_s\).**  
Orthant sum. Exact binomial form \((a,b,c)=(2,s,s)\). Locked. The orthant is **not** a cone chamber.

**Bridge \(C=P_s-H_s\).**  
Exact lattice formula:
\[
C=\sum_{\mathrm{orthant}}(1-w(v))q^{Q(v)}-\sum_{\mathrm{exterior}}w(v)q^{Q(v)}.
\]
Region decomposition:
- origin: \(C(0)=1.5\)
- orthant axes: half-weights (squares and \(s\)-triangular)
- negative \(n\)-axis: full squares
- third quadrant and mixed exterior: weight \(-1\) points at degrees \(8,18,22,30,39,\ldots\)

**Interpretation under NSFA/TTC.**  
\(C\) is the residual measure of the mismatch between the coordinate orthant and the cone chambers of the indefinite lattice. It is not a defect in the classical sense; it is the residual object that records that mismatch. Under RTTC it is a discrete torsion discrepancy between two residual indexings of the same lattice.

**Contradiction corrected.**  
Earlier residual notes that claimed the locked cones “recover the residual orthant” overstated the fact. They recover \(H_s\). The identity is \(P_s=H_s+C\). That is the accurate residual statement.

**Missed correlation.**  
The fibre decomposition of the Fricke cocycle (prior work) split as \(\alpha h_1+\beta+\rho\) with \(\sim90\%\) torsion mass in the remainder \(\rho\). The bridge \(C\) is a candidate residual source for that torsion remainder: both measure a failure of a scalar orthant/chamber identification to close without an extra residual series.

**Pattern.**  
Support of \(C=1\) is the union of  
(1) residual axis series (RNT residue data mod 7),  
(2) exterior chamber points (NSFA opposite chamber).  
No classical unary product is required for this pattern to be residual-admissible.

---

## 3. What is ruled out vs what is open

| Claim | Status |
|-------|--------|
| \(C\) must be a classical unary theta | Ruled out as a requirement; also fails coefficient match |
| \(C\) is a residual NSFA/TTC series | Consistent with the chain; adopted |
| Cones recover the orthant | False; corrected to \(P=H+C\) |
| Zwegers completes \(H\) | Locked |
| Zwegers completes \(P\) directly with these cones | False |
| Scalar residual transformation law for \(g_s\) via \(P=H+C\) | Open until \(C\) has its own law |

---

## 4. Next levers (filtered)

**L-A. Residual law for \(C\).**  
Treat \(C\) as a residual false theta or residual quantum modular form of weight \(1/2\) on the same lattice. Compute its Fricke samples and seek a cocycle (RTTC) without demanding classical identification.

**L-B. Vector packaging.**  
Package \((H_s,\,C,\,P_s)\) (or \((g_s,H_s,C)\)) as components of a residual vector-valued object compatible with the signed pairings of the 9 Maths chain. Test whether the fibre remainder \(\rho\) is linearly related to radial limits of \(C\).

**L-C. \(s=8\) Appell limit.**  
Second term of \(h_{2,8,8}\) vanishes; first term is \(j(q;q^2)m(q^{16},q^{24},-1)\). Confirm the \(\theta\)-piece limit and write the residual Appell expression for \(P_8\).

**L-D. Cone/characteristic search for direct \(P\).**  
Search residual characteristics \(\chi\) such that the completed series with locked cones has holomorphic projection equal to \(P_s\) (absorbing \(C\)). Prior moderate-growth candidates: \(\chi=(1/7,0)\), \(\chi=(1/2,0)\).

---

## 5. Immediate pursuit order

1. L-A: Fricke samples of \(C\) and first cocycle probe.  
2. L-B: correlation of those samples against the prior fibre remainder \(\rho\).  
3. L-C: finish \(s=8\) \(\theta\)-limit.  
4. L-D: characteristic scan for direct \(P\).

No continuum language. Residual packaging Pack+(S) only.

---

**Status code:** `NINE_MATHS_FILTER_BRIDGE_C_AND_NEXT_LEVERS`
