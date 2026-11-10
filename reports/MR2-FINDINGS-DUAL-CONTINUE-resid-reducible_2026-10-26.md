# MR2 FINDINGS — DUAL CONTINUE — residual of 7.4.a.a mod 7 is REDUCIBLE (PARTIAL)
Date 2026-10-26 · Executor MR2 · Builds on BM-JH 860f0139… (gap SF-3) · Authority OW 9b993a72… · MR2 ACK 78f34b4e…
Filtration: BOTH NAMED PARALLEL 10∥40 — NO PICK. Kerr BLOCKED. No RECS. No P5a. Bridge PARTIAL READY NO. No tip fold. tip_touched NO.

## STATUS: PARTIAL (Option A resolved in the negative direction for the absolutely-irreducible hypothesis)

## Soft SF facts (proved)
F1. f = 7.4.a.a = q − q² − 2q³ − 7q⁴ + 16q⁵ + … (Sage Newforms(Γ0(7),4), unique).
F2. Congruence: f·E6² ≡ θ(E8) · 4⁻¹ ≡ Σ n·σ1(n) qⁿ (mod 7) as weight-16 forms on Γ0(7).
    Proof: E_{p−1}=E6 ≡ 1 mod 7; E8 = 1+480Σσ7(n)qⁿ, σ7≡σ1, so θE8 ≡ 4Σnσ1(n)qⁿ, a mod-7 form of level 1, weight 8+8=16 (Katz θ, 7∤1).
    Sage: equality of q-expansions mod 7 verified to n<120 ≥ Sturm bound(Γ0(7),16)=11 ⇒ identity holds. (n with 7|n: both sides 0, since a7=−7, a_{7m}=a7·a_m.)
F3. Hence a_ℓ(f) ≡ ℓ + ℓ² (mod 7) for every prime ℓ ≠ 7 (also checked directly ℓ<200; only (ω,ω²) fits among ω^i+ω^j).
F4. By Chebotarev + Brauer–Nesbitt: ρ̄^ss ≅ ω ⊕ ω² (ω = mod-7 cyclotomic), det = ω³ consistent with weight 4.
F5. Consequence: ρ̄ is NOT absolutely irreducible. Any BM / Paškūnas step requiring ρ̄ abs. irreducible (SF-3 gap in 860f0139…) does NOT apply as stated.
F6. End_{G_Q}(ρ̄) depends on lattice: split lattice ⇒ End = k×k ≠ k; a non-split lattice (exists by Ribet's lemma, ω≠ω²) ⇒ End = k. So "End=k" is TRUE for a non-split lattice, FALSE for semisimple; not lattice-independent.

## Named ABSENT
- Which extension class (in H¹(G_Q, ω^{±1})) the Ribet lattice realizes, and restriction to G_{Q7} (End_{G_Q7}(ρ̄|) for the non-split lattice): ABSENT — needs explicit Ext computation / local class at 7. G_Q7-level End=k NOT claimed.
- G1 (L₇ unit residue) not attempted this run. Teitelbaum 𝓛 NOT closed.

## Repro
/tmp/a.sage (a_ℓ scan), /tmp/b.sage (congruence; used E6 in place of E6², equivalent since E6≡1). Sage /tmp/pm/bin/sage.
