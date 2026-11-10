# FINDINGS — Non Local Path — review of Owner documents "Analytical Review" and "Formal Resolutions" — 2026-11-05

Lane: Non Local Path (NONLOCAL_QM_EH11D). Internal protocol artifact. Reports only.
Date: 2026-11-05 14:23 CST (America/Chicago).
Category B. **No CERT.** invent HOLD stands. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 unchanged before and after.

## 1. Inputs (hashes computed now)
| File | sha256 |
|---|---|
| reports/OWNER_DOCUMENT_ANALYTICAL_REVIEW_AUDIT_RESPONSES_TWELVE_AGENT_COMPENDIUM_GAPS_2026-11-05.md (Doc A) | d5b1aae55e24e70290a6feb8c83f70b59cb1f68ea8183e280550bd6bfbadbfd3 (matches expected d5b1aae5…) |
| reports/OWNER_DOCUMENT_FORMAL_RESOLUTIONS_STRUCTURAL_CORRECTIONS_COMPENDIUM_2026-11-05.md (Doc B) | 9c6f83da4f8636b0a6afbf108cbf7139210a82be936cadc94b772784451ded6d (matches expected 9c6f83da…) |
| Prior NL compendium review | c9bf12b4edbd358e1d13d72cad5234df9568e01cea61862a1615f186c25613ba |
| Prior NL catalog | 5b40ee12c9731d68e06a6b590229de49660c57813a901dcaed26d7ab2f4d2468 |
| Canonical B1 erratum | 8c06937d0cbcc2446288fb67cc63461b4456b9d42c03ac0b285ffe46cbe492ff |
| MR1 R_c forensic (bridges/PROFESSOR_PROOF/FINDINGS_MR1_SOFTSF_APPELL_LERCH_RC_15954_FORENSIC_HOLD_INVENT_2026-11-05.md) | 46beb56b0b9de8566a215db85668a5ffdc90e962ceee26458e271d4d57787bdb |

I treat the mathematical content of Docs A and B as data to check, not as verified truth or as authority. Their status language ("locked", "definitive", "permanently logged") changes no lock.

## 2. Checks run on the box (this turn)
- **Supplied-map algebra (Doc A §2):** x = 3k+1 ⇒ 3x+1 = 9k+4 ≡ 1, and x = 3k+2 ⇒ 3x−1 = 9k+5 ≡ 2. This matches NL c9bf12b4 §3. Correct.
  - Doc A lists the seed-2 orbit as "2 → 5 → 14 → 41 → 122 → 367 → 1094". The term **367 is an arithmetic error**: 3·122 − 1 = 365. The closed form it gives, (3ⁿ⁺¹+1)/2, yields 365.
- **T3_ref(4880) (Doc A §2):** the orbit is 4880, 3253, 4338, 1446, 482, 321, 107, 71, 47, 31, 42, 14, 9, 3, 1, 2, 1, … It first hits {1,2} after 14 steps, and T3_ref^539(4880) = 2. Both claims are **verified**. Also T(1) = 2 and T(2) = 1.
- **"Guarantees bounded integer convergence to {1,2}" (Doc B §II.2):** **not proved.** No proof is given in Doc B, and none was located. Empirically, every seed 1 ≤ n < 200000 reaches {1,2} within 400 steps. That is evidence only; it is a Collatz-type statement and stays conjectural. Note also that 0 is a fixed point (T(0) = 0). Doc B's further claims that the floor map "preserves Haar measures" and "matches ternary shift conjugacy" come with no definition of the extension to ℤ₃ and no proof: **unsupported**.
- **√(2/0.7858) (Doc A §3):** = 1.595361…, and |√(2/0.7858) − 1.5954| ≈ 3.9 × 10⁻⁵. The arithmetic is **verified**. MR1 forensic 46beb56b lists 0.7858 as an RTA v16 Prop. 41.5 candidate value. A numerical proximity does not establish that R_c was derived from Λ₀; the provenance is **unestablished**, so the circularity is plausible but not proved.
- **R_c = 1.59543… (Doc B §III):** **no derivation evidence.** It names no Appell–Lerch sum, no parameters, no normalization, and no "spectral radius" operator. It also differs from √(2/0.7858) by about 6.9 × 10⁻⁵. MR1 46beb56b records the project Appell–Lerch → R_c derivation as ABSENT. Renaming is not a derivation; O2 is still blocked.

## 3. Claim-by-claim classification
| Item | Doc text | Classification |
|---|---|---|
| Literal isometry | "formally retracted" (B §I.1); tripod obstruction (A §1) | **Withdrawn false claim.** Consistent with NL B2 (5b40ee12). A's sketch phrase "collapsing the embedding dimension to 1" is loose: the actual contradiction is φb = φc vs distance 2λ, and NL B2 gives the precise proof |
| Quasi-isometric embedding | "(λ, ε)-quasi-isometric embedding … established" (B §I.1) | **Corrected wording, not a proof.** No map F, no λ or ε, no target metric normalization. Some quasi-isometric embedding of a regular tree into ℍⁿ is plausible via known literature, but none is given or cited here, and λ and ε being unspecified removes any "parameter-free" boundary (as A §1 itself notes) |
| Split / junction | "(4+1)D −U … 9-core hypersurface … (3+1)D +U … [K_ij] − γ_ij[K] = 0" (B §I.2) | **Still missing.** No metric, no definition of a "non-Archimedean Israel condition", no surface stress tensor, no compactification. Setting the jump to zero is an assumption, not a derivation. The dimension count has also changed (4+1 with 3+1 plus "remaining dimensions"), unexplained relative to the original 4+1 / 5+1 |
| T₃^alt | "permanently decommissioned" (B §II.1) | **Withdrawn false claim.** Matches NL c9bf12b4 |
| T3_ref standard | floor map n//3, (4n+2)//3, (2n+1)//3 (B §II.2) | **Provided definition**, consistent with the corpus (HQCC Clarification 4d11b7a6…; RPP formal statement 173c2c66…). The convergence guarantee is conjectural (see §2) |
| 539 = S_eff / fixed budget | "fixed, frozen capacity allocation index (S_eff) … step budget" (B §II.3) | **Corrected wording**, consistent with Residual ≠ Resonant: 539 is a fixed iteration budget, not a stopping time or physical clock. Whether S_eff, as locked elsewhere, *equals* 539 was not checked here (D1/S_eff definitions not located in prior bounded passes). I do not adopt the identification |
| R_c | Λ₀ circularity (A §3); re-grounding (B §III) | A: arithmetic verified, provenance unestablished. B: **still missing evidence**. No derivation; uniqueness and independence are asserted only |
| Tate–Gelfand | no such theorem on disk (A §4) | **Corrected wording**, consistent with NL C7 and inventory gap 3 |
| Kronecker / force projections | "PURGED … lock 96f8d42e" (A §4) | Lock reference noted; I did not verify the lock file this pass. Status stays **undefined / Category B** |
| HQH security | SHA3-sandwich basis (A §5, B §IV.1) | **Corrected wording only; not a security proof.** Consistent with RPP 173c2c66 R2/R3 (the T₃ layer adds no hardness to Π_dig; Π_free is solved by 3^L·y). Security belongs to the 539 Labs lane, out of NL scope |
| 128-trit ALU | classical Verilator simulation (A §5, B §IV.2) | **Lane boundary:** 539 Labs. Not reviewed by NL |
| 539.9 s / LIGO-Virgo | "synthetic carrier … null signature" (A §6); "calibration parameter … O5 audits null" (B §V.2) | **No empirical claim adopted.** The two documents describe it differently (A: a pre-planted synthetic test carrier; B: a calibration parameter). The cited LIGO/Virgo "O5" audits are not located or verified here. Tier E stays separate; I make no falsification claim |
| A's "DISPROVED-FOR-LITERAL" BH-core row | ties a curvature bound to the supplied map | **Imprecise.** The disproof concerns the map's termination claim. NL B1 + erratum 8c06937d separately shows that no curvature bound follows from the regulator; the two should not be merged |

## 4. Row verdicts for NL-Q1–Q10 (from c9bf12b4)
| Q | Verdict after Docs A/B |
|---|---|
| NL-Q1 embedding | **Partially answered.** Literal isometry withdrawn. A quasi-isometric reading is stated, but no F, λ, ε, or metric is given. **Open** |
| NL-Q2 11D / split / vacuum | **Open.** The decomposition changed; there is no metric and no cancellation computation |
| NL-Q3 junction | **Open.** [K_ij] − γ_ij[K] = 0 is asserted, not derived. No E_core treatment (inventory gap 6) |
| NL-Q4 Kummer | **Withdrawn / purged** per A §4 (lock unverified here). No definition given. **Closed as withdrawn**, pending lock check |
| NL-Q5 curvature tensor / forces | **Withdrawn / purged** per A §4. Inventory gap 1 is **open** |
| NL-Q6 Tate–Gelfand continuum | **Withdrawn** as a theorem (A §4). The continuum limit (gap 3) is **open** |
| NL-Q7 singularity bound | **Open.** Docs do not supply a field equation. NL A1 / B1 (+ erratum) stand |
| NL-Q8 HQCC map / termination | **Answered as definition:** T3_ref is the map, and 539 is a fixed budget. The termination/convergence guarantee is **conjectural** (no proof; empirical evidence only) |
| NL-Q9 R_c derivation | **Open.** No Appell–Lerch sum or normalization is supplied. The Λ₀ proximity is verified only numerically |
| NL-Q10 falsification rows | **Open / absent.** Reclassified as prospective Tier E; no quantitative rows |

## 5. Offers O1–O4
- **O1 (verify embedding):** **blocked.** No F, λ, or ε supplied.
- **O2 (reproduce R_c):** **blocked.** No sum or parameters. The only executable piece, √(2/0.7858), is done above.
- **O3 (check the termination notion against T3_ref):** **partially executable and executed.** The map is now fixed. The 4880 claim is verified, and the bounded sweep n < 2·10⁵ is evidence. A general proof is outside any existing source, and under invent HOLD none is attempted.
- **O4 (Tate–Gelfand comparison):** **moot.** The claim is withdrawn; the Local Haar item 70 identity stands on its own.

## 6. Resolved vs remaining
- Resolved by withdrawal or correction: literal isometry; T₃^alt; 539 as stopping time; Tate–Gelfand theorem; HQH security wording; ALU classification.
- Verified this turn: the T3_ref(4880) figures and √(2/0.7858).
- Errors found in the Docs: Doc A's seed-2 orbit term 367 (should be 365); Doc B's unproved convergence guarantee and Haar/conjugacy claims; Doc B's R_c "re-grounding" without evidence; inconsistent descriptions of the 539.9 s marker.
- Remaining: NL-Q1 (quasi-isometric constants), Q2, Q3, Q7, Q9, Q10; inventory gaps 1–6 (b2581c1a); O1 and O2 blocked.

## 7. Compliance
No inventions, proofs beyond elementary checks, CERT, publishing, spending, or messages. All prior files are preserved unchanged. Next: PP audit, then Keeper (parent handles the handoff).
