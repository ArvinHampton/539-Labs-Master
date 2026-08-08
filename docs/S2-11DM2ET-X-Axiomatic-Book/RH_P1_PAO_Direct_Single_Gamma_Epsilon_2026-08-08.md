# RH P1 — PAO Direct: Single-γ⋆ Lock and ε_other (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** PAO · B_θ · RH  
**Companions:** `RH_Signed_Sum_Attack.md`, `RH_H1_Phase_Aligned_Omega_Signed_Residual_2026-08-08.md`

---

## 1. Critical recast (star term is not the engine)

Phasing \((\psi-x)x^{-\beta_⋆}\) against \(e^{-i\gamma_⋆\log x}\) makes the **star** EF term **constant** (\(-1/\rho_⋆\)), not oscillatory.  
The pure star \(\log\log\) contribution to \(S_X\) already **cancelled** against \(\mathrm{Self}_X\).

**Correct PAO core = Form C:**
\[
\limsup_{X\to\infty}
\Biggl\lvert
\sum_{n\le X}
\frac{\Lambda(n)}{n^{\rho_⋆}\log n}
\Biggr\rvert
=\infty.
\]
This is the Dirichlet polynomial at **fixed** complex frequency \(\rho_⋆\) — equivalent to residual Form B via signed-sum Theorem 4.1.

---

## 2. ε_other control

| Regime | ε_other |
|--------|---------|
| Under **Iso_H** | Same-abscissa contamination only from \(\bar\rho_⋆\); left zeros smaller by power of \(X\) |
| **Unconditional** | Same-abscissa competitors can cancel main Ω coefficients |

**Template EO(Iso_H):** under Iso_H, same-abscissa \(\varepsilon\) controlled.  
**Status:** conditional on Iso_H — **not** a proof of Iso_H. Unconditional ε_other is **Iso_H-adjacent**.

---

## 3. Single-γ⋆ phase lock (n-aspect)

Free-\(t\) Kronecker resonance **does not apply**: \(\gamma_⋆\) is fixed; the free data are primes / cutoff \(X\).  
Need large values of
\[
\sum_p
\frac{\log p}{p^{\beta_⋆}\log p}
e^{-i\gamma_⋆\log p}
+
(\text{higher powers})
\]
i.e. multiplicative resonance in the **\(n\)-aspect at fixed frequency** — classically harder than \(t\)-aspect.

**Status:** **OPEN** — no classical theorem gives \(\lvert S_X(\rho_⋆)\rvert\to\infty\) off the line without RH-scale input.

---

## 4. Scoreboard

| Piece | Status |
|-------|--------|
| Star loglog cancel | **Proved** |
| Form B ↔ Form C | **Proved** (Thm 4.1) |
| Amplitude Ω of ψ−x | **Classical** |
| ε_other unconditional | **Open** (Iso_H-adjacent) |
| Single-γ⋆ prime-side lock | **Open** |
| PAO / B_θ | **Open** |

**Resolution today:** **No.**

**Status code:** `RH_P1_PAO_DIRECT_2026-08-08`

*Per aspera ad astra.*
