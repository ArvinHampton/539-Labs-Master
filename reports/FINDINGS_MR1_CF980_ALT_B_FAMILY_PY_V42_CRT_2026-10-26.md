# FINDINGS — MR1 CF980 Alt B: in-set exact V42 from family.py → 7×3×336 rel ω_p → CRT → CERT-under-H_work (2026-10-26 ~19:10 CDT America/Chicago)
Soft-SF Write-only. tip_touched NO (tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91). No Eigen file read, copied, run, or contacted. Kerr BLOCKED. Eight-only. Cat-A invent NONE. Proof standard: proof OR named gap.

## 1. STATUS: **MATCH (under Alt B redefinition) — 7/7 cells CERT-under-H_work**
Cells are those **re-defined by OW a71be23f item 2** (Written choice C6/C7); NOT identified with old Eigen-basis cells (G4c' stands). Path (a) remains **OPEN**.

## 2. Authority (live sha256, verified at start)
| Item | sha256 | |
|---|---|---|
| OWNER_WRITE Alt B | a71be23f5d1c15352f730bfb6067d2412c60cb971d4f81ccf087984a1e13c263 | MATCH |
| ASSIGN | c6fad66dab5e4babc0177d00ae4b491c2d206e4fc0de794694e1d38a3ab2530a | MATCH |
| Absorbed FINDINGS runner | e190135b635d536a8e1b1f764f96547a37f10d3b35d2efd3fee6c40d102ee9ac | MATCH |
| family.py | 07dabdaa1efbc52773f964547829925f4c7340a67cd0d2fc1bc92bb9ef686498 | MATCH (asserted in code) |
| Prime/ω_p table | 3ccf185a6710efb2714d36385adab4028d2d2942821cb1861fa9e52a7effb71a | MATCH (asserted) |
| tip pre = end | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | untouched |

## 3. Construction (Written choices doc 255b5a1079cf5bd9383015a2c6dcb3bebc40513bdb45389a40997aec7ed75de8)
- S,T from family.py taken symbolically: phases e(x), lcm of denominators | 140 ⇒ entries in Q(ζ140) ⊂ CF(980); 1/√35 via Gauss sum. Relations S⁴=I, (ST)³=I, S²T=TS² (note: (ST)³=S² FALSE).
- W=ker(S²−I) dim 72. Basis-free split: V36 = orbit of T-fixed line in W; V36+12 / V36+18 = orbits of e(35/140)/e(6/140) eigenspaces; V6 = W ∩ Ann(dual 36+12 + dual 36+18). Dims 72/36/48/54/66/6, invariance, pairing ranks (36,6), cross-annihilation: PASS at all 192 (p, a mod 140) points.
- Cell c(F,ν) = diagonal entry of ρ̄(S)=ρ(S)^{−T} on the ρ̄(T)=e(ν/140) line of V_F^*, = (w S⁻¹ v)/(w v). Choice-free: no basis, slot order, seed, RREF, cusp set or truncation enters.

## 4. Runner + CRT
`cf980_modp_runner_altb.py` (afabd41d…) extends base runner (ω_p re-verify, 336 embeddings, Vandermonde, CRT). Log 3e256605…: good-reduction PASS 144 points; **7056 = 7×3×336 residues emitted** → `CELL_RESIDUES_7x3x336_REL_OMEGA_ALTB_2026-10-26.csv` fbfa4695…. CRT `crt_cert_altb.py` 88ac1e00…; lifts `CRT_LIFT_SCALED70_CF980.csv` 338c9a12…; verify `verify_p4.py`/`verify_p4.log` 19e7399e….
∏p = 17303251105541478881544161 > 2·H_work (H_work=10^18).

| Cell | coords rational denom | 70·c max|coord| | nonzero coords (all j≡0 mod 7 ⇒ ∈Q(ζ140)) | p4 check | Stamp |
|---|---|---|---|---|---|
| N36 ν=1 | 1 | 0 (c=0) | 0 | ✓ | CERT-under-H_work |
| N36 ν=4 | 70 | 6 | 20 | ✓ | CERT-under-H_work |
| N36 ν=9 | 1 | 0 (c=0) | 0 | ✓ | CERT-under-H_work |
| N36 ν=14 | 70 | 5 | 21 | ✓ | CERT-under-H_work |
| N36 ν=16 | 70 | 8 | 17 | ✓ | CERT-under-H_work |
| N6 ν=1 | 35 | 24 | 23 | ✓ | CERT-under-H_work |
| N6 ν=9 | 35 | 24 | 23 | ✓ | CERT-under-H_work |
Independent verification prime p4=2147492621 (ω=9220085): 0 mismatches over 48×7=336 checks. Naive symmetric integer lift of c itself exceeds H_work (rational coords) — CERT stamped on 70·c (Written choice C11), heights ≤24.

## 5. Named gaps / caveats
- **Path (a) OPEN**: Owner/Author Soft-SF exact ρ̄(S),ρ̄(T) over CF(980) on V42 is still absent; not invented. Would allow identifying Alt-B cells with Card-1A Eigen cells.
- **G-ID**: equality of V36/V6 with v42.py float V_Eis/V_cusp only corroborated by spectra; not certified (not needed under Alt B).
- **G-IRR**: exact irreducibility of V36, V6 not proved (float commutant dim 1 cited); not used by cells.
- **G-EXACT**: a direct exact CF(140) run (`run_exact.py`) was stopped after ~30 min unfinished; CERT rests on CRT + p4 check, per CERT-under-H_work standard. run_exact.py also carries the stale (ST)³=S² check label.
- G4a, G4b OPEN; G4c' stands; H_work working bound only. No tip fold.

## 6. Rec A
Recommend Auditor MATCH on this FINDINGS + Written-choices doc. If Owner wants Alt-B cells tied to the original Card-1A/Eigen cells, recommend an Owner/Author Soft-SF supply for path (a) (exact ρ̄(S),ρ̄(T) over CF(980) plus basis spec). Optional: authorize a longer exact CF(140) run to close G-EXACT.
