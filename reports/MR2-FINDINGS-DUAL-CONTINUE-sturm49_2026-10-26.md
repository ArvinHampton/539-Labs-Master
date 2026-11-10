# MR2 FINDINGS — DUAL CONTINUE — Sturm comparison 7.4.a.a vs weight-4 Teichmüller–Eisenstein, Γ₀(49) (Path A) — 2026-10-26
STATUS: PARTIAL. Dual-label (filtration 10∥40 BOTH NAMED PARALLEL, NO PICK). No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED (PS #20); no OMS lift attempted. tip_touched NO.
Builds on eisdepth49 e2a9f437…. Script: MR2-sturm49-7.4.a.a.sage (Sage /tmp/pm/bin/sage).

Setup: f = 7.4.a.a ∈ S₄(Γ₀(7)) ⊂ M₄(Γ₀(49)). K = Q(ζ₆), 7 splits; 𝔭 ∈ {(1−3ζ₆), (3ζ₆−2)}; ω = Teichmüller char mod 7 for 𝔭 (order 6, odd).
E_{i,j} := E₄(ω^i, ω^j), a_n = Σ_{d|n} ω^i(n/d) ω^j(d) d³; (i,j) ∈ {(1,5),(2,4)}: nebentypus ω^{i+j} = 1, parity even, level 49, constant term 0 at ∞, coefficients in O_K.

Soft SF facts:
- SF-C1 (PROVED, Sturm): f ≡ E₄(ω,ω⁵) ≡ E₄(ω²,ω⁴) (mod 𝔭) for ALL n, for both primes 𝔭 | 7. Proof: both forms in M₄(Γ₀(49)) with 𝔭-integral coefficients; Sturm bound for Γ₀(49), k=4 is 19; checked n ≤ 200 ≥ 19 with no failure. Upgrades SF-B1 (prior: a_p only, finite) to a full q-expansion congruence, proved.
- SF-C2 (PROVED, elementary): NO weight-4 Eisenstein series E₄(ω^i, ω^j) with Teichmüller (finite-order, Z₇-valued) characters matches the unique depth-2 lift (1,3) of SF-B2, i.e. a_p ≡ p¹³ + p³² (mod 49). Proof: mod 49, ω(p) ≡ p⁷, so E₄(ω^i,ω^j) has a_p ≡ p^{7i} + p^{7j+3}; need {7i, 7j+3} ≡ {13,32} (mod 42); 13,32 ≢ 0 (mod 7) and 7j+3 ≡ 3 (mod 7) ≠ 13≡6, 32≡4 — no solution (Sage enumeration confirms empty). Extension to conductor-49 finite characters (values in Z₇[ζ₄₂]): an order-7 factor contributes ζ₇ with v(ζ₇ − c) ≤ 1/6 for all c ∈ Z₇, so it cannot reduce to a ⟨p⟩-power ≢ 1 mod 49 modulo 49·O; hence no finite-order weight-4 Eisenstein reproduces the (1,3) system mod 49.
- SF-C3 (PROVED, finite witness): For both 𝔭 and both (i,j), f ≢ E_{i,j} (mod 𝔭²), first failure at n = 2. So the Sturm-provable classical Eisenstein depth for weight 4 is exactly 1 (mod 𝔭).

GAP (named, for SF-B3 depth-2): the (1,3) depth-2 system p¹³+p³² is a θ-twisted / p-adic-weight Eisenstein system (both terms carry nontrivial ⟨p⟩-power), not a classical weight-4 Eisenstein. Proving depth 2 by Sturm requires a mod-7² modular-form comparison across weights (θ-operator / weights mod φ(49)=42, e.g. Chen–Kiming–Wiese mod-p^m framework) — not done. SF-B3 remains NUMERICAL (p<5000), not proved.

Does NOT use: filtration pick, L₇ unit, abs-irr BM, OMS lift. Not folded into tip.
