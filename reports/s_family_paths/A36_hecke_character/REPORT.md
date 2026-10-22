# A36: are the λ = 1/4 forms in S(ρ_s) Hecke-character (dihedral) forms?

**For:** Arvin Hampton (539 Labs) · 2026-10-22, America/Chicago (CDT).
`SF/` = `/workspace/quantum-comp/reports/s_family_paths/`. New files only, in `SF/A36_hecke_character/`.

**Ground rules.**
- CORE_FREEZE is respected: H_s is not redefined, no certifier code was touched or run, and the s31 mm sector was not touched.
- Jobs ran under `nice` with OMP_NUM_THREADS=1 and `ulimit -v` = 3 GB. Peak RSS was about 0.7 GB.
- Nothing was pushed or sent.

**Preregistration.** `prereg.md` was written before any computation. Its SHA-256 is
`4810c430cf50da096dc701f305d49f87dd397929151d030c971dca9383b3815b` (`prereg.sha256`), and it is unchanged.

**Categories.** Cat A means proved, or exact (integer, rational, or exact mod ℓ) relative to the named hypotheses. Cat B means numerical or post hoc. The two are kept apart below.

## Verdict per s

| s | K_s | Cl(O), O = Z[√n] | dim S(ρ_s) | forms identified as K_s-dihedral | verdict |
|---|---|---|---|---|---|
| 9 | Q(√7) | Z/2 | 1 | 1: a quadratic ray-class character | **all dihedral** |
| 11 | Q(√11) | Z/4 | 2 | 2: a ring-class character of order 4, and a ray-class character | **all dihedral** |
| 23 | Q(√483) | (Z/2)² | 3 | 3: quadratic ray-class characters | **all dihedral** |
| 25 | Q(√23) | Z/6 | 3 | 3: one ring-class character (order 3 or 6) and two ray-class characters | **all dihedral** |
| 27 | Q(√3) | Z/6 | 3 or 4 | 3: same pattern as s = 25 | **some dihedral** (3 forms); a possible 4th form is undetermined |
| 29 | Q(√87) | Z/6 | 3 or 4 | 3: same pattern as s = 25 | **some dihedral** (3 forms); a possible 4th form is undetermined |

Here "all dihedral" means that every form in S(ρ_s) is a linear combination of theta series θ_ψ of finite-order Hecke characters ψ of K_s with ψ ≠ ψ∘σ. These are the same kind of object as the Q(√6) form behind σ(q). However, none of the fields here is Q(√6).

## 1. Structural result (Cat A, relative to TB/TB4 and the classical Hecke–Maass theorem)

**Lemma.** Write Q(x) = x₁² + s x₁x₂ + (s/2)x₂², where n = s(s−2). Then Q(x) = N(x₁ + ωx₂), with ω = (s+√n)/2 in K_s = Q(√n).

**Why.** 2Q is primitive of discriminant 4n. So Λ = Z + Zω is an invertible ideal of the order O = Z[√n].

**Consequence for u.** Each component of the lift is
a_{α,β}(m) = ½ Σ_{ν∈α+Λ, Q(ν)=m, mod ε²} e(B(ν,β)),
where ε = (s−1)+√n. Every component of u is therefore a Hecke theta series of a function on D⁻¹Λ/Λ that is invariant under ε².
- For s = 9, …, 29, ε is the fundamental unit of O, of norm +1 (continued fraction, `out/classdata.json`).
- Expanding the weight function in characters of the group G₀ = I_D(O)/{(ν) : ν ≡ 1 mod D, N(ν) > 0} writes each component as a finite combination of θ_ψ(k·).
- The constraint "invariant along unit orbits, no |ν/ν′|^{it} factor" is exactly the condition for spectral parameter 0, that is λ = 1/4.
- Characters with ψ = ψ∘σ give Eisenstein series. Cusp parts involve only ψ ≠ ψ∘σ.

**Closure under the operations used.** P_σ is a constant matrix and T′_p (p ≡ 1 mod Tlevel) acts diagonally on θ_ψ, so the space of such combinations is preserved by both.

**Where the lower bounds come from.** At s = 9, 11, 23 and 25, every certified lower bound is built only from u:
- s = 9: u_cusp;
- s = 23: P_σu (the sector lemma);
- s = 11 and 25: P_σu and T′_pP_σu (`A9/certs/hecke_lower_s*.json`).

At each of these s the lower bound equals the certified upper bound. Hence S(ρ_s) is exactly the lift-derived span, and so (H2) S(ρ_s) is K_s-dihedral at s = 9, 11, 23 and 25.

**s = 27 and 29.** The three certified forms are dihedral by the same argument. A fourth form, if one exists, is not in the Hecke span of u (A34 §3.3), so nothing is known about it.

## 2. Exact class data, T0 (Cat A, unconditional)

**Method** (`scripts/classdata.py`, `out/classdata.json`):
- Gauss reduction cycles and composition give Cl(O).
- The continued fraction of √n gives the fundamental unit.
- (O/DO)^× is enumerated exhaustively.
- |G₀| = h·|(O/DO)^×| / |⟨−1, ε⟩ mod D|.

No PARI or GRH input is used.

| s | D | h⁺(4n) | h(4n) | wide Cl | ring-class cusp pairs (h − \|Cl[2]\|)/2 | \|(O/DO)^×\| | exp | \|G₀\| |
|---|---|---|---|---|---|---|---|---|
| 9 | 126 | 4 | 2 | Z/2 | 0 | 4536 | 126 | 36 |
| 11 | 198 | 8 | 4 | Z/4 | 1 | 11880 | 990 | 120 |
| 23 | 966 | 8 | 4 | (Z/2)² | 0 | 255024 | 10626 | 528 |
| 25 | 1150 | 12 | 6 | Z/6 | 2 | 506000 | 25300 | 1320 |
| 27 | 1350 | 12 | 6 | Z/6 | 2 | 486000 | 2700 | 1080 |
| 29 | 1566 | 12 | 6 | Z/6 | 2 | 789264 | 21924 | 1512 |

**Candidate pool.** The candidates are the characters of G₀ with ψ ≠ ψ∘σ, taken up to ψ ~ ψ∘σ. Their number is (|G₀| − |G₀^σ|)/2. I did not compute |G₀^σ|, so this pool size is not given exactly.

**Ring-class part.** The ring-class part of the pool is given exactly in the table. It does **not** match the dims (0, 1, 0, 2 against 1, 2, 3, 3). So the dims are not counted by ring-class characters alone, and ray-class characters of modulus dividing D are needed.

## 3. Exact Hecke eigenvalues, T1–T3 (Cat A as exact mod-ℓ identities)

**Method** (`scripts/hecke_modl.py`, `logs/run_s*.out`, `out/hecke_modl_s*.json`):
- The lift coefficients (from `A34/scripts/coeffsS.py`, imported read-only) are reduced exactly modulo a prime ℓ ≈ 10¹² with ℓ ≡ 1 mod lcm(D², phase denominators, E), where E = exp((O/DO)^×)·h.
- T′_p is computed for 8 split primes p ≡ 1 mod Tlevel.
- Rank-1 sectors without an Eisenstein part give λ_p directly.
- Rank-1 cusp sectors with an Eisenstein part, and rank-2 sectors, are solved using second-order coefficients a(p₀²m). In the rank-2 case the 2×2 matrix of T′_{p₀} was verified exactly on two extra columns at s = 25, 27 and 29.

**Test.** Is every λ_p of the form ζ + ζ⁻¹ with ζ^E = 1, i.e. a_p = ψ(𝔭) + ψ(𝔭̄)? The test is non-trivial: a random residue passes with probability about E/(2ℓ) ≤ 10⁻⁷ per prime.

**Results.** All 12 eigen-systems pass at all 8 primes. In the table, the entries are the orders of ψ(𝔭) prime by prime, and "cl" is the wide class of 𝔭 in Cl(O), where 0 is principal.

| s | sector | cl of 𝔭 (8 primes) | order of ψ(𝔭) | ring-class test (H4) |
|---|---|---|---|---|
| 9 | (3−,7−) | 0 0 0 0 0 0 0 0 | 2 2 2 2 2 2 2 1 | ray (λ = −2 at principal 𝔭) |
| 11 | (3+,11+) | 3 3 3 0 0 0 0 0 | 2 2 2 1 1 1 1 1 | **ring-class**, order-4 character (class 3 has order 2) |
| 11 | (3−,11−) | 3 3 3 0 0 0 0 0 | 4 4 4 2 2 1 2 2 | ray |
| 23 | (3+,7−,23−) | all 0 | 2 1 2 2 2 1 1 1 | ray, quadratic |
| 23 | (3−,7+,23−) | all 0 | 1 2 1 1 1 2 2 1 | ray, quadratic |
| 23 | (3−,7−,23+) | all 0 | 2 2 2 2 2 2 2 1 | ray, quadratic |
| 25 | (5+,23+) | 2 0 2 2 2 1 2 1 | 3 1 3 3 3 3 3 3 | **ring-class** (order 3 or 6) |
| 25 | (5−,23−) #1 | same | 6 2 6 3 3 6 6 6 | ray |
| 25 | (5−,23−) #2 | same | 2 2 2 1 1 2 2 2 | ray, quadratic |
| 27 | (3+,5+) | 3 3 0 4 4 3 3 3 | 3 3 1 3 3 3 3 3 | **ring-class** (order 3 or 6) |
| 27 | (3−,5−) #1 | same | 1 1 2 1 1 1 1 1 | ray, quadratic |
| 27 | (3−,5−) #2 | same | 3 3 2 3 3 3 3 3 | ray |
| 29 | (3+,29+) | 1 2 1 1 2 1 2 2 | 3 (all) | consistent with ring-class; there is no principal prime in the sample, so this is not a full test |
| 29 | (3−,29−) #1 | same | 1 1 1 1 1 1 1 2 | ray, quadratic (λ = −2 on a class of order 3) |
| 29 | (3−,29−) #2 | same | 3 3 3 3 3 3 3 6 | ray |

**Notes.**
- **What is exact.** Each λ_p is computed exactly mod ℓ. Its membership in {ζ + ζ⁻¹} is exact mod ℓ. Char-0 dihedrality itself comes from §1, and the mod-ℓ test is an independent exact consistency check of it.
- **Eigen-systems are distinct.** Within each s the systems differ, which matches the certified ranks.
- **s = 23 (Cat B observation).** The three quadratic systems multiply pointwise, ψ₁ψ₂ = ψ₃, on all 8 primes. They behave like the three non-trivial characters of a Klein four-group, as Cl(O_{4·483}) ≅ (Z/2)² does. They are not ring-class characters, however, since every one of these 𝔭 is principal.
- **Klein-four image.** The quadratic systems (s = 9, 23, and one each at 25, 27, 29) have a_p ∈ {±2, 0}, so their projective image is the Klein four-group. Such forms are dihedral with respect to three quadratic fields, and for even forms these fields are real. I did not identify the other two fields.
- **s = 25.** The second ring-class pair of Cl ≅ Z/6 does not occur in S(ρ_25). The 3 certified forms are the three systems above, and a form with the other ring-class system would be a fourth independent eigenform. (Its system agrees with the (5+,23+) one on the 8 sampled primes, so the sample cannot tell which of the two ring-class pairs is the one present.)

## 4. Class-number formula, H5

**Preregistered criterion: FAIL.** No count of characters derived from the data reproduces the dims. The visible systems split as (ring, ray) = (0,1), (1,1), (0,3), (1,2), and there is no derived rule for which ray-class characters land in ρ_s.

**Cat B, post hoc and not proved.** The empirical formula **dim S(ρ_s) = h(4n) − |Cl(4n)²| = h·(1 − 1/|Cl[2]|)** gives 1, 2, 3, 3 at s = 9, 11, 23, 25. This is exactly right at all four. It is A2's predictor, with the [2,2] case corrected: 4 − 1 = 3 at s = 23.
- At s = 27 and 29 it predicts 3, because Cl ≅ Z/6.
- It was fitted after seeing the data and has no derivation.
- It does **not** decide s = 27 or 29.

**Why s = 27 and 29 stay open.** Even a proved "all dihedral" formula would need the unknown fourth form to be dihedral too, and the lift's Hecke span cannot see that form.

## 5. What is not claimed
- Dihedrality of a hypothetical fourth form at s = 27 or 29, or that such a form exists or does not exist.
- Any statement about other real quadratic fields beyond K_s, apart from the Klein-four remark above.
- The exact size of the full candidate pool, since |G₀^σ| was not computed.
- No TPC/RH claims.

## Files (all new)
- `prereg.md`, `prereg.sha256`, `CHECKPOINT.md`
- `scripts/classdata.py`, `scripts/hecke_modl.py`
- `out/classdata.json`, `out/hecke_modl_s{9,11,23,25,27,29}.json`
- `logs/run_s*.out`, `logs/hecke_modl_s*.log`
- `REPORT.md`, `REPORT.html`, `REPORT.pdf`
