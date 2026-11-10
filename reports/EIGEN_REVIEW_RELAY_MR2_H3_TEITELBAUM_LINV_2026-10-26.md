# EIGEN Rule 5 REVIEW/RELAY — MR2 H3 Teitelbaum 𝓛 FINDINGS (2026-10-26 ~19:25 CDT)
Authority: Rules 4–5 Eigen↔MR2; Physicist CONTINUE after ACCEPT 6fa05a81…; MR2 took H3 compute
Source: MR2-FINDINGS-H3-TEITELBAUM-LINV_2026-10-26.md
Source sha256 (disk-MATCH): bdcaf1e6a898c8d2a894a4f3c97bacb2131f4983c784e4af5ea42f8c506257ef
Script sha (disk-MATCH): cf45cf5e7910bfe81b33ab604f911ca68342fd1a4297cb762bea41deff7d00f0 — Eigen re-ran: a₇=−7; w(θ³f̄)=40 under stated convention.
tip Soft SF LOCK 7cddb188… tip_touched NO. Kerr BLOCKED. GAP-5 Owner untouched. Bridge PARTIAL READY NO. P5a NOT claimed.

## REVIEW (Eigen)
STATUS absorb: **PARTIAL** — MATCH.
- **H3-0** a₇=−7 (JL theta + Hecke) — **ACCEPT PROVED** (script re-run MATCH).
- **H3-1** Teitelbaum one-vertex — **ACCEPT UNPROVEN** (named gap: edge-pairing + Sym² cocycle + 7-adic integration).
- **H3-2** Colmez −2a₇′/a₇ — **ACCEPT UNPROVEN** (overconvergent symbols ABSENT).
- **H3-3** BM threshold — **ACCEPT ABSENT** (no BM lit on disk; CITE-VERIFY failed).
- **H3-4** w(θ³f̄)=40 under stated convention — **ACCEPT PROVED under that convention**, with Soft SF HOLD pending convention reconcile below.

## Filtration convention reconcile (answer to MR2 ask)
Two different normalizations were compared; they are **not** Soft SF-inconsistent once named:
1. **Prior R4-2b / DEEPEN list {28,22,…,4}:** Jochnowitz/Serre filtration bound starting from **geometric weight w(f)=4** on Γ₀(7), with steps of size (p−1)=6 inside the θ-cycle, upper mark 4+3(p+1)=28. That list never claimed to be the Katz filtration in the level-1 ring.
2. **H3-4 compute:** Katz/Serre filtration of the **q-expansion inside level-1** spans ⟨E₄ᵃ E₆ᵇ Δᶜ⟩ mod 7. Under that ambient, w(f̄)=16 (not 4) — expected, since f is level 7 — then +8 each θ-step (p+1) while 7∤w → w(θ³f̄)=40. Eigen re-ran: MATCH.

**Soft SF rule:** do **not** treat 40 as Soft SF-clean against the prior candidate list until one of: (A) Owner/Auditor Writes which convention is operative for GAP-4/H3, or (B) MR2 recomputes filtration in the Γ₀(7) / geometric-weight-4 convention matching R4-2b. Until then: H3-4 = PROVED(level-1 Katz) + CONVENTION FLAG; prior list STANDS as a different named bound.

Note (Rule 4 assist, not invent): shared box has `/tmp/pm/bin/sage` — if MR2 wants Eigen compute-assist on H3-1/H3-2 once a Written method/code path exists, ping; no 𝓛 value invented.

## RELAY (to Physicist — first findings)
MR2 H3 Teitelbaum 𝓛 PARTIAL. a₇ pinned to −7 (PROVED). Teitelbaum one-vertex and Colmez routes still UNPROVEN (tooling/integration gaps). Breuil–Mézard threshold ABSENT on disk. Filtration: under level-1 Katz convention w(θ³f)=40 (PROVED), which is not Soft SF-clean against the prior {28,…,4} list until convention is Written or recomputed in the Γ₀(7) weight-4 convention. Does NOT prove P5a; Bridge PARTIAL READY NO; GAP-5 untouched.

Soft SF → Auditor (CONFIRM may HOLD). tip untouched.
