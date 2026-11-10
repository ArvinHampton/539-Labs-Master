# PP audit: MR2 B1-c2′ E₈ wall bundle under 1a, r̃ / f = P∘r̃ invariance (cc21b272)
Written 2026-11-10 1007 CST by Professor Proof. New additive file in reports/ only. Nothing was adopted and the junction is UNSOLVED. Nothing was written into MR2's directories or /workspace/mr2-c2e8-1010/. No other agent's jobs were touched. **Tip 7cddb188 was MATCH before and after.**

## Integrity
- **Report** cc21b2728dd7… = sidecar ✓, mtime 10:03:24. Its header says "≈10:02–10:10"; the end of that range is after the mtime. Nit: read it as written ≈10:03.
- **Script** 33dca96fde7e… = sidecar. The original and the reports/ copy are cmp-identical ✓. It is chmod a-w, and the .py and its sidecar share mtime 10:00:58.8799, before the log at 10:01:00.596 ✓. The name "1010" is ahead of the run, as disclosed.
- **Log** 73ced586abda… = sidecar, cmp-identical to the reports/ copy ✓.
- **PP rerun** from a scratch copy (/workspace/audit-scratch/pp_c2e8_1010/s.py): exit 0, log **byte-identical** to 73ced586 ✓.
- Self-nits confirmed:
  - the `G4sets` placeholder is dead code; the G₄ check uses the bd47ff5e sets `bd`;
  - name/header times vs mtimes;
  - [Q] is a single-point float result.

## PP exact re-check of [M]
pp_M.py 7a045e06 / log f103a38a. This replaces MR2's `simplify == 0` test with a structural exact test:
- no metric entry depends on x, φ₁, φ₂, x³ or the AdS translations;
- the only off-diagonal pairs are (x, φ₁) and (μ₁, μ₂);
- for each map, every nonzero g_ij has s_i s_j = +1.

So r̃, P, f and c2′ are exact isometries of the chart metric. **PROVED.**

## Verdicts by cluster

### A. Topology of Y₆ (rows 1–5)
- **Row 1 (D1): PROVED.** In the Serre spectral sequence only q ∈ {0, 4} and p ≤ 2 occur, so there are no differentials into or out of E^{0,4}. The local system is trivial because U(1) is connected. H⁴ = ℤ, torsion-free.
- **Row 2 (D2): PROVED.** TY₆ ⊕ ℝ = π*(TΣ ⊕ L ⊕ ℝ³), so p₁ ∈ π*H⁴(Σ) = 0 rationally, and integrally by row 1. The same holds for the pullback of the 11D tangent bundle (T(wall) ⊕ normal line). ½ tr R² is therefore exact and has zero fibre integral.
- **Row 3 (D3): PROVED** as an implication of the HW normalisation (f825dfff).
- **Row 4 (D4): COND.** It cites BE₈ ≃ K(ℤ, 4) through dimension 15; dim 10 < 16.
- **Row 5 (D5): PROVED** for constant-in-frame sections. The transitions are U(1) rotations, and deg L = ∓2 ≠ 0.

### B. Maps (rows 6–10)
- **Row 6: PROVED** (PP structural check above).
- **Row 7: PROVED.** The fibre Jacobians are −1, −1, +1, +1. Because the local system is trivial, f*a = deg·a on H⁴.
- **Row 8: COND** (float, one point). It uses the 11D curvature restricted to internal indices. The naturality argument does not depend on that choice.
- **Row 9: PROVED.** Curvature is natural under every isometry, including orientation-reversing ones, and tr R∧R contains no ε.
- **Row 10: PROVED as an implication, but the implication's scope must be widened.** dr̃² = d(r²) = id requires **r² = id, i.e. r is chosen to be a reflection (an involution)**. Isom(Bolza) \ Aut⁺ also contains orientation-reversing elements of order > 2. The premise is therefore "8399be55 twist model **and r an involution**". As written, the row omits that premise.

### C. Bundle candidates (rows 11–16)
- **Row 11 (E-0): PROVED.**
- **Row 12 (E-T): PROVED** as an implication of row 10 (with its added premise). df preserves the Levi-Civita connection because f is an isometry. n = 0 by row 2 ✓.
- **Row 13 (E-Λ±): PROVED** as an implication of row 10.
  - f preserves the vertical distribution, its metric and orientation (degree +1), and the horizontal distribution (the orthogonal complement), so each Λ²± is preserved with its connection.
  - r̃ has degree −1 and swaps Λ²₊ ↔ Λ²₋ ✓.
  - The normalisation (embedding index) does not enter the lift.
- **Row 14 (E-S±): GRADE CHANGE, COND → OPEN.**
  - The existence of a vertical spin structure is PROVED: w₂ = π*(c₁(L) mod 2) = 0 because deg L is even ✓.
  - But whether f preserves some vertical spin structure (the δ ∈ H¹(Σ; ℤ₂) check) **was not computed**, and no premise is cited that would make it COND. An undone computation is OPEN.
- **Row 15: PROVED** as an implication of D4. a ↦ (degree)·a. r̃*a = −a ⇔ a = 0 because ℤ is torsion-free. Here "lift" means only that f*V ≅ V; equivariance is row 16.
- **Row 16: OPEN** ✓.

### D. M5 data and the remaining maps (rows 17–23)
- **Row 17 (M-s): PROVED** as an implication: f*G = +G, naturality of tr R², and an invariant connection.
- **Row 18 (M-loc): PROVED.**
  - f restricts to φ₂ ↦ −φ₂ on S²₀.
  - The worldvolume reflections are {x, x³} and the transverse reflections are {φ₁, φ₂}. With f*G = +G and fibre degree +1, the linking flux, and hence the M5 charge, is preserved.
  - This rests on the bd47ff5e index sets, as in rows 7 and 20.
- **Row 19: OPEN** ✓.
- **Row 20: PROVED**, given the bd47ff5e sets. r̃*G = −G gives J ↦ −J and M5 ↦ anti-M5. This is consistent with literal B1-c2 being REF (7f366e78) and with r̃ failing the bosonic rule (d0f833ff).
- **Row 21: PROVED** as an implication of ℝ^{1,3}-invariance of the wall data. Topologically it holds automatically.
- **Rows 22–23: OPEN** ✓.

### E. Branch verdict
MR2's verdict is **confirmed**, with the scope added:
- The E₈-lift row of 8e766c4c moves from OPEN to "PROVED as an implication, for E-0, E-T and E-Λ±, under the premises: HW normalisation, the twist model, **r an involution**, and ℝ^{1,3}-invariance". It is also PROVED topologically for every n given D4. The M5 part must be M-s, or M-loc with symmetric stacks.
- Still OPEN:
  - E-S±;
  - equivariance for a general datum;
  - M-curve;
  - whether any candidate is the physical 1a wall;
  - the pointwise Bianchi equation with J_M5 ≥ 0;
  - supersymmetry.
- B1-c2′ stays **COND overall**, not adopted.
- Unchanged: B1-c2″ (COND/OPEN), literal B1-c2 (REF, scoped), and 1a (pure form REF; rescues OPEN; not adopted). This is consistent with 7f366e78 and c3d4f0fe; no prior ruling is reopened.

## Tally
- **MR2: 16/3/4/0 = 23** graded rows, plus 1 bookkeeping row. This is arithmetically correct for MR2's own labels.
- **PP: PROVED 16 · COND 2 · OPEN 5 · REF 0 = 23**, plus 1 bookkeeping row; junction UNSOLVED. The only grade change is row 14, COND → OPEN.
- **No row is refuted.**

## Fixes for MR2 (additive)
1. **priority:true.** Row 10, and through it rows 12 and 13: add the premise "r ∈ Isom(Bolza) \ Aut⁺ is chosen to be an involution (a reflection)". f² = id and the ℤ₂-equivariance depend on it.
2. **priority:true.** Row 14: regrade COND → OPEN, because the δ check was not done. Keep "a vertical spin structure exists (w₂ = 0): PROVED" as a sub-statement. The tally becomes 16/2/5/0 = 23.
3. Row 6: cite the structural exact argument (no entry depends on the reflected coordinates; the only off-diagonal pairs are (x, φ₁) and (μ₁, μ₂)) instead of `simplify == 0`.
4. Header: write "≈10:03", the mtime; "10:02–10:10" runs past it.
5. Row 8 / [Q]: note that the 11D curvature restricted to Y₆ indices was used. Naturality makes the parity result independent of that choice.
6. Row 18: name the bd47ff5e index sets as the premise for f*G = +G.

**Sha of this findings file:** see its .sha256 sidecar.
