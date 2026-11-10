# FINDINGS — MR1 in-set CF(980) mod-p runner + CRT toward CERT-under-H_work (Rec A AUTO) — 2026-10-26 ~18:10 CDT (America/Chicago)
Soft-SF Write-only. tip_touched NO. No Eigen contact (no Eigen file read, copied or run this run). Kerr BLOCKED. Eight-only. Cat-A invent NONE. Proof standard: proof OR named gap.

## 1. STATUS
**PARTIAL / GAP.** **0/7 cells CERT-under-H_work.**
PROVEN this run: Sage installed (passagemath 10.8.13, Py3.12 venv `/workspace/venv_sage_mr1_312`); ω_p LOCKED convention re-verified in Sage at all 3 primes (ω_p of exact order 980, least such g, Φ₉₈₀(ω_p)=0); ∏p = 17303251105541478881544161 > 2·H_work; CF(980) machinery (336 embeddings ζ↦ω_p^a, Vandermonde inversion to power-basis coordinates mod p, CRT + symmetric lift) self-tested PASS on 3 public test elements (NOT cell values).
BLOCKED: cell residues NOT emitted at any prime (blockers B1, B2 below). No old residue remapped (G4c').

## 2. Authority (live sha256 verified at start)
| Item | sha256 | |
|---|---|---|
| OWNER_WRITE in-set runner | 8460682f8531538c52540aec1146c5de052808ab2456de0db6d569c048aee8c1 | MATCH |
| ASSIGN | 8de2068e676ad3aa9009e2ceee59e252b49a07ec6fe1adf8f1936ca719c70af5 | MATCH |
| Source FINDINGS more-primes | a472e4b3681f6d0b1a23e53fbf44d914081f3907652432b56aef517a426bf43d | MATCH |
| Prime/ω_p table | 3ccf185a6710efb2714d36385adab4028d2d2942821cb1861fa9e52a7effb71a | MATCH (re-asserted inside runner) |
| tip residual-c-field-WRITTEN_PREMISES_DRAFT.md pre = end | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | untouched |
Operative CSVs TE-SIMPSON-FILL-MODP_N18 / SCHEDULE_TORD_N18 read only for cell identity; not modified.

## 3. Sage install outcome
pip passagemath-modular (Py3.13): no distribution. pip passagemath-standard (Py3.13): FAILED (memory_allocator wheel build). uv venv Py3.12 + passagemath-standard: **OK** — `CuspForms(Gamma0(49),4).dimension()=10` (public sanity). Log `mr1-cf980-inset-runner/sage_install.log`.

## 4. Runner (in-set, non-Eigen)
`mr1-cf980-inset-runner/cf980_modp_runner.py` — logic from public literature only (Washington Ch.2; standard Sage CyclotomicField/GF/crt). Output `cf980_modp_runner.log`. ω_p sidecar `OMEGA_SIDECAR_2026-10-26.csv`.
| p | ω_p | check |
|---|---|---|
| 7840981 | 34692 | order 980, least, Φ₉₈₀ root ✓ |
| 1027606441 | 4692531 | ✓ |
| 2147486741 | 2179324 | ✓ |

## 5. Per-cell table (rel. ω_p)
| Cell | p1 | p2 | p3 | Stamp |
|---|---|---|---|---|
| N36 ν=1,4,9,14,16 | NOT EMITTED | NOT EMITTED | NOT EMITTED | BLOCKED (B1,B2) |
| N6 ν=1,9 | NOT EMITTED | NOT EMITTED | NOT EMITTED | BLOCKED (B1,B2) |
Table `CELL_RESIDUES_REL_OMEGA_2026-10-26.csv`. N6 ν=29/81/109/121 (HOLD extras) not attempted; same blockers.

## 6. Named gaps
- **B1 (ρ̄ exact over CF(980) not in-set).** The target space S₄(Γ₀(49),ρ̄) is LOCKED (Card 1A) as inverse-transpose of the exact S,T action on V42_exact — which lives only under an Eigen path. The only in-set V42 build (heavy-daily `2026-10-18-V42-Structure/v42.py`, family.py 07dabdaa…) is a float SVD span; it is not an exact CF(980) basis and does not fix the 36⊕6 split basis. Rebuilding exact ρ̄ from it would require choices not Written in-set ⇒ would be Cat-A invention. Not done.
- **B2 (cell identity is basis-dependent).** The 7 cells are coordinates of "seed comp k e{ν}/140" vectors over Eigen-built echelon bases (503×… for N36, 89×6048 for N6, 8-cusp slot convention). No in-set Written specification of slot ordering, seed, or cusp truncation exists, so a fresh build cannot be proved to compute the same cells.
- **G4c'** stands: on-disk residues have unrecorded root; no identification to ω_p proved; none remapped.
- **CRT degree caveat (PROVEN):** CERT needs all 336 power-basis coordinates mod each p (equivalently all 336 embeddings ω_p^a); runner implements this, but has no cell input.
- **G4a** (ℚ(ζ₄₉) containment) OPEN; **G4b** true-H OPEN; H_work working bound only. No ζ₄₉-only claim. No tip fold.

## 7. Rec A (concrete next)
Owner Write either (a) **Write in-set** an exact ρ̄(S),ρ̄(T) over CF(980) on V42 (matrices with entries as power-basis vectors in ζ₉₈₀) plus the N36/N6 basis spec (cusp set, slot ordering, truncation, seed component, RREF normalization) as a hashed non-Eigen Soft-SF artifact — then MR1 runs `cf980_modp_runner.py` extended to solve the module mod p at each p with ζ↦ω_p^a, emits 7×3×336, CRTs, and stamps CERT-under-H_work if lifts verify; or (b) authorize an independent in-set exact construction of V42 from family.py label Weil rep (Written choices for basis/split/slots) and accept that cells are re-defined by that Write.

## 8. Posture
PARTIAL/GAP; 0/7 CERT; STATUS ≠ MATCH. tip_touched NO; Kerr BLOCKED; No Eigen.
