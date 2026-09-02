P-listen-on-wire bitstream experiment
2026-09-01

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
Twin Prime and RH unclaimed. HQH-539 hardness Category B.
This note is Category A discrete only. It is not a metal wire. It is not an entropy source. Coup_enc stays empty.


1. Question

On a recorded last-bit stream from production T3 walks, does a predictor given Class_6 compress the last-bit stream to nothing, and does a predictor given only bits fail to do the same.

Production T3 is the ePrint three-branch map, matching hqh539.py in hqh539-engine:
If n = 0 then T3(n) = 0.
If n > 0 and n ≡ 0 mod 3 then T3(n) = n // 3.
If n ≡ 1 mod 3 then T3(n) = (4n + 2) // 3.
If n ≡ 2 mod 3 then T3(n) = (2n + 1) // 3, equal to (2n − 1)/3.

Last-bit table under this map:
classes 0, 1, 4 modulo 6 give Bit_next = 0
classes 2, 3, 5 modulo 6 give Bit_next = 1


2. Integer-table lock already closed

On n = 1 through 5999 the last-bit table is exact.
Every class 0, 1, 4 sample has Bit_next = 0.
Every class 2, 3, 5 sample has Bit_next = 1.
H(Bit_next | Class_6) = 0 on that table.
That lock is not reopened.


3. Recorded bitstream experiment

Two recorded streams were built from the same production map.

Stream A. Seeds 1 through 2000. Forty steps each, including the 2-cycle {1, 2}. N = 80000 pairs.
Class_6 predictor accuracy = 1.
Markov-1 predictor that sees only previous bits has accuracy 0.762.
Empirical bit balance 0.4805 / 0.5195.
Empirical H(Bit | Class_6) = 0.
Empirical I(Bit ; Class_6) = 0.9989, equal to empirical H(Bit) on this finite sample.

Stream B. Seeds 10^6 through 10^6 + 499. Eighty steps each, stopping when n ≤ 2, so the attractor is excluded. N = 15177 pairs.
Class_6 predictor accuracy = 1.
Markov-1 bit-only predictor accuracy = 0.676.
Empirical bit balance 0.4989 / 0.5011.
Empirical H(Bit | Class_6) = 0.
Empirical I(Bit ; Class_6) = 0.999997, equal to empirical H(Bit) on this finite sample.

A large-seed check: n = 10^18 reaches 1 in 92 raw T3 steps. That matches the existing Category A short-orbit record. It is not a 539-step free termination.


4. What this closes and what it does not

Closed under Pack+(S), Category A discrete:
On a recorded last-bit stream from production T3 walks, Observer_O3 who is given Class_6 predicts every next bit.
Observer_O2 who is given only the bits does not. The best one-step bit predictor on Stream B is a persistence rule with accuracy 0.676, not 1.
The leftover that a binary observer calls noise is the Class_6 label. Given that label the leftover is zero.

Not closed:
P-Coup_enc remains empty.
P-mesh device remains unbuilt Category B.
P-Score_lab has no metal data.
P-N_res remains forbidden until Coup_enc exists.
HQH-539 is not an entropy source and is not an RNG. Hardness stays Category B.
This experiment is an integer walk written as bits. It is not a laboratory conductor.


5. Status

Status code:
P_LISTEN_ON_WIRE_BITSTREAM_EXPERIMENT_CLOSED_CAT_A_2026-09-01
CLASS6_PREDICTOR_ACCURACY_1
BIT_ONLY_MARKOV1_NOT_1
COUP_ENC_EMPTY

CORE_FREEZE unchanged.
