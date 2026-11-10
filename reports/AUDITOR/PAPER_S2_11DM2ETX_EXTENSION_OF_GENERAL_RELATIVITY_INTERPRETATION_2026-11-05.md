# The S²-11DM²ET-X Extension of General Relativity: Residual Ternary Structure, Resonant Algebra, and a Non-Archimedean Core

**Arvin Hampton** — 539 Labs

5 November 2026

## Abstract

General relativity predicts its own breakdown. In the Schwarzschild solution the radial metric coefficient and the Kretschmann invariant diverge as the areal radius tends to zero, and no continuum regulator inside the theory removes this. We set out an interpretation of the S²-11DM²ET-X model as an extension of general relativity in which the continuum is supplemented, at the smallest scales, by a discrete arithmetic layer and a non-Archimedean (3-adic) core. The mathematical spine is residual ternary algebra, whose established results are collected in the Foundation Bound, version 16 [1]: a residual packaging with nine sectors of cardinality $B'=539$, a thin form complex with $H^2(F)\cong\mathbb{Q}\cdot[s_{\alpha\delta}]$, a rank-one static classifier $D_1$, and a separation theorem showing that the residual count 539 and the resonant iteration length 539 cannot be identified. On this spine we place an interpretive physical reading, published in expository form [2], in which the radial coordinate is regulated by its 3-adic absolute value with a floor $3^{-539}$ and the Kretschmann invariant is replaced by a bounded expression in a 35-component mass matrix. We separate carefully what is established mathematics — notably a Haar-measure Euler-factor identity on $\mathbb{Z}_3^4$ — from what remains a physical proposal. We name the observational data sets against which the proposal is to be tested, and state that none of them has yet been confronted quantitatively; agreement with data, when obtained, will be empirical support and not mathematical proof.

## 1. Introduction

The Schwarzschild exterior,
$$ds^2=-\Big(1-\frac{2GM}{r}\Big)dt^2+\Big(1-\frac{2GM}{r}\Big)^{-1}dr^2+r^2d\Omega^2,$$
is among the best-tested solutions in physics, yet its interior ends in a curvature singularity. The coordinate singularity of $g_{rr}$ at $r=2GM$ is removable; the one at $r=0$ is not, as the Kretschmann invariant shows [3]:
$$\mathcal{K}=R_{\mu\nu\alpha\beta}R^{\mu\nu\alpha\beta}=\frac{48G^2M^2}{r^6}\longrightarrow\infty\qquad(r\to0).$$
Singularity theorems establish that such behaviour is generic under reasonable energy conditions [4]. The usual reading is that general relativity is an effective theory whose ultraviolet completion must alter the short-distance structure of spacetime.

Two features of the Archimedean real line drive the divergence: distance can be subdivided without bound, and a sequence of radii can approach zero continuously. A non-Archimedean metric removes the second feature in a precise sense. Under the 3-adic absolute value the ultrametric inequality $|x+y|_3\le\max(|x|_3,|y|_3)$ holds, balls are either nested or disjoint, and the set of attained values $\{3^{k}:k\in\mathbb{Z}\}\cup\{0\}$ is discrete away from zero. A discrete arithmetic layer can then supply a floor below which further subdivision carries no physical meaning.

The S²-11DM²ET-X model proposes such a layer. This paper reads that model as an extension of general relativity: the classical metric governs at macroscopic scales, and a residual ternary structure with a 3-adic core governs at the scale where classical curvature would diverge. Our aim is interpretive and organisational. We do not offer new theorems. We assemble the established mathematics [1], state the physical proposal as published [2], and mark the boundary between them.

Section 2 summarises residual ternary algebra and the resonant schedule. Section 3 explains why the integer 539 is a capacity and not a clock. Section 4 states the non-Archimedean metric regulation. Section 5 records the Haar-measure identity that underlies the adelic sector. Section 6 describes the scope of the provable mathematical inventory. Section 7 discusses recovery of classical general relativity and what remains open. Section 8 states the empirical status, and Section 9 concludes.

## 2. Residual ternary algebra and resonant algebra

Residual ternary algebra begins from a packaging rule [1, 5]. Set $N_{\mathrm{flux}}=\lfloor e^3\cdot3^5\rfloor=4880$ and $f_{\max}=\lceil 4880/243\rceil=21$. The residual pool is $R=N_{\mathrm{flux}}-f_{\max}=4859=9\cdot539+8$, so each of nine charge sectors carries a core of
$$B'=\lfloor R/9\rfloor=539=7^2\cdot11$$
leftover pieces. This integer is a cardinality.

The residual structure is organised on the product complex $X_\times=K_9\times P_{B'}$, the complete complex on nine sectors times a path of length $B'$. Its first cycle rank is $\beta_1=36B'-8=19396$, and the mixed cochain on it is closed [1]. A thinner truncation, the residual form complex $F$, has
$$H^0(F)\cong\mathbb{Q},\qquad H^1(F)=0,\qquad H^2(F)\cong\mathbb{Q}\cdot[s_{\alpha\delta}],$$
is formal, and carries a unique essential class [1]. The class $[s_{\alpha\delta}]$ is a feature of the truncation: in the full product cochain complex $s_{\alpha\delta}$ is not closed and the second cohomology vanishes [1, 5]. Physically, this is the statement that a single rational degree of freedom survives the coarse-graining of the residual sector, and that it should not be over-read as a property of the full discrete complex.

Resonant algebra is a different object. It is a schedule: a local ternary step is fired a fixed number of times, $18+521=539$, and then stopped, with $18=\lfloor e^3/\ln3\rfloor$ [1, 5]. The underlying step is the canonical ternary map
$$T_3(n)=\begin{cases}n/3,& n\equiv0\pmod 3,\\ (4n+2)/3,& n\equiv1\pmod 3,\\ \lfloor(2n+1)/3\rfloor,& n\equiv2\pmod 3,\end{cases}$$
a Syracuse-type map that contracts by a factor $2/3$ on average. Its free orbit takes $4880$ to $1$ in fourteen steps [5]. The profile used throughout — the canonical map, exactly 539 iterations, and a fixed finalisation — is frozen as a single reference specification [6], so that every numerical statement about $T_3$ refers to one map rather than a family of variants.

The separation theorem of [1] states that the residual count $B'=539$ and the resonant length $18+521=539$ cannot be identified: equality of the integers does not make them the same structure. This is the organising principle of the extension. A count is not a clock.

## 3. Discrete capacity versus continuum clocks

In general relativity time is a coordinate on a Lorentzian manifold, and proper time is the length of a timelike curve. Any discrete extension must decide whether its integers measure duration or something else. Residual ternary algebra decides firmly. The static budget $S_{\mathrm{eff}}$ treats $T_3=539$ as a capacity: a count of cells, or equivalently of hash slots, available to the residual sector [1, 7]. It is not a period, a tick rate, or a lapse function. There is no congruence $\Omega\equiv0\pmod{539}$ forced by the structure [1].

The static classifier $D_1$ acts with rank one over $\mathbb{Q}$ on $H^2(F)\cong\mathbb{Q}\cdot[s_{\alpha\delta}]$ [1, 7]. Because $H^1(F)=0$ and $F$ is formal, the classifier sees exactly one rational invariant. Two further layers of the model are not derivable from $D_1$ alone [1].

For the gravitational reading this has a direct consequence. When we later write the floor $3^{-539}$ into the metric, the exponent 539 enters as a resolution depth — the number of ternary digits the core can resolve — and not as an elapsed time. The orbit of $T_3$ under the frozen profile is a discrete arithmetic structure on the integers; it is not a spacetime clock and confers no preferred time coordinate on the manifold. Lorentz covariance of the exterior solution is therefore untouched by the discrete layer; whatever the layer does, it does at the level of short-distance resolution.

## 4. Non-Archimedean core: 3-adic metric regulation

The physical proposal of the S²-11DM²ET-X model, in the form published in [2], replaces the continuum radius near the core by its 3-adic absolute value with an additive floor:
$$g_{rr}=\Big(1-\frac{2GM}{r}\Big)^{-1}\;\longmapsto\;\Big(1-\frac{2GM}{|r|_3+3^{-539}}\Big)^{-1}.$$
Since $|r|_3+3^{-539}\ge3^{-539}>0$, the denominator inside the bracket never vanishes, and the regulated coefficient is a finite value at every point of the core. The ultrametric inequality guarantees that the radial coordinate cannot approach a continuous zero: in the 3-adic picture, radii live on the levels of a ternary tree, and $3^{-539}$ is the deepest level that the residual capacity resolves.

For the curvature, [2] proposes that the Kretschmann invariant be carried, through a Mellin–Barnes transform of the curvature fields, onto a 35-component mass matrix $M_{35}$, and that in the core it be replaced by
$$\mathcal{K}\;\longmapsto\;\mathcal{K}_0\,(-1)^{\Delta I_{\mathrm{top}}}\,\big|\det M_{35}\big|_3^{-539},$$
where $I_{\mathrm{top}}$ is an integer-valued topological index and $\Delta I_{\mathrm{top}}=\pm1$ marks a parity change at the threshold. The divergence $r^{-6}$ is thereby exchanged for a bounded quantity with a discrete sign. The same source reads the event horizon as the boundary of the $T_3$ dynamics, with infalling information held in periodic attractor basins on $\mathbb{Z}_3$ and with a dissipation timescale fixed by the Haar measure of those basins [2].

These statements are an interpretive physical reading. Several ingredients are not yet defined at the level required for proof: the transform from curvature fields to $M_{35}$, the definition of $I_{\mathrm{top}}$ and the mechanism forcing its parity change, the map identifying 3-adic valuations with the Archimedean radial derivative, and the matching of the core to the exterior Schwarzschild solution across a junction surface. The model also introduces a scale $\Lambda_0\approx0.7858$ in its exterior-matching attempt; this value is not derived from the residual algebra, and the Foundation Bound records that no normalisation of this kind is established, with only a Hecke-scale fallback available [1]. We therefore present Section 4 as a proposal to be tested and not as a consequence of Sections 2–3.

## 5. Haar measure and the adelic sector

One ingredient of the core is established mathematics independent of its physical interpretation. Let $\mu_3$ be the Haar measure on $\mathbb{Q}_3^4$ normalised by $\mu_3(\mathbb{Z}_3^4)=1$, and let $|x|_3$ denote the maximum of the 3-adic absolute values of the coordinates. Then for complex $\nu$ with $\mathrm{Re}(\nu+3)>0$,
$$\int_{\mathbb{Z}_3^4}|x|_3^{\nu-1}\,d\mu_3(x)=\frac{1-3^{-4}}{1-3^{-(\nu+3)}}.$$
This is a standard local zeta integral of Tate type [8], recorded in the model's adelic sector [1, 2]. It follows from the shell decomposition $\mathbb{Z}_3^4\setminus\{0\}=\bigsqcup_{k\ge0}3^k(\mathbb{Z}_3^4\setminus3\mathbb{Z}_3^4)$, on which $|x|_3=3^{-k}$ and $\mu_3=(1-3^{-4})3^{-4k}$; the integral becomes the geometric series $(1-3^{-4})\sum_{k\ge0}3^{-k(\nu+3)}$, convergent exactly when $\mathrm{Re}(\nu+3)>0$. The right-hand side is an Euler factor: a local factor of the type that assembles into a zeta function across places.

The identity matters physically in two ways. First, it gives a closed form for the measure-weighted volume of the 3-adic core as a function of a scaling exponent, which is the quantity [2] proposes as the dissipation timescale of attractor basins. Second, its pole at $3^{-(\nu+3)}=1$ marks the boundary of convergence and suggests where an adelic description — combining the 3-adic core with Archimedean exterior data — would need analytic continuation. Neither use is established. The identity is mathematics; its reading as a black-hole timescale is part of the interpretive proposal of Section 4. In particular, an exterior Schwarzschild match, Bekenstein–Hawking entropy, and a Hawking spectrum have not been derived from it.

## 6. The provable mathematical inventory

The model's published exposition contains many mathematical claims of varying maturity. A filter applied to a list of 72 such items sorts them into categories: those that are statements of mathematics capable of proof from stated definitions, those already established, those that need definitions before they can be stated, and those that are not mathematical claims at all [1]. Of the 72 items, 45 are classed as provable candidates by primary (first-listed) tag [12]. This means they are well-posed mathematical statements for which a proof route exists or is expected; it does not mean that all 45 have been proved, and the remaining 27 are not classed PROVABLE-CANDIDATE by that tally, not declared impossible to prove.

The count 45 uses each item's primary (first-listed) tag, not every tag position: it remains 45 before and after the ABSORB update. Counting items carrying a PROVABLE-CANDIDATE tag in any position gives 46 before that update and 47 afterward. The other 27 are not classed PROVABLE-CANDIDATE by the primary-tag tally; this is not a claim that they are impossible to prove. No adopted enumerated 45-ID list is supplied, and proof candidates are not completed proofs. The tally source is PP audit §3 [12], not the Foundation Bound v16 or ABSORB alone.

The Haar identity of Section 5 is one of the 45 primary-tag candidates [12]. Its physical surround — the reading as a horizon timescale, the "pole inversion" language attached to it, and a bundle of physical constants associated with the core — is classed as requiring definition or as not a mathematical statement. Other provable candidates include combinatorial rank statements, such as an extra-relation count $k(k-1)$ whose rank arithmetic $m(m+1)-k(k-1)$ checks at the cases $m=7,17,31,49$ but whose sharpness the published record does not state consistently, and modular-form identifications that await written verification.

The theorem spine against which these candidates are measured is the Foundation Bound, version 16, comprising 82 numbered statements [1]. It includes, besides the residual results of Sections 2–3, the identification of a 14-dimensional level-one parallel-weight-two cuspidal Hilbert newspace $V_{35}$ over $\mathbb{Q}(\sqrt{35})$ with narrow class number 4, decomposing as $2+2+2+8$ across the four narrow classes [1]. These are the established mathematical anchors of the extension; everything else in this paper is built on them or explicitly marked as interpretive.

## 7. Relation to classical general relativity

An extension of general relativity must reduce to it where it has been tested. In the present proposal the reduction is built into the form of the regulator. For radii large compared with the floor, $3^{-539}$ is negligible beside any physically resolved length, and the regulated $g_{rr}$ is meant to coincide with the Schwarzschild coefficient in the exterior. The core term of the model is supported only where $|r|_3<3^{-539}$, so that outside the core the classical Einstein equations hold unmodified [2]. The core field equation proposed in [2],
$$G_{\mu\nu}+\Lambda_3\,g_{\mu\nu}-\tilde\gamma_{\mu\nu}=8\pi T^{(3)}_{\mu\nu},$$
is of Einstein form with additional terms confined to the core, and with a conservation law for $T^{(3)}_{\mu\nu}$ claimed when the residual singlet is fixed. At maximal compression the proposal assigns $P_3=-\rho_3$, a de Sitter–like equation of state, placing it in the family of regular black-hole interiors with de Sitter cores.

What remains interpretive is the bridge between the two regimes. A complete extension would need: an explicit identification map from 3-adic valuations to Archimedean geometry; a derivation of junction conditions (vanishing jump in extrinsic curvature) at the core boundary from the core equations rather than by tuning; recovery of the Bekenstein–Hawking entropy $S=A/4G$ and the Hawking spectrum; and a definition of the core mass that is not inserted by hand. Each of these is open. The structure of the proposal — exact general relativity outside, an arithmetic core inside, a measure-theoretic timescale on the boundary — is coherent as a programme, but the residual ternary theorems do not by themselves establish it.

## 8. Empirical status

We distinguish two kinds of support. A mathematical proof establishes a statement from definitions. Agreement between a model's prediction and measured data is empirical evidence for the model; it can strengthen or weaken confidence in a physical reading, but it never substitutes for proof and never upgrades an interpretive statement into a theorem. We label each data comparison with one of five evidence grades: E-MATCH (prediction agrees with measurement within stated tolerance, with no parameter tuned to that data), E-PARTIAL (agreement in some observables or within a loose tolerance), E-TENSION (disagreement), E-UNTESTED (no quantitative comparison yet performed), and E-FIT (agreement obtained by tuning a parameter to the same data, which is weak evidence). A complete comparison records the data set, predicted and measured values, tolerance, and the number of free parameters.

The data sets identified as contact surfaces for the extension are:

1. **Baryon acoustic oscillation and dark-energy measurements from the Dark Energy Spectroscopic Instrument, Data Release 2** [9]. The adelic and residual sectors are proposed to bear on the effective dark-energy density and equation of state $w$. A $\chi^2$ comparison has been designed but the decisive computation has not been run, and the choice of data subset, number of points and free parameters is not yet fixed. **Status: E-UNTESTED.**

2. **Collider data from the ATLAS experiment at the Large Hadron Collider** [10]. The nine-sector residual packaging and the 3-adic sheet picture are proposed to inform hadronic and heavy-baryon observables, including candidate states quoted near 6.32 GeV and 6.84 GeV. No mass formula producing these values from the residual algebra exists, and a dimensionless numerical coincidence does not fix a GeV scale. **Status: E-UNTESTED.**

3. **Black-hole and strong-field observables** generally. The regulated $g_{rr}$ and bounded Kretschmann invariant of Section 4 make no quantitative prediction yet for horizon-scale imaging, ringdown, or evaporation, because the exterior matching and the core mass are not determined. The scale $\Lambda_0\approx0.7858$ used in one matching attempt is not derived; if it were adjusted to reproduce an observation, the result would be graded E-FIT. **Status: E-UNTESTED.**

No comparison has reached E-MATCH, E-PARTIAL, or E-TENSION, and we report none. The named data sets are the intended empirical tests of the proposal. Results, when obtained, will be reported with the grade appropriate to them, and will remain empirical evidence regardless of grade.

## 9. Conclusions

We have presented the S²-11DM²ET-X model as an extension of general relativity organised around one discipline: the separation of a residual count from a resonant schedule, and of established mathematics from physical proposal. The established side consists of the residual ternary algebra of [1] — the packaging $B'=539$, the cohomology $H^2(F)\cong\mathbb{Q}\cdot[s_{\alpha\delta}]$, the rank-one classifier $D_1$, the reading of $T_3=539$ as a capacity rather than a clock, the frozen canonical $T_3$ profile — together with the Haar Euler-factor identity on $\mathbb{Z}_3^4$, and a filtered inventory in which 45 of 72 claims are classed as provable candidates by primary (first-listed) tag [12]. The proposal side consists of the 3-adic regulation of $g_{rr}$, the bounded replacement of the Kretschmann invariant through $M_{35}$, the reading of the horizon as the boundary of $T_3$ dynamics, and a de Sitter–like core matched to an unmodified exterior.

The proposal resolves the classical singularity by construction, but the steps that would make the resolution a derivation — the valuation-to-geometry map, the junction conditions, entropy recovery, and a derived core mass — remain open. Its empirical tests are identified in cosmological and collider data and have not yet been carried out. The natural next steps are to define the missing objects precisely enough to state them as theorems, and to run the designed comparisons with their free parameters declared in advance.

## References

[1] A. Hampton, *Residual Ternary Algebra: Foundation Bound*, version 16, 539 Labs (2026). 82 numbered statements; includes the residual packaging, the cohomology of the residual form complex, the static classifier $D_1$ and budget $S_{\mathrm{eff}}$, the residual–resonant separation theorem, the newspace $V_{35}$, and the filtered inventory of provable candidates.

[2] A. Hampton / 539 Labs, "Cosmic Journey" thread post on the 3-adic black-hole core, X (5 November 2026). https://x.com/539Labs/status/2118167783133286898

[3] K. Schwarzschild, "Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie," *Sitzungsber. Preuss. Akad. Wiss.* (1916) 189–196.

[4] S. W. Hawking and G. F. R. Ellis, *The Large Scale Structure of Space-Time*, Cambridge University Press (1973).

[5] A. Hampton, *Residual Ternary Algebra and Bridge Series C: The Residual–Resonant Frame for the S²-11DM²ET-X Model*, 539 Labs (3 November 2026).

[6] 539 Labs, *HQH-539 Profile Freeze, Option A: Canonical $T_3$ Reference Specification* (2026).

[7] A. Hampton, *The Static Classifier $D_1$ and Budget $S_{\mathrm{eff}}$: Layer-Two Lock for $T_3$*, 539 Labs (3 November 2026).

[8] J. T. Tate, "Fourier analysis in number fields and Hecke's zeta-functions," in J. W. S. Cassels and A. Fröhlich (eds.), *Algebraic Number Theory*, Academic Press (1967) 305–347.

[9] DESI Collaboration, Data Release 2: baryon acoustic oscillation and cosmological constraints, Dark Energy Spectroscopic Instrument (2025).

[10] ATLAS Collaboration, public physics results and data, ATLAS experiment, CERN Large Hadron Collider.

[12] PP audit, *FINDINGS_PP_SOFTSF_AUDIT_LOCAL_FILTER_AMEND_c5755654_2026-11-05.md*, §3 (primary-tag and all-tag tallies), SHA256 4e1cf03555cc495382e949c438a54edc768a6cef8d8cb1e80bdd4f1b26410aea; /workspace/quantum-comp/reports/FINDINGS_PP_SOFTSF_AUDIT_LOCAL_FILTER_AMEND_c5755654_2026-11-05.md. Post-update comparison: ABSORB *FINDINGS_LOCAL_SOFTSF_AMEND_ABSORB_PP_FLAG_FILTER_X_DENSE_2026-11-05.md*, SHA256 0a4ddb32f7f891b93c0db120de21638d3e5a30543eca0a9f59116866751ca570, read together with the PP tally (ABSORB alone contains no 45 tally).
