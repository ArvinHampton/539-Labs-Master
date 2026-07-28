# Refined seed-orbit package \(\mathcal{C}_{\mathrm{seed}}\)

**Purpose.** Redefine the physical class space as basins (terminal orbits) of the **physical seeds** under \(T^\sharp\), without inserting 539 by hand. Then count basins computationally and compare to 539 **post-hoc**.

**Bott / \(B\mathrm{Spin}\):** only legitimate after a successful count (or a clear reformulation).

---

## 1. Physical seeds from flux democracy (no 539)

### 1.1 Tower flux assignment

\[
N_{\mathrm{tow}} = 243,\qquad N_{\mathrm{flux}} = 4880.
\]

\[
243\cdot 20 = 4860,\qquad 4880-4860 = 20.
\]

So exactly **20** towers carry flux **21** and **223** towers carry flux **20**:

\[
f_\tau =
\begin{cases}
21 & 0 \le \tau < 20,\\
20 & 20 \le \tau < 243.
\end{cases}
\]

### 1.2 Seed packages

**Package S243 — one seed per tower** (literally “243 physical seeds”):

\[
s_\tau := f_\tau \cdot 243 + \tau,
\qquad \tau = 0,\ldots,242.
\]

All \(s_\tau\) distinct; built only from \((f_\tau,\tau,243)\).

**Cardinality bound:** number of basins among these seeds is \(\le 243 < 539\).  
So **S243 cannot realize H0 as a raw basin count of 539**. It is still run as a control.

**Package S4880 — one seed per flux quantum** (democratic split of 4880):

\[
|\Sigma|
= \sum_{\tau=0}^{242} f_\tau
= 20\cdot 21 + 223\cdot 20
= 420 + 4460
= 4880.
\]

Seeds labeled \((\tau,j)\) with \(0\le j < f_\tau\):

\[
s_{\tau,j}
:= (f_\tau \cdot N_{\mathrm{tow}} + \tau)\cdot 64 + j + 1.
\]

(The factor 64 > max \(f_\tau\) ensures uniqueness; only uses tower data.)

**Note:** An older prose tally “223×21 + 20×20 = 5083 independent zero-mode seeds” is a **different** multiset (swapped 20/21 roles). The flux-consistent multiset is **4880** seeds.  
**Cardinality bound:** basins \(\le 4880\), so **539 is numerically possible**.

---

## 2. Dynamics and basins (no 539)

**Map:** \(T^\sharp\) (min-defect completion; ACE resolution).

**Forward orbit** of seed \(s\):

\[
s,\ T^\sharp(s),\ T^{\sharp 2}(s),\ \ldots
\]

**Terminal cycle:** first cycle entered under iteration (detected by a seen-set; includes fixed points \(\{1\}\), \(\{0\}\), and longer cycles if any).

**Basin equivalence:** seeds \(s\sim s'\) iff they share the same terminal cycle (same attractor). Equivalently, their forward orbits eventually merge.

**Definition (\(\mathcal{C}_{\mathrm{seed}}\))**

\[
\mathcal{C}_{\mathrm{seed}}(\Sigma)
:=
\bigl\{ \text{terminal cycles reached by some } s\in\Sigma \bigr\}
=
\Sigma\ /\ \sim
\quad\text{(set of basins)}.
\]

\[
N_{\mathrm{basins}}(\Sigma) := |\mathcal{C}_{\mathrm{seed}}(\Sigma)|.
\]

**Claim H0 (seed-orbit form), post-hoc test only:**

\[
N_{\mathrm{basins}}(\Sigma) \stackrel{?}{=} 539.
\]

The integer 539 is **not** used to build \(\Sigma\), \(T^\sharp\), or \(\sim\).

---

## 3. Enumeration algorithm

```text
for each seed s in Σ:
    walk until a state repeats → extract cycle C (frozenset)
    record attractor_id = canonical(C)  # e.g. min element + rotation
N_basins = number of distinct attractor_id
# only then compare to 539
```

Also report: hitting times to 1, fraction absorbed at 1, cycle length histogram.

**Script:** `scripts/phase0_seed_basins.py`

---

## 4. Bott gate

**Only if** \(N_{\mathrm{basins}}=539\) (or another pre-declared success criterion)  
→ ask whether \(\mathcal{C}_{\mathrm{seed}}\) admits a classifying map into \(B\mathrm{Spin}\) or \(BO\).

If \(N_{\mathrm{basins}}\ne 539\), the Bott link target must be changed; do not force 539 into the definition.

---

## 5. Relation to failed C2

Full-segment weak components of \(\{1,\ldots,N_{\mathrm{cut}}\}\) gave **2** components.  
Seed-orbit basins are a **different** package: only seed-reachable attractors matter.
