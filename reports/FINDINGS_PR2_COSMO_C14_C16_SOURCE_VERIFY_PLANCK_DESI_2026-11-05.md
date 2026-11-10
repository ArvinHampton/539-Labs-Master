# FINDINGS — PR2 Soft SF invent-free source verify Cosmo C14 + C16 (Planck / PDG / ACT DR6; DESI optional) — 2026-11-05 ~13:31 CST America/Chicago

## Authority (verbatim cite; Soft SF ACK)
- Owner OW ALL_AGENTS_RESOLUTION_NO_PER_ITEM: `OWNER_WRITE_CALL_53991ebf_ALL_AGENTS_RESOLUTION_NO_PER_ITEM_APPROVAL_2026-11-05.md` sha256 **06748ff29e8b5e103833c5dec0712443a255d4e26990ea53acaa8793306fe9e2**
- PR2 Soft SF ACK FINDINGS: `FINDINGS_PR2_SOFTSF_ACK_ALL_AGENTS_RESOLUTION_NO_PER_ITEM_APPROVAL_OW_06748ff2_2026-11-05.md` sha256 **2516486a3e921cc7cf6827dcef27aa3e2e7018ac8ba2251b7d6d57c8c01a038e**
- Role: PR2 Soft SF Write-only on the box for Project Quantum Comp. **invent HOLD stands** (no invent of physical mappings, Ω ratios, residual-C links, proofs, or citations).
- Tip Soft SF LOCK path: `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` — required sha256 **7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91** (verify start+end; tip_touched **NO**).
- Catalog READ-ONLY: `/workspace/obs-data-PR2-COSMO-BIO-NEURO.md` sha256 **4ed155d55c3a18ca4bc96a6a6eec4c1806abfc2e270f355f1ea58a197119dd04** — do not edit.

## Tip Soft SF LOCK check (before / after this Soft SF write)
| Checkpoint | sha256 | tip_touched |
|---|---|---|
| BEFORE write | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | NO |
| AFTER write | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | NO |
| Catalog (unchanged) | 4ed155d55c3a18ca4bc96a6a6eec4c1806abfc2e270f355f1ea58a197119dd04 | UNCHANGED |

Tip start (header) and end (hash-note footer) were read this beat; file content not modified by this Soft SF.

## Catalog fragments under test (READ-ONLY verbatim)
- **C14** (catalog line 37): Ω_Λ = 0.685 ± 0.007; ρ_Λ = 5.83(16)×10⁻³⁰ g cm⁻³; Λ = 1.088(30)×10⁻⁵⁶ cm⁻² (Planck 2018 via PDG)
- **C16** (catalog line 39): Ω_K = 0.0007 ± 0.0019 (Planck+BAO); ACT DR6 "no departure from flatness"

## Soft SF method (invent-free)
Look up primary published sources on the web this beat. Extract exact published central values ± uncertainties with DOI and/or arXiv id. Soft SF label each catalog fragment **MATCH** (same within rounding), **DRIFT** (published value differs), or **ABSENT-update** (source not found / not that claim). DESI BAO latest published Ω_K / Ω_Λ constraints noted only as **OPTIONAL cross-check** rows (clear label); no residual-C invent; no force-MATCH to Author Item4.

---

## Table — catalog claim vs published value vs Soft SF label

| ID | Catalog claim (v0.5.11 fragment) | Published primary value (this beat) | Soft SF label |
|---|---|---|---|
| C14a | Ω_Λ = 0.685 ± 0.007 (Planck 2018 via PDG) | PDG RPP 2024 Table 2.1 (Astrophysical Constants): Ω_Λ = 0.685(7); PDG Ch.25 Table 25.1: Ω_Λ = 0.685 ± 0.007 (Planck TT,TE,EE+lowE+lensing). Planck 2018 VI base-ΛCDM: Ω_Λ = 0.6847 ± 0.0073 (TT,TE,EE+lowE+lensing) — rounds to catalog form. | **MATCH** |
| C14b | ρ_Λ = 5.83(16)×10⁻³⁰ g cm⁻³ | PDG RPP 2024 Table 2.1: ρ_Λ = 5.83(16)×10⁻³⁰ g cm⁻³ (derived; Planck 2018 VI via PDG ref [2]). | **MATCH** |
| C14c | Λ = 1.088(30)×10⁻⁵⁶ cm⁻² | PDG RPP 2024 Table 2.1: Λ = 1.088(30)×10⁻⁵⁶ cm⁻² (derived; Planck 2018 VI via PDG ref [2]). | **MATCH** |
| C14 (row) | Combined dark-energy density triad as above | All three sub-claims match PDG Planck-via-PDG table; Planck primary Ω_Λ agrees within rounding. | **MATCH** |
| C16a | Ω_K = 0.0007 ± 0.0019 (Planck+BAO) | Planck 2018 VI (arXiv:1807.06209): Ω_K = 0.0007 ± 0.0019 (68%, TT,TE,EE+lowE+lensing+BAO). PDG Table 2.1: Ω_K = 0.0007(19) (CMB+BAO). Abstract rounding 0.001 ± 0.002 is coarser; catalog uses the table-precision form. | **MATCH** |
| C16b | ACT DR6 "no departure from flatness" | ACT DR6 abstract (arXiv:2503.14452): "We find no evidence for excess lensing in the power spectrum, and **no departure from spatial flatness**." Exact phrase family present. | **MATCH** |
| C16 (row) | Combined curvature + ACT flatness | Both sub-claims verified against primary sources this beat. | **MATCH** |

### OPTIONAL cross-check only (NOT a Soft SF MATCH force to Author Item4; no residual-C invent)
| Optional row | What exists with DOI / arXiv (this beat) | Soft SF note |
|---|---|---|
| DESI DR2 BAO primary | DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints*, Phys. Rev. D, DOI **10.1103/tr6y-kpc6**, arXiv:**2503.14738** (published 2025-05-23). Reports BAO distances and flat-ΛCDM / w₀wₐ fits (e.g. BAO-only Ω_m = 0.2975 ± 0.0086 in related catalog C13 context). | OPTIONAL only — DOI-verified primary exists. |
| DESI+CMB Ω_K (secondary cite of DESI) | Chen & Zaldarriaga, arXiv:**2505.00659**, cite DESI Collaboration [2503.14738] reporting curved ΛCDM+Ω_k: **Ω_k = 0.0023 ± 0.0011** (DESI+CMB, ~2σ preference for Ω_k > 0). | OPTIONAL cross-check only. Differs numerically from C16 Planck+BAO Ω_K = 0.0007 ± 0.0019 — **not** a Soft SF DRIFT of C16 (different dataset combination). **No** invent residual-C mapping; **no** force-MATCH to Author Item4. |
| DESI Ω_Λ (flat ΛCDM) | Under flat ΛCDM, DESI BAO prefers lower Ω_m than Planck; Ω_Λ ≈ 1 − Ω_m when flat is assumed — not treated here as a C14 MATCH/DRIFT (different probe; optional only). | OPTIONAL only. |

---

## References verified this beat (DOI / arXiv)
1. **Planck Collaboration 2018 VI** — *Planck 2018 results. VI. Cosmological parameters*. A&A 641, A6 (2020). DOI: **10.1051/0004-6361/201833910**. arXiv: **1807.06209**. Key extracts: Ω_Λ = 0.6847 ± 0.0073 (TT,TE,EE+lowE+lensing); Ω_K = 0.0007 ± 0.0019 (TT,TE,EE+lowE+lensing+BAO); abstract also quotes Ω_K = 0.001 ± 0.002 (rounded).
2. **PDG RPP 2024 — Astrophysical Constants and Parameters** (Table 2.1, rev. Aug 2023, Groom & Scott). URL: https://pdg.lbl.gov/2024/reviews/rpp2024-rev-astrophysical-constants.pdf — Ω_Λ = 0.685(7); ρ_Λ = 5.83(16)×10⁻³⁰ g cm⁻³; Λ = 1.088(30)×10⁻⁵⁶ cm⁻²; Ω_K = 0.0007(19) (CMB+BAO); cites Planck 2018 VI as ref [2].
3. **PDG RPP 2024 — Cosmological Parameters** (Ch. 25 / Lahav & Liddle). URL: https://pdg.lbl.gov/2024/reviews/rpp2024-rev-cosmological-parameters.pdf — Table 25.1 Ω_Λ = 0.685 ± 0.007 (Planck TT,TE,EE+lowE+lensing); +BAO column Ω_Λ = 0.689 ± 0.006; text: Ω_tot = 0.9993 ± 0.0019 with BAO (⇔ Ω_K ≈ +0.0007 ± 0.0019).
4. **ACT Collaboration — DR6 Power Spectra, Likelihoods and ΛCDM Parameters**. arXiv: **2503.14452**. Abstract quote verified: "no departure from spatial flatness."
5. **DESI Collaboration — DR2 Results II** (OPTIONAL). DOI: **10.1103/tr6y-kpc6**. arXiv: **2503.14738**.
6. **Chen & Zaldarriaga 2025** (OPTIONAL secondary citing DESI Ω_k). arXiv: **2505.00659** — reports DESI+CMB Ω_k = 0.0023 ± 0.0011 as cited from DESI DR2.

---

## Soft SF labels (summary)
- **C14 → MATCH** (Ω_Λ, ρ_Λ, and Λ all match PDG Planck-via-PDG table; Planck primary Ω_Λ agrees within rounding).
- **C16 → MATCH** (Planck+BAO Ω_K exact; ACT DR6 flatness phrase verified).

## Explicit NON-claims (Hard Soft SF)
- **No invent** of residual-C ↔ Cosmo / DE / curvature physical mappings.
- **No invent** of Ω ratios or transfer coefficients.
- **No invent** proofs or fabricated citations.
- **No tip edit**; tip Soft SF LOCK sha256 unchanged; tip_touched **NO**.
- **No catalog edit**; catalog sha256 **UNCHANGED**.
- **No CERT**.
- **No** force Soft SF MATCH of DESI optional rows to Author Item4 / residual-C.
- DESI rows are **OPTIONAL cross-check only**, clearly labeled.

## STATUS
RESOLVED this Soft SF beat: invent-free C14+C16 source verification complete. invent HOLD stands. Soft SF → Auditor.

