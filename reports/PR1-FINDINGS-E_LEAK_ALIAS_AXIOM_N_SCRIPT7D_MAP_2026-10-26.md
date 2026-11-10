# PR1 FINDINGS — E_leak alias inventory + Axiom N status + script↔7D term map (COOK / FREE PURSUE, proof standard) — 2026-10-26
Status: Soft SF, write-only, cite-only. Every claim is PROVED here or "UNPROVEN — gap" with the Owner Write that would settle it. No coefficient value, χ², dof or observational number invented. Rule-4 decisive recompute NOT run. Eight-only. Kerr BLOCKED (not loaded). tip_touched NO.
Continues: dependency table 9363abad0c859b1e843fc054e586545a3f5cd0f889a1af0af0f61357fabe514b (hereafter DT).

## 1. Authority (live sha256 verified 2026-10-26 ~17:50 CDT)
| Doc | sha256 |
|---|---|
| OW LET THEM COOK | 08c8cdb9f851f85add943c18705a77c4de899464e29c9389e1663a42dcc05411 |
| OW FREE PURSUE | 687b27f5ba8fab6a847563069f66bbb4b9511cf36d14df3e7143a83db335eecd |
| OW invent-ban lift | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 |
| DT (E_leak dependency table) | 9363abad0c859b1e843fc054e586545a3f5cd0f889a1af0af0f61357fabe514b |
| FREE PURSUE first (F1) | cb43f7d136b6cd9f22983d85b660f48e5a3af06e114e396595ce2dc9104fcd69 |
| Unlock | ae0bf4df80c1192a1b23a5fa56fcfc65325ca843e97587d734397a21af791eaa |
| Corrected 7D A27 txt (E_leak/F_friction) | 4758d180f467a35d139833711029ac4121fa98d79bb3129be1b579d8254250b1 (as cited in DT) |
| corrected_E_leak.py | a786538854a27c7b0409c24c8a7d1bfa595db780f05214796fcec9822c9b945a (as cited in DT) |
| tip Soft SF LOCK (NOT touched) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (verified before and after) |

## 2. Axiom N — explicit statement and status
**N (intra-expression):** Two symbols with distinct names/sub-/superscripts occurring inside the same Written expression denote distinct quantities unless a Written identity says otherwise.
**N′ (document-wide extension, newly separated here):** The same holds across distinct Written expressions of one document (E_leak vs F_friction); and identical names across expressions denote the same quantity.
**Owner-Written? N: NO. N′: NO.**
**Correction to DT.** DT Theorem 2 ("none matches an E_leak name", and β_z↔β_PBH "NO under axiom N") uses distinctness *across* E_leak and F_friction, which N as stated does not cover. Theorem 2 therefore rests on **N′** (distinct-name half only), not N. Theorem 1 rests on N alone (all symbols lie in the single E_leak expression). This is a precision fix; the numbers are unchanged.

**Consequence for k_min (cite DT §4):**
| Case | k_min(E_leak) | k_min(E_leak ∪ F_friction) |
|---|---|---|
| N accepted, N′ accepted | ≥ 35 (≥ 37 if Δ≠ΔE, Ω≠Ω_11D) | ≥ 46 (≥ 48) |
| N accepted, N′ rejected | ≥ 35 | ≥ 35 (F_friction names may all alias E_leak names) |
| N rejected | ≥ 2 (type bound: one scalar + one z-table) | ≥ 2 |
In every case: no Written upper bound (E3 "⋯", §5).

## 3. Alias inventory (all UNKNOWN pairs in DT, plus pairs DT left implicit)
Legend: PROVED same / PROVED distinct (unconditional) / DISTINCT-under-N (conditional) / UNPROVEN — gap (+ settling Owner Write).
| # | Pair | Where | Class | Reason / gap |
|---|---|---|---|---|
| A1 | τ (E1) ↔ τ (E3 integrand, dτ) | E1 vs E3 | **PROVED distinct** (unconditional) | In E3, τ is the bound integration variable of ∫…dτ; a bound variable is not a free parameter, so it cannot be identified with the free decay constant τ of E1. Same for δ(τ): δ evaluated at the dummy. Count effect: none (DT already counted τ once, from E1). |
| A2 | τ (E1) ↔ τ^- (E4) | both in E_leak | DISTINCT-under-N | Unconditional: UNPROVEN — gap. Settled by OW of N, or by explicit identity. |
| A3 | Ω_11D (E1) ↔ Ω (E6) | both in E_leak | DISTINCT-under-N | DT merged it adversarially. Gap: OW "Ω ≡ Ω_11D?" |
| A4 | Δ (E5) ↔ ΔE (E6) | both in E_leak | DISTINCT-under-N | DT merged adversarially. Gap: OW "Δ ≡ ΔE?" |
| A5 | δ(t) (E2) ↔ δ (E5) | both in E_leak | UNPROVEN — gap | Not a distinct-name case under N: same base letter, one written as a function and one bare. N does not decide whether "δ" abbreviates δ(t). DT counted them as one (adversarial). Gap: OW "δ in E5 ≡ δ(t)?" |
| A6 | **T** (E2, \mathbf{T}) ↔ T_rad (E7) | both in E_leak | DISTINCT-under-N | Supporting evidence: the LaTeX writes **T** bold next to bold **A**, and T_rad as plain with a subscript. A typographic type difference is still convention, not proof. Gap: OW of N. |
| A7 | S (E6) ↔ ρ_DM (=0.31) | both in E_leak | DISTINCT-under-N | Equal script literals (S=0.31, ρ-literal 0.31) are a numeric coincidence, not a Written identity. Under N they are distinct. Unconditional: UNPROVEN. Gap: OW of N, or OW of S's value/source. |
| A8 | E_b(z), E_z^-, Z_z^- mutual | E4 | DISTINCT-under-N | All co-occur in E4. |
| A9 | v_0, L, τ (E1/E2) ↔ v_0, L, τ (F1) | E_leak vs F_friction | UNPROVEN — gap | Same name across expressions; N is silent. Gap: OW of N′ (same-name half), or explicit identity. |
| A10 | Z_z^- (E4) ↔ Z_z^- (F2) | cross | UNPROVEN — gap | As A9. |
| A11 | τ^- (E4) ↔ τ^- (F2) | cross | UNPROVEN — gap | As A9. |
| A12 | {A_H-QP, δ, Δ, τ_echo, σ_inh} (E5) ↔ same (F3) | cross | UNPROVEN — gap | As A9. Note that E5 = F3 × (1 − τ_echo/t) structurally (PROVED by inspection, given same-name identity). |
| A13 | β_z (F2) ↔ β_PBH (E7) | cross | UNPROVEN — gap | DT's "NO under N" needs N′ (§2 correction). Gap: OW of N′, or explicit identity. |
| A14 | m_φ (E2, E3), g_11, Φ (E2, E3) | intra-E_leak, same name | Same under the same-name reading | This is the same-name half of N′ applied within a single expression. It is not Owner-Written, but no reading treats them as distinct; DT counted each once. UNPROVEN formally. |
No pair is **PROVED same**: no Written identity exists in any cited doc. Exactly one pair is **PROVED distinct** unconditionally: A1.

## 4. Script↔7D term map (structure only; corrected_E_leak.py L40–54 vs Corrected 7D E1–E8)
| Script term | Form | 7D candidate | Status |
|---|---|---|---|
| term1 | 1e-7·e^{−t/3.17e-6}·655 | E1 E_0 e^{−t/τ} L Ω_11D | **UNPROVEN — gap.** The shape c₁e^{−t/c₂}c₃ is compatible. But one literal (655) would stand for the product LΩ_11D, so the individual symbols are not recoverable even if the identification were Written. Gap: OW "term1 ≙ E1, with E_0=?, τ=?, LΩ_11D=?". |
| term2·term3 (product) | κ_dark·√(1e-20)·3e8·(1+0.31/10) × 0.31·sin(9.55e-3 t + …) | E2 + E3 (sum) | **PROVED syntactic mismatch:** the script combines by ×, the 7D combines by +. Sub-correspondences: κ_dark↔KAPPA_DARK (by name; PROVED same constant); (1+0.31/10)↔(1+ρ_DM/10) (literal 10 and value 0.31 match; PROVED structural); √1e-20↔√δ(t) and 3e8↔v_0 are UNPROVEN. The script has no f_energy factor and no (1+m_φΦ+…+g_sX^M) bracket, i.e. the bracket is implicitly 1 (UNPROVEN — gap). term3 has no integral, while E3 is ρ_DM∫sin(...)dτ; semantic equivalence is UNPROVEN because E3's "⋯" is open. Gap: OW of E3 "⋯" and of the composition rule. |
| term4 | 0.31·sin(2πt/539.9)·0.04 | E4 (Δt_11D=0) **or** E8 | **UNPROVEN — gap: two candidates.** E4 has sin(2πt/(539.9+Δt_11D)) with a z-sum; E8 has κ_dark·sin(2πt/539.9). The script prefactor 0.31 matches neither κ_dark (0.45) nor any E4 table. Gap: OW naming the target term. |
| term5 | S·100·e^{−S}(1+η_phonon) | E6 S ℏΩ e^{−S}(1 − E_em/ΔE) | **UNPROVEN — candidate (corrects DT §3C "no 7D counterpart").** The pattern S·X·e^{−S}·(1±Y) matches E6 with ℏΩ↔100 and −E_em/ΔE↔+η_phonon. That needs E_em/ΔE = −0.99, a sign condition that is not Written. η_phonon appears in no 7D term. Gap: OW "term5 ≙ E6?" |
| 0.18·e^{−1e6} | β_PBH e^{−…} | E7 β_PBH ρ_DM e^{−M_PBH/(k_B T_rad)} | **UNPROVEN — partial.** 0.18↔β_PBH is PROVED (sheet value, script name BETA_PBH is the literal). The ρ_DM factor is missing from the script (PROVED syntactic omission). 1e6↔M_PBH/(k_B T_rad) is UNPROVEN. |
| exciton_coherence | 0.031·e^{−t/70e-15}·cos(2πt/5) | none | **PROVED: no counterpart among E1, E2, E4–E8.** None of them has an e^{−t/c}·cos(·) factor (E1 has no oscillation; E4 and E8 use sin with period 539.9(+Δt); E5 is Gaussian). E3 is excluded only modulo "⋯": UNPROVEN for E3. |
| (none) | — | E5 Gaussian echo δΔA_H-QP(1−τ_echo/t)e^{−(t−τ_echo)²/2σ²} | **PROVED: no script term** has a Gaussian in t. E5 is unrepresented in the script. |
**Map result.** No script term is PROVED to instantiate a 7D term. Two structural non-correspondences are PROVED: the product-vs-sum composition, and exciton/E5 unmatched in both directions. The script is therefore PROVED not to be a term-wise literal instantiation of Corrected 7D E_leak. Its literals cannot serve as Written values for E1–E8 without an Owner-Written map.

## 5. Transcription gaps found in the Corrected 7D text (structure, no values)
- F_friction LaTeX: "…L \sum_{z=1}^{118}…" has no "+", while the Unicode line has "+". E_leak LaTeX: "…d\tau \sum…" likewise. **UNPROVEN — gap:** sum vs product. **PROVED:** k_min is invariant to this ambiguity, because under either reading the expression is evaluable only if every symbol is Written. The union U is unchanged.
- E5 LaTeX "e^{-(t \tau_{echo})^2…}" drops the "−" that the Unicode line has. Same invariance holds.
- E8 LaTeX line is truncated (κ_dark sin(2πt/539.9) appears only in the Unicode). DT used the Unicode form; U is unchanged.

## 6. Exact-k status (updated)
**PROVED (this doc + DT):**
- 0/12 terms are Written-evaluable.
- Unconditionally, k_min ≥ 2.
- Under N, k_min(E_leak) ≥ 35. Under N + N′, k_min(E_leak ∪ F_friction) ≥ 46.
- A1: the E3 τ is a dummy variable.
- k_min is invariant to the §5 transcription ambiguities.
- The script is not a term-wise instance of 7D.

**OPEN (named gaps):**
- G1 OW of N and/or N′.
- G2 OW alias table for A2–A14. If all were "distinct", the E_leak bound rises from 35 to 37 (A3, A4) or 38 (A5 too). Across E_leak ∪ F_friction it rises by up to 10 more for A9–A12 (v_0, L, τ, Z_z^-, τ^-, A_H-QP, δ, Δ, τ_echo, σ_inh), still a lower bound.
- G3 OW expansion of E3 "⋯". Without it there is no finite upper bound, so exact k is undefined.
- G4 OW script↔7D map (rows in §4).
Exact k_min remains **UNPROVEN**. The tightest conditional lower bounds are unchanged (35 / 46). The conditioning is now precise: N for E_leak, and N′ for the union.

## 7. Owner-Write ask list (no values proposed)
Owner, to settle exact k, please Write:
- (a) whether Axiom N and N′ (§2) are adopted;
- (b) the alias table A2–A14 (§3), each as same or distinct;
- (c) the full finite expansion of the "⋯" in E3, or a statement that it is empty;
- (d) the sum-vs-product reading at the §5 junctions;
- (e) optionally, whether corrected_E_leak.py is meant to instantiate E_leak and with which term map (§4).
Item (c) is decisive for the upper bound. Items (a)+(b) fix the lower bound exactly modulo (c). No coefficient values are requested here; those stay ABSENT pending separate OW.

## 8. Non-claims
- No ABSENT value was assigned.
- No χ², dof or observational data was invented.
- The Rule-4 decisive recompute was not run; prior INCONCLUSIVE stands.
- Kerr BLOCKED.
- Eight-only.
- **tip_touched NO.**
