# FINDINGS: PP, R_c = κℓ_P versus L_AdS/2 on the adopted AdS₅×S⁴×Σ_g proposal. 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file. Tip 7cddb188… untouched. No CERT. No outside service. Lock 96f8d42e honored: no four-force mapping is used.
Script and log: /workspace/audit-scratch/pp_rc_def_1512/rc.py and rc.log (mpmath at 30 digits; sympy for curvatures).

**Authority**
- OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c defines Λ₀ := ln(6+√35)/√10 and R_c := κℓ_P, with κ = √(2/Λ₀) = 1.5976222. It does not adopt DP-Rc.
- OW 7708ec5d1518e371540f7b37a51db1c014e36563c458181cf692b50124a0edd7 adopts AdS₅×S⁴×Σ_g as a CONDITIONAL proposal. Flux normalization, N and genus stay OPEN.
- Note that OW 5a6e7177 lists "N = 4880 and g = 2 as chosen inputs (not forced)" under Non Local O3, with standard flux normalization.

**Conventions (from 4660b73e / 4d07bd1b)**
- Metric: ds² = e^{−2ky}η + dy² + r²dΩ₄² + ρ²ds²(Σ_g), with G = 2√6k·vol(S⁴_r).
- Radii: **L_AdS = 1/k**, r = √6/(4k), ρ = 1/(2k). So L_AdS/2 = ρ.
- Curvatures (sympy):
  - S⁴ sectional curvature 8k²/3, Ricci eigenvalue 8k², scalar curvature 32k².
  - Σ_g Gauss curvature −4k², scalar curvature −8k².
  - AdS₅ sectional curvature −k², Ricci eigenvalue −4k², scalar curvature −20k².
  - Area(Σ_g) = π(g−1)/k².
- k(N) in the three normalizations:
  - STD: k = √(3/8)(πN)^{−1/3} ℓ_P⁻¹.
  - EH quantum (on this vacuum): k = √(3/8)(√2π²N)^{−1/3}.
  - EH's own lock: k³ = 25/(32π²N). This lock is REFUTED (4660b73e A3) and is listed for reference only.

## (a) The numerical gap at N = 4880 (PROVED, arithmetic)
| normalization | k [ℓ_P⁻¹] | L_AdS | L_AdS/2 | (L_AdS/2)/κ | r_S⁴/κ |
|---|---|---|---|---|---|
| STD (2πℓ_P)³N | 0.0246505 | 40.567128 | 20.283564 | **12.696095** | 15.549478 |
| EH quantum on this vacuum | 0.0149947 | 66.690282 | 33.345141 | **20.871731** | 25.562545 |
| EH own lock (REFUTED) | 0.0253138 | 39.504192 | 19.752096 | 12.363433 | 15.142051 |

R_c = κℓ_P = 1.5976 ℓ_P is about 12.7 times shorter than L_AdS/2 under STD normalization, and about 20.9 times shorter under the EH quantum. The value of R_c is on the order of ℓ_P, which is below the supergravity validity scale. Its meaning as an 11D supergravity length is therefore not controlled. This last point is CONDITIONAL, on the standard EFT-validity criterion that lengths must be ≫ ℓ_P.

## (b) Is R_c tied to L_AdS by the adopted equations?
**B1 (PROVED).** No adopted equation ties R_c to L_AdS. The adopted system consists of:
- the 11D Einstein–four-form equations with the adopted T^(EH) (OW 5a6e7177 NL O5);
- the AdS₅×S⁴×Σ_g ansatz;
- flux quantization ∫_{S⁴}G = Φ₀N.

None of these contains Λ₀, κ or R_c. They fix k as a function of (Φ₀, N) alone (4660b73e A4), and R_c is a fixed number times ℓ_P. So R_c/L_AdS = κ·k(N) is a free function of the OPEN inputs. Every N gives a consistent pair, and no constraint follows in either direction. The proof is by inspection of the equation set; see also 9ea1a7ad L2 (the scale no-go).

**B2 (PROVED).** The definitional pair is consistent with the vacuum for all N ≥ 1 and g ≥ 2. There is no contradiction, so nothing is REFUTED.

## (c) Hypothetical extra requirements (CONDITIONAL on an identification the Owner has NOT made)
Each requirement R_c = (a length) fixes k, and k then fixes N (rc.log):

| required identity | k [ℓ_P⁻¹] | N (STD) | N (EH quantum) | N (EH own) |
|---|---|---|---|---|
| R_c = L_AdS/2 = ρ_Σ (the Σ_g curvature radius) | 0.3129651 | 2.3846 | 0.5367 | 2.5823 |
| R_c = r_S⁴ | 0.3833024 | 1.2980 | 0.2922 | 1.4056 |
| R_c = L_AdS | 0.6259302 | 0.2981 | 0.0671 | 0.3228 |

**C1 (PROVED).** No case gives an integer N, so none is reachable under flux quantization (B1 of 4660b73e: N ∈ ℤ, N ≠ 0).

**C2 (PROVED).** Every case has N < 3. Even the nearest integer (N = 1 or 2) gives r = (πN)^{1/3}ℓ_P ≈ 1.5–1.8 ℓ_P, so the supergravity regime (N ≫ 1, r ≫ ℓ_P) breaks.

**Conclusion.** Imposing any of these identities would both clash with integrality and exit the supergravity regime. **REFUTED as a consistent supergravity identification, conditional on adopting it.** Since nobody has adopted it, the label is CONDITIONAL.

## (d) Does Λ₀ match any curvature of the metric? (PROVED, arithmetic)
Λ₀ = 2/κ² is the scalar curvature of a round S² of radius κ. Setting each curvature invariant c·k² equal to Λ₀ ℓ_P⁻² gives the following N:

| invariant (c) | N STD | N EH quantum | N EH own |
|---|---|---|---|
| S⁴ sectional (8/3) | 0.4589 | 0.1033 | 0.4970 |
| S⁴ Ricci eigenvalue (8) = Σ_g scalar curvature, absolute (8) | 2.3846 | 0.5367 | 2.5823 |
| great-S² ⊂ S⁴, 2/r² (16/3) | 1.2980 | 0.2922 | 1.4056 |
| S⁴ scalar (32) | 19.0765 | 4.2937 | 20.6582 |
| Σ_g Gauss curvature, absolute (4) = AdS₅ Ricci eigenvalue, absolute (4) | 0.8431 | 0.1898 | 0.9130 |
| AdS₅ sectional, absolute (1) | 0.1054 | 0.0237 | 0.1141 |
| AdS₅ scalar, absolute (20) | 9.4258 | 2.1216 | 10.2073 |

- **D1 (PROVED).** No invariant gives an integer N in any normalization. The largest N is 20.66 (EH own lock, S⁴ scalar), which is not ≫ 1 and not an integer. So Λ₀ is **not** a curvature of the vacuum at any admissible N. It is a separate quantity.
- **D2 (PROVED, ERRATUM to 4660b73e D3; additive, original file unchanged).**
  - 4660b73e lists "R_S⁴ = 24k²: N = 12.3906". With r = √6/(4k), the scalar curvature of S⁴ is 12/r² = **32k²** (sympy), giving N = 19.0765 (STD).
  - 24k² is not a curvature invariant of the S⁴ factor.
  - The same line labels 8k² as "K_S⁴". That value is the S⁴ **Ricci eigenvalue** (EH's K); the sectional curvature is 8k²/3.
  - D3's conclusion (no consistent identification) is unchanged.

## (e) Net verdict
- **E1 (PROVED).** The mismatch R_c = κℓ_P ≠ L_AdS/2 forces nothing. R_c is a separate, Owner-defined scale of order ℓ_P. The AdS vacuum scales are set only by (Φ₀, N), and the two are independent.
- **E2 (OPEN, unchanged).** The vacuum inputs remain OPEN as derivations: flux normalization, N and genus. STD normalization, N = 4880 and g = 2 are Owner-chosen inputs, not forced (OW 5a6e7177 NL O3).
- **E3 (CONDITIONAL).** Any future attempt to make R_c a vacuum length (ρ, r or L) or to make Λ₀ a vacuum curvature would require N = O(1) and a non-integer N. That is incompatible with the supergravity regime.
- **E4 (OPEN).** It is OPEN what physical role an ℓ_P-scale R_c plays in an 11D supergravity vacuum whose own lengths are about 40 ℓ_P. That role needs to be defined by the Owner.

## Rollup
- **PROVED 7:** (a), B1, B2, C1, C2, D1, D2/E1. D2 and E1 are counted as one item, the erratum.
- **CONDITIONAL 3:** the (a) sugra-validity remark, the (c) refutation-if-imposed, and E3.
- **OPEN 2:** E2 and E4.
- **REFUTED 0.**
