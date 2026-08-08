# Residual Probes — Re-verification (2026-08-08)

**Category:** A (residual-flux under Principle (S) only)  
**Does not reopen:** A0–A5⁺ / K⁺ · Option 3 · No-Go · packaging integers · continuum claims

---

## Probes re-run

| Script | Result |
|--------|--------|
| `scripts/residual_p_plus_multiscale_probe.py` | OK |
| `scripts/p_plus_2complex_topology_probe.py` | OK |

### Multi-scale P⁺

- Same-tower unordered triples: **56** (all consecutive index triples)
- Window faces k < 18: **3**; tower faces: **53**; straddling: **0**
- ω_P(δf) = 0 under path-integrated Stokes and chord-zero Stokes
- Thin H² proxy dim: **1**; permanent class **survives** (s_ad residual from im ≫ 1)
- Path H² proxy (path-integrated convention): **56** (secondary room only)
- r_W still nonzero; M_win unchanged on 1-skeleton
- Status remains research-stable; optional preservation lock recorded separately

### P⁺ M1 topology + Q0–Q8

- Cell census: V=539, path edges 538, chords 56, faces 56; χ = 1
- Contractible proxy: H0 = 1, H_{>0} = 0
- Block gaps multiset: {5: 6, 7: 25, 9: 24}
- d_P(δf) = 0 on all 56 faces under stay+chord natural extension
- Jump-mass support disjoint from stay-triple edges
- Q0–Q8 integers matched (N_flux=4880, B′=539, M=8676, M_win=252, M_tow=8424, W=18, e_win=17, e_tow=521)
- Status: `P_PLUS_M1_TOPOLOGY_EXECUTED_QUANTIZATION_PIPELINE_A`

---

## Optional combinatorial lock (new)

See `P_plus_Permanent_Class_Survival_Optional_Lock_2026-08-08.md`.

Under residual height δf, ω_P(δf)=0 on all 56 faces ⇒ permanent class [α⊗δf] survives with thin H² rank-1 proxy. Secondary multi-scale room for non-height 1-cochains stays open research. 56 is not packaging.

---

## Explicit non-claims

- No auto-lock of P⁺ as kit theorem beyond the optional preservation statement
- No free T♯ origin
- No continuum Cartan / hopfion claim
- No security reduction

**Status code:** `RESIDUAL_PROBES_REVERIFIED_2026-08-08`

*Per aspera ad astra.*
