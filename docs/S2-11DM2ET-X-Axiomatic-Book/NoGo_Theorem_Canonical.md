# No-Go Theorem (canonical)

## Definition

Assume **only** the following data:

1. the **residue-class structure** of the ternary map \(T_3\) (including the published charge-preserving correction that restores \(Q = n \bmod 9\));
2. the **topology of the 243** Kaluza–Klein towers;
3. the **democratic partition** of the flux integer **4880** that produces the initial seeds **20** and **21**;
4. **any completion** of the map on the previously impossible residue classes that is fixed solely by **minimality of the charge defect** among \(k \in \{0,1,2\}\)  
   (the completed map \(T^\sharp\)).

**Do not** assume any numerical bound that already contains the integer **539**, the puncture count **61**, or the period **539.9**.

Then the following hold:

| | Conclusion |
|--|------------|
| **(a)** | Flux democracy cannot break the circularity of the contraction-factor argument that sets \(\lambda = \ln 3 / 539\). |
| **(b)** | The specific Banach rate \(\lambda = \ln 3 / 539\) cannot be derived from the data above. |
| **(c)** | No unique generational dictionary that inserts the number **539** (in particular the windings \(w_j = 539 + 61\,j\)) is forced by those data. |

Equivalently, the following programme claims are **blocked** (ruled out as consequences of the assumed data alone):

| | Blocked programme claim |
|--|-------------------------|
| **(a′)** | Flux democracy breaks the circularity of \(\lambda = \ln 3 / 539\). |
| **(b′)** | \(\lambda = \ln 3 / 539\) follows from the assumed data. |
| **(c′)** | The dictionary \(w_j = 539 + 61\,j\) is forced by the assumed data. |

---

## Derivation and equations

Local logarithmic expansion factors of the ordinary map:

\[
\chi_0 = \ln\frac13,\qquad
\chi_1 = \ln\frac43,\qquad
\chi_2 = \ln\frac23.
\]

Uniform average (a priori negative):

\[
\frac13(\chi_0+\chi_1+\chi_2)
= \frac13\ln\frac{8}{27}
\approx -0.405.
\]

After the charge-preserving completion \(T^\sharp\), the leading ratio on every branch-2 step tends to \(1/3\). Under natural 3-adic equidistribution consistent with the 243-tower average:

\[
\mathbb{E}_\pi[\chi]
= \frac23\ln\frac13 + \frac13\ln\frac43
= \ln\Bigl(\frac{4^{1/3}}{3}\Bigr)
\approx -0.6365
< 0.
\]

Mean contraction rate:

\[
\lambda_{\mathrm{mean}}
= \frac{4^{1/3}}{3}
\approx 0.529
< 1.
\]

Non-circular e-fold bound from this rate and the flux integer:

\[
N_\star
= \Bigl\lceil
\frac{\ln 4880}{\bigl|\mathbb{E}_\pi[\chi]\bigr|}
\Bigr\rceil
= 14.
\]

**None** of these quantities equals **539**, and **none** of the steps that produce them inserts the number **539**.

---

## Proof

1. **Democracy fixes only initials.**  
   The democratic partition fixes only the initial seeds. It supplies no information about the mean size of the charge-correcting exponent along later iterates that would determine a Lipschitz constant **already containing 539**. Therefore it cannot break the circularity of \(\lambda = \ln 3/539\).  
   → **(a)**.

2. **What the data do determine.**  
   Residue Markov structure together with the completed map \(T^\sharp\) yields a strictly negative stationary mean  
   \(\mathbb{E}_\pi[\chi] \approx -0.6365\).  
   That derivation uses only residue probabilities and the asymptotic ratio \(1/3\); it does **not** use the integer 539.  
   The resulting e-fold depth is **14**, not **539**.  
   → **(b)** (the rate that follows is \(\lambda_{\mathrm{mean}}\), not \(\ln 3/539\)).

3. **Contradiction if \(\lambda = \ln 3/539\) were forced.**  
   Suppose, for contradiction, that the same data forced \(\lambda = \ln 3/539\).  
   Then the Banach fixed-point estimate would recover a step count of order **539**.  
   But the only Lipschitz-scale constant the data actually determine is \(\lambda_{\mathrm{mean}} \approx 0.529\), whose Banach / e-fold bound is of order **14**.  
   Therefore \(\lambda = \ln 3/539\) is an **additional assumption**, not a consequence.  
   Any generational dictionary that embeds **539** (in particular \(w_j = 539 + 61\,j\)) inherits that extra assumption and is likewise **unforced**.  
   → **(c)**.

4. **Long resonant trajectory.**  
   The long resonant trajectory of length **539** is maintained only by constraints **outside** the listed data: a fixed iteration count, a holographic window, and phase-locking to a pre-chosen period.  
   Those constraints are **not** implied by residue structure, tower topology, or flux democracy.

**Hence claims (a)–(c) hold. The no-go stands.**

---

## Corollary (empirical search)

The empirical search for a resonant period near **539.9** remains **permissible** precisely because it does **not** claim to derive that period from the data covered by the theorem.

The period is treated as a **hypothesis to be tested** after a **non-circular spectral estimate** has been obtained  
(periodogram / multitaper / Lomb–Scargle; bootstrap free of 539.9; compatibility only afterward).

See: `Empirical_PhaseLocking_Protocol.md`

---

## One-line ledger

| Derived from the assumed data | Not derived |
|-------------------------------|-------------|
| \(\frac13\ln(8/27)\approx -0.405\) | \(\lambda = \ln 3/\sigma = \ln 3/539\) |
| \(\mathbb{E}_\pi[\chi]\approx -0.6365\) | Model depth \(\sigma = 539\) |
| \(\lambda_{\mathrm{mean}}\approx 0.529\) | \(w_j = 539 + 61\,j\) |
| \(N_\star = 14\) (**≠** \(\sigma\)) | Democracy breaks circular Banach-539 |

**Macro split:** \(N_\star\) is only the ACE depth (14). HQCC depth is \(\sigma\) (539). See `PROVENANCE_TABLE.md`.

---

## Formal companions

| File | Role |
|------|------|
| `NoGo_Theorem_Canonical.tex` | Book-ready theorem environment |
| `NoGo_FluxDemocracy_ResonantAttractor.tex` / `.md` | Expanded chapter; ACE \(N_\star=14\) strengthens no-go for \(\sigma=539\) |
| `ACE_Resolution_CompletedMap.tex` | \(T^\sharp\), \(\mathbb{E}_\pi[\chi]\), \(N_\star=14\) |
| `ACE_Status_of_Record.md` | Full status ledger |
| `REFEREE_REPORT_Foundation_Layer.md` | Internal peer-review note |
| `PROVENANCE_TABLE.md` / `Provenance_and_DepthMacros.tex` | Integer provenance; \(N_\star=14\) vs \(\sigma=539\) |
