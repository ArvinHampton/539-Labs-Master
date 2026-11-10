# C1: W2d rerun, metric |direct-glued|/sum|terms|; |B(c')|, |B(c1)| normalised; all 105, 3 tau, dps 30
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp; from fractions import Fraction as Fr; from symbols import FAM,sym_pair
mp.mp.dps=30
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
fm=lambda r: mp.mpf(r.numerator)/r.denominator; ef=lambda r: mp.expjpi(2*fm(Fr(r)%1))
cp=(mp.mpf(7)/mp.sqrt(35),mp.mpf(-2)/mp.sqrt(35)); ch=(mp.mpf(-1)/mp.sqrt(2.5),1/mp.sqrt(mp.mpf(2.5))); e2h=(mp.mpf(0),1/mp.sqrt(mp.mpf(3.5)))
E=lambda s,sp,tau: mp.exp(2j*mp.pi*(sp*sp*tau/4-s*s*mp.conj(tau)/4))
mx={'C1':0,'Bcp':0,'Bc1':0}; per=[]
for j,(al,be) in enumerate(pairs):
    bmin=mp.inf; cmax=0; amax=0
    for tau in (mp.mpc(0.1,0.9),mp.mpc(-0.3,1.2),mp.mpc(0.37,0.7)):
        d1=0;m1=0;d2=0;m2=0;gl=0
        for n in range(-10,11):
            for k in range(-10,11):
                nu=(al[0]+n,al[1]+k); nm=(fm(nu[0]),fm(nu[1])); p=ef(Bf(nu,be))
                s=Bf(nm,cp); sp=-Bf(nm,(1,0)); t=p*s*sp*E(s,sp,tau); d1+=t; m1+=abs(t)
                s=Bf(nm,ch); sp=Bf(nm,e2h); t=p*s*sp*E(s,sp,tau); d2+=t; m2+=abs(t)
        for k in range(-10,11):
            n2=al[1]+k
            for n in range(-60,61):
                w=al[0]+Fr(7,2)*n2+n
                if abs(w)>30: continue
                gl+=-2*mp.sqrt(35)*fm(w)*fm(n2)*E(mp.sqrt(35)*fm(n2),2*fm(w),tau)*ef(w*(2*be[0]+7*be[1])-Fr(35,2)*be[1]*n2)
        c=abs(d1-gl)/m1; a=abs(d1)/m1; b=abs(d2)/m2
        mx['C1']=max(mx['C1'],c); mx['Bcp']=max(mx['Bcp'],a); mx['Bc1']=max(mx['Bc1'],b); bmin=min(bmin,b); cmax=max(cmax,c); amax=max(amax,a)
    per.append([j,mp.nstr(cmax,3),mp.nstr(amax,3),mp.nstr(bmin,3)])
    if j%15==0: print(per[-1],flush=True)
res={k:mp.nstr(v,4) for k,v in mx.items()}
res['C1_verdict']='pass' if mx['C1']<=1e-25 else ('FAIL' if mx['C1']>1e-12 else 'inconclusive')
res['Bcp_zero']='pass' if mx['Bcp']<=1e-25 else 'FAIL'
res['control_Bc1_nonzero']='pass' if mx['Bc1']>1e-6 else 'FAIL (C1 invalid)'
res['per']=per; print({k:v for k,v in res.items() if k!='per'}); json.dump(res,open('../data/c1.json','w'),indent=1)
