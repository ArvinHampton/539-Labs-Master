# order60 PREREG (LOCAL Bridge C only; RG* labels; CORE_FREEZE; new files only in order60/)
Date 2026-10-24 (America/Chicago). Physicist CLEARED. No P̂_orth, Ξ adoption, k≠0, Map-C6. No Eichler/QM-cocycle completion claimed.
Inputs (read-only): order3/data/parts.npz (A1,S_A1); order56/data/rg46_raw.npy (Xi_compl, strip, A1(P_orth)) and rg46.json; order58/data/rg47a_raw.npy (axis_Q1, axis_Q7/2, corner) at x and −1/x, 216 XS × 105 companions.

## RG47b — ray→sawtooth statistic. LABEL: asymptotic ≠ QM-cocycle.
Written ingredients only: G3 A1^ray = √π/(2√Q(u))·mean(f), Q∈{1,7/2} (v12 Thm 35.6 via order57 WRITTEN_CANDIDATES:29,39); order58 axis pieces −(√π/2)·Σ f·B̄1/N/√Q (lib2 formula); order6 shadows Σ n e(n²τ), Σ n e(7n²τ/2) ("argument sketch").
- RG47b-i (Cat A, symbolic): prefactor consistency. The Q-dependence of A1^ray and of the order58 axis piece is the same √π/(2√Q). PASS iff ratio of written prefactors (√π/(2√Q))/((√π/2)/√Q) = 1 exactly for Q=1 and Q=7/2.
- RG47b-ii (numeric match ray→sawtooth vs order56 A1(P_orth)): runs ONLY if a written map mean(f) → Σ f·B̄1/N (or ray → sawtooth B̄) exists. ORDER60_PREP search found none (order58 RESULTS:41 "needs a written ray-to-sawtooth map"). Decision fixed now: SKIP (obstruction). No diagnostic number is given a verdict.
- RG47b-iii (shadow evaluation at rational x): needs Eichler normalisation, constants and evaluation points for the order6 shadows. Absent (order58 RESULTS:23; book Eichler kernel Continue_Resolution…:42-44 is for Ξ, which is REJECTED G1). Decision fixed now: SKIP (obstruction).
- RG47b overall: PASS iff i PASS and ii, iii run and pass; SKIP if ii or iii skip with i PASS; FAIL if i fails.

## RG47c — axis-Q1 rank test (Cat A-numeric)
Â1 = A1 − Xi_compl + strip (exactly order56 RG46b H, HS). R_Q1 = Â1 − axis_Q1 (x and −1/x rows from order58 raw, k=0/1). Control R_Q7 = Â1 − axis_Q7/2. Also report Â1 − both axes (descriptive).
Rank = #σ/σ0 > 1e−9 (SVD). Closed at w iff rank[R(x) | diag(|x|^w) R(−1/x)] = rank R(x), w∈{½,1}. Gate: reproduce order56 Â1 rank 75, joints 148 (½) / 150 (1); fail gate ⇒ run invalid.
Excess e(w) = joint − rank. Baseline e = 73 (½), 75 (1).
- PASS (Q1 carries the obstruction) iff R_Q1 closed at some w.
- PARTIAL iff not closed but max_w over (baseline e − e_Q1) ≥ 10 AND reduction for Q1 > reduction for control Q7/2.
- FAIL otherwise. Control reported regardless.

## Route A pivot (documentation only, in RESULTS).
