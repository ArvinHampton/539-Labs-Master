# order55 PREREG (Bridge C, 35-component law vector; RG* labels only; CORE_FREEZE; new files only in order55/)
## RG45c-2′ (numeric, Category A-numeric): A1(R_j) sawtooth formula under per-case Poisson-scaled t
Object, walls, z_j, f, R_j, prediction A1_pred, m_r, P, B̄1(0)=0: IDENTICAL to order54 PREREG RG45c-2 (sha af2e5c10…1404); `direct` and `pred` reused verbatim from order54/scripts/rg45c.py (read-only exec), except `direct` is evaluated in chunks of lines (same terms, same truncation rules) to bound memory.
Per-case scale: P* = max(P_line(u_j), N_t) (both from order18 a2.period), T_j = π²/(40·Q(u_j)·P*²) (so Poisson remainder ≈ e^{−40}).
t schedule: t_k = c_k·T_j, c = (1, 1/2, 1/4). A1_num = quadratic-in-t polynomial fit (exact interpolation through 3 points) of √t·R_j, evaluated at t=0.
Sample (fixed now, deterministic, not chosen from outcomes): x ∈ XS[:6] = {1/15,…,1/10}; companions j ∈ {0,5,10,…,100} (21); both walls → 252 cases.
Plus 2 adversarial cases fixed from order54 (worst per wall): (x=1/14,j=26,w=1), (x=1/14,j=14,w=2). Total 254. No cases dropped/added after run; any case that cannot run (error/timeout) counts as FAIL.
PASS iff max_case |A1_num − A1_pred|/max(1,|A1_pred|) ≤ 1e−6 AND gating control FAILS: one-sided convention B̄1(0)=−½ must miss by >1e−4 on ≥1 case with θ_j+r∈Z and m_r≠0 (else control VOID, verdict states endpoint untested).
Secondary (reported, not gating): per-wall worst error; count of endpoint cases.
## RG46: runs only if an explicit Ξ_compl or A1−Ξ_compl object tied to the v12 shadow Ξ is found WRITTEN in sources (order5/18/53/54 and BRIDGE_C_35 top-level docs). A source search (grep for Ξ_compl / Xi_compl / shadow) is done after RG45c-2′; if none, RG46 SKIP with obstruction documented. No Ξ/Π/α1 invented.
## Phase-aware k≠0 bound: only if written; else Open.
