# Boardman Conditional Convergence

**S²-11DM²ET-X Model: Minimal Unification Core**  
**Author:** Arvin B. Hampton (String Weaver)

**Scope:** what Boardman conditional convergence is, when it is needed, and why residual thin \(F\) avoids it — with the correct slogans for any future infinite residual lifts.  
**Locks:** thin form SS strong collapse, kit, Option 3 — untouched.

**Probe:** `scripts/boardman_convergence_probe.py` → `boardman_convergence_results.json`.  
**Companions:** `Residual_Form_Spectral_Sequences.md`, `Thin_Complex_Formality.md`, `Mapping_Cone_rW.md`.

---

## 1. The problem Boardman addresses

A spectral sequence can have a well-defined page \(E_\infty\) and still **fail to reconstruct** the abutment \(H^\bullet\) if the filtration is infinite or not complete/Hausdorff in the inverse-limit sense.

Symptoms:

| Symptom | Meaning |
|---------|---------|
| \(E_\infty\) computed | associated graded “candidate” exists |
| Filtration on \(H^n\) not separated | nonzero elements in \(\bigcap_p F^p H^n\) |
| Filtration not exhaustive | union of \(F^p\) misses part of \(H^n\) |
| \(\lim^1\) obstruction | derived inverse limit of filtration quotients nonzero |

**Boardman theory** gives precise conditions under which
\[
E_r
\;\Rightarrow\;
H
\]
is only **conditional**, and how to read the obstruction.

---

## 2. Setup (filtered complex)

Let \((K,d)\) be a cochain complex with a decreasing filtration
\[
\cdots\supset F^p K\supset F^{p+1}K\supset\cdots,
\quad
d(F^p K)\subset F^p K.
\]

Assume the filtration is **multiplicative / compatible** so the usual SS forms:
\[
E_0^{p,q}=F^p K^{p+q}/F^{p+1}K^{p+q},
\quad
d_0=\text{induced }d,
\]
then \(E_1,E_2,\ldots,E_\infty\).

Define for the abutment candidates:

\[
\begin{aligned}
A^n
&:=
H^n(K),
\\
F^p A^n
&:=
\mathrm{im}\bigl(H^n(F^p K)\to H^n(K)\bigr),
\\
Q^p A^n
&:=
F^p A^n\big/ F^{p+1}A^n.
\end{aligned}
\]

Ideally \(E_\infty^{p,n-p}\cong Q^p A^n\).

---

## 3. Exhaustive, separated, complete

| Property | Definition | Failure mode |
|----------|------------|--------------|
| **Exhaustive** | \(\bigcup_p F^p K=K\) (or \(\bigcup F^p A=A\)) | missing low filtration degrees |
| **Separated** (Hausdorff) | \(\bigcap_p F^p A^n=0\) | phantom filtration elements |
| **Complete** | \(A^n\to\lim_p A^n/F^p A^n\) iso | Cauchy sequences of filtration don’t converge in \(A\) |

For **finite** filtrations (only finitely many nonzero steps per degree), exhaustive + separated ⇒ complete automatically, and \(E_\infty\cong\mathrm{gr}\,A\).

---

## 4. Boardman’s RE and \(RE_\infty\) conditions (ideas)

Boardman organizes convergence via the behavior of the **pages as \(r\to\infty\)** and the filtration on the abutment.

### 4.1 Conditional convergence (informal Boardman)

The SS **converges conditionally** to \(A\) if:

1. \(E_\infty^{p,q}\) is isomorphic to the associated graded \(Q^p A^{p+q}\) **whenever** the filtration on \(A\) is interpreted through the correct lim/colim; and  
2. the only possible failures are controlled by \(\lim^1\) terms of the filtration tower.

A standard cohomological form (one common packaging):

\[
0
\to
{\lim_r}^1\, Z_r^{p,q}
\to
F^p A^{p+q}
\to
\lim_r E_r^{p,q}
\to
0
\]
(schematic; exact shape depends on co- vs homological indexing and on whether one uses Boardman’s \(RE_\infty\)).

**Point:** \(E_\infty\) alone may equal \(\lim_r E_r\), while \(F^p A\) differs by a \(\lim^1\) of cycles \(Z_r\).

### 4.2 Strong convergence

**Strong convergence** means:

- exhaustive and separated filtration on each \(A^n\), and  
- \(E_\infty^{p,n-p}\cong Q^p A^n\) for all \(p\),  

with no \(\lim^1\) correction.

**Finite filtration length per degree ⇒ strong convergence** (as in residual thin \(F\)).

### 4.3 Conditional but not strong

Classic pathologies (infinite complexes):

- filtration complete but not separated;  
- \(E_\infty=0\) but \(A\neq 0\) (everything “hidden” in \(\bigcap F^p\));  
- \(E_2\) computable, abutment not recoverable without derived limits.

---

## 5. The \(\lim^1\) obstruction in one picture

Inverse system of filtration quotients:
\[
\cdots\to A/F^{p+1}A\to A/F^p A\to\cdots
\]

Exact sequence of lim:
\[
0
\to
\lim_p F^p A
\to
A
\to
\lim_p A/F^p A
\to
{\lim_p}^1 F^p A
\to
0
\]
(again schematic for countable inverse systems of abelian groups/vector spaces).

| If | Then |
|----|------|
| \(\lim F^p A=0\) and \(\lim^1 F^p A=0\) | \(A\cong\lim A/F^p A\) — complete + separated |
| \(\lim^1\neq 0\) | phantom information not seen by graded pieces |
| over a **field**, countable inverse systems of vector spaces | \(\lim^1\) often vanishes under Mittag-Leffler |

**Mittag-Leffler (ML):** images in the inverse system stabilize.  
Finite-dimensional pages that stabilize (collapse) often satisfy ML ⇒ \(\lim^1=0\).

---

## 6. Residual thin \(F\): Boardman is vacuous

| Boardman ingredient | Thin residual form SS |
|---------------------|------------------------|
| Filtration length per degree | **finite** (\(\le 3\) charge steps) |
| \(\lim^1\) of filtration | **0** (finite tower) |
| Collapse | \(E_2=E_\infty\) |
| Separated / exhaustive | yes |
| Convergence type | **strong**, not merely conditional |
| Extension problems | none in rank-1 \(H^2\) |

\[
\boxed{
\text{Boardman conditional convergence is not needed for thin }F.
}
\]

That is a feature of the residual design: **finite generators kill infinite-filtration pathology.**

---

## 7. Where Boardman *would* enter residual research

### 7.1 Inverse system of shells

\[
\cdots\to F_{\le W'}\to F_{\le W}\to\cdots
\quad(W\uparrow)
\]

Pro-object in \(D(\mathbb{Q})\):
\[
F_\infty^{\mathrm{pro}}
=
``\lim_W{}"\,F_{\le W}.
\]

If one tries
\[
H^\bullet\bigl(\mathrm{holim}_W F_{\le W}\bigr)
\quad\text{vs}\quad
\lim_W H^\bullet(F_{\le W}),
\]
a \(\lim^1 H^{\bullet-1}\) exact sequence appears:

\[
0
\to
{\lim_W}^1 H^{n-1}(F_{\le W})
\to
H^n(\mathrm{holim}\,F_{\le W})
\to
\lim_W H^n(F_{\le W})
\to
0.
\]

Under default residual thin + \(r_W\) iso for large \(W\):
\[
H^2(F_{\le W})\cong\mathbb{Q}
\quad\text{stabilizes}
\Rightarrow
\text{ML}
\Rightarrow
\lim^1=0.
\]

So even the shell tower is Boardman-quiet for the permanent class.

### 7.2 Infinite generator enrichments

If residual forms were enlarged to infinite towers (e.g. unbounded path cochains, infinite product of channels without finite support):

| Enrichment | Boardman risk |
|------------|----------------|
| Infinite product of paths | \(\lim^1\) on mass/cohomology |
| Unbounded charge filtration | conditional only |
| Continuum de Rham / EC forms as inverse limit of meshes | classic conditional convergence territory (**B**) |

### 7.3 Spectral sequence of a filtered inverse limit

Double limit issue: SS for each finite stage + limit over stages.  
Interchange of \(\lim\) and \(E_r\) requires ML / Boardman hypotheses.

**Residual rule:** compute finite thin SS first; only then take limits over \(W\) or cohorts.

---

## 8. Boardman vs collapse vs formality

| Notion | Controls |
|--------|----------|
| **Collapse** \(E_2=E_\infty\) | differentials die |
| **Strong convergence** | \(E_\infty=\mathrm{gr}\,H\) with good filtration |
| **Conditional convergence** | \(E_\infty\) relates to \(H\) up to \(\lim^1\) |
| **Formality** | \(F\simeq H(F)\) in \(D\) |

Thin residual \(F\): collapse + strong convergence + formality.  
Boardman layer is idle.

---

## 9. Practical residual checklist

```text
Before quoting E_∞ as H•:
  [ ] filtration finite per degree?  → strong; stop
  [ ] if infinite: exhaustive?
  [ ] separated (∩ F^p = 0)?
  [ ] Mittag-Leffler on pages / filtration quotients?
  [ ] lim¹ estimated or zero over field?
  [ ] extension problems in gr → H reconstructed?
```

Thin \(F\): first box checked ⇒ done.

---

## 10. Slogans (discipline)

| Avoid | Use |
|-------|-----|
| “SS converges” without type | “strongly converges (finite filtration)” |
| “\(E_\infty=0\Rightarrow H=0\)” always | only if strong/separated; else Boardman phantoms |
| “Boardman blocks residual \(H^2\)” | false for thin \(F\) |
| Continuum TTC SS “same as residual” | **B**; continuum may be conditional |

---

## 11. Reference card

\[
\begin{aligned}
&\text{Finite filtration}
\Rightarrow
\text{strong convergence},
\quad
\lim^1=0.
\\
&\text{Thin }F:
E_2=E_\infty\Rightarrow H^\bullet(F),
\quad
H^2\cong E_\infty^{1,1}.
\\
&\text{Boardman conditional:}
\text{infinite filtrations / pro-limits;}
\quad
\text{shell tower ML-quiet under }r_W\text{ iso}.
\\
&\text{holim}_W F_{\le W}:
0\to{\lim}^1 H^{n-1}\to H^n(\mathrm{holim})\to\lim H^n\to 0.
\end{aligned}
\]

---

## 12. Executed residual checks

| Check | Result |
|-------|--------|
| Finite charge filtration (\(\le 3\) steps) | **TRUE** |
| \(\lim^1\) filtration tower | **0** |
| Strong convergence | **TRUE** |
| \(E_2=E_\infty\), \(H^2\cong E_\infty^{1,1}\) | **TRUE** |
| Shell \(H^2\) rank-1 for all tested \(W\ge 5\) | **TRUE** (ML) |
| Boardman needed for thin \(F\) | **FALSE (O)** |
| Status | **`BOARDMAN_IDLE_THIN_F_STRONG_CONVERGENCE_A`** |

---

## 13. Category boundary

| Claim | Tag |
|-------|-----|
| Boardman needed for thin residual form SS | **O** (false) |
| Strong convergence of thin form SS | **A** |
| Shell inverse system \(\lim^1=0\) under stable rank-1 \(H^2\) | **A/S** |
| Continuum / unbounded residual lifts may be conditional | **S/B** |
| Boardman ⇒ free 539 | **O** |

---

## One-line summary

**Boardman conditional convergence governs infinite filtrations and \(\lim^1\) phantoms between \(E_\infty\) and the abutment; residual thin \(F\) has finite filtration length, so convergence is strong and Boardman-idle, while only pro-shell or infinite enrichments could revive \(\lim^1\) — and under default \(r_W\) iso even the shell tower is Mittag-Leffler quiet.**

*Per aspera ad astra.*
