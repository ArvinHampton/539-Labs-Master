# FINDINGS (Local): invent of g_s series and transformation law (order, level, multiplier, principal parts), s in {7,8,11}. PARTIAL. 2026-10-28 (CDT, America/Chicago)

Authority: OW 6081e5ac817cfb4e67c4562f59b3d1f32e718606183def768a828582450c1b00 (Local Write and pursue). tip Soft SF LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched NO. Kerr BLOCKED. Bridge PARTIAL READY NO. Path 8 is consistency-only. No agent messaged.

## 1. Cites (sha256 verified at Write)
- canon: FINDINGS_LOCAL_INVENT_GVI1_BETA_AS_ALPHA_PRINCIPAL_LEVEL_GS_2026-10-27.md 480f6d7298face1e9b15b51fd3d747a83b5c7384556721fcdae80994d4e1344d
- class: FINDINGS_LOCAL_WRITTEN_ASYMPTOTIC_GS_PATH4_CARD4_2026-10-26.md b19e12e6c313c98c40e28ce406ec08b3796fe8b0ad0f87a13365da1891c2d949
- deepen: FINDINGS_LOCAL_GVI1_PROOF_DEEPEN_P1_P5_CITE_GROUNDED_2026-10-27.md 40b5fd6726528ef6f3fcae5f482d337eb95035933f9aac32a1c4f138ca42a23b
- absent: FINDINGS_LOCAL_BETA_AS_ALPHA_LAND_OR_ABSENT_S7811_2026-10-28.md 1db3d05321863c7c991ad223fce23aa0a8cd98c629dbc6bf58d24a434c8fc295
- ow: OWNER_WRITE_LOCAL_ASYMPTOTICS_APPROVED_WRITE_PURSUE_2026-10-28.md 6081e5ac817cfb4e67c4562f59b3d1f32e718606183def768a828582450c1b00
- d1d2: OWNER_WRITE_D1_D2_DEFS_LOCKED_2026-10-26.md 6fba77178694a42e1556134323f1c67b1f79c83ca0b9ed4b071dedf200e5a4a2
- rank27: FINDINGS_PR2_VANISHING_RANK27_ZWEGERS_2026-10-26.md 55b3cf0bce4e5734154b9ed1fd6c3cb78d4c5ba8150bd856b78a272302523517

## 2. What is on disk
- Written: weight 1/2. g_s is the holomorphic part of a Zwegers completion ĝ_s (D1/D2). Growth class a(n) ~ A n^alpha e^(beta sqrt n) (b19e12e6).
- ABSENT: the explicit series of g_s, its level, multiplier, and principal parts. Rank27 says "no level/multiplier/shadow". The canon 480f6d describes g_s only by shape: sum q^(n^2)/(-q^s;q^s)_n type, with q^s scaling.
- No Owner cite exists for series, order, or level. Everything in Sections 3 to 5 is invented pending mathematical proof.

## 3. Invented series (invented pending mathematical proof; project-defined choice)
g_s(q) := f(q^s) = sum_(n>=0) q^(s n^2) / (-q^s; q^s)_n^2,
where f is Ramanujan's third-order mock theta function. This is the minimal object that matches the canon's shape and its q^s scaling. Whether it is the project's intended g_s is not Written.

## 4. Transformation law (literature-grounded given the Section 3 invent)
- Bringmann, K. and Ono, K., "The f(q) mock theta function conjecture and partition ranks", Invent. Math. 165 (2006) 243-266: M_f(z) = q^(-1) f(q^24) + R(24z) is a weight-1/2 harmonic Maass form on Gamma0(144) with Nebentypus chi_12, where R is a nonholomorphic period integral of a weight-3/2 theta series (the shadow).
- Zwegers, S., "Mock Theta Functions", PhD thesis, Utrecht 2002, Ch. 3: q^(-1/24) f(q) is a component of a vector-valued weight-1/2 harmonic Maass form on SL2(Z) with an explicit eta-type multiplier.
- Level raising (standard V_s / z -> s z): M_f(s z) = q^(-s) f(q^(24 s)) + R(24 s z) transforms with weight 1/2 on Gamma0(144 s), Nebentypus chi_12 (times the quadratic character from the dilation, chi_s; the exact character twist is NOT verified here and is invented pending mathematical proof).
- So, in the q^24 normalization: level N_s = 144 s, multiplier chi_12 (twist pending), principal part q^(-s) at infinity with leading coefficient 1, polar order 1 term, Delta_s = s/24 in the original q variable.
- Principal parts at cusps other than infinity: ABSENT. Bringmann-Ono place the full principal-part data on cusps of Gamma0(144). Transporting it under z -> s z to every cusp of Gamma0(144 s) was not done. Not where-feasible this turn.

## 5. Consequent asymptotics (derived; inherits the Section 3 invent)
Dragonette (1952) and Andrews (1966): the coefficients of f satisfy alpha_f(m) ~ (-1)^(m-1) e^(pi sqrt(m/6)) / (2 sqrt m). Coefficients of g_s live only on n = s m, so |a_s(n)| ~ (sqrt s / 2) n^(-1/2) e^(pi sqrt(n/(6 s))):
| s | level | multiplier | principal part | beta_s = pi/sqrt(6s) | alpha | A_s = sqrt(s)/2 |
|---|---|---|---|---|---|---|
| 7 | Gamma0(1008) | chi_12 (Nebentypus) | q^(-7) at infinity, coefficient 1 (variable q^24); Delta_s=7/24 | 0.484758 | -1/2 | 1.322876 |
| 8 | Gamma0(1152) | chi_12 (Nebentypus) | q^(-8) at infinity, coefficient 1 (variable q^24); Delta_s=8/24 | 0.453450 | -1/2 | 1.414214 |
| 11 | Gamma0(1584) | chi_12 (Nebentypus) | q^(-11) at infinity, coefficient 1 (variable q^24); Delta_s=11/24 | 0.386703 | -1/2 | 1.658312 |
All entries are invented pending mathematical proof, because they inherit the Section 3 choice of series. The asymptotic step itself is a theorem (Dragonette/Andrews), not an invent.

## 6. Conflict with canon 480f6d (flag; not decided here)
The canon invented N_s = 4s and Delta = 1/24, which gives beta_s = pi/(2 sqrt6 s) and A_s = 1/sqrt(8 s). Under g_s = f(q^s) these do not hold: Delta scales to s/24, the level is 144 s, and c_min scales from 2 to 2s, which gives beta_s = pi/sqrt(6 s). The deepen file 40b5fd67 already showed that c_min = N is false on the f template. This package is internally consistent and literature-anchored. The canon's is not. Selection is for Owner/Auditor.

## 7. Status
- Invented (labeled): the series, the level 144 s, the multiplier chi_12, the principal part at infinity (order 1, coefficient 1, Delta_s = s/24), and beta_s / A_s / alpha.
- Still ABSENT: the character twist from dilation, principal parts at the other cusps, the Owner identification of g_s, and the Owner cite for order and level.
- beta_s / A_s / alpha: computable as invented values, not Written numbers. They can be Written only after the Owner or a cite confirms g_s = f(q^s), or supplies the true series. alpha = -1/2 holds for any weight-1/2 choice.
- PARTIAL: a full transform law is not where-feasible, because of the other cusps and the twist.

## 8. Non-effects
No tip fold. No Kerr. No C1 evaluation. No READY or Bridge YES. Prior ABSENT FINDINGS 1db3d053 is not rewritten.
