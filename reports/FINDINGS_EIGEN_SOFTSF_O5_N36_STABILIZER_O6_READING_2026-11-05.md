# FINDINGS — Eigen Soft SF O5 N36 stabilizer / field / recon + O6 chosen reading — 2026-11-05 ~13:55 CST America/Chicago
Authority: OWNER_WRITE ALL_AGENTS_RESOLUTION_NO_PER_ITEM_APPROVAL 06748ff29e8b5e103833c5dec0712443a255d4e26990ea53acaa8793306fe9e2 (re-hashed MATCH). Prior: FINDINGS 3af326ba….
tip BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched **NO**. **No CERT.** Nothing sent or published. No invented Kr QQ coefficients, roots, ν, or proofs.
Compute: eigen-o5-n36-stab-2026-11-05/ (SHA256SUMS; INPUT_SOBJ.sha256). New on-disk lands: n36wz_modp_m7_p7840981_e3.sobj and _e48.sobj (solve36w_z.sage unchanged, rank 503/503 each). The first e3 attempt was OOM-killed while running in parallel with e48; it was rerun alone and completed.

## O5(a) stabilizer — RESOLVED (mod p, at p=7840981)
At p=7840981, Kr_rref with z49 = r_p^k equals the k=1 RREF exactly (pivots equal, 0 differing entries, stacked rank 503) for **k = 2, 3, 48**. 3 is a generator of (ℤ/49)ˣ (order 42), so Kr mod p is invariant under every k. **Stabilizer = all of (ℤ/49)ˣ.** The field is ℚ (as a mod-p statement at one prime). I did not run all 42 k: σ₃ alone generates the group, and each run takes about 5.5 min.

## O5(b) root convention — RESOLVED
Because the stabilizer is the full group, Kr mod p doesn't depend on which Φ₄₉ root is used. So the existing least-root rule (solve36w_z.sage line 10–11) is already consistent with the field ℚ, and any deterministic rule would give the same residues. The S3 "non-coherent least-root" observation is therefore **not** the cause of the CRT failure. This rests on the one-prime invariance in (a).

## O5(c) reconstruction over ℚ — REMAINING (partial diagnostic)
- Prior per-entry ℚ recon (13 primes): 0/3000 holdout.
- New common-denominator test (rowvec_recon.sage): for 5 rows × 12 non-pivot entries, simultaneous-denominator LLL over 12 primes (log10 M ≈ 82.75), checked on the 13th prime: **holdout False on every row**. The recovered D and numerators are about 10^75–10^76, which is the generic lattice bound (≈ M^{12/13}). So the true row denominators/heights exceed about 10^76.
- Missing input: substantially more e1 primes (p≡1 mod 980). 7 candidates are already listed in n36_e1_next_primes_candidates.txt, at ~5.5 min each. The number needed is unknown because no height bound is on disk (NEEDS-DEFINITION: a height bound for the RREF of the 503×11700 system).

## O5(d) zero-polar, G1-mem — REMAINING (not attempted)
Gated on (c) passing the holdout, which it does not.

## O6 — RESOLVED (hygiene)
**Chosen reading: target state = [1].** This is a chosen reading and is **not written in the source**: 539_Labs_Technical_Corpus.md (5a8f8630…) §2.1, lines 19–28, names no target. "[1]" appears there only as a group-ring term (L25 h₁=[0]+[1], L26 h₂=−[0]+[1]+3[2]).
Under this reading, in ℤ[ℤ/3], the paths into [1] are (0,1) with weight +1 and (1,0) with weight −1, giving **W = 0, N = 2**. That matches the corpus's stated "W = 0 while N = 2". For reference, target [0] gives W=2, N=4 and target [2] gives W=4, N=4 (prior o6_target_check.py), so [1] is the unique target that reproduces the stated values. Every merged statement should carry "with chosen reading target=[1]".
