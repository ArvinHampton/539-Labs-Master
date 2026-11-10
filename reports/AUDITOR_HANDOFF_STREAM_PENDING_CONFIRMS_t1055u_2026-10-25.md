# AUDITOR HANDOFF — STREAM_IDLE_LOCAL rows 'Pending Auditor CONFIRM' — t1055u — 2026-10-25 19:22 CDT (America/Chicago)
Source: reports/bridges/BRIDGE_C_35/STREAM_IDLE_LOCAL.md sha256 `c6df07ef31cdfe31c2da18b978b8fd5320cd8938651d44e42f2ecb6d14012930` (note: inventory cited ef47b136…; live file differs — Auditor please reconcile). Inventory L-10/A-2.
Mapping is filename-match only; Auditor must verify each CONFIRM's hashes against the row PREREG/RESULTS/SUMS. No CONFIRM asserted here.

| Line | Tag | Expected CONFIRM (bridges/AUDITOR/) | Exists | sha256 |
|---|---|---|---|---|
| 22 | deduce_t695u_accept | FINDINGS_2026-10-25_t695u_accept_CONFIRM.md | NO — missing/unknown | — |
| 24 | deduce_t704u_accept | FINDINGS_2026-10-25_t704u_accept_CONFIRM.md | NO — missing/unknown | — |
| 33 | deduce_t734u_accept | FINDINGS_2026-10-25_t734u_accept_CONFIRM.md | YES | 7e20e84c4508dcff21169c89eb407a914e9f99ff56e478dc71cf406a23b06a24 |
| 35 | deduce_t740u_accept | FINDINGS_2026-10-25_t740u_accept_CONFIRM.md | YES | 2b959003d46762278c8da36a6562da63cd5b6a30d47f02faed8ed2d23900638b |
| 36 | deduce_t743u_b3 | FINDINGS_2026-10-25_t743u_b3_CONFIRM.md | YES | 0e9e53ddd7b019be66f6e856e0da4701811a304065e3a2517aba968018621fd5 |
| 37 | deduce_t748u_accept | FINDINGS_2026-10-25_t748u_accept_CONFIRM.md | YES | b96ff7bdd579d6b431f44ba1421f22cfa025770cbb70aa721da9607cb0a5fde1 |
| 38 | deduce_t749u_tunnel | FINDINGS_2026-10-25_t749u_tunnel_CONFIRM.md | YES | 8a2b8755f0f6345e03d1964f3eebcc9597fc07cc00586d468d083d59579702ee |
| 39 | deduce_t756u_accept | FINDINGS_2026-10-25_t756u_accept_CONFIRM.md | YES | 5f5f283203834eeafe78a9d44a1a7a70baac51e3ac84c945bc286df25afc39f7 |
| 42 | deduce_t761u_accept | FINDINGS_2026-10-25_t761u_accept_CONFIRM.md | YES | aac04151accb03b0464ffaf2fff09b733af99b820a97479f262a6d82f60b13d1 |
| 44 | deduce_t761u_outer_accept | FINDINGS_2026-10-25_t761u_outer_accept_CONFIRM.md | YES | b467bb54b7d759416cf9898ba806926758f01efb7fe8c0624edf13458d35a5f0 |
| 46 | deduce_t761u_path_psi_accept | FINDINGS_2026-10-25_t761u_path_psi_accept_CONFIRM.md | YES | c26b5f72c4603acd05623df5d745bfa538c4a14131b222bf92c00537f34f458e |
| 48 | deduce_t761u_eps_abel_accept | FINDINGS_2026-10-25_t761u_eps_abel_accept_CONFIRM.md | YES | 0aaec40d13228770a4647189566017f65ff6d4c7ff8ce95586f513c80ceef956 |

Auditor action: confirm match, then (only Auditor/lane) update row status. This file edits nothing.
