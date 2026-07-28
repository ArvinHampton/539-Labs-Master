# Wilson loops, modular projections, and the No-Go

## 1. Wilson loops and the area law (standard meaning)

Wilson loops are the fundamental **gauge-invariant** observables of **lattice gauge theory**.

On a discrete lattice one assigns a **group element** (the parallel transporter) to every directed link. The Wilson loop for a closed path \(C\) is the trace of the ordered product of those group elements around the path:

\[
W(C)
= \operatorname{Tr}\,
\mathcal{P}
\prod_{\ell\in C} U_\ell,
\qquad
U_\ell \in G
\quad\text{(gauge group)}.
\]

### Area law and string tension (genuine)

In lattice gauge theory the **area law** is the statement that the expectation value of a Wilson loop falls **exponentially with the area** of the surface it encloses:

\[
\langle W(C)\rangle \sim e^{-\sigma\,\mathrm{Area}(C)}.
\]

The coefficient \(\sigma\) is the **string tension**. Physically:

- a **non-zero string tension** means the energy of a pair of static sources grows **linearly** with their separation;
- \(\sigma\) is the **energy per unit length** stored in the confining flux tube;
- non-zero \(\sigma\) is the standard diagnostic of **confinement** of static sources.

| Law | Signal |
|-----|--------|
| **Area law** | \(\langle W\rangle \sim e^{-\sigma\,\mathrm{Area}(C)}\), \(\sigma>0\) — confinement |
| **Perimeter law** | \(\langle W\rangle \sim e^{-\mu\,\mathrm{Perimeter}(C)}\) — deconfinement / screening |

**No genuine Wilson loop** exists inside the resonant dynamics of the present model, so a **genuine area law** and a **genuine string tension** are likewise **absent** (no gauge flux tubes are defined).

---

## 2. Status in the present model

In the resonant dynamics of S²-11DM²ET-X / HQCC:

- **No** continuum gauge field is defined.  
- **No** discrete lattice gauge field is defined.  
- Therefore **no genuine Wilson loop exists**.

Modular projections act on the **integer state** of the ternary map \(T_3\) / \(T^\sharp\). They restore a residue condition (\(Q=n\bmod 9\)) or a phase tolerance; they do **not** assign group-valued transporters to the edges of any lattice.

**Consequently the sequences of projections cannot be assembled into a Wilson loop in the ordinary sense.**

---

## 3. Statistical surrogate (area-law / perimeter-law **analogues**)

What **can** be examined is a purely **statistical** surrogate.

Along a long constrained trajectory one may:

1. form **closed sequences** of residue transitions or of modular-projection events;
2. record the **frequency** (statistical weight) of those sequences as a function of the **number of steps they enclose**.

| If frequencies decay… | Name | Meaning (descriptive only) |
|----------------------|------|----------------------------|
| exponentially with the **enclosed step-count** (discrete “area”) | **Area-law analogue** | large closed patterns of projections / residue changes are statistically suppressed |
| only with the **length of the boundary sequence** (discrete “perimeter”) | **Perimeter-law analogue** | suppression tracks boundary length, not enclosed steps |

### Surrogate string tension

If frequencies of closed sequences decay as \(\sim e^{-\sigma_{\mathrm{surr}} A}\) with enclosed step-count \(A\), the decay constant \(\sigma_{\mathrm{surr}}\) may be called a **surrogate string tension**.

| It measures | It does **not** mean |
|-------------|----------------------|
| How strongly large closed patterns of projections/residue changes are **statistically suppressed** | Energy per unit length of a confining **gauge** flux tube |
| A descriptive statistic of the **constrained** dynamics | Confinement of static gauge sources |
| Optional empirical fit under the locked protocol | Generation of **539**, **539.9**, or the long trajectories themselves |

### What a positive area-law analogue would **and would not** mean

| Would indicate | Would **not** mean |
|----------------|--------------------|
| Large closed projection/residue patterns are rare (exponentially in enclosed steps) | Confinement of a **gauge charge** |
| \(\sigma_{\mathrm{surr}}>0\) as a decay constant of pattern frequencies | Genuine string tension of lattice gauge theory |
| Optional empirical signature under the locked protocol | Generation of the integer **539** or period **539.9** |

---

## 4. Downstream of the resonant apparatus, not a source of it

The long trajectories on which surrogate loops are measured are themselves produced only after:

- a **fixed iteration count**, and  
- a **phase-locking period**  

have already been imposed.

Any area-law (or perimeter-law) behaviour extracted from them is therefore a **consequence of those external constraints**, not an **independent dynamical origin** of the constraints.

**In short:** an area-law analogue is a possible **statistical signature of the constrained system** and may be looked for under the locked protocol. It remains a **downstream consequence of the resonant apparatus**, not a **source** of that apparatus.

It **cannot** serve as an independent source of the integer **539** or of the period **539.9**.

---

## 5. ACE and No-Go unchanged

Canonical No-Go: `NoGo_Theorem_Canonical.md`

The a priori charge-correcting estimate for the completed map \(T^\sharp\) continues to yield a **short mean contraction depth of order \(N_\star = 14\)**.

The No-Go Theorem continues to place the **long resonant structure outside** the reach of residue structure, tower topology, and flux democracy.

| Derived without 539 | Not derived by area-law analogues |
|---------------------|-----------------------------------|
| \(\mathbb{E}_\pi[\chi]\approx -0.6365\) | Genuine Wilson loops / string tension |
| \(\lambda_{\mathrm{mean}}\approx 0.529\) | Period 539.9 |
| \(N_\star=14\) | Unique \(w_j=539+61j\) |

An empirical tally of surrogate-loop weights may **characterise** how modular projections organise themselves along **forced** trajectories; it **cannot** lift the No-Go or convert the resonant period into a quantity **derived from the local map alone**.

---

## 6. Empirical study (permitted; characterisation only)

| Allowed | Not allowed as a conclusion |
|---------|------------------------------|
| Evolve with projections active (\(T^\sharp\)) | “Area law ⇒ confinement of gauge charge” |
| Tally closed residue / projection sequences | “Area law ⇒ 539 or 539.9” |
| Fit weights vs enclosed steps \(A\) and boundary length \(L\) | “Surrogate loops lift the No-Go” |
| Report area-law vs perimeter-law **analogues** | Treating analogue \(\sigma\) as lattice string tension |

Optional future script: `scripts/surrogate_loop_stats.py`  
— closed walks on residue graph; weight vs enclosed step-count / boundary length; **no** 539.9 in the definition of loops.

---

## 7. Bottom line

> **Genuine string tension / area law:** absent (no Wilson loops, no gauge flux tubes).  
> **Surrogate string tension** \(\sigma_{\mathrm{surr}}\): optional decay constant of closed projection/residue pattern frequencies vs enclosed steps — a **descriptive statistic**, not confining energy per unit length.  
> **Role:** **effect** of the resonant constraints (fixed count + phase-lock), **not a cause** of them; does not generate 539 or 539.9.  
> **QCD confinement** (\(\sim 1\,\mathrm{GeV/fm}\), lattice area law, Millennium-level analytic gap): a fact of **4d gauge theory**, **not** realized in the ternary map and **not** a derivation of 539 / 539.9 here — see `QCD_Confinement_vs_Resonant_Dynamics.md`.  
> **ACE / No-Go:** short depth \(\sim 14\) from \(T^\sharp\); long resonance still outside residue + towers + democracy.  
> Empirical estimate of \(\sigma_{\mathrm{surr}}\) may characterise forced trajectories; it cannot lift the No-Go.
