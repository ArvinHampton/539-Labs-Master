# FINDINGS DRAFT for Auditor CONFIRM — t761u outer_* (2026-10-25 CDT)
Run: BRIDGE_C_35/deduce_t761u_outer_written. PREREG bdb2a87cce902ed58a6daa5eeeef742e8ccd9281fea3fdfe0324843f4575eca6; RESULTS/SUMS in SHA256SUMS + STREAM LOCK.
Claim to confirm: outer_even(m)=35m²+7m and outer_odd(m)=35m²+42m+49/4 (unit coeffs) are WRITTEN (e60cad9b… L16–22); DEDUCED check matches 1bab65c4… listed values and |ledger_exp| under AW-α. Draft+menu 39c9a9a6ba0441386508ada38563ce3c96b24c5271429d956963ab0b2d78f3a8 is AUTHOR-WRITTEN, NOT Cat A (rec O-α = O-1a+O-2a+O-3a+O-4a).
F-A PASS; F-nothing-CatA PASS; F-DED YES; F-δ≡0 NO; F-Bridge-YES NO; F-AW-X4 NO; residual-C OPEN.
Soft SF if: O-α read as ledger≡HD; any Cat A claimed; G-A3 auto-reopened; 4da09dec… revived; Ξ Fourier coeffs beyond outer_* formula values.
Checks requested: live shas per logs/verify_basis.txt; sha256sum -c SHA256SUMS; verbatim quotes vs HD source lines; rerun scripts/outer_check.py.
