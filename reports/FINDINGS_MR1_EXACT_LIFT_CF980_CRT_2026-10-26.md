# FINDINGS — MR1 Exact-lift coefficient field CF(980) + CRT p≡1 mod 980 (Rec A AUTO) — 2026-10-26 ~17:45 CDT (America/Chicago)
Soft-SF Write-only. Eight-only; no Eigen contact (Eigen files cite-only). No CSV edits. No invented coefficients. tip untouched.

## 1. STATUS
**PARTIAL.** PROVEN: (F1) ℚ(ζ₁₄₀)·ℚ(ζ₄₉)=ℚ(ζ₉₈₀), [ℚ(ζ₉₈₀):ℚ]=336; (F2) p splits completely in ℚ(ζ₉₈₀) ⇔ p≡1 mod 980 (p∤980); (F3) both on-disk mod-p primes (7840981, 1027606441) are ≡1 mod 980 — eligible. UNPROVEN+gap: G4a (ℚ(ζ₄₉) containment), G4b (height bound / number of CRT primes), G4c' (choice of prime above p — embedding-consistency across primes), G3a/G3b (off-mesh identification; char-0 basis). No cell promoted to exact.

## 2. Authority (live sha256, verified this run)
| Item | sha256 | Status |
|---|---|---|
| OW CF980 Rec A AUTO | ee3260468b890c8922274c1aa3bb4eec14c806032fc8814291b5061fce7bbb86 | MATCH |
| ASSIGN CF980 CRT | 01ade2a67fb1ee2c815c9d7a26255ace8736918db350a22b758821c9f9f002fa | MATCH |
| FINDINGS free-pursue | 67a1a1a3cf3c92c92cf7a242ffbc5d652df43494e802d6c3bde753a01664357f | MATCH |
| FINDINGS three-track PARTIAL | dac489f2fedf0cbf109fbd22a74593740dce13ad406983061c0fbb136e2f87b9 | MATCH |
| ζ₄₉ CRT GAP (EIGEN-TE-RHOBAR-Q89-ZETA49-CRT, cite-only) | 92e15d32703a1ec83d74fd801c70462c31c027c6bba519c9a1d73452de0eb1b9 | MATCH |
| Exact-lift PARTIAL (EIGEN-TE-RHOBAR-Q89-EXACT-LIFT, cite-only) | 40c2810da7995f54854bb088e220d87dca74ef2758775fee3fc35601151f2232 | on disk, MATCH prefix |
| SCOPE EIGHT | 203676c9e6118a5e19e843182940b1f94db873c7579510222f92c298eeb86187 | MATCH |
| Invent→proof standard | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 | MATCH |
| Schedule CSV TORD_N18 (read-only) | d3f12c981ec72b901ae7e97b76ac4a70c9cdd356ddda2eb5a721453d656f56f9 | MATCH |
| MODP_N18 CSV (read-only) | 9df646a935931fb70a523edf4e52190bbb08381fd24b51d8c4441873d827ccf3 | MATCH |
| MODP-N36 CSV (read-only) | 20c93d258f070bc5deefb8fcf26e869010332afc56884e3808a26d46b3619fa3 | MATCH |
| tip residual-c-field-WRITTEN_PREMISES_DRAFT.md pre=end | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | untouched |

## 3. Working field — PROOF
(a) ℚ(ζ_m)ℚ(ζ_n)=ℚ(ζ_lcm(m,n)), ℚ(ζ_m)∩ℚ(ζ_n)=ℚ(ζ_gcd(m,n)) (standard; Washington Prop. 2.4 / Gal(ℚ(ζ_N)/ℚ)≅(ℤ/N)^×). lcm(140,49)=980, gcd=7. Hence CF(140)·ℚ(ζ₄₉)=ℚ(ζ₉₈₀)=CF(980).
(b) 980=2²·5·7²; φ(980)=φ(4)φ(5)φ(49)=2·4·42=336. Check: [CF140]·[ℚ(ζ₄₉)]/[ℚ(ζ₇)]=48·42/6=336. ✓
(c) For p∤980, Frob_p ↦ p mod 980 in (ℤ/980)^×; p splits completely ⇔ Frob_p trivial ⇔ p≡1 mod 980. Then ℤ[ζ₉₈₀]/𝔭≅𝔽_p for each of 336 primes 𝔭|p, i.e. a ring hom ℤ[ζ₉₈₀]→𝔽_p sending ζ₉₈₀ to a chosen primitive 980th root of unity in 𝔽_p. ∎

## 4. On-disk CRT / mod-p prime inventory (read-only)
| Prime p | Used by | p mod 980 | p−1 factorization | Verdict |
|---|---|---|---|---|
| 7840981 | N36 ν=1,4,9,14,16 (5 FILLED-MODP cells; MODP-N36 + MODP_N18 + schedule) | 1 | 2²·3²·5·7³·127 | **OK for CF980** |
| 1027606441 | N6 ν=1,9 (2 FILLED-MODP cells); also tags VACUOUS/OPEN rows | 1 | 2³·3·5·7²·174763 | **OK for CF980** |
Count: **2 distinct primes ≡1 mod 980; 0 not.** 
Caveats: (i) one prime per cell — exact reconstruction needs ∏p > 2·H^? per G4b (height bound unknown); single 23–30-bit primes are certainly insufficient for generic ℤ[ζ₉₈₀] coefficients in a 336-dim ℤ-lattice. (ii) G4c': CSVs do not record which primitive 980th root of unity (prime 𝔭|p) was used; CRT across primes needs a compatible choice ζ ↦ ω_p. Unrecorded ⇒ GAP.

## 5. G4a — ℚ(ζ₄₉) containment OPEN
Not asserted. A proof would require: for each σ_a∈Gal(ℚ(ζ₉₈₀)/ℚ(ζ₄₉)) = {a∈(ℤ/980)^×: a≡1 mod 49} (order 8 ≅ (ℤ/4)^××(ℤ/5)^×), σ_a(c_ν)=c_ν for every coefficient of the 7 cells. Sufficient route: show the cusp-6 ρ̄ action restricted to the module is defined over ℚ(ζ₄₉) — i.e. the ρ₄⊗ρ₅ factor (Card1D, CF(140)) acts on the seed column through a ℚ-rational (or ℚ(ζ₇)-rational) basis, or that σ_a acting on the Weil-rep ρ₄⊗ρ₅ is realized by a module automorphism fixing the seed vector. Mod-p test (evidence only, not proof): at p≡1 mod 980, σ_a corresponds to ω_p↦ω_p^a; invariance ⇔ residues expressed in ω_p^{20} (order 49) only. Not run (would need the char-p basis in terms of ω_p; not recorded).

## 6. Off-mesh determination dependence on CF(980)
Per free-pursue P3 (existence PROVEN inside the 89-dim module; injectivity of q^18 truncation), off-mesh ν∈{21,25,29,81,109,121} are linear functionals of on-mesh data — over the coefficient field of the module. Under this OW that field is CF(980): determination over ℚ requires the truncation map injective over ℚ(ζ₉₈₀) (char-0), and mod-p determination at p≡1 mod 980 requires injectivity of the reduction (G3b, per prime). P4: ζ₄₉-only CRT (92e15d32, cite-only) may be insufficient until G4a. Values: none computed; cells remain OPEN-OFF-MESH.

## 7. HOLD (explicit)
The 7 FILLED-MODP cells (N36 ν=1,4,9,14,16; N6 ν=1,9) **stay FILLED-MODP**. No exact CSVs filled until an in-set CERT under CF(980) with eligible CRT primes (p≡1 mod 980, enough of them per G4b, compatible 𝔭-choice per G4c'). No Eigen.

## 8. Parallel
Mesh N>18 + W₇/slash Rec A AUTO ASSIGN continues in parallel; this pack does not rewrite it.

## 9. Posture; Rec A
Posture: PARTIAL; field arithmetic PROVEN; prime eligibility PROVEN for both on-disk primes; exact lift BLOCKED on G4b/G4c' (+G4a for ζ₄₉-only). tip_touched NO. Kerr BLOCKED.
**Rec A:** Owner Write (in-set MR1/Auditor) to set a Written height bound H (G4b) and fix a recorded primitive 980th root ω_p convention (G4c'), then generate additional p≡1 mod 980 mod-p runs in-set to reach ∏p > 2H for CERT of the 7 cells.
