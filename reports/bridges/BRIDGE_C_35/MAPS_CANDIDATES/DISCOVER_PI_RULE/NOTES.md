# NOTES: DISCOVER_PI_RULE (exploration first, then proofs)
## Inventory of residual objects that could index a length-539 sequence
O_res = {21+9j : 0≤j<539} (539 elements, 8 β♯ blocks 3×68 + 5×67); β♯/β̂; τ and g = (−1)^τ (accepted); C1 "index rounds by O_res"; C3/Principle (S) 18+521; residue-word bijection; MF2/DM1–DM5 hit law; Lemma V; P_res (accepted).

## Proofs (Category A)
- RP1: each T3 branch k ↦ k, 4k+2, 2k+1 is injective in k, and w_0 = x mod 3. By induction, w_0..w_{n−1} is determined by x mod 3^n and determines it. Checked exhaustively for n ≤ 8.
- RP2: u ≡ 3 (9) ⇔ u = 3k with k ≡ 1 (3) ⇔ w_i = 0 and T3(u) = k ≡ 1 (3), i.e. w_{i+1} = 1. Checked for u < 10^6.
- RP3: T3(21+9j) = 7+3j ≡ 1 (mod 3), and every element of O_res is ≡ 0 (mod 3). So no T3 step stays in O_res, and the "carrier walk" is empty.
- RP4: "01" occurrences cannot overlap, so a 540-letter word has at most 270 of them, with equality only for (01)^270. Confirmed by DP. Without w_539: the maximum is 269, reached by 810 words (tests T3c).
- MF2/DM laws and Lemma V are statements about u mod 2^k. By CRT, the seed's 2-adic part is independent of x mod 3^539 (RP1). They are distributional, not word-selecting: they cannot pick a single word. (Category A for the independence; the laws themselves come from the prior packages.)
- 18+521: nothing in the sources gives a branch letter to either block. Splitting a word 18+521 needs a letter assignment, which would be a free choice.
- β♯ schedule as word: the sources contain no forced map {0..7} → {0,1,2}. Dropped as an invention.

## Remaining free choices (any one of these would be needed to fix Π)
1. A seed, or a selection rule on x mod 3^539 (RP1: all 3^539 words are realised).
2. An extremal objective (for example max P_res hits) plus the endpoint convention for w_539.
3. An alphabet map from fibre index or block to branch letter.
