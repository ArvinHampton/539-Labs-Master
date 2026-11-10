# SOFTSF PRESS — MR1 CF(980) more primes + CRT toward CERT-under-H_work (Rec A AUTO) — 2026-10-26 ~17:50 CDT (America/Chicago)
Soft-SF Write-only. No CSV edits. No Eigen contact. tip untouched. Kerr BLOCKED.
## 1. STATUS
**PARTIAL.** PROVEN: prime set {7840981, 1027606441, 2147486741}, all prime and ≡1 mod 980, with ω_p recorded under the LOCKED convention; ∏p = 17303251105541478881544161 ≈ 1.73·10^25 > 2·H_work = 2·10^18. BLOCKED: residues at the new prime (no in-set mod-p runner: Sage absent on box; the only CF-capable runners are Eigen-dir scripts, off-limits), and on-disk residues lack a recorded root (G4c'), so they cannot be re-expressed relative to ω_p. **0/7 cells CERT-under-H_work.**

## 4. Prime set + ∏p vs 2·H_work
Running: 7840981 → 8057442579358621 (≈8.06e15, < 2e18) → 17303251105541478881544161 (≈1.73e25, **> 2e18 ✓**). New primes: **1**. Gate on product: MET.
Caveat (PROVEN arithmetic, not a gate change): reconstructing an element of ℤ[ζ₉₈₀] (rank 336) from one embedding per prime is under-determined; CERT needs either all 336 embeddings ζ↦ω_p^a (a∈(ℤ/980)^×) per prime, or the ℤ-coordinate vector mod p in a fixed power basis, at every prime of the set.
Note (cite-only, not used): Eigen-dir sobj names reference p=7851761, 7860581, 7863521, 7946821 (all ≡1 mod 980); No-Eigen rule — not consumed.

## 5. Per-cell CRT status
| Cell | residue p1 rel. ω_p | residue p2 rel. ω_p | residue p3 | Stamp |
|---|---|---|---|---|
| N36 ν=1 | unrecorded root (G4c') | — | missing | BLOCKED |
| N36 ν=4 | G4c' | — | missing | BLOCKED |
| N36 ν=9 | G4c' | — | missing | BLOCKED |
| N36 ν=14 | G4c' | — | missing | BLOCKED |
| N36 ν=16 | G4c' | — | missing | BLOCKED |
| N6 ν=1 | — | G4c' | missing | BLOCKED |
| N6 ν=9 | — | G4c' | missing | BLOCKED |
Named gap: **missing in-set mod-p runner for CF980 embedding** (must output residues at ζ₉₈₀↦ω_p for all three primes, both N36 and N6 cells at every prime). Cells remain FILLED-MODP; no exact companion table produced.

## 6. G4a OPEN
ℚ(ζ₄₉) containment not asserted; no ζ₄₉-only claim. True-H G4b OPEN; H_work is a working bound only.

## 7. Posture
## 7. Posture
PARTIAL; primes+ω_p PROVEN; product gate MET; residues BLOCKED; CERT-under-H_work 0/7. tip_touched NO. Kerr BLOCKED. No Eigen.
PARTIAL; primes+ω_p PROVEN; product gate MET; residues BLOCKED; CERT-under-H_work 0/7. tip_touched NO. Kerr BLOCKED. No Eigen.


## 8. Rec A
## 8. Rec A
Owner Write to authorize/build an in-set (non-Eigen) Sage/Python CF980 mod-p runner (install Sage on box or port solve36/N6 logic) that emits all 7 cells at p∈{7840981,1027606441,2147486741} relative to recorded ω_p, then CRT for CERT-under-H_work.
Owner Write to authorize/build an in-set (non-Eigen) Sage/Python CF980 mod-p runner (install Sage on box or port solve36/N6 logic) that emits all 7 cells at p∈{7840981,1027606441,2147486741} relative to recorded ω_p, then CRT for CERT-under-H_work.
