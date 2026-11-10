# EIGEN Soft SF — N36 crt36z named-gap DIAG (holdout/inconsistency) — 2026-10-27 ~15:19 CDT America/Chicago
STATUS: Soft SF FINDINGS (diagnostic). NOT CERT. Named gap STANDS. tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` tip_touched **NO**. Kerr BLOCKED. REPORTS ONLY. No RECS. No invent roots/Kr QQ/ν.

## Source / resume
Owner RESUME OW `a26b11d4…` Soft SF ACK `fe817502…`/`b800dd59…` (Pack WV MATCH). COOK: diagnose 12-prime FAIL Soft SF `4c494526…` + seek further e1 primes p≡1 mod 980. Artifacts under `/workspace/grok-batches/eigen-n36-503/`.

## Artifacts (sha256 verified this turn)
- `n36_named_gap_diag_2026-10-27.log` sha256 `1ef4e76c67db0c181513a608f6a8746b669696c20e9c9a7e4d548b804141358f`
- `diag36.sage` sha256 `7280453ce264a53331630210006f067b5b707e001a3c989316fc7fb096a11759`
- `n36_e1_next_primes_candidates.txt` sha256 `a2b702dc6665f339c2d1e3f167dcb869e43789c30cfea489189f88841f0c137e`
- Prior `crt36z_rebuild.log` sha256 `bca13f10fb2e95286860ad2b0a13de39a44b4023210f3197dbe6fe324704c45e` (unchanged)

## Diagnosis (sample n=3000 nonzero positions, seed 36; one-prime-at-a-time load)
Primes (12): [7840981, 7851761, 7860581, 7863521, 7864501, 7867441, 7872341, 7873321, 7875281, 7876261, 7885081, 7946821]. dims (503, 11700).

1. **Support / pivots identical across all 12 primes.** `Kr_piv` MATCH everywhere; nnz per prime 5091733–5091737; 0/3000 sampled positions zero at another prime → **not** a support mismatch.
2. **Moduli:** log10 M11 ≈ 75.85; log10 M12 ≈ 82.75.
3. **Sample 11+holdout:** ok **0**, no_recon 1194, holdout_fail 1806.
4. **Holdout-fail recon heights** (Sage `global_height` = **natural log**): min 82.0 / mean 86.5 / max 87.0. Bound at M11 ≈ ln(√(M11/2)) ≈ 87 → sampled reconstructions sit at the bound (random-looking), **not** small rationals.
5. **Units correction:** prior Soft SF FAIL “max height ~25.34” is also natural-log (~11 digits). Comparing log10(M12)≈82.75 against 2×25.34 mixed bases; under consistent units the 12-prime modulus is already large vs prior reported height.
6. **Subset recon (4 / 6 / 8 primes):** ~1848–1867/3000 reconstruct; each result MATCHES only the primes it was built from and MATCHES **0** of the primes left out.
7. **Leave-one-out (all 12):** ok **0** every drop; ~1130–1220 no_recon and ~1780–1870 mismatches each. **No single prime is the bad one.**

## Observation (report only; untested; no code change)
`solve36w_z.sage` lines 9–10 set `r_p` = least root of Φ₄₉ mod p per prime (EXP=1). That per-prime least-root choice is not, a priori, a coherent embedding of ℚ(ζ₄₉) across primes. Recorded only; not tested; not changed.

## Next e1 primes (verified p≡1 mod 980, unused, p>7946821)
7952701, 7957601, 7960541, 7961521, 7963481, 7969361, 7973281, 7975241.

## e1 job started (in flight at Soft SF stamp)
- `sage solve36w_z.sage 7 7952701` → log `solvez_p7952701_e1.log`; pid was 4051650 at ~15:18 CDT; weight/basis lines printing; sobj not yet written at stamp time.
- Tip hash unchanged `7cddb188…`; tip_touched **NO**.

## Named gap STANDS
- ABSENT: certified Kr over QQ from coordinated solve36w_z e1 CRT.
- Soft SF FAIL 12-prime `4c494526…` STANDS as baseline; this Soft SF adds the inconsistency / unit-corrected height diagnosis.
- G1-mem Soft SF GAP stands until usable Kr QQ + exact zero-polar. Zero-polar **HOLD**.
- No invent Kr QQ / roots / ν. No fake CERT.

## What is NOT claimed
- No invented Kr QQ entries. No coherent-embedding CERT or DISPROOF of the Φ₄₉ least-root observation. No exact ν invent.
- tip Soft SF LOCK tip_touched **NO**. Kerr BLOCKED. REPORTS ONLY. No RECS.
