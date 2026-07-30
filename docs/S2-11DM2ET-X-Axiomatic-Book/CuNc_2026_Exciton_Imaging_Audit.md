# CuNc 2026 Exciton Imaging — Femtosecond Data Audit

**Status:** `CUNC_2026_FS_AUDIT_CORRECTED`  
**Date lock:** 2026-07-30  
**Author:** Arvin B. Hampton / 539 Labs LLC  
**Rule:** Category A vs B mandatory. Empirical numbers must match primary literature.

---

## 1. Primary source

| Field | Value |
|-------|--------|
| Authors | Yang Luo et al. |
| Title | Orbital-resolved imaging of coherent femtosecond exciton dynamics in coupled molecules |
| Journal | Nature Communications (2026) |
| DOI | [10.1038/s41467-026-73191-0](https://doi.org/10.1038/s41467-026-73191-0) |
| Method | STM tip-localized photocurrent; two-pulse excitonic wave-packet interferometry |
| System | Copper naphthalocyanine (CuNc) monomer and dimer on NaCl / Ag(111) |

Supporting press summaries (non-canonical for numbers): Max-Planck FKF note; phys.org 2026-06-23.

---

## 2. Dataset numbers (authoritative)

### 2.1 Dephasing / coherence \(T_2\)

| System / state | \(T_2\) | Notes |
|----------------|--------|--------|
| Single CuNc (canonical headline) | **\(\approx 70\,\mathrm{fs}\)** | Fit of photocurrent interferogram |
| Single CuNc on thinner NaCl (2 ML) | **\(\approx 50\,\mathrm{fs}\)** | Faster dephasing |
| Dimer bright triplet (E1) | **\(\approx 60\,\mathrm{fs}\)** | State-dependent |
| Dimer dark triplet (E4) | **\(\approx 50\,\mathrm{fs}\)** | Slightly faster than bright |

### 2.2 Fit formula (paper)

\[
I(\tau)\;\propto\;\cos\!\left(\frac{\Delta E}{\hbar}\,\tau\right)\,e^{-\tau/T_2}
\]

- Oscillation **period** of the interferogram: **\(\sim 2.5\,\mathrm{fs}\)** (carrier of \(\cos(\Delta E/\hbar\,\tau)\); persists \(>200\,\mathrm{fs}\)).
- Envelope scale is \(T_2\sim 50\)–\(70\,\mathrm{fs}\), **not** the optical period.

### 2.3 Instrumental scales (not exciton \(T_2\))

| Quantity | Value |
|----------|--------|
| Laser pulse FWHM | \(\sim 10\,\mathrm{fs}\) |
| NaCl cross-correlation | \(\sim 15\,\mathrm{fs}\) |
| Delay scan (typical) | \(\sim -80\) to \(+200\,\mathrm{fs}\) |

---

## 3. Retracted draft numbers

The following expressions appeared in prior session prose / THEORETICAL_EXTENSIONS drafts and are **incorrect**:

| Draft claim | Status | Likely confusion |
|-------------|--------|------------------|
| Coherence time **2.3 fs** | **RETRACTED** | Misread \(\sim 2.5\,\mathrm{fs}\) **period** as \(T_2\) |
| \(0.031\,e^{-t/2.3\times 10^{-15}}\cos(2\pi t/5.0)\) | **RETRACTED** | Wrong \(T_2\), wrong period, amplitude **not** in paper |
| “2.3 fs confirms D2-brane / 11D phonon-defect qubits” | **FORBIDDEN language** | Cat B map only; dataset is molecular exciton dephasing |
| Phase-lock of CuNc dynamics to \(G_4=539.90\,\mathrm{s}\) | **Not in dataset** | Model overlay only |

**Code:** `CUNC_2P3FS_RETRACTED`  
**Replacement code:** `CUNC_T2_70FS_MONOMER_LOCKED_AS_DATA`

---

## 4. Correct numerical contact for Model notes

If \(E_{\mathrm{leak}}\) or any extension cites CuNc 2026, use **only**:

**Monomer (primary):**
\[
I(t)\;\propto\; e^{-t/T_2}\cos\!\left(\frac{\Delta E}{\hbar}\,t\right),
\qquad T_2 \approx 70\,\mathrm{fs},
\quad T_{\mathrm{osc}}\approx 2.5\,\mathrm{fs}.
\]

**Dimer (secondary, state-dependent):**
\[
T_2^{\mathrm{bright}}(E1)\approx 60\,\mathrm{fs},\qquad
T_2^{\mathrm{dark}}(E4)\approx 50\,\mathrm{fs}.
\]

Do **not** insert prefactor \(0.031\) unless a future primary-source fit publishes it.

---

## 5. Category classification

| Statement | Class |
|-----------|--------|
| \(T_2\approx 70\,\mathrm{fs}\) (monomer); period \(\sim 2.5\,\mathrm{fs}\) | **Empirical data** (external) |
| Bright/dark orbital-resolved imaging exists | **Empirical data** (external) |
| Map bright→+U leakage / dark→phonon-defect qubit | **Category B** model interpretation |
| Map to −Periodic Table / M2 tension / \(G_4\) | **Category B** |
| Confirmation of three-generation axiom or residual carrier | **Forbidden promotion** |

---

## 6. Cross-links

- Mirror extension: `Mirror_Periodic_Table_Halo_Extension.md`
- Numerical patch to leakage bookkeeping: `E_leak_CuNc_Numerical_Patch.md`
- Claim freeze: `CLAIM_TABLE_Master.md`
- Results JSON: `cunC_2026_audit_results.json`

---

## 7. One-line freeze

**CuNc 2026: \(T_2\approx 70\,\mathrm{fs}\) (monomer), interferogram period \(\sim 2.5\,\mathrm{fs}\); draft 2.3 fs and 0.031·exp·cos(2πt/5) terms are retracted; any ±U map remains Category B.**

*Per aspera ad astra.*
