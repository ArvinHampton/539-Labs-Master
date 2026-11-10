# order20: RG6' corrected, L_B check B1, Map RG7. PREREG sha b96dce4a...
import sys, math, json, numpy as np, cmath, time
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, phase_ints, Fr
from symbols import FAM, sym_pair, S_rows, L, MU, A, B
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
    """exact-phase Gauss mean of e(xQ(nu)+B(nu,be)) over nu in al+Z^2"""
    x=Fr(x); h,m=x.numerator,x.denominator; D=lcmd(*al,*be)
    a0=[int(Fr(v)*D) for v in al]; b=[int(Fr(v)*D) for v in be]; Ab=(2*b[0]+7*b[1],7*b[0]+7*b[1])
    Mod=2*m*D*D; Pmax=2*m*D
    def ph(n0,n1):
        V0=a0[0]+D*n0; V1=a0[1]+D*n1
        Q2=(2*V0*V0+14*V0*V1+7*V1*V1)%Mod; Bn=(V0*Ab[0]+V1*Ab[1])%Mod
        return (h%Mod*Q2+2*m*Bn)%Mod
    # minimal period dividing Pmax
    cand=sorted(d for d in range(1,Pmax+1) if Pmax%d==0)
    i=np.arange(min(Pmax,64),dtype=np.int64)
    for P in cand:
        if all((ph(i+P*u[0],i*0+3+P*u[1])==ph(i,i*0+3)).all() and (ph(i*0+5+P*u[0],i+P*u[1])==ph(i*0+5,i)).all() for u in ((1,0),(0,1))): break
    n0,n1=np.meshgrid(np.arange(P,dtype=np.int64),np.arange(P,dtype=np.int64),indexing='ij')
    k=ph(n0,n1); return np.exp(2j*np.pi*k/Mod).mean()
e=lambda r: cmath.exp(2j*math.pi*float(Fr(r)%1))
def lam(k,N): return (Fr(k,5*N),Fr(-2*k,35*N))
def ck(al,N): return [sum(B2((Fr(al[1])+j)/N)*e(-k*(Fr(al[1])+j)/N) for j in range(N))/N for k in range(N)]
out={}
Z=np.load('../../order19/data/rg5_arrays.npz'); C,SC=Z['C'],Z['SC']
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS]); nrm=np.linalg.norm
# --- RG6' corrected
GN=np.zeros((216,105),complex); SGN=GN.copy()
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        for X,y in ((GN,x),(SGN,-1/x)):
            N=Nof(al,be,y); i=np.arange(N); V=np.stack(np.meshgrid(i,i,indexing='ij'),-1).reshape(-1,2)
            k0,Mm=phase_ints(al,be,y,V); X[ix,j]=np.exp(2j*np.pi*k0/Mm).sum()
Xx=C[2]-GN/6; SX=SC[2]-SGN/6
Y=xs[:,None]*(Xx@M.T)/math.sqrt(35); kap=np.vdot(Y,SX)/np.vdot(Y,Y); R=nrm(SX-kap*Y)
out['RG6p']=dict(abs=float(R),rel=float(R/nrm(SX)),kappa=[kap.real,kap.imag],
   verdict='PASS (no law)' if (R>=1e-3*nrm(SX) and R>=1e-4) else ('FAIL (law holds)' if R<=1e-9 else 'inconclusive'))
print(out,flush=True)
# --- RG7
A0=np.load('../../order4b/data/A2.npz')['A0']; I=math.log(6+math.sqrt(35))/(2*math.sqrt(35)); G=A0/I
def rk(Mx): s=np.linalg.svd(Mx,compute_uv=False); return int((s/s[0]>1e-9).sum())
r0=rk(G); out['RG7']={'rankG':r0}
for ci,nm in enumerate(['C11','C2a','C2b']):
    out['RG7'][nm]=rk(np.hstack([G,xs[:,None]*SC[ci]]))
out['RG7']['verdict']='PASS' if all(out['RG7'][n]>r0 for n in ['C11','C2a','C2b']) else 'FAIL'
print(out['RG7'],flush=True)
# --- B1 check of L_B
pts=[Fr(1),Fr(1,2),Fr(2),Fr(1,3),Fr(3),Fr(2,3),Fr(3,2)]; comps=[0,17,35,52,70,87,104]
idx={x:XS.index(x) for x in pts}; e1=0; e2=0; t0=time.time(); rows=[]
for x in pts:
    for j in comps:
        al,be=pairs[j]
        N=Nof(al,be,x); c=ck(al,N)
        rhs1=N*N*sum(c[k]*Gmean(al,(be[0]+lam(k,N)[0],be[1]+lam(k,N)[1]),x) for k in range(N))
        d1=abs(rhs1-C[2][idx[x],j]); e1=max(e1,d1)
        y=-1/x; Np=Nof(al,be,y); cp=ck(al,Np); rhs2=0
        for k in range(Np):
            bk=(be[0]+lam(k,Np)[0],be[1]+lam(k,Np)[1])
            s=sum(Gmean((bk[0]+p[0],bk[1]+p[1]),(-al[0],-al[1]),x) for p in MU)
            rhs2+=cp[k]*e(B(al,bk))/(abs(float(x))*math.sqrt(35))*s
        rhs2*=Np*Np; d2=abs(rhs2-SC[2][idx[x],j]); e2=max(e2,d2)
        rows.append(dict(x=str(x),j=j,N=N,Np=Np,d_i=d1,d_ii=d2)); print(rows[-1],round(time.time()-t0),flush=True)
v=lambda d:'PASS' if d<=1e-9 else ('FAIL' if d>=1e-6 else 'inconclusive')
out['B1']=dict(max_i=e1,max_ii=e2,verdict_i=v(e1),verdict_ii=v(e2),rows=rows)
print({k:out[k] for k in ('RG6p','RG7')},out['B1']['max_i'],out['B1']['max_ii'],flush=True)
json.dump(out,open('../data/o20.json','w'),indent=1,default=float)
