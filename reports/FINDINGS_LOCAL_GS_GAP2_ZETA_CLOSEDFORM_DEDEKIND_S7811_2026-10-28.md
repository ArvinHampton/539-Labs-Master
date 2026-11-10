# FINDINGS — Local: Gap 2 ζ closed form via Dedekind sums, g_s=f(q^s), s∈{7,8,11} — 2026-10-28
Status: PARTIAL. Builds on db77a8e0… (not rewritten); 7b0eb063… / 595d6102… untouched. tip_touched NO. Kerr BLOCKED.

## Result (exact-rational verified, 17/17 f-type cusps; 278/278 γ' representatives for ρ₀₀)
Notation as db77a8e0…: γ'=[[p,x],[r,y]], p=24sa/A, r=c/A, D=24s/A, B from U=γ'^{-1}[[24s,0],[0,1]]γ.
(i) Algebraic identity (proof-grade, elementary): bottom row of γ'U equals (c,d) ⇒ r·w+y=(cτ+d)/D, w=(Aτ+B)/D; hence the chained √ factor/√(cτ+d)=e^{-iπ/4}·D^{-1/2} (principal branch, Im>0). This PROVES |C|=D^{-1/2} given B–O Thm 2.1.
(ii) Phase (numerically exact on all tested cases, NOT proved): ρ(γ')₀₀·√(−i(rw+y)) = σ_r·ε(γ')^{-1}, where ε is the Dedekind eta multiplier
   ε(γ')=exp(πi[(p+y)/(12r) − s(y,r)]), s(h,k)=Σ_{n=1}^{k−1}((n/k))((hn/k)) (Rademacher–Grosswald, Dedekind Sums, Carus Math. Monogr. 16, 1972; Apostol, Modular Functions & Dirichlet Series, Thm 3.4),
   σ_r=−1 for r=2, +1 for r=6 (only r∈{2,6} occur for s∈{7,8,11}).
(iii) Closed form:  C(a/c) = σ_r · D^{-1/2} · e( −(p+y)/(24r) + s(y,r)/2 − 1/8 − B/(24D) ).
   Reproduces every arg C in the db77a8e0… table exactly as rationals (script work/cf.py; ρ₀₀ check work/dz.py).
Interpretation: F₀=q^{-1/24}f(q) transforms on these γ'∈Γ₀(2) like η^{-1} up to σ_r — consistent with the classical Andrews (Amer. J. Math 88, 1966) / Dragonette (TAMS 72, 1952) transformation of f(q) involving ω_{h,k}=exp(πi s(h,k)) (as quoted in Bringmann–Ono, Annals 171 (2010) "Dyson's ranks and Maass forms"); not re-fetched this run — cite via secondary memory, label invent-pending until fetched.

## Still ABSENT
- Proof of (ii) for general γ' (sign σ_r rule beyond r∈{2,6}; a general proof would compose Thm 2.1 along the Euclid word = Rademacher-type cocycle argument — not written).
- Primary Zwegers Contemp. Math. 291 (2001) 269–277: not fetched this run.
- Rigorous error bounds.
## β/A path
Not moved: β_s=π/√(6s), A_s=√s/2, α=−1/2 remain invent-pending. (|C|=D^{-1/2} now proof-grade given B–O Thm 2.1, which modestly firms the cusp-weight input.)
