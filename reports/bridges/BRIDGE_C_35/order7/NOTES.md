# order7 notes (disclosures; verdicts stand)
1. **Parity-lemma check.** PREREG §0 promised an exact check in Z[e(1/9800)]. What was done is an mpmath check at dps 30 (residual 8.9e−30) plus a float check. The lemma's Category A status rests on Weil-representation theory (S² = Z), not on an exact certificate.
2. **c3.py, first run: void.** The positive control failed because companion columns that vanish identically (for example Ĥ_j = 0 by symmetry) were normalised by norms of about 1e−17. c3b.py (a new file, hashed before it ran) drops columns with norm below 1e−10·max. The void verdict of the first run stands.
3. **c3b: also non-discriminating.** The rerun's positive control reaches only 9.9e−9, against a pass line of 1e−10, and the singular values decay smoothly with no gap. The candidate-3 design is therefore inconclusive by construction. The candidate-2 coupling test shares the same flaw.
4. **Reading (descriptive).**
   - The even piece cannot be completed at weight 1 under the fixed law (lemma).
   - Weight-0 P-even modular objects of Hecke–Maass type, built from Siegel thetas over the arc of the unit 6+√35, do exist and obey the fixed weight-0 law with ε = +1.
   - The open question is how a weight-1 even holomorphic series couples to them. Candidates are a weight-raising or lowering operator, a non-modular "mixed" object, or a T-orbit or level change that alters P.
5. **Process.** nice, OMP_NUM_THREADS=1, ulimit -v 3000000; peak memory per process well under 1 GB. No push, no external sends. New files only.
