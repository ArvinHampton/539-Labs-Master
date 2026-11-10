# FINDINGS — PR2 VANISHING LEAD Rank 22 RG2 ρ_u · 2026-10-26 11:08 CDT (America/Chicago)
Authority: Owner voice LOCK via Physicist (rotate after Rank 33). VANISHING_LEAD_ASSIGNMENTS live sha 9e9118b8… (PM cited df2523ab… — DRIFTED; noted, not blocking).
Integrity: tip Soft SF LOCK 7cddb188… (MATCH; tip_touched NO). Catalog v0.5.11 4ed155d5… UNCHANGED.
Soft SF invent HOLD. Soft SF F3 CLOSED. No tip fold. Bridge PARTIAL READY NO. Φ stays REJECTED. Cite-only.
Map source MERGED_VANISHING_MAP_STUB_2026-10-26.md sha b3e0d20b… (MATCH), row 22: "RG2 c1-end shadow pieces vanish together on ρ_u [CI#29] | — | — | vanish | prereg (Cat A lemma corollary) | order16/PREREG.md L38 | d0cafdcf6367 | —".

## Vanishing point
Rank 22 — bridges/BRIDGE_C_35/order16/PREREG.md L38 (sha d0cafdcf63675c31… MATCH PREREG.sha256; L38 VERIFIED):
"No new Residual–Resonant map is proposed. **Map RG2 (residual-internal, statement only):** the c1-end shadow pieces of the two sectors vanish together exactly on the ρ_u set. This is a corollary of the Lemma (Category A), so it needs no test."
CI#29 (CORPUS_VANISHING_INVENTORY L55) matches: "c1-end shadow pieces of two sectors vanish together on ρ_u set (RG2) … vanishes (corollary of a Cat A Lemma) | prereg statement".
Caveat, order16/NOTES.md L2: "Map RG2 as stated in PREREG is imprecise: the P-odd c1-end piece is a product with θ_{7/2}, so it can also vanish if θ_{7/2} ≡ 0, not only on the ρ_u set. … No test depended on RG2."
order16/RESULTS.md L7: "Map RG2: corollary of the Lemma (see NOTES for an imprecision)."

## Backwards inference — RG2 vanishing → residual-C / T-D ξ-shadow track?
Disposition: **ABSENT link**
No Author-written or Owner-Write text maps RG2 (c1-end shadow pieces / ρ_u set) to the residual-C modular target or the T-D ξ-image/shadow template. RG2 is self-labelled "residual-internal, statement only" and PREREG L38 explicitly says "No new Residual–Resonant map is proposed." Exact-token search for RG2 (excluding RG20+) repo-wide: hits only in order16 and the derived inventory/stub/assignments files. T-D Write (sha 8eab95d3…, .sha256 OK; matches INDEX L10) cites MR1 reverse-all AMEND-2 / invent lift / P5a only; 0 hits for RG2|ρ_u|c1-end. INDEX: 0 hits. Tip Soft SF: 0 hits for RG2|ρ_u|c1-end.

Near-misses (not links; "shadow" word-overlap only):
1. T-D Write W-TD: "the obstruction class attached to residual-C — read as the ξ-image (shadow) … vanishes … at (Γ₀(49), ρ̄)" — different object (ξ-image at Γ₀(49), ρ̄), no c1-end / ρ_u / BRIDGE_C_35 order16 cite.
2. MR1 reverse-all L102 "T-D (ξ / shadow template): Claim vanishing of ξ-image / shadow … BF/mock template only"; L144 V19 "Zwegers-type completion term vanishes for c₂=γc₁"; L148 V23 "shadow Ξ (wt 3/2) unidentified" — Zwegers/shadow vanishings, none cite RG2 or ρ_u.
3. Tip Soft SF L418 P5c "shadow form, Zwegers route … W₇-eigenspace containing the shadow is 1-dimensional"; §10.8 L668–672 Zwegers shadow template — no ρ_u/c1-end/RG2.
4. order16 PREREG L30–31: RG1′ iff (ρ_u criterion), "same Lemma applies to the P-odd ξ₁ factor ϑ⁻" — ξ₁ here is a BRIDGE_C_35 internal factor label, not the T-D ξ-operator image; no residual-C tie.

## Paths checked
- MERGED_VANISHING_MAP_STUB b3e0d20b…; VANISHING_LEAD_ASSIGNMENTS (live 9e9118b8…)
- bridges/BRIDGE_C_35/order16/{PREREG.md, PREREG.sha256, RESULTS.md, NOTES.md}; order28–33 + REVIEW_2026-10-24 (RG2x labels only = RG20–RG28, label collision)
- OWNER_WRITE_TD_XI_SHADOW_TEMPLATE (+.sha256), OWNER_WRITE_ALL_REVISED_VANISHING_TARGETS_INDEX, CORPUS_VANISHING_INVENTORY (CI#29)
- residual-c-field-WRITTEN_PREMISES_DRAFT.md 7cddb188… (read-only)
- grok-batches/MR1-AUTHOR-REVERSE-ENGINEER-ALL-VANISHINGS_2026-10-26.md
- repo-wide rg -P "RG2(?!\d)" over *.md
- Prior Rank 35/33 FINDINGS (format only)

## Status for lead table
Rank 22 status = ABSENT link (prereg Cat A corollary, residual-internal statement only, imprecise per NOTES; no written map to residual-C / T-D ξ-shadow; nearest = shared "shadow" vocabulary in T-D / Zwegers templates). No invent.
