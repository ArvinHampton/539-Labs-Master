# INVENTORY — residual-C LOCK close criteria (t1055u follow-up) — 2026-10-25 ~19:20 CDT (America/Chicago)

**Status: INVENTORY ONLY.** No LOCK claimed. residual-C not edited. invent-ban ON. Not Cat A.

## 0. Verified inputs (sha256, checked ~19:15 CDT)
| File | sha256 | Match |
|---|---|---|
| /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md (tip) | 507bb43bad887fb193f4ca51515ac98d381ba912b477cb85c1794633b2fb37ca | YES |
| reports/OWNER_WRITE_P5_residualB1_X4_t1055u_2026-10-25.md | 64f7d95f1907e8c05737e1bd28f5c2843c65a6bd72e3698a087c3f076a14c1cb | YES |
| reports/bridges/AUDITOR/FINDINGS_2026-10-25_t1055u_P5_residualB1_X4_CONFIRM.md | 03d3e3b39520a74e73dfbc9faec759053e39cb236051d49122bc96b399f0b026 | YES |
| reports/ADOPTED_PATH_GUIDANCE_2026-10-25.md (ledger tip) | 9a24175ace294a33b85fde29fa0299c269f4a5d56fa570b931c8de6fbcb3f86f | YES |

## 1. LOCK definition (verbatim, tip 507bb43b…)
No standalone formal LOCK definition exists in the corpus. LOCK is defined operationally by these lines:
- L14: `| LOCK | **None.** No LOCK, no Cat A promotion |`
- L49: "Residual-C remains **OPEN-conditional** until P5 `[[ to prove / accepted ]]` and residual_B1 value are settled and Owner LOCKs."
- L494 (§11): "NOT Cat A until slots filled and LOCK; residual-C stays OPEN."
- §11 ACCEPT option text: "residual-C stays OPEN until P1–P5 are filled and P5 is proved or explicitly accepted."
- L498: "Arvin/Local will compute `sha256sum residual-c-field-WRITTEN_PREMISES_DRAFT.md` on the **final, filled** file at LOCK and record the digest."
- L204 (P5 header): "Pick one form and mark it as either *to prove* or *accepted as axiom*."
- L91 (§1e): "Still OPEN: LOCK; P5a proof; C_vol value (P4 blanks); full ρ matrix; cusp in/out rules; G-A3 PAUSED. READY NO; Bridge PARTIAL."

**Synthesis (no invent):** LOCK = an Owner act, performed on a file in which (a) all P1–P5 slots are filled, (b) P5 is either proved or explicitly accepted as axiom, (c) residual_B1 value settled; then the final-file sha256 is recorded as the LOCK digest. LOCK ≠ Cat A (Cat A is a separate later promotion). READY / Bridge C status is not named as a LOCK precondition in the tip text.

## 2. Prerequisite checklist
| # | Prerequisite | Status | Source |
|---|---|---|---|
| 1 | Structure P1–P5 accepted | MET | tip L494 (~14:25 CDT) |
| 2 | P1 G = Γ₀(49)⁺ | MET | tip L12/L111 |
| 3 | P1 V, dim V = 42 | MET | §1b; Item2 49aba949… (cite drift, see §3) |
| 4 | P1 k = −2, multiplier trivial, no cover | MET | §1c W-D2; P1-R1 |
| 5 | P1 ρ on generators (Written rules / matrix) | OPEN (`[[ ρ on generators — Arvin ]]`) | tip L102/L111 |
| 6 | P2 ρ(W₇) non-scalar, ρ(W₇)²=Id, eigenspace +1 | MET | §1c W-D4; L126–129 |
| 7 | P3 cusp-set rule (Γ₀(49)⁺ orbits) | MET (structure) | L155 |
| 8 | P3 V-components of Q support | OPEN (`[[ components — Arvin ]]`) | L154 |
| 9 | P3 mod-weakly-holomorphic rule | OPEN ("Exact rule **Arvin-blank**") | L156 |
| 10 | P4 other T-invariant components of c | OPEN (`[[ vanish / listed rules — Arvin ]]`) | L193 |
| 11 | P4 modular stand-in for X | OPEN | L193 |
| 12 | P4 Ω^{p−1}/e_q-power slot | OPEN | L193 |
| 13 | P4 C_vol value (= residual_B1) | OPEN symbolic; "= 1 only if Arvin Writes it as a convention" | L193; §1e; Write 64f7d95f… |
| 14 | P4 G-side convention ρ / ρ̄ | OPEN | L194 |
| 15 | P5 form chosen (P5a) + tag | MET (tag = to prove) | §1e; L206 |
| 16 | P5a proved OR accepted as axiom | OPEN (to prove; κ=4 vanishing unproved, DEVELOP_d2 fac67a14… caveat) | §1e; L208 |
| 17 | outer_* table | MET (t1052u e52446ff…) | §1d |
| 18 | X4 | ABSENT — not gating (X4-2) | §1e |
| 19 | G-A3 | PAUSED (gating role unstated in tip) | L91 |
| 20 | Final-file sha256 recorded at LOCK | ABSENT (not yet applicable) | L498 |
| 21 | Owner LOCK act | ABSENT | L14, L49 |
| — | Bridge PARTIAL / READY NO | Not listed as LOCK precondition in tip; status flags only | L17, L91 |

## 3. Soft SF (Auditor 03d3e3b3…)
| SF | Content | Blocks LOCK? |
|---|---|---|
| SF-1 | §1b cites Item2 49aba949…; live Item2 358f4d05… | Not a hard block; recommend fixing cite before final-file hash so LOCK digest carries correct provenance |
| SF-2 | No on-box backup of residual-C 9adb84fa… | Does not block (history provenance only) |
| SF-3 | L49/L68 stale (P5 tag/residual_B1 shown as blanks) | Does not block logically; should be annotated before LOCK hash (final file must not self-contradict) |
| SF-4 | invent-ban lift scoped to t1055u package | Does not block; informational |

## 4. What Owner can Write NOW (no invent)
1. **P5 tag change** to *accepted as axiom* (explicitly permitted by L204 and §11 "proved or explicitly accepted"). This removes the proof gate; it is an Owner choice, not a math claim. Keep κ=4 caveat.
2. **C_vol convention**: Write "C_vol = 1 (convention)" — L193 explicitly allows "= 1" only if Arvin Writes it. Settles residual_B1 value symbolically-as-convention.
3. **P4 remaining slots** as convention/template: G-side ρ vs ρ̄; "marked template" for modular stand-in X; other T-invariant components "vanish" (Owner Write).
4. **P3 blanks**: mod-weakly-holomorphic rule and Q V-components as Written conventions, or explicitly mark "accepted as template / not required for LOCK".
5. **ρ on generators**: Write a decision that LOCK does not require numeric matrices (packaging note at L102 already says "no numeric matrix required at accept"); plus authorise SF-1/SF-3 housekeeping edit before final hash.

## 5. Cannot close tonight without new math/proof
- P5a vanishing proof (cusp forms for (Γ₀(49)⁺, ρ̄), κ=4, +1 eigenspace = {0}) — only if Owner insists on *to prove*.
- C_vol numeric value from an actual pairing (vs convention).
- Explicit ρ matrices on generators of Γ₀(49) and W₇ on dim-42 V.
- Bridge C beyond PARTIAL / READY YES (not LOCK preconditions per tip, but not closable from corpus: t665u campaigns ABSENT-with-gap / PASS-NO-UNIQUE in STREAM_IDLE_LOCAL).

## 6. Recommended next Owner move
Write a single package: P5a → "accepted as axiom", C_vol = 1 (convention), P3/P4 remaining slots as conventions/"not required for LOCK", and authorise SF-1/SF-3 cleanup — then Auditor, then Owner LOCK with final sha256.
