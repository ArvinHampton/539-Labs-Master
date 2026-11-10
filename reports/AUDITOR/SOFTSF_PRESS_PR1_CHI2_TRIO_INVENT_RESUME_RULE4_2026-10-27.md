# Soft SF PRESS — PR1 χ² trio INVENT RESUME (Rule-4) → Auditor + NL Rule-5 (2026-10-27, ~12:12 CDT America/Chicago)
FINDINGS: `/workspace/quantum-comp/reports/PR1-FINDINGS-CHI2_TRIO_INVENT_RESUME_RULE4_2026-10-27.md` sha256 `ebc05e25f1cb902623dc602d9164ba6dd429bf80b3744e96fdc2f7a6135836ed`
Authority: OWNER LOCK call-a0858383 FINAL; ACK+BEGIN 75c7160f…. Tip 7cddb188… tip_touched NO; catalog 6c680789… untouched. Kerr BLOCKED. No RECS.

## Plain-language brief
- The three missing χ² pieces now have **invented** structures. Each one is marked INVENTED. None of them is Owner-Written or tip-Written.
- **(a) Data:** we define a schema for a DESI block and an ATLAS block, using a block-diagonal covariance (an invented assumption). The values stay symbolic, because the catalog has no DESI rows and no fake measurements were made up.
- **(b) Counting:** N = 12 (7 DESI + 5 ATLAS), with fitted parameters (A_leak, β_z, Ω_11D). That gives dof = 9, all INVENTED. χ² = rᵀC⁻¹r. If we take the script's hard-coded 0.79 as the target, χ² = 7.11 and p = 0.63. That makes 0.79 statistically unremarkable: it neither supports nor refutes the model.
- **(c) Model terms:** E_leak / F_friction bindings are invented placeholders. A proven arithmetic fact: the script's E_leak(0) is 45.28, dominated by term5, so it conflicts with the claimed 6.07e-12.
- **Proofs (math only):** whitening, dof via Cochran, moments, block additivity, a correlation-match null (ρ² ~ Beta(1/2,(N−p−1)/2)), a Bonferroni look-elsewhere bound, and invent-sensitivity. Invented dof cannot validate the model.
- **Still OPEN:** Written data and errors, Written N/θ/dof, a Written tie for 0.79, Written model forms and coefficients, the term5 resolution, and validation of hypotheses H1–H3. The decisive recompute was NOT RUN.

## Asks of reviewers (review only; no RECS)
Auditor: check that the INVENTED markers are complete and that nothing is presented as Written. NL Rule-5: check the lemma hypotheses and proofs in §5.
