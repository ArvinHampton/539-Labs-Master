# FINDINGS — PR2 Cook Soft SF — Bio/Neuro physical-load PROOF PURSUE (call-a0858383) — 2026-10-27
Lane: PR2. Status: **Soft SF Write-only** (NEW; subject Soft SF not amended). REPORTS only; **No RECS**. Kerr BLOCKED. tip Soft SF LOCK untouched (BEFORE `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`; never opened/edited). Catalog READ-ONLY, unchanged.

## Owner standing rule (cited)
Via Physicist and Mathematician: invent → **must pursue mathematical proof** of invented Bio/Neuro physical-load values labeled **"invented pending mathematical proof"**. OWNER AMEND (via PM): invent-then-prove is **where feasible**; where proof is not feasible, **record why** and **keep** the label — no forced/fake proof. Applied per PL below.
Invent-ban LIFT call-a0858383; label clause "invented pending mathematical proof".

## Authority / cites (re-hashed live 2026-10-27 12:18 CDT)
| Item | sha256 (live) | Note |
|---|---|---|
| OW invent-lift ALL_LANES `OWNER_WRITE_INVENT_BAN_LIFTED_ALL_LANES_PURSUE_FREEDOM_RIGHT_AUTHORITY_2026-10-27.md` | d087ff9d07f4b58a37aa27c8a85309c16b12969d4e38f661955573dee67de5b4 | **Dispatch expected 5cbc33ac93f166eec2b0680e0435b87c4eb97fd762777da6df8932c23eb23640 — MISMATCH.** File mtime 12:17 CDT; own sidecar matches live hash; contains LOCKED proof-pursue line. Cited at live hash; mismatch unresolved. "Where feasible" amend not present in file text (verbal relay via PM). |
| Subject FINDINGS (PHYSICAL_LOAD_INVENT) | c1c6775bae7d041a7460e6850e7ce6aa787937f96ca29a9b55702ca1db80d8fb | MATCH |
| Subject PRESS | b645e3bd24c6e977c71bad5559948be42f46dd0d3549ffccd82c52738002d93a | MATCH |
| Subject Local R5 ACCEPT REVIEW | 38443ead937f2817c32efe40a3589cff742d12a99d6aac59de92d67438c5cc69 | MATCH |
| Catalog obs-data-PR2-COSMO-BIO-NEURO.md | 4ed155d55c3a18ca4bc96a6a6eec4c1806abfc2e270f355f1ea58a197119dd04 | MATCH, unchanged |
| Tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | BEFORE MATCH |

## Catalog rows used (quoted, not altered)
- N1: 86.1 ± 8.1 ×10⁹ neurons [V hard].
- N2: ~20 W [P]; AP 47%, postsynaptic 34%, resting 13%, recycling 3% (sum 97%); ≤15% simultaneously active (Attwell & Laughlin 2001) [V soft, model-based].
- N10: 0.5–120 m/s [P]; v nearly ∝ diameter in geometrically similar myelinated fibres (Waxman 1980) [V qualitative].
No new measured values; no Author numbers written as values.

## PL-1 — Metabolic rate-budget law (N1, N2) — [invented pending mathematical proof]
**Claim (subject c1c6775b…):** P_tot = P_0 + N(e_AP f̄ + e_syn f̄ s̄); f̄ ≤ 1.09×10⁻¹⁰ W/e_AP; invariant e_syn s̄/e_AP = 0.723.
**Derivation.**
- Lemma 1a. Define P_AP = N e_AP f̄ and σ_AP = P_AP/P_sig. Then f̄ = σ_AP P_sig/(N e_AP). Since P_sig ≤ P_tot and the map is monotone increasing in P_sig, f̄ ≤ σ_AP P_tot/(N e_AP). With σ_AP=0.47, P_tot=20 W, N=8.61×10¹⁰: f̄ e_AP ≤ 1.0918×10⁻¹⁰ W. Propagating N1 range (78.0–94.2×10⁹): bound ∈ [9.98×10⁻¹¹, 1.205×10⁻¹⁰] W. ∎ **PROVED (lemma)**, conditional on ansatz + taking 20 W [P] as upper bound on P_sig.
- Lemma 1b. Under the ansatz, P_syn/P_AP = (N e_syn f̄ s̄)/(N e_AP f̄) = e_syn s̄/e_AP (f̄, N cancel, f̄>0). Catalog ratio 0.34/0.47 = 0.72340… ∎ **PROVED (lemma)**.
- Lemma 1c. If f̄ = p·f_act with active fraction p ≤ 0.15 (N2), then f_act/f̄ = 1/p ≥ 6.667. ∎ **PROVED (lemma)** under that decomposition.
**OPEN:** e_AP, e_syn, s̄, P_0, f̄ (ABSENT from catalog); whether ansatz form is physically correct; resolution of the 3% unassigned share; N2 split is rodent model, 20 W is [P].
**Proof feasibility of parent:** NOT feasible from catalog alone — parent is an empirical ansatz; a mathematical proof cannot establish a physical law without measured e_AP, f̄. Label KEPT.
**Falsification:** measured e_AP f̄ > 1.205×10⁻¹⁰ W (with 20 W budget) refutes; **UNTESTED** (inputs ABSENT).

## PL-2 — Conduction–causality latency (N10) — [invented pending mathematical proof]
**Claim:** v = k d, τ(L) = L/v; τ_max/τ_min = 240.
- Lemma 2. For fixed L>0 and v ∈ [0.5,120] m/s, τ = L/v is strictly decreasing in v, so τ ∈ [L/120, L/0.5] and τ_max/τ_min = 120/0.5 = 240, independent of L and k; log₁₀240 = 2.380 decades. ∎ **PROVED (lemma)** (conditional on N10 range, itself [P]).
- Corollary: any mechanism requiring timing spread < τ/240 across the full fibre range is excluded for that L. **PROVED (lemma)** as consequence.
**OPEN:** the linear link v = k d (Waxman is qualitative "nearly proportional"; k, d range, myelin/internode/temperature dependence ABSENT); L ABSENT.
**Proof feasibility of parent:** NOT feasible — v ∝ d is an empirical relation; catalog gives qualitative support only. Label KEPT.
**Falsification:** a geometrically similar myelinated fibre class off v∝d refutes the link; **QUALITATIVE-CONSISTENT**, quantitative test ABSENT.

## PL-3 — Energy–conduction coupling (N2 × N10) — [invented pending mathematical proof]
**Claim:** c(d) = a d² + b d, v = k d; superlinear power–speed; ρ(σ_AP, v̄) > 0.
- Lemma 3a. Substituting d = v/k: c(v) = a v²/k² + b v/k; c'(v) = (2a v + b k)/k²; c''(v) = 2a/k² > 0 for a>0, k>0 ⇒ strictly convex, marginal cost strictly increasing, c ~ v² as v→∞. ∎ **PROVED (lemma)** given ansatz and a,k>0 (a=0 gives linear — boundary case).
- Lemma 3b. c/v = (a d + b)/k is increasing in d for a>0, so minimized at d_min on [d_min, ∞). ∎ **PROVED (lemma)**.
**NOT proved:** ρ(σ_AP, v̄) > 0. Requires a volume-constrained model linking v̄ to AP energy share and paired data; neither in catalog. Proof **not feasible** — recorded why: correlation sign is an empirical statistic, not derivable from N2 (single split) and N10 (range).
**OPEN:** a, b, k, d_min; cost form (d² volume, d membrane) unvalidated.
**Falsification:** measured sublinear cost–speed in myelinated fibres, or ρ ≤ 0; **UNTESTED** (paired data ABSENT). Label KEPT.

## PL-4 — RH/scoped-C1 → load silence; W4.3 coefficient→leg pattern — [invented pending mathematical proof]
**Claim:** Ξ = Σ w_i Λ̂_i, w_i ≥ 0, Σw_i = 1, Λ̂_i ∈ [0,1].
- Lemma 4a. Ξ is a convex combination ⇒ min Λ̂ ≤ Ξ ≤ max Λ̂. Proof: Σw_i Λ̂_i ≥ Σw_i min Λ̂ = min Λ̂; symmetric for max. ∎ **PROVED (lemma)**.
- Lemma 4b. All terms nonneg ⇒ Ξ ≥ w_j Λ̂_j for each j; so Ξ ≤ ε implies Λ̂_j ≤ ε/w_j for every w_j > 0; Ξ = 0 iff Λ̂_j = 0 for all j with w_j > 0. ∎ **PROVED (lemma)**.
**OPEN:** w = (w_E, w_C, w_S) (G-B1/W4.3 coefficients ABSENT); normalization maps Λ → Λ̂ undefined; the premise that RH/C1 legs couple to load only via dimensionless invariants.
**Proof feasibility of parent:** NOT feasible — coupling premise is a modeling posit with no catalog leg; no Author numbers invented to close it. Label KEPT.
**Falsification:** any single nonzero Λ̂_j with w_j>0 refutes "silence" (by 4b); **OPEN**.

## Summary
| ID | PROVED (lemma) | OPEN | Parent | Falsify status |
|---|---|---|---|---|
| PL-1 | 1a bound 1.09e-10 W (N1 range 0.998–1.205e-10); 1b 0.7234; 1c ≥6.67 | e_AP,e_syn,s̄,P_0,f̄; ansatz | invented pending mathematical proof (proof not feasible: empirical) | UNTESTED |
| PL-2 | ratio 240 (2.38 dec); exclusion corollary | v=kd link, k, d, L | invented pending mathematical proof (not feasible: empirical) | QUAL-CONSISTENT |
| PL-3 | convexity, c'' = 2a/k²; d_min optimum | ρ>0 (not feasible); a,b,k | invented pending mathematical proof | UNTESTED |
| PL-4 | convex bounds; silence ⇔ all weighted legs 0 | w, normalization, coupling premise | invented pending mathematical proof | OPEN |
Prior IC-1..IC-3 (b7cf379c…): status-noted only, unchanged.

## Blockers
OW invent-lift hash mismatch (dispatch 5cbc33ac… vs live d087ff9d…); "where feasible" amend is verbal relay, not in OW file; all parent free parameters ABSENT from catalog.

## Constraints held
tip Soft SF LOCK untouched (AFTER recorded in PRESS/report); Kerr BLOCKED; catalog unchanged; subject not amended; no new measured values; no RECS; no messages.
