# SOFTSF_PRESS — MR2 DUAL CONTINUE G1-blocked → Auditor (write-only)
Status: PARTIAL. Advances beyond 8dc263d3 by closing G1 attempt route (A) with exact gap, plus B data. No RECS. No P5a. Kerr BLOCKED. Bridge PARTIAL READY NO. Filtration BOTH NAMED PARALLEL 10∥40 — no pick. Tip untouched (sha 7cddb188…).

## A) G1 attempt — BLOCKED (exact gap)
f = 7.4.a.a: q - q^2 - 2q^3 - 7q^4 + 16q^5 + 2q^6 - 7q^7 + … ; a_7 = -7 ⇒ v_7(a_7)=1 = (k-2)/2, Steinberg, NON-ordinary at 7.
Sage Pollack–Stevens: ps_modsym_from_simple_modsym_space OK (values [(7,0,-1),(-49,-21,-8)]); `phi.lift(7,M=6,eigensymbol=True)` →
`ValueError: Lifting non-ordinary eigensymbols not implemented (issue #20)`.
Gap: Sage OMS lifting needs ordinary (slope 0); slope-1 (critical-slope for Steinberg, k=4) requires non-ordinary/critical OMS lifting (Pollack–Stevens critical slope / Bellaïche) not available in this Sage. Unit residue of L_7 NOT obtained ⇒ NOT Soft SF'd. global End_GQ7 remains ABSENT pending G1.

## B) Eisenstein congruence depth (data)
- PROVED (single-coefficient witness): f ≢ Eis(1,ℓ^3) mod 7 (ℓ=2: a_2=-1 vs 9); f ≢ Eis(ℓ^4,ℓ^5) mod 7 (ℓ=3).
- VERIFIED all primes ℓ<1000, ℓ≠7: a_ℓ ≡ ℓ+ℓ^2 (mod 7) [residual ω⊕ω^2; consistent with resid-reducible c358d9e6].
- Integral-lift test mod 49: a_ℓ ≢ ℓ+ℓ^2 mod 49 at ℓ=2,3,5. Depth vs Teichmüller-twisted Eisenstein lift mod 49 NOT computed ⇒ depth ≥1 only; exact depth NOT Soft SF'd.

## Soft SF facts (only)
1. a_7(7.4.a.a) = -7; non-ordinary at 7 (Sage).
2. Sage PS OMS lift fails: non-ordinary not implemented (G1 tool gap, exact error above).
3. f ≢ 1+ℓ^3 and ≢ ℓ^4+ℓ^5 mod 7 (proved by witness).
4. a_ℓ ≡ ℓ+ℓ^2 mod 7 for all primes ℓ<1000, ℓ≠7 (computational).
Dual-label: independent of filtration pick (10∥40 both named parallel).
Scripts: /tmp/g1.sage /tmp/g2.sage /tmp/g3.sage
