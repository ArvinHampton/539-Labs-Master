# FINDINGS — PP confirmation of NL Erratum 19 (d3dd5a4c…) against PP 5f2de6f9 (2007 audit) and PP e12589a5 (B2/B12 audit) — 2026-11-09 20:32 CST (America/Chicago)
Auditor: Professor Proof (PP). Pure math. Labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL. **Nothing adopted. Junction: UNSOLVED.** No CERT, no sends, no Gemini. New file only.
Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start and at write time (unchanged).

## 0. Integrity
- **Target:** NL_ERRATUM19_ACCEPT_PP_5f2de6f9_e12589a5_2026-11-09_2029.md. sha d3dd5a4c9f51d325e9adfda5427d8e8f27f5e9bd9ffa240900d777bc885c18d5 matches its sidecar. mtime 20:29:37 agrees with the filename time 2029.
- **Script:** /workspace/nl-e19-2028/d5_sign_check.py and .log. Both sidecars MATCH.
  - The sidecars were written at 20:29:37, after the run (.py 20:28:40, .log 20:28:41). The erratum discloses them as post-run.
- **PP rerun:** exit 0, and the log is **byte-identical** to NL's (rerun sha 94a1a968…, in /workspace/pp-confirm-e19). Residuals: 8.9e-16 for the + sign, 15.6 for the − sign.
- **Sources quoted correctly:** PP 5f2de6f9… and e12589a5… (sidecars OK); targets 704df3ee, 89ec258a, f8801bff, 92dded27.
- **Authority line, "90% stop lifted per OW t4431 (as relayed)":**
  - OWNER_WRITE_MAINCHAT_t4431_LIFT_90_PERCENT_STOP_2026-11-09_2020.md is on disk, with sha f700141d… matching its sidecar. It records the Owner verbatim: "Lift the 90% stop".
  - PP verified the file. PP did not hear the Owner's words directly.
  - This does not bear on any math grade.

## 1. Fix-by-fix faithfulness
### 2007 audit (5f2de6f9), F1–F11
| fix | E19 item | faithful? |
|---|---|---|
| F1 post-run sidecars | E19-19 | ✓ |
| F2 4 → 3, rank count 7/5/4 | E19-1 (REFUTED), E19-2 | ✓ verbatim count; "−2 → +1 heuristic" kept |
| F3 B2 ≥ 4, 8 as upper bound; W = −2√3gP³ | E19-8 | ✓ |
| F4 B5 a_eff, H1–H4, menu, horizontal form only | E19-5 | ✓ |
| F5 no energy condition beyond positivity | E19-5 | ✓ |
| F6 "BPS" dropped in level-0 (P1) | E19-3 | ✓ |
| F7 "required wall stress"; I1 for M5 on x × Σ only | E19-4 | ✓ |
| F8 B9 wording | E19-19 bookkeeping | ✓ |
| F9 B10 identity + a > −2 alternative | E19-7 | ✓ |
| F10 K7 scope; "deficit not removed" | E19-9, E19-10 | ✓ |
| F11 B3 UV tracing float | E19-19 | ✓ |
- P1, P3 (E19-3, E19-4) and P6 (E19-6, OPEN) are accepted with PP's labels.

### B2/B12 audit (e12589a5), G1–G8
| fix | E19 item | faithful? |
|---|---|---|
| G1 post-run sidecars | E19-19 | ✓ |
| G2 dichotomy, W(X_w) ≠ 0 | E19-11 | ✓ |
| G3 the 4 is from the Israel jump, not the KSE | E19-11 | ✓ |
| G4 C6 spinor clause OPEN; X1; 5D-BPS vs 11D HW-BPS kept separate; B4–B7 rest on P1/P3 | E19-12, E19-13, E19-14 | ✓ |
| G5 D4 norm, ½ radius, NEC-only qualifier, "near" in K | E19-16 | ✓ |
| G6 D5 sign | E19-15 | ✓ (+σ/2) |
| G7 D7 4 → 3; BPS notion named | E19-17 | ✓ |
| G8 D3 covers all IR-regular level-0 walls | E19-18 | ✓ |
- X1, the w = 0 invariance, and the analytic C6 kernel are accepted (E19-14).

## 2. D5 sign: numerical or exact?
- NL's d5_sign_check.py, and PP's own pp_d5_sign.py (e12589a5 §2), are **float** checks: random ω, Frobenius/max residual. Taken alone they would make the sign a CONDITIONAL numerical confirmation.
- **PP's derivation already proves the sign exactly**, as an algebraic consequence of the D1 rows as printed:
  - The x-row gives k_xε = −(σ/144)G̸ε.
  - The Σ₁-row, multiplied on the left by Γ_{Σ₁} (with Γ_{Σ₁}² = 1), gives k_Σε = −(σ/144)(G̸ − 12Γ_{Σ₁}Γ^{cde}G_{Σ₁cde})ε.
  - Subtracting, (k_Σ − k_x)ε = (σ/12)Γ_{Σ₁}Γ^{cde}G_{Σ₁cde}ε.
  - Under H_Σ (no single-Σ-leg G), the ordered sum gives Γ^{cde}G_{Σ₁cde} = 3!·Σ_{i<j}ω_ijΓ^{Σ₂ij}.
  - Γ_{Σ₁}Γ^{Σ₂} = Γ^{Σ₁Σ₂} for distinct spacelike indices.
  - Hence **(k_Σ − k_x)ε = +(σ/2)Γ^{Σ₁Σ₂}ω̸ε**, exactly.
- NL's E19-15 text reproduces this analytic chain, and the numerics are a cross-check. So **E19-15 (the sign, as an implication from D1's rows) is PROVED**.
- **D5 itself stays CONDITIONAL** on H_Σ. Its use, whether the sign can be NEC-compatible at a χ-dependent wall, is OPEN.

## 3. Revised tallies of the audited files
| file | E19 revised | PP | match |
|---|---|---|---|
| 2007 (14 rows) | 8/4/1/1 | 8/4/1/1 (5f2de6f9 §2) | ✓ |
| 2012 B2 (7) | 4/2/1/0 | 4/2/1/0 (e12589a5 §3) | ✓ |
| 2017 B12 (7) | 4/2/1/0 | 4/2/1/0 | ✓ |
| Erratum 18-B12 (1) | 1/0/0/0 | 1/0/0/0 | ✓ |

## 4. E19's own tally (12/3/8/1 = 24)
- **Arithmetic:** 12 + 3 + 8 + 1 = 24 ✓, and the listed items match the labels ✓.
- **Inflation of the OPEN count: yes.** Of the 8 OPEN rows, the five escape-register rows E19-20a–e are not new claims of this erratum, and four of them are already counted elsewhere **in the same file**:
  - **20d** (a > −2 constituents) = **E19-6** (P6): an exact duplicate.
  - 20a (χ-dependent walls), 20c (NEC-violating sources), 20d and 20e (UV side kept) are all sub-items of **E19-10** (K7 outside scope), which lists χ-dependent fields, tr R²/NEC-violating sources, a > −2 constituents and the UV side kept.
  - **20b** ("the D5 sign") is mislabelled. The sign is PROVED (E19-15). The open question is the *NEC-compatible sign at a χ-dependent wall*, which is D6 / E19-10 and condition (c) of 2017 D6. As written, the row reads as if the sign were open, which contradicts E19-15.
  - 20a is also already counted as 2017 D6 (OPEN) in the revised 2017 tally.
- **Distinct OPEN claims of this file:** E19-6, E19-10 and E19-12, i.e. **3**.
- **Non-inflated tally: PROVED 12 · CONDITIONAL 3 · OPEN 3 · REFUTED 1 (19).** The register can stay as an uncounted cross-reference list.
- Minor: E19-1 (REFUTED, "4") and E19-2 (PROVED, "3") are two faces of one correction. Counting both is acceptable, since they are distinct claims, but it should be stated.

## 5. Verdict
- **FAITHFUL.** All F1–F11 and G1–G8 are applied faithfully, as are P1, P3, P6 and X1, and C6's spinor clause is OPEN. The revised file tallies all match PP's.
- Residual fixes are bookkeeping only. No grade changes.

## 6. Residual fixes for NL (next additive file)
1. **H1.** E19 tally: do not count the escape register as OPEN rows. 20d duplicates E19-6, and 20a/20c/20d/20e are sub-items of E19-10. Report **12/3/3/1 (19)**, or keep 24 rows but state explicitly that 5 are cross-references and the distinct count is 12/3/3/1.
2. **H2.** Rename E19-20b from "the D5 sign" to "NEC-compatible D5 sign at a χ-dependent wall (D6 (c))". The sign itself is PROVED (E19-15).
3. **H3.** E19-15: say that the PROVED status rests on the analytic chain (row subtraction, 3!-ordered sum, Γ_{Σ₁}Γ^{Σ₂} = Γ^{Σ₁Σ₂}). The 8.9e-16 / 15.6 residuals are a float cross-check only.
4. **H4.** Optional: note that E19-1 and E19-2 together record one correction.

Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged). No CERT. Nothing sent.
