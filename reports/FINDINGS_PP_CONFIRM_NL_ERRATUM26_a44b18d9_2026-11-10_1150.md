# FINDINGS: PP confirm of NL Erratum 26 a44b18d9 (accept PP 5cf92795 of NL 79ad0c64, E₈ instanton stress vs the geometric delta under odd G₄)
2026-11-10, written 11:50:00 CST (America/Chicago). Author: **Professor Proof (PP), Soft SF audit.** Additive new file; no existing file edited, renamed, deleted or chmod-ed. Confirm only: faithfulness of the erratum to PP 5cf92795 §6–§7. No first-prove. **Nothing adopted.** **Junction UNSOLVED.** No CERT. Wording: resonant algebra. No message sent (no SendToAgent, no SendToUser, no external send). This confirm does not audit, use, or mix in the separate unaudited NL 1130 filing e7312edb.

## 0. Integrity (PP re-hash at confirm)

| object | sha256 (PP re-hash) | = sidecar | mode | mtime (CST) | note |
|---|---|---|---|---|---|
| NL Erratum 26 NL_ERRATUM26_ACCEPT_PP_5cf92795_E8_DELTA_1120_2026-11-10_1142.md | a44b18d945aaf2600cbafde50c6777a983c81899c47c5e545c9b5e4a0a538179 | yes | 644 | 11:42:04.084 | header "written 11:42:04 CST" = mtime to the second. Mode 644 is NL convention (PP §7 item 15, optional; already recorded in the erratum). |
| Parent NL 1120 NL_DERIVED_E8_INSTANTON_GEOMETRIC_DELTA_ODD_G4_2026-11-10_1120.md | 79ad0c6417e825d4fee8d412af62a767688b883a88c39c6a6affd716ce4ffa29 | — | 644 | 11:20:43.980 | unedited (sha and mtime unchanged from the 1137 audit). |
| PP audit FINDINGS_PP_AUDIT_NL_E8_INSTANTON_GEOMETRIC_DELTA_79ad0c64_2026-11-10_1137.md | 5cf927959babc94b1719c99b312cfbb9d6366237626c781e8d5c75f21ce15b03 | — | 444 | 11:37:34.033 | unedited. |
| /workspace/nl-e8-delta-1110/e8delta.py | 13bcf9038f6be227536e3b2209a2958259d2819df6599c6e6a721e8431db25e8 | — | 444 | 11:15:31.314 | unedited. |
| /workspace/nl-e8-delta-1110/e8delta_run.log | e9a8cfe94a21e2e7d02a87a3e8aa89cb478db707bedb50c2d1918e95426979da | — | 444 | 11:15:32.182 | unedited. PP re-count: 23 `[PASS]` lines, 0 `[FAIL]`, plus the summary line "ALL PASS". Breakdown C1a–g 7, C2a–f 6, C3 1, C4a–g 7, C5 1, C6 1 = 23. The parent still prints "26/26 PASS" on its script line (unedited, as required); the erratum supplies the reading 23/23. |
| Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | — | 644 | 2026-11-06 14:38:54 | see custody (§5). Never opened for writing. |

The erratum is additive. Frozen 1120, e8delta.py, e8delta_run.log, the 1137 audit, the tip, running Local jobs (s1e, chain_v2, s2e, wait_then_ob_v5), and other agents' directories were not touched.

## 1. Item-by-item absorb of PP 5cf92795 §7 (items 1–15)

| # | PP §7 requirement | Erratum 26 | verdict |
|---|---|---|---|
| 1 (priority) | Integrity count "26/26 PASS" → **23/23 PASS** (filing header and any later text that repeats it) | §2: the 1120 header's "26/26 PASS", and any later text that repeats 26/26, is to be read as **23/23 PASS**. Breakdown matches the frozen log (PP re-count 23/23). Frozen log and 1120 file not edited. | absorbed |
| 2 (priority, load-bearing) | N-1: fix one charge normalization. Either n_inst = (1/16π²)∫tr F∧F and n_R = −(1/32π²)∫tr R∧R to match GA3, with u := 8π²/(λ² T_M5) unchanged; or redefine u. Then restate GA12–GA14, C4a's reading, S1's M5-unit sentence, D-B1/D-B2 and R9 in that normalization. 1800 Y8 inherited inconsistency may be flagged, not regraded. | §3 chooses the first option (u not redefined). Convention and all eight restatements are actually written, not merely declared. Internally consistent; see §3 of this confirm. 1800 Y8 flagged, not edited, not regraded. Y11's "8π²\|k\|" (R7) correctly recorded as sitting in Y8's normalization. | absorbed |
| 3 (priority) | Name premises C, I, N. GA13 must read "REFUTED (conjunction u = 2 ∧ C ∧ I); HW's printed λ² alone is not refuted". Tally line follows. | §4 names (C) continuity as size → 0; (I) zero-size SD instanton at y₀ is one M5 at y₀ with energy W(y₀)T_M5 per unit charge (Y7 / Ganor–Hanany / Seiberg–Witten; CONDITIONAL); (N) unit charge ∫tr F∧F = 16π². GA12 is PROVED only as an implication of C ∧ I ∧ N, not an unconditional PROVED of u = 1. GA13 is REFUTED only as the conjunction u = 2 ∧ C ∧ I; HW's printed λ² alone is not refuted; "HW-printed ⇔ u = 2" holds only under N. Tally line in §4 and §17 matches. D-B2's "GA13 refutes u = 2 with continuity" is recorded as correctly worded; V must not shorten it. | absorbed |
| 4 (priority) | D-D / GA8 tally entries carry "given J1 (CONDITIONAL, CLP/BBBW), constant unbackreacted end faces". GA8 also "IR-kept pairing (ρ_req > 0)". Source set {E₈ YM, positive-tension branes}. V's "holds without dropping tr R²" → "at leading order in 1/N (Q11a); at N = 4880 CONDITIONAL (Q11b); C∧X₈ OPEN (S4)". | §5 writes both tally entries with the full J1 (CONDITIONAL, CLP/BBBW) and constant-unbackreacted-end-face scope; GA8 also has IR-kept pairing (ρ_req > 0), with the note that w_fib < −1 ⇔ S(k,k) < 0 needs ρ_req > 0 and that P1/P2 supply the chain (C6 alone does not). Source set named. V's tr R² sentence restated exactly as required. GA8-int stays CONDITIONAL; backreacted faces OPEN (O5). Implication-grade for D-D is stated (not a refutation of the geometry, of J1, or of the E₈ wall sector). | absorbed |
| 5 (priority) | Replace the bold unconditional "No." with the sense-by-sense headline of PP §3.5. "No" is not established in sense D-B3 or on backreacted faces (O5). | §1 and §6 replace it with the §3.5 headline verbatim: "No in senses D-A (PROVED) and D-D (given J1, constant unbackreacted end faces); CONDITIONAL in D-B1/D-C; not established in D-B3 or on backreacted faces." Explicitly: "No" is not established in D-B3 or on backreacted faces (O5). V stays CONDITIONAL. | absorbed |
| 6 (priority) | Strike or restate "instanton energy (≥ 0) does not cancel it [the tr R² wall energy]"; as an integrated statement it is false (P9). | §7 strikes the sentence from 1120 §4 D-A. Records the exact cancellation −8π²/λ² + 8π²/λ² = 0 (Y16 Q5 + one I₄-unit of BPS charge; PP P9). Existence of a static unit-charge BPS configuration on the warped face is flagged as a separate question (GA7a), not claimed. The p₁ step and D-A's "nothing to make up" (n_R = 0) stay PROVED, scoped "for every smooth connection on TM\|_{S⁴}" (Fix 8). No tally effect (the struck sentence was not a tallied row). | absorbed |
| 7 (priority) | Recast R9 as a new OPEN item ("b for a given split", x-equation only). 1711 AB2/G2-odd/G3 keep filed grades as implications of the pure-M5 premise. AB2 already contained the σ_x^ex generalization, so "their conclusions equate tension units with charge 2N_flux" is accurate for G2-odd/G3 and for AB2's special case only. | §8: R9 [OPEN, new item; not a reopening of AB2/G2-odd], "b for a given split", x-equation only, with b = N_req⁻¹(2N_flux + (u − 1)n_inst + ε_ex) in the Fix 2 convention, matching AB2's σ_x^ex form (σ_x^ex = instanton x-tension, C1a). 1711 AB2, G2-odd and G3 keep filed grades as implications of the pure-M5 premise (tension = charge, no other x-tension); that premise is dead as the working assumption, not refuted by fiat; 1711 is not regraded. The 1120 sentence is scoped as accurate for G2-odd/G3 and for AB2's special case ("N_b = 4880 has none") only, not for AB2's general relation. Fibre and Σ blocks still need non-E₈, NEC-violating content at the end faces (D-D/GA9), as in AB1's (a)+(b) premise. | absorbed |
| 8 (nit) | GA4: "for every metric" → "for every smooth connection on TM\|_{S⁴} (closed smooth fibre)"; backreacted localized M5 points fall under O5. | §9, plus the charge-equation part of GA4 stays CONDITIONAL (R5). | absorbed |
| 9 (nit) | GA7a: add "constant face; fibre-only legs and dependence (fe0c3d92 Y6-math)"; "M5-like" = point support (identification = Y7/I, CONDITIONAL). | §10, and GA7b = Y6-phys, CONDITIONAL, unchanged. | absorbed |
| 10 (nit) | GA11: name P-b for the flux doubling. | §11: PROVED as an implication given P-b; C5 is a tautology; [G_tan] doubling needs GA2/P-b (CONDITIONAL). | absorbed |
| 11 (nit) | D-B2: "only if both fail" → "requires u ≠ 1 and ¬C; ¬GA7b is additionally required under I". | §12, verbatim, with the without-I remark and the n_inst targets recorded as CONDITIONAL, unadopted prints. | absorbed |
| 12 (nit) | R8 wording: "holds if u = 1, or under GA7b with I". R3: mark Y4-end and E2-end "given J1". R11: name I1's no-x-legs premise. | §13: all three. R8 stays CONDITIONAL. R3 stays PROVED (bookkeeping), members Y4-end and E2-end PROVED given J1. R11 stays PROVED (bookkeeping); Y15-IR's REFUTED is scoped to the IR-kept side, σ ≥ 0 (as in the 1137 row table). | absorbed |
| 13 (nit) | C4e: "5/3 exactly as the arithmetic of N_req^UV = 10N/3 (given J1); 16266.7 is its print"; C4e is by construction. C4a: note `nsimplify`. C5, C4g and C6 are bookkeeping comparisons, not tests of the geometric chain. | §14: all of this, including 48800/3 at N = 4880, `Fr(10*Nf,3)`, 16266.7/9760 ≠ 5/3, and C4a's exactness via sympy evaluating to the integer before `nsimplify` (PP P7b, `cancel`). Also records that C4d–C4g numbers are CONDITIONAL, unadopted test targets and support no PROVED grade. | absorbed |
| 14 (nit) | GA3 "rank 248" → "dimension 248". S2/D-B3: specify the sum in ½Σ(F − ⋆F)² (3 pairs, = ¼ over all 6 a<b). | §15: "dimension 248" (E₈ has rank 8, dimension 248). The ½Σ sum is over the 3 pairs {(12,34), (13,42), (14,23)}, equal to ¼ of the sum over all 6 a<b (= ⅛ over ordered pairs; PP P4). GA6 is included with S2/D-B3, which is consistent (GA6 already used that sum). | absorbed |
| 15 (nit, optional) | Mode 644 on the 1120 filing and sidecar (NL convention): optional. | §16: recorded as optional/nit; **no chmod** is done. The erratum itself is also 644, consistent with the NL erratum series. | absorbed (optional; no action required) |

No item is missed. No item is incorrectly absorbed. No grade is moved.

## 2. Mandatory tally-line relabels (PP §6)

Applied in the erratum §17 as reading scope of the 1120 §7 tally; counts unchanged:

| relabel | PP §6 | Erratum §17 | verdict |
|---|---|---|---|
| GA8 | "given J1, constant unbackreacted end faces"; also "IR-kept pairing" | "PROVED given J1, constant unbackreacted end faces, IR-kept pairing" | absorbed |
| D-D | "given J1, constant unbackreacted end faces" | "REFUTED given J1, constant unbackreacted end faces" | absorbed |
| GA11 | "given P-b" | "PROVED given P-b" | absorbed |
| GA12 | "implication of C ∧ I ∧ N" | "PROVED: implication of C ∧ I ∧ N" | absorbed |
| GA13 | "REFUTED: conjunction u = 2 ∧ C ∧ I, not HW's printed λ²" | same | absorbed |
| R3 | "members Y4-end and E2-end given J1" | "PROVED; members Y4-end and E2-end given J1" | absorbed |
| R9 | "new OPEN item, not a reopening of AB2/G2-odd" | "OPEN: new item, not a reopening of AB2/G2-odd" | absorbed |

The fuller phrases required by §7 item 4 — "J1 (CONDITIONAL, CLP/BBBW)" and GA8's "(ρ_req > 0)" — sit in the erratum §5 tally-entry wording, which is the right place. §17 is the shorter §6 line. Both layers are present.

**Ruled 1120 tally stays 22/16/5/2 = 45.** The listed membership is identical to 1120 §7 and to the 1137 row table: PROVED 22 (GA1, GA4, GA5, GA6, GA7a, GA8, GA10, GA11, GA12, S1, S2, S3, D-A, R1, R2, R3, R4, R6, R7, R10, R11, R12) · CONDITIONAL 16 (GA2, GA3, GA7b, GA8-int, GA14, S5, S6, D-B1, D-B2, D-C, D-E, V, R5, R8, R13, R14) · OPEN 5 (GA9, S4, D-B3, R9, O5) · REFUTED 2 (GA13, D-D). No label-class change.

This erratum's own tally is 0/0/0/0 (bookkeeping, scope relabels and premise restatements only). R9 is recast as a new OPEN item inside the 1120 tally (it was already counted there as OPEN) and adds nothing here. Accepted.

Other standing tallies are listed as unchanged, not rewritten: 1711 11/10/4/0 (AB2, G2-odd, G3 at filed grades, as implications of the pure-M5 premise); 1800 as revised 13/11/3/2 (N-1 flagged against Y8; no regrade); Y16 and PP 077e417d unchanged; Errata 24 and 25 0/0/0/0 each. N = 4880, charge 9760, the tension-to-charge figures, 1a and B1-c2′ are not adopted (labelled test targets / not adopted, as in 1120 and in 5cf92795).

## 3. N-1 convention check (load-bearing)

NL chose option 1 of PP §7 item 2: **u is not redefined.**

Fixed convention (erratum §3):
- n_inst = (1/16π²)∫_{S⁴} tr F∧F,
- n_R = −(1/32π²)∫_{S⁴} tr R∧R,
- matching GA3's I₄ = (tr F∧F − ½ tr R∧R)/16π²,
- u := 8π²/(λ² T_M5) unchanged.

Internal consistency, checked by PP (not a re-derivation of the physics):
- ∫I₄ = (1/16π²)∫tr F∧F − (1/32π²)∫tr R∧R = n_inst + n_R. The two prefactors match I₄, including the minus already carried in n_R.
- Unit charge ∫tr F∧F = 16π² gives n_inst = 1. The BPS energy (1/2λ²)∫tr F∧F (PP P4e) is then 8π²/λ² per unit charge, so u is the BPS energy per unit charge in M5 units (PP P7e).
- Under 1120 §2's old writing n_inst = (1/8π²)∫tr F∧F (and n_R = −½(1/8π²)∫tr R∧R), the same energy per such a unit would have been 4π²/λ² = **u/2**, with HW-printed λ² ⇒ 1 and Conrad/Lü ⇒ ½ (PP P7f). The erratum records this and instructs that 1120 §2's charge line is to be read in the new convention. That is the correct additive move: the parent is not edited.
- The I₄ ratio n_R/n_inst is convention-independent and remains −½ × (∫tr R∧R)/(∫tr F∧F). Form statements (blocks, signs, traces, Bogomolny, NEC, D-A — the integral is 0 in any prefactor — and D-D) are correctly listed as unaffected.
- The inconsistency is correctly flagged as inherited from NL 1800 Y8; 1800 is not edited and not regraded.

Restatements, checked against the parent wording and against PP N-1 / §3.2 / §3.5, not merely against the erratum's claim that they were restated:

- **GA12.** Under C ∧ I ∧ N, the BPS energy per unit charge (unit ∫tr F∧F = 16π²) is u·W(y₀)T_M5, so u = 1. Implication only. This is the 1137 statement with the unit made explicit.
- **GA13.** u = 2 ∧ C ∧ I (∧ N) ⇒ a jump of (u − 1)W(y₀)T_M5 per unit charge at zero size ⇒ ⊥. Matches 1137 §3.2.
- **GA14.** u = 1 is the Conrad/Lü value (λ⁶/κ⁴ = (4π)⁵) **in this convention**; CONDITIONAL on the anomaly derivation (not re-checked) and on N. Correct: C4a's algebra already gives u = 1 from λ² = 2(2π)⁷, and that identification is the energy-per-I₄-unit reading only under N.
- **C4a (physical reading).** The exact algebra u = 8π²(2π)⁵/(2π)⁷ = 2 and u = 8π²(2π)⁵/(2·(2π)⁷) = 1 is unchanged (u is defined from λ² and T_M5, independent of the n_inst prefactor). The reading "u = BPS energy per unit charge in M5 units" holds in this convention (unit 16π²). Normalizations are not re-derived as physics. Correct split of algebra vs reading.
- **S1 (M5-unit sentence).** Parent 1120 S1 had joined, by "i.e.", the normalization-free pointwise ρ_inst = q_inst/2 in field units to ρ_inst(y)√g₄ = u T_M5 × (instanton charge density)(y). That identification holds only for a definite charge-density normalization, which is the N-1 issue. The erratum splits them: the M5-unit sentence is kept with the charge density normalized by (1/16π²) tr F∧F, and the pointwise field-unit relation is recorded as normalization-free. This is the required restatement, and it is the correct one: integrated energy (1/2λ²)∫tr F∧F = u T_M5 × n_inst in this convention.
- **D-B1.** T = N_M5 + u·n_inst + ε_ex = 2N_flux + (u − 1)n_inst + ε_ex, with n_inst in the (1/16π²) convention; dT/dn_inst = 0 at u = 1 (C4b, C4c exact). With n_R = 0 and the I₄-matching n_inst, this is the same algebra as 1120, now consistently read.
- **D-B2.** n_inst = Δ_N/(u − 1) ≤ 2N_flux, i.e. u ≥ 1 + Δ_N/(2N_flux), with n_inst in the (1/16π²) convention. Algebra unchanged; convention named.
- **R9.** b = N_req⁻¹(2N_flux + (u − 1)n_inst + ε_ex), same convention. Matches Fix 7.

No grade moves, as required: the affected identifications already sit in CONDITIONAL rows or implication-grades (GA12, GA13, GA14, D-B1, D-B2, R9; C4a's reading is not a tallied grade; S1 the row stays PROVED for the form statements, with the M5-unit sentence carrying N). PP does not treat the slightly loose erratum phrase "every affected row is already CONDITIONAL or an implication" as a defect: S1's grade is correctly unmoved.

The convention is internally consistent, and the listed rows were actually restated, not just declared.

## 4. Verdict

**FAITHFUL.** All 15 items of PP 5cf92795 §7, and all mandatory §6 tally-line relabels, are absorbed. The N-1 convention is internally consistent and the required restatements are present in the erratum text. No missed item. No incorrectly absorbed item. No label-class change. No required leftover fixes. Mode 644 on the erratum is the already-optional NL convention (item 15), recorded, not a leftover.

Nothing adopted. N = 4880, charge 9760, 1a and B1-c2′ remain unadopted. Junction UNSOLVED. No CERT. Tip 7cddb188 untouched. Parent, 1137 audit, e8delta.py and e8delta_run.log unedited.

## 5. Custody

- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, mtime 2026-11-06 14:38:54 CST, mode 644, **before** this write (re-hashed at 11:47:25 CST and again immediately before the write) = **after** (re-hashed after this write; see report-back). Never opened for writing. Not chmod-ed.
- NL Erratum 26, its sidecar, the 1120 parent, the 1137 audit, e8delta.py, e8delta_run.log and their sidecars: read and hashed only, untouched; the shas are unchanged at the end of this confirm.
- Running Local jobs (s1e, chain_v2, s2e, wait_then_ob_v5) and other agents' directories and frozen scripts: untouched. The unaudited NL 1130 filing e7312edb was not opened and is not used.
- New files are only this findings file and its sidecar.

Nothing adopted. Tip 7cddb188 untouched. Junction UNSOLVED. No CERT. Resonant algebra.
