# FINDINGS — Ω/F factor tables ingest (t614u) — 2026-10-24 23:13 CDT America/Chicago
**Track:** NONLOCAL_QM_EH11D. Residual-vs-Resonant. Extract/ingest only.
**Label: Cat B continuum (chat lock).** Not paper Cat A. W-PO-3 OPEN until Drive/paper original.

## Source
- Pin (mirrored): `OMEGA_F_FACTOR_TABLES_2026-10-24.md`
- sha256: `c9c3b30df6576fd58cd65cec1d2072c12d8db7f222d781d1cb8c8904be048df2` (pins/ + inventory_check/ identical; verified)
- BRIDGE_C_35/pins/SHA256SUMS sha `45e696ff9d896bf8f2d5ae1765d3db92ed4721c1cfdc9159953e6b4c8313f31a` (8/8 OK)
- Provenance: Arvin Hampton t614u. Prior hunt `W_PO2_OMEGA_F_TABLES_HUNT.md` ff5ff7f0… ABSENT table bodies — this pin is the author write.

## Ingested (as written — no invent)
### Ω packaging
Ω₁₁D(k,K,b,Φ)=Ω₀·f_warp(k)·f_curv(K)·f_b(b)·Φ_flux(Φ)

### Ω channel table (status as written)
| Channel | Contribution | Status in pin |
|---|---|---|
| Warp k | f_warp(k) | Functional form **pending** explicit compactification |
| Curvature K | f_curv(K) | Functional form **pending** explicit compactification |
| Residual scale b | f_b(b) | Residual packaging scale |
| Flux phase Φ | Φ_flux(Φ) | Locked to 539.9 s period |

### F_total component table (each × Ω₁₁D)
Five Codex forms as in pin: Coulomb^rel, SO, Torsion, Flux, Leak — explicit expressions quoted in source pin lines 22–26. Not recopied here to avoid transcription drift; cite pin sha c9c3b30d….

## Explicitly NOT done / banned
- No invent of Ω₀, f_warp, f_curv closed forms, or numeric Ω.
- No NL2 Z=1–118 fit (`periodic_table_539labs.json` still ABSENT).
- Do not treat chat lock as paper Cat A.
- Maps separate — no local G1 / Ξ / P̂_orth / residual-C claims.
- NL1 structural PREREG untouched (495c7944… / 85bd2f63…).

## Posture
W-PO-2 table-body gap addressed by author write (chat). **W-PO-3 remains OPEN** until Drive/paper attach. IDLE_AFTER_LOCK / NL1_STRUCTURAL_ACCEPT stands.
