# EIGEN-TE-RHOBAR-Q89-EXACT-LIFT — FINDINGS (2026-10-26)
STATUS: PARTIAL

## Authority (cited, disk re-verified)
- CLOSED_A 3cf5735ca0c2a61a0aeb5e7ed62de00cea47395ece07e4ed18b3330dfe2f2057
- ASSIGN 29ede292036d155f1eede8913609ba6a0b91ff5aa7daa956ee848bd117aec463
- Source MATCH (mod p) FINDINGS a8788e5c63c9f84d6bed66c808db5831ab751d9d0d930b8603fa7e25fedf2efd
- Dual OW 538a02d9… / ASSIGN b20ec0ee…; RHOS cb6469e2…/ce812a2a…; Step3 88911d8c… (cited only)

## Primes (all ≡1 mod 980, m=6, each RANK 89, kernel 89x1726)
CRT: 1027606441, 1027611341, 1027614281, 1027640741 (modulus 119.7 bits). Held-out: 1027644661. No new solves launched.

## Results
1. crt.sage (combination coefficients, RREF over 1726 unknowns): pivots agree across 5 primes, but RECON FAILED.
   Diagnostic (diag.sage): of 124815 nonzero entries, 75920 reconstruct with 4 primes, only 94 agree at held-out prime.
   Diagnosis: the combos are NOT rational — the cusp-polar conditions at cusps 0 and a/7 involve ζ49, and solve.sage fixes
   z49 = gen^((p-1)/49) per prime, i.e. an uncoordinated embedding of Q(ζ49) per prime. CRT over QQ is therefore not valid
   for combos; more primes would not fix it (not a height issue).
2. Cusp-∞ truncated image (108 slots through q^18, 6 seed components): RREF rank 89 at every prime; 1666/1666 nonzero entries
   reconstruct in QQ and match held-out prime. Max height 7.8 bits (vs 119.7-bit modulus), denominator lcm 6.
   Exact rank over QQ = 89 (CERT: the 89x89 pivot minor is nonzero mod p ⇒ nonzero over QQ).
   Exports: eigen-q89-basis/rhos/q89_basis_q18_cuspinf_QQ.sobj (sha c54be5b9d423da9e871a92f479aff463cca9a7a0797d7524257cd20a78f88065)
            eigen-q89-basis/rhos/q89_basis_q18_cuspinf_QQ.csv  (sha 770deb2d00d3aa7d17d7e6d52e7ef7f40dad24757b5db2d40b2ce6bb38d77116)
3. Char-0 holomorphy at all 8 cusps: NOT CERTIFIED. Mod-p holomorphy holds at 5 primes (polar eqs 11968 vanish), but the
   char-0 lift of the full 8-cusp expansions needs coefficients in CF(49) ⊂ CF(980).

## Exact blocker
Lift over Q(ζ49): rerun solve per prime with z49 chosen as the image of a fixed ζ49 under a coordinated prime ideal
(e.g. z49 = root of Φ49 mod p picked consistently via a fixed lift / Galois-normalized choice), then CRT+RR in the
Q(ζ49)-power basis (42 coords) and verify polar equations exactly. Not executed (each solve ≈26 min; method choice under invent HOLD).

## Tip
/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha start = end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched NO.
eigen-n36-503/ untouched. Soft SF F3 CLOSED; Bridge PARTIAL READY NO; Cards 8–11 not opened.
