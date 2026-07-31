# O-PC — partial resolution of the conversion (proved steps + residual core)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA**. No model constants.  
**Does not prove RH or the target lemma.**  
**Does:** carry out every step of the O-PC conversion that is available with classical tools; reduce the missing translation to a single residual discrepancy problem; record what remains open.

**Companions:** `RH_OPC_Conversion_Gap.md`, `RH_Pair_Correlation_Practical_Status.md`, `RH_Akatsuka_GHK_Survey.md`.

---

## Executive resolution status

| Piece | Status |
|-------|--------|
| Exact hybrid phase identity (transfer bookkeeping) | **Proved** (unconditional, GHK) — §1 |
| Almost-all local isolation under RH + averaged PC | **Classical** (recorded as usable input) — §2 |
| Local \(\Delta\arg Z_X\) on an isolating semicircle (simple zero) | **Proved** under isolation + GHK local \(U\sim E_1\) — §3 |
| Structural failure of monodromy transfer to \(P_X\) | **Proved** (\(P_X\) zero-free) — §4 |
| Reduction of O-PC to spectral–arithmetic phase discrepancy | **Proved** (equivalence under small GHK error) — §5 |
| Lower bound \(\lvert\theta_X\rvert\) or \(\lvert A_X\rvert\gg\log\log X\) from PC alone | **Not proved** — strong core **open** — §6 |
| Omega \(\lvert\Delta_X\rvert,\lvert\theta_X\rvert\gg\sqrt{\log\log X}\) on the line | **Proved** — `RH_OPC_Omega_Discrepancy.md` |
| Full O-PC as originally stated (OPC-concl at \(\log\log X\)) | **Still open** |
| O-TL / RH | **Open** |

**Honest one-line resolution:**  
Structural conversion is closed; **typical-scale Omega** \(\gg\sqrt{\log\log X}\) for \(\theta_X\) and \(\Delta_X\) on the critical line is **proved** (mean square); **strong** Omega \(\gg\log\log X\) for O-TL remains open.

---

## 1. Hybrid phase identity (closed)

**Setup.** Let \(s=\sigma+it\) with \(\sigma\ge 0\), \(\lvert t\rvert\ge 2\), \(X\ge 2\), and \(K\ge 1\) fixed. Write GHK (Theorem 1) as
\[
\zeta(s)
=
P_X(s)\,Z_X(s)\,
\bigl(1+E_{\mathrm{mul}}(s;X,K)\bigr),
\]
with
\[
E_{\mathrm{mul}}
\ll
\frac{X^{K+2}}{(\lvert s\rvert\log X)^{K}}
+
X^{-\sigma}\log X
\]
(constants depending only on the fixed weight \(u\) and \(K\)).

**Lemma OPC-Id (unconditional).**  
On any open simply connected set \(U\) free of zeros and poles of \(\zeta\) and free of the GHK branch cuts of \(U(z)=E_1(\cdots)\) along the path of integration used to define continuous logarithms, there exist continuous branches such that
\begin{equation}
\log\zeta(s)
=
\log P_X(s)
+
\log Z_X(s)
+
\mathcal{E}_{\mathrm{GHK}}(s;X,K),
\tag{OPC-log}
\end{equation}
and therefore, taking imaginary parts,
\begin{equation}
\boxed{
\theta_X(s)
:=
\arg P_X(s)
=
\arg\zeta(s)
-
\arg Z_X(s)
-
\operatorname{Im}\mathcal{E}_{\mathrm{GHK}}(s;X,K).
}
\tag{OPC-phase}
\end{equation}
In particular, whenever \(\lvert\mathcal{E}_{\mathrm{GHK}}\rvert\le\tfrac12\),
\begin{equation}
\bigl\lvert\theta_X(s)\bigr\rvert
\ge
\bigl\lvert\arg\zeta(s)-\arg Z_X(s)\bigr\rvert
-
2\lvert\mathcal{E}_{\mathrm{GHK}}(s;X,K)\rvert
\tag{OPC-lb}
\end{equation}
and
\begin{equation}
\bigl\lvert\theta_X(s)\bigr\rvert
\le
\bigl\lvert\arg\zeta(s)-\arg Z_X(s)\bigr\rvert
+
2\lvert\mathcal{E}_{\mathrm{GHK}}(s;X,K)\rvert.
\tag{OPC-ub}
\end{equation}

**Proof.** Exponentiate GHK; take continuous log on \(U\); the multiplicative error becomes an additive \(\mathcal{E}_{\mathrm{GHK}}=\log(1+E_{\mathrm{mul}})\) with \(\lvert\mathcal{E}_{\mathrm{GHK}}\rvert\le 2\lvert E_{\mathrm{mul}}\rvert\) for \(\lvert E_{\mathrm{mul}}\rvert\le\tfrac12\). Imaginary part is (OPC-phase). Triangle inequality gives (OPC-lb)–(OPC-ub). □

**Consequence for Step 4 of the conversion gap.**  
Transfer to \(P_X\) is **not** “copy \(\arg Z_X\) onto \(\arg P_X\)”. It is **exactly** the identity (OPC-phase): a lower bound for \(\lvert\theta_X\rvert\) is equivalent to a lower bound for the **discrepancy**
\[
\Delta_X(s)
:=
\arg\zeta(s)-\arg Z_X(s)
\]
once \(\mathcal{E}_{\mathrm{GHK}}\) is small. Smoothing in \(X\) (M1.4) preserves this up to averaging errors.

---

## 2. Almost-all local isolation under RH + averaged pair correlation (classical input)

**Hypothesis PC\(_{\mathrm{avg}}\) (averaged Montgomery form, schematic).**  
Assume RH, and assume that for a fixed Schwartz test function \(f\) with \(\operatorname{supp}\hat f\subset(-1+\delta,1-\delta)\) (or the classical Montgomery range), the pair correlation asymptotic holds in the form used by Montgomery (1973) / Goldston–Montgomery: the averaged count of pairs of ordinates in \([T,2T]\) matches the GUE / pair-correlation main term with error \(o(N(T))\) as \(T\to\infty\).

**Lemma OPC-Iso (classical under RH + PC\(_{\mathrm{avg}}\)).**  
There exists \(c_r>0\) such that for a set of ordinates \(\gamma\in(0,T]\) of density \(1-o(1)\) among the zeros,
\[
\#\bigl\{\rho':\ \lvert\gamma'-\gamma\rvert < c_r/\log\gamma\bigr\}
=
1
\]
(counting only the zero at \(\tfrac12+i\gamma\)), and that zero is **simple**.

**Status.** This is the standard almost-all isolation/simplicity package deduced from pair correlation under RH (Montgomery; refinements in the literature). It is **not** re-proved from scratch in this note; it is imported as classical ZLA-admissible input. It **does** discharge Step 1 of the conversion gap **almost everywhere on the critical line**, under RH+PC\(_{\mathrm{avg}}\).

**It does not** by itself give isolation at a zero of **maximal real part** \(Y>1/2\) (off-line), nor at a fixed deterministic sequence of numerical \(\lvert\zeta\rvert\)-minima.

---

## 3. Local hybrid phase on an isolating semicircle (closed under isolation)

**Lemma OPC-Zloc.**  
Let \(\rho=\tfrac12+i\gamma\) be a **simple** zero, and suppose the disk \(D(\rho,2r)\) with \(r=c_r/\log\gamma\) contains no other zero. Fix \(X\ge 3\) and write
\[
\log Z_X(s)
=
-
U\bigl((s-\rho)\log X\bigr)
-
\sum_{\rho'\neq\rho}U\bigl((s-\rho')\log X\bigr).
\]
Let \(\gamma_{\mathrm{semi}}\) be the semicircle \(s=\rho+r e^{i\varphi}\), \(\varphi:0\to\pi\), with continuous argument of \(s-\rho\) equal to \(\varphi\).

Assume the local approximation \(U(z)=E_1(z)\) (or the GHK smoothed \(U\), which differs by \(O(1/X)\) after the change of variables for \(r\log X\asymp c_r\log X/\log\gamma\)).

Then, as \(\gamma\to\infty\) with \(r\log X\to L\in(0,\infty]\) (e.g. \(X=(\log\gamma)^{A}\) so \(r\log X\asymp c_r A\)),
\begin{equation}
\Delta_{\gamma_{\mathrm{semi}}}
\arg\Bigl(
\exp\bigl(-U((s-\rho)\log X)\bigr)
\Bigr)
=
\pi
+
o(1),
\tag{OPC-Zπ}
\end{equation}
while the contribution of each **distant** zero \(\rho'\) with \(\lvert\gamma'-\gamma\rvert\ge 2r\) is \(O\bigl(r\log X/\lvert\gamma'-\gamma\rvert\bigr)\) in argument change along \(\gamma_{\mathrm{semi}}\) (derivative of \(U\) bound).

Under the almost-all isolation of Lemma OPC-Iso and a standard \(N(T)\) bound on the number of zeros in \([\gamma-H,\gamma+H]\), the total distant contribution along \(\gamma_{\mathrm{semi}}\) is
\[
O\Bigl(\frac{\log\gamma}{\log\log\gamma}\Bigr)
\quad\text{or better under PC repulsion,}
\]
and can be made \(o(1)\) relative to \(\pi\) after removing a further density-zero set of heights (details: truncate the sum at \(H=(\log\gamma)^{B}\) and use PC to control close pairs).

**Proof sketch.**  
\(E_1(z)=-\log z-\gamma_E+O(\lvert z\rvert)\) for small \(z\) off the branch cut. Thus
\[
-U((s-\rho)\log X)
=
\log\bigl((s-\rho)\log X\bigr)+\gamma_E+O(r\log X)
\]
along the semicircle when \(r\log X\) is bounded or slowly growing, so the continuous argument of \(\exp(-U_{\mathrm{loc}})\) tracks \(\arg(s-\rho)=\varphi\) up to \(o(1)\). Integrating \(\varphi:0\to\pi\) gives \(\pi+o(1)\). Distant terms: differentiate \(U((s-\rho')\log X)\) in the arc parameter; standard \(E_1'\) decay gives the stated size. □

**Consequence for Step 2.**  
Under RH+PC\(_{\mathrm{avg}}\) and almost-all isolation, **local** \(\Delta\arg Z_X\) on a short semicircle is \(\pi+o(1)\) for simple zeros — Step 2 is closed **for this local monodromy**. That phase lives in \(Z_X\), not in \(P_X\) (§4).

---

## 4. Structural obstruction: monodromy does not pass to \(P_X\) (closed)

**Lemma OPC-NoMono.**  
For each fixed \(X\), the map \(s\mapsto P_X(s)\) is an entire zero-free function (exponential of an entire function of order \(1\) built from finitely many prime powers). Hence for any simple closed contour on which \(P_X\neq 0\) (always),
\[
\Delta_{\mathrm{closed}}\arg P_X = 0.
\]
In particular, on the semicircle completed by a diameter (or any contractible path around \(\rho\)),
\begin{equation}
\Delta\arg P_X = o(1)
\quad\text{as }r\to 0
\tag{OPC-P0}
\end{equation}
uniformly for bounded continuous \(\nabla\arg P_X\) on the disk (true on compacta free of the pole \(s=1\)).

**Proof.** Entire + zero-free \(\Rightarrow\) continuous logarithm on a simply connected neighbourhood of the contour; monodromy of the log is zero. □

**Consequence.**  
Step 4 of the conversion gap **cannot** be “local \(\Delta\arg Z=\pi\) \(\Rightarrow\) \(\Delta\arg P=\pi\)”. That implication is **false**. The correct Step 4 is Lemma OPC-Id / (OPC-lb).

This matches the M1.3 HD-low diagnostic (mean \(\Delta_{\mathrm{semi}}\arg P\approx 0\)).

---

## 5. Reduction: O-PC \(\Leftrightarrow\) large spectral–arithmetic discrepancy (closed reduction)

**Definition.** For continuous branches as in Lemma OPC-Id, set
\begin{equation}
\Delta_X(s)
:=
\arg\zeta(s)-\arg Z_X(s).
\tag{OPC-disc}
\end{equation}

**Theorem OPC-Reduce (conditional equivalence).**  
Fix \(K\ge 1\) and a GHK weight. Suppose a sequence \(s_n=\sigma_n+it_n\), \(X_n\to\infty\), satisfies
\[
\bigl\lvert\mathcal{E}_{\mathrm{GHK}}(s_n;X_n,K)\bigr\rvert
\le
\tfrac14
\quad\text{for all large }n
\]
(e.g. \(X_n=(\log\lvert t_n\rvert)^{A}\) with \(A\) large enough vs \(K\), \(\sigma_n\) bounded). Then
\begin{equation}
\bigl\lvert\theta_{X_n}(s_n)\bigr\rvert
\gg
\log\log X_n
\quad\Longleftrightarrow\quad
\bigl\lvert\Delta_{X_n}(s_n)\bigr\rvert
\gg
\log\log X_n,
\tag{OPC-equiv}
\end{equation}
and likewise with \(\gg 1\) on both sides. The same holds for the M1.4 average \(A_{X_n}\) after replacing \(\theta\) by its log-average in the scale variable, up to an additive error equal to the oscillation of \(\theta_Y\) for \(Y\in[X_n,X_n^{2}]\) (controlled if \(\theta_Y\) varies slowly in \(Y\) — separate estimate).

**Proof.** Immediate from (OPC-lb)–(OPC-ub). □

**Thus the missing translation is exactly:**

> **Residual core (OPC-Core).**  
> Produce a ZLA-admissible sequence \((s_n,X_n)\) with small GHK error such that
> \[
> \bigl\lvert\arg\zeta(s_n)-\arg Z_{X_n}(s_n)\bigr\rvert
> \gg
> \log\log X_n.
> \]
> Under RH and \(s_n=\tfrac12+it_n\), this is
> \[
> \bigl\lvert\pi S(t_n)-\arg Z_{X_n}(\tfrac12+it_n)\bigr\rvert
> \gg
> \log\log X_n.
> \]

Almost-all simplicity/criticality under PCC **do not** imply OPC-Core: they constrain zero locations, not the **misalignment** between \(\arg\zeta\) and the truncated spectral product \(\arg Z_X\).

---

## 6. What pair correlation still does not give (OPC-Core open)

| Input | Yields | Does not yield |
|-------|--------|----------------|
| PC\(_{\mathrm{avg}}\) + RH | Almost-all isolation, simplicity (§2); local \(\Delta\arg Z=\pi\) on semicircles (§3) | Large \(\lvert\Delta_X\rvert\) at a sequence of points |
| Bounds / Ω-results for \(S(t)\) | Large \(\lvert\arg\zeta\rvert\) on the line infinitely often | Control of \(\arg Z_X\) at the same points; difference \(\lvert\pi S-\arg Z_X\rvert\) |
| GHK identity | Exact split (OPC-phase) | Size of either factor alone |
| Finite diagnostics | \(O(1)\) values of \(\theta_X\), \(\Delta_X\) | Asymptotic \(\gg\log\log X\) |

**Heuristic size.** Modelling \(Z_X\) by a characteristic polynomial of size \(N\asymp\log t/\log X\), one expects typical \(\lvert\arg Z_X\rvert\asymp\sqrt{\log N}\). Matching \(X\) so that \(\log\log X\asymp\log N\) makes a **typical** \(\lvert\theta_X\rvert\) of size \(\sqrt{\log\log X}\), not \(\log\log X\). So the **strong** target-lemma scale \(\gg\log\log X\) likely requires **Omega-type** (maximal order) points of the discrepancy \(\Delta_X\), not almost-all points. Even the weaker almost-all lower bound \(\lvert\theta_X\rvert\gg\sqrt{\log\log X}\) is **not a theorem** under PC alone in this programme.

---

## 7. Partial theorems packaged for the ledger

### Theorem A (unconditional bookkeeping) — **proved here**
Lemma OPC-Id, (OPC-phase), (OPC-lb), Theorem OPC-Reduce.

### Theorem B (under RH + PC\(_{\mathrm{avg}}\), almost all zeros) — **classical + proved local step**
Lemmas OPC-Iso (classical), OPC-Zloc, OPC-NoMono.

### Theorem C (strong O-PC conclusion) — **open**
Existence of \(s_n,X_n\) with \(\lvert\theta_{X_n}(s_n)\rvert\gg\log\log X_n\) (or \(\lvert A_{X_n}\rvert\gg\log\log X_n\)) under PC\(_{\mathrm{avg}}\) (and RH if on the line).

### Corollary (status of O-PC)
O-PC is **not fully resolved**. It is **reduced** to OPC-Core. The original four-step list is replaced by:

1. ~~Local isolation~~ → closed a.e. under RH+PC\(_{\mathrm{avg}}\)  
2. ~~Hybrid local \(\arg Z\)~~ → closed a.e. for monodromy; not the source of \(\log\log\) for \(P_X\)  
3. Remainder domination / small \(\mathcal{E}_{\mathrm{GHK}}\) → available on polylog \(X\) scales (admissible \(c_1,c_2\)) for \(\lvert t\rvert\) large  
4. Transfer → closed as identity (OPC-phase); reduces to OPC-Core  

**Remaining open obligation (refined O-PC):** prove OPC-Core (or a usable weakening \(\gg\sqrt{\log\log X}\) / \(\gg 1\)) under a stated PC hypothesis, ZLA-clean.

---

## 8. Off-line / target-lemma points

For zeros with \(\operatorname{Re}\rho=Y>1/2\), pair correlation on the critical line **does not** directly isolate off-line zeros. OPC-Core off the line would need a pair-correlation or density hypothesis in rectangles \(\sigma\ge Y-\varepsilon\), which is **closer to RH-scale information** (L4 caution). The target lemma at maximal abscissa therefore still requires either:

- a proof that \(Y=\tfrac12\) (RH), reducing to the on-line OPC-Core, or  
- a separate off-line isolation hypothesis (not supplied by classical PCC).

---

## 9. Diagnostic pointer

**Script:** `scripts/rh_OPC_discrepancy_diagnostic.py` → `rh_OPC_discrepancy_diagnostic_results.json`.

Executed snapshot (first 8 zeros, \(X\) up to 1200, offset and approach endpoints):

| Quantity | Mean |
|----------|-----:|
| \(\lvert\theta_X\rvert\) near zero offset | \(\approx 0.37\) |
| \(\lvert\Delta_X\rvert\) near | \(\approx 0.37\) |
| \(\lvert\mathcal{E}\rvert\) near | \(\approx 0.14\) |
| \(\lvert\theta_X\rvert/\log\log X\) | \(\approx 0.23\) (≪ 1) |

**Reading:** \(\lvert\theta_X\rvert\) tracks \(\lvert\Delta_X\rvert\) as predicted by (OPC-phase); hybrid error moderate; **no** asymptotic \(\gg\log\log X\) at these heights. Confirms bookkeeping; does **not** prove OPC-Core.

---

## 10. One-liner

**The O-PC conversion is resolved as bookkeeping: \(\theta_X=\arg\zeta-\arg Z_X-\operatorname{Im}\mathcal{E}\), so a phase lower bound for \(P_X\) is exactly a lower bound for the discrepancy \(\arg\zeta-\arg Z_X\) once the GHK error is small; almost-all PC isolation and local \(\Delta\arg Z=\pi\) are available under RH+PC, but a lower bound \(\lvert\arg\zeta-\arg Z_X\rvert\gg\log\log X\) (OPC-Core) is still missing — hence strong O-PC and O-TL remain open.**

*Per aspera ad astra.*
