# EIGEN-TE-RHOBAR-N36-503-EXACT-CRT — 2026-10-26 (America/Chicago)

## STATUS
**CERT (multi-prime CRT, held-out verified)** for the rational RREF basis of the 503-dim cusp-∞ q-expansion space (through q^18) and the exact ν∈{1,9,4,14,16} rows.
**PARTIAL** for the combination/kernel coefficients (combos): not reconstructed (see Obstruction). The N36 lane is not fully closed.

## Authority (sha256 checked on disk at start)
- OW 6bc5f5ab5e855b7aab79e25691e97932cd57e71a7fbf790c8b5c29adf451d917
- ASSIGN 4403ebe5e501711c7227bb2fef0b61968a5e9ffef1263d3994a3e056916a6fc1
- Eigen ACK ea7a2e565f284742c65ba97c9de0a9eabd517a9d5b8678ba7a706b04c80dd781
- W1 MATCH source ee9c36f9e5a23f3147bdbd104a4ba648cf8e9e2f3f22c750c0d143459364da96
- Prior CLOSED_B HOLD CRT 80ae4f5b… has been SUPERSEDED for N36 exact CRT (owner voice call-b052d177).
- Tip Soft SF LOCK: start = end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, **tip_touched NO**.

## Method
- solve36w.sage (unchanged) run at m=7 for primes p≡1 mod 980, p<2^23: 7840981, 7851761, 7860581, 7863521, 7864501, 7946821 (6 primes). Every prime gives polar matrix 11700×13305, kernel dim 503, and **rank 503** (target 503).
- crt36.sage follows the rhos/crt.sage pattern (rhos/ was only read, never modified). It checks that cols metadata and RREF pivots agree across all primes, CRT plus rational_reconstruction over 5 primes (modulus 114.5 bits), then holds out p=7946821 for verification.
- Result: pivots agree on all 6 primes. Max rational height is 9.65 bits (lcm of denominators 16), well below the bound of about 57 bits. The QQ RREF reduces exactly to the mod-p RREF at **all 6 primes, including the held-out prime: True**. The height matches the earlier 2-prime attempt (renamed *_crt2_NOTCERT.sobj and superseded), so the reconstruction is stable.
- Caveat: this is the standard multi-prime modular certificate. It rests on all six primes being good primes, with rank 503 at each prime equal to the dimension cited in W1. It is not an independent char-0 linear-algebra proof.

## Exact ν rows (column of QQ RREF at component exponent ν/140)
- ν=1 (comp 31): 338 nonzero rows, max denominator 16. **Nonsparse**, which is the MR1 ask.
- ν=9 (comp 34): 327 nonzero rows, max denominator 8. **Nonsparse.**
- ν=4 (comp 9), ν=14 (comp 20), ν=16 (comp 6): each column is a single pivot row with value 1.
Written to n36_mr1_nu_rows_QQ_m7.csv.

## Obstruction (combos) — Rec A
solve36w.sage saves only basis_mod_p = RREF(Kr·MT), not the kernel Kr. In addition, the polar conditions at the non-∞ cusps use z49 = g0^((p-1)/49) with g0 = F.multiplicative_generator(), so the ζ49 embedding is **not coordinated across primes**. Kernel combos are therefore Q(ζ49)-valued with uncoordinated embeddings, the same failure mode as the old ζ49 CRT. The ∞ image is unaffected because its RREF is rational.
**Rec A:** re-solve with a coordinated cyclotomic embedding (fix ζ49 as the image of a chosen root of Φ49 mod p, consistent across primes), save Kr, then CRT over Q(ζ49). I invented no fix outside cite.
**Rec B:** if MR1 only needs ∞-expansions and ν rows, the CERT artifacts below are enough.

## Artifacts (/workspace/grok-batches/eigen-n36-503/, sha256 in ARTIFACTS_CRT.sha256)
- n36_basis_q18_inf_QQ_m7_crt6.sobj 74d8eb15b0ad41879c098ebf03f8b2d033f326826e3ef98179c16487bb192686 (dict: primes, cols, basis_inf_QQ 503×648, rank)
- n36_mr1_nu_rows_QQ_m7.csv 43ee912cb20d696a29b71dbb7b9b04048db91699a52c40f32a4f5890500c1a68
- crt36.sage 884d4d23…, export36_QQ.sage d1784c10…
- New n36w_modp_m7_p{7851761,7860581,7863521,7864501}.sobj
- The W1 exports (n36_mr1_nu_rows_modp.csv, n36_basis_q18_inf_modp.csv, seeds36w.sobj) are unchanged; their hashes match ARTIFACTS_W1.sha256.
- /workspace/grok-batches/eigen-q89-basis/rhos/ was left untouched apart from one read-only look at crt.sage.
