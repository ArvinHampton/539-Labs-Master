# Phase 0 — Definition of the physical trajectory space \(\mathcal{C}\)

**Purpose.** Make the HQCC claim “exactly 539 homotopy classes” a **precise mathematical target** so Bott/\(KO\) linking has something well-posed to map into or out of.

**Rules.**  
- No Bott/\(KO\) used in the definition of \(\mathcal{C}\).  
- No smuggling: counting formulae may use only \(\{3,e,243,4880,9,61,18,\ldots\}\) as already fixed model integers — the numeral **539 may appear only as a claimed equality to be proved**, not as an input.  
- Category B: definition + claimed count; proof of \(|\pi_0(\mathcal{C})|=539\) remains open unless a combinatorial identity is completed.

---

## 0. Fixed combinatorial data (inputs only)

\[
\begin{aligned}
g &= 3 && \text{(generations / Axiom 0)}\\
N_{\mathrm{tow}} &= 3^5 = 243 && \text{(KK towers)}\\
N_{\mathrm{flux}} &= \lfloor e^3\cdot 3^5\rfloor = 4880 && \text{(flux budget)}\\
Q &= n \bmod 9 && \text{(charge)}\\
n_\star &= 1 && \text{(declared minimal-action sink)}\\
W &= 18 && \text{(holographic coherent window length; optional stratum)}\\
P &= 61 && \text{(puncture / screen digit count; optional)}\\
T^\sharp &= \text{min-defect completed ternary map (ACE resolution)}.
\end{aligned}
\]

---

## 1. Discrete path category of the completed map

### 1.1 Objects and arrows

**Definition (state space).**  
\[
\mathcal{S} := \mathbb{N}_{\ge 1}.
\]

**Definition (one-step relation).**  
\[
n \xrightarrow{\,T^\sharp\,} T^\sharp(n).
\]

**Definition (finite paths).**  
A **path of length \(L\)** is a sequence
\[
\gamma = (n_0,n_1,\ldots,n_L)
\quad\text{with}\quad
n_{t+1}=T^\sharp(n_t)\ \text{for all }t.
\]
Write \(\mathrm{Path}_L(\mathcal{S})\) for the set of all such paths, and
\[
\mathrm{Path}(\mathcal{S}) := \bigsqcup_{L\ge 0} \mathrm{Path}_L(\mathcal{S}).
\]

### 1.2 Charge-preserving paths

**Definition (path charge).**  
For \(\gamma=(n_0,\ldots,n_L)\),
\[
Q(\gamma) := Q(n_0) = n_0 \bmod 9
\]
(the model’s initial-charge label; along \(T^\sharp\), exact preservation holds off \(\mathcal{I}\), min-defect otherwise).

**Definition (charge sector).**  
\[
\mathrm{Path}^{(q)} := \{\gamma\in\mathrm{Path}(\mathcal{S}): Q(\gamma)=q\},\qquad q\in\{0,1,\ldots,8\}.
\]

---

## 2. Physical subspace (three equivalent packages)

The literature speaks of a “charge-preserving physical subspace.” Phase 0 fixes **three concrete packages**; the Bott link may target any one, but **must name which**.

### Package C1 — Seeded flux paths of combinatorial length (forced-length model)

**Tower seed multiset (democratic partition of 4880).**  
Published tallies (model): among 243 towers, multiplicities of seed types **20** and **21** (exact partition as in HQCC/negPBH notes). Write
\[
\Sigma_{\mathrm{seed}} \subset \mathcal{S}
\]
for the finite multiset of initial integers obtained from that partition (cardinality 243 if one seed per tower, or larger if multiple seeds per tower — **declare the multiset explicitly in any computation**).

**Definition (\(\mathcal{C}_1\)).**  
\[
\mathcal{C}_1
:=
\bigl\{
\gamma\in\mathrm{Path}_L(\mathcal{S})
:
n_0\in\Sigma_{\mathrm{seed}},\ 
L = L_\star,\ 
n_L = 1
\bigr\}
\]
where \(L_\star\) is **not** inserted by hand as 539; it is defined by the **first** of the following that is adopted as the official combinatorial law:

| Option | Definition of \(L_\star\) (no numeral 539 on RHS) | Claim |
|--------|--------------------------------------------------|--------|
| **C1a** | \(L_\star := L_{\mathrm{win}}+L_{\mathrm{mst}}+L_{\mathrm{tow}}\) with \(L_{\mathrm{win}}:=W=18\), \(L_{\mathrm{mst}}:=1\), \(L_{\mathrm{tow}}:=\Psi_{\mathrm{tow}}(20,21,243)\) | Need \(\Psi_{\mathrm{tow}}=520\) **derived** |
| **C1b** | \(L_\star := \min\{L: T^{\sharp L}(n_0)=1\}\) (natural hitting time of the sink) | Then \(|\mathcal{C}_1|\) is a set of short paths; **not** expected to give 539 |
| **C1c** | \(L_\star := \lceil \ln N_{\mathrm{flux}} / \chi_{\min}\rceil = 14\) (ACE e-fold) | Matches No-Go short depth; **≠ 539** |

**HQCC long-structure claim (Category B)** corresponds to making **C1a** precise: derive
\[
\Psi_{\mathrm{tow}}(20,21,243)=520
\]
from tower combinatorics alone (e.g. \(223\times 21 + 20\times 20 = 4683+400=5083\) is **not** 520 — so the published 520 must be a **different** functional; it must be written down without reverse-engineering from \(539-19\)).

**Status of C1a:** \(\Psi_{\mathrm{tow}}\) is **not yet a clean closed form** from 20, 21, 243 only. Phase 0 **flags** this as the first gap in the combinatorial package.

### Package C2 — Path components of a graph (homotopy = path components)

**Definition (physical graph).**  
Vertices: \(\mathcal{S}_{\mathrm{phys}} := \{n\in\mathcal{S}: n\le N_{\mathrm{cut}}\}\cup\{1\}\) with a cutoff \(N_{\mathrm{cut}}\) fixed by flux data only, e.g.
\[
N_{\mathrm{cut}} := 3^{\lceil \log_3 N_{\mathrm{flux}}\rceil + c}
\]
for a declared small constant \(c\) (e.g. \(c=2\)), **not** using 539.

Edges: \(n\to T^\sharp(n)\) when both vertices lie in \(\mathcal{S}_{\mathrm{phys}}\).

**Definition (\(\mathcal{C}_2\)).**  
\[
\mathcal{C}_2 := \pi_0\bigl(\mathrm{Geom}(G_{\mathrm{phys}})\bigr)
\]
i.e. path-components of the geometric realization of the directed graph \(G_{\mathrm{phys}}\) (or weakly connected components of the underlying undirected graph, **declare which**).

**Claim (Category B, to prove or refute):**  
\[
|\mathcal{C}_2| = 539.
\]
This is a **finite graph computation** once \(N_{\mathrm{cut}}\) and the undirected/directed convention are fixed — an executable test.

### Package C3 — Residue-word language (finite combinatorial model)

**Definition (alphabet).**  
\[
\mathcal{A} := \{0,1,2\}\times\{0,1,2,\varnothing\}
\]
encoding (residue mod 3, correction level \(k\) or \(\varnothing\) if not branch-2).

**Definition (physical words).**  
A word \(w\in\mathcal{A}^{L}\) is **physical** if it arises as the event sequence of some path of \(T^\sharp\) from a seed in \(\Sigma_{\mathrm{seed}}\) that reaches \(n=1\) in exactly \(L\) steps (or at most \(L\), declare).

**Definition (\(\mathcal{C}_3\)).**  
\[
\mathcal{C}_3 := \mathrm{PhysicalWords}\,/\!\sim
\]
where \(\sim\) is a declared equivalence (e.g. free homotopy in the residue graph, or cyclic conjugation, or reduction mod Bott-shift once Bott is linked — **not** in Phase 0).

**Claim (Category B):** after a natural \(\sim\) **not** using Bott,
\[
|\mathcal{C}_3|=539.
\]

---

## 3. The precise HQCC counting claim (Phase 0 target)

**Claim H0 (to be proved in Category B, independent of Bott).**  
There exists a package \(\mathcal{C}\in\{\mathcal{C}_1,\mathcal{C}_2,\mathcal{C}_3\}\) (with all options in its definition fixed using only the input data of §0) such that
\[
\boxed{|\pi_0(\mathcal{C})|\ \text{or}\ |\mathcal{C}|\ =\ 539}
\]
and each class corresponds one-to-one with a resonant trajectory of the constrained dynamics.

**Recommended primary target for computation:** **\(\mathcal{C}_2\)** (finite graph components) with explicit \(N_{\mathrm{cut}}\) and undirected components — fully checkable.

**Recommended primary target for theory:** **\(\mathcal{C}_1\)** once \(\Psi_{\mathrm{tow}}\) is written without \(539-19\).

---

## 4. Gaps exposed by Phase 0 (must close before Bott link)

| Gap | Description | Blocking? |
|-----|-------------|-----------|
| **G0.1** | \(\Psi_{\mathrm{tow}}(20,21,243)=520\) not yet a derived identity from those integers alone | Blocks clean C1a |
| **G0.2** | Multiset \(\Sigma_{\mathrm{seed}}\) not uniquely standardized (one seed per tower vs 20/21 types) | Blocks unique \(|\mathcal{C}_1|\) |
| **G0.3** | “Cobordism class” in prose not yet a bordism group element | Blocks Architecture A until rephrased as \(\Omega_*^{\mathrm{Spin}}(X)\) or \(\pi_0(\mathcal{C})\) |
| **G0.4** | Natural hitting time (C1b) does **not** reproduce 539 | Confirms 539 ≠ free \(T^\sharp\) dynamics |

---

## 5. Interface to Bott (only after H0 is well-posed)

Once \(\mathcal{C}\) is fixed:

\[
\begin{CD}
\mathcal{C} @>{f}>> B\mathrm{Spin}\ \text{or}\ BO \\
@VVV @VV{\mathrm{ABS}/KO}V \\
\{\text{539 classes}\} @. KO_*(\mathrm{pt})\ \text{or}\ KO_*(X)
\end{CD}
\]

Bott acts on the right. The link asks for a factorization of the 539-fold set through a Bott-periodic invariant with arithmetic
\[
539 = 8\cdot 67 + 3.
\]

Phase 0 **stops** at defining \(\mathcal{C}\) and stating H0; it does **not** construct \(f\).

---

## 6. Executable checklist

- [x] Define path space and \(T^\sharp\) edges  
- [x] Define packages C1–C3  
- [x] State H0 without Bott  
- [ ] Fix \(\Sigma_{\mathrm{seed}}\) uniquely from 4880 and 243  
- [ ] Derive or abandon \(\Psi_{\mathrm{tow}}=520\)  
- [ ] Compute \(|\mathcal{C}_2|\) for a declared \(N_{\mathrm{cut}}\) (script)  
- [ ] Only then: Architecture A classifying map  

**Script:** `scripts/phase0_C2_components.py` (finite-graph probe).

---

## 7. Bottom line

> Phase 0 replaces the vague phrase “cobordism class contains 539 homotopy classes” with **named spaces** \(\mathcal{C}_1,\mathcal{C}_2,\mathcal{C}_3\) and a sharp claim **H0**.  
> The hardest combinatorial gap is deriving **520** (tower segment) without subtracting from 539.  
> Bott linking is **out of scope until** H0’s space is fixed and the count is either proved or reformulated.
