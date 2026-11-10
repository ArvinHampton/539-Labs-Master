# OWNER WRITE CANDIDATE — T-E coefficient list advance
2026-10-26 ~11:58 CDT (America/Chicago). Authority: Owner voice call-018c4fcf "pursue-all write-all". **CANDIDATE only. NO tip fold. tip_touched NO.** Tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`. Soft SF invent HOLD tip fill else. Soft SF F3 CLOSED. Bridge PARTIAL; READY NO.

## Cites
- T-E Owner Write `OWNER_WRITE_TE_COEFF_CYCLE_592_2026-10-26.md` sha256 `5048e04490f0a4b7d32f1ce2ae57227205679864a633d8f8fb603327fe1048dc` — list `[[ coefficient list — open ]]`.
- Eigen `/workspace/grok-batches/EIGEN-PURSUE-ALL-VANISHING_2026-10-26.md` sha256 `0cc29a390b638d31b9b30181f9fbc369d7f3bd297bc3a6eba40030cb591dc34d` — T-E: HOLD; ambient dim 592 numerically PASS.
- `.out` sha256 `e2b260385fe0b4ce55e04ba364b74163cb3c66d1c4e42fa97696c774e59473e9`.

## Known (numeric, proposed; from `.out`)
- l.24: `rhobar k 4 … G0(49) M,S,Eis 603 592 11 | S new= 581` → **ambient dim 592 numeric PASS** (Eigen re-run bit-identical).
- l.32: piece dim 36, T-ord exps [0,1,4,9,14,16,21,25], k4 S=503.
- l.33: piece dim 6, T-ord exps [1,9,29,81,109,121], k4 S=89. 503+89=592.
- **No individual Fourier / special-cycle coefficient is computed on box.** Known coeffs: NONE.

## Coefficient list [[open]] — status
| slot | content | status |
|---|---|---|
| index set (n, cusp, isotypic piece) | — | [[open]] |
| N₃₆ piece (503-dim) coeffs | — | [[open]] |
| N₆ piece (89-dim) coeffs | — | [[open]] |
| KM special-cycle coeffs | — | [[open]] (template only) |

## Gaps
- No q-expansion basis of S₄(Γ₀(49),ρ̄) on box.
- No Kudla–Millson lattice / special cycles defined for ρ̄.
- No selection rule for which coefficients.

## Next fill steps (CANDIDATE)
1. Extend dimcalc script to emit a q-expansion basis per piece (T-ord exps above fix the q^{1/49}-grading).
2. Sturm bound for weight 4 on Γ₀(49) to cap index range (computed, not invented).
3. Owner chooses selection rule (e.g. exps per piece, or KM cycles) → Owner Write fills list.
4. Compute; Auditor Soft SF CONFIRM; then MR1 cite-only fold. No tip invent before step 3.
