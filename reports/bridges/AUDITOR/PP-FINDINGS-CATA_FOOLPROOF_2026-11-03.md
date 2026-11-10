# PP-FINDINGS — Cat A foolproof check of 539_Labs_Technical_Corpus.md (2026-11-03)
REPORTS ONLY. No CERT. No tip fold. Video EXCLUDED. Messaged nobody.
Corpus: reports/539labs/539_Labs_Technical_Corpus.md sha256 5a8f863093c6eacb57a03b74b8c3906808111fbe43f6ba9677aebae4b8f17f9e (prefix 5a8f8630 MATCH).
Tip (READ ONLY): /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — see end for tip_touched.
Proof files this turn: PROOF_PI_FAST_IDEMPOTENT_2026-11-03.md, PROOF_WILSON_C1_CLOSED_FORM_2026-11-03.md, scripts/m3_counterexample_2026-11-03.py.

## Table
| # | Claim | Status | Corpus loc | Basis |
|---|---|---|---|---|
| 1 | det≠0 does not prevent cancellation (M=3) | PROVED; corpus ⇔ Lemma 5 C2 AGREE | §2.1 L24–27 | python: det 2, 36; W=0, N=2 |
| 2 | C ∉ V_35, polar bounds w/o cocycle vanishing | ABSENT (V_35, map C, "polar bounds" undefined) / invented pending mathematical proof; NF-WHY | §3.2 L44 | V_35 not on tip (tip uses dim V=42); P5b cocycle dim-1 is `[[ to prove ]]` |
| 2b | Hecke deformation; "T3 map" | Hecke deformation ABSENT (corpus+project); "T3 map" ABSENT in corpus, present elsewhere (raw dynamics, unrelated to C) | — | rg |
| 3 | Π_fast idempotent, spec {0,1} | General lemma PROVED; corpus Π_fast invented pending mathematical proof (Ad_{(ζ^t−1)∧} undefined) | §1.1 L8–11 | PROOF_PI_FAST_IDEMPOTENT |
| 4 | Wilson C1: (1+κ)^{-7/20} | FALSE under R_x const; corrected C1(μ)=C1(μ0)(μ/μ0)^{-(7/20)κ} PROVED under INVENTED assumption A1 | PROOF_22_TO_13 Phase 2 (not corpus) | PROOF_WILSON_C1_CLOSED_FORM |
| 5 | Audit Local FINDINGS 733db7de… F1–F6 | F1 FLAG(minor), F2 CONFIRM, F3 CONFIRM, F4 FLAG(minor), F5 CONFIRM, F6 CONFIRM; INTAKE sha FLAG | — | §5 |
| 5b | Audit Local F4–F6 FINDINGS 0a1c4add… | F4 CONFIRM (+minor FLAG: CX1 not Ad-type; CX2 supplied), F5 FLAG (FALSE only under stopping-time reading; ABSENT confirmed), F6 CONFIRM | — | §5b |
| 6 | Π_fast Cesàro Ad-average, Tr=128 (Codex §1.2) | Idempotent PROVED under invented H (T unitary, finite-dim); Tr=rank PROVED; 128 ABSENT (= Σm_i², T unspecified); conflicts with corpus §1.1 formula | Codex §1.2 | PROOF_CODEX_ITEMS_6_10 §6 |
| 7 | HQCC Φ/χ (Codex §2.1) | Defs PRESENT; theorem ABSENT; "convergence" FALSE: |Φ(x)|>|x| on 3-units, orbits →∞ | Codex §2.1 | §7 |
| 8 | Ω≡0 mod 539 | 539=7²·11 PROVED; W undefined ⇒ invented pending mathematical proof; as cancellation criterion FALSE (M=3: Ω=2); RTL tests mod 27 | Codex §2.1, §4.2 | §8 |
| 9 | det≢0 mod 3 ⇒ no collisions/cancellation | Inverse mod 3 PROVED; no-cancellation FALSE (h2'=−[0]+[1]+[2], dets 2,4, W=0,N=2); corpus h2 has det≡0 mod 3 | Codex §2.2 | §9 |
| 10 | BQP ⊂ C_HQH ⊂ NP-Complete | FALSE (∅∈BQP not NP-complete); repaired ⊆NP reading open/ABSENT (Raz–Tal oracle) | Codex §2.2 | §10 |

## 1. det≠0 vs cancellation — PROVED, AGREE
Quote (L24–27): "A non-vanishing matrix determinant ($\det \rho \neq 0$) does *not* prevent local or total state cancellations. For instance, given an odd modulus $M=3$ … $h_1 = [0] + [1]$ $h_2 = -[0] + [1] + 3[2]$ … total cancellation occurs yielding $W = 0$ while $N = 2$."
Proof: in ℤ[ℤ/3], h1·h2 = 2[0] + 0[1] + 4[2]. Residue 1 paths: (1,0): 1·(−1); (0,1): 1·1 ⇒ W=0, N=2. det ρ(h)=∏_k ĥ(k): det ρ(h1)=2·|1+ω|²=2; det ρ(h2)=36 (numeric, script). Matches PROOF_GROUP_RING_LEMMA5.md C2 exactly. Caveat: "total cancellation" is W=0 at target residue 1 only (other residues nonzero); Lemma 5 D labels the phrase invent-pending. Lemma 5 overall remains PARTIAL.

## 2. C outside V_35 — ABSENT / NF-WHY
Quote (L44): "The leading profile of the transfer element $C$ lies outside the primary space $V_{35}$, matching exact polar bounds without requiring unproven internal cocycle vanishing identities."
NF-WHY: no definition of C, V_35, the ambient space, or "polar bounds"; claim not precise enough to prove or refute. Comparison with Bridge C Written premises: tip uses dim V = 42 (L16, L41 "dim V = 42 = RTA Thm 11.6 Siegel-theta span"); no V_35 (rg 0 hits). Tip polar/cocycle language: L416 "P5b … residual cocycles modulo coboundaries … dimension 1. `[[ to prove / accepted ]]`"; L436 DMZ "polar part + Δ=0 normalisation … unique modulo J_{2,m}"; L522 P-W7.2 polar data W₇-compatible; L525 "W₇ cuts the obstruction / cocycle space to dimension ≤ 1"; L556 "Leading polar: fix one named polar / principal-part coefficient to 1"; L577, L622, L661 "Polar coeffs (Δ<0)". Tip's uniqueness route REQUIRES the cocycle-dimension statement (P5b, unproved) — so "without requiring cocycle vanishing" contradicts tip structure as Written (FALSE as a description of the tip; ABSENT as math).
Hecke: corpus 0 hits. Project: only literature (lit/1105.1918.txt Hecke operators/algebras) and scripts/mr2_h3_ps_lift.sage L3 hecke_polynomial/hecke_matrix. "Hecke deformation": 0 hits → ABSENT. "T3 map": corpus 0 hits (corpus has "$T_3 = 539$ stabilization" L5); elsewhere grok-files/new-HQCC-Theorem-Clarification-Topological-Derivation.txt L81,105; oct17-master/README.md L28; oct17-master/PAPERS.md L28; grok-chats/13-t3-vs-hqcc.md L1 — a Collatz-type local rule, unrelated to C/V_35.

## 3. Π_fast — lemma PROVED; corpus operator invented pending mathematical proof
Quote (L8–11): "idempotent projectry operator: $\Pi_{\text{fast}} = (\text{Id} - G_4^{-1} \int_0^{G_4} \cdot \, dt) \circ \text{Ad}_{(\zeta^t - 1) \wedge}$ … Spectrum: Formally bounded within $\{0, 1\}$."
P²=P ⇒ spec⊆{0,1}, diagonalizable (min poly | x(x−1)), orthogonal ⇔ self-adjoint: PROVED. Id−(time average) is idempotent: PROVED. Composition with Ad_{(ζ^t−1)∧}: undefined (ζ, ∧, domain); not idempotent in general (B=2Id counterexample). No definition in DEFINITIONS*.md/THEOREMS.md. Converse spec⊆{0,1} ⇒ idempotent is FALSE ([[0,1],[0,0]]).

## 4. Wilson C1 — corrected form under INVENTED A1
A1 (invented): one-loop, β=μ dC1/dμ = −(7/20)κ C1, R_x, x_11, T_c constant, no mixing. Then C1(μ)=C1(μ0)(μ/μ0)^{−(7/20)κ}; consistency verified by substitution. (1+κ)^{−7/20} is μ-independent ⇒ FALSE under A1. If R_x runs: C1(μ)=C1(μ0)exp(−(7/20)∫κ dlnμ); (1+κ*)^{−7/20} only if ∫κ dlnμ = ln(1+κ*), needing an unwritten R_x(μ): ABSENT. No physics CERT.

## 5. Audit — reports/FINDINGS_LOCAL_SOFTSF_CAT_A_FOOLPROOF_LIFT_539LABS_CORPUS_BRIDGE_C_2026-11-03.md
Hashes: FINDINGS 733db7de995eb20d9923bbcf02e765a7126e795d729a758ed4b2b5ea6ecea865 MATCH; PRESS d954d37146c9b7e31baa85937022cb3e05d1d07258fa3fdb5d9b9f63bc055de3 MATCH prefix d954d371. Cited input prefixes: THEOREMS 4535611a MATCH; PROOF_NP_HARDNESS c907b4db MATCH; LEMMA5 bf397de7 MATCH; INTAKE claimed d75a0a3a, actual 074f7032 → MISMATCH (file changed after citation or wrong cite).
| F | Local claim | PP-AUDIT | Note |
|---|---|---|---|
| F1 | READY (Thm A/B + Lem 5 E) | FLAG (minor) | Cites correct. Lemma 5 E covers M=2^k+1>Σ (and NO-instance M=5), C={0,1}, unit coeffs only; corpus's "odd prime or integer sequence" wording is broader — odd prime M ≤ Σ is NOT covered. Lift must restrict to E's hypotheses; general ℤ⁺/larger C slice-checkability is NF-WHY per E. |
| F2 | READY (Lem 5 C) | CONFIRM | Agrees with item 1. Add: "total cancellation" phrase invent-pending (Lem 5 D). |
| F3 | READY (Lem 5 B) | CONFIRM | Both corpus inequalities (incl. \|W\|≤∏spr ρ(h_i)) are in B. Not overstated; Local notes D invent-pending. Should also state Lemma 5 overall = PARTIAL. |
| F4 | NOT READY | FLAG (minor) | Conclusion consistent with item 3. Factual slip: says tubulin Π is "rank-13 on ℝ^22"; PROOF_22_TO_13 finds rank 8. Add that the general idempotent lemma is PROVED. |
| F5 | NOT READY | CONFIRM | "T_3=539" unsourced (PROOF_22_TO_13 Phase 2); not the T3 map. |
| F6 | NOT READY | CONFIRM | Consistent with item 2 (V_35 ABSENT; tip dim V=42; P5b `[[to prove]]`). |
PP-AUDIT F1: FLAG — restrict to Lemma 5 E hypotheses (M=2^k+1>Σ, C={0,1}, unit coeffs).
PP-AUDIT F2: CONFIRM.
PP-AUDIT F3: CONFIRM.
PP-AUDIT F4: FLAG — correct "rank-13" to rank 8; verdict NOT READY confirmed.
PP-AUDIT F5: CONFIRM.
PP-AUDIT F6: CONFIRM.
PP-AUDIT INTAKE cite: FLAG — d75a0a3a ≠ on-disk 074f7032.
Also: Local says "Kerr UNLOCKED"; consistent with LEAD_KERR_STATUS.md (Owner t64u) though PROOF_22_TO_13 (earlier) says BLOCKED — stale file, not an error in Local.

## 5b. Audit — Local F4–F6 (reports/FINDINGS_LOCAL_SOFTSF_CAT_A_FOOLPROOF_F4_F6_539LABS_BRIDGE_C_2026-11-03.md)
Hashes (all MATCH): FINDINGS 0a1c4add7648daea30937f17dc4c243cab0280fd44bcc73edc57bd8d85e9bfa6 (sidecar agrees); PRESS reports/PRESS_LOCAL_SOFTSF_CAT_A_FOOLPROOF_F4_F6_PP_THEN_KEEPER_2026-11-03.md 6331028e65069f92ce36640bb48343f943fba424f6acabe8997ae4a1db533ead; ACK FINDINGS reports/FINDINGS_LOCAL_SOFTSF_ACK_OW_8a0325da_CAT_A_FOOLPROOF_CONTINUE_2026-11-03.md 3617d03ec2e184d3e2cf784244f894166f07c005ccd665d2131ea2aa54ff9004; ACK PRESS reports/SOFTSF_PRESS_PP_LOCAL_ACK_OW_8a0325da_CAT_A_FOOLPROOF_CONTINUE_2026-11-03.md 023980dbb34f6fe3697a9892db929cd426c39461d1e41ff8dfe40472a172af36. Cited ADVANCEMENTS (nov-dec) d4ad9a72… and oct17 README 34d3c678… MATCH; L131 / L44 quotes verified.
- F4 PARTIAL. Re-ran CX1 (P=diag(0,1), A=2Id): (PA)²≠PA, eig {0,2} — reproduced. P0=Id−mean idempotent, σ={0,1}: agrees with my item 3. S1 (commuting case) agrees. FLAG (minor): A=2·Id is not an Ad (Ad_g(1)=1, unital), so CX1 refutes "composition of a projector with anything" but not the Ad-class. Supplied CX2 (scripts/f4_cx2_ad_model_2026-11-03.py): V=M_2(ℂ), P0 = Id − (projection onto span I), A=Ad_{diag(1,−1)}; A commutes with P0, yet P0A has eig {1,0,−1,−1}, not idempotent. So composite FALSE in general even within Ad-type, PROVED. Reconcile item 6: Codex Cesàro Π_fast is a different (invariant-part) projector, idempotent under invented H — Local F4 doesn't cover it; should note the two definitions conflict.
- F5 FALSE/ABSENT. ABSENT-with-rigor CONFIRM (no definition of "stabilization"; 539 on disk = hash budget 18+521). FLAG: "FALSE" holds only under the reading "539 = free T₃ stopping time"; the corpus line doesn't define which reading → label should be FALSE-under-reading / ABSENT. Reconcile items 7–8: Codex Φ has no stabilization at all (orbits diverge), and 539=7²·11 enters only as the Ω modulus, which is itself FALSE as a criterion.
- F6 ABSENT-with-rigor CONFIRM. Tip read-only check: 40 occurrences of V₄₂, no V_35/V₃x; dim Fix(S_lab⁻²)|_{V₄₂}=42 (L256); "35" in tip only as coefficient 35m² (L76). P5b (L416) and L525 cocycle statements `[[ to prove ]]` — agrees with item 2.
PP-AUDIT F4(Local F4–F6): CONFIRM (minor FLAG: add Ad-type CX2).
PP-AUDIT F5(Local F4–F6): FLAG — relabel FALSE→FALSE-under-reading; ABSENT CONFIRM.
PP-AUDIT F6(Local F4–F6): CONFIRM.

## 6–10. Codex addendum (sha 0183093491115f3c7928446eaa5d9c15a0b30bd32d09acdd7484a67799c1cc21, prefix MATCH)
See PROOF_CODEX_ITEMS_6_10_2026-11-03.md for full proofs/quotes. Quotes: §1.2 "Tr(Π_fast) = dim(H_invariant) = 128"; §2.1 "Ω(x) ≡ 0 (mod 539)"; §2.2 "det(M) ≢ 0 (mod 3) ⟹ ∃ M^{-1} (mod 3)" and "BQP ⊂ C_HQH ⊂ NP-Complete". Item 6 merges with item 3: the corpus and Codex give two inconsistent Π_fast definitions.

## Owner clarifications needed
1. Define C, V_35 (vs tip dim V=42), "polar bounds" — or rename V_35 to a tip object.
2. Define ζ, ∧, domain of Ad in Π_fast; G_4 as time scale.
3. Source of 7/20 and whether R_x runs (κ(μ)).
4. Corpus M "odd prime or integer sequence": confirm restriction to M=2^k+1>Σ.
5. Re-confirm INTAKE sha.
6. Pick ONE Π_fast definition; specify T, H (finite dim?) so Tr can be computed.
7. State the HQCC theorem conclusion (Φ diverges on ℤ as written).
8. Define W (winding number) and the intended Ω criterion; fix RTL width.
9. Replace complexity chain by a conditional statement (e.g. inversion ∈ FNP).
