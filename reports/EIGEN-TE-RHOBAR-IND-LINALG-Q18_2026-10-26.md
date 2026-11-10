# EIGEN — Card 1B: exact Ind path, S₄(Γ₀(49),ρ̄) — FINDINGS 2026-10-26
STATUS: PARTIAL. The dim-check is an exact MATCH: 592 = 503 ⊕ 89. The q^18 basis was not constructed, and no coefficients were invented.

## Authority (sha256 verified)
- OW Card 1B 43e94be25c8137112b1722a20616533f4a9d9c69ef95a88691965dcd202586a6 ✔ (both copies). Card 1A target dede8346d5639ebc9b2667af36728d894c12c7cefc4b2bfac1db6bc866de8c2a.
- Prior ABSENT step4 7ef0042ba998546ce910f70c8db4724deff9cda5759e5a1a3456ae929c456e5a ✔; V42_exact.sobj d1e532c8…f520d; ST_W.sobj a86980cf…1c72 (both verified this session); Card 2 ACCEPT f56b7d9b… (no commutant re-run).
- Tip: start 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; end recorded below. tip_touched NO. invent HOLD. No tip fold. No Card 7 work.

## Method (exact data from the landed V₄₂)
- ρ̄ = inverse-transpose of S,T restricted to the exact Eis36 and cusp6 bases over CyclotomicField(140).
- Ind_{Γ₀(49)}^{SL₂ℤ}1 is the permutation action on the 56 points of P¹(Z/49). Total dimension 42·56 = 2352.
- Dimension formula for k>2: dim M_k = d + dk/12 − α(e(k/4)ρ(S)) − α((e(k/6)ρ(ST))⁻¹) − α(ρ(T)); dim S_k = dim M_k − #{T-exponents = 0}.
  - ρ(T) exponents are exact: roots z^j of the exact charpoly, added to the Ind T-cycle exponents.
  - S and ST eigenvalue multiplicities come from exact traces of powers, using tr(A⊗B) = trA·trB and character orthogonality. Each integer multiplicity was asserted to lie within 1e-6 of an integer; this is the only float step, and it only certifies integers.
- Calibration: the formula reproduces Sage CuspForms(Γ₀(N),k).dimension() for N∈{2,7,11,25,49}, k∈{4,6,8}, with 15/15 agreement.

## Result
| piece | dim M₄ | dim S₄ |
|---|---|---|
| ρ̄ Eis36 | 514 | **503** |
| ρ̄ cusp6 | 89 | **89** |
| ρ̄ total | | **592**, MATCH |

Cross-check: undualized ρ gives 494 + 79 = 573. This confirms that ρ̄ (inverse-transpose) is the convention behind 592. Weight-2 values (167/33) are listed in the log for information only; the formula is not valid at k=2.

## Not done: q^18 basis
- An explicit basis means 592 vector-valued forms, each with 2352 components, through q^18 over K.
- The two routes are modular symbols for Γ(140·49)-level data, or scalar forms on Γ(980) assembled through Ind. Both are far beyond this session's compute.
- passagemath has no constructor for VVMFs with an arbitrary ρ.

## Artifacts (grok-batches/eigen-ind-linalg/)
5ad8f8d3ee8a3b94cf948dbab0fc28e90b919250bf465edfa09ad2e7c3defd23  eigen-ind-linalg/dimind.sage
a129f9a581195ae68386a6de1736f406c5501fdc4e358ecfcd7c263cdf903ec3  eigen-ind-linalg/dimind.log

## Next unblock (one crisp Owner Write)
Accept the exact dim MATCH as the dim-check. Then authorize one of two scopes for the basis:
- Reduce scope to the cusp6 piece (89 forms) via Hecke/modular symbols on Γ₀(49) ∩ Γ(140) with exact projection onto ρ̄|cusp6.
- Or allocate a long background compute run (hours) for the full 592.
- Tip end sha: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91
