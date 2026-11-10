# AUDITOR FINDINGS — t665u NL W-PO-2 deduction CONFIRM — 2026-10-25 00:27 CDT (America/Chicago)
Scope: NONLOCAL_QM_EH11D only. Read-only on NL files. Local (BRIDGE_C_35 / residual-C) untouched. No order78. PASS/FAIL not altered.

## Hash match (live sha256sum)
| File | Claimed | Live | Match |
|---|---|---|---|
| inventory_check/FINDINGS_T665U_WPO2_DEDUCTION_2026-10-25.md | ed41fb85…f243 | ed41fb85eb91eb001e289f0d39baf172b9c29621633b1becc9a52461ca26f243 | MATCH |
| prereg/T665U_WPO2_DEDUCTION_20261025/PREREG.md | 599712c3…e231 | 599712c3293b6ee4fedb7c6cd26fc4765985b7631d52a6b59c42563d852ce231 | MATCH |
| prereg/T665U_WPO2_DEDUCTION_20261025/result.log | 388a4a24…af70c | 388a4a24d54ca099a628801f9a936e79f0d44b49d9dd28438bfb6722c49af70c | MATCH |
| inventory_check/SHA256SUMS | 1858185c…cf24 | 1858185ca2b135511fa0e3188d795473e5de7a759a7c1a6779023c642b20cf24 | MATCH |
| inventory_check/STREAM_IDLE_WRITTEN.md (+ ../ mirror) | cc256f07…6e95 | cc256f077e3fa8e21bb13f69aead84aafa70c174ef760a1b3078bbcc05346e95 (both) | MATCH |
| Premise Codex docx | e24c4904…72da | e24c4904…72da | MATCH |
| Premise Explicit_Derivations docx | bf202d05…3ace | bf202d05…3ace | MATCH |
| Premise OMEGA_11D_STRUCTURAL | 946ba49c…9b08 | 946ba49c…9b08 | MATCH |
| Premise ARVIN_WRITTEN_NL_VARS | c4d92ca9…d20c | c4d92ca9…d20c | MATCH |

SUMS: cd inventory_check && sha256sum -c SHA256SUMS → **23/23 OK**, 0 FAILED (35 lines = 23 hash lines + 12 comment lines). Includes lines 33–35 for t665u FINDINGS/PREREG/result.log.
PREREG.sha256: OK from NONLOCAL_QM_EH11D/ root (fails from its own dir — root-relative path).

## Claim-by-claim
1. PREREG before RESULTS — CONFIRMED. mtimes PREREG.md 00:24:19.711 < PREREG.sha256 .715 < result.log .719 CDT; result.log cites PREREG sha 599712c3…. (SF-T665NL-1)
2. DEDUCED F_total = Ω₁₁D·ΣF̂_i (uniform) — CONFIRMED. Codex docx (Cat A e24c4904) line "each scaled by the single geometric factor Ω₁₁D" re-read directly; Ω11D on each term; distributivity is a forced step. No per-term sub-factor assignment claimed.
3. f_b ↔ B'=539 — CONFIRMED as written tie, but source is Cat B pin 946ba49c (table row "Residual scale factor tied to packaging B'=539"), not Cat A; no functional form. (SF-T665NL-2)
4. Φ_flux ↔ 539.9 s — CONFIRMED as phase tie: 539.9 s appears in Cat A (Explicit_Derivations, Codex sin(2πt/539.9) inside F_torsion/F_flux). Link of that period to the Ω-factor Φ_flux is via Cat B (t614u tables), not Cat A. No amplitude form. (SF-T665NL-3)
5. ABSENT Ω₀, f_warp(k), f_curv(K), per-term sub-factors — CONFIRMED. Auditor re-grep of both Cat A docx XML: no f_warp/f_curv/Ω₀ hits; Cat B pin marks them "Symbol-only; explicit form requires compactification". No hidden FOUND. (SF-T665NL-4)
6. W-PO-2 OPEN — CONFIRMED. Factorization Ω₀·f_warp·f_curv·f_b·Φ_flux still ABSENT as Cat A originals; only partial DEDUCED aliases (f_b↔539, Φ_flux↔539.9 s) exist and are Cat B-sourced ties. W-PO-2 must NOT close.
7. W-PO-3 PARTIAL (t660u + factorization DEDUCED) — CONFIRMED; not finished.
8. Free invent — none found. No numerics introduced; CHAT premise (ARVIN_WRITTEN_NL_VARS) explicitly marked non-forcing.
9. No Local mutation / no order78 — CONFIRMED for NL track: NL t665u writes confined to NONLOCAL_QM_EH11D/. Files under BRIDGE_C_35/ (deduce_t665u/, STREAM_IDLE_LOCAL.md, inventory_check/SHA256SUMS) are newer than PREREG — sibling Local track, not audited here. No order78 file anywhere.
10. STREAM IDLE_AFTER_LOCK — CONFIRMED (00:24 CDT line: "IDLE_AFTER_LOCK, awaiting Auditor"; mirror identical).

Prior pins stand: t660u f27c750e… (AUDIT_STATUS:358), t658u d17f83cf… (Local, untouched), Ω11D Cat B ecd670f2… / 0e5e4528… (not rewritten).

## Soft SF (no PASS/FAIL change)
- SF-T665NL-1: PREREG/sha/result written within 8 ms in one session; ordering valid but weak (no external timestamp).
- SF-T665NL-2: "DEDUCED" label on f_b↔B'=539 overstates — it is a restatement of a Cat B pin, not a deduction from Cat A.
- SF-T665NL-3: Φ_flux↔539.9 s mixes Cat A period with Cat B factor mapping; label should read Cat B tie.
- SF-T665NL-4: D2 regex ran on unhashed /tmp text extracts; Auditor re-ran on hashed docx and agrees (0 hits).
- SF-T665NL-5: PREREG.sha256 uses root-relative path; sha256sum -c only works from NONLOCAL_QM_EH11D/.

## Open set
W-PO-2 OPEN (Cat A Ω₀/f_warp/f_curv/f_b/Φ_flux forms ABSENT). W-PO-3 PARTIAL. Z_eff ABSENT. No NL2. Residual-C (Local) untouched. order78 not started.

## Blockers
Closing W-PO-2 needs a written Cat A compactification ansatz → factor map (Ω₀ normalization, f_warp(k), f_curv(K)). Deduction cannot supply it.
