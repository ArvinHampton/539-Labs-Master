# Soft SF FINDINGS — MR1 proof-logic review: B §III (Appell–Lerch → R_c)
Prepared 2026-11-05 ~16:06 CST (America/Chicago). Soft SF → Professor Proof (lead); copy Local. Owner 15:58: validation means the mathematics. Parent usage 77.1% (below 90% stop). No invention, no CERT, arithmetic only. tip LOCK `7cddb188…` untouched; invent HOLD.
Part (1) of PP's call (local.md + T3_ref correction) was already shipped as FINDINGS `829febd7…`; it is unchanged and not repeated here. Pack H / §6 QI is skipped (MR2 has it).

Source: B = `OWNER_DOCUMENT_FORMAL_RESOLUTIONS_STRUCTURAL_CORRECTIONS_COMPENDIUM_2026-11-05.md` sha `9c6f83da…`, §III.1 (lines 28–33). Prior MR1 forensic: `46beb56b…` (Appell→R_c ABSENT on disk; Prop. 41.5 residue 0.837679 is no match).

Status key: PASS · GAP (exact step) · FAIL (counterexample).

## S1. Diagnosis: R_c ≈ 1.5954 was circular via Λ₀ ≈ 0.7858, √(2/Λ₀) ≈ 1.595361
Arithmetic: √(2/0.7858) = 1.5953611. Describing it as circular (Λ₀ underived) is accurate. **PASS**

## S2. "R_c is the absolute spectral-radius bound from normalized Appell–Lerch boundary-sum evaluations matching the tree's asymptotic vertex growth"
Assumptions that are needed but not stated:
(a) which Appell–Lerch sum μ(u,v;τ) or A_ℓ(u,v;τ), with what parameters and τ;
(b) the normalization;
(c) what the "boundary sum" is and where it is evaluated;
(d) which operator's spectral radius is meant;
(e) how that is matched to vertex growth.
**GAP**: none of (a)–(e) is given, so the step can't be checked.
Consistency note, from standard facts and not invented: for the (p+1)=4-regular Bruhat–Tits tree of ℚ₃, the vertex growth rate is 3 and the adjacency spectral radius is 2√3 ≈ 3.4641 (Kesten). Neither is 1.5954, so any match needs an extra normalization, and that normalization is missing.

## S3. "Explicit evaluation yields R_c = 1.59543…"
- No evaluation is shown (no series, no truncation, no error bound). **GAP** at the evaluation step.
- Inconsistency: 1.59543 − √(2/Λ₀) = 6.9×10⁻⁵. That exceeds Owner C's stated tolerance of 4×10⁻⁵ (which was quoted for 1.5954). So B's new value isn't the Λ₀ value, and it isn't shown to be anything else. PP's prior finding stands: **1.59543 is underived and ≠ 1.595361.**

## S4. Conclusion: "independent of empirical vacuum scaling; resolves the underdetermination gap"
This depends on S2 and S3, which are both GAP. Not established. **GAP**. No counterexample is claimed, so this is not FAIL.
Superseded: Owner C §3 (`918f5c37…`) explicitly de-escalates R_c to Tier E, √(2/Λ₀), overriding B §III's "parameter-free" claim.

## Summary
PASS: S1. GAP: S2 (definitions a–e), S3 (no evaluation; value ≠ 1.595361 by 6.9×10⁻⁵), S4 (conclusion unsupported; superseded by Tier E). FAIL: none.
Net: the B §III re-grounding is **not a derivation**. R_c stays Tier E.
REPORTS ONLY. No CERT.
