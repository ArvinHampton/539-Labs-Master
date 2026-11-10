# order61 RESULTS (LOCAL Bridge C; RG* labels; CORE_FREEZE; no push/send)
PREREG sha256 9cc780f182bf4f21538b4547a28b96b0e5289f71828906973023081205edc04d, hashed before any test.
Scripts: scripts/rg47a_bis.py, scripts/rg47d.py. Data: data/rg47a_bis.json, rg47a_bis_raw.npy, rg47d.json. Logs: logs/.
Not used: P̂_orth, Ξ, k≠0, Map-C6. order58/ and order60/ were only read.

## RG47a-bis (Cat A-numeric): PASS
- max |A1 − Σpieces| = 2.29e−16, which is ≤ 1e−12 (absolute; no scaling, no filter).
- Control (axis signs flipped): max abs = 3.34, which is > 1e−4, so the control is OK.
- The recomputed pieces are bit-identical to order58 rg47a_raw.npy (max diff 0).
- Dominance (disclosure):

| piece | frac dominant | median ratio to A1 | max abs |
|---|---|---|---|
| axis Q=1 | 83.5% | 1.0 | 1.67 |
| axis Q=7/2 | 11.9% | 0.27 | 0.73 |
| corner/EVEN | 7.0% | 8e−16 | 1.34 |

## RG47d both-axes closure (Cat A-numeric): FAIL
- Gate reproduced: Â1 rank 75, joint 148 at w=½ and 150 at w=1.
- R = Â1 − axis_Q1 − axis_Q7/2 has rank 34 at both weights:
  - w=½: joint 68, excess **34**;
  - w=1: joint 36, excess **2**.
- The PASS bar was excess ≤ 0 at both weights, so this is a FAIL.
- The result is robust to the rank tolerance: it is unchanged at 1e−6 and 1e−12. The singular values have a clean gap, about 0.13 against 1e−15.
- Controls, recomputed and matching order60:

| object | excess w=½ | excess w=1 |
|---|---|---|
| minus Q1 only | 71 | 49 |
| minus Q7/2 only | 84 | 72 |

- Characterization (disclosure):
  - The largest entry of R, 1.3436, equals the corner/EVEN max abs, so the leftover is carried by the corner/EVEN piece.
  - At w=1 the two excess directions have relative singular values 0.207 and 0.153. They are spread over many samples: the top row weights are only about 0.03 each, led by x = 11/7, 10/7, 20/7, 8/5, 9/5, 3/7, i.e. denominators 7 and 5. No single sample carries them.
  - At w=½ the 34-dimensional excess sits on the small-x rows, x = 1/15 … 1/8 (weights about 0.78). So w=½ is the wrong weight: R pairs with weight 1, apart from a 2-dimensional defect.

## RG48-Weil: SKIP (ABSENT)
These ingredients are missing from disk:
- the χ=±i Weil-representation eigenvectors over the full basis;
- the discriminant form or Weil matrices of the companion lattice;
- a signature-2 genus-mate basis.

order12 only proposes building these (RESULTS:29). order12/a.py tests χ residuals on the 82 det-35 definite thetas, which is not a full-basis Weil span. Milgram stays Cat B.

## Suggested order62
Preregister an RG47e test of the corner/EVEN piece. Test whether R_both − corner closes at w=1, and/or whether the 2-dimensional w=1 defect is spanned by corner pieces. Use the same rank method and tolerance.
Separately, write out the companion discriminant form and its Weil matrices before rerunning RG48.
