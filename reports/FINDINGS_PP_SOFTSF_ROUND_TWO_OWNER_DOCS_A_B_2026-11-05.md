# FINDINGS: PP Soft SF round-two review of Owner docs A d5b1aae5… and B 9c6f83da… (2026-11-05, ~14:40 CST)
REPORTS ONLY. No CERT. tip untouched. invent HOLD STANDS. This is an independent review, not an endorsement. It reuses PP abea4b11…, 9f2368d6…, e2939293…, 4fe0c159… and dac95f2a….
Both docs MATCH. Authority JSON: parent-relayed (Physicist).

## A (analytical audit responses)
- A§1 tripod: the conclusion is correct, but the mechanism is stated loosely. The contradiction is φ(v₂) = φ(v₃) via geodesic continuation (PP abea4b11…), not "collapsing the embedding dimension to 1". The QI/bi-Lipschitz relaxation is correct.
  - PP STATEMENT: QI existence is standard. The specific F and (λ, ε) are ABSENT, and R_c is not linked to them.
- A§2 T₃^alt: the valuations ν₃(3x±1) = 0 are correct, the seed-1 orbit is correct, and the 3-adic limits −1/2 and +1/2 are correct.
  - **PP DEFECT A2-1:** the seed-2 orbit is listed as "122 → 367". PP recomputation gives 3·122 − 1 = **365**, consistent with the stated (3^{n+1}+1)/2. "1094" is correct as the next term.
  - The T3_ref facts (14 steps, T3^539(4880) = 2, S_eff capacity) are correct and match PP 9f2368d6….
- A§3: √(2/0.7858) = 1.595361 and the gap is < 4·10⁻⁵. Correct.
- A§4: the Haar fence is correct. A minor display slip: the identity is ∫|x|^{ν−1}dμ = (1−3⁻⁴)/(1−3^{−(ν+3)}), and A shows an integral sign before the closed form.
- A§5: these are Ops/Tier claims, not PP-audited proofs. Π_free inversion by division is stated, not proved here.
- A§6: **PP FLAG A6-1:** "VIRGO/LIGO gravitational-wave streams" is wrong for the DF record. DF's VIRGO is the SOHO solar irradiance instrument (per DF GR axis-2 a8f94cf0…, PP dac95f2a…), not GW. A6-2: "pre-planted synthetic carrier wave" is an unverified assertion. It needs a source path and hash.
- A closing questions 1–3 are the Owner's choices. PP has no recommendation beyond: 2 is documentary-safe; 1 and 3 need written definitions, with no invented derivations.

## B (formal resolutions)
- B I.1 QI: PROPOSED, not completed. No F and no (λ, ε) are given. Existence alone is standard.
- B I.2 junction: ABSENT proof, and the setup is internally inconsistent as written.
  - (a) A junction between a (4+1)-dimensional region and a (3+1)-dimensional sector cannot be a "9-core hypersurface". A hypersurface has codimension 1 in a single ambient manifold of fixed dimension.
  - (b) [K_ij] − γ_ij[K] = 0 is just the source-free (S_ij = 0) Israel condition, i.e. continuity of K_ij. It does not by itself give a "balance of cosmological terms".
  - (c) A "non-Archimedean Israel condition" is undefined.
  - PROOF REQUEST: the ambient manifold, the induced metric, the definition of K_ij in that setting, the action, and existence.
- B II.1 decommission: completed, correct, and consistent with Local/PP.
- B II.2 T3_ref: the formula is correct. The attached claims are PROPOSED or false:
  - **PP DEFECT B2-1:** "guarantees bounded convergence for all n∈ℕ to {1,2}" is false at n = 0, since T3(0) = 0 is a fixed point. For n ≥ 1 it is an unproved Collatz-type claim.
  - "Preserves Haar measures" and "ternary shift conjugacy" are UNDEFINED/unproved. T3_ref is defined on ℕ, and no extension to ℤ₃ is given.
- B II.3 S_eff: correct, and it matches Lock 96f8d42e….
- B III.1 R_c = 1.59543…: UNDERIVED. No Appell–Lerch sum, normalization, or "spectral radius" operator is written. The value is also not √(2/Λ₀) = 1.595361; the two differ at the 5th digit, so this is a new asserted number.
- B IV.1: **PP DEFECT B4-1:** "539-step T3_ref permutation loop" is false. T3_ref is not injective: T3(2) = T3(3) = 1. The SHA3 decoupling is otherwise consistent with A§5.
- B IV.2: completed and consistent with Ops.
- B V.1: correct as Tier E-UNTESTED.
- B V.2: same flag as A6-1. "VIRGO/LIGO O5 data audits" is not the DF dataset (SOHO VIRGO solar). No GW/O5 audit is on record.
- B VI: "locked into the ledger" and "submitted for final repository synchronization" are not effective. No OWNER_WRITE lock, adoption, or sync is on disk. The closing LaTeX and Layer2-config questions are the Owner's decision. PP will not act on them.

## Summary
- Completed: B II.1, II.3, IV.2, V.1.
- PROPOSED / ABSENT: B I.1, I.2, II.2 extras, III.1.
- Defects: A2-1 (367→365), B2-1 (n = 0), B4-1 (not a permutation).
- Flags: A6-1/B V.2 (VIRGO is solar, not GW), A6-2 (synthetic carrier needs a source).
Soft SF → Auditor Keeper; results → Physicist.
