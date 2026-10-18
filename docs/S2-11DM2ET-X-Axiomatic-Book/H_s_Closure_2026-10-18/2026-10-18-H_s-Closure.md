> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** The x ≠ 0 fits at x = 1/2 (s = 7, 9, 10) and x = 1/3 (s = 7, 10) are unstable and are not quoted on Master. Category convention for Master (rev. 4): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Where this report labels a floating result Cat A, read it as Cat B (C12, C13). Theorem names: Theorem G = Lewis–Zagier period theorem (rev. 3 meaning); the g_s asymptotics = Theorem G_s; the zero-set theorem = Theorem D. Erratum: ERRATUM_Consolidated_CrossReview_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev4_2026-10-18/.

# H_s — Closure (Path B follow-up)

Date: 2026-10-18 (CDT). Local only; nothing pushed. Builds on `2026-10-18-H_s-Closed-Forms.md`.
Labels: **Cat A** = exact or proved. "A modulo F1" is the prior report's convention: the result is proved given the cited 2-D Euler–Maclaurin input F1. **Cat B** = numerical or conjectural. No TPC/RH claims.

Notation: g := gcd(24, s−8), Δ := (s−2)(7s−32). The expansion is H_s(e^{−t}) at x = 0, H_s ~ Σ_r H_r t^r.

Scripts and outputs: `2026-10-18-H_s-Closure/`
- `H_em2.py` → `H_generic2.pkl`: symbolic 2-D Euler–Maclaurin. Uses sinh-expansion orders j = 1, 3, 5, 7 and Bernoulli orders p ≤ 6.
- `H_closed2.py` → `H_closed2.pkl`, `H_closed2.txt`: closed forms, written as rational part + (rational)·√Δ.
- `H_validate2.py` → `H_validate2.txt` and `H_validate3.py` → `H_validate3.txt`: validation.
- `H_x.py` → `H_x.txt`: x ≠ 0 fits.
- `H_numeric.py`: copy of the earlier numeric engine.

## 1. Summary

| Item | Result | Status |
|---|---|---|
| H_{−1/2}, H_{1/2} re-derived by the extended code | Identical to the prior closed forms | A modulo F1 (consistency) |
| **H_{3/2}** closed in (s, g) | §2 | A modulo F1. Numerics confirm at 9 values of s (B) |
| **H_{5/2}** closed in (s, g) | §2 | A modulo F1. Numerics confirm at s = 6 and s = 8 only (B) |
| Integer orders t⁰, t¹, t² | Edge and area parts vanish identically. Corner terms were not computed in this extension; the prior report's B7 covers them. | A modulo F1 (edge/area). Corner terms at t² are not re-derived here. |
| s = 5 | Every coefficient vanishes (H_5 ≡ 0) | A modulo F1 |
| H_{−1}(x) = 0 for every rational x | §3 | A modulo F1 |
| x = 1/2 and x = 1/3, s even or 3 \| s: leading orders | Stable fits (table §3) | B |
| x ≠ 0 closed forms | **Not obtained** | Open |
| t^{7/2} and beyond | Not computed: needs j = 9 and p ≤ 8 | Open (mechanical) |

## 2. Closed forms at x = 0

H_r = √(2πs)·[R_r(s) + S_r(s,g)·√Δ]. The full expressions are in `H_closed2.txt`.

**t^{−1/2}:** R = −1/(2(s−2)), S = 1/(2(s−2)(7s−32)).

**t^{1/2}:** R = −(s−4)(3s−2)/(48(s−2)²), S = (2g²s − 4g² + s³ − 44s² + 192s)/(48(s−2)²(7s−32)²).

**t^{3/2}:**
- R = −(15s⁴ − 76s³ + 108s² + 96s − 128)/(3840(s−2)³)
- S = (−8g⁴s² + 32g⁴s − 32g⁴ + 20g²s⁴ − 360g²s³ + 1920g²s² − 2560g²s + 3s⁶ − 152s⁵ + 3872s⁴ − 28160s³ + 61440s²)/(3840(s−2)³(7s−32)³)

**t^{5/2}:**
- R = −(s−4)(105s⁵ − 730s⁴ + 2732s³ − 5208s² + 5696s − 2560)/(645120(s−2)⁴)
- S = P₅(s,g)/(645120(s−2)⁴(7s−32)⁴), where P₅ has g-degree 6 (in `H_closed2.txt`).

Structural observations:
- The denominator pattern is (s−2)^{r+3/2}(7s−32)^{r+3/2} at order t^r.
- g enters only through even powers g^{2i}, with i ≤ r + 1/2.
- At s = 5 the forms reduce to 0, consistent with H_5 ≡ 0.

**Derivation.** Same bookkeeping as the prior H_em.py, with scaling X, Y ~ t^{−1/2}:
- area term of order j → t^{j/2−1};
- edge term (j,p) → t^{(j+p−2)/2};
- corner terms → integer powers only.

So t^{5/2} needs j + p = 7, i.e. (1,6), (3,4), (5,2), plus the j = 7 area term. All of these are included.

An indexing bug was found and fixed: the angular-weight map must be −1 → ANG1, 1 → ANG3, 3 → ANG5, 5 → ANG7. A √Δ normal form was added.

**Validation:**
- Generic Bernoulli-sum identities for p ≤ 6 hold for s = 5..80, 99, 100, 151, 223, 300, with no mismatch (`H_validate2.txt`).
- h_{3/2} agrees with the earlier small-t numerics to 3–4 digits at s = 6, 7, 9, 11, 13, 20, 25, 41 (`H_validate3.txt`).
- At s = 8, Richardson-type ratios converge toward h_{3/2} = −0.957344 (−0.9551 at t = 0.00125) and h_{5/2} = 1.81439 (1.8049).
- At s = 6, R2(t) settles at −0.02456 against h_{5/2} = −0.024492.
- At s = 7, 9, 11, 13, 20 the t^{5/2} numerics are dominated by oscillation at the t-values used, so they give no check there.

## 3. x ≠ 0

**H_{−1}(x) = 0 for all rational x (A modulo F1).** The leading area term is the residue-class average of e(xQ) over the cone. Under (n,k) → −(n,k), the averages for e(xQ₊) and e(xQ₋) coincide, so they cancel in H.

**Fits (Cat B).** These are least-squares fits in t^{−1}, t^{−1/2}, …. The stability column compares against dropping the t² term and using fewer points.

| x | s | t^{−1} | t^{−1/2} | t⁰ | t^{1/2} | stable? |
|---|---|---|---|---|---|---|
| 1/2 | 6 | 0 | 0 | 0 | −0.767481 | yes (8e−5) |
| 1/2 | 8 | 0 | 0 | −2e−5 | −0.8855 | yes |
| 1/2 | 12 | 0 | −2e−5 | 2e−3 | −1.194 | marginal |
| 1/3 | 6 | 0 | −0.162864i | ≈0 | −0.9585 + 0.3520i | yes |
| 1/3 | 9 | 0 | −0.162751i | ≈0 | −1.2506 + 0.4604i | yes |
| 1/3 | 12 | 0 | −0.140740i | ≈0 | −1.4265 + 0.5206i | yes |
| 1/3 | 8 | 0 | −0.3691 − 0.1279i | −0.009 | — | marginal |
| 1/2 | 7, 9, 10 | not quoted | | | | **unstable**: fits change by more than the value when the t² term is dropped (see `H_x.txt` stability column); not fixed |
| 1/3 | 7, 10 | not quoted | | | | **unstable** for the same reason; not fixed |

Observations (Cat B):
- At x = 1/2 with s even, the t^{−1/2} and t⁰ coefficients appear to vanish, and the first non-zero order is t^{1/2}.
- At x = 1/3 with 3 | s, t^{−1/2} is purely imaginary. Its values at s = 6 and s = 9 agree to 4 digits (−0.1629i), while s = 12 gives −0.1407i.

No closed form was identified. A route to one is to redo `H_em2.py` with e(xQ) inserted, so that the residue-class averages over (Z/N)² with N = denominator(x)·(lattice level) become explicit Gauss-sum weights. This was not done (open).

## 4. Open items
1. t^{7/2} and beyond at x = 0. This is mechanical: extend JS to j ≤ 9 and Pm to 8.
2. Corner contributions at integer orders: re-derive them within this extension. The prior B7 claims all integer orders vanish.
3. Exact x ≠ 0 expansion via Gauss-sum-weighted Euler–Maclaurin.
4. Stable numerics at s = 7, 9, 10 (x = 1/2) and s = 7, 10 (x = 1/3). Following Cross-Review §5.7, these values are not quoted anywhere in this report. `H_x.txt` still contains the raw unstable fits, flagged by its stability column.
