# order6 notes (descriptive; disclosures)
1. **Axis companions.** 15 companions have α1 ∈ Z or α2 ∈ Z, so ν can lie on an axis, where sgn 0 = 0 gives weight ½. PREREG §1 required these to be listed (data/slaw.json, "axis_alphas"). For them, the v-to-ν correction L_O has extra half-lines on the axis. The completed functions and the S-law tests are unaffected, because they use ν-signs throughout.
2. **Dropped descriptive check.** The check in PREREG §3 that "y^{1/2}∂_τ̄Ê is not antiholomorphic" was not run: its statement was ill-posed, since Zwegers shadows also carry a holomorphic θ factor. No verdict depended on it.
3. **slaw.py edit.** A garbled multiplier line in shadow_O was cleaned up before hashing and before any run. The value is unchanged: the factor is 1.
4. **Reading (Category B).**
   - Ê fails with r ≈ 0.90, and the completed orthant and full series fail with exactly half of that (F2). So the entire remaining S-law defect of the full series sits in the even double-orthant piece.
   - A modular completion of the even piece would need a different object: for example a non-Vignéras weight-1 completion, a weight-0 Maass/Hecke-type form attached to Q(√35), or an enlargement of the 35-component law vector space. This is open.
5. **Process.** nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no external sends. New files only.
