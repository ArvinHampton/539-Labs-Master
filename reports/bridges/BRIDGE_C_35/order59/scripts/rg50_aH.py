import sys,os,json,math; sys.path.insert(0,os.path.dirname(__file__)); sys.dont_write_bytecode=True
import numpy as np, mpmath as mp
from em import res
mp.mp.dps=30; sp=mp.sqrt(mp.pi)
c={'a_H':sp*(mp.sqrt(1190)-17*mp.sqrt(14))/170,'K1_signflip':sp*(mp.sqrt(1190)+17*mp.sqrt(14))/170,'K2_sqrt1191':sp*(mp.sqrt(1191)-17*mp.sqrt(14))/170}
def Hs(t):
    nmax=int(math.sqrt(80/t))+5; n=np.arange(-nmax,nmax+1,dtype=float)[:,None]; k=n.T
    W=0.5*(np.sign(5*n)-np.sign(-n-21*k)); Q=np.where(W!=0,n*n+7*n*k+3.5*k*(k+1),0.0); return float(np.sum(W*np.exp(-t*Q)))
H={t:Hs(t) for t in [1e-4,2.5e-5]}; out={'res_H_t^-1/2':str(res['H_s'][1]),'res_H_t^-1':str(res['H_s'][0])}
for nm,a in c.items():
    A1=abs(mp.mpf(res['H_s'][1])-a); rr={t:(H[t]-float(a)/math.sqrt(t))/math.sqrt(t) for t in H}
    A2=abs(rr[1e-4]-rr[2.5e-5]); out[nm]={'value':str(a),'A1_diff':mp.nstr(A1,5),'A2_ratio':rr,'A2_drift':A2,'A1':bool(A1<mp.mpf('1e-25')),'A2':bool(A2<1e-3)}
ok=out['a_H']['A1'] and out['a_H']['A2'] and not any(out[k]['A1'] or out[k]['A2'] for k in ['K1_signflip','K2_sqrt1191'])
out['RG50']='PASS' if ok else 'FAIL'; print(json.dumps(out,indent=1,default=str)); json.dump(out,open('data/rg50.json','w'),indent=1,default=str)
