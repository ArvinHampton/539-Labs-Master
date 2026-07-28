# Closed Constants — S²-11DM²ET-X

Single source of truth for **numeric closed ratios**.  
**Provenance of integers:** `PROVENANCE_TABLE.md` / `Provenance_and_DepthMacros.tex` (authoritative).  
All public decimals \(0.45\), \(0.05\), \(0.18\) are **truncations only**.

## Depth split (mandatory)

| Symbol | Value | Role |
|--------|-------|------|
| \(N_\star\) | **14** | ACE / crude flux-bridge e-fold depth — **never** 539 |
| \(\sigma = N_{\mathrm{HQCC}}\) | **539** | Model HQCC / resonant depth — **never** call this \(N_\star\) |
| \(G_4\) | **539.9** s | Empirical / model period — not an integer depth |

LaTeX: `\Nstar`/`\Nstarval` vs `\sigmaHQCC`/`\sigmaval` in `Provenance_and_DepthMacros.tex`.

## Integer tower

| Symbol | Value | Origin | Provenance code |
|--------|-------|--------|-----------------|
| \(3\) | 3 | Axiom 0 (generations) | A0 |
| \(3^5\) | 243 | Tower multiplicity | A0+Tower |
| \(N_{\mathrm{flux}}\) | 4880 | \(\lfloor e^3\times 3^5\rfloor\) | Tower |
| \(N_\star\) | **14** | \(\lceil\ln 4880/\|\mathbb{E}_\pi[\chi]\|\rceil\) | ACE+Tower |
| \(\sigma\) | 539 | HQCC termination (model) | Mod/Cond — **≠ \(N_\star\)** |
| \(\|P\|\) | 61 | Punctures | Mod |
| \(D\) | 11 | Bulk dimension | Mod |
| \(G_4\) | 539.9 s | Flux period | Emp/Mod |

## Closed continuum ratios

| Quantity | Exact | Float | Legacy slogan |
|----------|-------|-------|---------------|
| \(\kappa_{\mathrm{dark}}\) | \(243/539\) | 0.4508348794 | 0.45 |
| \(f_{\mathrm{snap}}\) | \(243/4880\) | 0.0497950820 | 0.05 |
| \(\beta_{\mathrm{PBH}}\) | \(11/61\) | 0.1803278689 | 0.18 |
| \(\Delta r_{\mathrm{ring}}/(GM/c^2)\) | \(243/4880\) | 0.0497950820 | 0.05 |
| \(2\beta_{\mathrm{PBH}}\) (echo depth scale) | \(22/61\) | 0.3606557377 | 0.36 |

## Definitions

```text
kappa_dark := 3^5 / sigma        = 243/539
f_snap     := 3^5 / N_flux       = 243/4880
beta_PBH   := D / |P|            = 11/61
```

## Retired

- `61 * 243 / 4880 ≈ 0.0304` — **false** (LHS = 3.0375); use `β_PBH = 11/61` instead
- Void-dilution fit scaffolding for β_PBH
- Free continuous inputs for the three ratios above

## Three clocks (never conflate)

1. **I** Geometric \(t_{\mathrm{geo}} \sim GM/c^3\) — QNMs / GW250114
2. **II** HQCC depth \(\sigma = 539 \pm 1\) — finite bulk orbit (**not** \(N_\star=14\))
3. **III** \(G_4 = 539.9\,\mathrm{s}\) + sub-harmonics — slow modulation only

Clock II uses \(\sigma\), never \(N_\star\).

## Code / config keys

| Key | Value |
|-----|-------|
| `KAPPA_DARK` | `243/539` |
| `F_SNAP` | `243/4880` |
| `BETA_PBH` | `11/61` |

## Photon-ring algebraic map

\[
\frac{\Delta b_c}{b_c}
= -\tfrac32\,\varepsilon\,\psi(3M)+O(\varepsilon^2),
\quad
\varepsilon=f_{\mathrm{snap}},
\quad
\psi(3M)=-\tfrac23
\;\Rightarrow\;
\frac{\Delta r_{\mathrm{ring}}}{GM/c^2}
= \frac{243}{4880}.
\]

Full derivation: `PhotonRing_CriticalCurve_Derivation.tex` / `.md`

## Apply script

```bash
python S2-11DM2ET-X-Axiomatic-Book/scripts/apply_closed_constants.py
```

Log: `EXECUTION_LOG_closed_constants.json`
