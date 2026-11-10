# PP-FINDINGS — AUDIT of Local PARTIAL invent ĝ_s transform/order/level (s∈{7,8,11})
Soft SF · Write-only · Author Professor Proof · REPORTS · No RECS · tip_touched NO · Kerr BLOCKED · OW 3e2b924a… Local Path work only · AUDIT-only (not first-prove) · 2026-10-28 (CDT)

## §0 Live sha table
| Item | sha256 | Result |
|---|---|---|
| tip lock | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | untouched |
| FINDINGS_LOCAL_INVENT_GS_TRANSFORM_ORDER_LEVEL_S7811_2026-10-28.md | 05f6bf59ccf317416bfdaff789c3bfcdf29885c7741b6e4a690b7844d666a963 | MATCH |
| PRESS-to-PP SOFTSF_PRESS_PP_THEN_KEEPER_…INVENT_GS… | 92d21ad94051da83af74e3fac08ca392ed666bc4f06c40e23662cc75e44f8570 | MATCH (92d21ad9) |
| Auditor PRESS SOFTSF_PRESS_WRITE_…INVENT_GS… | 950fe9abbecf19dc9f1abcde89068cc231b1d14585c0a95ca875bfbac2f0a79d | MATCH (950fe9ab) |
| cites 480f6d72 / b19e12e6 / 40b5fd67 / 1db3d053 / 6081e5ac | MATCH all | |
| d1d2 6fba7717 / rank27 55b3cf0b | not re-hashed this audit | — |

## §1 Verdicts
| Claim | PP audit | Why |
|---|---|---|
| g_s := f(q^s) labeled invent-pending | CONFIRM | Explicitly a project-defined choice, not Written; Owner identity ABSENT. |
| Level Γ₀(144s), Nebentypus χ₁₂ | CONFIRM as invent-pending, character NARROW | Level raising z→sz from Bringmann–Ono Γ₀(144) is standard; half-integral-weight dilation generally twists the character (e.g. by a Kronecker symbol in s) — Local correctly flags twist ABSENT; "χ₁₂" alone must not be read as final. |
| Polar q^(−s) at ∞, Δ_s=s/24 | CONFIRM (invent-pending) | Follows from q^{−1}f(q^{24}) under q→q^s. |
| Other cusps ABSENT | CONFIRM | Not transported; hence PARTIAL is honest. |
| β_s=π/√(6s), A_s=√s/2, α=−1/2 | CONFIRM arithmetic, with caveat | Re-derived: α_f(n/s) gives (√s/2)n^{−1/2}e^{π√(n/(6s))}; values 0.484758/0.453450/0.386703 and 1.322876/1.414214/1.658312 correct. Caveat: holds only on n≡0 (mod s), up to sign (−1)^{m−1}; and table mixes q^{24}-normalized principal part with q-variable n — reader must keep variable explicit. Correctly marked not Written. |
| Conflict vs canon 480f6d (N_s=4s, Δ=1/24) | CONFIRM flag | Genuine: under g_s=f(q^s), c_min=2s, level 144s, Δ=s/24 ≠ canon. Correctly left for Owner/Auditor selection; not decided here either. |

## §2 Overall
PARTIAL label honest; invent clearly fenced; literature anchors (Bringmann–Ono 2006; Zwegers 2002; Dragonette/Andrews) appropriate. Narrowings: character twist and subsequence/sign caveat. β_s/A_s remain not Written. No FAIL.

## §3 Disposition
Soft SF → Keeper. Canon-vs-invent selection is Owner/Auditor. Local may retry where-feasible (twist, other cusps) under OW.
