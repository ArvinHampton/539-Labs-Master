# \(E_{\mathrm{leak}}\) Numerical Patch — CuNc 2026

**Status:** `E_LEAK_CUNC_NUMERICS_PATCHED_2026-07-30`  
**Supersedes:** any draft term using \(2.3\,\mathrm{fs}\) or prefactor \(0.031\) with \(\cos(2\pi t/5.0)\).  
**Does not rewrite** the full master equation; patches **only** the CuNc / exciton contact term.

---

## 1. Retracted term (do not use)

\[
\boxed{
0.031\,\exp\!\big(-t / 2.3\times 10^{-15}\big)\,
\cos\!\big(2\pi t / 5.0\big)
\quad\text{— RETRACTED}
}
\]

Reasons: wrong dephasing scale; wrong carrier period; unsupported amplitude (see `CuNc_2026_Exciton_Imaging_Audit.md`).

---

## 2. Replacement contact term (data-faithful schematic)

Let \(A_{\mathrm{CuNc}}\) be a **dimensionless Cat B amplitude** (unset by Luo et al.; not fixed to 0.031). Define the **external-data kernel**

\[
K_{\mathrm{CuNc}}(t)
=
e^{-t/T_2}\cos\!\left(\frac{\Delta E}{\hbar}\,t\right),
\qquad
T_2 = 70\times 10^{-15}\,\mathrm{s}
\quad\text{(monomer headline)},
\]

with interferogram period \(T_{\mathrm{osc}}\approx 2.5\times 10^{-15}\,\mathrm{s}\) fixed by \(\Delta E/\hbar\), not by \(G_4\).

**Optional dimer branch (Cat B bookkeeping only):**

\[
T_2^{\mathrm{br}} = 60\times 10^{-15}\,\mathrm{s},\qquad
T_2^{\mathrm{dk}} = 50\times 10^{-15}\,\mathrm{s}.
\]

**Allowed insertion into leakage sector (schematic):**

\[
\delta E_{\mathrm{leak}}^{\mathrm{(CuNc)}}(t)
=
A_{\mathrm{CuNc}}\,
\Big(
c_{\mathrm{br}}\,e^{-t/T_2^{\mathrm{br}}}
+
c_{\mathrm{dk}}\,e^{-t/T_2^{\mathrm{dk}}}
\Big)
\cos\!\left(\frac{\Delta E}{\hbar}\,t\right),
\]

with \(c_{\mathrm{br}}+c_{\mathrm{dk}}=1\), \(c_{\mathrm{br}},c_{\mathrm{dk}}\ge 0\). Defaults for monomer-only contact: \(c_{\mathrm{br}}=1\), \(T_2^{\mathrm{br}}=70\,\mathrm{fs}\).

---

## 3. What is **not** patched in

| Object | Rule |
|--------|------|
| \(G_4 = 539.90\,\mathrm{s}\) sine sector | Unchanged; **orthogonal timescale** to CuNc fs kernel |
| \(\sum_{z=1}^{118} E_b(z)\) −element sum | Mirror extension (Cat B); not set by CuNc \(T_2\) |
| \(\delta a_\mu^{(55)}\) Path A average | Unchanged (2026-07-30 muon freeze) |
| Residual \(\mathcal{O}_{\mathrm{res}}\) / A0–A5 | Untouched |

**Forbidden:** equating \(T_2\) with \(G_4\), or claiming fs imaging measures the flux clock.

---

## 4. Falsifiers for this patch

1. Primary literature revision of Luo et al. monomer \(T_2\) outside \(50\)–\(90\,\mathrm{fs}\) band without Model update.  
2. Re-introduction of the retracted \(2.3\,\mathrm{fs}\) term in any master-equation paste.  
3. Claiming \(A_{\mathrm{CuNc}}=0.031\) as a measured constant without a cited fit.

---

## 5. One-line freeze

**Replace CuNc leakage numerics with \(T_2\approx 70\,\mathrm{fs}\) monomer kernel; retract 2.3 fs / 0.031 / cos(2πt/5); keep \(G_4\) sector separate.**

*Per aspera ad astra.*
