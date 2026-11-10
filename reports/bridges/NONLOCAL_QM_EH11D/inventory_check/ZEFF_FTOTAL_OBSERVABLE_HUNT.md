# ZEFF_FTOTAL_OBSERVABLE_HUNT (Hunt B) — written 2026-10-24 22:20 CDT (file mtime)
Context read: CODEX_FTOTAL_STRUCTURE.md, PT_WRITTEN_LINKS.md, ARVIN_WRITTEN_NL_VARS.md. Quote-only.

| item | verdict | evidence |
|---|---|---|
| 1 Z_eff(Z,n,l) rule | ABSENT | Z_eff appears only as a symbol inside F_Coulomb^rel: theorems/periodic-table-codex.txt:53-54 "-\frac{Z_{\rm eff} \alpha \hbar c}{r^2}(1+\frac{(\alpha Z_{\rm eff})^2}{n^2})\Omega_{11D}"; same in theorems/batch-late/resonant-attractor-mathematics-hqh-539.txt:58-60. No rule. Only numeric: reports/s_family_paths/A22_grok_export_search/chats/13fd994e-…txt:669 [ASSISTANT 2026-06-10] "Z_eff = 79 * 0.85 # screened effective charge (standard for 6s)" — single ad hoc chat value for Au, not a rule. |
| 2 F_total → observable map | ABSENT | Paper/theorem: sum F_total = F_Coulomb+F_SO+F_torsion+F_flux+F_leak only (periodic-table-codex.txt:48). Chat claims without map: reports/s_family_paths/A22_grok_export_search/chats/482268c8-…txt:312-316 [ASSISTANT 2026-06-18] "Numerical integration of F_total across the table yields: ... Ionization energies: exact experimental match for every Z when Ω_{11D} is held fixed." ; reports/s_family_paths/A22_grok_export_search/chats/e85353a0-…txt:414 "model_first_ie: float # computed with full F_total * Ω_11D" with model values identical to exp values (lines 419-423, e.g. H 13.59844/13.59844) — circular, no procedure. WRITTEN-CHAT, not Cat A. |
| 3 NIST + tolerance prereg by Arvin | ABSENT | NIST hits are PQC/crypto (grok-chats/01-17-theorems.md:2681 etc.) or chat label "exp_first_ie # eV (NIST 2025)" (e85353a0:413, ASSISTANT). No Arvin-authored tolerance text. |

- periodic_table_539labs.json: still ABSENT (find -iname '*539labs*' → only AFRL_WhitePaper_539Labs.pdf/.txt, unrelated).
- Z=1–118 F_total table: still ABSENT. e85353a0:417 "Representative high-fidelity subset (full 118-element .npz/CSV generated identically)" — referenced, file not present; only 5 rows written, copied from experiment.
- Z-table numeric test: BLOCKED (no Z_eff rule, no F_total→observable map, no numeric Ω₁₁D in paper Cat A). No Z-table PREREG written. Nothing invented.
