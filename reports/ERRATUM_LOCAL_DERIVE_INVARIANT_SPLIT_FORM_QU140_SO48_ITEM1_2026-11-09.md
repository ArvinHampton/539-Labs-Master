# ERRATUM — Local Path — item 1 of FINDINGS_LOCAL_DERIVE_INVARIANT_SPLIT_FORM_QU140_SO48_2026-11-09.md (sha 0344dc48…) — 2026-11-09 ~13:05 CST
This is an additive erratum. The original file is preserved unchanged. No CERT. The tip 7cddb188… is untouched.

Line 13 contains a garbled clause, "z = Σ_g B(1,g)·g⁻¹... precisely: set z_g := B(1, g⁻¹)…". Line 13 should read as follows.

**PROVED (classification).** Let B be an A-invariant bilinear form on ℚ[A]. Taking a = g⁻¹ in invariance gives B(g,h) = B(1, h g⁻¹). Put z := Σ_k B(1,k)·k. Then ε(g z h⁻¹) = z_{hg⁻¹} = B(1, hg⁻¹) = B(g,h), so B(x,y) = ε(x z y*).

B is symmetric if and only if z* = z, because B(1,k) = B(k,1) = B(1,k⁻¹).

For symmetric B, the original line 13's choice z = Σ_k B(1,k⁻¹)·k is z* = z. So for symmetric forms the original formula agrees with this one, and its final statement is correct.

Inversion-compatibility follows as stated, since A is abelian. Items 2–9 and the explicit z = [−1] are unaffected.
