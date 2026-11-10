# FINDINGS — t1118u PR1 Author-power pursue CONFIRM (2026-10-25, America/Chicago)
Auditor scope: CONFIRM-only. No physics added. No measured-row PASS/FAIL altered. residual-C not edited.

## Verdict: **MATCH-with-SF**

## Hashes (sha256, all verified on disk)
- Stamp OWNER_AUTHORITY_SEARCH_PURSUE_WRITE_APPLY_t1118u: `c1d59d58d391e03340eb2b79391d519fa4eac6f7259239d16a4599ff387ee014` — MATCH
- Catalog /workspace/obs-data-PR1-HEPP-QM-GR.md (rev.14): `586dcf94986c33414ebcf5dcf0ee9eebed3181cb4a03dac3c2182d5ff9e7daec` — MATCH
- Prior backup obs-data-PR1-HEPP-QM-GR.pre-rev14-67ee59e8.md (rev.13): `67ee59e844b9a602c26509fd8e726c816116fa2ab81d9cfda87868ee8c27bb6b` — MATCH to prior tip
- Report PR1_AUTHOR_POWER_PURSUE_t1118u: `d73f732daab4fc8ba2d2d69e7cebea2a7f8518e4dc28b6f269e419b87b527a92` — MATCH
- reports/OWNER_WRITE_PR1_TORSION_HOLE_STRIKE_COUPLING_t1118u: `39359cf72b315f24b41e505b0b70c9922f0e8f59282a48e660e4519a4c83626d` — MATCH
- reports/OWNER_WRITE_PR1_EXPOSES_ELECTRON_FIELD_MECH_t1118u: `d6e71e092c3093bc0af45872f8960b8857098cf7d00e423ef6e64765a35367e2` — MATCH
- reports/OWNER_WRITE_PR1_W4_RATES_COEFFS_t1118u: `8c402294a5ce9fe60c9dbbe43bf007fa74dfddf5ff6e9d31014fabc34e424abf` — MATCH
- residual-C tip (before and after this write): `492fb3ac95c20e9117594639eb5947c90785a09e93da8301d6e83980c490a6fa` — untouched

## Per-expect
1. **rev.14 delta vs rev.13 — PASS.** The diff has 5 hunks: the header rev line; §2B GW250114 ringdown/Kerr sub-bullet added; §2B GWTC-3 row corrected and extended; §2F rev.14 Author-power status paragraph; §4.7 folded, plus changelog/footer. No other lines changed.
2. **Writes keep ABSENT framing — PASS.** All three Writes are on disk with matching sha:
   - Torsion hole: strike, post-collision and coupling are ABSENT. The d2a0bf2e quote is framing only, explicitly not linked to photons.
   - Electron field: mechanism ABSENT.
   - W4: W4.3/W4.4/W4.6 rates are ABSENT. The W4.6 qualitative channel is Written. The Ecosmos Φ equation is a CANDIDATE and not adopted.

   The catalog §2F text agrees with this tag for tag and imports no mechanism or number ("No catalog numbers come from Author text").
3. **LVK [V] fold — PASS.**
   - GWTC-3: m_g ≤ 2.42×10⁻²³ eV/c² (90%) and |−1PN| ≤ 7.3×10⁻⁴ are present.
   - GW250114: ≥2 ringdown modes at 4.1σ are present.

   Both are backed by the report's §D, which records the arXiv PDF re-fetch (2112.06861 `10451d67…`, 2509.08054 `1d10e5bc…`). The extra digits in the same rows (δf̂₂₂₀/₂₂₁, ΔM_f, ±30% Kerr, A₂₂₀ >7σ) come from the same re-fetched sources and the report lists them, so they are not unbacked rows. No new [V] row exists outside GWTC-3 and GW250114. Auditor did not independently re-fetch the PDFs; digits are scored for consistency between report and catalog.
4. **Status flags — PASS.** Bridge PARTIAL / READY NO. Not Cat A. residual-C LOCKED. The invent-ban lift is scoped to t1118u Author scope. There is no Zenodo blocker citation.
5. **residual-C untouched — PASS.** `492fb3ac…` before and after.

## Measured rows
One measured row changed value: GWTC-3 m_g went from 1.27×10⁻²³ [SOFT] to 2.42×10⁻²³ [V rev.14][HARD]. This is a primary-source correction, backed by the re-fetch and tasked LVK fold. It is a null-test bound, so no PASS/FAIL outcome changed (still "no deviation from GR"). The GW250114 area-law row is unchanged; the ringdown sub-bullet was added. No other measured row changed.

## Soft SF (clerical)
- SF1: §4.7 keeps the rev.13 text after "*Prior rev. 13 text follows:*". It carries a stray `):**` bold-marker fragment and a stale "not folded / no digits quoted" sentence. These are cosmetic.
- SF2: In the GW250114 bullet, the start time is written as "t₀ = 6 t_Mf" in one place and "t₀ = 6 t_M" in another. This is a notation inconsistency.
- SF3: The GWTC-3 row carries both "[V rev. 14]" and a trailing "[HARD]" tag. This is redundant tagging, not a conflict.
