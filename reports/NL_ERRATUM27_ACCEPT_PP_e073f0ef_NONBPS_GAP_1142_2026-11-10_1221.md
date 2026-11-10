# NL ERRATUM 27: accept PP e073f0ef (audit of NL e7312edb, non-BPS tension-minus-charge gap, D-B3)
2026-11-10, written 12:23:15 CST (America/Chicago). **NL derived proposal.** Author: Non Local Path (NL). Additive only. No existing file is edited, renamed, deleted or chmod-ed; the 1142 filing, its sidecar, nonbps_gap.py, nonbps_gap_run.log and their sidecars stay frozen, and this erratum records the fixes. Wording: resonant algebra.
Frozen targets (read and hashed only, each sha = its sidecar):
- NL 1142 NL_DERIVED_NONBPS_TENSION_CHARGE_GAP_MAKEUP_2026-11-10_1142.md = e7312edb8e4b5ad3d104c779688d7842a9e7b5deb3aaafe6176de1bfe94fe4bd (mode 644).
- /workspace/nl-e8-nonbps-1130/nonbps_gap.py = e483f4b183773da0e3791cacc0ba27d93f56e55cbba8fc4a4208d29af5dbbe12 (444).
- /workspace/nl-e8-nonbps-1130/nonbps_gap_run.log = bf2484a6718be693dcca5802c8f8bf6791894b9f8213cf738f0adf4f3b7c6402 (444). Clean run, exit 0, **23/23 PASS** (23 `[PASS]` lines, 0 `[FAIL]`; a naive `grep -c PASS` of 25 counts the summary lines).
- Frozen 1120 (79ad0c64), e8delta.py, e8delta_run.log, PP 5cf92795, NL Erratum 26 (a44b18d9), and PP confirm of Erratum 26 (f2e64d44, FAITHFUL, 11:50:00 CST): not edited. The 12:05 gap and junction filings (debc7d52, dff93e21) are not edited and are not adopted; they remain a separate unaudited package.

Input: PP audit FINDINGS_PP_AUDIT_NL_NONBPS_TENSION_CHARGE_GAP_e7312edb_2026-11-10_1211.md, sha e073f0ef804d788043a08c0d06d6e5b3a0e288dca3695c9f194fc69d14350bca (= sidecar; written 12:11:36 CST; mode 444), read in full. PP evidence (read-only) /workspace/quantum-comp/reports/evidence_pp_audit_nl_nonbps_gap_e7312edb_2026-11-10/: nonbps_gap_copy.py and nonbps_gap_rerun.log byte-identical to NL's frozen files (e483f4b1… / bf2484a6…); pp_exact_checks_v2.py 90f085ccca81e8126226ea7ba55de55decdf5b92ccaa81c2d8470b1516a2f3ff; pp_exact_checks_v2.log 62a3ece066f7048ff97f43cff144a94c5014d3af6dcc17d96ca723e6c4da9b48, 32/32 PASS, exit 0 (a second run byte-identical). PP's v1 draft is disclosed in that directory and is not used.
Authority: OW 1130 (945d81bb…), OW 1117 (bff79185…), OW 1108 (c6375f85…), standing OW t4436 (32881263…), OW t4431 (f700141d…), OW t552u (eae1b39d…). Each re-hashed = sidecar. PP 1211 checked the 5cf92795 restatements directly, not against Erratum 26; that is the right source. Erratum 26 is already confirmed FAITHFUL (f2e64d44) and is not an input to these scope fixes.
Not adopted: N = 4880 and charge 9760, and the test targets Δ_N(IR) = 14043/5 and Δ_N(UV) = 19520/3, remain **labelled CONDITIONAL test targets**. 1a and B1-c2′ are not adopted. The E₈ wall sector stays CONDITIONAL, gated by backreaction (O5). Nothing adopted by fiat. **Junction: UNSOLVED.** D-B3 stays unclosed. No CERT, no Gemini, nothing sent at write (no agent messages, no external sends). Tip 7cddb188… checked before and after the write.

**Tally: PROVED 0 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · total 0.**
This erratum contains **only bookkeeping, scope relabels and premise restatements**. Distinct new claims (for any roll-up): **0/0/0/0**. No label class of any 1142 row changes.

## 1. Accepted ruling
- **Grades stand: 1142 = PROVED 16 · CONDITIONAL 6 · OPEN 6 · REFUTED 1 = 29.** No row changes label class. Only the mandatory scope relabels of §10 apply.
- Integrity: all hashes match; 23/23 PASS; PP's re-run is byte-identical; no float or nsimplify issues in the frozen tests (PP M-1–M-4 are nits only).
- **D-B3 is correctly left unclosed.** What is PROVED is only the integrated sign at u ≥ 1 (A1, as scoped in Fix 7) and the off-shell kinematics at n = 0 (A5, as scoped in Fix 1). Fixed-face on-shell (A6), [u=1] flow (A9′), profile (A12) and backreacted (A15) closure stay OPEN. [u=2] flow closure (A9) stays CONDITIONAL on gates (i)–(xi) (Fix 4). A13 is REFUTED only under its stated hypotheses and does not close D-B3 or the junction. D-B3 stays OPEN in 1120's ledger.
- Other standing tallies are unchanged by this file: t4436 menus, Bridge C (PARTIAL), the parent E₈ ledger, 1120's ruled 22/16/5/2, 1800 as revised, Y14 stage 2 (7/10/2/1 per 077e417d), and Y16. The E₈ wall sector stays CONDITIONAL (gated by O5). The 12:05 filings are not regraded here.

## 2. Fix 1 (priority) — A5 scoped to n = 0
A5 stays **PROVED**, with its statement restricted to **n = 0**: for any u > 0 and any Δ_N ≥ 0, there is an off-shell charge-0 configuration with ε_ex = Δ_N (A3 + Q9 + connectedness; N₋ = 0, N₊ = Q). "Not a closure; off shell" stands. The literal [u ≠ 1] clause "every target Δ_N − (u−1)n ≥ 0" overclaims for n ≠ 0 and is not to be read that way.
- For **n > 0** the extension is **CONDITIONAL on A4** (Taubes / grafting, cited, not re-checked). Only targets ≥ ε_ex(A₀) for an exhibited charge-n A₀ are proved without A4.
- For **n < 0** the filed "target ≥ 0" is false as written. GB2 gives ε_ex ≥ 2u|n|. The condition must be **target ≥ 2u|n|**. Counterexample: u = 2, n = −1, Δ_N = 0 gives target 1 < floor 4 (PP Q1g).
The citation in A4 is not upgraded.

## 3. Fix 2 (priority) — GB8 sign of 2N₋
GB8 stays **PROVED** as an IVT lemma for continuous g on a compact interval, after the sign fix:
**g(b) := u·e_u(n,b) − n + 2N₋ − Δ_N(b)**
(PP Q1e/f). Closure is T − Q − Δ_N = u·e_u − n + 2N₋ − Δ_N. As filed, g = u·e_u − n − 2N₋ − Δ_N differs from that by −4N₋, so "g(b*) = 0 i.e. integrated closure" is false for N₋ > 0. It is correct at **N₋ = 0**, which is R9's form and A9's case; A9 is unaffected. No class change.

## 4. Fix 3 (priority) — GB3, A7 and A11 scope
GB3 stays **PROVED** for the stated equation, with required scope (GA7a / PP fe0c3d92 Y6-math, as restated in 5cf92795 §3.4):
- the stated equation is the **source-free** D(W⋆₄F) = 0;
- on a **constant** (unbackreacted) face, with W = c_x²c_Σ ∝ Δ̃ so that dW = dΔ̃;
- for fields with **fibre-only legs and fibre-only dependence**;
- W real-analytic and non-constant;
- the full HW system is GA7b, CONDITIONAL.
The row heading "warped face … every smooth static charged E₈ field" must not be read beyond that class. **Twisted (Σ-legged, sourced) blocks are not covered.** The Y14 stage-2 blocks used in A9 have an F_tot = F_fib^hor + Φ·π*F_tw ΣΣ leg (Y14 T1) and solve D(W⋆F_fib) = (twist source) ≠ 0, so GB3 does not apply to them.
A11 stays **PROVED** with the same scope as GB3 (GB3 local form). A7 is rescoped in Fix 6. For twisted blocks, GB4's on-shell virial and GB6′ do not apply as stated (a source term appears).

## 5. Fix 4 (priority) — A9 gates and attribution; A9′ stays OPEN
A9 stays **CONDITIONAL**, an implication of gates (i)–(xi). It does not close D-B3. N = 4880, charge 9760, 14043/5 and 19520/3 appear only as labelled CONDITIONAL test targets. N₋ = 0 in A9, so Fix 2 does not affect A9. Gates (ii)–(vi) as filed stand.
Required additions and the attribution fix:
- **(vii) branch continuity is assumed** for n ≈ 115 (Y14 S2-c computed this only for n = 1–3).
- **(viii) UV landing (new gate):** the same branch must reach, at the UV end, a field with e_u(UV) < 19865/6 at n = 115 (PP Q10c). Round S⁴ has non-SD equivariant critical points, so this is not automatic.
- **(ix) the UV is a limit** (c → 0, R/R₀ → ∞). Either g extends continuously to that limit, or a finite b₂ with g(b₂) < 0 must be exhibited.
- **(x) continuity of Δ_N(b)** along the flow: on record only as interior float prints (Y14 §5).
- **(xi) attribution:** replace "the closing configuration is strictly non-BPS at b* (GB3)" with **"(Y14 S2-2, CONDITIONAL per PP 077e417d)"**. Citing GB3 for a twisted block is wrong (Fix 3).
**A9′ [u=1] stays OPEN.** No extrapolation past n = 160 is used. Read "places this just beyond its computed range" as **"not reached within the computed range n ≤ 160 (e_u)"**. A9′'s OPEN status depends on taking the x-tension to be e_u (unweighted), which 1142 defines in the header and which belongs with the D-B1 premise "x-tension = energy density"; that choice is stated here explicitly. Y14's **e**-column (weighted) gives an in-range bracket (155, 160].

## 6. Fix 5 (priority) — V′ headline scopes
V′ stays **CONDITIONAL**, sense by sense. Two headline overreaches are restricted:
- (a) "kinematically yes, with continuous tuning and no quantization (A5)" carries A5's **n = 0 scope** (Fix 1).
- (b) "Any smooth static closing field is strictly non-BPS (GB3, A7)" is replaced by: **on constant warped faces, for fibre-only fields obeying the stated equation (GB3); twisted blocks CONDITIONAL (Y14 S2-2)**. The round UV face (W constant) is outside GB3.
The other senses stay as labelled: A1 PROVED (u ≥ 1, source set, Fix 7); A6 OPEN; A9 CONDITIONAL / A9′ OPEN; A10–A12; A13 REFUTED as scoped; A14 CONDITIONAL; A15 OPEN.

## 7. Fix 6 (priority) — A7 wording
A7 stays **PROVED** as an implication, with GB3's scope (constant warped face, fibre-only, source-free stated equation), u = 1, and N₋ = 0. Drop "can only be realized by zero-size (point) instantons." Read instead: **it is not realized by any smooth static fibre-only field in GB3's class; a realization would need zero-size objects, whose identification with M5s is I (CONDITIONAL).**

## 8. Fix 7 (priority) — A1 bookkeeping premises and u < 1
A1 stays **PROVED** as an implication at [u ≥ 1]. The label must name the bookkeeping premises: **R5, S1, N, and x-tension = energy density** (the D-B1 premises), plus the source set {E₈ YM, positive-tension M5/anti-M5}. C∧X₈ (S4) is outside the source set and is OPEN. T = N₊ + N₋ + u·e_u and Q = N₊ − N₋ + n.
The u ≥ 1 scope is sharp: at **u < 1** a negative Δ_N is kinematically closable (PP Q1c: u = ½, n = Q, BPS, N± = 0 gives T − Q = −Q/2 < 0). Only N_req ≥ uQ survives there. A2 stays PROVED (Q1d), with that u < 1 companion stated. On-record Δ_N test targets 14043/5 and 19520/3 are > 0 (PP Q10a), so A1 does not fire on them; they remain unadopted CONDITIONAL test targets.

## 9. Non-priority nits (all absorbed; frozen files not edited)
- **N-1.** A9′ wording and the e vs e_u choice: absorbed in Fix 4.
- **N-2.** A10: the label carries **[u ≥ 1]** and **GA2/P-b** (CONDITIONAL set-up). A10 stays PROVED as an implication (pointwise P1).
- **N-3.** GB2: n_inst ≥ 0 ↔ SD is under the trace/orientation convention of the filing; W5 holds for both orientations (PP Q3). GB2 stays PROVED.
- **N-4.** C3's comment factor is **(X_b − X_a)²**, not (X_b − X_a). GB6 may (and does, below) say the fibre is **conformally flat iff X_a = X_b on this family** (PP Q5). GB6 stays PROVED and is strengthened to that biconditional. The round-fibre no-go (GB5) does not transfer to MN2 faces; A8 already says GB5 does not apply, and A8 stays OPEN. This strengthening is not evidence that static non-BPS fields exist and is not a no-go.
- **N-5.** A13(b) holds for a **general** 10D E₈ field (including electric and x-legs) and for any positive-tension brane with ≤ 4 fibre directions in its worldvolume (PP Q8). The restriction to "magnetic Y₆ fields" and the M5 orientation (t, x, Σ) is not needed for (b). This remark does not raise any grade. A13 stays **REFUTED only as an implication** under J1 (CONDITIONAL, CLP/BBBW), constant unbackreacted end faces, IR-kept pairing (ρ_req > 0), source set {E₈ YM, positive-tension branes}, tr R² at leading 1/N only (CONDITIONAL at N = 4880), and C∧X₈ OPEN. It is not a refutation of J1, of the geometry, or of the E₈ wall sector, and it does not close D-B3 or the junction.
- **N-6.** GB0: the p₁ step is **for every smooth connection on TM|_{S⁴} (closed smooth fibre)**, as in 5cf92795 §3.3; backreacted point sources = O5. Label **"(p₁ step)"**; the charge equation with no curvature term is the HW Bianchi identity, **R5 CONDITIONAL**. GB0 stays PROVED (p₁ step only). The struck D-A sentence is not reused.
- **N-7.** A6: "codimension-1 coincidence" is a **heuristic, not proved**. A6 stays OPEN.
- **N-8.** K2 takes F_A and D_A a as unconstrained symbolic 2×2 matrices (not su(2)-valued); harmless, because the t⁴ coefficient does not involve them. Z1, F2 and I1–I3 are bookkeeping comparisons of inputs, not tests of the geometric chain.
- **N-9.** The frozen log has no RUN_START wall-clock line; "frozen before the run" is supported only by mtime order (script 11:39:35.528 < sidecar 11:39:35.532 < log 11:39:39.488). Nit only; the frozen log is not edited.
- **N-10.** Mode 644 on the 1142 filing and its sidecar is NL convention. Recorded as optional/nit only; **no chmod** is done. This erratum and its sidecar are also 644, consistent with the NL erratum series.

GB7 stays PROVED as filed (first variation of E_W along a C¹ family of critical points; no external continuous parameter). GB6′ stays CONDITIONAL (Ferrand–Obata not re-checked), with the twist-source remark of Fix 3. A8 stays OPEN, with that same twist-source remark. A12, A15 and A16 stay OPEN. A14 stays CONDITIONAL. A15's GB3 transfer stays "CONDITIONAL on the static equation holding there." No backreacted metric is constructed or ruled out (MR2's job).

## 10. Mandatory tally-line relabels (PP findings §7)
Applied to the 1142 tally as reading scope; counts unchanged:
- **A1** "PROVED: implication of R5, S1, N, and x-tension = energy density, source set {E₈ YM, positive-tension M5/anti-M5}, [u ≥ 1]; at u < 1 a negative Δ_N is kinematically closable";
- **A5** "PROVED only for n = 0 (any u, any Δ_N ≥ 0); n > 0 CONDITIONAL on A4; n < 0 requires target ≥ 2u|n|";
- **GB3, A7, A11** "PROVED (stated equation) on a constant unbackreacted face, fibre-only legs and dependence, source-free D(W⋆F) = 0; twisted blocks not covered";
- **A7** additionally: "not realized by any smooth static fibre-only field in that class; zero-size objects need I (CONDITIONAL)";
- **GB8** "PROVED after sign fix: g = u·e_u − n + 2N₋ − Δ_N; as filed, the sign of 2N₋ is wrong except at N₋ = 0";
- **GB0** "PROVED (p₁ step) for every smooth connection on TM|_{S⁴} (closed smooth fibre); charge equation R5 CONDITIONAL";
- **GB6** "PROVED; on this family conformally flat iff X_a = X_b; GB5 does not transfer to MN2";
- **A9** "CONDITIONAL on gates (i)–(xi), including assumed branch continuity at n ≈ 115, UV landing, UV-as-limit, Δ_N(b) continuity, and strict non-BPS by Y14 S2-2 (CONDITIONAL, 077e417d), not GB3";
- **A9′** "OPEN: not reached within the computed range n ≤ 160 (e_u)";
- **A10** "PROVED as implication, [u ≥ 1], GA2/P-b";
- **A13** "REFUTED only under the stated hypotheses (§9 N-5); does not close D-B3 or the junction";
- **V′** "CONDITIONAL, sense by sense, with A5's n = 0 scope and GB3's class for the strict non-BPS claim (twisted blocks via S2-2, CONDITIONAL)".

1142 tally as ruled: PROVED 16 (GB0, GB2, GB3, GB4, GB5, GB6, GB7, GB8, GB9, A1, A2, A3, A5, A7, A10, A11) · CONDITIONAL 6 (GB1, GB6′, A4, A9, A14, V′) · OPEN 6 (A6, A8, A9′, A12, A15, A16) · REFUTED 1 (A13) = 29.

## 11. Tallies of earlier files (unchanged)
| file | tally |
|---|---|
| NL 1142 (e7312edb), as ruled by PP e073f0ef | 16/6/6/1 = 29, with the §10 relabels |
| NL 1120 (79ad0c64), as ruled by PP 5cf92795 and Erratum 26 (FAITHFUL, f2e64d44) | 22/16/5/2 = 45 |
| NL 1711 | 11/10/4/0 |
| NL 1800, as revised | 13/11/3/2 |
| NL Y14 stage 2, PP 077e417d | 7/10/2/1 |
| NL Y16; Errata 24–26 | unchanged; E24–E26 are 0/0/0/0 each |
| NL 1205 gap (debc7d52) and junction (dff93e21) | unaudited; not regraded here; not edited |

No previously ruled grade changes. Refutations: none new.

## 12. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 0 | — |
| CONDITIONAL | 0 | — |
| OPEN | 0 | — |
| REFUTED | 0 | — |

Check: 0 + 0 + 0 + 0 = 0 (bookkeeping, scope relabels and premise restatements only). Header = body.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before and after the write (re-hashed after; reported back). Never opened for writing.

Nothing adopted. Junction UNSOLVED. No CERT. D-B3 is not closed. Resonant algebra.
