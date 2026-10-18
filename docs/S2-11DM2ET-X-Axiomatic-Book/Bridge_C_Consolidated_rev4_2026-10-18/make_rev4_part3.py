# rev4 part 3: status table, audit note, caveats, reconciliation (C14 reword, rev.4 items), open problems (C10 fix + new list).
f="bridge_c_consolidated_rev4.tex"
s=open(f).read()
def rep(old,new):
    global s
    c=s.count(old)
    assert c==1, (c, old[:90])
    s=s.replace(old,new)
rep(r"""Thm.~\ref{thm:C} & exact (symbolic EM) for $P_s,R,E,a_P$; $a_H,a_C$ 30-digit evaluation + PSLQ; $H_s$ constant $0$ to 30 digits & Hecke continuation; Siegel--Klingen (sanity check only)\\""",
r"""Thm.~\ref{thm:C} & exact (symbolic EM) for $P_s,R,E,a_P$; $a_H,a_C$ and the $H_s$ constant $0$: proved modulo F1 (rev.~4; were PSLQ / 30 digits) & Hecke continuation; F1; Siegel--Klingen (sanity check only)\\""")
rep(r"""Thm.~\ref{thm:E}(ii) & proved ($a_C\neq0$ from 30-digit value) & none\\""",
r"""Thm.~\ref{thm:E}(ii) & proved ($a_C\neq0$ from its closed form, rev.~4) & F1 (for $C$)\\""")
rep(r"""Thm.~\ref{thm:F} & $S$-law, $T$-law proved, audited once (rev.~3); group relations exact; $\dim V=42$ numerical & none (Borcherds no longer needed)\\""",
r"""Thm.~\ref{thm:F} & $S$-law, $T$-law proved, audited once (rev.~3); group relations exact; $\dim V=42$ exact (rev.~4) & none (Borcherds no longer needed)\\""")
rep(r"""Thm.~\ref{thm:H} & $u_L,u_R$ Eisenstein: proved (PARI-free); $36+6$ split of $V$: numerically verified (two independent codes) & PARI ray-class data""",
r"""Thm.~\ref{thm:H} & $u_L,u_R$ Eisenstein: proved (PARI-free); $36+6$ split of $V$: exact (rev.~4); component fits: Category~B (floating) & PARI ray-class data""")
rep(r"""Thm.~\ref{thm:K} & numerically verified, not proved & PARI \texttt{lfun}\\\bottomrule""",
r"""Thm.~\ref{thm:K} & \textbf{Category B} (rev.~4 relabel): numerically verified, not proved & PARI \texttt{lfun}\\
Thm.~\ref{thm:tensor7} & exact factorisation; congruence by citation & Nobs--Wolfart / Skoruppa / Str\"omberg\\
Prop.~\ref{prop:matched} & exact (upper bound + modular rank lower bound) & as Thm.~\ref{thm:tensor7}\\
Thm.~\ref{thm:tensorodd} & symbolic for all odd $s$; exact at $8$ values of $s$; congruence by citation & as above\\
Thm.~\ref{thm:dims} & exact per $s$ ($s=5..51$, $72$); general-$s$ lower bound open (B) & as above; $\lambda=\tfrac14$ constant-term criterion\\
Prop.~\ref{prop:cuspcrit} & reduction exact; verdicts exact finite per $s$; modulus sufficiency B & Tate; content dictionary\\
Prop.~\ref{prop:deep} & per tested part exact; general $S$-invariance B & as above\\
Thm.~\ref{thm:Hs} & proved modulo F1; numerics supporting & F1; Zwegers Cor.~2.9 (for the completion only)\\
Thm.~\ref{thm:cthird} & (i), (ii) proved; (iii) weight~1 proved, weight~0 by citation (B) & Zwegers 2012 (via a restatement)\\\bottomrule""")
rep(r"""Theorem~\ref{thm:profile} have had no separate audit pass. This pass was also internal (same workflow); it is not external refereeing.""",
r"""Theorem~\ref{thm:profile} have had no separate audit pass. This pass was also internal (same workflow); it is not external refereeing.

\emph{Revision~4.} No new audit pass was made. The revision~4 results (\S\S\ref{sec:family}--\ref{sec:conn}) come from internal reports \src{16}--\src{27} with exact
checks where stated, and an internal cross-review \src{16} that found the inconsistencies corrected in Appendix~\ref{app:rev4}. The short argument for
$d_{\rm Eis}$ at odd $s$ via pure tensors (proof of Theorem~\ref{thm:dims}) was written for this consolidation and has had no separate check.""")
rep(r"""The radical forms of $a_H$, $a_C$ and the exact $\Z[\zeta_{12}]$ $L(0)$ values are recognitions (PSLQ / numerical) rather than derivations. The Gauss-mean
zero/nonzero decisions and the $W_7$ statistics are floating-point with a wide margin.""",
r"""Since rev.~4 the radical forms of $a_H$, $a_C$ are derived (modulo F1), and the $\Z[\zeta_{12}]$ $L(0)$ values are exact PARI-free Shintani sums; only the
$7\times24$ cusp-row identities of Theorem~\ref{thm:K} remain numerical (Category~B). The Gauss-mean zero/nonzero decisions are exact by Theorem~\ref{thm:D}; the
$W_7$ phase values are floating-point with a wide margin (Category~B).""")
rep(r"""\item Component count: the ``36-component'' vector and ``Weil representation on the 35-element discriminant group'' \src{2, 3} are replaced by the
$140$-label family and its $72$-dimensional representation; the lattice is odd and the $T$-law needs $w_c$ \src{4, \S2}
(\path{ERRATUM_psi_Cocycle_Component_Count}). The leading-order $T$-law checks of \src{2, A5} stand, since their shift is $\equiv w_c$ mod $L'$.""",
r"""\item Component count: the ``36-component'' vector of \src{2, 3} is replaced by the $140$-label family and its $72$-dimensional representation; the
lattice is odd and the $T$-law needs $w_c$ \src{4, \S2} (\path{ERRATUM_psi_Cocycle_Component_Count}). The leading-order $T$-law checks of \src{2, A5} stand,
since their shift is $\equiv w_c$ mod $L'$. \emph{Rev.~4 rewording:} what was wrong was the $36$-component Weil claim, not the Weil structure. The
$140$-label representation is exactly $\rho_{2x^2/5}\otimes\rho_{x^2/7}\otimes\rho_2$, the Weil representations of the local forms at $5$ and $7$ tensored with a
$4$-dimensional $2$-adic factor on the theta characteristics (Theorem~\ref{thm:tensor7}).""")
rep(r"""\item Minor numerical differences between runs (e.g.\ Theorem~\ref{thm:I} at rationals""",
r"""\item \emph{Rev.~4.} All further corrections (internal cross-review \src{16}, items C1--C18 there) are listed in Appendix~\ref{app:rev4} and in the repository file
\path{ERRATUM_Consolidated_CrossReview_2026-10-18.md}.
\item Minor numerical differences between runs (e.g.\ Theorem~\ref{thm:I} at rationals""")
# open problems: replace the whole list
i0=s.index(r"""\section{Open problems}\label{sec:open}""")
i1=s.index(r"""\begin{enumerate}[leftmargin=2em]""", i0)
i2=s.index(r"""\end{enumerate}""", i1)+len(r"""\end{enumerate}""")
new_open=r"""\begin{enumerate}[leftmargin=2em]
\item \textbf{Lower bound for $\dim V$ in general.} Prove $\dim V=s(s-1)$ for every odd $s$ (certified exactly only for odd $s\le51$), and find the even-$s$
formula. The even-$s$ tensor factorisation (where $L'/\Z^2$ is not cyclic) is not done.
\item \textbf{The $s=2m^2$ gap.} The gap is exactly $m(m-1)$ for $m=2,\dots,6$. At $s=98$ ($m=7$) the exact bounds $2406\le\dim V\le2408$ do not meet, and
the lower bound is stable from $Q=40$ to $130$: find the two missing relations or prove that they are absent. Prove the gap formula for general $m$, or
refute it.
\item \textbf{The $2$-adic Eisenstein factor $d_2(k,u)$ for $k\ge6$} (first case $s=64$): only exact lower bounds are known.
\item \textbf{$u_L$ cusp criterion.} The ambiguous-class count $|\bar G^\sigma|=2^{\omega(s)}\varphi(s-2)$ in general; $S$-invariance of every $T_\fc$ (deep
bad primes); sufficiency of the modulus $M=2dc$ for all norms; complete coverage at $s=32,34,36,40$ (predicted CUSP).
\item \textbf{Arithmetic of the sectors.} An exact ray-class (Hecke-character) proof that the non-all-even local sectors are cuspidal for general $s$;
identification of the local reflections $Z_p$ with Atkin--Lehner operators on the lifted forms; which Hecke eigenforms make up $V_{\rm cusp}$.
\item \textbf{$H_s$.} Orders $t^{7/2}$ and beyond at $x=0$ (mechanical); a re-derivation of the corner terms at integer orders inside the extended
computation; closed forms at $x\neq0$ via Gauss-sum-weighted Euler--Maclaurin; stable numerics at $x=\tfrac12$ ($s=7,9,10$) and $x=\tfrac13$ ($s=7,10$),
which are not quoted here.
\item \textbf{$\Cthird$.} A rigorous pairing argument for $\int_{\Gamma_F}\Xi_1\,dt=0$; a direct check of Zwegers' 2012 paper (only a restatement was
read); whether any single-weight object, or a depth-$2$ theta on a rank-$3$ lattice obtained with $\theta_3$, carries both parts.
\item \textbf{Retained from revision~3:} hand certification of the ray-class structure at $\fp_2^3\fp_5\fp_7\infty_1\infty_2$; an arithmetic proof of
Theorem~\ref{thm:J}; a proof of Theorem~\ref{thm:K} (Category~B); the Lewis--Zagier interpretation (Category~B); the prescription behind the framework's
``Fricke samples''.
\item \textbf{Refereeing.} Independent (external) refereeing of Theorems~\ref{thm:B}, \ref{thm:F}, \ref{thm:G}, \ref{thm:profile}, \ref{thm:tensor7},
\ref{thm:tensorodd}, \ref{thm:dims}, \ref{thm:Hs} and of the internally audited Theorems~\ref{thm:I}--\ref{thm:J}.
\end{enumerate}
\emph{Removed in rev.~4 (C10):} the rev.~3 item ``$s=8$ and $s=11$ analogues (computation in progress)'' was stale and contradicted Appendix~\ref{app:s811}: the
$q$-series identity has been checked for $s=7,8,11$; ``$D=99$'' was the radicand $n_{11}=s(s-2)$, not a discriminant (notation, Appendix~\ref{app:rev4}); and $E_8$
does not double count. The $s=8,11$ data are in Appendix~\ref{app:s811} and \S\ref{sec:family}. The rev.~3 item on the $30$-dimensional complement is answered
(Proposition~\ref{prop:matched}): the lift kills $V^\perp$ exactly."""
s=s[:i1]+new_open+s[i2:]
open(f,"w").write(s)
print("part3 ok")
