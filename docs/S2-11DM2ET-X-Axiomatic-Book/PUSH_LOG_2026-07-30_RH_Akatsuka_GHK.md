# Push log — Akatsuka–GHK survey + hybrid probe (2026-07-30)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A** only. No model constants. **Does not prove RH or M1.2.**

## Artefacts

| File | Role |
|------|------|
| `RH_Akatsuka_GHK_Survey.md` | Pure Cat A survey: Akatsuka expansions + GHK hybrid; **Lemma M1.2-GHK** with explicit errors |
| `scripts/rh_GHK_hybrid_diagnostic.py` | Numeric hybrid \(P_X Z_X\) at first zeros / L5-style off-line minima |
| `rh_GHK_hybrid_diagnostic_results.json` | Diagnostic results (no proof claim) |
| Cross-links | README, Next_Directions, PROGRAMME_BASELINE, RH_L1, RH_M1_2, CLAIM_TABLE_RH_Debt |
| This push log | Hygiene |

## M1.2-GHK (one line)

After \(\zeta=P_X Z_X(1+\mathcal{E}_{\mathrm{GHK}})\), peel local \(m\,U((s-\rho)\log X)\); bound \(\operatorname{Im}\) of distant \(U\) + \(\mathcal{E}_{\mathrm{GHK}}\) by \(c_0 m\lvert\arg(s-\rho)\rvert\) on a path about \(\rho\).

## Probe snapshot (diagnostic)

\(X=200\), primes to \(15\,000\): mean \(|\arg\zeta-(\arg P+\arg Z^{\mathrm{trunc}})|\) \(\approx 0.19\) near first zeros, \(\approx 0.059\) at \(\sigma=0.60\) minima. Full \(U=E_1\) still open for tighter on-line error.

## Firewall

- No \(G_4\), \(\mu\), \(E_{\mathrm{leak}}\), 539.9 in theorems  
- Residual stack untouched  
- RH remains open  
