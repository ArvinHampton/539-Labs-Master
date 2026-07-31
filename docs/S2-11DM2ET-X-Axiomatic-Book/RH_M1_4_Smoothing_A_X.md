# M1.4 — Smoothing \(\theta_x\) to \(A_X\)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. No model constants.  
**Does not prove** the target lemma.

**Companions:** `RH_L1_Phase_Functional_CatA.md`, `RH_M1_3_Path_Design.md`.  
**Probe:** `scripts/rh_research_batch.py` path **R3**.

---

## 1. Definition (aligned with L1)

At fixed \(s=\sigma+it\), for a scale \(X\ge 3\),
\begin{equation}
A_X(s)
:=
\frac{1}{\log(X_1/X)}
\int_{X}^{X_1}
\theta_Y(s)\,\frac{dY}{Y},
\qquad
X_1=X^{2}\ \text{(or }X_1=\min(X^{2},x_{\max})\text{)},
\tag{M1.4-def}
\end{equation}
where \(\theta_Y(s)=\arg P_Y(s)\) is a continuous branch of the argument of the GHK partial product
\[
P_Y(s)=\exp\Bigl(\sum_{n\le Y}\frac{\Lambda(n)}{n^{s}\log n}\Bigr).
\]
In discrete form (diagnostic),
\[
A_X^{\mathrm{disc}}(s)
=
\frac1N\sum_{j=1}^{N}\theta_{Y_j}(s),
\qquad
\log Y_j
=
\log X
+
\frac{j-1}{N-1}\log(X_1/X).
\]

---

## 2. Why smooth

- Single-\(Y\) \(\theta_Y\) oscillates with primes near \(Y\).  
- Target lemma is stated for a **sequence** \(X_n\to\infty\) of scales.  
- Averaging in \(\log Y\) damps local prime noise while preserving slow growth (if any).

---

## 3. Transfer principle (sketch)

If on a path \(\gamma_{\mathrm{path}}\) one has a lower bound for \(\theta_X\) uniform for \(Y\in[X,X^{2}]\) up to \(o(1)\) errors, then the same lower bound passes to \(A_X\) up to that \(o(1)\).  
Conversely, large \(A_X\) does not force large \(\theta_X\) at a single \(Y\) without reverse inequalities (open).

**Status:** principle standard; **not** a proof that \(A_X\) meets the target lemma.

---

## 4. Diagnostic (R3)

Evaluate \(A_X^{\mathrm{disc}}\) at:
- near on-line points \(\tfrac12+\varepsilon+i\gamma_n\),  
- \(\sigma=0.6\) and \(\sigma=1\) controls,

with continuous unwrapping in the \(Y\)-variable.  
Results: `rh_research_batch_results.json` → `R3_A_X`.

---

## 5. Status

| Item | Status |
|------|--------|
| Definition of \(A_X\) | **Formalized** (this note + L1) |
| Numeric R3 probe | **In research batch** |
| Transfer from M1.3 bound | **Open** |
| Target lemma | **Open** |

---

## One-liner

**M1.4 freezes \(A_X\) as a log-average of continuous \(\arg P_Y\) over \(Y\in[X,X^{2}]\); diagnostics compute the discrete mean; the target-lemma lower bound remains open.**
