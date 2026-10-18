# U1 LEDGER — u_L criterion closure (2026-10-18)

Package: `uL_Criterion_Closure_2026-10-18/`. Consolidated in rev. 5 §13.5 (Theorems 13.8 and 13.9).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. exact finite computation); floating-only = Cat B. Notation as rev. 4 (W_P = Fix(P); V_Eis/d_Eis). See ERRATUM_Consolidated_Rev5_2026-10-18.md.
Text outputs (json/log/txt/jsonl/flag) are stored verbatim in the package's OUTPUTS_BUNDLE_2026-10-18.txt (byte counts and sha256 per member); reports and scripts are separate files.

## Category A
- A1. For odd s with s(s−2) squarefree: |Ḡ^σ| = 2^{ω(s)}φ(s−2), proved by Chevalley (ray form, unit-norm index 1) and independently by genus theory. Only the coprime c-part occurs.
- A2. Squarefree criterion: u_L is Eisenstein ⇔ h(Q(√(s(s−2)))) = 2^{ω(s)}. Exact cross-check at 47 values of s ≤ 151: Eisenstein only at s = 5, 7, 13, 15.
- A3. Coset property: T_𝔠 + ψ(W) = T_𝔠 for every 𝔠, and S₀ = ψ(W) for all s (§3A general local proof). Bold W is the unit stabiliser, not W_P.
- A4. Verdicts for s ≤ 44. Eisenstein: s = 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 20, 24, 28. CUSP: every other s in 5..44.
- A5. s = 32, 34, 36, 40 are CUSP (enumeration to B = 200000 agrees with the bound-free exact sets).
- A6. s = 24 has no mixed-prime parts (local proof). (1,12), (12,1), (1,16) and (16,1) are genus-pure.

## Category B / open
- A closed criterion for non-squarefree s(s−2) (verdicts are per s).

## Files not included
`__pycache__/`, empty logs (listed in the bundle manifest).
