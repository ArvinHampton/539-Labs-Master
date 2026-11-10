# Local-derived (t4436, branch Oc-3 / Oc-1 identification test). For every squarefree t <= 400: dimension of the subspace of
#   S = S_{3/2}(Gamma0(196), chi_28) and of K = ker T(9)  (= W4)
# consisting of forms whose coefficients c(n), n <= B, vanish unless n lies in t*(square). The R8 object (Continue_Resolution_Residual_
# Shadow_Xi_2026-08-23.md, 552541cf..., lines 20-24) is built from unary series sum (n+a) q^{(n+a)^2} (or chi-twisted analogues); any
# rescaling q -> q^t keeps the support inside one square class t*(square). A zero dimension here for K proves (exact linear algebra, no
# Sturm bound needed) that no nonzero element of K has such a support.
import cypari2; pari=cypari2.Pari(); pari.allocatemem(3*10**9)
P=lambda s: pari(s)
B=1200
P(f"m=mfinit([196,3/2,28],1); Bh=mfbasis(m); d=mfdim(m); C=matconcat(vector(d,j,mfcoefs(Bh[j],{B})~)); K=matker(mfheckemat(m,9))")
res=[]
for t in range(1,401):
    if not int(P(f"issquarefree({t})")): continue
    P(f"rows=select(n->!(n%{t}==0 && issquare(n/{t})),vector({B},n,n)); Cn=matrix(#rows,d,i,j,C[rows[i]+1,j])")
    dS=int(P("#matker(Cn)")); dK=int(P("#matker(Cn*K)"))
    res.append((t,dS,dK))
print(f"B = {B}; squarefree t <= 400 tested: {len(res)}")
print("t with dim_S > 0:", [(t,dS) for t,dS,dK in res if dS>0])
print("t with dim_K > 0:", [(t,dK) for t,dS,dK in res if dK>0])
print("max dim_K over all t:", max(dK for _,_,dK in res))
