# FINDINGS — Eigen lane: loosen Category B (11D ↔ ternary merger) — 2026-11-05 ~12:15 CST America/Chicago
**ACK: OW `ae380bf6c09980ec0a88dabbb02347a873b672f2b62b7f68fba2d5ddec9b30fa` MATCH** (OWNER_WRITE_CALL_9ee0f248_LOOSEN_CAT_B_11D_TERNARY_MERGER_2026-11-05.md, re-hashed this turn).
tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER (see footer) — tip_touched **NO**. **No CERT.** REPORTS ONLY, no RECS. No invented proofs/coefficients/roots/Kr QQ/ν. Nothing sent.
Scope: eigen / spectral / matrix / ρ̄ / modular-representation compute + residual-algebra (residual ternary / circulant group-ring ℤ[ℤ/3]) claims per parent scope addendum.

## Sources (sha256 verified this turn)
- S1 grok-batches/FINDINGS_EIGEN_CAT_A_FOOLPROOF_539_CORPUS_S21_2026-11-03.md — 755ec7124c17cc15ff309ad6b6371eecf7c9b78cca9cb4daaf17b2eabffcdbd8
- S2 grok-batches/FINDINGS_EIGEN_CAT_A_FOLD_LABS539_CORE_REPORTS_ONLY_2026-11-03.md — 29b6f6e266e63f48b57eb4a1c532211a34a43ee7ad8ceb3265b39158df1ef9bf
- S3 grok-batches/EIGEN-TE-RHOBAR-N36-CRT36Z-NAMED-GAP-DIAG_2026-10-27.md — eca390848dac11223bc553ea7431443b1f190b9435b5b5134ed5877470b1179d
- S4 grok-batches/EIGEN-TE-RHOBAR-N36-E1-P7952701-MATCH_2026-10-27.md — 9cac9a3983eb5960dfd429dcd671515e2ce775804669e92b0177df95b6b589d2
- S5 grok-batches/EIGEN-TE-RHOBAR-Q89-ZETA49-SOLVE42G-COMPLETE_42of42_2026-10-27.md — d4aa7ea1e78d913b274cc07b1294fa706708fb332937bc5c199a8b42b5b25d1c
- S6 quantum-comp/reports/FINDINGS_LOCAL_SOFTSF_AMEND_FILTERED_PROVABLE_MATH_X_DENSE_2026-11-05.md — c57556545032be55772a96e0886d35cb8ed33e16f6ce375c23c6363a691301c9
- S7 quantum-comp/reports/bridges/AUDITOR/FINDINGS_AUDITOR_SOFTSF_CONFIRM_PP_REAUDIT_LOCAL_ABSORB_0a4ddb32_2026-11-05.md — 531762193aaadd786a49db73926572feefeebe8264f3f12ddfb8d6ba12f7c388
- S8 quantum-comp/reports/bridges/AUDITOR/FINDINGS_AUDITOR_SOFTSF_CONFIRM_RTA_FOUNDATION_BOUND_v16_2026-11-05.md — 012c2e3c433e9d8f5a093e6628230c3c7bede69596f23d69c756e74f3b7b6e72 (hash-only confirm; content not evaluated by Auditor or here)
- S9 grok-batches/eigen-cata-foolproof-2026-11-03/compute.log — 68549e9ed004e5ec021c8ec9b59717a41092b15e51decf5a68e7e5c1f4f363e6
- Cited via S1 (not re-read): PROOF_HANKEL_POSITIVITY 663f6c4f…, Codex 01830934…, Corpus 5a8f8630….

Note: in-lane sources rarely use the literal label "Cat B"; items below are those S1–S6 mark invent-pending / MATCH-on-example / named gap / Cat B (S6 #61, #63). Few in-lane items; list is complete for sources read.

## Table
| # | Claim | Source | Current wording | Loosened wording | Bridge target | Objection / risk |
|---|---|---|---|---|---|---|
| 1 | General \|W\| ≤ ∏ spr(ρ(h_i)) (residual circulant algebra) | S1 | MATCH-on-example (trivial, W=0); general statement invent-pending | "On the §2.1 example \|W\| ≤ ∏spr holds (W=0; per-target max 4 ≤ 6.928). Whether it holds generally is open; *if* it holds, it would give a spectral bound on cancellation consistent with the 11D path-sum reading." | \|W\| ≤ N ≤ ∏‖h_i‖₁ (triangle inequality) + Perron: ∏‖h_i‖₁ = spr(ρ(\|T\|)) for nonneg circulants (S1) | Safe only as conjecture. Note ∏spr(ρ(h_i)) ≤ ∏‖h_i‖₁, so the proposed bound is strictly stronger than the proven one; no proof exists. |
| 2 | HQCC Φ/χ "convergence theorem" (labs539_core Phi) | S1, S2 | AMBIGUOUS / invent-pending; demo trajectory, not a proof | "Φ is well-defined on ℤ₃; demo trajectories (seed 17) are consistent with convergence; a convergence theorem is a named gap." | Well-definedness of Φ on ℤ₃ (S1) | Do not cite demo trajectory as evidence of a theorem. |
| 3 | Ω = N − \|W\| ≡ 0 (mod 539) hardness | S1, S2, S6 #71 | invent-pending; AMBIGUOUS definitions (N, W redefined); Ω=2 on §2.1 example | "*If* a single definition of N (path multiplicity) and W (signed path sum) is fixed, Ω = N−\|W\| ≥ 0 is proven; any mod-539 / hardness property is a named gap requiring definitions first." | Ω ≥ 0 from \|W\| ≤ N (S1) | **Partial objection:** loosening allowed only for Ω ≥ 0. Mod-539 claim conflicts with the example (Ω=2); labs539 Ω is float atan2 winding with N capped at 539 — a different object. Hardness "between BQP and NP-complete" (S6 #71) NEEDS-DEFINITION; do not loosen. |
| 4 | Corpus §1 "odd M ⇒ 1+ω^j ≠ 0 ⇒ det ρ ≠ 0" | S1 | TENSION: true over ℂ for h=1+x; h2 layer singular mod 3 | "Over ℂ (and ℤ), for h=1+x and odd M, det ρ(h) ≠ 0. Over ℤ/3 this can fail (h2: det 36 ≡ 0 mod 3); statements must name the ring." | Circulant eigenvalues h(ω^j) (S1, S9) | Safe only with the ring named explicitly. |
| 5 | "Multi-layered Hankel" (HQH-539-512) ghost elimination | S1 | AMBIGUOUS / ABSENT; no Hankel matrix given | "*If* a Hankel matrix H is specified, PSD positivity (not det ≠ 0) is the condition that rules out ghosts." | PROOF_HANKEL_POSITIVITY 663f6c4f… (via S1) | Nothing to loosen into: no data. Any det≠0 ⇒ no-ghost wording is FALSE (H=[[1,2],[2,1]], det −3, eigenvalue −1). |
| 6 | Π_fast idempotent averaging operator | S2 | code stub = eye(128); does not prove corpus/Codex formula | "The coded stub is the identity (trivially idempotent). Idempotence of the corpus Π_fast averaging operator is a named gap." | none proven beyond the trivial identity | Do not cite eye(128) as evidence for the averaging operator. |
| 7 | N36 Kr over QQ via coordinated e1 CRT | S3, S4 | Named gap STANDS; ABSENT; 12-prime FAIL | "13 mod-p e1 lands are rank-503 MATCH with identical support. Char-0 Kr QQ is a named gap. Residues are consistent with *non-coherent* Φ₄₉ root choices across primes (untested observation)." | mod-p rank 503/503 (S4); support/pivot identity (S3) | Must not be loosened into "Kr QQ exists modulo technicality"; the CRT reconstruction failed (ok 0). The least-root observation is untested. |
| 8 | Q89 ζ₄₉ basis lift to char 0 | S5 | mod-p landing at one prime p=1027606441; NOT char-0 | "At p=1027606441 all 42 roots give kernel dim 89 / rank 89 through q^18. *If* a coherent ℚ(ζ₄₉) embedding and a lift exist, this is consistent with a dim-89 char-0 basis; the lift is a named gap." | mod-p rank 89 (S5) | Single prime; don't phrase as dimension over ℚ(ζ₄₉). Shares the embedding-coherence risk with #7. |
| 9 | S6 #61: dim S(ρ_s) = h − \|Cl²\| (Local) | S6 | "dim=h−\|Cl²\| is Cat B" | "At s=9,11,23,25 the forms are Hecke-character thetas (PROVABLE-CANDIDATE); the dimension formula dim = h − \|Cl²\| is conjectural and consistent with the listed cases." | S6 #58/#61 PROVABLE-CANDIDATE; Local filter ABSORB 0a4ddb32 (S7) | Spectral/representation-dimension claim, but it belongs to the Local lane; Eigen has no computation verifying it. Owner-lane loosening only. |
| 10 | S6 #63: RG1′ necessity | S6 | sufficiency proved; necessity Cat B; NEEDS-DEFINITION | "RG1′ is sufficient; *if* necessity holds, endpoint reflections characterize vanishing of the P-even defect." | S6 #62 (PROVABLE-CANDIDATE) | NEEDS-DEFINITION status: definitions have to come first. Local lane. |

**Count loosened (proposed wording): 8** (#1, #2, #3 partial, #4, #6, #7, #8, #9/#10 cross-lane counted as 1 pair → 8 net). #5 is not loosened: there is no data.
Bridge note: S8 (RTA v16) confirms hashes only. No item above is shown to merge against RTA v16 content. That link is ABSENT.

## Objections (do NOT loosen)
O1. Codex: "invertibility (det ≢ 0 mod 3) prevents information collisions" is a **FAIL / category error** (S1). Invertible per-layer maps coexist with W=0 total cancellation (det 2·36 = 72 ≠ 0 over ℤ, W = 0). Also h2 det = 36 ≡ 0 mod 3, so the example fails the Codex hypothesis over ℤ/3. labs539 validate_odd_moduli_rule does not repair this (S2).
O2. Any "det(H) ≠ 0 eliminates ghosts" Hankel wording is FALSE (S1 / PROOF_HANKEL_POSITIVITY). Only PSD may be used.
O3. Ω ≡ 0 mod 539 is contradicted by the §2.1 example (Ω = 2). It may not be softened into "consistent with".
O4. Hardness "between BQP and NP-complete" (S6 #71) and the physics bundle (S6 #72: N_flux, κ/539, Orch-OR, ngEHT) are NOT-MATH / NEEDS-DEFINITION. They are not Cat B and not mergeable.
O5. N36 Kr QQ / zero-polar / G1-mem: the named gap stands. No loosening may imply existence, coefficients, or ν.
O6. Labeling the target state [1] in §2.1 is an inferred reading (S1). Every merged statement must carry "with stated reading".

Tip AFTER: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched NO. No CERT.
