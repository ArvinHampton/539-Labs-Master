# Route B: B1 (Psi0 = y^{-1/2} Phi0, |tau| law), B2 (y^{1/2} Theta_E)
from common import *
import json
mp.mp.dps=20; M=Mmat(); A=((2,7),(7,7))
Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
L2=mp.log(6+mp.sqrt(35)); ch=[mp.mpf(-1)/mp.sqrt(2.5),1/mp.sqrt(mp.mpf(2.5))]; e2h=[mp.mpf(0),1/mp.sqrt(mp.mpf(3.5))]
xs,ws=mp.gauss_legendre if False else (None,None)
import numpy as np
gx,gw=np.polynomial.legendre.leggauss(40)
nodes=[(L2*(mp.mpf(float(u))+1)/2, L2*mp.mpf(float(w))/2) for u,w in zip(gx,gw)]
zf=lambda m:[mp.cosh(m)*ch[i]+mp.sinh(m)*e2h[i] for i in range(2)]
Z=[(zf(m),w) for m,w in nodes]
def Psi0(al,be,tau):
    y=tau.imag; x=tau.real; s=mp.mpc(0)
    for n in range(-12,13):
        for k in range(-12,13):
            nu=(al[0]+n,al[1]+k); Q=Fr(Bf(nu,nu),2); nm=[fm(nu[0]),fm(nu[1])]
            ph=ef(Bf(nu,be))*mp.expjpi(2*fm(Q)*x)
            acc=0
            for z,w in Z:
                sv=Bf(nm,z); K=2*fm(Q)+sv*sv
                if mp.pi*y*K<70: acc+=w*mp.exp(-mp.pi*y*K)
            if acc: s+=ph*acc
    return s   # = y^{-1/2} Phi0
sgn=lambda v:(v>0)-(v<0)
cE=lambda nu: Fr(1+sgn(nu[0])*sgn(nu[1]),2)
out={}
c=lambda t: abs(t)/mp.sqrt(35)
mx=lambda v:max(abs(z) for z in v)
r1=0;r2=0
tb=[tables(A,al,be,45,12,cE) for al,be in pairs]
for t in T4:
    vs=mp.matrix([Psi0(al,be,-1/t) for al,be in pairs]); vt=mp.matrix([Psi0(al,be,t) for al,be in pairs])
    r1=max(r1,mx(vs-c(t)*(M*vt))/mx(vt))
    es=mp.matrix([mp.sqrt((-1/t).imag)*evalt(D,-1/t) for D in tb]); et=mp.matrix([mp.sqrt(t.imag)*evalt(D,t) for D in tb])
    r2=max(r2,mx(es-c(t)*(M*et))/mx(et)); print(t,mp.nstr(r1,4),mp.nstr(r2,4),flush=True)
out=dict(B1=mp.nstr(r1,4),B1_verdict='pass' if r1<=1e-12 else ('FAIL' if r1>=1e-4 else 'inconclusive'),
         B2=mp.nstr(r2,4),B2_verdict='FAIL (as predicted)' if r2>=1e-4 else ('pass (UNEXPECTED)' if r2<=1e-12 else 'inconclusive'))
print(out); json.dump(out,open('../data/b.json','w'),indent=1)
