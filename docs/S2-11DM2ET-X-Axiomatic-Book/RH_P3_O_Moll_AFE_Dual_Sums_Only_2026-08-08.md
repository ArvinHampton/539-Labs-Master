# RH P3 — O-Moll from AFE Dual Sums Only (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not construct a working O-Moll. Does not prove O-TL.**  
**Forbidden:** Levinson / Conrey / zero-count mollifiers as O-Moll

---

## 1. Forbidden list

- Levinson mollifier (zeros on the critical line)  
- Conrey long mollifiers (proportion on the line)  
- Any \(\mu\)-polynomial designed only for horizontal zero detection  

These scored **−1** (false friends) in the resonance/Selberg explore.

---

## 2. AFE surface (only allowed design surface)

\[
\zeta(s)
=
\sum_{n\le u}n^{-s}
+
\chi(s)\sum_{n\le v}n^{s-1}
+
R_{\mathrm{AFE}}(s;u,v).
\]

Dual Dirichlet polynomials \(F(s)\), \(G(1-s)\) linked by \(\chi(s)\).

---

## 3. AFE-Moll skeleton (template — not a theorem)

1. Peel hybrid phase: \(\theta_X=\arg\zeta-\arg Z_X-\operatorname{Im}E\) (GHK).  
2. Replace \(\arg\zeta\) by \(\arg(F+\chi G+R)\) along the evaluation path.  
3. Choose \((u,v)\) and coefficients to amplify \(\operatorname{Im}\log P_X\), **not** \(\lvert F+\chi G\rvert\).  
4. Prove dual \(G\)-term and \(R\) do not destroy the phase lower bound.

**Blocker:** no classical optimization is known for \(\operatorname{Im}\log P_X\). Steps 3–4 remain open design.

---

## 4. Verdict

**Construction:** not found. **O-Moll:** still **OPEN**.

**Status code:** `RH_P3_OMOLL_AFE_ONLY_2026-08-08`

*Per aspera ad astra.*
