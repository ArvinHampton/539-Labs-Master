# PP-FINDINGS — Cat A foolproof RE-RUN under Owner definitions OW 9aec847a (2026-11-03)
REPORTS ONLY · No CERT · tip READ ONLY · messaged nobody.
Inputs verified (sha256): OW reports/OWNER_WRITE_CAT_A_DEFINITIONS_C_V35_PI_FAST_RG_HQCC_2026-11-03.md 9aec847a7ccb8a815255c1d3c645367fbf12205a079085ddf40f7975cf8e095f (prefix MATCH). INTAKE reports/539labs/INTAKE_539LABS_TECHNICAL_CORPUS_2026-11-03.md 074f703283420dc9757c7dc0ca3efaaa1957f4f5f37022d60292c8f80b96870b (MATCH, sidecar agrees). Tip 7cddb188…dfc91 (start and end MATCH).
Script: scripts/rerun_ow9aec847a_2026-11-03.py (+ .out).

## Table (old → new)
| # | Claim | Old status | New status | What changed |
|---|---|---|---|---|
| 1 | det≠0 ≠> no cancellation (M=3) | PROVED/AGREE | PROVED/AGREE (unchanged) | M odd ≥3 includes M=3. |
| 2 | C∉V_35; polar bounds w/o cocycle vanishing | ABSENT/NF-WHY | NF-WHY (defs now PRESENT but non-operational) | C is a "distribution" with no formula ⇒ not computable; V_35 has no weight/level/degree/rank ⇒ no basis, no dimension. "Siegel forms over Q(√35)" is a category slip: forms attached to a real quadratic field are Hilbert modular forms (or Siegel restricted via a Hilbert–Siegel embedding, unstated). C (distribution) and V_35 (space of forms) live in different ambients, so "C∉V_35" needs a stated embedding. Polar = Mellin–Barnes residue matching, but no matrix system written; "independent of H² cocycle vanishing" is asserted by definition, not proved; tip P5b still `[[to prove]]`. |
| 2b | Hecke deformation / T3 map | ABSENT | ABSENT (unchanged) | OW §9 says Hecke audit "pending"; see Hecke table below. |
| 3 | Π_fast idempotent, spec{0,1} | lemma PROVED; operator invented-pending | **FALSE** (operator now defined) | With Ad_X=[X,·], (Id−avg)∘ad_{X_t} = ad_{X_t−X̄}; model X_t=(ζ^t−1)D, D=diag(±1) (∧ = parity ±1): X̄=−D ⇒ Π_t=ζ^t ad_D, spec ζ^t·{0,±2}, Π²≠Π (M=3,5,7 numeric). General proof: any ad_Y on a finite-dim Lie algebra with tr ad=0 (gl_n, any perfect/exceptional algebra) has Tr=0; idempotent with Tr=0 ⇒ rank 0 ⇒ Π=0. So Π_fast idempotent ⇔ Π_fast≡0. ad_X nilpotent for X nilpotent (A³=0 checked), never a nonzero projector. |
| 4 | Wilson C1 (1+κ)^{−7/20} | FALSE under const R_x; corrected form under A1 | **invent-pending (gap exact)** | R_x runs ⇒ C1(μ)=C1(μ0)exp(−(7/20)∫κ dlnμ). Snapshot at fixed point κ→κ* gives (μ/μ0)^{−(7/20)κ*}, still μ-dependent; (1+κ*)^{−7/20} requires ∫_{μ0}^{μ}κ dlnμ = ln(1+κ*) — no β-function for R_x/κ written. "KK tower / LCFT" gives no reference, no anomalous-dimension computation yielding 7/20. Gap: (i) β_κ, (ii) derivation of γ=7/20 from KK/LCFT spectrum. |
| 5 | Audit Local 733db7de F1–F6 | F1 FLAG, F4 FLAG, INTAKE FLAG, rest CONFIRM | F1 FLAG (stands, see row 11); INTAKE FLAG **RESOLVED** (Owner confirms 074f7032, d75a0a3a deprecated); others unchanged | OW §4, §9. |
| 5b | Audit Local F4–F6 0a1c4add | F4 CONFIRM, F5 FLAG, F6 CONFIRM | F4 CONFIRM (now with defined Ad: FALSE, row 3); **F5 CONSISTENT** (ABSENT-as-stopping-time; as hash budget 18+521=539=7²·11 CONSISTENT); F6 CONFIRM (V_35 still not a tip object; tip V₄₂) | OW §8 picks the hash-budget reading. |
| 6 | Codex Π_fast Cesàro, Tr=128 | idempotent under H; 128 ABSENT | **FALSE for OW Π_fast** (Tr=0); Codex Cesàro version still conditional-PROVED but superseded/inconsistent | OW chose Ad=[X,·] form. "Width 128" qutrits ⇒ state dim 3^128 (or Lie block dim unstated), not 128; Tr=128 would need rank 128 projector — impossible for traceless Π. |
| 7 | HQCC Φ convergence | convergence FALSE, orbits →∞ | **CONSISTENT** (confirmed) | OW §5: orbits unbounded, no convergence = our prior finding (codex_items_6_10 script). Theorem still ABSENT as stated ("densities trace non-compact paths" undefined). |
| 8 | Ω≡0 mod 539 criterion | FALSE as criterion | **WITHDRAWN** | OW §6. Residual: |W|≤N≤∏‖h_i‖₁ = Lemma 5 B (PROVED for integer W); W now "non-integer phase rotation" — bound needs W redefined consistently (FLAG). |
| 9 | det≢0 mod3 ⇒ no cancellation | inverse PROVED; no-cancel FALSE | unchanged | — |
| 10 | BQP⊂C_HQH⊂NP-Complete | FALSE; ⊆NP open | **OPEN / conditional** | BQP⊆C_HQH⊆NP ⇒ BQP⊆NP, open (Raz–Tal 2018 oracle separation BQP⊄PH^O). Unprovable without resolving that. Well-posed conditional: "If C_HQH ⊆ NP (certificate = Thm A) and BQP ⊆ C_HQH, then BQP ⊆ NP"; provable part: C_HQH-decision ∈ NP (Thm A). |
| 11 | M any odd ≥3 vs Lemma 5 E | — | **CONSISTENT with restriction** | Hardness holds for problem with M as input (slice M=2^k+1>Σ is a sub-family, so NP-hardness transfers). For fixed small odd M≤Σ the reduction FAILS (wraparound: M=3,w={1,2} target 0 false positive). Bonus: for odd M, 1+ω^{kw}≠0 always ⇒ det≠0 automatic on unit {0,1} instances (script, M<40). FLAG: "M^{-1} mod M preserved" is meaningless (M≡0 mod M); likely means 2^{-1} mod M or det invertible mod M. |

## Hecke audit open items vs OW
| Item | Addressed by OW? | New status |
|---|---|---|
| Field choice Q(√35) (disc 140, χ₁₄₀ vs χ₃₅) | No; OW adds "Siegel forms over Q(√35)" (Hilbert vs Siegel mismatch) | FALSE rows #5–8 unchanged; new FLAG |
| T_p space (weight/level/char) | No (V_35 lacks weight/level) | ABSENT |
| Θ_p | No | ABSENT |
| Λ / Λ₀≈1.81 | Partially: "Polar" = Mellin–Barnes residues, no threshold | ABSENT |
| C₃=538.1 | No | FALSE (≤2.5) unchanged |
| P5b link (#13) | Asserted "independent of cocycle vanishing", no proof | ABSENT |

## Remaining Owner clarifications
1. Embedding of C into the ambient of V_35; weight, level, degree, rank of V_35; Hilbert vs Siegel.
2. Π_fast: since traceless ⇒ only 0 is idempotent, state intended operator (e.g. projector onto ker ad / invariants) and its space; reconcile "width 128" with dim.
3. β-function for κ/R_x and derivation (with reference) of 7/20.
4. Fix "M^{-1} mod M" wording; state M is input (hardness) vs fixed.
5. Redefine W (non-integer) and restate |W|≤N bound.
6. Hecke: all items above.
