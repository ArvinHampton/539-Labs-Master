# FINDINGS (Local, Soft SF): beta_s, A_s, alpha for g_s=f(q^s), s in {7,8,11}. 2026-10-28 (CDT)
Status: PARTIAL invent-pending Soft SF LAND. NOT Written, NOT Cat A, no tip fold.
tip Soft SF LOCK 7cddb188... tip_touched NO. Kerr BLOCKED. No agent messaged. Prior FINDINGS were not rewritten.

## Inputs (sha256 verified on disk)
- Prior ABSENT-with-rigor: FINDINGS_LOCAL_BETA_AS_ALPHA_LAND_OR_ABSENT_S7811_2026-10-28.md 1db3d05321863c7c991ad223fce23aa0a8cd98c629dbc6bf58d24a434c8fc295
- Gap2 CLOSED-numerical: FINDINGS_LOCAL_GS_GAP2_ZETA_MULTIPLIERS_S7811_2026-10-28.md db77a8e05c82573a60bb564d8816e599d151d8b74b65deee32d7eb0eb338e4fc
- Gap2 Dedekind PARTIAL: FINDINGS_LOCAL_GS_GAP2_ZETA_CLOSEDFORM_DEDEKIND_S7811_2026-10-28.md e8f54ca304f1a690b51836d00ae3d74c37050f68db59e711983929bc89c944ef
- Gap2 phase/sigma CLOSED: FINDINGS_LOCAL_GS_GAP2_ZETA_PHASE_SIGMA_CHARACTER_PROOF_S7811_2026-10-28.md 76a92e8b7150274de0c8114daf5a05f1dd4e39ca62f8cf8d8e20f44aec890118
- Asymptotics APPROVED: OW 6081e5ac... / b19e12e6...; a87ec206 ack is on disk.
- g_s := f(q^s) Owner-ACCEPTED (OW 3f67afd5...). Canon invent 480f6d... is SUPERSEDED, and its table (beta about 0.0916 etc.) is not used.

## Derivation
1. f(q) = sum_n q^(n^2)/(-q;q)_n^2 = sum alpha_f(n) q^n. By the circle method (Rademacher-type, Ramanujan-Dragonette-Andrews), Bringmann-Ono, Invent. Math. 165 (2006), Thm 1.1 / Thm 2.1, proves the Andrews-Dragonette exact formula. Its k=1 main term is
   alpha_f(n) ~ (-1)^(n-1) exp(pi sqrt(n/6 - 1/144)) / (2 sqrt(n - 1/24))   [cite-grounded].
   The dominant singularity is q -> -1 (the Ramanujan/Watson cusp). It is consistent with the Gap2 C(a/c) dominant exponent and with the D=1 cusps sharing exponent -s; the subdominant cusps give only exponentially smaller terms (k>=2 Kloosterman-type terms in B-O).
2. g_s(q) = f(q^s) has coefficient c_s(N) = alpha_f(N/s) when s | N, and 0 otherwise. Substituting n = N/s gives
   |c_s(N)| ~ A_s N^alpha exp(beta_s sqrt(N)) along N = s m,
   with beta_s = pi/sqrt(6s), A_s = sqrt(s)/2, alpha = -1/2, and sign (-1)^(N/s - 1).
3. The conjugate-pair framing N_s=4s, Delta=1/24 used in 1db3d053 is not needed. The level change is Gamma_0(144s) (Zwegers arXiv:0807.4834 completion). The q -> q^s rescaling is elementary.

## Numeric check (Python, Local)
alpha_f(m) / [(-1)^(m-1) e^(pi sqrt(m/6)) / (2 sqrt m)]: m=500 0.99885, m=1000 0.99918, m=2000 0.99941, which tends to 1. The exact k=1 term matches alpha_f(2000) to about 1e-12 relative.

## Landed values (invent-pending Soft SF; NOT Written)
| s | beta_s | A_s | alpha |
|---|---|---|---|
| 7 | pi/sqrt(42) = 0.484758 | sqrt(7)/2 = 1.322876 | -1/2 |
| 8 | pi/sqrt(48) = 0.453450 | sqrt(8)/2 = 1.414214 | -1/2 |
| 11 | pi/sqrt(66) = 0.386703 | sqrt(11)/2 = 1.658312 | -1/2 |

## Label and honesty
- Step 1 is cite-grounded (B-O 2006). Steps 2 and 3 are elementary.
- These remain invent-pending: (i) packaging the result as Written beta/A in the project's convention, which needs PP/Owner Soft SF review; (ii) the role of the Dedekind closed form, still PARTIAL (e8f54ca3). That role is not needed for the main term but is open for the full multiplier write-up.
- No promotion to Written, Cat A, or tip fold.
