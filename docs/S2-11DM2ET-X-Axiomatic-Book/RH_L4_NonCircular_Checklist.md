# L4 — Non-circular hypotheses checklist

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. No model constants.

**Purpose:** list every hypothesis that may enter M1.2–M1.4 / target lemma work, and mark circularity risk relative to RH.

**Language purity (prior):** **Axiom ZLA** — a theorem about the location of the zeros of \(\zeta\) may use only objects that are functions of \(\zeta\), its Euler product, its zeros, or classical number-theoretic auxiliaries.  
See `RH_Zeta_Language_Admissibility.md`. L4 is about *which hypotheses*; ZLA is about *which symbols*.

---

## Allowed (classical / unconditional / finite-height)

| ID | Hypothesis | Circularity vs RH | Status in programme |
|----|------------|-------------------|---------------------|
| H0 | Classical \(\zeta\) analytic continuation, FE, Euler product for \(\sigma>1\) | None | Used freely |
| H1 | GHK hybrid identity (Thm 1) | Unconditional | Used |
| H2 | Odlyzko zero list up to fixed \(T_0\) (HD-low) | Finite check; assumes listed zeros only | Diagnostics only |
| H3 | Admissible \(c_1,c_2\) for fixed \(f_\star,K\) | Effective majorants; not RH | Written |
| H4 | Zero-density / \(N(T)\) classical bounds | Weaker than RH; standard | Available for \(c_3\) |
| H5 | \(k=2\) fourth-moment theorem | Proved | Surveyed |

## Conditional (must be stated, not hidden)

| ID | Hypothesis | Risk | Notes |
|----|------------|------|-------|
| C1 | **HD** at unbounded height (isolation + spacing) | If HD uses RH-scale zero free regions, circular | Use classical density or finite HD-low |
| C2 | Pair correlation / PCC | Conjectural about zeros of \(\zeta\); **ZLA-admissible** as a hypothesis | Classical almost-all simplicity/criticality under PCC; **O-PC open** for phase bounds (`RH_Pair_Correlation_Practical_Status.md`) |
| C3 | Moment conjectures \(k\ge 3\) | Open | Not used for M1.2 |
| C4 | DRH-scale prime error \(c(x)=x+o(x^{1/2}\log x)\) | Equivalent to strong RH forms on the line | Akatsuka on-line only |
| C5 | \(Y=\sup\operatorname{Re}\rho=1/2\) | **Is RH** | Target lemma is contrappositive/open |

## Forbidden in theorem statements

| ID | Material |
|----|----------|
| F1 | \(G_4\), \(\mu\), \(E_{\mathrm{leak}}\), 539.9 s |
| F2 | Residual packaging integers as zeta lemmas |
| F3 | Invented numerical \(c_i\) without majorant tree |
| F4 | Function-field theorems as proofs for \(\zeta\) |

## Standing rule

Any completed proof of the target lemma or of M1.2 must:

1. satisfy **Axiom ZLA** (language: only \(\zeta\), Euler product, zeros, classical auxiliaries);  
2. cite only **H0–H5** plus **explicitly labelled** C-hypotheses that are **not equivalent to RH**.

Finite-height diagnostics may use H2 freely without claiming unbounded RH.

---

## One-liner

**L4 freezes the non-circularity ledger under ZLA: classical GHK and effective \(c_i\) are allowed; RH-strength zero-free regions, invented constants, and non-zeta language are not.**
