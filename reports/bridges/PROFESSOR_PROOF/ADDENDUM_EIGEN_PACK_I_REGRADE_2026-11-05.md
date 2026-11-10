# Addendum to FINDINGS 9e57acc6… (Pack I D1–D3 review): regrade under the Owner's 16:23 pure-math rule

PP audit: CONFIRM with REGRADE. Under the 16:23 rule, a claim is rejected only on a proof that it is false or inconsistent. The verdicts are relabelled as follows.

- Gal(ℚ(ζ₄₉)/ℚ) ≅ (ℤ/49)×, cyclic of order 42: **PROVED** (unchanged).
- 25 primes sufficient: **REFUTED** (unchanged). The basis is the concrete holdout mismatch. The ~573-bit vs envelope comparison is withdrawn as a refutation argument, because the envelope is not a lower bound.
- Mod 140 Kronecker ⇒ D1 descent: REJECT → **GAP**. This is a non sequitur, since a CRT filter does not imply Gal-stability. Descent to ℚ itself is not shown false.
- D3 height via Kronecker+(A,B): REJECT → **OPEN** (no derivation given).
- D2 ALU/RTL script as the N36 integral matrix: REJECT → **OPEN/ABSENT**. The script is not on disk, and treating it as the integral matrix is a category error.
- "D1/D3 UNLOCKED": REJECT → **OPEN**. The status claim is unsupported.

Net: D1, D2 and D3 are OPEN. 25-prime sufficiency is REFUTED by the holdout mismatch. Tip untouched. No CERT.

## Correction (16:30 CST)
"25 primes sufficient: REFUTED" is retracted. The status is now **OPEN**.

The holdout run (recon_batch1.log) used 24 training primes, sampled at most 12 entries per row, and held out prime 8007581. Its failure shows only that 24 primes are insufficient for the sampled entries, and only conditionally on two hypotheses:
- H1: the RREF has entries in ℚ (D1, OPEN).
- H2: none of the primes is bad.

25-prime sufficiency was never tested.
