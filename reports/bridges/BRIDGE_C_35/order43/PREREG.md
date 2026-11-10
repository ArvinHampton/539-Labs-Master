# order43 PREREG: exact law for the k = 0 part and the exact miss split (written and hashed before numerics)
Sources: the G S-law (paper Theorem STlaw; checked in order17 C0): G(−1/x) = (|x|√35)^{−1}·M·G(x) for x > 0. Order42 E0: the k = 0 term of L_B (i) is D0 = diag(b)·G, with b_l = B2(α2_l) (rational, nonzero for rational α2).
## LD0 (Category A; proof fixed now)
D0(−1/x) = diag(b)·G(−1/x) = (x√35)^{−1}·diag(b)·M·G(x) = (x√35)^{−1}·M_b·D0(x), with M_b := diag(b)·M·diag(b)^{−1}.
This is a weight-one law (factor 1/x) with the B2-twisted matrix M_b.
Test: max|D0(−1/x) − (x√35)^{−1}M_b D0(x)| ≤ 1e−12 (absolute; D0 entries are O(1)) at the test points. Also report min|b_l| > 0.
## RG40: exact miss split (prediction from LD0, no fit)
With κ̂, M fixed (order37) and Rem := C2b − D0, the measured residual is R(x) = C2b(−1/x) − κ̂x35^{−1/2}M·C2b(x).
Prediction: R_pred(x) = [(x√35)^{−1}M_b − κ̂x35^{−1/2}M]·D0(x) + [Rem(−1/x) − κ̂x35^{−1/2}M·Rem(x)]. The first bracket uses LD0 instead of D0(−1/x).
PASS iff max over points of ‖R − R_pred‖/‖R‖ ≤ 1e−10. FAIL iff ≥ 1e−6.
Note (disclosed): given LD0, RG40 is an algebraic identity, so it is a consolidation, not new evidence. The informative output is the split of the miss into
(a) the law mismatch of the k = 0 part, [(x√35)^{−1}M_b − κ̂x35^{−1/2}M]D0(x): a weight 1/x vs x mismatch and an M_b vs M mismatch, both explicit;
(b) the k ≠ 0 remainder.
Both norms are reported, along with their cancellation ratio ‖R‖/(‖a‖+‖b‖).
Test points: x ∈ {1, 2, 3, 4, 5, 6, 7, 8, 1/2, 1/3, 2/3, 3/2}, all 105 companions.
## Order41 monotone (note only)
No test. Explaining it would need a model of ‖(a)+(b)‖ in num and den, which I cannot write without new fits.
## v11 criterion (fixed now)
LD0 is an immediate corollary of Theorem STlaw times constants, so a PASS alone does not warrant v11. v11 would need a non-trivial statement about the remainder, which is not attempted here.
## Follow-up (order44) rule
If LD0 and RG40 pass, the only immediate follow-up would be a law for Rem. No such law can be written from existing objects without fitting, so order44 is NOT run, as decided here in advance.
Naming: RG* only, no labels L1–L7; "36" only as dim V. MAPS_CANDIDATES untouched; no Resonant objects; no new Bernoulli objects; no bridge claim.
