# U1 LEDGER — PARI-free certification of the s = 7 cusp-part results (K = Q(√35)) — 2026-10-18

Package: `PARI_Free_Certification_2026-10-18/` (report `2026-10-18-PARI-Free-Certification.md`, scripts and logs, verbatim).
Pure copy-and-create. No existing file edited. No locks altered. CORE_FREEZE holds. Distinct from any HQCC termination claim. No TPC or RH claim.

## Category A (verified / proved; exact finite computation or standard theorem on exact data)
- A1. Cl⁺_𝔪 for 𝔪 = 𝔭₂³𝔭₅𝔭₇∞₁∞₂, built by hand from U → (O/𝔪)^× × {±}² → Cl⁺_𝔪 → Cl → 1: order 96, structure Z/24 × Z/2 × Z/2. Same for 𝔣 = (2√35)∞₁∞₂. (`rc.py`, `groupinv.txt`)
- A2. Independent class assignment of all 140 components reproduces the PARI fit exactly: 22 empty (label, sign) slots, all contents g, Eis/cusp/mixed norms (≤ 6.7e-16), the same 24 cusp components with coefficients (1/48)e(k/60), and the 60 + 12 split (ranks 60 / 12). (`part1.py`, `part1_compare.py` → `part1.txt`)
- A3. The 12 values L(0,χ) of the totally odd, non-σ-invariant characters of conductor (2√35), exactly, in Z[ζ₁₂] (exact Shintani cone sums; Shintani's s = 0 formula is a standard theorem): −(6+4√3) ± (6√3−4)i, −12 ± 4i, (4√3−6) ∓ (4+6√3)i, each occurring twice. Validations: Σ_c ζ(0,c) = 0; L(0,χ) = 0 for the 72 non-totally-odd characters; L(χ) = L(χ∘σ); genus test exact for all 8 characters mod 20; two independent moduli agree exactly. (`shintani.py`, `cyc24.py`, `part2.py` → `part2.txt`)
- A4. All 7 × 24 cusp-row identities hold to 1.2e-14 with PARI-free inputs. (`part3.py` → `part3.txt`)
- No discrepancy with the PARI-based results was found.

## Category B / caveats
- The all-n theta identity is checked for |Q| ≤ 400 only (B for all n).
- Hand inputs not recomputed: ε = 6+√35 fundamental; Cl = Z/2 (𝔭₁₃, 𝔭₁₃² = (22+3√35)).
- Characters are determined only up to χ ↔ χ∘σ (inherent).
- Not redone without PARI: L(1/2,χ), L(1,χ), root numbers, functional-equation checks.
- No modularity / Maass-Hecke interpretation claimed beyond these identities.

## Files not included
- `part1.pkl` (0.86 MB), `part2.pkl`, `char_match.pkl`: binary pickles (regenerable by the scripts).
