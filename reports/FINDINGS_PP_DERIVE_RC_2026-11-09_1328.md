# FINDINGS — PP DERIVE item (1): R_c — 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). New additive file. No existing record edited. Tip 7cddb188… untouched. No CERT. Nothing sent outside.
Authority: OW 68a2b8e1f14e872204da8aed62f895f5bf3315ef1ccdc04d4f14c3d81c04c09e ("tell Professor Proof to pursue derivation"); OW 33d25a790fb1e0da5d93dc5cfb911963fa9a9a83c6dab6dfc8326c34096d7e15.
Locks read before use: LOCK 96f8d42e80c1975b4390fed950a4fb4b420088e6b19b2cbef8a44bebd28ff2ba (§4 purged Kronecker/four-force mappings — NOT used here); Λ₀ LOCK /workspace/reports/539labs/ow/OW_PP_picks_Lambda0_V35_Owner_LOCK_2026-11-03.md c290a274e7b31dc781cd2506a1fbd29a84a0af1f8b8a19adf1872a68432b36e3.
Steering input: Auditor batch 13 /workspace/quantum-comp/reports/bridges/AUDITOR/AUDITOR_CORPUS_CRAWL_BATCH13_OWNER_WRITE_1026C_1109_2026-11-09.md — sha re-hashed db0a69652f2b027e4fa39765ac2c3a8496c1d00cccb726b37802b0dacc10186d (MATCH db0a6965…).
Scripts/logs: /workspace/audit-scratch/pp_derive_1320/item1_rc.py, item1_rc.log (also geom.py, item3_metric.py for the proposal geometry).

## Rollup
PROVED 5 · CONDITIONAL 2 · OPEN 2 · REFUTED 0.
Verdict: **OPEN.** R_c cannot be derived from the model's own definitions, because no Owner record defines R_c or the Λ₀ that enters √(2/Λ₀). The missing input is identified exactly (§4).

## 0. Search confirmation (Auditor B13 §6)
- Searched 564 OWNER_WRITE* files (quantum-comp + /workspace/reports, excluding distributions/). Not one defines R_c. The case-insensitive hits for "R_c" are false matches inside sha strings and words. CONFIRMED.
- The only formula on disk is R_c = √(2/Λ₀) with Λ₀ ≈ 0.7858. It appears in OWNER_DOCUMENT_EXECUTION_PROTOCOL_ACTIVE_RESOLUTIONS_MATH_CORRECTIONS_2026-11-05.md (bridges/NONLOCAL_QM_EH11D, 918f5c37…, l.39), which is a Gemini-compendium-derived document that Soft SF de-escalated to a Tier E fit. The claim "parameter-free R_c ≈ 1.5954" comes from the Gemini compendium (references/gemini-compendium-2026-11-05/INTAKE_NOTE.md f1fab209…, l.18). Local L4 (892964f4…) and NL (96f81064…) both found it UNDERIVED. None of these sources is an Owner definition.

## 1. Both κ values (kept separate per B13-3, no choice made)
| label | definition | value (30-digit mpmath) |
|---|---|---|
| κ_rejected | √(2/0.7858); 0.7858 is rejected as an F1–F3 normalization by LOCK c290a274 | 1.595361053114… |
| κ_lock | √(2/Λ₀) with Λ₀ = ln(6+√35)/√10 = 0.783577217617… (per OW 4e5a39af2fca6b46…) | 1.597622240065… |
Gap: κ_lock − κ_rejected = 0.0022612. Rounding Λ₀ to 0.783577 gives 1.5976225; the exact Λ₀ gives 1.5976222. Both round to 1.597622. **PROVED (arithmetic).** Which κ is the source is Auditor item B13-3, which still awaits the Owner. This file does not choose.
Other values on disk: R_c = 1.5954 implies Λ₀ = 0.785762. Pack H's 1.59543590 implies Λ₀ = 0.785726. The lock's canonical invariant Res ζ_K = 0.837679 gives √(2/Res) = 1.545169, which matches neither. **PROVED (arithmetic).**

## 2. Lemmas
- **L1 (PROVED, sympy).** A round S² of radius a has scalar curvature 2/a². So R_c = √(2/Λ₀) holds exactly when Λ₀ is the scalar curvature of a round 2-sphere of radius R_c (for H² of radius ρ, use |R| = 2/ρ²). This is the only geometric reading of the √(2/·) form that the computations here support. It is an identity, not a derivation.
- **L2 (PROVED, scale no-go).** Under g → L²g, F₄ → L³F₄, Ric_MN and T_MN are both invariant (sympy check: Ric unchanged), so the classical 11D Einstein–four-form equations have a one-parameter scaling family of solutions. No dimensionful R_c follows from them. Only ratios do, unless an external scale is supplied, for example flux quantization in ℓ_p units or a stated unit for Λ₀.
- **L3 (PROVED).** Λ₀ is NONE for F1–F3 (LOCK c290a274 §1). No Owner record gives Λ₀ a value or a unit outside F1–F3 (Auditor B13 §6, confirmed). So √(2/Λ₀) is undefined from Owner records, and R_c is **OPEN (undefined ⇒ OPEN).**

## 3. DERIVED PROPOSAL (not Owner-adopted) and what follows from it
- **DP-Rc.** Take the 11D vacuum AdS₅ × S⁴ × H² (or a compact Σ_g quotient), which item (3) FINDINGS_PP_DERIVE_11D_METRIC derives. Define Λ₀ := |scalar curvature of the 2D factor| = 8k². Then R_c := √(2/Λ₀) = ρ_H² = 1/(2k).
- **Consequences (CONDITIONAL on DP-Rc and DP-metric).**
  - R_c/L_AdS = 1/2 exactly, and R_c/r_S⁴ = √(2/3) = 0.816497.
  - With flux quantization ∫_{S⁴}F = (2πℓ_p)³N and N = 4880, R_c = 20.2836 ℓ_p.
- **Comparison (PROVED, arithmetic).** None of the natural ratios {1/2, √(2/3), √(8/3) = 1.632993, √(3/2), 2} equals κ_rejected or κ_lock. The closest is L_AdS/r_S⁴ = 1.632993, which is off by +0.0376 and +0.0354. So DP-Rc does **not** reproduce 1.5954. This rules out only DP-Rc; it does not refute R_c.

## 4. Exact missing input (OPEN)
For R_c to be derivable, the Owner must supply all of the following:
1. **What Λ₀ denotes outside F1–F3**: which curvature or which invariant.
2. **The unit in which R_c is dimensionless**: ℓ_p, the AdS radius, the S⁴ radius, or something else. Without it, L2 forbids any numerical value.
3. **Which κ is the source** (B13-3): κ_rejected (0.7858) or κ_lock (ln(6+√35)/√10). The arithmetic link Λ₀ = ln ε/√10 is also open, because the √10 normalization is underived (OW 4e5a39af…).

## 5. Owner decisions needed
- **D-Rc-1.** Define Λ₀ (meaning and unit) outside F1–F3, or adopt or reject DP-Rc.
- **D-Rc-2.** Resolve B13-3, the source of κ: κ_rejected = 1.595361 or κ_lock = 1.597622. Both stay labeled until then.
