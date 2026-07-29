# Near-term residual unification kit

**Operations:**  
1. Pair permanent form class \([\alpha\otimes\delta f]\) with mixed cells  
2. Filter by packaging window \(W=L_{\mathrm{pref}}=18\)  
3. Pre-register sector↔band map  

**Locks respected (do not reopen):**  
- Thin form complex \(H^2(F)\cong\mathbb{Q}\cdot[\alpha\otimes\delta f]\); filled Tot acyclic  
- \(\eta\) exact; graph \(\beta_1=36B'-8\) independent of form \(H^2\)  
- Packaging \(18+521=539\) under Principle **(S)**  
- Free \(T^\sharp\) **Option 3** (two basins; not 539 free classes)  
- Public MT peaks do **not** encode 18/521  

**Provenance:** residual **(S)** only for (1)–(2). Dictionary (3) is **Category B** + data.  
**Probes:** `scripts/gf_pairing_window_probe.py` → `gf_pairing_window_results.json`.  
**RFC:** `Sector_Band_Dictionary_RFC.md` — D2 executed on CHB-MIT `chb01_01` (S1–S3 PASS → working Cat B; residual locks unchanged).  
**P+ research:** `Residual_P_plus_MultiScale.md` (stable permanent class; not theorem-locked).  
**Review:** `Multi_Angle_Unification_Review.md`.

---

## 0. Why these three

Cross-scale residual unification is **not** one continuum equation.  
It is **preservation of the mixed class and its pairings** under refinement and measurement.

```text
[α⊗δf]  ──(1) pairing──►  mixed squares S(a,b;i)
    │
    └──(2) window filtration W=18 ──►  shell vs tower pairing mass
    │
    └──(3) dictionary RFC ──►  DDG/MT bands (falsifiable Cat B)
```

---

## 1. Pair \([\alpha\otimes\delta f]\) with mixed cells

### 1.1 Definition (residual product)

Mixed 2-cell = square
\[
S(a,b;i)
=
\text{charge edge }a\to b\text{ at residual index }i
\times
\text{path edge }i\to i+1.
\]

Kronecker pairing with the permanent 2-cochain representative:
\[
\boxed{
\big\langle \alpha\otimes\delta f,\; S(a,b;i)\big\rangle
=
\alpha(a,b)\,\delta f(i)
}
\]
where \(\alpha(a,b)=\mathrm{sgn}(a-b)\) and \(\delta f(i)=\tau(x_{i+1})-\tau(x_i)\) on canonical core 0.

This evaluates the form class on the fundamental mixed cells dual to mixed graph 4-cycles (square boundaries), tying **Layer (F)** to **Layer (G)** without continuum geometry.

### 1.2 Global residual pairing mass

Over ordered pairs \(a<b\) (so \(\alpha(a,b)=-1\)):
\[
\Sigma
=
\sum_{i=0}^{B'-2}\sum_{0\le a<b\le 8}
\bigl|\alpha(a,b)\,\delta f(i)\bigr|
=
\binom{9}{2}\sum_i|\delta f(i)|
=
36\sum_i|\delta f(i)|.
\]

### 1.3 Locked residual numbers (canonical core 0)

| Quantity | Value |
|----------|------:|
| \(B'\) | 539 |
| Squares \(a<b\) | 19368 |
| Nonzero pairings | 8676 |
| \(\Sigma\) | **8676** |
| Graph \(\beta_1\) (independent) | 19396 \(=36B'-8\) |

**Interpretation:** nonzero mixed mass shows the permanent class is **detectable** on residual mixed cells. Absolute mass is path-order-insensitive under \(\delta f\mapsto -\delta f\) reverse; **window split** (§2) uses residual order.

### 1.4 Non-claims

- Not free \(T^\sharp\) cycle counts  
- Not continuum Stokes theorem  
- Not a security reduction  

---

## 2. Filter by packaging window 18

### 2.1 Definition under Principle (S)

\[
W
:=
L_{\mathrm{pref}}
=
\bigl\lfloor e^{3}/\ln 3\bigr\rfloor
=
18
\quad\text{(vertices on residual path)}.
\]

Edge partition:
\[
\begin{aligned}
E_{\mathrm{win}}
&=
\{0,1,\ldots,W-2\}
&&\text{\(17\) edges},
\\
E_{\mathrm{tow}}
&=
\{W-1,\ldots,B'-2\}
&&\text{\(521\) edges}.
\end{aligned}
\]

Note: \(17+521=538=B'-1\). The **521** here is edge count in the residual tower segment of the path, which **matches** the packaging body integer \(L_{\mathrm{body}}=521\) as path combinatorics under this split — still residual (S), not free dynamics.

### 2.2 Restricted pairing masses

\[
\Sigma_{\mathrm{win}}
=
36\sum_{i\in E_{\mathrm{win}}}|\delta f(i)|,
\qquad
\Sigma_{\mathrm{tow}}
=
36\sum_{i\in E_{\mathrm{tow}}}|\delta f(i)|,
\qquad
\Sigma_{\mathrm{win}}+\Sigma_{\mathrm{tow}}=\Sigma.
\]

### 2.3 Locked residual numbers (canonical core 0)

| Quantity | Value |
|----------|------:|
| Window edges | 17 |
| Tower edges | 521 |
| \(\Sigma_{\mathrm{win}}\) | 252 |
| \(\Sigma_{\mathrm{tow}}\) | 8424 |
| \(\Sigma_{\mathrm{win}}/\Sigma\) | \(\approx 0.02905\) |
| Target \(W/B'=18/539\) | \(\approx 0.03340\) |
| \(\sum|\delta f|_{\mathrm{win}}\) | 7 |
| \(\sum|\delta f|_{\mathrm{tow}}\) | 234 |

**Interpretation:** window filtration is a **homological shell diagnostic** on residual path prefixes. Proximity of \(\Sigma_{\mathrm{win}}/\Sigma\) to \(18/539\) is residual arithmetic under (S), **not** recovery of MT peak labels 18/521.

### 2.4 Non-claims

- Not empirical biology  
- Not “measured 18-step window in data”  
- Does not reopen free 539 basins  

---

## 3. Pre-register sector↔band map

### 3.1 Status

| Item | Status |
|------|--------|
| RFC document | `Sector_Band_Dictionary_RFC.md` |
| Default dictionary for first test | **D2**: 9 equal \(\log_{10} f\) bins |
| Pass/fail stats | S1–S3 (adjacent coupling, shell contrast, path-order surrogate) |
| Locked as theorem? | **No** — Category B until primary data |

### 3.2 Why D2

Does **not** force \(9=12\) (DDG band count). Orientation high→low or low→high must be fixed in the pre-registration before looking at results.

### 3.3 Decision rule

| Outcome | Residual math | Bio metaphor |
|---------|---------------|--------------|
| S1–S2 pass | Unchanged | Working Cat B dictionary |
| Fail | Unchanged | Retire sector↔band slogan for that dataset |
| No data | Unchanged | RFC stays open |

### 3.4 Non-claims

- Not Orch-OR proof  
- Not 18/521 peak recovery  
- Not Option 3 lift  

---

## 4. Unified residual reading

\[
\begin{aligned}
&\text{permanent class }
&&[\alpha\otimes\delta f]\in H^2(F),
\\
&\text{pairing }
&&\langle\alpha\otimes\delta f,S(a,b;i)\rangle=\alpha(a,b)\,\delta f(i),
\\
&\text{window split }
&&E_{\mathrm{win}}\sqcup E_{\mathrm{tow}}
\text{ with }|E_{\mathrm{tow}}|=521,\ |E_{\mathrm{win}}|=17,
\\
&\text{measurement bridge }
&&\text{D2 dictionary + S1–S3 (Cat B)}.
\end{aligned}
\]

**Unification (residual language):** keep \([\alpha\otimes\delta f]\) and its pairings under refinement, gluing, and (when data exist) dictionary pullbacks — **not** fill the product, **not** free dynamics, **not** continuum TTC by declaration.

---

## 5. Verification

```text
python scripts/gf_pairing_window_probe.py
```

Asserts: \(\Sigma\) formula, window/tower edge counts \(17+521=538\), \(\Sigma_{\mathrm{win}}+\Sigma_{\mathrm{tow}}=\Sigma\), \(\beta_1=36B'-8\), provenance flags.

---

## 6. Bottom line

> **Pair, filter, dictionary** — three residual operations that open cross-scale contact without reopening Option 3 or the thin-complex lock.  
> Pairing and window filtration are **executed residual numbers**.  
> Sector↔band map is **pre-registered Cat B**, waiting on data.

*Per aspera ad astra.*
