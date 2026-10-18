# U1 LEDGER — E-part cocycle closure (2026-10-18)

Package: `Cocycle_Closure_2026-10-18/`. Consolidated in rev. 5 §13.4 (Theorem 13.7).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact (incl. exact finite computation); floating-only = Cat B. Notation as rev. 4 (W_P = Fix(P); V_Eis/d_Eis). See ERRATUM_Consolidated_Rev5_2026-10-18.md.
Text outputs (json/log/txt/jsonl/flag) are stored verbatim in the package's OUTPUTS_BUNDLE_2026-10-18.txt (byte counts and sha256 per member); reports and scripts are separate files.

## Category A
- A1. The constant C = −π/2, derived by hand: I_n(z) = C·e(nz) exactly, and y → ∞ asymptotics. Hence E_L(z) = −(1/π)∫_z^{i∞}[u_L, R_z^{1/2}].
- A2. Boundary step from H to the rationals, both signs of cx+d: κ_L(x) − |cx+d|⁻¹κ_L(γ′x) = −(1/π)∫_{γ′⁻¹∞}^{i∞}[u_L, R_x^{1/2}], with branch ε = sgn(cx+d) and A(x) = |cx+d|A(γ′x).
- A3. Vector law u∘γ′ = ρ(γ′)u, label by label for all 140 labels (§3A). The constant terms b_λ = log ε·δ_{α∈Z²} are carried inside the theta identity. The general-γ′ vector cocycle reduces to the psi-Cocycle S-formula.

## Category B (support only)
- Vector identity at STS, ST²S, ST³S: ≤ 3.3e−12 (§3B).
- Quadrature check of C: 1e−18. Non-tangential κ fits in 4 directions.

## Files not included
`Cocycle-Closure.pre-3A.md.bak` (pre-§3A backup, superseded); `__pycache__/`.
