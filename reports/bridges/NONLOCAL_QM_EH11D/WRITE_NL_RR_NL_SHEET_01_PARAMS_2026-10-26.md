# WRITE — RR-NL-SHEET-01 parameters, residual side, pass criteria
Date: 2026-10-26 ~14:06 CDT America/Chicago
Lane: Non Local Path (NL ≠ Local Bridge C)
**NO PASS CLAIM. READY NO.**

## 1. Header / authority (live sha verified)
- General NL invent lift OW `c6e9aad7823f14b0bf134c34daaac0d4edf9cc971aa630ec7444da430555e353` (supersedes the reverse-parity-only lift `0fbd9b85…`).
- Priority amend OW `fe2ee91204797cff827acd78cf597707f763ca8a63ac51872b7602a7a7316356`.
- Card CLOSED B `3b39c35c9cfe74f47d4d933ec82c8d79aaeeac9fef603aec1fceef9382882134`.
- Hybrid MC FINDINGS `6bbc198e9a73ef8d80b8d7c1127404b3226faf66f4893272ba0fdaadd465968b`.
- tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — tip_touched NO.
- Scope used for this sheet: reverse-parity work, inside the general lift.

## 2. Sheet identity (name FROZEN)
- Sheet: **RR-NL-SHEET-01 "RPPT118 E_leak(t) load"**.
- Primary NL observable: E_leak(t). Secondary observable: F_friction.
- Cites: RPPT deepen `ce6520ce182a8c26ec1c99b783c8d31a4f0620b99b0cc4da71362dbdec82b070`; join Doc DRAFT `75fe9b93b41db12aa46cd29f78a5ab153efd39d7ef66c3ff24cff4c56fddb7a0`, items 4–5.

## 3. Parameters
Anchor: Corrected 7D §3.1 (`4758d180f467a35d139833711029ac4121fa98d79bb3129be1b579d8254250b1`), verbatim: "integrating -U beta decay rates over 118 elements … achieving χ²/dof = 0.79. Parameters: ρ_DM = 0.31 GeV/cm³, β_PBH = 0.18, κ_dark = 0.45."

| Parameter | Value | Label |
|---|---|---|
| ρ_DM | 0.31 GeV/cm³ | CITED-from-Corrected-7D |
| β_PBH | 0.18 | CITED-from-Corrected-7D |
| κ_dark | 0.45 | CITED-from-Corrected-7D |
| element sum | z = 1…118 | CITED-from-Corrected-7D |
| MC meaning | 118-element reverse-parity integration of E_leak(t); not lattice QCD | CITED (structure) + deepen ce6520ce |
| null control | residual weight w ≡ 1 | INVENT-under-lift (sheet-only) |

This parameter set is frozen for this sheet.

## 4. Residual side (DRAFT invent, NOT an Owner-Written join)
Candidate map for join item 5: **residual packaging / g_s scale (join Doc Part A) ↔ NL E_leak(t) load, through the g_s X^M term** in the E_leak bracket.
- Owner must Write the join before any test.
- The Smith dictionary is Local-only and stays Local.

## 5. Pass criteria (PRECONDITIONS only)
- Reference band: χ²/dof = 0.79, quoted from the Doc only. It is not a result of this sheet.
- Proposed criterion (inactive): a PR1 null-control run reproduces the band, then the residual-weighted run stays within it.
- **PASS assertion: BLOCKED** until an Owner-Written join exists. READY NO.

## 6. Explicit holds
No tip fold or tip Soft SF fill. Card4 HOLD. No recompute was run. Rule 4: any numerical recompute → DELEGATE to PR1.

## 7. Integrity
sha256 is in the `.sha256` sidecar.
