# order35 RG32. PREREG hashed first. Helpers copied verbatim from order20/scripts/o20.py.
import sys, math, json, numpy as np, cmath, time
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, phase_ints, Fr
from symbols import FAM, sym_pair, S_rows, L, MU, A, B, reduce
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
def B2(u): u=float(Fr(u)%1); return u*u-u+1/6
def period(al,be,x,u):
    N=2*Fr(x).denominator
    for mult in (1,2,5,7,10,14,35,70):
        P=N*mult; j=np.arange(P); pts=j[:,None]*np.array(u)[None,:]
        k1,_=phase_ints(al,be,x,pts); k2,_=phase_ints(al,be,x,pts+P*np.array(u))
        if (k1==k2).all(): return P
def Nof(al,be,x): return math.lcm(period(al,be,x,(1,0)),period(al,be,x,(0,1)))
def lcmd(*fs): return math.lcm(*[Fr(f).denominator for f in fs])
def Gmean(al,be,x):
    x=Fr(x); h,m=x.numerator,x.denominator; D=lcmd(*al,*be)
    a0=[int(Fr(v)*D) for v in al]; b=[int(Fr(v)*D) for v in be]; Ab=(2*b[0]+7*b[1],7*b[0]+7*b[1])
    Mod=2*m*D*D; Pmax=2*m*D
    def ph(n0,n1):
        V0=a0[0]+D*n0; V1=a0[1]+D*n1
        Q2=(2*V0*V0+14*V0*V1+7*V1*V1)%Mod; Bn=(V0*Ab[0]+V1*Ab[1])%Mod
        return (h%Mod*Q2+2*m*Bn)%Mod
    cand=sorted(d for d in range(1,Pmax+1) if Pmax%d==0)
    i=np.arange(min(Pmax,64),dtype=np.int64)
    for P in cand:
        if all((ph(i+P*u[0],i*0+3+P*u[1])==ph(i,i*0+3)).all() and (ph(i*0+5+P*u[0],i+P*u[1])==ph(i*0+5,i)).all() for u in ((1,0),(0,1))): break
    n0,n1=np.meshgrid(np.arange(P,dtype=np.int64),np.arange(P,dtype=np.int64),indexing='ij')
    k=ph(n0,n1); return np.exp(2j*np.pi*k/Mod).mean()
e=lambda r: cmath.exp(2j*math.pi*float(Fr(r)%1))
def lam(k,N): return (Fr(k,5*N),Fr(-2*k,35*N))
def ck(al,N): return [sum(B2((Fr(al[1])+j)/N)*e(-k*(Fr(al[1])+j)/N) for j in range(N))/N for k in range(N)]
def inside(a,b):
    try: reduce(a,b); return True
    except Exception: return False
Z=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order19/data/rg5_arrays.npz'); C,SC=Z['C'],Z['SC']
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
pts=[Fr(1),Fr(1,2),Fr(2),Fr(1,3),Fr(3),Fr(2,3),Fr(3,2)]; idx=[XS.index(x) for x in pts]
Sin=np.zeros((7,105),complex); Sout=Sin.copy(); Sk0=Sin.copy(); nin=0; nout=0; t0=time.time()
for a,x in enumerate(pts):
    y=-1/x
    for j,(al,be) in enumerate(pairs):
        Np=Nof(al,be,y); cp=ck(al,Np)
        for k in range(Np):
            bk=(be[0]+lam(k,Np)[0],be[1]+lam(k,Np)[1]); pref=Np*Np*cp[k]*e(B(al,bk))/(abs(float(x))*math.sqrt(35))
            for p in MU:
                ch=(bk[0]+p[0],bk[1]+p[1]); t=pref*Gmean(ch,(-al[0],-al[1]),x)
                if inside(ch,(-al[0],-al[1])): Sin[a,j]+=t; nin+=1; Sk0[a,j]+=t if k==0 else 0
                else: Sout[a,j]+=t; nout+=1
    print('x',x,round(time.time()-t0),flush=True)
n=np.linalg.norm; S=SC[2][idx]; xs=np.array([float(x) for x in pts])
X=xs[:,None]*(C[2][idx]@M.T)/math.sqrt(35)
def perp(V): Xv=X.ravel(); v=V.ravel(); return v-Xv*np.vdot(Xv,v)/np.vdot(Xv,Xv)
out={}
out['D0']=float(np.abs(Sin+Sout-S).max()); out['n_terms_in']=nin; out['n_terms_out']=nout
rm=float(n(perp(S))/n(S)); rl=float(n(perp(Sout))/n(S))
out['r_meas_P7']=rm; out['r_leak']=rl; out['rel_diff']=abs(rl-rm)/rm
out['H1_inside_perp_rel']=float(n(perp(Sin))/n(Sin)); out['outside_share']=float(n(Sout)/n(S)); out['inside_k0_share']=float(n(Sk0)/n(Sin))
kap=np.vdot(X.ravel(),S.ravel())/np.vdot(X.ravel(),X.ravel()); out['kappa']=[kap.real,kap.imag]
out['RG32']='PASS' if out['rel_diff']<=1e-6 else ('FAIL' if out['rel_diff']>=1e-2 else 'inconclusive')
out['H1']='PASS' if out['H1_inside_perp_rel']<=1e-10 else 'FAIL'
np.savez('../data/o35_split.npz',Sin=Sin,Sout=Sout,Sk0=Sk0,X=X,S=S)
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o35.json','w'),indent=1)
