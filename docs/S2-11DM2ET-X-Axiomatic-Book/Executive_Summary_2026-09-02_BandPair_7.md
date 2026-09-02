Executive Summary — U1-GS-NEWOBJ-BANDPAIR7
2026-09-02

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds. Category A residual discrete only.

Question. LayerFilt_7 already records residue-2 n-layers of g_7 as consecutive pairs (7k+3, 7k+4) and says BandPair_7 stays unnamed unless a Lucas identity is written. What residual-flux object is that pair, and does the identity force occupancy after 247?

Answer. BandPair_7(k) := (7k+3, 7k+4) with the Pack+(S) identity

n_R^2 - n_L^2 = 7(2k+1)

and the two-term evaluation

BP_k(d) := phi_{n_L}(m) + phi_{n_R}(m - (2k+1)),   m = (d - n_L^2)/7

on residue-2 degrees d = 7t+2. The right term is absent until the right layer is eligible. This is the consecutive-term pairing LayerFilt_7 required.

LayerFilt_7 recovery. On the exact window 121 <= d <= 282,

S(t) = BP_0(d) + BP_1(d).

Independently checked: window zeros remain 135, 191, 247; five post-247 exact-window values remain -3, 6, -2, 3, -5 at 254, 261, 268, 275, 282. BandPair_7 does not rewrite LayerFilt_7. It names the pair whose first two evaluations sum to S.

Decision. Finite-window identity only. Pair 2 starts at n=17, d=289, after the exact window ends at 282. Higher pairs can cancel the running sum. BandPair_7 does not occupy class 2 after 247 as a theorem.

What it is not. Not OccFilt_7 and not OccFilt_7(r ; infty). Not a LayerFilt_7 redo. Not Comp_7. Not Dom_res / XferPot / End_res / NecMono. Not Path 4 twin-pairs of C_third. Not Path 2 density. Not TPC. Not a majorant. Not a clock. 539 stays leftover COUNT. 247 stays LastMiss_7(2), not COUNT 539.

R2 stays R2_COMPUTATIONAL_NOT_PROVED. P-g7-inf stays open after 247. Twin Prime and RH unclaimed. Continuum Category B. CORE_FREEZE unchanged.
