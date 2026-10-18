# rev4 part 4: appendix A fixes (s=8/11: C2, C11, C17, notation for D), g_s / C_third notes, source list.
f="bridge_c_consolidated_rev4.tex"
s=open(f).read()
def rep(old,new):
    global s
    c=s.count(old)
    assert c==1, (c, old[:90])
    s=s.replace(old,new)
rep(r"""\catA{Computed or checked on the box, exact or to the stated finite range \src{10}; transfers of the $s=7$ proof template are Category B.}""",
r"""\catA{Computed or checked on the box, exact or to the stated finite range \src{10}; transfers of the $s=7$ proof template are Category B. Rev.~4: the
floating-point items below (content norms, Herglotz agreement, character contents) are Category~B under the rev.~4 convention; the corrected dimensions
are exact (Theorem~\ref{thm:dims}).}""")
rep(r"""\item Fields and orders: $s=8$: $\Q(\sqrt3)$, order $\Z[2\sqrt3]$, $\varepsilon=2+\sqrt3$, $\gamma$-eigenvalue $\varepsilon^2$ but multiplicity
one (no double counting, answering the caveat in \S\ref{sec:open}); $s=11$: $\Q(\sqrt{11})$, order $\Z[3\sqrt{11}]$, $\varepsilon=10+3\sqrt{11}$.""",
r"""\item Fields and orders: $s=8$: $\Q(\sqrt3)$, order $\Z[2\sqrt3]$; the maximal order has fundamental unit $2+\sqrt3$, but $2+\sqrt3\notin\Z[2\sqrt3]$ and the
fundamental unit of the order is $7+4\sqrt3=(2+\sqrt3)^2$, which is the $\gamma$-eigenvalue $\varepsilon_\gamma$ (rev.~4 correction C17; statements made for
``$\varepsilon=2+\sqrt3$'' hold for the maximal order only). Multiplicity one (no double counting). $s=11$: $\Q(\sqrt{11})$, order $\Z[3\sqrt{11}]$,
$\varepsilon=10+3\sqrt{11}$.""")
rep(r"""characters of conductor $(3)$ and $(9)$); $\psi=\psi_{\rm Eis}+\psi_{\rm cusp}$ with $\psi_{\rm cusp}\neq0$ at $8$ rationals. So ``$\psi$ is purely
Eisenstein'' is not family-wide. Cusp rank $\ge73$ and $\ge90$ dihedral newforms for $s=11$ are lower bounds.""",
r"""characters of conductor $(3)$ and $(9)$; confirmed by the exact ray-class test of \src{20}); $\psi=\psi_{\rm Eis}+\psi_{\rm cusp}$ with $\psi_{\rm cusp}\neq0$ at $8$
rationals (floating, Category~B). So ``$\psi$ is purely Eisenstein'' is not family-wide. \textbf{Rev.~4 correction (C2):} the rev.~2/3 statement ``cusp rank
$\ge73$, Eisenstein $\le37$'' for the $s=11$ family is wrong. Exactly, $\dim V=110$, $d_{\rm Eis}=90$ and $d_{\rm cusp}=20$ (Theorem~\ref{thm:dims}). The count
``$\ge90$ dihedral newforms'' from conductor norms is Category~B and is not a dimension: as at $s=7$, the forms can occur only in fixed combinations.""")
rep(r"""\textbf{Cusp onset} (Category A for the counts; Category B for ``$h^+\neq\#$genera $\Leftrightarrow$ cusp part'').
With $D=4s(s-2)$ ($s$ odd), $s(s-2)$ ($s$ even), $h^+$ equals the number of genera for every $s\in\{3,\dots,20,30\}$ except $s=11$ ($8$ vs $4$)
and $s=19$ ($8$ vs $4$); also $s=25$ ($12$ vs $4$) and $s=41$ ($24$ vs $8$). The cusp onset is at $s=11,19,25,41$ in the tested range; only
$s=11$ has an actual cusp decomposition (the others are predictions, Category B). The onset is invisible in all radial data at $x=0$, which are
$s$-uniform (\S\S\ref{app:zeta}--\ref{app:gs}).""",
r"""\textbf{Class numbers versus genera} (Category A for the counts). With $D_s$ the discriminant of the order ($D_s=4s(s-2)$ for $s$ odd, $s(s-2)$ for $s$ even;
notation of rev.~4, Appendix~\ref{app:rev4}), $h^+$ equals the number of genera for every $s\in\{3,\dots,20,30\}$ except $s=11$ ($8$ vs $4$) and $s=19$ ($8$ vs
$4$); also $s=25$ ($12$ vs $4$) and $s=41$ ($24$ vs $8$).

\textbf{Rev.~4 correction (C11): the rule ``cusp part $\Leftrightarrow h^+\neq\#$genera'' is refuted}, and the ``cusp onset at $s=11,19,25,41$'' of revisions~2--3
is withdrawn. At the level of the family span the cusp part is generic: $d_{\rm cusp}>0$ for every odd $s$ in $5..51$, including $s=5,7,13,15$ where
$h^+=\#$genera (Theorem~\ref{thm:dims}). At the level of $u_L$ the implication fails at $s=14,17,18,22,23$ (cusp content with $h^+=\#$genera); the correct
criterion is Proposition~\ref{prop:cuspcrit}. The two notions are distinct. Both are invisible in the radial data at $x=0$, which are $s$-uniform
(\S\S\ref{app:zeta}--\ref{app:gs}).""")
rep(r"""Higher radial coefficients of $H_s$ in $s$ are not computed (open).""",
r"""Higher radial coefficients of $H_s$ in $s$: computed in rev.~4 through $t^{5/2}$ (Theorem~\ref{thm:Hs}).""")
rep(r"""algebraic and $\beta=-\tfrac7{20}G(x)$, which vanishes iff $2\mid m$ or $5\mid m$;""",
r"""algebraic and $\beta=-\tfrac7{20}G(x)$, which vanishes iff $2\mid m$ or $5\mid m$ (Theorem~\ref{thm:D});""")
# sources
rep(r"""All in \path{/workspace/quantum-comp/reports/heavy-daily/}, with scripts and outputs in the companion folders. [S14] and [S15] were added in revision~3.""",
r"""All in \path{/workspace/quantum-comp/reports/heavy-daily/}, with scripts and outputs in the companion folders. [S14] and [S15] were added in revision~3,
[S16]--[S27] in revision~4. Repository copies of [S16]--[S27] are listed in \path{PUSH_LOG_2026-10-18_Rev4.md}.""")
rep(r"""\item \texttt{2026-10-18-Audit-and-ProfileLaw.md} and folder \path{2026-10-18-Audit-and-ProfileLaw/} (second internal audit; profile-law proof and checks) (rev.~3).
\end{enumerate}""",
r"""\item \texttt{2026-10-18-Audit-and-ProfileLaw.md} and folder \path{2026-10-18-Audit-and-ProfileLaw/} (second internal audit; profile-law proof and checks) (rev.~3).
\item \texttt{2026-10-18-Cross-Review.md} (internal cross-review: contradictions C1--C18, connections N1--N11) (rev.~4).
\item \texttt{2026-10-18-Tensor-Pattern-Proof.md} (local structure; numerical certificates, superseded where [S18] is exact) (rev.~4).
\item \texttt{2026-10-18-Tensor-Pattern-Closure.md} (exact tensor factorisation at $s=7$; $V$ = matched sectors) (rev.~4).
\item \texttt{2026-10-18-General-s-Tensor.md} (exact factorisation for odd $s$) (rev.~4).
\item \texttt{2026-10-18-Cusp-Onset.md} (function-span dimensions, floating; exact $u_L$ ray-class test) (rev.~4).
\item \texttt{2026-10-18-Cusp-Onset-Closure.md} (orbit bound, exact ranks, $s=2m^2$ mechanism, $u_L$ criterion, deep bad primes) (rev.~4).
\item \path{2026-10-18-H_s-Closed-Forms.md} ($H_s$ $q$-series, Zwegers parameters, radial coefficients through $t^{1/2}$) (rev.~4).
\item \path{2026-10-18-H_s-Closure.md} ($t^{3/2}$, $t^{5/2}$; $H_{-1}(x)=0$) (rev.~4).
\item \texttt{2026-10-18-C\_third-Unified.md} (single coset; Lemma~R; parity split) (rev.~4).
\item \texttt{2026-10-18-C\_third-Closure.md} (single kernel, two chains) (rev.~4).
\item \texttt{2026-10-18-V42-Structure.md} (irreducible pieces of $W_P$; its local forms are corrected in [S17]) (rev.~4).
\item \texttt{2026-10-18-rev3-changes-note.md} (planning note for rev.~3) (rev.~4, for provenance).
\end{enumerate}""")
rep(r"""\bibitem{Zw} S.~Zwegers, \emph{Mock theta functions}, Ph.D. thesis, Utrecht, 2002, arXiv:0807.4834. [Local copy used in \src{2}; Cor.~2.9.]""",
r"""\bibitem{Zw} S.~Zwegers, \emph{Mock theta functions}, Ph.D. thesis, Utrecht, 2002, arXiv:0807.4834. [Local copy used in \src{2}; Cor.~2.9.]
\bibitem{Zw12} S.~Zwegers, Mock Maass theta functions, \emph{Q. J. Math.} \textbf{63} (2012), 753--770. [Abstract and review read in \src{24}; used via the restatement in \cite{BCN}; the paper itself was not read.]
\bibitem{BCN} K.~Bringmann, W.~Craig, C.~Nazaroglu, arXiv:2409.17818, \S2.2. [Restatement of Zwegers' 2012 Lemma~2.4, read in \src{25}.]
\bibitem{Weil} A.~Nobs, J.~Wolfart (1976); N.-P.~Skoruppa; F.~Str\"omberg, Weil representations associated with finite quadratic modules, \emph{Math. Z.} \textbf{275} (2013). [Congruence and tensor-product properties of Weil representations of finite quadratic modules of odd order; cited in \src{18}, \src{19}; convention checked against the exact $s=7$ relations, not line by line against the published text.]""")
open(f,"w").write(s)
print("part4 ok")
