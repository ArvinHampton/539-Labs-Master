---
title: "Residual Ternary Algebra and Bridge Series C: The Residual–Resonant Frame for the S²-11DM²ET-X Model"
author: "Arvin B. Hampton — 539 Labs, Project Quantum Comp"
date: "3 November 2026"
abstract: |
  We develop the residual (ternary) discrete algebra of the S²-11DM²ET-X model. We separate it formally from the resonant schedule that shares its central integer. Packaging $N_{\mathrm{flux}}=4880$ flux units with seed $f_{\max}=21$ leaves $B'=\lfloor 4859/9\rfloor=539$ pieces in each of nine charge sectors. This 539 is a count. The resonant schedule $18+521=539$ is an iteration length, with $18=\lfloor e^3/\ln 3\rfloor$. The free canonical ternary map $T_3$ takes $4880$ to $1$ in $14$ steps.

  On the product complex $X_\times=K_9\times P_{B'}$ we prove that the cycle rank of the product graph is $\beta_1=36B'-8=19396$, and that the mixed cochain $\eta$ is closed. On the thin residual form complex $F$ we prove $H^0(F)\cong\mathbb{Q}$, $H^1(F)=0$ and $H^2(F)\cong\mathbb{Q}\cdot[s_{\alpha\delta}]$. We show that $F$ is formal and that its essential class is unique. We prove that the class $[s_{\alpha\delta}]$ is a feature of the thin truncation: in the full product cochain complex, $s_{\alpha\delta}$ is not closed and $H^2=0$.

  We derive three further results: the static classifier $D_1$ has rank one; the residual count and the resonant clock cannot be identified; and the residual core cannot force the alternating group $A_5$ on the natural flux quintic. For the real-quadratic field $\mathbb{Q}(\sqrt{35})$ we record the 14-dimensional level-one parallel-weight-two cuspidal newspace $V_{35}$ as a cited database result. We isolate precisely which definitions and lemmas are missing for the bridge $A1\to\Xi\to\mathrm{RTA}$, for the eleven-dimensional Einstein–Hampton programme, and for the related non-local questions.
---

# 1. Introduction

The S²-11DM²ET-X model attaches two different meanings to the integer 539, and conflating them leads to false statements. This paper takes the separation as its organising principle.

- **Residual discrete algebra** studies the combinatorics of what is left over after the flux is packaged under Principle (S). Its 539 is the cardinality $B'$ of each of nine sector cores.
- **Resonant algebra** is a design choice. It fires a local ternary step a fixed number of times, $18+521=539$, and then stops.
- A third number, about $14$, is the typical depth of the free basins of the canonical ternary map $T_3$. That map contracts by a factor $2/3$ on average.

In short: *a count is not a clock.*

The paper is organised as follows.

- §2 constructs the residual product complex and the thin form complex, computes their cohomology, and proves formality and uniqueness of the essential class.
- §3 proves the separation theorem.
- §4 treats the static classifier $D_1$ and the static budget $S_{\mathrm{eff}}$.
- §5 develops the local path through Bridge Series C and the newspace $V_{35}$.
- §6 states what is presently available for the non-local path.
- §7 summarises a consistency audit of the corpus.
- §8 ranks the open steps toward a residual foundation of RTA.

Throughout, a claim is either **proved**, with a complete proof, or explicitly described as **not established from the definitions and lemmas presently available**, in which case we name what is missing. Category A denotes statements of the discrete residual algebra. Category B denotes continuum and physical interpretations, which are not used in any proof.

All cochains have rational coefficients unless stated otherwise.

# 2. Residual ternary algebra

## 2.1 Packaging

**Definition 2.1.** Let $N_{\mathrm{flux}}=\lfloor e^3\cdot 3^5\rfloor=4880$ and $f_{\max}=\lceil 4880/243\rceil=21$. The *residual pool* is $R=N_{\mathrm{flux}}-f_{\max}$. The *residual cardinality* is $B'=\lfloor R/9\rfloor$. Each of the nine charge sectors carries a core of $B'$ leftover pieces.

**Proposition 2.2.**

- (a) $R=4859=9\cdot539+8$, so $B'=539$.
- (b) $N_{\mathrm{flux}}-9B'=29$.
- (c) $B'=7^2\cdot 11$, and $B'\equiv3\pmod 8$.
- (d) $B'-1\equiv2\pmod8$.

*Proof.* (a) $e^3\cdot243=4880.78\ldots$ and $4880/243=20.08\ldots$, so $N_{\mathrm{flux}}=4880$ and $f_{\max}=21$. Then $9\cdot 539=4851$ and $4859-4851=8<9$. (b) $4880-4851=29$. (c) $49\cdot11=539$ and $539=8\cdot67+3$. (d) $538=8\cdot67+2$. $\square$

## 2.2 The product complex

Let $K_9$ be the complete simplicial complex on the sectors $\{0,\dots,8\}$, and let $P_{B'}$ be the path with vertices $0,\dots,B'-1$ and edges $e_i=(i\to i+1)$. Set
$$X_\times:=K_9\times P_{B'} .$$
Its cells are:

- vertices $(a,i)$;
- horizontal edges $(a,b;i)$ and vertical edges $(a;e_i)$;
- triangles $(a,b,c;i)$ and squares $(a,b)\times e_i$;
- prisms $(a,b,c)\times e_i$, together with higher cells.

The product differential is
$$D(\varphi\otimes\psi)=d_Q\varphi\otimes\psi+(-1)^{\deg\varphi}\,\varphi\otimes d_P\psi ,$$
and $D^2=0$ by the graded Leibniz rule.

The basic cochains are:

- $\alpha(a,b)=\mathrm{sgn}(a-b)$;
- $\omega_2=d_Q\alpha$;
- $\mu=B'\,\alpha\smile\alpha$;
- the tower label $f(i)=\tau(x_i)$ of the $i$-th element of the ordered core;
- $\delta f=d_Pf$.

**Lemma 2.3.** For distinct sectors, $\omega_2(a,b,c)=\alpha(a,b)+\alpha(b,c)+\alpha(c,a)$. On ordered triples $a<b<c$ this gives $\omega_2=-1$ and $\mu=B'$, so $\mu=-B'\omega_2$.

*Proof.* By definition $(d_Q\alpha)(a,b,c)=\alpha(b,c)-\alpha(a,c)+\alpha(a,b)$, and $\alpha$ is skew. For $a<b<c$ the three terms are $-1,-1,+1$, which sum to $-1$. Also $\mathrm{sgn}(a-b)\,\mathrm{sgn}(b-c)=1$. $\square$

**Theorem 2.4 (mixed closure).** The cochain $\eta:=\alpha\otimes\delta f-\omega_2\otimes f$ satisfies $D\eta=0$.

*Proof.* We use $d_P\delta f=0$ (the path has no 2-cells) and $d_Q\omega_2=0$. Then
$$D(\alpha\otimes\delta f)=\omega_2\otimes\delta f \qquad\text{and}\qquad D(\omega_2\otimes f)=\omega_2\otimes\delta f .$$
Subtracting gives $D\eta=0$. $\square$

**Proposition 2.5.** The following hold.

- $\sum_{a<b<c}\mu(a,b,c)=84B'=45276$.
- $\sum_{a\ne b}\sum_i\alpha(a,b)\,\delta f(i)=0$.
- There are $72$ oriented squares over each path edge.

*Proof.* There are $\binom93=84$ ordered triples, and $\mu=B'$ on each by Lemma 2.3. Since $\alpha$ is skew, $\sum_{a\neq b}\alpha(a,b)=0$, and this factor multiplies the double sum. Finally, $9\cdot8=72$. $\square$

## 2.3 The cycle space

**Theorem 2.6.** Let $G_\times=K_9^{(1)}\,\square\,P_{B'}$ be the Cartesian product of undirected 1-skeleta. Then $G_\times$ is connected, and
$$\beta_1(G_\times)=36B'-8 .$$
At $B'=539$ this gives $V=4851$, $E=24246$ and $\beta_1=19396$.

*Proof.* There are $V=9B'$ vertices. The edges are $\binom92=36$ per level, plus $B'-1$ per sector, so $E=36B'+9(B'-1)$. Any vertex $(a,i)$ is joined to $(0,i)$ and then along the path to $(0,0)$, so the graph is connected. For a connected graph, $\beta_1=E-V+1=36B'-8$. $\square$

The rank of the cycle group of the 1-skeleton is $E-\operatorname{rank}\partial_1=E-V+1$. This is the same number, so the "free cycle space" of $X_\times$ has rank exactly $36B'-8$. A direct union-find computation of $E-V+c$ agrees with the formula for $B'\in\{1,2,3,10,100,538,539,540\}$. If horizontal edges are counted as ordered pairs, the analogous count is $72B'-8$. We use the undirected convention.

## 2.4 The thin residual form complex

**Definition 2.7.** The thin residual form complex $F^\bullet$ is the $\mathbb{Q}$-complex with the following generators.

- $F^0=\langle\mathbf 1,\,f\rangle$.
- $F^1=\langle h_\alpha,\,v_\delta,\,h_{\alpha f}\rangle$, where $h_\alpha=\alpha\otimes1$, $v_\delta=1\otimes\delta f$ and $h_{\alpha f}=\alpha\otimes f$.
- $F^2=\langle t_\mu,\,t_\omega,\,s_{\alpha\delta},\,t_{\omega f}\rangle/(t_\mu+B't_\omega)$, where $t_\omega=\omega_2\otimes1$, $t_\mu=\mu\otimes1$, $s_{\alpha\delta}=\alpha\otimes\delta f$ and $t_{\omega f}=\omega_2\otimes f$.
- $F^{n}=0$ for $n\geq3$.

The differential is
$$D\mathbf 1=0,\quad Df=v_\delta,\quad Dh_\alpha=t_\omega,\quad Dv_\delta=0,\quad Dh_{\alpha f}=t_{\omega f}-s_{\alpha\delta},\quad D|_{F^2}=0 .$$

These values follow from the product rule. For example, $D(\alpha\otimes f)=\omega_2\otimes f-\alpha\otimes\delta f$. The relation $t_\mu=-B't_\omega$ is Lemma 2.3.

*Remark 2.8.* $F$ is the brutal truncation $\sigma_{\le2}$ of the generator model, so $H^2(F)=\operatorname{coker}(D^1:F^1\to F^2)$. The generator $f$ must lie in $F^0$, because the product structure requires $Df=d_Pf=\delta f$.

If $f$ is omitted from $F^0$, then $v_\delta$ becomes a cocycle that is not a coboundary, and $H^1\cong\mathbb{Q}$. With $f$ omitted, exact rank computation gives $H^\bullet=(1,1,1)$. With $f$ included it gives $(1,0,1)$. Only the latter is compatible with formality onto $\mathbb{Q}[0]\oplus\mathbb{Q}[-2]$.

**Theorem 2.9 (form cohomology).** Over $\mathbb{Q}$, we have $H^0(F)=\mathbb{Q}[\mathbf 1]$, $H^1(F)=0$, $H^2(F)=\mathbb{Q}\,[s_{\alpha\delta}]$, and $H^{\ge3}(F)=0$. Moreover
$$[\eta]=[t_\mu]=[t_\omega]=0 \qquad\text{and}\qquad [t_{\omega f}]=[s_{\alpha\delta}] .$$

*Proof.* Eliminating $t_\mu$, the space $F^2$ has basis $(t_\omega,s_{\alpha\delta},t_{\omega f})$. In the bases above, the differentials are
$$D^0=\begin{pmatrix}0&0\\0&1\\0&0\end{pmatrix},\qquad D^1=\begin{pmatrix}1&0&0\\0&0&-1\\0&0&1\end{pmatrix},\qquad D^2=0,$$
with ranks $1$, $2$ and $0$.

- *Degree 0.* $\ker D^0=\langle\mathbf 1\rangle$.
- *Degree 1.* $\ker D^1=\langle v_\delta\rangle=\operatorname{im}D^0$, so $H^1=0$.
- *Degree 2.* $\dim H^2=3-2=1$.

Next we show $s_{\alpha\delta}\notin\operatorname{im}D^1=\langle t_\omega,\,t_{\omega f}-s_{\alpha\delta}\rangle$. Suppose $s_{\alpha\delta}=x\,t_\omega+y\,(t_{\omega f}-s_{\alpha\delta})$. Comparing coefficients gives $x=0$, $y=0$ and $1=-y$, which is impossible.

Finally:

- $\eta=s_{\alpha\delta}-t_{\omega f}=-Dh_{\alpha f}$;
- $t_\omega=Dh_\alpha$;
- $t_\mu=D(-B'h_\alpha)$;
- $t_{\omega f}-s_{\alpha\delta}\in\operatorname{im}D^1$, so $[t_{\omega f}]=[s_{\alpha\delta}]$. $\square$

**Corollary 2.10 (unique essential class).** Every $z\in F^2$ can be written as $z=\lambda s_{\alpha\delta}+Dw$, with $\lambda\in\mathbb{Q}$ unique.

*Proof.* This is immediate from $\dim H^2(F)=1$ and $[s_{\alpha\delta}]\ne0$. $\square$

We write $\xi_{\mathrm{mix}}:=[s_{\alpha\delta}]\in H^2(F)\cong\mathbb{Q}$ for the *mixed class*. It is the coupling of sector orientation $\alpha$ with residual tower transport $\delta f$.

**Theorem 2.11 (formality).** Let $H=\mathbb{Q}e_0\oplus\mathbb{Q}e_2$ with zero differential. The map $\iota:H\to F$ given by $e_0\mapsto\mathbf 1$ and $e_2\mapsto s_{\alpha\delta}$ is a quasi-isomorphism. Hence $F\simeq\mathbb{Q}[0]\oplus\mathbb{Q}[-2]$ in $D(\mathbb{Q})$, and all Massey products in $H(F)$ vanish.

*Proof.* $\iota$ is a chain map, because both images are cocycles. By Theorem 2.9, $H(\iota)$ is an isomorphism in every degree.

An explicit contraction of the complement is given by the isomorphisms $\langle f\rangle\cong\langle v_\delta\rangle$ and $\langle h_\alpha,h_{\alpha f}\rangle\cong\langle t_\omega,\,t_{\omega f}-s_{\alpha\delta}\rangle$.

For the Massey products: a triple product of degree-2 classes would lie in degree $5$, where $H^5(F)=0$, and products with $[\mathbf 1]$ are trivial. $\square$

## 2.5 The full product complex

**Proposition 2.12.** Let $\overline X_\times$ be the full product $\Delta^8\times P_{B'}$, with all simplices of the 8-simplex. Then:

- (a) $\tilde H^\bullet(\overline X_\times;\mathbb{Z})=0$.
- (b) On each prism, $D s_{\alpha\delta}\big((a,b,c)\times e_i\big)=\omega_2(a,b,c)\,\delta f(i)$. Hence $s_{\alpha\delta}$ is a cocycle if and only if $\delta f\equiv0$.
- (c) For the residual tower labels, $\delta f\in\{0,1\}$ and $\delta f$ is nonzero on $241$ of the $538$ path edges. Hence $s_{\alpha\delta}$ fails to be closed on $84\cdot241=20244$ prisms.
- (d) $\eta$ is closed and exact: $\eta=-D(\alpha\otimes f)$.

*Proof.* (a) The product of a simplex and an interval is contractible. (b) This is the first identity in the proof of Theorem 2.4, evaluated on the prism. (c) This is a direct evaluation of $f$ on the ordered core: there are 243 towers, with loads $21$ (twenty towers) and $20$ (the rest), and the core is taken as every ninth element of the residual pool. (d) This is the product rule. $\square$

Thus $\xi_{\mathrm{mix}}$ is a class of the thin truncation $F$, namely the generator of $\operatorname{coker}D^1$. It is not a class of the full product cochain complex. Retaining the degree-3 generator $\omega_2\otimes\delta f$ in the generator model gives $H^2=0$, because then $\ker D^2=\langle t_\omega,\,t_{\omega f}-s_{\alpha\delta}\rangle=\operatorname{im}D^1$.

No untruncated complex in which $\xi_{\mathrm{mix}}$ is a nonzero cohomology class is established from the definitions presently available.

# 3. Resonant algebra and separation

## 3.1 The free map

The canonical ternary map is defined by
$$T_3(n)=\begin{cases} n/3, & n\equiv0 \pmod 3,\\ \lfloor (4n+2)/3\rfloor, & n\equiv1 \pmod 3,\\ \lfloor(2n+1)/3\rfloor, & n\equiv2 \pmod 3,\end{cases}$$
with $T_3(0)=0$.

**Proposition 3.1.**

- (a) The orbit $4880\to3253\to4338\to1446\to482\to321\to107\to71\to47\to31\to42\to14\to9\to3\to1$ has $14$ steps.
- (b) $10^{18}$ reaches $1$ in $92$ steps, and $1616033987$ reaches $1$ in $37$ steps.
- (c) On $[1,50000]$ the maximal orbit length is $55$, attained exactly at $36043$ and $36592$.
- (d) $\{1,2\}$ is a 2-cycle.

*Proof.* (a)–(c) are exact iteration. (d) $T_3(1)=2$ and $T_3(2)=1$. $\square$

The branch factors $1/3$, $4/3$ and $2/3$ have geometric mean $2/3$. This is the heuristic behind the average contraction factor $2/3$, and the Lyapunov exponent $\ln(2/3)<0$. A measure-theoretic proof that the typical depth is about $14$ is not established from the lemmas presently available. That figure is empirical.

## 3.2 The resonant schedule

**Definition 3.2.** The window is $W=\lfloor e^3/\ln3\rfloor$ and the body is $b=521$. The resonant schedule fires the local ternary step exactly $W+b$ times and then stops. The counter is the stopping rule.

**Proposition 3.3.** $W=18$, so $W+b=539$.

*Proof.* $e^3/\ln3=18.2826\ldots$ $\square$

**Theorem 3.4 (separation).** Define three functions:

- $\mathcal R(N,f,k)=\lfloor(N-f)/k\rfloor$;
- $\mathcal S(W,b)=W+b$;
- $\mathcal L(n)=\min\{t: T_3^t(n)\in\{0,1\}\}$.

Then:

- (a) $\mathcal R(4880,21,9)=\mathcal S(18,521)=539$, while $\mathcal L(4880)=14$.
- (b) Neither of $\mathcal R$ and $\mathcal S$ factors through the other on the data that define them.
- (c) Every object of §2 (the spaces $F$ and $H^\bullet(F)$, and the classifier $D_1$ of §4) is a finite-dimensional $\mathbb{Q}$-vector space or a linear map. None of them carries an iteration parameter.

Consequently, $539$ is not the free stopping time of $N_{\mathrm{flux}}$, and no result of §2 implies or uses a number of iterations.

*Proof.* (a) follows from Propositions 2.2, 3.3 and 3.1.

(b) Compare $\mathcal R(4880,21,9)=539$ with $\mathcal S(18,522)=540$, and $\mathcal S(18,521)=539$ with $\mathcal R(4889,21,9)=540$. In each pair, one function keeps the value 539 while the other changes it, so neither value determines the other.

(c) Inspect Definition 2.7 and §4. $\square$

**Corollary 3.5.** A finite schedule determines no cell complex, covering or local system. Any geometry attached to the schedule, to $540=539+1$, or to a phase law $2\cos\theta$ is a Category B interpretation.

*Proof.* A counter carries no incidence data. The phase angle is continuum-valued and is not determined by any residual datum. $\square$

The only geometry forced by the residual core is the contractibility of Proposition 2.12(a).

# 4. The static classifier $D_1$ and the budget $S_{\mathrm{eff}}$

**Definition 4.1 ($D_1$).** $D_1$ is a static invariant classifier on the nine charge sectors of $X_\times$, over $\mathbb{Q}$. It is independent of time, schedule and metric, so the normalisation scale is $\Lambda_0=\emptyset$. Its invariant subspace is the span of $\xi_{\mathrm{mix}}=[s_{\alpha\delta}]$ in $H^2(F)$. It shares no structure with the resonant counter, in the precise sense of (ND) below.

**(ND) Non-identification.** The definition of $D_1$ uses only the cells of $X_\times$ and the cochains $\alpha,\omega_2,\mu,f,\delta f$. It takes no argument from, and no value in, the counter set $\{1,\dots,W+b\}$. No map of chain complexes, graded vector spaces or sets from $C^\bullet(X_\times)$, $F$ or $H^\bullet(F)$ to that counter set is part of the definition. The equality $B'=W+b$ is an equality of values, not a structure map.

**Proposition 4.2.** $D_1$ has rank exactly one. In particular its rank is independent of the cycle rank $\beta_1(G_\times)=19396$.

*Proof.* By Theorem 2.9, $\xi_{\mathrm{mix}}\neq0$ and $\dim H^2(F)=1$. The cycle rank belongs to the graph layer, a different complex (Theorem 2.6). $\square$

**Proposition 4.3.** Property (ND) holds for $D_1$ as defined.

*Proof.* This is Theorem 3.4(c). $\square$

Layer 2, the component that would implement $D_1$, has not yet been constructed from this definition. No result here depends on it.

**Definition 4.4 ($S_{\mathrm{eff}}$).** $S_{\mathrm{eff}}$ treats $T_3=539$ as a static cell capacity, or hash budget. It is not a convergence rate or a stopping time. The assignment
$$\mathcal M:S_{\mathrm{eff}}\to\mathrm{Residual}_{539}\times\mathrm{Resonant}_{539}$$
has independent projections: the residual projection depends only on $(N_{\mathrm{flux}},f_{\max},9)$, and the resonant projection only on $(W,b)$. The internal stability bound is the free attractor depth of §3.1. The $539$-step schedule is an external, constant-time override. A dual-rail ternary representation of local remainders belongs to the hardware layer and is not part of the algebraic definition.

**Proposition 4.5.** No global congruence $\Omega\equiv0\pmod{539}$ holds as a cancellation criterion.

*Proof.* In $\mathbb{Z}[\mathbb{Z}/3]$, Proposition 5.3 below exhibits a cancelling configuration whose determinants are $2$ and $36$, which are nonzero. The quantity $\Omega$ attached to it is $2$, and $2\not\equiv0\pmod{539}$. A winding functional $W$ that would make $\Omega$ a criterion is not defined in the lemmas presently available. $\square$

# 5. The local path: Bridge Series C

## 5.1 From packaging to Bridge Series C

The packaging integers factor through $7$, $11$ and $3^5$:

- $B'=7^2\cdot11$;
- $18=7+11$;
- $68=3\cdot11+5\cdot7$;
- $67=7\cdot11-5\cdot2$;
- $243=3^5$.

These factorisations single out the residual parameters $s\in\{7,8,11\}$. For such $s$, let
$$g_s(q)=\sum_{n\ge0}\frac{q^{n^2}}{(-q^s;q^s)_n}.$$
For $s=1$ this has the shape of Ramanujan's fifth-order mock theta function $f_0$. The orthant counts are $P_s=(-q^s;q^s)_\infty\,g_s$. Let $H_s$ be the cone-weighted series on the associated indefinite lattice of signature $(1,1)$. The coordinate orthant is not a cone chamber of that lattice, and **Bridge Series C** measures the mismatch:
$$C:=P_{\mathrm{orth}}-H_s .$$
For $s=7$ the quadratic form is $Q(n,k)=n^2+7nk+\tfrac72k(k+1)$. The series splits as $C_7=C_{\mathrm{axis}}+C_{\mathrm{third}}$, with coefficients in $\{0,1,\tfrac32\}$ and support on the residues $0,1,2,4\bmod7$. The residual shadow $\Xi$ is a weight-$3/2$ series. Its Eichler integral, together with the axis period, is the candidate residual period of $C$. The published theorems on $g_s$ and $C$ [R1, R2] are used with the hypotheses stated there.

## 5.2 The field $\mathbb{Q}(\sqrt{35})$ and the newspace $V_{35}$

**Proposition 5.1.** Let $K=\mathbb{Q}(\sqrt{35})$, of discriminant $140$, with fundamental unit $\varepsilon=6+\sqrt{35}$.

- (a) $N(\varepsilon)=1$ and $\operatorname{Tr}\varepsilon=12$.
- (b) The regulator is $\ln\varepsilon=2.477888\ldots$
- (c) With $h_K=2$, $\operatorname{Res}_{s=1}\zeta_K=2h_K\ln\varepsilon/\sqrt{140}=0.837679\ldots$
- (d) The odd residues $r$ modulo $140$ with $(140/r)=-1$ are 3, 11, 27, 37, 39, 41, 47, 51, 53, 57, 61, 69, 71, 79, 83, 87, 89, 93, 99, 101, 103, 113, 129 and 137. The inert primes below $100$ are $3,11,37,41,47,53,61,71,79,83,89$.

*Proof.* (a) $(6+\sqrt{35})(6-\sqrt{35})=1$. (b)–(d) are direct evaluation. In (d), the Kronecker symbol at odd moduli equals the Jacobi symbol. $\square$

The narrow class number is $h^+=4$, with $\mathrm{Cl}^+(K)\cong C_2\times C_2$. Representatives of the four classes are $(1)$, $\mathfrak p_2=(2,1+\sqrt{35})$, $\mathfrak p_{19}$ and $\mathfrak p_5=(5,\sqrt{35})$.

**Cited Result 5.2 [LMFDB].** The cuspidal Hilbert newspace of level $(1)$ and parallel weight $[2,2]$ over $K$, summed over all four narrow components, has dimension $14$. It decomposes into four newforms:

| Newform | Dimension | CM | Base change |
|---|---|---|---|
| a | 2 | CM | yes |
| b | 2 | CM | no |
| c | 2 | CM | yes |
| d | 8 | non-CM | yes |

We denote this space by $V_{35}$. The subscript names the field, not the dimension. The F1–F3 results below are combinatorial and scale-free, so no normalisation enters them ($\Lambda_0=\emptyset$). If a Hecke deformation requires a scale, the canonical invariant of $K$ is $\operatorname{Res}\zeta_K=L(1,\chi_{140})$.

## 5.3 Cancellation lemmas (F1–F3)

The following are established results, restated with their exact hypotheses [R3].

- **F1.** The RPP cancellation problem is weakly NP-complete when the modulus $M$ is part of the input. The result holds on the slice $M=2^k+1>\Sigma$, with $C=\{0,1\}$ and unit coefficients, and admits an $O(nM)$ dynamic programme. It fails for fixed odd $M\le\Sigma$: take $M=3$, $w=\{1,2\}$ and target $0$.
- **F2.** A nonzero determinant does not prevent signed cancellation.
- **F3.** $|W|\le N\le\prod_i\|h_i\|_1=\operatorname{spr}\rho(|T|)$.

**Proposition 5.3 (F2 witness).** In $\mathbb{Z}[\mathbb{Z}/3]$ let $h_1=[0]+[1]$ and $h_2=-[0]+[1]+3[2]$. Then $\det\rho(h_1)=2$ and $\det\rho(h_2)=36$. Yet the signed count of paths to residue $1$ is $W=0$, while the number of such paths is $N=2$.

*Proof.* Write $\omega=e^{2\pi i/3}$, so that $\det\rho(h)=\prod_k\hat h(\omega^k)$.

- For $h_1$: $\hat h_1(1)=2$ and $|1+\omega|^2=1$, so $\det\rho(h_1)=2$.
- For $h_2$: $\hat h_2(1)=3$, and $-1+\omega+3\omega^2=-3-\sqrt3\,i$, which has modulus squared $12$. So $\det\rho(h_2)=3\cdot 12=36$.

There are two paths to residue $1$: $(0,1)$, with weight $+1$, and $(1,0)$, with weight $-1$. They cancel. $\square$

## 5.4 What the bridge requires

The bridge $A1\to\Xi\to\mathrm{RTA}$ would assert that the leading profile of $C$ lies outside $V_{35}$. This is **not established from the definitions presently available**. Four ingredients are missing:

- (i) a definition of $C$, or of its leading component, as an object in a category containing $V_{35}$;
- (ii) the explicit polar (Mellin–Barnes residue) system and its positivity bounds;
- (iii) a stated relation between $V_{35}$ and the $42$-dimensional monomial space $V_{42}$ used in the written premises;
- (iv) the lemma that the residual cocycle space has dimension one.

Given (i)–(iv), the statement $C\notin V_{35}$ would become a finite linear-algebra check against the four newforms of Cited Result 5.2.

The *residual law* for $C$ is likewise not established. This is the modular completion whose period matches the Fricke samples at $1/7$, $3/7$, $5/7$ and $1$ under a weight-$1/2$ slash factor. The quantum modularity of $g_s$ and of $C$ is open as well.

The operator $\Pi_{\mathrm{fast}}$ is not established either: a domain and a single definition are missing. What is known is a general lemma: an idempotent has spectrum in $\{0,1\}$, and $\mathrm{Id}$ minus a time-average is idempotent. On the other hand, $P_0\circ\mathrm{Ad}_g$ is not idempotent in general. For example, on $M_2(\mathbb{C})$ with $g=\mathrm{diag}(1,-1)$, the eigenvalues are $\{1,0,-1,-1\}$.

Three analytic facts constrain any estimate on this path.

- Holomorphic Hilbert newforms of parallel weight $2$ satisfy the Ramanujan–Petersson bound ($\theta=0$) [Bl]. The exponent $7/64$ of Kim–Sarnak, which concerns Maass forms, plays no role here.
- The Burgess exponent is $3/16$ [Bu].
- The elliptic curve $Y^2=X^3-35X$ has conductor $78400=2^6\cdot5^2\cdot7^2$. It is a different object from $V_{35}$.

The inclusion $\mathrm{BQP}\subseteq C_{\mathrm{HQH}}\subseteq\mathrm{NP}$ is not established. The stronger form, with "NP-complete" in place of $\mathrm{NP}$, is false, since $\emptyset\in\mathrm{BQP}$ is not NP-complete. Relativised separations are known [RT].

# 6. The non-local path

## 6.1 The Einstein–Hampton equation

The eleven-dimensional equation is
$$G_{MN}=8\pi G_{11}\,T^{(EH)}_{MN},\qquad T^{(EH)}=T(G_4)+T(M2)+T(m)+T(-)+T(\mathrm{PBH}),$$
with no $\Lambda_{11}$. It is posed on the warped metric
$$ds^2=e^{-2A(y)}\eta_{\mu\nu}dx^\mu dx^\nu+dy^2+e^{2B}\hat g_{ab}dz^adz^b ,$$
where $B$ is constant and $\hat R_{ab}=\kappa_{\mathrm{int}}\hat g_{ab}$ [EH]. For this ansatz the curvature layers L1–L7 give the block equations
$$6k^2-3K=-\Phi/96,\qquad 4k^2+K=\Phi/144 .$$

**Proposition 6.1.** These two equations hold simultaneously if and only if $k^2=\Phi/1728$ and $K=8k^2=\Phi/216$.

*Proof.* The system is linear in $(k^2,K)$ with determinant $6\cdot1-(-3)\cdot4=18\neq0$, so its solution is unique. Multiplying the second equation by $3$ and adding the first gives $18k^2=-\Phi/96+\Phi/48=\Phi/96$, so $k^2=\Phi/1728$. Then $K=\Phi/144-4k^2=(12-4)\Phi/1728=\Phi/216=8k^2$. $\square$

With $N=4880$ the flux match requires $N=4870.45$, a deficit of $9.55$ units. The following are **not established from the definitions presently available**:

- the independence of the layers;
- the field content and action beyond the metric (in particular $C_3$ and $G_4$);
- whether the halo geometry is a solution of the equations or a fitted profile;
- the reduction formula to a four-dimensional observable;
- the origin of a four-dimensional cosmological constant.

The next decisive computation is the comparison of the four-form weights $T_{\mu\nu}/g=-G^2/96$ and $T_{ab}/g=-G^2/288$.

## 6.2 Reverse-parity PT and non-local quantum mechanics

The reverse-parity table is specified by the test sheet RR-NL-SHEET-01. A pass criterion requires a written join between the table and an observable, and no such join is yet available. The following are not established from the definitions presently available:

- the action of P and T on $M_4$ versus $X_7$;
- whether the PT Hamiltonian is of Bender type, and if so its metric operator;
- the meaning of non-locality (a kernel, bulk entanglement, or a guidance field);
- a no-signalling theorem for the reduced four-dimensional theory;
- a Bell/CHSH discriminator from standard quantum mechanics.

No map from $V_{35}$ to any eleven-dimensional object is defined. In particular, $\operatorname{Res}\zeta_K$ is an arithmetic scale and not a gravitational cutoff, and the primes $2$, $5$ and $7$ of the conductor $78400$ are local arithmetic.

# 7. Consistency audit of the corpus

A keyword inventory over $24{,}009$ text files of the project corpus checked eighteen classes of potential inconsistency with the definitions used here:

1. superseded normalisations $\Lambda_0$ (32 files);
2. earlier definitions of $V_{35}$ (5);
3. class number without a narrow/wide marker (60);
4. the Burgess value $0.2000$ in place of $3/16$ (17);
5. the conductor $560$ in place of $78400$ (11);
6. a Petersson decomposition across inequivalent spaces (6);
7. incomplete inert-prime lists (9);
8. physical readings of newform dimensions (4);
9. F1–F3 cited to unpublished drafts (39);
10. Cesàro averaging without a domain (12);
11. $\operatorname{Res}\zeta_K$ used as an unconditional constant (26);
12. Kerr status markers (4556, mostly noise);
13. assumed presence of Layer 2 (139, including neutral mentions);
14. missing hash sidecars (19);
15. conflicting copies of the same file (none);
16. over-broad complexity wording (1);
17. locked-on-open dependencies (1507, pattern too broad);
18. $V_{35}$ tied directly to predictions (4).

The inventory is heuristic. It finds candidate files and does not adjudicate them. Every fingerprinted file checked matched its recorded hash.

Three inequivalences recur throughout the corpus:

- residue classes versus primes;
- newform dimensions versus narrow class components;
- the elliptic curve $Y^2=X^3-35X$ versus the Hilbert space $V_{35}$.

Each of these is fixed by the definitions of §5.2.

# 8. Toward a residual foundation of RTA: open steps, ranked

1. A definition of $C$ comparable with $V_{35}$, and the relation $V_{35}\leftrightarrow V_{42}$ (§5.4 (i)–(iii)).
2. A written link from the residual objects ($T_3$, $O_{\mathrm{res}}$, $B'$, the packaging identities) to the modular framework. By Theorem 3.4, this link cannot pass through identifying the count with the schedule.
3. The residual law for $C$, and the quantum modularity of $g_s$ and $C$.
4. The lemma that the residual cocycle space has dimension one.
5. A single definition, with a domain, of a nonzero projector $\Pi_{\mathrm{fast}}$.
6. Density and necessity statements for $A_5$ fibres. These require structure outside the residual core (Theorem 8.1).
7. Three-adic equidistribution for $T^\sharp$. Neither the free basins nor the residual counts supply it.
8. Complexity-theoretic containments (§5.4).
9. The construction of Layer 2 from Definition 4.1.

**Theorem 8.1 (the residual core does not force $A_5$).** Let $P(x)=x^5-4880x^3+32879x-243$.

- (a) $P$ is irreducible over $\mathbb{Q}$, and
$$\begin{aligned}\operatorname{disc}P&=318948969013863311130132536069\\&=47\cdot1901\cdot788309\cdot4528399596133175803 .\end{aligned}$$
Since this is not a square, $\operatorname{Gal}(P/\mathbb{Q})\not\subseteq A_5$.
- (b) The objects of §2 carry no Galois action on the roots of $P$. Consequently no evenness condition on $\operatorname{Gal}(P/\mathbb{Q})$ follows from them.

*Proof.* (a) Irreducibility and the factorisation are exact computations. All exponents in the factorisation are odd, so the discriminant is not a square. For an irreducible separable quintic, $\operatorname{Gal}\subseteq A_5$ if and only if the discriminant is a square. (b) The objects of §2 are vector spaces built from sector indices and tower labels, and none of them refers to $P$. $\square$

The full equality $\operatorname{Gal}(P/\mathbb{Q})=S_5$ is recorded in [R4]. It is not needed for Theorem 8.1.

# References

- **[R1]** A. B. Hampton, *Residual Ternary Algebra and a modular foundation*, Zenodo, doi:10.5281/zenodo.23644022, v12 (2026).
- **[R2]** A. B. Hampton, *5th Order Unification and Residual Ternary Algebra* (main text and supplement), Zenodo record 22143607.
- **[R3]** 539 Labs technical notes: *Group-ring Lemma 5* and *NP-hardness of RPP cancellation*; *Local F1–F3 interface* (2026).
- **[R4]** 539 Labs technical notes, *S²-11DM²ET-X Axiomatic Book*:
  - Residual Product Complex;
  - Residual Product Cohomology;
  - Thin Complex Formality;
  - Residual Form Spectral Sequences;
  - Residual vs Resonant;
  - Free vs Packaging;
  - O1–O6;
  - M1–M7;
  - U1-DNE D1–D9 (2026).
- **[EH]** 539 Labs, *The Einstein–Hampton Equation*, technical appendix (28 September 2026).
- **[LMFDB]** The LMFDB Collaboration, *The L-functions and Modular Forms Database*, Hilbert modular forms over 2.2.140.1, level 1, weight [2,2].
- **[Bl]** D. Blasius, Hilbert modular forms and the Ramanujan conjecture, in *Noncommutative Geometry and Number Theory*, Vieweg (2006).
- **[KS]** H. Kim and P. Sarnak, Refined estimates towards the Ramanujan and Selberg conjectures, *J. Amer. Math. Soc.* 16 (2003).
- **[BB]** V. Blomer and F. Brumley, On the Ramanujan conjecture over number fields, *Ann. of Math.* 174 (2011).
- **[Bu]** D. A. Burgess, On character sums and L-series II, *Proc. London Math. Soc.* 13 (1963).
- **[RT]** R. Raz and A. Tal, Oracle separation of BQP and PH, *STOC* (2019).
- **[Z]** S. Zwegers, *Mock Theta Functions*, PhD thesis, Utrecht (2002).

---

*Status: Tip Untouched. No CERT.*
