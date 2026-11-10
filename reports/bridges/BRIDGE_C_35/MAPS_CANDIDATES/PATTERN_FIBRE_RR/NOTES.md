# NOTES: PATTERN_FIBRE_RR
## Explore (data/explore.json)
- Written label family reproduced: 70 α's × 2 β's = 140 labels. The α1 values are {0, 1/10, 1/5, 3/10, 2/5, 1/2, 3/5, 7/10, 4/5, 9/10}.
- Cross-checks against the text: (7/10,4/5) and (1/2,j/7) are present, and exactly 28 β=−a labels have 70α1 ∈ {7,21,49,63} (rev8 l.786–787: "gives 28 labels").
- Minimal integral scale N = 40 (the denominators of α1 divide 10). The ×68 convention is not integral here, so it is not used.
- Per α1 (N=40):
  - α1 ∈ (1/5)Z gives (1/2,0,0,0,1/2,0,0,0).
  - α1 ∈ 1/10 + (1/5)Z gives mass 1 on fibre 1.
- Pools:
  - all 140 labels: (1/4,1/2,0,0,1/4,0,0,0) (COMMITTED);
  - 28 labels with 70α1 ∈ {7,21,49,63}, β=−a: (0,1,0,0,0,0,0,0).
- The paper's condition 2α1 ∈ Z holds only for α1 ∈ {0,1/2}; that subset gives fibres {0,4} and {1}.

## Lemma PF1 (Category A): pooled square-class obstruction
Name: PF, not L, since L1–L7 are Einstein–Hampton only. Fibre lemmas elsewhere are MF1–MF3.
For any label pool, any weights and any common integral scale N, the exponent is N·5u²/2 = (N/40)·x² with x = 10u ∈ Z. So every fibre lies in c·{0,1,4} mod 8 (at most 3 classes).
ρ_res has 6 classes. So no pooling of the single unary theta 5u²/2 over the written label family can give MF2. This holds for the unshifted theta (BATCH8) and for every label shift.

## Next pattern step (not run)
The obstruction is in the unary exponent itself. The written object that escapes it is the **binary** form of the same family: Q(ν) = ν1² + 7ν1ν2 + (7/2)ν2² on α+Z² (rev8 l.134), i.e. the full theta-lift exponent per label. A binary indefinite form can hit more than 3 classes mod 8. A next package would preregister "the uniform 140-label pool of the scaled Q(ν) mod 8 (scale = least integer making Q integral on all α+Z²)", with natural density on a box and the cone weight w(v) as written, vs ρ_res. Its density convention must be fixed in PREREG. Not done here (stop rule).
