# FINDINGS — Eigen Soft SF O5 (N36 char-0 named gap) + O6 (§2.1 target hygiene) — 2026-11-05 ~13:30 CST America/Chicago
Authority: OWNER_WRITE call-53991ebf OPEN LANE RESOLUTION a0c2ed5ab2ee7da8af4942eaf7ea86a1d91b3de6645ae4bfe898cddc538e8068 (re-hashed MATCH).
tip BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched **NO**. **No CERT.** Reports only. Nothing sent or published. No invented Kr QQ coefficients, roots, ν, or tip Cat A coefficients.

## Sources (on disk)
- S3 EIGEN-TE-RHOBAR-N36-CRT36Z-NAMED-GAP-DIAG_2026-10-27.md (eca39084…): 12-prime QQ CRT ok 0; per-prime least-root Φ₄₉ observation untested.
- S4 EIGEN-TE-RHOBAR-N36-E1-P7952701-MATCH_2026-10-27.md (9cac9a39…): 13th e1 land, rank 503/503.
- Cat B O5 wording (FINDINGS_EIGEN_SOFTSF_LOOSEN_CAT_B_11D_TERNARY + AMEND + ERRATUM_AMEND2): "N36 Kr QQ / zero-polar / G1-mem: the named gap stands. No loosening may imply existence, coefficients, or ν."
- Data: eigen-n36-503/n36wz_modp_m7_p*_e1.sobj (13 primes) and n36wz_modp_m7_p7840981_e2.sobj.

## Compute (eigen-o5-n36-2026-11-05/, SHA256SUMS)
1. galois_e1e2.sage: at p=7840981, Kr_rref with z49=r_p (e1) vs z49=r_p² (e2): pivots equal, RREF **identical** (0 differing of 5091735 nnz), stacked rank 503. So mod p the Kr row space is invariant under σ₂ (order 21 in (ℤ/49)ˣ). This tests the S3 observation at one prime: changing the root by σ₂ does not change Kr there.
2. qsqrtm7_crt.sage: hypothesis that the entries lie in Q(√−7), the fixed field of ⟨σ₂⟩. Coherent √−7 image per prime was the Gauss sum from the actually-used root (ε_p vs least √−7 is mixed: 6 of 13 are −1). 12-prime CRT + LLL reconstruction of (d,a,b), checked on a 13th-prime holdout, n=3000 sampled positions: **ok 0 / fail 3000**. Q-only control: ok 0/3000 (reproduces S3).
   Reading: with 13 primes (~10^89 modulus), entries are not small-height elements of Q or Q(√−7). The test can't tell whether the heights are too large or the field/embedding is wrong. Galois invariance was checked only for σ₂ and only at one prime.

## Sub-item status
| sub-item | status | reason / precise missing input |
|---|---|---|
| Kr over QQ | **REMAINING** (with a PARTIAL diagnostic) | Holdout reconstruction fails over both Q and Q(√−7) with 13 primes. Missing: (a) a σ₃ (full-Galois) e-test (needs an e3 sobj, e.g. `sage solve36w_z.sage 7 7840981 3`, ~5 min), and (b) either many more e1 primes (height bound) or a coherent Φ₄₉ embedding rule (e.g. roots fixed as images of one prime ideal of ℤ[ζ₄₉]). Neither is on disk. |
| zero-polar | **REMAINING** (HOLD) | Depends on exact Kr QQ. Exact zero-polar conditions can't be evaluated without char-0 Kr. Nothing new computed. |
| G1-mem | **REMAINING** | Per S3/S4 the GAP stands "until usable Kr QQ + exact zero-polar". Both inputs are absent. |

## O6 (hygiene)
Source: /workspace/quantum-comp/reports/539labs/539_Labs_Technical_Corpus.md (sha 5a8f8630…), §2.1 at lines 19–28. The target state is **ABSENT** from the source. The only "[1]" strings are group-ring terms: line 25 "$$h_1 = [0] + [1]$$" and line 26 "$$h_2 = -[0] + [1] + 3[2]$$". Line 27 states "a total cancellation occurs yielding $W = 0$ while $N = 2$" and names no target. Exact recompute (o6_target_check.py): target [0] W=2 N=4; [1] W=0 N=2; [2] W=4 N=4. So [1] is the unique target that reproduces the stated values. It is **inferred, not stated**, and "with stated reading" remains required.

## Not claimed
No Kr QQ entries, roots, ν, CERT, or proof. The σ₂-invariance is a mod-p observation at one prime only.
