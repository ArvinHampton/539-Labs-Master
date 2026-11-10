# order53 PREREG — RG45b (and conditional RG46)
Hashed before any test. CORE_FREEZE; new files only; read-only on order5/order18/order52; MAPS_CANDIDATES untouched; no Ξ/Π/α1 invented; 35-component law vector; RG* labels.
## RG45b: exact extraction of (m_ℓ, θ, character) for walls (−c1,c2)
Sources: order5 §1.4(ii) (line summation parallel to c_j^⊥), order5 RESULTS completion constants, order18 a2.py lines() (written line decomposition, read-only exec of lines 1–30 only).
Claim to test: lines parallel to c_j^⊥ are u1=(0,1), u2=(21,−1); line label ℓ = B(c_j,ν) ∈ θ_j+Z with θ_1=α_1(companion shift), θ_2=α_1+21α_2; m_ℓ = mean over one period of the companion phase f along the line; character = f = e(B(ν,β)) phase from order2 lib2.
Predefined tests (all exact/integer; PASS iff all true, Category A):
- T1: B_lines(u1,(n,0))-type orthogonality: line direction has B(c1,u1)=0 and B(c2,u2)=0 in the order18 convention (B(c1,v)=v1, B(c2,v)=v1+21v2).
- T2: bijection Z²→{(ℓ,b)}: v=(n,0)+b u1 and v=(m,0)+b u2 each hit every v in [−30,30]² exactly once.
- T3: for all 105 companions × all 216 XS: a period P exists on each wall line (order18 period()), and m_ℓ is P_ℓ-periodic in ℓ: |m_{ℓ+N}−m_ℓ| ≤1e−12 with N = lcm of the u-periods over ℓ∈{0..N−1} sample (N := period along the transverse coordinate).
- T4: m_ℓ independent of base point on the line (shift by u): ≤1e−12.
Fail any → document obstruction.
## RG46: run iff RG45b yields an explicit Ξ_compl or A1−Ξ_compl object. Otherwise SKIPPED.
