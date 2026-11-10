> **SUPERSEDED 2026-10-24 22:54 CDT:** Ω₁₁D(k,K,b,Φ) written by Arvin t591u (pin a6dfcec4…/6de428d8…); see NL1_OPEN_SUPERSEDED_BY_T591U.md. History below retained.

# NL1 — Ω₁₁D(k,K,b,Φ) search result (2026-10-24, read-only)
Verdict: **ABSENT** — no written Ω₁₁D = f(k,K,b,Φ), and no Ω₁₁D derived from EH lock / N=4880 flux quantization, anywhere under /workspace.

## Primary source (Codex 20709375) — quote
- reports/self-audit/zenodo/txt/20709375_*.txt and theorems/periodic-table-codex.txt:18 "single 11D geometry factor Ω₁₁D absorbs all scaling"; :46 "scaled by the single geometric factor Ω₁₁D (fixed once by 11D compactification geometry)". No formula, no value.

## Other written Ω_11D definitions found (all Category B, none in k,K,b,Φ)
| id | path:line | written form | note |
|---|---|---|---|
| EH-Ω1 | reports/crypto/RPP_spec_v1/scripts/chats/e1a411f6-…txt:17335,17794,18374 (also 984f09e4…:5646,5669; grok-chats/raw-neutrino/c39b5dc0…:499) | Ω_11D = 1/√(1+g_11²+g_s²) ≈ 0.99995, with g_11=9.70e−3, g_s=9.80e−3 (same file :17427,:17430) | couplings inserted, not from L1–L7 / N=4880 |
| EH-Ω2 | reports/s_family_paths/A30_540_thermo/logs_search3.txt:33 | Ω_11D = 1/√(1+g_11²+g_s²+(539.9/540)²) ≈0.99994 | contains inserted 539.9 s → excluded |
| EH-Ω3 | reports/s_family_paths/A22_grok_export_search/chats/e85353a0-…txt:~405 | "Ω_11D = 0.99987  # Geometry-fixed 11D scaling factor (absorbs all relativistic + many-body corrections)" | fit/absorber constant; differs from 0.99995 |
| EH-Ω4 | A22 chats/8537483b-…:1551 | "Ω_{11D} = 1 (normalized)" | normalization choice |
| critique | A22 chats/e9658c0b-…:97 (dup RPP chats/6a433805…:19075) | "The division by √Ω_{11D} (with g_{11} and g_s plugged in) is tuning, not derivation." | source-side self-critique |
Consequence: Ω₁₁D is written with ≥3 inconsistent values (0.99995 / 0.99994 / 0.99987 / 1) and no k,K,b,Φ dependence. Using any as "the" Ω₁₁D would be a free choice → no PREREG.

## N=4880 hits
Only: EH1 (EH-k) k₁₁ miss; Mirror_Periodic_Table_Halo_Extension.md:21 "N_flux=4880 … Cat A / locked" (no Ω, no L1–L7); fsnap=243/4880 inserted (EH1:95); Collatz/T3 orbit code in grok_export (unrelated). None fixes Φ in a written Ω₁₁D.

## periodic_table_539labs.json
**ABSENT** (find / -name '*539labs*' → only reports/crypto/RPP_spec_v2_drafts/mirrors/539labs.org_index_2026-10-23*.html + a patch). Nearest: A22 chats/e85353a0 Python `PERIODIC_TABLE` "representative subset (full 118-element .npz/CSV generated identically)" — subset only, full table not present; model_first_ie values tied to Ω=0.99987 absorber (Cat B).
