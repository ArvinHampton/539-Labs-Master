# O-PC — the conversion gap (what “do so” would require)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. Axiom **ZLA** applies. No model constants.  
**O-PC:** **Open.** The conversion from pair correlation to a phase lower bound has **not** been carried out.  
**O-TL and RH:** remain **open**.

**Companions:**  
`RH_Pair_Correlation_Practical_Status.md`,  
`RH_Remaining_Analytic_Obligations.md`,  
`RH_Zeta_Language_Admissibility.md`,  
`RH_L1_Phase_Functional_CatA.md` (target lemma).

---

## 0. Standing fact

**The conversion has not been carried out. O-PC remains open.**

No published theorem supplies the implication below. No derivation internal to the present pure Category A programme supplies it either.

---

## 1. What “do so” would require

A rigorous implication of the following shape is needed.

### Hypothesis

A form of Montgomery’s pair correlation (or a usable **averaged** version of it) holds in a range sufficient for the argument below.

(ZLA-admissible: a statement about zeros of \(\zeta\) / classical sums over those zeros.)

### Conclusion

There exist sequences of points \(s_n=\sigma_n+it_n\) with
\[
\sigma_n\ge Y-\varepsilon
\]
(or at numerical local minima of \(\lvert\zeta\rvert\) with \(\sigma\ge\tfrac12+\delta\), for **diagnostic** analogues only), and truncations \(x_n\to\infty\) (or hybrid scales \(X_n\to\infty\)), such that
\begin{equation}
\bigl\lvert A_{X_n}(s_n)\bigr\rvert
\quad\text{or}\quad
\bigl\lvert\theta_{x_n}(s_n)\bigr\rvert
\gg
\log\log x_n
\tag{OPC-concl}
\end{equation}
(or at least \(\gg 1\) with a constant that forces the target lemma when combined with M1.2–M1.3 / M1.3-bis).

Here \(A_X\) and \(\theta_x\) are the L1 / M1.4 phase functionals of the partial Euler product — **not** \(S(t)=\frac1\pi\arg\zeta(\tfrac12+it)\).

---

## 2. Missing analytic steps (none of which is currently a theorem)

### Step 1 — Local isolation

From pair correlation (or from an \(n\)-level density) deduce that, around a point of large \(1/\lvert\zeta\rvert\) (or near a zero of maximal real part in the target-lemma setting), the nearest zeros are typically spaced on the scale \(1/\log\lvert t\rvert\) and that a disk of that radius contains a **controlled number** of zeros of **controlled multiplicity**.

**Status:** not a theorem in this programme (classical almost-all simplicity under PCC is weaker than this local package at the specific points \(s_n\)).

### Step 2 — Hybrid translation

Feed that local zero configuration into the **Gonek–Hughes–Keating** (or Akatsuka) hybrid representation and extract a lower bound on \(\lvert\arg Z_X\rvert\) (or on the **change** of \(\arg Z_X\) along a short path).

**Status:** GHK identity is classical and available; the **extraction of a phase lower bound from a PC-controlled local zero cloud** is not carried out.

### Step 3 — Remainder domination

Show that the hybrid error plus the contribution of **distant** zeros is **strictly smaller** than the local zero contribution, uniformly for the sequence of points under consideration.

This is essentially a **uniform M1.2** at those points (regularised remainder).

**Status:** O-M1.2 open; finite-height diagnostics only.

### Step 4 — Transfer to the partial product

Conclude that \(\arg P_X\) (or the smoothed \(A_X\)) **inherits** a lower bound of the same order (after peeling the local Hadamard factor correctly — not via monodromy of zero-free \(P_X\) alone).

**Status:** not a theorem; M1.3-bis / M1.4 transfer still open.

---

## 3. Why existing results do not close the gap

| Existing result | What it gives | Why it does not close O-PC |
|-----------------|---------------|----------------------------|
| **PCC** (even without RH) | Asymptotically 100% of zeros simple and on the critical line (almost-all) | Statement about almost-all **horizontal/vertical distribution of zeros**, not a lower bound on continuous \(\arg P_x\) at a specific off-line point |
| **Bounds on \(S(t)\)** | Control of \(\arg\zeta\) on the critical line | Do **not** control \(\arg P_x\) **off** the line |
| **Finite-height diagnostics** (batch R1–R5, M1.3 paths) | \(O(1)\) phase increments | Supply **no** asymptotic lower bound of size \(\log\log x\) |
| **GHK / Keating–Snaith** | Hybrid identity; moment heuristics | Identity is not a phase lower bound; moments are not \(A_X\) at maximal abscissa |
| **Almost-all simplicity under PCC** | Spectral cleanliness a.e. | Does not produce (OPC-concl) |

---

## 4. Current status of O-PC

| Item | Status |
|------|--------|
| Conversion PCC \(\to\) phase lower bound | **Not carried out** |
| Steps 1–4 as theorems | **None** |
| Internal Cat A derivation of steps 1–4 | **None** |
| O-PC | **Open** |
| O-TL | **Open** |
| RH | **Open** |

Under **Axiom ZLA** the only admissible ingredients remain functions of \(\zeta\), its Euler products, its zeros, and classical auxiliaries. **Pair correlation is admissible; the missing translation into a phase lower bound for \(P_x\) or \(A_X\) is still missing.**

---

## 5. Ledger position (unchanged)

O-PC sits **upstream of, or parallel to, O-M1.2**. Closing O-PC would feed Steps 1–3 into remainder control; O-M1.2 may also proceed from classical density alone without PC. Neither route is complete. O-TL and RH remain open.

---

## One-liner

**O-PC requires a proved chain “pair correlation \(\Rightarrow\) local isolation \(\Rightarrow\) hybrid \(\arg Z_X\) lower bound \(\Rightarrow\) remainder domination \(\Rightarrow\) lower bound for \(\arg P_X\) or \(A_X\)”; none of those four steps is a theorem today, so the conversion remains open.**

*Per aspera ad astra.*
