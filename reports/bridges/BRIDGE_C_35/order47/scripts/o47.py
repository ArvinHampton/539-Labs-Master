# order47: exact certification in Z[zeta_9800]. PREREG hashed first. Integer arithmetic only for verdicts.
import sys, json
from collections import defaultdict
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import Fr
from symbols import FAM, sym_pair, S_rows, reduce, L
assert L==9800
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]; N=105
Sr=S_rows()   # Sr[j][k] = list of exponents
Mt={(j,k):list(es) for j,d in enumerate(Sr) for k,es in d.items()}
def mono(gm):
    p=[None]*N; g=[None]*N
    for j,(al,be) in enumerate(pairs):
        ga=tuple(sum(Fr(gm[r][c])*al[c] for c in range(2)) for r in range(2)); gb=tuple(sum(Fr(gm[r][c])*be[c] for c in range(2)) for r in range(2))
        p[j],g[j]=reduce(ga,gb)
    return p,g
# Pi: (al,be)->(al,-be)
pi=[None]*N; gp=[None]*N
for j,(al,be) in enumerate(pairs): pi[j],gp[j]=reduce(al,(-be[0],-be[1]))
Pm,Pg=mono([[-1,0],[0,-1]])
# Phi_70 integer coefficients (monic, degree 24)
import sympy
y=sympy.symbols('y'); phi=[int(c) for c in sympy.Poly(sympy.cyclotomic_poly(70,y),y).all_coeffs()][::-1]; D=len(phi)-1; assert D==24
def is_zero(cvec):   # cvec: dict exponent->int coefficient
    by=defaultdict(lambda: defaultdict(int))
    for e,c in cvec.items():
        if c: e%=L; by[e%140][e//140]+=c
    for r,poly in by.items():
        a=[0]*70
        for q,c in poly.items(): a[q]+=c
        for d in range(69,D-1,-1):   # reduce mod monic phi
            c=a[d]
            if c:
                for t in range(D+1): a[d-D+t]-=c*phi[t]
        if any(a[:D]): return False
    return True
def rowmul(A,B):  # A,B dict (j,k)->list of exponents (each term coefficient 1); returns dict (j,k)->Counter of exponents
    Brow=defaultdict(list)
    for (l,k),es in B.items(): Brow[l].append((k,es))
    out=defaultdict(lambda: defaultdict(int))
    for (j,l),e1s in A.items():
        for k,e2s in Brow[l]:
            d=out[(j,k)]
            for a in e1s:
                for b in e2s: d[(a+b)%L]+=1
    return out
def check(prod,target):  # target dict (j,k)->dict exponent->int
    bad=0
    for j in range(N):
        for k in range(N):
            c=defaultdict(int)
            for e,v in prod.get((j,k),{}).items(): c[e]+=v
            for e,v in target.get((j,k),{}).items(): c[e]-=v
            if not is_zero(c): bad+=1
    return bad
conjM={(j,k):[(-e)%L for e in es] for (j,k),es in Mt.items()}
PiM={(j,k):[(gp[j]+e)%L for e in Mt[(pi[j],k)]] for j in range(N) for k in range(N) if (pi[j],k) in Mt}   # (Pi M)_{jk}=zeta^{gp_j} M_{pi(j),k}
MdagT={(k,j):[(-e)%L for e in es] for (j,k),es in Mt.items()}   # M^dagger
out={}
# control (a): M^2 = 35 P
t={(j,Pm[j]):{Pg[j]:35} for j in range(N)}
out['control_M2_35P_bad']=check(rowmul(Mt,Mt),t)
# X2: M M^dagger = 35 I ; control (b): 34 I
MMd=rowmul(Mt,MdagT)
out['X2_bad']=check(MMd,{(j,j):{0:35} for j in range(N)})
out['control_wrong_34I_bad']=check(MMd,{(j,j):{0:34} for j in range(N)})
# X1: conj(M) Pi M = 35 Pi
out['X1_bad']=check(rowmul(conjM,PiM),{(j,pi[j]):{gp[j]:35} for j in range(N)})
out['X1']='PASS' if out['X1_bad']==0 else 'FAIL'; out['X2']='PASS' if out['X2_bad']==0 else 'FAIL'
out['controls_ok']=out['control_M2_35P_bad']==0 and out['control_wrong_34I_bad']>0
print(out); json.dump(out,open('../data/o47.json','w'),indent=1)
