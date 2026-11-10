# FINDINGS — PP AUDIT of NL F1 (O3 + O5): T^(EH) on AdS₅×S⁴×Σ₂, standard flux normalization — 2026-11-09 ~15:30 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Additive new file; nothing edited or renamed. Tip 7cddb188… untouched. No CERT. Nothing sent outside. No Gemini.
Authority: OW OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md, sha 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c — sidecar MATCH. GO (2): PP audits NL. LOCK 96f8d42e… §4 honored: no Kronecker/four-force mapping is used; F1's "G₄" is the 4D Newton constant of PP 9dde377d B2/B3, not a purged mapping.
Scratch (local sympy/mpmath/numpy): /workspace/audit-scratch/pp_nl_f1f2_1525/
- f1_check.py d7df120a… · f1_check.log f8429336… · f1_num.py 1adf4b8f… · f1_num.log 726d2076…

## 0. Target verification
| item | expected | on disk | sidecar |
|---|---|---|---|
| NL_DERIVED_F1_TEH_ON_ADS5_S4_SIGMA2_STD_NORMALIZATION_O3_O5_2026-11-09_1520.md | f2e5120d | f2e5120d975da057ca77ffee345cc9dcd66ebbd271f0528a8f8e8f20b7d4694e | MATCH |
| /workspace/nl-1511/f1_teh_vacuum.py | 21e96ef9 | 21e96ef909a948fe… | MATCH (prefix) |
| /workspace/nl-1511/f1_teh_vacuum.log | 253b967a | 253b967aef0318d0… | MATCH (prefix) |
| context PP 4660b73e, 1ab88ebd, 4f370d8f, 4d07bd1b, 9dde377d; OW 7708ec5d; RECORD 5b4592d4 | — | all located by sha prefix | — |
- NL's T^(EH) definition, quoted from F1 §1: "T^(EH)^M_M = (1/6)GG − (1/48)G²". Owner text (OW 5a6e7177, NL O5), quoted: "T^(EH)_MN = (1/6) F_MPQR F_N^PQR − (1/48) g_MN F_PQRS F^PQRS." NL's usage matches the Owner's formula.

## 1. Standard stress tensor and the ½ (A1, A2 — PROVED, CONFIRM)
- **A1 (PROVED).** Take S = (1/2κ²)∫√−g R + S_m with S_m = −(1/48)∫√−g F_PQRS F^PQRS, and the Hilbert definition T_MN = −(2/√−g) δS_m/δg^MN. Since δ(√−g F²)/δg^MN = √−g(4F_MPQR F_N^PQR − ½ g_MN F²), we get T_MN = (1/6)F_M···F_N··· − (1/48)g_MN F² = **T^(EH)_MN exactly**. The Einstein equation is G_MN = κ² T^(EH)_MN. **In conventions with 2κ² = 1 this is G_MN = ½ T^(EH)_MN.**
- **A2 (PROVED, identity).** The standard 11D form, from (1/2κ²)∫(R − ½|G|²) with |G|² = (1/4!)G², is G_MN = (1/12)(G_M···G_N··· − (1/8)g_MN G²) =: T_std. Identically (1/6)FF − (1/48)gF² = 2·(1/12)(FF − (1/8)gF²), so **T^(EH) = 2 T_std** for every 4-form (sympy: T_EH − 2T_std = 0 in all 11 components). NL §2 CONFIRMED.
- **A2′ (PROVED).** NL's equivalent form, G_MN = κ₁₁² T^(EH)(F) with F := G_std/(√2 κ₁₁), is the same statement: (1/2κ²)·(−½|G|²) = −(1/48)F² under that rescaling. CONFIRMED. So NL's "½ convention" is nothing more than G = κ²T with 2κ² = 1 — the standard equation, not a new convention.

## 2. Block values on AdS₅(L=1/k)×S⁴(r=√6/4k)×H²(ρ=1/2k) (A3–A5 — PROVED, CONFIRM)
Full 11D diagonal metric e^{−2ky}η + dy² + r²dΩ₄² + ρ²(du² + sinh²u dv²), Christoffels/Ricci computed directly in sympy (f1_check.log):
- Off-diagonal Ricci ≡ 0. Mixed Ricci: −4k² (5 AdS₅ directions incl. y), +8k² (S⁴), −4k² (Σ). R₁₁ = −20k² + 32k² − 8k² = **4k²**.
- **Einstein tensor G^M_M: −6k² (AdS₅), +6k² (S⁴), −6k² (Σ₂)** — i.e. (−4−2), (8−2), (−4−2). **(−6, +6, −6)k² CONFIRMED.**
- G = q vol(S⁴_r): G_MPQR G_N^PQR = 6q² g_MN on S⁴, 0 elsewhere; G² = 24q². T^(EH) mixed = (−½, +½, −½)q²; T_std = (−¼, +¼, −¼)q². CONFIRMED.
- G_MN = ½T^(EH) ⇔ q² = 24k² ⇒ **q₀ = 2√6 k**; residual 0 in all 11 components. Extra (PROVED): dG = 0 and ∂_M(√−g G^{MNPQ}) = 0 (√−g G^{5678} is independent of the S⁴ angles), and G∧G = 0, so the 4-form equation holds; the solution is complete, not only the Einstein part.
- **A6 (PROVED).** The reading G_MN = T^(EH)(G_std) gives residual (+6, −6, +6)k² at q₀ and would need q = 2√3 k; with ∫_{S⁴}G = (2πℓ_P)³N and Vol(S⁴_r) = (3π²/8)k⁻⁴ this rescales k³ by 1/√2, i.e. k by 2^{−1/6}. CONFIRMED. NL's remark that this "breaks Dirac pairing" is CONDITIONAL on PP 4660b73e A1/A3 (it is the same issue as A3: the quantum (2πℓ_P)³ belongs to the action normalization (1/2κ²)∫(R − ½|G|²)).
- NL's choice to record the failed reading as "PROVED-fails" rather than REFUTED is acceptable: no adopted record asserted it.

## 3. Numerics at N = 4880, g = 2 (A8 — arithmetic PROVED; inputs CONDITIONAL)
mpmath 30 digits (f1_num.log); every NL value reproduced:
k = 0.0246505002 · r = 24.8421911 = (πN)^{1/3} · ρ = 20.2835641 · L = 40.5671282 · flux check q₀Vol(S⁴)/(2π)³ = 4880.000 · Area(Σ₂) = 5170.09355 · Vol(S⁴_r) = 1.00237002×10⁷ · V₆ = 5.18234680×10¹⁰ · G₁₁ = 16π⁷ = 4.83246916×10⁴ · G₅ = 9.32486643×10⁻⁷ · V₇eff(kb→∞) = 1.05116463×10¹² · G₄(∞) = 4.59725243×10⁻⁸ · G₄(kb = 0.8, 1, 2) = 5.76022×10⁻⁸, 5.31680×10⁻⁸, 4.68303×10⁻⁸. Curvatures k² = 6.0765×10⁻⁴, 8k²/3 = 1.6204×10⁻³, 4k² = 2.4306×10⁻³, (ℓ_P/r)⁶ = 4.2546×10⁻⁹. **All MATCH.**
- G₄ beyond kb → ∞: OPEN (b unfixed) — CONFIRMED.

## 4. Λ₀, κ, R_c and side fact (A9 — PROVED; one citation CONDITIONAL)
- Λ₀ = 0.7835772176, κ = 1.5976222401, r/R_c = 15.5495, ρ/R_c = 12.6961, L/R_c = 25.3922, 1/R_c² = 0.3918 ℓ_P⁻². MATCH (agrees with PP 4f370d8f, 1ab88ebd).
- Fundamental unit (PROVED, independent proof): 35 ≡ 3 (mod 4) so 𝒪 = ℤ[√35]; x² − 35y² = −1 has no solution (−1 is a non-residue mod 7), and y = 1, x = 6 is the least solution of x² − 35y² = 1, so ε = 6+√35 is fundamental and ln ε is the regulator. CONFIRMED.
- "V₃₅ field of OW c290a274": no top-level reports/ file with sha prefix c290a274 was located; the reference is CONDITIONAL (unverified citation). Nothing in F1 depends on it.

## 5. Sugra validity and stability
- Curvature values PROVED (§3); "two-derivative sugra controlled" is CONDITIONAL on the EFT criterion — CONFIRMED as labeled. Stability stays OPEN beyond PP C4 — CONFIRMED (MR2's O4 BF claim 7824e789 is audited separately).

## 6. NL label tally check
NL states PROVED 5 · CONDITIONAL 4 · OPEN 3 · REFUTED 0 and lists exactly 5/4/3/0 items. **Tally MATCH.** No PROVED label found to be wrong.

## Errors found
- None material. Minor: (m1) the "½ convention" is just G = κ²T with 2κ² = 1 (A1) and could be stated so; (m2) the Dirac-pairing remark should carry CONDITIONAL (on PP A1/A3); (m3) c290a274 citation not located.

## Rollup (this audit)
PROVED 9 (A1, A2, A2′, Ricci/Einstein blocks, flux contractions and T blocks, q₀ closure incl. 4-form eqs, A6 core, §3 arithmetic, §4 values + fundamental unit) · CONDITIONAL 4 (Dirac-pairing remark; numbers as model statements at chosen N, g under OW 5a6e7177/7708ec5d; sugra validity; c290a274 citation) · OPEN 3 (G₄ for finite kb; physical role of R_c, Λ₀; full stability) · REFUTED 0.
**Verdict: F1 is CORRECT.** T^(EH) = 2T_std, G_MN = ½T^(EH) (= κ²T^(EH) at 2κ² = 1), blocks (−6, +6, −6)k², q₀ = 2√6k and all N = 4880, g = 2 numbers are confirmed. Everything is CONDITIONAL on the Owner's adopted vacuum and inputs.
