# RH pure Category A — L1 phase functional and target lemma

**Status:** RH **open**; workstream **active** (not frozen).  
**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** **A only** in this note — no model constants.  
**Forbidden in theorems:** \(G_4\), \(\mu\), \(E_{\mathrm{leak}}\), \(539.9\,\mathrm{s}\), phonon / brane language, residual packaging integers as zeta lemmas.

**Companions:** `RH_Debt_Argument_Status.md` (programme stance), `CLAIM_TABLE_RH_Debt.md`,  
`RH_Target_Lemma_Sketch_Literature_L5.md` (lift sketch, literature, L5 plan),  
`RH_Akatsuka_Theorem_Extract.md` (exact [Aka17] statements vs (★)),  
`RH_M1_Explicit_Formula_Remainder.md` (M1: IvM remainder \(R_{\mathrm{IvM}}\), \(\mathcal{R}_x^{\mathrm{EP}}\)).

---

## 0. Stance

RH is **not proved**. The model debit bound is **set aside**.  
The only path that can close RH here is a **pure growth theorem** for a rigorously defined phase of the partial Euler product. That is this workstream.

---

## 1. L1 — Definition of the phase functional (no model constants)

Fix \(s=\sigma+it\) with \(0<\sigma<1\) and \(t\neq 0\). Let
\[
P_x(s)=\prod_{p\le x}(1-p^{-s})^{-1}.
\]
This product is never zero for finite \(x\).

### 1.1 Continuous argument of partial products

Define the continuous argument along the ray of partial products by starting from
\[
\theta_2(\sigma,t)=\arg P_2(\sigma+it)
\]
(principal value at the first prime, or the continuous branch with \(\theta_2=0\) after fixing a global phase convention once and for all) and, at each successive prime \(p\), adding the continuous increment of
\[
\arg(1-p^{-s})^{-1}
=
-\arg(1-p^{-s})
\]
along the path of partial products ordered by increasing primes. Call the resulting continuous function
\[
\theta_x(\sigma,t)=\arg P_x(\sigma+it).
\]

### 1.2 Smoothed version \(A_X\)

Let \(\phi\) be a fixed non-negative smooth test function supported on \([1,2]\) with
\[
\int_1^2\phi(u)\,du=1.
\]
Set
\[
\boxed{
A_X(\sigma,t)
=
\int_1^\infty
\theta_{e^u}(\sigma,t)\,
\phi\Bigl(\frac{u}{\log X}\Bigr)
\frac{du}{\log X}
}
\]
for \(X>e\) (so that the support of the weight meets the integration range in the intended way; equivalently integrate \(u\) over \([\log X,\,2\log X]\)).

### 1.3 Well-definedness (L1 content)

| Property | Status |
|----------|--------|
| \(P_x(s)\neq 0\) for all finite \(x\) | Yes |
| Continuous branch \(\theta_x\) along primes | Defined by successive continuous increments |
| \(A_X\) well-defined | Yes — finite smooth average of \(\theta_{e^u}\) |
| Continuous in \((\sigma,t)\) off partial-product zeros | Vacuous zeros of \(P_x\); \(A_X\) continuous on \(0<\sigma<1\), \(t\neq 0\) |
| Model constants in definition | **None** |

**L1 (definition) is formalized.** Analytic estimates of \(A_X\) remain open (L2–L4).

---

## 2. Conjectures A and B (stated for \(A_X\))

### Conjecture A (bounded phase on the critical line)

There exist absolute constants \(C,c>0\) such that for all \(|t|\) large and all \(X\) in a suitable range relative to \(|t|\) (e.g. \(\exp(c\log|t|)\le X\le |t|^A\) for fixed \(A\), or the range needed to couple to zero-density technology),
\[
A_X\bigl(\tfrac12,t\bigr)
=
O\bigl(\log\log|t|\bigr),
\]
with the implied constant absolute (or depending only on \(\phi\)).

### Conjecture B (growth at off-line zeros)

If \(\zeta(\sigma+it)=0\) and \(\sigma\neq 1/2\), then
\[
\limsup_{X\to\infty}
\frac{\bigl|A_X(\sigma,t)\bigr|}{\log\log X}
=\infty.
\]
(A quantitative form with a factor \(\gg m|\sigma-1/2|\) or \(\gg m\) is preferred when multiplicity \(m\) is available.)

No \(G_4\), \(\mu\), \(E_{\mathrm{leak}}\), or \(539.9\) appears in the definition or the conjectures.

---

## 3. Target lemma (smallest useful intermediate)

Let
\[
Y
=
\sup\{\operatorname{Re}\rho:\zeta(\rho)=0\}.
\]

**Lemma (target).**  
Assume \(Y>1/2\) and let \(\rho=\beta+i\gamma\) be a zero with \(\beta=Y\) and multiplicity \(m\ge 1\). Then there exists a sequence \(X_n\to\infty\) such that
\[
\bigl|A_{X_n}(\beta,\gamma)\bigr|
\ge
c\,m\log\log X_n
\]
for an absolute constant \(c>0\) (depending only on \(\phi\)).

### Why this lemma is enough for the RH strategy

1. The target lemma \(\Rightarrow\) Conjecture B for zeros that realize the abscissa \(Y\).  
2. Functional equation \(\Rightarrow\) zeros symmetric about \(\operatorname{Re}s=1/2\).  
3. Classical zero-free regions near \(\operatorname{Re}s=1\) constrain how large \(Y\) can be.  
4. If every zero with \(\operatorname{Re}=Y>1/2\) forces unbounded growth of \(A_X\), and if that growth is incompatible with known structure of \(\log P_x\) / explicit formulae unless \(Y=1/2\), one obtains \(Y=1/2\), i.e. RH.

**Precise logical finish** still requires packaging (2)–(4) carefully; the **load-bearing analytic step** is the target lemma (or Conjecture B at maximal abscissa zeros).

**Status of the target lemma:** **open** — to be proved from the explicit formula and/or Akatsuka-type expansions, with **no** model constants.

---

## 4. Literature map (usable expansions)

| Source | Usable content | Relation to this note |
|--------|----------------|------------------------|
| **Conrad (2005)** | Controlled asymptotics of partial Euler products on the critical line of the form \(C/(\log x)^r\) imply RH for a wide class of \(L\)-functions; such product asymptotics are, in a precise sense, **stronger than RH** | Motivates Conjecture A–type control; shows product asymptotics are a hard but powerful route |
| **Goldfeld** (related product / RH implications) | Same circle: product asymptotics \(\Rightarrow\) RH for broad \(L\)-function classes | Aligns “bounded / controlled product on the line” with RH |
| **Akatsuka (2017)** | Pointwise asymptotics of the partial Euler product of \(\zeta\) on the right half of the critical strip; if \(Y=\sup\operatorname{Re}\rho\) and \(Y\le\sigma_0<1\), a zero of multiplicity \(m\) at \(s_0=\sigma_0+it_0\) produces an explicit \(m\log\log x\) term in the expansion of \(\log\) of the partial product (or associated Dirichlet series for \(\log\zeta\)) | **Primary classical mechanism** for off-line zero \(\Rightarrow\) extra \(\log\log\) growth — input for the target lemma |
| **LeClair et al.** (random-walk / prime trigonometric sums) | Heuristic \(\sqrt N\)-type growth for certain series; suggests Euler product meaningful for \(\sigma>1/2\) and, with FE, zeros on the line — under an **unproved** random-walk conjecture | Heuristic only until converted into estimates for \(\theta_x\) or \(A_X\) |
| Classical \(S(t)=\frac1\pi\arg\zeta(1/2+it)\) | Average behaviour known; pointwise off-line at a zero is hard | Related continuous-argument tradition; \(A_X\) is partial-product based |

**Missing conversion step:** turn Akatsuka-type \(m\log\log x\) expansions into a clean lower bound for the **continuous argument** \(A_X\) (or \(\theta_x\)) strong enough for the target lemma, free of circular assumptions (L4).

---

## 5. Active work list (pure Cat A)

| ID | Task | Status |
|----|------|--------|
| **L1** | Definition of \(\theta_x\), \(A_X\) | **Formalized** (this note) |
| **M1** | \(\log\zeta=\log P_x+\mathcal{R}_x^{\mathrm{EP}}\) via \(R_{\mathrm{IvM}}\) | **Identity formalized**; bounds open |
| **Target lemma** | \(\lvert A_{X_n}(Y,\gamma)\rvert\ge c\,m\log\log X_n\) | **Open — primary** |
| **L2** | Bounds for \(A_X(1/2,t)\) (Conjecture A range) | Open |
| **L3** | General off-line lower bound (Conjecture B) | Open; target lemma is the sharp intermediate |
| **L4** | Non-circular hypotheses (no presupposed Lyapunov / mean) | Open |
| **L5** | Numerics: \(\theta_x\) or \(A_X\) at first on-line zeros vs artificial off-line points | **Executed** — `scripts/rh_L5_phase_diagnostic.py` (no RH claim) |

---

## 6. Firewall (unchanged)

| Material | Role |
|----------|------|
| Resonant Algebra | Quarantined; finished; **unrelated** |
| Residual architecture A0–A5+ | **Unrelated** as RH lemmas |
| Debt / \(E_{\mathrm{leak}}\) / \(\mu\) / 539.9 | Cat B motivation only; **never** inside theorem statements |
| DQPT experiment | Finite dynamical check only |

---

## 7. Optional L5 diagnostic plan (not a proof)

1. Implement continuous \(\theta_x(1/2,t)\) along primes for the first \(N\) ordinates of known critical zeros.  
2. Compute smoothed \(A_X(1/2,t)\) for a grid of \(X\).  
3. At artificial points \(\sigma\neq 1/2\) where \(\lvert\zeta(\sigma+it)\rvert\) is small but non-zero, compare growth of \(\lvert A_X\rvert\).  
4. Report only diagnostic plots/tables; **no** RH claim from finite \(X\).

---

## One-liner

**RH remains open; the active pure-math task is a lower bound on the smoothed continuous argument \(A_X\) of the partial Euler product at an off-line zero of maximal real part, built from the explicit formula or Akatsuka-type expansions, with no model constants.**

*Per aspera ad astra.*
