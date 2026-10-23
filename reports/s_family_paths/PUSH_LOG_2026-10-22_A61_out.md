# PUSH LOG — 2026-10-22 — A61 out/ (regenerated), new files only

Authorised by Arvin (2026-10-22 10:40 PM CDT request). Same method as earlier logs (GitHub connector push_files, max 4 file arguments, base64 for binaries, sequential commits). Base tip: aa1c352. Secret/e-mail/credential/home-path scan over every file: 0 hits.

## Commit
```
0aa50ce Add A61 out/ regenerated bundle + out_regen_note (new files only)
```

## Paths (reports/s_family_paths/A61_clt_proofs/)
- A61_out_regenerated.tgz.b64: gzip tar (base64) with CONTENTS.txt and the 12 regenerated `out/` files plus `out_regen_note.md`.
- out_regen_note.md: box restart (22:21:44 CDT, track restored 22:24:49 CDT without out/), regeneration with code/run_all.sh (22:41:10-22:41:36 CDT), comparison with SHA256SUMS, and the substantive numbers.

## Result of the comparison
All 11 out/ entries listed in SHA256SUMS match byte-for-byte (out_tail61.json is a byte copy of the regenerated out_tail61_partial.json, which has the SHA256SUMS hash; run_all.sh writes the 9-k result only as the partial file). run_all.log is unhashed; the regenerated one cannot be compared with the lost original. 28/28 symbolic identities, 2079 / 1512 / 3200 arb checks with 0 violations, and D0 and T(D0) for k = 17..33 are unchanged. SHA256SUMS and all existing files were not edited.
