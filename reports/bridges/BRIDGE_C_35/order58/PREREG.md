# order58 PREREG — Bridge C local modular; RG* only; CORE_FREEZE; new files only in order58/
Hashed before any test. No inventing P̂_orth/Ξ/k≠0. Read-only on order≤57. Local modular only. No push/send.

## RG47a (Cat A-numeric): localize A1(P_orth) obstruction
Decompose using order6 PREREG §1 half-line L_O only:
  A1(P_orth) = A1(axis Q=1) + A1(axis Q=7/2) + A1(EVEN/ν-orthant remainder)
Axis pieces = half-line contributions along e1 (Q=1) and e2 (Q=7/2), midpoint B̄1(0)=0 (order54).
Remainder is DEFINED as the written orthant/EVEN sum over the same L_O, computed independently (not as a difference).
Sample: order56 sample, 216×105 at x and −1/x; Â1 ≡ A1(P_orth) (RG46a).
PASS iff (i) max relative residual |A1 − Σpieces|/max(|A1|,1e−300) ≤ 1e−6 over sample (or exact Cat A identity cited from order6 text + numeric check),
and (ii) dominance table reported: per piece, max and median |component|/|A1|.
Control: flip sign of axis half-line weights; must give relative residual >1e−4 on ≥1 case, else RG47a FAIL(control).
If order56 sample or L_O definition cannot be loaded/reconstructed from written files: SKIP with obstruction.

## RG47b (Cat A-numeric): axis S-defects vs order6 quantum shadows
Shadows (order6 RESULTS): g1 = Σ n e(n²τ), n∈α1+7α2/2+Z ; g2 = Σ n e(7n²τ/2), n∈α1+α2+Z.
Only if order6 written text gives an explicit match statistic (period integral/defect formula) with constants: PASS iff max rel err ≤ 1e−6 and wrong-shadow (g1↔g2 swap) control rel err > 1e−4.
Otherwise SKIP with obstruction — no invented match statistic.

## RG48 (Cat A no-go attempt): full Weil χ=±i basis for P-even
Enumerate discriminant form of companion lattice (as written in order12) + signature-2 genus mates.
Test: is the P-even target in span of χ=±i Weil eigenvectors over FULL basis (exact rational/cyclotomic linear algebra, or numeric with rank tol 1e−9).
Clean FAIL → document Cat A no-go upgrade path for order12. Positive find → document for authors; NOT adopted as P̂_orth.
If companion lattice Gram is not written in order12: SKIP with obstruction.
