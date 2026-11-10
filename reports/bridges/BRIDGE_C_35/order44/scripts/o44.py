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
# ---- order44
b=np.array([B2f(al[1]) for al,be in pairs]); Mb=np.diag(b)@M@np.diag(1/b); K=1/math.sqrt(35)
def data(x):
    Y=np.zeros(105,complex); S=Y.copy(); G=Y.copy(); SG=Y.copy()
    for j,(al,be) in enumerate(pairs):
        Y[j],_=C2b_direct(al,be,x); S[j],_=C2b_direct(al,be,-1/x); G[j]=Gmean(al,be,x); SG[j]=Gmean(al,be,-1/x)
    return Y,S,G,SG
def split(x,Y,S,G,SG):
    xf=float(x); D,SD=b*G,b*SG; Rm,SRm=Y-D,S-SD
    a=(Mb@D)/(xf*math.sqrt(35))-kap*xf*K*(M@D); bb=SRm-kap*xf*K*(M@Rm); R=S-kap*xf*K*(M@Y)
    return a,bb,R,D,Rm
def LBii(x):
    y=-1/x; out=np.zeros(105,complex)
    for j,(al,be) in enumerate(pairs):
        Np=Nof(al,be,y); cp=ck(al,Np)
        for kk in range(Np):
            bk=(be[0]+lam(kk,Np)[0],be[1]+lam(kk,Np)[1]); pref=Np*Np*cp[kk]*e(B(al,bk))/(abs(float(x))*math.sqrt(35))
            out[j]+=pref*sum(Gmean((bk[0]+p[0],bk[1]+p[1]),(-al[0],-al[1]),x) for p in MU)
    return out
out={'RG41':[], 'RG42':[]}; w41=0.0
for x in [Fr(2),Fr(3),Fr(4),Fr(1,2),Fr(2,3),Fr(3,2)]:
    Y,S,G,SG=data(x); a,bb,R,D,Rm=split(x,Y,S,G,SG); xf=float(x)
    bp=LBii(x)-(Mb@D)/(xf*math.sqrt(35))-kap*xf*K*(M@Rm); er=float(n(bp-bb)/n(bb)); w41=max(w41,er)
    out['RG41'].append(dict(x=str(x),err=er,q=float(n(Y)/n(D)),LBii_vs_direct=float(np.abs(LBii(x)-S).max()) if False else None)); print('41',x,er,flush=True)
out['RG41_verdict']='PASS' if w41<=1e-10 else ('FAIL' if w41>=1e-6 else 'inconclusive'); out['RG41_max']=w41
w42=0.0
for x,y in [(Fr(5,7),Fr(7,5)),(Fr(4),Fr(1,4)),(Fr(9,2),Fr(2,9)),(Fr(5),Fr(1,5)),(Fr(7,3),Fr(3,7))]:
    cs=[]
    for z in (x,y):
        a,bb,R,_,_=split(z,*data(z)); cs.append(float(n(R)/(n(a)+n(bb))))
    d=abs(cs[0]-cs[1])/cs[0]; w42=max(w42,d); out['RG42'].append(dict(pair=[str(x),str(y)],c=cs,reldiff=d)); print('42',x,y,cs,d,flush=True)
out['RG42_max']=w42; out['RG42_verdict']='PASS' if w42<=1e-8 else ('FAIL' if w42>=1e-4 else 'inconclusive')
json.dump(out,open('../data/o44.json','w'),indent=1); print(json.dumps(out,indent=1))
