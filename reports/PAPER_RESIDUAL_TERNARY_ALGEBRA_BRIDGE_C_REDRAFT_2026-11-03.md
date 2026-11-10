---
title: "Residual Ternary Algebra and Bridge Series C: The Residual-vs-Resonant Frame for S²-11DM²ET-X (Redraft, 2026-11-03)"
author: "Arvin B. Hampton (539 Labs) — Project Quantum Comp"
date: "Tuesday 3 November 2026 (America/Chicago, CST)"
---

**Status line.** Tip `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` untouched (hash re-verified on disk when this draft was compiled). No CERT. Kerr UNLOCKED on the Owner record. Layer2 ABSENT on disk. Cat A READY = Local F1–F3 cite-lifts only.

**Provenance rule for this paper.** Every result below comes from a file on disk, cited by path and the first 16 hex digits of its sha256. Arithmetic identities were recomputed while this draft was written (exact integer arithmetic in Python/SymPy). Nothing here is a new result. Where the record has only a proof sketch, the proof is written out in full from the stated generators and relations, with no extra assumptions. Where the record has no proof, the item is labelled **Conjecture** or **Open problem**.

**Two corrections to the commissioning brief (the record governs).**

1. `generated/Layer2.md` **does not exist on disk.** The Soft SF REFUSE `OW_Layer2_md_status_SoftSF_REFUSE_2026-11-03.md` (sha `559111934cc1a274…`) records `find /workspace -name 'Layer2.md'` → empty, and shows that neither `/workspace/quantum-comp/generated/` nor `/workspace/generated/` exists. The Layer2 *component* remains **ABSENT**. The Owner has locked only the **definition** of $D_1$ (§4).
2. The mixed class is $\xi_{\mathrm{mix}} = [s_{\alpha\delta}] \in H^2(F)\cong\mathbb{Q}$. It lives in **degree 2** of the residual thin form complex $F$, with **rational** coefficients. It is **not** a class in $H^1(X_\times;\mathbb{Z})$. (Source: Owner Write `OWNER_WRITE_LOCK_D1_Seff_Layer2_T3_2026-11-03.md`, sha `96f8d42e80c1975b…`, Flag 1 CLOSED; `Residual_Product_Cohomology.md`.)

# Abstract

We assemble the record's results on the Residual (ternary) Discrete Algebra of the S²-11DM²ET-X model under the RESIDUAL_VS_RESONANT author lock of 2026-08-16. Residual Discrete Algebra is the combinatorics of the pieces left over when $N_{\mathrm{flux}}=4880$ flux units are packaged under Principle (S) with seed $f_{\max}=21$. Its central integer is $B'=\lfloor(4880-21)/9\rfloor=539$, the **count** of leftover pieces in each of nine charge sectors. Resonant Algebra is a separate design decision: a window $18=\lfloor e^3/\ln 3\rfloor$ plus a body of $521$ gives a hard schedule of 539 forced firings. The free Canonical $T_3$ map has neither 539-step nor 55-step closure: the free orbit of 4880 reaches 1 in 14 steps, and the average contraction factor is $2/3$ (Lyapunov exponent $\ln(2/3)<0$).

We prove the following in full: the packaging arithmetic; the graph Betti number $\beta_1(G_\times)=36B'-8=19396$; mixed closure $D\eta=0$; the form-cohomology theorem $H^0(F)\cong\mathbb{Q}$, $H^1(F)=0$, $H^2(F)\cong\mathbb{Q}\cdot[s_{\alpha\delta}]$; formality $F\simeq\mathbb{Q}[0]\oplus\mathbb{Q}[-2]$; uniqueness of the essential class; rank 1 of the Owner-locked classifier $D_1$; a formal Residual/Resonant non-identification theorem; and the non-forcing of $A_5$ by the residual core (O1). The $V_{35}$ lock (dimension $14=2+2+2+8$ over $\mathbb{Q}(\sqrt{35})$, $h^+=4$, $\mathrm{Cl}^+\cong C_2\times C_2$) enters as a **cited** LMFDB result.

The bridge $A1\to\Xi\to\mathrm{RTA}$, the residual law for Bridge Series C, the EH 11D curvature programme, reverse-parity PT, non-local QM, $T^\sharp$ 3-adic equidistribution, O1 density/Necessity, and the BQP chain are all stated as conjectures or open problems. For each we record what is known, what is missing, and what would close it, together with the pitfalls the Soft SF refusals have already identified.

# 1. Introduction and governing frame

## 1.1 The author lock

Source: `RESIDUAL_VS_RESONANT_2026-08-16.md` (sha `342862a6dc643916…`).

> *Residual Discrete Algebra is what the leftover pieces are. … Resonant Algebra is how long you choose to stir. … They touch without merging. Residual cohomology does not force the schedule. 539 vertices do not make a hash. A count is not a clock.*

The record uses three distinct numbers:

| Number | Meaning | Lane | Source |
|---|---|---|---|
| $539=B'$ | count of leftover pieces in each of the 9 sector cores | Residual | `Residual_Product_Cohomology.md` |
| $539=18+521$ | hard schedule: fire the local ternary step exactly 539 times | Resonant | `RESIDUAL_VS_RESONANT_2026-08-16.md` |
| $\approx 14$ | typical free-basin depth; the free orbit of 4880 has length 14 | Free $T_3$ | `FREE_VS_PACKAGING_LOCK_2026-08-16.md` |

## 1.2 Categories

- **Category A.** Residual discrete algebra through A5⁺, packaging under Principle (S), Option 3 free basins, and the No-Go results. All of these are locked and untouched.
- **Category B.** Continuum claims, resonant-attractor claims, G4-clock claims, and biological claims. Per `O6_Remaining_CatB_After_O1_O5_2026-08-16.md` (sha `508eeb61a0f913bd…`), all of these stay Category B.
- **Cat A READY**, as of 2026-11-03, consists **only** of the Local F1–F3 cite-lifts (Owner Writes `c290a274…`, `96f8d42e…`; Auditor summary `759bf06b107d3b4b…`).

Residual-flux provenance (Principle (S), *not* free $T^\sharp$) is mandatory for every residual statement.

## 1.3 Conventions

$K_9$ is the complete complex on the nine charge sectors $\{0,\dots,8\}$. $P_{B'}$ is the residual path with vertices $0,\dots,B'-1$. Cochains have coefficients in $\mathbb{Q}$ unless stated otherwise.

# 2. Residual ternary algebra

## 2.1 Packaging arithmetic

Sources: `MISS_LIST_M1_to_M7_2026-08-16.md` (sha `d539e34294192f6f…`); `DEFINITION_RTA_RESIDUALS_TO_FIFTH_ORDER_ORTHANT_CONES_LIMA_CHAIN_2026-10-26.md` (sha `bd7520f98716062c…`), steps R0–R3; `Residual_Product_Cohomology.md` §4.

**Definition 2.1.** $N_{\mathrm{flux}}=4880$ and $f_{\max}=21$ (the seed). The residual pool is $R=N_{\mathrm{flux}}-f_{\max}$. The packaging residual cardinality is $B'=\lfloor R/9\rfloor$.

The record's root axiom (9-Maths Axiom 0.1, cited in the Lima-chain definition file) writes $N_{\mathrm{flux}}=\lfloor e^3\cdot 3^5\rfloor=4880$. This paper takes 4880 as given input.

**Proposition 2.2 (packaging identities).**

- (a) $R=4859=9\cdot 539+8$, so $B'=539$ and the remainder is $8$.
- (b) $4880-9\cdot 539=29$ (MISS_LIST M1, the "excess").
- (c) $539=7^2\cdot 11$, and $B'\equiv 3\pmod 8$.
- (d) $B'-1=538\equiv 2\pmod 8$.

*Proof.* (a) $9\cdot539=4851$ and $4859-4851=8$, with $0\le 8<9$. (b) $4880-4851=29$. (c) $49\cdot 11=539$, and $539=8\cdot 67+3$. (d) $538=8\cdot 67+2$. $\square$

**Remark 2.3 (nine sectors; linking $\pm539$).** The nine charge sectors each have core size $B'=539$, a **count**. The linking numbers $L_{ab}=\pm 539$ are recorded as integers/counts (`U1_DNE_Discrete_NonEuclidean_D1_to_D9_2026-08-18.md`, sha `47bb1deb2c2b0c42…`, "ALREADY CLOSED"). The record does not contain a derivation of the linking values beyond that lock statement, so this paper cites them and does not re-prove them. The record also cites, but this paper does not re-derive, the fibre blocks $68/67$ and the $K^+$ data ($V=539$, $E=594$, $F=56$, $H_*(K^+;\mathbb{Z})\cong H_*(\mathrm{pt})$) (`P4_Product_Complex_Only_One_Essential_Class_2026-08-16.md`, sha `16ab8489ffb788f0…`).

## 2.2 The product complex $X_\times$

Source: `Residual_Product_Complex.md` (sha `f155466edf9858cf…`).

$X_\times := K_9\times P_{B'}$. Its cells are:

- 0-cells: $(a,i)$.
- Horizontal 1-cells: $H(a,b;i)$.
- Vertical 1-cells: $V(a;i)$.
- Triangles: $T(a,b,c;i)$.
- Squares: $S(a,b;i)$.
- 3-cells: prisms $T(a,b,c;i)\times e_i$.

The product differential on $C^\bullet(K_9)\otimes C^\bullet(P_{B'})$ is
$$D(\varphi\otimes\psi)=d_Q\varphi\otimes\psi+(-1)^{\deg\varphi}\varphi\otimes d_P\psi .$$
$D^2=0$ follows from $d_Q^2=d_P^2=0$ (graded Leibniz rule).

The locked cochains are:

- $\alpha(a,b)=\mathrm{sgn}(a-b)$
- $\omega_2=d_Q\alpha$
- $\mu=B'\,\alpha\smile\alpha$
- $f(i)=\tau(x_i)$ (tower labels on core 0)
- $\delta f=d_Pf$

**Lemma 2.4 (cyclic identity).** For distinct $a,b,c$: $\omega_2(a,b,c)=\alpha(a,b)+\alpha(b,c)+\alpha(c,a)$. For $a<b<c$ this gives $\omega_2=-1$, and $\mu(a,b,c)=B'\,\mathrm{sgn}(a-b)\mathrm{sgn}(b-c)=B'$.

*Proof.* The coboundary of a 1-cochain on the 2-simplex $(a,b,c)$ is $\alpha(b,c)-\alpha(a,c)+\alpha(a,b)$. Skew-symmetry gives $-\alpha(a,c)=\alpha(c,a)$, which yields the first identity. For $a<b<c$: $\alpha(a,b)=-1$, $\alpha(b,c)=-1$, $\alpha(c,a)=+1$, so the sum is $-1$. Also $\mathrm{sgn}(a-b)\mathrm{sgn}(b-c)=(-1)(-1)=1$. $\square$

**Theorem 2.5 (mixed closure; record: `Residual_Product_Complex.md` §4.2).** Let $\eta:=\alpha\otimes\delta f-\omega_2\otimes f$. Then $D\eta=0$.

*Proof.* Use $d_P(\delta f)=0$ (there are no path 2-cells) and $d_Q\omega_2=d_Q^2\alpha=0$:
$$D(\alpha\otimes\delta f)=\omega_2\otimes\delta f-\alpha\otimes d_P\delta f=\omega_2\otimes\delta f,$$
$$D(\omega_2\otimes f)=0\otimes f+(+1)\,\omega_2\otimes\delta f=\omega_2\otimes\delta f .$$
Subtracting gives $D\eta=0$. Geometric check on the prism $(a,b,c)\times e_i$: the boundary sum is $\omega_2(a,b,c)\,(f(i)-f(i+1))+(\alpha(a,b)+\alpha(b,c)+\alpha(c,a))\,\delta f(i)$. Since $f(i+1)-f(i)=\delta f(i)$, Lemma 2.4 makes this zero. $\square$

**Proposition 2.6 (P1, P2, P4).**

- P1: $\sum_{a<b<c}\mu(a,b,c)=84B'=45276$.
- P2: $\sum_{a\ne b}\sum_i\alpha(a,b)\,\delta f(i)=0$.
- P4: each path edge carries $9\cdot 8=72$ oriented square types.

*Proof.* P1: there are $\binom93=84$ ordered triples, each with $\mu=B'$ (Lemma 2.4), and $84\cdot539=45276$. P2: skew-symmetry gives $\sum_{a\ne b}\alpha(a,b)=0$, and this factor multiplies the whole sum. P4: there are $9\cdot 8$ ordered pairs $a\ne b$. $\square$

## 2.3 Graph layer and the cycle space ($\sim$20k)

Source: `Residual_Product_Cohomology.md` (sha `900ffa219417d0b6…`), Layer (G).

**Theorem 2.7 (graph cycle rank).** Let $G_\times=K_9^{(\mathrm{gr})}\,\square\,P_{B'}$ be the Cartesian product of the undirected 1-skeleta. Then:

- $V=9B'$
- $E=36B'+9(B'-1)$
- $\beta_0=1$
- $\beta_1=36B'-8$

At $B'=539$: $V=4851$, $E=24246$, $\beta_1=19396$.

*Proof.* Vertices are the pairs $(a,i)$, so $V=9B'$. Edges come in two kinds. Each of the $B'$ copies of $K_9$ contributes $\binom92=36$ edges. Each of the 9 copies of the path contributes $B'-1$ edges. The graph is connected: any $(a,i)$ reaches $(0,i)$ by a $K_9$ edge and then $(0,0)$ along the path. So $\beta_0=1$. For a connected graph, $\beta_1=E-V+1=36B'+9B'-9-9B'+1=36B'-8$. Substituting $B'=539$ gives $19404-8=19396$. $\square$

**Remark 2.8 (record discrepancy).** `MISS_LIST` M2 (2026-08-16) says that no exact closed form for the free cycle-space rank beyond linearity is forced by the locked stack. `Residual_Product_Cohomology.md` (dated 2026-07-29) gives $\beta_1(G_\times)=36B'-8$ for the graph layer, and Theorem 2.7 proves it. The two statements can be reconciled only if M2 refers to a different "free cycle space", for example the chain-rank count of `P4…` ("rank of the chain groups"). The record does not say which. This paper proves only the graph-layer formula. The phrase "cycle space $\sim$20k" in the Owner specs (`ATTACH…a71f388e`, §1) agrees with $19396$.

## 2.4 The residual thin form complex $F$

Source: `Residual_Product_Cohomology.md` §2.1–2.4.

**Definition 2.9 (presentation, as written in §2.1–2.2 of the source).** $F^\bullet$ is the $\mathbb{Q}$-cochain complex with these generators:

- $F^0=\langle \mathbf 1,\ f\rangle$
- $F^1=\langle h_\alpha,\ v_\delta,\ h_{\alpha f}\rangle$, where $h_\alpha=\alpha\otimes1$, $v_\delta=1\otimes\delta f$, $h_{\alpha f}=\alpha\otimes f$
- $F^2=\langle t_\mu,\ t_\omega,\ s_{\alpha\delta},\ t_{\omega f}\rangle\,/\,(t_\mu+B't_\omega)$, where $t_\omega=\omega_2\otimes 1$, $t_\mu=\mu\otimes 1$, $s_{\alpha\delta}=\alpha\otimes\delta f$, $t_{\omega f}=\omega_2\otimes f$
- $F^{n}=0$ for $n\ge3$

The generators listed in each degree are linearly independent, apart from the one stated relation. The relation $t_\mu=-B't_\omega$ is Lemma 2.4 read on ordered triples. The differential $D$ is
$$D\mathbf 1=0,\quad Df=v_\delta,\quad Dh_\alpha=t_\omega,\quad Dv_\delta=0,\quad Dh_{\alpha f}=t_{\omega f}-s_{\alpha\delta},\quad D|_{F^2}=0 .$$

These values follow from the product rule: $D(\alpha\otimes f)=\omega_2\otimes f+(-1)^1\alpha\otimes\delta f$. The condition $D|_{F^2}=0$ is the thin-model truncation $F^3=0$ that the record adopts. In the full cochain complex, $D(\alpha\otimes\delta f)=\omega_2\otimes\delta f\neq0$, so the theorem below is a statement about the thin model $F$ and not about $C^\bullet(X_\times)$. $D^2=0$ holds trivially, because $D(Df)=Dv_\delta=0$ and $D$ vanishes on $F^2$.

**Remark 2.10 (presentation caveat).** The generator table in `Thin_Complex_Formality.md` (sha `325002c4cc5f08c4…`, §1.1) lists only $\mathbf 1$ in degree 0. Under that presentation, $1\otimes\delta f$ would be a non-exact cocycle and $H^1$ would be nonzero. The theorem below uses the presentation of `Residual_Product_Cohomology.md` §2.1, which puts $f$ in $F^0$. That is the presentation the record's proof sketch ("$H^1$: $\ker D=\mathrm{span}\{v_\delta\}=\mathrm{im}(D:F^0\to F^1)$") uses.

**Theorem 2.11 (form cohomology).** Over $\mathbb{Q}$:

- $H^0(F)=\mathbb{Q}\cdot[\mathbf 1]$
- $H^1(F)=0$
- $H^2(F)=\mathbb{Q}\cdot[s_{\alpha\delta}]$, and $\dim_{\mathbb{Q}}H^2(F)=1$
- $H^n(F)=0$ for $n\ge 3$

Moreover $[\eta]=0$, $[\tilde\mu]=[t_\mu]=0$, $[t_\omega]=0$, and $[t_{\omega f}]=[s_{\alpha\delta}]$.

*Proof (explicit linear algebra).* $F^2$ has basis $\{t_\omega,s_{\alpha\delta},t_{\omega f}\}$ (we eliminate $t_\mu=-B't_\omega$), so $\dim F^2=3$. Also $\dim F^0=2$ and $\dim F^1=3$. In these bases:

$D^0:F^0\to F^1$ sends $\mathbf 1\mapsto 0$ and $f\mapsto v_\delta$. Its matrix with respect to $(\mathbf 1,f)$ and $(h_\alpha,v_\delta,h_{\alpha f})$ is
$$D^0=\begin{pmatrix}0&0\\0&1\\0&0\end{pmatrix},\qquad \operatorname{rank}D^0=1 .$$

$D^1:F^1\to F^2$, with respect to $(h_\alpha,v_\delta,h_{\alpha f})$ and $(t_\omega,s_{\alpha\delta},t_{\omega f})$, is
$$D^1=\begin{pmatrix}1&0&0\\0&0&-1\\0&0&1\end{pmatrix},\qquad \operatorname{rank}D^1=2 .$$
The two nonzero columns $(1,0,0)^T$ and $(0,-1,1)^T$ are independent.

$D^2=0$.

*Degree 0.* $\ker D^0=\mathrm{span}\{\mathbf 1\}$, so $H^0=\mathbb{Q}[\mathbf 1]$.

*Degree 1.* $\dim\ker D^1=3-2=1$, and $\ker D^1=\mathrm{span}\{v_\delta\}$ (the middle column is zero). $\operatorname{im}D^0=\mathrm{span}\{v_\delta\}$. Hence $H^1=0$.

*Degree 2.* $\ker D^2=F^2$ has dimension 3. $\operatorname{im}D^1=\mathrm{span}\{t_\omega,\ t_{\omega f}-s_{\alpha\delta}\}$ has dimension 2. Hence $\dim H^2=1$.

*Nontriviality of $[s_{\alpha\delta}]$.* Suppose $s_{\alpha\delta}=x\,t_\omega+y\,(t_{\omega f}-s_{\alpha\delta})$. Comparing coefficients in the basis gives: $t_\omega$: $x=0$; $t_{\omega f}$: $y=0$; $s_{\alpha\delta}$: $1=-y=0$. This is a contradiction, so $[s_{\alpha\delta}]\ne0$ and it spans $H^2$.

*Relations among classes.*

- $\eta=s_{\alpha\delta}-t_{\omega f}=-D h_{\alpha f}$, so $[\eta]=0$.
- $t_\omega=Dh_\alpha$, so $[t_\omega]=0$.
- $t_\mu=-B't_\omega=D(-B'h_\alpha)$, so $[t_\mu]=0$.
- $t_{\omega f}-s_{\alpha\delta}\in\operatorname{im}D^1$, so $[t_{\omega f}]=[s_{\alpha\delta}]$.

$F^{\ge3}=0$ gives the last claim. $\square$

**Corollary 2.12 (uniqueness of the essential class; record: `P4_Product_Complex_Only_One_Essential_Class_2026-08-16.md`, MISS_LIST M3).** Every closed degree-2 element $z\in F^2$ can be written as $z=\lambda\,s_{\alpha\delta}+Dw$ for a unique $\lambda\in\mathbb{Q}$ and some $w\in F^1$. In particular, every named 2-cocycle in $F$ ($\eta$, $\tilde\mu$, $t_\omega$, $t_{\omega f}$) is either a boundary or cohomologous to a rational multiple of $[s_{\alpha\delta}]$.

*Proof.* This is immediate from $\dim H^2(F)=1$ with generator $[s_{\alpha\delta}]$. The scalar $\lambda$ is unique because $[s_{\alpha\delta}]\ne0$. From Theorem 2.11, the multiples are $\lambda=0,0,0,1$ for $\eta,\tilde\mu,t_\omega,t_{\omega f}$ respectively. $\square$

**Scope note.** Corollary 2.12 is uniqueness *inside the thin model $F$*. The record's companion statement that $H_*(K^+;\mathbb{Z})\cong H_*(\mathrm{pt})$ is cited from `P4…` and is not re-proved here.

## 2.5 Formality

Source: `Thin_Complex_Formality.md`.

**Theorem 2.13 (thin formality).** $F\simeq \mathbb{Q}[0]\oplus\mathbb{Q}[-2]$ in $D(\mathbb{Q})$. A quasi-isomorphism is given explicitly by $\iota:H\to F$ with $H=\mathbb{Q}e_0\oplus\mathbb{Q}e_2$, $d_H=0$, $\iota(e_0)=\mathbf 1$, and $\iota(e_2)=s_{\alpha\delta}$.

*Proof.* $\iota$ is a chain map, because $D\mathbf 1=0$ and $Ds_{\alpha\delta}=0$ in $F$, which matches $d_H=0$. On cohomology, $H(\iota)$ sends $e_0\mapsto[\mathbf 1]$ and $e_2\mapsto[s_{\alpha\delta}]$. By Theorem 2.11 these are bases of $H^0(F)$ and $H^2(F)$, and $H^1(F)=H^{\ge3}(F)=0=H^{1}(H)=H^{\ge3}(H)$. So $H(\iota)$ is an isomorphism in every degree, and $\iota$ is a quasi-isomorphism.

An explicit splitting (Lemma A of the source) is:

- $F^0=\langle\mathbf 1\rangle\oplus\langle f\rangle$, with $D:\langle f\rangle\xrightarrow{\sim}\langle v_\delta\rangle$;
- $F^1=\langle v_\delta\rangle\oplus\langle h_\alpha,h_{\alpha f}\rangle$, with $D:\langle h_\alpha,h_{\alpha f}\rangle\xrightarrow{\sim}\langle t_\omega,t_{\omega f}-s_{\alpha\delta}\rangle$;
- $F^2=\langle s_{\alpha\delta}\rangle\oplus\langle t_\omega,t_{\omega f}-s_{\alpha\delta}\rangle$.

The acyclic summand is a direct sum of two-term complexes $S\xrightarrow{\sim}B$, and its contraction gives $\iota\pi\simeq\mathrm{id}_F$. $\square$

**Corollary 2.14 (record: `Thin_Complex_Formality.md` Cor. 3).** All Massey products among classes of $H(F)$ vanish for degree reasons.

*Proof.* Only $H^0$ and $H^2$ are nonzero. A triple Massey product $\langle x,y,z\rangle$ of positive-degree classes would land in degree $\ge 2+2+2-1=5$, and $H^5=0$. Any product involving $[\mathbf 1]$ is defined with zero indeterminacy and vanishes. $\square$

## 2.6 Layer (S) — the filled product is acyclic

**Proposition 2.15.** $\tilde H^\bullet(|\Delta^8\times P_{B'}|;\mathbb{Z})=0$.

*Proof.* $|\Delta^8|$ is a simplex and therefore contractible. $|P_{B'}|$ is an interval. A product of contractible spaces is contractible. $\square$

The record's reading (`residual_to_geometric_2026-08-16.md`, sha `72737caec62044b9…`) is that the only geometric identity the residual core forces is this contractibility. Residual pattern content lives in layers (G) and (F).

# 3. Resonant algebra and the separation theorem

## 3.1 Canonical $T_3$ and free dynamics

Source: `FREE_VS_PACKAGING_LOCK_2026-08-16.md` (sha `489c786a545576ad…`).

$$T_3(n)=\begin{cases} n/3 & n\equiv0\\ \lfloor(4n+2)/3\rfloor & n\equiv1\\ \lfloor(2n+1)/3\rfloor & n\equiv2\end{cases}\pmod 3,\qquad T_3(0)=0 .$$

**Proposition 3.1 (free orbit facts, Category A empirical; recomputed for this draft).**

- (a) The free orbit of 4880 is $4880\to3253\to4338\to1446\to482\to321\to107\to71\to47\to31\to42\to14\to9\to3\to1$. It has exactly 14 steps.
- (b) $10^{18}$ reaches 1 in 92 steps, and the $\varphi$-seed $1616033987$ reaches 1 in 37 steps.
- (c) On $[1,50000]$ the maximum free orbit length is 55, attained exactly at $n=36043$ and $n=36592$.

*Proof.* Direct iteration in exact integer arithmetic. For (a), every step can be checked by hand: for example $4880\equiv2$ gives $\lfloor 9761/3\rfloor=3253$, and $3253\equiv1$ gives $\lfloor13014/3\rfloor=4338$. $\square$

**Remark 3.2 (contraction).** Each branch multiplies $n$ by about $1/3$, $4/3$ or $2/3$. Weighting the three residue classes equally gives a geometric-mean factor of $(1/3\cdot4/3\cdot2/3)^{1/3}=(8/27)^{1/3}=2/3$, a heuristic that reproduces the record's "average contraction factor $2/3$, Lyapunov $\ln(2/3)<0$". The record states this as a free-map fact. This paper does not give a measure-theoretic proof of the Lyapunov exponent, so the typical depth $\sim14$ is **empirical**. Per `U1_DNE…`, the only genuine periodic orbits recorded are the fixed point $0$ and the 2-cycle $\{1,2\}$: $T_3(1)=\lfloor 6/3\rfloor=2$ and $T_3(2)=\lfloor5/3\rfloor=1$.

## 3.2 Resonant Algebra

**Definition 3.3 (record).** The window is $W=\lfloor e^3/\ln3\rfloor$ and the body is $521$. The resonant schedule fires the local ternary step exactly $W+521$ times and stops. "The counter is the stop."

**Proposition 3.4.** $W=18$ and $W+521=539$.

*Proof.* $e^3/\ln 3=20.0855\ldots/1.0986\ldots=18.2826\ldots$, so the floor is 18. Then $18+521=539$. $\square$

## 3.3 Separation theorem

**Theorem 3.5 (Residual/Resonant non-identification).** Consider the three integer-valued constructions:

- (i) $\mathcal R(N,f,k)=\lfloor (N-f)/k\rfloor$ (Residual count);
- (ii) $\mathcal S(W,b)=W+b$ (Resonant schedule length);
- (iii) $\mathcal L(n)=\min\{t: T_3^t(n)\in\{0,1\}\}$ (free stopping time).

Then:

- (a) $\mathcal R(4880,21,9)=\mathcal S(18,521)=539$, but $\mathcal L(4880)=14\neq539$.
- (b) $\mathcal R$ depends only on $(N,f,k)$ and $\mathcal S$ only on $(W,b)$. Neither is a function of the other's inputs, so the equality in (a) is an equality of values, not an identity of constructions.
- (c) Every object of the residual thin model ($F$, $H^\bullet(F)$, $D_1$) is a finite-dimensional $\mathbb{Q}$-vector space or a linear map between such spaces, and carries no time or iteration parameter. A schedule, by contrast, is a function $\{1,\dots,539\}\to\{\text{firings}\}$. So no statement in Theorems 2.5–2.13 implies or uses a number of iterations.

In short, a count is not a clock.

*Proof.* (a) is Propositions 2.2(a), 3.4 and 3.1(a).

(b) Vary the inputs independently. For example, $\mathcal R(4880,21,9)=539$ while $\mathcal S(18,522)=540$. And $\mathcal S(18,521)=539$ while $\mathcal R(4889,21,9)=540$. So there is no function $g$ with $\mathcal S=g\circ\mathcal R$ on the common domain that is fixed by the record's data.

(c) is inspection of Definition 2.9 and §4.1: every object is defined by finitely many generators and linear relations over $\mathbb{Q}$, with no index set of time steps.

Finally, (a) shows that the free map does not produce the value 539 at $N_{\mathrm{flux}}$, so "539 = free stopping time of 4880" is **false**. $\square$

**Corollary 3.6 (record: `resonant_to_geometry_2026-08-16.md`, sha `fcd9d57d45bad166…`).** A finite hard schedule does not by itself determine a geometric space, cell complex, covering, or local system. Any geometry attached to the schedule, to the 540 ladder ($540=539+1$, trivial arithmetic), or to the Phase Law $2\cos(\cdot)$ is Category B.

*Proof sketch, as on record.* A schedule is a finite counter, and a finite counter carries no incidence data. The Phase Law angle is continuum-valued and is not derived from residual data. $\square$

**Retained No-Go (record).** The printed "55-lemma" is IMPOSSIBLE ($539/\varphi^7\approx18.564$; the printed closure $\approx1476$). The measured free maximum 55 (Prop. 3.1(c)) is not that lemma.

# 4. Layer2 and $T_3$ under Owner Write

Sources: `OWNER_WRITE_LOCK_D1_Seff_Layer2_T3_2026-11-03.md` (sha `96f8d42e80c1975b…`); locked text `ATTACH_Layer2_T3_specs_LOCKED_t3511u_a71f388e.txt` (sha `a71f388efa353125…`).

## 4.1 $D_1$ (definition locked; component ABSENT)

**Definition 4.1 (Owner-locked, §1 of the locked text).** $D_1$ is a static invariant classifier on the nine charge sectors of $X_\times$, over $\mathbb{Q}$, with $\Lambda_0=\emptyset$ (no time, schedule or metric). It isolates $[\xi_{\mathrm{mix}}]=[s_{\alpha\delta}]\in H^2(F)\cong\mathbb{Q}$. Its invariant subspace is rank 1 over $\mathbb{Q}$, spanned by $[s_{\alpha\delta}]$. It sits adjacent to, and does not alter, the ambient cycle space ($\sim$20k). "Boundary disjointness" requires that no algebraic data be shared with the Resonant counters.

**Proposition 4.2 (rank 1 of $D_1$ as a consequence).** Any $\mathbb{Q}$-linear classifier whose invariant subspace is "the span of the essential mixed class in $H^2(F)$" has rank exactly 1. That subspace is all of $H^2(F)$, and it has rank 1 regardless of $\beta_1(G_\times)=19396$.

*Proof.* By Theorem 2.11, $[s_{\alpha\delta}]\neq0$ and $\dim H^2(F)=1$. The span of a nonzero vector in a 1-dimensional space is the whole space and has dimension 1. The graph layer (G) is a different complex (Theorem 2.7), so its rank does not enter. $\square$

**Caveat (record).** The "boundary disjointness" clause, $\operatorname{Im}(\partial_1)\cap\text{Resonant}=\emptyset$, was flagged as ill-typed in `OW_A5plus_fibre_closure_D1_SoftSF_REFUSE_2026-11-03.md` (sha `d3a172ad29ac25aa…`, item 6): the Resonant side is a counter, not a chain group. The Owner lock stands as written. This paper reads the clause only as the non-identification of Theorem 3.5(c), which is the strongest reading that is formally meaningful.

**Layer2 status, stated plainly.** Only the **definition** of $D_1$ is Owner-locked. No Layer2 artifact exists on disk: `generated/Layer2.md` is absent (Soft SF REFUSE `559111934cc1a274…`), and the Auditor summary records "Layer2 does not exist on disk". Nothing in this paper depends on a Layer2 file.

## 4.2 $S_{\mathrm{eff}}$ ($T_3$ structural entry)

**Definition 4.3 (Owner-locked, §2 of the locked text).**

- $T_3=539$ is a **static cell capacity / hash budget**. It is not a convergence rate or a stopping time.
- There is **no global guarantee** that $\Omega\equiv0\pmod{539}$. Local remainders are uncanceled structural traits.
- The clause "handled entirely by the local dual-rail ternary representation" is **HARDWARE-ONLY** (HQH side-channel countermeasure), by Owner voice 8bff661b…. It is excluded from Category A treatment of $\Omega$ and from the algebraic criteria of $S_{\mathrm{eff}}$.
- $\mathcal M:S_{\mathrm{eff}}\to\mathrm{Residual}_{539}\times\mathrm{Resonant}_{539}$ has disjoint projections.
- The stability boundary is the free attractor depth ($\sim14$, $\ln(2/3)$). The 539-step mixer is an external constant-time override.

**Supporting record fact.** "$\Omega\equiv0\bmod 539$" as a cancellation criterion is FALSE (M=3 example with $\Omega=2$), per `PP-FINDINGS-CATA_FOOLPROOF_2026-11-03.md` (sha `4e70be9ad36c2914…`), item 8. That finding also records that $W$ (winding) is undefined there. The Owner lock's "no global guarantee" wording is consistent with it.

# 5. Local Path: Bridge C, $A1\to\Xi\to\mathrm{RTA}$

## 5.1 The residual chain to Bridge Series C (definitions, as on record)

Source: Lima-chain definition file (sha `bd7520f98716062c…`), R0–R9.

- **R5.** $g_s(q)=\sum_{n\ge0}q^{n^2}/(-q^s;q^s)_n$. At $s=1$ this has the shape of Ramanujan's fifth-order $f_0$.
- **R4.** The packaging integers select $s\in\{7,8,11\}$.
- **R6.** Orthant counts $P_s=(-q^s;q^s)_\infty g_s$, and the cone series $H_s$ on an indefinite lattice of signature $(1,1)$.
- **R7.** **Bridge Series C** := $P_{\mathrm{orth}}-H_s$. At $s=7$: $Q(n,k)=n^2+7nk+\tfrac72k(k+1)$ and $C_7=C_{\mathrm{axis}}+C_{\mathrm{third}}$, with coefficients in $\{0,1,1.5\}$ and support on residues $0,1,2,4\bmod 7$.
- **R8.** Ξ is the residual weight-3/2 shadow.
- **R9.** The residual law for $C$ is **OPEN**.

`T928U_RTA_THEOREM_COUNT_2026-10-25.md` (sha `a85e30bdd41ea75e…`) counts 64 distinct theorems in the published RTA sources (Zenodo 10.5281/zenodo.23644022 v12 and 22143607). Several are conditional (for example 11.5 on Baker; 19.3 on a cited congruence; 20.11 on (C3); 24.5 on the analyticity of harmonic-Maass cocycles). The same file records the line from 23644022 Part IV: "written RTA objects (T3, O_res, 539, the packaging identities) have no written link to it [the modular framework]". This paper does not restate those theorems. It cites them as published results with their stated conditions.

## 5.2 Locks in force

- **$\Lambda_0$ = NONE** for F1–F3 (`OW_PP_picks_Lambda0_V35_Owner_LOCK_2026-11-03.md`, sha `c290a274e7b31dc7…`). The values $\sqrt{10}$, $1.81$ and $0.7858$ are rejected. If a Hecke deformation ever needs a scale, the only canonical field invariant is $\mathrm{Res}_{s=1}\zeta_K=2hR/\sqrt{140}=L(1,\chi_{140})$.
- **$V_{35}$** = the full level-1 parallel-weight $[2,2]$ cuspidal newspace over 2.2.140.1 $=\mathbb{Q}(\sqrt{35})$, of dimension 14.

**Cited Result 5.1 ($V_{35}$; LMFDB, as discharged on record).** The level-1 parallel-weight $[2,2]$ Hilbert cuspidal newspace over $\mathbb{Q}(\sqrt{35})$ has four newforms:

| Newform | Dimension | CM | Base change |
|---|---|---|---|
| a | 2 | CM | BC |
| b | 2 | CM | not BC |
| c | 2 | CM | BC |
| d | 8 | non-CM | BC |

Total dimension: $2+2+2+8=14$. Records: caveat 3 DISCHARGED by `OWNER_WRITE_CAVEAT3_LMFDB_DISCHARGE_FINDINGS_378ca325_2026-11-03.md` (sha `3bbf715f5d021fe3…`), with independent re-fetch MATCH `74453e8c…`. This is a **cited database result, not a proof**.

**Caveats.**

1. "35" names the field, not the dimension.
2. CLOSED: $V_{35}$ includes all four narrow components $C_{00}=(1)$, $C_{10}=\mathfrak p_2=(2,1+\sqrt{35})$, $C_{01}=\mathfrak p_{19}$, $C_{11}=\mathfrak p_5=(5,\sqrt{35})$. Here $h^+=4$ and $\mathrm{Cl}^+\cong C_2\times C_2$ (`OWNER_WRITE_CAVEAT2_NARROW_ALL_FOUR_CLPLUS_V35_2026-11-03.md`, sha `e4ef0a810d1be98f…`).
3. DISCHARGED (above).

**Proposition 5.2 (field arithmetic used on record; recomputed for this draft).** Let $K=\mathbb{Q}(\sqrt{35})$, with discriminant $\Delta=140$ and fundamental unit $\varepsilon=6+\sqrt{35}$ (cited).

- (a) $N(\varepsilon)=36-35=+1$ and $\mathrm{Tr}\,\varepsilon=12$.
- (b) $R=\ln\varepsilon=2.477888\ldots$
- (c) With $h=2$ (cited), $2hR/\sqrt{140}=0.837679\ldots$
- (d) $\ln\varepsilon/\sqrt{10}=0.783577\ldots\neq0.837679\ldots$
- (e) The odd residues $r$ mod 140 with $(140/r)=-1$ are exactly the 24 classes {3, 11, 27, 37, 39, 41, 47, 51, 53, 57, 61, 69, 71, 79, 83, 87, 89, 93, 99, 101, 103, 113, 129, 137}. The inert primes below 100 are $3,11,37,41,47,53,61,71,79,83,89$.

*Proof.* (a) $(6+\sqrt{35})(6-\sqrt{35})=1$. (b)–(d) are direct evaluation. (e) is direct evaluation of the Jacobi symbol $(140/r)$ for odd $r$ coprime to 140, which equals the Kronecker symbol there. $\square$

The class number $h=2$, $h^+=4$, the unit, and the claim "$h^+=2h$ since $N(\varepsilon_0)=+1$" are cited from `OW_gemini_answers_SoftSF_REFUSE_2026-11-03.md` ("soft/open — OK") and the caveat-2 lock. They are not re-proved here.

**Warning.** (e) shows that the 11-element list is *correct but incomplete* as an inert-prime register. That is exactly the reason for the Kronecker REFUSE (sha `443555560472…`): an incomplete subset was presented as a complete locked register, and residue classes were swapped with primes.

## 5.3 F1–F3: Cat A READY as cite-lifts only

Sources: `PP_DOSSIER_Local_F1F3_Interface_Verification_CORRECTED_v2_2026-11-03.md` (sha `525c8a689a6ca1d9…`); PP audit `PP-FINDINGS-CATA_FOOLPROOF_2026-11-03.md` §5.

- **F1** (Thm A/B + Lemma 5 E). The RPP cancellation problem is weakly NP-complete when $M$ is part of the input. Restricted to the slice $M=2^k+1>\Sigma$, $C=\{0,1\}$, unit coefficients. FALSE for fixed odd $M\le\Sigma$ (counterexample $M=3$, $w=\{1,2\}$, target 0). Pseudo-polynomial DP in $O(nM)$. PP: FLAG (minor), restrict to the E hypotheses.
- **F2** (Lemma 5 C). $\det\rho\ne0$ does not prevent signed cancellation. PP: CONFIRM.
- **F3** (Lemma 5 B). $|W|\le N\le\prod\|h_i\|_1=\mathrm{spr}(\rho(|T|))$. The det-causation reading (Lemma 5 D) is FALSE and is not lifted. PP: CONFIRM.

Lemma 5 is PARTIAL overall. These are **cite-lifts**, not new proofs.

The F2 counterexample can be checked by hand, so we record it.

**Proposition 5.3 (F2 witness; record: PP item 1).** In $\mathbb{Z}[\mathbb{Z}/3]$ let $h_1=[0]+[1]$ and $h_2=-[0]+[1]+3[2]$. Then $\det\rho(h_1)=2$ and $\det\rho(h_2)=36$, both nonzero. Yet the signed path count to residue 1 has $W=0$ while $N=2$.

*Proof.* For the regular representation of $\mathbb{Z}/3$, $\det\rho(h)=\prod_{k=0}^2\hat h(\omega^k)$ with $\omega=e^{2\pi i/3}$.

For $h_1$: $\hat h_1(1)=2$ and $\hat h_1(\omega)\hat h_1(\bar\omega)=|1+\omega|^2=1$, so $\det=2$.

For $h_2$: $\hat h_2(1)=3$ and $|{-1}+\omega+3\omega^2|^2$. Using $\omega^2=\bar\omega$: the real part is $-1-\tfrac12-\tfrac32=-3$, and the imaginary part is $\tfrac{\sqrt3}2-\tfrac{3\sqrt3}2=-\sqrt3$. So the modulus squared is $9+3=12$, and $\det=3\cdot12=36$.

Paths to residue 1 choose one term from each factor, with exponents summing to $1\pmod3$:

- $(0,1)$: coefficient $1\cdot1=1$;
- $(1,0)$: coefficient $1\cdot(-1)=-1$.

(The pair $(2,2)$ is not available, because $h_1$ has no $[2]$ term.) So $W=1-1=0$ and $N=2$. $\square$

## 5.4 Open gaps on the Local Path

**Conjecture/Open 5.4 (Bridge $A1\to\Xi\to\mathrm{RTA}$).** The record conjectures a residual map from $A1$ through the shadow Ξ to RTA objects, under which the leading profile of $C$ lies outside $V_{35}$ ("$C\notin V_{35}$", F6).

- *Known:* $V_{35}$ is locked (Cited Result 5.1). Bridge Series C is defined (R7). The published RTA theorems are conditional as listed in §5.1.
- *Missing:* a formula for $C$ as an object comparable to $V_{35}$; a written polar system; a stated relation between $V_{35}$ and the tip's $V_{42}$ (the tip uses $\dim V=42$, with no $V_{35}$; PP §2 / F6 ABSENT); and the tip's P5b cocycle-dimension statement, which is marked `[[ to prove ]]`.
- *Would close it:* an Owner-written definition of $C$ in a Hilbert-modular (not elliptic-curve) category, together with a finite decision procedure against the 14-dimensional space (Gemini R2 Local Q1–3, Q20).

**Open 5.5 (residual law for C, R9).** Find the modular completion of $C$ whose period matches the Fricke samples at $1/7,3/7,5/7,1$ under a weight-1/2 slash prefactor. Status: OPEN. Quantum modularity of $g_s$ and $C$ is likewise open (RTA manuscript line 226, cited).

**Open 5.6 ($\Pi_{\mathrm{fast}}$).** The general lemma (an idempotent $P$ has spectrum in $\{0,1\}$; $\mathrm{Id}$ minus the time-average is idempotent) is PROVED on record. The corpus operator is undefined. $P_0\circ\mathrm{Ad}$ is not idempotent in general (Ad-type CX2, PP §5b). The Cesàro version is withdrawn pending a domain. Two inconsistent definitions are on record.

**Open 5.7 (exponents).** 7/20 has no source. It is invented and is not Kim–Sarnak's $7/64$. Moreover, $7/64$ concerns Maass forms: holomorphic parallel-weight-2 Hilbert newforms satisfy Ramanujan–Petersson with $\theta=0$ (Blasius, cited in `OW_asymptotic_complexity_SoftSF_PARTIAL_2026-11-03.md`, sha `df94665e09ee81cb…`). Burgess is $3/16=0.1875$, not $0.2000$, and no Burgess-type bound for this setting is in Cat A.

**Open 5.8 (BQP chain).** "BQP ⊂ C_HQH ⊂ NP-Complete" is FALSE as written: $\emptyset\in\mathrm{BQP}$ is not NP-complete (PP item 10). The repaired "⊆ NP" reading is open (Raz–Tal oracle separation, cited on record). Its wording is limited to 539 Labs sources.

**Object-swap pitfalls (record).**

- The elliptic curve $E:Y^2=X^3-35X$ has conductor $78400=2^6\cdot5^2\cdot7^2$ (PARI, cited), **not 560**. It is a different object from the Hilbert space $V_{35}$.
- Newform dimensions (2+2+2+8) are not narrow-class components.
- $V_{35}$ is not a Petersson-orthogonal summand of an elliptic weight-2 space, so the Ξ-Petersson decomposition is ill-typed.

# 6. Non Local Path

Sources: `Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt` (sha `08b8541a1b40e169…`); `OWNER_WRITE_INVENT_HOLD_LIFT_NONLOCAL_GENERAL_2026-10-26.md` (sha `c6e9aad7823f14b0…`); Gemini R2 NL Q1–20 (sha `f5ad0537fa344985…`).

## 6.1 Einstein–Hampton 11D (L1–L7): status

The record writes $G_{MN}=8\pi G_{11}T^{(EH)}_{MN}$, with $T^{(EH)}=T(G_4)+T(M2)+T(m)+T(-)+T(\mathrm{PBH})$, no $\Lambda_{11}$, and the warped metric $ds^2=e^{-2A(y)}\eta_{\mu\nu}dx^\mu dx^\nu+dy^2+e^{2B}\hat g_{ab}dz^adz^b$ with $B$ constant and $\hat R_{ab}=\kappa_{\mathrm{int}}\hat g_{ab}$. The derivation sketches L1–L7 for this ansatz are on record (Appendix B; SymPy check dated 28 Sep 2026; "Lean source L5, L7. No kernel run here.").

**Remark 6.1 (algebraic consistency of the lock; checked here).** Take the record's block equations $6k^2-3K=-\Phi/96$ and $4k^2+K=\Phi/144$. Substituting $K=8k^2$ gives $-18k^2=-\Phi/96$ and $12k^2=\Phi/144$. Both are equivalent to $k^2=\Phi/1728$. So the pair (EH-lock) solves the system, and $K=\Phi/216$ agrees with the SymPy output.

This checks only the final algebra step. We do **not** re-derive the curvature identities L4–L6 here. They are cited as record derivations for a stated ansatz.

**Open 6.2 (EH 11D programme).** *Known:* the ansatz and the lock algebra above. The flux match "wants $N=4870.45$; miss 9.55 units" against $N=4880$, per the record. *Missing:*

- independence and definition of each layer (Riemann, Weyl, warp or flux object);
- the field content beyond the metric ($C_3$, $G_4$) and the action;
- whether the dark-halo geometry is a solution or a fit, and the 4D observable through a stated reduction;
- the origin of a 4D $\Lambda$.

Many inputs are marked "Inserted" on record (4880, 243/539, 243/4880, 0.181, …, 539.90 s). *Would close it:* answers to Gemini R2 NL Q1–6, plus the record's own "next check": four-form weights $T_{\mu\nu}/g=-G^2/96$ vs $T_{ab}/g=-G^2/288$.

## 6.2 Reverse-parity PT and non-local QM

**Open 6.3.** The general invent HOLD on Non Local is lifted (Owner Write `c6e9aad7…`). The reverse-parity test sheet is RR-NL-SHEET-01. The rule is **"No pass claim until a Written join exists."** No such join is on disk in the sources read for this paper.

Open questions (Gemini R2 NL Q7–16) include:

- what the table labels;
- how P and T act on $M_4$ vs $X_7$;
- whether the PT Hamiltonian is Bender-type, and if so its metric operator $\eta$;
- no-signalling for the reduced 4D theory;
- Bell/CHSH discrimination from standard QM;
- whether "simulated" is literal.

## 6.3 Boundaries with Local locks

These separations are on record and are kept here:

- NL ≠ Local Bridge C.
- There is no written map from $V_{35}$ to any EH object.
- $\mathrm{Res}\,\zeta_K$ is a Local Hecke-scale fallback only, not a GR singularity cutoff (four-forces REFUSE, sha `58885bf3d0660960…`).
- Kim–Sarnak $7/64$ does not apply to holomorphic weight 2.
- The conductor 78400 is Local arithmetic.
- The 3-adic SU(3) / confinement / four-force mappings are REFUSED (§9).

# 7. Auditor: full-corpus audit status and the 18 classes

Sources: `AUDITOR_FULL_REPORT_PLAIN_EXEC_SUMMARY_2026-11-03.md` (sha `759bf06b107d3b4b…`); `FINDINGS_AUDITOR_FULLCORPUS_SOFTSF_INVENTORY_18CLASS_2026-11-03.md` (sha `e51cbc41eb8a9b80…`).

**Status.**

- Nothing is certified.
- The tip is untouched.
- Professor Proof has no queue.
- Every checked file matched its fingerprint (zero mismatches). Some files are missing their sidecar, which is a housekeeping gap.
- The method was a regex inventory over 24,009 text files. It is heuristic, so expect false positives and misses.

| # | Class | Hits |
|---|---|---|
| 1 | Old $\Lambda_0$ numbers | 32 |
| 2 | $V_{35}$ defined the old way | 5 |
| 3 | $h=2$ without narrow/wide marker | 60 |
| 4 | Burgess 0.2000 | 17 |
| 5 | Conductor 560 | 11 |
| 6 | Ξ Petersson described as proven | 6 |
| 7 | 11-element Kronecker set | 9 |
| 8 | Refused systemic/four-forces claims as fact | 4 |
| 9 | F1–F3 on unpublished draft or called certified | 39 |
| 10 | Cesàro / Fréchet | 12 |
| 11 | $\mathrm{Res}\,\zeta_K$ 0.837679 as fixed constant | 26 |
| 12 | Kerr marked BLOCKED | 4556 (mostly noise) |
| 13 | Layer2 assumed present | 139 (includes neutral mentions) |
| 14 | Owner records missing sidecar | 19 |
| 15 | Same basename, different contents | none found |
| 16 | Complexity chain too broad | 1 |
| 17 | Locked-on-open dependencies | 1507 (pattern too vague) |
| 18 | $V_{35}$ tied to physical predictions | 4 (best effort) |

Open items listed by the Auditor:

- Layer2 ABSENT (only the $D_1$ definition is now locked; §4);
- Wilson 7/20 invented (not found in the literature; PP confirmed);
- BQP chain open;
- Cesàro withdrawn;
- tubulin literature pair `58fe2225` awaiting PP.

# 8. Residual path to RTA: what remains open, ranked

The ranking is by blocking strength, judged from how many downstream items each gap gates on record. It is an editorial ordering, not an Owner Write.

1. **Definition of $C$ comparable to $V_{35}$, and the $V_{35}\leftrightarrow V_{42}$ relation.** This blocks F6, the whole Bridge $A1\to\Xi\to\mathrm{RTA}$, and any "$C\notin V_{35}$" statement.
2. **Written link from RTA objects ($T_3$, $O_{\mathrm{res}}$, 539, packaging) to the modular framework.** On record it is absent (23644022 Part IV). Theorem 3.5 shows that the link cannot be supplied by identifying the count 539 with a schedule.
3. **Residual law for C (R9) and the quantum modularity of $g_s$ and $C$.**
4. **The tip's P5b cocycle dimension `[[to prove]]`.** It is needed by the tip's uniqueness route.
5. **$\Pi_{\mathrm{fast}}$.** One definition, a domain, and a non-zero idempotent.
6. **O1 density / Necessity.** By O1, the residual core cannot force $A_5$ (Theorem 8.1 below), so this needs external geometric input.
7. **$T^\sharp$ 3-adic equidistribution (O2).** Open-unconditional. Neither the free basins nor the counts supply it.
8. **BQP chain.** Conditional or open.
9. **Layer2 artifact.** It needs an Owner-authorised build of the locked $D_1$ definition. Until then it stays ABSENT.

**Theorem 8.1 (O1: $A_5$ is not forced by the residual core; record: `O1_A5_Necessity_Impossibility_from_Residual_Core_2026-08-16.md`, sha `a167105ec8de2e8b…`).** Let $P(x)=x^5-4880x^3+32879x-243$. Then:

- (a) $P$ is irreducible over $\mathbb{Q}$, and $\mathrm{disc}(P)=318948969013863311130132536069=47\cdot1901\cdot788309\cdot4528399596133175803$, which is not a square. Hence $\mathrm{Gal}(P/\mathbb{Q})\not\subseteq A_5$.
- (b) The residual thin data ($F$, $H^\bullet(F)$, $D_1$, $G_\times$, the counts) carry no action of $\mathrm{Gal}(\bar{\mathbb{Q}}/\mathbb{Q})$ on the roots of $P$, so they cannot impose evenness.

*Proof.* (a) Irreducibility and the discriminant factorisation were recomputed with SymPy for this draft. All four prime exponents are odd, so the discriminant is not a rational square. For an irreducible separable polynomial, $\mathrm{Gal}\subseteq A_n$ if and only if $\mathrm{disc}$ is a square. The full statement $\mathrm{Gal}=S_5$ is **cited** from O1 and is not re-proved here: it needs a further argument, for example the existence of a 5-cycle and a transposition.

(b) The objects of §2 are $\mathbb{Q}$-vector spaces built from sector indices and tower labels, with no reference to $P$. Any evenness criterion would be extra structure. On record that structure is imported from geometric multi-$k$ fusion and is "not derived from residual discrete combinatorics alone". $\square$

**Scope.** Theorem 8.1 is an *impossibility of forcing from the residual core*. The density and Necessity statements stay **OPEN**. The REFUSE of the "A₅⁺ fibre-closure under $D_1$" sketch (§9) rests on exactly this theorem.

# 9. Appendix — refused claims

All files are in `/workspace/reports/539labs/ow/`. The sha prefixes were computed while this draft was compiled.

| Claim | Verdict | Reason on record | File (sha) |
|---|---|---|---|
| Kronecker residue filter mod 35 | REFUSE | Period of $(140/\cdot)$ is 140, not 35. Isolate and purge sets overlap. Split primes isolated. Broken code. | `OW_kronecker_720_dossier…` (c072f9fc7e63) |
| "Corrected" mod-140 isolate set | REFUSE | Many split residues included and true inert residues missed. 117 split primes wrongly isolated and 62 inert primes missed below 2000. | `OW_kronecker_mod140_corrected…` (04a1ede06ae0) |
| Kronecker purge / 11-element register | REFUSE | Residue classes swapped with primes. Incomplete list presented as complete. Ramified 5, 7 labelled split. | `OW_kronecker_filter_push…` (443555560472) |
| Systemic implications (purge "stabilises", Ξ insulators, EPR, confinement, measurement problem) | REFUSE | Rests on the refused purge. Newform/narrow-class object swap. Overclaims. | `OW_systemic_implications…` (a1bb2988be90) |
| Four forces from $V_{35}$ / Kronecker / $\mathrm{Res}\,\zeta_K$ | REFUSE | Invented mappings. Newform dimensions are not gauge groups. $\mathrm{Res}\,\zeta_K$ is not a GR cutoff. External blog cites. | `OW_four_forces_structural…` (58885bf3d066) |
| A₅⁺ fibre closure under $D_1$ | REFUSE | Contradicts O1. Wrong base field. Unnamed $H^2(S_5,\mathbb{Z}/2)$ class. Undefined cup product. A local prime cannot kill a global class. Hom into $\mathbb{F}_5$ is not a group. | `OW_A5plus_fibre_closure_D1…` (d3a172ad29ac) |
| "generated/Layer2.md on disk" | REFUSE | `find` returns empty. Layer2 ABSENT. | `OW_Layer2_md_status…` (559111934cc1) |
| Structural implications (Burgess 0.2000, $\Lambda_0$ "derived", N=560, Eichler–Selberg dimension lock, BQP) | REFUSE | Burgess is 3/16. $\sqrt{10}$ underived. Conductor 78400. Dimension per LMFDB. BQP open. | `OW_structural_implications…` (ea1815f7af82) |
| Local "resolution" v1/v2 | REFUSE | Single-dimension lock unjustified. Cesàro still uses $\mathrm{ad}$. Ξ/Petersson construction only open. $\Lambda_0\ne\mathrm{Res}\,\zeta_K$. | `OW_local_resolution…` (a8dc29ec8c1b), `…_v2…` (886e5efc7cf3) |
| $\Lambda_0=0.7858$ governs F1–F3 | REFUSE | Numeric drift from $0.783577$. Agent assertion. | `OW_lambda0_governance…` (4e5a39af2fca) |
| Gemini 25-question answer matrix | REFUSE | Wrong inert list. False spectral-radius product (counterexample $A=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$, $B=A^T$). LMFDB not unique. C/$V_{35}$ swap. $7/20\neq7/64$. | `OW_gemini_answers…` (49500bfd363a) |
| "Live" LMFDB validation | REFUSE | Hard-coded split. No API call. | `OW_lmfdb_validation_push…` (c45f01c7a101) |
| Ξ projection / Petersson leakage | REFUSE (in PARTIAL) | $V_{35}$ is not a summand of the elliptic weight-2 space. Kim–Sarnak not applicable ($\theta=0$). | `OW_asymptotic_complexity…` (df94665e09ee) |

**General pitfalls.**

- Object swaps: residues ↔ primes; newform dimensions ↔ narrow components; elliptic $C$ ↔ Hilbert $V_{35}$; Galois cohomology ↔ $H^\bullet(X_\times)$.
- Kronecker, SU(3) and four-forces physical mappings.
- Ξ Petersson decomposition.
- Burgess $0.2000\to3/16$.
- Conductor $560\to78400$.
- Kim–Sarnak $7/64$ applied to holomorphic weight 2.
- Using 539 as a clock.

# References

## On-disk record

Paths are relative to `/workspace/`, with sha256 prefixes.

- `quantum-comp/oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/`:
  - `RESIDUAL_VS_RESONANT_2026-08-16.md` (342862a6dc643916)
  - `Residual_Product_Complex.md` (f155466edf9858cf)
  - `Residual_Product_Cohomology.md` (900ffa219417d0b6)
  - `Thin_Complex_Formality.md` (325002c4cc5f08c4)
  - `P4_Product_Complex_Only_One_Essential_Class_2026-08-16.md` (16ab8489ffb788f0)
  - `Executive_Summary_2026-08-16_Pursue_All_Residuals.md` (2e8b07e3a46db382)
  - `O1_…` (a167105ec8de2e8b), `O2_…` (10fa5d07741ed103), `O3_…` (59239400bda05c75), `O4_…` (68e262590934fb00), `O5_…` (f73dd6ea1828c809), `O6_…` (508eeb61a0f913bd)
  - `FREE_VS_PACKAGING_LOCK_2026-08-16.md` (489c786a545576ad)
  - `resonant_to_geometry_2026-08-16.md` (fcd9d57d45bad166)
  - `residual_to_geometric_2026-08-16.md` (72737caec62044b9)
  - `MISS_LIST_M1_to_M7_2026-08-16.md` (d539e34294192f6f)
  - `U1_DNE_Discrete_NonEuclidean_D1_to_D9_2026-08-18.md` (47bb1deb2c2b0c42)
- `quantum-comp/reports/OWNER_WRITE_LOCK_D1_Seff_Layer2_T3_2026-11-03.md` (96f8d42e80c1975b)
- `reports/539labs/ow/ATTACH_Layer2_T3_specs_LOCKED_t3511u_a71f388e.txt` (a71f388efa353125)
- `reports/539labs/ow/OW_PP_picks_Lambda0_V35_Owner_LOCK_2026-11-03.md` (c290a274e7b31dc7)
- `quantum-comp/reports/OWNER_WRITE_CAVEAT2_NARROW_ALL_FOUR_CLPLUS_V35_2026-11-03.md` (e4ef0a810d1be98f)
- `quantum-comp/reports/OWNER_WRITE_CAVEAT3_LMFDB_DISCHARGE_FINDINGS_378ca325_2026-11-03.md` (3bbf715f5d021fe3)
- `quantum-comp/reports/bridges/AUDITOR/AUDITOR_FULL_REPORT_PLAIN_EXEC_SUMMARY_2026-11-03.md` (759bf06b107d3b4b)
- `quantum-comp/reports/bridges/AUDITOR/FINDINGS_AUDITOR_FULLCORPUS_SOFTSF_INVENTORY_18CLASS_2026-11-03.md` (e51cbc41eb8a9b80)
- `reports/539labs/gemini/GEMINI_Q_ROUND2_FULL_BATCH_2026-11-03.md` (f5ad0537fa344985)
- `reports/539labs/ow/PP_DOSSIER_Local_F1F3_Interface_Verification_CORRECTED_v2_2026-11-03.md` (525c8a689a6ca1d9)
- `quantum-comp/bridges/PROFESSOR_PROOF/PP-FINDINGS-CATA_FOOLPROOF_2026-11-03.md` (4e70be9ad36c2914)
- `quantum-comp/reports/DEFINITION_RTA_RESIDUALS_TO_FIFTH_ORDER_ORTHANT_CONES_LIMA_CHAIN_2026-10-26.md` (bd7520f98716062c)
- `quantum-comp/reports/T928U_RTA_THEOREM_COUNT_2026-10-25.md` (a85e30bdd41ea75e)
- `quantum-comp/nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt` (08b8541a1b40e169)
- `quantum-comp/reports/OWNER_WRITE_INVENT_HOLD_LIFT_NONLOCAL_GENERAL_2026-10-26.md` (c6e9aad7823f14b0)
- The Soft SF refusal files listed in §9.

## Published sources (only as already cited on disk)

- A. B. Hampton, *Residual Ternary Algebra and a modular foundation*, Zenodo, doi:10.5281/zenodo.23644022 (v12, 2026-10-25); and Zenodo record 22143607 (main draft and supplemental). Both are cited via T928U.
- LMFDB, Hilbert modular forms over 2.2.140.1, level 1, parallel weight [2,2]. Cited via caveat-3 discharge `3bbf715f…` and MATCH `74453e8c…`.
- H. Kim and P. Sarnak, the $7/64$ bound; V. Blomer and F. Brumley (2011); D. Blasius, Ramanujan–Petersson for Hilbert modular forms. All three are cited via `OW_asymptotic_complexity…` (df94665e).
- D. A. Burgess, the subconvexity exponent $3/16$. Cited via the structural/local REFUSE files.
- R. Raz and A. Tal, the oracle separation of BQP and PH. Cited via PP-FINDINGS item 10.
- A. Einstein (1915); E. Cremmer, B. Julia and J. Scherk (1978); L. Randall and R. Sundrum (1999). Cited via the EH appendix.
- S. Zwegers (indefinite theta / mock theta), cited via the Lima-chain definition file; listed on record as a missing primary source (Gemini R2 Local Q13).

---

**Status:** tip `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` untouched. No CERT. Layer2 ABSENT (only the $D_1$ definition is Owner-locked). Cat A READY = Local F1–F3 cite-lifts only.
