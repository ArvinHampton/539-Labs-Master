# AUTHOR-CANDIDATE (NOT Cat A until Arvin ACCEPT) — G-A3 h-table schema v2 (values EMPTY)
Extends ACCEPTed empty schema P-B3 5f60d40f… (does not replace it). No numeric cells by rule. Cite: 7368b855 L44 (W_7 images), L46 (δ def), L50 (values not tabulated), L56 (method: truncated Ξ series + incomplete-gamma Eichler); be1faa52 L43–44 (h^{high} = ψ(x)/√i − ∫ Ξ_N(w)(w−x)^{−1/2} dw; term-by-term incomplete-gamma); 736cfd72 L48–52.

## Table H (per sample point)
| x | W_7 x | ψ(x) | Re h(x) | Im h(x) | Re h(W_7x) | Im h(W_7x) | residual_slash(x) [in-family, S-B1′/S-B1, 437d4571…] | Re δ(x) | Im δ(x) | |δ(x)| | tol | Cat | source sha |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1/7 | −1 | | | | | | | | | | | | |
| 3/7 | −1/3 | | | | | | | | | | | | |
| 5/7 | −1/5 | | | | | | | | | | | | |
| 1 | −1/7 | | | | | | | | | | | | |

## Provenance block (required for any filled cell)
- Ξ truncation N_trunc; coefficient table sha (ledger Ξ 7dbd63af… or Written successor); path of integration (endpoints, branch of (w−x)^{−1/2}); ψ(x) definition sha; script sha; data sha; error bound vs N_trunc.
- Source class: (W) Written Cat A table by Arvin | (C) computation explicitly AUTHORIZED by Arvin (lifts "new table" ban for this table only) — either requires ACCEPT before Cat A.

## Optional denser grid (7368b855 L56) — slot only; rows TBD by author.

## Force criteria (pre-stated; not evaluated)
- F1: |δ(x)| ≤ tol at all 4 points AND at W_7 images (consistency) ⇒ RG76d PASS-candidate at samples.
- F2: δ≡0 identically needs more than samples (identity proof or dense grid + author rule); samples alone ⇒ δ≡0 NOT forced.
- F3: nonzero controlled defect ⇒ obstruction refined (7368b855 L56), Bridge stays PARTIAL.
