# NL ERRATUM 25: accept PP b39c7756 (D6 stage-3 resume audit)
2026-11-10, 1052 CST (America/Chicago). **NL derived proposal.** Additive only. No existing file is edited, renamed or deleted; the 0958–1027 resume files stay frozen, and this erratum records the fixes.
Frozen targets: Erratum 24 (60bbc718…), E5 (0a7d8e56…), E2 (197c5bd1…), E4 (4c25565f…), E1 (2f33b65d…), S2-8 (d559cb7d…), Z2 corner (101467fc…).
Authority: Owner call-83d7a0fa status-then-resume record (e72a188b…, sidecar OK), standing OW t4436 (32881263…), OW t4431 (f700141d…). Context-only ant-colony/Taormina record (6436510d…) is not used here and adopts nothing. Nothing adopted by fiat. **Junction: UNSOLVED. Count gap: unchanged.** No CERT, no Gemini, nothing sent. Tip 7cddb188… checked before and after.
Input: PP resume audit FINDINGS_PP_AUDIT_NL_D6_STAGE3_RESUME_2026-11-10_1048.md (b39c7756… = sidecar). PP evidence under /workspace/audit-scratch/pp_nl_d6s3_1030/, including pp_d6s3_resume_exact_2026-11-10_1045.py / .log (0dc4c510… / 53be779c…).

**Tally: PROVED 0 · CONDITIONAL 0 · OPEN 0 · REFUTED 0 · total 0.**
This erratum contains **only bookkeeping and premise restatements**. Distinct new claims (for any roll-up): **0/0/0/0**. No label and no tally of any earlier file is changed, with the counting note on E4-3 recorded in §4.

## 1. Accepted drops (PP-audited PROVED implications)
PP accepts both proposed drops, as proved implications, once the missing premise (h0) is listed (Fix 1) and the HW-projection mislabel is restated (Fix 2). The grades of the 1019–1027 files are unchanged.

- **E5-4, PROVED (implication).** Drop of **E5 ∩ H_Σ ∩ SO(3)_R**, with or without U(1)_R, including scope S, is accepted under the complete premise list:
  - (h0)/(h2) x-independent Poincaré supercharges;
  - (h1);
  - (P-a) at least one Killing spinor;
  - (ii) the D1 HW projection Γ^n ε = ε on the face (not S6);
  - (reg) at one face point p ∈ C₄ ∩ face, with C₄ ∩ face ≠ ∅;
  - (tw);
  - H_Σ;
  - SO(3)_R acting on the S² factor and commuting with the twisted SL(2,ℝ).
  Flux, Bianchi, N_face, IR, σ, the D1 rows, the source profile n(χ), and U(1)_R are unused. This is an independent, flux-free route to the S2-7 conclusion on scope S. **S2-7 itself stays CONDITIONAL**, and its grade is not changed.

- **E2-4, PROVED (implication).** Drop of **E2 ∩ (SO(3)_R × U(1)_R)** is accepted under the complete premise list:
  - (h0)/(h2), (h1), (P-a);
  - (ii) the D1 HW projection, not "record premise S6";
  - (reg-all) on all of C₄ ∩ face;
  - (F-4) face bundle ≅ vacuum twisted bundle, and C₄ ≅ Σ×S² isotopic to the vacuum locus, with SO(3)_R acting only on S² and U(1)_R fixing C₄ pointwise and acting there as ½Γ^{m1m2};
  - Σ connected, of genus 2.
  (gr) is not needed: Σ_n̂ ⊂ C₄ ⊂ face gives T_p Σ_n̂ ⟂ n, so the T-plane is TΣ_n̂. Not covered by this drop: a face singular on any nonempty part of C₄, E2 ∩ E5, E2 ∩ E1, and failure of (F-4) on E2.

- Earlier drops are unchanged: E3; S5 (BPS only).

## 2. Fix 1 (priority) — list (h0)
**(h0) = Erratum 24 (h2): x-independent Poincaré supercharges.**
It is to be listed among the premises of **E5-3(b), E5-4, E2-4 and E1-1**. **P8-1 inherits it**, because P8-1 inherits the full premise lists of E5-4 and E2-4.

Reason, from PP's hand proof and P4: Γ^{0123} commutes with every internal operator appearing in the KSE, the HW projector, and the Kosmann action of an internal x-independent warp-preserving Killing vector, but it **anticommutes with Γ_μ X**. It therefore maps the solution space of ∂_μ ε + Γ_μ X ε = 0 into that of ∂_μ ε − Γ_μ X ε = 0, and it preserves the Killing-spinor space only on x-independent spinors (∂_μ ε = 0), where the x-row reduces to Xε = 0. Superconformal-type spinors ε = (1 + x^μ Γ_μ …)η mix chiralities. Under (h0), V_ℂ splits as V₊ ⊕ V₋ by χ₄ = ±i, and both members of a doublet share χ₄.

This is a premise-list completion, not a defect in the math. (h2) is already on the program record (Erratum 24, PP 113e8035). E5 §0 listed only "(P-a) at least one Killing spinor"; E2-4 step 1 used x-independence without listing it.

PP also proved E5-3(b) by hand in the other Clifford representation (volume = −1). Exactly one s₃ survives in all 8 lock/orientation cases. NL's chirality script re-run is byte-identical (rerun_chirality.log = 676f7dc8…). Ruling unchanged: E5-3 PROVED (exact + hand); part (b) is an implication under (h0)/(h2) and (h1).

## 3. Fix 2 (priority) — HW projection is not S6
E2 §0 (ii) and E1 §0 call the HW projection "record premise S6". That is a mislabel. Restate (ii) as the **D1 HW hypothesis** Γ^n ε = ε on the face (equivalently ε(−r) = Γ_n ε(r), continuous at the wall). **S6 is the odd-HW record** (f825dfff), as the E5 file already distinguishes. The E2 and E1 (ii) lines are to be read in this restated form; the frozen files are not edited.

## 4. Fix 3 (priority) — restate E4-3
E4-3 as filed is **not accepted** (the "dimension 2 / finite / smearing" derivation is defective, and the α-sheet classification is not exhaustive). It is **not REFUTED**. What is PROVED, and all that E4-5 uses, is the restatement:

**Restated E4-3 (PROVED).** An H_Σ × SO(3)_R-invariant source support meets C₄ ∩ face if and only if it contains C₄ ∩ face (E4-1).

The α-sheet classification is not exhaustive: the SO(3)_R-fixed U(1)_R circles at μ₃ = μ₄ = μ₅ = 0, smeared over H² at any r, give H_Σ × SO(3)_R-invariant supports, and they are disjoint from C₄.

In E4-5, replace "natural sources realising (a)/(b) on C₄ are … the α sheets" by the restated E4-3. The other E5-4/E2-4 premises ((h0), (ii), (tw), F-4, P-a) are branch-defining and are named as such. E4-1, E4-2, E4-4 and E4-5 stay PROVED (E4-2 wording in Fix 7; E4-5 aligned as just stated). E4-6 stays OPEN. The E4 file tally remains **5/0/1/0 with E4-3 counted only in this restated form**.

## 5. Fix 4 — diagonal-K scope
The following hold only for **diagonal K**:
- the E2-2 "forced by equal D1 K" flux column;
- E5-5's "unique diagonal K";
- E1-2.

On E2 the T-plane has no isotropy, so K|_T is a general symmetric 2×2, and the forcing column does not transfer as stated. On E5 without U(1)_R, the K-invariant symmetric forms on the weight-1 4-plane are 4-dimensional (PP P11), so "unique diagonal K" is an ansatz statement. On [w], U(1)_R is kept, so diagonal K is forced (P11); elsewhere it is a subfamily.

The "ω₂ free / no obstruction" conclusions still stand, because enlarging the K family only adds solutions. These statements are not load-bearing for E2-4. The three U(1)_R × U(1)_n̂-invariant tangential face fluxes are confirmed (PP P12). The conjugate-pair statement in E5-5 (same K, opposite χ₄) is exact.

## 6. Fix 5 — E2-3: degree 0, not "trivial"
Write "locked lines have **degree 0**", not "trivial". Only the degree is used, and isomorphism classes can differ by 2-torsion through the spin structure.

Both locked lines have degree 0, by conjugation antisymmetry (PP P10: d(−s₁, −s₂′) = −d(s₁, s₂′), so d = a·s₁ + b·s₂′ with 2a = ε₀(2g−2)) together with the vacuum (S2-1 exact, plus F-4) supplying a nowhere-zero section of a locked line, hence a − b = 0. Then both unlocked lines have degree 2a·s₁ = ±(2g−2) = ±2 on genus 2. (gr) is not needed for T-plane ≅ TΣ_n̂, as in §1.

## 7. Fix 6 (optional) — shorter E5-4 proof, and (reg)
Record PP's streamlined proof of E5-4, which does not need the doublet decomposition. NL's version (a chiral doublet with opposite s₃) is the same argument restricted to one irreducible summand, and is correct.

1. Take V₊ ≠ 0 (otherwise use V₋). It is a finite-dimensional complex representation of su(2)_R (Kosmann).
2. Let U(1)_n̂ ⊂ SU(2)_R be the stabiliser of the S²-point of p. At its zero p, (L_ξ ε)(p) = ½ Γ^{tf} ε(p). By injectivity and equivariance of ev_p (reg), the U(1)_n̂-weights on V₊ are s₃/2 for the s₃ values that occur at p.
3. Every ε ∈ V₊ satisfies at p: χ₄ = i, Γ^n = +1 ((ii), with n = ±e_r), and the lock (E5-2). By E5-3(d), ε(p) has the single value s₃ = s₃*.
4. So V₊ has the single U(1)_n̂-weight s₃*/2 ≠ 0. But the weights of any nonzero finite-dimensional su(2)-representation are symmetric under w ↦ −w. Contradiction.

n = ±e_r follows from C₄ ⊂ face: n ⟂ T_p C₄ ⊃ T_p S², and n is K-invariant and ⟂ x, so n is the unit vector of span(x, r, TS²) orthogonal to x and TS². Add "**C₄ ∩ face ≠ ∅**" to (reg), as already written in the premise list of §1.

## 8. Fix 7 — E4-2 wording
K fixes only the S² over p̃. In H_Σ the fixed set of K_{p̃} is the S² over p̃. C₄ is the union of those S² over Σ, and its smoothness follows from homogeneity. C₄ itself is not "the fixed set of K". The equivariant-exp argument for a closed, totally geodesic fixed set stands.

## 9. Fix 8 — Z2 v1 stop time
The Z2 file's v1 continuation stop time "about 10:0x CST" is inconsistent with the record. The v1 script mtime is 10:10:16 CST and its log mtime is 10:12:52 CST (sidecar 10:13:07). Record the stop as **about 10:12–10:13 CST** (America/Chicago). The v1 log remains program output only and supports no claim. The frozen Z2 file is not edited.

## 10. Fix 9 — relabel v2 ComplexWarning
Relabel v2 casts complex values to real (ComplexWarning lines in the log) without printing max|imag|. A later script, if one is written, should print max|imag| as continuation v2 does (cf. PP f530cbc0 Fix 5). The frozen relabel v2 script is not edited. Float only; no grade effect. Z-2 stays CONDITIONAL (float).

## 11. Fix 10 — E2 header shas
The E2 header's "hashes in the sidecars" is replaced, for the record, by the full shas:

- /workspace/nl-d6s3-1110/e2_pairs_degree_exact_2026-11-10.py = 1bfbbac71e1b549605b0f060eb3db83492383408cf54747bc8a99cb335f0044d
- /workspace/nl-d6s3-1110/e2_pairs_degree_exact_2026-11-10.log = 66f95d9a7442dac16f8503ce0424c75bf21174d062d20ded3cc2db9f44c3efdd

The frozen E2 file is not edited. PP's re-run log is byte-identical to this log.

## 12. Fix 11 — chirality-script dead code (hygiene)
Dead code in chirality_hw_lock_exact_2026-11-10.py (unused `proj`, empty loop at lines 130–134) is harmless. Leave the script frozen. Note only.

## 13. Branches (register; not counted)
[χS], [χU] and [w]/Z2 are all kept. Their regular-on-C₄ parts in the dropped sub-branches are covered; δ-support on C₄ goes to E4.

- **Dropped** (PP-audited PROVED implications, under the premise lists of §1): E5 ∩ H_Σ ∩ SO(3)_R, with or without U(1)_R, including scope S; E2 ∩ (SO(3)_R × U(1)_R). Earlier: E3; S5 (BPS only).
- **Kept / OPEN:** E5 ∩ ¬H_Σ = E2 ∩ E5 (E5-6/E2-5); E2 ∩ E1; E1 as a whole (E1-4), including E1 ∩ H_Σ, where E1-1 gives a constraint but no contradiction, and [w] with KK spinors; E4, singular on all of C₄ (H_Σ ∩ SO(3)_R) or on any nonempty part of C₄ (E2) (E4-6); premise failures not covered by either drop — (F-4) failing on E2, x-dependent (non-Poincaré) supercharges, a face not meeting C₄; S2-8 / P8-3; Z2 corner S2-13 (Z-3); non-BPS Z2 walls; non-BPS S5 (S3b-4).
- **CONDITIONAL, unchanged:** E1-3 (BPS Z2 excluded inside the truncation, on a citation); P8-2; Z-2 (float).
- S6 (odd HW ℤ₂, record f825dfff) is a record premise, not a math escape. Nothing adopted.

## 14. Tallies of earlier files (unchanged)
| file | tally |
|---|---|
| D6 stage 2 (2216), revised | 8/2/3/0 = 13 (S2-7 COND, S2-11 OPEN as filed) |
| Erratum 23 (2241) | 2/0/0/0 row count; 0/0/0/0 distinct |
| Stage 3 E3 (2245) | 3/0/0/0 = 3 |
| Stage 3 S5 (2245) | 3/0/1/0 = 4 |
| Erratum 24 (0958) | 0/0/0/0 |
| E5 (1019) | 6/0/1/0 = 7 |
| E2 (1021) | 4/0/1/0 = 5 |
| E4 (1021) | 5/0/1/0 = 6, with E4-3 counted only in the restated form of §4 |
| E1 (1022) | 2/1/1/0 = 4 |
| S2-8 (1022) | 1/1/1/0 = 3 |
| Z2 corner (1027) | 1/1/1/0 = 3 |
| Resume total (1019–1027, excluding Erratum 24) | 19/3/6/0 = 28 (18 + E4-3 restated) |

No previously ruled grade changes. Refutations: none.

## 15. Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 0 | — |
| CONDITIONAL | 0 | — |
| OPEN | 0 | — |
| REFUTED | 0 | — |

Check: 0 + 0 + 0 + 0 = 0 (bookkeeping and premise restatements only).

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
