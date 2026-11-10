# FINDINGS — MR1 Soft SF invent-then-prove WHERE FEASIBLE: Exact-ν / G-PATH-A / Fricke Role A
Time: 2026-10-27 12:39 CDT (America/Chicago)
Lane: MR1 Soft SF Write-only → Auditor mirror. No SendToAgent. No RECS. No CSV edits. No new invents.
Authority: Owner Arvin YES (MR1 chat ~12:37 CDT). Source invent-close FINDINGS b024fb66e6e49c31531deb7f481c380d98672fac53a353e22e5a3726852211fa (live-verified).
Live OW hashes (sha256sum at write):
- 5130fa73b14b67fb76dcb7da5799298023b4052d6d9aab8aae5e734b3c8db90c  FINDINGS_AGENT_ACK_OWNER_LOCK_INVENT_HARD_GATE_PROOF_PURSUIT_OW_04b2c268_2026-10-27.md
- d15993ec63f8ea7fe4606e0527559763a0d452e18c8ded4ff7e5536d55fb1649  FINDINGS_AGENT_ACK_OWNER_LOCK_INVENT_THEN_PROVE_WHERE_FEASIBLE_OW_922c5230_2026-10-27.md
- 87de10d31793c197863f2bd9f33e4679649896153c4aafb509d43bf345c1851b  FINDINGS_AGENT_ACK_OWNER_LOCK_NOT_FEASIBLE_RETRY_24H_OW_649ddc2d_2026-10-27.md
- 1844993c175342f4c264f8eda7ad22790524b93b9aff6fdecf080656873c0ad7  FINDINGS_AGENT_ACK_TOKEN_HARD_STOP_90PCT_PLUS_MR1_ACK_HARD_GATE_2026-10-27.md
tip LOCK /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched NO. Kerr BLOCKED.
On-disk certificates used (/workspace/grok-batches/eigen-q89-basis/rhos/):
- certS.log 1ba492890ff13810c2823b30b1172fda03e8f8d4d8a84034838100b3ac870514
- S_seed_exact.sobj a453f5887e68bf852db2a56b3f26a3734e77d9d1e1f0a789deae72147505c2c5
- crt.log 96fe95cffbd49cc8cb5ffdd0f53cd1781ae8cd5842b56accf6cf6d0f85d9a74b
- zrecon_z.log 68e8403d444c91d221b98c57b1334ffc13cd33c71db45f55a88c934d49d45223

## Sage run this turn (Sage via /tmp/pm/bin/sage, on S_seed_exact.sobj)
Seed (6×6, CF(140)): S²==1 True; (ST)³==S² True; T diagonal True; T^140==1 True.
Image under ring hom CF(140)→CF(980), ζ140↦ζ980^7: S²==1 True; (ST)³==S² True.

## Status table
| Item | Status | Basis / WHY |
|---|---|---|
| I-EX1 | NOT-FEASIBLE | crt.log: 5-prime CRT (89×1726, pivots agree) → RECON FAILED; zrecon_z.log: only 3 held-out checks/cusp. No height bound on char-0 entries ⇒ RR uniqueness (Wang bound) cannot be invoked; more primes / height bound needed. |
| I-EX2 | NOT-FEASIBLE | Depends on I-EX1 machinery + complete mod-p data; solve42g PARTIAL (m=6 p=1027606441, running root 40 at write); no 2nd-prime solve42g. |
| I-PA1 | PARTIAL | Proved: ζ140↦ζ980^7 is a well-defined injective field embedding (ζ980^7 primitive 140th root) and preserves seed relations (Sage above). Open: 42-element V42 basis not exact on disk (only 6-dim seed); Card-1A ID NOT claimed. |
| I-PA2 | PARTIAL | Proved for 6-dim seed: T_seed exact diagonal, T^140=1 in CF(140), hence ζ980^{7k} in CF(980). Open: 42 exponents a_i in char 0 (only mod-p certificate). |
| I-PA3 | PARTIAL | Proved for 6-dim seed: exact S_seed with S²=1 (central), (ST)³=S² in CF(140) and CF(980) image (certS.log + Sage rerun; intertwiner Q certified). Open: 42×42 char-0 lift of d2ce6132… mod-p ρ̄(S) — needs exact V42 (blocked with I-EX). |
| I-FA1 | NOT-FEASIBLE | No W₄₉ matrix on V42 on disk; cited P2 PROOF only gives AL set {1,W₄₉}, not that Role A = W₄₉. Needs exact V42 + W₄₉ action. |
| I-FA2 | NOT-FEASIBLE | Sign ε requires trace/eigenvalue of W₄₉ on V42 exact (or on Role A eigenspace); not computed; may be −1. |

All NOT-FEASIBLE and PARTIAL-open portions keep label "invented pending mathematical proof". No new values invented; PARTIAL proofs cover only the 6-dim seed + the embedding, not the 42-dim claims.

## NOT-FEASIBLE RETRY 24h
Not-feasible recorded 2026-10-27 12:39 CDT. First 24h retry due ~2026-10-28 12:39 CDT; retry every 24h applies (I-EX1, I-EX2, I-FA1, I-FA2; plus open parts of I-PA1–3).
