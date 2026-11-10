# deduce_t713u_ga3_fill — PREREG (written before RESULTS / table; frozen)
Stamp: 2026-10-25 CDT. Scope: Local Bridge C only (local modular). CORE_FREEZE; SF-W7-3; Residual-vs-Resonant lock; no nonlocal EH11D/Ω₁₁D/F_total; no order78.

## Authority
- t712s4471 AUTHOR AUTHORIZE (Arvin via Physicist): G-A3-only compute, source class (C), THIS h-table only. Invent-ban holds elsewhere.
- t713s4484: ψ ≡ Bridge C ψ := psi-Cocycle ψ (reports/heavy-daily/2026-10-17-psi-Cocycle.md 1be7f7d198ce6c527702d36e84db6722fd9562557e408b6d02d09fa7ffcaeb5a).
- t713s4497 AUTHOR ACCEPT: G-A3 compute defaults LOCKED; re-run under t712s4471.
- Schema being filled (identity preserved, not replaced): AUTHOR_CANDIDATE_GA3_h_table_schema_v2 sha 8d247feb4f1b644dfbaf1d28237eaddfe9ba45c82d40464a2290d4721b0f8051 (deduce_t708u_ga3/author_candidates/). Filled values NOT Cat A until Arvin ACCEPT.

## Premises (ACCEPT-sourced AUTHOR conventions; all cited)
P1 ψ ≡ psi-Cocycle ψ (t713s4484; 1be7f7d1…). x>0: fastkappa.psi (exact Bernoulli sums; 2026-10-17-psi-cocycle/fastkappa.py 70f605a4…). x<0: psi_minus (|x| factor, psi-Cocycle §A4; neg_side2.py), = conj ψ(−x).
P2 Path i∞ → x (Construct_Higher_Fidelity 1bab65c4… L32, Fricke-compatible discrete): vertical ray w = x+it, t: ∞→0.
P3 Branch principal (w−x)^{−1/2}, Arg ∈ (−π, π]; on the ray (it)^{−1/2} = t^{−1/2}e^{−iπ/4}. √i = e^{iπ/4} principal.
P4 Ξ regenerated from Written product form Σ outer_even(m)·Θ_{3/2}(·;a=7m) + Σ outer_odd(m)·Θ_{3/2}(·;a=7m+7/2) (1bab65c4 L18; 736cfd72 L16; 552541cf L20–22). Ledger Ξ 7dbd63af… HOLD — NOT used.
P5 N_trunc = 106 (Θ_third landmark; last listed degree 736cfd72 / 1bab65c4). Partials 43/58/67 carried as FLAGGED (sensitivity variant only).
P6 Ξ table second column (if consulted): index label, unit coefficients c_N = 1.
P7 Θ_{3/2}(·;a) leading factor 1 under locked completed-square rewrite; no extra prefactor (be1faa52 warn).

## Written ingredients used (located, not invented)
- Θ_{3/2}(·;a) = Σ (n+a) q^{(n+a)²} (552541cf L24).
- Outer factor enters as q^{outer(·)} with unit coefficient: outer_even(m)=35m²+7m, m≥1; outer_odd(m)=35m²+42m+49/4, m≥0 ("residual partial theta of squares", e60cad9b… = 1f80d0d5 Next_Levers L16–22; values 42,154,…/12.25,89.25,… in 1bab65c4 L16–17).
- n ≥ 0 (partial theta): forced, since Σ_{n∈ℤ}(n+a)q^{(n+a)²} ≡ 0 for a ∈ ½ℤ (odd in k=n+a) — recorded as reading, cross-checked against Written table entries 24.5:3.5 … 106:8.
⇒ Ξ_N(w) = Σ_{ν≤106} c_ν e(νw), c_ν = Σ over (sector,m,n≥0) with outer+(n+a)² = ν of (n+a).

## Sample set
x ∈ {1/7, 3/7, 5/7, 1}; W₇x = −1/(7x) ∈ {−1, −1/3, −1/5, −1/7} (7368b855 L44).

## Compute
- I(x) := ∫_{i∞}^{x} Ξ_N(w)(w−x)^{−1/2}dw = Σ c_ν · (−e^{iπ/4} e(νx)/√(2ν)) (exact termwise Γ(1/2)); cross-check by mpmath quadrature.
- h(x) = ψ(x)/√i − I(x).
- residual_slash(x) = |7x|^{−1/2}·(a+bt+ct²+d/(1+t²)), t=7x−3, (a,b,c,d)=(10.6923,0.2160,2.7618,−7.5316) (7368b855 §2; selectors Cat A 437d4571…, S-B1′ 3d502756…).
- δ(x) = h(x) − residual_slash(x)·h(W₇x) (7368b855 L46).
- Error: ψ quadrature/exact floor ~1e-13; I exact closed form (fp ~1e-14); slash coefficient rounding Δ=5e-5 each → σ_slash(x)=|7x|^{−1/2}·5e-5·(1+|t|+t²+1/(1+t²)). tol(x) := 10·(1e-12 + σ_slash(x)·|h(W₇x)|). Truncation: Ξ series does not converge on ℝ (|e(νx)|=1, growing c_ν/√ν); report N-sensitivity (N=106 vs 150) as diagnostic, not a convergent bound.
- Sensitivity variant V-P: add flagged partials ν=43,58,67 with c=1 (P5/P6). Main table = regenerated only.

## Pre-registered rules
- RG-F0 Input gate: all inputs above Written/ACCEPT-sourced ⇒ proceed; any missing ingredient ⇒ STOP BLOCKED.
- RG-F1 fill table under author_candidates/ (NOT Cat A), per-cell provenance.
- RG-F2 F1: |δ|≤tol at all 4 x ⇒ RG76d PASS-candidate at samples. F2: samples alone NEVER force δ≡0. F3: |δ|>tol nonzero ⇒ controlled defect recorded, obstruction refined, Bridge PARTIAL.
- Standing until ACCEPT: Bridge PARTIAL; READY NO; residual-C OPEN unless F-criteria force otherwise (only F1 PASS + identity proof could move this; samples cannot).
