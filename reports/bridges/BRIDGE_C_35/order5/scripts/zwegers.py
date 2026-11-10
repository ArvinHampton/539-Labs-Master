# task (a) test Z + controls + P3: completed indefinite theta series at interior tau vs the fixed 35-component law vector S-matrix
import sys, json, numpy as np, math; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from symbols import FAM, sym_pair, S_rows, L as LL
from scipy.special import erfc
SQ=math.sqrt(math.pi)
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: M[j,kk]+=np.exp(2j*np.pi*e/LL)
from scipy.special import erfcx
def wexp(a,b,expo):
    """(E(a)+E(b))*exp(expo), E(z)=erf(sqrt(pi) z), cancellation- and overflow-safe"""
    A=SQ*a; Bv=SQ*b; sa=np.sign(A); sb=np.sign(Bv)
    opp=(sa==-sb)&(sa!=0)
    with np.errstate(over='ignore',invalid='ignore'):
        same=(sa*(1-erfc(np.abs(A)))+sb*(1-erfc(np.abs(Bv))))*np.exp(np.where(opp,0,expo))
        o=sa*(erfcx(np.abs(Bv))*np.exp(np.where(opp,-Bv*Bv+expo,0))-erfcx(np.abs(A))*np.exp(np.where(opp,-A*A+expo,0)))
    return np.where(opp,o,same)
def series(al,be,tau,kind,Lb,scale=1.0):
    y=tau.imag; n,k=np.meshgrid(np.arange(-Lb,Lb+1),np.arange(-Lb,Lb+1),indexing='ij')
    n1=float(al[0])+n; n2=float(al[1])+k
    Q=n1*n1+7*n1*n2+3.5*n2*n2
    b0,b1=float(be[0]),float(be[1]); Bb=n1*(2*b0+7*b1)+n2*(7*b0+7*b1)
    sy=math.sqrt(y)*scale; expo=-2*np.pi*Q*y
    if kind=='H':  w=0.5*wexp(math.sqrt(10)*n1*sy,(n1+21*n2)*math.sqrt(2/17)*sy,expo)
    elif kind=='O': w=0.5*wexp(math.sqrt(10)*n1*sy,math.sqrt(35)*n2*sy,expo)
    elif kind=='Hhol':
        rho=0.5*(np.sign(n1)+np.sign(n1+21*n2)); w=rho*np.exp(np.where(rho!=0,expo,0))
    assert np.isfinite(w).all()
    return (w*np.exp(2j*np.pi*(Q*tau.real+Bb))).sum()
rng=np.random.default_rng(5); taus=[]
while len(taus)<120:
    t=complex(rng.uniform(-0.45,0.45),rng.uniform(0.55,1.3))
    if 0.8<=abs(t)<=1.25: taus.append(t)
def test(kind,Lb=40,scale=1.0):
    V=np.array([[series(al,be,t,kind,Lb,scale) for al,be in pairs] for t in taus])
    W=np.array([[series(al,be,-1/t,kind,Lb,scale) for al,be in pairs] for t in taus])
    pred=np.array([(t/math.sqrt(35))*(M@V[i]) for i,t in enumerate(taus)])
    nrm=max(1,np.abs(W).max()); r=float(np.abs(W-pred).max()/nrm)
    return r,V,W
res={}
for kind,scale in (('Hhol',1.0),('H',1.25),('O',1.25),('H',1.0),('O',1.0)):
    r,V,W=test(kind,40,scale); res['%s_scale%s'%(kind,scale)]=r; print(kind,scale,r,flush=True)
    if scale==1.0 and kind!='Hhol':
        r2,V2,W2=test(kind,50,scale); res['%s_trunc40vs50'%kind]=float(max(np.abs(V-V2).max(),np.abs(W-W2).max()))
        res['%s_rank'%kind]=int((np.linalg.svd(V,compute_uv=False)/np.linalg.svd(V,compute_uv=False)[0]>1e-9).sum())
        print(res,flush=True)
ctrl=res['Hhol_scale1.0']>1e-4 and res['H_scale1.25']>1e-4
res['controls_fail_as_required']=bool(ctrl)
v=lambda r:'pass' if r<=1e-10 else ('FAIL' if r>1e-4 else 'inconclusive')
res['Z_H']=v(res['H_scale1.0']) if ctrl else 'void'; res['Z_O']=v(res['O_scale1.0']) if ctrl else 'void'
# P3: shadow identity
def shadow(al,be,tau,Lb=40):
    y=tau.imag; n,k=np.meshgrid(np.arange(-Lb,Lb+1),np.arange(-Lb,Lb+1),indexing='ij')
    n1=float(al[0])+n; n2=float(al[1])+k; b0,b1=float(be[0]),float(be[1]); Bb=n1*(2*b0+7*b1)+n2*(7*b0+7*b1)
    e=lambda z,t: np.exp(2j*np.pi*z*t.real)*np.exp(-2*np.pi*z*t.imag)
    tot=0
    for sig,Qc,w,s,Qu in ((1,2.5,-n1,n1+n2,3.5),(-1,8.5,(n1+21*n2)/17,(n1+4*n2)/17,297.5)):
        tot=tot+sig*math.sqrt(Qc)*(w*e(Qu*s*s,tau)*np.exp(2j*np.pi*Bb)*np.conj(e(Qc*w*w,tau))).sum()
    return -1j/(2*math.sqrt(y))*tot
h=1e-5; p3=[]
for t in taus[:4]:
    for j in (0,7,40,52,80,101):
        al,be=pairs[j]; f=lambda z: series(al,be,z,'H',40)
        d=0.5*((f(t+h)-f(t-h))/(2*h)+1j*(f(t+1j*h)-f(t-1j*h))/(2*h))
        s=shadow(al,be,t); p3.append(float(abs(d-s)/max(1e-12,abs(s))))
res['P3_max_relerr']=max(p3); res['P3']='pass' if max(p3)<=1e-6 else 'FAIL'
print(json.dumps(res,indent=1)); json.dump(res,open('../data/zwegers.json','w'),indent=1)
