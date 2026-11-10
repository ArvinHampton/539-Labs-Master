# Summary of reports: s-family, RTA/Bridge C, RNT tests and Time

**Prepared for:** Arvin Hampton · **Date:** 2026-10-21 (CDT)
**Scope:** read-only summary of existing reports. Category labels (A = proved/exact relative to stated imports; B = numerical or interpretive) are carried over as each report gives them. Nothing has been upgraded. New files only; nothing pushed or sent.

---

## 1. S-pairing (tr_C S = 0) for all s

### 1.1 Even s: early per-s certificates (A8c)
- **Category A (computer-assisted, exact mod-p rank):** tr_C S = 0 (and tr_E S = 0) certified for s = 8, 16, 18, 24, 26, 32, 40, 48, 50, 56, 58 via an operator Y = Z − SZS that anticommutes with S on W and is invertible (rank mod a prime ideal = dim W). s = 10 is trivial (C = 0).
- **Category A (hand proof):** tr_W S = 0 for every even s, via a monomial unitary K_y that anticommutes with S and commutes with γ_s and −1 (so it preserves W). Exact check for even s = 6..60.
- **Category A:** the label-dilation Galois-sign route gives no sign −1 at s = 8, 10, 16, 18 (rigorous negative).
- **Category B:** s = 34 and 42 were not certified by this method (a persistent 2-dimensional kernel); numerically tr_C S = 0 there.

Source: /workspace/quantum-comp/reports/s_family_paths/A8c_Spairing_even/REPORT.md

### 1.2 Local factorisation and coverage (A10)
- **Caveat stated in A10:** definitions of W, E, C were reconstructed because the A8-series material was not on disk at the time; A10 asks that they be reconciled with the originals (done in A11).
- **Category A:** tr S = tr SZ = 0 on the full space (one-line Gauss-sum argument); tensor factorisation of the Eisenstein trace into local factors; vanishing of the local factor for odd p ≡ 3 mod 4 with exponent 1; exact computer certificates of several 2-adic and odd local classes.
- **Category A (modulo the reconstructed definitions):** tr_C S = 0 for all 29 values s ≡ 0, 2 mod 8 with 8 ≤ s ≤ 120 (including 34 and 42), and 489 of 499 values up to 2000. Ten gaps: 130, 488, 514, 578, 1090, 1154, 1282, 1602, 1666, 1858.
- **Category B:** conjectural closed forms for the 2-adic and odd local factors; numerical scan for s ≤ 120.

Source: /workspace/quantum-comp/reports/s_family_paths/A10_uniform_Spairing/REPORT.md

### 1.3 Original definitions and the 2-adic induction (A11)
- **Category A:** original definitions recovered from the A2 scripts; for even s they collapse to C[D] (complex conjugate of the A10 convention, so vanishing transfers). Factorisation tr_C S = −∏_p t_p. Lift lemma tr_{P E0_a} S = t_{a−2}. Exact base classes a = 2, 3, 4 (with P-stability). Same unconditional coverage as A10 (all 29 values ≤ 120; 489/499 ≤ 2000).
- **Conditional / Category B:** the induction t_a = t_{a−2} needed two hypotheses, H1 (P-stability) and H2 (zero trace on (1−P)E0), verified only numerically for a ≥ 5 (up to a = 9). Nine of the A10 gaps closed conditionally; 488 needed an odd-prime step. E0 = E_A10 beyond s = 18 is Category B.

Source: /workspace/quantum-comp/reports/s_family_paths/A11_induction/REPORT.md

### 1.4 The uniform proof (A12)
- **Category A (written proofs, relative to imported facts F1–F5):**
  - H1 for all a ≥ 2 (δ_h lies in the δ_0-span via an explicit word S T^{2^a} S).
  - H2 for all a ≥ 3 (a basis of X indexed by P¹(Z/M) with S acting monomially and fixed-point-free; uses Scheithauer's upper-triangular formula only for the upper bound on dim X).
  - Odd p: the δ_0-span equals the full even part for every exponent e, with closed form t_p = 1 (e even), (2/p) (e odd, p ≡ 1 mod 4), 0 (e odd, p ≡ 3 mod 4). So t_p = 0 exactly when p^e ≡ 3 mod 4.
  - **Main result:** for every s ≡ 0, 2 mod 8, tr_C S = 0 for the original W, E, C, hence dim C⁺ = dim C⁻ (and tr_E S = 0). Closes 34, 42, all A10 gaps and the odd-step cases (488, 2664, 2746, 6176, 7778, 8264, 9722, 17498).
- **Category A (computer-assisted):** the 2-adic base classes a = 2, 3, 4 (exact certificates, not hand proofs).
- **Category B:** numerical checks (corroboration only).
- **A12's own caveat:** written in one session; independent review recommended before external use, especially the stabiliser/generation step and F3 sign conventions.
- Odd s and s ≡ 4, 6 mod 8 rely on the earlier Galois-sign argument (A6), as noted in A11/RTA_implications.

Source: /workspace/quantum-comp/reports/s_family_paths/A12_H1H2_odd/REPORT.md

### 1.5 Referee check of H1 (A13)
- **Verdict: confirmed with minor fixes.** Independent derivation (done before reading A12) agrees with all A12 constants.
- **Category A:** hand derivation for all a ≥ 2 and odd u.
- Exact mod-p check (p = 33556993) for a = 2..7, all u mod 8 (24 classes): identity, support, Gauss sum, order of T, q(h) = 0, and an independent Krylov membership test all pass. A13 notes a single prime is a strong exact cross-check but not by itself a characteristic-0 proof.
- Issues found: all minor/expository (unnormalised constant not pinned, compressed odd-y sum, isotropy of h not flagged in H1, P-commutation step unstated, conjugate-convention transfer for a membership statement should be stated). No sign or constant error.
- Not reviewed by A13: H2 and the odd-prime part; flagged dead arithmetic in the `Yok` line of A12's checks.py.

Source: /workspace/quantum-comp/reports/s_family_paths/A13_H1_check/REPORT.md

### 1.6 Referee check of H2 (A14)
- **Verdict: confirmed with minor fixes; no mathematical gap found.**
- **Category A (independent hand derivation):** v ∈ X, line stabiliser, spanning/coset count, the lower bound, and no S-fixed point on P¹(Z/M).
- Points to fix: the level is lcm(4, M) (equals Γ_0(M) only for a ≥ 3, the real reason a = 2 is excluded); state F3 for the level-L Borel with Γ(L) acting by a scalar; only a projective representation is needed, so signature parity is irrelevant; restate the triangular-number lemma; say explicitly the lower bound makes the lines independent and in bijection with P¹(Z/M).
- **Category B:** independent float checks for a = 2..8, all u, both conventions — all consistent for a ≥ 3; correspondence fails at a = 2 as predicted.

Source: /workspace/quantum-comp/reports/s_family_paths/A14_H2_check/REPORT.md

---

## 2. dim S(ρ_s) table (odd s, A9 Hecke family)

As of 2026-10-21, 7:15 AM CDT. Upper bounds from the unchanged certifier (M = 6, Q = 40); lower bounds from exact Hecke/T-row determinants.

**Category A — certified**

| s | lower | upper | dim S(ρ_s) | status |
|---|---|---|---|---|
| 11 | 2 | 2 | **2** | closed |
| 15 | 3 | 4 | 3 ≤ dim ≤ 4 | open (one sector 1 ≤ d ≤ 2) |
| 17 | 3 | 4 | 3 ≤ dim ≤ 4 | open (one sector 0 ≤ d ≤ 1) |
| 19 | 2 | 2 | **2** | closed |
| 25 | 3 | 3 | **3** | closed (new overnight) |
| 27 | 3 | — | ≥ 3 | upper bounds not yet run |
| 29 | 3 | — | ≥ 3 | upper bounds not yet run |
| 31 | 3 | — | ≥ 3 | upper bounds rerunning |

**Category B — numerical only, not claimed:** float-scan values s = 15: 4, 17: 4, 27: 4, 29: 4, 31: 3.

Operational notes: s = 31 mm was OOM-killed; s = 31 pp stopped when the box went down; s = 27/29 never ran (earlier logs are from a failed launch). A low-memory rerun queue started 7:11 AM CDT Oct 21 (s31 mm, s31 pp, s27 mm, s29 mm, s27 pp, s29 pp). s31 pp may OOM again; reducing memory would need a certifier change, which CORE_FREEZE blocks without Arvin's sign-off. Even if they succeed, the queued claims would only bracket s = 27, 29 as 3 ≤ dim ≤ 4 unless the lower bound is raised.

Other certified values quoted in the preregistrations (from earlier reports): s = 5, 7, 9, 12, 13, 14 → 1; s = 21 → 5; s = 23 → 3.

Source: /workspace/quantum-comp/reports/s_family_paths/A9_hecke_family/REPORT.md

---

## 3. RTA / Bridge C

### 3.1 What the S-pairing implies (RTA_implications)
- Bridge C is the **odd** case s = 7 (A = [[2,7],[7,7]], |D| = 35, level 70). The new even-s uniform result does **not** apply to Bridge C itself; s = 7 uses the earlier odd-s Galois-sign result (A6).
- Only the even/E_L piece lives in the ρ_s world; the odd Zwegers part, P_s, and the c2-wall pieces lie outside C. The 35-component law (Weil rep of D(A_7)) and the 42-dim ρ_7 label space are different spaces; no map was established (Category B gap).
- **Category A (relative to the A2/A6 trust base and a cited identification):** at s = 7, C is a 6-dim irreducible ρ-module with dim C⁺ = dim C⁻ = 3; hence no 1-dim (scalar) cusp-residual law, and every S-eigenvector spans all of C. The constant term c0 is Eisenstein, so the pairing does not constrain it.
- **Category B:** float check at s = 5, 7, 9, 13 (tr_C S ≈ 1e−16, balanced splits, End = 1); consistency with certified dims; untested Hejhal prediction; the even-s E_L link depends on the A11 collapse and is unverified.
- Caveat: the E_L ↔ u_L identification is Category B by citation and the main implication inherits that.

Source: /workspace/quantum-comp/reports/s_family_paths/RTA_implications/REPORT.md

### 3.2 Preregistered link tests RTA-1 (Residual only; RNT not used)
Preregistration fixed six predictions (P1 intertwiner 35 → 42; P2 3+3 Hejhal split; P3 E_L lands in C for even s; P4 order-3 balance of R = ST; P5 shape of C determined by (h, Nε); P6 c2-wall false-theta S-behaviour), controls and Holm correction (m = 5) before any run.

Results (**all Category B**, floating-point with logged gaps; no Holm rejection):
- Step 0: Q(√35) h = 2, unit 6+√35 of norm +1 correct; [[2,1],[1,−17]] is odd, so even indefinite det −35 controls cannot exist (Amendment 1 corrected controls).
- **P1 FAIL:** dim Hom(ρ₃₅, ρ_7|W) = 0 (and for the dual); also 0 for all controls. No intertwiner Φ exists.
- **P2 DEFERRED** (Hecke queue running). **P3 INCONCLUSIVE** (no label-space vector for E_L,s). **P6 INCONCLUSIVE** (not decidable at finitely many rationals).
- **P4 PASS-generic → not a link:** tr_C R = 0 at s = 7 and at all 8 s with 3 | d_cusp, but the Eisenstein part is balanced at 16/16 s too. Candidate future local-factor formula tr_C(ST) ∈ {0, −ω} (new hypothesis, not part of RTA-1).
- **P5 INCONCLUSIVE** (underpowered pilot; Fisher p = 0.221; only 9 matched s).
- Overall: negative or generic on everything decidable; no Bridge-C-specific link. Caveats include amendment timestamp corrections and some P1 outputs seen before code fixes (final run reproduces Hom = 0).

Source: /workspace/quantum-comp/reports/s_family_paths/RTA_prereg/REPORT.md and /workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results/RESULTS.md

---

## 4. RNT link tests (negative)

Kept separate from the Residual work. Preregistration RNT-1 fixed six predictions linking the 539 arithmetic (ord_539(3) = 210; 18 + 521; the 540 ladder) to ρ_s invariants, with matched controls and Holm correction over 13 sub-tests, before any computation. Design fact: 7 ∤ 7s − 32, so any "539 | D" test is empty by construction.

Results (**all Category B**; no Category A claim):
- **P2(i) FAIL:** 210 | ord(3) at 539 is structural — shared by 100% of other order-210 units, so "3" is not special.
- **P3(a), P3(c) FAIL** at T = 18, 521, 540; no exact period anywhere. Smallest p = 0.057 vs Holm threshold 0.0038.
- **P4 FAIL** (p ≈ 1; residues more uniform than chance, expected since D/11 is linear).
- **INCONCLUSIVE:** P1b and P5 (need certified dims at s ≥ 198), P3(b), P2(ii) (preregistered infeasible), P6 (pilot).
- None of the 13 confirmatory sub-tests rejected. **Overall: negative on everything testable, inconclusive where data does not exist. No link candidate; the Residual/RNT separation stands.**

Source: /workspace/quantum-comp/reports/s_family_paths/RNT_prereg/REPORT.md and /workspace/quantum-comp/reports/s_family_paths/RNT_prereg/results/RESULTS.md

---

## 5. Time (Category B)

### 5.1 Framework-level review
- **All Category B (interpretation, no derivation).** In the framework, time is one global parameter with two arrows (+U forward, −U reversed), periodically structured by G₄ = 539.9 s and coupling +U to −U through D2-brane transfer. "A structural clock, not an extra free time dimension" is congruent with the chain; the chain's own word is periodicity (O(t + G₄) = O(t)).
- Not established: the step from the count 539 to the 539.90 s period; separate sector clocks; a compact second time; a literal second timelike dimension; a Bars-style 2T reduction; the meaning of the d³t factor.
- Where the earlier Grok reply overreached: "requires" (better "postulates", since the claim table lists G₄ as a modelling hypothesis); galactic time law not established; "PBH chiral shifts" only partially supported.
- Audit flags (arithmetic, kept separate): TTC "T² = 0" needs an extra condition; e^{2πi/539.9} is not a root of unity; 538.996 ≠ 539; T23 distance mismatch; 58 481 × 539.9 s misses the tropical year by 4.7 h; the period is written inconsistently (539.9, 539.90 ± 0.05, 540, 539 ± 1).

Source: /workspace/quantum-comp/reports/time_review/REVIEW_CatB.md

### 5.2 Two-time postulate exploration
- **All Category B** ([checked] = algebra/numerics of the exploration only; [interp] = interpretation).
- Locked variant (t₋ = −t₊ + φ) reduces to one observable time with a −U phase; it matches Ridley & Cohen's Bauer two-time QM and is the most congruent with the chain.
- Separable variant gives a torus; a 33.74-day beat (2,915,460 s) between 539.9 s and 540 s — conditional on the 540 not being a typo (flag A6).
- Coupled variant: the negative-norm toy model has a ghost-type instability above g_c ≈ 2.51×10⁻⁸ s⁻² (and at every coupling if the periods are equal); in Bauer's positive-norm frame it becomes a bounded, unitary arrow oscillation.
- Bars 2T physics is incongruent with all variants. Open: meaning of d³t; whether the negative norm should be read as Bauer's negative energy.

Source: /workspace/quantum-comp/reports/time_review/two_time/REPORT.md

---

## 6. Open items
- **S-pairing:** independent review of A12's odd-prime part (not covered by A13/A14); fold in the A13/A14 minor fixes; a hand proof of the 2-adic base classes a = 2, 3, 4 (currently computer-assisted). (A12, A13, A14)
- **dim S(ρ_s):** close s = 15, 17; obtain upper bounds for s = 27, 29, 31 (low-memory rerun in progress; s31 pp memory risk; raising lower bounds needed to close 27/29 at 3). (A9)
- **RTA/Bridge C:** no map between the 35-component law and ρ_7 (P1 shows no equivariant one); the B3 law vector has never been built; E_L ↔ u_L identification is Category B; P2 Hejhal check deferred; P3, P5, P6 inconclusive; candidate tr_C(ST) local-factor formula is a new hypothesis. (RTA_implications, RTA_prereg)
- **RNT:** inconclusive tests await certified dims at s ≥ 198 or many more s. (RNT_prereg)
- **Time:** meaning of d³t; negative-norm vs negative-energy reading; status of 540 vs 539.9 (flag A6). (time_review)

Source: compiled from the reports listed in sections 1–5 (paths given there).

---

## 7. Awaiting go-ahead
The following are **not started** and await Arvin's explicit go-ahead:
- **Paper draft** on the S-pairing results.
- **Clean v3 fold** of these results.
- **Zenodo / Master pushes** (no uploads or pushes have been made).

Source: request of 2026-10-21; no source report (status item).
