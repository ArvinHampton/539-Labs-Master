# A36 preregistration: are the λ = 1/4 forms in S(ρ_s) dihedral (Hecke-character) forms?

For: Arvin Hampton (539 Labs). Written 2026-10-22, America/Chicago (CDT), before any A36 computation.
Folder: `SF/A36_hecke_character/` (SF = /workspace/quantum-comp/reports/s_family_paths). New files only.
CORE_FREEZE: H_s not redefined; no certifier code touched or run; no s31 mm sector. nice, OMP_NUM_THREADS=1, ulimit -v 3 GB.

## Setting (read from code, not redefined)
- Lattice Λ = Z² with Q(x) = x1² + s x1x2 + (s/2)x2² (A_s = [[2,s],[s,s]], det = −n, n = s(s−2)).
  Q(x) = N_{K/Q}(x1 + ωx2), ω = (s+√n)/2, K = K_s = Q(√n). 2Q is primitive of discriminant 4n, so Λ is an
  invertible ideal of the order O = Z[√n] (discriminant 4n).
- Lift (`A9/scripts/liftS.py`, `coeffsS.py`): a_{α,β}(m) = ½ Σ_{ν∈α+Λ, Q(ν)=m, mod γ²} e(B(ν,β)), with α ∈ D⁻¹Λ/Λ.
- Hecke operators T'_p (ledger entry 24), p prime, p ≡ 1 mod Tlevel.

## Hypotheses
- H1 (structural, Cat A target). Every component of u, of P_σu and of T'_pP_σu is a finite linear combination of
  θ_ψ(kz)-type series of K_s, ψ a finite-order character of the ray class group of O modulo D, with infinity type
  trivial on ν with N(ν) > 0 (this is what gives λ = 1/4). Cusp parts involve only ψ ≠ ψ∘σ.
- H2 (all dihedral). For s ∈ {9, 11, 23, 25}: S(ρ_s) equals the span of lift-derived forms, hence consists of
  K_s-dihedral forms. Test: check (from the source certificates) that each certified lower bound uses only
  forms built from u (P_σu, T'_pP_σu, u_cusp) and that it equals the certified upper bound.
- H3 (eigenvalue match). In each sector, the T'_p eigenvalues on the lift span are λ_p = ζ + ζ⁻¹ with ζ^E = 1,
  E = exp((O/DO)^×)·h(O) (a multiple of the exponent of the ray class group); i.e. a_p = ψ(𝔭) + ψ(𝔭̄).
- H4 (ring-class part). For ring-class characters ψ of Cl(O), λ_p depends only on the class of 𝔭 in Cl(O).
- H5 (formula). If all forms are dihedral, dim S(ρ_s) is a count of character pairs {ψ, ψ∘σ}; test whether a
  count built from exact class numbers reproduces dims at s = 9, 11, 23, 25 and decides s = 27, 29.

## Exact tests
- T0 Class data (unconditional): wide/narrow h(4n) and Cl(O) group structure by Gauss reduction cycles and
  Dirichlet composition; fundamental unit of O by the continued fraction of √n; |(O/DO)^×| and its exponent
  by exhaustive enumeration; |G0| = h·|(O/DO)^×| / |⟨−1, ε₊⟩ mod D|. Ring-class cusp pairs = (h − |Cl[2]|)/2.
- T1 Lift spans mod ℓ: for each sector σ, the vectors F0 = P_σu and T'_pF0 (8 primes p ≡ 1 mod Tlevel) are
  reduced exactly modulo a prime ℓ ≡ 1 mod lcm(phase denominators, E). Rank mod ℓ ≤ rank over C.
- T2 Eigen-search: with r = rank, solve the exact linear relations of T'_pF0 in the basis; for r = 1 (cuspidal
  combinations g_p = T'_pF0 − 2F0) λ_p = 2 + (g_p/g_{p0})(μ − 2); for r = 2, λ_p = x_p + y_p μ_j. Search μ over
  the candidate set Λ_E = {ζ+ζ⁻¹ : ζ^E = 1} in F_ℓ.
  PASS (H3, sector): there are exactly r admissible values μ (one eigen-system per form) such that every λ_p lies
  in Λ_E for all 8 primes, and the symmetric functions of the eigenvalues are consistent with the relations.
  FAIL: no admissible μ (not dihedral of modulus D), or a sector where no assignment works.
- T3 Ring-class test: for each Hecke prime p, the class of 𝔭 in Cl(O) (form class representing p). PASS (H4)
  for a system if λ_p is constant on primes with the same class and equals 2 on principal 𝔭; otherwise the
  system is a ray-class (not ring-class) character.
- Verdict per s: "all dihedral" if H2 holds (dim = lift span rank, certified both ways); "some dihedral" if only
  the lift-derived part is identified (s = 27, 29: 3 of 3 or 4); "none" if H3 fails in every sector.
- H5 PASS only if a closed count from T0/T3 data equals the certified dim at all of s = 9, 11, 23, 25 with no
  free parameter; it "decides" s = 27/29 only if it gives a value that, together with the proved bracket,
  is forced. Otherwise reported as FAIL / undecided.

## Categories
Cat A: proved statements or exact computations (integer, rational, mod-ℓ exact). Cat B: anything float.
A mod-ℓ match is reported as an exact mod-ℓ identity; it is not by itself a char-0 proof.
