# order6 S-law at interior tau, F2 identity, FD shadow tests
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from symbols import FAM, sym_pair, S_rows, L as LL
from lib6 import *
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
res={'axis_alphas':[ [str(a[0]),str(a[1])] for a,b in pairs if a[0].denominator==1 or a[1].denominator==1]}
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: M[j,kk]+=np.exp(2j*np.pi*e/LL)
rng=np.random.default_rng(5); taus=[]
while len(taus)<120:
    t=complex(rng.uniform(-0.45,0.45),rng.uniform(0.55,1.3))
    if 0.8<=abs(t)<=1.25: taus.append(t)
RES={}
for kind in ('Hhol','H','O','E','orth','full'):
    V=np.array([[series(al,be,t,kind) for al,be in pairs] for t in taus])
    W=np.array([[series(al,be,-1/t,kind) for al,be in pairs] for t in taus])
    pred=np.array([(t/math.sqrt(35))*(M@V[i]) for i,t in enumerate(taus)])
    RES[kind]=(W-pred); r=float(np.abs(W-pred).max()/max(1,np.abs(W).max())); res['r_'+kind]=r
    if kind in ('E','full'):
        V2=np.array([[series(al,be,t,kind,50) for al,be in pairs[:10]] for t in taus[:10]]); res['trunc_'+kind]=float(np.abs(V[:10,:10]-V2).max())
    print(kind,r,flush=True)
res['F2_maxdiff']=float(np.abs(RES['full']-0.5*RES['E']).max())
v=lambda r:'pass' if r<=1e-10 else ('FAIL' if r>1e-4 else 'inconclusive')
res['gating']=bool(res['r_H']<=1e-10 and res['r_Hhol']>1e-4)
for key,kind in (('O1','O'),('E1','E'),('O3','orth'),('F1','full')): res[key]=v(res['r_'+kind]) if res['gating'] else 'void'
res['F2']='pass' if res['F2_maxdiff']<=1e-10 else 'FAIL'
# FD
def dtb(al,be,t,kind,h=1e-5):
    f=lambda z: series(al,be,z,kind)
    return 0.5*((f(t+h)-f(t-h))/(2*h)+1j*(f(t+1j*h)-f(t-1j*h))/(2*h))
def mesh(al,be,tau,Lb=40):
    n,k=np.meshgrid(np.arange(-Lb,Lb+1),np.arange(-Lb,Lb+1),indexing='ij'); n1,n2=grid(al,n,k)
    b0,b1=float(be[0]),float(be[1]); return n1,n2,n1*(2*b0+7*b1)+n2*(7*b0+7*b1)
ee=lambda z,t: np.exp(2j*np.pi*z*t.real)*np.exp(-2*np.pi*z*t.imag)
def shadow_O(al,be,tau):
    n1,n2,Bb=mesh(al,be,tau); y=tau.imag; tot=0
    for sig,Qc,w,s,Qu in ((1,2.5,-n1,n1+n2,3.5),(-1,35.0,n2/2,n1+3.5*n2,1.0)):
        tot=tot+sig*math.sqrt(Qc)*(w*ee(Qu*s*s,tau)*np.exp(2j*np.pi*Bb)*np.conj(ee(Qc*w*w,tau))).sum()
    return -1j/(2*math.sqrt(y))*tot
def dE(a,y): return 1j*a/(2*math.sqrt(y))*np.exp(-np.pi*a*a*y)
def prod_E(al,be,tau):
    n1,n2,Bb=mesh(al,be,tau); y=tau.imag; Q=n1*n1+7*n1*n2+3.5*n2*n2
    a1=math.sqrt(10)*n1; a2=math.sqrt(35)*n2; E=lambda a: np.sign(a)*(1-erfc(SQ*np.abs(a)*math.sqrt(y)))
    with np.errstate(over='ignore',invalid='ignore'):
        term=0.5*(dE(a1,y)*E(a2)+E(a1)*dE(a2,y))*np.exp(-2*np.pi*Q*y)
    term=np.where(np.isfinite(term),term,0)
    return (term*np.exp(2j*np.pi*(Q*tau.real+Bb))).sum()
o2=[];e2=[]
for t in taus[:4]:
    for j in (0,7,40,52,80,101):
        al,be=pairs[j]
        d=dtb(al,be,t,'O'); s=shadow_O(al,be,t); o2.append(float(abs(d-s)/max(1e-12,abs(s))))
        d=dtb(al,be,t,'E'); s=prod_E(al,be,t); e2.append(float(abs(d-s)/max(1e-12,abs(s))))
res['O2_max']=max(o2); res['E2_max']=max(e2)
res['O2']='pass' if max(o2)<=1e-6 else 'FAIL'; res['E2']='pass' if max(e2)<=1e-6 else 'FAIL'
print(json.dumps(res,indent=1)); json.dump(res,open('../data/slaw.json','w'),indent=1)
