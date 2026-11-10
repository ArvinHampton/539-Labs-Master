# FINDINGS — Local: Gap 2 non-∞ cusp principal parts, g_s=f(q^s), s∈{7,8,11} — 2026-10-28
Status: PARTIAL (orbit classification + representative formulas CLOSED modulo labeled steps; roots of unity ABSENT). Prior 595d6102… not rewritten. tip_touched NO. Kerr BLOCKED.

## Setup (cite-grounded)
- Zwegers 2002 thesis (Ch. 4) / Bringmann–Ono 2006: F(τ)=(q^{-1/24}f(q), 2q^{1/3}ω(q^{1/2}), 2q^{1/3}ω(−q^{1/2}))ᵀ plus nonholomorphic completion transforms as a weight-1/2 vector-valued form on SL₂(ℤ); T,S matrices explicit there (S swaps f-component with ω-components). M_f(τ)=F₁(24τ); object here M_f(sτ)=F₁(24sτ).
- Only the f-component has negative order (−1/24); ω-components start at q^{1/3} ⇒ no principal part. Nonholomorphic completion contributes no principal part (period integral decays).

## Reduction (derived; elementary)
Cusp a/c of Γ₀(144s), gcd(a,c)=1, γ=[[a,b],[c,d]]∈SL₂(ℤ). Then [[24s,0],[0,1]]γ = γ'·[[A,B],[0,D]], A=gcd(24s,c), AD=24s, γ' bottom-left = c/A.
- γ'∈Γ₀(2) (c/A even) ⇒ F₁|γ' = ζ·F₁ (f-type) ⇒ principal part ζ·e(−(Aτ+B)/(24D)), leading exponent −A/(24D)=−A²/(576s) in q=e(τ) (single term, the q^{-1/24} term of F₁).
- c/A odd ⇒ F₁|γ' is a combination of ω-components (S-type) ⇒ holomorphic at that cusp.
- ζ (24th root of unity × character values): invented pending mathematical proof as to exact value — explicit from Zwegers' T/S matrices but NOT computed/verified here → ABSENT.
- Independence of representative a within a denominator class: holds for type and exponent (depend only on c); ζ may depend on a — ABSENT.

## Tables (Python-computed; cusp classes of Γ₀(N) by denominator c|N, φ(gcd(c,N/c)) each)
### s=7, Γ₀(1008): 47 non-∞ cusps, 7 with principal part
| denom c | #cusps | width | A=gcd(24s,c) | type | leading exponent −A²/(576s) |
|---|---|---|---|---|---|
| 1 | 1 | 1008 | 1 | ω-type | none (holomorphic) |
| 2 | 1 | 252 | 2 | ω-type | none (holomorphic) |
| 3 | 2 | 112 | 3 | ω-type | none (holomorphic) |
| 4 | 2 | 63 | 4 | ω-type | none (holomorphic) |
| 6 | 2 | 28 | 6 | ω-type | none (holomorphic) |
| 7 | 1 | 144 | 7 | ω-type | none (holomorphic) |
| 8 | 1 | 63 | 8 | ω-type | none (holomorphic) |
| 9 | 1 | 112 | 3 | ω-type | none (holomorphic) |
| 12 | 4 | 7 | 12 | ω-type | none (holomorphic) |
| 14 | 1 | 36 | 14 | ω-type | none (holomorphic) |
| 16 | 1 | 63 | 8 | f-type | -1/63 (in q=e(τ)) |
| 18 | 1 | 28 | 6 | ω-type | none (holomorphic) |
| 21 | 2 | 16 | 21 | ω-type | none (holomorphic) |
| 24 | 2 | 7 | 24 | ω-type | none (holomorphic) |
| 28 | 2 | 9 | 28 | ω-type | none (holomorphic) |
| 36 | 2 | 7 | 12 | ω-type | none (holomorphic) |
| 42 | 2 | 4 | 42 | ω-type | none (holomorphic) |
| 48 | 2 | 7 | 24 | f-type | -1/7 (in q=e(τ)) |
| 56 | 1 | 9 | 56 | ω-type | none (holomorphic) |
| 63 | 1 | 16 | 21 | ω-type | none (holomorphic) |
| 72 | 1 | 7 | 24 | ω-type | none (holomorphic) |
| 84 | 4 | 1 | 84 | ω-type | none (holomorphic) |
| 112 | 1 | 9 | 56 | f-type | -7/9 (in q=e(τ)) |
| 126 | 1 | 4 | 42 | ω-type | none (holomorphic) |
| 144 | 1 | 7 | 24 | f-type | -1/7 (in q=e(τ)) |
| 168 | 2 | 1 | 168 | ω-type | none (holomorphic) |
| 252 | 2 | 1 | 84 | ω-type | none (holomorphic) |
| 336 | 2 | 1 | 168 | f-type | -7 (in q=e(τ)) |
| 504 | 1 | 1 | 168 | ω-type | none (holomorphic) |

### s=8, Γ₀(1152): 63 non-∞ cusps, 3 with principal part
| denom c | #cusps | width | A=gcd(24s,c) | type | leading exponent −A²/(576s) |
|---|---|---|---|---|---|
| 1 | 1 | 1152 | 1 | ω-type | none (holomorphic) |
| 2 | 1 | 288 | 2 | ω-type | none (holomorphic) |
| 3 | 2 | 128 | 3 | ω-type | none (holomorphic) |
| 4 | 2 | 72 | 4 | ω-type | none (holomorphic) |
| 6 | 2 | 32 | 6 | ω-type | none (holomorphic) |
| 8 | 4 | 18 | 8 | ω-type | none (holomorphic) |
| 9 | 1 | 128 | 3 | ω-type | none (holomorphic) |
| 12 | 4 | 8 | 12 | ω-type | none (holomorphic) |
| 16 | 4 | 9 | 16 | ω-type | none (holomorphic) |
| 18 | 1 | 32 | 6 | ω-type | none (holomorphic) |
| 24 | 8 | 2 | 24 | ω-type | none (holomorphic) |
| 32 | 2 | 9 | 32 | ω-type | none (holomorphic) |
| 36 | 2 | 8 | 12 | ω-type | none (holomorphic) |
| 48 | 8 | 1 | 48 | ω-type | none (holomorphic) |
| 64 | 1 | 9 | 64 | ω-type | none (holomorphic) |
| 72 | 4 | 2 | 24 | ω-type | none (holomorphic) |
| 96 | 4 | 1 | 96 | ω-type | none (holomorphic) |
| 128 | 1 | 9 | 64 | f-type | -8/9 (in q=e(τ)) |
| 144 | 4 | 1 | 48 | ω-type | none (holomorphic) |
| 192 | 2 | 1 | 192 | ω-type | none (holomorphic) |
| 288 | 2 | 1 | 96 | ω-type | none (holomorphic) |
| 384 | 2 | 1 | 192 | f-type | -8 (in q=e(τ)) |
| 576 | 1 | 1 | 192 | ω-type | none (holomorphic) |

### s=11, Γ₀(1584): 47 non-∞ cusps, 7 with principal part
| denom c | #cusps | width | A=gcd(24s,c) | type | leading exponent −A²/(576s) |
|---|---|---|---|---|---|
| 1 | 1 | 1584 | 1 | ω-type | none (holomorphic) |
| 2 | 1 | 396 | 2 | ω-type | none (holomorphic) |
| 3 | 2 | 176 | 3 | ω-type | none (holomorphic) |
| 4 | 2 | 99 | 4 | ω-type | none (holomorphic) |
| 6 | 2 | 44 | 6 | ω-type | none (holomorphic) |
| 8 | 1 | 99 | 8 | ω-type | none (holomorphic) |
| 9 | 1 | 176 | 3 | ω-type | none (holomorphic) |
| 11 | 1 | 144 | 11 | ω-type | none (holomorphic) |
| 12 | 4 | 11 | 12 | ω-type | none (holomorphic) |
| 16 | 1 | 99 | 8 | f-type | -1/99 (in q=e(τ)) |
| 18 | 1 | 44 | 6 | ω-type | none (holomorphic) |
| 22 | 1 | 36 | 22 | ω-type | none (holomorphic) |
| 24 | 2 | 11 | 24 | ω-type | none (holomorphic) |
| 33 | 2 | 16 | 33 | ω-type | none (holomorphic) |
| 36 | 2 | 11 | 12 | ω-type | none (holomorphic) |
| 44 | 2 | 9 | 44 | ω-type | none (holomorphic) |
| 48 | 2 | 11 | 24 | f-type | -1/11 (in q=e(τ)) |
| 66 | 2 | 4 | 66 | ω-type | none (holomorphic) |
| 72 | 1 | 11 | 24 | ω-type | none (holomorphic) |
| 88 | 1 | 9 | 88 | ω-type | none (holomorphic) |
| 99 | 1 | 16 | 33 | ω-type | none (holomorphic) |
| 132 | 4 | 1 | 132 | ω-type | none (holomorphic) |
| 144 | 1 | 11 | 24 | f-type | -1/11 (in q=e(τ)) |
| 176 | 1 | 9 | 88 | f-type | -11/9 (in q=e(τ)) |
| 198 | 1 | 4 | 66 | ω-type | none (holomorphic) |
| 264 | 2 | 1 | 264 | ω-type | none (holomorphic) |
| 396 | 2 | 1 | 132 | ω-type | none (holomorphic) |
| 528 | 2 | 1 | 264 | f-type | -11 (in q=e(τ)) |
| 792 | 1 | 1 | 264 | ω-type | none (holomorphic) |

## Closed vs ABSENT
CLOSED: orbit classification (f-type vs ω-type) for all 157 non-∞ cusps; leading exponents for f-type cusps; holomorphy at ω-type cusps (cite-grounded on Zwegers' vector-valued law; reduction step derived here, invented pending mathematical proof for full rigor of Γ₀(2)-stability claim F₁|γ'∝F₁).
ABSENT: exact roots of unity ζ per cusp; mechanical numeric check of expansions. Reason: Zwegers' multiplier system not transcribed/verified this run.
β_s=π/√(6s), A_s=√s/2, α=−1/2: remain invented pending mathematical proof; dominant cusps for circle method now identified (max |exponent|) — path advanced, NOT Written.
