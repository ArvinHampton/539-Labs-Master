# M2a/M2b: t^{1/2} Phi_orth radial constancy and value; arg x
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order5/scripts')
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from lib5mp import A012mp, Fr, PIECES
from symbols import sym_pair
x=Fr(sys.argv[1]); xf=float(x)
A=np.array([[2,7],[7,7]]); h1=np.array([-1.,1.])/math.sqrt(2.5); hp=np.array([-7.,2.])/math.sqrt(35)
L=math.acosh(-(h1@A@hp)/2)
g,wq=np.polynomial.legendre.leggauss(24); mus=(g+1)/2*L; wq=wq/2*L
comps=[sym_pair('K2',i) for i in range(35)]; comps=[c for c in comps if c[0][0].denominator>1 and c[0][1].denominator>1][:2]
out={'x':str(x),'rows':[]}
for al,be in comps:
    b0,b1=float(be[0]),float(be[1]); vals=[]
    for t in (2e-3,1e-3,5e-4):
        y=t/(2*math.pi); r=int(math.sqrt(300/t))+5; tot=0j
        for na in range(-r,r+1,96):
            n,k=np.meshgrid(np.arange(na,min(na+96,r+1)),np.arange(-r,r+1),indexing='ij')
            n1=float(al[0])+n; n2=float(al[1])+k; Q=n1*n1+7*n1*n2+3.5*n2*n2
            ph=np.exp(2j*np.pi*(Q*xf+n1*(2*b0+7*b1)+n2*(7*b0+7*b1)))
            for mu,w in zip(mus,wq):
                z=(math.sinh(L-mu)*h1+math.sinh(mu)*hp)/math.sinh(L); Az=A@z
                Bz=n1*Az[0]+n2*Az[1]
                tot+=w*(ph*np.exp(-2*np.pi*y*(Q+Bz*Bz/2))).sum()
        vals.append(math.sqrt(y)*tot*math.sqrt(t))
    # predicted: mean_N f via A0 of the full plane = mean f; use A0 of orthant piece / area
    m=x.denominator; N=2*m
    nn,kk=np.meshgrid(np.arange(N),np.arange(N),indexing='ij'); n1=float(al[0])+nn; n2=float(al[1])+kk
    Q=n1*n1+7*n1*n2+3.5*n2*n2; meanf=np.exp(2j*np.pi*(Q*xf+n1*(2*b0+7*b1)+n2*(7*b0+7*b1))).mean()
    pred=(2*math.pi)**-0.5*(2*math.pi/math.sqrt(35))*L*meanf
    sc=max(1e-12,abs(pred))
    rw=dict(vals=[[v.real,v.imag] for v in vals],pred=[pred.real,pred.imag],const_dev=max(abs(v-vals[0]) for v in vals)/max(1e-12,abs(vals[0])) if abs(vals[0])>1e-12 else max(abs(v) for v in vals),
            rel_err=max(abs(v-pred) for v in vals)/sc if abs(pred)>1e-12 else max(abs(v) for v in vals))
    out['rows'].append(rw); print(rw,flush=True)
out['M2ab']='pass' if all(r['const_dev']<=1e-8 and r['rel_err']<=1e-8 for r in out['rows']) else 'FAIL'
json.dump(out,open('../data/m2phi_%s.json'%str(x).replace('/','-'),'w'),indent=1); print(out['M2ab'])
