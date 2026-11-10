# M2: radial data of Theta_E vs prediction; Phi_orth radial constancy. arg: x
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order5/scripts')
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from lib5mp import A012mp, Fr
from symbols import sym_pair
x=Fr(sys.argv[1]); m=x.denominator; xf=float(x)
comps=[sym_pair('K2',i) for i in range(35)]
comps=[c for c in comps if c[0][0].denominator>1 and c[0][1].denominator>1][:4]
ts=[2.0**-j*0.02/(2*m)**2 for j in range(6)]
L=math.acosh(7/(2*math.sqrt(3.5)))
out={'x':str(x),'rows':[]}
for al,be in comps:
    n0=math.floor(-al[0])+1; k0=math.floor(-al[1])+1; n1=math.ceil(-al[0])-1; k1=math.ceil(-al[1])-1
    pcs=[(Fr(1),(n0,k0),((1,0),(0,1))),(Fr(1),(n1,k1),((-1,0),(0,-1)))]
    pred=[complex(v) for v in A012mp(al,be,x,pieces=pcs,walls=[])]
    b0,b1=float(be[0]),float(be[1]); acc=np.zeros(6,complex)
    for ti,t in enumerate(ts):
        r=int(math.sqrt(150/t))+5
        for sgn_ in (1,-1):
            for na in range(0,r,128):
                nn=np.arange(na,min(na+128,r)); kk=np.arange(0,r)
                n,k=np.meshgrid(nn,kk,indexing='ij')
                if sgn_==1: n=n+n0; k=k+k0
                else: n=n1-n; k=k1-k
                n1f=float(al[0])+n; n2f=float(al[1])+k; Q=n1f*n1f+7*n1f*n2f+3.5*n2f*n2f
                acc[ti]+=(np.exp(-t*Q)*np.exp(2j*np.pi*(Q*xf+n1f*(2*b0+7*b1)+n2f*(7*b0+7*b1)))).sum()
    T=np.array(ts); X=np.stack([1/T,1/np.sqrt(T),np.ones(6),np.sqrt(T),T],1)
    c=np.linalg.lstsq(X,acc,rcond=None)[0]
    errs=[abs(c[i]-pred[i])/max(1,abs(pred[i])) for i in range(3)]
    # M2a identity check: A0_pred vs mean f*2L/sqrt35
    rw=dict(al=[str(al[0]),str(al[1])],pred=[[v.real,v.imag] for v in pred],meas=[[v.real,v.imag] for v in c[:3]],errs=errs)
    out['rows'].append(rw); print(rw,flush=True)
out['max_err']=max(max(r['errs']) for r in out['rows']); out['M2_theta']='pass' if out['max_err']<=1e-5 else 'FAIL'
json.dump(out,open('../data/m2_%s.json'%str(x).replace('/','-'),'w'),indent=1); print(out['max_err'],out['M2_theta'])
