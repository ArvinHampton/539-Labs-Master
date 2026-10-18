# ERRATUM — genus count for s = 11 (2026-10-18)

Affected text: `s8_s11_Analogues_2026-10-18/2026-10-18-s8-s11-Analogues.md`, §0 table ("s = 11 | 396 | h⁺ = 8 | genera = 2") and the related phrase "h⁺ = 8 > 2 genera" in §6. That file is kept verbatim (new-files-only rule); this erratum supersedes those entries.

Correction: for discriminant D = 396 (s = 11) the number of genera is **4**, not 2. Gauss's count 2^{μ−1} with μ = 3 (characters at 3, 11 and the 2-adic one) gives 4, and the coset computation in `g_s_Closed_Forms_2026-10-18/cusp_onset.py` (→ `cusp_onset.txt`, cross-checked with PARI in `pari_crosscheck.txt`) agrees. Hence Cl⁺ ≅ Z/4 × Z/2 (not Z/8, and not with 2 genera).

Unchanged: h⁺ = 8 > 4 = #genera, so the cusp conclusion for s = 11 (a genuine dihedral cusp component in u_L and ψ) stands. Category A for the counts; the explanation "h⁺ ≠ #genera ⇔ cusp part" remains Category B.
No lock altered. CORE_FREEZE holds.
