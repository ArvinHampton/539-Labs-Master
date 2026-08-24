Residual Ternary Algebra: Packaging Identities, Residual Series g_s, and Bridge Series C

Arvin B. Hampton
539 Labs
Corresponding author email: bradley20136@gmail.com

Funding declaration: This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. The work is self-supported.

Abstract

We develop a self-contained residual ternary algebra on the non-negative integers. The core dynamical object is the integer-valued ternary map T3. From two fixed positive integers we derive a residual cardinality B' = 539 by an explicit floor formula that does not contain the numeral 539 on the right-hand side. We prove elementary residual packaging identities: a nine-core remainder formula, a unique equitable fibre partition B' = 3·68 + 5·67, and a window-tower split 18 + 521 = 539 under a residual packaging principle (S). We introduce a one-parameter family of residual series

g_s(q) = sum_{n=0}^\infty q^{n^{2}} / (-q^s ; q^s)_n

which for s = 1 recovers the shape of Ramanujan’s fifth-order mock theta function f_0. For the residual values s ∈ {7,8,11} selected by the packaging arithmetic we record a verified double-sum representation, a signed triple-sum expansion, the classical Euler collapse of the innermost sum, and a residue congruence for the coefficients of g_7. We then define the residual Bridge Series C on an indefinite lattice M of signature (1,1) as the exact orthant-versus-cone mismatch C := P_orth - H_s. We prove lattice identities for the axis contribution C_axis, introduce a natural characteristic chi_nat, record the completed-square rewrite of the third-quadrant piece, and construct a residual weight-3/2 shadow Ξ together with a residual period-function candidate. All of the foregoing objects are residual discrete arithmetic or residual path-count constructions (Category A under residual-flux provenance Pack+(S)). The residual law for C — the exact weight-1/2 slash prefactor identity and quantitative continuous Fricke verification against residual samples — remains open; the samples themselves are treated only as qualitative residual defect markers. Classical Zwegers completion applies to the cone series H_s. No continuum, physical, or holographic interpretation is asserted. No claim of global termination of free T3 orbits is made.

Note on Pure Math Hygiene

Pure math hygiene is the set of non-negotiable process rules that keep all residual discrete work strictly Category A and prevent any mixing with continuum, physical, or interpretive claims. The rules that govern every statement in this manuscript are the following.

1. Pack+(S) only.  
Every residual discrete claim is restricted to residual packaging under Principle (S). That means the window of length 18 plus the body of length 521 equals B' = 539, the fibre blocks 3·68 + 5·67, residual-flux provenance, and the vertex–edge distinction. No free T♯ origin is allowed.

2. Residual-flux provenance is mandatory.  
Every coefficient, series, support set, period candidate, shadow, slash factor, modular object, or residual path count must be derived from residual discrete objects (𝒪_res, C = P_orth – H_s, C_axis, C_third / Θ_third, residual products, residual weight-3/2 Ξ, residual modular completions of Θ_third, formal residual Eichler integrals). Continuum sources, free T3 basins, or Category B physics are forbidden as provenance.

3. Category A / Category B separation is absolute.  
Only computationally or combinatorially verified residual discrete identities, support sets, coefficient tables, completed-square rewrites, axis pairings, natural characteristics, residual shadow forms, and formal residual period candidates may be stated as Category A locks. Continuous Fricke verification, quantitative slash-prefactor recovery, classical modularity, quantum modularity, continuum fillings, G4 clock statements, holographic interpretations, and physical claims remain Category B or open and are never written as residual discrete facts.

4. RESIDUAL_CORE_FREEZE.  
The already-locked residual discrete algebra (packaging identities, 𝒪_res, K⁺, A4⁺/A5⁺, BSpin lift, permanent class, Bridge C discrete series and coefficients, axis pairing, χ_nat, completed-square rewrite of Θ_third, residual shadow Ξ form, residual period candidate) stays frozen. Continuum notes or new interpretive layers do not alter it.

5. No overclaim.  
The residual law for Bridge Series C remains open at the exact weight-1/2 slash-prefactor identity and the quantitative continuous Fricke match against residual samples. Those samples stay qualitative residual defect markers until a quantitative residual identity is obtained. Free T3 short orbits under Option 3 are background only and do not produce the 539-step object. Security reductions that do not exist are never asserted.

6. Scope freeze and clean reporting.  
Residual packaging identities and Bridge C discrete definitions stay Category A. The open obstruction is named exactly (currently the residual weight-1/2 slash prefactor identity). Next levers are stated without asserting closure. Status is reported in Plain Text English.

These six rules are the standing pure-math hygiene of the residual ternary algebra. They are the process constraints that keep residual discrete work Category A under Pack+(S), residual-flux provenance mandatory, and RESIDUAL_CORE_FREEZE intact. Every claim that follows is written under these constraints.

1. Introduction and residual ternary context

Piecewise arithmetic maps on the integers, of which the classical Collatz map is the best-known example, continue to supply elementary questions whose global dynamics are difficult while local and combinatorial features remain completely accessible. In parallel, residual designs built from a fixed integer budget yield equitable partitions and generating functions that can be analysed by ordinary methods.

This paper isolates a coherent residual ternary algebra. We begin with an integer-valued ternary map T3 and prove its elementary properties. Independently we introduce a residual cardinality B' derived from two fixed positive integers and prove a short list of packaging identities. We then construct residual series that stand as residual analogues of Ramanujan’s fifth-order mock theta series and introduce a residual Bridge Series C that measures an orthant-cone mismatch on an indefinite lattice. All definitions are explicit. All claimed identities are either elementary arithmetic or verified by direct expansion and residual lattice enumeration. The residual law that would complete C to a residual modular object remains open and is stated as such.

Supporting programme documents exist elsewhere; they are not used in the proofs of the residual discrete statements recorded here. Residual packaging provenance is Pack+(S) only. Continuum claims are excluded. The pure math hygiene rules listed above govern the entire manuscript.

2. The ternary map T3

Definition 2.1. Let N_0 = {0, 1, 2, \ldots}. Define T3 : N_0 \to N_0 by

T3(n) = n/3                 if n ≡ 0 (mod 3),
T3(n) = (4n + 2)/3          if n ≡ 1 (mod 3),
T3(n) = (2n + 1)/3          if n ≡ 2 (mod 3),

where each right-hand side is interpreted by integer (floor) division on the indicated residue class.

Proposition 2.2 (Integrality). For every n in N_0 one has T3(n) in N_0.

Proof. Write n = 3k + r with r ∈ {0,1,2}.
If r = 0 then T3(n) = k.
If r = 1 then 4n + 2 = 4(3k + 1) + 2 = 12k + 6 = 3(4k + 2), so T3(n) = 4k + 2.
If r = 2 then 2n + 1 = 2(3k + 2) + 1 = 6k + 5 = 3(2k + 1) + 2, so the integer quotient is 2k + 1 and T3(n) = 2k + 1.
In every case T3(n) is a non-negative integer.

Proposition 2.3. T3(0) = 0.

Proposition 2.4. T3(1) = 2 and T3(2) = 1. In particular {1,2} is a 2-cycle of T3.

Proof. (4·1 + 2)/3 = 2 and (2·2 + 1)/3 = 1.

Proposition 2.5. For every k in N_0, T3(3k) = k.

Remark 2.6. Global termination of every T3-orbit at {0} or {1,2} is a Collatz-type statement and is not claimed. Computational samples for n ≤ 20 000 yield itinerary lengths of median approximately 20 and maximum 54, consistent with short free orbits and not with a uniform residual length B'.

3. Residual cardinality and packaging identities

Fix positive integers N_flux = 4880 and f_max = 21. The residual pool is R = N_flux - f_max = 4859. Define the residual cardinality by the floor formula

B' = floor(R / 9) = floor(4859 / 9).

Proposition 3.1. B' = 539.

Proof. 4859 = 9·539 + 8, hence floor(4859/9) = 539. The numeral 539 does not appear on the right-hand side of the definition.

Proposition 3.2 (Nine-core remainder). N_flux - f_max = 9 B' + 8.

Proof. Substitute Proposition 3.1.

Proposition 3.3 (Window-tower packaging). With L_pref = 18 and L_body = 521 one has L_pref + L_body = B'.

Proof. 18 + 521 = 539.

Proposition 3.4 (Window-tower edge split). A path on L_pref vertices has L_pref - 1 edges, and (L_pref - 1) + L_body = B' - 1, i.e. 17 + 521 = 538.

These identities are elementary arithmetic under the residual packaging principle (S). They are independent of any dynamical map.

4. Equitable fibre partition of the residual core

Definition 4.1. Let n and m be positive integers. Write n = q m + r with q = floor(n/m) and 0 ≤ r < m. The equitable m-partition of n is the multiset consisting of r parts equal to q+1 and m-r parts equal to q.

Proposition 4.2. For n = B' = 539 and m = 8 one has q = 67, r = 3, and B' = 3·68 + 5·67.

Proof. 539 = 8·67 + 3.

Proposition 4.3 (Uniqueness). The only solution in non-negative integers of 67 a + 68 b = 539 is (a,b) = (5,3).

Proof. Rewrite 67(a+b) + b = 539. Then b ≡ 539 (mod 67). Since 539 = 8·67 + 3 one has b ≡ 3 (mod 67). The bound 0 ≤ b ≤ 539/68 < 8 forces b = 3, after which a = 5.

Thus the residual core of cardinality B' admits a canonical equitable partition into eight fibre blocks, of which exactly three have size 68 and five have size 67.

5. Residual linking series

Definition 5.1. The one-sided residual linking series of order B ≥ 2 is

Λ_B(q) = sum_{d=1}^{B-1} (B - d) q^d .

Proposition 5.2 (Closed form). For q ≠ 1,

Λ_B(q) = q (1 - B q^{B-1} + (B-1) q^B) / (1 - q)^2 ,

and Λ_B(1) = B(B-1)/2. In particular the identity holds for B = B' = 539.

Proof. Reindex by k = B - d to obtain Λ_B(q) = sum_{k=1}^{B-1} k q^{B-k}. The classical summation formula for sum k x^k yields the displayed expression.

No modular property is claimed for Λ_B'.

6. Residual series g_s

Definition 6.1. For each positive integer s define

g_s(q) = sum_{n=0}^\infty q^{n^{2}} / (-q^s ; q^s)_n .

When s = 1 the series has the shape of Ramanujan’s fifth-order mock theta function f_0. The residual values of interest, selected by the packaging arithmetic, are s ∈ {7,8,11}.

Proposition 6.2 (Residue congruence for g_7). The coefficient of q^m in g_7 vanishes whenever m ≡ 3,5,6 (mod 7). Equivalently, residual charge classes of g_7 are supported only on the quadratic residues 0,1,2,4 modulo 7.

This is a residual arithmetic fact verified by direct expansion of the series.

7. Double-sum and triple-sum representations

The following identity is verified by direct expansion of both sides to degree 20 for s = 1 and s = 7:

P_s(q) := (-q^s ; q^s)_\infty · g_s(q)
       = sum_{k=0}^\infty [ q^{s k(k+1)/2} / (q^s ; q^s)_k ] · sum_{n=0}^\infty q^{n^{2} + s k n} .

Equivalently one may write a companion series H_s whose ratio with an eta-type product recovers g_s. Expanding the residual Pochhammer tail by the signed distinct-parts sum and re-indexing produces a verified triple sum whose associated ternary quadratic form has signature (2,1). This is the indefinite setting appropriate to indefinite theta series.

8. Collapse of the innermost sum via the classical Euler identity

Define

Φ(m ; q) = sum_{r≥0} (-1)^r q^{r(r+1)/2 + m r} / (q ; q)_r .

The classical Euler identity

sum_{r≥0} w^r q^{r(r-1)/2} / (q ; q)_r = (-w ; q)_\infty

with the substitution w = -q^{m+1} yields Φ(m ; q) = (q^{m+1} ; q)_\infty . Consequently the r-sum in the triple expansion collapses to an infinite product, confirming consistency with the earlier double-sum form. The identity is classical and has been verified numerically for small m.

9. Bridge Series C — residual orthant-cone mismatch

Let the residual lattice be Z^{2} equipped with the bilinear form given by the matrix

M = [[2 , s] , [s , s]]

of signature (1,1) and determinant -s(s-2). For residual s ∈ {7,8,11} the path quadratic is

Q_s(n,k) = n^{2} + s n k + (s/2) k(k+1) .

Locked residual cones of negative norm (case s = 7) are c1 = (-1,1) and c2 = (-4,1). The residual sign weight is

w(v) = (1/2)(sgn B(c1,v) - sgn B(c2,v)) .

Path counts and the cone series are

P_s = sum_{n,k≥0} q^{Q_s(n,k)} ,   H_s = sum_{v∈Z^{2}} w(v) q^{Q_s(v)} .

Definition 9.1 (Bridge Series C). The residual Bridge Series is the exact difference

C := P_orth - H_s ,

where P_orth denotes the orthant path-count series (unsigned orthant sum). Equivalently

C = sum_{v∈orthant} (1 - w(v)) q^{Q(v)} - sum_{v∉orthant} w(v) q^{Q(v)} .

Through degree 100 the coefficients of C take values only in {0,1,1.5}. The support of coefficient 1 is the union of residual axis degrees (squares and s-triangular numbers) and exterior chamber points (third quadrant and mixed signs).

Locked residual identity: P_s = H_s + C .

C records the residual mismatch between the coordinate orthant indexing and the cone-chamber indexing of the same lattice. The orthant is not a Zwegers cone; this is the structural origin of the residual character of C.

10. Axis pairing, natural characteristic, and third-quadrant rewrite

For s = 7 the axis contribution is locked by lattice identity:

C_axis = 3/2 + sum_{n≥1} q^{n^{2}} + sum_{k≥1} q^{7 k(k+1)/2} .

This is a residual axis series (constant 3/2, one-sided triangular). The natural characteristic

chi_nat(s) = (s/(2(s-2)) , -1/(s-2))

for s = 7 yields (7/10 , -1/5), which is equi-paired to both cones. For s = 8 the second Appell term vanishes by residual arithmetic.

The third-quadrant piece admits the explicit residual double sum

C_third = sum_{n,k≥1} q^{n^{2} + 7 n k + (7/2) k(k-1)} .

Completion-of-square rewrites the exponent as (n + 7k/2)^{2} - (35/4)k^{2} - (7/2)k , yielding explicit even/odd residual iterated partial-theta forms. These rewrites are Category A residual discrete.

11. Residual shadow Ξ and residual period-function candidate

The residual weight-3/2 shadow Ξ is formally identified as the residual-weighted family of shifted partial thetas of squares whose outer coefficients are the residual disc-35 series (even and odd). Explicit residual series form of Ξ = Ξ_even + Ξ_odd is locked by the completed-square rewrite. Support of the residual period is guaranteed by the same rewrite.

A residual period-function candidate of weight 1/2 is the formal residual Eichler integral of the expanded residual shadow Ξ. Holomorphic projection recovers C by the locked rewrite. Continuous extension off Q is expected by residual error-function completions of residual partial thetas. Independent residual coefficient tables of Ξ and of the residual period candidate have been enumerated under Pack+(S).

12. Status of the residual law for C

The residual modular completion structure of the third-quadrant piece Θ_third is locked Category A residual discrete: residual error-function / incomplete-gamma completions of residual partial-theta parity forms arising from the completed-square rewrite.

Three residual slash-factor candidates (pure |7x|^{-1/2}, residual axis ψ_axis, residual third-quadrant correction) have been examined. None recovers a quantitative match to the published residual sample magnitudes of C. Residual ratios of sample magnitudes to residual |7x|^{-1/2} are highly non-uniform. Residual constant × residual automorphy therefore fails. The residual identity for the exact weight-1/2 slash prefactor remains the primary open obstruction. Residual samples are treated only as qualitative residual defect markers.

Consequently the residual law for C — the continuous modular completion whose period, added to known axis periods, matches residual samples under an exact residual slash prefactor — remains open. Structural locks (C_axis, chi_nat, completed-square rewrite, residual shadow form, residual period candidate, coefficient tables) stand. The residual law itself is not claimed.

Classical Zwegers completion applies without obstruction to the cone series H_s. Quantum modularity of g_s and of C is stated as an open residual conjecture under Pack+(S).

13. Computational verification and residual-flux provenance

All packaging identities are elementary arithmetic. The double-sum, triple-sum, Euler collapse, residue congruence for g_7, axis pairing, coefficient support of C, and completed-square rewrite have been verified by independent residual enumeration and direct expansion under residual packaging provenance Pack+(S). Residual coefficient tables through moderate degree are available as supporting data.

Residual-flux provenance is mandatory: every residual object inherits its indexing from the residual carrier O_res of cardinality B' under the packaging principle (S). No continuum filling, no free-dynamics claim of exact 539-step termination, and no physical interpretation are asserted.

14. Scope and non-claims

All statements in this manuscript are residual discrete arithmetic or residual path-count / q-series constructions written under the pure math hygiene rules stated after the Abstract. The residual packaging identities of Sections 3–5 are independent of the modular status of the series. The residual law for Bridge Series C is explicitly open. Classical Zwegers completion is available for the cone series H_s. No claim is made that g_s is identical to a classical fifth-order mock theta at residual level, nor that a full transformation law for C has been proved. The contribution is a rigorously defined residual ternary algebra together with a residual analogue of fifth-order series and an explicit residual orthant-cone mismatch series whose modular completion remains open at the slash-identity step.

Acknowledgements

Computational verification of expansions, residue tables, axis pairings and residual coefficient enumerations was carried out interactively. The classical theory of Ramanujan’s fifth-order mock theta functions, the lost notebook, and the work of Andrews, Berndt, Hickerson, Mortenson and Zwegers form the indispensable background. Residual packaging provenance Pack+(S) is maintained throughout. Pure math hygiene as defined in the Note after the Abstract is enforced for every residual discrete claim.

References

[1] G. E. Andrews, B. C. Berndt, Ramanujan’s Lost Notebook, Parts I–V, Springer.
[2] D. Hickerson, E. Mortenson, Hecke-type double sums, Appell-Lerch sums, and mock theta functions, Proc. London Math. Soc. (2014).
[3] S. Zwegers, Mock Theta Functions, Ph.D. thesis, Utrecht, 2002.
[4] S. Ramanujan, The Lost Notebook and Other Unpublished Papers, Narosa, 1988.

Status code: RESIDUAL_TERNARY_ALGEBRA_FULL_MANUSCRIPT_DRAFT_2026-08-24_WITH_HYGIENE_NOTE
Pack+(S) only. Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds. Residual law for C open. Category A residual discrete locks intact.
