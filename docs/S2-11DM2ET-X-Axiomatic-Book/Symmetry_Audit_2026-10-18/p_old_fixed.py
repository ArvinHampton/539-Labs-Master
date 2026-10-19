# (a) identify the complement as the p-local-invariant subspace: F = {v in sector : T_p v = v, S T_p S^-1 v = v},
# T_p = T^c with c≡1 mod N_p, c≡0 mod N/N_p (N = Kbig, multiple of ord T). <T_p, S T_p S^-1> generates the image of SL2(Z_p)-factor.
import sys, json
src=open('sec_fixed.py').read(); src=src[:src.index('fac=Td.charpoly()')]
exec(src)
from sympy.ntheory.modular import crt
p=[q for q,e in sympy.factorint(s*(s-2)).items() if e>=2 and q!=2][0]
Np=p**sympy.multiplicity(p,Kbig); c=int(crt([Np,Kbig//Np],[1,0])[0])
def mpow(M,e):
    R=Id_=flint.nmod_mat(d,d,[int(i==j) for i in range(d) for j in range(d)],ell); B_=M
    while e:
        if e&1: R=R*B_
        B_=B_*B_; e>>=1
    return R
Id=flint.nmod_mat(d,d,[int(i==j) for i in range(d) for j in range(d)],ell)
Tp=mpow(Td,c); Sinv=Sd.inv(); U=Sd*Tp*Sinv
st=flint.nmod_mat(2*d,d,[int(M_[i,j]) for M_ in (Tp-Id,U-Id) for i in range(d) for j in range(d)],ell)
Fx,f=st.nullspace()
Fk=flint.nmod_mat(d,f,[int(Fx[i,j]) for i in range(d) for j in range(f)],ell)
SF=Sd*Fk; TF=Td*Fk
r=flint.nmod_mat(d,3*f,[int(M_[i,j]) for i in range(d) for M_ in (Fk,SF,TF) for j in range(f)],ell).rank()
# also the p-local "odd" check: eigenvalues of T_p on sector -> p-adic orbit sizes
res={"s":s,"p":p,"Np":Np,"c":c,"sector_dim":d,"p_invariant_dim":f,"rank[F,SF,TF]":r,
     "pred_3(s-1)/2":3*(s-1)//2,"ratio_sector_over_F":d/f if f else None,"pred_(p^2+1)/2":(s+1)/2}
print(res); json.dump(res,open(f"p_old_fixed_{s}_{sys.argv[2]}.json","w"),indent=1)
