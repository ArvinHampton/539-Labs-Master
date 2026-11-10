# NL Rule-5 REVIEW — PR1 χ² trio (a)(b)(c) INVENT RESUME Rule-4 — 2026-10-27 ~12:08 CDT America/Chicago
Reviewer: Non Local Path. Write-only, cite-only. No RECS.

## Subject (live MATCH)
- FINDINGS PR1-FINDINGS-CHI2_TRIO_INVENT_RESUME_RULE4_2026-10-27.md `ebc05e25f1cb902623dc602d9164ba6dd429bf80b3744e96fdc2f7a6135836ed`
- PRESS SOFTSF_PRESS_PR1_CHI2_TRIO_INVENT_RESUME_RULE4_2026-10-27.md `bf47ca1b69a7100e6af4ac0822e7fb24225ff6e55a55149c1cf37a13eb1e2e8e`
- tip LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` MATCH READ ONLY
- Invent authority ACK+BEGIN Soft SF 75c7160f… (NL ACCEPT Soft SF 4ccc78bc…) MATCH

## Verdict: ACCEPT-WITH-FLAGS
Honest invent Soft SF under OWNER LOCK invent lift. Slots (a)(b)(c) are all marked INVENTED; no fake DESI/ATLAS numbers; decisive recompute NOT RUN; prior Written-only INCONCLUSIVE stands. Arithmetic checks live: dof 12−3=9; χ²_min target 0.79×9=7.11; P(χ²₉≥7.11)≈0.626; 95% band of χ²₉/dof ≈[0.300,2.114]; |0.79−1|≈0.45 sd at dof=9.

### Lemma review
- L1 whitening: ACCEPT (PROVEN).
- L2 Cochran dof under H1–H2: ACCEPT (PROVEN).
- L3 moments: ACCEPT (PROVEN); 0.79 is unremarkable at dof=9.
- L4 block additivity under H3: ACCEPT (PROVEN).
- L5 Beta null for ρ²: ACCEPT with FLAG-1.
- L6 Bonferroni: ACCEPT (PROVEN).
- L7 invent-sensitivity: ACCEPT (PROVEN) — invented dof cannot validate the model against Written data.

### FLAG-1 (precision, L5)
The Beta(1/2,(N−p−1)/2) null for ρ² holds when the template τ is fixed (non-data-dependent) before seeing y. If τ is chosen or tuned from the same residuals (e.g. SCRIPT SUB/SUPER_HARMONICS fit to y), the null is no longer Beta and L5+L6 understate look-elsewhere. Fix: state “τ fixed a priori”; for data-dependent τ use a separate null (permutation / sample-split).

### FLAG-2 (cite, Fact (c).F)
Script E_leak(0)≈45.28 vs historically asserted 6.07e-12 conflict is correctly left unresolved (Owner Write). NL does not re-audit the script live this beat; FLAG only that Fact (c).F is SCRIPT-arithmetic, not a Written physics claim — already how PR1 labels it. No class change.

No invented values treated as Owner-Written. tip_touched NO. Kerr BLOCKED. Soft SF → Auditor.
