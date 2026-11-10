# PP-FINDINGS — Katz level-1 filtration w(θ³f̄)=40, f=7.4.a.a, p=7 — proof pursuit (2026-10-27)
Role: Professor Proof → Auditor. Soft SF, REPORTS ONLY, no RECs. Tip untouched; Kerr/Path4/link(b) not touched. OW BOTH NAMED PARALLEL respected: no Owner pick, conventions NOT collapsed; geometric Γ₀(7) w=10 is a separate ambient and is NOT equated with Katz 40.

## Live sha table (2026-10-27 ~13:20 CDT)
| item | sha256 | match |
|---|---|---|
| tip residual-c-field-WRITTEN_PREMISES_DRAFT.md (before) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH |
| tip (after writes) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH (tip_touched NO) |
| OW filtr BOTH NAMED PARALLEL (reports/, bridges/AUDITOR, bridges/EIGEN) | c3288fbfdb3c9c0952eaecb950e0dc67642dba712d550e744c8bcebedc5aa43a | MATCH |
| MR2-FINDINGS-H3-TEITELBAUM-LINV_2026-10-26.md | bdcaf1e6a898c8d2a894a4f3c97bacb2131f4983c784e4af5ea42f8c506257ef | MATCH |
| scripts/mr2_h3_theta_filtration.py | cf45cf5e7910bfe81b33ab604f911ca68342fd1a4297cb762bea41deff7d00f0 | MATCH |

## Convention (Katz/Serre level-1 ambient only)
M_k(F_7) := span over F_7 of q-expansions E4^a E6^b Δ^c, 4a+6b+12c=k, reduced mod 7. Filtration w(g) := least k with g ∈ M_k(F_7). θ = q d/dq. (Geometric Γ₀(7) filtration is a different ambient — not addressed here.)

## Re-run (live, exit 0, ~31 s)
f computed as weight-4 theta series (harmonic poly b²−7c², halved) of the quaternary form: f = q − q² − 2q³ − 7q⁴ + 16q⁵ + 2q⁶ − 7q⁷ + 15q⁸ − 23q⁹ − 16q¹⁰ − 8q¹¹ + 14q¹² + 28q¹³ + 7q¹⁴ − 32q¹⁵ …, consistent with 7.4.a.a. Span test over 60 coefficients, all even k in 2..56:
- θ⁰f̄ ∈ M_k for k = 16,22,28,…  → least 16
- θ¹f̄: 24,30,…  → 24
- θ²f̄: 32,38,…  → 32
- θ³f̄: 40,46,52  → **40** (not in M_k for any k<40, in particular k=4,10,16,22,28,34)

## Proof
1. (Serre) f ∈ S_4(Γ₀(7)) ⇒ f̄ is a mod-7 level-1 form of weight 4·7=28. Since E6 ≡ 1 (mod 7) multiplication by E6 maps M_k→M_{k+6} identically on q-expansions, so membership in M_16 can be tested in M_28; Sturm bound for level 1 weight 28 is ⌊28/12⌋=2 < 60 coefficients. Hence f̄ ∈ M_16 rigorously. Non-membership in M_k, k<16 (k≡16 mod 6: 4,10) is rigorous from truncated q-expansions (a truncated mismatch is a genuine mismatch). ⇒ w(f̄)=16.
2. (Katz) w(θg) ≤ w(g)+p+1, with equality iff w(g) ≢ 0 mod p. w=16,24,32 are ≡ 2,3,4 mod 7 ≠ 0, so w(θf̄)=24, w(θ²f̄)=32, w(θ³f̄)=40. Steps +8 = p+1.
3. Independent computational cross-check: θ³f̄ ∉ M_k for k ∈ {4,10,16,22,28,34} (rigorous non-membership) and ∈ M_40 (Sturm bound ⌊40/12⌋=3 < 60, given θ³f̄ is a weight-40 level-1 mod-7 form by step 2). Agrees with step 2.

## Verdict
**PROVED under the stated Katz/Serre level-1 convention** (span E4^a E6^b Δ^c mod 7): w(θ³f̄)=40. Eligible to discharge the invent-pending item **for the Katz level-1 ambient only**. Does not affect, equal, or replace the geometric Γ₀(7) w=10 (separately discharged). No Owner pick, no tip-fold, no new values (16/24/32/40 are the H3-4 values, re-derived). Residual caveat: identification of the computed f with LMFDB label 7.4.a.a rests on q-expansion match (first coefficients) + Sturm on S_4(Γ₀(7)); not re-fetched from LMFDB this run.
