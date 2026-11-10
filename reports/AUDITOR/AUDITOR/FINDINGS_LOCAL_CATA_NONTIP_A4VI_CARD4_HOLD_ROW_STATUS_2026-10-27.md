# FINDINGS — Local Cat A (conditional, non-tip) — A4 (vi) Card4 HOLD row status vs asymptotic landing — 2026-10-27 (CDT)
Role: Local Path. Mode: Cat A lifted for THIS ITEM ONLY under Owner Write `42bf6b7bb18995f34e92982c50ece345df82492e993f4864449e69d0d8efb6e6` (Auditor Pack HX MATCH). Proof standard: each step proved from cited text, or marked UNPROVEN with the gap named. No tip edit. No numerics. No RECS.

## 0. Why this item qualifies
- **Named:** A4 row (vi) "Card4 HOLD row status vs asymptotic landing — unresolved" (free-pursue F4 `2e45574b…`; COOK A4 cite-check `33bf86a9…` §3 verdict STILL-OPEN-UNPROVEN).
- **Proof-level:** needs a deduction from the Card4 Write's own release conditions against what has landed, not a cite lookup.
- **Non-tip:** subject is the RH map `9910ade2…` §4/§5 and Card4 OW `6298ad26…`. Neither is the tip file; tip Soft SF LOCK `7cddb188…` is not read for content and not touched.
- Not Channel A, not the five test-sheet slots, not Kerr.

## 1. Authority (sha256 live)
| Item | sha256 |
|---|---|
| tip Soft SF LOCK | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (tip_touched NO) |
| OW conditional Cat A lift | 42bf6b7bb18995f34e92982c50ece345df82492e993f4864449e69d0d8efb6e6 |
| Card4 HOLD OW | 6298ad2696f19560be92087e4bccae4770ee3dca79a337d261a00e48c75696c2 |
| C1 NAMED OW | 586dbac0d703a10f547277a7e9a61792da0da89c72dac4af1624af7ca117baff |
| Local Written asymptotic | b19e12e6c313c98c40e28ce406ec08b3796fe8b0ad0f87a13365da1891c2d949 |
| RH map | 9910ade24d1c4cdb0f010b728c7b138fc904beb79c423f689889b5b3fc4f1290 |
| A4 cite-check | 33bf86a9657c843d7b3bb827e6de8c87f7b58cb23fbab65761e6537791c81784 |
| Packaging NEXT | 3b90a14f1d87207e5e6d9aeccded40c87af9223d47820aa1f3f7c01857f770c3 |

## 2. Deduction
Card4 OW §Decision states the HOLD as two conditions, both required before package numerics:
- (H1) "a Written asymptotic lands (Owner Write)";
- (H2) "Owner names C1 tolerance".

**Step 1 — H2 is satisfied.** C1 OW `586dbac0…` writes "C1 relative tolerance = 10% (0.10) of the leading A/4 term" under Owner-delegated authority. That is an Owner-attributed naming of C1. PROVED by cite. (FLAG carried from `b19e12e6…` §STATUS: the value was chosen under delegation, not spoken as a number.)

**Step 2 — H1 is satisfied at the level of the asymptotic *class* only.** `b19e12e6…` lands the Written class \(a_s(n)\sim A_s n^{\alpha}e^{\beta_s\sqrt n}\) and the C1 map \(L_{\hat g_s}=\beta_s\sqrt n\). Its §3 table records \(\beta_s, A_s, \alpha\) for \(s\in\{7,8,11\}\) as **ABSENT**. PROVED by cite.

**Step 3 — the C1 test is not evaluable yet.** The C1 criterion \(|L_{\hat g_s}-A/4|/(A/4)\le 0.10\) needs a value of \(L_{\hat g_s}\), so it needs \(\beta_s\). With \(\beta_s\) ABSENT, the left side is undefined. So no C1 pass or fail can be computed. PROVED (direct from the criterion's form).

**Step 4 — acceptance step outstanding.** `b19e12e6…` §69 says NL may run C1–C3 "once the Owner or Auditor accepts this landing." PR2 ACCEPT-with-FLAG is on disk. The Auditor Soft SF PRESS on `b19e12e6…` sits in `SOFTSF_PRESS_DEFERRED_2026-10-26/`, and no Auditor CONFIRM file for `b19e12e6…` was found. Owner acceptance of the landing: none located. Status UNPROVEN (named gap G-vi-2).

## 3. Result — Card4 HOLD row status (A4 vi)
- **Gate conditions:** H2 MET; H1 MET (class only).
- **Numerics:** still **HELD**. Two named gaps remain:
  - **G-vi-1:** numerical \(\beta_s\) (and \(A_s,\alpha\)) for \(s\in\{7,8,11\}\) ABSENT, so C1 cannot be evaluated.
  - **G-vi-2:** Owner/Auditor acceptance of the `b19e12e6…` landing not on disk (Auditor PRESS deferred).
- **RH map §5 line** "C1 stays blank until a Written asymptotic and an Owner C1 tolerance exist" is **STALE**. Both named inputs exist (Steps 1–2). Replacement text, recorded here only (no edit to the RH map file): *"C1 NAMED = 0.10 (`586dbac0…`); Written asymptotic class LANDED (`b19e12e6…`); C1 not evaluable until β_s Written (G-vi-1) and the landing is accepted (G-vi-2)."*
- **A4 (vi) verdict:** moves from STILL-OPEN-UNPROVEN to **RESOLVED-AS-STATUS** (row status proved), with the HOLD on numerics **standing** on G-vi-1 and G-vi-2.
- A4 (iv) is not touched here (separate named gap).

## 4. Non-claims
No β_s/A_s/α values. No numerics. No C1 pass/fail. No Card4 breach. No RH map file edit (supersede text recorded here only). No tip read/edit/fold. Channel A gated. Five test-sheet slots untouched. Kerr BLOCKED. Bridge PARTIAL READY NO. NL Cat A not touched.

## 5. Tip hygiene
BEFORE = AFTER = `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`; tip_touched NO.

## Soft SF
PRESS this FINDINGS → Auditor Write-only Soft SF CONFIRM.
