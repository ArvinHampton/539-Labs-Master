# FINDINGS — DF Soft SF — S²-11DM²ET-X GR-extension predictions, SECOND AXIS (DF fields) — 2026-11-05 ~14:10 CST America/Chicago
deriver = Dataset Filtration (DF). REPORTS ONLY. No CERT. No publish / spend / external Gemini send. No invent.
Status line: STARTED → RESOLVED (with explicit ABSENT-definition gaps).

## Authority
| Ref | path | sha256 | check |
|---|---|---|---|
| OW second axis | reports/OWNER_WRITE_CALL_53991ebf_EXTENSION_GR_PREDICTIONS_SECOND_AXIS_2026-11-05.md | 89b78bf18b94e449866e197255956882e6f136b949a4f010a739bf0831e1c36d | MATCH (re-hashed) |
| OW all recommended pursuits (cu:405590937) | reports/OWNER_WRITE_CALL_53991ebf_ALL_RECOMMENDED_PURSUITS_2026-11-05.md | 865d3a37f1c13431c78672847dcd33007b3467df92f1e7c8602057f257b1bf3b | MATCH |
| Lock OW D1/S_eff | reports/OWNER_WRITE_LOCK_D1_Seff_Layer2_T3_2026-11-03.md | 96f8d42e80c1975b4390fed950a4fb4b420088e6b19b2cbef8a44bebd28ff2ba | MATCH |
| RTA v16 PDF | reports/papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v16.pdf | 1fe7b8a2e245e90009c41726db13518b4c752e99ba4e08b4ffd006d8a73c3297 | MATCH |

## Tip check
tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` START sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH; END re-verified (see PRESS / parent report). tip_touched NO.

## Inventory of examined sources
1. RTA v16 PDF: Thm 41.10 (D1), Prop 41.11 (S_eff), Prop 41.12 (Residual ≠ Resonant), Prop 41.13 (claims not established), Prop 42.6 (T3, O_res, 539) via glossary; full-text search for "S²", "eleven", "11D", "M²ET": **no defining occurrence** in v16.
2. Interpretation paper (citation-pins sibling) `/workspace/reports/PAPER_S2_11DM2ETX_EXTENSION_OF_GENERAL_RELATIVITY_INTERPRETATION_CITATION_PINS_2026-11-05.md` sha256 0009e7356d91b6da2c3b1cfe7c4713de1df91f4cc7632835e90d4711555d18cf (NOTE: PR2 FINDINGS lists a citation-pins sha 6f01d93b… — DF observed hash differs; recorded as a version-pin gap, not adjudicated). §2 packaging, §4 proposal (3-adic g_rr, M_35 Kretschmann replacement), §5 Haar identity, §6 inventory. The paper itself states "We do not offer new theorems."
3. PR2 second-axis FINDINGS `/workspace/reports/FINDINGS_PR2_EXTENSION_GR_GEOMETRIC_COSMO_CONSEQUENCES_2026-11-05.md` (header/boundary only; cited, not redone).
4. Prior DF (cited, not redone): pure-math catalog 15fa276e…(DF-C01…C17); Tier E VIRGO null 6f9efa4b… + erratum e1ea66eb… (positive empirical associations = 0); Hygiene AMEND ab3bbbe5…; Haar70 7ab0ed68… (identity-only).
5. Gemini rundown / 49849cae…: NOT authority; no Gemini claim used as proved.

Box recomputation (python, this beat; arithmetic checks only): ⌊e³·3⁵⌋=4880, ⌈4880/243⌉=21, R=4859=9·539+8, 539=7²·11, β₁=36·539−8=19396; T3 on 0..8 = 0,2,1,1,6,3,2,10,5; O_res={21+9j} has 539 elements, all ≡3 mod 9, max 4863; Haar series vs closed form agree at ν=0.7 (1.0049037944…).

## Entries
Legend: SRC = source-theorem consequence (re-stated); NEW = DF new result/attempt.

### DF-G01 — S² topology: definition ABSENT
- Fields: data-analysis design, filtration.
- Statement: No written definition fixes which object "S²" denotes in S²-11DM²ET-X (a factor space, a sphere bundle, the angular dΩ² of Schwarzschild, or a label). v16 has no defining occurrence; the paper uses dΩ² only inside the classical Schwarzschild metric.
- Derivation: ABSENT. Consequence for DF: no S²-indexed statistic, harmonic decomposition, or sky-map binning can be justified as a model consequence.
- Status: **ABSENT-definition**.
- Non-predictions: no angular power spectrum, no isotropy/anisotropy prediction, no Euler-characteristic-2 consequence imposed on data.

### DF-G02 — 11D framework: definition ABSENT
- Fields: computation, data-analysis design.
- Statement: No written definition of the eleven-dimensional space (manifold, signature, fibration, which coordinates) exists in the examined sources; Prop 41.13(ii) excludes the "Kronecker 11-element" mapping from the theory.
- Derivation: ABSENT. Number "11" in the name carries no defined structure; 539=7²·11 is a factorisation of a cardinality (SRC arithmetic), not a dimension (no structure map written).
- Status: **ABSENT-definition**.
- Non-predictions: no Kaluza–Klein tower, no compactification scale, no 11D supergravity identification, no 11-channel / 11-bin data design.

### DF-G03 — M²ET component: definition ABSENT; M_35 only a proposal
- Fields: statistics, observable association hygiene.
- Statement: "M²ET" has no written definition. The only mass-like object is M_35 in the §4 *proposal* (Kretschmann ↦ K₀(−1)^{ΔI_top}|det M_35|₃^{−539}); M_35 entries, K₀, I_top and the Mellin–Barnes map are undefined in v16.
- Derivation: ABSENT. DF cannot form any estimator or likelihood on M_35.
- Status: **ABSENT-definition** (proposal = NOT-MATH as a claim about curvature).
- Non-predictions: no mass spectrum, no 35-parameter fit, no identification of M²ET with M_35.

### DF-G04 — Residual packaging arithmetic (grounding) — SRC
- Fields: computation, filtration (bin/cell design).
- Statement: N_flux=4880, f_max=21, R=4859=9·539+8, B'=539=7²·11 per sector, remainder 8; β₁(X_×)=19396.
- Source: v16 Prop 42.6 / §41.7; paper §2. Derivation: integer arithmetic (recomputed).
- Status: **proved** (SRC; arithmetic).
- Non-predictions: 539 is a count; it is not a number of data bins, detector channels, or a physical constant; remainder 8 carries no assigned meaning.

### DF-G05 — D1 lock: static rank-1 classifier over ℚ — SRC
- Fields: statistics, filtration.
- Statement: H⁰(F)≅ℚ, H¹(F)=0, H²(F)≅ℚ·[s_αδ]; D1 = ℚ-linear projection to that line; acts on the nine charge sectors only; no time/schedule/metric argument; no data shared with resonant counters.
- Source: v16 Thm 41.10; Lock OW 96f8d42e…. Status: **proved** (SRC, Category A).
- DF consequence (NEW, proved from (ii)): any filter/statistic depending on a time index, cadence, metric normalisation, or real-valued amplitude is **not** a function of D1; D1's output is a single ℚ-valued coordinate (rank 1), so it supplies at most one degree of freedom and cannot be a multi-class or continuous detection statistic.
- Non-predictions: D1 is not a detector, not a trigger, not a GR observable.

### DF-G06 — S_eff / Canonical T3=539 as static budget, not stopping time — SRC
- Fields: computation, data-analysis design.
- Statement: T3=539 is a static cell/hash capacity; no global Ω≡0 (mod 539); dual-rail hardware-only; M: S_eff→Residual₅₃₉×Resonant₅₃₉ keeps factors disjoint.
- Source: v16 Prop 41.11; Lock OW. Status: **proved** (SRC).
- DF consequence (NEW, proved): no analysis may use 539 as an iteration cap, convergence criterion, segment length, or time window *as a model consequence*; any such use is an external design choice (Lock OW: "539 schedule external override").
- Non-predictions: no 539-sample periodicity, no mod-539 signature in data.

### DF-G07 — Residual ≠ Resonant (observable-association hygiene) — SRC + NEW
- Fields: observable-association hygiene, filtration.
- Statement: residual cardinality 539 and resonant schedule length 539 are equal values, not related by any structure map (v16 Prop 41.12). NEW (proved, logical): a data association justified via one factor cannot be transferred to the other; any filter that conflates the two (e.g., keying residual cells to T3 iteration counts) has no source support.
- Status: **proved**.
- Non-predictions: no residual–resonant cross-correlation predicted.

### DF-G08 — T3 map elementary facts — SRC + NEW check
- Fields: computation.
- Statement: T3(3k)=k, T3(3k+1)=4k+2, T3(3k+2)=2k+1 (v16 Prop 42.6 glossary); values on 0..8 recomputed. O_res={21+9j : 0≤j≤538} has 539 elements, all ≡3 (mod 9) (NEW, proved, trivial arithmetic).
- Status: **proved**.
- Non-predictions: no claim that T3 orbits model infall, horizons, or attractor basins (paper §4 reading = proposal, NOT-MATH).

### DF-G09 — Non-Archimedean core: Haar Euler-factor identity — SRC (cite Haar70)
- Fields: computation, statistics (measure normalisation).
- Statement: ∫_{ℤ₃⁴}|x|₃^{ν−1}dμ₃ = (1−3⁻⁴)/(1−3^{−(ν+3)}) for Re(ν+3)>0.
- Source: paper §5; Haar70 FINDINGS 7ab0ed68… (identity-only). Derivation: shell decomposition, geometric series (numerically re-checked at ν=0.7).
- Status: **proved** (SRC; standard Tate-type local integral). Not new.
- Non-predictions: no dissipation timescale, no Hawking spectrum, no BH entropy (paper §5 itself says none derived).

### DF-G10 — 3-adic g_rr regulation: finiteness is conditional and does not touch data
- Fields: data-analysis design, hygiene.
- Statement (NEW, conditional): IF one adopts the §4 proposal g_rr ↦ (1−2GM/(|r|₃+3^{−539}))^{−1} with r in ℚ₃ (or ℚ), THEN the denominator |r|₃+3^{−539} ≥ 3^{−539} > 0, so the bracket is defined except where |r|₃+3^{−539} = 2GM exactly; the attained values of |r|₃ form the discrete set {3^k}∪{0}.
- Gap: how a real-valued areal radius r is assigned a 3-adic absolute value, what units GM carries, and whether 1−2GM/(·)=0 can occur are **undefined**; so "finite at every point" is not established in general (the bracket's reciprocal diverges if equality holds).
- Status: **conditional** (on undefined embedding/units); the physical reading is **NOT-MATH**.
- Non-predictions: no modified horizon radius, no ringdown/echo/shadow prediction usable for filtration.

### DF-G11 — Kretschmann replacement via M_35: ABSENT-definition
- Fields: statistics.
- Statement: |det M_35|₃^{−539} is undefined without M_35 entries in ℚ₃; ΔI_top undefined; boundedness claim not derivable.
- Status: **ABSENT-definition**.
- Non-predictions: no curvature bound value, no sign-flip observable.

### DF-G12 — GR recovery / exterior match: ABSENT
- Fields: data-analysis design.
- Statement: No written map from the residual/3-adic layer to Einstein equations, an action, or matching conditions with an unmodified exterior. Status: **ABSENT-definition**. DF therefore has no model-derived GR deviation template.
- Non-predictions: no PPN parameter, no GW waveform deviation.

### DF-G13 — DF design rule from G01–G12 (NEW, proved as a logical consequence)
- Fields: filtration, observable-association hygiene.
- Statement: Under the examined sources, the set of observable-level quantities defined by S²-11DM²ET-X is empty; hence every candidate data association is at best Tier E exploratory and must be pre-registered as such, with the null as default.
- Derivation: G01–G03, G10–G12 leave no defined map from model objects to observables; G05–G07 forbid time/metric uses of D1/S_eff.
- Status: **proved** (relative to the examined inventory; becomes false only if a definition is written).
- Non-predictions: none of the 45/72 inventory candidates is thereby promoted.

### DF-G14 — Relation to pure-math catalog DF-C01…C17
- Statement: GR-extension grounding does not change any DF-C statement; DF-C entries on D1/S_eff/Haar/T3 coincide with G05–G09 and are cited, not duplicated.
- Status: **NOT-MATH** (bookkeeping).

### DF-G15 — Citation-pin version gap
- Statement: observed citation-pins sha 0009e735… ≠ PR2-listed 6f01d93b…; the PAPER main file (bridges/AUDITOR, e140947e…) not re-hashed by DF. Keeper should pin which version is canonical.
- Status: **ABSENT-definition** (of canonical version) — process gap.

## Optional Tier E note (separate; not a prediction)
Only existing actual Tier E: VIRGO null (6f9efa4b…, erratum e1ea66eb…): positive empirical associations = 0. No new association asserted or invented here.

## Counts
proved 7: G04, G05, G06, G07, G08, G09, G13 = 7 proved; conditional 1 (G10); conjectural 0; ABSENT-definition 6 (G01, G02, G03, G11, G12, G15); NOT-MATH 1 (G14). Total 15.

## Confirmations
No tip edit (tip_touched NO). No invent / no fabricated proofs / no physical mappings inferred from names, topology, or dimension. residual ≠ resonant kept. D1/S_eff locks kept. No CERT. No publish / spend / Gemini send.
