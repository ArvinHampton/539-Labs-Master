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
def B2f(u): u=float(Fr(u)%1); return u*u-u+1/6
def C2b_direct(al,be,x):
    N=Nof(al,be,x); i=np.arange(N); V=np.stack(np.meshgrid(i,i,indexing='ij'),-1).reshape(-1,2)
    k0,Mm=phase_ints(al,be,x,V); f=np.exp(2j*np.pi*k0/Mm).reshape(N,N); c2=np.array([B2((Fr(al[1])+t)/N) for t in i])
    return np.einsum('ij,j->',f,c2), N
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
kap=complex(1.0000146975519928,-0.00033624064241876014); n=np.linalg.norm; k=1/math.sqrt(35)
# ---- order43
pts=[Fr(v) for v in (1,2,3,4,5,6,7,8)]+[Fr(1,2),Fr(1,3),Fr(2,3),Fr(3,2)]
b=np.array([B2f(al[1]) for al,be in pairs]); Mb=np.diag(b)@M@np.diag(1/b)
eLD=0.0; worst=0.0; rows=[]
for x in pts:
    xf=float(x); Y=np.zeros(105,complex); S=Y.copy(); G=Y.copy(); SG=Y.copy()
    for j,(al,be) in enumerate(pairs):
        Y[j],_=C2b_direct(al,be,x); S[j],_=C2b_direct(al,be,-1/x); G[j]=Gmean(al,be,x); SG[j]=Gmean(al,be,-1/x)
    D,SD=b*G,b*SG; Rm,SRm=Y-D,S-SD
    eLD=max(eLD,float(np.abs(SD-(Mb@D)/(xf*math.sqrt(35))).max()))
    R=S-kap*xf*k*(M@Y)
    a=(Mb@D)/(xf*math.sqrt(35))-kap*xf*k*(M@D); bb=SRm-kap*xf*k*(M@Rm); Rp=a+bb
    e=float(n(R-Rp)/n(R)); worst=max(worst,e)
    rows.append(dict(x=str(x),r=float(n(R)/n(S)),normR=float(n(R)),norm_a=float(n(a)),norm_b=float(n(bb)),cancel=float(n(R)/(n(a)+n(bb))),err=e)); print(rows[-1],flush=True)
out=dict(min_abs_b=float(np.abs(b).min()),LD0=dict(err=eLD,verdict='PASS' if eLD<=1e-12 else ('FAIL' if eLD>=1e-9 else 'inconclusive')),RG40=dict(max_err=worst,verdict='PASS' if worst<=1e-10 else ('FAIL' if worst>=1e-6 else 'inconclusive')),points=rows)
json.dump(out,open('../data/o43.json','w'),indent=1); print(json.dumps({k_:v for k_,v in out.items() if k_!='points'},indent=1))
