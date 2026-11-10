# EH_K11N_HUNT — written k11(N) / flux→k hunt (2026-10-24 22:16 CDT (mtime; was ~22:15); read-only outside this dir; no PREREG; nothing invented)

## Verdict: ABSENT as a closed-form k11(N). FOUND (WRITTEN-CHAT only; CHAT≠paper, not Cat A; convention-unfixed): flux→k *recipe* with ingredients and numeric outputs only.

## FOUND candidates (quotes exact)
1. reports/s_family_paths/A22_grok_export_search/chats/cd250095-2abb-4dee-b86a-e4481020d5ef.txt:604-610
   "Name the fibre \(S^6\) and the four-cycle the equatorial \(S^4\). Keep the constant-\(B\) solution. Put \(N=4880\) on that \(S^4\) and use \(16\pi G_{11}=(2\pi)^8\ell_{11}^9\). Then k\,\ell_{11}=0.02531,\qquad \frac{1}{k}=39.50\,\ell_{11}" ; "The six-sphere radius is \(31.23\,\ell_{11}\)."
   :612 "Change the flux unit to \((2\pi\ell_{11})^3 N\) and the numerical prefactor moves." (flux-unit convention NOT fixed in writing)
2. same file :579 "\Phi=8\pi G_{11}\,G_{ABCD}G^{ABCD}=1728\,k^2" ; :584 "\(4880\) enters only as \(N^2\) in the four-form square. That square still contains the hat volume of the four-cycle and the fibre size \(e^B\). Those are not fixed by the Einstein equation."
3. reports/s_family_paths/A22_grok_export_search/chats/a01dcbad-ac7b-400e-bca4-1e7b6a7f2336.txt (block ~:83-89)
   "The written law is 16 pi G_11 = (2 pi)^8 ell_11^9. That defines ell_11 from G_11."
   "T_2 ell_11^3 = 1/(4 pi^2) = 0.025330 is the membrane convention T_2 = 1 / ((2 pi)^2 ell_11^3). k ell_11 = 0.025314 is 4880 flux units on an equatorial four-sphere plus the lock Phi = 1728 k^2. Same package. They miss by three flux units. Exact match would need N = 4876.82."
   (~:219 repeats: "Flux 4880 on the equatorial four-sphere becomes k ell_11 = 0.02531.")
4. EH1 reports/self-audit/zenodo/txt/23010998_*Appendix_2026-09-28.txt:47-57 (garbled; quote only, layout-split superscripts):
   "4. Flux" / "N = 4880 on equatorial S4 of unit S6. 16π G11 = (2π)8 … 9 … 11" / "k … = 0.02531377 … 11 … (EH-k)" / "T2 … 3 … = 0.02533030 … 11 … (EH-T2)"
   Legible reading of fragments only: 16πG11=(2π)^8 ℓ11^9; kℓ11=0.02531377; T2ℓ11^3=0.02533030. No k(N) expression in the text layer.

## Written items requested
- 16πG11=(2π)^8 ℓ11^9: WRITTEN (EH1:48 garbled-legible; cd250095:604; a01dcbad).
- T²₁₁ definition: WRITTEN (a01dcbad) "T_2 = 1 / ((2 pi)^2 ell_11^3)" ⇒ T2ℓ11^3=1/(4π²).
- N_flux→k link: WRITTEN as recipe (S^6 fibre, equatorial S^4, constant B, Φ=1728k², 16πG11 law), numeric only.

## Inconsistencies noted (not resolved)
- Required-N: EH1 "N=4870.45 (miss 9.55)" vs a01dcbad "N = 4876.82 … three flux units"; k: 0.02531377 (EH1) vs 0.025314 (a01dcbad). Different conventions/rounding — not determinable from written text.
- Flux-unit normalisation (G-flux quantum, e.g. (2πℓ11)^3 vs other) explicitly left open (cd250095:612); Vol(S^4)/e^B dependence stated (:584) but no formula.

## ABSENT — checked
Closed-form k11(N) / Φ(N) / flux quantization integral: not in EH1 txt (text layer only; PDF not re-OCR'd), cd250095, a01dcbad, Execute_Three_Advancement_Paths_2026-09-28.md (no flux/4880 hits), Lean EinsteinHampton*.lean (Φ free real, per LEAN_L1L7_ASSUMPTIONS), oct17-master, theorems, grok-chats, grok_export (rg 4880/4870/4876/0.0253/equatorial/(2π)^8/T_2).

**Status (auditor relabel 2026-10-24 22:16 CDT):** Φ=8πG11·G² and the flux→k recipe are WRITTEN-CHAT only (CHAT≠paper; not Cat A, not paper). kℓ11=0.02531 and the ~3-unit (or 9.55-unit) miss are convention-unfixed; k(N) OPEN, not derived. Physicist GC-1/GC-2 acceptance = bookkeeping + CHAT-labeled tests only; does NOT clear NL1 or any paper gate. NL1 OPEN.
