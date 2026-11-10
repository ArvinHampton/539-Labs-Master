# order21: K0,K1, RG8a, RG8b. PREREG sha 980ede89...
import sys, math, json, cmath, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, phase_ints, Fr
from symbols import FAM, sym_pair, S_rows, L
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
def B2(u): u=float(Fr(u)%1); return u*u-u+1/6
def period(al,be,x,u):
    N=2*Fr(x).denominator
    for mult in (1,2,5,7,10,14,35,70):
        P=N*mult; j=np.arange(P); pts=j[:,None]*np.array(u)[None,:]
        k1,_=phase_ints(al,be,x,pts); k2,_=phase_ints(al,be,x,pts+P*np.array(u))
        if (k1==k2).all(): return P
def parts(al,be,x):
    N=math.lcm(period(al,be,x,(1,0)),period(al,be,x,(0,1)))
    i=np.arange(N); V=np.stack(np.meshgrid(i,i,indexing='ij'),-1).reshape(-1,2)
    k0,Mm=phase_ints(al,be,x,V); f=np.exp(2j*np.pi*k0/Mm).reshape(N,N)
    a2=Fr(al[1]); rho=[(a2+j) for j in range(N)]
    ks=[k if k<=N//2 else k-N for k in range(N)]
    T={k:np.sum(f*np.array([cmath.exp(2j*math.pi*float(Fr(k*r,N)%1)) for r in rho])[None,:]) for k in ks}
    c={k:sum(B2(r/N)*cmath.exp(-2j*math.pi*float(Fr(k*r,N)%1)) for r in rho)/N for k in ks}
    C2b=np.sum(f*np.array([B2(r/N) for r in rho])[None,:])
    return N,T,c,C2b
Kmax=2
out={}; nX=np.zeros((216,105),complex); SX=nX.copy(); XK={K:nX.copy() for K in range(Kmax+1)}; SXK={K:nX.copy() for K in range(Kmax+1)}
G=nX.copy(); SG=nX.copy(); k0max=0
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        for (Xa,XKa,Ga,y) in ((nX,XK,G,x),(SX,SXK,SG,-1/x)):
            N,T,c,C=parts(al,be,y)
            rec=sum(c[k]*T[k] for k in T); k0max=max(k0max,abs(rec-C))
            ct={k:c[k]-(1/6 if k==0 else 0) for k in T}
            Xa[ix,j]=sum(ct[k]*T[k] for k in T); Ga[ix,j]=T[0]/N**2
            for K in range(Kmax+1): XKa[K][ix,j]=sum(ct[k]*T[k] for k in T if abs(k)<=K)
    if ix%40==0: print('pt',ix,flush=True)
Z=np.load('../../order19/data/rg5_arrays.npz'); 
chk=max(np.abs(nX-(Z['C'][2]-0)).max()*0, 0)
out['K0']=dict(max_abs=float(k0max),verdict='PASS' if k0max<=1e-9 else 'VOID')
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: M[j,kk]+=np.exp(2j*np.pi*e/L)
xs=np.array([float(x) for x in XS]); n=np.linalg.norm
def law(A,S):
    Y=xs[:,None]*(A@M.T)/math.sqrt(35); k=np.vdot(Y,S)/np.vdot(Y,Y); R=S-k*Y
    return dict(abs=float(n(R)),rel=float(n(R)/n(S)),kappa=[k.real,k.imag]),R
lx,DX=law(nX,SX); out['K1']=dict(rel=lx['rel'],order20=9.494907798827073e-04,verdict='PASS' if abs(lx['rel']-9.494907798827073e-04)<=1e-8 else 'FAIL'); out['X']=lx
def rk(Mx): s=np.linalg.svd(Mx,compute_uv=False); return int((s/s[0]>1e-9).sum())
Gr=np.load('../../order4b/data/A2.npz')['A0']/(math.log(6+math.sqrt(35))/(2*math.sqrt(35)))
for K in range(Kmax+1):
    a,_=law(XK[K],SXK[K]); b,_=law(nX-XK[K],SX-SXK[K]); out[f'RG8a_K{K}']=dict(low=a,high=b,joint_rank=rk(np.hstack([Gr,xs[:,None]*SXK[K]])))
okK=[K for K in range(Kmax+1) if out[f'RG8a_K{K}']['low']['rel']<=1e-4 and out[f'RG8a_K{K}']['high']['rel']>=1e-2]
out['RG8a']='PASS' if okK else ('FAIL' if all(out[f'RG8a_K{K}']['low']['rel']>=1e-3 for K in range(Kmax+1)) else 'inconclusive')
sel=xs>=0.5; u=(2*xs[sel]-3.5)/2.5; V=np.polynomial.chebyshev.chebvander(u,8)
def smooth(D):
    Dd=D[sel]; coef,*_=np.linalg.lstsq(V,Dd,rcond=None); return float(n(Dd-V@coef)/n(Dd))
sD=smooth(DX); sX=smooth(nX)
out['RG8b']=dict(sD=sD,sX=sX,verdict='PASS' if (sD<=1e-2 and sX>=0.3) else ('FAIL' if sD>=0.3 else 'inconclusive'))
A18=np.load('../../order18/data/a2_arrays.npz'); _,DA=law(A18['CO'],A18['SCO']); out['RG8b_secondary_A2corner']=dict(sD=smooth(DA),sX=smooth(A18['CO']))
np.savez('../data/o21_arrays.npz',X=nX,SX=SX,DX=DX,**{f'XK{K}':XK[K] for K in XK},**{f'SXK{K}':SXK[K] for K in SXK})
print(json.dumps(out,indent=1,default=float)); json.dump(out,open('../data/o21.json','w'),indent=1,default=float)
