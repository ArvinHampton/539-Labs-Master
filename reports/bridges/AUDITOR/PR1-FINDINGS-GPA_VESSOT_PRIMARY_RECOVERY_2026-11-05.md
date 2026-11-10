# PR1 FINDINGS — GP-A Vessot primary recovery (2026-11-05)
Status: STARTED → RESOLVED (primary mission digits obtained; PRL page-level digits remain paywalled — see Gaps)
Auth: OW 06748ff29e8b5e103833c5dec0712443a255d4e26990ea53acaa8793306fe9e2 ("Physics Research 1: retrieve Gravity Probe A measurements.") + OW bcc3ced0f1dfe15560e0bdb2e45bb35f4b1db26dcfb439e647a98c12fc5bc9a9 (PRIMARY OPERATING RULE). Both sha-verified on disk.
Locks: tip Soft SF LOCK untouched (sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 re-verified). invent HOLD respected — digits below quoted verbatim from primary text; nothing invented. No CERT. No publish. No spend. No RECS.

## Primary source recovered
Vessot, R.F.C. & Levine, M.W. (SAO), "Gravitational redshift space-probe experiment", NASA final report (NAS8-27969 lineage), pub. 1979-12-01, NTRS 19800011717, 145 pp.
URL: https://ntrs.nasa.gov/api/citations/19800011717/downloads/19800011717.pdf (HTTP 200, 5,988,729 B)
Local copy: sources/gpa/NTRS_19800011717_Vessot_Levine_1979.pdf sha256 1f129029cfa0e87ce03807567ef334995eb5e47dab367a6104cad4f6eb4e69e7 (+ pdftotext .txt). Same authors/mission/data as PRL 45, 2081 (1980).

## Digits (verbatim, OCR of scanned report)
| Quantity | Value | Location |
|---|---|---|
| Formal redshift-agreement parameter ε (regression, 100-s intervals) | ε = (5 ± 126) × 10⁻⁶ | §15 Experiment Results, p.90; Fig. 32 ("SLOPE 5 X 10-6", "ONE SIGMA UNCERTAINTY OF SLOPE = ±126 X 10-6") |
| Bias uncertainty (Table 4 system bias) | ±6.8×10⁻¹⁵ / 1.13×10⁻¹⁰ = ±60.2×10⁻⁶ | §15, p.90 |
| FINAL RESULT (RSS) | Δf/f = [1 ± (5 ± 140) × 10⁻⁶] Δφ/c² — "as our final result" | §15, p.90 |
| Redshift at apogee (flight result) | 4.283 × 10⁻¹⁰ (preflight pred. 4.295e-10) | trajectory table |
| Apogee geocentric radius | 1.66242 × 10⁴ km | same table |
| Δφ/c² span used (apogee→1322) | 1.13 × 10⁻¹⁰ | §15, p.90 |
| Gravitational effect / oscillator stability | ~4.5 parts in 10¹⁰; stability better than 1 part in 10¹⁴ | Abstract |
Interpretation (no new claim): |α| ≡ |ε| ≲ 1.4×10⁻⁴ (1σ, with ε central 5e-6) — consistent with secondary Herrmann 2018 α_rs < 1.4e-4 and Will LRR |α| < 2e-4 (Will's 2e-4 is the conventional rounded statement).

## Routes tried
- doi.org / journals.aps.org abstract: HTTP 403 (curl). PRL full text paywalled.
- OpenAlex W1977499976: is_oa=false, no pdf_url. Semantic Scholar: abstract null, no OA pdf. Unpaywall: 422 (needs valid email; not pursued).
- NASA NTRS API: SUCCESS (19800011717).

## S20 classification
S20 GP-A: PARTIAL (primary-open) → primary-VERIFIED (mission final report, Vessot & Levine 1979). Recommend catalog change; held for Keeper (no catalog edit performed here).

## Gaps (remaining)
1. PRL 45, 2081 page-level text itself not retrieved (paywalled); digits are from the authors' NASA final report of the same experiment. If PRL quotes a different rounding (commonly "7×10⁻⁵" / 1.4e-4 level), it is not verified here.
2. Values OCR'd from scan; cross-checked across p.90 text and Fig. 32 labels (consistent).
