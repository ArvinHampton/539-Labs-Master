# Photon-ring critical curve from the integer tower

**Algebraic ngEHT chain** (not merely definitional)  
Companion to `PhotonRing_CriticalCurve_Derivation.tex`

---

## One-line result

\[
\frac{\Delta b_c}{b_c}
= f_{\mathrm{snap}}
= \frac{243}{4880}
\approx 0.049795
= \frac{\Delta r_{\mathrm{ring}}}{GM/c^2}
\quad\text{(linear order, snap matching \(\alpha=1\))}
\]

---

## Chain

```text
Axiom 0 (3 gen)
  → N_flux = ⌊e³ × 3⁵⌋ = 4880,  3⁵ = 243
  → f_snap := 243/4880

Schwarzschild (G=c=1)
  → r_ph = 3M,  b_c = 3√3 M

Snap deformation
  → f_ε(r) = 1 − 2M/r + ε ψ(r),  ε = f_snap

Linear critical-curve formula
  → Δb_c / b_c = −(3/2) ε ψ(3M) + O(ε²)

Snap matching (model)
  → ψ(3M) = −2/3  ⇒  α = 1

ngEHT map
  → Δθ_c/θ_c = Δb_c/b_c
  → Δr_ring/(GM/c²) := Δb_c/b_c = 243/4880
```

---

## 1. Integer tower → \(f_{\mathrm{snap}}\)

\[
f_{\mathrm{snap}}
:= \frac{\rho_{\mathrm{snap}}}{\rho_{\mathrm{DM}}}
:= \frac{3^5}{N_{\mathrm{flux}}}
= \frac{243}{4880}
= \frac{3^5}{2^4 \cdot 5 \cdot 61}
\approx 0.049795081967
\]

No free continuous parameter. Note \(61\) already sits in the denominator of \(f_{\mathrm{snap}}\).

---

## 2. Schwarzschild critical curve (exact)

Metric: \(f(r)=1-2M/r\).

Null critical condition:
\[
\frac{\mathrm{d}}{\mathrm{d}r}\!\left(\frac{f}{r^2}\right)=0
\quad\Leftrightarrow\quad
r f'-2f=0.
\]

**Result:**
\[
r_{\mathrm{ph}}=3M,
\qquad
b_c=\frac{r_{\mathrm{ph}}}{\sqrt{f(r_{\mathrm{ph}})}}=3\sqrt{3}\,M\approx 5.1961524227\,M.
\]

Angular scale at distance \(D_A\): \(\theta_c=b_c/D_A\), so
\[
\frac{\Delta\theta_c}{\theta_c}=\frac{\Delta b_c}{b_c}.
\]

---

## 3. First-order shift formula

Deform:
\[
f_\varepsilon(r)=1-\frac{2M}{r}+\varepsilon\,\psi(r),
\qquad
\varepsilon:=f_{\mathrm{snap}}.
\]

Photon-sphere shift:
\[
\delta r
= \frac{3M}{2}\bigl(3M\,\psi'(3M)-2\psi(3M)\bigr).
\]

Critical impact parameter (log differential along the critical family):
\[
\frac{\mathrm{d}b}{b}=\frac{\mathrm{d}r}{r}-\frac12\frac{\mathrm{d}f}{f}.
\]

**Master formula** (δr terms cancel):
\[
\boxed{
\frac{\Delta b_c}{b_c}
= -\frac{3}{2}\,\varepsilon\,\psi(3M)
+ O(\varepsilon^2).
}
\]

So only the value of the deformation at the unperturbed photon sphere enters at linear order.

---

## 4. Snap matching \(\alpha=1\)

Define
\[
\alpha := -\frac{3}{2}\psi(3M).
\]

**Snap-matching principle (model):** the bulk density ratio and the critical-curve fractional shift share the same dimensionless coefficient,
\[
\psi(3M)=-\frac{2}{3}
\quad\Rightarrow\quad
\alpha=1.
\]

Then:
\[
\boxed{
\frac{\Delta b_c}{b_c}
= f_{\mathrm{snap}}
= \frac{243}{4880}
+ O(f_{\mathrm{snap}}^2).
}
\]

Minimal profile realising the match: \(\psi(r)\equiv -2/3\) (constant near \(r\sim 3M\)), which also gives
\[
r_{\mathrm{ph}}=3M+2M\,f_{\mathrm{snap}}+O(f_{\mathrm{snap}}^2).
\]

This is a **linearised effective description at the photon sphere**, not a claim that a Planck core has radius \(0.05\,M\).

---

## 5. Map to \(\Delta r_{\mathrm{ring}}/(GM/c^2)\)

**VLBI-facing definition** used for ngEHT comparison:
\[
\boxed{
\frac{\Delta r_{\mathrm{ring}}}{GM/c^2}
:= \frac{\Delta b_c}{b_c}
= \frac{243}{4880}
\approx 0.049795.
}
\]

| Observable | Prediction |
|------------|------------|
| Fractional critical-curve / diameter shift | \(243/4880\) |
| Thickness coefficient in units of \(GM/c^2\) | \(243/4880\) |
| Relative linear truncation error | \(O(f_{\mathrm{snap}}^2)\approx 2.5\times 10^{-3}\) |

Kerr spin changes background \(b_c(M,\chi)\); the **fractional** snap shift remains \(f_{\mathrm{snap}}\) at this linear matching order (spin-dependent \(\psi\) deferred).

---

## 6. Worked numbers (\(M=1\))

| Quantity | Value |
|----------|-------|
| \(b_c^{(0)}=3\sqrt{3}\) | 5.1961524227 |
| \(f_{\mathrm{snap}}=243/4880\) | 0.0497950820 |
| \(\Delta b_c=f_{\mathrm{snap}} b_c^{(0)}\) | 0.258743 |
| \(b_c\) | 5.454895 |
| \(r_{\mathrm{ph}}=3+2f_{\mathrm{snap}}\) | 3.099590 |

---

## 7. What is *not* claimed

1. **Planck core ⇒ 5% ring.**  
   \(r_{\mathrm{core}}/M\sim\ell_{\mathrm{Pl}}/M\ll 10^{-38}\) cannot produce \(\Delta b_c/b_c\sim 0.05\).  
   The coefficient is the **density ratio** \(f_{\mathrm{snap}}\) as a deformation amplitude at \(r\sim 3M\), not \(r_{\mathrm{core}}/M\).

2. **GW250114 measures \(f_{\mathrm{snap}}\).**  
   QNMs stay pure Kerr on Clock I; \(\{243/539,\,243/4880,\,11/61\}\) are not QNM fit knobs. Kerr match remains parameter-free.

3. **\(\beta_{\mathrm{PBH}}=11/61\) sets the ring.**  
   Ring coefficient is \(f_{\mathrm{snap}}=243/4880\).  
   \(\beta_{\mathrm{PBH}}\) is Clock-III weight only.

4. **Zenodo.**  
   No public DOI yet; this note + the Resolution chapter are the local derivation.

---

## 5. Files

| File | Role |
|------|------|
| `PhotonRing_CriticalCurve_Derivation.tex` | Full formal chapter (book `\input`) |
| `PhotonRing_CriticalCurve_Derivation.md` | This readable summary |
| `CLOSED_CONSTANTS.md` | SSOT for \(f_{\mathrm{snap}}\) |
| `Resolution_GW250114_ThreeClocks_ClosedConstants.tex` | Three clocks + closed triple |

---

*Per aspera ad astra.*
