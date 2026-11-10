# FINDINGS: PP confirmation of NL Erratum 21 (078b0b32…) against PP 3fa2e067 (2122) and 2252cafc (2123); and the pp_a2_flux_fix push-forward false negative
2026-11-09, 21:41 CST (America/Chicago). Auditor: Professor Proof (PP). Pure math. Labels PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only results are CONDITIONAL; a citation alone never proves; a stated premise is graded as an implication. **Nothing adopted. Junction: UNSOLVED.** No CERT, nothing sent, no Gemini. New file only.
Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 at start and at write time (unchanged).

## Part 1. Erratum 21 (2135): **FAITHFUL**

### 1.0 Integrity
- NL_ERRATUM21_ACCEPT_PP_3fa2e067_2252cafc_2026-11-09_2135.md: sha 078b0b322835bb3bca70f75d22b09ed2d1de8eb67151b6000bc389d6b89b216b = sidecar ✓. The md was written at 21:36:23 and its sidecar at 21:37:45 (post-write integrity sidecar).
- Sources quoted with full shas: 3fa2e067… (2122) and 2252cafc… (2123) ✓. All nine targets are listed and none was edited.
- NL scripts in /workspace/nl-e21-2132/: each .py sidecar was written within 4 ms of its .py and before its log, and each .log sidecar after its run, as disclosed ✓. PP reran all three from their own paths, with output to /workspace/pp-rerun-e21/: **exit 0, byte-identical** in every case.
| script | .py sha | log sha (NL = PP rerun) |
|---|---|---|
| e21_checks_2026-11-09_2132 | 6067be4c… | 964cb5770b0595cba0c62bcf6e027df70693f3608627a0b0c2654753966e43bc ✓ |
| e21_z1_check_exponents_2026-11-09_2132 | a3847a2c… | 434a2e727b5a370e6ce200ebaf31c194d77fc5f8540f464aa57d3250a69572e1 ✓ |
| e21_a2_identities_2026-11-09_2132 | a1ecf721… | a2bbd5463056275f0192d8b2f3b4d5f9baf11f5a9ec8eff1d3f179b0483fa8cb ✓ |
The logs confirm the following:
- rank P₂ = 1;
- c·64π²/T_M5 = u;
- the radial integral is −2;
- the 2D mpmath quadrature gives −2.0, a float cross-check only;
- the exponents are μL ∈ {−2, 6}, {2} (double root) and {0, 4};
- tr M + 12k_x = 0;
- c = 2·2^{1/3}g = 2^{4/3}g;
- the slaving is (1/5, 13/30);
- U_CLP = gU_CGR;
- det[μ|J] = −sin³α sinβ cosβ;
- Δ and U depend on s only;
- the integral is −2 for every k = X₀/X₁.
z1_check.py (nl-e20-z1) is untouched (313d2be8…).

### 1.1 Fix-by-fix
| PP fix | E21 | faithful? |
|---|---|---|
| F9-1 antilinear, not antiunitary; drop T1⁻¹ | E21-1 | ✓ |
| T2-1 R2-Y16 → COND | E21-2; 2026 revised 2/6/1/0 | ✓ |
| T2-2 R2-C4 unlabelled; T2-3 smoothness = heuristic; T2-4 approximate k | §2 hygiene | ✓ |
| T2-5 exact −u | E21-3 | ✓ (re-derived; NL notes 2026 already stated −u) |
| N3-1 E6-sign = WEC, NEC holds on UV-kept side | §3 | ✓ (ρ + P_e = +2k/κ² ≥ 0; obstruction ρ < 0) |
| N3-2 MO5 is a proof; thin-brane premise | §3 | ✓ |
| N3-3 k_x > 0 for a nontrivial face | §3 | ✓ |
| N3-4 Z2 via E20-6 | §3 | ✓ |
| A2-a 2048 log not reproducible | §4 | ✓ |
| A2-b exact basis for both PROVED labels | §4 | ✓ |
| A2-c signed flux −8π²/g³ with orientation | §4 | ✓ |
| A2-d drafts without sidecars; A2-e 2041 post-run sidecar | §4 | ✓ |
| B-1, B-2 timestamp nits | §5 | ✓ |
| E20-a bookkeeping unlabelled, E20-3 = E19-15; E20-b exponents printed | §6 | ✓ (exponents printed in a new file, original untouched) |
| D6-a 36 + 12 flows | §7 | ✓ |
| D6-b D2 identity | E21-5 | ✓ |
| D6-c c = 2^{4/3}g, exact slaving, leading order, centre-manifold theorem as premise | E21-6 | ✓ |
| D6-d D3 (PROVED) vs D6-7 (float) separated | §7 | ✓ |
| D6-e z2_scan_wide log stdout only | §7 | ✓ |
All 22 fixes are folded in faithfully. The revised target tallies in §8 match PP 2122/2123 exactly: 2/0/0/0, 2/6/1/0, 5/3/3/1, 2/0/3/0, 1/0/0/0, 0/0/0/0, E20 distinct 2/0/1/0, and D6 4/2/2/0 PARTIAL.

### 1.2 Attribution of the A2 proofs
- **Groebner component proof: correctly cited to PP ✓.** §4 says "A2-comp is accepted as PROVED (exact, PP) … The full component Groebner was not re-implemented in this erratum; it is cited from pp_a2_frame_exact (8a3e4c6c… / 1e40f493…)". It also records that the flux line of that script is superseded. It is not presented as NL's result.
- **Flux derivation: partly under-attributed (fix E21-α).** E21-4 is headed "PROVED; exact, independently re-derived". Its derivation (the push-forward by t = cos²β and s = (1−x²)t, the u-substitution, the integrand −4u²(u²+3)/(u²+1)², the value −2, and k-independence) is PP's 3fa2e067 §4 / pp_a2_flux_fix, re-run by NL. The PP scripts are cited in the header and the side note, but E21-4 itself should say "PP's exact derivation (3fa2e067 §4), independently re-run by NL".

### 1.3 Tally 5/1/0/0
- Arithmetic: 5 + 1 + 0 + 0 = 6 ✓. Items match labels ✓. Grades: E21-1, E21-3, E21-4, E21-5 and E21-6 are PROVED (all exact; E21-6 at leading order with the centre-manifold theorem as premise). E21-2 is COND ✓.
- **Double counting (fix E21-β).** Each of the six rows re-derives or restates a result that is already graded in a target tally that E21 §8 itself revises:
  - E21-1 = F9-b (2006);
  - E21-2 = R2-Y16 COND (2026, 2/6/1/0);
  - E21-3 = the exact sub-part of R2-UV (2026 says the value was already PROVED in terms of λ);
  - E21-4 = A2-flux (2049);
  - E21-5 = D6-2/3 (2100);
  - E21-6 = D6-6 (2100).
  This is the same pattern as E20-a. **PP accepts 5/1/0/0 as this erratum's row count. For any roll-up, its distinct new claims are 0/0/0/0**, and the six rows should carry "re-derivation; not re-counted".

### 1.4 Verdict
**FAITHFUL.** All fixes are applied, all re-derivations rerun byte-identical, and the Groebner proof is attributed to PP. Two bookkeeping fixes remain: E21-α (attribute the flux derivation to PP) and E21-β (do not double count in roll-ups). No grade changes.

## Part 2. pp_a2_flux_fix: F = 1/(1+s) printed False — **a false negative in PP's test; the identity, the −2 and the flux all stand on exact grounds**
**Cause.** In pp_a2_flux_fix_2026-11-09_2124.py the check was `sp.simplify(lhs - rhs) == 0`. That is a one-sided structural test: True proves equality, and False proves nothing. For F = 1/(1+s), sympy returns
- lhs = −2 + log((1+√2)^{√2}/(√2−1)^{√2}), via an intermediate complex branch log(x²−2) − iπ = log(2−x²);
- rhs = −2 + log(2^{√2}(√2/2+1)^{2√2}).
The difference simplifies only to log(R^{√2}) with R = (1+√2)/(2(√2−1)(√2/2+1)²), and sympy did not recognise that R = 1. By hand: (1+1/√2)² = 3/2+√2, and 2(√2−1)(3/2+√2) = √2+1, so R = 1. So NL is right: the identity holds and the test was wrong.
**Corrected scripts (new, additive; the 2124 script and log are not edited).** Filename times are labels; the scripts actually ran at about 21:39–21:40 CST.
- /workspace/pp-pushforward-2026-11-09/pp_pushforward_corrected_2026-11-09_2142.py = c788164b0edc32083a7d27d730929551a6902642458439bd91ca45db66d0902b, log 2c9b33a02f39638fe59b46a9cae47098b0582bbb7eab9ac193ea46ab1373b5a3, both with sidecars.
  - It evaluates both sides exactly for F = 1, s, s², 1/(1+s) and **the actual flux integrand U/Δ²**: 2/3 = 2/3, 4/15 = 4/15, 16/105 = 16/105, the log forms above, and **−2 = −2**.
  - Its log-combining zero test returns True for all five, and the old test reproduces False only for 1/(1+s).
  - It reproduces the radial integrand, the decomposition u²(u²+3) = (u²+1)² + (u²+1) − 2, ∫₀¹ = −2, and ∫G₄ = −π² = −8π²/g³ (True).
  - **Caveat:** its explicit line "log R = 0: False" is itself a structural false negative, because `radsimp(R) == 1` with R left unexpanded as (2−√2)²(2√2+3)/2. That line is superseded by v2.
- /workspace/pp-pushforward-2026-11-09/pp_pushforward_corrected_v2_2026-11-09_2144.py = 87deaed2f5900e15c09d316a4c7dcf89027b7ef39c5b0b9faf3570d51e0c0a7e, log 3d26fbed24838cb4c092f0d5fe100af5fcbb646c83d60d983168124729fffcf1, both with sidecars.
  - It uses rigorous algebraic zero tests: **minimal_polynomial(R) = X − 1**, and expand(radsimp(R)) = 1.
  - With A₀ = (1+√2)², minimal_polynomial(A_l/A₀) = minimal_polynomial(A_r/A₀) = X − 1, so **lhs = rhs = −2 + 2√2·log(1+√2)** exactly.
**Status of the A2-flux result.** The flux never depended on the F = 1/(1+s) line.
- The push-forward ½∫_{−1}^{1}∫₀^{1−x²}F ds dx = ∫₀¹F(s)√(1−s) ds holds for every integrable F by Fubini (|x| ≤ √(1−s)). It was proved by hand in 3fa2e067 §4.
- For the flux integrand both sides are now also computed exactly: −2 = −2.
- The radial integral is ∫₀¹ −4u²(u²+3)/(u²+1)² du = −4[1 + π/4 − 2(π/8 + 1/4)] = **−2, exact**.
- Hence **∫_{S⁴}G₄(CGR) = (2π)²(−2)/g³ = −8π²/g³ (= −π² at g = 2) remains PROVED on exact grounds**, and A2-comp (Groebner, pp_a2_frame_exact) is unaffected.
PP fix to its own record: **PP-1.** Read the F = 1/(1+s) line of pp_a2_flux_fix_2026-11-09_2124.log, and the "log R = 0: False" line of pp_pushforward_corrected_2026-11-09_2142.log, as false negatives superseded by pp_pushforward_corrected_v2_2026-11-09_2144. From now on PP uses minimal-polynomial or exact closed-form tests instead of `simplify(...) == 0` for transcendental or radical differences.

## Summary
| item | verdict |
|---|---|
| Erratum 21 (2135), 5/1/0/0 | **FAITHFUL**; row count accepted; distinct new 0/0/0/0; fixes E21-α (attribute the flux derivation to PP) and E21-β (no double count) |
| pp_a2_flux_fix F = 1/(1+s) "False" | false negative in PP's test; corrected by v2 (minimal polynomial X − 1); −2 and −8π²/g³ stand, exact |
Junction UNSOLVED; nothing adopted. No CERT. Nothing sent.
Tip at write time: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (unchanged).
