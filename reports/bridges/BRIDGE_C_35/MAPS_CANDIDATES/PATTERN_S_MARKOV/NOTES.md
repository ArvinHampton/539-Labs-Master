# NOTES: PATTERN_S_MARKOV
## S matrix used
- Taken directly from the written S-law (rev8 l.274): each label goes to 35 targets with |coef|² = 1/35.
- The A35 / 105-companion S was not needed: the written label S-law is already a 140×140 mixer.
- I verified 2a ∈ L′, so the β-index mod L′ is consistent.

## Lemma PSM1 (Category A)
(a) The |S|² chain is doubly stochastic. It is reducible into exactly 3 closed classes indexed by (coset α, coset β): (0,0) and (1,1) (35 labels each), and (0,1)↔(1,0) (70 labels, period 2). The stationary space has dimension 3, and each class's law is uniform.
(b) Under the T-phase fibre, every stationary law (any convex mix of the 3 class laws) has zero mass on fibres 2 and 6. MF2 has 3/32 + 5/32 there. So **no** stationary law of the S-chain matches MF2.
(c) The S-orbit average equals the uniform pool, so the S-dynamics adds nothing beyond PB2 on this fibre.

## Observation (post hoc, not a claim)
- The (1,1) class (a-cosets) supports {1,3,5,7}, the odd fibres. The (0,0) class supports {0,4}.
- MF2 is not a mix of these, because it needs {2,6}.
- Under MF1, MF2's open fibres split as {1,5} odd-open and {0,2,4,6} even-open, with {3,7} closed. The Resonant T-fibre has an exactly opposite parity block structure.

## Next pattern step
The written S/T action is now exhausted as label dynamics (PSM1). The Markov analogue that MF2 actually is, a chain on residues u mod 2^k, would need a written Resonant chain on Z/2^k or Z/8, such as the T-phase action of T on labels composed with S (the ST order-3 element).
The cheapest written next test is the **ST chain**: the transition |(ST)_{ij}|² from the written T-law and S-law, whose stationary laws on the 3 classes may mix differently because T permutes β (β → α+β+w_c).
If that also fails, the written modular side has no 8-fibre law matching MF2. The honest stopping point is then to report this to Arvin and ask for his intended Π/grading.
