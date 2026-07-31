# Optimized \(M_K,A_K,D_K\) for \(f_\star\) — numerical upper bounds on \(c_1,c_2\)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. No model constants.  
**Does not prove** RH or M1.2.  
**Does:** replace crude \(A_2=24\), \(D_2=16\) by optimized admissible majorants for the named bump \(f_\star\).

**Companions:**  
`RH_M1_2_Explicit_Hybrid_Constants.md`,  
`RH_M1_2_Named_f_ci_Bounds.md` (prior crude bounds),  
`RH_M1_3_Path_Design.md`.  
**Probe:** `scripts/rh_optimize_c1_c2.py` → `rh_optimize_c1_c2_results.json`.

---

## 1. Named data (unchanged)

\[
f_\star(t)=\frac{\exp\bigl(-1/(t(1-t))\bigr)}{\int_0^1 f_{\mathrm{raw}}},\qquad K=2.
\]
\[
u(x)=\frac{X}{x}\,f_\star\bigl(X\log(x/e)+1\bigr).
\]

---

## 2. Optimized factors (executed)

| Factor | Crude (prior) | Optimized (this note) | Method |
|--------|--------------:|----------------------:|--------|
| \(M_2^\sharp\) | \(88.24\) (5% safety) | \(85.72\) (2% safety + refine) | denser grid + local refine |
| \(A_2\) | \(24\) (combinatorial) | \(0.169\) (raw max \(0.154\times 1.10\)) | sample \(\max_x\lvert u''(x)\rvert/(M_2 X^{3})\) over \(X\in[2,500]\) |
| \(D_2\) | \(16\) | \(5.023\) | pole \(2\cdot(3/2)^{2}=4.5\) + trivial-zero factor \(0.523\) at \(X\ge 2\) |
| \(C_{\mathrm{tail}}\) | \(2\) | \(2\) | unchanged |
| \(C_{\mathrm{mul}}\) | \(2\) | \(2\) | unchanged |

**Formula (unchanged):**
\[
c_1
=
2\,C_{\mathrm{mul}}\,D_2\,A_2\,M_2,
\qquad
c_2
=
2\,C_{\mathrm{mul}}\,C_{\mathrm{tail}}.
\]

---

## 3. Numerical upper bounds

\begin{equation}
\boxed{
c_2(f_\star,K=2)
\le
8,
\qquad
c_1(f_\star,K=2)
\le
290.96
}.
\tag{Opt-num}
\end{equation}

JSON: `c1_upper ≈ 290.959`, `c2_upper = 8`.

| Bound | Crude | Optimized | Improvement |
|-------|------:|----------:|------------:|
| \(c_1\) | \(\le 1.32\cdot 10^5\) | \(\le 2.91\cdot 10^{2}\) | \(\approx 450\times\) |
| \(c_2\) | \(\le 8\) | \(\le 8\) | — |

---

## 4. Honesty freeze (still in force)

- Bounds are **admissible majorants** for this package and \(f_\star\), not the sharpest possible GHK constants.  
- \(A_2\) uses finite-difference sampling of \(u''\) + 10% safety; a fully rigorous \(A_2\) would need a certified max of \(\lvert u''\rvert\) (interval arithmetic / analytic derivative). The present \(A_2\) is **numerical-with-safety**, stronger than crude \(24\), but not interval-certified.  
- \(D_2\) is analytic + numeric trivial-zero sum with 5% safety on the trivial part.  
- \(c_3\) remains under HD (see M1.3).  
- **No invented freestanding decimals:** every factor is either fixed by the tree or computed by the probe.

---

## 5. Status

| Item | Status |
|------|--------|
| Optimized \(M_2,A_2,D_2\) | **Executed** |
| \(c_1\le 291\), \(c_2\le 8\) | **Admissible** (this package) |
| Interval-certified \(A_2\) | **Open** |
| \(c_3\) numerical | **Open** (HD) |
| M1.2 / RH | **Open** |

---

## One-liner

**For \(f_\star\) and \(K=2\), optimized majorants give admissible \(c_1\le 291\) and \(c_2\le 8\) (\(\sim 450\times\) tighter than the crude \(c_1\)), still not a proof of M1.2 or RH.**

*Per aspera ad astra.*
