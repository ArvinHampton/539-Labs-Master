# PR1 FINDINGS — E_leak / F_friction term-by-term Written dependency table (Owner FREE PURSUE, proof standard) — 2026-10-26
Status: Soft SF, write-only, cite-only. Every claim below is either PROVED here or marked "UNPROVEN — gap". No numeric value was invented for any ABSENT coefficient. No χ² recompute was run. Eight-only lane. Kerr BLOCKED (not loaded). tip_touched NO.
Purpose: close or narrow the F1 exact-k gap from FINDINGS cb43f7d1….

## 1. Authority (live sha256, verified 2026-10-26 ~17:45 CDT)
| Doc | Path | sha256 |
|---|---|---|
| OW FREE PURSUE | reports/OWNER_WRITE_FREE_PURSUE_MISSED_VARS_PROOF_STANDARD_2026-10-26.md | 687b27f5ba8fab6a847563069f66bbb4b9511cf36d14df3e7143a83db335eecd |
| OW invent-ban lift | reports/OWNER_WRITE_INVENT_BAN_LIFTED_PROOF_STANDARD_NO_CATA_GATE_2026-10-26.md | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 |
| FREE PURSUE first FINDINGS (F1) | reports/PR1-FINDINGS-HEPP_QM_GR_MISSED_VARS_FREE_PURSUE_2026-10-26.md | cb43f7d136b6cd9f22983d85b660f48e5a3af06e114e396595ce2dc9104fcd69 |
| Unlock FINDINGS (inventory §3(iii)) | reports/PR1-FINDINGS-RULE4_CHI2_INPUTS_UNLOCK_2026-10-26.md | ae0bf4df80c1192a1b23a5fa56fcfc65325ca843e97587d734397a21af791eaa |
| Sheet params RR-NL-SHEET-01 | reports/bridges/NONLOCAL_QM_EH11D/WRITE_NL_RR_NL_SHEET_01_PARAMS_2026-10-26.md | da91ad83ac35a2f3a897dbd1794b90d102b409284012b889d6b74849e3af5998 |
| Runnable spec | reports/bridges/NONLOCAL_QM_EH11D/WRITE_NL_HYBRID_MC_RUNNABLE_SPEC_POST_JOIN_PASS_2026-10-26.md | 27058bad386fc64dff071324e4f4d248a60113c68349917b42656c93025fe980 |
| Corrected 7D A27 (E_leak L84–92, F_friction L77–80, §3.1 L95) | reports/s_family_paths/A27_drive_review_complete/txt/12RM_gft3rNFqCqYoBEsHUvPtDlpIN_lq5YvVu1P8dLY.txt | 4758d180f467a35d139833711029ac4121fa98d79bb3129be1b579d8254250b1 |
| minus-PT A27 (read; no E_leak formula, ρ_DM≈0.31 narrative only) | reports/s_family_paths/A27_drive_review_complete/txt/1IaS2PUycsnm9ME4f2Ia7jPhJxNzNunAgpIWOMNi4VRs.txt | 7302244a8fd5dd641855191e1f2e92dfe638fcb69845af6203b28c72dfcbb65d |
| corrected_E_leak.py (read) | grok-files/corrected_E_leak.py | a786538854a27c7b0409c24c8a7d1bfa595db780f05214796fcec9822c9b945a |
| Catalog (READ-ONLY, unmodified) | /workspace/obs-data-PR1-HEPP-QM-GR.md | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d |
| tip Soft SF LOCK (NOT touched) | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |

## 2. Classification rules
- **LANDED** = Owner-Written or CITED-from-Corrected-7D through the sheet: ρ_DM=0.31 GeV/cm³, β_PBH=0.18, κ_dark=0.45, z=1…118 (sheet §3). Numeric literals written inside the Corrected 7D formulas themselves (539.9, 0.9, 1000, 118, 10, 2, 8π², 1) are also LANDED as structure.
- **EXT-STD** = standard physical constants (c, ℏ, k_B, m_μ). They are not ABSENT and not invented. Their use as Rule-4 inputs still needs an Owner Write of the source (CODATA/PDG). No values are transcribed here.
- **ABSENT** = everything else. This includes Cat-B chat-only fragments (E_0, τ^-, σ_inh, δ(t), β_z, Ω_11D; unlock §3(iii)) and the script literals in corrected_E_leak.py, which are not Owner-Written.
- Alias: YES means a Written identity exists; NO means the symbols are distinct under notation axiom N (§4); UNKNOWN means plausible same-symbol reuse with no Written resolution.

## 3. Term-by-term table
### 3A. E_leak(t), Corrected 7D (4758d180…, L84–92)
| # | Term | LANDED | ABSENT | Alias ambiguity | Written-evaluable |
|---|---|---|---|---|---|
| E1 | E_0 e^{−t/τ} L Ω_11D | — | E_0 (chat-only), τ, L, Ω_11D (chat-only) | UNKNOWN (Ω_11D↔Ω of E6; τ↔τ^-, also τ in F1) | NO |
| E2 | κ_dark √δ(t) v_0 f_energy (1+ρ_DM/10)(1 + m_φΦ + g_coupling A + h_coupling T + m_ψψ + g_11Φψ + g_s X^M) | κ_dark, ρ_DM, 10, 1 | δ(t) (chat-only), v_0, f_energy, m_φ, Φ, g_coupling, A, h_coupling, T, m_ψ, ψ, g_11, g_s, X^M | UNKNOWN (δ(t)↔δ of E5; T↔T_rad) | NO |
| E3 | ρ_DM ∫_0^{t/(1+g_11Φ)} sin(m_φτ + λ_field δ(τ) + ⋯) dτ | ρ_DM | g_11, Φ, m_φ, λ_field, δ(·), and **"⋯" (unspecified terms)** | UNKNOWN; "⋯" is an open set | NO (and not even finitely specified) |
| E4 | Σ_{z=1}^{118} E_b(z)(E_z^- − Z_z^-)/(c²τ^-) · sin(2πt/(539.9+Δt_11D)) | 118, 539.9; c (EXT-STD) | E_b(z) table, E_z^- table, Z_z^- table, τ^- (chat-only), Δt_11D | UNKNOWN (Z_z^- shared with F2) | NO |
| E5 | δΔ A_H-QP (1 − τ_echo/t) e^{−(t−τ_echo)²/2σ_inh²} | 2 | δ, Δ, A_H-QP, τ_echo, σ_inh (chat-only) | UNKNOWN (Δ↔ΔE of E6; δ↔δ(t)); shared with F3 | NO |
| E6 | S ℏ Ω e^{−S}(1 − E_em/ΔE) | ℏ (EXT-STD) | S (script literal 0.31 only, not Written), Ω, E_em, ΔE | UNKNOWN (S vs ρ_DM 0.31 numeric coincidence in script; Ω↔Ω_11D) | NO |
| E7 | β_PBH ρ_DM e^{−M_PBH/(k_B T_rad)} | β_PBH, ρ_DM; k_B (EXT-STD) | M_PBH, T_rad | NO | NO |
| E8 | δa_μ^{−U} g_{−U}² m_μ²/(8π² M_{−U}²) · κ_dark sin(2πt/539.9) | κ_dark, 8π², 539.9; m_μ (EXT-STD) | δa_μ^{−U}, g_{−U}, M_{−U} | NO | NO |

### 3B. F_friction(t), Corrected 7D (4758d180…, L77–80)
| # | Term | LANDED | ABSENT | Alias | Written-evaluable |
|---|---|---|---|---|---|
| F1 | 0.9(γ−1) m_adj v_0² (1000/539.9) e^{−t/(τ+γ_LQG N_simplex)} L | 0.9, 1000, 539.9 | γ, m_adj, v_0, τ, γ_LQG, N_simplex, L | UNKNOWN (v_0, τ, L shared with E1/E2, presumed same symbol) | NO |
| F2 | Σ_{z=1}^{118} β_z (N_z^- − 2Z_z^-) e^{−t/τ^-} | 118, 2 | β_z (chat-only fragment β_z=0.065 is scalar; table form unknown), N_z^- table, Z_z^- table, τ^- | UNKNOWN (β_z↔β_PBH: NO under axiom N) | NO |
| F3 | A_H-QP δΔ e^{−(t−τ_echo)²/2σ_inh²} | 2 | A_H-QP, δ, Δ, τ_echo, σ_inh | UNKNOWN (shared with E5) | NO |
| F4 | cos((k_1−k_2)d − θ)(1+α_alt) | 1 | k_1, k_2, d, θ, α_alt | NO | NO |

### 3C. Other Written-adjacent forms
| Source | Form | Status |
|---|---|---|
| Sheet da91ad83… §3–4 | Lands ρ_DM, β_PBH, κ_dark, z range. Names the g_s X^M term as the join wire. | Lands no further coefficient. g_s and X^M stay ABSENT. |
| Runnable spec 27058bad… | Step 1: "Recompute E_leak integration over z = 1…118 with frozen params." | Structure only. No coefficient landed. |
| SymPy chat form (A22 chat ef92a5c4… L8501; Cat-B) | E_leak/F_friction = κ_dark √δt v_0 f_energy (1+ρ_DM/10)[e^{−t/τ}] sin(2πt/G_4) | A Cat-B reduced form, structurally the same as E2's prefactor. Not Written. ABSENT: δt, v_0, f_energy, τ. |
| corrected_E_leak.py a7865388… L41–54 | term1…term5, exciton, 0.18·e^{−10⁶} | Every coefficient is a script literal, so all are ABSENT-for-Written. **Alias ambiguity YES/UNKNOWN**: the script terms do not map 1:1 to E1–E8 (e.g. term5 = S·100·e^{−S}(1+η_phonon) has no 7D counterpart; exciton term is absent from 7D). There is no Written script↔7D map. Script-evaluable YES, but Written-evaluable NO. |

**Result.** Written-evaluable terms: **0 of 12** (E1–E8, F1–F4). No term has all of its coefficients LANDED. ∎ (by inspection of 3A/3B; each row lists at least one ABSENT symbol)

## 4. k_min: lower bound on the distinct ABSENT covering set
**Correction to F1 (cb43f7d1…).** A summand T_i is evaluable only if *every* ABSENT symbol in T_i is Written, not just one. So the minimal unlocking Write is the **union** U = ⋃_i A_i modulo Written aliases, not a hitting set. k_min = |U / ~|, where ~ is the (unknown) alias relation.

**Axiom N (notation).** Two symbols written with distinct names/sub/superscripts **inside the same Written expression** denote distinct quantities unless a Written identity says otherwise. N is the standard convention for mathematical notation, but it is **not Owner-Written**. Results that rely on it are flagged.

**Theorem 1 (E_leak alone).** Under N, with every UNKNOWN cross-name alias merged adversarially (δ(t)≡δ, Δ≡ΔE, Ω≡Ω_11D, all same-name symbols identified), and the "⋯" in E3 contributing ≥ 0:
k_min(E_leak) ≥ 35.
*Proof.* There are 37 distinct ABSENT names in 3A: E_0, τ, L, Ω_11D, δ, v_0, f_energy, m_φ, Φ, g_coupling, A, h_coupling, T, m_ψ, ψ, g_11, g_s, X^M, λ_field, E_b, E_z^-, Z_z^-, τ^-, Δt_11D, Δ, A_H-QP, τ_echo, σ_inh, S, Ω, E_em, ΔE, M_PBH, T_rad, δa_μ^{−U}, g_{−U}, M_{−U}. (δ(t) and δ are already counted once.) The only cross-name UNKNOWN pairs left are Δ~ΔE and Ω~Ω_11D. Merging both removes at most 2, which leaves 35. Every remaining pair either appears together in one expression (so N makes them distinct) or differs in type (a 118-entry table vs a scalar; for example E_b, E_z^-, Z_z^- are tables, and under N they are mutually distinct because all three appear in E4). Under N, any name pair not in the UNKNOWN list co-occurs in the full E_leak expression, so it is distinct. E_leak is evaluable only if all of U is Written (F1 proof, sum rule). ∎

**Theorem 2 (E_leak ∪ F_friction).** Under the same assumptions, F_friction adds these names, absent from E_leak: γ, m_adj, γ_LQG, N_simplex, β_z, N_z^-, k_1, k_2, d, θ, α_alt (11). They co-occur within F_friction (so N applies), and none matches an E_leak name. So k_min(E_leak ∪ F_friction) ≥ 35 + 11 = **46**. ∎ (Without merging the two UNKNOWN pairs: 48.)

**Unconditional statement (no axiom N).** Without N, all ABSENT scalars of the same type could formally be identified. The only unconditional bound is type-based: at least one scalar plus at least one z-indexed table, since E4 needs a 118-entry table and E7 needs a scalar with M_PBH/(k_B T_rad) dimensionless. That gives k_min ≥ 2. ∎ This is trivially weak and is reported only for completeness.

**Upper side / exact k.** UNPROVEN — gap: exact k_min. Three things are missing:
(i) the "⋯" in E3 makes U not finitely specified, so there is no Written upper bound;
(ii) no Written alias table (Owner Write of identities, e.g. whether δ(t)=δ, Δ=ΔE, Ω=Ω_11D, whether the shared τ/L/v_0 are the same in E_leak and F_friction);
(iii) no Written script↔7D term map.
**Narrowed:** F1's "k > 1" is upgraded to **k_min ≥ 35 (E_leak), ≥ 46 (E_leak ∪ F_friction), conditional on axiom N**. Unconditionally k_min ≥ 2.

## 5. Explicit non-claims / holds
- No numeric value was assigned to any ABSENT coefficient. Chat fragments and script literals were not used as Written values.
- No χ², dof, or observational number was invented or computed. Doc 0.79 stays a script literal (F2 of cb43f7d1…).
- Rule-4 slots (a) data points with errors, (b) dof, (c) full coefficient list: **all still ABSENT**. The decisive recompute was not run. Prior INCONCLUSIVE (8e6d0b8a…) stands.
- Kerr / Path4 C2–C3: NOT loaded (BLOCKED). Eight-only; no Eigen/Ops.
- Catalog unmodified (6c680789…). **tip_touched NO** (tip 7cddb188… verified before and after).
