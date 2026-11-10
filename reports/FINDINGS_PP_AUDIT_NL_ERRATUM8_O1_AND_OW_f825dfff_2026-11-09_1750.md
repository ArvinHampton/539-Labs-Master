# FINDINGS: PP audit of NL erratum 8 (O1, 96fb6069) and verification of Owner record OW f825dfff (t4369). 2026-11-09 17:50 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. No CERT. Nothing adopted. No message sent. No outside service. Convention G = ½T^(EH) (OW 2d1e877e).
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, re-hashed 17:46 and 17:50: **MATCH (untouched)**.
Scratch: /workspace/audit-scratch/pp_parity_1740/eps_all_signs.py 766d491c… / eps_all_signs.log c4609543… (sidecars written). Also parity_cases.py 26125f67… / .log ca971a5e… from 544fc7b0.

## Rollup
PROVED 14 · CONDITIONAL 3 · OPEN 1 · REFUTED 1 · PENDING 1 (20 items).
- **OW f825dfff is on disk and its sidecar matches.** Five of the six relayed points match the record. The sixth, "NL works the odd case only, including n_inst", is **not in the record** (W3).
- **Erratum 8:** all four PP fixes are applied faithfully. The P-b wording (both topological terms) and the A8 scope are applied too.
- **The sign rule ε = −s_x s_Σ is correct for every fibre-preserving τ**, including any S⁴ action: s₄ cancels identically (8/8 sign patterns). No extra S⁴ or transverse factor is needed beyond s_r = −1, which is already in. It is not established for τ that mix S⁴ with Σ or x (OPEN, moot under f825dfff).
- **Tallies:** §A 9/4/2/3 = 18 ✓. 1736 overall 21/8/6/3 = 38 ✓. The 17-vs-18 header belongs to the §B–§D audit (PENDING).
- **NL fixes requested: 3** (wording only; no conclusion changes), plus 1 alignment note after f825dfff.

## 1. Integrity
- **I1 [PROVED].** Each file's sha256 equals its sidecar:
  - OWNER_WRITE_MAINCHAT_t4369_FACE_Z2_FIXED_PLANE_HW_WALL_G4_ODD_O1_RESOLVED_2026-11-09_1745.md: f825dfffb8cd17a7f3f57a2b0a70bd0d9c9d73f215febffdbd2ca95b494d7cd1 (file mtime 17:46)
  - NL_ERRATUM8_O1_ACCEPT_PP_544fc7b0_2026-11-09_1745.md: 96fb60698c4f0dc59c1f27b98beb6a2cf3df47d08141956760ea2707636d80cd
  - PP 544fc7b0b0183022… (the audit this erratum answers)
- **I2 [PROVED].** Tip MATCH (header).

## 2. OW f825dfff (t4369)
- **W1 [PROVED] On disk.** `rg f825dfff reports/` finds only that record's sidecar, and the file hashes to f825dfff…. It is the only OWNER_WRITE_* file modified at or after 17:39 besides t4367 (17:38).
- **Exact wording.** Source: main-chat widget t4369s18138. Owner own words, verbatim:
  > "As mine: the face is a Z2 fixed plane (Horava-Witten-type wall); G4 parity odd per PP 544fc7b0, with an E8 wall sector CONDITIONAL."
  - Definition: the face (the 10D matching hypersurface, OW f283cffd) is a Z₂ FIXED PLANE, an HW-type wall.
  - Consequence: O1 is ODD (PROVED given P-b under the fixed-plane premise; even or a flip is REFUTED on a fixed plane). Face charge N_M5 + n_inst = 2N_flux (N_b = 2N_flux only with no E₈ instantons: CONDITIONAL). E₈ wall sector CONDITIONAL. P-b is a stated CONDITIONAL premise.
  - Supersedes: flip plan 602b6427; the parity claim in pasted record fe8bcb00; parity cards t4363s18113 and t4369s18138.
  - Unchanged: vacuum HOLD (587eca0c); b and J7 OPEN; no source adopted; tip untouched; No CERT; no Gemini; additive only.
- **W2 [PROVED] Relayed points that match.** All of these are on disk:
  - fixed plane / HW wall;
  - G₄ odd per 544fc7b0;
  - E₈ CONDITIONAL;
  - O1 resolved (the filename says "O1_RESOLVED"; the body says "O1: G4 parity is ODD");
  - 602b6427 superseded.
- **W3 [REFUTED, by quotation] "NL works the odd case only, including n_inst".** The record contains no NL assignment. Its only n_inst mention is the face-charge relation. No other Owner record from ≥ 17:39 says this. It is an agent paraphrase, not Owner text on disk.
- **W4 [PROVED] Consistency with OW 9a8ced02.** 9a8ced02 forbids *declaring* a parity. Here the Owner defines σ (τ = id, P-fix), and the parity is then derived: C0 + R1 + R3 in 544fc7b0, plus the A1–A3 audit. That is a derivation that PP has audited, not a declaration. 9a8ced02 is about locking *even*. Odd is not locked by declaration either.
- **W5 [CONDITIONAL on P-b] O1 status.** It is resolved as ODD given the Owner definition (on disk) and P-b. P-b says the fixed-plane Z₂ is a symmetry of 11D sugra including C∧G∧G and C∧I₈. It is the standard condition for an M-theory orbifold to be consistent, but it is a premise, and the record states it as one.
  - E₈ sector and n_inst: CONDITIONAL (HW).
  - Consequence (CONDITIONAL on W5): the O1-dependent results filed for both parities may now be read in their odd branch: 5cbd050a P3e, NL 1711 G2-odd, 1713 L3/PD2. The even branches (G2-even, PD4) become inapplicable on the fixed plane. The no-go results NC1–NC3 and the fibre-NEC obstruction are parity-independent and unchanged.

## 3. Erratum 8: fidelity to PP 544fc7b0
- **F1 [PROVED] Fix 1 = PP NA0.** The 1736 claim "[K] = 2K needs pointwise fixing" is retracted and REFUTED with PP's counterexample: τ*K = K gives K(y) + τ*K(τ⁻¹y) = 2K(y), and K depends on the S⁴ only through μ_a². P-fix is now stated as a premise. Faithful.
- **F2 [PROVED] Fix 2 = PP NA9b.** "O1 meaningless off a fixed plane" is REFUTED. The (i) even, net-0 and (ii) odd, 2N_flux cases are added with PP's examples, and O1 is undefined only with no Z₂. Faithful, apart from wording item N1 below.
- **F3 [PROVED] Fix 3 = PP NA4.** N_M5 + n_inst = 2N_flux (CONDITIONAL, HW), and N_b = 2N_flux ∈ 2ℤ only if n_inst = 0. It is split into A4a (net 2N_flux, PROVED) and A4b (CONDITIONAL), exactly as PP graded it. Faithful.
- **F4 [PROVED] Fix 4 = PP R2.** The linking cycle is S⁴(r₊) − S⁴(r₋), and the charge is Φ₊ − Φ₋ = (1 − ε)Φ. Faithful.
- **F5 [PROVED] A8 scope.** "Scope P-fix only" is applied (= PP NA8).
- **F6 [PROVED] P-b wording.** Both ∫C∧G∧G and ∫C∧I₈ are included, giving C₃ → s₁₁σ*C₃ (= PP C0).

## 4. The sign claim "parity = −s_x s_Σ"
- **S1 [PROVED, for every fibre-preserving τ].** The orbifold condition is G = s₁₁σ*G with σ = (r → 2r_b − r) × τ and s₁₁ = s_r s_x s_Σ s₄, where s_r = −1. Then:
  1. Φ(r) = ∫_{S⁴_r} G = s₁₁∫_{S⁴_r} σ*G = s₁₁∫_{σ(S⁴_r)} G = s₁₁s₄Φ(r′).
  2. So ε = s₁₁s₄ = s_r s_x s_Σ s₄² = −s_x s_Σ.
  - **s₄ cancels identically.** eps_all_signs.log checks all 8 patterns (s_x, s_Σ, s₄) ∈ {±1}³: TRUE. In parity_cases.log the antipodal case has s₄ = −1 and the result is still odd.
  - The only transverse factor is s_r = −1, which is already in the formula. Equivalently, ε = −(worldvolume orientation sign), and the transverse sign s_r s₄ never enters ε alone.
  - **The sign is right.** Odd ⇔ s_x s_Σ = +1 ⇔ worldvolume orientation preserved (PD1). This includes s_x = s_Σ = −1, a double reversal, which is odd.
  - Needed: (a) τ maps S⁴ fibres to S⁴ fibres, so that s₄ is defined. (b) Fibres over different base points are homologous (the base is connected), and Φ is constant along the flow (PD5).
- **S2 [OPEN].** τ that do not preserve the S⁴ fibration (mixing S⁴ with Σ or x) are not covered, because s₄ is undefined there. This is moot under f825dfff (τ = id).
- **S3 [CONDITIONAL].** If s_x = −1 is realized by t → −t, the classical action rule C → s₁₁σ*C still holds. The quantum time-reversal (antiunitary) treatment is not checked. Not needed under f825dfff.

## 5. Tallies
- **T1 [PROVED] §A, revised: 9 / 4 / 2 / 3 = 18.**
  - PROVED: A1, A2, A3, A4a, A4c, A5, A9a, A10, A11.
  - CONDITIONAL: A4b, A6, A10e, A11e.
  - OPEN: A7, O1 lock.
  - REFUTED: A0r, A8, A9b.
  - Each item is graded consistently with 544fc7b0.
- **T2 [PROVED, arithmetic] 1736 overall: 21 / 8 / 6 / 3 = 38.**
  - The old §A was 6/1/2/1 = 10, with the O1 lock counted in §A. 1736's own "A: … 1 OPEN" plus "O1 lock adds 1 OPEN" gives 2.
  - The old overall was 18/5/6/1 = 30. So the old §B–§D was 12/4/4/0 = 20:
    - PROVED: B0a–d, B1, B2, B3 (|z| ≤ 1), B4, C1, C2, D1, D2 (|z| ≤ 1);
    - CONDITIONAL: B3 (z = 2, 3), C3, D3, D2 (z = 2, 3);
    - OPEN: B5, B6, C4, D4.
  - 20 + 18 = 38 and 12 + 9 = 21 ✓.
- **T3 [PENDING].** The 1736 header PROVED "17" vs the 18 in the table (D2 for |z| ≤ 1 added) belongs to the §B–§D audit. Not graded here.

## 6. NL fixes requested (additive; no conclusion changes)
- **N1 [CONDITIONAL; wording].** Fix 2(ii) / A11, "net face charge 2N_flux" for the free antipodal τ: add "on the covering space". On the quotient the face is face/τ, and the charge normalization per fundamental domain is not stated.
- N2. State the domain of ε = −s_x s_Σ: τ preserving the S⁴ fibration (S1), with s₄ cancelling. τ that mix S⁴ with the base are not covered (S2). Optionally note the time-reversal caveat (S3).
- N3. Alignment after OW f825dfff: an additive note that the Owner has now defined τ = id (P-fix). "O1 lock (OPEN) / remaining Owner choice τ" is therefore superseded: O1 = ODD, CONDITIONAL on P-b, with E₈ and n_inst CONDITIONAL. The P-nofix items A9b, A10, A10e, A11 and A11e stay correct, but they are now off-premise. Erratum 8 predates f825dfff, so this is not an error in it.
- N4. Do not cite "Owner: NL works the odd case only" as Owner text. f825dfff contains no NL assignment (W3). An odd-branch focus follows from the definition, but any work go must come from an Owner record.

## Tally detail
- PROVED 14: I1, I2, W1, W2, W4, F1, F2, F3, F4, F5, F6, S1, T1, T2.
- CONDITIONAL 3: W5, S3, N1.
- OPEN 1: S2.
- REFUTED 1: W3.
- PENDING 1: T3.

Tip 7cddb188 untouched (MATCH). No CERT. Nothing adopted. No message sent.
