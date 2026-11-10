# NOTES: PATTERN_SIGNED_RR
## Reconstruction (written)
- w(v) = ½(sgn 5n − sgn(−n−21k)), from rev8 l.156–158 (c1 = (−1,1), c2 = (−4,1)).
- Points ν = α+v. Phase e(B(ν,β)), β ∈ {0,−a}, B(x,y) = xᵀ[[2,7],[7,7]]y (Q = ½B).
- I use the signed cone-weighted lattice content, i.e. the H_s-type indefinite theta per label. I do not use the full Siegel-lift integral kernel of §sec:lift (geodesic integral), which is not reconstructed here. This is a written but partial reconstruction of u_{α,β}.

## Lemma PS1
- **PS1a (Category A).** Any weighting of lattice points that is binned by 140·Q(ν) mod 8 (signed, complex, cone-weighted, or the full kernel too) is supported inside the unsigned support of PQ1, {0,2,3,4,7}. So fibres 1, 5 and 6 are always empty. **No refinement of the coefficient weighting can reach MF2 while the fibre is 140Q mod 8.**
- **PS1b (Category B).** With the signed cone weight, the L′-coset labels (fibres {0,2,4}) cancel to relative size ~10⁻¹¹. Only the a-coset survives, so the signed mass sits on {3,7}, exactly the complement of MF2's support.
  - The likely mechanism is w(−v) = −w(v) together with the label symmetry α ↔ −α on L′. This is not proved here.

## Observation (post hoc, not a claim)
The Resonant signed mass lives exactly on MF2's empty fibres {3,7}. This sharpens the PQ1 observation. A complement map is still not registered, because there is no written reason independent of ρ_res.

## Next pattern step
The obstruction is now in the **fibre coordinate** (140Q mod 8), not in the weights. The pattern-forced alternative is a different written fibre coordinate on the Resonant side. Two candidates:
- B(ν,a) mod 8-type: rev8 l.896 gives B(ν,a) = Re θ/10.
- The T-phase class Q(α)+B(α,w_c) from the written T-law (l.272–275), reduced to Z/8.
Either should be preregistered only if a written reason ties it to an 8-fibre structure. Otherwise ask Arvin for the intended Resonant fibre coordinate.
