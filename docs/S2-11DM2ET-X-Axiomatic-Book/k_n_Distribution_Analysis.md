# Distribution of the charge-correcting exponent \(k(n)\)

## Definition (published form)

For \(n \equiv 2 \pmod{3}\), the charge-preserving step is

\[
T(n,k) \;=\; \frac{n+1}{3} + 2\cdot 3^{k},
\qquad k\in\mathbb{Z}_{\ge 0},
\]

with **minimal** \(k\) such that the 11D flux charge is preserved:

\[
Q(n) \;=\; n \bmod 9,
\qquad
T(n,k) \equiv n \pmod{9}.
\]

(Corpus: S²-11DM²ET-X model statement — “same residue mod 9”.)

Other residue classes use ordinary \(T_3\) branches (no \(k\)).

Script: `scripts/analyze_k_distribution.py`

---

## 1. Structural fact: only three distinct corrections mod 9

| \(k\) | \(2\cdot 3^{k}\) | \(\bmod 9\) |
|------:|-----------------:|------------:|
| 0 | 2 | 2 |
| 1 | 6 | 6 |
| ≥2 | \(2\cdot 3^{k}\) | **0** |

**Corollary.** For mod-9 matching, \(k\ge 3\) never improves on \(k=2\).  
If a preserving \(k\) exists, a minimal one satisfies

\[
k(n)\in\{0,1,2\}.
\]

So \(k\) **cannot** become arbitrarily large under this published family.  
(The informal claim that “for other \(n\) the minimal \(k\) is large enough that the ratio becomes arbitrarily large” is **false** for \(Q\bmod 9\) with additive \(2\cdot 3^{k}\).)

---

## 2. Complete classification: \(k\) is a function of \(n \bmod 27\)

Since \((n+1)/3\) for \(n\equiv 2\pmod{3}\) depends on \(n\bmod 27\) when reduced mod 9, the existence and value of \(k^\ast\) are **periodic with period 27**.

Among the 9 classes with \(n\equiv 2\pmod{3}\):

| \(n \bmod 27\) | \(n \bmod 9\) | \(k^\ast\) |
|---------------:|--------------:|----------:|
| 2 | 2 | **impossible** |
| 5 | 5 | **impossible** |
| 8 | 8 | **impossible** |
| 11 | 2 | **impossible** |
| 14 | 5 | **2** |
| 17 | 8 | **0** |
| 20 | 2 | **impossible** |
| 23 | 5 | **1** |
| 26 | 8 | **impossible** |

### Densities (uniform over branch-2 integers)

| Event | Probability |
|-------|-------------|
| No preserving \(k\) (impossible) | \(6/9 = 2/3\) |
| Feasible | \(3/9 = 1/3\) |
| \(k=0\) \| feasible | \(1/3\) (class 17) |
| \(k=1\) \| feasible | \(1/3\) (class 23) |
| \(k=2\) \| feasible | \(1/3\) (class 14) |

\[
\mathbb{E}\bigl[k \mid \text{feasible}\bigr] \;=\; 1,
\qquad
\max k \;=\; 2.
\]

Monte Carlo (\(10^6\) values of \(n\equiv 2\pmod{3}\), \(n<3\cdot 10^6\)): matches these fractions exactly (periodicity).

---

## 3. Logarithmic expansion factor on the feasible set

For feasible \(n\) with fixed \(k\in\{0,1,2\}\),

\[
\frac{T(n,k)}{n}
= \frac{n+1}{3n} + \frac{2\cdot 3^{k}}{n}
\;\xrightarrow{n\to\infty}\;
\frac13.
\]

\[
\chi(n) \;=\; \ln\frac{T(n,k)}{n} \;\xrightarrow{n\to\infty}\; \ln\frac13 \approx -1.0986.
\]

Empirical mean on feasible \(n<3\cdot 10^6\): \(\mathbb{E}[\chi\mid\mathrm{feas}] \approx -1.08\) (approaching \(\ln\frac13\)).

**No runaway expansion from large \(k\)** — \(k\) is bounded and the \(3^{k}/n\) term vanishes as \(n\to\infty\).

---

## 4. Histogram (feasible branch-2 only)

```text
k |  P(k|feasible) |  role
--+----------------+------------------
0 |     1/3        |  n ≡ 17 (mod 27)
1 |     1/3        |  n ≡ 23 (mod 27)
2 |     1/3        |  n ≡ 14 (mod 27)
```

```text
Full branch-2 mass:
  impossible |████████████████████| 2/3
  k=0        |██████              | 1/9
  k=1        |██████              | 1/9
  k=2        |██████              | 1/9
```

---

## 5. Consequences for the ACE

### What this analysis **settles**

1. Under the published rule \(T=(n+1)/3+2\cdot 3^{k}\) + \(Q=n\bmod 9\):  
   **\(k(n)\) is bounded, periodic, and fully known.**
2. The distribution of \(k\) on the feasible set is **uniform on \(\{0,1,2\}\)** and **independent of global orbit length** (no \(539\), \(61\), \(G_4\)).
3. The fear that \(\mathbb{E}[\chi]\) is ruined by arbitrarily large \(k\) **does not apply** to this family.

### What remains **open** for a full ACE

| Gap | Why it matters |
|-----|----------------|
| **(G1) Infeasible mass \(2/3\)** | For \(n\bmod 27\in\{2,5,8,11,20,26\}\), **no** \(k\) preserves \(Q\). The map is not defined on all of \(\{n\equiv 2\pmod{3\}\) by this rule alone. Need a secondary rule (reject step, different correction, leave subspace, …). |
| **(G2) Invariant measure** | ACE needs \(\mathbb{E}[\chi]\) along **trajectories** in the charge-preserving subspace, not only the uniform density on branch-2 integers. Markov structure on \(\mathbb{Z}/27\mathbb{Z}\) (or larger) for the **full** map including branches \(0,1\) is still required. |
| **(G3) Bridge** | Even a negative \(\mathbb{E}[\chi]\) does not force \(\sigma=539\) (ACE depth is \(N_\star=14\), distinct). |

### Revised ACE pathway (sharper than before)

**Step A (done here).**  
Classify \(k\) on branch 2: periodic mod 27, \(k\in\{0,1,2\}\) or impossible.

**Step B (open).**  
Define the map on the impossible classes (must be part of the official charge-preserving dynamics).

**Step C (open).**  
Build the Markov chain on the finite state (e.g. \(n\bmod 27\) or \(\bmod 9\) plus branch) induced by the **completed** map; compute the stationary mean

\[
\mathbb{E}_\pi[\chi]
= \sum_s \pi(s)\,\ln\frac{T(s)}{n\text{-factor}(s)}
\]
in the large-\(n\) limit (branch rates \(\ln\rho_r\) plus \(o(1)\)).

**Step D (open).**  
If \(\mathbb{E}_\pi[\chi]\le -\chi_{\min}<0\) with no input of \(539\), that **is** the ACE.  
Then supply bridge \(\Psi(\chi_{\min},243,\ldots)\to N_\star\).

---

## 6. Comparison to unrestricted mean

| Quantity | Value |
|----------|------:|
| Unrestricted \(\frac13\ln(8/27)\) | \(-0.405465\ldots\) |
| Branch-2 unrestricted \(\ln(2/3)\) | \(-0.405465\ldots\) |
| Feasible charge-preserving \(\chi\to\ln(1/3)\) | \(-1.0986\ldots\) |
| \(\mathbb{E}[k\mid\mathrm{feas}]\) | \(1\) |
| \(\max k\) | \(2\) |
| \(P(\mathrm{impossible}\mid n\equiv 2\pmod{3})\) | \(2/3\) |

On the feasible set, charge preservation is **more contractive** at leading order (\(\to 1/3\) vs \(2/3\)), because the rule uses \((n+1)/3+\ldots\) rather than the ordinary \((2n+1)/3\) continuum ratio.

---

## 7. Bottom line (sharpened open problem)

The open problem is **sharpened rather than solved**.

**Proved by this analysis:** no runaway expansion; \(k\) bounded and classified.

**What remains (strict order):**

1. **Complete** the dynamics on the density-\(2/3\) impossible set \(\mathcal{I}\)  
   (projection, rejection rule, or alternative charge-preserving branch).
2. **Compute** \(\mathbb{E}_\pi[\chi]\) for a **stationary** measure \(\pi\) of the resulting map,  
   from residue Markov structure + 243-tower average **alone** (no \(539\), \(61\), \(G_4\)).
3. **Only after** a strictly negative stationary mean: a separate **bridge**  
   \(\Psi(\chi_{\min},243,\ldots)\to N_\star\) for a candidate integer orbit length.

Until the completed map and its stationary expectation are exhibited, the ACE stays **open** and the **No-Go stands**.  
New information eliminates runaway expansion; it does **not** yet supply the missing stationary average or the non-circular bridge to 539.

Formal open problems: `ACE_Open_ChargePreserving.tex` (Op. complete → ACE → bridge).
