# Classical constraints on (Iso_H)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA**.  
**Companions:** `RH_ND1_Stability_Resolve.md`, `RH_ND1_Status_Acceptance.md`.  
**Does not prove (Iso_H), unconditional B_θ, or RH.**

---

## 0. ND1 lock (unchanged)

| Item | Status |
|------|--------|
| Conjugate obstruction | **Closed** (optimal lock) |
| (RM) + L2 → positive-density good \(u_k\), \(\Phi^\star\ge c\) (S11) | **Proved** |
| (RM)+(Iso_H) ⇒ OP1 (S13), ⇒ B_θ (S16) | **Proved implications** |
| (Iso_H) unconditional | **Open** |
| Unconditional B_θ / RH | **Open** |

**Barrier after ND1:**
```text
phase lock ✓ · residual ✓ · conjugate lock ✓
        │
        ▼
(RM)+(Iso_H) ──proved──► B_θ
        │
        └── Iso_H unconditional ✗ OPEN
```

B_θ is blocked only by **abscissa isolation** on the rightmost line, not by loglog, E1, or conjugate phase.

---

## 1. Definition (Iso_H)

At a fixed rightmost abscissa \(\beta_\star>1/2\) for a zero \(\rho_\star=\beta_\star+i\gamma_\star\) of multiplicity \(m\ge 1\),

> **(Iso_H):** up to EF truncation, the only zeros with \(\operatorname{Re}\rho=\beta_\star\) are \(\{\rho_\star,\bar\rho_\star\}\).

---

## 2. What classical analysis **does** give

### 2.1 Point isolation ⇒ finite-height Iso_H is trivial

Zeros of \(\zeta\) are **isolated points** in \(\mathbb{C}\). Hence any **compact** segment of the vertical line \(\operatorname{Re}=\beta_\star\) contains only **finitely many** zeros.

**Consequence:** for each fixed height bound \(T\), the restriction of (Iso_H) to \(\lvert\gamma\rvert\le T\) is a finite combinatorial statement. The difficulty is **uniformity in \(T\to\infty\)** (unbounded height).

### 2.2 Functional equation and quartets

The functional equation forces zeros in **quartets** \(\{\rho,\,1-\rho,\,\bar\rho,\,1-\bar\rho\}\) (when not on the critical line or real axis).

For a **rightmost** zero \(\rho_\star\) with \(\beta_\star>1/2\):

- \(\bar\rho_\star\) has the **same** abscissa \(\beta_\star\) (forced same-abscissa partner).  
- \(1-\bar\rho_\star\) has abscissa \(1-\beta_\star<1/2\) (strictly to the **left**).  
- \(1-\rho_\star\) likewise sits at \(1-\beta_\star\).

**Consequence:** the only **forced** same-abscissa partner of \(\rho_\star\) under the functional equation is the conjugate. The FE does **not** force additional zeros on \(\operatorname{Re}=\beta_\star\).

### 2.3 Multiplicity bounds (Ivić and relatives)

Large multiplicity at a zero forces zeros to the left; near \(\sigma=1\) multiplicities are small.

**Consequence:** this controls the **multiplicity \(m\) at one point**, not the **number of distinct ordinates** on the vertical line \(\operatorname{Re}=\beta_\star\). It does **not** prove (Iso_H).

### 2.4 Zero-density \(N(\sigma,T)\)

Classical bounds \(N(\sigma,T)\ll T^{c(1-\sigma)^{3/2}}(\log T)^{O(1)}\) control the **total number** of zeros with \(\beta\ge\sigma\) up to height \(T\).

**Consequence:** density bounds the bulk of zeros to the right of \(\sigma\). They do **not** force “at most two zeros on any single vertical line \(\operatorname{Re}=\beta_\star\)”.

---

## 3. What classical analysis does **not** give

| Missing theorem | Status |
|-----------------|--------|
| The number of zeros on a fixed vertical line \(\operatorname{Re}=\beta_\star>1/2\) is finite (as \(T\to\infty\)) | **No classical theorem** |
| Only \(\{\rho_\star,\bar\rho_\star\}\) occupy that abscissa | **No classical theorem** |
| Isolation hypotheses near \(\sigma=1\) used to improve zero-free regions | **Different object** from (Iso_H); not a substitute |

---

## 4. Weakenings recorded (still open as theorems)

### 4.1 StripDens

A density bound in a **thin strip** about \(\beta_\star\) would control the near/same-abscissa Lip contribution \(A\) in the ND1 derivative majorant.

**Status:** **Open** as a theorem; would feed residual estimates without full (Iso_H).

### 4.2 Mass-with-A (sharpest unconditional target)

Under **(RM) alone**, on the good set \(K_\star\) from S11, does
\begin{equation}
\sum_{\substack{k\in K_\star\\ u_k\le U}}
\frac{\delta_k}{u_k}
\quad\text{with}\quad
\delta_k\sim\frac{1}{\max\bigl(A(u_k),1\bigr)}
\tag{Mass-A}
\end{equation}
still **diverge** as \(U\to\infty\)?

If **yes**, OP1 mass (and thus B_θ) would follow **without full (Iso_H)**.

**Status:** **Open** — preferred pure next step after ND1.

---

## 5. Solid next directions (updated after this pass)

| Rank | Direction |
|------|-----------|
| **1** | **Mass-with-A under (RM) only** — preferred pure next step |
| **2** | **StripDens** from classical density tables |
| **3** | Resonance off the line |
| **4** | Effective density constants |
| **5** | Finite-product approximation off the line |
| **6** | Path continuation from on-line Ω (independent of Iso_H) |

**No claim** that (Iso_H) or B_θ is closed.

---

## 6. Status

| Item | Status |
|------|--------|
| ND1 acceptance | **Locked** |
| (RM)+(Iso_H)⇒B_θ | **Proved** |
| Classical constraints on Iso_H (this note) | **Recorded** |
| Unconditional Iso_H | **Open** |
| Mass-with-A / StripDens | **Open** |
| Unconditional B_θ / O-TL | **Open — primary not closed** |
| RH | **Open** |
| Programme label | `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` |

---

## One-liner

**Classical analysis makes finite-height Iso_H trivial and forces only the conjugate as same-abscissa partner, but does not bound the number of distinct ordinates on \(\operatorname{Re}=\beta_\star>1/2\); Mass-with-A under (RM) is the sharpest unconditional bypass of full Iso_H, and remains open.**

*Per aspera ad astra.*
