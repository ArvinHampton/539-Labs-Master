# U1 LEDGER — Open items, algebraic track, post-rev5 update (2026-10-18)

Package: `Open_Algebraic_Update_2026-10-18/` (a report snapshot at 19:37 CDT plus the new scripts and outputs). The earlier package `Open_Algebraic_2026-10-18/` is unchanged. Erratum items (a) and (d).
Pure copy-and-create. No locks altered. CORE_FREEZE holds. Distinct from HQCC termination claims. No TPC or RH claim. Convention: Cat A = proved or exact; floating-only/numerical/cited = Cat B. See ERRATUM_Rev5_PostPush_2026-10-18.md. Text outputs are verbatim in the package's OUTPUTS_BUNDLE_2026-10-18.txt (sha256 per member).

## Category A
- A1. g·M_t = M_t for every odd m, including composite m (t₀ = (0, 1/m)). Hence span{g-relations} = δ_iso ⊗ X, of dimension m(m−1), for all odd m, and dim V(2m²) ≤ (s/2)(s/2+1) − m(m−1).
- A2. Extra h-relations at m = 2k²−1, as proved relations (hence upper bounds):
  - m = 7: 2 (validated against the exact Fourier result);
  - m = 17: 6, giving dim V(578) ≤ 83532;
  - m = 31: 12.
- A3. Exact diagnosis: for odd s no order-p subgroup of L′/Z² is q′-isotropic (s = 9, 11, 25). The finer.py old/new split is therefore an image/kernel split, not a ρ-decomposition. The exact ranks and ν₀ statements stand.

## Category B
- Commutants (floating): s = 9 has (+,+) = 48 + 12 and (−,−) irreducible; at s = 11 both sectors are irreducible.
- The general count extra = k(k−1).
- Open: s = 25 commutants (run not completed); lower bounds at m = 17 and 31.

## Files not included
`krylov25.log` (empty; the s = 25 run was stopped). `h_lattice.py`/`.json` are already in `Open_Algebraic_2026-10-18/`.
