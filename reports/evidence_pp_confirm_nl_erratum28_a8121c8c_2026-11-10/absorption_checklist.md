# Absorption checklist: NL Erratum 28 (a8121c8c) vs PP 087acf47 + 3844d94d (gap) and f25a6d55 + d3e7306e (junction)
Each row: required wording (12:21 leftover, as updated by 12:24 addendum) -> erratum location -> verdict.

## Gap debc7d52
| fix | required | erratum | verdict |
|---|---|---|---|
| F-1 | H2: P1 = pointwise identity (PP-verified PG2), not "1142 P1"; W real-analytic, non-constant, W_min > 0; eps, q in N-1 units | s2 L40; s15 L100 | ABSORBED |
| F-2 (addendum) | A12-a PROVED sufficiency/kinematics only; "Delta >= 0 necessary (1142 A10)" = citation of scoped A10 ([u>=1], GA2/P-b), outside A12-a PROVED content; no silent upgrade | s3 L43; s15 L102 | ABSORBED (not absorbed into A12-a; no upgrade) |
| F-3 (addendum) | A6-n: N- <= Delta_N/2 names Bogomolny floor e_u >= abs(n), u >= 1; 1142 A1 PROVED as that implication with bookkeeping premises | s4 L46; s15 L103 | ABSORBED |
| F-4 | A9-T label carries 2808.6, 19520/3, Q=9760 (unadopted) and U-uniform compactness; optional n*=173 at u=2 | s5 L49; s15 L104 | ABSORBED (optional recorded, "not sharp") |
| F-5 (addendum) | A8-R cites 1142 GB3 with ruled scope (constant unbackreacted face, fibre-only legs/dependence, source-free); twisted blocks under Y14 S2-2 CONDITIONAL (077e417d) | s6 L52; s15 L105 | ABSORBED |
| tally | 7/6/4/0 = 17; no moves; H6 implication for stage-2 ansatz only; A9-T COND; D-B3 unclosed | s1 L31; s15 L107 | CONFIRMED (row lists match PP 087acf47 s5) |

## Junction dff93e21
| fix | required | erratum | verdict |
|---|---|---|---|
| F-1 | S4-2 CONDITIONAL; P-b, GA2, D-C, fixed unbackreacted face, stated wall delta(0)/curvature prescription; upgrade needs boundary-term derivation + coefficient; not refuted | s1 L33; s7 L55; s15 L110 | ABSORBED |
| F-2 (addendum, load-bearing) | A15-2 CONDITIONAL on scoped 1142 A1-A3 holding on backreacted face, NOT "pending 1142 audit"; keep "does not transfer" (A9-T, kappa); A5 only n=0; no auto-upgrade; 1142 A15 OPEN | s1 L34; s8 L58; s15 L111 | ABSORBED (follows addendum, explicitly rejects pre-addendum wording) |
| F-3 | GA9-1/2 labels name block-averaged source model; O(N) and ~3253/~4190 CONDITIONAL | s9 L61; s15 L112 | ABSORBED |
| F-4 | premise J1 vs test ID J1 disambiguated; JX0-JX9 reading map; frozen script unedited | s10 L64-79 | ABSORBED (script sha b054521b unchanged, 444) |
| F-5 | A15-1/s1: Z2 Israel convention (2/kappa^2), K_tj=0, Poincare; optional PJ8 | s11 L82; s15 L113 | ABSORBED (PJ8 recorded, no grade change) |
| F-6 (addendum) | GA9 cites 1120 D-D (given J1); 1142 A13 REFUTED only under stated hypotheses; no D-B3/junction closure; not auto to backreacted face | s12 L85; s15 L115 | ABSORBED |
| F-7 | S4-1: P-b or double cover drops wall term; degree 4 by hand | s13 L88; s15 L114 | ABSORBED |
| tally | 5/7/3/0 = 15; two already-ruled moves accepted, none new; GA9, S4-4, A15 OPEN | s1 L32; s15 L117; s16 L123 | CONFIRMED (row lists match PP f25a6d55 s5) |

## Erratum own tally
0/0/0/0 (header L27 = body s17 L132-139). Every s15 relabel keeps its ruled class; the only class changes are the two moves PP already ruled. CONFIRMED.

## Watch list
- 2808.6 / 19520/3 / 9760 adopted? No (L25, L46, L49).
- GB3 applied to twisted blocks? No (L52).
- A15-2 auto-upgraded? No (L34, L58).
- D-B3 or junction closed? No (L25, L36, L143).
- Metric invented? No.
- Frozen script edited? No (hashes = sidecars).
- E27 used as proved input? No (L19, L124, L127: "pending confirm"; not grade-changing).
- 12:09 BPS audits mixed in? No (L37, L126).
