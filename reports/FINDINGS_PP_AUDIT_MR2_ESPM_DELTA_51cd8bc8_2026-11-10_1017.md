# PP audit: MR2 E-S± δ(f) on vertical spin structures (51cd8bc8), proposed regrade of cc21b272 row 14
Written 2026-11-10 by Professor Proof (CST; the file mtime is authoritative).
- Additive file in reports/ only. Nothing was edited, and nothing was written into MR2's directories or /workspace/mr2-c2e8-1010/.
- Nothing is adopted. Junction UNSOLVED. No CERT, no Gemini, nothing sent.
- E-T is not touched.
- **Tip 7cddb188 was MATCH before and after.**

## Integrity
| file | sha = sidecar | mtime (CST) | notes |
|---|---|---|---|
| report 51cd8bc8… | ✓ | 10:11:21 | header says ≈10:11–10:14; read it as ≈10:11 (MR2 note aca26c53) |
| script 5cdf6aaa… | ✓ | 10:08:44.800 (sidecar same) | r--r--r--; reports/ copy cmp ✓ |
| log 7837d39c… | ✓ | 10:08:45.360 | reports/ copy cmp ✓; the script was frozen before the log |
| note aca26c53… | ✓ | 10:12:53 | — |

**PP rerun** of a scratch copy (/workspace/audit-scratch/pp_espm_1015/s.py): exit 0.
- Its output is identical to 7837d39c **except the final line "EXIT 0"**. That line was appended by MR2's run wrapper, not printed by the script.
- With that line added, my output is byte-identical (cmp ✓). Nit: say so in the log description.

**PP independent exact script:** pp_indep.py 88c7e6c9 / log 981e3b38. No floats, no simplify.

**Self-disclosed nits, all confirmed:**
- The first `cl = {…}` comprehension is dead. It computes the same conjugation g∘p∘g⁻¹ and is overwritten, so it is harmless.
- The assertion `len(set(...)) >= 1` is vacuous.
- The script name "1015" is ~6 min ahead of the run.

**New PP nits:**
- [S] uses numpy `allclose` (float).
- [W2] uses `sp.simplify(…) == 0`.

PP replaced both with exact checks (below). No grade is affected.

## Checks (1)–(7)
**(1) δ(f), exact. Confirmed.**
- I derived the W-permutations myself from explicit maps:
  - g1: x ↦ ix, with f(ix) = i·f(x);
  - g2: x ↦ (1+x)/(1−x), with f(g2 x)(1−x)⁶ = −8 f(x), so both lift to Bolza;
  - c: complex conjugation.
  They equal MR2's GEN.
- Image orders are 48 and 24.
- I computed fixedness through invariance of the **quadratic form** q_T under the induced action on H¹, which does not depend on the subset normalisation. There are 16 distinct forms.

**(2) Fixed counts. Confirmed exactly.**
- The (fixed, Arf=1 among fixed) counts over the 24 orientation-reversing images are: (8,4)×3, (4,2)×6, (2,0)×6, (4,0)×1, (1,0)×8. This matches MR2's table.
- c fixes exactly the 8 listed structures.
- By hand: a singleton is fixed iff it is not {±i}. A 3-set is fixed only as {a,b,d} ⊂ {0,∞,1,−1} or as {i,−i,a}, which are the same 4 classes mod complement. c(T) = complement(T) is impossible, because c fixes 0, ∞, 1 and −1.
- Cross-check by citation only: the Gross–Harris count 2^{g+k−1} with k = 2 real ovals gives 8. The Sturm/sign count gives real branch points {−1, 0, 1}, with x⁵−x > 0 on (−1,0) and (1,∞).
- **"S₊ and S₋ lift exactly on those 8":**
  - Lifts of Λ²± to SU(2)± form H¹(Y₆;ℤ₂)-torsors, and s ↦ S±(s) is equivariant over the identity of H¹, so it is a bijection. Hence f lifts to S±(s), covering df|Λ²±, iff δ(f;s) = 0. This holds for both chiralities on the same 8 ✓.
  - **Scope defect, "no lift for the other 8":** this is PROVED only for lifts covering df on Λ²±, or equivalently connection-preserving lifts of the canonical form. As an unscoped statement it is too broad: a *topological* isomorphism f*V ≅ V exists for every instanton number n (cc21b272 row 15, given D4).
  - For an *arbitrary* connection-preserving E₈ lift, PP has a sketch, which is COND and not part of the graded rows:
    - the fibre restriction of the vertical connection is the Levi-Civita connection of the squashed S⁴;
    - its holonomy is SO(4) (de Rham + Berger, and S⁴ has no almost-complex structure; these are citations);
    - so the holonomy of S± is the full SU(2);
    - a connection-preserving E₈ lift then reduces to an SU(2) lift (the normaliser acts by inner automorphisms), and that lift must cover df.

**(3) Strict ℤ₂ lift. PP proof supplied; it holds given Emb.**
- *f̃² = −1.* For r = c there is a fixed point p: a real point of Σ, and in its fibre a point of the +1 eigenspace of the fibre O(5) element. df_p on V_vert = diag(1,1,−1,−1).
  - The lift is ±e₃e₄, and (e₃e₄)² = −1 exactly (sympy Clifford check). It commutes with chirality, so it preserves S₊ and S₋.
  - f̃² covers f² = id (R-inv), so it is a deck transformation: a continuous ±1 on connected Y₆, hence constant, so it equals −1.
- *Dressing.* With Q = P ×_{SU(2)} E₈, set F′[p,g] = [f̃p, h g].
  - F′ is well-defined iff h centralises ι(SU(2)), i.e. h ∈ E₇. h is a single group element, so the dressing is **constant** (global, independent of the point).
  - F′ preserves the induced connection, because horizontal lifts are taken at fixed g.
  - F′²[p,g] = [f̃²p, h²g] = [p, ι(−1) h² g].
  - In (SU(2)×E₇)/⟨(−1, z₇)⟩, ι(−1) = z₇, the central element of E₇, so F′² = 1 iff h² = z₇.
  - E₇ is compact and connected, so exp is surjective: z₇ = exp X, and h = exp(X/2) works.
- So the lift squares to +1. This is **proved**, not just asserted.
- MR2's phrase "h commutes … with f̃" is not the operative reason; the reason is centraliser well-definedness. Wording fix.

**(4) Emb premise.** It is stated, with the index-1 SU(2), centraliser E₇, and 248 = (3,1)+(1,133)+(2,56). Its scope is correct for rows 11–12.
- **Missing from the premise list:** the identification L ≅ TΣ, or K^{±1}, **with f|_L = dr**, i.e. the gauge field equals the spin connection, A = dx/y = ω₁₂.
- This is used in §2(b) and row 3, and it is the 8399be55 *twist* model (COND). It is stated in the text but not listed. It is inherited from cc21b272 rows 10, 12 and 13, so the implication is sound once it is listed.
- No other unstated premise was found. The fixed point needed in (3) follows from R-inv as stated ("with fixed points").

**(5) 8399be55.** Model M is graded COND (row 4) and is used only as a premise. It is not upgraded ✓. The twist part must also be listed as COND (see (4)).

**(6) Note, Arf wording. Confirmed.** All 8 c-fixed representatives have odd cardinality (4 singletons with Arf 1, four 3-sets with Arf 0), which gives 4/4 in the Arf sense ✓. The note is faithful and changes no grades.

**(7) Parent tally.** If the parent erratum accepts row 14, the cc21b272 tally moves **15/2/6/0 → 16/2/5/0 = 23**.

## Verdict on the 13 rows
1. PROVED. PP's exact check replaces simplify.
2. PROVED. π* is a torsor isomorphism, and stabilisation is a bijection.
3. PROVED as an implication of M **and the twist identification f|_L = dr**. Scope addition.
4. COND.
5. PROVED, exact.
6. PROVED.
7. PROVED as an implication of M.
8. PROVED.
9. PROVED as an implication of M.
10. PROVED as an implication of R-inv and the twist-model fibre action. PP's exact Clifford check replaces numpy.
11. PROVED as an implication of Emb and R-inv, using PP's proof above.
12. PROVED as an implication of M, the twist model, R-inv and Emb, **scoped**:
    - the "exists for the 8" half: as filed;
    - the "fails for the other 8" half: only for lifts covering df|Λ²±.
    - Unscoped, it is not proved; topological lifts exist.
13. OPEN.

**PP tally: PROVED 11 · COND 1 · OPEN 1 · REF 0 = 13.** It agrees with MR2 numerically; rows 3 and 12 need scope fixes. **No grade changes.**

**cc21b272 row 14, E-S±. Accepted: OPEN → PROVED as an implication** of:
- M (COND);
- the 8399be55 twist identification f|_L = dr (COND);
- R-inv;
- Emb;

**for** r in the c-class (c, Jc and their conjugates; they are involutions with fixed points) and s one of the 8 structures fixed by *that* r. The fixed set is conjugated along with r.

Both S± lift, with a strict ℤ₂ lift after a constant E₇ dressing. For the other 8 structures there is no lift covering df|Λ²±.

Still OPEN:
- which r and which s the physical 1a datum uses;
- the other orientation-reversing classes (only δ is computed there; involutivity is not claimed);
- E-T.

B1-c2′ stays COND overall, not adopted. Literal c2 and c2″ are unchanged. 8399be55 remains COND.

## Fixes for MR2 (additive)
1. **priority:true.** List the twist identification "L ≅ TΣ (K^{±1}) with f|_L = dr (8399be55 twist model, COND)" as a premise of rows 3, 9, 10, 12 and of the row-14 regrade.
2. **priority:true.** Row 12 and §4: scope "no lift for the other 8" to lifts covering df|Λ²± (connection-preserving, canonical). Topological lifts exist for all n (cc21b272 row 15). The general connection-preserving case needs the holonomy argument (COND).
3. Row 11: replace "h commutes with f̃" with the centraliser well-definedness argument and ι(−1) = z₇ ∈ Z(E₇). Cite exp surjectivity on compact connected E₇.
4. [S] and [W2]: replace numpy `allclose` and `simplify == 0` with exact checks (as in pp_indep.py).
5. Log description: state that the trailing "EXIT 0" line is written by the wrapper.
6. Optional: cite the Gross–Harris 2^{g+k−1} cross-check, as a citation only.
