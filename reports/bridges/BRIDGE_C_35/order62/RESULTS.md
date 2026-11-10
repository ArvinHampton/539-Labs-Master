# order62 RESULTS (LOCAL Bridge C; RG* labels; CORE_FREEZE; no push/send)
PREREG sha256 83a7b4654553b7e0d5781acd05e6a5270463f398b1a21d6793374c732ff90eaa (hashed before any test).
Script scripts/rg47e.py; data/rg47e.json; logs/rg47e.log. Not used: P̂_orth, Ξ, k≠0, Map-C6, Weil matrices. order≤61 read-only.

## RG47e (Cat A-numeric): FAIL
- Gate: R excess reproduced (34 at w=½, 2 at w=1).
- (1) Sanity PASS: max |R − corner/EVEN| = 2.67e−15 ≤ 1e−12 (x and −1/x sides). So R = corner/EVEN identically.
- (2) Span test at w=1 FAIL: rank[R|C] = 34 (= rank R, so corner is already the span), joint 36, **excess_proj = 2**. w=½ (disclosure): excess_proj 34. Unchanged at tol 1e−6 and 1e−12.
- Meaning: the 2-dim w=1 defect is NOT removed by the corner column span; it is the corner/EVEN piece failing its own weight-1 S-pairing. The defect directions lie outside span(|x|·C_S) (residual norm 0.21).
- Carriers (w=1): spread, top row weights ≈0.03 each, x = 11/7, 10/7, 20/7, 8/5, 9/5, 3/7, 13/7, 11/5 (denominators 7 and 5). w=½: small-x rows 1/8…1/15 (weights ≈0.78).
- Disclosure: rank/excess of R2 itself (reported 105) is noise-floor rank of a ~1e−15 matrix (relative tol), not meaningful.

## RG48-Weil: SKIP (ABSENT, OPEN)
FOUND (written, quoted):
1. order12/RESULTS.md:29 — "the χ = ±i basis should be built from the Weil representation itself, by computing the discriminant form of the companion lattice and its signature-2 genus mates." (proposal only)
2. order12/PREREG.md:11 — definite lattice with same discriminant form as A has Weil factor e(−2/8) = −i (rationale only).
3. order13/PREREG.md:6–14, RESULTS.md:7–9 — T-law obstruction: Θ_E + h cannot satisfy χ=±i for any h; genus-mate basis "not needed"; Milgram remark (rank-2 definite impossible).
4. papers/RTA_FOUNDATION_BOUND/src/partII/s11_family.tex Thm tensor7 — explicit Weil matrices for ρ_lab = ρ5⊗ρ7⊗ρ2 (q5=2x²/5, q7=x²/7, F_p, T_p, S_2, T_2 on L'/Z²≅Z/35 with g=(7,3)/35). This is the LAB lattice Weil rep, not a companion lattice / χ=±i full basis.
5. order61/RESULTS.md:37–44 — prior ABSENT list.
ABSENT: companion-lattice discriminant form / Gram as a written object; χ=±i Weil eigenvectors over a full basis; written signature-2 genus-mate basis construction.
READY-FOR-RG48-WEIL: NO. Milgram stays Cat B. Note order13 (Cat A T-law obstruction) may make RG48 moot; physicist to decide whether s11 ρ_lab qualifies as the "companion" (not assumed here).

## Suggested order63
RG47f: test the corner/EVEN piece alone under a vector-valued (ρ_lab, s11) S-law or Δ-type law at w=1 to explain the 2-dim defect (carriers den 5,7 → ρ5/ρ7 sectors). RG48: either physicist rules order13 supersedes (close), or Arvin supplies written companion form.
