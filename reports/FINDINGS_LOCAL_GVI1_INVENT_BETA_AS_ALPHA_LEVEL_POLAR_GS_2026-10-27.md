# FINDINGS (Local) — G-vi-1 invent: β_s, A_s, α, level N_s, polar order m_s for g_s, s∈{7,8,11} — 2026-10-27

Status: Soft SF Write-only FINDINGS. REPORTS ONLY, no RECS.

## Authority (live sha256)
| file | role | live sha256 |
|---|---|---|
| `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | tip LOCK | `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` |
| `OWNER_WRITE_INVENT_BAN_LIFTED_ALL_LANES_PURSUE_FREEDOM_RIGHT_AUTHORITY_2026-10-27.md` | OW invent ban lifted | `1c7163deec3cd5ee7ec6c8ee6db6b02c8bf7738e52a052218157c3b9239e0dec` |
| `SOFTSF_PRESS_OWNER_WRITE_INVENT_BAN_LIFTED_ALL_LANES_PURSUE_FREEDOM_RIGHT_AUTHORITY_2026-10-27.md` | PRESS of OW | `7a242ab5dd7445702e0b5dd6ee12ce55b449311e770c1fa282e623451119b94d` |
| `FINDINGS_LOCAL_CATA_NONTIP_A4VI_CARD4_HOLD_ROW_STATUS_2026-10-27.md` | A4(vi) status | `d4ed8cfd85222581d451d0a6b5c5ff8db4359bb7a8075921d0623c5e0c752bde` |
| `FINDINGS_LOCAL_WRITTEN_ASYMPTOTIC_GS_PATH4_CARD4_2026-10-26.md` | asymptotic class | `b19e12e6c313c98c40e28ce406ec08b3796fe8b0ad0f87a13365da1891c2d949` |
| `OWNER_WRITE_D1_D2_DEFS_LOCKED_2026-10-26.md` | D1/D2 defs | `6fba77178694a42e1556134323f1c67b1f79c83ca0b9ed4b071dedf200e5a4a2` |
| `OWNER_WRITE_ZWEGERS_BH_CONSISTENCY_CHECK_SHEET_LOCKED_2026-10-26.md` | Zwegers/BH sheet | `28bf58fb406fb2f3e3ebe8c9727f20d0eb6b5c4d4f046c891de44cfba366c9b3` |

Tip BEFORE `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` (expected `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`).

## 1. Corpus re-scan (forced invent)
Re-scanned `/workspace/quantum-comp/reports` (incl. bridges/clone docs) for an Owner/Author cite of Γ₀-level N_s or principal-part polar order m_s for g_s(q)=Σ q^(n²)/(-q^s;q^s)_n. Result: **ABSENT**. Only find: Master contact 8 "Levels for series g_s | {7, 8, 11}" (via `g_s_Closed_Forms_2026-10-18`), which uses "level" for the index s itself; it does not fix a modular level N_s nor a polar order. Hence invent under OW 1c7163de….

## 2. Invent rules (single rule for all s)
- Level: **N_s = 4s (INVENTED)**. Justification: g_s is the holomorphic part of a weight-½ harmonic Maass form (D2, Zwegers ĝ_s); weight-½ forms live on metaplectic covers of Γ₀(4N) (Shimura convention), and s plays the role of the q-scaling index (q→q^s in the denominator), so the natural rule among {s, 4s, s²} is 4s.
- Polar order: **m_s = 1 (INVENTED)** for all s — simplest principal part q^(-1/N_s) at the dominant cusp, i.e. polar exponent Δ_s = m_s/N_s = 1/(4s).

## 3. Derivation (formula cites)
Rademacher / Bringmann–Ono exact formula for coefficients of a weight-k harmonic Maass form's holomorphic part with principal part q^(-Δ) (Bringmann–Ono, Invent. Math. 2006; Bringmann–Manschot; Zagier Bourbaki 986): a(n) = Σ_c K_c(n)/c · (Δ/n)^((1-k)/2) · I_(1-k)(4π√(Δn)/c) + …; the c=1 term dominates. With I_ν(x) ~ e^x/√(2πx):
- β_s = 4π√(Δ_s) = 4π√(m_s/N_s) = 2π/√s.
- α = (k-1)/2 − 1/4 = −1/2 for k=½ (matches Andrews–Dragonette/Bringmann–Ono third-order f(q): a(n) ~ e^(π√(n/6))/(2√n)).
- A_s = Kloosterman-type leading constant K_1(n)·Δ^(1/4)·(2π)^(-1/2)·(…); not determined by (N_s,m_s) alone → concrete **A_s = 1/2 INVENTED** placeholder, FLAG: per b19e12e6… C1 map uses only L=β_s√n vs A/4 (tolerance 0.10), so A_s is secondary to G-vi-1 closure.

## 4. INVENTED table
| s | level | polar order | β_s | α | A_s |
|---|---|---|---|---|---|
| 7 | N_s=28 **INVENTED** | m_s=1 **INVENTED** | β_s=4π/√28=2π/√7=2.374821 **INVENTED** | α=-1/2 **INVENTED** | A_s=1/2 **INVENTED** (placeholder; true A_s = Kloosterman-weighted leading constant, symbolic) |
| 8 | N_s=32 **INVENTED** | m_s=1 **INVENTED** | β_s=4π/√32=2π/√8=2.221441 **INVENTED** | α=-1/2 **INVENTED** | A_s=1/2 **INVENTED** (placeholder; true A_s = Kloosterman-weighted leading constant, symbolic) |
| 11 | N_s=44 **INVENTED** | m_s=1 **INVENTED** | β_s=4π/√44=2π/√11=1.894452 **INVENTED** | α=-1/2 **INVENTED** | A_s=1/2 **INVENTED** (placeholder; true A_s = Kloosterman-weighted leading constant, symbolic) |

All β_s > 0. Class: a_s(n) ~ A_s n^α exp(β_s √n) (b19e12e6…).

## 5. Status
- G-vi-1 (numerical β_s, A_s, α ABSENT) is **CLOSED by invent** under OW 1c7163de…; C1 becomes evaluable in principle (NL Path4). Local does NOT run package numerics (B'=539, N_flux=4880, f_max=21) nor C1 pass/fail here.
- **G-vi-2 (landing acceptance) still OPEN** — named for Owner/Auditor, not invented.

## 6. Non-claims
No tip fold; Kerr BLOCKED (no Kerr path); Channel A gated unless separately lifted; Bridge PARTIAL READY NO; no READY YES / Cat A claim from invent alone. Invented values are not proofs; rigor goal (72b3c992…) requires later verification of N_s, m_s against the actual transformation law of ĝ_s.

## 7. Tip hygiene
BEFORE = AFTER = `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`; tip_touched NO.

## 8. Soft SF PRESS this FINDINGS → Auditor.
