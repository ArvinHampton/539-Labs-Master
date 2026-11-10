# RESIDUAL_IDENTITY_HUNT — Bridge Series C (LOCAL) — 2026-10-24 (CDT)
Search-and-extract only. No proof, closed form, or δ≡0 claim authored. CORE_FREEZE: locked files read-only. Local map only; nonlocal (Φ_orth etc.) excluded.
Paths: HD = reports/heavy-daily/ ; B = reports/bridges/BRIDGE_C_35/ . sha = sha256 prefix (12).

## 1. Executive identification (current candidate)
Per Arvin t625u/t630u and pin B/pins/RESIDUAL_LAW_C_CANDIDATE_W7_2026-10-24.md (sha b9a214385ef8…3f90), the current residual-identity candidate for C is the Fricke/W7 cocycle
  δ_W7 h(x) = h(x) − residual_slash(x)·h(W7(x)),  W7(x) = −1/(7x),
with h the residual period function (weight 1/2; formal Eichler integral of shadow Ξ), residual_slash recovered from the continuous span of residual periods of C_axis, the modular completion of Θ_third, and the Eichler integral of the weight-3/2 shadow Ξ. Sample vanishing is asserted at x = 1/7, 3/7, 5/7, 1. The identity δ_W7 h ≡ 0 for all x is NOT proved. Residual law for C: **OPEN**. Zwegers applies to H_s, not C.

## 2. Component table
| Component | Written definition / status | Source + sha | Status |
|---|---|---|---|
| Cocycle statement δ_W7 h | as §1 | B/pins/RESIDUAL_LAW_C_CANDIDATE_W7… b9a214385ef8; B/order76/RESULTS.md 49d13fd3693a (RG76a verbatim ingest) | FOUND (candidate, open) |
| W7 action | W7(x) = −1/(7x) ("packaging-type Fricke"); images of samples: −1, −1/3, −0.2, −1/7 | HD/968c9830ea15-… 8f2f43b56d9d | FOUND |
| h (period function) | weight-1/2 formal residual Eichler integral of Ξ; holomorphic projection recovers C | HD/26ce36226487-PUSH_LOG…Residual_Period_Candidate a7e4d5c4814f | FOUND (definition); numeric h values ABSENT |
| h_residual^{high} | higher-fidelity Eichler integral using full Ξ tables; "exact functional form of the slash prefactor is not recovered from the truncated integral alone" | HD/3957bc442bd8-Construct_Higher_Fidelity… 1bab65c422e4 | FOUND (construction recipe); numbers ABSENT |
| residual_slash | Recovery description only (pin). Historical Pack+(S) form: |7x|^{-1/2}·(a+bt+ct²+d/(1+t²)), t=7x−3, a≈10.6923,b≈0.2160,c≈2.7618,d≈−7.5316; sample values ≈19.8012, 1.8248, 9.2417, 20.9022 | pin b9a214385ef8; HD/968c9830ea15 8f2f43b56d9d (SUPERSEDED tree) | Pin: recovery only. Fit form: HISTORICAL/non-binding (an empirical 4-parameter fit to 4 points, not a derived formula) |
| C decomposition | C = C_axis + C_third; notation lock C := P_orth − H_s | HD/3957bc442bd8 1bab65c422e4; HD/5a9b1cf8b366 736cfd72a83d | FOUND |
| C_axis periods | named as recovery input; no explicit period table found | pin; 968c | ABSENT (numerics) |
| Θ_third completion | "locked Category A rewrite" / completed-square rewrite + iterated partial thetas; continuous extension via error-function completions "expected" | HD/26ce36226487; HD/3957bc442bd8 | FOUND (verbal); explicit completion ABSENT |
| Ξ shadow (wt 3/2) | Ξ = Σ outer_even(m)Θ_{3/2}(·;7m) + Σ outer_odd(m)Θ_{3/2}(·;7m+7/2); outer disc-35 even 42,154,336,…; odd 12.25,89.25,…; coefficient table to deg ≤120 | HD/545edf7dd645 f2f9d897cc07; HD/5a9b1cf8b366 736cfd72a83d; B/order57/WRITTEN_CANDIDATES.md 36c680a196f6 | FOUND (series + table); Ξ HOLD / outer_* Written for G1 ABSENT |
| Sample vanishing numerics | Pin asserts machine-precision vanishing; 968c claims max |δ|/|h| ~1e-17 — no table of h(x), h(W7x), δ values; no script | pin; 968c (superseded) ; HD/2753862a7f88 098f47a5caaf: "h_residual^{high} at samples + Fricke images not yet tabulated" | ABSENT (no reproducible data) |
| Magnitude check | residual_factor recovers |C| sample magnitude ratios (19.8012, 3.1607, 20.6652, 55.3021) — magnitude only, not complex cocycle | HD/2753862a7f88 098f47a5caaf | FOUND (magnitude only) |
| Gauss-sum W7 phase probe | G(x)=Gauss average of Q=n²+7nk+7k(k+1)/2 (P_7 form, not C); after removing e(7(x−W7x)/20) only 4 phases {0.15,0.35,0.65,0.85} over 120 pairs | HD/2026-10-18-C_third-modularity/w7_explain.py 2261fdd2bf45, .txt 8b440b0c4ebd | FOUND, but NEAR-MISS (P_7 quadratic form, not δ_W7 h for C) |
| P_s = (−q^s;q^s)_∞ g_s | definitional identity, double sum q^{Q_s(n,k)} | HD/ad40955-… d6ac16c350de | NEAR-MISS (not the C residual law) |
| Global identity δ≡0 ∀x | — | pin; order76 RG76c; Arvin t625u/t630u | OPEN |

## 3. Strongest quotes
- Pin: "The exact identity that would make δ_W7 h(x) = 0 for all x (not merely the sample points) is **not yet proved**. That is the open residual law for C."
- Pin: "Zwegers completion applies to the cone series H_s, **not** to C itself."
- order76 RG76d: "Corpus … contains no written residual_slash values, period spans, Θ_third completion or Ξ Eichler numerics; only recovery description."
- 2753862a7f88: "Residual law for Bridge Series C remains open at quantitative continuous complex Fricke verification … (explicit numerical residual values of h_residual^{high} at samples + Fricke images not yet tabulated from residual series of Xi)."
- 3957bc442bd8: "the residual exact residual functional form of the residual slash prefactor is not recovered from the residual truncated integral alone."
- 545edf7dd645: "samples qualitative; exact slash prefactor unrecovered … Residual law for C remains open."

## 4. OPEN — missing for Bridge YES
1. Proof of δ_W7 h ≡ 0 for all x (the residual law itself).
2. Derived (not fitted) residual_slash formula.
3. Tabulated complex h(x), h(W7 x), δ at the four samples + script (reproducible sample check).
4. Explicit C_axis period span and explicit Θ_third modular completion.
5. outer_* Written for G1; Ξ HOLD; GATE 640da80d… binding.
6. T1–T4 (order76 RG76f).

## 5. Do-not-mix (superseded / non-binding)
- HD/968c9830ea15-Residual_Law_for_Bridge_Series_C_Closed_Under_Pack_S_Sample_Points_2026-08-25.md — claims "closed residual-discretely … at the residual sample points". SUPERSEDED/NON-BINDING (Auditor SF-W7-3; Arvin t625u/t630u leave law OPEN). Its residual_slash coefficients are a 4-param fit to 4 sample magnitudes.
- oct17-master BK/PUSH_LOG_2026-08-25_Residual_Law_C_Closure.md, Continue_Closure_Residual_Slash_Identity_C_2026-08-23.md, PUSH_LOG_2026-08-23_Pursue_All_C_Closure.md, PUSH_LOG_2026-08-23_Continue_Closure_Slash_Identity.md — 2026-08 Closure trees, non-binding.
- Zwegers / H_s completions (HD/2026-10-18-H_s-Closure*, H_s-Closed-Forms) — apply to H_s, not C.
- Pre-09-01 Zwegers orthant completion (Transformation_Law_CLOSED_2026-08-20) — WITHDRAWN (order57).
- w7_explain Gauss-sum phases (P_7 form) and P_s Euler identity (ad40955) — not the C residual law.
- Nonlocal Φ_orth (v12 §37.5) — excluded (local only).
- RESIDUAL_CORE_FREEZE-fa66317.md (sha 1f8941d58a7d) — governs Cat A freeze; contains no C residual identity.

## 6. RG76d feasibility
Only Cat A-adjacent numbers found: residual_slash sample values (968c, superseded) and |C| magnitude ratios (2753862). No written h / h(W7x) values exist, so an RG76d sample check of δ cannot be run without inventing h numerics. RG76d remains ABSENT-blocked.
