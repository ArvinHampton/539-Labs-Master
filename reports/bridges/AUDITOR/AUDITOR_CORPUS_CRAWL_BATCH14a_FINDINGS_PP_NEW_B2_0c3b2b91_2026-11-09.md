# AUDITOR: Corpus crawl BATCH 14a. New PP files since the batch-09 manifest, including PP 0c3b2b91 (B2), and the B2 Owner decision
Date: 2026-11-09, ~13:30 CST (America/Chicago). Lane: Auditor, audit-only.
Method: read-only. Hashes recomputed. Computations ran only in /tmp/aud14. No sidecars created, nothing edited or moved, no CERT, nothing external.
Tip re-hash: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
Labels: PROVED / CONDITIONAL / OPEN / REFUTED-by-proof.

## 1. Custody
| file | sha256 | sidecar |
|---|---|---|
| FINDINGS_PP_SOFTSF_AUDIT_LOCAL_B2_CONSTRUCTION_A_ADDENDUM_NL_ERRATUM_2026-11-09_1316.md | 0c3b2b9153b53a0fca6510fcc309495d947dc2ab17599a5d5116ed49112843af | MATCH |
| FINDINGS_PP_SOFTSF_AUDIT_NL_B2_CLOSURES_A_B_COMPARISON_2026-11-09_1309.md | f95223774c21222c9e8ca71dbf711fb1234f6fad69a553e32daf495c2245b0ce | MATCH |
| FINDINGS_PP_DERIVED_DEFS_D1_LAYER2_SEFF_T3_2026-11-09_1309.md | bd3730eb57a929a40eaed6547daac212b3f7baf468ce8b08b0bbe902d75a565b | MATCH |
| ERRATUM_PP_OWNER_PDF_1715_CHAIN_AUDITOR_BATCH8_2026-11-09_1311.md | 50f066b3faea6ec81c4ded397e245ea7087f83f350024bac5cdf04f423aad323 | MATCH |
| RECORD_PP_B2_CONDITIONAL_ON_ADOPTION_B_M_2026-11-09_1319.md | 09498bf7dc5ac428d5fd5efbacbbe8a9fb23c7e98c973f5ef238a29c0d7e9a38 | MATCH |
| RECORD_PP_B2_ADOPTION_B_M_VERIFIED_2026-11-09_1321.md | 09ea8de1de16d64d776d96d67b58a9c310bb0a23b927e9b86f1b29cc567262ce | MATCH |
| OWNER_WRITE_CALL_e9c1dbda_B2_ADOPT_M_AND_PP_DERIVE_AUTHORIZATION_2026-11-09_1320.md (decision source) | 68a2b8e1f14e872204da8aed62f895f5bf3315ef1ccdc04d4f14c3d81c04c09e | MATCH |
| /workspace/audit-scratch/pp_b2_local_1312/checks.py / checks_output.txt | 0a7d0a6e… / ad85b076… | n/a |

## 2. Owner decision on B2 (recorded)
- As relayed by Physicist, the Owner adopted B2 closure (B)-M, the Majorana pure swap on H⊗ℂ². B2 is recorded as CONDITIONAL on that choice.
- An on-disk source now exists: OW 68a2b8e1 §1 (:5). It quotes the 13:18 CST widget answer verbatim: "Adopt B2 closure (B)-M, the Majorana pure swap on H⊗ℂ², as mine. Record B2 as CONDITIONAL on this choice."
- PP record 09498bf7 states the scope correctly: uniqueness holds only on H⊗ℂ² with constant anti-diagonal U and m > 0, and P̂² = −1 is a HYPOTHESIS. PP record 09ea8de1 upgrades provenance to VERIFIED. The Auditor confirms that both records match the OW text.
- Auditor status:
  - **B2 = CONDITIONAL on (B)-M.** It is not PROVED unconditionally, and there is no CERT.
  - Adopting (B)-M also adopts two choices that are not derived: the re-read H₋ = H⊗e₂ (fibre rank 4, not the literal rank-8 H₊⊗ℂ²), and the Majorana class of γ⁰K.
  - Not adopted, but still valid: Local A3, the (A) unitary-ι swap, and (B)-D.
- OW 68a2b8e1 §2 (:9) also authorizes PP to derive R_c ("currently only a numerical fit at sqrt(2/Λ₀)"), the 11D map, the 11D metric and the Israel junction. That is an authorization only; no derivation has landed (see §5).

## 3. PP 0c3b2b91: internal correctness
Independent checks:
- **Re-run of PP's script.** /tmp copy of checks.py; output is byte-identical (sha ad85b076…).
- **Independent script (/tmp/aud14/mine.py), built with my own Majorana basis:**
  - Clifford relations hold.
  - η = γ⁰γ̄⁰ is −1 in the Majorana representation and +1 in the Dirac representation.
  - A₀H(p)A₀⁻¹ = −H(p) holds in the Majorana representation and fails in the Dirac representation.
  - S·S̄ = 1 for the permutation (1 2).
  - The identity A₀XA₀ = η·A₀XA₀⁻¹ holds.
- **By hand:** the Majorana-class iff of PP-1309:24 (γ⁰ᾱᵏγ⁰ = −αᵏ ⇔ γ̄ᵏ = −γᵏ, and γ⁰β̄γ⁰ = −β ⇔ γ̄⁰ = −γ⁰, for m > 0).

| 0c3b2b91 item (line) | Auditor label | note |
|---|---|---|
| §1 Q_ι² = η·diag(1, ιι*); general ι, scalar ⇔ unitary (:27–43) | PROVED | algebra re-derived |
| §2(a) sign rule B = εC⁻¹ = εη·A₀ι* (:48–53) | PROVED | |
| §2(b) Q_ι = S_ι·D with [S_ι, D] = 0 (:55–59) | PROVED | |
| §2(c) "P̂² = η·(a b̄)" (:62) | **REFUTED as stated (counterexample); corrected form PROVED** | U = [[0,a],[b,0]] gives P̂² = η·diag(a b̄, ā b), which is scalar iff a b̄ ∈ ℝ (= ±1). Counterexample: a = i, b = 1 gives diag(i, −i). PP-1309:18 (B-3) states this correctly. Every case used (σ_x, iσ_y, a = b, εη) has real a b̄, so **no verdict changes**. |
| §2 verdicts: NL-A A-4 REFUTED; CMP row REFUTED; P² = η·s in both closures (:68–78) | PROVED (counterexample U = iσ_y verified: P̂² = +1, fixed-t holds) | |
| §3 A3 = A₀⊗SK₃: properties 1–5; A3 = M ⊕ A₀\|_R (:83–97) | PROVED | Q² = η·SS̄ = η; QH_totQ⁻¹ = A₀HA₀⁻¹⊗1₃ |
| §3 "M only closure" unrestricted (:99–104) | REFUTED (counterexample A3), confirmed | |
| §3 uniqueness in scope, plus literal-forward extension (:105–116) | PROVED; non-literal forward map OPEN | U = [[0,εη],[1,0]] ⇒ P̂² = η·εη = ε |
| §4 finite-dimensional anti-diagonal P² = ±1 impossible; Eckart–Young ≥ √n (:120–131) | PROVED | rank(CB) ≤ n < 2n; for n = 4 the bound is 2, attained by the projector (recomputed) |
| §5 LA result 4 (:138–141) | PROVED, **scope note** | VV̄ = −1₃ is impossible (det argument). This rules out a tensor Kramers complement only when η = +1 (Dirac/chiral), which is the scope LA:24 states. In the Majorana representation, V = S gives Q² = −1 (that is A3). 0c3b2b91 omits the η = +1 scope. |
| §5 results 5–7, M/D bare-vs-pair (:142–155) | PROVED (result 7: existence only, intertwiner OPEN) | Hahn–Hellinger with uniform multiplicity ℵ₀; separable quaternionic structures are unique |
| §6 NLE E1–E4 CONFIRM; E5 REFUTED as stated (:158–168) | concur | |
| §7 PP-1309 errata E1–E4 (:170–175) | concur | the PP-1309:44 uniqueness-of-M claim is withdrawn |
| §8 four candidates, B2 not closed (:177–185) | concur; superseded by the Owner's adoption of candidate 1 | |

**Net for 0c3b2b91: internally correct.** There are two precision defects: the §2(c) formula needs a b̄ ∈ ℝ, and §5 result 4 needs the η = +1 scope. Neither changes any verdict.

## 4. Other new PP files
- **f9522377 (PP-1309).** B-3, the Majorana-class iff and A-5(ii) are re-verified (PROVED). Line 44 is withdrawn by its own erratum in 0c3b2b91 §7; the Auditor concurs.
- **bd3730eb (derived definitions DP-a / DP-b).**
  - a-L0 and a-L1 PROVED: λ = (0,1,1), the connecting map, H²(G) = H³(G) = 0.
  - a-1 to a-4 are CONDITIONAL on DP-a (a proposal, not adopted).
  - b-L0 recomputed, PROVED: 4880; 21; 4859 = 9·539 + 8; 29; W = 18; max O_res = 4863.
  - b-3 recomputed, PROVED: L(4880) = 14 with the orbit as stated; L(3^600) = 600.
  - b-5 recomputed: T3^539(4880) = 2 (CONDITIONAL on DP-b).
  - b-6 recomputed, PROVED: max L on n ≤ 10⁶ is 87, at 481780; on n ≤ 50000 it is 55, at 36043 and 36592.
  - b-9 recomputed: medians 21 and 28, mean 29.30, ln4880/ln1.5 = 20.95.
  - b-4 Lyapunov mean ln(2/3) PROVED.
  - a-5, the D1-norm → Kerr area transfer, is **OPEN**.
- **50f066b3 (PP erratum on Auditor B8).** It independently confirms B8-2, B8-3, B8-4 and C3-4.
  - χ₁₄₀ split/inert = 24/24; χ(13) = χ(9) = +1; 8007581 ≡ 1 (mod 140). All recomputed.
  - **Arithmetic slip at :35:** it writes "8007581 = 57200·140 + 1". The correct decomposition is 57197·140 + 1 (57200·140 + 1 = 8008001). The conclusion ≡ 1 is unaffected.
  - a_μ = 11659181×10⁻¹⁰ = 116591810×10⁻¹¹, the 2020 SM value. PROVED by digit match.

## 5. κ, R_c, junction, Layer2 transfer
- None of these six files defines κ = 1.595361 or R_c. OW 68a2b8e1:9 itself calls R_c "only a numerical fit at sqrt(2/Λ₀)". The κ/R_c bridge item stays OPEN/UNDERIVED.
- Israel junction: authorized for PP derivation, not derived. OPEN.
- Layer2 transfer: bd3730eb a-5 OPEN. DP-a gives "D1-norm" a referent only if the Owner adopts it.
- **Closable: none.** B8-2, B8-3 and B8-4 are now confirmed by PP; see the blockers in 14b.
