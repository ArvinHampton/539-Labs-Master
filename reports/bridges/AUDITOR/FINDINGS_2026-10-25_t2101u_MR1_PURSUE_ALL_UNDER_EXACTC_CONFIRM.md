# FINDINGS t2101u — MR1 Author PURSUE-ALL under exact-c — CONFIRM (2026-10-25 ~21:10 CDT, America/Chicago)
**Verdict: MATCH-with-SF**

## Hashes
| Object | Expected | Observed | |
|---|---|---|---|
| Package grok-batches/MR1-AUTHOR-PURSUE-ALL_UNDER_EXACTC_2026-10-25.md | 499f9262…d5c9 | 499f9262c03756f3622bb104991c839b7e7f3661787eea9b45fe4fb6a3d7d5c9 | OK (+ sidecar OK) |
| Live tip residual-c-field-WRITTEN_PREMISES_DRAFT.md (LOCK) | 23644d6a…4bf8 | 23644d6a1baa568b81078cf91957ab0deb5e412035cbd52c8d81dc76f75e4bf8 | OK |
| Backup .pre-hygiene-fold-3d47ce49.md (pkg BEFORE pin) | 3d47ce49…bf79 | 3d47ce497f812792a900cb103baff6ddfe838058d7883399239cd7763ba7bf79 | OK |
| OWNER_WRITE_MR1_EXACT_C_t1218u | 7a86075e… | 7a86075e96ae6647f51dfcdf21296310da6380a620f40b0ec2559fcf4edb020f | OK |
| MR1_EXACT_C_FOLD_CLOSED_t1218u | c21eb995… | c21eb9950e3007540e7447cc48c7558d7bfd7e8ad48f8c5a2a0fe96e73fd1c69 | OK |
| OWNER_WRITE_MR1_EXACT_C_FOLD_t1218u | 071fef56… | 071fef56f835c15e9c6896aaa37263e6b95323417d699167b4bce49ce013a6c9 | OK (l.16 "Not folded: Fricke W₇…Z₇↔W₇" verified) |
| BRIDGE_C_35/AUTHOR_WRITE_APPLY_EXACT_C_LOCAL | 1f6e3d2e… | 1f6e3d2e9415612930c7f388551a6802eaadacc67304d02b9b936d20ce6549f8 | OK (l.20 verified) |
| U1_LEDGER_P_SLASH_Remark85… (3 copies) | dfd2b4b0… | dfd2b4b04816a409760c266aa7384100662c8e34514b69138ab5c4d987ff1785 | OK (l.36 quote verbatim) |
| OWNER_WRITE_OUTER_STAR_t1052u | e52446ff… | e52446ff1be74cd22c62fec84e6bc398d0602e124f47c907e7631f9b8b99bc26 | OK |
| MR1-AUTHOR-PURSUE-rho-Xi-LEVERS | 7f0d2965… | 7f0d296553dd3706ee38e60b6e50ad647d63e5d74775e26f7d92109a3e47f6a7 | OK |
| Prior pkg MR1-AUTHOR-PURSUE-W7-GENS-K | 5abf1da6… | 5abf1da6777424374075ee12dc35ae0cce11581c860cea186359d00df7e4950b | OK |
| Prior FINDINGS MR1 ABSENT pursue | ada4f9d6… | ada4f9d62f23e467cc052c5e2e9ad90e34ef82eeae90e1a22d4061690a7f7887 | OK |
| FINDINGS exact-c Cat B | c52cb8d7… | c52cb8d73ab7bbecff40eeb226c6833824d14350dcf8de3d42a6c911bd1281b3 | OK |
| FINDINGS exact-c fold re-CONFIRM | 9667f44e… | 9667f44eaeebc69fdb680720bbbe42d7af51764ccd0174d9587b0ffb34e51399 | OK |
| FINDINGS MR2 hygiene fold re-CONFIRM | f93f0744… | f93f0744b6a0d16951c068146bf0883673cdb6c9df7ecd142833f1c7fff22108 | OK |

## Checks
- Rows 1–5, 8, 9 (ρ(W₇), Γ₀(49) gens, ρ(γᵢ), k=−2↔wt 0, Ξ/χ/ϑ, μ₁₀↔W₇, d±) ABSENT; every exact-c Write excludes them. ✔ Row 10 Z₇↔W₇ not made. ✔
- Row 6 outer_* PRESENT already in tip (4 hits in live tip), not new; outer_*≡HD ABSENT. ✔
- Row 7 Author non-uniqueness of residual_slash cited verbatim (U1_LEDGER l.36) — PRESENT as obstruction, not invented; not folded. ✔
- W₄₉²=−1 vs tip ρ(W₇)²=Id logged, unreconciled (Auditor does not reconcile). ✔
- Proposed Write: NO. No matrix/gens/k invented. Nothing invented. ✔
- Tip untouched by MR1: Y. Drift 3d47ce49→23644d6a is the MR2 hygiene fold (backup = 3d47ce49…; diff §1k only), already Auditor-CONFIRMED f93f0744….

## Soft SF
- SF-1 Package tip pin BEFORE 3d47ce49… vs live 23644d6a… — tip-drift via concurrent MR2 Soft-SF hygiene fold (not MR1).
- SF-2 Package says "Owner should confirm whether the hygiene fold is authorized" — already resolved by Auditor re-CONFIRM f93f0744… (stamp f6d18dcc…).
- SF-3 Row 7 status label "ABSENT (Author text is negative)" ≡ PRESENT-as-obstruction; wording only.
- SF-4 Some support paths elided ("…"); resolved here, all match.

## Standing
Bridge PARTIAL. READY NO. Not Cat A. No tip edits. No physics invented. No outbound messages.
