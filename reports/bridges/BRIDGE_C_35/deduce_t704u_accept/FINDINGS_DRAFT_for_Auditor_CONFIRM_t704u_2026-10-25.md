# FINDINGS DRAFT (executor; for Auditor CONFIRM; NOT an Auditor CONFIRM) — deduce_t704u_accept LOCK (G-A1b R-DS0)
Stamp: 2026-10-25 CDT. Authority: Arvin t704s4427 AUTHOR ACCEPT (R-DS0 only). Base: BRIDGE_C_35/. CORE_FREEZE; SF-W7-3; local only; no order78.

## Hash match (live at draft time)
| Artifact | sha256 | Live |
|---|---|---|
| deduce_t704u_accept/PREREG.md | dc74aab66ab20821251625d1dbc6dc1d023e6389a8710c926fa869f522524470 | MATCH |
| deduce_t704u_accept/PREREG.sha256 | e8d481896077af3489cc615a234629018a59e83c1f7a577449b0647add25870b | MATCH |
| deduce_t704u_accept/RESULTS.md | e5b65693825612866c76c5466e48b6e85abf0935bad12d51664a253048c2790a | MATCH |
| deduce_t704u_accept/SHA256SUMS | 2700f98c510d0d48bb73c59c1135a085ccb3bdafa1619890f5eca95c810a43f3 | MATCH (3/3 OK) |
| STREAM_IDLE_LOCAL.md (root) | 6b54d64221bdb2ca0744a4b3392b3d641d61ccf14f2613d547b109c1cd9cb35c | MATCH |
| inventory_check/SHA256SUMS | 59a05632870fe9707a1c1376cb5024e8e2a7e15955687ff692059338f40b97a4 | MATCH (55/55 OK) |
| Candidate (t700) | 0504098862367dc0c8d2ea08af4460feb19064c23481701bf85d9e7cf63c5650 | MATCH (unaltered) |
| Baseline FINDINGS t695u | 437d4571e0f707460c7ac2a7dd983d0649161dd7975779101907eaedba7d7476 | MATCH (stands) |
| Pre-ACCEPT FINDINGS t700u | 914bda3c5830a0fe4efd0d24ff91d337d95a10406dd1bbc3459c18b5f3b44898 | MATCH (draft-only; superseded on CONFIRM) |
Order: PREREG sha fixed before RESULTS written; RESULTS cites PREREG sha unchanged.

## Claims to CONFIRM
1. R-DS0 only ingested as ACCEPT-sourced Cat A [t704s4427; 05040988…]; R-DS1/R-DS2 NOT ingested.
2. G-A1b CLOSED under R-DS0; no Dual-split cells; Dual-split OUT of scope for residual_slash.
3. Selectors baseline 437d4571… stands (S-B1′, weakened S-B1; t695s4386; 3d502756…).
4. UNIQUE-in-family / overall PARTIAL (G-A1c OPEN). δ≡0/RG76d/Bridge YES NOT forced (G-A3 ABSENT). Bridge PARTIAL; READY NO; residual-C OPEN.
5. Scoping/fences: local modular only; no nonlocal EH11D/Ω₁₁D/F_total; SF-W7-3; no numeric invent; no order78.

## Open set
G-A1c, G-A3, G-R2; X4 coeffs ABSENT; B3 empty.
