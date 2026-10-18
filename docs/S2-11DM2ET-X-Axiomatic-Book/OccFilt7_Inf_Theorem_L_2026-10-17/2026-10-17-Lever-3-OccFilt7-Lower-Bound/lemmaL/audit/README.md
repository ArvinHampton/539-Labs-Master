# Independent audit of Theorem L (2026-10-17, ~19:00–19:55 CDT)

Nothing outside this `audit/` folder was modified. The audit is summarised in the section
"Independent audit of Theorem L" at the end of ../../../2026-10-17-Lever-3-OccFilt7-Lower-Bound.md.

Files:
- `rerun/`: verbatim copies of route3/*.py, rerun here so the original JSON files were not overwritten.
  out_tails.txt, out_blocks.txt, blocks_N900_0.3_1.6.json, out_exponent.txt: identical to the originals.
- `delta_split.txt`: D1/D2/D3 split of the CLT error for three cells (n >= 893).
- `den_check.py/.txt`: the odd-side lower factors 1-gfac-delta in blocks.py are all >= 0.78. block_ratio has no assert for this.
- `clt_spot.py/.json/.log` (Cat B): empirical local-CLT error and moments at n = 893, 900, 1306, compared with the rigorous enclosures.
- `fullEO.py`, `validate_1e6.txt`, `val1e5.json`, `val1e6.json` (Cat B): long-double a_n(m), validated against exact g_7 at d near 10^6 (relative error 6e-14).
- `fullEO_1e7.json/.log`, `block_spot.py/.txt` (Cat B): E_d/O_d and empirical block ratios at d = 8890004..8890009 and 9999994..9999999, n in [850, 1900].
- `closedforms.py/.txt`: closed forms for c and lim E/O (derivation in the md section).
- `ladder.py`, `validate.py`: a first attempt using the signed ladder in long double. It is numerically unstable (E-O error of order 1e14 at d ~ 10^6) and was not used. It is kept as a warning: signed recurrences in floating point are not usable here.
