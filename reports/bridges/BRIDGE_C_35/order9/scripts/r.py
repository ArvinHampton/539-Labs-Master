# R1 (Theta_E, orthants) / R2 (Theta_{C_arc}) radial fits with 7 terms on 8 points; args: mode x
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order5/scripts')
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from lib5mp import A012mp, Fr
from symbols import sym_pair
mode=sys.argv[1]; x=Fr(sys.argv[2]); m=x.denominator; xf=float(x)
comps=[c for c in (sym_pair('K2',i) for i in range(35)) if c[0][0].denominator>1 and c[0][1].denominator>1][:4]
ts=np.array([2.0**-j*0.02/(2*m)**2 for j in range(8)]); tmin=ts[-1]; Qmax=150/tmin
L=math.acosh(7/(2*math.sqrt(3.5)))
def accum(rows,acc,be):
    # rows: list of (nu1 scalar, nu2 array)
    b0,b1=float(be[0]),float(be[1])
    for n1,n2 in rows:
        Q=n1*n1+7*n1*n2+3.5*n2*n2; sel=Q<=Qmax
        if not sel.any(): continue
        n2=n2[sel]; Q=Q[sel]; w=np.exp(2j*np.pi*(Q*xf+n1*(2*b0+7*b1)+n2*(7*b0+7*b1)))
        E=np.exp(-tmin*Q)
        for jj in range(7,-1,-1): acc[jj]+=(w*E).sum(); E=E*E
out={'mode':mode,'x':str(x),'rows':[]}
for al,be in comps:
    acc=np.zeros(8,complex); a1,a2=float(al[0]),float(al[1])
    if mode=='R1':
        R=int(math.sqrt(Qmax))+3
        n0=math.floor(-al[0])+1; k0=math.floor(-al[1])+1; n1=math.ceil(-al[0])-1; k1=math.ceil(-al[1])-1
        accum([(a1+n, a2+np.arange(k0,k0+int(math.sqrt(Qmax/3.5))+3)) for n in range(n0,n0+R)],acc,be)
        accum([(a1+n, a2-np.arange(-k1,-k1+int(math.sqrt(Qmax/3.5))+3)) for n in range(n1,n1-R,-1)],acc,be)
        pcs=[(Fr(1),(n0,k0),((1,0),(0,1))),(Fr(1),(n1,k1),((-1,0),(0,-1)))]
        pred=[complex(v) for v in A012mp(al,be,x,pieces=pcs,walls=[])]
    else:
        # nu = a e2 + b(-7,13), a,b>0 (generic alpha: no edge points since nu1=-7b, a=nu2+13nu1/7)
        bm=math.sqrt(Qmax/3.5)+2; rows=[]
        for n in range(math.floor(-7*bm-a1)-1, math.ceil(-a1)+1):
            nu1=a1+n; b=-nu1/7
            if b<=0: continue
            kmin=math.floor(-13*nu1/7-a2)+1; ks=np.arange(kmin,kmin+int(bm)+3); rows.append((nu1,a2+ks))
            kmax=math.ceil(-13*(-nu1)/7+a2)-1  # negative cone: nu -> -nu ; enumerate -nu with same rule
        accum(rows,acc,be)
        rows=[]
        for n in range(math.floor(-a1)-1, math.ceil(7*bm-a1)+2):
            nu1=a1+n; b=-nu1/7
            if b>=0: continue
            kmax=math.ceil(-13*nu1/7-a2)-1; ks=np.arange(kmax-int(bm)-2,kmax+1); rows.append((nu1,a2+ks))
        accum(rows,acc,be)
        N=2*m; nn,kk=np.meshgrid(np.arange(N),np.arange(N),indexing='ij'); u1=a1+nn; u2=a2+kk; Q=u1*u1+7*u1*u2+3.5*u2*u2
        meanf=np.exp(2j*np.pi*(Q*xf+u1*(2*float(be[0])+7*float(be[1]))+u2*(7*float(be[0])+7*float(be[1])))).mean()
        pred=[meanf*2*(2*L)/math.sqrt(35),None,None]
    X=np.stack([ts**e for e in (-1,-0.5,0,0.5,1,1.5,2)],1); c=np.linalg.lstsq(X,acc,rcond=None)[0]
    errs=[abs(c[i]-pred[i])/max(1,abs(pred[i])) for i in range(3) if pred[i] is not None]
    rw=dict(al=[str(al[0]),str(al[1])],pred=[None if p is None else [p.real,p.imag] for p in pred],meas=[[v.real,v.imag] for v in c[:3]],errs=errs)
    out['rows'].append(rw); print(rw,flush=True)
out['max_err']=max(max(r['errs']) for r in out['rows'])
thr=1e-5 if mode=='R1' else 1e-6
out['verdict']='pass' if out['max_err']<=thr else ('FAIL' if out['max_err']>1e-3 else 'inconclusive')
json.dump(out,open('../data/%s_%s.json'%(mode,str(x).replace('/','-')),'w'),indent=1); print(out['max_err'],out['verdict'])
