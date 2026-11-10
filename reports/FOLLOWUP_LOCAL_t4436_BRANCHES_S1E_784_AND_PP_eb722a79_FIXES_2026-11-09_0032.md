# FOLLOW-UP (Local-derived) to 26a7c91e + erratum ab20f7ca: PP eb722a79 fixes (C2′, CNF′), A1′ certificates, Oc-2 level 784 status, 2026-11-09 00:32 CST (America/Chicago)

- **Status:** additive. 26a7c91e and ab20f7ca are not edited. This file supersedes only the wording named below.
- **Audit answered:** FINDINGS_PP_AUDIT_LOCAL_ERRATUM_ab20f7ca_2026-11-09_2305.md (sha eb722a79fe11f624f4cb12792d16d6be042ae43240fba06f74e9c7a1796f4479, recomputed; matches its sidecar). PP accepted all of ab20f7ca. **Ruled tally: 96 rows, PROVED 63 · CONDITIONAL 17 · OPEN 5 · REFUTED 9 · PENDING 2**, with c-2 PROVED.
- **Discipline:** Owner t4436, "Let the math lead the pursuits on all open paths". Every menu candidate stays a labelled branch. **Nothing is adopted.** A citation alone never makes a claim PROVED (OW 36683379). "Resonant algebra" is used throughout; RTA appears only as a historical alias.
- **Rules kept:**
  - Additive files only. Nothing was deleted, renamed, moved or overwritten; s9b is not edited.
  - No CERT, nothing sent outside. The other stream's files and its ob_v3 job were not touched.
  - J-2 at 9800 was **not** started; it will be run as s2e by the other stream.
  - Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 is unchanged (checked by this generator at write time).

## C2′ (c-2 row, final wording)

> **c-2 [PROVED, PP eb722a79]** For every **odd** q and every n ≥ 1, SO(V) has exactly two orbits on the Lagrangians (n-dimensional totally singular subspaces) of the split 2n-dimensional nondegenerate symmetric bilinear space (V,B) over F_q. Any reflection r_v with B(v,v) ≠ 0 swaps the two orbits. **One SO-orbit has ∏_{i=1}^{n−1}(q^i+1) members**, and the Codex contour 2∏_{i=1}^{23}(23^i+1) at (24, 23) equals the number of Lagrangians, i.e. exactly two SO-orbits.

- **q odd is used twice:**
  - in the Witt step, f₁ = x − ½B(x,x)e₁ needs 2 invertible;
  - in the reflection step, v = e₁+f₁ has B(v,v) = 2 ≠ 0.
- **"Family" → "SO-orbit".** Wherever 26a7c91e's c-2 row and ab20f7ca's C2 section say "family" or "the two families", read "SO-orbit" or "the two SO-orbits".
- **The r_v remark is restated as: dim(U ∩ r_vU) = n−1.** U ∩ r_vU ⊇ U ∩ v^⊥, which has dimension ≥ n−1. Also r_vU ≠ U, since otherwise r_v ∈ Stab(U) ⊂ SO.
- **Not claimed:** that an SO-orbit equals a parity class (codim U∩U₀ mod 2). The ab20f7ca sentence "r_v changes dim(U∩gU) parity" is withdrawn as a claim beyond the dimension statement above. The count does not use it.

## CNF′ (cosmetic note on s9b)

- s9b's printout reads "x^2-35y^2=+-5 => … 5u^2-7y^2=+-1; mod 5: **-7y^2=2y^2** in [0, 2, 3]". It should read **−7y² ≡ 3y² (mod 5)**.
- The printed value set {0, 2, 3} is correct (3y² mod 5 ∈ {0, 3, 2}), and ±1 ≡ {1, 4} is not hit, so 𝔭₅ is not principal and h(140) = 2 stands.
- s9b is not edited (its sha is in ab20f7ca §E).

## A1′ (optional: certificates for the 146 remaining GB = [1] jobs; no grade change either way)

**Method (s10c):**
- Target: Σ c_i g_i = P^k (k = 1, 2), with deg c_i ≤ D for D = 4…7.
- The degree is found by a rank test mod 2^61−1. Exact cofactors are then solved over ℚ on the pivot columns, and **each identity is verified by exact sympy.expand**.
- Only verified identities count.

**Run:**
- Status: stopped by Local's memory guard to protect the other stream's ob_v3 job (memguard: killed s10c at 00:22:31 rss=2517904 avail=1744MB (to protect ob_v3)).
- Of the 146 jobs it tried 130: **122 certified**, 8 not certified within D ≤ 7; 16 not reached.
- Jobs were ordered by support size (2, 4, 5, then 6 τ-variables).
- Local added a memory guard (kill only if s10c's RSS > 2.5 GB or system available memory < 700 MB) to protect the other stream's ob_v3. It fired: memguard: killed s10c at 00:22:31 rss=2517904 avail=1744MB (to protect ob_v3)

**Running total of certified GB = [1] jobs:** s10 96 + s10b 48 + s10c 122 = **266 of 290**. The other **24** verdicts rest on sympy's exact Buchberger, which is disclosed in the computational base.

Grade: α-3 stays **PROVED** (unchanged).

## Oc-2 at level 784 (s1e)

- **s1e status:** still running (PID 932685), on character D = 8 since about 22:15 CST. Lines on record:
  - level 784, char 1: dim S = 36; T(121) eigenspace for a_11(Xi) = -4: 0; for a_11(49a1) = +4: 8; 20s
  - level 784, char -4: dim 0
- **New, s12 (cheap PARI mfdim of the same cuspidal spaces):**
  - dim S_{3/2}(Γ₀(784), χ_D) = 36 (D = 1), 0 (−4), 42 (8), **0 (−8)**, **0 (−7)**, 34 (28), **0 (−56)**, 41 (56).
  - D = 1 and −4 agree with s1e.
- **[PROVED, new; PARI base]** There is no Oc-2 vector at level 784 for D ∈ {1, −4, −8, −7, −56}: D = 1 has no −4 eigenspace (s1e), and the other four spaces are 0.
- **[PENDING]** D ∈ {8, 28, 56} (dims 42, 34, 41) need the T(121) test that s1e is still running. Oc-2 stays OPEN (alive) and its 784 row stays PENDING.
- The final s1e result, the final sha of its log, and a new sidecar for the log will be recorded in a **second follow-up file** when s1e ends.

## J-2 at 9800

PENDING, to be run as s2e by the other stream. Not started by Local.

## Tally

- **PP-ruled (eb722a79): 96 rows, PROVED 63 · CONDITIONAL 17 · OPEN 5 · REFUTED 9 · PENDING 2.**
- This file changes no grade:
  - C2′ and CNF′ are wording only.
  - A1′ adds evidence.
  - At 784, three more characters are settled inside the still-PENDING row.
- Bridge C stays PARTIAL. The PP Bridge C rollup (46/11/5/2/1 + V₈₄, PP 0f1d3361) is separate and unchanged.

## E. New evidence (evidence_local_t4436_branches_2026-11-09/; each file gets a .sha256 sidecar)

| File | sha256 |
|---|---|
| s10c_alpha_gb1_highdeg_certificates.py | 302cf8d61cf28acca97a64f18555a1ddf12916f985ac1a555af4f2e644040a58 |
| s10c_alpha_gb1_highdeg_certificates.log | 357ddd2112b75a8c3b06c314f536bd7291fad13f7195844ffa42bb826139ffca |
| s10c_alpha_gb1_highdeg_certificates.txt | bacba9b5078c89f189d4cbcd6df5be13775e90d8fbfdf6d3ffe3e1015430ef90 |
| s12_oc2_784_cusp_dims.py | cd150b19ae6928e708e9f010aec20e22890e21e76feb7b4c54c53587cbbff969 |
| s12_oc2_784_cusp_dims.log | c0fe3fd559ce8b44d473514e30d3d28a84a13451591bfa9e716588c75a5ace40 |
| gen_followup1_t4436.py | 51beef46d4d586d4825dbdb50d0e15fafd71f7948876e59e6970e79e966fb7f6 |
