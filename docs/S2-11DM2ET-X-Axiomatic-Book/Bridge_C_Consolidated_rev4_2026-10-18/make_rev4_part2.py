# rev4 part 2: body fixes (radial table, E_{-a}=E_a, Baker (ii), W7 box, quadrant-cone ratios, lift remark,
# split section, Prop. spec with V^perp naming, L(0) section, numerical-verification preamble).
f="bridge_c_consolidated_rev4.tex"
s=open(f).read()
def rep(old,new):
    global s
    c=s.count(old)
    assert c==1, (c, old[:90])
    s=s.replace(old,new)
rep(r"""\begin{mainthm}[Cusp rows and $L(0)$]\label{thm:K}""",
r"""\begin{mainthm}[Cusp rows and $L(0)$; Category~B since revision~4]\label{thm:K}""")
rep(r"""$H_s$ & $0$ & $a_H=\sqrt\pi(\sqrt{1190}-17\sqrt{14})/170=-0.3035254127$ & $0$ (to 30 digits)\\""",
r"""$H_s$ & $0$ & $a_H=\sqrt\pi(\sqrt{1190}-17\sqrt{14})/170=-0.3035254127$ & $0$\\""")
rep(r"""\caption{Radial coefficients at $q=e^{-t}$ \src{2, A3}. Status as in Theorem~\ref{thm:C}.}\label{tab:radial}""",
r"""\caption{Radial coefficients at $q=e^{-t}$ \src{2, A3}. Status as in Theorem~\ref{thm:C}; since rev.~4 the $H_s$ and $C$ entries are proved closed forms modulo F1 (Theorem~\ref{thm:Hs}).}\label{tab:radial}""")
rep(r"""$r=(1,0),(1,1),(7,-1),(1,2)$. Also $E_{-a}=E_a$ exactly to $q^{3000}$, so the sign-twisted partner $E_a-E_{-a}$ (a weight-$1$
Hecke form in Zwegers' $c_2=\gamma c_1$ set-up) vanishes for this coset.}""",
r"""$r=(1,0),(1,1),(7,-1),(1,2)$. Also $E_{-a}=E_a$, so the sign-twisted partner $E_a-E_{-a}$ (a weight-$1$
Hecke form in Zwegers' $c_2=\gamma c_1$ set-up) vanishes for this coset: in revisions~1--3 this was an exact check to $q^{3000}$ only; since rev.~4 it is
\emph{proved} for every $s\ge5$ (Lemma~R, Theorem~\ref{thm:cthird}).}""")
rep(r"""\catA{Proved. For $C$ the nonvanishing of $a_C$ rests on the 30-digit value $0.8291\ldots$ (far from $0$). This covers every space with""",
r"""\catA{Proved. For $C$ the nonvanishing of $a_C$ rests on its closed form (proved modulo F1 since rev.~4; value $0.8291\ldots$). This covers every space with""")
rep(r"""\catA{Exact finite computation (floating-point exponential sums; nonzero values $\ge0.034$, zeros $<10^{-9}$).}""",
r"""\catA{Zero/nonzero pattern and moduli: exact, by Theorem~\ref{thm:D} (the floating-point exponential sums, nonzero values $\ge0.034$ and zeros $<10^{-9}$, agree).}
\catB{Rev.~4 relabel: the phase values quoted above are floating-point (wide margin) and are not separately proved.}""")
rep(r"""(Category A, finite computation; the second-order formula is a derivation in the source).""",
r"""(Category~B under the rev.~4 convention: floating-point ratios and residuals; the second-order formula is a derivation in the source).""")
rep(r"""the coset and phase) \src{3, A1}, checked for all norms $\le25$ (Category A, numerical).""",
r"""the coset and phase) \src{3, A1}, checked for all norms $\le25$ (Category A for the automorph argument; the numerical check is supporting).""")
# split section
rep(r"""\emph{Function-space dimensions (rev.~3).} Since distinct frequencies give independent mode functions,""",
r"""\emph{Function-space dimensions (rev.~3; exact since rev.~4, Proposition~\ref{prop:matched}).} Since distinct frequencies give independent mode functions,""")
rep(r"""\catA{Numerically verified fits and split (PARI ray-class data for $\fm$; base field certified with \texttt{bnfcertify}$=1$); phases recognised to
$6\cdot10^{-9}$ from $10^{-14}$-accurate fits. The structure of $\mathrm{Cl}^+_{(2\sqrt{35})\infty_1\infty_2}$ is hand-certified (\S\ref{sec:L0});
the structure at the fitting modulus $\fp_2^3\fp_5\fp_7\infty_1\infty_2$ is PARI-only.}""",
r"""\catB{Rev.~4 relabel (Category~A in revisions~1--3): the component fits and the Eisenstein/cusp classification of components are floating-point
(PARI ray-class data for $\fm$; base field certified with \texttt{bnfcertify}$=1$); phases recognised to $6\cdot10^{-9}$ from $10^{-14}$-accurate fits.}
\catA{The structure of $\mathrm{Cl}^+_{(2\sqrt{35})\infty_1\infty_2}$ is hand-certified (\S\ref{sec:L0}); the structure at the fitting modulus
$\fp_2^3\fp_5\fp_7\infty_1\infty_2$ is PARI-only. The dimensions $36$ and $6$, the $S,T$-invariance of the split, and the fact that the $24$ cusp components are exactly the
nonzero labels of odd theta characteristic are exact (Proposition~\ref{prop:matched}).}""")
# Prop spec: rename complement, statuses
rep(r"""$\mathrm{Fix}(P)=V\oplus W$ with a $30$-dimensional $T$-stable complement $W$ (multiplicities $0,1,2$), which the lift functions do not realise.""",
r"""$\mathrm{Fix}(P)=V\oplus V^\perp$ with a $30$-dimensional $T$-stable complement $V^\perp$ (multiplicities $0,1,2$), which the lift functions do not realise.
(Rev.~4 notation: revision~3 called this complement $W$; here $W_P:=\mathrm{Fix}(P)$ and the complement is $V^\perp$.)""")
rep(r"""\catA{(ii) multiplicities on $\mathrm{Fix}(P)$: the eigenvalues are $\pm1$ since $S^2=I$ there (exact), and the trace is numerically $0$ to $10^{-16}$, hence exactly
$0$; (iii) order $140$ exact (monomial $T$, rational phases), multiplicities from the exact phases. (i), (ii) on $V$, (iii) on $V$, (iv): numerically verified
(singular-value gap $17.1\to1.8\cdot10^{-13}$, invariance residuals $\le8\cdot10^{-16}$) \src{14}; (i), (ii) and (iii) on $V$ recomputed with independent code \src{15}.
\emph{Open:} whether $W$ is realised by any functions (the positive-frequency partners $f_{\alpha,\beta}$ span the same $V$ \src{14}); the structure behind
the $6$ cusp combinations.}""",
r"""\catA{Since rev.~4, (i)--(iii) are exact: (i) by Proposition~\ref{prop:matched}; (ii) by the exact Gauss-sum traces of the local factors (Theorem~\ref{thm:tensor7}), which
give $n_\pm=d/2$ on each of the four sectors; (iii) order $140$ exact (monomial $T$, rational phases), multiplicities from the exact phases and the sector
decomposition. In revisions~1--3, (i), (ii) on $V$ and (iii) on $V$ were numerical (singular-value gap $17.1\to1.8\cdot10^{-13}$, invariance residuals
$\le8\cdot10^{-16}$) \src{14}, \src{15}; these numerics agree.}
\catB{(iv): the rank $6$ of the content matrix is floating-point. Its dimension is explained exactly by $V_{\rm cusp}=B_1\otimes X^-$ ($\dim=6$). The complement
$V^\perp=B_1\otimes X^+\oplus A_3\otimes X^-$ is killed by the lift exactly (Proposition~\ref{prop:matched}); the positive-frequency partners $f_{\alpha,\beta}$ span the same $V$
\src{14}. The rev.~2 hypothesis that $V^\perp$ is realised by weight-$1$ lifts is retired, since weight-$1$ vectors lie in $\mathrm{Fix}(-P)$ (connection N7, \S\ref{sec:conn}).}""")
# L(0) section
rep(r"""characters have $L(0)=0$ (Category A from PARI values; Category B as Hecke functional-equation theory).
\catA{Numerically verified, conditional on PARI \texttt{lfun}""",
r"""characters have $L(0)=0$ (Category A from the exact PARI-free Shintani sums of Appendix~\ref{app:pari}; the PARI values agree).
\catB{Rev.~4 relabel (Category~A in revisions~1--3): numerically verified, conditional on PARI \texttt{lfun}""")
rep(r"""All entries are Category A at the stated status; ``exact'' means rational/integer arithmetic.""",
r"""``Exact'' means rational/integer arithmetic. Under the rev.~4 convention, an entry that is exact supports a Category~A statement; a floating-point entry
is supporting evidence for a proved statement where one exists, and is otherwise Category~B.""")
open(f,"w").write(s)
print("part2 ok")
