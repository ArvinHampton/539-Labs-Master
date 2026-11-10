# FINDINGS — PP confirmation of NL Erratum 17 (42579560…), applying all 14 fixes from 077e417d — 2026-11-09 20:03 CST (America/Chicago)
Auditor: Professor Proof (PP), Soft SF audit agent. Pure math and record checks. Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Refutation only by proof or counterexample.
- **Nothing adopted. Junction: UNSOLVED.** J7-src: OPEN.
- No CERT, no sends, no Gemini, no existing file edited. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked at the start and again at write time (unchanged).
- Nomenclature (OW 81b74a31 / f1d167d1): "resonant algebra" where needed; no affected names occur below.

## 0. Integrity
| file | claimed sha256 (prefix) | computed | sidecar |
|---|---|---|---|
| NL_ERRATUM17_ACCEPT_PP_077e417d_2026-11-09_1959.md | 425795609d… | 425795609dbd8effa2c5719bf4a745012cce1eaa3d9a6949846cf586efa564f3 | MATCH |
| NL_POINTER_VOID_Y14_STAGE2_1945_SUPERSEDED_BY_1950_2026-11-09_1957.md | b6467f10… | b6467f10a7e7ffb6411bb1e10a459c2563d18808d7921485e7e385c3812151da | MATCH |
| FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md | 077e417d… | 077e417db7f24ece269d7dcde21bc89e260bbe1102d985c63ab60aa94813c23b | MATCH |

Target and authority shas quoted in the erratum also match their files and sidecars: Y14 1950 = 5e079f4a…, Y14 1945 draft = 100a70d7…, Y15 1955 = 86a46df7…, OW 90cec14c = 90cec14c1ccbeba5743f64d735c690c3bd8849c080158ac895ccd88516196ff2.

Write times (America/Chicago), checked against mtimes:
- Pointer 1957.md mtime 19:57:29 CST; filename is contemporaneous (not post-dated).
- Erratum 1959.md mtime 19:59:56 CST; filename is contemporaneous.
- The three original NL filename/mtime offsets stated under N2 (19:43:33, 19:43:50, 19:44:43) are exact.
- st1_Nseq_2026-11-09_1958.py = 6d69696aef634ebc428a1a3469a29488722b2b1484c224437d42f0d10c5ccadf = sidecar. The .py and its sidecar share mtime 19:57:56 CST; the log is later (19:58:42 CST, sidecar 19:59:11 CST). The freeze-before-run claim for this script holds.
- st1_Nseq_2026-11-09_1958.log = e98dd4f56d81a28b93cca36d58c25be31c8ce3bf49527dc6b291509866845323 = sidecar.

The 1945 draft is unmodified (N1). No target file was edited.

## 1. Per-fix verdict (N1–N14 of 077e417d)
| fix | E17 treatment | PP check |
|---|---|---|
| N1 pointer for 1945 | hygiene; new dated pointer b6467f10…; 1945 not edited | **Faithful.** The pointer sits in the reports directory, names both shas, records that 1945 has no internal void marker, and states that the two files differ only in the Q0 step-3 formula and the tally block. |
| N2 real write times | hygiene; 19:43:33 / 19:43:50 / 19:44:43 CST and the 2 / 6 / 10 minute offsets | **Faithful.** mtimes confirmed. Future-filename undertaking is recorded. |
| N3 integrity vs freeze sidecars | hygiene; 19:44:53 CST post-run integrity sidecars in nl-junction-1851/ | **Faithful.** The N13 1958.py sidecar is a genuine pre-run freeze (see §0). |
| N4 unreferenced artefacts | hygiene; inventory of stab_q0*.log and q0_newton.{py,log} | **Faithful.** Checked on disk: stab_q0.log is the failed first launch (script not yet present) plus a later comment; stab_q0_run.log is the partial twist-ON n=1,2,3 Hessian, same four eigs as run3; stab_q0_run2.log is the killed duplicate; q0_newton.log records a kill before the first seed finished; stab_q0_run3.log has the complete N=4000 Hessian lines and an L-BFGS iteration-limit seed that is not a critical point. |
| N5 T=22 status-1 rows | hygiene; four rows quoted | **Faithful.** Verified against run_bign_Tcheck.log: n=20, e=57.25868, e_u=60.11232; n=80, e=773.58584, e_u=768.16233; n=110, e=1440.01593, e_u=1419.92203; n=160, e=3007.43048, e_u=2947.27994; all status=1. The parenthetical that 1950 already said the T=22 lines are status 1 and unused is correct (1950 line 12). The erratum supplies the missing row values. Last-digit differences versus the status-0 T=12/T=16 runs are at most a few units, as stated. Unused, correctly. |
| N6 I1 hypothesis and counterexample | E17-N6a PROVED given no x-legs / 4D Poincaré; E17-N6b PROVED (counterexample); I2 needs no such hypothesis | **Faithful.** The general form T^a_a − T^x_x = \|F(e_a,·)\|² is stated. NL's extra algebra T_{x¹ x¹} = ½\|f\|², T^Σ_Σ = −½\|f\|² for a pure F_{x¹ y} component is correct and yields T^Σ_Σ − T^{x¹}_{x¹} = −\|F(x̂¹,·)\|² < 0, matching 077e417d §2. |
| N7 Y15-trace "independent" | wording only; grade stays PROVED; "independent" dropped | **Faithful.** The fibre-trace requirement ε_Σ = 8k/κ² is correctly identified as using I1's required value ε_Σ = −k/κ², already forcing ε_Σ < 0. |
| N8 T5 wording | T5 stays PROVED as definitions; E17-N8 CONDITIONAL on P3c's measure | **Faithful.** The wording is now "e_u is what enters P3c's dvol₄-integrated count". Any positive fibre measure is a valid necessary condition and none is sufficient, because the obstruction is pointwise. |
| N9 S11-real scope | E17-N9 REFUTED, scoped to decoupled commuting-block sums with additive energy | **Faithful.** Multi-centre U(1)-equivariant configurations within one block are correctly left to Q0-out / ST2, which stay OPEN. |
| N10 S2-2 downgrade | E17-N10 CONDITIONAL; gap in the D(W⋆F) argument stated; bog = 0.013081 at n=1 cited; no alternative proof | **Faithful.** This is the grade change that revises the Y14 stage-2 tally from 8/9/2/1 to 7/10/2/1. |
| N11 Q0 boundary term | E17-N11 PROVED within the ansatz; [2B a a′] vanishes at both ends | **Faithful.** The required statements are present: at the S² orbit, a′ t₀ = 2a and a(0)=0 force a ~ t²; at the S¹ orbit, a → 0. The extra expansions (B ~ 1/t near the S² orbit so 2B a a′ ~ t² → 0; B ~ e^{−t} at the S¹ orbit) are consistent elaborations. PP did not re-derive the S¹ warp factor independently; the requested statement is made. |
| N12 Y15-int scope | wording only; stays CONDITIONAL; 398-face scan is I2 only; I1 on the 9 listed faces; optional I1 extension not run | **Faithful.** The overstatement "both necessary conditions … on all 398 faces" is withdrawn. The verdict is correctly left standing on I2 alone (min margin +2.01×10⁻² ℓ_P⁻¹). A 120×60 grid is not every point of S⁴. |
| N13 ST1 N-sequence | E17-N13 CONDITIONAL (float64, (h,a) sector, T=12 fixed) | **Faithful.** See §3. The N-sequence was computed; a T-sequence was not, and is correctly marked as not applied. |
| N14 cite OW 90cec14c | citation, no claim; placed next to 9bb1858c | **Faithful.** The file sha matches its sidecar (checked above). Junction remains UNSOLVED; the citation is a GO, not an adoption. |

Y15 no-go and the escape conditions are kept intact in E17 §2 (E17-NEC, E17-NEC-IR, E17-J7):
- NEC along ℓ_v = t̂ + v requires k_v ≤ k_x pointwise for every unit wall-spatial direction v, Σ and fibre included. NL's identity S(ℓ_v, ℓ_v) = −(2/κ²)(k_v − k_x) reproduces the IR-face value S(ℓ,ℓ) = −2k/κ² and the corollary k_v ≤ k_x for NEC-respecting content.
- On the unperturbed MN2 IR face (IR side kept), k_Σ = k_fib = 0 > k_x = −k everywhere, so every NEC-satisfying wall content fails, with margin k.
- Escape remains: either k_v ≤ k_x pointwise on S⁴, or an NEC-violating source (σ < 0 M5s, G₄ / worldvolume flux of the right sign, or a tr R² stress far larger than Y16's bound); alternatives are a different face, or keeping the UV side (negative wall energy). The integrated tr R² bound remains ~10³ too small; a per-direction check is still owed (Y15 §7).
- Y15 is a proved no-go for E₈ + σ ≥ 0 M5s with the IR side kept, not a statement about the junction in general.

## 2. Tally check
Erratum's own claims, as listed in its § header table:

| label | count | items | PP |
|---|---|---|---|
| PROVED | 5 | E17-N6a, N6b, N11, NEC, NEC-IR | **Confirmed** |
| CONDITIONAL | 3 | E17-N8, N10, N13 | **Confirmed** |
| OPEN | 1 | E17-J7 | **Confirmed** |
| REFUTED | 1 | E17-N9 | **Confirmed** |

5+3+1+1 = 10. Hygiene / wording / citation items (N1–N5, N7, N12, N14) are unlabelled, correctly.

Revised file tallies, matching 077e417d §7:

| file | as filed | revised | PP |
|---|---|---|---|
| Y14 stage 2 (20 items) | 8/9/2/1 | **7/10/2/1** | **Confirmed** (only change: S2-2 PROVED → CONDITIONAL) |
| Y15 (8 items) | 4/2/1/1 | **4/2/1/1** | **Confirmed** (wording only) |
| combined | 12/11/3/2 | **11/12/3/2** | **Confirmed** |

S4-abstract remains uncounted (PP's own item).

## 3. ST1 rerun
PP reran /workspace/nl-e17-st1/st1_Nseq_2026-11-09_1958.py from an unmodified copy in scratch /workspace/pp_nl_e17_confirm/ (start 20:01:34 CST, end 20:02:17 CST, exit 0, wall time 43 s). Log: st1_Nseq_PP_RERUN_2026-11-09.log, sha b38abc60cf9b266bc5e71c1fb3a8c5debc24a673b3693344c6434c641fc8a469 (= sidecar in that scratch directory). The 1851 modules y14s2.py and disc.py were imported and not modified.

NL's claims, checked against both the original 1958.log and the PP rerun:

- **All 9 BVPs status 0**, rms ≤ 1.0×10⁻⁸ (largest printed rms 9.999×10⁻⁹). **Confirmed.**
- **Eigenvalues converge in N to a strictly positive, N-independent limit at fixed T=12.** On every MN2 configuration the four lowest at N=4000 are 5.833987×10⁻⁵, 1.365498×10⁻⁴, 2.427727×10⁻⁴, 3.772097×10⁻⁴, matching stab_q0_run3.log when rounded to the four printed digits. The Richardson N⁻² estimate from (4000, 8000) is λ_∞ = (5.834003×10⁻⁵, 1.365507×10⁻⁴, 2.427756×10⁻⁴, 3.772164×10⁻⁴) on MN2, and (1.250546×10⁻⁴, 2.927028×10⁻⁴, 5.204008×10⁻⁴, 8.085810×10⁻⁴) on the round UV n=1 face (n=2,3 agree to 1 ULP in the last component). Residuals λ_N − λ_∞ scale as N⁻² (ratios 4.00). **Confirmed.**
- **Relative change N=4000 → 8000.** The printed relΔ values are 2.063×10⁻⁶, 5.044×10⁻⁶, 8.741×10⁻⁶, 1.328×10⁻⁵ (same on every face, up to a 1 ULP print of 5.043×10⁻⁶). NL's wording "2×10⁻⁶ to 1×10⁻⁵" slightly tightens the upper end; the accurate range is **2.06×10⁻⁶ to 1.33×10⁻⁵**. This is a rounding nit, not a change of conclusion.
- **Richardson agreement.** |λ_8000 − λ_∞| runs from 4.01×10⁻¹¹ (MN2 λ1) to 3.58×10⁻⁹ (round UV λ4), i.e. O(10⁻¹¹) to O(10⁻⁹), as stated. **Confirmed.**
- **Six lowest modes are far-end a-modes** in every case, including the two higher modes: |a|-fraction = 1, |h|-fraction = 0, peaking at t_maxa ≈ 11.35–11.86 (the last 10% of [10⁻³, 12]). **Confirmed.**
- **No negative mode** in this sector: every printed eigenvalue is positive. **Confirmed.**
- The incomplete 1957 run's n=1 twist-ON eigenvalues match the 1958 log to every printed digit, as NL said.

The PP rerun log is not byte-identical to 1958.log: a handful of last-digit ULP differences appear in printed relative deltas and in some λ_N − λ_∞ residuals (e.g. −6.418×10⁻¹⁰ vs −6.419×10⁻¹⁰). All eigenvalues, statuses, mode kinds, Richardson λ_∞ values to the printed precision, and the summary table agree. This is ordinary float64 / ARPACK variation and does not affect any claim.

**ST1 correctly stays CONDITIONAL.** The run is float64 only, restricted to the equivariant (h, a) sector, and at a single finite T=12. There is no T-sequence and no interval arithmetic. The small size of λ_1 remains a finite-T cutoff effect, now shown not to be an N-discretisation artefact.

## 4. Not applied (already marked in E17 §4); remaining items
Already marked, and correctly not counted as done:
- N10 optional alternative: no proof that rules out dW ∧ ⋆F cancelling the twist source for a self-dual F; S2-2 is downgraded instead.
- N12 optional: the 398-face scan was not extended to count I1.
- A T-sequence of the ST1 eigenvalues was not re-run (N13 asked for an N-sequence, which was computed).

**No remaining required fixes from 077e417d N1–N14.** Optional follow-ups, if NL takes them up later (not required for this acceptance):
1. Tighten the N=4000→8000 relative-change range to 2.06×10⁻⁶ to 1.33×10⁻⁵ if the interval is restated.
2. The optional 398-face I1 scan.
3. A T-sequence of the ST1 eigenvalues, if one wishes to confirm the finite-T cutoff interpretation beyond the existing 1950 remark.

## 5. Verdict
Erratum 17 is **faithful**. All 14 fixes from 077e417d are applied; S2-2 is downgraded to CONDITIONAL; I1 is stated with its no-x-legs / 4D Poincaré hypothesis; the Y15 no-go and the escape conditions (k_v ≤ k_x pointwise, or an NEC-violating source) are kept intact. Claimed tallies 5/3/1/1 (erratum), 7/10/2/1 (Y14 stage 2) and 4/2/1/1 (Y15) are confirmed. The ST1 N-sequence claims hold, with only the minor range-rounding noted in §3; ST1 stays CONDITIONAL.

Scratch: /workspace/pp_nl_e17_confirm (rerun log sha b38abc60…).
Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
