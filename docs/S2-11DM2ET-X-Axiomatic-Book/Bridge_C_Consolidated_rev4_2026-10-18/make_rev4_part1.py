# rev4 part 1: front matter, category convention, statuses of the main theorems (C9, C12, C13, C14, C15).
f="bridge_c_consolidated_rev4.tex"
s=open(f).read()
def rep(old,new):
    global s
    c=s.count(old)
    assert c==1, (c, old[:90])
    s=s.replace(old,new)
rep(r"""revision 3\\ \small (internal working paper; not externally refereed)}""",
r"""revision 4\\ \small (internal working paper; not externally refereed)}""")
# abstract
rep(r"""profile law in general by Poisson summation. For the scalar row we prove (given three""",
r"""profile law in general by Poisson summation. Revision~4 adds an exact tensor factorisation of the label representation through
$\mathrm{SL}_2(\Z/140)$, and through $\mathrm{SL}_2(\Z/4s(s-2))$ for the whole family $Q_s$ with $s$ odd; it identifies the function span
with the two matched local-parity sectors. It also adds exact dimensions of the function span, its Eisenstein part and its cusp part for
$s=5,\dots,51$ and $s=72$, closed forms in $s$ for the radial coefficients of $H_s$ through $t^{5/2}$, and a single-kernel, two-chain
construction of both parts of $\Cthird$. For the scalar row we prove (given three""")
rep(r"""be finite combinations of Hecke $L$-values at $s=0$. Every statement is labelled as proved,
exactly/finitely verified, or numerically verified (Category A), or as interpretation/conjecture
(Category B). No claim""",
r"""be finite combinations of Hecke $L$-values at $s=0$. Every statement is labelled Category A (proved, or exact,
including exact finite computation) or Category B (floating-point or PSLQ evidence only, identification by citation only,
interpretation, or conjecture); revision~4 applies this convention uniformly. No claim""")
# category convention
rep(r"""\begin{itemize}[leftmargin=2em]
\item \textbf{Category A} (proved or exactly verified). We always state the precise status, among:
\emph{proved} (written proof in the sources, not audited); \emph{proved, audited once} (one internal audit
pass, \S\ref{sec:audit}; in revision~3 this includes the items re-derived in the audit of Appendix~\ref{app:rev3}); \emph{exact finite verification} (rational or integer arithmetic over a stated
range); \emph{numerically verified} (floating-point or multiprecision agreement at a stated tolerance);
\emph{conditional on} a named cited theorem or on PARI/GP; \emph{PSLQ identification} (a closed form
recognised from high-precision numerics).
\item \textbf{Category B} (interpretation, expectation or conjecture): statements resting on standard
theory that was not re-proved, analogies, and untested expectations.
\end{itemize}""",
r"""\begin{itemize}[leftmargin=2em]
\item \textbf{Category A} (proved, or exact). We always state the precise status, among:
\emph{proved} (written proof in the sources, not audited); \emph{proved, audited once} (one internal audit
pass, \S\ref{sec:audit}; in revision~3 this includes the items re-derived in the audit of Appendix~\ref{app:rev3}); \emph{exact finite verification}
(rational, integer, modular or cyclotomic arithmetic over a stated finite set, including exact ranks); \emph{conditional on} a named cited theorem
(stated each time) or on exact data produced by PARI/GP; \emph{modulo F1} (proved given the cited two-dimensional Euler--Maclaurin expansion F1).
\item \textbf{Category B}: results whose only support is floating-point or multiprecision numerics (including SVD ranks, FFT character counts and
fits), PSLQ recognitions, identifications by citation only, interpretations, analogies, patterns on finitely many cases, and conjectures.
\end{itemize}
\emph{Revision~4 convention.} Revisions~1--3 allowed ``numerically verified'' and ``PSLQ identification'' inside Category~A. From revision~4 on, a
statement whose \emph{only} support is numerical is Category~B. Numerical checks reported inside a Category~A box are supporting evidence for a
statement that is proved or exact. Items relabelled under this rule are listed in Appendix~\ref{app:rev4}.""")
# Thm C status (C9)
rep(r"""$a_H$ and $a_C$: explicit Euler--Maclaurin expressions evaluated to 30 digits; the radical forms are PSLQ
identifications at 30 digits; numerically confirmed (remainder $\sim\sqrt t$ down to $t=2.5\cdot10^{-5}$).
The constant term $0$ of $H_s$ is known to 30 digits only. \textbf{Correction:}""",
r"""$a_H$ and $a_C$: \emph{proved closed forms, modulo F1} (rev.~4): $a_H=H_{-1/2}(7)$ and $a_C=C_{-1/2}(7)$ are the $s=7$ values of the closed forms in $s$
of Theorem~\ref{thm:Hs}, and they agree symbolically with the radical forms above, which revisions~1--3 had only as PSLQ recognitions at 30 digits.
The constant term $0$ of $H_s$ is now proved (all integer orders of $H_s$ vanish at $x=0$, modulo F1; Theorem~\ref{thm:Hs}); revisions~1--3 had it to 30
digits only. \textbf{Correction:}""")
# Thm E(ii) status
rep(r"""for $C$ over $\C$: proved, the nonvanishing input being
$a_C=0.829\ldots\neq0$ from a 30-digit evaluation of an explicit expression \src{2, A3} (erratum E2).""",
r"""for $C$ over $\C$: proved, the nonvanishing input being
$a_C=\sqrt\pi(833+204\sqrt{14}-14\sqrt{1190})/2380\neq0$, a proved closed form modulo F1 since rev.~4 (Theorem~\ref{thm:Hs}) \src{2, A3} (erratum E2).""")
# Thm F statement: convention sentence
rep(r"""$\mathrm{PSL}_2(\Z)$ on label space. The functions $u_{\alpha,\beta}$ span a $42$-dimensional subspace $V\subset\mathrm{Fix}(P)$, invariant under
$S$ and $T$ (Theorem~\ref{thm:H}, \S\ref{sec:spec}).
\end{mainthm}""",
r"""$\mathrm{PSL}_2(\Z)$ on label space; we write $W_P:=\mathrm{Fix}(P)$. The functions $u_{\alpha,\beta}$ span a $42$-dimensional subspace $V\subset W_P$, invariant under
$S$ and $T$ (Theorem~\ref{thm:H}, \S\ref{sec:spec}). (Label convention, rev.~4: $S$ here is the label matrix $S_{\rm lab}$; the representation of
$\mathrm{SL}_2(\Z)$ in the standard presentation is $\rho(S):=S_{\rm lab}^{-1}$, $\rho(T):=T$, see Remark~\ref{rem:Sconv}.)
\end{mainthm}""")
# Thm F status (C14, C15)
rep(r"""verified on all $140$ rows ($\le1.2\cdot10^{-15}$). $\dim V=42$: numerically verified twice, independently \src{14}, \src{15}. \textbf{Correction:} the earlier ``36-component''
family and ``Weil representation on the 35-element discriminant group'' are superseded (erratum, \S\ref{sec:recon}).}""",
r"""verified on all $140$ rows ($\le1.2\cdot10^{-15}$; supporting). $\dim V=42$: \emph{exact} since rev.~4 ($V$ equals the matched-sector space
$\mathrm{Fix}(N)\cap\mathrm{Fix}(\gamma)$, exact upper bound plus an exact modular rank lower bound, Proposition~\ref{prop:matched}); revisions~1--3 had it
numerically only. \textbf{Correction, reworded in rev.~4:} the earlier ``36-component'' family and the earlier claim of a Weil representation \emph{with $36$
components} are superseded (erratum, \S\ref{sec:recon}); but the label representation \emph{is} a Weil representation: exactly
$\rho=\rho_{2x^2/5}\otimes\rho_{x^2/7}\otimes\rho_2$ with a $4$-dimensional $2$-adic factor (Theorem~\ref{thm:tensor7}).}""")
# Thm H status
rep(r"""$\fp_2^3\fp_5\fp_7\infty_1\infty_2$ (reproduced PARI-free \src{9}). $36+6$ split and its $S,T$-invariance: numerically verified in function space
(invariance residuals $\le8\cdot10^{-16}$), independently in \src{14} and \src{15}; rank of the $12$ forms inside the cusp components: $6$ \src{14}.""",
r"""$\fp_2^3\fp_5\fp_7\infty_1\infty_2$ (reproduced PARI-free \src{9}); \emph{these fits are floating-point, hence Category~B under the rev.~4 convention}.
$36+6$ split and its $S,T$-invariance: \emph{exact} since rev.~4: $V_{\rm Eis}$ (the cyclic span of the constant-term vector) is the sector $A_3\otimes X^+$ and the
cuspidal complement is $B_1\otimes X^-$ (Proposition~\ref{prop:matched}); revisions~1--3 had the split numerically \src{14}, \src{15}. Rank $6$ of the $12$ forms inside the
cusp components: floating (Category~B), now explained by $\dim(B_1\otimes X^-)=1\cdot2\cdot3=6$.""")
rep(r"""\textbf{Correction (rev.~3):} the earlier ``$60+12$'' were ranks of label rows in $\mathrm{Fix}(P)$, a coordinate artifact (\S\ref{sec:spec}). Category B: cuspidality
$\Leftrightarrow\chi\neq\chi\circ\sigma$, level $19600$, nebentypus, newform status (standard theory \cite{Maass}).""",
r"""\textbf{Correction (rev.~3):} the earlier ``$60+12$'' were ranks of label rows in $\mathrm{Fix}(P)$, a coordinate artifact (\S\ref{sec:spec}). Category B: cuspidality
$\Leftrightarrow\chi\neq\chi\circ\sigma$, level $19600$, nebentypus, newform status (standard theory \cite{Maass}); the expression of the cusp components through the $12$ named dihedral forms (floating fits).""")
# Thm K: Category B
rep(r"""\catA{Numerically verified at the seven points, all $24$ cusp rows, to $4\cdot10^{-14}$, \emph{conditional on PARI}
\texttt{lfun}. The $\Z[\zeta_{12}]$ values are recognitions to $10^{-10}$. Not proved.""",
r"""\catB{Rev.~4 relabel (Category~A in revisions~1--3): numerically verified only, at the seven points, all $24$ cusp rows, to $4\cdot10^{-14}$, \emph{conditional on PARI}
\texttt{lfun} (also $1.2\cdot10^{-14}$ with PARI-free inputs, Appendix~\ref{app:pari}). Not proved. The $12$ values $L(0,\chi)\in\Z[\zeta_{12}]$ themselves are exact
(PARI-free Shintani sums, Category~A, Appendix~\ref{app:pari}).}
\catA{""")
# Theorem D title (C7)
rep(r"""\begin{mainthm}[Gauss-mean pattern]\label{thm:D}""",
r"""\begin{mainthm}[Gauss-mean pattern and zero set]\label{thm:D}""")
rep(r"""\catA{Pattern: proved \src{2, A4}; checked on all $3374$ coprime pairs with $m\le105$.""",
r"""\catA{Pattern: proved \src{2, A4}; checked on all $3374$ coprime pairs with $m\le105$. (Rev.~4 name note: the zero-set statement ``$G(h/m)=0$ iff $2\mid m$ or $5\mid m$''
is called ``Theorem~G'' in \src{11}; its consolidated name is Theorem~\ref{thm:D}. Theorem~G of this paper is the Lewis--Zagier period formula; Theorem~G$_s$ is the $g_s$ result.)""")
open(f,"w").write(s)
print("part1 ok")
