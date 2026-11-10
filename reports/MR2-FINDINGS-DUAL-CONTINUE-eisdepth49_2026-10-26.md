# MR2 FINDINGS — DUAL CONTINUE — Teichmüller-Eisenstein depth mod 49 for 7.4.a.a (Path B) — 2026-10-26
STATUS: PARTIAL. Dual-label (filtration 10∥40 BOTH NAMED PARALLEL, NO PICK). No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. G1 BLOCKED (PS #20), OMS lift not attempted. tip_touched NO.
Script: MR2-eisdepth49-7.4.a.a.sage (Sage /tmp/pm/bin/sage).

f = 7.4.a.a = q − q² − 2q³ − 7q⁴ + 16q⁵ + … ; residual ρ̄^ss ≅ ω⊕ω² (per c358d9e6…).
Lift family: all 49 mod-49 lifts a_p ≡ ω(p)·⟨p⟩^{6a·} + ω²(p)·⟨p⟩^{6b·}, i.e. ω̃(p)p^{6a} + ω̃²(p)p^{6b} (mod 49), a,b∈0..6, ω̃ = Teichmüller.

Soft SF facts:
- SF-B1 (proved, finite compute): mod 7 depth ≥1 for every lift (re-confirms G1blocked, not new).
- SF-B2 (proved, finite witness): among the 49 mod-49 lifts, exactly ONE, (a,b)=(1,3), satisfies a_p ≡ ω̃(p)p⁶ + ω̃²(p)p¹⁸ mod 49 for all p<400; the other 48 fail mod 49 at an explicit prime p<400. Equivalently (ω̃(p)≡p⁷ mod 49): a_p ≡ p¹³ + p³² (mod 49); exponents sum 45 ≡ 3 mod 42 (det-consistent with weight 4).
- SF-B3 (numerical, NOT proved): (1,3) congruence holds for all primes 3≤p<5000, p≠7 → depth exactly 2 (mod 49) for this lift; no lift of the 49 reaches depth 3 (p<400 valuations sets {1,2}). Naive lifts 1+p³ (depth 0), p+p², ω̃+ω̃² (depth 1) are NOT the matching lift.
- Upgrade path to proved: Sturm-bound comparison vs weight-4 Eisenstein with characters of conductor 49 — not done (labelled open).
Valuation distribution of a_p−p−p² (p<400): {1:55, 2:19, 3:2}.

Does NOT use: filtration pick, L₇ unit, abs-irr BM, OMS lift. Not folded into tip.
