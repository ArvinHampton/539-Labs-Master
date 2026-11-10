# FINDINGS — Local: Gap 2 ζ multipliers at f-type non-∞ cusps, g_s=f(q^s), s∈{7,8,11} — 2026-10-28
Status: CLOSED-numerical for the representative table (17 f-type cusps); proof-grade promotion pending. Prior 7b0eb063… / 595d6102… not rewritten. tip_touched NO. Kerr BLOCKED.

## Source (reopened & fetched this run)
- Bringmann–Ono, Invent. Math. 165 (2006) 243–266, author PDF uva.theopenscholar.com/files/ken-ono/files/098_8.pdf, §2 eq. (2.2)–(2.5), Theorem 2.1 (Zwegers): H=F−G, F=(q^{-1/24}f(q), 2q^{1/3}ω(q^{1/2}), 2q^{1/3}ω(−q^{1/2}))ᵀ,
  H(z+1)=[[ζ₂₄⁻¹,0,0],[0,0,ζ₃],[0,ζ₃,0]]H(z),  H(−1/z)=√(−iz)·[[0,1,0],[1,0,0],[0,0,−1]]H(z).
- Zwegers thesis arXiv:0807.4834 (fetched): p.~85 defers the third-order vector law to Zwegers, Contemp. Math. 291 (2001) 269–277 [ref 30] — that is the primary source; quoted via Bringmann–Ono Thm 2.1.

## Formula for ζ(a/c)
For cusp a/c of Γ₀(144s), γ=[[a,b],[c,d]] (d=a⁻¹ mod c, b=(ad−1)/c), [[24s,0],[0,1]]γ=γ'·[[A,B],[0,D]], A=gcd(24s,c), D=24s/A, γ'=[[24sa/A,x],[c/A,y]].
Write γ' as a T/S word (Euclid), ρ(γ')=product of the Thm 2.1 matrices, with principal-branch √(−iz) factors chained.
Then (cτ+d)^(−1/2)·M_f(sγτ) = C(a/c)·e(−A²τ/(576s)) + (holomorphic at that cusp) + nonholomorphic decaying part, with
  C(a/c) = ρ(γ')₀₀ · e(−B/(24D)) · [chained √ factor / √(cτ+d)],  |C| = D^(−1/2).
Verified numerically: for every f-type cusp ρ(γ') row 0 = (ρ₀₀,0,0) (F₀ ↦ multiple of F₀ — confirms Gap-2 f-type claim, previously invented); for every ω-type cusp ρ₀₀=0 (no principal part) — 157/157 cusps checked.
Consistency: at ∞ (A=24s,D=1) exponent −s, matching q^(−s).

## Table (Python, script /workspace/quantum-comp/work/zeta.py sha256 67614b7ab5d0f543de4863133505a1f5749c4ad88520b81a86bdf9672630c153)
### s=7, Γ₀(1008)
| c | a | A | D | B | |C| | arg C (turns) | leading exponent |
|---|---|---|---|---|---|---|---|
| 16 | 1 | 8 | 21 | -10 | D^(-1/2)=0.2182178902 | 59/63 | -1/63 |
| 48 | 1 | 24 | 7 | -3 | D^(-1/2)=0.377964473 | 19/84 | -1/7 |
| 48 | 5 | 24 | 7 | 11 | D^(-1/2)=0.377964473 | 47/84 | -1/7 |
| 112 | 1 | 56 | 3 | -1 | D^(-1/2)=0.5773502692 | 11/36 | -7/9 |
| 144 | 1 | 24 | 7 | -1 | D^(-1/2)=0.377964473 | 27/28 | -1/7 |
| 336 | 1 | 168 | 1 | 0 | D^(-1/2)=1.0 | 1/3 | -7 |
| 336 | 5 | 168 | 1 | 134 | D^(-1/2)=1.0 | 2/3 | -7 |
### s=8, Γ₀(1152)
| c | a | A | D | B | |C| | arg C (turns) | leading exponent |
|---|---|---|---|---|---|---|---|
| 128 | 1 | 64 | 3 | -1 | D^(-1/2)=0.5773502692 | 11/36 | -8/9 |
| 384 | 1 | 192 | 1 | 0 | D^(-1/2)=1.0 | 1/3 | -8 |
| 384 | 5 | 192 | 1 | 38 | D^(-1/2)=1.0 | 2/3 | -8 |
### s=11, Γ₀(1584)
| c | a | A | D | B | |C| | arg C (turns) | leading exponent |
|---|---|---|---|---|---|---|---|
| 16 | 1 | 8 | 33 | -16 | D^(-1/2)=0.174077656 | 68/99 | -1/99 |
| 48 | 1 | 24 | 11 | -5 | D^(-1/2)=0.3015113446 | 19/132 | -1/11 |
| 48 | 5 | 24 | 11 | 9 | D^(-1/2)=0.3015113446 | 23/132 | -1/11 |
| 144 | 1 | 24 | 11 | -9 | D^(-1/2)=0.3015113446 | 29/44 | -1/11 |
| 176 | 1 | 88 | 3 | -1 | D^(-1/2)=0.5773502692 | 11/36 | -11/9 |
| 528 | 1 | 264 | 1 | 0 | D^(-1/2)=1.0 | 1/3 | -11 |
| 528 | 5 | 264 | 1 | 158 | D^(-1/2)=1.0 | 2/3 | -11 |

## Caveats / labels
- C depends on the choice of γ (b,d) through e(−B/(24D)) — convention fixed above; a different representative shifts the phase by a root of unity consistent with cusp width. 
- Branch convention: principal √ in Thm 2.1 assumed as stated in Bringmann–Ono; results are numerical (float, phases rationalized with denominator ≤10⁴, all land on 1/(24·D·k)-type rationals). Promotion to Written requires a closed-form (Dedekind-sum/Rademacher-style) proof: invented pending mathematical proof for any closed-form generalization beyond the table.
- Primary Zwegers 2001 Contemp. Math. paper not fetched (cited via B–O).

## Closed vs ABSENT
CLOSED (numerical, cite-grounded on B–O Thm 2.1): ζ/C for all 17 f-type non-∞ cusp representatives; f-/ω-type split now verified (upgrades prior invented label). 
ABSENT: closed-form ζ(a/c) proof; rigorous error bounds; direct check of primary Zwegers 2001.
β_s=π/√(6s), A_s=√s/2, α=−1/2: remain invented pending mathematical proof. Note for path: dominant non-∞ cusp exponent equals −s at c=144s/… with D=1 (same as ∞), so circle-method main term is shared across D=1 cusps — path advanced, NOT Written.
