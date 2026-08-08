# Open Routes — Closure Angle Analysis (2026-08-08)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure A · ZLA · no model constants  
**Mandate:** Analyze all angles for open routes for closure  
**Does not close:** any open gate unconditionally · RH · O-TL · B_θ

**Results:** `rh_open_routes_closure_analysis_results.json`  
**Priors:** explore-all final · pursue-open · ZEFB · MA8 · gap analysis

---

## 0. Executive findings

| Finding | Value |
|---------|------:|
| Open routes analyzed | **10** |
| Unconditional closure paths today | **0** |
| Conditional closure paths (honest hyps) | **9** |
| Highest leverage pair | **GO → κ** |
| B_θ strategy | **OR** (one input suffices) |
| O-TL strategy | **AND** (all four required) |
| RH | Superordinate; needs O-TL (B_θ not enough) |

---

## 1. Priority ranking (closure leverage)

| Rank | Route | Type | Viability | Effort | Feeds |
|-----:|-------|------|-----------|--------|-------|
| 1 | **kappa** | AND_input | hard | conditional_then_estimate | O_M1_2, O_TL |
| 1 | **GO** | AND_input | hard | joint_correlation_theorem | O_M1_3bis, kappa_full_path, O_TL |
| 2 | **Form_C** | OR_input | hard | research_breakthrough | B_theta |
| 2 | **B_theta** | goal | depends_on_OR | or_reduction | RH_related |
| 3 | **Iso_H** | OR_input | very_hard | research_breakthrough | B_theta, EO_for_Form_C |
| 4 | **DH** | OR_input | very_hard | research_breakthrough | Mass_with_A, B_theta |
| 5 | **SOC_strong_offline** | AND_input | hard | scale_and_transfer | O_PC, O_TL |
| 6 | **AFE_Moll** | AND_input | medium_hard | design_search | O_Moll, O_TL |
| 7 | **O_TL** | goal | depends_on_AND | multi_arm | RH |
| 8 | **RH** | goal | open_millennium | superordinate | — |

**Reading:** Ranks 1–2 are where effort can unlock the most downstream structure. Rank 8 is not a direct attack surface.

---

## 2. Closure criteria and angles (all open routes)

### kappa (priority 1)

| | |
|--|--|
| Type | AND_input |
| Closure criterion | far_signed <= J^{-p} * far_abs on full M1.3 paths for some p>1 (safer p~2), under executable c1 |
| Hard dependencies | GO for approach arcs (full-path) |
| Soft dependencies | MA8 dual identity (CLOSED) |
| Blockers | approach-to-zero poles of zeta'/zeta; absolute only p=0; RW p=1/2 insufficient |
| Allowed methods | Kappa_away + GO upgrade; zeta'/zeta bounds with distance-to-zero; named Kappa(p0) hypothesis |
| Forbidden methods | RW-only as theorem; c1/absolute cosmetics alone |
| Viability | hard |
| Effort class | conditional_then_estimate |
| Partials | Kappa_away, MA8 dual |
| Closes if done | kappa p>1 on full paths |
| Still does not close | RH, B_theta, O_TL alone |
| Notes | Best partial structure; GO is the missing upgrade key |

### GO (priority 1)

| | |
|--|--|
| Type | AND_input |
| Closure criterion | Infinitely many t_n with hybrid Omega scale AND gap >= theta * mean_gap |
| Hard dependencies | — |
| Soft dependencies | online hybrid Omega accepted for fixed X |
| Blockers | joint correlation Omega x gap missing |
| Allowed methods | resonance + gap statistics joint theorem; named GO(theta,X) hypothesis; conditional on pair correlation / GUE models (not RH) |
| Forbidden methods | mean gaps alone; Omega alone as GO |
| Viability | hard |
| Effort class | joint_correlation_theorem |
| Partials | GO(theta,X) named, structural link to kappa |
| Closes if done | GO theorem |
| Still does not close | RH, Form_C |
| Notes | Highest leverage: unlocks kappa approach arcs AND M1.3bis tubes |

### Form_C (priority 2)

| | |
|--|--|
| Type | OR_input |
| Closure criterion | limsup_X |sum_{n<=X} Lambda(n)/(n^{rho*} log n)| = infinity for a fixed off-line rho* (or equivalent residual Form B lower bound) |
| Hard dependencies | — |
| Soft dependencies | Iso_H for EO(epsilon_other) on amplitude path |
| Blockers | FFML; ZEFB |
| Allowed methods | zero-aware EF feedback (non-circular); conditional under Iso_H; new entangled-frequency technology |
| Forbidden methods | free-t resonance as proof; generic/almost-all gamma Diophantine; absolute triangle inequality as Form C |
| Viability | hard |
| Effort class | research_breakthrough |
| Partials | EO(Iso_H), zero-aware sketch |
| Closes if done | Form_C theorem |
| Still does not close | RH, O_TL |
| Notes | Shortest B_theta object; double-fenced |

### B_theta (priority 2)

| | |
|--|--|
| Type | goal |
| Closure criterion | Any one of Form_C | Iso_H+(RM) | DH+(RM) fully closed |
| Hard dependencies | at least one OR input |
| Soft dependencies | signed residual CLOSED |
| Blockers | all three OR inputs open |
| Allowed methods | close any OR input |
| Forbidden methods | claim B_theta => RH without O_TL |
| Viability | depends_on_OR |
| Effort class | or_reduction |
| Partials | three proved implications under hyp |
| Closes if done | one OR input |
| Still does not close | RH, O_TL |
| Notes | Not automatic RH |

### Iso_H (priority 3)

| | |
|--|--|
| Type | OR_input |
| Closure criterion | For rightmost beta*>1/2, only {rho*, bar rho*} lie on Re=beta* (up to EF truncation / multiplicity bookkeeping) |
| Hard dependencies | — |
| Soft dependencies | — |
| Blockers | no classical unbounded line-isolation technology |
| Allowed methods | genuinely new isolation tech; strong named hypothesis |
| Forbidden methods | density counts as isolation; finite-height only as unbounded Iso_H |
| Viability | very_hard |
| Effort class | research_breakthrough |
| Partials | (RM)+Iso_H => B_theta proved |
| Closes if done | Iso_H theorem |
| Still does not close | RH, O_TL, Form_C unconditionally |
| Notes | Also unlocks EO path for Form C |

### DH (priority 4)

| | |
|--|--|
| Type | OR_input |
| Closure criterion | N(beta*, T) = O((log T)^C) for some C and some usable beta* in (1/2,1) |
| Hard dependencies | — |
| Soft dependencies | — |
| Blockers | classical density exponents positive at moderate sigma |
| Allowed methods | new density exponent 0 at moderate sigma; named DH hypothesis |
| Forbidden methods | confusing near-sigma=1 log-power with moderate-sigma DH |
| Viability | very_hard |
| Effort class | research_breakthrough |
| Partials | (RM)+DH => Mass-with-A => B_theta proved |
| Closes if done | DH at moderate beta* |
| Still does not close | RH, O_TL, Iso_H |
| Notes | Classical ceiling well documented (Step B) |

### SOC_strong_offline (priority 5)

| | |
|--|--|
| Type | AND_input |
| Closure criterion | |Delta_X| >> log log X at relevant locations AND transfer to maximal abscissa / O-TL path |
| Hard dependencies | path package (M1.2/M1.3), possibly GO |
| Soft dependencies | typical Omega CLOSED |
| Blockers | scale jump sqrt(loglog)->loglog; offline transfer |
| Allowed methods | strong resonance for hybrid phase; FE path bookkeeping + path bounds |
| Forbidden methods | claiming typical = O-TL scale |
| Viability | hard |
| Effort class | scale_and_transfer |
| Partials | typical closed, FE path hygiene P4 |
| Closes if done | SOC strong + transfer |
| Still does not close | RH alone, B_theta |
| Notes | Depends on path package; later in AND order |

### AFE_Moll (priority 6)

| | |
|--|--|
| Type | AND_input |
| Closure criterion | Explicit dual-sum mollifier with proved boost of Im log P_X or A_X at O-TL locations |
| Hard dependencies | — |
| Soft dependencies | AFE surface, GHK hybrid |
| Blockers | no coefficients optimizing Euler phase; literature optimizes wrong functional |
| Allowed methods | AFE dual F+chi G design for Im log P_X |
| Forbidden methods | Levinson/Conrey zero-count mollifiers as O-Moll |
| Viability | medium_hard |
| Effort class | design_search |
| Partials | AFE-Moll skeleton, Euler-phase objective |
| Closes if done | working O-Moll construction + estimate |
| Still does not close | RH alone, B_theta |
| Notes | Most 'engineering' of the open gates; still empty |

### O_TL (priority 7)

| | |
|--|--|
| Type | goal |
| Closure criterion | All four AND arms discharged at programme scales |
| Hard dependencies | kappa, GO, SOC_strong_offline, AFE_Moll |
| Soft dependencies | typical Omega, R4.1, hybrid identity |
| Blockers | all four arms open |
| Allowed methods | close all AND arms |
| Forbidden methods | partial typical as O_TL |
| Viability | depends_on_AND |
| Effort class | multi_arm |
| Partials | architecture M1.2 accepted; typical Omega |
| Closes if done | full AND |
| Still does not close | RH automatically without target lemma close |
| Notes | Primary programme gate to RH |

### RH (priority 8)

| | |
|--|--|
| Type | goal |
| Closure criterion | All nontrivial zeros have Re=1/2 (or equivalent programme-complete debt close via O_TL) |
| Hard dependencies | O_TL as primary |
| Soft dependencies | B_theta related only |
| Blockers | O_TL open; no residual shortcut (ZLA) |
| Allowed methods | close O_TL stack; classical RH methods outside this ledger |
| Forbidden methods | residual A0-A5+; assuming GRH as proof |
| Viability | open_millennium |
| Effort class | superordinate |
| Partials | — |
| Closes if done | O_TL programme success or external RH proof |
| Still does not close | — |
| Notes | Superordinate; do not attack directly without arms |


---

## 3. Method-angle matrix

Which analytic angles help which open routes?

| Angle | Helps | Neutral/blocked on | Note |
|-------|-------|--------------------|------|
| MA8_zeta_prime_dual | kappa, GO | Form_C | Identity ready; estimates need GO for full kappa |
| Kappa_away_segments | kappa | — | Partial only until GO |
| zero_aware_Form_C_sketch | Form_C, B_theta | — | Needs Iso_H or new tech |
| Weil_smoothed_Form_C | Form_C | — | Surface only |
| VK_ZF_uppers | — | Form_C | Upper only — does not close lower-bound gates |
| AFE_Euler_phase_design | AFE_Moll | — | Design open |
| FE_path_bookkeeping | SOC_strong_offline | — | Hygiene only |
| free_t_resonance | SOC_strong_offline | Form_C | On-line only; FFML for Form C |
| generic_Diophantine | — | Form_C | ZEFB |
| classical_density | — | DH, Iso_H | Insufficient for polylog/isolation |
| named_conditionals | Form_C, kappa, GO, DH, Iso_H, SOC_strong_offline, B_theta, O_TL | — | Honest conditional closures possible; not unconditional RH |

**Closure-ready angles today:** none (all need estimates or new tech).  
**Identity-ready angles:** MA8 dual, residual formula, E1 (already closed).

---

## 4. Recommended closure order

### Track A — B_θ (OR)

```text
Pick ONE:
  Form_C  (zero-aware / under Iso_H)   ─┐
  Iso_H   (new isolation tech)         ├─► B_θ
  DH      (polylog moderate sigma)     ─┘
```

Parallel research lines; no AND between them.

### Track B — O-TL (AND) — sequential leverage

```text
1. GO          (joint Omega + gap)
2. kappa       (Kappa_away + GO → full path, p>1)
3. SOC strong  ──┐
   AFE_Moll    ──┴─ parallel design/estimate
4. O_TL assemble
5. RH (superordinate)
```

### Portfolio rule

| Do | Do not |
|----|--------|
| GO first on AND track | Absolute far cosmetics |
| Conditional theorems under named hyps | Free-t as Form C (FFML) |
| Keep ZLA firewall | Generic Diophantine as Form C (ZEFB) |
| Treat B_θ and O_TL as separate portfolios | Claim B_θ ⇒ RH |

---

## 5. Dependency diagram for closure

```text
                    ┌── Form_C ◄── (Iso_H soft for EO)
                    │
         B_θ ◄─ OR ─┼── Iso_H
                    │
                    └── DH

         O_TL ◄─ AND ─┬── kappa ◄── GO (hard dep for full path)
                      ├── GO
                      ├── SOC_strong_offline ◄── path (kappa/GO partial)
                      └── AFE_Moll

         RH ◄── O_TL (primary)
              B_θ related only
```

**Critical path (O_TL):** GO → κ → (SOC ∥ AFE-Moll) → O_TL → RH  
**Critical path (B_θ):** any single OR input  

---

## 6. Conditional vs unconditional closure

| Route | Unconditional path today? | Honest conditional closure? |
|-------|:-------------------------:|:---------------------------:|
| Form_C | No | Yes (e.g. under Iso_H / named FC) |
| Iso_H | No | Yes (named hyp only) |
| DH | No | Yes (named DH) |
| kappa | No | Yes (Kappa(p0); or GO+Kappa_away) |
| GO | No | Yes (GO(θ,X)) |
| SOC strong | No | Yes (SOC(X)+transfer) |
| AFE_Moll | No | Yes if construction found under design hyp |
| B_θ | No | Yes if any OR hyp holds |
| O_TL | No | Yes if full AND hyps hold |
| RH | No | Not by assuming RH |

Named conditionals **close programme gates under hypothesis** without being Millennium solutions.

---

## 7. Negative results (angles that do not open closure)

| Angle | Why it fails to close |
|-------|----------------------|
| VK / classical ZF | Uppers only |
| Free-t resonance | FFML on Form C; on-line SOC only |
| Generic Diophantine | ZEFB |
| Density theorems | Not Iso_H; not moderate-σ DH |
| Levinson mollifiers | Wrong functional for O-Moll |
| RW κ | Below p>1 bar |
| Residual algebra | ZLA |
| Re-deriving closed identities | No new tip |

---

## 8. One-liner

> Every open route has a sharp closure criterion and a method budget; **none** has an unconditional closure path today; maximum leverage is **GO then κ** on the AND track and **any one** of Form_C / Iso_H / DH on the OR track.

**Status code:** `RH_OPEN_ROUTES_CLOSURE_ANALYSIS_2026-08-08`

*Per aspera ad astra.*
