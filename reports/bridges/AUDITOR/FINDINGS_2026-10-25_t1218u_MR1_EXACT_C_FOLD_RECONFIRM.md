# AUDITOR FINDINGS — MR1 exact-c Cat B tip fold RE-CONFIRM (t1218u) — 2026-10-25 ~20:55 CDT

**Verdict: MATCH-with-SF**

## Hash pins (all verified)
- Live tip post-fold: `3d47ce497f812792a900cb103baff6ddfe838058d7883399239cd7763ba7bf79` (matches tip .sha256 sidecar)
- Pre-fold backup `.pre-exact-c-fold-0677d02a.md`: `0677d02a10f298d0e84f41f6da876fe6ed4b886b92000ed70e9cec3be6173ca3`
- Fold stamp OWNER_WRITE_MR1_EXACT_C_FOLD_t1218u: `071fef56f835c15e9c6896aaa37263e6b95323417d699167b4bce49ce013a6c9`
- Write OWNER_WRITE_MR1_EXACT_C_t1218u: `7a86075e96ae6647f51dfcdf21296310da6380a620f40b0ec2559fcf4edb020f`
- Prior Write-CONFIRM FINDINGS: `c52cb8d73ab7bbecff40eeb226c6833824d14350dcf8de3d42a6c911bd1281b3`

## Diff (backup → tip): 4 hunks
1. §1j l.157 "Not folded" line annotated "(at V₄₂ fold time) … exact algebraic c (later folded §1l t1218u)" — wording only.
2. New §1l ledger (Write/FINDINGS/stamp shas, Folded = W-EXACTC-1 into §2 P1 only, Not folded list, backup sha, READY NO / Bridge PARTIAL / NOT Cat A).
3. §2 P1: V₄₂ bullet Category B note upgraded to reference exact-c §1l; new exact-c bullet {1, −1, ζ₁₀, ζ₁₀², ζ₁₀⁶, ζ₁₀⁷} ⊂ μ₁₀ ⊂ ℚ(ζ₅), Cat B numerical recognition (max err 4.84e-7), not formal proof.
4. §2 slot line `[[ ρ ]]`: appends "+ exact-c μ₁₀ t1218u".

## Checks
| Expectation | Result |
|---|---|
| W-EXACTC-1 into §2 P1 + §1l only | MATCH (see SF-1) |
| Soft SF-1 base `0677d02a…` (not stale `70c47a4c…`) | MATCH — backup sha and §1l both pin 0677d02a |
| NOT folded: W₇ / Γ₀(49) gens / k / Z₇↔W₇ / ρ matrices | MATCH — ABSENT hold; listed under Not folded; k=−2 slot unchanged; ρ matrices blank; Z₇≠W₇ retained |
| N₂ / Ω_11D≡1 / 55-Step / V₄₂ / P-fgeom §1k preserved | MATCH — §1g–§1k unchanged (grep counts identical; V₄₂ +1 only from new reference) |
| Cat B; Bridge PARTIAL; READY NO; NOT Cat A | MATCH |
| Exact-c set as claimed | MATCH — identical to Write/prior FINDINGS; all six in μ₁₀ |

## Soft findings
- **SF-1 (scope, soft):** hunk 1 touches §1j l.157 (outside §2 P1 + §1l). Annotation-only historical clarifier, no content change; acceptable, noted.
- **SF-2 (cosmetic):** §1l header still says "pending Auditor re-CONFIRM"; may be updated by Owner to cite this FINDINGS. Auditor did not edit tip.

No physics invented. No tip edits. No outbound messages.
