# Push log — optimized \(c_i\) + M1.3 HD-low (2026-07-30)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**. **Does not prove RH / M1.2 / M1.3.**

## Artefacts

| File | Role |
|------|------|
| `RH_M1_2_Optimized_ci_Bounds.md` | \(c_1\le 291\), \(c_2\le 8\) for \(f_\star\) |
| `scripts/rh_optimize_c1_c2.py` | Optimize \(M_2,A_2,D_2\) |
| `rh_optimize_c1_c2_results.json` | Results |
| `RH_M1_3_HD_Low_Path_Report.md` | HD-low isolation + monodromy correction |
| `scripts/rh_M1_3_path_diagnostic.py` | Semicircle + approach paths |
| `rh_M1_3_path_diagnostic_results.json` | Results |
| Updated | `RH_M1_3_Path_Design.md`, baseline, claim table, README, Next |

## Key outcomes

1. **\(c_1\le 291\)** (\(\sim 450\times\) vs crude \(10^5\)).  
2. **HD-low:** 6/6 first zeros isolated.  
3. **Monodromy:** \(\Delta_{\mathrm{semi}}\arg P\sim 0\) — bare \(m\pi\) claim on \(\arg P\) **withdrawn**.  
4. Naive peel \(\lvert\operatorname{Im}(\log P-m\log(s-\rho))\rvert\sim\pi\).  
5. Approach path is the correct phase geometry; large \(\log\log\) still open.

## Firewall

No model constants · residual stack untouched · RH open.  
