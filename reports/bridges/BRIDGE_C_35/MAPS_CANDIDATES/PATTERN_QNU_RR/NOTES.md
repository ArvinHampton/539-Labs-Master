# NOTES: PATTERN_QNU_RR
## Explore
- N = 140 is the least integral scale and matches the written e(Nz/140) of rev8 l.896.
- 140Q mod 8 has period 8 in n (checked against 16).
- Per-label supports: 35 labels give {0,2,4} and 35 give {3,7}.
- Pools:
  - all 140: (1/8,0,1/4,1/4,1/8,0,0,1/4) (COMMITTED);
  - the 28 labels with 70α1 ∈ {7,21,49,63}: (0,0,0,1/2,0,0,0,1/2).

## Lemma PQ1 (Category A; exact enumeration over a full period, logs/test.log)
On the coset α ∈ L′ (the 35 α with no a-shift), 140·Q(α+n) mod 8 ∈ {0,2,4}. On α ∈ a+L′, 140·Q(α+n) ≡ 3 mod 4, i.e. it lies in {3,7} (140·Q(a) = −49 ≡ 7).
Hence for **any** non-negative weighting of the 140 labels (or of β), with scale 140, fibres 1, 5 and 6 get zero mass. ρ_res has 5/8 of its mass there, so no label pool of the binary exponent can equal MF2.

## Observation (post hoc, NOT a claim, not preregistered)
The a-coset fills exactly {3,7}, the two fibres that MF2 leaves empty, and the L′ coset sits in {0,2,4}. The two {0,2,4,…}/{3,7} splits look complementary. Testing any transform built from this (e.g. a complement or shift of fibres) would be chosen after seeing ρ_res, so it is fitting. It can only be preregistered if a written reason for that transform exists.

## Next pattern step (not run)
Unsigned pools are exhausted (PF1, PQ1). The remaining written structure in the same lift is the phase e(B(ν,β)), β ∈ {0,−a}, together with the signed cone weight w(v). This is the signed mass per fibre: Σ w(v)·e(B(ν,β)) binned by 140Q mod 8. That is the actual coefficient content of u_{α,β}, not lattice-point counting.
A next package would preregister |signed fibre mass|, normalized, over the 140 labels vs ρ_res. Its density convention (cone-weighted boxes, written w) must be fixed in PREREG.
