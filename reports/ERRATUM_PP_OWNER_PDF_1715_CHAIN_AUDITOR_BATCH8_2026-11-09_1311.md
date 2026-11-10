# ERRATUM — PP Owner-PDF-1715 chain vs Auditor Batch 8 — 2026-11-09 13:11 CST (America/Chicago)

Role: Professor Proof (Soft SF). Reports only. Additive new dated file.
Authority: OWNER_WRITE_CALL_e9c1dbda_WRITE_DERIVE_AUTHORIZATION_2026-11-09_1300.md (sha 33d25a79…).
Limits: no overwrite of frozen/hashed records; tip 7cddb188… untouched; no CERT; nothing external; pure math.
Labels: PROVED / CONDITIONAL / OPEN / REFUTED.

## Sources audited
| Tag | Path | sha256 prefix |
|---|---|---|
| B08a | reports/bridges/AUDITOR/AUDITOR_CORPUS_CRAWL_BATCH08a_INTAKE_1715_2026-11-09.md | 06278429… |
| B08b | reports/bridges/AUDITOR/AUDITOR_CORPUS_CRAWL_BATCH08b_INTAKE_1854_1910_1944_2026-11-09.md | 99f9e748… |
| C3-4 note | reports/bridges/AUDITOR/AUDITOR_NOTE_C3-4_G2_LABEL_2026-11-09.md | (note) |
| P1715 | intake/owner-20261105-1715/01M6PZWMGT7HB8CRARJ1RXF4BE.pdf | 65b08abb… |
| T1854 | intake/owner-20261105-1854/OWNER_MASTER_COORDINATE_TRANSFER_1854.txt | dbfa0f94… |
| PP base | reports/FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW_2026-11-05.md | 17ab357b… |
| AdC | …_ADDENDUM_C_BLUEPRINT_1734_2026-11-05.md | d6344622… |
| AdK | …_ADDENDUM_K_1855_2026-11-05.md | 6fa122a8… |
| AdA | …_ADDENDUM_A_2026-11-05.md | ae8aa76f… |
| AdH/I/L | Addenda H, I, L (same chain) | — |

Batch 8 found. Flags B8-2, B8-3, B8-4, C3-4 verified independently below (not by trust of Auditor).

Computation (python3 + sympy.kronecker_symbol): `8007581 % 140 == 1`; `χ_140 := (140/·)` on `(ℤ/140ℤ)^×` yields split (+1, 24 residues) and inert (−1, 24 residues) matching AdC :8–:9 exactly; `χ_140(9)=χ_140(13)=+1`; `isprime(8007581)=True`.

---

## Flag 1 — B8-2: `8007581 ≡ 121 (mod 140)` vs `≡ 1`

### Original lines
- **P1715 (pdftotext)** ~:647–649: `independent holdout prime 8007581, which satisfies 8007581 ≡ 121 (mod 140), it maps into a distinct split class`
- **AdC :13**: `Original 25 primes cover 24 unit classes mod 140 (8007581≡1): 1,3,11,…`

### PP verdict: **CONFIRMED error** (in P1715); **PARTIAL** as to the PP chain
- **PROVED** by direct arithmetic: `8007581 = 57200·140 + 1`, so `8007581 ≡ 1 (mod 140)`, not 121.
- AdC :13 already states the correct congruence `≡1`. The PP chain therefore does **not** repeat the false `≡121`.
- What the chain **omitted** (Auditor B8-2): it never flagged P1715's false `≡121` claim. That omission is real.

### Corrected text
> The holdout prime 8007581 satisfies `8007581 ≡ 1 (mod 140)`. Since `χ_140(1)=+1`, it lies in the split class of the identity residue. It does **not** occupy class 121.

### Downstream
- AdC's coverage list (class 1 included via the holdout; class 121 among the 24 missing) is consistent with `≡1` and needs no change.
- P1715's "distinct split class 121 ⇒ row independence ⇒ det K_140 ≠ 0" argument is void as stated. Independently, PP base :5 already **REFUTED** `det ≠ 0` (row p=7 identically 0). No later addendum depends on `≡121`.
- Note: none of the 24 training primes is ≡1 mod 140, so the holdout does add class 1; the PDF's "new class" intuition survives only after correcting 121→1. Class 121 remains uncovered by the 25-prime set.

---

## Flag 2 — B8-3: inert list wrong at 13

### Original lines
- **P1715** :67–68 / :179 / :385: inert domain `{3,9,13,27}` (mod 140), i.e. `K[i,j]=−1` iff `p_i p_j ≡ 3,9,13,27 (mod 140)`.
- **PP base :6**: flags `(35/9)=+1` vs `K(3,3)=−1` (so flags 9); describes the PDF residue set as `{1,3,9,13,27}` without separately computing `χ(13)`.
- **AdC :8–:10**:
  - Split: `1,9,13,17,19,23,29,31,33,43,59,67,73,81,97,107,109,111,117,121,123,127,131,139`
  - Inert: `3,11,27,37,39,41,47,51,53,57,61,69,71,79,83,87,89,93,99,101,103,113,129,137`
  - `Claimed inert 13,19,29 are SPLIT`

### PP verdict: **CONFIRMED error** (in P1715 at 13 and at 9); **PARTIAL** on "PP flagged 9 only"
- **PROVED**: `χ_140(13)=kronecker(140,13)=+1` ⇒ 13 is **split**, not inert. Same for 9. True inert set = AdC :9 (24 residues); matches Auditor's listed set.
- Context of the character: for odd `p ∤ 140`, inertness in `ℚ(√35)` is `χ_140(p)=(35/p)=(5/p)(7/p)=−1` (AdG :33, PROVED). The PDF's four-residue "Inert Domain" is not that set.
- Base PP :6 explicitly refuted only the 9-case via `K(3,3)`. AdC :10 already flagged 13 (and 19,29) as SPLIT and published the correct 24+24 lists. So "PP chain missed 13" is false for AdC; it is true only of the base review.

### Corrected text
> Replace the PDF inert domain `{3,9,13,27}` by the Kronecker set `{n ∈ (ℤ/140ℤ)^× : (140/n)=−1}` (= AdC :9). In particular 9 and 13 are split (`χ=+1`).

### Downstream
- AdC/AdG/AdL/AdW already use the correct character; AdW :52 "3 is inert in ℚ(√35)" remains **VALID**.
- No later PP addendum treats 13 as inert. The old piecewise K refutation (PP base :5–:6; AdC :11) stands independently of the 13-label.

---

## Flag 3 — B8-4: T1854 `coker D = 0` (:125–127) vs parameter-dependent (:195)

### Original lines (T1854, sha dbfa0f94…)
- **:125–127** (`Exact Surjectivity and Cokernel Vanishing`): recursive solve `x_i = y_i + T_i x_{i−1}` ⇒ `D` surjective ⇒ `\operatorname{coker} D = 0`, "regardless of the choice of transformation matrices, even when every `T_i = 0`".
- **:195** (final sentence of `Decoupling of the Sequential Action`): `dim ker D` and `dim coker D` "must be determined through actual parameter values rather than follow from prime classifications alone".

### PP-chain lines
- **AdK :13** (initial): called the :195 claim CORRECT — **itself an error**, later withdrawn.
- **AdK.1 :39–:41**: CORRECTION — unrestricted `D` has `coker D = 0` and `ker D ≅ L_0` for every `T_i`; only the boundary kernel `ker(C_0 + C_M T_M⋯T_1)` is parameter-dependent. Source sentence :195 is FALSE for unrestricted `D`.
- **AdH :11**, **AdI :12–:13**: independent proofs of surjectivity / `ker D ≅ L_0`.
- **AdL :11**: affirms K.1.

### PP verdict: **CONFIRMED** — T1854 is internally inconsistent; the correct statement is AdK.1 / AdH / AdI
- **PROVED** (Addenda H, I): for `D(x)_i = x_i − T_i x_{i−1} : ⊕_{i=0}^M L_i → ⊕_{i=1}^M L_i`, forward recursion shows surjectivity for every choice of `T_i`, hence `coker D = 0` identically, and `ker D ≅ L_0`.
- Therefore :125–127 is **PROVED** (as a statement about unrestricted `D`), and :195 is **REFUTED** as stated (it asserts parameter-dependence of `dim coker D` / `dim ker D` for that same `D`).
- Soft reading of :195: if "unreached state boundaries" is re-parsed as the **boundary** cokernel/kernel after imposing `C_0, C_M`, then that object *is* parameter-dependent — but that is not what the source text says (`dim coker D`). Under the Soft SF standard the two passages conflict as written.

### Corrected text
> For unrestricted `D`, `coker D = 0` and `ker D ≅ L_0` for every `(T_i)`. Parameter dependence begins only at the boundary map `C_0 + C_M T_M⋯T_1`. Strike or rewrite T1854 :195 accordingly.

### Downstream
- AdK.1 already applied the correction; AdL stands on it. No further PP addendum reverts to the :195 claim. Initial AdK :13 remains a superseded in-file error (B6-2 class: post-hoc amendment).

---

## Flag 4 — C3-4: mislabel at PP base line 18

### Original line
- **PP base :18**: `Tier E input: a_μ = 11659181×10⁻¹⁰ is the muon g−2 measured value, not an arithmetic constant.`

### PP verdict: **CONFIRMED** MISLABEL (label only; Tier-E status unchanged)
- **PROVED** by matching digits: `11659181×10⁻¹⁰ = 116591810×10⁻¹¹`, which equals the 2020 Muon g−2 Theory Initiative **SM prediction** `a_μ^SM = 116591810(43)×10⁻¹¹` (Aoyama et al., Phys. Rep. 887 (2020), arXiv:2006.04822), not any experimental average (E821 / FNAL 2021 / FNAL 2023 world averages all lie near `11659206×10⁻¹⁰`).
- Auditor note C3-4 is correct on the label. AdA :10 already regraded provenance to "stipulated parameter (DEFINITION) / Tier E" without correcting measured-vs-SM.

### Corrected text
> `a_μ = 11659181×10⁻¹⁰` is the 2020 Standard-Model prediction (Aoyama et al., Phys. Rep. 887), not a measured value. Tier-E / non-arithmetic status unchanged. Measured world averages are ~`11659206×10⁻¹⁰`.

### Downstream
- No pure-math verdict in the 1715 chain depends on measured-vs-SM. κ / Λ₀ remarks on the same line are unaffected (`√(2/0.7858) = 1.5953610…`, PROVED arithmetic). AdA :10 regrade stands.

---

## Rollup

| Flag | Target | PP Soft-SF verdict | Already fixed in PP chain? |
|---|---|---|---|
| B8-2 | P1715 `8007581≡121` | CONFIRMED error in source; PP states `≡1` but never flagged the PDF | Omission only |
| B8-3 | P1715 inert domain at 13 | CONFIRMED error in source; "PP flagged 9 only" is PARTIAL (AdC flagged 13) | Yes (AdC) |
| B8-4 | T1854 :125–127 vs :195 | CONFIRMED self-contradiction; :125–127 PROVED, :195 REFUTED for unrestricted D | Yes (AdK.1) |
| C3-4 | PP base :18 "measured" | CONFIRMED MISLABEL | Label pending; Tier E already AdA |

No tip edit. No CERT. No existing file modified.
