# FINDINGS: PP audit of MR2 O1 map (11D AdS₅×S⁴×Σ₂ → Φ, V₃₅), with NL O1 draft cross-check. 2026-11-09 15:30 CST (America/Chicago)
Agent: Professor Proof (Soft SF), audit under GO (2).
Authority: OW reports/OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md, sha256 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c (re-hashed this turn: MATCH). Vacuum (D): OW 7708ec5d (CONDITIONAL proposal); PP conventions 4660b73e (1357) and 1ab88ebd (1515).
Limits: additive new file only; nothing edited. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 untouched (re-hashed: MATCH). No CERT. Nothing sent outside (one public arXiv PDF read). No Gemini. LOCK 96f8d42e §4: the purged four-force projection mapping is not used, and neither MR2 nor NL uses it (grep: no hit).
Scratch (sympy 1.14.0 / mpmath): /workspace/audit-scratch/pp_mr2_phi_v35_1522/
- pp_audit.py ac695236… / pp_audit.log 99408405… (explicit 11D metric, Ricci, flux, Einstein eq, EH lemma, KR ratios)
- pp_exact_ads.py de6f239f… / .log 5f26539b… (exactness re-check, AdS₅ block; pp_audit prints a Float 4.0 from simplify, exact value confirmed −4k²)
- pp_numbers.py c1137667… / .log 56eb986f… (all numbers, three k normalizations)
- pp_g2.py 8cd76466… / .log 75df2955… (G₂ singlet fractions)
- kr.pdf (hep-th/0003281) sha256 a9640d134c60a6e4c1103f3a821038ddf225a64043179006846bcec5526ed6f8 (prefix a9640d13 = MR2's [L4] pin)
Labels: PROVED / CONDITIONAL / OPEN / REFUTED. Literature citations are CONDITIONAL.

## Rollup
PROVED 17 · CONDITIONAL 7 · OPEN 3 · REFUTED 2.
MR2 label corrections requested: 5 (S1 split, S2, A3, A4, M3-existence). No numeric mismatch found. No claim touches the purged four-force mapping.

## 0. Integrity
- **H1 (PROVED).** sha256 recomputed: MR2 .md fd191d28fb1aa40f974bb2f6df5ff3150984f88803907d534668d7b771ff733f, .py 62be2fa178c295064688aa9d4ddda040e737c8a4b0777b66175e1dcac3deb108, .log cf7b9833fb3547c208c16c1e84ba021f1bbbffc65e685426a68a226d2bc8aa35; each equals its .sha256 sidecar. NL draft 965de066afd51ab52f1ea40fb29271c2e3501d4dc408233b03494709b8fb3302 equals its sidecar (prefix 965de066 MATCH).
- **H2 (PROVED).** PP re-ran a byte copy of MR2's .py (exit 0). Output sha256 cf7b9833… — **byte-identical** to MR2's .log (diff empty).
- Caveat: MR2's script inputs Ricci eigenvalues by hand (3/r², −1/ρ²); it does not compute curvature from a metric. D1 below closes that gap.

## 1. (D) and Kehagias–Russo
- **D1 (PROVED, sympy, exact in k).** Metric ds² = e^{−2ky}η + dy² + r²dΩ₄² + ρ²(du²+dv²)/v², r = √6/(4k), ρ = 1/(2k); G = q₀ vol(S⁴_r), q₀ = 2√6k. Computed from the metric:
  - Ricci eigenvalues −4k² (AdS₅, 5 directions), +8k² (S⁴), −4k² (Σ); off-diagonal Ricci 0. Scalar curvatures: R₁₁ = 4k², R_{S⁴} = 32k² (agrees with PP 1515 erratum), R_Σ = −8k², R_AdS₅ = −20k².
  - G² := G_MNPQG^MNPQ = 576k² and R_MN − (1/12)(G_MPQRG_N^PQR − (1/12)g_MN G²) = 0 identically (all 121 components). Trace check R₁₁ = G²/144 holds.
  - Form equations: dG = 0 (top form on S⁴); *G = c·vol(AdS₅)∧vol(Σ) with c constant, so d*G = 0 = −½G∧G (G∧G = 0). So (D) solves all bosonic 11D equations.
  - MR2's convention G_MN = (1/12)(GG − (1/8)gG²) is equivalent (trace-reversed) to the one used here.
- **D2 (CONDITIONAL, citation; PDF fetched and read).** KR hep-th/0003281 eq. (1) has (1/2κ²)(R − (1/2·4!)F²), eq. (2) R_MN = (1/12)(FF − (1/12)gF²) (same as D1), Freund–Rubin eq. (4) F = 6m₀ε, eq. (5) R_μν = −6m₀² on the 7D part and +12m₀² on X⁴. §3.2 eq. (13): AdS₅ radius² 2R₀²/3, H² radius² R₀²/6, S⁴ radius² R₀²/4; §3.2 names genus-2 quotients; §3.1 shows finite-volume H²/Γ preserves no supersymmetry.
  - With m₀ = 1/R₀ and R₀ = √(3/2)/k: −6m₀² = −4k² and 12m₀² = 8k², and the radii are exactly (D) (L/ρ = 2, L/r = √(8/3)). So (D) **is** the KR solution: Freund–Rubin on S⁴ with the Einstein 7-space AdS₅×H²/Γ (Ric = −6m₀² on both factors).
  - **Flux convention flag (answers NL Q2).** KR (14) prints F̂₄ = 6R₀³Ω₄. The orthonormal amplitude required by (2)/(5) is 6m₀ = 6/R₀ = q₀. If Ω₄ is the unit-S⁴ volume form, 6R₀³Ω₄ has orthonormal amplitude 96/R₀, which is 16 = (R₀/r)⁴ times too large. Our solution has G = (3/8)R₀³·vol(unit S⁴) (sympy). So (14) agrees with (D) only when read as 6m₀·vol(S⁴_{R₀/2}), i.e. Ω₄ normalized as vol(unit S⁴)/16. This is a printing/normalization convention in KR; it does not affect the identification, which D1 proves directly.
- **MR2 S1 label.** "(D) = KR" as a statement about the solution: PROVED (D1 + ratios). The attribution to KR's equations: CONDITIONAL (citation), with the Ω₄ caveat above. MR2's single label PROVED should be split this way.
- **MR2 S2 (MN/GM ≠ (D)): CONDITIONAL** (citation; PP did not re-fetch MN/GM this turn). MR2 labels it PROVED.
- **MR2 S4:** cites PP 4660b73e C4 (probe-M5 charge/tension √6/2 > 1). Correct citation of a PP PROVED-at-probe-level result.

## 2. Φ
MR2's Φ is P-Φ-a: Φ := G_MNPQG^MNPQ (sugra field G). It is a PROPOSAL, not an Owner definition; everything in this section is CONDITIONAL on adopting it, except F4.
- **F1 (PROVED).** On (D), Φ = 24q₀² = 576k² (D1). The O5 equivalence: with G = αF, (α²/12)FF − (α²/96)gF² = 8πG₁₁[(1/6)FF − (1/48)gF²] forces α² = 16πG₁₁ in both terms, so Φ = 16πG₁₁F² = 2κ²F². MR2 M4 correct.
- **F2 (PROVED).** Einstein blocks G^M_M = −6k² (AdS₅), +6k² (S⁴), −6k² (Σ) = −Φ/96, +Φ/96, −Φ/96. k² = Φ/576; Ric_S⁴ = 8k² = Φ/72; **K_Σ (Gaussian = sectional curvature of Σ) = −1/ρ² = −4k² = −Φ/144** (Physicist's check: ✓). At N = 4880 (STD): K_Σ = −0.002430589 = −Φ/144 to all digits.
- **F3 (REFUTED, on (D) and under P-Φ-a; MR2 M6 label correct).** EH (alg-2) "G_fib − G_ext = Φ/144": with fibre S⁴ it is 12k² = Φ/48; with fibre Σ it is 0; fibre-averaged it is 8k² = Φ/72. EH lock "k² = Φ/1728": actually Φ/576 (ratio 3). Each is a precise equation false for k ≠ 0. What MR2's numbers are: Φ/48 = G_S⁴ − G_ext (= (3/2)Ric_S⁴); Φ/576 = k² = 1/L_AdS².
- **F4 (PROVED, new; independent of how Φ is defined).** On (D), G_ext = −6k² is definition-free. EH (alg-1) "G_ext = −Φ/96" forces Φ = 576k²; the lock forces Φ = 1728k². Both cannot hold for any scalar Φ (k ≠ 0). Also EH's own left-hand side G_ext = 6k² − 3K, at its K = 8k², gives −18k², but the actual value is −6k². That formula assumes a 6D Einstein fibre, and S⁴×Σ₂ is not Einstein. For Φ_λ = λ·G·G: alg-1 needs λ = 1; lock and alg-2(S⁴) need λ = 3; alg-2(Σ) has no solution. **So the full EH system (alg)+(EH-lock) is REFUTED on (D) for every possible Φ**, not only under P-Φ-a. This strengthens MR2 M6 and NL §2 (Φ-2).
- **F5.** MR2 "the external coefficient −1/96 does match (PROVED)": correct, but only as the relation G_ext = −Φ/96 under P-Φ-a; EH's formula for G_ext (6k² − 3K) does not hold (F4).

## 3. V₃₅ / Λ⁴ split
- **V1 (PROVED).** The 35-dim space is Λ⁴T*_pM₇, M₇ = ℝ_y × S⁴ × Σ₂ (7-dim; x^μ excluded), dim C(7,4) = 35. Bidegree (y, S⁴, Σ) counts C(1,a)C(4,b)C(2,c), a+b+c = 4: (0,4,0) 1, (1,3,0) 4, (0,3,1) 8, (0,2,2) 6, (1,2,1) 12, (1,1,2) 4; sum 35. MR2 M2 correct. G lies in (0,4,0); of the 35 orthonormal components exactly one is nonzero. Only Λ⁴ of the 6D internal space would give 15.
- **V2 (PROVED, clarification).** The six blocks are the bidegree decomposition, invariant under SO(4)×SO(2) but **not irreducible**: (0,2,2) = Λ²ℝ⁴ = Λ²₊ ⊕ Λ²₋ = 3+3, and (1,2,1) = (3+3)⊗ℝ² = 6+6. The real irreducible decomposition is 1+4+8+3+3+6+6+4. MR2 should say "bidegree split", not "the SO(4)×SO(2) splitting".
- **V3 (OPEN, remark).** The ℝ_y factor comes from the Poincaré/RS slicing of AdS₅; SO(2,4) mixes y with x^μ, so Λ⁴T*M₇ is slicing-dependent. Φ itself is a full 11D scalar and slicing-independent. Owner should know V₃₅/W₃₅ as defined depends on the brane slicing.
- **V4 (PROVED).** MR2 M3 canonicity: Hol(M₇) = SO(4)×SO(2) has rank 3 > rank G₂ = 2, so it is not a subgroup of G₂. Hence no torsion-free G₂-structure induces the (D) metric on M₇. For Bryant's φ (pp_g2.log), the G₂-singlet fraction of a unit coordinate 4-form is 1/7 for 7 of the 35 coordinate 4-planes and 0 for the other 28. So the 1+7+27 split of G is frame-dependent (agrees with NL §4). M3 "existence PROVED" rests on the orientable+spin ⇒ G₂-structure theorem (Gray; Bryant ~L461): **CONDITIONAL** (citation).
- **V5 (A3 label correction).** MR2 refutes "E₇/SU(8) 35+35 applies to (D)" by "11 = 5+6, not 4+7". That argument contradicts MR2's own M1, which uses the 4+7 split x^μ | M₇. A REFUTED needs a precise claim and a valid proof. NL's reason is valid: b₃(S⁴×Σ₂) = 0 (Künneth, Betti numbers 1,4,1,0,1,4,1), so (D) has no 35 massless C₃ axion moduli. **Recommended relabel:** "35 massless C₃ moduli on (D)": REFUTED (b₃ = 0, PROVED); the broader "E₇₍₇₎ structure applies": OPEN.
- **V6 (A4 label).** "No 35 in the 7D SO(5) gauged-sugra sector, REFUTED by count (14, 10, 5)" rests on NVvN field content, which PP did not fetch: **CONDITIONAL** (citation). A5 dims (35 = (2,1) and (4,0) of B₂) PROVED: Weyl formula checked.
- **V7 (name collision; Physicist's request).** The Owner-locked V₃₅ (OW e4ef0a81 / LOCK c290a274) is a dim-14 Hilbert newspace over ℚ(√35). MR2's Λ⁴T*M₇ is a different object. **Recommendation:** use a distinct symbol for the geometric space (NL already uses **W₃₅**; PP recommends adopting W₃₅ in both lanes). **Do not rename the Owner's V₃₅.** dim W₃₅ = 35 ≠ 14 (PROVED), so no linear isomorphism exists. NL's "dim V₃₅(RTA Def. 33.2) = 36" is CONDITIONAL on the corpus statement (Prop. 33.6), which PP did not re-check.

## 4. Numbers (N = 4880, g = 2, ℓ_p = 1; pp_numbers.log, mpmath 30 digits)
Conventions: L₅ = L_AdS = 1/k; Vol(S⁴_r) = 8π²r⁴/3; Vol(Σ₂) = 4π(g−1)ρ² = π(g−1)/k²; G₁₁ = 16π⁷ℓ_p⁹ (2κ² = (2π)⁸ℓ_p⁹); G₅ = G₁₁/(Vol S⁴·Vol Σ₂) = 128π⁴k⁶/(3(g−1)); a = c = πL₅³/(8G₅) = **3(g−1)/(1024π³k⁹)** (PROVED algebra). The holographic formula itself (Henningson–Skenderis; GM (2.8)) is CONDITIONAL (citation) and the reading is CONDITIONAL on a dual CFT existing (PP C4 instability). Calibration AdS₅×S⁵ → N²/4 reproduced (MR2 log, re-run).

| quantity | STD √(3/8)(πN)^{−1/3} | EH quantum on (D) √(3/8)(√2π²N)^{−1/3} | EH own lock (25/(32π²N))^{1/3} [lock REFUTED] |
|---|---|---|---|
| k | 0.02465050 | 0.01499469 | 0.02531377 |
| L_AdS = 1/k | 40.56713 | 66.69028 | 39.50419 |
| r (S⁴) | 24.84219 | 40.83929 | 24.19128 |
| ρ (Σ₂) | 20.28356 | 33.34514 | 19.75210 |
| Area(Σ₂) | 5170.094 | 13972.53 | 4902.710 |
| Φ = 576k² | 0.3500048 | 0.1295082 | 0.3690933 |
| K_Σ = −Φ/144 | −0.002430589 | −0.0008993627 | −0.002563148 |
| Ric_S⁴ = 8k² | 0.004861177 | 0.001798725 | 0.005126295 |
| R_S⁴ = 32k² | 0.01944471 | 0.007194902 | 0.02050518 |
| R₁₁ = 4k² | 0.002430589 | 0.0008993627 | 0.002563148 |
| (ℓ_p/r)⁶ | 4.254618×10⁻⁹ | 2.155415×10⁻¹⁰ | 4.989386×10⁻⁹ |
| G₅ | 9.324866×10⁻⁷ | 4.724033×10⁻⁸ | 1.093526×10⁻⁶ |
| a = c | **2.811513×10¹⁰** | 2.465668×10¹² | 2.213912×10¹⁰ |
| a/((g−1)N³) | 0.2419249 = 8√6/81 | 21.21657 | 0.1905026 |

- **N1 (PROVED).** Every MR2 §5 STD number (k, L, r, ρ, Area, (ℓ_p/r)⁶, Φ, G₅, a_D) matches PP to all printed digits (≥ 7). k and Area also match PP 4660b73e A4/C1. No mismatch.
- **N2 (PROVED, flag).** a = c ∝ k⁻⁹, so it is very normalization-sensitive. EH quantum gives 87.70 × the STD value ((√2π)³); the EH own lock gives 0.7874 ×. MR2 quotes only STD, consistent with the 15:11 Owner record choosing the standard normalization. The EH normalization was already REFUTED by Dirac pairing (4660b73e A3), so the STD value 2.8115×10¹⁰ is the only admissible one. Physicist's "a = c ≈ 2.8115×10¹⁰": ✓ (STD).
- **N3 (CONDITIONAL, citation).** Class-S numbers (MR2 §5 MN rows, §6 P3): re-run reproduces them byte-for-byte. The arithmetic is correct given GM (2.1), (2.4), (2.5) and BBBW (2.22); applicability is only to the MN geometry, not (D), as MR2 states.
- **N4 (PROVED).** P2: pants count 2g−2+n = 63 and 3g−3+n = 64 at g = 2, n = 61. P4: cusped Gauss–Bonnet Area = 2π(2g−2+n)ρ² = 162857.95 and the a ratio 63/2 are correct. ⌊e³·3⁵⌋ = 4880.

## 5. Scan of MR2's other PROVED labels
- M5, M7, M2, P2, A5 dims, the arithmetic of M8: PROVED and confirmed.
- S1, S2, A3, A4, M3-existence: corrected above (§1, V4–V6).
- The OPEN labels (Φ/V₃₅/61-puncture undefined, P1, P5, A7) are appropriate.
- Four-force projection (Lock 96f8d42e §4): not used anywhere in MR2 fd191d28 or NL 965de066.

## 6. Cross-check: NL draft 965de066 vs MR2 fd191d28
| item | MR2 | NL | verdict |
|---|---|---|---|
| Φ definition and value | P-Φ-a, 576k², = 16πG₁₁F² | Φ-1, 576k², = 2κ²F²; "T^(EH) = 2T_std" | **Agree**, and both right (F1: α² = 16πG₁₁ = 2κ²). |
| restoring 1/1728 | via 3·G·G is "a convention, not derived" | Φ-2 = 3G·G breaks L7a, so REFUTED as a choice | **Agree in substance**; NL sharper. F4 here goes further: no Φ at all works. |
| EH relation refutations | alg-2 Φ/48, lock Φ/576 | same + Σ fibre (0) + averaged (Φ/72) | **Agree**; NL more complete; all correct (F3). |
| K_Σ = −Φ/144 | PROVED | PROVED | **Agree**, correct (F2). |
| 35-space and split | Λ⁴T*M₇, 1+4+8+6+12+4 | same, named W₃₅ | **Agree**; both miss that blocks are reducible (V2). |
| symbol | flags collision, keeps V₃₅ | uses W₃₅ | NL's practice is right; recommend W₃₅ (V7). |
| G₂ split | canonicity OPEN | frame-dependent PROVED | **Compatible**; NL right (V4 confirms). |
| A3 (E₇ 35+35) | REFUTED by 5+6 vs 4+7 | CONFIRMED via b₃ = 0 | **Disagree on the reason**: NL's is right; MR2's conflicts with its own M1 (V5). |
| KR flux amplitude | quotes 6R₀³Ω₄ as matching | unresolved convention factor | PP resolves: matches only with Ω₄ = vol(unit S⁴)/16 (D2). MR2's "ratios match" right; NL right to flag. |
| numbers (k, Φ, G₅, a) | as §5 | same | **Agree**; both right (N1). |
| L-dim (W₃₅ ≇ V₃₅) | not stated | REFUTED (14, 36 vs 35) | NL right for 14 (PROVED); 36 CONDITIONAL on corpus. |
No substantive mathematical disagreement; the only conflict is A3's rationale.

## 7. Handoff note for O4 (not audited here; MR2 KK file 7824e789 is a separate audit)
KR eq. (5) shows (D) is Freund–Rubin with flux on S⁴ and an Einstein 7-space Y⁷ = AdS₅×H²/Γ, Ric = −6m₀² on both factors (PROVED in D1: −4k² on each). So any DeWolfe et al.-type formula that uses only the Einstein condition on the non-flux factor applies with Y⁷ in the AdS₇ slot, as long as the derivation never uses maximal symmetry of AdS₇. The O4 auditor should check that point, and the Σ-Laplacian shifts, there.

## 8. Plain verdict
MR2's O1 map is mathematically sound. PP recomputed (D) from the metric and confirmed it solves the 11D equations exactly, is the Kehagias–Russo solution, and gives Φ = G·G = 576k², K_Σ = −Φ/144, and the 35-dim Λ⁴ count with the 1+4+8+6+12+4 bidegree split. All numbers at N = 4880, g = 2 match to all printed digits, including a = c ≈ 2.8115×10¹⁰ (standard normalization only; a ∝ k⁻⁹ so other normalizations differ by large factors). The EH relations Φ/144 and Φ/1728 are correctly REFUTED on (D), and PP proves more: no definition of Φ can make the EH system hold on (D). Five labels need correction (S1 split into PROVED/CONDITIONAL, S2, A4 and M3-existence to CONDITIONAL as citations, and A3's refutation argument replaced by b₃ = 0), and the geometric space should be called W₃₅ to keep the Owner's V₃₅ untouched. Φ and W₃₅ remain PROPOSALS awaiting Owner adoption.

Tip 7cddb188 untouched. No CERT. Nothing sent outside. No Gemini.
