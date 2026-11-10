# M1: Theta_E = H(Phi_orth) coefficient identity, mpmath
import sys, json, math; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp, numpy as np
from fractions import Fraction as Fr
from symbols import FAM, sym_pair
mp.mp.dps=25
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
c1=(mp.mpf(-1),mp.mpf(1)); cp=(mp.mpf(-7),mp.mpf(2))
h1=tuple(v/mp.sqrt(mp.mpf(5)/2) for v in c1); hp=tuple(v/mp.sqrt(35) for v in cp)
L=mp.acosh(-Bf(h1,hp)/2)
res={'L':mp.nstr(L,20),'half_log_eps':mp.nstr(mp.log(6+mp.sqrt(35))/2,20)}
sgn=lambda v:(v>0)-(v<0)
def weight(nu,N,y):
    b1=Bf(nu,h1); b2=Bf(nu,hp)
    zh=lambda m: tuple((mp.sinh(L-m)*h1[i]+mp.sinh(m)*hp[i])/mp.sinh(L) for i in range(2))
    f=lambda m: mp.exp(-mp.pi*y*Bf(nu,zh(m))**2)
    den=b2-b1*mp.cosh(L); pts=[mp.mpf(0),L]
    if den!=0:
        th=-b1*mp.sinh(L)/den
        if abs(th)<1:
            mu=mp.atanh(th)
            if 0<=mu<=L:
                d=10/mp.sqrt(N*y); pts=sorted(set([mp.mpf(0),L]+[p for p in (mu-d,mu,mu+d) if 0<p<L]))
    if len(pts)==2 and mp.pi*y*min(b1*b1,b2*b2)>200: return mp.mpf(0)
    return 2*mp.sqrt(N*y)*mp.quad(f,pts)
out=[]; maxd=0
for j,(al,be) in enumerate(pairs):
    cE={}; cF={}
    for n in range(-60,61):
        for k in range(-60,61):
            nu=(al[0]+n,al[1]+k); Q=Fr(Bf(nu,nu),2)
            if not (0<Q<=8): continue
            ph=mp.expjpi(2*mp.mpf(Fr(Bf(nu,be)).numerator)/Fr(Bf(nu,be)).denominator)
            ev=Fr(1+sgn(nu[0])*sgn(nu[1]),2)
            if ev: cE[Q]=cE.get(Q,0)+ev*ph
            nm=(mp.mpf(nu[0].numerator)/nu[0].denominator,mp.mpf(nu[1].numerator)/nu[1].denominator); Nm=mp.mpf(Q.numerator)/Q.denominator
            w1=weight(nm,Nm,mp.mpf(10)**4); 
            if w1==0: continue
            w2=weight(nm,Nm,2*mp.mpf(10)**4); w=2*w2-w1
            cF[Q]=cF.get(Q,0)+w*ph
    keys=set(cE)|set(cF)
    d=max([abs(cE.get(q,0)-cF.get(q,0)) for q in keys]+[mp.mpf(0)]); maxd=max(maxd,d)
    out.append(dict(j=j,nQ=len(keys),maxdiff=mp.nstr(d,5)))
    print(j,len(keys),mp.nstr(d,5),flush=True)
res['max_diff']=mp.nstr(maxd,5); res['M1']='pass' if maxd<=1e-7 else ('FAIL' if maxd>1e-4 else 'inconclusive'); res['per']=out
json.dump(res,open('../data/m1.json','w'),indent=1); print(res['max_diff'],res['M1'],res['L'],res['half_log_eps'])
