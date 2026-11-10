# INVENTORY — written sources (read-only), 2026-10-24
| id | source | content relevant | Cat |
|---|---|---|---|
| EH1 | zenodo 23010998 Einstein–Hampton Equation Rewrite Appendix (2026-09-28) | L1–L7; (alg) 6k²−3K=−Φ/96, 4k²+K=Φ/144 ⇒ k²=Φ/1728, K=8k²; (EH-k) N=4880 ⇒ k₁₁=0.02531377 vs T²₁₁=0.02533030, "match wants N=4870.45, miss 9.55"; faces +U y=0 / −U y=b; snap 0.0155, eject 0.31 GeV/cm³ "(convention)"; κ_dark=243/539, f_snap=243/4880, β_PBH=0.181, R11=85 μm all listed INSERTED; "L1–L7 contain no time"; next check: four-form weights −G²/96 vs −G²/288 | A (L1–L7), B (insertions) |
| EH2 | oct17-master/lean/EinsteinHamptonCurvature.lean (+README) | L1–L7 statements; header says Lake/Mathlib built L1–L7 29 Sep 2026 (appendix says "no kernel run here" — status discrepancy, not re-run) | A (claimed) |
| PT1 | zenodo 17926999 −Periodic Table (reverse parity) | 118 −elements; Z, mass, config identical to +U, "reversed filling"; mp/bp copied from +U; parity-flipped weak sector; g_portal≈0.005; halo = mirror plasma, ρ_DM≈0.31 GeV/cm³; qualitative H0, S8 0.75/0.83, dipole ~2×, θ_CP<1e−10 | B |
| PT2 | zenodo 20709375 Periodic Table Codex | F_total = (F_Coul+F_SO+F_torsion+F_flux+F_leak)·Ω₁₁D; Ω₁₁D "fixed once by 11D compactification" — no numeric value / derivation written; 61 ω-punctures; predictions: 539.9 s Raman sidebands amp ~0.18 in Au/Hg; η_ZPL>0.99; SN GW precursors | B |
| PT3 | zenodo 20617775 Resonant Attractor / Torsion Transfer Points & PT | RTA ↔ PT (local stream; noted only) | B (local) |
| SP1 | zenodo 17990940 Master List of Falsification Bounds | 12 clauses, each "if X, adjust parameter by δ" (retune, not falsify) | B |
| SP2 | zenodo 17822998 7D Torsion & −U beta decay in DM halo | 539.9 s as G₂ torsion eigenvalue, galaxy-local ±1–4 s | B |
| SP3 | 17812891 Galactic Dynamics; 18111709 CDM rebuttal; 18425770 three-body non-local DM/DE; 18132056 light duality non-local | halo/non-local framing | B |
| SP4 | 18442276 / 18509384 17 (and 18–40) Theorems of Entanglement; theorems/17-theorems-v5.txt | non-local entanglement framing | B |
| NLb | BRIDGE_C_35 order15 P-even ½𝓗(Φ_orth) | local-hybrid framing; related Category B only; NOT read into or modified; no bulk claim drawn from it | B (related) |
| LG | grok-chats/*, oct17-master Axiomatic-Book (Master_Glossary 09-29, Executive_Summary_*), SELF_AUDIT.md | hits for reverse parity/Ω_11D/halo/L1–L7 — restate the above; no additional numeric link found | B |

## Written testable LINKS (EH 11D curvature ↔ reverse-parity PT ↔ simulated physics ↔ non-local/halo bulk): **0 fully written**
Candidates examined and why each fails to be a predefined falsifiable link:
1. ρ_eject=0.31 GeV/cm³ (EH1) = ρ_DM≈0.31 (PT1): EH1 itself marks it "(convention)"/inserted → identity by insertion, vacuous.
2. Ω₁₁D (PT2) ↔ L7 lock k²=Φ/1728, K=8k²: no written formula Ω₁₁D(k,K,Φ,b); no Φ value written. Missing clause.
3. Reverse parity (PT1) ↔ −U face T(−) (EH1): no written map from −element table entries (all copied from +U) to T(−) components ρp, ρd, fu≈3e−4 (fu inserted).
4. Codex 539.9 s / 0.18 amplitude: EH1 states "L1–L7 contain no time" and 539.90 s inserted → not an EH-curvature consequence.
5. n_wall = n_halo·R11 = 28 m⁻² : n_halo and R11=85 μm inserted; no PT input.
6. SP1 bounds: retune clauses, not falsification.
Written EH-internal (non-link) testables: (EH-k) N=4880 miss (already self-reported FAIL by 9.55 units, Cat A as written); four-form weight check (listed "next", not done).

## Inventory verification (Category A, EH-internal only, NOT a link test)
inventory_check/l7_recheck.py (SymPy): (alg) ⇒ {k²=Φ/1728, K=Φ/216}, K/k²=8; on lock G_ext/g=−18k²=−Φ/96, 10k²−2K=−6k²=−Φ/288 — reproduces written L6/L7. Note: second (alg) equation 4k²+K=Φ/144 is not literally the G_fib block 10k²−2K; consistent on the lock but the source of 4k²+K is not written (open clause EH-O1).

## Deepening pass 2026-10-24 (appended; prior rows unchanged)
| id | source | content | Cat |
|---|---|---|---|
| EH-Ω1 | RPP chats e1a411f6 :17335 etc.; neutrino chat c39b5dc0:499 | Ω_11D=1/√(1+g_11²+g_s²)≈0.99995, g's inserted | B |
| EH-Ω2 | A30_540_thermo/logs_search3.txt:33 | variant with (539.9/540)² → excluded (inserted 539.9) | B (excluded) |
| EH-Ω3 | A22 chats e85353a0 ~:405 | Ω_11D=0.99987 "absorbs all … corrections"; 118-table subset only | B |
| EH-Ω4 | A22 chats 8537483b:1551 | Ω_11D=1 normalized | B |
| NL-crit | A22 chats e9658c0b:97 | "division by √Ω_{11D} … is tuning, not derivation" | B (critique) |
| PT4 | _git_v8_unpushed_clone/.../Mirror_Periodic_Table_Halo_Extension.md | reverse-parity halo; N_flux=4880 "Cat A/locked"; all cosmology maps self-labelled Cat B; no L1–L7 | B |
Link count after deepening: **still 0** written falsifiable EH↔PT↔sim↔halo links. Details: inventory_check/{NL1_OMEGA_ABSENCE,EH_O1_FOURFORM,SEARCH_LOG}.md. periodic_table_539labs.json: ABSENT.

## 2026-10-24 expanded search (see inventory_check/EXPANDED_SEARCH_LOG.md)
- EH-Ω5 (Cat B, structural only): Ω_11D = ∫d^{11}x√|g| / V_compact, V_compact≈(2π l_s)^7 — A22 chats/eda69302…:1567. Not in k,K,b,Φ; not evaluable.
- Still ABSENT: Ω₁₁D(k,K,b,Φ); Φ from N=4880; derivation of 4k²+K=Φ/144; periodic_table_539labs.json/.npz; any Z=1–118 F_total table.

## 2026-10-24 — EH-RB1 (prereg/EH_RICCIBLOCK_20261024) Cat A PASS, convention-free
From-scratch SymPy Ricci of written metric EH1:18 (A=ky, B const, ĝ=round S^6) reproduces EH1:118 Rext/g=Ryy=−4k², Rfib/g=K; L6 blocks 6k²−3K / 10k²−2K; and EH1:43 on-lock R=28k², G=−18k²/−6k². Controls (A=ky², 3+1+7 split) fail → non-vacuous. sha256 PREREG.md 97e2bcec…973a, run.py 3780b9ff…445c. No Φ, no 8πG11 used. Upgrades L1–L6 from "Lean defs" (LEAN_L1L7_ASSUMPTIONS) to computed-from-metric. Remaining L7 dependence on Φ≡G², 8πG11=1, a=1/24 unchanged.

## 2026-10-24d [SOURCE=WRITTEN-CHAT]
- EH-GC1-INDEX PASS, EH-FF1-CJS PASS (see MILESTONE_2026-10-24d). Removes residual assumption (ii) 8piG11=1 only conditional on WRITTEN-CHAT GC-1 (CHAT≠paper; no paper upgrade); (i) Phi def remains CHAT-only, (iii) fork choice remains.

## 2026-10-24e
- EH-FORK: F1 a=1/24 (paper) vs F2 CJS (CHAT). Both PASS internally; OPEN. Hunt: paper Φ def ABSENT; written selection "a=1/24 locked" (09-28 Afternoon wrap:2) has no reasoning. EH-JX1 candidate source: 09-29 Junctions wrap:32-33 (fork-free geometry).
- Relabel (auditor): EH-FF1 = Cat A algebra | B-conditional (not a bare Cat A). EH-FF1-CJS / EH-GC1-INDEX = CHAT-conditional. EH-RB1 C2 deviated from the prereg; it was rerun as preregistered (prereg/EH_RICCIBLOCK_C2_RERUN_20261024, PASS, RESULTS.sha256). EH-RB1 stands, and the timestamp is corrected to 22:00:50 CDT.

## 2026-10-24 EH-JX1 (Physicist-cleared)
prereg/EH_JX1_20261024: **PASS = Cat A geometry [WRITTEN-CHAT tier: wrap source, not paper-forced] | normal-convention n=+∂_y**. K_μν=−k q_μν, K=−4k (4D and 10D, B const), K_μν−Kq_μν=3k q_μν. Controls C1 (A=ky²), C2 (flipped normal), C3 (B=by) all fail as preregistered. PREREG.sha256 file digest 8459dbd5…62b5. RESULTS.sha256 file digest ddd62af5…5e9f. τ₋ excluded. Cosmetic: result.log line "K_mn = Matrix(0, 0, [])" is a print bug (diag() call); verdicts are unaffected. Not rerun, to keep the prereg hash intact.
"a=1/24 locked" = DECLARED-LOCK (underived). Fork OPEN.

## 2026-10-24 pivot — PT + halo/sim written-link inventory
Detail: inventory_check/PT_WRITTEN_LINKS.md (PTW1–12), inventory_check/HALO_SIM_WRITTEN_LINKS.md (HW1–12).
- Fully written Cat A EH↔PT↔sim↔halo links: still **0**. No GATE_CANDIDATE.
- Closest written falsifiers: PTW6 (Codex 20709375:134-135, Raman 0.18 / 539.9 s) and HW3 (17822998:96-102 null set) — both Cat B-keyed, PTW6 amplitude = plugged β_PBH, HW3 non-discriminating and contradicted by 17812891:124-125 / 18132056:116.
- New noted: Codex sub-harmonics {5,10,15,30,45} s ≠ 539.9/n; only written halo↔−PT formula is ⟨J_−U⟩ ∝ ⟨N⁻−2Z⁻⟩ (17822998:60) with no values.

**Status (auditor relabel 2026-10-24 22:16 CDT):** Φ=8πG11·G² and the flux→k recipe are WRITTEN-CHAT only (CHAT≠paper; not Cat A, not paper). kℓ11=0.02531 and the ~3-unit (or 9.55-unit) miss are convention-unfixed; k(N) OPEN, not derived. Physicist GC-1/GC-2 acceptance = bookkeeping + CHAT-labeled tests only; does NOT clear NL1 or any paper gate. NL1 OPEN.

## 2026-10-24 (late) — contradiction ledger + Codex structure
- inventory_check/CONTRADICTION_LEDGER.md: 6 entries (4 hard: LISA 1.851 mHz null vs peak; CMB ℓ≈540 null vs dip; 539.9 s local vs universal; Ω₁₁D fixed vs absorbs-all). Cat A documentation of disagreement only.
- inventory_check/CODEX_FTOTAL_STRUCTURE.md: F_total 5 terms, ≥19 unvalued params, Cat B plugs 539.9 s / β_PBH=0.18. No Z-table possible.
- periodic_table_539labs.json: still ABSENT.
- 2026-10-24 W-NL-3 label: EH-JX1 PASS is **WRITTEN-CHAT tier (non-paper wrap source, not paper-forced)**; hash discipline PASS. See inventory_check/EH_JX1_HASH_AND_LABEL.md.
