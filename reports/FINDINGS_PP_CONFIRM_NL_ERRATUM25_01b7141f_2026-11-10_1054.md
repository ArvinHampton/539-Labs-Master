# PP CONFIRM — NL Erratum 25 01b7141f (applies PP b39c7756, D6 stage-3 resume audit). 2026-11-10, written 10:54:33 CST (America/Chicago)

Labels are pure math (PROVED / CONDITIONAL / OPEN / REFUTED / PENDING). This is a faithfulness confirm only: no new mathematics, nothing adopted, no CERT. **Junction: UNSOLVED.** "Resonant algebra" is the term in use. Additive; no existing file edited; nothing written into /workspace/nl-d6s3-1110/ or any NL directory.

## 0. Integrity
- Target: NL_ERRATUM25_ACCEPT_PP_b39c7756_D6_STAGE3_RESUME_2026-11-10_1052.md, sha256 01b7141f92ac5764da9fdb7facbcbd240cda53bfdd642d6fa7fd771c318ba8d4 = sidecar = claimed. mtime 10:51:46 CST, mode 644 (sidecar the same).
- Input audit: FINDINGS_PP_AUDIT_NL_D6_STAGE3_RESUME_2026-11-10_1048.md, still b39c7756d8cbb9fa1fc8cc44d0fb843bd14717f8bea7223da4ed8c9fe44a71ab = sidecar, mode 444, mtime 10:48:34 CST (unchanged).
- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, checked before writing. Not touched.
- Header vs mtime: the label "1052" is about 1 min ahead of the 10:51:46 mtime. This is the same harmless pattern as Erratum 24 ("0958" vs 09:57:04). Nit only.

## 1. Frozen 0958–1027 files: untouched
Each file still matches its sidecar, and each mtime equals the one recorded in PP b39c7756 §0:
- Erratum 24: 60bbc718…e0fe1093, mtime 09:57:04.
- E5: 0a7d8e56…c4333d, mtime 10:19:44.
- E2: 197c5bd1…0569d, mtime 10:21:12.
- E4: 4c25565f…eb685, mtime 10:21:44.
- E1: 2f33b65d…dcd9c, mtime 10:22:21.
- S2-8: d559cb7d…a270, mtime 10:22:43.
- Z2 corner: 101467fc…4c654, mtime 10:27:43.

/workspace/nl-d6s3-1110/: all 12 .py/.log files match their sidecars, with the same mtimes as recorded in b39c7756 §0. The newest entry in the directory is from 10:26:57, so nothing was written there after the audit. The shared definitions file /workspace/nl-bps-d6-2057/z2_centre_flow_faces.py is still 21bcbc3f… .

The authority records cited in the erratum header also match their sidecars:
- e72a188b (call-83d7a0fa 0953);
- 32881263 (t4436);
- f700141d (t4431);
- 6436510d (ant-colony/Taormina 1049, cited as context only and not used);
- f825dfff (S6 odd-HW record).

**The erratum is additive.**

## 2. The 11 fixes (b39c7756 §8) compared with the erratum
| fix | b39c7756 requirement | Erratum 25 | verdict |
|---|---|---|---|
| 1 (priority) | (h0) = Erratum 24 (h2), x-independent Poincaré supercharges, listed on E5-3(b), E5-4, E2-4, E1-1; P8-1 inherits; reason Γ^{0123} anticommutes with Γ_μX (P4), so the χ₄ split holds only on ∂_με = 0 | §2 lists all four rows, records P8-1 inheritance, gives the P4 reason, the ∂_με = 0 restriction and the superconformal mixing remark, and calls it a premise-list completion. It also appears in the §1 premise lists | faithful |
| 2 (priority) | E2 §0 (ii) **and E1 §0**: restate as the D1 HW hypothesis Γ^nε = ε (ε(−r) = Γ_nε(r), continuous at the wall); S6 = odd-HW record f825dfff | §3 covers both E2 and E1 and gives the exact restatement with the equivalent wall form. S6 is recorded as f825dfff | faithful |
| 3 (priority) | E4-3 → "invariant source support meets C₄ ∩ face iff it contains C₄ ∩ face (E4-1)"; α-sheet classification not exhaustive (SO(3)_R-fixed U(1)_R circles at μ₃ = μ₄ = μ₅ = 0, disjoint from C₄); E4-5 replace "natural sources … α sheets" | §4 states the restatement verbatim, records "as filed not accepted, not REFUTED", gives the non-exhaustive circles (smeared over H² at any r), aligns E4-5, and names the branch-defining premises. Only the restated form is counted | faithful |
| 4 | diagonal-K scope: E2-2 forcing column, E5-5 "unique diagonal K", E1-2; K\|_T general symmetric 2×2 on E2; 4-dim forms on E5 without U(1)_R (P11); conclusions survive | §5 includes all three items, both reasons, [w] forced vs subfamily, "ω₂ free" surviving, P12's three fluxes and the exact conjugate pair | faithful |
| 5 | "degree 0" not "trivial"; make explicit that both locked lines have degree 0 (P10 or the vacuum); unlocked = ±(2g−2); (gr) not needed | §6 has the wording, the 2-torsion caveat, the derivation d = a·s₁ + b·s₂′ with a − b = 0, unlocked ±2 on genus 2, and (gr) not needed | faithful |
| 6 (optional) | record PP streamlined E5-4 proof (SU(2) weight symmetry on V₊; no doublet decomposition); n = ±e_r from C₄ ⊂ face; add "C₄ ∩ face ≠ ∅" to (reg) | §7 reproduces steps 1–4 of b39c7756 §3, the n = ±e_r argument, and C₄ ∩ face ≠ ∅ in (reg) (also in §1) | faithful |
| 7 | E4-2 wording: fixed set of K_{p̃} is the S² over p̃; C₄ is the union over Σ; smooth by homogeneity | §8 | faithful |
| 8 | Z2 v1 stop ≈ 10:12–10:13 CST (script 10:10:16, log 10:12:52, sidecar 10:13:07) | §9 gives the same times. The v1 log is record only | faithful |
| 9 | relabel v2 ComplexWarning without max\|imag\|; print it as continuation v2 does | §10: records the issue and leaves the frozen script unedited, with any later script to print max\|imag\|. No grade effect; Z-2 COND | faithful (deferral is the only additive option) |
| 10 | E2 header: full script and log shas | §11: e2 .py 1bfbbac71e1b549605b0f060eb3db83492383408cf54747bc8a99cb335f0044d and .log 66f95d9a7442dac16f8503ce0424c75bf21174d062d20ded3cc2db9f44c3efdd. PP re-hashed both, and both equal the live files and their sidecars | faithful |
| 11 (hygiene) | dead code in chirality_hw_lock_exact (unused proj, empty loop 130–134); leave frozen, note | §12 | faithful |

All 11 fixes are folded. There are no misses and no misstatements. The §1 premise lists for E5-4 and E2-4 match b39c7756 §3 and §4 item for item, including the "not covered" list for E2-4.

## 3. Grades and tallies
- Accepted drops are recorded as PP-audited PROVED implications:
  - E5 ∩ H_Σ ∩ SO(3)_R, with or without U(1)_R, including scope S (E5-4);
  - E2 ∩ (SO(3)_R × U(1)_R) (E2-4).
  Earlier drops (E3; S5, BPS only) are unchanged.
- E5-3 (including (b) / Lemma CH) is recorded as PROVED (exact + hand), with (b) an implication under (h0)/(h2) and (h1).
- E4-3 is counted only in its restated form. E4 is 5/0/1/0.
- S2-7 stays CONDITIONAL.
- E1-3 and P8-2 stay COND (citation). Z-2 stays COND (float).
- Open rows stay OPEN: E5-6, E2-5, E4-6, E1-4, P8-3, Z-3, S3b-4.
- Branch register §13 matches b39c7756 §7.
- Earlier tallies are unchanged:
  - 2216: 8/2/3/0, with S2-7 COND and S2-11 OPEN;
  - Erratum 23: 2/0/0/0 row count, 0/0/0/0 distinct;
  - E3: 3/0/0/0;
  - S5: 3/0/1/0;
  - Erratum 24: 0/0/0/0;
  - E5 6/0/1/0, E2 4/0/1/0, E1 2/1/1/0, S2-8 1/1/1/0, Z2 1/1/1/0.
- **Resume total: 19/3/6/0 = 28 (18 + E4-3 restated), confirmed.**
- The erratum's own tally is 0/0/0/0. This is accepted: it adds no new graded row. "Restated E4-3 (PROVED)" is the existing E4 row in the form PP already graded, not a new claim. No grade is changed by NL or by this confirm.

## 4. Nits (not required)
- N1: the header label "1052" vs the mtime 10:51:46 CST (about 1 min ahead). Harmless.
- N2: the erratum and its sidecar are mode 644, not 444. This is consistent with every NL file in the series. Not a grade or faithfulness issue.

## Verdict
**FAITHFUL with nits** (N1, N2). No required fixes. No grade change. Frozen 0958–1027 files are untouched. Tip 7cddb188 is unchanged. Nothing is adopted, there is no CERT, and the junction stays UNSOLVED.
