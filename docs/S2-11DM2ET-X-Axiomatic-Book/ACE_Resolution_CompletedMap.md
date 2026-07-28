# ACE Resolution — Completed map, stationary mean, bridge

## Resolved chain (no \(539\), \(61\), \(G_4\) in steps 1–2)

### (1) Completion on density-\(2/3\) impossible set — **derived**

**Rule \(T^\sharp\) (min charge defect):**

| \(n \bmod 3\) | Action |
|---------------|--------|
| \(0\) | \(n/3\) |
| \(1\) | \(\lfloor(4n+2)/3\rfloor\) |
| \(2\), feasible | \(T(n,k^\ast)\) exact \(Q\)-preserve |
| \(2\), impossible \(\mathcal{I}\) | \(T(n,k_\delta)\) with \(k_\delta\in\{0,1,2\}\) minimizing charge defect \(\delta_9(T,n)\); ties → minimal \(k\) |

**Why derived (not a free candidate):**
- Correction family and \(Q=n\bmod 9\) already published  
- Only three inequivalent \(k\) mod 9  
- Exact preserve when possible; else **minimal defect** (canonical)  
- Minimal-\(k\) tie-break (same minimality as \(k^\ast\))  

No \(539\), \(61\), \(G_4\) enter the definition.

---

### (2) Stationary expectation — **strictly negative (ACE)**

Under **flux democracy as 3-adic equidistribution** of higher digits (243-tower average):

\[
\pi_3 \equiv \text{uniform on }\{0,1,2\}
\]

Asymptotic rates under \(T^\sharp\): \(\ln\frac13,\;\ln\frac43,\;\ln\frac13\).

\[
\boxed{
\mathbb{E}_\pi[\chi]
= \tfrac23\ln\tfrac13 + \tfrac13\ln\tfrac43
= \ln\bigl(4^{1/3}/3\bigr)
\approx -0.6365141683
< 0
}
\]

\[
\chi_{\min}
= -\mathbb{E}_\pi[\chi]
= \ln\bigl(3/4^{1/3}\bigr)
\approx 0.6365141683
\]

\[
\lambda_{\mathrm{mean}}
= \exp(\mathbb{E}_\pi[\chi])
= 4^{1/3}/3
\approx 0.52913
< 1
\]

**ACE status for this completed map: established** (conditional on democratic equidistribution).

---

### (3) Bridge — **only after (2); no target length inserted**

\[
\boxed{
N_\star
= \Bigl\lceil \frac{\ln N_{\mathrm{flux}}}{\chi_{\min}} \Bigr\rceil
= \Bigl\lceil \frac{\ln 4880}{\chi_{\min}} \Bigr\rceil
= 14
}
\]

Uses only \(N_{\mathrm{flux}}=4880=\lfloor e^3\cdot 3^5\rfloor\) and \(\chi_{\min}\).

| Claim | |
|-------|--|
| Inserts \(539\)? | **No** |
| Equals HQCC depth \(539\)? | **Not claimed** |
| Meaning | E-fold contraction depth vs flux budget under \(\mathbb{E}_\pi[\chi]\) |

Any link \(N_\star\leftrightarrow 539\) needs a **separate** non-circular argument (e.g. tower seed composition).

---

## What the No-Go still blocks vs what is lifted

**Essential No-Go claim (stands):** flux democracy + residue structure + completed charge-preserving map yield strict contraction and a short e-fold depth (\(N_\star=14\)), but they **do not** determine the model’s **539-step** orbit or a unique dictionary that inserts that number.

| | |
|--|--|
| Circular \(\lambda=\ln 3/539\) from assuming \(539\) | Still blocked |
| Mean rate \(\lambda_{\mathrm{mean}}=4^{1/3}/3<1\) without assuming \(539\) | **Available** |
| Non-circular bound of **order 14** | **Available** (\(N_\star\)) |
| Integer **539** from ACE/bridge | **Does not follow** |
| Unique \(w_j=539+61j\) from ACE alone | **Unforced** |
| Long resonant structure (fixed count, holographic window, phase-lock) | **Outside pure contraction** |
| Empirical Resonant Attractor ~ \(539.9\) | **Legitimate route; no presupposition** |

Canonical ledger: `ACE_Status_of_Record.md`

---

## Order of operations (satisfied)

```text
(1) Complete on I     ✓  min-defect T^♯
(2) E_π[χ] < 0        ✓  ln(4^{1/3}/3)
(3) Bridge Ψ          ✓  N_⋆=14 (not 539)
(4) Full democracy ⇒ 539 dictionary   ✗ not claimed
```

---

## Files

- `ACE_Resolution_CompletedMap.tex` — formal theorems  
- `ACE_Resolution_CompletedMap.md` — this summary  
- Prior: `k_n_Distribution_Analysis.md`, `NoGo_*.tex`, `ACE_Open_*.tex` (historical open statement; resolution supersedes for \(T^\sharp\))
