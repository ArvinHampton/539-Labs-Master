# AUDITOR FINDINGS — batch clear "Pending Auditor CONFIRM" rows, STREAM_IDLE_LOCAL — t1055u — 2026-10-25 19:25 CDT (America/Chicago)
Residual-vs-Resonant. Residual-C LOCKED at LOCK_DIGEST 964294ccc4516dee846676510a6e1f99d830a355ed29bb84527aad84cdd4274d and NOT touched. invent-ban ON; CORE_FREEZE; no order78; Empty #7–#9 HOLD; 4da09dec… not revived. PASS/FAIL not altered. No physics invented. This was a reconciliation only, with no re-audit. STREAM_IDLE_LOCAL was NOT edited. Bridge PARTIAL; READY NO.

## Inputs verified (sha256 recomputed)
- Inventory reports/INVENTORY_POST_LOCK_OPEN_ITEMS_t1055u_2026-10-25.md = d299708f2bd2717cea2aa09be6b5bedf166f8aa60cf5c5dcd3ee7be1d3e6b277: MATCH with the expected d299708f… (L-10).
- Handoff reports/AUDITOR_HANDOFF_STREAM_PENDING_CONFIRMS_t1055u_2026-10-25.md = 612275ebbdd7a2a11d5dd3a711715c00a8b84111dc857445d2732bed82c21ad9: MATCH.
- Live STREAM_IDLE_LOCAL reports/bridges/BRIDGE_C_35/STREAM_IDLE_LOCAL.md = c6df07ef31cdfe31c2da18b978b8fd5320cd8938651d44e42f2ecb6d14012930. The inventory cites ef47b136…. I used the live tip (see Soft SF-1).
- HASH_INTEGRITY.md = 066413fdf5a9beac0236d86e5a2610e10d28696df6425ec65ba833f47e69a875 (before this append). It records LOCK_DIGEST 964294cc… and POST_LOCK 492fb3ac….

## Method
For each row, I recomputed sha256 for the row's package PREREG.md, RESULTS.md and SHA256SUMS under BRIDGE_C_35/deduce_*/ and compared them with the hashes cited in the row: 36/36 MATCH. I then confirmed that an existing Auditor CONFIRM FINDINGS cites the same package hashes and states verdict MATCH/CONFIRM.

| Line | Ticket / tag | Subject | Prior Auditor CONFIRM FINDINGS (path, sha256) | Status | Note |
|---|---|---|---|---|---|
| 22 | t695u deduce_t695u_accept | t695s4386 ACCEPT of 3d502756…, selectors Cat A | FINDINGS_2026-10-25_t695u_local_accept.md 437d4571e0f707460c7ac2a7dd983d0649161dd7975779101907eaedba7d7476 | CLEARED-by-existing-CONFIRM | The handoff marked this "missing" because it only matched filenames. A non-standard filename exists. It cites 8cb69ab3/f36beeea/a17199bc, all MATCH |
| 24 | t704u deduce_t704u_accept | R-DS0 → G-A1b | FINDINGS_2026-10-25_t704u_accept_confirm.md b34aebe65a3f57eff1690dde5fce01efa8e3722331e1098ee5f6efb578c905ac | CLEARED-by-existing-CONFIRM | Lowercase filename. It cites dc74aab6/e5b65693/2700f98c, all MATCH |
| 33 | t734u deduce_t734u_accept | R-UQ0 → G-A1c | FINDINGS_2026-10-25_t734u_accept_CONFIRM.md 7e20e84c4508dcff21169c89eb407a914e9f99ff56e478dc71cf406a23b06a24 | CLEARED-by-existing-CONFIRM | MATCH; SF none |
| 35 | t740u deduce_t740u_accept | R-NV0 → G-R2 | FINDINGS_2026-10-25_t740u_accept_CONFIRM.md 2b959003d46762278c8da36a6562da63cd5b6a30d47f02faed8ed2d23900638b | CLEARED-by-existing-CONFIRM | ALL MATCH |
| 36 | t743u deduce_t743u_b3 | B3 ABSENT-with-gap | FINDINGS_2026-10-25_t743u_b3_CONFIRM.md 0e9e53ddd7b019be66f6e856e0da4701811a304065e3a2517aba968018621fd5 | CLEARED-by-existing-CONFIRM | ALL MATCH |
| 37 | t748u deduce_t748u_accept | B3-α KEEP | FINDINGS_2026-10-25_t748u_accept_CONFIRM.md b96ff7bdd579d6b431f44ba1421f22cfa025770cbb70aa721da9607cb0a5fde1 | CLEARED-by-existing-CONFIRM | 6/6 MATCH |
| 38 | t749u deduce_t749u_tunnel | tunneling ABSENT-with-gap | FINDINGS_2026-10-25_t749u_tunnel_CONFIRM.md 8a2b8755f0f6345e03d1964f3eebcc9597fc07cc00586d468d083d59579702ee | CLEARED-by-existing-CONFIRM | 6/6 MATCH |
| 39 | t756u deduce_t756u_accept | T-α KEEP + T-γ FYI | FINDINGS_2026-10-25_t756u_accept_CONFIRM.md 5f5f283203834eeafe78a9d44a1a7a70baac51e3ac84c945bc286df25afc39f7 | CLEARED-by-existing-CONFIRM | MATCH; SF none |
| 42 | t761u deduce_t761u_accept | AW-α Ξ defs | FINDINGS_2026-10-25_t761u_accept_CONFIRM.md aac04151accb03b0464ffaf2fff09b733af99b820a97479f262a6d82f60b13d1 | CLEARED-by-existing-CONFIRM | Written baseline is face665b…. AW-X4 soft SF carried |
| 44 | t761u deduce_t761u_outer_accept | O-α outer_* | FINDINGS_2026-10-25_t761u_outer_accept_CONFIRM.md b467bb54b7d759416cf9898ba806926758f01efb7fe8c0624edf13458d35a5f0 | CLEARED-by-existing-CONFIRM | Written baseline is 46e4e3bd…. O-X4 soft SF carried |
| 46 | t761u deduce_t761u_path_psi_accept | PB-α path/branch/ψ | FINDINGS_2026-10-25_t761u_path_psi_accept_CONFIRM.md c26b5f72c4603acd05623df5d745bfa538c4a14131b222bf92c00537f34f458e | CLEARED-by-existing-CONFIRM | Arg ACCEPT-default soft flag carried |
| 48 | t761u deduce_t761u_eps_abel_accept | E-α ε→0/W₇ | FINDINGS_2026-10-25_t761u_eps_abel_accept_CONFIRM.md 0aaec40d13228770a4647189566017f65ff6d4c7ff8ce95586f513c80ceef956 | CLEARED-by-existing-CONFIRM | EP-β analogy soft SF carried |

Note: Line 46 of the handoff says this CONFIRM exists, and it matches. The inventory still lists L-11 (PB-α awaiting Owner ACCEPT) as an Owner item. The row LOCK records an ACCEPT. That item is outside this clear and needs Owner/coordinator reconciliation.

## Counts
12 cleared / 0 still pending / 0 superseded. Row content was not changed. The coordinator may flip each row to "Auditor CONFIRM <sha>".

## Soft SF
- SF-1: The inventory cites STREAM_IDLE_LOCAL ef47b136…, but the live file is c6df07ef…. I used the live tip, and all 12 row hashes check out against it.
- SF-2: CONFIRM filenames are inconsistent for t695u (local_accept) and t704u (lowercase confirm). That is why the handoff reported them as missing. Hygiene only.
- SF-3: Physics-level soft SFs carried unchanged from the prior CONFIRMs: AW-X4/O-X4 G-2, Arg default, EP-β.
- SF-4: The residual-C file whose sha should be 492fb3ac… was not located by a filename/sha scan of reports/*.md. I did not verify the file sha, and I made no edit.
