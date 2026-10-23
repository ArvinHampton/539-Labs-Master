# A37: a dimension count for the dihedral forms in S(ρ_s)

**For:** Arvin Hampton (539 Labs) · 2026-10-22, America/Chicago (CDT).
`SF/` = `/workspace/quantum-comp/reports/s_family_paths/`. New files only, in `SF/A37_dihedral_count/`.

**Preregistration.** `prereg.md` was written and hashed before any computation. Its SHA-256 is
`e0ba89527a572e2611317dae0a3b11198d63fca92869dfa163fae98f2dfd4fe0`, and the file is unchanged.

**Ground rules.**
- CORE_FREEZE is respected: no certifier code was touched or run, and H_s was not redefined.
- The s31 mm sector was not touched. No TPC/RH claims are made.
- Jobs ran under `nice` with OMP_NUM_THREADS=1 and `ulimit -v` = 3 GB. Peak RSS was about 0.7 GB per job.
- Nothing was pushed or sent.

**Categories.** Cat A means exact, or proved relative to TB, TB4 and TB5 (defined in prereg.md). Cat B means float or post hoc.

## Preregistered verdicts

| Question | Verdict |
|---|---|
| Q1: exact count of all characters landing in ρ_s | **Partial.** I computed an exact lower bound d_dih(s) from lattices in every ideal class of the principal genus, together with Hecke images (§2). Saturation over all ray classes of modulus dividing D is not proved, so this is not a complete enumeration. |
| Q2: count against proved dims at s = 9, 11, 23, 25 | **PASS** for the visible count: d_dih = dim at all four. This is forced by A36, since S(ρ_s) is the lift span there. The genus lifts add nothing, so there is no contradiction with the certified dims (control). A closed class-number formula is **not** derived (§3). |
| Q3: every form dihedral / s = 27, 29 | **Proof: FAIL.** No complete argument (trace formula, Galois, or Bessel span) was obtained (§4). For the s = 27 and 29 rank test, see §5. |
| Q4: further s | Not run, because no formula was proved. |

## 1. Construction: genus lifts (Cat A relative to TB5)

- **Setup.** Take a split prime p ≡ 1 mod lcm(2D², Tlevel) and a prime 𝔭 | p. Let Θ_𝔭 be the manuscript lift formula applied to the lattice Λ_𝔭 = {ξ ∈ Λ : ξ ∈ 𝔭 at p} with the form Q/p.
- **Same labels.** (Λ_𝔭, Q/p) has the same discriminant form, characteristic shift and labels as A_s, because p ≡ 1 mod 2D² and Λ_𝔭 agrees with Λ at every q | D.
- **Coefficients.** a^𝔭_{α,β}(m) = ½ Σ_{ν∈α+Λ, Q(ν)=pm, Dν∈𝔭} e(B(ν,β)), with ν taken modulo ε².
- **Which classes are reached.** Since p ≡ 1 mod 4n, every genus character is trivial at p. So the classes of 𝔭 lie exactly in the principal genus Cl(O)², and as 𝔭 varies they cover it. These are all the lattices 𝔞Λ with the discriminant form of ρ_s. Lattices in other genera have a different discriminant form and cannot carry ρ_s with these labels.
- **Covered classes.** Primes were chosen to cover every class of Cl²:
  - s = 9 and 23: Cl² = {0};
  - s = 11: Cl² = {0, class of order 2};
  - s = 25, 27 and 29: Cl² = the subgroup of order 3.
- **Script.** `scripts/genus_rank.py`. Exact ranks mod ℓ ≈ 10¹² over coefficient columns k/Tlevel with |k| ≤ KR. A mod-ℓ rank is a lower bound for the true rank. In sectors with an Eisenstein part, the cuspidal combinations Θ_𝔭 − F0 and T′_qF0 − 2F0 are used.

## 2. Results for s = 9, 11, 23, 25 (Cat A lower bounds)

| s | sector | rank(u, T′_q u) | + genus lifts Θ_𝔭, Θ_𝔭̄ | genus lifts alone | proved dim (sector) |
|---|---|---|---|---|---|
| 9 | (3−,7−) | 1 | 1 | 1 | 1 |
| 11 | (3+,11+) | 1 | 1 | 1 | 1 |
| 11 | (3−,11−) | 1 | 1 | 1 | 1 |
| 23 | three mixed sectors | 1 each | 1 each | 1 each | 1 each (total 3) |
| 25 | (5+,23+) | 1 | 1 | 1 | 1 |
| 25 | (5−,23−) | 1 (KR = 10) | 1 | 1 | 2 |

All other sectors have rank 0.

**Reading the table.**
- At s = 9, 11 and 23 the genus lifts lie in the span of u and its Hecke images. The dihedral count equals the proved dim, and it equals the A36 eigen-system count (s = 9: 1, s = 11: 1 ring + 1 ray, s = 23: 3 quadratic ray).
- **s = 25, (5−,23−) sector.** With |k| ≤ 10 the columns reach only rank 1. A36 needed |k| up to 16 to see rank 2. So this row is limited by column coverage, not a disagreement.
- **s = 25 control.** The genus lifts never exceeded the lift rank, so nothing contradicts the certified dim = 3. A KR = 16 control rerun at s = 25 was not done.
- Logs: `logs/run_s9.out`, `logs/run_s11.out`, `logs/kr6/` (s = 23 and 25 at KR = 6, s = 25 at KR = 10), and `out/genus_*.json`.

## 3. Formula status

- **What holds.** By A36 (lift span equals S(ρ_s) at s = 9, 11, 23, 25) and §2, the dihedral count equals dim S(ρ_s) at these four values. This is an identity of spaces, not a closed formula.
- **Ring-class part (exact).** The visible systems split as (ring, ray) = (0,1), (1,1), (0,3), (1,2), while the ring-class cusp pairs of Cl(O) are 0, 1, 0, 2. The ray-class part has no derived closed count.
- **Cat B, post hoc (A36).** The empirical formula dim = h(4n) − |Cl(4n)²| fits all four values and predicts 3 at s = 27 and 29. It is not derived, and the prereg excludes it as a stated formula.

## 4. Upper bound (Q3): why the proof attempt fails

The goal was to show that every λ = 1/4 form of type ρ_s is dihedral. The three routes considered each fail at a specific point:
- **Trace formula / Weyl law.** These give counts in eigenvalue windows. No exact multiplicity at the single eigenvalue λ = 1/4 follows (A17).
- **Galois route.** An even Maass form with λ = 1/4 is conjecturally attached to an even Artin representation. Even when it is, the representation can have tetrahedral, octahedral or icosahedral image, not only dihedral. No theorem excludes those types here.
- **Bessel-basis span.** "The K₀ Bessel space of A17 is spanned by lifts" would need exactly the missing upper bound.

So "all forms dihedral" is proved only where the certified upper bound equals the lift rank: s = 9, 11, 23, 25.

## 5. s = 27 and s = 29

<!-- S2729 -->
