# Torsion Amplitude to Laboratory \(\delta G\) — Parameter-Free Closure

**Date lock:** 2026-07-31  
**Status:** Category B continuum ansatz closed under locked integers + \(G_4\) + CODATA  
**Code:** `TORSION_DELTA_G_ANSATZ_CLOSED_2026-07-31`  
**Does not alter:** residual Architecture A0–A5⁺, Option 3, No-Go, packaging under (S)

---

## 1. Standard Einstein–Cartan baseline

\[
T^\lambda{}_{\mu\nu}=\kappa S^\lambda{}_{\mu\nu},\qquad \kappa=\frac{8\pi G}{c^4}
\]

Torsion algebraic in spin; non-propagating in vacuum. Spinless test masses follow metric geodesics. Pure EC laboratory \(\delta G/G\sim 10^{-60}\) or smaller — unobservable.

Any laboratory \(\delta G\) requires either metric modification from torsion-sourced stress-energy, or a non-standard long-range / background torsion (continuum 7D \(G_2\) singlet is of this second type). Both are Category B relative to residual algebra.

---

## 2. Master conversion (all experiments)

\[
a_{\mathrm{true}}
=
G_{\mathrm{fund}}\frac{M}{r^2}(1+\varepsilon_{\tau})
+
a_{\mathrm{spin\text{-}torsion}}
\]

Experimenter fits \(a_{\mathrm{obs}}=G_{\mathrm{fit}}M/r^2\):

\[
\frac{\delta G}{G}
\equiv
\frac{G_{\mathrm{fit}}-G_{\mathrm{fund}}}{G_{\mathrm{fund}}}
=
\varepsilon_{\tau}
+
\frac{r^2}{G_{\mathrm{fund}}M}\,a_{\mathrm{spin\text{-}torsion}}
+O(\varepsilon_{\tau}^2)
\]

---

## 3. Locked inputs only

| Symbol | Value | Origin |
|--------|--------|--------|
| \(N_{\mathrm{flux}}\) | 4880 | \(\lfloor e^3\cdot 3^5\rfloor\) |
| \(\sigma\) | 539 | packaging \(18+521\) |
| \(\|P\|\) | 61 | punctures |
| \(N_{\mathrm{tow}}\) | 243 | \(3^5\) |
| \(N_{\mathrm{elem}}\) | 118 | mirror table |
| \(G_4\) | 539.90 s | continuum clock |
| \(\varepsilon\) | \(61/4880\) | puncture/flux |
| \(\kappa_{\mathrm{dark}}\) | \(243/539\) | tower/packaging |
| \(\eta_{\mathrm{geom}}^{\star}\) | \(81/539=3^4/539\) | locks continuum 0.15 |
| \(\lambda_{G_4}\) | \(cG_4\) | only length from clock |
| \(\ell_{\mathrm{Pl}}\) | CODATA | bulk gravitational scale |

Nuclear combinatorial weight (no binding table required for projection): \(w_{118}=118/539\).

---

## 4. Closed formulas

\[
\boxed{
\eta_{\mathrm{geom}}^{\star}
=
\frac{81}{539}
\approx 0.150278
}
\]

\[
\boxed{
\alpha_{\mathrm{proj}}^{\star}
=
\varepsilon\cdot\kappa_{\mathrm{dark}}\cdot
\frac{\ell_{\mathrm{Pl}}}{\lambda_{G_4}}\cdot
\frac{118}{539}
=
\frac{61}{4880}\cdot\frac{243}{539}\cdot\frac{\ell_{\mathrm{Pl}}}{c\,G_4}\cdot\frac{118}{539}
\approx
1.23196\times 10^{-49}
}
\]

\[
\tau_{\mathrm{lab}}
=
\alpha_{\mathrm{proj}}^{\star}\,
\frac{2\pi}{G_4\,c}
\approx
4.78\times 10^{-60}\,\mathrm{m^{-1}}
\]

\[
f_n(L)=\Bigl(\frac{L}{\lambda_{G_4}}\Bigr)^n
\]

\[
\varepsilon_{\tau}
=
\eta_{\mathrm{geom}}^{\star}\,
\alpha_{\mathrm{proj}}^{\star}\,
f
\]

\[
\boxed{
\frac{\delta G}{G}
=
\varepsilon_{\tau}
+
\Theta_{\mathrm{spin}}
\frac{r^2}{GM}
\frac{\hbar}{m}
\frac{2\pi\,\alpha_{\mathrm{proj}}^{\star}}{G_4\,\ell}
}
\]

\(\Theta_{\mathrm{spin}}=0\) (Cavendish, ephemeris); \(1\) (polarized AI).

---

## 5. Branches

### Branch D — Mirror-consistent (preferred)

Laboratory source masses are not DM \(\Rightarrow\) metric torsion channel off for Cavendish/AI metric.

| Observable | \(\delta G/G\) |
|------------|----------------|
| Cavendish | \(0\) |
| AI metric | \(0\) |
| AI spin (\(\ell=\lambda_{G_4}\)) | \(4.85\times 10^{-65}\) |
| Ephemeris (local DM mod. amplitude) | \(1.76\times 10^{-18}\) |

All pass present bounds.

### Branch U — universal \(G\) shift

\[
\frac{\delta G}{G}\Big|_{\mathrm{U}}
=
\eta_{\mathrm{geom}}^{\star}\,\alpha_{\mathrm{proj}}^{\star}
=
1.85\times 10^{-50}
\]

Dipole Cavendish: \(5.72\times 10^{-63}\). Passes bounds; galactic unsuppressed \(\eta\sim 0.15\) then cannot share the same amplitude (see Planck note).

---

## 6. Why packaging-only \(\alpha\) fails

Without \(\ell_{\mathrm{Pl}}/\lambda_{G_4}\), pure integer products with \(f=1\) give \(\delta G/G\sim 10^{-3}\)–\(10^{-7}\) and **fail** ephemeris / Cavendish bounds. Planck/clock ratio is the unique parameter-free suppressor using only locked quantities + CODATA + \(G_4\).

---

## 7. Non-claims

- Residual algebra does **not** evaluate \(\tau\) or \(\delta G\).
- CODATA \(G\) is **not** derived from the 118-sum.
- Continuum “gravity is reverse-parity EM” remains Category B narrative.
- HQH-539 hardness unchanged (Category B).

## 8. Status codes

`TORSION_DELTA_G_ANSATZ_CLOSED_2026-07-31`  
`MIRROR_CONSISTENT_LAB_G_NULL_OR_NEGLIGIBLE`  
`ALPHA_PROJ_STAR_1P23E-49`  
`ETA_GEOM_STAR_81_OVER_539`

*Per aspera ad astra.*
