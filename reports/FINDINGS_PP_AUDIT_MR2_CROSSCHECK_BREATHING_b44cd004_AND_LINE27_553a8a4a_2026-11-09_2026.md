# FINDINGS: PP audit of MR2 breathing cross-check (b44cd004) and MR2 line-27 note (553a8a4a)
Auditor: PP (Professor Proof), Soft SF audit agent. Written 20:26 CST (America/Chicago). Scope: OW d5eaeef3, OW 90cec14c.
- Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only = COND. A citation alone is never PROVED. A stated premise is graded as an implication. Refutation is by proof or counterexample only.
- Additive; nothing edited; nothing sent; no CERT; no Gemini; nothing adopted. "Resonant algebra" naming.
- Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, unchanged.

## 1. Provenance
| file | sha256 (recomputed) | sidecar | mtime CST |
|---|---|---|---|
| MR2_CROSSCHECK_NL_BREATHING_MODE_CURVATURE_EFT_2026-11-09.md | b44cd00425b792f12c3772898949fc2ed735a1bab0992f4c276bb253e4c333e3 | MATCH | 20:16:18 |
| ….py | c82a524d349e98dc09ac38fe3dceb0105babbe7da16fbf19c133177d77251845 | MATCH | 20:02:03 |
| ….log (ends `EXIT 137`) | 435c340f2a325ba6aa7972f4e1ae9df69c04dd8977c83c31f49bbf2f85dcc970 | MATCH | 20:13:38 |
| …_PART2_E4_NUMERIC.py | 098bf6fce90848e713f25815ed8f223cc586bd7f18a0d75359054bb03404a05b | MATCH | 20:13:38.306 |
| …_PART2_E4_NUMERIC.log | cc90c88826f01e0693a377d57e350eebc18b79c718f2d94add9c7fe1faf85889 | MATCH | 20:14:44 |
| MR2_NOTE_9ab8f0a6_LINE27_D_PRODUCT_F0_2026-11-09.md | 553a8a4a62e288794cb2c98b72b51d69367eb1c6df16acb692f057f3616ffaca | MATCH | 20:08:09 |
- **.py before log:** both confirmed. The main log was written when the OOM kill ended the run (about 11.5 min after the .py), and PART2's .py was frozen at that moment.
- Inputs re-hashed: NL 1935 ebdda4b6, 1936 358c4b09, 1942 59a4f05e, 1943 b103f08f, 1948 9a29b6da. All present.
- **PART2 rerun** (/workspace/pp_bx_2025/part2.py, same sha): exit 0. The log is **byte-identical, sha cc90c888…**.
- **Main rerun, not full size.** I ran it under `ulimit -v 3.5 GB` with a 14-min timeout (main_rerun_capped.log 2a8aaed4…).
  - (a1) and (b) are **identical** to MR2's log lines 1–21.
  - (a2) aborted at the cap ("GNU MP: Cannot reallocate memory", EXIT 134). This reproduces the memory blow-up without a full-size run.
- PP exact script: /workspace/pp_bx_2025/pp_exact.py 83bfb414… / .log ae43fdb9….

## 2. Which claims depend on the killed run
The main script's order is (a1) → (b) → (a2) → (d), and it was killed inside (a2).
- (a1) and (b) completed. They support M1 and M3–M5.
- The original (a2) and **all of (d) never ran** in the main script.
- **M2, M9 and M10 rest only on PART2**, which completed and reproduces byte-identically.
- No claim depends on missing output. The md should say explicitly that (d) never ran in the main script (fix 6).

## 3. Independent checks
- **M3 (fixed point = (D) product): PROVED, exact.** PP checked 11D directly. AdS₅ (L² = 1), H² (ρ² = 1/4) and S⁴ (r² = 3/8) with G₄ = q·vol_{S⁴} and q² = 24 give:
  - Ric_AdS = −4 = −q²/6, Ric_H² = −1/ρ² = −4 = −q²/6, and Ric_S⁴ = 3/r² = 8 = +q²/3;
  - RHS block factors (6q² − 2q²)/12 = 8 and −2q²/12 = −4;
  - ratios 1/4 = (1/6)/(2/3) and 3/8 = (1/4)/(2/3), with R = 4 rescaling to 6 at L² = 2/3.
- **M4 (kinetic matrix): PROVED** as an implication of E0–E2, which PP grades PROVED (3982a4b8).
  - PP re-derived it from Gauss–Codazzi: ½[(tr K)² − tr K²] with K = (A′×4, B′×2, C′×4) and A′ = a′ − (2B′+4C′)/3 gives 6a′² − (5B′² + 8B′C′ + 14C′²)/3, with no a′ cross terms.
  - With 6ȧ² − ¼Kφ̇φ̇ + ½V = 0 for L = R − ½K(∂φ)² − V, this gives K = [[20/3, 16/3], [16/3, 56/3]].
  - **det K = 96 exactly**, tr = 76/3 > 0, so K is positive definite. Eigenvalues (38 ∓ 2√145)/3 = 4.63894 and 20.69440.
- **M5 (S1 masses 8, 48): PROVED, exact, toy vacuum.**
  - PP built V independently from −R_int + |G|²/2 (L = R − G²/48): V = e^{−2w}[2e^{−2B} − 12e^{−2C} + Q²e^{−8C}/2] = 2Ue^{−2w}, which matches MR2's U.
  - At the point: ∇V = 0, V₀L₅² = −12, and K⁻¹Hess·L₅² has eigenvalues {8, 48}, eigenvectors (1 : 0) and (−4/5 : 1). Δ = 2+2√3 and 2+2√13.
  - Scope: the (D)-type singlet toy, not MN2. M6 says so.
- **M1 (E1 vs 11D, about 1e-40): COND (float).** Rerun identical. The control works by construction: A″, B″ and C″ are recomputed from the scaled q², so the second-order equations still hold and only the constraint fails. But the log asserts "in yy only" without printing per-component residuals (fix 4). This agrees with PP 3982a4b8's exact PROVED for E1, which is not changed.
- **M2 (E4 on the V2 MN2 metric, 1.19e-15): COND (float).** PART2 is identical.
  - PART2 does **not** use mp.diff or analytic derivatives. It uses central finite differences, h = 1e-12 for first and 1e-8 for second derivatives, at dps 50. That is why the control gives R = 5.99999999999999075 (error ~1e-14) and not ~1e-40 (fix 3).
  - The β′ = 0 control gives ~1e-16.
  - This agrees with the closed-form E4, PROVED in PP 3982a4b8/fb515bef and NL 1942. The S⁴ block scaling includes the twist cross terms (G[5,φ], G[5,5]) as stated.
- **M7 (K1 vs ecee2668 §7): PROVED** (comparison of stated values). ecee2668 §7 lists −4 (Δ = 2) and 12 (Δ = 6, mixes with h), and PP 99593076 grades K1 PROVED.
- **M9 (EFT arithmetic): PROVED as arithmetic on stated inputs.** ℓ = 2(πN)^{1/3} = 49.6843821928 and L₅ = ℓ·2^{−2/5} = 37.6537205933. Then 12/ℓ² = 4.86118e-3, √3408/ℓ² = 0.0236488, its cube 1.3226e-5, and 0.028464² = 8.102e-4. The input statuses carry over: sup Riem² = 3408 is COND (ERRATUM3 W6), and the hard-coded R_max = 12/ℓ² and k-range [0.025358, 0.028464] need source citations (fix 7).
- **Batch 1 unchanged (M12, M13, M16).** These are consistent with PP's standing grades: uniform breathing REFUTED (fb515bef: β′ ≡ 0 forced); T9/T10 OPEN; K6 OPEN, K6′ COND (99593076); K4 PROVED. L3 and B5 premises are untouched by NL's files. Agreed.
- **Per-NL table.** MR2's "PP grade" column matches PP 3982a4b8 (E1 PROVED; E3 REF; E4 PROVED; E10 PROVED; S1 PROVED), fb515bef (T tally 6/1/3/1) and 99593076 (K1 PROVED; K2 PROVED with the Δ = 4 sub-clause COND; K4 PROVED; K6 OPEN with K6′ COND; K8 PROVED).

## 4. Line-27 note (553a8a4a) and PP 2cf2630b
- **V2 (ad134752) facts: CONFIRMED.**
  - Line 327 reads `# product validation inside the candidate ansatz: X=1, a=0, F0=2/3, G0=1/6 (KR (D) metric)`, and line 328 has parD = [1, 1, 2/3, 1/6, 0, 0].
  - The V2 log (49d0562c…) line 17 gives K = 618, RicSq = 828, R = 6.
  - There is no "4/9" in the V2 .py.
  - 9ab8f0a6 line 27 does read "e^{2f} = 4/9 so that L_AdS5 = 2/3", which is an md text slip.
- **MR2's broader claims are REFUTED by counterexample.** MR2 writes "No 4/9 appears in the code", "The only '4/9' in the record is the md slip" and "The brief said 4/9 is the coded control value. It is not."
  - MR2_BATCH2_SEC10_PHI_ON_MN2_RICCI_SCALAR_CHECK_2026-11-09.py (sha 516438eb…, frozen, the file PP audited in 2cf2630b §0) **codes F = 4/9**. Line 65 reads `control: (D) product in-ansatz X1=X2=1, a=0, F=4/9, Gs=1/6 (expect R=6)` and line 66 reads `run("D", {…, F: sp.Rational(4,9), Gs: sp.Rational(1,6)})`.
  - The log line 1 of that script repeats it. Exactly: −20/(4/9) − 2/(1/6) + 12/(1/4) = −45 − 12 + 48 = −9.
- **PP's 2cf2630b line was NOT wrong.** "The control coded F = 4/9 (R = −9)" referred to the batch-2 §10 script 516438eb (2cf2630b §0 custody row; §1 line 32 and fix 3 say "the frozen script codes F = 4/9"). It is literally true of that file. The same paragraph says (D) has F = 2/3 and R = 6, which matches the V2 code.
  - **No PP correction is required.** Optional additive clarification: 2cf2630b's "coded F = 4/9" means file 516438eb lines 65–66, not V2 ad134752.
- **MR2's retraction is misplaced.** MR2 retracts its earlier "coded 4/9" statement. If that statement referred to 516438eb, which is the batch-2 context, the retraction is itself wrong and should be withdrawn (fix 1).
- 2cf2630b fix 3 (relabel the 516438eb control, which is not (D)) stands.

## 5. Per-claim table
| # | claim | MR2 | PP | reason |
|---|---|---|---|---|
| M1 | E1 vs 11D, ~1e-40; constraint = yy equation | COND | **COND** | float; "yy only" not printed |
| M2 | E4 on V2 MN2 metric, 1.2e-15, both angles, any γ | COND | **COND** | float (finite differences); PART2 identical |
| M3 | fixed point = (D) product | PROVED | **PROVED** | PP exact 11D check |
| M4 | K = [[20/3,16/3],[16/3,56/3]] PD, no ghost | PROVED | **PROVED** | implication of E0–E2 (PROVED); det 96; PP re-derived |
| M5 | S1 masses 8, 48 | PROVED | **PROVED** | exact; toy (D)-type vacuum only |
| M6 | toy masses ≠ MN2 masses | PROVED | **PROVED** (core) | Fix 2: "lowest Group A spin-2 level above 0 is 46.157" contradicts MR2's own stage 1 (8ca7b93a: 12, 20, 32, 40, COND), so restrict to S⁴-constant modes. The 23.0786 / "(0, 25.5)" inputs are COND (ed0e5bd6). |
| M7 | K1 = ecee2668 §7 | PROVED | **PROVED** | verified |
| M8 | NL counting consistent with KK truncation | PROVED | **PROVED** | implication given T7 (PROVED) |
| M9 | EFT numbers | PROVED | **PROVED** (arithmetic) | inputs 3408 (COND) and k-range carried |
| M10 | R⁴ ~ 1.3e-5, two-derivative EFT holds | COND | **COND** | power counting, O(1) coefficient |
| M11 | toy-trajectory curvature | OPEN | **OPEN** | — |
| M12 | L3, B5 unchanged | PROVED | **PROVED** | scope implication |
| M13 | uniform breathing closes MN2 face | REF | **REF** | fb515bef / NL 1942 P1–P3 |
| M14a | V2 ad134752 codes F0 = 2/3; 9ab8f0a6 line 27 "4/9" is an md slip | PROVED | **PROVED** | read from frozen files |
| M14b | "no 4/9 in the code; only 4/9 in the record is the md slip; the brief's coded-4/9 is false" | (in M14) | **REFUTED** | counterexample 516438eb L65–66 |
| M15 | recommendation unchanged | COND | **COND** | on T9/T10 OPEN |
| M16 | (r,χ) route OPEN | OPEN | **OPEN** | — |
- **MR2 tally: 9 / 4 / 2 / 1 = 16.**
- **PP tally: PROVED 9 · COND 4 · OPEN 2 · REF 2 = 17 rows**, because M14 is split. If M14 is kept as one row, it is **REFUTED in part**, giving 8/4/2/2 = 16.
- Self-disclosed heading slip ("excluding M14 and M15" while M15 is counted COND): **CONFIRMED.**

## 6. Fixes
1. **Note 553a8a4a / M14.** Scope "no 4/9 in the code" to V2 ad134752. Acknowledge that 516438eb lines 65–66 code F = 4/9 (R = −9 exactly) under a "(D) product" label. Withdraw the retraction of the earlier "coded 4/9" statement if it referred to 516438eb. PP 2cf2630b stands.
2. **M6.** Replace "the lowest Group A spin-2 level above 0 is λ = 23.0786 (46.157)" with "lowest S⁴-constant (Σ-only) invariant spin-2 level". MR2's stage 1 gives S⁴-dependent invariant spin-2 at 12, 20, 32, 40 (COND).
3. **PART2 wording** (md line 23 and the PART2 header comment). It uses central finite differences (h = 1e-12 / 1e-8) at dps 50, not mp.diff or analytic derivatives. The accuracy is ~1e-15.
4. **M1 control.** Print the per-component residuals or drop "(in yy only)".
5. **Tally heading.** Change to "M1–M16 (M14 in §5)"; self-disclosed.
6. **OOM dependence.** State that (d) never ran in the main script, so M2, M9 and M10 rest on PART2 alone, and M1 and M3–M5 on the completed (a1)/(b).
7. **M9 inputs.** Cite the source files for R_max = 12/ℓ² and the k-range [0.025358, 0.028464]. Carry sup Riem² = 3408 as COND.
8. **Note section label.** The note's "(REF, read from frozen files)" heading refutes only the md slip. Make that explicit so it is not read as refuting PP.
