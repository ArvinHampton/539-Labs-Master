# PR1 FINDINGS — HEPP / QM / GR missed variables, patterns and correlations (Owner FREE PURSUE) — 2026-10-26
Status: Soft SF, write-only, cite-only. Proof standard: each claim is either proved here or marked "UNPROVEN — gap: …". The invent ban is lifted only under that proof standard; no observational number was invented. Cat-A proof-gate OFF. Eight-only lane (no Eigen/Ops). Kerr/Path4 C2–C3 BLOCKED (no Kerr load).

## 1. Authority (live sha256, verified 2026-10-26 ~17:40 CDT)
| Doc | Path | sha256 |
|---|---|---|
| OW FREE PURSUE | reports/OWNER_WRITE_FREE_PURSUE_MISSED_VARS_PROOF_STANDARD_2026-10-26.md | 687b27f5ba8fab6a847563069f66bbb4b9511cf36d14df3e7143a83db335eecd |
| ASSIGN | reports/ASSIGN_EIGHT_PURSUE_MISSED_VARS_REPORT_2026-10-26.md | d763ac36900df1f0bb55e0ce8d7f72e96aa29e1b1e44af7269ce0d892dc73bba |
| OW invent-ban lift | reports/OWNER_WRITE_INVENT_BAN_LIFTED_PROOF_STANDARD_NO_CATA_GATE_2026-10-26.md | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 |
| Prior unlock FINDINGS | reports/PR1-FINDINGS-RULE4_CHI2_INPUTS_UNLOCK_2026-10-26.md | ae0bf4df80c1192a1b23a5fa56fcfc65325ca843e97587d734397a21af791eaa |
| Prior PREPARE | reports/PR1-FINDINGS-RULE4_CHI2_INGEST_PREPARE_2026-10-26.md | 37b289b1b11db8b902596144d2716a8d7d24129d1cec85ab2a42135848ada622 |
| Prior INCONCLUSIVE | reports/PR1-FINDINGS-RULE4_HYBRID_MC_RECOMPUTE_2026-10-26.md | 8e6d0b8affda74855e6dc4d8af7de85bdafb053cc97d49f9b015cfae9501e2c1 |
| Catalog (READ-ONLY) | /workspace/obs-data-PR1-HEPP-QM-GR.md | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d |
| tip Soft SF LOCK (not touched) | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |
| corrected_E_leak.py (read) | grok-files/corrected_E_leak.py | a786538854a27c7b0409c24c8a7d1bfa595db780f05214796fcec9822c9b945a (per unlock FINDINGS) |

## 2. What was pursued
Targets 1–5 from ASSIGN: (1) the systemic every-term-missing pattern; (2) the risk of correlating against the hard-coded Doc χ²/dof 0.79; (3) the Cat-B conflict cluster; (4) catalog observables that are not Rule-4 χ² inputs; (5) the RPPT/MC E_leak ↔ GR-lab/GW timing correlation.
Method: re-read the unlock inventory, grepped the catalog (DESI|ATLAS|BAO; §-headers), and inspected corrected_E_leak.py lines 26, 32 and 70. Proofs are elementary and written in full below.

## 3. First findings
### F1 — The ABSENT status is structural, not one missing number [PROVED, conditional on the inventory]
Premise (cite: unlock FINDINGS §3(iii)): every E_leak/F_friction term T_i has at least one coefficient c_i that is not Owner-Written. Examples: g_s X^M, the E_b(z) table, L, v_0, f_energy, Δt_11D, τ_echo, M_PBH, k1, k2.
- **Claim.** Let E_leak = Σ_{i=1..n} T_i(c_i, …), where each T_i depends non-trivially on c_i ∈ A (the ABSENT set). Then E_leak is not Written-evaluable unless every c_i is Written. The smallest Owner Write that unlocks evaluation is |{c_i}| ≥ k, where k is the number of distinct absent coefficients that cover all terms.
- **Proof.** E_leak is Written-evaluable only if every T_i is, because a sum is defined only when all its summands are. T_i depends non-trivially on c_i, so T_i is undetermined while c_i ∈ A. That forces a Write of a covering set of A-coefficients. ∎
- The inventory lists more than 25 distinct ABSENT symbols across disjoint terms, so k > 1. "One missing number" is therefore false.
- UNPROVEN — gap: the exact minimum k. Proving it needs a Written term-by-term dependency table, which is not in the corpus. Whether some ABSENT symbols are aliases of each other (shared coefficients) is undetermined.

### F2 — Doc χ²/dof = 0.79 cannot validate any observational match [PROVED]
- **(a) It is not a statistic.** In corrected_E_leak.py, CHI2_DOF = 0.79 is a literal (line 26; echoed at line 70). It is not computed from E_leak (line 32) or from any data array. A literal is constant under every change of model parameters. A goodness-of-fit statistic must depend on the model residuals. So 0.79 carries zero information about this model's fit. ∎
- **(b) A bare ratio cannot be identified.** For any r > 0, any N > p, and any model predictions m_j, there exist data d_j and errors σ_j such that Σ((d_j − m_j)/σ_j)²/(N − p) = r. Proof: take σ_j = 1 and d_j = m_j + √(r(N−p)/N). ∎ So a quoted r with no Written {d_j, σ_j, N, p} is compatible with any model, including a wrong one.
- **Named gap.** Doc 0.79 has no validating force until the Owner Writes (a) the DESI/ATLAS data points with errors, (b) the dof (N, p), and (c) the full coefficient list (F1). Any correlation drawn against 0.79 before then is circular.

### F3 — Cat-B conflict cluster is a contamination risk [PROVED as a risk; magnitude UNPROVEN]
- Conflicting chat fragments: ρ_DM 0.31 vs 0.32 (Δ ≈ 3.2%) and β_PBH 0.18 vs 0.19 (Δ ≈ 5.4%). The Written frozen values are 0.31 and 0.18 (sheet da91ad83…).
- **Claim.** If a non-Written fragment is ingested, the choice between the two values is an extra, unconstrained degree of freedom. Any downstream χ² then becomes a function of that choice.
- **Proof.** With two admissible values and no Written selector, the output is set-valued. Picking one is a selection that the data do not constrain, which is the definition of a researcher degree of freedom (contamination). ∎
- **Rule.** Keep these fragments UNUSED. If they are ever ingested without an Owner Write, flag the result as contaminated.
- UNPROVEN — gap: the sensitivity ∂χ²/∂ρ_DM and ∂χ²/∂β_PBH. Computing them needs F1 and F2 to be filled first. No number is given.

### F4 — Catalog observables that could fill slot (a) are ABSENT for Rule-4 [PROVED for the catalog]
- **(i) The catalog has no DESI/BAO/ATLAS-Open-Data dataset.** Catalog §1 line 8 excludes Cosmology (owned by PR2). grep finds no DESI or BAO hits; the only ATLAS hit is line 238 (the W-mass consensus note), which is not a dataset. So slot (a) as currently defined (DESI/ATLAS) cannot be filled from the PR1 catalog. ∎
- **(ii) Candidate HEPP/QM/GR observables.** Each has published values and errors, but none is Owner-Written as a Rule-4 χ² input. All are ABSENT-for-Rule-4, and no values are transcribed here:
  - §2A: Borexino pp/⁷Be/pep/CNO fluxes; SNO ⁸B; SN1987A burst timing (L41–44).
  - §2B: GW150914 radiated energy; GW170817 v_GW bound (L53); GWTC-3/GWTC-4.0 TGR (graviton mass, PN, dispersion) (L55+); EHT M87*/Sgr A* ring diameters; S2 redshift and precession. **Kerr-ringdown rows are excluded because Kerr is BLOCKED.**
  - §2C: photon mass bound; Bell S; muon g−2 (L99); Casimir; Lamb shift (L116).
  - §2D: M_W, M_Z, M_H, m_t, α_s, CKM (L119–155).
  - §2E: Mercury perihelion, Shapiro/VLBI γ, clocks, MICROSCOPE, binary-pulsar Ṗb, GP-B, inverse-square (L164–194).
  - §2G: SME bounds.
- **Named gap.** Using any of these needs Owner Writes for three things: the observable↔model map (which model output predicts it), the chosen subset (N), and p. Without those, F2(b) applies.
- UNPROVEN — gap: whether the E_leak/F_friction model produces any output commensurable with these observables at all. No Written prediction function exists.

### F5 — The RPPT/MC E_leak ↔ GR-lab/GW timing correlation cannot be stated [PROVED: no map exists today]
- The 118-element reverse-parity integration runs over a dimensionless index z = 1…118. Timing observables (GW170817 Δt = 1.7 s and |Δv/c| bounds; SN1987A ~10 s; pulsar Ṗb) carry units of time.
- **Claim.** Any dimensionally consistent map f: {E_leak(z)} → seconds needs at least one Written dimensional constant with units of time.
- **Proof.** The integrand and the index carry no time dimension once the coefficients are excluded. The candidates with time units (Δt_11D, τ_echo, τ^-) are ABSENT or chat-only Cat-B (unlock FINDINGS §3(iii)). By dimensional homogeneity, no such f exists over the Written set. ∎
- UNPROVEN — gap: whether any correlation exists once Δt_11D or τ_echo is Written. Even then it remains an open conjecture until the Owner Writes a propagation law. No Kerr physical load was used, and echo/ringdown rows were not invoked.

## 4. Explicit non-claims
- No χ², dof, or data point was invented or computed. No script literal was used as a coefficient.
- No Kerr or Path4 C2–C3 load. Kerr-ringdown catalog rows are excluded.
- No Eigen/Ops content.
- The catalog was not modified (still 6c680789…).
- tip_touched NO (tip still 7cddb188…).

## 5. Parallel Rule-4 status
Slots (a), (b) and (c) remain ABSENT. I did not run the decisive recompute and did not write PR1-FINDINGS-RULE4_HYBRID_MC_DECISIVE_RECOMPUTE. The prior INCONCLUSIVE (8e6d0b8a…) stands.
