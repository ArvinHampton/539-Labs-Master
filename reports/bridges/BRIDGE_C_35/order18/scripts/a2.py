# order18: RG3, RG4, T (A2c law). PREREG sha 593a2016...
import sys, json, math, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, phase_ints, Fr
from symbols import FAM, sym_pair, S_rows, reduce, L
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
def sg(r): return (r>0)-(r<0)
def fr(u): return Fr(u)%1
def B1b(u): u=fr(u); return 0.0 if u==0 else float(u)-0.5
def B2(u): u=float(fr(u)); return u*u-u+1/6
def ph(al,be,x,pts): k,M=phase_ints(al,be,x,np.asarray(pts)); return np.exp(2j*np.pi*k/M)
def period(al,be,x,u):
    N=2*Fr(x).denominator
    for mult in (1,2,5,7,10,14,35,70):
        P=N*mult; j=np.arange(P); pts=j[:,None]*np.array(u)[None,:]
        k1,_=phase_ints(al,be,x,pts); k2,_=phase_ints(al,be,x,pts+P*np.array(u))
        if (k1==k2).all(): return P
    raise RuntimeError
def corner(al,be,x):
    N=math.lcm(period(al,be,x,(1,0)),period(al,be,x,(0,1)))
    i=np.arange(N); V=np.stack(np.meshgrid(i,i,indexing='ij'),-1).reshape(-1,2)
    k1,_=phase_ints(al,be,x,V+np.array([N,0])); k0,M=phase_ints(al,be,x,V); assert (k1==k0).all()
    f=np.exp(2j*np.pi*k0/M)
    a1,a2=Fr(al[0]),Fr(al[1])
    b1=np.array([B1b((a1+n)/N) for n in i]); b2=np.array([B1b((a2+n)/N) for n in i])
    c1=np.array([B2((a1+n)/N) for n in i]); c2=np.array([B2((a2+n)/N) for n in i])
    W=(b1[:,None]*b2[None,:]+0.5*c1[:,None]+1.75*c2[None,:]).reshape(-1)
    return np.sum(f*W)
def Bi(u,v): return u[0]*(2*v[0]+7*v[1])+u[1]*(7*v[0]+7*v[1])
def lines(al,be,x):
    a1,a2=Fr(al[0]),Fr(al[1]); sig=a1+21*a2; R=range(-40,41); tot=0j
    h1=lambda n:Fr(1 if n>=0 else 0)-Fr(1+sg(n+a1),2); h2=lambda k:Fr(1 if k>=0 else 0)-Fr(1+sg(k+a2),2)
    g1=lambda n:sg(n)-sg(n+a1); g3=lambda m:sg(m)-sg(m+sig)
    def line(v0,u,w):   # w: function of b (exact), line v0+b u
        P=period(al,be,x,u); b=np.arange(P); f=ph(al,be,x,np.array(v0)[None,:]+b[:,None]*np.array(u)[None,:])
        fm=ph(al,be,x,np.array(v0)[None,:]-b[:,None]*np.array(u)[None,:])
        nu0=(al[0]+v0[0],al[1]+v0[1]); l=float(Bi(u,nu0)); Qu=Bi(u,u)/2; m=f.mean(); B1v=b/P-0.5
        wp=w(60); wm=w(-60); s=0j
        s+=float(wp)*(-m*l/(2*Qu)-np.sum(f*B1v))+float(wm)*(m*l/(2*Qu)-np.sum(fm*B1v)-f[0])
        for bb in range(-59,60):
            d=w(bb)-(wp if bb>=0 else wm)
            if d: s+=float(d)*ph(al,be,x,[[v0[0]+bb*u[0],v0[1]+bb*u[1]]])[0]
        return s
    for k in R:
        if h2(k): tot+=line((0,k),(1,0),lambda n,k=k:Fr(1+sg(n+a1),2)*h2(k))
    for n in R:
        if h1(n) or g1(n): tot+=line((n,0),(0,1),lambda k,n=n:Fr(1+sg(k+a2),2)*h1(n)-Fr(g1(n),2))
    for mm in R:
        if g3(mm): tot+=line((mm,0),(21,-1),lambda b,mm=mm:-Fr(g3(mm),2))
    for n in R:
        for k in R:
            if h1(n) and h2(k): tot+=float(h1(n)*h2(k))*ph(al,be,x,[[n,k]])[0]
    return tot
P=np.zeros((105,105),complex)
for j,(al,be) in enumerate(pairs):
    k,e=reduce((-al[0],-al[1]),(-be[0],-be[1])); P[j,k]=np.exp(2j*np.pi*e/L)
M=np.zeros((105,105),complex)
for j,dct in enumerate(S_rows()):
    for k,es in dct.items():
        for e in es: M[j,k]+=np.exp(2j*np.pi*e/L)
D=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order4b/data/A2.npz')
LN=np.zeros((216,105),complex); CO=LN.copy(); SLN=LN.copy(); SCO=LN.copy()
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        LN[ix,j]=lines(al,be,x); CO[ix,j]=corner(al,be,x); SLN[ix,j]=lines(al,be,-1/x); SCO[ix,j]=corner(al,be,-1/x)
    if ix%20==0: print('pt',ix,x,flush=True)
np.savez('../data/a2_arrays.npz',LN=LN,CO=CO,SLN=SLN,SCO=SCO)
n=np.linalg.norm; od=lambda A:0.5*(A-A@P.T)
out={}
xs=np.array([float(x) for x in XS])
r0=n(D['S_A0']-(1/(xs*math.sqrt(35)))[:,None]*(D['A0']@M.T))/n(D['S_A0']); out['C0']=dict(r0=r0,verdict='PASS' if r0<=1e-10 else 'VOID')
v=lambda e:'PASS' if e<=1e-9 else ('FAIL' if e>1e-6 else 'inconclusive')
e3=max(n(od(D['A2']-LN))/n(od(D['A2'])), n(od(D['S_A2']-SLN))/n(od(D['S_A2']))); out['RG3']=dict(e=e3,verdict=v(e3))
e4=max(n(D['A2']-LN-CO)/n(D['A2']), n(D['S_A2']-SLN-SCO)/n(D['S_A2'])); out['RG4']=dict(e=e4,verdict=v(e4))
A=D['A2']-LN; S=D['S_A2']-SLN
for w in (-0.5,-1.0,0.0):
    Y=(xs**-w)[:,None]*(A@M.T)/math.sqrt(35); k=np.vdot(Y,S)/np.vdot(Y,Y); r=n(S-k*Y)/n(S)
    out[f'T_w{w}']=dict(r=float(r),kappa=[k.real,k.imag],zero_guard=float(n(S)/n(D['S_A2'])),
        verdict='vacuous' if n(S)/n(D['S_A2'])<1e-10 else ('PASS' if r<=1e-8 else ('FAIL' if r>=1e-3 else 'inconclusive')))
print(out,flush=True); json.dump(out,open('../data/a2.json','w'),indent=1,default=float)
