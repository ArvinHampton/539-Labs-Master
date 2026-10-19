# U1 LEDGER — Analytic Cat-B push (2026-10-18)
Package: `Analytic_CatB_Push_2026-10-18/`. Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact; floating-only/numerical/cited = Cat B. Text outputs are verbatim in the package OUTPUTS_BUNDLE_2026-10-18.txt (sha256 per member).

**Renaming in the paper:** the report's "Theorem L" (CRT factorisation) is rev6 Prop 14.7(ii), and its "Lemma R" is the q-adic reduction lemma (rev6 Lemma 14.8). The report file is copied verbatim and keeps its own labels.

## Category A
- A1. Period 72 at x=1/3. ea depends only on (s mod 9, ε), with ε = (−1)^{v₂(gcd(s,8))}. Exact for s ≤ 1000, r ≤ 10. Corrects the Open-Analytic wording (split by ε; sign (−1)^r).
- A2. Exact t^{11/2} and t^{13/2} coefficients at x = 0, 1/2, 1/3 (K=13; held-out re-verification).
- A3. Periodicity mod N′ / 24N′. CRT factorisation of H(c). Gauss evaluation for p ∤ a·s(s−2)(7s−32). Degenerate p cases. q-adic reduction. (Brute-force checks, 0 mismatches.)
- A4. Even-N minimal periods 16, 16, 144, 96 for N = 2, 4, 6, 8. 144 is explained; 16 and 96 are by exhaustive check up to the proved bound. x=1/4 Gauss data.

## Category B
- Engine and mpmath numerical agreement.
- t^{e/2} at x = 1/4, 1/6 not computed.

## Files not included (binaries/empty)
pkl files, __pycache__, empty .err/.log files (listed with sha256 in the bundle header).
