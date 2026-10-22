# A31: referee check of ledger entry 7 (odd-prime local factor) and its use in entry 4

Written 2026-10-22 (America/Chicago). New files only. CORE_FREEZE respected (H_s not used; no certifier code touched; A12 scripts not reused). nice, OMP_NUM_THREADS=1, < 0.5 GB. Nothing pushed or sent.

## Verdict: **confirmed with wording fixes** (no mathematical gap found)

## 1. Precise statement (Category A, P-rel standard Weil-representation facts and Gauss sums)

Let p be odd, e ≥ 0, D_p = (Z/p^e, q(x) = c x²/p^e), c a unit. Let ρ_p be its Weil representation (factors through SL2(Z/p^e); odd-order forms have even signature, so no metaplectic cover is needed). Let E0_p = ρ_p(SL2(Z))·δ_0 (linear span) and W⁺_p = {f ∈ C[D_p] : f(−x) = f(x)}.

**Lemma.** (i) E0_p = W⁺_p, dimension (p^e+1)/2. (ii) t_p := tr(S | E0_p) = ½(tr S + tr SZ) equals 1 if e is even, (2/p) if e is odd and p ≡ 1 mod 4, and 0 if e is odd and p ≡ 3 mod 4. So t_p = 0 iff p^e ≡ 3 mod 4. The value does not depend on c.

The quantity is a trace on the p-part only, on the even subspace. No γ_s-invariance is imposed locally, and none is needed (see §2).

## 2. Legitimacy of the tensor step

- W and C do **not** factor, and the proof does not need them to. Only E0 = ρ-span(δ_0) is factored.
- δ_0 = ⊗_p δ_{0,p}. SL2(Z) → ∏_p SL2(Z/p^{k_p}) is surjective (CRT plus surjectivity of reduction), and ρ = ⊗ρ_p. The span of a pure tensor under a product group is the tensor product of the local spans, so E0 = ⊗_p E0_p and tr_E S = ∏_p t_p. The phases are consistent because the total signature is 0 and each odd local part has even signature.
- E0 ⊆ W because γ_s commutes with ρ and fixes δ_0, and Z ∈ ρ(SL2) fixes δ_0. So C = W ⊖ E0 and tr_C S = tr_W S − tr_E S = 0 − ∏_p t_p, where tr_W S = 0 is imported from A8c.
- Caveat (inherited, not new): this identifies E with E0 = ρ-span(δ_0), as the task specifies. A11 notes that E0 = E_A10 (the isotropic-span definition) was only observed numerically beyond s = 18.

## 3. Hand derivation of t_p

Take the convention S e_x = ε |D|^{-1/2} Σ_y e(−B(x,y)) e_y with B(x,y) = 2cxy/p^e and ε = conj(γ(c))/|γ(c)|, where γ(a) = Σ_{x mod p^e} e(a x²/p^e).
- tr S = conj γ(c)·γ(−2c)/p^e.
- tr SZ = conj γ(c)·γ(2c)/p^e.
- The opposite T-sign convention conjugates everything. The result is real, so it is unchanged.

**e even:** γ(a) = p^{e/2} for every unit a, so tr S = tr SZ = 1 and t = 1.

**e odd:** γ(a) = p^{(e−1)/2} (a/p) ε_p √p, with |ε_p| = 1. Then tr S = (c/p)(−2c/p) = (−2/p) and tr SZ = (2/p). So t = (2/p)·(1 + (−1/p))/2, which gives (2/p) for p ≡ 1 mod 4 and 0 for p ≡ 3 mod 4.

This matches A12. For e odd, (2/p) is the Legendre symbol of the prime p; the Jacobi notation is harmless.

(i) is the content of A12's odd H1/H2 (strong form). I checked its logic, and §4 verifies it independently for p^e ≤ 201. Since E0_p ⊆ W⁺_p is automatic, the claim t_p = ½(tr S + tr SZ) depends exactly on (i).

## 4. Computer verification (Category A, exact; independent code)

**`local_odd.py` → `logs_local_odd.txt`.** Covers every odd prime power p^e ≤ 201 (53 values), each with c = 1 and with c a non-residue (106 runs).
- t was computed exactly in Z[ζ_{p^e}] by reducing modulo Φ_{p^e}.
- dim E0_p was computed as a rank mod a prime ℓ ≡ 1 mod p^e. Since mod-ℓ rank ≤ true rank ≤ dim W⁺, equality certifies E0_p = W⁺_p.
- Result: **0 failures.** Nonzero values ±1 occur where predicted, which also exercises the trace code.

**`global_trE.py` → `logs_global_trE.txt`.** This works directly on the full D = A^{-1}Z²/Z² for every s ≡ 0, 2 mod 8 with 8 ≤ s ≤ 74.
- It computes the ⟨S,T⟩-span of δ_0 and tr_E S modulo two primes ℓ (ℓ ≡ 1 mod 8M; int64-safe).
- On E we have S² = Z = 1, so tr_E S is an integer with |tr| ≤ dim E < ℓ/2. Hence tr = 0 mod ℓ implies tr = 0. The sign of √|D| only flips the sign of the trace.
- Result: **tr_E S = 0 for all 18 values of s**, so tr_C S = 0 given tr_W S = 0 (A8c).
- dim E agrees across both primes and with A11/A15 data (s = 8: 18 = 9·2; s = 56: 560 = 187+186+187).
- These checks cover and cross-check the existing certificates s = 8, …, 58, and extend them to 64, 66, 72, 74. Larger s was not run because dense elimination cost grows like |D|³.

## 5. Combination with the 2-adic part

For s ≡ 0, 2 mod 8, m ≡ 0, 1 mod 4, so 4 | M and a ≥ 2.
- u = 1 would force m(m−1) to be a power of 2, i.e. m = 2 (s = 4), so u ≥ 3 for every s ≥ 8. This is not needed for the argument, which handles u ≡ 1 mod 4 in the 2-adic factor anyway.
- **a odd or u ≡ 1 mod 4:** t_2 = 0 by H1/H2 plus the CC base classes a = 2, 3, 4, imported from A12/A13/A14.
  - Note: H2 is proved for a ≥ 3 only. The a = 2 classes rest on the exact base certificates (A11 `logs_exact_E0.txt`: classes (2, 1/4)⊕(8, −u/16) have tr = 0 exactly for u ≡ 1, 5 mod 8, i.e. u ≡ 1 mod 4).
- **a even and u ≡ 3 mod 4:** u is a product of odd prime powers. If none were ≡ 3 mod 4, then u ≡ 1 mod 4. So some p^e ∥ u has p^e ≡ 3 mod 4 (p ≡ 3 mod 4, e odd), and t_p = 0.

No case falls through. The odd-prime factor is only ever invoked in the second branch, and there only the vanishing direction is used.

## 6. Wording fixes for entry 7

1. "The δ₀-span equals the full even part" should read: "the SL2-span of δ_{0,p} in C[D_p] equals the even functions on D_p (local statement; W, C are not factored; only E0 = ⊗E0_p is)."
2. State t_p := tr(S | E0_p) explicitly, and note that it is independent of the unit c.
3. Note the scope: entry 4's identification uses E := ρ-span(δ_0). The equality with the isotropic-span E is not proved in general (A11).
4. Note that entry 4's a = 2 case relies on the CC base classes, not on H2.
5. Status of entry 7 may be upgraded to **P-rel F1–F5, IC by A31** (hand re-derivation, plus an exact check for p^e ≤ 201).

No TPC/RH claims. No Category B material is used here.
