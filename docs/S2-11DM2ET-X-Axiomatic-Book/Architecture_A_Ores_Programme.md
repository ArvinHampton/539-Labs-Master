# Architecture A / Bott / classifying-map programme on \(\mathcal{O}_{\mathrm{res}}\)

**Status:** Active Category B developmental programme.  
**Carrier:** \(\mathcal{O}_{\mathrm{res}}\) only (verified combinatorial 539-set).  
**Does not claim** free \(T^\sharp\) origin of the 539 objects.  
**Does not claim** a lift of the No-Go on \(\lambda=\ln 3/539\) from democracy alone.

**Companions:**  
`Object539_NonCircular_Construction.md`,  
`Architecture_A_Spin_KO_Draft.md` (legacy trajectory draft — superseded target),  
`Bott_HQCC_Link_Research.md`,  
`Foundational_Arithmetic_Packaging.md`.

**Probe:** `scripts/architecture_A_ores_probe.py` → `architecture_A_ores_results.json`.

---

## 0. Mandatory provenance (every claim in this programme)

> **Provenance block (locked).**  
> The 539 objects under study are **residual flux quanta** in the guaranteed democratic charge-sector core \(\mathcal{O}_{\mathrm{res}}\) (or the nine parallel cores \(\mathrm{core}(C_q)\)).  
> They are obtained from:
> 1. Category A atoms \(N_{\mathrm{flux}}=\lfloor e^3\cdot 3^5\rfloor\), \(N_{\mathrm{tow}}=3^5\), charge modulus \(9\);
> 2. **Principle (S):** clear one fully loaded tower seed of size \(f_{\max}=\lceil N_{\mathrm{flux}}/N_{\mathrm{tow}}\rceil\);
> 3. **Democratic (equitable) partition** of the residual pool into nine charge classes;
> 4. Guaranteed core size \(B'=\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\).
>
> They are **not** free or charge-preserving \(T^\sharp\) basins, path classes, or homotopy classes of resonant trajectories.  
> Using Bott / \(KO\) / spin bordism on this carrier does **not** lift the canonical No-Go and does **not** identify \(N_\star=14\) with \(539\).

Any theorem, figure, or commit message in this programme **must** restate or cite this block.

---

## 1. Carrier (fixed)

\[
\lvert\mathcal{O}_{\mathrm{res}}\rvert
=
B'
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}-f_{\max}}{9}\Bigr\rfloor
=
539
\quad\text{(no 539 on the RHS)}.
\]

Canonical model: charge sector \(q=0\) core after seed \(\{0,\ldots,f_{\max}-1\}\) and round-robin partition (`Object539_NonCircular_Construction.md`).

**Nine-core package** (optional extension):
\[
\mathcal{O}_{\mathrm{res}}^{(9)}
:=
\bigsqcup_{q=0}^{8}\mathrm{core}(C_q),
\qquad
\lvert\mathcal{O}_{\mathrm{res}}^{(9)}\rvert
=
9B'
=
4851.
\]

---

## 2. Discrete background space (Architecture A, retargeted)

Replace trajectory space \(\mathcal{C}\) by the carrier. Working discrete model of the Architecture A product:

\[
X_{\mathrm{disc}}
:=
\underbrace{\mathbb{Z}/9\mathbb{Z}}_{\text{charge sector}}
\times
\underbrace{\mathbb{Z}/N_{\mathrm{tow}}\mathbb{Z}}_{\text{tower}}
\times
\underbrace{\mathbb{Z}/8\mathbb{Z}}_{\text{Bott clock / real period}}.
\]

Continuous lift (later):
\[
X_4
=
B(\mathbb{Z}/9)
\times
B(\mathbb{Z}/N_{\mathrm{tow}})
\times
BO
\quad\text{or}\quad
B(\mathbb{Z}/9)\times B(\mathbb{Z}/N_{\mathrm{tow}})\times B\mathrm{Spin},
\]
with the third factor receiving the Bott clock via the classical map to \(BO\).

**No** \(G_4=539.9\,\mathrm{s}\) is placed in \(X_{\mathrm{disc}}\).  
**No** free path space of \(T^\sharp\) is required.

---

## 3. Classifying map \(f\colon \mathcal{O}_{\mathrm{res}}\to X_{\mathrm{disc}}\)

### 3.1 Tower assignment (democratic seed multiset)

Partition \(\Omega=\{0,\ldots,N_{\mathrm{flux}}-1\}\) into \(N_{\mathrm{tow}}\) consecutive blocks with loads
\[
\underbrace{21,\ldots,21}_{R}\,,
\underbrace{20,\ldots,20}_{N_{\mathrm{tow}}-R},
\quad
R=N_{\mathrm{flux}}-20\cdot N_{\mathrm{tow}}=20.
\]
For \(x\in\Omega\), let \(\tau(x)\in\mathbb{Z}/N_{\mathrm{tow}}\) be the unique block containing \(x\).

### 3.2 Bott degree

\[
\beta(x) := x \bmod 8 \in \mathbb{Z}/8.
\]

### 3.3 Charge sector of the core

For the canonical core of class \(C_q\), every label satisfies a **fixed** residue
\[
x \equiv r_q \pmod 9
\]
(verified: cores are monochromatic mod 9). For \(q=0\), \(r_0=3\).

### 3.4 Definition of \(f\)

\[
f(x)
:=
\bigl(q(x),\;\tau(x),\;\beta(x)\bigr)
\in
X_{\mathrm{disc}}.
\]

For a single core \(\mathcal{O}_{\mathrm{res}}=\mathrm{core}(C_0)\), \(q\equiv 0\) (construction index) or use ambient \(x\bmod 9\).

### 3.5 Executed facts (probe)

| Fact | Status |
|------|--------|
| \(\lvert\mathcal{O}_{\mathrm{res}}\rvert=539\) | Verified |
| \(f\big|_{\mathcal{O}_{\mathrm{res}}}\) injective into \(\{0\}\times\mathbb{Z}/243\times\mathbb{Z}/8\) via \((\tau,\beta)\) | **Verified** (539 distinct pairs) |
| \(f\) on \(\mathcal{O}_{\mathrm{res}}^{(9)}\) injective into \(X_{\mathrm{disc}}\) | **Verified** (4851 distinct triples) |
| Each core monochromatic in \(x\bmod 9\) | Verified |
| Free \(\mathbb{Z}/8\)-action on a 539-set | **Impossible** (\(8\nmid 539\)) |

---

## 4. Bott filtration on the carrier

### 4.1 Degree fibers

\[
F_k
:=
\{x\in\mathcal{O}_{\mathrm{res}}:\beta(x)=k\},
\qquad
k\in\mathbb{Z}/8.
\]

**Canonical core \(q=0\), canonical seed \(\{0,\ldots,f_{\max}-1\}\) (executed):**

| \(k\bmod 8\) | \(\lvert F_k\rvert\) | Classical \(\pi_k(O)\) type (label only) |
|-------------:|---------------------:|----------------------------------------|
| 0 | 67 | \(\mathbb{Z}/2\) |
| 1 | 67 | \(\mathbb{Z}/2\) |
| 2 | 67 | \(0\) |
| 3 | 67 | \(\mathbb{Z}\) |
| 4 | 67 | \(0\) |
| 5 | 68 | \(0\) |
| 6 | 68 | \(0\) |
| 7 | 68 | \(\mathbb{Z}\) |

Check: \(5\cdot 67 + 3\cdot 68 = 335+204 = 539\).

### 4.2 Relation to \(B'=8\cdot 67+3\)

Always (seed-independent cardinality):
\[
B' = 8\cdot\lfloor B'/8\rfloor + (B'\bmod 8) = 8\cdot 67 + 3.
\]
On the **canonical** core, **67** is also the **minimum** Bott-fiber size under \(\beta\), with excess \(+1\) on degrees \(\{5,6,7\}\).

**Seed dependence (probe, 50 random seeds):** fiber minima vary (sample saw 62–66); **injectivity** of \((\tau,\beta)\) on the \(q=0\) core held in **50/50** trials. So:
- the identity \(B'=8\cdot 67+3\) is **seed-independent** (pure arithmetic of \(B'\));
- the tidy fiber table above is a **canonical-seed** phenomenon, not yet a theorem for all seeds;
- Phase **A1** tracks equivariance / normalization of \(\beta\) under seed change.

**Interpretation (Category B, provisional):**  
the carrier admits a Bott-clock grading; cardinality forces residual \(B'\equiv 3\pmod 8\). Canonical seed realizes bulk fiber size 67 with excess 3. This is **compatible** with obstruction O2 (no free \(\mathbb{Z}/8\) action) and **does not** use free \(T^\sharp\).

**Forbidden reading:** “\(\pi_3(O)=\mathbb{Z}\) produces 539 trajectories.”  
**Allowed reading:** “On the residual-flux carrier of size \(B'\), the Bott clock is a grading; \(B'\equiv 3\pmod 8\) is forced by packaging+(S).”

### 4.3 No free \(\mathbb{Z}/8\) action (O2 cleared on carrier)

Because \(8\nmid 539\), no free period-8 permutation of \(\mathcal{O}_{\mathrm{res}}\) exists.  
Any Bott **action** must be non-free (fixed points / residual orbits).  
The fiber description above is a **grading**, not a free group action — consistent with obstruction O2 in `Bott_HQCC_Link_Research.md`.

---

## 5. Spin / \(KO\) interface (programme, not completed theorem)

### 5.1 Discrete \(KO\)-proxy

Assign to each \(x\in\mathcal{O}_{\mathrm{res}}\) the classical Bott table slot \(\pi_{\beta(x)}(O)\) as a **label** only:

\[
\kappa(x) \in \{\mathbb{Z}/2,\,0,\,\mathbb{Z}\}
\quad\text{per real Bott table}.
\]

This is a function \(\mathcal{O}_{\mathrm{res}}\to\{\text{Bott types}\}\), **not** a computed \(KO\)-homology class.

### 5.2 Target continuous map (open)

Construct a continuous (or simplicial) map
\[
\Phi\colon |\mathcal{O}_{\mathrm{res}}|_{\mathrm{disc}}
\longrightarrow
B\mathrm{Spin}\times B(\mathbb{Z}/9)\times B(\mathbb{Z}/N_{\mathrm{tow}})
\]
whose restriction to discrete points recovers \(f\), then push
\[
\Phi_*[\mathrm{pt}_x] \in KO_0(\cdots)
\quad\text{or bordism}.
\]

**Exit criteria for a theorem (not yet met):**

- [x] Carrier fixed with 539-free count  
- [x] Discrete classifying map \(f\) defined and injective on cores  
- [x] Bott grading \(\beta\) computed; O2 residual structure exhibited  
- [ ] Geometric / simplicial lift to \(B\mathrm{Spin}\) or \(BO\)  
- [ ] Actual \(KO\) or \(\Omega^{\mathrm{Spin}}\) computation (not only labels)  
- [ ] Naturality under change of seed representative (equivariance)

---

## 6. Classifying-map architectures (scoped to \(\mathcal{O}_{\mathrm{res}}\))

| Arch | Content on carrier | Status |
|------|-------------------|--------|
| **A** | \(f\to X_{\mathrm{disc}}\); spin/\(KO\) lift | **Active** — discrete layer executed |
| **B** | Clifford word on \((\tau,\beta)\) or branch labels of \(x\) | Parallel — discrete labels available; no free \(T^\sharp\) words required |
| **C** | Loop space of frames | Deferred — needs bulk geometry |
| **D** | Index of Dirac-type operator on a space built from flux quanta | Deferred — needs geometry |

Architecture B **on the carrier** may use only functions of \(x,\tau(x),\beta(x)\) — **not** \(T^\sharp\)-orbits — unless clearly labeled as a separate free-dynamics probe (still Option 3).

---

## 7. Consistency with No-Go / ACE / packaging

| Statement | Stance in this programme |
|-----------|---------------------------|
| \(\lvert\mathcal{O}_{\mathrm{res}}\rvert=B'\) | Cat.\ A + (S); verified |
| Free \(T^\sharp\) basins \(=2\) | Intact Category A; **not** modified |
| \(N_\star=14\) | Intact; distinct from \(B'\) |
| \(\lambda=\ln 3/539\) from democracy alone | **Still blocked** (No-Go) |
| Crypto hard budget \(\sigma:=L_{\mathrm{pack}}\) | Independent design use of same integer |
| Bott produces free 539 trajectories | **Forbidden claim** |
| Bott grades residual flux quanta | **Allowed claim** (this programme) |

---

## 8. Developmental roadmap

| Phase | Deliverable | Priority |
|-------|-------------|----------|
| **A0** | Provenance + carrier + discrete \(f\) + \(\beta\)-filtration | **Done** (this doc + probe) |
| **A1** | Seed-equivariance: \(f\) and fiber sizes under random \(\mathrm{Seed}\) of size \(f_{\max}\) | Next |
| **A2** | Simplicial nerve of \(X_{\mathrm{disc}}\); \(f\) as simplicial map | Next |
| **A3** | Compare fiber statistics to Bott table (heuristic only) | Ongoing |
| **A4** | Spin structure check on a geometric model of tower×charge | Later |
| **A5** | Spectral sequence / board game \(KO\) computation | Later |

Secondary (lower priority, parallel): E1–E2 free-map word probes; 1001 provenance; R-FFT; individuality falsifiability — **must not** be mixed into carrier provenance.

---

## 9. Bottom line

> Architecture A / Bott / classifying-map work **proceeds** with \(\mathcal{O}_{\mathrm{res}}\) as the **only** 539-carrier.  
> Discrete classifying map and Bott-clock grading are **executed and verified**.  
> Continuous \(KO\)/spin theorems remain open.  
> Honest provenance is mandatory: residual flux quanta under (S) + democratic charge partition — **not** free \(T^\sharp\), **not** a No-Go lift.
