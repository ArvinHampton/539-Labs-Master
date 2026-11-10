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
# ---- order42 (helpers above verbatim from order35/order20)
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
e0c=0.0; e0t=0.0; rows=[]
for nn in range(1,9):
    x=Fr(nn); Y=np.zeros(105,complex); S=Y.copy(); D=Y.copy(); SD=Y.copy()
    for j,(al,be) in enumerate(pairs):
        for y,tgtC,tgtD in ((x,Y,D),(-1/x,S,SD)):
            c,N=C2b_direct(al,be,y); cks=ck(al,N); g=Gmean(al,be,y); b2=B2f(al[1])
            e0c=max(e0c,abs(N*N*cks[0]-b2)); e0t=max(e0t,abs(N*N*cks[0]*g-b2*g))
            tgtC[j]=c; tgtD[j]=b2*g
    R=lambda A,SA: SA-kap*float(x)*k*(M@A)
    RC=R(Y,S); RD=R(D,SD); RR=R(Y-D,S-SD)
    rows.append(dict(n=nn,r_C2b=float(n(RC)/n(S)),r_D0=float(n(RD)/n(SD)),r_rem=float(n(RR)/n(S-SD)),normRC=float(n(RC)),normRD=float(n(RD)),rel=float(abs(n(RC)-n(RD))/n(RC)),rem_share=float(n(RR)/n(RC))))
    print(rows[-1],flush=True)
mx=max(r['rel'] for r in rows)
out=dict(E0=dict(max_N2c0_minus_B2=e0c,max_term_err=e0t,verdict='PASS' if (e0c<=1e-12 and e0t<=1e-10) else 'FAIL'),points=rows,RG39=dict(max_rel=mx,verdict='PASS' if mx<=1e-6 else ('FAIL' if mx>=1e-2 else 'inconclusive')))
json.dump(out,open('../data/o42.json','w'),indent=1); print(json.dumps({k_:v for k_,v in out.items() if k_!='points'},indent=1))
