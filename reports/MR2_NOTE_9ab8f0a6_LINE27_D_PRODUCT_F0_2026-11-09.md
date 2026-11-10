# MR2 note on 9ab8f0a6, line 27: the (D) product control value (additive; 9ab8f0a6 is not edited)

Date: 2026-11-09, America/Chicago. Author: MR2. This is a text-only note. Nothing was rerun.

## What line 27 says
File: `MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09.md` (sha prefix 9ab8f0a6, re-verified 20:0x CST). Line 27:
> (D) product AdS₅×H²×S⁴ inside the candidate ansatz (X = 1, a = 0, e^{2f} = 4/9 so that L_AdS5 = 2/3, e^{2g} = 1/6)

## What the code and the log actually use (REF, read from frozen files)
- V2 .py (sha ad134752…), line 327: `# product validation inside the candidate ansatz: X=1, a=0, F0=2/3, G0=1/6 (KR (D) metric)`.
- Line 331 prints `AdS5(F0=2/3)xH2(G0=1/6)xS4(1/2)` together with the exact targets K = 40·9/4 + 4·36 + 384 = 618, Ric² = 828, R = 6, max|eig Q| = 6.
- The V2 log reproduces these: K = 618.0, RicSq = 828.0, R = 6.0, max|eig Q| = 6.000000000000.
- The string "4/9" does not appear anywhere in the V2 .py (grep).
- In `cand_metric` the AdS₅ block is D^{1/3}·F0·(…)/r². At X = 1 we have D = 1, so L²_AdS5 = F0 = 2/3. The AdS₅ term in K is 40/L⁴ = 40·9/4, which confirms L² = 2/3.

## Correction (PROVED: this is arithmetic on the frozen code)
The coded (D) control value is **e^{2f} = F0 = 2/3 = L²_AdS5**, so L_AdS5 = √(2/3), with e^{2g} = G0 = 1/6. For this metric, K = 618 and R = 6.
The md wording "e^{2f} = 4/9 so that L_AdS5 = 2/3" is a text slip. It squares L where it should not. The numbers and verdicts in 9ab8f0a6 are unaffected.
This agrees with PP 205dbc3f §2 fix 1 (e^{2f} = F0 = 2/3, L² = 2/3).

**The brief said 4/9 is the coded control value. It is not.** No 4/9 appears in the code. The coded value is 2/3, and the (D) product uses that same F = 2/3 with R = 6, so the two coincide. The only "4/9" in the record is the md slip above.

Cross-check: `MR2_CROSSCHECK_NL_BREATHING_MODE_CURVATURE_EFT_2026-11-09.log` finds NL's singlet fixed point at e^{2B}/L² = 0.25 = G0/F0 and e^{2C}/L² = 0.375 = (1/4)/(2/3). This is the same (D) geometry with L² = 2/3 in V2 units.
