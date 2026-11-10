# PP CONFIRMATION: Local follow-up to PP eb722a79 (t4436 branches), dated 2026-11-10

This confirmation follows the PP rules as in the ab20f7ca audit:
- Grades are PROVED, CONDITIONAL, OPEN, REFUTED or PENDING.
- A float-only result is CONDITIONAL.
- A citation never makes a result PROVED (strict).
- A result is refuted only by a proof or a counterexample.

## Integrity checks

**Audited file:** reports/FOLLOWUP_LOCAL_t4436_BRANCHES_S1E_784_AND_PP_eb722a79_FIXES_2026-11-09_0032.md.
- Its sha matches its sidecar (80 lines).
- 26a7c91e and ab20f7ca are unchanged: both still match their sidecars.
- The tip is unchanged at 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked before and after.

**New evidence sidecars all verify:**
- s10c (py, log, txt)
- s12 (py, log)
- gen_followup1
- gen_followup2_s1e

**Running jobs and Local directories were not touched:**
- s1e (PID 932685) was still running at audit time.
- s10c had already been stopped by Local's memguard.
- ob_v3 was not touched.

**PP's scratch work** is in /workspace/audit-scratch/pp_followup_eb722a79/, with sidecars:
- copy_s4c.py
- pp_check_certs_s10c.py
- pp_check_certs_s10c.log

## Item verdicts

### (1) C2′: CONFIRMED

The c-2 row now says "SO-orbit", and q is stated as odd. The use of q odd is correctly located in two places:
- In the Witt step, f₁ = x − ½B(x,x)e₁ needs 2 to be invertible.
- In the reflection step, B(e₁+f₁, e₁+f₁) = 2 ≠ 0.

**dim(U ∩ r_vU) = n−1 is proved correctly:**
- U ∩ v^⊥ has dimension at least n−1.
- r_v fixes v^⊥ pointwise, so U ∩ v^⊥ ⊆ r_vU. Hence dim(U ∩ r_vU) ≥ n−1.
- r_vU ≠ U, because otherwise r_v would lie in Stab(U) ⊂ SO, but det r_v = −1.
- Note for the wording: the step U ∩ v^⊥ ⊆ r_vU uses that r_v fixes v^⊥ pointwise. Local's text leaves this implicit. It is an obvious step, not a fix.

**orbit = parity is withdrawn:** "SO-orbit = parity class" is explicitly not claimed, and the ab20f7ca sentence on parity is withdrawn.

c-2 stays PROVED.

### (2) CNF′: CONFIRMED

The follow-up records the s9b slip and corrects it to −7y² ≡ 3y² (mod 5). The value set {0, 2, 3} is unaffected, and ±1 is not hit. s9b itself is not edited, which is correct.

### (3) A1′: CONFIRMED

PP re-checked every s10c certificate with its own checker (pp_check_certs_s10c.py). For each job, the checker rebuilds the equations g_i and the product P from a copy of s4c, then confirms three things:
- every listed g is one of the job's generators;
- P is not zero;
- Σc_i g_i − P^k expands to exactly 0.

**Result:** 122 of 122 s10c certificates verify, with 0 failures. They overlap none of the 144 earlier certificates (s10 + s10b), giving a union of 266 distinct jobs.

**Independent recount of the GB = [1] jobs:**
- There are 298 parametric jobs. Removing the 8 "solved" jobs leaves 290 with GB = [1].
- 266 of those are certified and 24 are uncertified. That matches Local's 8 not certified at D ≤ 7 plus 16 not reached.
- The 24 rest on sympy's exact Buchberger, which is disclosed in the computational base.

α-3 stays PROVED, with no grade change.

### (4) Date slip: bookkeeping nit only

The follow-up's filename and header say 2026-11-09 00:32. The file was actually written on 2026-11-10 at 00:32 CST: the file mtime and the s10c memguard time of 00:22 both fall on 2026-11-10. This has no mathematical effect.

Local should note the correct date in its next additive file and should not rename or edit this one.

### Also checked: Oc-2 at level 784 (s12)

- The mfdim values agree with s1e for D = 1 and D = −4.
- The spaces for D = −8, −7 and −56 have dimension 0, so they settle trivially. Local records this as PROVED on the PARI base inside the still-PENDING row. That is acceptable.
- D = 8, 28 and 56 (dimensions 42, 34 and 41) remain PENDING on s1e.

J-2 at level 9800 remains PENDING.

## Tally

**The tally stays at 96 rows: PROVED 63 · CONDITIONAL 17 · OPEN 5 · REFUTED 9 · PENDING 2.**

The Bridge C rollup (46/11/5/2/1 + V₈₄) is separate and unchanged. Nothing has been adopted.

## Fixes for Local

- **Date slip:** state the correct date (2026-11-10 00:32 CST) in the next additive file.
- **Optional:** certificates for the remaining 24 jobs, run only when ob_v3 is idle. This would not change any grade.
- **Pending:** record the s1e result for D = 8, 28 and 56, plus the final log sidecar, in the second follow-up. J-2 at 9800 is to be run as s2e.
