# AUDITOR FINDINGS — PR1 PURSUE ALL catalog rev.16 CONFIRM (t2033)
Date: 2026-10-25 ~20:38 CDT (America/Chicago). CONFIRM-only; no physics invented; no edits to catalog, report, or residual-C.

## Verdict: MATCH-with-SF

## Hashes (verified on box)
- Catalog rev.16 `/workspace/obs-data-PR1-HEPP-QM-GR.md`: 0a9ef2dc75496d3b3e523e5b27e169c433285e8f9f345f4ba08c7297fac20f90 (MATCH expected)
- Prior rev.15 backup `obs-data-PR1-HEPP-QM-GR.md.pre-rev16-29cf7c98.bak`: 29cf7c98d3ef0ea670acae4580eeeee7fb21d4c4eeb80b0a4520d28f29090b87 (located; MATCH)
- Report `/workspace/quantum-comp/reports/PR1_PURSUE_ALL_t2033_2026-10-25.md`: 13f090fa5c7609b03d8abaaf042431f9dc1f4a7b3bb0f847dda789e13e9feee7 (MATCH)
- Prior CONFIRM FINDINGS (rev.15, t1129u): 84f6ebaf5b1f599c20ad7887f3d8b798fc2b327336073cf679de55f815df3afa (cited in the catalog rev.16 changelog and the report)
- residual-C live `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: c7121aa8bf7d2e534f0ad55ce1b4a1a1a26db8289087979f3a263efe9565a5ef (mtime 20:34:37 CDT, changed by another lane)

## Checks
- Soft SF-A (t₀ restored): ADDRESSED. No corrupted "t>" left in the body. The only remaining instance is the changelog quoting the old glyph.
- Soft SF-B (Table VII subset): ADDRESSED. The subset is stated explicitly, and the α=0.5/1.5/2.5/3.5 GWTC-3 row was added [V]. All 8 α values are quoted.
- Extra LVK: the GWTC-4.0 TGR II SME bound |k₀₀⁽⁵⁾| ≤ 1.52×10⁻¹⁴ m (90%, 40 O4a events) is folded [V]. The other GWTC-4.0 TGR II bound, mg ≤ 1.92×10⁻²³ eV/c², is also present. PRESENT.
- GP-A secondary caveat: KEPT. The Vessot 1980 ADS fetch returned HTTP 405, and the catalog states the caveat as secondary-only (Herrmann 2018 / Will LRR).
- Bridge PARTIAL / READY NO: MATCH.
- No Cat A: MATCH. There is no Author ACCEPT for residual-C, and the invent-ban is held.
- PR1 tip / residual-C touched: N. Only the catalog tip cite was refreshed, read-only, to c7121aa8…. The drift 87fcda27→c7121aa8 came from another lane and is disclosed in the report.

## Soft SF (new, non-blocking)
- SF-1: the §2F DE-transfer line (catalog line 198) still cites "tip 87fcda27…". Other cites were refreshed to c7121aa8…, so this cite is inconsistent with them.
- SF-2: the report header lists the pre-refresh catalog sha 7a4d795b… and says the post-refresh sha is "see parent message". The final rev.16 sha 0a9ef2dc… is recorded only here, not in the report.
- SF-3: the residual-C .sha256 sidecar may be stale relative to the live c7121aa8… (carried from prior lanes; not PR1's scope).

residual-C untouched by PR1: Y.
