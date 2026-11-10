# FINDINGS: Auditor Soft SF CONFIRM, Lane ACK resume presses (Local, MR1, PR1, Eigen, NL) (Write-only)
Date: 2026-10-26 ~19:27 CDT America/Chicago
Scope: packaging only. No physics assessed. No Owner verdict altered. Tip not edited.

## Tip Soft SF LOCK
Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` start sha `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`. tip_touched NO.

## Hash check
| File | Claimed | Actual | Result |
|---|---|---|---|
| /workspace/quantum-comp/reports/LOCAL_ACK_ACCIDENTAL_STOP_RESUME_NINE_CONTINUE_2026-10-26.md | f3779bf4… | f3779bf4830cb39bcb24d230eaa2c79a3088a46352020cc9f6884ae79cf6c32c | MATCH |
| /workspace/quantum-comp/reports/SOFTSF_PRESS_LOCAL_ACK_ACCIDENTAL_STOP_RESUME_NINE_CONTINUE_2026-10-26.md | 640fde7d… | 640fde7d710de290e26a78676f58e7fdd3bae12aefad1ed715deae676362fb66 | MATCH |
| /workspace/quantum-comp/reports/MR1_ACK_ACCIDENTAL_STOP_RESUME_NINE_CONTINUE_2026-10-26.md | f71ab7e7… | f71ab7e7ec69e6d7d8dc9969e4a0ff1b132d9c1e166212acbdb38fd66cde1594 | MATCH |
| /workspace/quantum-comp/reports/SOFTSF_PRESS_MR1_ACK_ACCIDENTAL_STOP_RESUME_NINE_CONTINUE_2026-10-26.md | 9b15286f… | 9b15286f269b9068fc4fa47d3701c2d5a1de5b3f2fd08bfa5ccb6431a1304ef1 | MATCH |
| /workspace/quantum-comp/reports/PR1_ACK_RESUME_NINE_AFTER_NL_STOP_2026-10-26.md | 405f156e… | 405f156e13cbc0da724a1c5ec070e5f9efd461ecea96064de306431308a244d8 | MATCH |
| /workspace/quantum-comp/reports/SOFTSF_PRESS_PR1_ACK_RESUME_NINE_AFTER_NL_STOP_2026-10-26.md | 3dbce0ba… | 3dbce0bae94422efd5f9331a579aa97a3e50d36985ac367446017171a042b4a9 | MATCH |
| /workspace/quantum-comp/reports/EIGEN_ACK_RESUME_NINE_AFTER_NL_STOP_2026-10-26.md | 4d72de07… | 4d72de070c69a66dde2a38bbafb6cf6d2e29de02f6940814feaa143ae0c8b200 | MATCH |
| /workspace/quantum-comp/reports/SOFTSF_PRESS_EIGEN_ACK_RESUME_NINE_AFTER_NL_STOP_2026-10-26.md | c0ef4d9f… | c0ef4d9fbcdc39b4e8e30371ae7e93d068ecd006c5002093e4e232331fab1142 | MATCH |
| /workspace/quantum-comp/reports/SOFTSF_CONFIRM_NL_ACK_RESUME_NINE_AFTER_ACCIDENTAL_STOP_2026-10-26.md | 9c5af8d1… | 9c5af8d151cc098b245935c1da20299074ab57e79649d216a2af4cdb0aaf7b5d | MATCH |

## Spot-checks
1. All ACKs carry tip 7cddb188 + tip_touched NO. Present.
2. NL ACK records HARD BAN on StopSubagent(all). Present.

## Soft SF flags
SF-1: MR2 resume press — no SOFTSF_PRESS for an MR2 resume ACK found on disk; MR2 resumed via FINDINGS feae6fa3… citing RESUME OW a51992d4…. Recorded as UNPAID/absent, not invented.
SF-2: NL ACK 9c5af8d1… duplicated in reports/ and bridges/NONLOCAL_QM_EH11D/ (identical sha).

## Verdict
MATCH-with-SF (packaging).

Tip end sha `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`; tip_touched NO.
