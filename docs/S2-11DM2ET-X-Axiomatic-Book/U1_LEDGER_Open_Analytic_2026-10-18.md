# U1 LEDGER — Open items, analytic track (2026-10-18)

Package: `Open_Analytic_2026-10-18/`. Consolidated in rev. 5 §13.1–13.3 (Propositions 13.1–13.6).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. exact finite computation); floating-only = Cat B. Notation as rev. 4 (W_P = Fix(P); V_Eis/d_Eis). See ERRATUM_Consolidated_Rev5_2026-10-18.md.
Text outputs (json/log/txt/jsonl/flag) are stored verbatim in the package's OUTPUTS_BUNDLE_2026-10-18.txt (byte counts and sha256 per member); reports and scripts are separate files.

## Category A
- A1. F1 is proved: the 2-D cone Euler–Maclaurin expansion holds for every rational x (1-D Zagier lemma, quadrant lemma, cone decomposition, half-weight rule). The H_s closed forms at x = 0 are unconditional.
- A2. Exact reductions (R1)–(R3) hold for every rational x: corners cancel, and all integer orders vanish.
- A3. x = 1/2. Odd s: H_s(−e^{−t}) = O(t^N) for all N (Proposition O). Even s: closed forms through t^{9/2}, including the 16 | s √Δ terms.
- A4. x = 1/3. Closed form; γ₀ and eb depend on s mod 3; ea depends on s mod 144.
- A5. t^{7/2} and t^{9/2} at x = 0 (two symbolic routes agree to 170 digits).
- A6. C_third: the unit-cone weight-1 piece vanishes, including its completion. The weight-0 integral equals Zwegers' Θ_a (orbit unfolding).

## Category B
- ea at x = 1/3 is periodic mod 72 with four shapes (exhaustive table).
- Engine-vs-symbolic agreements and numerical windows (support only).
- No depth-2 rank-3 object carries C_third (structural argument).
- Section 4 (cocycle numerics, 45 rationals to 7e−13): superseded by Cocycle_Closure_2026-10-18 (Cat A proof).

## Files not included
`__pycache__/`, 9 pickles (sym_universal_*.pkl, H_closed3/4.pkl, H_generic3/4.pkl; 3–26 KB each, binary). They are listed with sha256 in the bundle manifest.
