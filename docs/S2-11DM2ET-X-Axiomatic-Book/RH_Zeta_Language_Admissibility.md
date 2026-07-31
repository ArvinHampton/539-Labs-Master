# Zeta language admissibility (ZLA)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** — methodological axiom for theorems about zeros of \(\zeta\).  
**Does not prove RH.** Freezes what may appear inside a theorem statement about the location of the zeros of \(\zeta\).

**Companions:** `RH_L4_NonCircular_Checklist.md`, `RH_L1_Phase_Functional_CatA.md`, `CLAIM_TABLE_RH_Debt.md`.

---

## Axiom (ZLA)

> **A theorem about the location of the zeros of \(\zeta\) may use only objects that are functions of \(\zeta\), its Euler product, its zeros, or classical number-theoretic auxiliaries.**

This is the **language purity** rule for the pure Category A phase programme. It is independent of whether any particular bound is proved; it constrains the **signature** of admissible statements.

---

## 1. Admissible objects

| Class | Examples |
|-------|----------|
| **Functions of \(\zeta\)** | \(\zeta(s)\), \(\zeta'/\zeta\), \(\log\zeta\) (continuous branches off zeros/poles), \(\lvert\zeta\rvert\), Hadamard product factors built from \(\zeta\) |
| **Euler product** | \(\prod_p(1-p^{-s})^{-1}\) for \(\sigma>1\); partial products \(P_x\), \(P_X\); Dirichlet series \(\sum\Lambda(n)n^{-s}\), \(\sum\Lambda(n)/(n^{s}\log n)\) |
| **Zeros** | Nontrivial zeros \(\rho\), ordinates \(\gamma\), multiplicities \(m\), \(Y=\sup\operatorname{Re}\rho\), zero-counting \(N(T)\), explicit formulae summing over \(\rho\) |
| **Classical number-theoretic auxiliaries** | Primes; \(\Lambda\), \(\psi\), \(\pi\); \(\Gamma\), \(\xi\); Stieltjes constants; classical zero-density estimates; Ingham–von Mangoldt remainders; GHK hybrid \(P_X,Z_X,U,E_1\); smooth test functions of compact support used only to truncate arithmetic/spectral sums; absolute effective constants arising from such truncations |

Smooth weights \(f,u\) and majorant constants \(c_1,c_2\) built from them are **auxiliaries** in the sense of analysis of \(\zeta\): they do not introduce external physical or residual-model data.

---

## 2. Inadmissible objects (in theorem statements about zeros of \(\zeta\))

| Class | Examples |
|-------|----------|
| Model / residual packaging | \(G_4\), \(\mu\), \(E_{\mathrm{leak}}\), \(539.9\,\mathrm{s}\), Option-3 free dynamics as zeta lemmas |
| Residual geometric stack | \(K^+\), \(r_W\), shell \(18/521\), \(\mathcal{O}_{\mathrm{res}}\) as inputs to a zero-location theorem |
| Resonant Algebra / HQCC | Security or attractor language as proof ingredients for \(\zeta\) |
| Invented constants | Numerical \(c_i\) without a classical majorant tree from admissible data |
| Category-B continuum fillings | Continuum spin / hopfion material as zeta lemmas |
| Unrelated \(L\)-functions **as if they were \(\zeta\)** | Function-field theorems may motivate, but **transfer is not automatic**; a theorem “for \(\zeta\)” must be proved for \(\zeta\) |

Diagnostics and motivation notes may mention inadmissible objects **outside** theorem environments. They must not appear in the hypothesis or conclusion of a zero-location theorem.

---

## 3. Relation to L4 (non-circularity)

| Layer | Role |
|-------|------|
| **ZLA** | *What symbols may occur* (language / ontology of the theorem) |
| **L4** | *Which hypotheses may be assumed* without circular appeal to RH |

Both are required. A statement can be ZLA-clean yet circular (e.g. assume a zero-free region equivalent to RH), or non-circular yet ZLA-dirty (e.g. use \(G_4\)). **The programme requires both ZLA and L4.**

---

## 4. Worked checks on current track

| Object / statement | ZLA? | Notes |
|--------------------|------|-------|
| Target lemma for \(A_X=\mathrm{avg}\,\arg P_Y\) | **Yes** | \(P_Y\) from Euler/von Mangoldt; \(A_X\) is a function of that product |
| M1 / \(R_{\mathrm{IvM}}\) / \(\mathcal{R}_x^{\mathrm{EP}}\) | **Yes** | Explicit formula for \(\zeta\) |
| M1.2-GHK, \(c_1,c_2\) from \(f_\star\) | **Yes** | Classical hybrid + analysis auxiliaries |
| Akatsuka partial products | **Yes** | Classical |
| Fourth moment \(k=2\) | **Yes** | Classical |
| Function-field RMT as **motivation** | **Yes** (motivation only) | Not a proof for \(\zeta\) |
| “Debt argument” with \(E_{\mathrm{leak}}\) | **No** (as theorem) | Quarantined; status already `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` |
| Residual \(539\) in a zero theorem | **No** | Forbidden |

---

## 5. Formal consequences for the phase programme

1. Every claimed theorem about \(\operatorname{Re}\rho\) or about \(Y\) must have a **ZLA audit**: every symbol is classified under §1 or rejected under §2.  
2. Partial Euler products and continuous arguments \(\theta_x\), \(A_X\) are **in-language**: they are built from the Euler product / \(\Lambda\).  
3. Random-matrix models may appear only as **heuristic commentary**, not as hypotheses of a zero-location theorem for \(\zeta\), unless reduced to classical statements about zeros of \(\zeta\).  
4. ZLA does **not** by itself prove RH; it only keeps the theorem language pure.

---

## 6. Status

| Item | Status |
|------|--------|
| Axiom ZLA | **Frozen** (this note) |
| Alignment with L4 / Cat A firewall | **Yes** |
| RH / target lemma | **Open** |

---

## One-liner

**Theorems locating the zeros of \(\zeta\) may mention only \(\zeta\), its Euler product, its zeros, and classical number-theoretic auxiliaries — nothing from the residual model stack or other external packaging.**

*Per aspera ad astra.*
