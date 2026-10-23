# A37 preregistration: from A36 to a dimension count for dihedral forms in S(ρ_s)

For: Arvin Hampton (539 Labs). Written 2026-10-22 ~12:35 PM CDT, before any A37 computation.
Folder: SF/A37_dihedral_count/ (SF = /workspace/quantum-comp/reports/s_family_paths). New files only.
CORE_FREEZE (no certifier code touched/run, H_s not redefined), no s31 mm sector, nice, OMP_NUM_THREADS=1, ulimit -v 3 GB.

## Construction (the "genus lifts")
Λ = Z + Zω with Q = N (A36 §1), O = Z[√n]. For a split prime p ≡ 1 mod lcm(2D², Tlevel) and a prime 𝔭 | p
of O, put Λ_𝔭 = {ξ ∈ Λ : ξ ∈ 𝔭 locally at p} with form Q/p. Since p ≡ 1 mod 2D² and Λ_𝔭 ⊗ Z_q = Λ ⊗ Z_q for
q | D, (Λ_𝔭, Q/p) has the same discriminant form, characteristic shift a and label set as A_s, and the
manuscript lift formula applied to it is
  Θ_𝔭: a^𝔭_{α,β}(m) = ½ Σ_{ν∈α+Λ, Q(ν)=pm, Dν∈𝔭 at p, mod ε²} e(B(ν,β)).
As 𝔭 runs over primes in all classes, Λ_𝔭 runs over all lattices of the form 𝔞Λ (all ideal classes).
Hypothesis TB5: the manuscript theta-lift theorem (TB2: type ρ_s, λ = 1/4, constant term ∝ c₀, criterion)
holds for every (Λ_𝔭, Q/p) (same proof; lattices in the genus of A_s). Category A results below are relative
to TB, TB4, TB5.

## Questions and tests
- Q1 (count). d_dih(s) := dim of the span of {P_σΘ_c} over classes c and Hecke images (cusp parts),
  i.e. the dihedral K_s-forms of modulus | D landing in ρ_s, which are the ψ ~ ψ∘σ classes visible through lattices
  of the genus. Test: exact mod-ℓ rank of the coefficient matrix of
  {P_σu, T'_qP_σu (3 primes), P_σΘ_𝔭, P_σΘ_𝔭̄ (primes 𝔭 covering every wide class of Cl(O))}, cuspidal
  combinations in sectors with Eisenstein part. Mod-ℓ rank ≤ true rank, so each value is an exact lower bound.
- Q2 (compare). PASS if d_dih = proved dim at s = 9, 11, 23, 25 (control: at s = 25 any rank > 3 would contradict
  the certified dim = 3 and falsify TB5 or the implementation). Formula stated only if PASS.
- Q3 (upper bound / s = 27, 29). Primary: if d_dih(27) or d_dih(29) ≥ 4, then a 4th form exists and is dihedral
  (dim ≥ 4; with the bracket [3,4], dim = 4). If d_dih = 3, the 4th form is not decided by this test. A proof that
  every form is dihedral (trace formula / Galois / Bessel-span) is attempted on paper; it is reported as FAIL
  unless a complete argument is written.
- Q4: if a formula is proved, test further s where feasible.

## Categories
Cat A: exact (integer / mod-ℓ rank lower bounds) relative to TB, TB4, TB5. Cat B: float, post hoc fits.
