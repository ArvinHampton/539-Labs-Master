# FINDINGS — MR2 P-Ω tip fold (Ω_11D ≡ 1) re-CONFIRM — 2026-10-25 ~20:50 CDT (America/Chicago)

**Verdict: MATCH-with-SF** (fold-scope PASS). Auditor did not edit the residual-C tip.

## Hashes (all verified by sha256sum)
| Artifact | sha256 | Result |
|---|---|---|
| Live tip post-fold `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | `87fcda27e6eac193e1bf6d258109b27a73ac5cdf86ecc155b7952085776393c4` | MATCH |
| Pre-fold backup `.pre-p-omega-fold-5eefa02b.md` | `5eefa02b97a974cecf6c95f7bcea4677eab0bb06198046f082a192117f510e4f` | MATCH |
| Fold stamp `MR2-FOLD-STAMP-P-OMEGA-O1_2026-10-25.md` | `12c3fd0edf68c3a1f2487d78db39f00b34d3ea323550afd6fa6c5d3af1a88bba` | MATCH |
| Prior Write-CONFIRM `..._MR2_OMEGA11D_O1_ACCEPT_CONFIRM.md` | `3e18a772570f432ebc50ded002d394a675f9cd3e7bc6cf721443a3bf5333a06f` | MATCH |
| ACCEPT Write `MR2-AUTHOR-WRITE-OMEGA11D-O1-ACCEPT.md` | `a5ac32749bb712ae37491e1a564310273e04af8314fa2de578e1f93c9e523e93` | MATCH |

## Diff summary (backup → tip)
`diff` shows a single hunk `133a134,142`: insert-only new §1h (9 lines). No deleted or changed lines anywhere else.

## Checks
- P-Ω only → §1h Ω_11D ≡ 1: **PASS**
- Retire list (0.68 / 1−3⁻⁵³⁹-as-Ω / 0.99995 / 3509): **PASS**. The only place these appear in the tip is the §1h retire sentence (line 138). None is supplied as Ω anywhere else.
- P-fgeom NOT folded: **PASS** (listed explicitly under "Not folded").
- N₂ W-N2-1 preserved: **PASS** (line 131 is unchanged; the N₂ carrier block is untouched).
- Bridge PARTIAL / READY NO / NOT Cat A: **PASS**. "Cat A" count went from 21 to 23; both new hits are negations ("not claimed" / "NOT Cat A").
- No Z₇↔W₇ introduced: **PASS** (match count 4 before and 4 after; all are pre-existing).

## Soft SF
- **SF-A:** §1h header and Status line still say "pending/await Auditor re-CONFIRM" and "tip sha post-fold out-of-band". This is a self-reference that can't be resolved in place. Cosmetic; no edit by Auditor.
- **SF-B:** Carried forward from the prior CONFIRM: tip base moved 492fb3ac→5eefa02b (MR1), and MR2 authority comes from t1118u + Owner t23s4 (it is not named in t1129u). Both are acknowledged in §1h.

## Live LOCK tip
**`87fcda27e6eac193e1bf6d258109b27a73ac5cdf86ecc155b7952085776393c4`** (supersedes 5eefa02b…).
