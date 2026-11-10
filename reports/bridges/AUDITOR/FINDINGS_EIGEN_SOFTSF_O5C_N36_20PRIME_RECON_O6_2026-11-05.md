# FINDINGS — Eigen Soft SF O5(c) N36 20-prime reconstruction + PP N1/N2/N3 — 2026-11-05 ~14:50 CST America/Chicago
Authority: OWNER_WRITE ALL_AGENTS_RESOLUTION_NO_PER_ITEM_APPROVAL 06748ff29e8b5e103833c5dec0712443a255d4e26990ea53acaa8793306fe9e2 (re-hashed MATCH) + OW bcc3ced0… (standing rule). Folds in PP audit 4fb6f706… notes N1–N3. Prior: FINDINGS 24bb435c….
tip BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched **NO**. **No CERT.** Nothing sent or published. No invented Kr QQ values, roots, ν, or proofs.

## Compute paths (N3)
- Stabilizer pass: /workspace/grok-batches/eigen-o5-n36-stab-2026-11-05/ (SHA256SUMS). Mirrors: same folder name under /workspace/quantum-comp/bridges/{AUDITOR,PROFESSOR_PROOF,PHYSICIST}/, /workspace/quantum-comp/reports/bridges/{AUDITOR,PROFESSOR_PROOF,PHYSICIST}/, /workspace/quantum-comp/reports/.
- This pass: /workspace/grok-batches/eigen-o5c-n36-moreprimes-2026-11-05/ (SHA256SUMS, INPUT_SOBJ.sha256). Mirrors: same folder name under /workspace/quantum-comp/bridges/{AUDITOR,PROFESSOR_PROOF,PHYSICIST}/, /workspace/quantum-comp/reports/bridges/{AUDITOR,PROFESSOR_PROOF,PHYSICIST}/, /workspace/quantum-comp/reports/.
- New sobjs (in /workspace/grok-batches/eigen-n36-503/): n36wz_modp_m7_p{7957601,7960541,7961521,7963481,7969361,7973281,7975241}_e1.sobj and n36wz_modp_m7_p7957601_e3.sobj.

## Runs
The 7 candidate primes were run strictly one at a time (o5c_seq_runs.log, all exit 0), then the σ₃ run at 7957601. A queued waiter for that σ₃ run had matched its own command line in pgrep and never fired; it was killed and the run was done directly. All 20 e1 primes reach **rank 503/503** and have **identical Kr_piv** (asserted in recon_all.sage).

## O5(a)/(b) — RESOLVED-mod-p evidence (not a proof over ℚ) (N1)
- p=7840981: Kr_rref is invariant for k=2, 3, 48 (prior pass).
- **p=7957601 (second prime, N1): k=3 vs k=1, pivots equal, RREF equal, 0 differing entries, stacked rank 503** (stab2.log).
- Since 3 generates (ℤ/49)ˣ, Kr mod p is invariant under the full group at both tested primes. This is consistent with field ℚ and with root-choice independence (so the least-root rule is consistent). It is mod-p evidence at 2 primes, not a proof over ℚ.

## O5(c) reconstruction over ℚ — REMAINING
Shared-denominator LLL per row (5 rows × 12 non-pivot entries), trained on all primes except the last and checked on the last:
| batch | train primes | log10 M | holdout prime | rows passing |
|---|---|---|---|---|
| prior | 12 | 82.75 | 7952701 | 0/5 |
| batch 1 | 14 | 96.56 | 7960541 | 0/5 |
| final | 19 | 131.06 | 7975241 | 0/5 |
In every batch the recovered D and numerators sit at the generic lattice bound (log10 ≈ M·12/13: 76 → 89 → 121), so they look random. There was no early stop.

**Achieved height bound:** the true row height (common denominator and numerators, jointly) is **greater than about 10^121 (~400 bits)**. This is a lower bound only; no upper bound is on disk.

**Estimate (labelled ESTIMATE):** each prime adds log2(7.9×10⁶) ≈ 22.9 bits. Reconstruction with 12 entries needs about (13/12)·h bits of modulus for true height h bits, plus a holdout prime, so primes ≈ ⌈1.083·h/22.9⌉ + 1. For example, h = 500 bits needs about 25 primes (5 more), 1000 bits about 49 (29 more), and 2000 bits about 96, which is beyond the supply. Since there has been no plateau through 400 bits, a true h of ≥ 500 bits is plausible but unknown. **Supply:** 66 further primes p≡1 mod 980 lie below the script's p<2^23 limit, which allows at most ~86 total (~1970 bits), at about 5.5 min each when run sequentially. If h exceeds ~1800 bits, the supply is insufficient without lifting the 2^23 limit (NEEDS-DEFINITION: a height bound for the RREF of the 503×11700 system).

## O5(d) zero-polar, G1-mem — REMAINING
Gated: Kr QQ has not verified on a holdout, so nothing was attempted.

## O6 — RESOLVED (hygiene; N2)
Definitions: **W = signed sum of path weights** into the target state; **N = sum of |weights| over the same paths**. In ℤ[ℤ/3] a path is a pair (a,b) of support terms of h₁, h₂ with a+b ≡ target (mod 3), and its weight is h₁[a]·h₂[b].
**Chosen reading: target = [1]. This is a chosen reading and is not written in the source** (539_Labs_Technical_Corpus.md 5a8f8630… §2.1, lines 19–28, names no target; "[1]" appears there only as a term in h₁ and h₂).
Under this reading the paths are (0,1) with weight +1 and (1,0) with weight −1, giving **W = 0, N = 2**, which matches the corpus. For reference, [0] gives W=2, N=4 and [2] gives W=4, N=4.
