# PP confirm E29 (5e12e444) — absorption checklist
Audit FX 9bfa9657 (617bc443) / NEC e7d3a64f (6ccc9ef4) leftover fix → E29 location → status.

| Fix | Required content (audit §7) | E29 | Status |
|---|---|---|---|
| FX F-1 | withdraw "A7(i)–(iv) and A10 all have cohomogeneity ≥ 4"; E4-6 main case (H_Σ×SO(3)_R×U(1)_R, singular on all C₄) in A10/A7(iii), cohomogeneity 2, (r,χ) needed; ≥4 (≥6 w/o H_Σ) on A7(i),(ii) only; coh-3 singular branches; A7(iv) unbounded; widen A13; drop "(B) fails by construction" there; restatement, not REFUTED row; A12 PROVED as restated | §2, §11, §13 l.113 | ABSORBED |
| FX F-2 | c₂(W^±) = (c₁² ∓ 2χ − 3σ)/4 in A2 and A11 prose; ±2 unaffected; W^− line of A11 wrong as written; A11 CONDITIONAL | §3, §11 | ABSORBED |
| FX F-3 | general (a,b): s₃ ↦ −s₃ bijection; coincidence only a=±b, value 0; |a|=|b|, q≠0: extremal Γ^J line, J homotopic to vacuum under (lin) | §4, §11 | ABSORBED |
| FX F-4 | A1 2q/w=±1 forced by ε(p)≠0; A8 Z closed and tame; T1 both lock orientations; line 48 dead code, frozen; header nit not edited | §5 | ABSORBED |
| E1-1 note | single-section gloss; two poles + A5 premises ⇒ contradiction; no regrade; E1-3 COND | §6 | ABSORBED |
| Drops A3–A6 | audit §4 wording, common premises, per-item regularity | §1 | MATCH (A5 branch description abbreviated — nit R1) |
| NEC F-1 | (A−) A′=−√(…)≤0 as premise of B2 "(<0)"/Σ clause, B3, Z-N6; B3: −V ≤ (9/2)A′² − 30λ′² − (3/2)w′²; |V| form only where V≤0; counterexample (−1,−1,0,0), V=18; (A−) necessary via (1,0); V(MN2)=−3·2^{2/3} | §7, §11 | ABSORBED |
| NEC F-2 | title/B3 scope → (φ,λ,w) truncation, frozen 21bcbc3f face data, (Y15), (HC), (A−); not arbitrary 3-scalar; (h0),(ii) unused | §1, §8, §11 | ABSORBED |
| NEC F-3 | MN2 corollary as implication: velocities→0, continuity, (A−); not adoption | §9, l.24 | ABSORBED |
| NEC F-4 | Z-N5 arithmetic; identity −V − [...] = −30(φ′−A′/2)(φ′+A′/2) (PP D4); header nit | §10 | ABSORBED |

Spot re-checks (sympy, exact): D4 identity expands to 0 on HC 12A′² = 30φ′²+30λ′²+(3/2)w′² − V; V(−1,−1,0,0) = 18; at zero velocities A′(MN2) = −2^{−2/3}.
Tallies: erratum 0/0/0/0; FX 8/2/3/0 = 13 (A12 restated); NEC 3/0/2/0 = 5 (B3 restated). No label-class moves. A7, A10, A13 OPEN; A9, A11 CONDITIONAL; B4, B5 OPEN. E5-4, E2-4, E3, BPS S5 not reopened.
