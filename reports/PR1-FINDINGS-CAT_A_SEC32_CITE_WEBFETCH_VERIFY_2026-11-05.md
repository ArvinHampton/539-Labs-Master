# PR1 FINDINGS — Cat A Soft SF — §3.2 cite WebFetch verify (2026-11-05)
REPORT only. No CERT. No RECS. Cite-only; invent HOLD STANDS. No tip edits.

## §0 Integrity / authority
- Authority: Owner Soft SF via Physicist (cite-verify lane for Cat A §3.2 pack). Video EXCLUDED.
- Source FINDINGS: `/workspace/quantum-comp/reports/PR1-FINDINGS-CAT_A_539_CORPUS_SEC32_BARYON_PEAKS_6p32_6p84_2026-11-03.md`
  - live sha256 **575e7aa472b574e7c5390f89e398b2c8bf2f66d4f2c9e16923ce64b5fa7c4f31** — MATCH Soft SF 575e7aa4…
- Companion PRESS present: `SOFTSF_PRESS_PR1_CAT_A_539_CORPUS_SEC32_BARYON_PEAKS_6p32_6p84_2026-11-03.md` (read-only this turn).
- tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha **7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91** — pre MATCH / post MATCH. tip_touched **NO**. tip Soft SF LOCK preserved.
- Method: WebFetch (and curl HEAD for PDFs) of each public LHCb / arXiv abs / PDG URL named in the 2026-11-03 FINDINGS. No new literature invented. No recommendations.

## §1 Cite inventory (from source FINDINGS)
Cites tied to 6.32 / 6.84 GeV / Ω_b / Ξ_b / LHCb:

| # | Cite key | URL / resolver |
|---|---|---|
| C1 | LHCb-PAPER-2019-042; PRL 124 (2020) 082002 | https://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/LHCb-PAPER-2019-042.html |
| C2 | LHCb-PAPER-2021-025; PRL 128 (2022) 162001 | https://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/LHCb-PAPER-2021-025.html |
| C3 | PDG listing Ξ_b(6333)⁰ | https://pdg.lbl.gov/2025/listings/rpp2025-list-Xi-b-6333-zero.pdf |
| C4 | PDG listing Ω_b⁻ (ground) | https://pdg.lbl.gov/2025/listings/rpp2025-list-omegab-minus.pdf |
| C5 | PDG RPP-2025 table (URL as in source: mesons-bottom) | https://pdg.lbl.gov/2026/download/rpp-2025/tables/rpp2025-tab-mesons-bottom.pdf |
| C6 | LHCb-PAPER-2020-014; JHEP 11 (2020) 095 | https://lhcbproject.web.cern.ch/lhcbproject/Publications/LHCbProjectPublic/LHCb-PAPER-2020-014.html (+ arXiv:2009.02481) |
| C7 | arXiv:2104.04759; LHCb-PAPER-2021-002; Chin. Phys. C45 (2021) 093002 | https://arxiv.org/abs/2104.04759 |

## §2 Per-cite WebFetch verify

### C1 — LHCb-PAPER-2019-042 / PRL 124 (2020) 082002 — **VERIFIED**
- Page live. Title: "First observation of excited Ω_b⁻ states." Journal line: Phys. Rev. Lett. 124 (2020) 082002; arXiv:2001.00851.
- Mass claim MATCH: m(Ω_b(6316)⁻)=6315.64±0.31±0.07±0.50 MeV; m(Ω_b(6330)⁻)=6330.30±0.28±0.07±0.50 MeV; Γ(Ω_b(6316)⁻)<2.8 MeV (90% CL); after LEE, Ω_b(6316)⁻ global significance 2.1σ.
- Quote confirmed: "The observed peaks are consistent with expectations for excited Ω_b⁻ resonances."

### C2 — LHCb-PAPER-2021-025 / PRL 128 (2022) 162001 — **VERIFIED**
- Page live. Title: "Observation of Two New Excited Ξ_b⁰ States Decaying to Λ_b⁰ K⁻ π⁺." Journal: Phys. Rev. Lett. 128 (2022) 162001; arXiv:2110.04497.
- Mass/width MATCH: m(Ξ_b(6327)⁰)=6327.28^{+0.23}_{-0.21}±0.12±0.24 MeV, Γ<2.20 MeV (90%); m(Ξ_b(6333)⁰)=6332.69^{+0.17}_{-0.18}±0.03±0.22 MeV, Γ<1.60 (1.92) MeV at 90% (95%).
- Quote confirmed: "in good agreement with the expectations for a doublet of 1D Ξ_b⁰ resonances."
- Note (not FAIL): source FINDINGS compressed Ξ_b(6333)⁰ systematics to a single ±0.22 MeV; paper/PDG carry ±0.03 (syst) ±0.22 (Λ_b mass). Key mass/width/quote MATCH; no classification change.

### C3 — PDG Ξ_b(6333)⁰ listing — **VERIFIED**
- PDF live (HTTP 200). Citation Navas et al., PRD 110, 030001 (2024) and 2025 update.
- Status *** ; J^P = ?? ; mass 6332.69^{+0.17}_{-0.18}±0.22 MeV (AAIJ 22I / PRL 128 162001); width <1.92 MeV (95%).

### C4 — PDG Ω_b⁻ ground listing — **VERIFIED**
- PDF live (HTTP 200). OUR AVERAGE mass 6045.8±0.8 MeV.
- Quote confirmed: "In the quark model Ω⁻_b is ssb ground state."

### C5 — PDG RPP-2025 table URL (mesons-bottom) — **VERIFIED** (URL resolves; key organizational claim MATCH)
- PDF live (HTTP 200) at the exact source URL.
- Organization section lists excited Ω_b states including Ω_b(6316)⁻, Ω_b(6330)⁻, Ω_b(6340)⁻, Ω_b(6350)⁻ — supports source claim that the PDG 2025 named Ω_b excited sequence ends at Ω_b(6350)⁻ (no PDG-listed baryon near 6.84 GeV in that organizational map).
- Note (not FAIL / not cite-correction): URL path is `…tab-mesons-bottom.pdf` while the prose claim concerns b-baryons; content nonetheless carries the b-baryon organizational list used by the source. Alternate `…tab-baryons-bottom.pdf` paths returned 404 this turn.

### C6 — LHCb-PAPER-2020-014 / JHEP 11 (2020) 095 — **VERIFIED**
- LHCb public page live; arXiv:2009.02481 abs/HTML also fetched.
- Title: "Search for the doubly heavy Ξ_bc⁰ baryon via decays to D⁰ p K⁻." Journal: JHEP 11 (2020) 095.
- Quotes confirmed: "No significant signal is found in the invariant mass range from 6.7 to 7.2 GeV/c²"; body: "expected to have a mass in the range of 6.8–7.1 GeV/c²"; "The Ξ_bc⁰ baryon has not been observed to date."

### C7 — arXiv:2104.04759 — **VERIFIED**
- abs page live. LHCb-PAPER-2021-002; CERN-EP-2021-046; published Chin. Phys. C45 (2021) 093002.
- Title: Search for doubly heavy baryons Ω_bc⁰ and Ξ_bc⁰ decaying to Λ_c⁺π⁻ and Ξ_c⁺π⁻.
- Quote confirmed: "No significant excess is found for invariant masses between 6700 and 7300 MeV/c²."

## §3 Classification status (peaks)
| Peak | Prior Soft SF class (2026-11-03) | Cite-forced change? |
|---|---|---|
| 6.32 GeV | PARTIAL | **NO** — all C1–C4 mass/interpretation quotes MATCH |
| 6.84 GeV | ABSENT | **NO** — C5–C7 null-search / no-PDG-entry claims MATCH |

No cite-correction recorded. Peak classifications remain PARTIAL / ABSENT as prior Soft SF.

## §4 Summary table (VERIFIED / FAIL)

| Cite | Result | Confirmed (short) |
|---|---|---|
| C1 LHCb-PAPER-2019-042 / PRL 124 082002 | VERIFIED | Ω_b(6316/6330) masses, Γ<2.8 MeV, 2.1σ global; excited-Ω_b quote |
| C2 LHCb-PAPER-2021-025 / PRL 128 162001 | VERIFIED | Ξ_b(6327/6333) masses/widths; 1D doublet quote |
| C3 PDG Ξ_b(6333)⁰ | VERIFIED | *** ; 6332.69 MeV; Γ<1.92 (95%); J^P=?? |
| C4 PDG Ω_b⁻ ground | VERIFIED | 6045.8±0.8 MeV; ssb ground-state wording |
| C5 PDG mesons-bottom table URL | VERIFIED | live PDF; org list ends Ω_b(6350)⁻ |
| C6 LHCb-PAPER-2020-014 / JHEP 11 (2020) 095 | VERIFIED | null 6.7–7.2 GeV; expected 6.8–7.1; not observed |
| C7 arXiv:2104.04759 | VERIFIED | null 6700–7300 MeV/c² |

**FAIL count: 0 / 7.** invent HOLD STANDS. No CERT. No RECS. tip_touched NO.
