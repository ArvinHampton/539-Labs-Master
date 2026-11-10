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
# ---- order36 main (helpers above copied verbatim from order35/order20)
from scipy.stats import spearmanr
Z=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order19/data/rg5_arrays.npz'); C,SC=Z['C'],Z['SC']
A0=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order4b/data/A2.npz')['A0']; I=math.log(6+math.sqrt(35))/(2*math.sqrt(35)); G=A0/I
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
n=np.linalg.norm
def split(pts):
    Sin=np.zeros((len(pts),105),complex); Sout=Sin.copy(); t0=time.time()
    for a,x in enumerate(pts):
        y=-1/x
        for j,(al,be) in enumerate(pairs):
            Np=Nof(al,be,y); cp=ck(al,Np)
            for k in range(Np):
                bk=(be[0]+lam(k,Np)[0],be[1]+lam(k,Np)[1]); pref=Np*Np*cp[k]*e(B(al,bk))/(abs(float(x))*math.sqrt(35))
                for p in MU:
                    ch=(bk[0]+p[0],bk[1]+p[1]); t=pref*Gmean(ch,(-al[0],-al[1]),x)
                    if inside(ch,(-al[0],-al[1])): Sin[a,j]+=t
                    else: Sout[a,j]+=t
        print('x',x,round(time.time()-t0),flush=True)
    return Sin,Sout
def analyse(pts,Sin,Sout,tag):
    idx=[XS.index(x) for x in pts]; S=SC[2][idx]; xs=np.array([float(x) for x in pts]); X=xs[:,None]*(C[2][idx]@M.T)/math.sqrt(35)
    Gs=G[idx]; U,s,_=np.linalg.svd(Gs,full_matrices=False); rk=int((s/s[0]>1e-9).sum()); U=U[:,:rk]
    perp=lambda V: V-U@(U.conj().T@V)
    kap=np.vdot(X.ravel(),S.ravel())/np.vdot(X.ravel(),X.ravel()); Rr=S-kap*X
    rm=float(n(Rr)/n(S)); rp=float(n(perp(Sout))/n(S))
    pp_r=[float(n(Rr[i])/n(S[i])) for i in range(len(pts))]; pp_l=[float(n(perp(Sout)[i])/n(S[i])) for i in range(len(pts))]
    o=dict(npts=len(pts),rank_G=rk,D0=float(np.abs(Sin+Sout-S).max()),kappa=[kap.real,kap.imag],r_meas=rm,r_pred=rp,rel_diff=abs(rp-rm)/rm,
      perp_S=float(n(perp(S))/n(S)),perp_Sin=float(n(perp(Sin))/n(S)),perp_X=float(n(perp(X))/n(X)),
      per_point=[dict(x=str(x),r=a,leftover=b) for x,a,b in zip(pts,pp_r,pp_l)],
      spearman_r_vs_leftover=float(spearmanr(pp_r,pp_l)[0]) if len(pts)>2 else None)
    np.savez(f'../data/o36_{tag}.npz',Sin=Sin,Sout=Sout,S=S,X=X); return o
out={}
P7=[Fr(1),Fr(1,2),Fr(2),Fr(1,3),Fr(3),Fr(2,3),Fr(3,2)]
o35=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order35/data/o35_split.npz')
out['P7_trivial_control']=analyse(P7,o35['Sin'],o35['Sout'],'P7')
G48=sorted(XS,key=lambda x:(abs(Fr(x).numerator)*Fr(x).denominator,abs(Fr(x).numerator)))[:48]
Sin,Sout=split(G48); o=analyse(G48,Sin,Sout,'G48')
o['verdict']='VOID' if o['rank_G']!=36 else ('PASS' if o['rel_diff']<=1e-6 else ('FAIL' if o['rel_diff']>=1e-2 else 'inconclusive'))
out['RG33']=o
json.dump(out,open('../data/o36.json','w'),indent=1)
print(json.dumps({k:{kk:vv for kk,vv in v.items() if kk!='per_point'} for k,v in out.items()},indent=1))
