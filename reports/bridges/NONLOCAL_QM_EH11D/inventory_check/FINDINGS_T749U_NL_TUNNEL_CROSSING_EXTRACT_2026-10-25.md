# FINDINGS t749u — NL tunnel / barrier / exp-crossing EXTRACT (2026-10-25, CDT)
PREREG: prereg/T749U_NL_TUNNEL_CROSSING_EXTRACT_20261025/PREREG.md sha256 2fe34c2513cf883464e820030da4d0e73ecc0b1e734303909accc747bd540e0d (written before this file).

## VERDICT: ABSENT-with-gap
No Written NL/EH11D/PT source on disk states a transmission coefficient T, a barrier width L with decay constant κ, T≈e^(−2κL), or width-doubling ⇒ T². Nothing is DEDUCED. No AUTHOR-CANDIDATE package built: the nearest Written objects (below) do not carry a width variable, so framing one would require inventing κ/L (invent-ban).

## Scope searched
Track root, inventory_check (incl. _drive_unpack A/B, drive_extracts, author_candidates, prior FINDINGS T652U/T660U/T665U/T674U/T682U/T685U, OMEGA_F_FACTOR_TABLES, OMEGA_11D_STRUCTURAL), prereg. Terms: tunnel, transmission, barrier, WKB, instanton, κ/kappa, e^{-…}, exp(−…), exponential suppression, penetrat, throat, warp.
Hits for "transmission coefficient", "WKB", "κL", "T²": **zero**.

## Near-misses (NOT tunneling mates)
| # | Object | Source (attachments/, sha256) | Why not a mate |
|---|---|---|---|
| NM1 | S ℏ Ω e^{−S}(1−E_em/ΔE) | S²-11DM²ET-X.txt l.60 (620592e6…f8bf5); also Corrected 7D Torsion l.98, Three-Body l.100 (14e5a826…63ed), QGP-HEP l.63 | Instanton-style weight but S undefined as an action over a width; no L; labelled "-U gamma decay / coherence", not a crossing. Closest Written-adjacent item; would need Arvin to define S=2κL (that would be NEW). |
| NM2 | "Instanton entropy"; "Hampton e³ Instanton Theorem" | S²-11DM²ET-X.txt l.41, l.176 | Titles/table entry only; no amplitude formula. |
| NM3 | "exponential suppression follows from the negative-signature energy barrier for PBHs in −U" | Negative-Signature Functional Analysis… l.541 (fae73b96…f8bf5) | Prose; factor is Boltzmann e^{−M_PBH/k_BT}, thermal not tunneling; no width. |
| NM4 | Thm 46: leakage ΔE≈5–15 MeV "reduces effective barrier in +U projection"; P_leak ∝ sin²(2πt/539.9) | Theorems 41-61 l.119 (f9b8e15a…a5e728) | Fission-barrier prose; crossing is periodic (539.9 s, Cat B phase), not e^(−2κL). Closest to a ±U "cut" crossing but no exponential-in-width. |
| NM5 | Ringdown "tunnels through a wormhole throat" | Three-Body l.247 | Paraphrase of external Sept-2025 arXiv paper; not Arvin Written formula. |
| NM6 | Warp e^{−kb}=243/539 (κ_dark) | DRIVE_HUNT_OMEGA_ZEFF File 6 §7 | "Inserted ratio"; warp factor, not transmission; κ_dark is a coupling ≠ decay constant κ (symbol collision). |
| NM7 | exp(−2ky), y_max tuned | 17 Theorems v5 5a6a1d87… l.2123–2128 (via T674U 5b36037b…) | RS warp profile; formally e^{−2·k·y} but y is a bulk coordinate, y_max tuned; no transmission semantics, not forced. Superficial shape match only — NOT promoted. |
| NM8 | "tunneled/spacetime tunneling" (Boring Company) | latex_book_document_class_configurations.tex l.104, l.215 | Metaphor. |

## Gap (what Written would need)
A Written statement on the NL side defining a barrier across the local↔quantum-modular cut with explicit κ and width L (or S as a function of width) and T=|amplitude|² — none exists. Local Bridge C geometry not imported. WRITTEN-CHAT not used to close anything.

## Standing held
t685u ACCEPT untouched; W-PO-2 CLOSED; W-PO-3 FINISHED; Φ_flux↔539.9 s Cat B; CORE_FREEZE; invent-ban; no NL2; no order78; maps separate; no Local files touched; no push; no messages.
