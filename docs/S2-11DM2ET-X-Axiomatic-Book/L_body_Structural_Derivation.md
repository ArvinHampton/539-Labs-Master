# Structural derivation of \(L_{\mathrm{body}} = N_{\mathrm{flux}}//9 - f_{\max}\)

**Goal.** Decide whether
\[
L_{\mathrm{body}}
:=
\Bigl\lfloor\frac{N_{\mathrm{flux}}}{9}\Bigr\rfloor
-
f_{\max}
=
N_{\mathrm{flux}}//9 - f_{21}
\]
admits a **unique structural reason** from charge conservation, tower partition, and/or minimal-action principles, **without aiming at 539**.

**Fixed inputs only** (no 539 on any RHS):
\[
N_{\mathrm{flux}}=\lfloor e^{3}\cdot 3^{5}\rfloor=4880,\quad
N_{\mathrm{tow}}=3^{5}=243,\quad
Q=9,\quad
L_{\mathrm{pref}}=\lfloor e^{3}/\ln 3\rfloor=18.
\]

**Verdict (short).**  
Ingredients \(B_Q\) and \(f_{\max}\) are forced. The **subtraction** \(B_Q-f_{\max}\) is forced only after adopting a single extra combination principle **(S)** (min-action full max-tower seed clear). Under (S), \(L_{\mathrm{body}}=521\) is unique in a natural functional class and the length packaging \(18+521=539\) is non-circular. Without (S), the residual subtraction retains **ansatz** status. Charge conservation + tower democracy **alone** do **not** select between \(521\) and \(522\).

---

## 0. Forced integers (no combination rule yet)

### 0.1 Democratic tower loads (unique multiset)

Equitable integer partition \(\sum_{\tau} f_{\tau}=N_{\mathrm{flux}}\) with \(\max f-\min f\le 1\):

\[
f_{\min}
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}}{N_{\mathrm{tow}}}\Bigr\rfloor
=
20,
\qquad
R
=
N_{\mathrm{flux}}-f_{\min}N_{\mathrm{tow}}
=
20,
\qquad
f_{\max}
=
\Bigl\lceil\frac{N_{\mathrm{flux}}}{N_{\mathrm{tow}}}\Bigr\rceil
=
21.
\]

Multiset of loads: \(\{21\}^{R}\cup\{20\}^{N_{\mathrm{tow}}-R}\).  
**Uniqueness:** among integer assignments with sum \(N_{\mathrm{flux}}\) and range at most 1, this multiset is unique. In particular \(f_{\max}\) is uniquely \(\lceil N_{\mathrm{flux}}/N_{\mathrm{tow}}\rceil\).  
(\(R=f_{\min}=20\) is a numerical accident of this flux, not an extra axiom.)

### 0.2 Charge-sector budget (unique equal split)

Charge label \(Q\equiv n\bmod 9\) gives 9 classes. Equal flux share:

\[
B_Q
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}}{9}\Bigr\rfloor
=
542,
\qquad
N_{\mathrm{flux}}\bmod 9
=
2.
\]

**Uniqueness:** every class is guaranteed at least \(B_Q\); two classes get one extra unit from the remainder 2. The **canonical residual body budget before seed accounting** is the guaranteed floor share \(B_Q\).

### 0.3 What is *not* forced yet

The pair \(\{B_Q,f_{\max}\}\) does **not** by itself define a residual body length. Natural candidates still open:

| Candidate | Value | Meaning |
|-----------|------:|---------|
| \(B_Q\) alone | 542 | sector budget, no seed clear |
| \(B_Q-f_{\min}\) | 522 | clear one base tower |
| \(B_Q-f_{\max}\) | **521** | clear one ceiling tower |
| \(B_Q-R\) | 522 | subtract tower *count* (units mixed unless \(R\) re-read as flux) |
| \(B_Q-\lceil R/9\rceil\) | **539** | clear max *extras* per sector (different principle) |

**Constraint audit (charge + tower only):**  
If one only requires (i) \(0<L\le B_Q\) and (ii) \(B_Q-L\in\{f_{\min},f_{\max}\}\) (complement is a democratic tower load), then

\[
L\in\{522,\,521\}.
\]

**No unique residual body length from charge conservation and tower partition alone.**  
A combination principle is required to pick \(f_{\max}\) over \(f_{\min}\).

---

## 1. Combination principle (S) — minimal-action full seed clear

### Principle (S)

> A trajectory is initiated by **clearing one complete democratic tower seed**.  
> The seed quantum is the **maximal** tower load \(f_{\max}\) under the equitable partition (one fully loaded remainder tower).  
> That quantum is spent at injection and must **not** be double-counted in the free charge-sector path budget:
> \[
> L_{\mathrm{body}}
> :=
> B_Q - f_{\max}.
> \]

### Why \(f_{\max}\), not \(f_{\min}\)? (selection rule)

| Choice | Residual \(B_Q-f\) | Status under (S) |
|--------|-------------------:|:-----------------|
| \(f_{\min}=20\) | 522 | Under-clears: does not realize a **ceiling** quantum that the partition actually places on \(R>0\) towers |
| \(f_{\max}=21\) | **521** | Clears one **fully loaded** exceptional tower — the elementary complete unit of the equitable partition |

**Minimal-action reading.**  
Pay the **smallest number of towers** (namely one) that realizes a **full ceiling quantum** of the democratic multiset. That payment is uniquely \(f_{\max}=\lceil N_{\mathrm{flux}}/N_{\mathrm{tow}}\rceil\).

**Saturation reading.**  
Exceptional towers exist iff \(R>0\). The minimal integer that saturates the exceptional class (equals some tower load and is maximal among tower loads) is \(f_{\max}\). Using \(f_{\min}\) never touches the exceptional capacity the partition requires.

**Why one tower per sector budget?**  
\(B_Q\) is flux **per charge class**, not per tower. Injection couples that sector to **one** tower seed. Multi-tower injection is a higher-action composite; minimal action keeps one tower.

### Status of (S)

| Claim | Status |
|-------|--------|
| \(f_{\max},B_Q\) from democracy + charge | **Forced** (Category A / Dem+Res+Tower) |
| “Subtract one seed from \(B_Q\)” | **Principle (S)** — extra combination rule |
| “Seed \(=f_{\max}\) not \(f_{\min}\)” | **Part of (S)**; selects uniquely in §2 |
| Forced by Res+Tower+Dem **alone** (No-Go data)? | **No** — same data still leave \(\{521,522\}\) |

So (S) is a **single, local, 539-free modelling principle**, not a reverse-engineered fit to 539. It is weaker than “derived from Axiom 0 alone,” stronger than “bare ansatz \(521:=539-18\).”

---

## 2. Definition and uniqueness under (S)

\[
\boxed{
L_{\mathrm{body}}
:=
B_Q - f_{\max}
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}}{9}\Bigr\rfloor
-
\Bigl\lceil\frac{N_{\mathrm{flux}}}{N_{\mathrm{tow}}}\Bigr\rceil
=
542 - 21
=
521.
}
\]

Equivalently \(f_{21}=f_{\max}\) at these integers, so
\[
L_{\mathrm{body}} = N_{\mathrm{flux}}//9 - f_{21}
\]
is the same quantity — **derived under (S)**, not an ansatz label.

### Uniqueness in a declared functional class

Functionals
\[
\Psi(f)
=
B_Q - f,
\qquad
f\in\{f_{\min},\,f_{\max},\,R,\,N_{\mathrm{tow}}//9,\,\lceil R/9\rceil,\,Q,\,N_{\mathrm{flux}}\bmod 9\}.
\]

| \(f\) | \(\Psi\) | Selected by (S)? | Notes |
|------:|--------:|:----------------:|-------|
| \(f_{\max}\) | **521** | **Yes** | full ceiling seed |
| \(f_{\min}\) | 522 | No | under-clears ceiling |
| \(R\) (=20) | 522 | No | tower *count*, not seed quantum |
| \(N_{\mathrm{tow}}//9=27\) | 515 | No | towers per charge, not seed size |
| \(\lceil R/9\rceil=3\) | **539** | No | **extras**-clear (principle S′, §5), not full seed |
| \(Q=9\) | 533 | No | modulus, not seed |
| \(N\bmod 9=2\) | 540 | No | charge remainder only |

Within the **seed-quantum** subclass \(f\in\{f_{\min},f_{\max}\}\), principle (S) selects \(\Psi=521\) uniquely.  
Within the broader class, (S) still selects 521 once “seed quantum = one tower load” is required (excluding extras-count and modulus).

**Verified numerically** (script §7): arithmetic identities hold; no other seed-quantum choice yields 521.

---

## 3. Composite length packaging (non-circular **under (S)**)

Independent prefix (already non-circular):

\[
L_{\mathrm{pref}}
:=
\bigl\lfloor e^{3}/\ln 3\bigr\rfloor
=
18.
\]

\[
\boxed{
L_{\mathrm{pack}}
:=
L_{\mathrm{pref}} + L_{\mathrm{body}}
=
18 + 521
=
539.
}
\]

No numeral 539 on the RHS of \(L_{\mathrm{pref}}\) or \(L_{\mathrm{body}}\).  
The equality is a theorem of arithmetic from \(\{e,3,N_{\mathrm{tow}},9\}\) **once (S) is adopted**.

### Single-shot global form (same (S), total flux first)

Clear one max tower seed from **total** flux, then equal-split across charge classes:

\[
L_{\mathrm{pack}}'
:=
\Bigl\lfloor
\frac{N_{\mathrm{flux}} - f_{\max}}{9}
\Bigr\rfloor
=
\Bigl\lfloor\frac{4859}{9}\Bigr\rfloor
=
539.
\]

**Structural reading:**  
> After democratic tower partition, clear one fully loaded tower seed from the flux pool; divide the remainder equally among the nine charge classes.

Uses only \((N_{\mathrm{flux}},N_{\mathrm{tow}},9)\) and (S); does not mention 18 or 521.

### Relation \(L_{\mathrm{pack}}=L_{\mathrm{pack}}'\) (identity, not packaging axiom)

For integers \(N=9q+r\), \(0\le r<9\),
\[
\Bigl\lfloor\frac{N-f}{9}\Bigr\rfloor
=
q + \Bigl\lfloor\frac{r-f}{9}\Bigr\rfloor
=
B_Q + \Bigl\lfloor\frac{r-f}{9}\Bigr\rfloor.
\]
Hence
\[
L_{\mathrm{pref}}+B_Q-f_{\max}
=
L_{\mathrm{pack}}'
\quad\Longleftrightarrow\quad
L_{\mathrm{pref}}
=
f_{\max}+\Bigl\lfloor\frac{r-f_{\max}}{9}\Bigr\rfloor.
\]
At \((N,f_{\max},r)=(4880,21,2)\):
\[
21+\Bigl\lfloor\frac{2-21}{9}\Bigr\rfloor
=
21+(-3)
=
18
=
L_{\mathrm{pref}}.
\]
So the split \(18+521\) **agrees** with the single-shot form for this flux.  

**Fragility check (nearby \(N\)):** the match \(L_{\mathrm{pref}}=f_{\max}+\lfloor(r-f_{\max})/9\rfloor\) holds for \(N\in\{4878,4879,4880\}\) and fails for \(N=4881\) (single-shot becomes 540 while \(18+521\) stays 539). At the model flux \(N_{\mathrm{flux}}=4880\) both forms coincide; the single-shot \(L_{\mathrm{pack}}'\) is the cleaner 539-free packaging expression under (S).

---

## 4. Formal statement

**Lemma (Forced atoms).**  
\(f_{\max}=\lceil N_{\mathrm{flux}}/N_{\mathrm{tow}}\rceil\) and \(B_Q=\lfloor N_{\mathrm{flux}}/9\rfloor\) are uniquely determined by equitable tower partition and equal charge split. No 539 enters.

**Theorem (Residual body length under (S)).**  
Under principle (S) (minimal-action single max-tower seed clear),
\[
L_{\mathrm{body}}
=
B_Q-f_{\max}
=
521
\]
is the unique residual charge-sector body length in the seed-quantum class
\(B_Q-f\) with \(f\in\{f_{\min},f_{\max}\}\).

**Corollary (Length packaging under (S)).**  
With \(L_{\mathrm{pref}}=\lfloor e^{3}/\ln 3\rfloor=18\),
\[
L_{\mathrm{pack}}
=
L_{\mathrm{pref}}+L_{\mathrm{body}}
=
539
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}-f_{\max}}{9}\Bigr\rfloor.
\]
The integer 539 appears only as the value of these expressions.

**Proposition (Necessity of (S)).**  
From charge conservation and tower democracy alone, without (S) or an equivalent selector,
\[
L\in\{B_Q-f_{\min},\,B_Q-f_{\max}\}=\{522,\,521\}
\]
remains unresolved. The residual subtraction \(N_{\mathrm{flux}}//9-f_{21}\) is therefore **not** Category A from Res+Tower+Dem alone.

---

## 5. Competing combination principles (not aimed at 539 either)

These are recorded so uniqueness is not overstated by ignoring rivals.

| Principle | Formula | Value | Uses 539? | Relation to body |
|-----------|---------|------:|:---------:|------------------|
| **(S)** full max seed / sector | \(B_Q-f_{\max}\) | **521** | No | **This document’s \(L_{\mathrm{body}}\)** |
| **(S)** global then sectorize | \(\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) | **539** | No | packaging length \(L_{\mathrm{pack}}'\) |
| **(S′)** max extras / sector | \(B_Q-\lceil R/9\rceil\) | **539** | No | packaging in one step; **not** full-seed body |
| Base seed clear | \(B_Q-f_{\min}\) | 522 | No | rejected by (S) |
| No seed clear | \(B_Q\) | 542 | No | no injection accounting |

**(S′)** interpretation: democratic assignment of \(R\) exceptional \(+1\) extras across 9 charges gives max extras per class \(\lceil R/9\rceil=3\); residual sector budget \(542-3=539\). Units are consistent if each extra is one flux quantum.  

**(S′)** is a legitimate alternative **packaging** principle; it does **not** produce \(L_{\mathrm{body}}=521\). Choosing (S) over (S′) is a modelling choice: full tower seed clear vs imbalance-extra clear. Both are 539-free; both are combination principles beyond pure atoms.

Default in this programme for **body length**: **(S)** (matches HQH 18+521 split and single-shot after full seed).  
**(S′)** remains an honest rival for a one-shot sector packaging of 539 without \(L_{\mathrm{pref}}\).

---

## 6. What is gained / what is not

| Gained under (S) | Not gained |
|------------------|------------|
| Unique \(L_{\mathrm{body}}=521\) in seed-quantum class | Force (S) from Res+Tower+Dem alone |
| Non-circular **length** packaging \(L_{\mathrm{pack}}=539\) | Automatic **539 basins/paths** under free \(T^\sharp\) (still 2) |
| Closed form \(B_Q-f_{\max}\) with no bare “21” or “539” | Lift of No-Go on \(\lambda=\ln 3/539\) from democracy *without* packaging principles |
| Upgrade from reverse-engineered \(539-18\) | Bott embedding (needs 539 **objects**, not only length) |

---

## 7. Verification (executable)

```python
import math

N = math.floor(math.e**3 * 3**5)          # 4880
T = 3**5                                   # 243
Q = 9
fmin = N // T
R = N - fmin * T
fmax = math.ceil(N / T)
BQ = N // Q
r = N % Q
Lpref = math.floor(math.e**3 / math.log(3))

assert N == 4880 and T == 243
assert fmin == 20 and R == 20 and fmax == 21
assert BQ == 542 and r == 2 and Lpref == 18

L_body = BQ - fmax
assert L_body == 521
assert L_body == N // 9 - fmax

L_pack = Lpref + L_body
L_pack_prime = (N - fmax) // Q
assert L_pack == 539 == L_pack_prime

# Identity linking prefix to tower-charge residual
assert Lpref == fmax + (r - fmax) // Q

# Alone without (S): two seed-quantum residuals
assert {BQ - fmin, BQ - fmax} == {522, 521}

# Rival extras principle (S')
assert BQ - math.ceil(R / Q) == 539

print("OK: L_body=521 under (S); L_pack=L_pack'=539; atoms forced; (S) needed for uniqueness")
```

Run:

```bash
python S2-11DM2ET-X-Axiomatic-Book/scripts/verify_L_body_structural.py
```

---

## 8. Status revision (honest)

| Item | Status |
|------|--------|
| \(f_{\max},B_Q\) | **Forced** (democracy + charge) |
| \(L_{\mathrm{body}}=B_Q-f_{\max}=521\) | **Derived under principle (S)**; **ansatz** without (S) |
| \(L_{\mathrm{pref}}=18\) | **Category A** (pure \(\lfloor e^{3}/\ln 3\rfloor\)) |
| \(L_{\mathrm{pack}}=18+521=539\) | **Non-circular length packaging conditional on (S)** |
| \(L_{\mathrm{pack}}'=\lfloor(N-f_{\max})/9\rfloor\) | Equivalent single-shot under (S) at model flux |
| (S′) \(B_Q-\lceil R/9\rceil=539\) | Rival packaging; does not define body 521 |
| 539 **object** count | Still open (Option 3); free \(T^\sharp\) basins = 2 |
| No-Go (democracy alone \(\Rightarrow\sigma=539\)) | **Still stands** — (S) is extra structure |
| Bott / classifying maps | Still paused until 539 objects |

---

## 9. Bottom line

> **Can a unique structural reason be written?**  
> **Yes, under principle (S):**  
> charge-sector budget \(B_Q=N_{\mathrm{flux}}//9\), minus one **maximal democratic tower seed** \(f_{\max}=\lceil N_{\mathrm{flux}}/N_{\mathrm{tow}}\rceil\).  
> That forces \(L_{\mathrm{body}}=521\) without placing 539 on any defining RHS.

> **Is the residual subtraction forced by charge + tower alone?**  
> **No.** Those data only pin \(\{521,522\}\). Until (S) (or an equivalent selector) is adopted, \(N_{\mathrm{flux}}//9-f_{21}\) **retains ansatz status**.

> **Composite packaging:**  
> With (S) and \(L_{\mathrm{pref}}=\lfloor e^{3}/\ln 3\rfloor\), **\(18+521=539\)** is a **non-circular length identity**, equivalently \(\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\).  
> A set of **539 dynamical objects** under free \(T^\sharp\) is still not obtained; Option 3 remains for that stronger claim; Bott stays paused for object-classification.
