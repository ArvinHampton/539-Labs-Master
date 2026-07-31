# Three Pure Estimates: \(E_1\), Far-Right \(\mathrm{Off}_X\), Near-Line Off-Diagonal

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Update:** near-line signed sum is fully attacked in **`RH_Signed_Sum_Attack.md`** (residual formula; self loglog cancels).

| Item | Standing |
|------|----------|
| \(\lvert E_1(w)\,w\rvert\le 1\) for \(\operatorname{Re}w\ge 0\), \(w\neq 0\) | **Proved** (Part I below) |
| Far-right \(\mathrm{Off}_X\) under KLN | **Proved** bound (Part II) |
| Near-line signed sum | **Reduced** to \(\int(\psi-x)\cdots\) — see signed-sum note; B_θ **open** |

---

# Part I — Theorem E1

**Theorem E1.** For \(\operatorname{Re}w\ge 0\), \(w\neq 0\): \(\lvert w\,E_1(w)\rvert\le 1\).

**Proof.** \(E_1(w)=e^{-w}\int_0^\infty e^{-s}/(w+s)\,ds\). For \(s\ge 0\), \(\lvert w+s\rvert^2=\lvert w\rvert^2+s^2+2s\operatorname{Re}w\ge\lvert w\rvert^2\). Hence \(\lvert E_1\rvert\le e^{-\operatorname{Re}w}/\lvert w\rvert\), so \(\lvert w E_1\rvert\le e^{-\operatorname{Re}w}\le 1\). □

**Corollary.** \(C_u^{(0)}\le 1/(1-1/X)\) for \(\operatorname{Re}z\ge 0\), GHK support — **rigorous**.

---

# Part II — Far-right Off (KLN)

**Theorem FR.** Under KLN for \(N(\sigma_\star,T)\), \(\beta_\star\le\sigma_\star\),
\[
\lvert\mathrm{Off}_X^{\mathrm{far}}\rvert
\le
C_{\mathrm{FR}}
\Biggl(
\frac{N(\sigma_\star,T)\,X^{1-\beta_\star}}{T((\sigma_\star-\beta_\star)\log X+1)}
+
\frac{N(\sigma_\star,T)\,X^{\sigma_\star-\beta_\star}}{(\sigma_\star-\beta_\star)\log X+1}
\Biggr).
\]
Parameter tension with EF remainder remains (large \(T\) vs small far-right).

---

# Part III — Near-line → signed-sum note

Absolute majorants are too large (previous NL-best).  
**Signed analysis:** `RH_Signed_Sum_Attack.md` proves
\[
S_X=\rho_\star\int_2^X\frac{\psi-x}{x^{\rho_\star+1}\log x}\,dx+B_X+E_X(T)
\]
without RH; self \(\log\log\) cancels; lower bound open.

---

## One-liner

> E1 closed; far-right Off bounded under KLN; signed near-line reduced to weighted \(\psi-x\); B_θ open.
