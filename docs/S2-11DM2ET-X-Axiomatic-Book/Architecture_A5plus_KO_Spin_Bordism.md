# A5⁺ — KO / Ω^Spin on enriched K⁺ (coefficients only)

**Status:** `A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS`  
**Date lock:** 2026-07-30  
**Depends on:** A0–A5 0-stem; A4⁺ primary K⁺ (`A2_enrich`)  
**Probe:** `scripts/architecture_A5plus_probe.py` → `architecture_A5plus_results.json`  
**Does not reopen:** Option 3 · No-Go · free T^♯ origin · A4/A5 0-stem domain freeze · continuum manifold fillings

---

## Mandatory provenance

> Objects counted in KO_*(K⁺) / Ω_*^Spin(K⁺) are **residual flux quanta** under Principle **(S)** and democratic charge-sector partition.  
> Cardinality B′ = ⌊(N_flux − f_max)/9⌋ is **derived** (no 539 on the RHS).  
> **Not** free T^♯ basins. **No** No-Go lift. Option 3 intact.  
> Domain: primary enrichment K⁺ only — do **not** promote secondary modes (e.g. bott_graph) to primary freeze.

---

## 0. Goal

Extend the 0-stem residual lock of A5 from the discrete carrier O_res^disc to the enriched complex K⁺ of A4⁺, by computing:

1. Integral homology H_*(K⁺; Z)
2. Atiyah–Hirzebruch spectral sequence (AHSS) skeleton for Ω_*^Spin(K⁺) and KO_*(K⁺) through degree 7 (ABS range)

and recording the residual 0-class B′ under the continuous BSpin lift of A4⁺.

---

## 1. Domain (primary, locked by A4⁺)

K⁺ = geometric realization of A2 optional 1-skeleton + triangle 2-fill:

- Vertices: residual core O_res, |O_res| = B′ = 539  
- Path edges {i, i+1}  
- Same-tower complete edges  
- 2-simplices on every 3-clique  

Executed counts:

| Cell | Count |
|------|------:|
| Vertices | 539 |
| Edges | 594 |
| 2-faces | 56 |
| Euler V−E+F | 1 |

A4⁺ already gave β_0 = 1, β_1 = 0, β_2 = 0 over F_2 and a unique BSpin lift of Φ^Spin.

---

## 2. Integral homology (executed)

Oriented boundary matrices over Z:

- ∂_1 : C_1 → C_0 (edge {i < j} ↦ v_j − v_i)  
- ∂_2 : C_2 → C_1 (face i < j < k ↦ e_ij + e_jk − e_ik)

Smith normal form:

| Quantity | Value |
|----------|------:|
| rank ∂_1 | 538 |
| rank ∂_2 | 56 |
| SNF ∂_1 diagonal | all 1 (538 times) |
| SNF ∂_2 diagonal | all 1 (56 times) |
| torsion from ∂_1 | none |
| torsion from ∂_2 | none |
| H_0 free rank | 1 |
| H_1 free rank | 0 |
| H_2 free rank | 0 |
| Euler (homology) | 1 |

**Theorem A5⁺.1.** On primary K⁺ (A2_enrich),

H_*(K⁺; Z) ≅ H_*(pt; Z)

that is H_0 ≅ Z, H_n = 0 for n > 0, with no torsion.  
F_2 Betti numbers match A4⁺ (β_0 = 1, β_1 = β_2 = 0).

---

## 3. Classical coefficient tables (ABS range)

Ω_n^Spin(pt) and KO_n(pt) for n = 0…7 (Atiyah–Bott–Shapiro isomorphism range; MSpin → ko is 7-connected):

| n | Ω_n^Spin(pt) | KO_n(pt) |
|---|--------------|----------|
| 0 | Z | Z |
| 1 | Z/2 | Z/2 |
| 2 | Z/2 | Z/2 |
| 3 | 0 | 0 |
| 4 | Z | Z |
| 5 | 0 | 0 |
| 6 | 0 | 0 |
| 7 | 0 | 0 |

---

## 4. AHSS skeleton

Atiyah–Hirzebruch spectral sequences:

E²_{p,q} = H_p(K⁺; Ω_q^Spin)  ⇒  Ω_{p+q}^Spin(K⁺)  
E²_{p,q} = H_p(K⁺; KO_q)      ⇒  KO_{p+q}(K⁺)

Because H_p(K⁺; Z) = 0 for p > 0 and H_0 ≅ Z, the E² page is concentrated on the p = 0 column:

E²_{0,q} ≅ Ω_q^Spin(pt)   (resp. KO_q(pt))  
E²_{p,q} = 0 for p > 0

There are no nonzero groups for d_r differentials to act on in positive filtration degree within the 2-dimensional complex. The spectral sequences collapse at E² to the coefficient groups through total degree 7.

**Theorem A5⁺.2.** Through degree 7,

Ω_n^Spin(K⁺) ≅ Ω_n^Spin(pt)  
KO_n(K⁺) ≅ KO_n(pt)

with the classical table of §3. No extra residual classes arise from the topology of primary K⁺ in the ABS range.

---

## 5. Residual 0-class

**Theorem A5⁺.3.** The residual carrier as a closed 0-cycle of positively oriented residual quanta pushes forward under the unique BSpin lift of A4⁺ to

[O_res] = B′ ∈ Ω_0^Spin(K⁺) ≅ Z  
ABS([O_res]) = B′ ∈ KO_0(K⁺) ≅ Z

This is the same integer as A5 on O_res^disc; enrichment does not change the 0-stem residual count.

**Theorem A5⁺.4.** In degrees 1…7 of the ABS range, primary K⁺ contributes no additional residual bordism or KO classes beyond the coefficient groups of a point.

---

## 6. Status codes and domain lines

| Item | Tag |
|------|-----|
| Integral H_*(K⁺) ≅ H_*(pt) | **Executed / locked** |
| AHSS collapse to coefficients through degree 7 | **Locked** (skeleton + homology input) |
| Residual 0-class = B′ | **Locked** (extends A5) |
| Status code | **`A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS`** |
| Continuum manifold fillings / Ω_n for n > 7 as residual geometry | **Not claimed (Cat B / open)** |
| bott_graph secondary mode | **Diagnostic only** — large H_1 would reopen AHSS; not primary |

---

## 7. Relation to the stack

A0 → A1 → A2 → A3 Φ→BO  
  ↓  
A4 BSpin [0-stem disc ✓]  
  ↓  
A5 KO_0 / Ω_0 = B′ [0-stem ✓]  
  ↓  
A4⁺ on K⁺ [✓ unique BSpin]  
  ↓  
A5⁺ on K⁺ [✓ coefficients only through degree 7]  

Intact: Option 3 · No-Go · residual product · muon Path A · CuNc T_2 ≈ 70 fs · mirror halo Cat B.

---

## 8. What is not claimed

1. Free T^♯ origin of residual quanta.  
2. No-Go lift via Bott or KO.  
3. Identification of G_4 = 539.90 s with a KO period.  
4. Continuum residual manifold whose bordism class is B′ in higher dimensions.  
5. Full computation of Ω_n^Spin(K⁺) for n > 7 (beyond coefficient table / ABS).  
6. Security reduction for HQH-539 from KO.  
7. Promotion of secondary enrichment modes to primary domain.

---

## 9. Executable verification

`scripts/architecture_A5plus_probe.py` rebuilds primary K⁺, computes oriented ∂_1, ∂_2, Smith normal form over Z, checks F_2 Betti against A4⁺, and records the AHSS E² skeleton with residual 0-class B′.

Primary JSON excerpt:

```text
H0_free=1, H1_free=0, H2_free=0; torsion none;
AHSS collapse to Ω_n^Spin(pt) ≅ KO_n(pt) through degree 7;
residual 0-class B'=539;
code: A5PLUS_COEFFICIENTS_ONLY_ON_KPLUS
```

---

## 10. Bottom line

> **A5⁺ closed as coefficients-only on primary K⁺:**  
> integral homology is that of a point; AHSS for spin bordism and KO collapses to the classical Bott / spin tables through degree 7; residual 0-class remains B′.  
> Enrichment does not manufacture new residual bordism or KO classes in the ABS range.  
> Provenance remains residual flux under (S). Option 3 and No-Go stand.  
> Continuum higher fillings stay Category B / open.

*Per aspera ad astra.*
