# PP confirmation: MR2 erratum 0f635774 (per PP 60293840)
Written 2026-11-09 2221 CST by Professor Proof. New additive file in reports/ only. Nothing was adopted, and nothing was written into MR2's directories. Tip 7cddb188… was re-hashed and is unchanged.

## Integrity
- MR2_ERRATUM_BRANCH_FIVE_FILES_PER_PP_60293840_2026-11-09.md: sha 0f6357745f045edb… = sidecar ✓ (mtime 22:20:46).
- The five targets are unchanged: 4c618493, c5a65972, 04b94770, 3da6285a and db06bd2c, each matching its sidecar. Citation 8399be55 ✓; PP 60293840 ✓.
- **No c2 work.** No new file has appeared in /workspace/mr2-branch-2134/ since 22:08:04 (L1_Nprime_roots). The only new MR2 report after db06bd2c is this erratum. The files named *oc2* in evidence_local_t4436_branches are Local's and unrelated to B1-c2. ✓

## Fix-by-fix
1. **Rc-1 interval → [0.04051, 0.04548].** This is PP-certified, with arithmetic PROVED and the thin-wall reading COND. **Faithful.**
2. **L1 values.**
   - μ₁ = 1/3, μ₂ = 1/4: MR2 quotes −1.161192993378910693…, citing frozen log 264fdf1d (value −1.161192993378910693119096).
     - PP's closed-form interval evaluation (pp_L1_TW2.log b62caad3) gives −1.16119299337891069311909579…. **Match** ✓.
     - Log 264fdf1da0d77ef2… = its sidecar. Script 2f2b9d4f1d974934… = its sidecar. The script sidecar is older than the log (22:02:59 → 22:03:25), so the script was frozen before it ran ✓.
     - Nit: the log's sidecar was written at 22:08:04, about 4.7 min after the run. The log is unchanged, but db06bd2c's "sidecars MATCH" should note that the log sidecar was written after the run.
   - (1/2, −1/5): MR2 quotes −2.10578925447730, which agrees with PP's −2.105789254477301124531… ✓. This value comes from PP and the v3 log, printed to 15 digits, **not** from 264fdf1d: that log evaluates only (1/3, 1/4), and MR2's erratum attributes it correctly.
   - The width claim is withdrawn and the grade is unchanged. **Faithful.**
3. **Lemma TW.** P-iii (a: null Einstein equation inside the wall; b: flux NEC) is added. The lemma and "2b REF" are now implications of P-i, P-ii and P-iii. The 113.26 ℓ_p threshold is stated as a proper width at (9/10, 1/10), with 41.50 and 39.60 at the other points. **Faithful.**
4. **E1.** The y⁻² factor is added. D = 2^{1/5}Δ³(p−2)²(2^{3/5}Δ² + 4Δp + 2^{7/5}p²), equivalent to MR2's d-form under d³ = Δ, as in PP's exact reduction. **Faithful.**
5. **E2 coverage.** μ₀ < 0 follows from the μ₀ → −μ₀ isometry. At μ₀ = 0 the chart switches, using P_{xyμ₂φ₁} ≡ 0. μ₁ = 0 is covered by the Cartesian argument. E3 stays COND. **Faithful.**
6. **Premises.** K1 on shell is stated for T3-6, and the G₂ ⊂ Spin(7) spinor stabilizer for T3-7. **Faithful.**
7. **Batch-2 tally.** 8/3/1/4 = 16. **Faithful.**
8. **B1-c2.**
   - Keep criterion (PROVED): the (i′)/(ii′) re-derivation on the doubled MN2, i.e. the Pin lift exists, commutes with W̃, and is compatible with HW chirality.
   - Drop criterion (REFUTED): a proof of inconsistency.
   - Next computation: the spinor lift of P∘r on Σ × S⁴ with the twist (~1–2 h), only if the Owner allows it.
   - It is labelled "parked pending Owner ruling", and the conflict is recorded as a scope conflict, not a REF.
   - No c2 work was done. **Faithful.**
9. **Register table.** All post-audit grades match PP 60293840 §3, and the tally is 14/4/3/5 = 26 (8/3/1/4, 4/0/2/1, 2/1/0/0). The carried tallies are ff7fb67f 10/3/2/0 and BPS 14/2/1/1. **Faithful.**
   - Note: the table is in the erratum. c5a65972 itself is unedited (additive rule ✓), so readers of the register must read it together with 0f635774.

## Verdict
**FAITHFUL: all nine fixes are applied as specified, with no grade changes.** PP tally unchanged: **14 PROVED · 4 COND · 3 OPEN · 5 REF = 26**. Nothing is refuted.

**Optional nits for a future additive note:**
- (a) Note that the 264fdf1d sidecar was written after the run (22:08:04).
- (b) Add a pointer from the register's header to 0f635774 in the next register revision.
