# AUTHOR-CANDIDATE FILLED (class C AUTHORIZED compute; NOT Cat A until Arvin ACCEPT) — G-A3 h-table
Fills schema v2 sha 8d247feb4f1b644dfbaf1d28237eaddfe9ba45c82d40464a2290d4721b0f8051 (identity preserved; schema file unaltered). Authority t712s4471; defaults t713s4497; ψ t713s4484. PREREG 49bd0b24fa2bd488a25d93293b47ec02d114b8c1d77d3bf7973234a8119e425b.

## Table H (N_trunc=106, regenerated Ξ, main variant)
| x | W_7 x | ψ(x) | Re h(x) | Im h(x) | Re h(W_7x) | Im h(W_7x) | residual_slash(x) | Re δ(x) | Im δ(x) | abs δ(x) | tol | Cat | source sha |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1/7 | -1 | +0.0000565214-0.0011017034i | +1.5705684148 | -0.1473779266 | -2.2075625123 | -2.2172979497 | 19.801180 | +45.282911 | +43.757738 | 62.970482 | 1.13e-02 | C (NOT Cat A) | data 55b1b16a… |
| 3/7 | -1/3 | +0.0011075781-0.0089974728i | -1.2783999093 | +1.4284210943 | +2.9036429210 | -0.6561653344 | 1.824831 | -6.577058 | +2.625812 | 7.081848 | 1.72e-03 | C (NOT Cat A) | data 55b1b16a… |
| 5/7 | -1/5 | +0.0035493172-0.0220901122i | -0.4074907224 | +1.1216645699 | -0.6252254324 | +0.2761816679 | 9.241749 | +5.370686 | -1.430737 | 5.557992 | 1.10e-03 | C (NOT Cat A) | data 55b1b16a… |
| 1 | -1/7 | +0.0068839938-0.0382597122i | -2.2616699162 | -2.2714053536 | -0.1457399494 | +1.5720465253 | 20.902216 | +0.784618 | -35.130661 | 35.139422 | 6.28e-03 | C (NOT Cat A) | data 55b1b16a… |

ψ(W_7x) (psi_minus, |x| factor): -1: +0.0068839938+0.0382597122i; -1/3: +0.0005873917+0.0056523668i; -1/5: +0.0001473670+0.0021281899i; -1/7: +0.0000565214+0.0011017034i

## Provenance block
- Ξ: regenerated from Written product form (P4,P7; 552541cf L24 Θ_{3/2}=Σ(n+a)q^{(n+a)²}, n≥0; q^{outer} unit coeff e60cad9b L16–22). N_trunc=106. Coefficient table data/Xi_regen_N106.tsv sha 35b186f9df70c2bf247432edcef946e5f66f0ddf1bbca2f4454a30b210707197 (9 terms: 24.5,32.5,42.5,54.5,68.5,84.5,91,102.5,106 with c=k). Ledger Ξ 7dbd63af… NOT used.
- Flagged: Written partials 43/58/67 NOT reproduced by regeneration (carried in variant V-P with c=1, data JSON 'partials'); Written entry 78:6 (unflagged) also NOT reproduced (would need n=−1 at m=1) — SOFT FLAG.
- Path i∞→x vertical; branch principal; closed form I_ν(x)=−e^{iπ/4}e(νx)/√(2ν); mpmath quadrature check max 2.0e-9 (logs/quad_check.log).
- ψ: fastkappa.py 70f605a43132c18f5eccd969e8527333ea410dd39a1037a1cca1faf3ecafe832 (x>0), psi_minus per neg_side2.py 10d86dc4e63fd35ece0157298aae2e372181078d9a75ee4f189f8383a5eff5ee logic (x<0); def sha 1be7f7d1… (exact Bernoulli sums, floor ~1e-13).
- Scripts: scripts/ga3_fill.py 24fd6e52af0479adb6e4c0b33956c9687fbca41e89bc3aa80f37ae453180989a; scripts/quad_check.py 977b3497362e15a6b8b5b027f3553b2cdda4fdaac0032f7ca3b793f5b9132d1a. Data: ga3_fill_N106.json 55b1b16ab28f643784fa0a740fe17f2d0f522403b1527aefd36e017072c32cdb; N150 1b91dce7383b6a982c2b626e2738033e0a51f32dc776e64c24fa660634097b2c.
- Error: numerical ≤1e-12 (h); slash rounding σ propagated into tol. Truncation: Ξ series NOT convergent on ℝ; N=150 shifts h by O(1) (e.g. h(1/7) 1.57−0.15i → 0.48−1.52i) ⇒ values are N_trunc=106-convention quantities, no convergent tail bound exists (SOFT).
- residual_slash: 7368b855 §2 coeffs (10.6923,0.2160,2.7618,−7.5316); selectors 437d4571…/3d502756….
- Source class (C) AUTHORIZED; NOT Cat A until Arvin ACCEPT.
