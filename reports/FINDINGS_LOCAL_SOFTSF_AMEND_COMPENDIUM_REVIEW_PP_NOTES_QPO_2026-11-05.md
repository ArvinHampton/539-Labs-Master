# FINDINGS — Local Soft SF AMEND + Q/P/O — compendium lane review — 2026-11-05
REPORTS ONLY. No CERT. tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 tip_touched NO. invent HOLD STANDS.
AMENDS: FINDINGS_LOCAL_SOFTSF_LANE_REVIEW_COMPENDIUM_S2_11DM2ET_3ADIC_2026-11-05.md (892964f4…).
PP Soft SF CONFIRM with notes: FINDINGS_PP_SOFTSF_AUDIT_LOCAL_COMPENDIUM_REVIEW_892964f4_2026-11-05.md (ddcf72ee…).
Source re-check: RECEIVED_COMPENDIUM.txt sha 49849cae20fe57c24533b770c13c4a53e5844f0bb75086250b9a82af0b446b73; PROVENANCE.md sha c6fea7d2….

## PP note absorption

### N1 / L1 restatement (source check)
Re-read RECEIVED_COMPENDIUM.txt line 26 under hash above. The piecewise formula is present in full ASCII form:
T₃(x) = { x/3 if x≡0 (mod 3); (3x+1)/3^{ν₃(3x+1)} if x≡1; (3x−1)/3^{ν₃(3x−1)} if x≡2 }.
Under that **literal** reading (not a guessed reconstruction), for every tested positive integer with residue ≠0 mod 3, ν₃(3x±1)=0, so T₃(x)=3x±1 and orbits diverge (e.g. x=1 → (3^{n+1}−1)/2). PP's "stripped numerators/exponents" note does not match the currently hashed file bytes; Local records that conflict. Either way the map is not T3_ref; HQCC as stated (universal bounded 539-step termination) is FALSE for this literal map; HQH hardness inherits the gap.

### N2 / L4
"Parameter-free" recorded as **author assertion**, not a validated Local claim. R_c≈1.5954 remains UNDERIVED on disk.

### L2 precision (Physicist request)
Metric assumptions for the impossibility claim:
- Domain: full geometric Bruhat–Tits tree of PGL₂(ℚ₃) as a metric graph with positive edge lengths (standard 4-regular tree), or at minimum any metric tree containing a tripod (three positive-length edges from one vertex).
- Target: ordinary real hyperbolic space ℍⁿ (n finite) with the usual Riemannian hyperbolic metric of constant negative curvature.
- Claim ruled out: an **isometric** embedding (distance-preserving on the whole tree metric).
- Argument: ℍⁿ is uniquely geodesic / CAT(−1); an isometric tripod forces the three geodesic rays from the branch image to coincide pairwise near that point, contradicting distinct positive leaf distances.
- Same obstruction for a **vertex-set** embedding that preserves **all** graph distances (center + three neighbors suffice).
- **Not** ruled out here: quasi-isometric embedding, bi-Lipschitz embedding of a restricted subset, or embedding into an ℝ-tree / ℍ^∞. Prior review parenthetical about ℍ^∞ is **RETRACTED** as unsupported; no automatic bi-Lipschitz restatement claimed.

## Local-numbered questions / proof requests / proof offers (Owner deliverable)

**Local-1 (embedding).** Q: Which tree and metric (full geometric tree vs vertices only; edge length; ordinary real ℍ¹¹ with what curvature)? Proof request: explicit F and distance identity, or QI constants. Completed: isometric tripod→ℍⁿ impossible under assumptions above. Offer: none for a specific QI embedding.

**Local-2 (R_c).** Q: Exact matching equation, Appell–Lerch inputs, domains, regularization, units, uniqueness, certified error. Status: UNDERIVED; "parameter-free" = author assertion. Offer: none until Written definitions.

**Local-3 (splitting).** Q: Direct sum / product / glue? Bilinear forms, signatures, junction/balance equation. Completed: only 5+6=11 arithmetic. Vacuum balance ABSENT. Offer: none without definitions.

**Local-4 (continuum / Tate–Gelfand).** Q: Define spaces, topology, limiting parameter, convergence theorem; relation to Bridge C A1→Ξ→RTA under Residual≠Resonant. Offer: none without definitions (same gap as CLOSE 3-adic BH b9747bfe… item 2).

**Local-5 (T₃ / HQCC).** Q: Confirm domain and literal T₃; supply HQCC theorem/target. Completed counterexample for literal map in hashed file; not a verdict on a different T3_ref. Cryptographic hardness not established by convergence alone. Offer: can re-supply the counterexample computation; not inventing a corrected map (invent HOLD).

**Local-6 (Haar completed).** Completed proof available: Haar item 70 on ℤ₃⁴, max-norm, Re ν>−3 → (1−3^{−4})/(1−3^{−(ν+3)}). FINDINGS 7ab0ed68…; DC AMEND 56e59a8e…; PP 965139fc…; Keeper 878b5308…. Identity-only; no BH/GR consequences. Offer = completed existing proof, not new research.

→ Soft SF PP re-audit of this AMEND then Keeper. Physicist already sent Q/P/O payload. tip untouched; No CERT.
