# PP-FINDINGS — Θ_p / Π_fast / pipeline v3 audit (2026-11-03)
REPORTS ONLY · No CERT · tip READ ONLY · messaged nobody.
Target: reports/OWNER_WRITE_THETA_P_PI_FAST_PIPELINE_V3_2026-11-03.md sha256 88410ea5551d39895468806de1975769fee875a3ab073008aac9484fa839f555 — sidecar MATCH.
Context: PP-FINDINGS-HECKE_ARITHMETIC_CORRECTION_AUDIT, PP-FINDINGS-CATA_FOOLPROOF_RERUN_OW9aec847a (Π_fast def from OW 9aec847a).
Script: scripts/theta_pi_fast_pipeline_v3_audit_2026-11-03.py (+ .out). Pipeline: 539labs/src/cern_539_pipeline.py 4f173950… (sidecar MATCH); no v3 file exists; cern_539_pipeline_v2.py is byte-identical. Pipeline not modified.

Note: the OW (15 lines) is a claim summary; it gives no formulas for ε_p, T_𝔭, π_𝔭, Λ, 𝕋, or the trace. It does not address any of the six failures; it restates them under "Physicist check".

## Physicist failures — independent verification
| # | Physicist failure | Verified? | Evidence | OW addresses? |
|---|---|---|---|---|
| 1 | ε_p "mod 35" collides for p>35; use (140/p) | CONFIRMED (refined) | For odd p, (35/p)=(140/p) exactly (4 is a square; 0 odd p<400 differ). Differ only at p=2: (35/2)=−1, (140/2)=0. (35/p) is periodic mod 140, NOT mod 35: e.g. 37≡2 (−1 vs 0), 73≡3, 83≡13, 227≡17 (mod 35) have different symbols. Reversed Jacobi (p/35)≠(35/p) at p≡3 mod 4 (11,19,23,31,43,…). | NO — "case table on listed primes" only; the formula is ABSENT, so what it computes can't be determined |
| 2 | Θ_p ∈ M₂(𝕋), so T̃_p leaves 𝕋 | CONFIRMED | M_𝔭=[[0,T],[πT,0]] ⇒ T̃_p ∈ M₂(𝕋⊗K_𝔭), not 𝕋. [M_𝔭,M_𝔮]=T_𝔭T_𝔮(π_𝔮−π_𝔭)·diag(1,−1) ≠0 ⇒ the family doesn't commute. M²=π_𝔭T²·I, eigenvalues ±T√π_𝔭 ⇒ needs √π_𝔭 (ramified extension), so no simultaneous eigenbasis over 𝕋 | NO |
| 3 | π_𝔭 ∉ ℚ₃ except p=3 | CONFIRMED | Uniformizer of K_𝔭, 𝔭|p: inert ⇒ p ∈ ℚ_p, v₃(p)=0 for p≠3 (a unit in ℚ₃, not a uniformizer); ramified 5,7 ⇒ √35 ∈ ℚ_p(√35); 35≡2 mod 3 is a non-residue, so √35∉ℚ₃. p=3 is inert, uniformizer 3 ∈ ℚ₃ ✓ | NO |
| 4 | U_t not unitary, M=3, t=1,2 | CONFIRMED | c=ζ^t−1=−1.5±0.866i; UU*=exp(−2 Im c·Λ); ‖UU*−I‖=4.7245 (Λ=diag(1,−1) and diag(1,0,−1)); unitary iff ζ^t=1 (t=0) | NO |
| 5 | Tr=128 underived | CONFIRMED | (Id−avg)∘ad, discrete t: Tr=−8 (n=2), −12 (n=3), −512 (n=16, M=3,5). Conjugation average: non-idempotent, non-integer trace (e.g. −1.18, 1.42). 128 = rank of the commutant projector only if Λ=diag(1⁸,−1⁸) (8²+8²); this isn't stated. Continuum ∫₀^{G₄}dt vs discrete t also unresolved | NO |
| 6 | Pipeline API | CONFIRMED | grep: api_url="https://cern.ch" (l.16), URL f"{api_url}/{id}"; line 50 calls harvest_real_open_data() and DISCARDS the return value; the fit uses np.random.poisson synthetic background (l.53–54). curl https://opendata.cern.ch/api/records/1 → 200 (single call). v3 is ABSENT; v2 is identical | NO — OW: "URL still https://cern.ch" |

## New OW claims
| Claim | Label |
|---|---|
| ε_p case table on listed primes | PARTIAL (correct only if (140/p); p=2 wrong under (35/p); no formula/list) |
| M_𝔭=[[0,T_𝔭],[π_𝔭T_𝔭,0]] | invented pending mathematical proof (2×2 over 𝕋; T_𝔭, π_𝔭 domain undefined) |
| Θ_p=(1−ε_p)M_𝔭; T̃_p ∈ 𝕋⊗ℚ₃ | FALSE (lands in M₂; π_𝔭∉ℚ₃; non-commuting) |
| Π_fast via conjugation average, U_t=exp(i(ζ^t−1)Λ) | FALSE as unitary conjugation (U_t non-unitary); Λ ABSENT |
| Π_fast is a projector (implicit) | FALSE (not idempotent numerically; prior audit: ad-form idempotent ⇔ 0) |
| Tr=128 | ABSENT derivation / invented pending mathematical proof |
| Pipeline v3 uses real data | FALSE (cern.ch URL; payload discarded; synthetic Poisson) |
| "unplanted background fit" | FALSE (background is generated in code) |

## Owner clarifications needed
1. ε_p formula: (140/p) Kronecker? Value at ramified 2,5,7? Explicit prime list.
2. Ring for T̃_p: 𝕋, M₂(𝕋), or 𝕋⊗K_𝔭? Which uniformizer for split primes (𝔭 not unique)?
3. Why ℚ₃: is a fixed embedding K_𝔭→ℂ_3 intended, or a single p=3 completion?
4. Λ (dimension, spectrum, Hermitian?); is ζ^t−1 to be replaced by a real phase (e.g. 2πt/M) to make U_t unitary?
5. Derivation of Tr=128: the space Π_fast acts on, its dimension, and discrete vs continuum t.
6. Pipeline v3 file location; switch to opendata.cern.ch/api/records/{id} and actually feed the payload into the fit.
