# order40 PREREG: RG37, (0,1)-edge decomposition (written and hashed before numerics)
## e2 identity (derived from the corner formula; fixed now)
For the cone ((1,n),(0,1)), with u2 = e2 = (0,1) and Q(e2) = 7/2: the coordinates of ν are a = ν1 and b = ν2 − nν1, and B = (1,n)ᵀA(0,1) = 7 + 7n.
The e2-ray B2 term is T_e2 = Σf·(B/(4Q(e2)))·B2(a) = ((1+n)/2)·Σf·B2(ρ1/N) = ((1+n)/2)·C2a, using the order20 C2a (order19 arrays C[1]).
Identity I-e2: T_e2((1,n),(0,1)) = ((1+n)/2)·C2a, for n = 1..6. For n = 0 this reduces to order34's I-a, T_other(K) = ½C2a.
Data: the stored pieces from order34/data/o34_control_pieces.npz (pieces order [Bu/(4Q1)B2(b), Bu/(4Q2)B2(a), B̄1B̄1], so T_e2 = piece 1) and order19 C2a.
I-e2 PASS if max error ≤ 1e−10 (x and −1/x); FAIL if ≥ 1e−6. The identity holds by definition; if it passes, it is Category A in the trivial sense (bookkeeping).
## Role of Q(e2) = 7/2
Q(e2) enters only the scalar coefficient (1+n)/2. The law metric r is scale-invariant, so Q(e2) does NOT set r. The predictor of the weaker near-law is the law miss of C2a itself, r(C2a). This is stated in place of the requested "Q(e2) as predictor".
## RG37a: which piece carries the near-law on (0,1)-edge cones (consistency)
T_e2 has r = r(C2a) to 1e−12 for all n, and meets the criterion (w* = −1, |κ̂−1| ≤ 0.01, r ≤ 0.10). PASS if both hold on 6/6.
## RG37b: the r ≈ 0.022 claim (Category B; not blind: order34 observed 0.0217–0.0232)
The B2 part T_2a + T_2b on e2-cones has r within [½, 2]·r(C2a) on 6/6 cones, and T_BB fails the criterion on 6/6. PASS iff both; FAIL if either fails on ≥ 2 cones.
## Controls
(1,0)-edge cones: r(T_e1) = r(C2b) (order34). Interior cones (order34 non-edge controls): neither B2 piece is a scalar multiple of C2a or C2b.
Rule: the best-scale relative residual against both C2a and C2b is ≥ 1e−3 for every interior piece. Report the count violating.
Category: A only for I-e2 (by definition); B for RG37b. v11 only for a non-trivial proved statement.
Naming: RG* only, no labels L1–L7; "36" only as dim V. Geometric only; MAPS_CANDIDATES and REVIEW untouched; no Resonant objects; no new Bernoulli objects; no bridge claim; E1–E3 OPEN; Ξ not identified.
