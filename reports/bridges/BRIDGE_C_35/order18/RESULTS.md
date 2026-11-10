# order18 RESULTS
PREREG sha256 593a201649e7171e66bbe3f12d66d712ea6f94d5696d249ba66342497bd51121 (hashed before numerics; Maps RG3, RG4 hashed there).
| test | value | verdict (preregistered rule) |
|---|---|---|
| C0 control (A0 fixed-M) | 1.3e−15 | PASS |
| Map RG3: Π−(A2_lit − A2_lines) = 0 | 6.9e−14 | PASS |
| Map RG4: A2_lit = A2_lines + A2_corner | 7.8e−15 (x and −1/x sets) | PASS |
| T, w = −½ (primary, weight-½) | r = 0.210 | **FAIL** |
| T, w = −1 (weight-1 induced) | r = 0.058, κ ≈ 0.998 | FAIL |
| T, w = 0 | r = 0.503 | FAIL |
Zero guard: ‖A2c(−1/x)‖/‖A2_lit(−1/x)‖ = 0.997, so target is nonzero and T is discriminating. All outcomes match the written predictions.

## Category A content (argued in PREREG (a)–(d), confirmed numerically)
- A2(S^o) = 0: the P-odd sector has no t^0 coefficient after removing line terms (completion and wall corrections contribute nothing at t^0).
- A2 is fully explicit: A2 = A2_lines + Σ_r f_r[B̄1(ρ1/N)B̄1(ρ2/N) + ½B2(ρ1/N) + (7/4)B2(ρ2/N)].
- A2c := A2 − lines − completion = A2_corner is P-even and nonzero, and satisfies no pure fixed-M law at w ∈ {−½, −1, 0}.
RG3/RG4 are residual-internal maps with preregistered passes; they are not Residual↔Resonant bridges.
