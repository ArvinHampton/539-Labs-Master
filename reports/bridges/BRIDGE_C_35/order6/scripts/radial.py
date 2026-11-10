# order6 R1: radial expansion of completed full series S-hat_nu vs uncompleted S_nu (control), one x per process
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from fractions import Fraction as Fr
from symbols import FAM, sym_pair
from lib6 import weight, grid
x=Fr(sys.argv[1]); m=x.denominator; xf=float(x)
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]; J=[0,7,40,52,80,101]
ts=[2.0**-j*0.02/(2*m)**2 for j in range(6)]
out={'x':str(x),'ts':ts,'rows':[]}
for j in J:
    al,be=pairs[j]; b0,b1=float(be[0]),float(be[1])
    acc={k:np.zeros(6,complex) for k in ('full','fullhol')}
    for ti,t in enumerate(ts):
        y=t/(2*math.pi); r=int(math.sqrt(150/t))+5
        for n0 in range(-r,r+1,64):
            n,k=np.meshgrid(np.arange(n0,min(n0+64,r+1)),np.arange(-r,r+1),indexing='ij')
            n1,n2=grid(al,n,k); Q=n1*n1+7*n1*n2+3.5*n2*n2
            ph=np.exp(2j*np.pi*(Q*xf+n1*(2*b0+7*b1)+n2*(7*b0+7*b1)))
            for kind in acc:
                w=weight(kind,n1,n2,y,-t*Q); acc[kind][ti]+=(w*ph).sum()
    row={'j':j}
    T=np.array(ts); X=np.stack([np.ones(6),np.sqrt(T),T],1)
    for kind in acc:
        c=np.linalg.lstsq(X,T*acc[kind],rcond=None)[0]; row[kind]=[[v.real,v.imag] for v in c]
    out['rows'].append(row); print(j,row,flush=True)
c1max=max(math.hypot(*r['full'][1])/max(1,math.hypot(*r['full'][0])) for r in out['rows'])
c2max=max(math.hypot(*r['full'][2])/max(1,math.hypot(*r['full'][0])) for r in out['rows'])
ctl=max(math.hypot(*r['fullhol'][1]) for r in out['rows'])
out.update(c1max=c1max,c2max=c2max,control_c1max=ctl,R1='pass' if max(c1max,c2max)<=1e-6 else 'FAIL')
json.dump(out,open('../data/radial_%s.json'%str(x).replace('/','-'),'w'),indent=1); print(json.dumps({k:out[k] for k in ('c1max','c2max','control_c1max','R1')}))
