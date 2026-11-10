# WRITE — NL g_s index: choice slot or independence (T1.2) — Soft SF write-only, non-tip — 2026-10-26
Lane: Non Local Path · Project Quantum Comp NONLOCAL_QM_EH11D · Written ~17:55 CDT (America/Chicago)
Proof standard (`ef6da7e7…`): each claim is a **PROOF** or a **named UNPROVEN-GAP**. COOK OW `08c8cdb9…` authorizes pursuing NL RECS without waiting for the Owner. **Result: PARTIAL + GAP.**

## 1. Authority table (live sha256sum, 2026-10-26)
| Item | Path | sha256 |
|---|---|---|
| COOK OW | reports/OWNER_WRITE_LET_THEM_COOK_EIGHT_PURSUE_OWN_RECS_2026-10-26.md | 08c8cdb9f851f85add943c18705a77c4de899464e29c9389e1663a42dcc05411 |
| Invent-ban lift | reports/OWNER_WRITE_INVENT_BAN_LIFTED_PROOF_STANDARD_NO_CATA_GATE_2026-10-26.md | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 |
| Free-pursue FINDINGS (T1.2 source) | bridges/NONLOCAL_QM_EH11D/FINDINGS_NL_FREE_PURSUE_MISSED_VARS_EH11D_RPPT_2026-10-26.md | f82989d74faaf2c59eb9b52c95d3ae7fb516fa0893c67171c022c906b1b0816d |
| PROOF NL-JOIN-1 | bridges/NONLOCAL_QM_EH11D/PROOF_NL_JOIN_1_RIGOROUS_2026-10-26.md | 946a5910ead0631eca28c5971a74d28d61b66e853f8cb8d88c1cd7b42c88d2fe |
| δ_W₇ invent-scope | bridges/NONLOCAL_QM_EH11D/WRITE_NL_DELTA_W7_PACKAGING_INVENT_SCOPE_2026-10-26.md | 45bc050a5c003b4858c1f4e39adf720379dd419ad64830de84384a82e1f3d561 |
| Sheet params | bridges/NONLOCAL_QM_EH11D/WRITE_NL_RR_NL_SHEET_01_PARAMS_2026-10-26.md | da91ad83ac35a2f3a897dbd1794b90d102b409284012b889d6b74849e3af5998 |
| Hybrid runnable-spec | bridges/NONLOCAL_QM_EH11D/WRITE_NL_HYBRID_MC_RUNNABLE_SPEC_POST_JOIN_PASS_2026-10-26.md | 27058bad386fc64dff071324e4f4d248a60113c68349917b42656c93025fe980 |
| Deepen LIFT8 | bridges/NONLOCAL_QM_EH11D/WRITE_NL_INVENT_SCOPED_DEEPEN_LIFT8_2026-10-26.md | dcc48a554f322d3b424a921201e342bcfeed0b90ebdd220db51d34aa6c670af4 |
| Residual Packaging FINAL (defines g_s, s∈{7,8,11}) | reports/heavy-daily/Residual_Packaging_and_Series_Manuscript_FINAL_2026-08-20.txt | 7ab9a254ab7e2bd82497bc50fb9cf7d245136a02ec90efb74f4bcb7f37750aa7 |
| PR1 E_leak dependency (FYI cite only, slot (c)-adjacent; no coefficients taken) | reports/PR1-FINDINGS-E_LEAK_TERM_DEPENDENCY_TABLE_2026-10-26.md | 9363abad0c859b1e843fc054e586545a3f5cd0f889a1af0af0f61357fabe514b |
| tip Soft SF LOCK (read-only) | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |

## 2. The gap (T1.2)
Residual Packaging FINAL `7ab9a254…` §3 defines g_s(q) = Σ_{n≥0} q^{n²}/(−q^s;q^s)_n and names the residual values s∈{7,8,11}. The NL-JOIN-1 proof (P1/P2/P4, `946a5910…`) and the sheet `da91ad83…` say the g_s scale enters through the bracket term g_s X^M. **Neither one fixes which s enters, or whether the term is a combination over s.**

## 3. Attempt: (A) proof of independence fails at the series level; (B) the Owner-choice slot is opened

### Lemma G1 (PROOF): g_7, g_8 and g_11 are pairwise distinct formal power series.
*Proof.* Write g_s = Σ_n T_n with T_n = q^{n²}/∏_{k=1}^n(1+q^{sk}). Every T_n has lowest degree n², and T_n ∈ ℤ[[q]].
- Coefficient [q^8]: T_0 = 1 contributes nothing. T_1 = Σ_j (−1)^j q^{1+sj} contributes −1 only when 1+sj = 8, that is s=7, j=1. T_2 = q^4·∏(1+q^{s})^{-1}(1+q^{2s})^{-1} needs s·j₁ + 2s·j₂ = 4, which has no solution for s≥7. T_{n≥3} starts at degree 9 or higher. So [q^8]g_7 = −1 and [q^8]g_8 = [q^8]g_11 = 0.
- Coefficient [q^9]: T_1 needs 1+sj = 9, which gives s=8 with value −1. T_2 needs sj₁+2sj₂ = 5, which has no solution. T_3 contributes +1. So [q^9]g_8 = 0 and [q^9]g_11 = 1.
Therefore g_7 ≠ g_8, g_7 ≠ g_11 and g_8 ≠ g_11. ∎
(Machine cross-check to degree 39, done on box, is a SAMPLE confirmation only: the first differences are at degrees 8, 8 and 9. The script also found that [q^i]g_7 = 0 for every i ≡ 3, 5, 6 (mod 7) with i < 40. This agrees with FINAL §3 and is a sample, not a proof.)

### Corollary G2 (PROOF, conditional form): there is no s-independence for any load that is injective in g_s.
Let L be any load functional on RR-NL-SHEET-01 that factors as L = Φ(g_s·X^M), where X^M does not depend on s and Φ is injective on the span {g_7 X^M, g_8 X^M, g_11 X^M}. Assume also that X^M is a non-zero-divisor in the coefficient ring. Then L depends on s. *Proof:* if X^M is a non-zero-divisor, then g_s X^M = g_{s'} X^M forces g_s = g_{s'}, which contradicts G1. Injectivity of Φ then carries the difference through to L. ∎
So **option (A), unconditional independence, is FALSE at the series level.** Independence is still possible only if Φ, X^M or w actively kills the differences g_s − g_{s'}. One example would be an M that depends on s, compensating so that the products agree.

### Lemma G3 (PROOF): the join's P1–P4 do not constrain s.
In P1–P4 of `946a5910…` the only objects named are g_s, X^M, E_leak and the LOCK/DRAFT/sheet shas (FINDINGS T1.1). No step uses a property that tells s=7, 8 or 11 apart. The level, the residue vanishing and the transformation law are all absent from P1–P4. So every s∈{7,8,11} satisfies P1–P4 equally well, and the join is **compatible with each choice but selects none.** ∎

### UNPROVEN-GAP G4: whether the load is independent of s, or which s applies.
The missing Written objects are:
1. the definition of X^M, M and the domain of q on the sheet (T1.3);
2. the load functional Φ and the weight map w = w(g_s, X^M) (T1.4);
3. an Owner statement of which s applies.
Without (1) and (2), the non-injectivity escape left open by G2 cannot be decided.

### OWNER-CHOICE SLOT (named; NOT decided here)
> **SLOT NL-GS-INDEX-01.** Owner must Write exactly one of:
> (i) "g_s X^M on RR-NL-SHEET-01 uses **s = 7**"; XOR
> (ii) "... uses **s = 8**"; XOR
> (iii) "... uses **s = 11**"; XOR
> (iv) a Written proof (or Written definition of X^M, Φ, w) showing the load is **independent of s∈{7,8,11}**, which by G2 must exhibit why Φ(g_s X^M) annihilates g_s − g_{s'}.
> Any combination over s (sum or vector over s) counts as option (iv) and needs its own Written definition.
Status: **UNPROVEN-GAP / OPEN**. This Write does **not** pick s. A Doc remark that g_7 has residue vanishing mod 7, together with δ_W₇ (`45bc050a…`), might *suggest* s=7. That is SAMPLE-level suggestion only, not a choice.

## 4. Summary of partial lemmas
- G1 PROOF: the three series are pairwise distinct (first differences at q^8 and q^9).
- G2 PROOF (conditional): any injective load depends on s, so unconditional independence is refuted.
- G3 PROOF: join P1–P4 do not constrain s.
- G4 UNPROVEN-GAP and slot NL-GS-INDEX-01: the Owner must choose.

## 5. Explicit non-claims
tip_touched **NO**. Kerr / Path4 C2–C3 **NO**, and there are no Kerr numerics. No χ² data, dof or coefficients were invented. The PR1 table `9363abad…` is cited as FYI only. No MC was run. No tip fold. Eight-only. Soft SF → **Auditor**. sha256 is in the `.sha256` sidecar.
