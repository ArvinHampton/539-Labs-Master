# FINDINGS — Non Local Path — Round 2 questions on Owner Docs A/B — 2026-11-05
Internal protocol artifact. Additive to NL review 96f810645c6356c30b5edd2990da3f16657f866f56af22ff8cdbfe8a1007b0a6 (PRESS 2196a40505b90258c17607d120cafed02d93117655a8f35c0b610ec7f5bc8118).
Date: 2026-11-05 14:27 CST (America/Chicago). Category B. **No CERT.** invent HOLD. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 unchanged before and after.
Authority: in-scope continued review under the original Owner utterance the parent verified at transcript position 16394. The parent-relayed JSON /workspace/pqc-round-two-intake-20261105/parent-relayed-owner-authorization-and-routing.json (recorded 14:24:27 CST) is treated as **provenance only**, not independent authorization.

## Sources (documents[] in the JSON matches the files on disk; both read in full: A 9098 bytes, B 6140 bytes)
- Doc A: /workspace/quantum-comp/reports/OWNER_DOCUMENT_ANALYTICAL_REVIEW_AUDIT_RESPONSES_TWELVE_AGENT_COMPENDIUM_GAPS_2026-11-05.md, sha256 d5b1aae55e24e70290a6feb8c83f70b59cb1f68ea8183e280550bd6bfbadbfd3 (MATCH)
- Doc B: /workspace/quantum-comp/reports/OWNER_DOCUMENT_FORMAL_RESOLUTIONS_STRUCTURAL_CORRECTIONS_COMPENDIUM_2026-11-05.md, sha256 9c6f83da4f8636b0a6afbf108cbf7139210a82be936cadc94b772784451ded6d (MATCH)
- Also cited:
  - NL review c9bf12b4edbd358e1d13d72cad5234df9568e01cea61862a1615f186c25613ba
  - NL catalog 5b40ee12c9731d68e06a6b590229de49660c57813a901dcaed26d7ab2f4d2468
  - B1 erratum 8c06937d0cbcc2446288fb67cc63461b4456b9d42c03ac0b285ffe46cbe492ff
  - MR1 forensic bridges/PROFESSOR_PROOF/FINDINGS_MR1_SOFTSF_APPELL_LERCH_RC_15954_FORENSIC_HOLD_INVENT_2026-11-05.md 46beb56b0b9de8566a215db85668a5ffdc90e962ceee26458e271d4d57787bdb
  - reports/crypto/RPP_formal_statement/RPP_formal_statement.md 173c2c6661792613298011d7be1442b1db9fe88c7401914b8e3a277d65177dac

Statements are attributed to "NL" unless marked otherwise. A or B content is quoted as a claim, not adopted as fact.

## Prioritized questions and exact requests
**NL-R2-Q1 (B §I.1; A §1) Quasi-isometric embedding.**
- Request: give an explicit map F: V(T₃) → ℍ¹¹, the curvature normalization of ℍ¹¹, and constants λ ≥ 1, ε ≥ 0, with a proof that λ⁻¹d_T − ε ≤ d_H(F·,F·) ≤ λd_T + ε holds for all vertex pairs.
- Missing: everything. B states the inequality without F or constants.
- Also: does any "parameter-free" boundary survive, given that λ and ε are free?

**NL-R2-Q2 (A §1) Tripod proof precision.**
- A says that the geodesics "locally coincide … collapsing the embedding dimension to 1". Request: replace this with the exact contradiction.
- NL B2 (5b40ee12): for a scaled isometry φ with scale c > 0 and a center u with neighbors a, b, d, equality in the triangle inequality puts φ(u) on the unique geodesics [φa, φb] and [φa, φd] at distance c from φa. So the point at distance 2c from φa along each geodesic is the same point, which forces φb = φd, while d_T(b, d) = 2 requires d_H = 2c > 0.
- Question: will A adopt this statement, or supply its own proof?

**NL-R2-Q3 (A §2) Seed-2 arithmetic.**
- A lists the seed-2 orbit as "…122 → 367 → 1094". This is incorrect: 3·122 − 1 = 365, and A's own closed form, (3ⁿ⁺¹+1)/2, gives 365.
- Request: correct the term to 365. The term after it (1094) is then consistent.

**NL-R2-Q4 (B §II.2; A §2) Floor map convergence, extension, Haar.**
- (a) Request a proof, or a source path, that for every n ∈ ℕ with n ≥ 1, some k gives T3_refᵏ(n) ∈ {1, 2}.
  - Note that 0 is a fixed point.
  - The NL sweep (n < 2·10⁵, 400 steps) is evidence only. This is a Collatz-type statement.
  - Is a bounded k ≤ 539 claimed?
- (b) Define the claimed extension of the floor map to ℤ₃. Prove that it "preserves Haar measure", and state the claimed shift conjugacy exactly.

**NL-R2-Q5 (B §II.3) S_eff identification.**
- Request: the locked source path and hash that defines S_eff, and an exact statement that S_eff = 539 as an iteration budget.
- Also: does the 539 = 3^539 / 3^270 correction note (fbbac9a9…) bear on this?
- NL does not adopt the identification until this is supplied.

**NL-R2-Q6 (A §3; B §III) R_c provenance and re-grounding.**
- (a) A: the proximity √(2/0.7858) = 1.595361 (|Δ| ≈ 3.9e-5) is verified. Request the provenance showing that R_c was actually computed from Λ₀. Proximity does not prove circularity. MR1 lists 0.7858 only as a v16 Prop. 41.5 candidate.
- (b) B: request the operator whose "spectral radius" is meant, the explicit Appell–Lerch sum (parameters u, v, τ), the normalization, the units, and a computation reproducing 1.59543…
- (c) Request a uniqueness and parameter-independence argument.
- (d) Explain the 6.9e-5 gap between 1.59543 and √(2/0.7858).

**NL-R2-Q7 (B §I.2; A §1) Split and junction.**
- Request: the bulk metrics on each side and the hypersurface Σ with its induced metric γ_ij.
- Define "non-Archimedean Israel condition" (B gives none). The condition [K_ij] − γ_ij[K] = 0 means zero surface stress (S_ij = 0): is that assumed, or derived?
- Reconcile the original (4+1)⊕(5+1) split with B's (4+1) / (3+1) plus a "compactification ansatz", and specify that ansatz.
- Show the vacuum-term cancellation and how E_core is handled (inventory b2581c1a, gap 6).

**NL-R2-Q8 (A §6; B §V.2) 539.9 s marker.**
- A calls it a synthetic, pre-planted carrier for testing recovery scripts. B calls it a calibration parameter. Request: one consistent classification, with the source path and hash of the pipeline file.
- "VIRGO/LIGO (O5) null" audits: no evidence was located. The DF corpus name "VIRGO" refers to the SOHO solar instrument, not the gravitational-wave detector. The name coincidence is not GW evidence. Request the actual GW analysis source, or withdraw the claim.
- NL makes no empirical claim.

**NL-R2-Q9 (A §6 BH-core row) Row merging.**
- A ties "DISPROVED-FOR-LITERAL" curvature bounds to the supplied map. Request that these be separated:
  - The map disproof concerns termination only.
  - The absence of a curvature bound follows separately from NL B1 and erratum 8c06937d (g_rr coefficient undefined at D = 2GM; no curvature bound).

**NL-R2-Q10 (A §4–5; B §IV) Lane boundaries.**
- Request: the path and hash for the purge lock "96f8d42e…" (not verified by NL).
- Confirm that the SHA3-sandwich wording is a design statement, not a security proof. That belongs to the 539 Labs lane, and RPP 173c2c66 notes that Π_free is solvable.
- The ALU classification is a 539 Labs matter; NL takes no position.

## Completed vs proposed (from 96f81064)
- **Completed (elementary algebra and computation):**
  - ν₃(3x ± 1) = 0 algebra.
  - T3_ref(4880) hits {1,2} at step 14, and T^539(4880) = 2.
  - √(2/0.7858) arithmetic.
  - Seed sweep for n < 2·10⁵ (evidence only).
  - Seed-2 correction to 365.
  - Prior NL A1, A2, B1 (+ erratum) and B2.
- **Offers:**
  - O1 (embedding) is blocked until Q1 is answered.
  - O2 (R_c) is blocked until Q6(b) is answered.
  - O3 (floor-map termination) is partly done (computation only); a general proof is not attempted under invent HOLD.
  - O4 (Tate–Gelfand) is moot, since the claim was withdrawn in A §4.
- No new empirical work.

## Compliance
- No inventions.
- No adoption of source locks.
- No manuscript or config edits.
- No Gemini send, messages, publishing, or spending.
- No CERT.
- All prior files are preserved.
