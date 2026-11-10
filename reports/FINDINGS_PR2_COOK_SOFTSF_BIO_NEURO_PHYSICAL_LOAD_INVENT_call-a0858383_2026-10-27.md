# FINDINGS — PR2 Cook Soft SF — Bio/Neuro physical-load link INVENT (call-a0858383) — 2026-10-27
Lane: PR2. Status: **Soft SF Write-only**. REPORTS only; **No RECS**. Kerr BLOCKED. Tip untouched (BEFORE `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`; never opened/edited). Catalog READ-ONLY, unchanged.

## Authority / cites (re-hashed live)
| Item | sha256 (live) | Note |
|---|---|---|
| OW invent-lift ALL_LANES 2026-10-27 | 5cbc33ac93f166eec2b0680e0435b87c4eb97fd762777da6df8932c23eb23640 | **Dispatch expected `1c7163de…` — MISMATCH**; live file = its own sidecar. Cited at live hash; mismatch noted, unresolved. |
| OW blanket 2026-10-26 | 9b993a72bcdfed3fe2d78c15cbe76d0c8197958ca5ac60111546cd5e7ec6498b | on disk, matches |
| Prior Bio/Neuro invent Soft SF | b7cf379cb59b56cd075d509dd76a9a62a46b62a19ed8db7fa7cddd017c21a877 | Local R5 ACCEPT b1641b60fe47bbf32065d1133a156c3674a1de4eaec49318e6d70e3e97c19855 |
| Catalog obs-data-PR2-COSMO-BIO-NEURO.md | 4ed155d55c3a18ca4bc96a6a6eec4c1806abfc2e270f355f1ea58a197119dd04 | UNCHANGED |
| Owner clause swap (via PM, relayed by parent) | — (verbal relay, no file) | invent label = "**invented pending mathematical proof**" |

## Label rule
Every invented item below is marked **[invented pending mathematical proof]**. Invented = link/mechanism/pattern only; **no** catalog [V] numbers are invented; free parameters are OPEN. Catalog values used are quoted as-is (N2, N10 rows).

## Status note — prior Soft SF (b7cf379c…)
IC-1/IC-2/IC-3 stand as **Soft SF Write-only** (cite b7cf379c…). Under the Owner clause swap their [INVENTED] marks *read as* "invented pending mathematical proof"; that confirmed subject is **not amended**. G-B1/W4.3 coefficients remain **ABSENT** as Author numbers (only a pattern is offered in PL-4).

## Catalog inputs (quoted, not altered)
- N2: ~20 W, ~20% resting energy [P]; AP 47%, postsynaptic 34%, resting 13%, recycling 3%; +1 AP/neuron/s → +145 mL O₂/100 g/h; ≤15% simultaneously active (Attwell & Laughlin 2001) [V soft].
- N10: 0.5–120 m/s [P]; v ≈ ∝ diameter in geometrically similar myelinated fibres (Waxman 1980) [V qualitative]; bridge-target causality.
- N1 86.1×10⁹ neurons (as used in IC-1).

## PL-1 — Metabolic rate-budget law (N2) [invented pending mathematical proof]
Ansatz: P_tot = P_0 + N·(e_AP·f̄ + e_syn·f̄·s̄) where f̄ mean rate, s̄ synapses/neuron, e_AP, e_syn, P_0 OPEN.
**Lemma 1 (proof).** If the AP share σ_AP = N e_AP f̄ / P_sig is fixed, then f̄ = σ_AP P_sig /(N e_AP). With P_sig ≤ P_tot ≈ 20 W [P], σ_AP = 0.47, N = 8.61×10¹⁰: f̄ ≤ 0.47·20/(8.61×10¹⁰·e_AP) = 1.09×10⁻¹⁰ W / e_AP. Proof: substitution; monotone in P_sig. ∎
Corollary: the 4-way split (0.47,0.34,0.13,0.03; sum 0.97) is scale-free in this ansatz iff e_syn s̄/e_AP = 0.34/0.47 = 0.723 — a **dimensionless invariant** (exact arithmetic from catalog ratios).
Falsification: any measured (e_AP, f̄) with e_AP f̄ > 1.09×10⁻¹⁰ W violates PL-1 under the 20 W budget; sparsity ≤15% is consistent iff f̄_active/f̄ ≥ 1/0.15 ≈ 6.67. **Status: UNTESTED** (e_AP, f̄ not in catalog — ABSENT).

## PL-2 — Conduction–causality latency pattern (N10) [invented pending mathematical proof]
Ansatz: v = k·d (Waxman proportionality), latency τ(L) = L/(k d). Causal window for path length L (OPEN): τ ∈ [L/120, L/0.5] s.
**Lemma 2 (proof).** For fixed L, τ_max/τ_min = 120/0.5 = 240 exactly, independent of L and k. ∎ Hence a 2.38-decade latency band is a catalog-forced invariant; any claimed neural causal-synchrony mechanism needing timing spread < 1/240 of path latency across the full fibre range is excluded.
Falsification: a fibre class off the v∝d line (geometrically similar myelinated) falsifies the linear link; **Status: QUALITATIVE-CONSISTENT** with Waxman [V qual], quantitative test ABSENT.

## PL-3 — Energy–conduction coupling (N2 × N10) [invented pending mathematical proof]
Ansatz: per-length axon cost c(d) = a d² (volume) + b d (membrane), a,b OPEN; v = k d.
**Lemma 3 (proof).** Cost per unit speed c/v = (a d + b)/k, minimized over admissible d ≥ d_min at d_min; total cost to achieve latency τ over L with v=L/τ: c = a(L/kτ)² + b(L/kτ), strictly convex in 1/τ, so marginal cost of speed dc/dv = (2a v + b k)/k² is increasing ⇒ **power-speed trade-off is superlinear** (∝ v² at large v). ∎
Pattern prediction: the 47% AP share (N2) should rise with mean v in a fixed volume; correlation sign ρ(σ_AP, v̄) > 0. **Status: UNTESTED** (paired data ABSENT).

## PL-4 — RH / scoped-C1 → Bio/Neuro load silence; W4.3 coefficient→leg pattern [invented pending mathematical proof]
RH/scoped-C1 legs carry no physical-load term in-catalog; we posit the load enters only via dimensionless invariants: Λ = (σ_AP, e_syn s̄/e_AP, τ_max/τ_min, α_taxon(IC-1)).
Pattern (not numbers): W4.3 coefficient vector w = (w_E, w_C, w_S) maps to legs (N2 energy, N10 conduction, IC-1 scaling) with w ≥ 0, Σw = 1, all **OPEN**. **Lemma 4 (proof).** Under any such convex weighting, the composite load index Ξ = Σ w_i Λ̂_i (Λ̂ normalized to [0,1]) is bounded in [min Λ̂, max Λ̂]; so a silence result (Ξ ≈ 0) requires every leg with w_i > 0 to be ≈ 0. ∎ Thus "load silence" is falsified by any single nonzero normalized leg carrying positive weight.
**Status: OPEN** — G-B1/W4.3 coefficients ABSENT; no Author numbers invented.

## Summary table
| ID | Link | Form | Rows | Status |
|---|---|---|---|---|
| PL-1 | N2 metabolic | f̄ ≤ 1.09e-10 W/e_AP; invariant 0.723 | N1,N2 | UNTESTED (ABSENT inputs) |
| PL-2 | N10 conduction | τ_max/τ_min = 240 | N10 | QUAL-CONSISTENT |
| PL-3 | N2×N10 | c(v) convex, ρ(σ_AP,v̄)>0 | N2,N10 | UNTESTED |
| PL-4 | RH/C1→load, W4.3 pattern | convex weighting bound | N2,N10,IC-1 | OPEN |
All four: **[invented pending mathematical proof]**.

## Constraints held
Tip untouched; Kerr BLOCKED; catalog unchanged; Gap-X1 Local cite-only; no tip fold of invent labels; no RECS; no messages; no amend of confirmed subjects.
