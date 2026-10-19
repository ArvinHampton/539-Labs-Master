# U1 LEDGER — Analytic rounds 3–4 (2026-10-19)
Package: `Analytic_Round3_4_2026-10-19/`. Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact; floating-only/numerical/cited = Cat B. Text outputs are verbatim in the package OUTPUTS_BUNDLE_2026-10-19.txt (sha256 per member); pickles in BINARIES_B64_BUNDLE_2026-10-19.txt. Only files new or changed since Master tip 1ec3baaf are included.

**Labels:** CRT factorisation = CFP (rev7 PDF Prop 14.8(ii)); q-adic reduction lemma = rev7 PDF Lemma 14.9. See NOTE_LABEL_CFP.md.

## Category A
- A5. General H(c) formula (CFP + q-adic reduction) exact vs brute force for N = 32, 35, 45, 49 (199680/327600/421200/802620 tests, 0 mismatches); now all N in {2–13,15,16,21,25,27,32,35,45,49}. (rev7 Prop 15.10)
- A6. Even N: H_{1/2} = 4(−1)^c[16|s]; H_{a/4} explicit; N = 8 six classes, period 96 = lcm(32,48). (rev7 Prop 15.11)
- A7. N = 8 classes pairwise distinct via invariants I1–I4; residue-level finite computation, no scan over s. ea tables at x = a/8. (rev7 Prop 15.12)
- A8. t^{11/2}, t^{13/2} at x = 1/4, 1/6 (universal form + exact class constants); vanishing to all orders at x = ±1/4, 4∤s and at x = 1/6, s odd. (rev7 Prop 15.13)
- A9. t^{15/2}, t^{17/2} at x = 0: R + S√Δ split persists; R₁₅, R₁₇ explicit; 10 held-out checks; c₁₅(5) = c₁₇(5) = 0. (rev7 Prop 15.14)
- A10. S_e exact factorisations at e = 11, 13, 15, 17 (each e).
- A11. R_e (frozen) = S^ax_e exactly at e = 7, 9, 11, 13 (compare_axes). (rev7 Prop 15.9)

## Category B
- Double-precision engine agreement (x = 1/4, 1/6; c₁₅, c₁₇ at s = 6, 7, 9) and 60-digit direct sums (s = 8, 20, 32).
- General S_e pattern for all e (even powers, (s−8)^{max(0,e+3−4j)}, pairing, Bernoulli numerators 691, 3617, 43867 in the top coefficient): observation only.

## Open
t^{19/2}+; axes forms at K ≥ 15 (to test R_e = S^ax_e at e = 15, 17); direct numerics at x = 1/4, 1/6 for s ≠ 8.

## Files not included
__pycache__ and empty .err files (listed with sha256 in the bundle header). Unchanged files already on Master in Analytic_CatB_Push_2026-10-18/ are not re-pushed.
