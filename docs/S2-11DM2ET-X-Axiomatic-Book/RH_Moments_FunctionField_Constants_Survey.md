# Explicit constants for \(k=2\), function-field analogs, and the status of \(c_1,c_2,c_3\)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** survey for the phase programme.  
**No model constants.** RH open; infrastructure and honesty about effectiveness — not a proof of the target lemma or of M1.2.

**Companions:**  
`RH_Akatsuka_GHK_Survey.md` (GHK hybrid, M1.2-GHK),  
`RH_M1_2_Remainder_Bound_Strategy.md`,  
`RH_L1_Phase_Functional_CatA.md`.

---

## 1. Explicit constants for the fourth moment (\(k=2\))

The fourth moment is a **theorem**. Ingham proved the leading asymptotic
\[
\int_0^T\bigl\lvert\zeta(\tfrac12+it)\bigr\rvert^4\,dt
=
\frac1{2\pi^2}T(\log T)^4
+
O\bigl(T(\log T)^3\bigr).
\]

Heath-Brown and later authors obtained the full asymptotic polynomial of degree 4. In the CFKRS normalisation one has
\[
\int_0^T\bigl\lvert\zeta(\tfrac12+it)\bigr\rvert^4\,dt
=
\int_0^T P_2\bigl(\log(t/2\pi)\bigr)\,dt
+
O\bigl(T^{7/8+\varepsilon}\bigr),
\]
where \(P_2(x)\) is the explicit degree-4 polynomial whose leading term is
\[
\frac1{2\pi^2}x^4.
\]
(The lower coefficients involve \(\gamma\), \(\zeta'(2)\), \(\zeta''(2)\), Stieltjes constants, etc., and are known in closed form; they appear in the works of Heath-Brown, Motohashi, and the CFKRS tables.)

**Thus for \(k=2\) every coefficient of the moment polynomial is an explicit, rigorously established constant. No conjecture remains at this order.**

### Use for the phase programme

- Fourth-moment control is classical input for mean-square estimates of \(\zeta\) and of Dirichlet polynomials on the critical line; it does **not** by itself force argument growth of partial Euler products off the line.
- It shows that at the first non-trivial moment order beyond \(k=1\), the CFKRS / random-matrix leading term is **proved** for \(\zeta\), so the hybrid philosophy of GHK (arithmetic factor \(\times\) spectral factor) is not free-floating: at least for \(\lvert\zeta\rvert^4\), the spectral side has been fully accounted for by analytic number theory.
- Higher even moments \(k\ge 3\) remain open for \(\zeta\) (conjectural asymptotics); the programme does **not** rely on unproved moment conjectures for M1.2.

---

## 2. Function-field analogs

Over finite fields the analogous statements become theorems in many cases.

### Setting

Let \(\mathbb{F}_q[T]\) be the ring of polynomials over a finite field. Dirichlet \(L\)-functions attached to characters of this ring, or zeta functions of curves over \(\mathbb{F}_q\), possess Euler products, functional equations, and zeros. The “height” is replaced by the degree of the modulus or by the genus of the curve.

### Results

- **Katz–Sarnak:** the monodromy groups of many geometric families are the full classical groups; consequently the local statistics of zeros are exactly those of the corresponding random-matrix ensembles in the large-genus or large-degree limit.
- **Moments of quadratic Dirichlet \(L\)-functions over function fields** (Andrade–Keating and later work): leading-term asymptotics matching the Keating–Snaith predictions have been proved for the first few moments, and full CFKRS-type recipes have been verified under geometric hypotheses.
- For the **rational function field** the fourth moment of Dirichlet \(L\)-functions has been established with an explicit leading coefficient of the expected shape.
- In some geometric settings the **full moment polynomials** (including lower-order terms) can be extracted from the cohomology of the associated monodromy representations, confirming the CFKRS recipe exactly.

### Interpretation for the programme

The function-field theory supplies a setting in which the random-matrix predictions and the hybrid Euler–Hadamard philosophy become **theorems** rather than conjectures. It does **not** prove the corresponding statements for the classical Riemann zeta function, but it demonstrates that the conjectural framework is consistent and, in a closely analogous arithmetic setting, correct.

**Firewall.** Function-field theorems are **Category A classical input** (motivation and structural consistency). They are **not** lemmas that close RH for \(\zeta\). No transfer of monodromy or Katz–Sarnak equidistribution into a theorem about \(\arg P_x\) for \(\zeta\) is claimed here.

---

## 3. Numerical values for \(c_1\), \(c_2\), \(c_3\) in the M1.2 bound

### Schematic form (hybrid / GHK shape)

In hybrid language the remainder controlling \(\operatorname{Im}\mathcal{R}\) after peeling the local zero can be written schematically
\begin{equation}
\bigl\lvert\operatorname{Im}\mathcal{R}_X^{(\mathrm{EP})}(s)\bigr\rvert
\le
c_1\frac{X^{4}}{(\lvert t\rvert\log X)^2}
+
c_2 X^{-\sigma}\log X
+
c_3,
\tag{M1.2-const}
\end{equation}
for a fixed truncation order \(K=2\) (the powers match the GHK shape \(X^{K+2}/(\lvert s\rvert\log X)^K\) when \(K=2\); other \(K\) give analogous constants). The constant \(c_3\) absorbs absolute contributions from the fixed weight \(f\) (or GHK \(u\)), the Gamma factor on bounded contours, and a chosen zero-density theorem on a fixed height range.

(Parallel form with general \(K\): replace the first summand by \(c_1(K)\,X^{K+2}/(\lvert t\rvert\log X)^K\).)

### Honest status

The constants \(c_1,c_2,c_3\) are **effective in principle**: they depend only on

- a fixed smooth test function \(f\) (or GHK weight \(u\)),
- a fixed truncation order \(K\),
- a concrete zero-density theorem,

and arise from tracking derivatives of \(f\) through the contour shifts of the smoothed explicit formula and from standard estimates on the Gamma factor and on horizontal integrals.

**However:** the original Gonek–Hughes–Keating paper (and the subsequent literature) does **not** tabulate numerical values for these implied constants. No published source supplies ready-to-use decimal numbers for \(c_1,c_2,c_3\).

Consequently it is **not possible** to quote rigorous numerical values such as “\(c_1=17.3\)” without performing a separate, fully explicit estimation that has **not** yet been carried out in the literature. Any such numbers offered without that calculation would be **invented** and therefore **inadmissible**.

### What can be said rigorously

| Statement | Status |
|-----------|--------|
| \(c_1,c_2,c_3\) are finite and absolute once \(f\), \(K\), and a density theorem are fixed | **True** |
| They can be bounded by a (possibly large) explicit number by careful elementary estimation; the bound is effective | **True** — majorant tree written in `RH_M1_2_Explicit_Hybrid_Constants.md` (symbolic \(c_1,c_2\); \(c_3\) under HD) |
| At low height the same remainder can be evaluated numerically to arbitrary precision; those values are rigorous for the finite range examined | **True** — diagnostics (`rh_GHK_hybrid_diagnostic.py` with full \(U=E_1\), `rh_M1_2_remainder_diagnostic.py`) |
| Published decimal table for \(c_1,c_2,c_3\) | **Does not exist** |
| Optimized decimals for a named \(f\) | **Open** (majorants only; no invented sharp floats) |

### Correct standing statement

> The constants \(c_1,c_2,c_3\) exist, are effective, and depend only on the fixed data of the hybrid formula and on a chosen zero-density theorem; their **optimized numerical** values have not been tabulated and are therefore left **symbolic**, with an explicit majorant tree in `RH_M1_2_Explicit_Hybrid_Constants.md`.

### Relation to M1.2-GHK

Lemma M1.2-GHK in `RH_Akatsuka_GHK_Survey.md` uses the **shape** of \(\mathcal{E}_{\mathrm{GHK}}\) with \(O(\cdots)\). The constants note tracks \(c_1=2C_{\mathrm{mul}}D_K A_K M_K\), \(c_2=2C_{\mathrm{mul}}C_{\mathrm{tail}}\), and \(c_3\) under HD. **No invented decimals.**

---

## 4. Summary

| Item | Status |
|------|--------|
| Moment polynomial for \(k=2\) (\(\lvert\zeta\rvert^4\)) | **Completely explicit and proved** |
| Function-field RMT / CFKRS analogs | **Theorems** in many cases; do not prove RH for \(\zeta\) |
| Symbolic majorants for \(c_1,c_2\) (fixed \(f,K\)) | **Written** (`RH_M1_2_Explicit_Hybrid_Constants.md`) |
| Numerical \(c_1,c_2,c_3\) optimized | **Open** — left symbolic / crude majorants only |
| Hybrid numeric with full \(U=E_1\) | **Executed** (diagnostic) |
| RH / target lemma / full M1.2 | **Open** |

**Next increments (still pure Cat A):** optimize \(M_K,A_K,D_K\) for a named \(f\); produce \(c_3\) under a concrete HD; M1.3 path design.

---

## 5. Selected classical references (pointers only)

| Topic | Pointers |
|-------|----------|
| Fourth moment leading term | Ingham; Heath-Brown; Motohashi |
| Full \(P_2\) / CFKRS form | Conrey–Farmer–Keating–Rubinstein–Snaith; tables in the CFKRS literature |
| GHK hybrid | Gonek–Hughes–Keating, Duke Math. J. **136** (2007); arXiv:math/0511182 |
| Function fields / monodromy | Katz–Sarnak; Andrade–Keating and successors |

(Exact bibliographic details for Ingham / Heath-Brown / Motohashi / Andrade–Keating may be expanded when a full bibliography block is needed; none of these close RH.)

---

## One-liner

**For \(k=2\) the moment polynomial is proved and fully explicit; function-field analogs make RMT/CFKRS theorems in an analogous setting; the M1.2 constants \(c_1,c_2,c_3\) exist and are effective but are not tabulated in the literature and must remain symbolic until an explicit estimation is written.**

*Per aspera ad astra.*
