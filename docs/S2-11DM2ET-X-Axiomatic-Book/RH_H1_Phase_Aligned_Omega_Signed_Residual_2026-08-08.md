# RH H1 — Phase-Aligned Omega for the Signed Residual (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** B_θ · Form B · RH  
**Vessel:** `RH_Signed_Sum_Attack.md` Theorem 4.1 / Form B  
**Results:** `rh_ranked_hopes5_results.json`

---

## 1. Object (Form B ≡ B_θ off-line)

After proved residual formula (19):

\[
S_X(\rho_\star)
=
\rho_\star\int_2^X\frac{\psi(x)-x}{x^{\rho_\star+1}\log x}\,dx
+
B_X
+
E_X(T).
\]

**Form B.** \(\limsup_{X\to\infty}\bigl|\int_2^X(\psi-x)x^{-\rho_\star-1}(\log x)^{-1}dx\bigr|=\infty\).

---

## 2. What is already proved

| Item | Status |
|------|--------|
| Residual formula; self log log cancel | **Proved** |
| ZF **upper** bound on residual | **Proved** |
| Classical Ω: ψ−x = Ω(x^{β⋆}/|ρ⋆|) if ζ(ρ⋆)=0 | **Classical** |
| Phase alignment of those Ω points with x^{iγ⋆} | **Open** |

---

## 3. Named conditional: PAO(c, δ)

**PAO(c, δ).** There exist x_n→∞ and intervals [x_n, x_n(1+δ_n)] on which

\[
\operatorname{Re}\Bigl(e^{-i\gamma_\star\log x}(\psi(x)-x)x^{-\beta_\star}\Bigr)\ge c>0
\]

and the log-measure \(\int dx/(x\log x)\) over those intervals is bounded below by δ>0 i.o. (or sums to ∞).

**Conclusion (template):** Form B / |S_X|→∞ along a subsequence (admissible T(X)).

**Status:** **Hypothesis — not proved.**

Schematic measure demand: if c=O(1), a **positive fraction** of total log-measure \(\log\log X\) must be aligned — a strong multiplicative resonance hypothesis at ordinate γ⋆.

---

## 4. Duality with H2

H1 is a **lower bound** via resonance. H2 is an **upper bound** via cancellation. Dual; neither implies the other.

---

## 5. Resolution today

**False.** PAO named and obstruction frozen.

**Status code:** `RH_H1_PHASE_ALIGNED_OMEGA_2026-08-08`

*Per aspera ad astra.*
