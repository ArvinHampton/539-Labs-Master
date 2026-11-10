# parity lemma check + candidate 1 + FD
import sys, json, math, numpy as np, mpmath as mp; sys.dont_write_bytecode=True
from lib7 import *
res={}
res['M2_minus_35P_float']=float(np.abs(M@M-35*P).max())
mp.mp.dps=30
Mm=mp.matrix([[mp.mpc(0)]*105 for _ in range(105)])
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: Mm[j,kk]+=mp.expjpi(mp.mpf(2*e)/LL)
Pm=mp.matrix([[mp.mpc(0)]*105 for _ in range(105)])
for j,(al,be) in enumerate(pairs):
    k,e=reduce(neg(al),neg(be)); Pm[j,k]=mp.expjpi(mp.mpf(2*e)/LL)
D=Mm*Mm-35*Pm; res['M2_minus_35P_mp30']=mp.nstr(max(abs(D[i,j]) for i in range(105) for j in range(105)),5)
print(res,flush=True)
T=taus(120,5)
def law_resid(kind):
    V=np.array([[series(al,be,t,kind) for al,be in pairs] for t in T])
    W=np.array([[series(al,be,-1/t,kind) for al,be in pairs] for t in T])
    pred=np.array([(t/math.sqrt(35))*(M@V[i]) for i,t in enumerate(T)])
    return W-pred, W
RE,WE=law_resid('E'); RG,WG=law_resid('G')
lam=-np.vdot(RG.ravel(),RE.ravel())/np.vdot(RG.ravel(),RG.ravel())
R=RE+lam*RG; W=WE+lam*WG
res['lambda_star']=[lam.real,lam.imag]
res['r_lambda0']=float(np.abs(RE).max()/max(1,np.abs(WE).max()))
res['r_lambda_star']=float(np.abs(R).max()/max(1,np.abs(W).max()))
res['C1']='fails as predicted' if res['r_lambda_star']>1e-4 else ('PASS (contradicts lemma)' if res['r_lambda_star']<=1e-10 else 'inconclusive')
# FD of F_lambda
from scipy.special import erfc
SQ=math.sqrt(math.pi)
def dtb_formula(al,be,tau,Lb=40):
    y=tau.imag; n,k=np.meshgrid(np.arange(-Lb,Lb+1),np.arange(-Lb,Lb+1),indexing='ij'); n1,n2=grid(al,n,k)
    Q=n1*n1+7*n1*n2+3.5*n2*n2; b0,b1=float(be[0]),float(be[1]); Bb=n1*(2*b0+7*b1)+n2*(7*b0+7*b1)
    a1=math.sqrt(10)*n1; a2=math.sqrt(35)*n2
    E=lambda a: np.sign(a)*(1-erfc(SQ*np.abs(a)*math.sqrt(y))); dE=lambda a: 1j*a/(2*math.sqrt(y))*np.exp(-np.pi*a*a*y)
    with np.errstate(over='ignore',invalid='ignore'):
        dp=0.5*(dE(a1)*E(a2)+E(a1)*dE(a2))+lam*(-np.pi*(10*n1*n1+35*n2*n2)*0.5j)*np.exp(-np.pi*y*(10*n1*n1+35*n2*n2))
        term=dp*np.exp(-2*np.pi*Q*y)
    term=np.where(np.isfinite(term),term,0)
    return (term*np.exp(2j*np.pi*(Q*tau.real+Bb))).sum()
fd=[]; h=1e-5
for t in T[:4]:
    for j in (0,7,40,52,80,101):
        al,be=pairs[j]; f=lambda z: series(al,be,z,'E')+lam*series(al,be,z,'G')
        d=0.5*((f(t+h)-f(t-h))/(2*h)+1j*(f(t+1j*h)-f(t-1j*h))/(2*h)); s=dtb_formula(al,be,t)
        fd.append(float(abs(d-s)/max(1e-12,abs(s))))
res['FD_max']=max(fd); res['FD']='pass' if max(fd)<=1e-6 else 'FAIL'
print(json.dumps(res,indent=1)); json.dump(res,open('../data/c1.json','w'),indent=1)
