# RH pure Cat A — execution report for all recommended research paths

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. No model constants.  
**Does not prove** RH, M1.2, M1.3, M1.4, or the target lemma.

**Batch script:** `scripts/rh_research_batch.py`  
**Results:** `rh_research_batch_results.json`  
**Date context:** programme continuum 2026-07-30.

---

## 0. Inventory of recommended paths

| ID | Path | Deliverable | Outcome |
|----|------|-------------|---------|
| R1 | Regularised remainder on approach paths | Batch R1 | **Executed** |
| R2 | Multi-\(X\) phase vs \(\log\log X\) | Batch R2 | **Executed** |
| R3 | M1.4 smoothed \(A_X\) | Batch R3 + `RH_M1_4_Smoothing_A_X.md` | **Executed** |
| R4 | L2 on-line vs L3 off-line approach \(\Delta\arg P\) | Batch R4 | **Executed** |
| R5 | Dense \(A_2\) re-check → \(c_1\) | Batch R5 | **Executed** |
| R6 | L4 non-circular checklist | `RH_L4_NonCircular_Checklist.md` | **Written** |
| R7 | M1.2-GHK finite-height statement under HD-low | §3 this note | **Stated** (conditional/finite) |
| R8 | Prior paths (Akatsuka, GHK, \(c_i\), M1.3 HD-low, \(U=E_1\)) | Existing notes | **Already on Master** |

Unproved analytic closures (not executable as proofs here): full M1.2 at unbounded height; target lemma; RH.

---

## 1. R1 — Regularised remainder

**Definition used:**
\[
R_{\mathrm{reg}}(s;X,\rho)
=
\log P_X(s)
+
U\bigl((s-\rho)\log X\bigr)
-
\log\zeta(s)
\]
with \(U=E_1\), approach \(\sigma:1.5\to\tfrac12+r\), \(t=\gamma\).

Under GHK, \(R_{\mathrm{reg}}=-\log Z_X^{\mathrm{far}}-\mathcal{E}\) (up to branch), so small \(\lvert R_{\mathrm{reg}}\rvert\) means local zero absorbed into \(U\) and distant zeros + hybrid error controlled.

**Results (6 first zeros, \(X=(\log(2+\gamma))^3\)):**

| Quantity | Mean |
|----------|-----:|
| \(\max\lvert R_{\mathrm{reg}}\rvert\) | \(\approx 1.48\) |
| \(\max\lvert\mathcal{E}_{\mathrm{hyb}}\rvert\) | \(\approx 0.079\) |
| \(\Delta\arg P_X\) on approach | \(\approx 0.008\) (mean) |

**Reading:** Hybrid error is **small** (\(\sim 0.08\)); regularised remainder is **\(O(1)\)** (not \(o(1)\)), dominated by far zeros / incomplete \(Z\) window / branch of \(\log\zeta\) near the zero. \(\Delta\arg P\) remains small — consistent with zero-free \(P_X\).

---

## 2. R2 — Multi-\(X\) phase

For fixed approach path, \(\lvert\Delta\arg P_X\rvert\) as function of \(X\in\{30,\ldots,1500\}\):

- Values typically \(0.02\)–\(0.18\); **no clear** growth like \(c\log\log X\) at these heights.  
- Target-lemma scale is **not** visible in this finite range (as expected).

---

## 3. R3 — M1.4 \(A_X\)

Discrete mean of continuous \(\arg P_Y\) for \(Y\in[X_0,X_1]\):

| Point type | Typical \(\lvert A_X\rvert\) | \(\arg\) range over \(Y\) |
|------------|-----------------------------:|-------------------------:|
| Near critical line \(\sigma=1/2+\varepsilon\) | \(O(10^{-1})\) | up to \(\sim 1\) |
| \(\sigma=0.6\) | smaller | \(\sim 0.2\)–\(0.4\) |
| \(\sigma=1\) | \(O(10^{-1})\) | \(\sim 0.02\) (very stable) |

Smoothing is well-defined and computable; **no** target-lemma lower bound observed.

---

## 4. R4 — L2 vs L3

Mean \(\lvert\Delta\arg P\rvert\) on approach paths (\(X=200\)):

| Regime | Mean \(\lvert\Delta\arg P\rvert\) |
|--------|----------------------------------:|
| On-line (near first zeros) | \(\approx 0.100\) |
| Off-line \(\lvert\zeta\rvert\) minima \(\sigma\ge 0.60\) | \(\approx 0.197\) |

Off-line control paths can show **larger** phase change than near on-line zeros at low height — **not** evidence against RH (minima are not zeros; path length/geometry differs). Diagnostic only.

---

## 5. R5 — \(A_2\) / \(c_1\)

Dense Fornberg sampling confirms:
\[
A_2^{\mathrm{raw}}\approx 0.1536,
\qquad
A_2\le 0.169\ (10\%\ \mathrm{safety}),
\qquad
c_1\le 291,
\qquad
c_2\le 8
\]
(unchanged order from `RH_M1_2_Optimized_ci_Bounds.md`).

---

## 6. R6 — L4 checklist

See `RH_L4_NonCircular_Checklist.md`. Allowed: GHK, classical density, effective \(c_i\), HD-low tables. Forbidden: model constants; RH-equivalent zero-free regions disguised as lemmas.

---

## 7. R7 — Finite-height M1.2-GHK (HD-low)

**Statement (finite, not RH):**  
Let \(\rho=\tfrac12+i\gamma\) be among the first \(N\) Odlyzko zeros, \(r=c_r/\log(2+\gamma)\), and assume HD-low isolation in \(D(\rho,2r)\) (verified for \(N=6\)). Let \(X=(\log(2+\gamma))^3\), \(K=2\), \(f=f_\star\). Along the approach path \(\sigma:1.5\to\tfrac12+r\),
\[
\max\lvert\mathcal{E}_{\mathrm{hyb}}\rvert
\le
\varepsilon_N
\quad\text{(empirically }\varepsilon_6\approx 0.12\text{ in the batch)},
\]
and
\[
\max\lvert R_{\mathrm{reg}}\rvert
\le
C_N
\quad\text{(empirically }C_6\approx 1.55\text{)}.
\]
These are **numerical certificates for the finite sample**, not uniform theorems for all \(\gamma\).

**Does not** imply the target lemma or unbounded M1.2.

---

## 8. What remains open (cannot be “executed” as proofs here)

1. Uniform M1.2 bound for all heights under classical HD only.  
2. Large continuous \(\theta_X\) or \(A_X\) of size \(\gg\log\log X\) at a maximal-abscissa zero.  
3. Target lemma and RH.  
4. Interval-arithmetic certified \(A_2\) (optional sharpening).  
5. M1.3-bis: designed long paths / \(X=X(s)\) coupling modulus and argument.

---

## 9. One-liner

**All executable pure-Cat-A research paths (regularised remainder, multi-\(X\), \(A_X\), L2/L3, \(A_2\), L4, finite HD-low M1.2) have been run or written; RH and the target lemma remain open with status `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`.**

*Per aspera ad astra.*
