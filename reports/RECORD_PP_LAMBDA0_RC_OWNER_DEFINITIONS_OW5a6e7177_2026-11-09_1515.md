# RECORD: PP, Λ₀ and R_c as Owner DEFINITIONS (not proofs). 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). This file is additive. I edited nothing. Tip 7cddb188… is untouched. No CERT was issued and nothing was sent outside.

## Authority (verified)
- OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md, sha256 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c. The sidecar MATCHES.
  - Owner verbatim: "As mine: adopt the 3:09 blueprint with your five corrections (Λ₀ and R_c as definitions, the 4-form T^(EH) term, the +1 law on a vector-valued carrier rather than 49a1, α still to be defined by me, nothing frozen) and send the go-aheads to Local, MR1, Non Local, MR2 and PP."
- **The 3:09 blueprint text itself (t4289u) is ABSENT from disk.** I searched quantum-comp/reports and audit-scratch for "t4289" and "blueprint" and found no file of it. The OW states the blueprint is "Gemini-style" and that "only this widget answer is the Owner's decision". The definitions below are therefore quoted from the OW's own "As adopted" section:
  - "Λ₀ := ln(6+√35)/√10 ≈ 0.7835772."
  - "R_c := κ ℓ_P, where κ = √(2/Λ₀) ≈ 1.597622."
  - "PP's DP-Rc (R_c = L_AdS/2) is not adopted."
- Consistent with OW 45aeba5f… (…AUDITOR_B11_B12_B13_B10_DECISIONS_1323): "B13-3 κ is defined as √(2/Λ₀) with Λ₀ = 0.783577 (≈1.597622), a definition not a proof; 1.595361 is unsourced and superseded."

## Recorded as Owner DEFINITIONS (no PROVED label attaches to these as derivations)
- **D-Λ₀.** Λ₀ := ln(6+√35)/√10 = 0.7835772176. This agrees with 45aeba5f's value 0.783577 to all 6 printed decimals; the blueprint form is the exact closed form.
- **D-κ.** κ := √(2/Λ₀).
- **D-Rc.** R_c := κ·ℓ_P, a length in Planck units.

## κ recomputed (PROVED, arithmetic, mpmath at 30 digits)
Script: /workspace/audit-scratch/pp_rc_def_1512/rc.py, log in rc.log.
| Λ₀ used | κ |
|---|---|
| Exact ln(6+√35)/√10 | **1.5976222** (1.59762224006…) |
| 0.783577 (45aeba5f) | 1.5976225 (1.59762246191…) |
- The two agree to 6 decimals (1.597622). They differ at the 7th digit because 0.783577 is a 6-digit truncation. Under the blueprint, the exact value 1.5976222 is the operative one.
- The superseded value is 1.595361 (unsourced, per 45aeba5f).

## PP's prior DERIVED PROPOSAL DP-Rc: NOT ADOPTED
- **Source 1.** FINDINGS_PP_DERIVE_RC_2026-11-09_1328.md (9ea1a7adfaca665258a0d1f892db17b0e63ecee84210118a623032475234346d), l.30: "DP-Rc. … Define Λ₀ := |scalar curvature of the 2D factor| = 8k². Then R_c := √(2/Λ₀) = ρ_H² = 1/(2k)" (that is, L_AdS/2).
- **Source 2.** FINDINGS_PP_DERIVE_ADS5S4SIGMA_PARAMETERS_2026-11-09_1357.md (4660b73edc32ceac2a01dcd59185d4d6d997fd93f8fd56455a380e7b055bfefa), D4: "PP's DP-Rc (R_c = ρ = L/2) stays a DERIVED PROPOSAL that does not reconcile with κ."
- **Source 3.** ADDENDUM 6be5f3d8… (1331) also lists it as not adopted.
- **Status now.** The Owner has explicitly **NOT ADOPTED** DP-Rc (OW 5a6e7177). It is withdrawn as a candidate definition. The Owner's definition R_c := κℓ_P replaces it.
- The consequences of the mismatch are derived in FINDINGS_PP_RC_KAPPA_VS_LADS_MISMATCH (same date).

## Still OPEN
- The physical meaning of Λ₀ outside F1–F3, beyond its definition. Supplying the unit ℓ_P closes the unit question *by definition*.
