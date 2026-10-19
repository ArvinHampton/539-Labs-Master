# NOTE — flags on earlier pushed files (Bridge C rev7 push, 2026-10-19)

This note records errors and superseded statements in files already on Master. Per the copy-and-create rule, none of those files is edited; this note is the correction. Categories: A = proved or exact; B = floating-point only. No TPC/RH claims; distinct from HQCC termination claims. CORE_FREEZE holds.

## Errors (label numbers)
1. `Bridge_C_Consolidated_rev6_2026-10-18/CHANGELOG_rev6.md` and `U1_LEDGER_Analytic_CatB_Push_2026-10-18.md` cite the CRT factorisation as "Prop 14.7(ii)" and the q-adic reduction lemma as "Lemma 14.8". In the rev6 PDF (and unchanged in rev7) they are **Proposition 14.8(ii)** and **Lemma 14.9**. CHANGELOG_rev6.md also cites "Thm 14.5, period 72"; the PDF number is **Theorem 14.6** (14.5 is the h-relations proposition). The rev6 PDF itself is consistent (it uses \ref).
2. `Bridge_C_Consolidated_rev6_2026-10-18/CHANGELOG_rev6.md` says the unchanged \input files (dims_table, rev4_*, rev5_*) are in `Bridge_C_Consolidated_rev5_2026-10-18/`. Only rev5_*.tex are there; dims_table.tex and rev4_*.tex are in **`Bridge_C_Consolidated_rev4_2026-10-18/`** (sha256 verified identical to the rev6/rev7 build inputs).
3. Label: the letter label used for the CRT factorisation in `Analytic_CatB_Push_2026-10-18/2026-10-18-Analytic-CatB-Push.md` (C.2–C.3) and in the comment of `Analytic_CatB_Push_2026-10-18/gauss_local.py` collides with the framework's label for the Parity Dominance Theorem. It means the **CRT Factorization Proposition (CFP)**. See `Analytic_Round3_4_2026-10-19/NOTE_LABEL_CFP.md`.

## Superseded (not errors)
4. rev6 PDF §14.3 status box and §14.6 item 1, and `U1_LEDGER_Open_Algebraic_Update2_2026-10-18.md` (if it lists k(k−1) as Cat B): the count k(k−1) of extra h-relations is now **proved for all k ≥ 2** (Proposition K1, rev7 §15.1). The dimension bounds it yields are proved upper bounds; sharpness is open.
5. rev6 PDF Proposition 14.8(v) status ("only a partial conceptual reason" for periods 16, 96): superseded by rev7 Propositions 15.11–15.12 (N = 2, 4 conceptual; N = 8 distinctness by residue-level proof, no scan over s).
6. rev6 PDF and `U1_LEDGER_Analytic_CatB_Push_2026-10-18.md` ("t^{e/2} at x = 1/4, 1/6 not computed"): now computed at t^{11/2}, t^{13/2} (rev7 Proposition 15.13).
7. Role of Δ: any earlier statement that Δ = (s−2)(7s−32) constrains the S²-side expansions intrinsically is **refined** — only (s − 2) = −2Q(c₁) is intrinsic given c₁; 7s − 32 and the √Δ terms are tied to the locked choice c₂ = (−4,1) (rev7 Remark 15.16, Cat A). The locked object is unchanged.

## Source-level corrections carried into rev7
8. Analytic report G.2: the (s−8)-exponent bullet is garbled; correct exponent max(0, e+3−4j) (its own G.0).
9. Algebraic Round 3 §7: `c7/verify.json` is empty, so the "≤ 3·10⁻⁴⁷ engine agreement" sentence is not backed by a stored file and is not used in rev7; the closed forms are Cat A by derivation, and `c7/verify_direct.json` is Cat B support.
