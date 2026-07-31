# Analytic O1 — Akatsuka / M1 Package

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Tag:** O1 complete at **schematic** level; M1.2–M1.4 open.

---

## (O1-A) On-line product shape (Akatsuka-type)

**Schematic (on the critical line, when a DRH-type limit exists).**  
At a fixed height \(s_0=1/2+it_0\) corresponding to a zero of multiplicity \(m\) in the limiting sense of partial products,

\[
\zeta_x(s_0)
= C\,e^{R_{\mathrm{pole}}}\,(\log x)^{-m}\,(1+o(1))
\quad\text{(modulus-leading form)},
\]

equivalently

\[
\log\zeta_x(s_0)
= -m\log\log x + R_{\mathrm{pole}} + \log C + o(1).
\]

| Tag | Content |
|-----|---------|
| (O1-A) | Exact Akatsuka: \(\zeta_x(s_0)=C e^{R_{\mathrm{pole}}}/(\log x)^m\) on the line when DRH-limit exists |
| (O1-A-log) | \(\log\zeta_x(s_0)=-m\log\log x+R_{\mathrm{pole}}+\log C+o(1)\) |
| (O1-pole) | Named pole renormalizer integral (to be matched to GHK \(U\) near \(s=1\)) |

**Important O1 conclusion:** under Akatsuka on the line, \(m\log\log\) sits in the **modulus**, not automatically in \(\arg\). Off-line target lemma still needs M1.2–M1.4.

---

## (O1b) Dictionary toward GHK / explicit formula

| Akatsuka / classical | GHK hybrid |
|----------------------|------------|
| Partial Euler \(\zeta_x\) or \(P_x\) | \(P_X=\exp(\sum_{n\le X}\Lambda(n)n^{-s}/\log n)\) |
| Remainder after zeros | \(Z_X=\exp(-\sum_\rho U((s-\rho)\log X))\) |
| \(R_{\mathrm{pole}}\) | pole piece of M1 / IvM-type regularizer |
| Error | \(O(X^{K+2}/(|s|\log X)^K)+O(X^{-\sigma}\log X)\) |

**O1b:** \(R_{\mathrm{pole}}\leftrightarrow\) pole piece of M1 / \(R_{\mathrm{IvM}}\).

---

## (O1-M1) / (O1-arg) Near a zero

Near a nontrivial zero \(\rho\) of multiplicity \(m\), with \(s\) close to \(\rho\) but \(\zeta(s)\neq 0\),

\[
\log P_X(s)
= m\log(s-\rho)
- \mathcal R_X^{(\mathrm{EP})}(s)
+ \cdots,
\]

\[
\theta_X(s)
= m\arg(s-\rho)
- \operatorname{Im}\mathcal R_X^{(\mathrm{EP})}(s)
+ \cdots.
\]

Here \(\mathcal R_X^{(\mathrm{EP})}\) collects:

1. contributions of **other** zeros through \(U((s-\rho')\log X)\);
2. difference between \(\log\zeta-\log Z_X\) and \(\log P_X\) errors;
3. smooth arithmetic remainders.

---

## Obligations after O1

| Tag | Task | Doc |
|-----|------|-----|
| M1.2 | Bound \(\lvert\operatorname{Im}\mathcal R_X^{(\mathrm{EP})}\rvert\) near a point (on- or off-line) | `RH_M1_2_Remainder_Bound.md` |
| M1.3 | Path design for large \(m\arg(s-\rho)\) relative to M1.2 | `RH_M1_3_Path_Design.md` |
| M1.4 | No circular RH; smoothing to \(A_X\) | `RH_Next_Directions.md` |

---

## Forbidden in O1

- Using Sheth / Ramanujan–Kaneko expansions **under RH** as the sole justification of off-line growth (circular for an RH proof).
- Inserting model debit caps.

---

## Literature anchors

- H. Akatsuka, Kodai Math. J. **40** (2017), 79–101.
- S. M. Gonek, C. P. Hughes, J. P. Keating, Duke Math. J. **136** (2007), 507–549.
- K. Conrad, Canad. J. Math. **57** (2005), 267–297.
