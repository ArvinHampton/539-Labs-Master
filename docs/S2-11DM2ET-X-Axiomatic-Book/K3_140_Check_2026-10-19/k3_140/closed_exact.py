# Exact (Z[zeta_280]) verification of the closed-form intertwiner X e_z = u_{[z],0} + e(B(z,beta1)) u_{[z],beta1}
# plus: gamma on A_{N2} per local component; explicit T = N2^perp in Lambda_K3.
import pickle, json, numpy as np, sympy as sp
from fractions import Fraction as Fr
from collections import Counter
R=pickle.load(open('rev_s7_exact.pkl','rb')); IDX={l:i for i,l in enumerate(R['labels'])}; N=140
Xp=pickle.load(open('X_explicit.pkl','rb')); A=sp.Matrix([[2,7],[7,7]]); D=70; BES=Xp['BES']
Z=[sp.Matrix([sp.Rational(v) for v in z]) for z in Xp['Z']]; q=[Fr(x) for x in Xp['q']]
B=lambda u,v: Fr(str((u.T*A*v)[0]))
b=[[B(z,w)%1 for w in Z] for z in Z]
mb=sp.Matrix([sp.Rational(BES[1][0],D),sp.Rational(BES[1][1],D)])
Xe={}
for k,z in enumerate(Z):
    a=tuple(Xp['alpha'][k]); Xe[(IDX[(a,BES[0])],k)]=Fr(0); Xe[(IDX[(a,BES[1])],k)]=B(z,mb)%1
M_=280; x=sp.Symbol('x')
Phi=[int(c) for c in sp.Poly(sp.cyclotomic_poly(M_,x),x).all_coeffs()[::-1]]; dP=len(Phi)-1
def is_zero(v):
    v=list(v)
    for i in range(len(v)-1,dP-1,-1):
        c=v[i]
        if c:
            for j in range(len(Phi)): v[i-dP+j]-=c*Phi[j]
    return not any(v[:dP])
add=lambda v,r,c=1: v.__setitem__(int((Fr(r)%1)*M_)%M_, v[int((Fr(r)%1)*M_)%M_]+c)
Xrows={}
for (i,k),c in Xe.items(): Xrows.setdefault(i,{})[k]=c
Sinv={}
for (j,i),r in R['S'].items(): Sinv.setdefault(i,[]).append((j,(-r)%1))   # sqrt35*S_lab^{-1}[i,j] = e(-r_ji)
Trow={i:(j,r) for (i,j),r in R['T'].items()}
badS=badT=0
for i in range(N):
    for k in range(N):
        v=[0]*M_
        for y,c in Xrows.get(i,{}).items(): add(v,c-b[y][k])          # 2sqrt35 (X S_W)[i,k]
        for j,r in Sinv[i]:
            if k in Xrows.get(j,{}): add(v,r+Xrows[j][k],-2)          # 2sqrt35 (S_lab^{-1} X)[i,k]
        if not is_zero(v): badS+=1
        v=[0]*M_
        if k in Xrows.get(i,{}): add(v,Xrows[i][k]+q[k])
        j,r=Trow[i]
        if k in Xrows.get(j,{}): add(v,r+Xrows[j][k],-1)
        if not is_zero(v): badT+=1
# invertibility: per alpha 2x2 block [[1,1],[e(B(z,b1)), e(B(z',b1))]], z'=z+v (v=(0,1)); det = e(B(z',b1))-e(B(z,b1)) != 0 iff B(v,b1) not in Z
v0=sp.Matrix([0,1]); Bvb=B(v0,mb)%1
out={'exact_S_failures':badS,'exact_T_failures':badT,'B(v,beta1) mod 1':str(Bvb),'invertible':Bvb!=0}
# gamma on A_{N2}
g=sp.Matrix([[-1,-7],[2,13]]); assert g.T*A*g==A
Bm=sp.Matrix([[1,0],[0,2]]); assert all(v.is_integer for v in Bm.inv()*g*Bm)   # preserves L_ev
G2=Bm.T*A*Bm
def cls(z):  # class of z (standard coords) in L_ev'/L_ev
    y=Bm.inv()*z; return tuple(Fr(str(t))%1 for t in y)
keys=[cls(z) for z in Z]; pos={k:i for i,k in enumerate(keys)}
perm=[pos[cls(g*z)] for z in Z]
order=lambda z: next(n for n in range(1,141) if all(Fr(str(t)).denominator==1 for t in Bm.inv()*(n*z)))
def local(z,pp):   # component: z multiplied by cofactor to land in p-part
    m=140; e={2:4,5:5,7:7}[pp]; return (m//e)*z
res={}
for pp in (2,5,7):
    comp=[k for k,z in enumerate(Z) if all(Fr(str(t)).denominator==1 for t in Bm.inv()*({2:4,5:5,7:7}[pp]*z))]
    plus=all(perm[k]==k for k in comp); minus=all(keys[perm[k]]==tuple((-t)%1 for t in keys[k]) for k in comp)
    res[pp]={'|A_p|':len(comp),'gamma=+1':plus,'gamma=-1':minus}
out['gamma_on_A_N2_local']=res
out['gamma_is_pm1_on_A']={'+1':all(perm[k]==k for k in range(N)),'-1':all(keys[perm[k]]==tuple((-t)%1 for t in keys[k]) for k in range(N))}
g2=g*g; out['gamma^2_is_+1']=all(cls(g2*z)==cls(z) for z in Z)
# N2 ~ <2> + <-70>:  basis change
P=sp.Matrix([[1,-7],[0,1]]); out['N2_diagonalised']=str(P.T*G2*P)
# explicit embedding into U+U: e1+f1 (norm 2), e2-35 f2 (norm -70); complement e1-f1 (-2), e2+35f2 (70)
U=sp.Matrix([[0,1],[1,0]]); UU=sp.diag(U,U)
n1=sp.Matrix([1,1,0,0]); n2=sp.Matrix([0,0,1,-35]); t1=sp.Matrix([1,-1,0,0]); t2=sp.Matrix([0,0,1,35])
out['embedding_norms']=[int((n1.T*UU*n1)[0]),int((n2.T*UU*n2)[0]),int((t1.T*UU*t1)[0]),int((t2.T*UU*t2)[0])]
out['orthogonality']=[int((a.T*UU*c)[0]) for a in (n1,n2) for c in (t1,t2)]
# complement of span(n1,n2) in U+U is exactly span(t1,t2): solve
Ms=sp.Matrix.hstack(n1,n2).T*UU; ker=Ms.nullspace(); kerZ=sp.Matrix.hstack(*ker)
out['complement_check']='span(t1,t2) has index 1 in (n1,n2)^perp' if abs(sp.Matrix.hstack(t1,t2).T*UU*sp.Matrix.hstack(t1,t2)).det()==140 else 'check'
# primitivity of span(n1,n2) in U+U: gcd of 2x2 minors of [n1 n2] = 1
Mn=sp.Matrix.hstack(n1,n2); minors=[Mn.extract([i,j],[0,1]).det() for i in range(4) for j in range(i+1,4)]
out['primitive_gcd_minors']=int(sp.gcd(minors))
Mt=sp.Matrix.hstack(t1,t2); out['T-part_primitive_gcd_minors']=int(sp.gcd([Mt.extract([i,j],[0,1]).det() for i in range(4) for j in range(i+1,4)]))
# discriminant forms: q_N2 on <2>+<-70> is x^2/4 - y^2/140; q of <-2>+<70> is -x^2/4 + y^2/140 = -q_N2 (identity map)
out['q_T_equals_minus_q_N2']='identity map on (Z/2 x Z/70): q_T(x,y)=-x^2/4+y^2/140 = -q_N2(x,y)'
json.dump(out,open('closed_exact.json','w'),indent=1,default=str); print(json.dumps(out,indent=1,default=str))
