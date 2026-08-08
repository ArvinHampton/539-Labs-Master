# RH MA8 — EF Dual of Far Hybrid U for κ (2026-08-08)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** κ with p>1 · O-M1.2 · O-TL · RH  
**Does:** record the classical logarithmic-derivative dual for far \(U\)-sums

---

## Identity (classical partial fractions)

For \(s\) not a zero or pole,
\[
\sum_{\rho}\frac{1}{s-\rho}
=
-\frac{\zeta'}{\zeta}(s)
-
(\text{trivial zeros})
+
(\text{archimedean}/\xi\text{ factors}),
\]
in the usual Hadamard/ξ sense. Split \(\sum=\sum_{\mathrm{near}}+\sum_{\mathrm{far}}\).

Under the model \(U(s,\rho')\sim 1/((s-\rho')\log X)\) (E1 regime),
\[
\sum_{\rho'\ \mathrm{far}}U(s,\rho')
\sim
\frac{1}{\log X}
\sum_{\rho'\ \mathrm{far}}\frac{1}{s-\rho'}
=
\frac{1}{\log X}
\Biggl(
-\frac{\zeta'}{\zeta}(s)
-
\sum_{\mathrm{near}}\frac{1}{s-\rho}
-
\mathrm{triv}
-
\mathrm{arch}
\Biggr).
\]

---

## Consequence for κ

| Rewrite | Meaning |
|---------|---------|
| κ as control of \(\zeta'/\zeta\) on paths | Far signed \(U\) ↔ \(\zeta'/\zeta\) minus near/arch |
| Approach-to-zero arcs | \(\zeta'/\zeta\) has poles at zeros → need **distance-to-nearest-zero** (GO territory) |
| Zero-free path segments | Classical \(|\zeta'/\zeta|\ll\log^2|t|\) can make far \(U\) small — not the hard O-TL arcs |

**Identity win:** far \(U\) is dualized (no longer “missing dual”).  
**Estimate:** still open — κ with \(p>1\) **not** obtained.  
**Correlation:** κ ↔ GO **strengthened** (approach arcs).

**Status code:** `RH_MA8_EF_DUAL_KAPPA_2026-08-08`

*Per aspera ad astra.*
